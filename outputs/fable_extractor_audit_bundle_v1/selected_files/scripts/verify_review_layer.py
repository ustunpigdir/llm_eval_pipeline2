#!/usr/bin/env python3
"""Read-only verification for the review/correction layer."""
from __future__ import annotations

import argparse
import sqlite3
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
EXPECTED_UNUSABLE_IDS = [185, 187, 188, 256, 286, 380, 514]
EXPECTED_VERDICTS = {
    "MATCH": 1012,
    "MISMATCH": 742,
    "NOT_FOUND": 63,
    "REVIEW": 44,
}


def table_exists(con: sqlite3.Connection, name: str) -> bool:
    row = con.execute(
        "SELECT 1 FROM sqlite_master WHERE type IN ('table', 'view') AND name = ?",
        (name,),
    ).fetchone()
    return row is not None


def scalar(con: sqlite3.Connection, sql: str, params: tuple = ()) -> int:
    return int(con.execute(sql, params).fetchone()[0])


def count_or_zero(con: sqlite3.Connection, table_name: str) -> int:
    if not table_exists(con, table_name):
        return 0
    return scalar(con, f'SELECT COUNT(*) FROM "{table_name}"')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    args = parser.parse_args()

    failures: list[str] = []
    con = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    try:
        run_quality_rows = count_or_zero(con, "run_quality_status")
        usable_count = scalar(
            con,
            "SELECT COUNT(*) FROM run_quality_status WHERE usability_status = 'USABLE'",
        )
        review_count = scalar(
            con,
            "SELECT COUNT(*) FROM run_quality_status WHERE usability_status = 'REVIEW'",
        )
        unusable_count = scalar(
            con,
            "SELECT COUNT(*) FROM run_quality_status WHERE usability_status = 'UNUSABLE'",
        )
        unusable_ids = [
            int(row[0])
            for row in con.execute(
                """
                SELECT run_id
                FROM run_quality_status
                WHERE usability_status = 'UNUSABLE'
                ORDER BY run_id
                """
            )
        ]
        override_rows = count_or_zero(con, "review_overrides")
        correction_rows = count_or_zero(con, "correction_log")
        official_gradeable_runs = count_or_zero(con, "official_gradeable_runs")
        official_grading_rows = count_or_zero(con, "grading_results")

        verdicts = Counter(
            {
                verdict: count
                for verdict, count in con.execute(
                    "SELECT verdict, COUNT(*) FROM grading_results GROUP BY verdict"
                )
            }
        )

        print(f"run_quality_status_rows={run_quality_rows}")
        print(f"usable_count={usable_count}")
        print(f"review_count={review_count}")
        print(f"unusable_count={unusable_count}")
        print("unusable_run_ids=" + ", ".join(str(run_id) for run_id in unusable_ids))
        print(f"review_overrides_rows={override_rows}")
        print(f"correction_log_rows={correction_rows}")
        print(f"official_gradeable_runs={official_gradeable_runs}")
        print(f"official_grading_rows={official_grading_rows}")
        print("official_verdict_distribution")
        for verdict in sorted(verdicts):
            print(f"  {verdict}={verdicts[verdict]}")

        missing_status = scalar(
            con,
            """
            SELECT COUNT(*)
            FROM questions q
            LEFT JOIN run_quality_status rqs ON rqs.run_id = q.run_id
            WHERE rqs.run_id IS NULL
            """,
        )
        duplicate_status = scalar(
            con,
            """
            SELECT COUNT(*)
            FROM (
                SELECT run_id
                FROM run_quality_status
                GROUP BY run_id
                HAVING COUNT(*) <> 1
            )
            """,
        )
        if missing_status or duplicate_status:
            failures.append(
                "Every questions.run_id must have exactly one run_quality_status row "
                f"(missing={missing_status}, duplicate_run_ids={duplicate_status})"
            )

        if unusable_ids != EXPECTED_UNUSABLE_IDS:
            failures.append(
                "Expected unusable run IDs "
                + ", ".join(str(run_id) for run_id in EXPECTED_UNUSABLE_IDS)
                + "; found "
                + ", ".join(str(run_id) for run_id in unusable_ids)
            )

        if official_grading_rows != 1861:
            failures.append(f"grading_results should have 1861 rows, found {official_grading_rows}")

        for verdict, expected in EXPECTED_VERDICTS.items():
            actual = verdicts.get(verdict, 0)
            if actual != expected:
                failures.append(f"verdict {verdict} should be {expected}, found {actual}")
        extra_verdicts = sorted(set(verdicts) - set(EXPECTED_VERDICTS))
        if extra_verdicts:
            failures.append("Unexpected verdict(s): " + ", ".join(extra_verdicts))

        if failures:
            print("consistency=FAIL")
            for failure in failures:
                print(f"  {failure}")
            raise SystemExit(1)

        print("consistency=PASS")
    finally:
        con.close()


if __name__ == "__main__":
    main()
