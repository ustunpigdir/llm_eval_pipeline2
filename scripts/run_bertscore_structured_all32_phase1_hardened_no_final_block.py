#!/usr/bin/env python3
"""Run BERTScore on structured all-32 answers after removing FINAL ANSWER blocks."""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median
from typing import Any

from run_bertscore_structured_all32_phase1_hardened import (
    CANDIDATE_SOURCE,
    EXPECTED_CLEAN_ROWS,
    EXPECTED_FAIL,
    EXPECTED_PASS,
    EXPECTED_SCENARIOS,
    LANG,
    REFERENCE_SOURCE,
    ROOT,
    SUMMARY_DIR,
    compute_bertscore_batches,
    load_categories,
    load_structured_rows,
    parse_references,
    sha256_text,
    utc_now,
    validate_inputs,
)


DEFAULT_DB = ROOT / "learning.db"
DEFAULT_REFERENCE_DIR = Path("/Users/upigdir/Desktop/Pipeline/Scenarios to Run")
OUTPUT_DIR = ROOT / "outputs" / "bertscore_structured_all32_phase1_hardened_no_final_block_v1"
FULL_ANSWER_DIR = ROOT / "outputs" / "bertscore_structured_all32_phase1_hardened_v1"
RUN_NAME = "structured_prompt_all32_phase1_hardened_no_final_block_v1"

FINAL_ANSWER_BLOCK_RE = re.compile(
    r"""
    (?P<block>
        ^[ \t]*(?:\#{1,6}[ \t]*)?(?:\*\*)?[ \t]*final[ \t]+answer[ \t]*(?:\*\*)?[ \t]*:?[
        \t]*\n+
        [ \t]*(?:\\\[[ \t]*\n*)?
        [ \t]*\\begin\{aligned\}
        .*?
        \\end\{aligned\}
        [ \t]*(?:\n*[ \t]*\\\])?
    )
    """,
    re.IGNORECASE | re.MULTILINE | re.DOTALL | re.VERBOSE,
)


def remove_final_answer_block(text: str) -> tuple[str, bool, int]:
    match = FINAL_ANSWER_BLOCK_RE.search(text or "")
    if not match:
        return text or "", False, 0
    start, end = match.span("block")
    transformed = ((text or "")[:start].rstrip() + "\n" + (text or "")[end:].lstrip()).strip()
    removed = len(text or "") - len(transformed)
    return transformed, True, removed


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
        "rows_scored": len(rows),
        "mean_precision": mean(p),
        "mean_recall": mean(r),
        "mean_f1": mean(f),
        "median_f1": median(f),
        "min_f1": min(f),
        "max_f1": max(f),
        "pass_count": grades.get("PASS", 0),
        "fail_count": grades.get("FAIL", 0),
        "pass_mean_f1": mean([float(row["bert_f1"]) for row in rows if row["deterministic_grade"] == "PASS"])
        if grades.get("PASS", 0)
        else "",
        "fail_mean_f1": mean([float(row["bert_f1"]) for row in rows if row["deterministic_grade"] == "FAIL"])
        if grades.get("FAIL", 0)
        else "",
        "PASS_minus_FAIL_mean_F1_gap": (
            mean([float(row["bert_f1"]) for row in rows if row["deterministic_grade"] == "PASS"])
            - mean([float(row["bert_f1"]) for row in rows if row["deterministic_grade"] == "FAIL"])
        )
        if grades.get("PASS", 0) and grades.get("FAIL", 0)
        else "",
    }


def summarize(rows: list[dict[str, Any]], keys: tuple[str, ...]) -> list[dict[str, Any]]:
    grouped: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[tuple(row[key] for key in keys)].append(row)
    out: list[dict[str, Any]] = []
    for key_values, group in sorted(grouped.items()):
        item = {keys[idx]: key_values[idx] for idx in range(len(keys))}
        item.update(stats_for(group))
        out.append(item)
    return out


def load_full_answer_rows() -> tuple[dict[str, dict[str, Any]], str]:
    path = FULL_ANSWER_DIR / "bertscore_structured_all32_phase1_hardened.csv"
    if not path.exists():
        return {}, "skipped_missing_full_answer_csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    keys = [row.get("source_run_id", "") for row in rows]
    if any(not key for key in keys) or len(set(keys)) != len(keys):
        compound = [f"{row.get('batch')}|{row.get('scenario_id')}|{row.get('model_name')}|{row.get('source_run_id')}" for row in rows]
        if len(set(compound)) != len(compound):
            return {}, "skipped_no_unique_safe_key"
        return {key: row for key, row in zip(compound, rows)}, "aligned_by_batch_scenario_model_source_run_id"
    return {row["source_run_id"]: row for row in rows}, "aligned_by_source_run_id"


def compare_to_full(no_final_rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any], str]:
    full_rows, status = load_full_answer_rows()
    full_path = FULL_ANSWER_DIR / "bertscore_structured_all32_phase1_hardened.csv"
    if not full_rows:
        return [], {"row_level_alignment_status": status}, status

    paired: list[dict[str, Any]] = []
    for row in no_final_rows:
        key = row["source_run_id"] if status == "aligned_by_source_run_id" else (
            f"{row['batch']}|{row['scenario_id']}|{row['model_name']}|{row['source_run_id']}"
        )
        full = full_rows.get(key)
        if not full:
            continue
        full_f1 = float(full["bert_f1"])
        no_final_f1 = float(row["bert_f1"])
        paired.append(
            {
                "source_run_id": row["source_run_id"],
                "batch": row["batch"],
                "scenario_id": row["scenario_id"],
                "model_name": row["model_name"],
                "deterministic_grade": row["deterministic_grade"],
                "full_bert_f1": full_f1,
                "no_final_bert_f1": no_final_f1,
                "delta_f1": no_final_f1 - full_f1,
            }
        )

    if len(paired) != len(no_final_rows):
        status = f"{status}_partial_{len(paired)}_of_{len(no_final_rows)}"

    full_all = [float(row["bert_f1"]) for row in full_rows.values()]
    no_all = [float(row["bert_f1"]) for row in no_final_rows]
    full_pass = [float(full_rows[row["source_run_id"]]["bert_f1"]) for row in no_final_rows if row["deterministic_grade"] == "PASS"]
    full_fail = [float(full_rows[row["source_run_id"]]["bert_f1"]) for row in no_final_rows if row["deterministic_grade"] == "FAIL"]
    no_pass = [float(row["bert_f1"]) for row in no_final_rows if row["deterministic_grade"] == "PASS"]
    no_fail = [float(row["bert_f1"]) for row in no_final_rows if row["deterministic_grade"] == "FAIL"]
    full_gap = mean(full_pass) - mean(full_fail)
    no_gap = mean(no_pass) - mean(no_fail)
    deltas = [float(row["delta_f1"]) for row in paired]
    delta_by_grade: dict[str, float] = {}
    for grade in ("PASS", "FAIL"):
        vals = [float(row["delta_f1"]) for row in paired if row["deterministic_grade"] == grade]
        delta_by_grade[grade] = mean(vals) if vals else 0.0

    scenario_deltas: dict[str, list[float]] = defaultdict(list)
    for row in paired:
        scenario_deltas[row["scenario_id"]].append(float(row["delta_f1"]))
    scenario_delta_rows = [
        {"scenario_id": scenario_id, "rows_scored": len(vals), "mean_delta_f1": mean(vals)}
        for scenario_id, vals in scenario_deltas.items()
    ]

    comparison = {
        "row_level_alignment_status": status,
        "full_answer_csv": str(full_path.relative_to(ROOT)),
        "aligned_rows": len(paired),
        "full_overall_mean_f1": mean(full_all),
        "no_final_overall_mean_f1": mean(no_all),
        "delta_overall_mean_f1": mean(no_all) - mean(full_all),
        "full_PASS_mean_f1": mean(full_pass),
        "no_final_PASS_mean_f1": mean(no_pass),
        "full_FAIL_mean_f1": mean(full_fail),
        "no_final_FAIL_mean_f1": mean(no_fail),
        "full_PASS_minus_FAIL_gap": full_gap,
        "no_final_PASS_minus_FAIL_gap": no_gap,
        "delta_gap": no_gap - full_gap,
        "rows_no_final_f1_increased": sum(1 for value in deltas if value > 0),
        "rows_no_final_f1_decreased": sum(1 for value in deltas if value < 0),
        "rows_no_final_f1_unchanged": sum(1 for value in deltas if value == 0),
        "mean_delta_f1_by_grade": delta_by_grade,
        "largest_scenario_drops": sorted(scenario_delta_rows, key=lambda row: float(row["mean_delta_f1"]))[:5],
        "largest_scenario_increases": sorted(scenario_delta_rows, key=lambda row: float(row["mean_delta_f1"]), reverse=True)[:5],
    }
    return paired, comparison, status


def write_comparison_csv(path: Path, comparison: dict[str, Any]) -> None:
    rows = [
        {"metric": key, "value": json.dumps(value, sort_keys=True) if isinstance(value, (dict, list)) else value}
        for key, value in comparison.items()
    ]
    write_csv(path, rows, ["metric", "value"])


def interpretation(comparison: dict[str, Any]) -> tuple[str, str]:
    delta_overall = float(comparison.get("delta_overall_mean_f1", 0.0))
    delta_gap = float(comparison.get("delta_gap", 0.0))
    if delta_overall < 0 and delta_gap > 0:
        interp = (
            "Removing the FINAL ANSWER block reduced overall BERTScore while increasing PASS-vs-FAIL separation; "
            "the final block was likely inflating semantic overlap, and no-final-block BERTScore is more diagnostic."
        )
        recommendation = "Report both, with no-final-block as the reasoning-overlap diagnostic and deterministic grading as primary."
    elif delta_overall < 0 and delta_gap < 0:
        interp = (
            "Removing the FINAL ANSWER block reduced overall BERTScore and shrank PASS-vs-FAIL separation; "
            "BERTScore remains weak as a correctness proxy."
        )
        recommendation = "Report both for transparency, but do not rely on no-final-block BERTScore as a primary separator."
    else:
        interp = (
            "Removing the FINAL ANSWER block did not materially improve PASS-vs-FAIL separation; "
            "the final block is not the main reason BERTScore weakly separates deterministic outcomes."
        )
        recommendation = "Report both if space permits; otherwise keep deterministic grading primary and treat BERTScore as context."
    return interp, recommendation


def write_report(
    path: Path,
    manifest: dict[str, Any],
    by_grade: list[dict[str, Any]],
    by_batch: list[dict[str, Any]],
    comparison: dict[str, Any],
    warnings: list[dict[str, Any]],
) -> None:
    interp, recommendation = interpretation(comparison)
    lines = [
        "# BERTScore Structured All-32 Phase-1-Hardened No-Final-Block Report",
        "",
        "## Scope",
        "",
        f"- Run name: `{RUN_NAME}`",
        "- Transformation: remove FINAL ANSWER aligned block from candidate and reference texts before scoring",
        f"- Rows scored: {manifest['rows_scored']}",
        f"- Rescale with baseline: {manifest['rescale_with_baseline']}",
        f"- BERTScore model hash: {manifest['bertscore_model']}",
        "",
        "## Final Block Removal",
        "",
        f"- Candidate blocks removed: {manifest['final_block_removal_summary']['candidate_blocks_removed']}",
        f"- Candidate warnings: {manifest['final_block_removal_summary']['candidate_blocks_not_found']}",
        f"- Reference blocks removed: {manifest['final_block_removal_summary']['reference_blocks_removed']}",
        f"- Reference warnings: {manifest['final_block_removal_summary']['reference_blocks_not_found']}",
        "",
        "## Overall No-Final-Block BERTScore",
        "",
        f"- Mean F1: {manifest['overall']['mean_f1']:.6f}",
        f"- Median F1: {manifest['overall']['median_f1']:.6f}",
        f"- Min F1: {manifest['overall']['min_f1']:.6f}",
        f"- Max F1: {manifest['overall']['max_f1']:.6f}",
        "",
        "## By Deterministic Grade",
        "",
        "| grade | rows | mean_f1 | median_f1 | min_f1 | max_f1 |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in by_grade:
        lines.append(
            f"| {row['deterministic_grade']} | {row['rows_scored']} | {float(row['mean_f1']):.6f} | "
            f"{float(row['median_f1']):.6f} | {float(row['min_f1']):.6f} | {float(row['max_f1']):.6f} |"
        )
    lines.extend(["", "## By Batch", "", "| batch | rows | PASS | FAIL | mean_f1 | median_f1 |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    for row in by_batch:
        lines.append(
            f"| {row['batch']} | {row['rows_scored']} | {row['pass_count']} | {row['fail_count']} | "
            f"{float(row['mean_f1']):.6f} | {float(row['median_f1']):.6f} |"
        )
    lines.extend(
        [
            "",
            "## Full vs No-Final Comparison",
            "",
            f"- Row-level alignment status: {comparison.get('row_level_alignment_status')}",
            f"- Full overall mean F1: {comparison.get('full_overall_mean_f1'):.6f}",
            f"- No-final overall mean F1: {comparison.get('no_final_overall_mean_f1'):.6f}",
            f"- Delta overall mean F1: {comparison.get('delta_overall_mean_f1'):.6f}",
            f"- Full PASS-minus-FAIL gap: {comparison.get('full_PASS_minus_FAIL_gap'):.6f}",
            f"- No-final PASS-minus-FAIL gap: {comparison.get('no_final_PASS_minus_FAIL_gap'):.6f}",
            f"- Delta gap: {comparison.get('delta_gap'):.6f}",
            f"- Rows increased: {comparison.get('rows_no_final_f1_increased')}",
            f"- Rows decreased: {comparison.get('rows_no_final_f1_decreased')}",
            "",
            "## Interpretation",
            "",
            f"1. Did removing the FINAL ANSWER block reduce overall BERTScore? {'Yes' if comparison.get('delta_overall_mean_f1', 0) < 0 else 'No'}.",
            f"2. Did it increase or decrease PASS-vs-FAIL separation? {'Increased' if comparison.get('delta_gap', 0) > 0 else 'Decreased or unchanged'}.",
            f"3. Does this make BERTScore more useful as a reasoning-overlap metric? {interp}",
            "4. Does deterministic grading remain primary? Yes.",
            f"5. Future reporting recommendation: {recommendation}",
            "",
            "## Validation",
            "",
            f"- PASS/FAIL: PASS={manifest['deterministic_grade_distribution'].get('PASS', 0)}, FAIL={manifest['deterministic_grade_distribution'].get('FAIL', 0)}",
            f"- Warning rows: {len(warnings)}",
            "- learning.db modified: false",
            "- raw outputs modified: false",
            "- model/LLM API calls made: false",
            "- old full-answer BERTScore outputs overwritten: false",
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
    full_rows = load_structured_rows(categories, references)
    validate_inputs(full_rows, references)

    scoring_rows: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    for row in full_rows:
        candidate_no_final, candidate_removed, candidate_removed_chars = remove_final_answer_block(row["candidate_text"])
        reference_no_final, reference_removed, reference_removed_chars = remove_final_answer_block(row["reference_text"])
        if not candidate_removed or not reference_removed:
            warnings.append(
                {
                    "batch": row["batch"],
                    "scenario_id": row["scenario_id"],
                    "model_name": row["model_name"],
                    "source_run_id": row["source_run_id"],
                    "final_block_removed_candidate": candidate_removed,
                    "final_block_removed_reference": reference_removed,
                }
            )
        scoring_rows.append(
            {
                **row,
                "candidate_no_final_text": candidate_no_final,
                "reference_no_final_text": reference_no_final,
                "candidate_full_text_length_chars": len(row["candidate_text"]),
                "candidate_no_final_text_length_chars": len(candidate_no_final),
                "reference_full_text_length_chars": len(row["reference_text"]),
                "reference_no_final_text_length_chars": len(reference_no_final),
                "candidate_removed_chars": candidate_removed_chars,
                "reference_removed_chars": reference_removed_chars,
                "final_block_removed_candidate": candidate_removed,
                "final_block_removed_reference": reference_removed,
            }
        )

    precision, recall, f1, model_hash, rescale, notes = compute_bertscore_batches(
        [row["candidate_no_final_text"] for row in scoring_rows],
        [row["reference_no_final_text"] for row in scoring_rows],
        args.batch_size,
    )

    output_rows: list[dict[str, Any]] = []
    for idx, row in enumerate(scoring_rows):
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
                "candidate_full_text_length_chars": row["candidate_full_text_length_chars"],
                "candidate_no_final_text_length_chars": row["candidate_no_final_text_length_chars"],
                "reference_full_text_length_chars": row["reference_full_text_length_chars"],
                "reference_no_final_text_length_chars": row["reference_no_final_text_length_chars"],
                "candidate_removed_chars": row["candidate_removed_chars"],
                "reference_removed_chars": row["reference_removed_chars"],
                "final_block_removed_candidate": row["final_block_removed_candidate"],
                "final_block_removed_reference": row["final_block_removed_reference"],
                "source_run_id": row["source_run_id"],
                "reference_source": REFERENCE_SOURCE,
                "candidate_source": CANDIDATE_SOURCE,
                "candidate_no_final_text_hash": sha256_text(row["candidate_no_final_text"]),
                "reference_no_final_text_hash": sha256_text(row["reference_no_final_text"]),
            }
        )

    if len(output_rows) != EXPECTED_CLEAN_ROWS:
        raise SystemExit(f"Expected {EXPECTED_CLEAN_ROWS} output rows, found {len(output_rows)}")
    grades = Counter(row["deterministic_grade"] for row in output_rows)
    if grades["PASS"] != EXPECTED_PASS or grades["FAIL"] != EXPECTED_FAIL:
        raise SystemExit(f"Expected PASS={EXPECTED_PASS}, FAIL={EXPECTED_FAIL}; found {dict(grades)}")
    if len({row["scenario_id"] for row in output_rows}) != EXPECTED_SCENARIOS:
        raise SystemExit("Scenario count validation failed")

    row_fields = [
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
        "candidate_full_text_length_chars",
        "candidate_no_final_text_length_chars",
        "reference_full_text_length_chars",
        "reference_no_final_text_length_chars",
        "candidate_removed_chars",
        "reference_removed_chars",
        "final_block_removed_candidate",
        "final_block_removed_reference",
        "source_run_id",
        "reference_source",
        "candidate_source",
        "candidate_no_final_text_hash",
        "reference_no_final_text_hash",
    ]
    write_csv(output_dir / "bertscore_structured_all32_phase1_hardened_no_final_block.csv", output_rows, row_fields)
    by_batch = summarize(output_rows, ("batch",))
    by_scenario = summarize(output_rows, ("scenario_id", "category"))
    by_model = summarize(output_rows, ("model_name",))
    by_grade = summarize(output_rows, ("deterministic_grade",))
    write_csv(output_dir / "bertscore_structured_all32_phase1_hardened_no_final_block_by_batch.csv", by_batch)
    write_csv(output_dir / "bertscore_structured_all32_phase1_hardened_no_final_block_by_scenario.csv", by_scenario)
    write_csv(output_dir / "bertscore_structured_all32_phase1_hardened_no_final_block_by_model.csv", by_model)
    write_csv(output_dir / "bertscore_structured_all32_phase1_hardened_no_final_block_by_grade.csv", by_grade)
    write_csv(
        output_dir / "final_block_removal_warnings.csv",
        warnings,
        [
            "batch",
            "scenario_id",
            "model_name",
            "source_run_id",
            "final_block_removed_candidate",
            "final_block_removed_reference",
        ],
    )

    paired, comparison, alignment_status = compare_to_full(output_rows)
    write_comparison_csv(output_dir / "bertscore_full_vs_no_final_block_comparison.csv", comparison)

    overall = stats_for(output_rows)
    removal_summary = {
        "candidate_blocks_removed": sum(1 for row in output_rows if row["final_block_removed_candidate"]),
        "candidate_blocks_not_found": sum(1 for row in output_rows if not row["final_block_removed_candidate"]),
        "reference_blocks_removed": sum(1 for row in output_rows if row["final_block_removed_reference"]),
        "reference_blocks_not_found": sum(1 for row in output_rows if not row["final_block_removed_reference"]),
        "total_candidate_removed_chars": sum(int(row["candidate_removed_chars"]) for row in output_rows),
        "total_reference_removed_chars": sum(int(row["reference_removed_chars"]) for row in output_rows),
    }
    manifest = {
        "run_name": RUN_NAME,
        "created_at": utc_now(),
        "source_summary_folder": str(SUMMARY_DIR.relative_to(ROOT)),
        "output_folder": str(output_dir.relative_to(ROOT)),
        "reference_source": REFERENCE_SOURCE,
        "reference_files": [str(path) for path in reference_files],
        "candidate_source": CANDIDATE_SOURCE,
        "rows_scored": len(output_rows),
        "review_rows_scored": 0,
        "scenario_count": len({row["scenario_id"] for row in output_rows}),
        "batch_distribution": dict(Counter(row["batch"] for row in output_rows)),
        "deterministic_grade_distribution": dict(grades),
        "extraction_status_distribution": dict(Counter(row["extraction_status"] for row in output_rows)),
        "helper_status_distribution": dict(Counter(row["helper_status"] for row in output_rows)),
        "final_block_removal_summary": removal_summary,
        "warning_rows": len(warnings),
        "lang": LANG,
        "rescale_with_baseline": rescale,
        "bertscore_model": model_hash,
        "bertscore_notes": notes,
        "overall": overall,
        "comparison_to_full_answer": comparison,
        "row_level_alignment_status": alignment_status,
        "paired_row_comparison_count": len(paired),
        "learning_db_modified": False,
        "raw_outputs_modified": False,
        "model_or_llm_api_calls": False,
    }

    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (output_dir / "bertscore_structured_all32_phase1_hardened_no_final_block.json").write_text(
        json.dumps({"manifest": manifest, "rows": output_rows, "paired_full_answer_comparison": paired}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_report(
        output_dir / "BERTSCORE_STRUCTURED_ALL32_PHASE1_HARDENED_NO_FINAL_BLOCK_REPORT.md",
        manifest,
        by_grade,
        by_batch,
        comparison,
        warnings,
    )

    print(f"run_name={RUN_NAME}")
    print(f"rows_scored={len(output_rows)}")
    print(f"deterministic_grade_distribution={json.dumps(dict(grades), sort_keys=True)}")
    print(f"final_block_removal_summary={json.dumps(removal_summary, sort_keys=True)}")
    print(f"row_level_alignment_status={alignment_status}")
    print(f"rescale_with_baseline={rescale}")
    print(
        "overall_f1 "
        f"mean={overall['mean_f1']:.6f} median={overall['median_f1']:.6f} "
        f"min={overall['min_f1']:.6f} max={overall['max_f1']:.6f}"
    )
    print(f"output_dir={output_dir}")


if __name__ == "__main__":
    main()
