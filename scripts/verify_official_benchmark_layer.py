#!/usr/bin/env python3
"""Read-only verification for the official benchmark layer."""
from __future__ import annotations

import argparse
import csv
import sqlite3
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
LAYER1B_CSV = ROOT / "remaining_layer1b_flag_classification_v3.csv"


def scalar(con: sqlite3.Connection, sql: str) -> int:
    return int(con.execute(sql).fetchone()[0])


def table_exists(con: sqlite3.Connection, name: str) -> bool:
    row = con.execute(
        "SELECT 1 FROM sqlite_master WHERE name = ? AND type IN ('table', 'view')",
        (name,),
    ).fetchone()
    return row is not None


def count_or_zero(con: sqlite3.Connection, name: str) -> int:
    if not table_exists(con, name):
        return 0
    return scalar(con, f'SELECT COUNT(*) FROM "{name}"')


def layer1b_unusable_count() -> str:
    if not LAYER1B_CSV.exists():
        return "classification CSV not found"
    with LAYER1B_CSV.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return str(sum(1 for row in rows if row.get("classification") == "UNUSABLE"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    args = ap.parse_args()

    con = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    try:
        print("official_benchmark_layer_audit")
        print(f"db_total_runs={count_or_zero(con, 'questions')}")
        print(f"official_scenarios={count_or_zero(con, 'scenarios')}")
        print(f"benchmark_scenarios={count_or_zero(con, 'benchmark_scenarios')}")
        print(f"gold_fields={count_or_zero(con, 'gold_fields')}")
        print(f"official_gradeable_runs={count_or_zero(con, 'official_gradeable_runs')}")
        print(f"excluded_runs={count_or_zero(con, 'excluded_runs')}")
        print(f"final_answer_runs={count_or_zero(con, 'final_answer_runs')}")
        print(f"final_answer_values={count_or_zero(con, 'final_answer_values')}")
        print(f"grading_result_rows={count_or_zero(con, 'grading_results')}")

        verdicts = Counter()
        if table_exists(con, "grading_results"):
            for verdict, n in con.execute(
                "SELECT verdict, COUNT(*) FROM grading_results GROUP BY verdict ORDER BY verdict"
            ):
                verdicts[verdict] = n
        print("verdict_distribution=" + ", ".join(f"{k}:{verdicts[k]}" for k in sorted(verdicts)))

        print(f"layer1b_raw_flag_count={count_or_zero(con, 'extraction_quality_flags')}")
        print(f"layer1b_classified_unusable_count={layer1b_unusable_count()}")
    finally:
        con.close()


if __name__ == "__main__":
    main()
