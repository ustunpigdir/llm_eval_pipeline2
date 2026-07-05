#!/usr/bin/env python3
"""Thirty-run BERTScore pilot against worked-solution references."""
from __future__ import annotations

import argparse
import csv
import re
import sqlite3
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, median


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
DEFAULT_REFERENCE_DIR = Path("/Users/upigdir/Desktop/Pipeline/Scenarios to Run")
OUTPUT_DIR = ROOT / "outputs" / "bertscore_pilot_30_runs"

SCENARIO_HEADING_RE = re.compile(r"^##\s+([A-Z]{2,4}_[A-Z0-9]+_[0-9]{3})\b.*$", re.MULTILINE)
SUBHEADING_RE = re.compile(r"^\*\*(.+?)\*\*\s*$")
USEFUL_HEADING_RE = re.compile(r"(derivation|reasoning checkpoint|checkpoints|reasoning|solution)", re.I)
STOP_HEADING_RE = re.compile(r"(final answer|wrong-answer|wrong answer|fingerprint)", re.I)


@dataclass(frozen=True)
class CandidateRun:
    group_label: str
    run_id: int
    scenario_id: str
    model_name: str
    answer: str
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
        for scenario_id, section in split_scenario_sections(path.read_text(encoding="utf-8")).items():
            references[scenario_id] = extract_reference_text(section)
    return references, files


def connect_readonly(db_path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def official_scenario_ids(con: sqlite3.Connection) -> set[str]:
    return {
        row["scenario_id"]
        for row in con.execute("SELECT DISTINCT scenario_id FROM official_gradeable_runs ORDER BY scenario_id")
    }


def load_candidate_rows(con: sqlite3.Connection, references: dict[str, str]) -> list[sqlite3.Row]:
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
                JOIN run_quality_status AS rqs
                    ON rqs.run_id = ugr.run_id
                WHERE rqs.usability_status = 'USABLE'
                GROUP BY ugr.run_id, ugr.scenario_id, ugr.model_name
            )
            SELECT
                vc.run_id,
                vc.scenario_id,
                vc.model_name,
                q.answer,
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
    return [row for row in rows if row["scenario_id"] in references]


def row_to_candidate(row: sqlite3.Row, group_label: str) -> CandidateRun:
    return CandidateRun(
        group_label=group_label,
        run_id=int(row["run_id"]),
        scenario_id=row["scenario_id"],
        model_name=row["model_name"] or "",
        answer=row["answer"] or "",
        match_count=int(row["match_count"] or 0),
        mismatch_count=int(row["mismatch_count"] or 0),
        not_found_count=int(row["not_found_count"] or 0),
        review_count=int(row["review_count"] or 0),
    )


def take_unique(
    rows: list[sqlite3.Row],
    selected_ids: set[int],
    group_label: str,
    limit: int = 10,
) -> list[CandidateRun]:
    out: list[CandidateRun] = []
    for row in rows:
        run_id = int(row["run_id"])
        if run_id in selected_ids:
            continue
        out.append(row_to_candidate(row, group_label))
        selected_ids.add(run_id)
        if len(out) == limit:
            break
    return out


def select_30_runs(rows: list[sqlite3.Row]) -> tuple[list[CandidateRun], list[str]]:
    selected_ids: set[int] = set()
    notes: list[str] = []

    match_rows = sorted(
        [
            row
            for row in rows
            if row["match_count"] > 0
            and row["mismatch_count"] == 0
            and row["not_found_count"] == 0
            and row["review_count"] == 0
        ],
        key=lambda row: (-row["match_count"], row["run_id"]),
    )
    match_group = take_unique(match_rows, selected_ids, "MATCH-heavy")

    strict_mismatch_rows = sorted(
        [
            row
            for row in rows
            if row["mismatch_count"] > 0
            and row["mismatch_count"] >= row["match_count"]
            and row["not_found_count"] == 0
            and row["review_count"] == 0
        ],
        key=lambda row: (-row["mismatch_count"], row["match_count"], row["run_id"]),
    )
    mismatch_group = take_unique(strict_mismatch_rows, selected_ids, "MISMATCH-heavy")
    if len(mismatch_group) < 10:
        notes.append(
            f"MISMATCH-heavy strict selection produced {len(mismatch_group)} runs; relaxed to any mismatch_count > 0."
        )
        relaxed_rows = sorted(
            [row for row in rows if row["mismatch_count"] > 0],
            key=lambda row: (-row["mismatch_count"], row["not_found_count"], row["review_count"], row["run_id"]),
        )
        mismatch_group += take_unique(relaxed_rows, selected_ids, "MISMATCH-heavy", 10 - len(mismatch_group))

    nf_review_rows = sorted(
        [row for row in rows if row["not_found_count"] > 0 or row["review_count"] > 0],
        key=lambda row: (-(row["not_found_count"] + row["review_count"]), -row["not_found_count"], -row["review_count"], row["run_id"]),
    )
    nf_review_group = take_unique(nf_review_rows, selected_ids, "NOT_FOUND/REVIEW-heavy")
    if len(nf_review_group) < 10:
        notes.append(
            f"NOT_FOUND/REVIEW-heavy selection produced only {len(nf_review_group)} usable runs."
        )

    selected = match_group + mismatch_group + nf_review_group
    if len(match_group) != 10:
        notes.append(f"MATCH-heavy selected {len(match_group)} runs instead of 10.")
    if len(mismatch_group) != 10:
        notes.append(f"MISMATCH-heavy selected {len(mismatch_group)} runs instead of 10.")
    if len(selected) != 30:
        notes.append(f"Total selected run count is {len(selected)} instead of 30.")

    return selected, notes


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
        precision, recall, f1, model_hash = unpack_bertscore_result(
            score(
                candidates,
                references,
                lang="en",
                rescale_with_baseline=True,
                verbose=False,
            )
        )
        rescale = True
    except Exception as exc:
        notes = f"rescale_with_baseline=True failed; retried without baseline: {type(exc).__name__}: {exc}"
        precision, recall, f1, model_hash = unpack_bertscore_result(
            score(
                candidates,
                references,
                lang="en",
                rescale_with_baseline=False,
                verbose=False,
            )
        )
        rescale = False

    return (
        [float(x) for x in precision.tolist()],
        [float(x) for x in recall.tolist()],
        [float(x) for x in f1.tolist()],
        str(model_hash),
        rescale,
        notes,
    )


def summarize_groups(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    summaries: list[dict[str, object]] = []
    for group_label in ["MATCH-heavy", "MISMATCH-heavy", "NOT_FOUND/REVIEW-heavy"]:
        group = [row for row in rows if row["group_label"] == group_label]
        if not group:
            continue
        f1_values = [float(row["bertscore_f1"]) for row in group]
        summaries.append(
            {
                "group_label": group_label,
                "n_runs": len(group),
                "mean_precision": mean(float(row["bertscore_precision"]) for row in group),
                "mean_recall": mean(float(row["bertscore_recall"]) for row in group),
                "mean_f1": mean(f1_values),
                "median_f1": median(f1_values),
                "min_f1": min(f1_values),
                "max_f1": max(f1_values),
                "mean_match_count": mean(int(row["deterministic_match_count"]) for row in group),
                "mean_mismatch_count": mean(int(row["deterministic_mismatch_count"]) for row in group),
                "mean_not_found_count": mean(int(row["deterministic_not_found_count"]) for row in group),
                "mean_review_count": mean(int(row["deterministic_review_count"]) for row in group),
            }
        )
    return summaries


def scenario_distribution(selected: list[CandidateRun]) -> list[dict[str, object]]:
    by_scenario: dict[str, list[str]] = {}
    for run in selected:
        by_scenario.setdefault(run.scenario_id, []).append(run.group_label)
    return [
        {
            "scenario_id": scenario_id,
            "n_selected_runs": len(groups),
            "groups_present": ";".join(sorted(set(groups))),
        }
        for scenario_id, groups in sorted(by_scenario.items())
    ]


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def expected_order_holds(summaries: list[dict[str, object]]) -> bool:
    means = {row["group_label"]: float(row["mean_f1"]) for row in summaries}
    return (
        means.get("MATCH-heavy", float("-inf"))
        > means.get("MISMATCH-heavy", float("inf"))
        > means.get("NOT_FOUND/REVIEW-heavy", float("inf"))
    )


def write_markdown_report(
    output_path: Path,
    rows: list[dict[str, object]],
    summaries: list[dict[str, object]],
    distributions: list[dict[str, object]],
    reference_files: list[Path],
    parsed_ids: list[str],
    missing_ids: list[str],
    extra_ids: list[str],
    sampling_notes: list[str],
) -> None:
    order_holds = expected_order_holds(summaries)
    lines = [
        "# Thirty-Run BERTScore Pilot",
        "",
        "## Purpose",
        "",
        "Test whether full-answer BERTScore separates deterministic outcome groups before building a broader semantic judge layer.",
        "",
        "## Reference Source",
        "",
    ]
    for path in reference_files:
        lines.append(f"- `{path}`")
    lines.extend(
        [
            "",
            f"Parsed scenario references: {len(parsed_ids)}",
            f"Missing official references: {', '.join(missing_ids) if missing_ids else 'none'}",
            f"Extra reference IDs: {', '.join(extra_ids) if extra_ids else 'none'}",
            "",
            "## Sampling Rules",
            "",
            "- MATCH-heavy: exact all-match runs.",
            "- MISMATCH-heavy: mismatch_count > 0, preferring mismatch_count >= match_count and no NOT_FOUND/REVIEW.",
            "- NOT_FOUND/REVIEW-heavy: not_found_count > 0 or review_count > 0, preferring highest combined count.",
            "",
            f"Sampling notes: {'; '.join(sampling_notes) if sampling_notes else 'none'}",
            "",
            "## Selected Run List",
            "",
            "| group | run_id | scenario_id | model_name | MATCH | MISMATCH | NOT_FOUND | REVIEW | F1 |",
            "| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['group_label']} | {row['run_id']} | {row['scenario_id']} | {row['model_name']} | "
            f"{row['deterministic_match_count']} | {row['deterministic_mismatch_count']} | "
            f"{row['deterministic_not_found_count']} | {row['deterministic_review_count']} | "
            f"{float(row['bertscore_f1']):.6f} |"
        )
    lines.extend(
        [
            "",
            "## Group-Level BERTScore Summary",
            "",
            "| group | n | mean_f1 | median_f1 | min_f1 | max_f1 |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in summaries:
        lines.append(
            f"| {row['group_label']} | {row['n_runs']} | {float(row['mean_f1']):.6f} | "
            f"{float(row['median_f1']):.6f} | {float(row['min_f1']):.6f} | {float(row['max_f1']):.6f} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            f"Expected ordering held: {'yes' if order_holds else 'no'}.",
            "",
            "MATCH-heavy should tend to be highest, MISMATCH-heavy lower, and NOT_FOUND/REVIEW-heavy lowest.",
            "",
            "## Scenario Distribution",
            "",
            "| scenario_id | n_selected_runs | groups_present |",
            "| --- | ---: | --- |",
        ]
    )
    for row in distributions:
        lines.append(f"| {row['scenario_id']} | {row['n_selected_runs']} | {row['groups_present']} |")
    lines.extend(
        [
            "",
            "## Limitations",
            "",
            "This pilot scores the full model answer, not a separately extracted concept-explanation span. Full-answer BERTScore may be inflated by copied formulas, repeated prompt text, or final-answer formatting.",
            "",
            "## Recommendation",
            "",
            "Continue to a full BERTScore judge layer only if the group separation is strong enough to add value over deterministic field grading.",
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
        if missing_ids:
            raise SystemExit("Cannot run pilot: missing official references: " + ", ".join(missing_ids))
        candidate_rows = load_candidate_rows(con, references)
    finally:
        con.close()

    selected, sampling_notes = select_30_runs(candidate_rows)
    if len(selected) != 30:
        raise SystemExit(f"Expected 30 selected runs, found {len(selected)}")

    candidates = [run.answer for run in selected]
    reference_texts = [references[run.scenario_id] for run in selected]
    precision, recall, f1, model_hash, rescale, bertscore_notes = compute_bertscore(candidates, reference_texts)

    rows: list[dict[str, object]] = []
    for idx, run in enumerate(selected):
        notes = "full answer scored"
        if bertscore_notes:
            notes += "; " + bertscore_notes
        rows.append(
            {
                "group_label": run.group_label,
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

    summaries = summarize_groups(rows)
    distributions = scenario_distribution(selected)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(
        output_dir / "bertscore_pilot_30_runs.csv",
        rows,
        [
            "group_label",
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
        ],
    )
    write_csv(
        output_dir / "group_summary.csv",
        summaries,
        [
            "group_label",
            "n_runs",
            "mean_precision",
            "mean_recall",
            "mean_f1",
            "median_f1",
            "min_f1",
            "max_f1",
            "mean_match_count",
            "mean_mismatch_count",
            "mean_not_found_count",
            "mean_review_count",
        ],
    )
    write_csv(
        output_dir / "scenario_distribution.csv",
        distributions,
        ["scenario_id", "n_selected_runs", "groups_present"],
    )
    write_markdown_report(
        output_dir / "bertscore_pilot_30_runs.md",
        rows,
        summaries,
        distributions,
        reference_files,
        sorted(references),
        missing_ids,
        extra_ids,
        sampling_notes,
    )

    counts = Counter(run.group_label for run in selected)
    print(f"scenario_references_parsed={len(references)}")
    print("missing_official_references=" + (", ".join(missing_ids) if missing_ids else "none"))
    print("extra_reference_ids=" + (", ".join(extra_ids) if extra_ids else "none"))
    print("sampling_notes=" + ("; ".join(sampling_notes) if sampling_notes else "none"))
    for group_label in ["MATCH-heavy", "MISMATCH-heavy", "NOT_FOUND/REVIEW-heavy"]:
        print(f"selected_{group_label}={counts[group_label]}")
    print("group_summary")
    for row in summaries:
        print(
            f"{row['group_label']} n={row['n_runs']} mean_f1={float(row['mean_f1']):.6f} "
            f"median_f1={float(row['median_f1']):.6f} min_f1={float(row['min_f1']):.6f} "
            f"max_f1={float(row['max_f1']):.6f}"
        )
    print(f"expected_ordering_held={'yes' if expected_order_holds(summaries) else 'no'}")
    print(f"wrote={output_dir.relative_to(ROOT) / 'bertscore_pilot_30_runs.csv'}")
    print(f"wrote={output_dir.relative_to(ROOT) / 'bertscore_pilot_30_runs.md'}")
    print(f"wrote={output_dir.relative_to(ROOT) / 'group_summary.csv'}")
    print(f"wrote={output_dir.relative_to(ROOT) / 'scenario_distribution.csv'}")


if __name__ == "__main__":
    main()
