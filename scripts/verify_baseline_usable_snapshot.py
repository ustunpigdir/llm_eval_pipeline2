#!/usr/bin/env python3
"""Verify the baseline usable benchmark snapshot against the current DB."""
from __future__ import annotations

import argparse
import csv
import json
import sqlite3
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
SNAPSHOT_NAME = "baseline_usable_20260705"
SNAPSHOT_DIR = ROOT / "exports" / SNAPSHOT_NAME

REQUIRED_CSVS = [
    "usable_grading_summary_overall.csv",
    "usable_grading_summary_by_model.csv",
    "usable_grading_summary_by_scenario.csv",
    "usable_grading_results.csv",
    "official_usable_gradeable_runs.csv",
    "unusable_official_runs.csv",
    "all_grading_summary_overall.csv",
    "all_grading_results_verdict_distribution.csv",
]


def connect_readonly(db_path: Path) -> sqlite3.Connection:
    return sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)


def count(con: sqlite3.Connection, table_or_view: str) -> int:
    return int(con.execute(f'SELECT COUNT(*) FROM "{table_or_view}"').fetchone()[0])


def verdict_distribution(con: sqlite3.Connection, table_or_view: str) -> dict[str, int]:
    return {
        str(verdict): int(row_count)
        for verdict, row_count in con.execute(
            f'SELECT verdict, COUNT(*) FROM "{table_or_view}" GROUP BY verdict'
        )
    }


def csv_data_row_count(path: Path) -> int:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return 0
    return max(len(rows) - 1, 0)


def expected_manifest_counts(con: sqlite3.Connection) -> dict[str, Any]:
    return {
        "official_gradeable_runs": count(con, "official_gradeable_runs"),
        "usable_official_gradeable_runs": count(con, "official_usable_gradeable_runs"),
        "unusable_official_runs": count(con, "unusable_official_runs"),
        "grading_result_rows_all": count(con, "grading_results"),
        "grading_result_rows_usable": count(con, "usable_grading_results"),
        "all_verdict_distribution": verdict_distribution(con, "grading_results"),
        "usable_verdict_distribution": verdict_distribution(con, "usable_grading_results"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    parser.add_argument("--snapshot-dir", default=str(SNAPSHOT_DIR))
    args = parser.parse_args()

    snapshot_dir = Path(args.snapshot_dir)
    failures: list[str] = []

    if not snapshot_dir.exists():
        failures.append(f"Snapshot folder does not exist: {snapshot_dir}")

    csv_counts: dict[str, int] = {}
    for filename in REQUIRED_CSVS:
        path = snapshot_dir / filename
        if not path.exists():
            failures.append(f"Missing required CSV: {filename}")
            continue
        row_count = csv_data_row_count(path)
        csv_counts[filename] = row_count
        if row_count == 0:
            failures.append(f"Required CSV is empty: {filename}")

    manifest_path = snapshot_dir / "manifest.json"
    manifest: dict[str, Any] = {}
    if not manifest_path.exists():
        failures.append("Missing manifest.json")
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    con = connect_readonly(Path(args.db))
    try:
        if manifest:
            expected = expected_manifest_counts(con)
            for key, expected_value in expected.items():
                actual_value = manifest.get(key)
                if actual_value != expected_value:
                    failures.append(f"Manifest {key} mismatch: expected {expected_value}, found {actual_value}")
            if manifest.get("concept_gate_applied") is not False:
                failures.append("Manifest concept_gate_applied must be false")
            if manifest.get("review_overrides_applied") is not False:
                failures.append("Manifest review_overrides_applied must be false")
    finally:
        con.close()

    print(f"snapshot_folder={snapshot_dir}")
    for filename in REQUIRED_CSVS:
        if filename in csv_counts:
            print(f"{filename}={csv_counts[filename]} rows")

    if failures:
        print("verification=FAIL")
        for failure in failures:
            print(f"  {failure}")
        raise SystemExit(1)

    print("verification=PASS")


if __name__ == "__main__":
    main()
