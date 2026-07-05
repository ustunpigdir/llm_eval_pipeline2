#!/usr/bin/env python3
"""Three-run BERTScore pilot against worked-solution references."""
from __future__ import annotations

import argparse
import csv
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
DEFAULT_REFERENCE_DIR = Path("/Users/upigdir/Desktop/Pipeline/Scenarios to Run")
OUTPUT_DIR = ROOT / "outputs" / "bertscore_pilot_3_runs"

SCENARIO_HEADING_RE = re.compile(r"^##\s+([A-Z]{2,4}_[A-Z0-9]+_[0-9]{3})\b.*$", re.MULTILINE)
SUBHEADING_RE = re.compile(r"^\*\*(.+?)\*\*\s*$")
USEFUL_HEADING_RE = re.compile(r"(derivation|reasoning checkpoint|checkpoints|reasoning|solution)", re.I)
STOP_HEADING_RE = re.compile(r"(final answer|wrong-answer|wrong answer|fingerprint)", re.I)


@dataclass
class PilotRun:
    run_id: int
    scenario_id: str
    model_name: str
    answer: str
    reasoning_text: str | None
    calculation_text: str | None
    match_count: int
    mismatch_count: int
    not_found_count: int
    review_count: int


def preview(text: str, limit: int = 260) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3] + "..."


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
        sections = split_scenario_sections(path.read_text(encoding="utf-8"))
        for scenario_id, section in sections.items():
            references[scenario_id] = extract_reference_text(section)

    return references, files


def connect_readonly(db_path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def official_scenario_ids(con: sqlite3.Connection) -> set[str]:
    return {
        row["scenario_id"]
        for row in con.execute(
            "SELECT DISTINCT scenario_id FROM official_gradeable_runs ORDER BY scenario_id"
        )
    }


def select_pilot_runs(con: sqlite3.Connection, references: dict[str, str]) -> list[PilotRun]:
    rows = list(
        con.execute(
            """
            WITH verdict_counts AS (
                SELECT
                    ugr.run_id,
                    ugr.scenario_id,
                    ugr.model_name,
                    SUM(CASE WHEN ugr.verdict = 'MATCH' THEN 1 ELSE 0 END) AS match_count,
                    SUM(CASE WHEN ugr.verdict = 'MISMATCH' THEN 1 ELSE 0 END) AS mismatch_count,
                    SUM(CASE WHEN ugr.verdict = 'NOT_FOUND' THEN 1 ELSE 0 END) AS not_found_count,
                    SUM(CASE WHEN ugr.verdict = 'REVIEW' THEN 1 ELSE 0 END) AS review_count
                FROM usable_grading_results AS ugr
                GROUP BY ugr.run_id, ugr.scenario_id, ugr.model_name
            )
            SELECT
                vc.run_id,
                vc.scenario_id,
                vc.model_name,
                q.answer,
                q.reasoning_text,
                q.calculation_text,
                vc.match_count,
                vc.mismatch_count,
                vc.not_found_count,
                vc.review_count
            FROM verdict_counts AS vc
            JOIN questions AS q
                ON q.run_id = vc.run_id
            ORDER BY vc.run_id
            """
        )
    )
    rows = [row for row in rows if row["scenario_id"] in references]

    selected: list[sqlite3.Row] = []
    selected_ids: set[int] = set()

    def add_best(candidates: list[sqlite3.Row], key) -> None:
        for row in sorted(candidates, key=key):
            if int(row["run_id"]) not in selected_ids:
                selected.append(row)
                selected_ids.add(int(row["run_id"]))
                return

    add_best(
        [row for row in rows if row["match_count"] > 0],
        lambda row: (-row["match_count"], row["mismatch_count"], row["not_found_count"], row["review_count"], row["run_id"]),
    )
    add_best(
        [row for row in rows if row["mismatch_count"] > 0],
        lambda row: (-row["mismatch_count"], -row["match_count"], row["not_found_count"], row["review_count"], row["run_id"]),
    )
    add_best(
        [row for row in rows if row["not_found_count"] > 0 or row["review_count"] > 0],
        lambda row: (-(row["not_found_count"] + row["review_count"]), -row["match_count"], row["run_id"]),
    )

    if len(selected) != 3:
        raise SystemExit(f"Could not select exactly 3 pilot runs; selected {len(selected)}")

    return [
        PilotRun(
            run_id=int(row["run_id"]),
            scenario_id=row["scenario_id"],
            model_name=row["model_name"] or "",
            answer=row["answer"] or "",
            reasoning_text=row["reasoning_text"],
            calculation_text=row["calculation_text"],
            match_count=int(row["match_count"] or 0),
            mismatch_count=int(row["mismatch_count"] or 0),
            not_found_count=int(row["not_found_count"] or 0),
            review_count=int(row["review_count"] or 0),
        )
        for row in selected
    ]


def require_bertscore():
    try:
        from bert_score import score
    except ImportError:
        print("Missing dependency: bert-score")
        print("Install with:")
        print("python3 -m pip install bert-score")
        raise SystemExit(2)
    return score


def unpack_bertscore_result(result):
    if len(result) == 3:
        precision, recall, f1 = result
        return precision, recall, f1, "unknown"
    if len(result) == 4:
        precision, recall, f1, model_hash = result
        return precision, recall, f1, model_hash
    raise RuntimeError(f"Unexpected bert_score.score return length: {len(result)}")


def compute_bertscore(candidates: list[str], references: list[str]) -> tuple[list[float], list[float], list[float], str, bool, str]:
    score = require_bertscore()
    notes = ""
    try:
        result = score(
            candidates,
            references,
            lang="en",
            rescale_with_baseline=True,
            verbose=False,
        )
        precision, recall, f1, model_hash = unpack_bertscore_result(result)
        rescale = True
    except Exception as exc:
        notes = f"rescale_with_baseline=True failed; retried without baseline: {type(exc).__name__}: {exc}"
        result = score(
            candidates,
            references,
            lang="en",
            rescale_with_baseline=False,
            verbose=False,
        )
        precision, recall, f1, model_hash = unpack_bertscore_result(result)
        rescale = False

    return (
        [float(x) for x in precision.tolist()],
        [float(x) for x in recall.tolist()],
        [float(x) for x in f1.tolist()],
        str(model_hash),
        rescale,
        notes,
    )


def write_csv_report(rows: list[dict[str, object]], output_path: Path) -> None:
    fieldnames = [
        "run_id",
        "scenario_id",
        "model_name",
        "deterministic_match_count",
        "deterministic_mismatch_count",
        "deterministic_not_found_count",
        "deterministic_review_count",
        "reference_source",
        "reference_text_preview",
        "candidate_source",
        "candidate_text_preview",
        "bertscore_precision",
        "bertscore_recall",
        "bertscore_f1",
        "bertscore_model",
        "rescale_with_baseline",
        "notes",
    ]
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown_report(
    rows: list[dict[str, object]],
    reference_files: list[Path],
    parsed_ids: list[str],
    missing_ids: list[str],
    extra_ids: list[str],
    output_path: Path,
) -> None:
    lines = [
        "# Three-Run BERTScore Pilot",
        "",
        "## Purpose",
        "",
        "Compare gold worked-solution reference text against model answer text for a tiny usable-run pilot.",
        "",
        "## Reference Source Files",
        "",
    ]
    for path in reference_files:
        lines.append(f"- `{path}`")
    lines.extend(
        [
            "",
            "## Reference Parsing Result",
            "",
            f"- Parsed scenario references: {len(parsed_ids)}",
            f"- Missing official references: {', '.join(missing_ids) if missing_ids else 'none'}",
            f"- Extra reference IDs: {', '.join(extra_ids) if extra_ids else 'none'}",
            "",
            "## Selected 3 Runs",
            "",
            "| run_id | scenario_id | model_name | MATCH | MISMATCH | NOT_FOUND | REVIEW |",
            "| --- | --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['run_id']} | {row['scenario_id']} | {row['model_name']} | "
            f"{row['deterministic_match_count']} | {row['deterministic_mismatch_count']} | "
            f"{row['deterministic_not_found_count']} | {row['deterministic_review_count']} |"
        )
    lines.extend(
        [
            "",
            "## BERTScore Results",
            "",
            "| run_id | scenario_id | precision | recall | f1 |",
            "| --- | --- | ---: | ---: | ---: |",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['run_id']} | {row['scenario_id']} | "
            f"{float(row['bertscore_precision']):.6f} | {float(row['bertscore_recall']):.6f} | "
            f"{float(row['bertscore_f1']):.6f} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This pilot is meant to test whether semantic similarity offers a useful signal alongside deterministic verdict counts.",
            "",
            "## Limitations",
            "",
            "This pilot scores the full model answer, not a separately extracted concept-explanation span. Full-answer BERTScore may be inflated by copied formulas, repeated prompt text, or final-answer formatting.",
            "",
            "## Recommendation",
            "",
            "Continue only if the three-run scores separate the strong deterministic case from mismatch/not-found/review cases enough to justify a broader validation set.",
        ]
    )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    parser.add_argument("--reference-dir", default=str(DEFAULT_REFERENCE_DIR))
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR))
    args = parser.parse_args()

    references, reference_files = parse_references(Path(args.reference_dir))

    con = connect_readonly(Path(args.db))
    try:
        official_ids = official_scenario_ids(con)
        parsed_ids = sorted(references)
        missing_ids = sorted(official_ids - set(references))
        extra_ids = sorted(set(references) - official_ids)

        print(f"scenario_references_parsed={len(parsed_ids)}")
        print("parsed_scenario_ids=" + ", ".join(parsed_ids))
        print("missing_official_references=" + (", ".join(missing_ids) if missing_ids else "none"))
        print("extra_reference_ids=" + (", ".join(extra_ids) if extra_ids else "none"))

        if missing_ids:
            raise SystemExit("Cannot run pilot: missing official references")

        pilot_runs = select_pilot_runs(con, references)
    finally:
        con.close()

    for run in pilot_runs:
        print(
            f"selected_run run_id={run.run_id} scenario_id={run.scenario_id} model_name={run.model_name} "
            f"MATCH={run.match_count} MISMATCH={run.mismatch_count} "
            f"NOT_FOUND={run.not_found_count} REVIEW={run.review_count} "
            f"reasoning_text_populated={bool(run.reasoning_text)} calculation_text_populated={bool(run.calculation_text)}"
        )

    candidates = [run.answer for run in pilot_runs]
    reference_texts = [references[run.scenario_id] for run in pilot_runs]
    precision, recall, f1, model_hash, rescale, bertscore_notes = compute_bertscore(candidates, reference_texts)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, object]] = []
    for idx, run in enumerate(pilot_runs):
        notes = "full answer scored"
        if bertscore_notes:
            notes += "; " + bertscore_notes
        rows.append(
            {
                "run_id": run.run_id,
                "scenario_id": run.scenario_id,
                "model_name": run.model_name,
                "deterministic_match_count": run.match_count,
                "deterministic_mismatch_count": run.mismatch_count,
                "deterministic_not_found_count": run.not_found_count,
                "deterministic_review_count": run.review_count,
                "reference_source": str(DEFAULT_REFERENCE_DIR / "worked_solutions_batch*.md"),
                "reference_text_preview": preview(reference_texts[idx]),
                "candidate_source": "questions.answer",
                "candidate_text_preview": preview(run.answer),
                "bertscore_precision": precision[idx],
                "bertscore_recall": recall[idx],
                "bertscore_f1": f1[idx],
                "bertscore_model": model_hash,
                "rescale_with_baseline": rescale,
                "notes": notes,
            }
        )

    csv_path = output_dir / "bertscore_pilot_3_runs.csv"
    md_path = output_dir / "bertscore_pilot_3_runs.md"
    write_csv_report(rows, csv_path)
    write_markdown_report(rows, reference_files, parsed_ids, missing_ids, extra_ids, md_path)

    print(f"wrote={csv_path.relative_to(ROOT)}")
    print(f"wrote={md_path.relative_to(ROOT)}")
    for row in rows:
        print(
            f"bertscore run_id={row['run_id']} scenario_id={row['scenario_id']} "
            f"P={float(row['bertscore_precision']):.6f} "
            f"R={float(row['bertscore_recall']):.6f} "
            f"F1={float(row['bertscore_f1']):.6f}"
        )


if __name__ == "__main__":
    main()
