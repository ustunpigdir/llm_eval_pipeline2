#!/usr/bin/env python3
"""Verify the full usable BERTScore layer and exports."""
from __future__ import annotations

import argparse
import csv
import re
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
DEFAULT_REFERENCE_DIR = Path("/Users/upigdir/Desktop/Pipeline/Scenarios to Run")
OUTPUT_DIR = ROOT / "outputs" / "bertscore_full_usable_v1"
RUN_NAME = "pre_structured_prompt_usable_full_v1"
EXPECTED_RESULTS = 617
EXPECTED_SCENARIOS = 32
SCENARIO_HEADING_RE = re.compile(r"^##\s+([A-Z]{2,4}_[A-Z0-9]+_[0-9]{3})\b.*$", re.MULTILINE)

REQUIRED_EXPORTS = [
    "bertscore_full_usable_results.csv",
    "bertscore_summary_by_model.csv",
    "bertscore_summary_by_scenario.csv",
    "bertscore_summary_by_deterministic_group.csv",
    "manifest.json",
    "BERTSCORE_FULL_USABLE_REPORT.md",
]


def connect_readonly(db_path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def parse_reference_ids(reference_dir: Path) -> set[str]:
    ids: set[str] = set()
    files = sorted(reference_dir.glob("worked_solutions_batch*.md"))
    if len(files) != 7:
        raise SystemExit(f"Expected 7 worked solution files, found {len(files)}")
    for path in files:
        ids.update(SCENARIO_HEADING_RE.findall(path.read_text(encoding="utf-8")))
    return ids


def csv_rows(path: Path) -> int:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return max(len(list(csv.reader(handle))) - 1, 0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    parser.add_argument("--reference-dir", default=str(DEFAULT_REFERENCE_DIR))
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR))
    args = parser.parse_args()

    failures: list[str] = []
    con = connect_readonly(Path(args.db))
    try:
        run = con.execute("SELECT * FROM bertscore_runs WHERE run_name = ?", (RUN_NAME,)).fetchone()
        if not run:
            failures.append(f"Missing bertscore_runs row for {RUN_NAME}")
            bertscore_run_id = None
        else:
            bertscore_run_id = int(run["bertscore_run_id"])
            result_count = int(
                con.execute(
                    "SELECT COUNT(*) FROM bertscore_results WHERE bertscore_run_id = ?",
                    (bertscore_run_id,),
                ).fetchone()[0]
            )
            if result_count != EXPECTED_RESULTS:
                failures.append(f"Expected {EXPECTED_RESULTS} result rows, found {result_count}")

            outside_count = int(
                con.execute(
                    """
                    SELECT COUNT(*)
                    FROM bertscore_results AS br
                    LEFT JOIN official_usable_gradeable_runs AS ogr
                        ON ogr.run_id = br.run_id
                    WHERE br.bertscore_run_id = ?
                      AND ogr.run_id IS NULL
                    """,
                    (bertscore_run_id,),
                ).fetchone()[0]
            )
            if outside_count:
                failures.append(f"{outside_count} result rows are not in official_usable_gradeable_runs")

            unusable_count = int(
                con.execute(
                    """
                    SELECT COUNT(*)
                    FROM bertscore_results AS br
                    JOIN run_quality_status AS rqs
                        ON rqs.run_id = br.run_id
                    WHERE br.bertscore_run_id = ?
                      AND rqs.usability_status = 'UNUSABLE'
                    """,
                    (bertscore_run_id,),
                ).fetchone()[0]
            )
            if unusable_count:
                failures.append(f"{unusable_count} unusable runs are included")

        reference_ids = parse_reference_ids(Path(args.reference_dir))
        official_ids = {
            row["scenario_id"]
            for row in con.execute("SELECT DISTINCT scenario_id FROM official_usable_gradeable_runs")
        }
        missing_refs = sorted(official_ids - reference_ids)
        if len(reference_ids) != EXPECTED_SCENARIOS:
            failures.append(f"Expected {EXPECTED_SCENARIOS} reference IDs, found {len(reference_ids)}")
        if missing_refs:
            failures.append("Missing references: " + ", ".join(missing_refs))

        for view_name in [
            "bertscore_latest_results",
            "bertscore_summary_by_model",
            "bertscore_summary_by_scenario",
            "bertscore_summary_by_deterministic_group",
        ]:
            view_count = int(con.execute(f'SELECT COUNT(*) FROM "{view_name}"').fetchone()[0])
            if view_count == 0:
                failures.append(f"View {view_name} returned zero rows")
    finally:
        con.close()

    output_dir = Path(args.output_dir)
    for filename in REQUIRED_EXPORTS:
        path = output_dir / filename
        if not path.exists():
            failures.append(f"Missing export file: {filename}")
            continue
        if path.stat().st_size == 0:
            failures.append(f"Export file is empty: {filename}")
        if path.suffix == ".csv" and csv_rows(path) == 0:
            failures.append(f"Export CSV has no data rows: {filename}")

    print(f"run_name={RUN_NAME}")
    print(f"reference_ids={len(reference_ids) if 'reference_ids' in locals() else 0}")
    if 'bertscore_run_id' in locals() and bertscore_run_id is not None:
        print(f"bertscore_run_id={bertscore_run_id}")
    print("exports_checked=" + ", ".join(REQUIRED_EXPORTS))

    if failures:
        print("verification=FAIL")
        for failure in failures:
            print(f"  {failure}")
        raise SystemExit(1)

    print("verification=PASS")


if __name__ == "__main__":
    main()
