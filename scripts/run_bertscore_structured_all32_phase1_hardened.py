#!/usr/bin/env python3
"""Run BERTScore for the Phase-1-hardened structured-prompt all-32 dataset."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
DEFAULT_REFERENCE_DIR = Path("/Users/upigdir/Desktop/Pipeline/Scenarios to Run")
SUMMARY_DIR = ROOT / "outputs" / "structured_prompt_all32_summary_phase1_hardened"
OUTPUT_DIR = ROOT / "outputs" / "bertscore_structured_all32_phase1_hardened_v1"
BASELINE_DIR = ROOT / "outputs" / "bertscore_full_usable_v1"

RUN_NAME = "structured_prompt_all32_phase1_hardened_v1"
REFERENCE_SOURCE = "worked_solutions_batch1.md through worked_solutions_batch7.md"
CANDIDATE_SOURCE = "structured_prompt_pilot_v2-v5 saved raw model responses"
LANG = "en"

EXPECTED_CLEAN_ROWS = 252
EXPECTED_PASS = 117
EXPECTED_FAIL = 135
EXPECTED_SCENARIOS = 32
EXPECTED_BATCHES = ("V2", "V3", "V4", "V5")

SCENARIO_HEADING_RE = re.compile(r"^##\s+([A-Z]{2,4}_[A-Z0-9]+_[0-9]{3})\b.*$", re.MULTILINE)
SUBHEADING_RE = re.compile(r"^\*\*(.+?)\*\*\s*$")
USEFUL_HEADING_RE = re.compile(r"(derivation|reasoning checkpoint|checkpoints|reasoning|solution)", re.I)
STOP_HEADING_RE = re.compile(r"(final answer|wrong-answer|wrong answer|fingerprint)", re.I)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def iter_reference_files(reference_dir: Path) -> list[Path]:
    return sorted(reference_dir.glob("worked_solutions_batch*.md"))


def split_scenario_sections(markdown: str) -> dict[str, str]:
    matches = list(SCENARIO_HEADING_RE.finditer(markdown))
    sections: dict[str, str] = {}
    for idx, match in enumerate(matches):
        scenario_id = match.group(1)
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(markdown)
        sections[scenario_id] = markdown[start:end].strip()
    return sections


def extract_reference_text(section: str) -> str:
    lines = section.splitlines()
    selected: list[str] = []
    capture = False
    for line in lines:
        heading_match = SUBHEADING_RE.match(line.strip())
        if heading_match:
            heading = heading_match.group(1)
            if STOP_HEADING_RE.search(heading):
                capture = False
                continue
            capture = bool(USEFUL_HEADING_RE.search(heading))
            if capture:
                selected.append(line)
            continue
        if capture:
            selected.append(line)
    text = "\n".join(selected).strip()
    return text if text else section.strip()


def parse_references(reference_dir: Path) -> tuple[dict[str, str], list[Path]]:
    files = iter_reference_files(reference_dir)
    if len(files) != 7:
        raise SystemExit(f"Expected 7 worked_solutions_batch*.md files, found {len(files)} in {reference_dir}")
    references: dict[str, str] = {}
    for path in files:
        for scenario_id, section in split_scenario_sections(path.read_text(encoding="utf-8")).items():
            references[scenario_id] = extract_reference_text(section)
    if len(references) != EXPECTED_SCENARIOS:
        raise SystemExit(f"Expected {EXPECTED_SCENARIOS} scenario references, found {len(references)}")
    return references, files


def connect_readonly(db_path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def load_categories(db_path: Path) -> dict[str, str]:
    con = connect_readonly(db_path)
    try:
        return {
            row["scenario_id"]: row["category"] or ""
            for row in con.execute("SELECT scenario_id, category FROM scenarios ORDER BY scenario_id")
        }
    finally:
        con.close()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_batch_rows(batch_num: int) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    batch_dir = ROOT / "outputs" / f"structured_prompt_pilot_v{batch_num}"
    autograde_path = batch_dir / "autograde_no_bert_v1" / f"structured_prompt_v{batch_num}_clean_autograde.json"
    runs_path = batch_dir / f"structured_prompt_pilot_v{batch_num}_runs.json"
    if not autograde_path.exists():
        raise SystemExit(f"Missing autograde file: {autograde_path}")
    if not runs_path.exists():
        raise SystemExit(f"Missing runs file: {runs_path}")
    runs = {str(row["run_id"]): row for row in load_json(runs_path)}
    return load_json(autograde_path), runs


def load_structured_rows(categories: dict[str, str], references: dict[str, str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for batch_num in (2, 3, 4, 5):
        batch = f"V{batch_num}"
        clean_rows, runs = load_batch_rows(batch_num)
        for clean in clean_rows:
            if clean.get("review_status") != "CLEAN":
                raise SystemExit(f"Unexpected non-CLEAN row in clean autograde: {batch} {clean}")
            if clean.get("extraction_status") != "OK":
                raise SystemExit(f"Unexpected non-OK extraction row in clean autograde: {batch} {clean}")
            run_id = str(clean["output_path_or_run_id"])
            run = runs.get(run_id)
            if not run:
                raise SystemExit(f"Missing raw run for {batch} run_id={run_id}")
            scenario_id = clean["scenario_id"]
            if scenario_id not in references:
                raise SystemExit(f"Missing reference for {scenario_id}")
            response = run.get("response") or ""
            rows.append(
                {
                    "batch": batch,
                    "scenario_id": scenario_id,
                    "category": categories.get(scenario_id, ""),
                    "model_name": clean.get("model_name") or run.get("model_label") or "",
                    "deterministic_grade": clean.get("deterministic_grade") or "",
                    "extraction_status": clean.get("extraction_status") or "",
                    "helper_status": clean.get("raw_helper_status") or "",
                    "candidate_text": response,
                    "source_run_id": run_id,
                    "reference_text": references[scenario_id],
                    "reference_source": REFERENCE_SOURCE,
                    "candidate_source": CANDIDATE_SOURCE,
                }
            )
    return rows


def validate_inputs(rows: list[dict[str, Any]], references: dict[str, str]) -> None:
    if len(rows) != EXPECTED_CLEAN_ROWS:
        raise SystemExit(f"Expected {EXPECTED_CLEAN_ROWS} CLEAN rows, found {len(rows)}")
    batches = Counter(row["batch"] for row in rows)
    missing_batches = [batch for batch in EXPECTED_BATCHES if batches[batch] == 0]
    if missing_batches:
        raise SystemExit(f"Missing batches: {', '.join(missing_batches)}")
    scenario_count = len({row["scenario_id"] for row in rows})
    if scenario_count != EXPECTED_SCENARIOS:
        raise SystemExit(f"Expected {EXPECTED_SCENARIOS} scenarios, found {scenario_count}")
    grades = Counter(row["deterministic_grade"] for row in rows)
    if grades["PASS"] != EXPECTED_PASS or grades["FAIL"] != EXPECTED_FAIL:
        raise SystemExit(f"Expected PASS={EXPECTED_PASS}, FAIL={EXPECTED_FAIL}; found {dict(grades)}")
    extraction = Counter(row["extraction_status"] for row in rows)
    if dict(extraction) != {"OK": EXPECTED_CLEAN_ROWS}:
        raise SystemExit(f"Expected only OK extraction rows; found {dict(extraction)}")
    missing_refs = sorted(set(row["scenario_id"] for row in rows) - set(references))
    if missing_refs:
        raise SystemExit(f"Missing references: {', '.join(missing_refs)}")


def require_bertscore():
    try:
        from bert_score import score
    except ImportError:
        raise SystemExit("Missing dependency: bert-score")
    return score


def unpack_bertscore_result(result):
    if len(result) == 3:
        precision, recall, f1 = result
        return precision, recall, f1, "unknown"
    if len(result) == 4:
        precision, recall, f1, model_hash = result
        return precision, recall, f1, model_hash
    raise RuntimeError(f"Unexpected bert_score.score return length: {len(result)}")


def compute_bertscore_batches(
    candidates: list[str],
    references: list[str],
    batch_size: int,
) -> tuple[list[float], list[float], list[float], str, bool, str]:
    score = require_bertscore()
    all_precision: list[float] = []
    all_recall: list[float] = []
    all_f1: list[float] = []
    model_hash = "unknown"
    notes = ""
    rescale = True
    for start in range(0, len(candidates), batch_size):
        end = min(start + batch_size, len(candidates))
        batch_candidates = candidates[start:end]
        batch_references = references[start:end]
        try:
            precision, recall, f1, batch_model_hash = unpack_bertscore_result(
                score(
                    batch_candidates,
                    batch_references,
                    lang=LANG,
                    rescale_with_baseline=True,
                    verbose=False,
                )
            )
        except Exception as exc:
            if start != 0:
                raise
            notes = f"rescale_with_baseline=True failed; retried without baseline: {type(exc).__name__}: {exc}"
            rescale = False
            precision, recall, f1, batch_model_hash = unpack_bertscore_result(
                score(
                    batch_candidates,
                    batch_references,
                    lang=LANG,
                    rescale_with_baseline=False,
                    verbose=False,
                )
            )
        if batch_model_hash != "unknown":
            model_hash = str(batch_model_hash)
        all_precision.extend(float(x) for x in precision.tolist())
        all_recall.extend(float(x) for x in recall.tolist())
        all_f1.extend(float(x) for x in f1.tolist())
        print(f"processed {end}/{len(candidates)}")
    return all_precision, all_recall, all_f1, model_hash, rescale, notes


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def stats_for(rows: list[dict[str, Any]]) -> dict[str, Any]:
    p = [float(row["bert_precision"]) for row in rows]
    r = [float(row["bert_recall"]) for row in rows]
    f = [float(row["bert_f1"]) for row in rows]
    grades = Counter(row["deterministic_grade"] for row in rows)
    return {
        "n_rows": len(rows),
        "pass": grades.get("PASS", 0),
        "fail": grades.get("FAIL", 0),
        "pass_rate": grades.get("PASS", 0) / len(rows) if rows else 0.0,
        "mean_precision": mean(p),
        "median_precision": median(p),
        "mean_recall": mean(r),
        "median_recall": median(r),
        "mean_f1": mean(f),
        "median_f1": median(f),
        "min_f1": min(f),
        "max_f1": max(f),
        "mean_candidate_text_length_chars": mean(int(row["candidate_text_length_chars"]) for row in rows),
        "mean_reference_text_length_chars": mean(int(row["reference_text_length_chars"]) for row in rows),
    }


def summarize(rows: list[dict[str, Any]], keys: tuple[str, ...]) -> list[dict[str, Any]]:
    grouped: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[tuple(row[key] for key in keys)].append(row)
    summary: list[dict[str, Any]] = []
    for key_values, group_rows in sorted(grouped.items()):
        item = {keys[idx]: key_values[idx] for idx in range(len(keys))}
        item.update(stats_for(group_rows))
        summary.append(item)
    return summary


def load_baseline_summary() -> dict[str, Any] | None:
    path = BASELINE_DIR / "bertscore_full_usable_results.csv"
    if not path.exists():
        return None
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return None
    f1 = [float(row["bertscore_f1"]) for row in rows]
    return {
        "run_name": "pre_structured_prompt_usable_full_v1",
        "n_rows": len(rows),
        "mean_f1": mean(f1),
        "median_f1": median(f1),
        "min_f1": min(f1),
        "max_f1": max(f1),
    }


def write_baseline_comparison(path: Path, structured_stats: dict[str, Any], baseline: dict[str, Any] | None) -> None:
    rows = [
        {
            "dataset": RUN_NAME,
            "n_rows": structured_stats["n_rows"],
            "mean_f1": structured_stats["mean_f1"],
            "median_f1": structured_stats["median_f1"],
            "min_f1": structured_stats["min_f1"],
            "max_f1": structured_stats["max_f1"],
            "comparison_note": "structured CLEAN rows only; no row-level alignment with original baseline",
        }
    ]
    if baseline:
        rows.append(
            {
                "dataset": baseline["run_name"],
                "n_rows": baseline["n_rows"],
                "mean_f1": baseline["mean_f1"],
                "median_f1": baseline["median_f1"],
                "min_f1": baseline["min_f1"],
                "max_f1": baseline["max_f1"],
                "comparison_note": "previous usable official baseline",
            }
        )
    write_csv(path, rows)


def write_report(
    path: Path,
    rows: list[dict[str, Any]],
    by_batch: list[dict[str, Any]],
    by_scenario: list[dict[str, Any]],
    by_model: list[dict[str, Any]],
    by_grade: list[dict[str, Any]],
    manifest: dict[str, Any],
    baseline: dict[str, Any] | None,
) -> None:
    overall = stats_for(rows)
    lowest = sorted(by_scenario, key=lambda row: float(row["mean_f1"]))[:5]
    highest = sorted(by_scenario, key=lambda row: float(row["mean_f1"]), reverse=True)[:5]
    lines = [
        "# BERTScore Structured All-32 Phase-1-Hardened Report",
        "",
        "## Scope",
        "",
        f"- Run name: `{RUN_NAME}`",
        "- Source: saved structured-prompt V2-V5 outputs only",
        "- Rows scored: CLEAN rows only",
        f"- Reference source: {REFERENCE_SOURCE}",
        f"- Rescale with baseline: {manifest['rescale_with_baseline']}",
        f"- BERTScore model hash: {manifest['bertscore_model']}",
        "",
        "## Validation",
        "",
        f"- CLEAN rows scored: {len(rows)}",
        f"- REVIEW rows scored: 0",
        f"- Scenarios represented: {len({row['scenario_id'] for row in rows})}",
        f"- Batches represented: {', '.join(sorted({row['batch'] for row in rows}))}",
        f"- Deterministic PASS/FAIL: PASS={manifest['deterministic_grade_distribution'].get('PASS', 0)}, FAIL={manifest['deterministic_grade_distribution'].get('FAIL', 0)}",
        "- learning.db modified: false",
        "- raw outputs modified: false",
        "- model/LLM API calls made: false",
        "",
        "## Overall",
        "",
        f"- Mean F1: {overall['mean_f1']:.6f}",
        f"- Median F1: {overall['median_f1']:.6f}",
        f"- Min F1: {overall['min_f1']:.6f}",
        f"- Max F1: {overall['max_f1']:.6f}",
        "",
        "## By Deterministic Grade",
        "",
        "| grade | n_rows | mean_f1 | median_f1 | min_f1 | max_f1 |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in by_grade:
        lines.append(
            f"| {row['deterministic_grade']} | {row['n_rows']} | {float(row['mean_f1']):.6f} | "
            f"{float(row['median_f1']):.6f} | {float(row['min_f1']):.6f} | {float(row['max_f1']):.6f} |"
        )
    lines.extend(["", "## By Batch", "", "| batch | n_rows | PASS | FAIL | mean_f1 | median_f1 |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    for row in by_batch:
        lines.append(
            f"| {row['batch']} | {row['n_rows']} | {row['pass']} | {row['fail']} | "
            f"{float(row['mean_f1']):.6f} | {float(row['median_f1']):.6f} |"
        )
    lines.extend(["", "## Lowest Scenario Mean F1", "", "| scenario_id | n_rows | mean_f1 |", "| --- | ---: | ---: |"])
    for row in lowest:
        lines.append(f"| {row['scenario_id']} | {row['n_rows']} | {float(row['mean_f1']):.6f} |")
    lines.extend(["", "## Highest Scenario Mean F1", "", "| scenario_id | n_rows | mean_f1 |", "| --- | ---: | ---: |"])
    for row in highest:
        lines.append(f"| {row['scenario_id']} | {row['n_rows']} | {float(row['mean_f1']):.6f} |")
    if baseline:
        delta = overall["mean_f1"] - baseline["mean_f1"]
        lines.extend(
            [
                "",
                "## Baseline Context",
                "",
                f"- Previous baseline rows: {baseline['n_rows']}",
                f"- Previous baseline mean F1: {baseline['mean_f1']:.6f}",
                f"- Structured mean F1 minus previous baseline mean F1: {delta:.6f}",
                "- Comparison is aggregate only; no unsafe row-level alignment was performed.",
            ]
        )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- `bertscore_structured_all32_phase1_hardened.csv`",
            "- `bertscore_structured_all32_phase1_hardened.json`",
            "- `bertscore_structured_all32_phase1_hardened_by_batch.csv`",
            "- `bertscore_structured_all32_phase1_hardened_by_scenario.csv`",
            "- `bertscore_structured_all32_phase1_hardened_by_model.csv`",
            "- `bertscore_structured_all32_phase1_hardened_by_grade.csv`",
            "- `bertscore_structured_vs_original_baseline_summary.csv`",
            "- `manifest.json`",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    parser.add_argument("--reference-dir", default=str(DEFAULT_REFERENCE_DIR))
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR))
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    if output_dir.exists() and any(output_dir.iterdir()) and not args.force:
        raise SystemExit(f"Output directory already exists and is not empty: {output_dir}; use --force to replace files there")
    output_dir.mkdir(parents=True, exist_ok=True)

    references, reference_files = parse_references(Path(args.reference_dir))
    categories = load_categories(Path(args.db))
    rows = load_structured_rows(categories, references)
    validate_inputs(rows, references)

    candidates = [row["candidate_text"] for row in rows]
    reference_texts = [row["reference_text"] for row in rows]
    precision, recall, f1, model_hash, rescale, notes = compute_bertscore_batches(candidates, reference_texts, args.batch_size)

    output_rows: list[dict[str, Any]] = []
    for idx, row in enumerate(rows):
        output_rows.append(
            {
                "batch": row["batch"],
                "scenario_id": row["scenario_id"],
                "category": row["category"],
                "model_name": row["model_name"],
                "deterministic_grade": row["deterministic_grade"],
                "extraction_status": row["extraction_status"],
                "helper_status": row["helper_status"],
                "bert_precision": precision[idx],
                "bert_recall": recall[idx],
                "bert_f1": f1[idx],
                "candidate_text_length_chars": len(row["candidate_text"]),
                "reference_text_length_chars": len(row["reference_text"]),
                "source_run_id": row["source_run_id"],
                "reference_source": row["reference_source"],
                "candidate_source": row["candidate_source"],
                "candidate_text_hash": sha256_text(row["candidate_text"]),
                "reference_text_hash": sha256_text(row["reference_text"]),
            }
        )

    csv_fields = [
        "batch",
        "scenario_id",
        "category",
        "model_name",
        "deterministic_grade",
        "extraction_status",
        "helper_status",
        "bert_precision",
        "bert_recall",
        "bert_f1",
        "candidate_text_length_chars",
        "reference_text_length_chars",
        "source_run_id",
        "reference_source",
        "candidate_source",
        "candidate_text_hash",
        "reference_text_hash",
    ]
    write_csv(output_dir / "bertscore_structured_all32_phase1_hardened.csv", output_rows, csv_fields)

    by_batch = summarize(output_rows, ("batch",))
    by_scenario = summarize(output_rows, ("scenario_id", "category"))
    by_model = summarize(output_rows, ("model_name",))
    by_grade = summarize(output_rows, ("deterministic_grade",))
    write_csv(output_dir / "bertscore_structured_all32_phase1_hardened_by_batch.csv", by_batch)
    write_csv(output_dir / "bertscore_structured_all32_phase1_hardened_by_scenario.csv", by_scenario)
    write_csv(output_dir / "bertscore_structured_all32_phase1_hardened_by_model.csv", by_model)
    write_csv(output_dir / "bertscore_structured_all32_phase1_hardened_by_grade.csv", by_grade)

    baseline = load_baseline_summary()
    overall = stats_for(output_rows)
    write_baseline_comparison(output_dir / "bertscore_structured_vs_original_baseline_summary.csv", overall, baseline)

    manifest = {
        "run_name": RUN_NAME,
        "created_at": utc_now(),
        "source_summary_folder": str(SUMMARY_DIR.relative_to(ROOT)),
        "output_folder": str(output_dir.relative_to(ROOT)),
        "reference_source": REFERENCE_SOURCE,
        "reference_files": [str(path) for path in reference_files],
        "candidate_source": CANDIDATE_SOURCE,
        "candidate_rows_scored": len(output_rows),
        "review_rows_scored": 0,
        "scenario_count": len({row["scenario_id"] for row in output_rows}),
        "batch_distribution": dict(Counter(row["batch"] for row in output_rows)),
        "deterministic_grade_distribution": dict(Counter(row["deterministic_grade"] for row in output_rows)),
        "extraction_status_distribution": dict(Counter(row["extraction_status"] for row in output_rows)),
        "helper_status_distribution": dict(Counter(row["helper_status"] for row in output_rows)),
        "lang": LANG,
        "rescale_with_baseline": rescale,
        "bertscore_model": model_hash,
        "bertscore_notes": notes,
        "overall": overall,
        "previous_baseline_summary": baseline,
        "learning_db_modified": False,
        "raw_outputs_modified": False,
        "model_or_llm_api_calls": False,
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (output_dir / "bertscore_structured_all32_phase1_hardened.json").write_text(
        json.dumps({"manifest": manifest, "rows": output_rows}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_report(
        output_dir / "BERTSCORE_STRUCTURED_ALL32_PHASE1_HARDENED_REPORT.md",
        output_rows,
        by_batch,
        by_scenario,
        by_model,
        by_grade,
        manifest,
        baseline,
    )

    print(f"run_name={RUN_NAME}")
    print(f"clean_rows_scored={len(output_rows)}")
    print(f"scenario_count={manifest['scenario_count']}")
    print(f"deterministic_grade_distribution={json.dumps(manifest['deterministic_grade_distribution'], sort_keys=True)}")
    print(f"rescale_with_baseline={rescale}")
    print(f"overall_f1 mean={overall['mean_f1']:.6f} median={overall['median_f1']:.6f} min={overall['min_f1']:.6f} max={overall['max_f1']:.6f}")
    print(f"output_dir={output_dir}")


if __name__ == "__main__":
    main()
