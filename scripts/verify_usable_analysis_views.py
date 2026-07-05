#!/usr/bin/env python3
"""Read-only verification for usable-only benchmark analysis views."""
from __future__ import annotations

import argparse
import sqlite3
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
EXPECTED_ALL_VERDICTS = {
    "MATCH": 1012,
    "MISMATCH": 742,
    "NOT_FOUND": 63,
    "REVIEW": 44,
}


def count(con: sqlite3.Connection, table_or_view: str) -> int:
    return int(con.execute(f'SELECT COUNT(*) FROM "{table_or_view}"').fetchone()[0])


def verdict_distribution(con: sqlite3.Connection, table_or_view: str) -> Counter:
    return Counter(
        {
            verdict: row_count
            for verdict, row_count in con.execute(
                f'SELECT verdict, COUNT(*) FROM "{table_or_view}" GROUP BY verdict'
            )
        }
    )


def print_verdicts(label: str, verdicts: Counter) -> None:
    print(label)
    for verdict in sorted(verdicts):
        print(f"  {verdict}={verdicts[verdict]}")


def print_overall_summary(con: sqlite3.Connection) -> None:
    row = con.execute(
        """
        SELECT
            total_rows,
            match_count,
            mismatch_count,
            not_found_count,
            review_count,
            match_rate_all_rows,
            match_rate_found_rows
        FROM usable_grading_summary_overall
        """
    ).fetchone()
    print("usable_overall_summary")
    print(f"  total_rows={row[0]}")
    print(f"  MATCH={row[1]}")
    print(f"  MISMATCH={row[2]}")
    print(f"  NOT_FOUND={row[3]}")
    print(f"  REVIEW={row[4]}")
    print(f"  match_rate_all_rows={row[5]:.6f}")
    print(f"  match_rate_found_rows={row[6]:.6f}")


def print_model_summaries(con: sqlite3.Connection) -> None:
    print("top_model_summaries_by_found_match_rate")
    for row in con.execute(
        """
        SELECT model_name, total_rows, match_count, mismatch_count, not_found_count, review_count,
               match_rate_all_rows, match_rate_found_rows
        FROM usable_grading_summary_by_model
        ORDER BY match_rate_found_rows DESC, match_rate_all_rows DESC, model_name
        LIMIT 10
        """
    ):
        print(
            f"  {row[0]} total={row[1]} match={row[2]} mismatch={row[3]} "
            f"not_found={row[4]} review={row[5]} all_rate={row[6]:.6f} found_rate={row[7]:.6f}"
        )

    print("bottom_model_summaries_by_found_match_rate")
    for row in con.execute(
        """
        SELECT model_name, total_rows, match_count, mismatch_count, not_found_count, review_count,
               match_rate_all_rows, match_rate_found_rows
        FROM usable_grading_summary_by_model
        ORDER BY match_rate_found_rows ASC, match_rate_all_rows ASC, model_name
        LIMIT 10
        """
    ):
        print(
            f"  {row[0]} total={row[1]} match={row[2]} mismatch={row[3]} "
            f"not_found={row[4]} review={row[5]} all_rate={row[6]:.6f} found_rate={row[7]:.6f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    args = parser.parse_args()

    failures: list[str] = []
    con = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    try:
        official_count = count(con, "official_gradeable_runs")
        usable_official_count = count(con, "official_usable_gradeable_runs")
        unusable_official_count = count(con, "unusable_official_runs")
        grading_count = count(con, "grading_results")
        usable_grading_count = count(con, "usable_grading_results")
        all_verdicts = verdict_distribution(con, "grading_results")
        usable_verdicts = verdict_distribution(con, "usable_grading_results")

        print(f"official_gradeable_runs={official_count}")
        print(f"official_usable_gradeable_runs={usable_official_count}")
        print(f"unusable_official_runs={unusable_official_count}")
        print(f"grading_results={grading_count}")
        print(f"usable_grading_results={usable_grading_count}")
        print_verdicts("all_results_verdict_distribution", all_verdicts)
        print_verdicts("usable_results_verdict_distribution", usable_verdicts)
        print_overall_summary(con)
        print_model_summaries(con)

        if official_count != usable_official_count + unusable_official_count:
            failures.append(
                "official_gradeable_runs must equal official_usable_gradeable_runs + unusable_official_runs "
                f"({official_count} != {usable_official_count} + {unusable_official_count})"
            )

        unusable_rows_in_usable_results = int(
            con.execute(
                """
                SELECT COUNT(*)
                FROM usable_grading_results AS ugr
                JOIN run_quality_status AS rqs
                    ON rqs.run_id = ugr.run_id
                WHERE rqs.usability_status = 'UNUSABLE'
                """
            ).fetchone()[0]
        )
        if unusable_rows_in_usable_results:
            failures.append(
                f"usable_grading_results contains {unusable_rows_in_usable_results} row(s) for unusable runs"
            )

        if grading_count != 1861:
            failures.append(f"grading_results should still have 1861 rows, found {grading_count}")

        for verdict, expected in EXPECTED_ALL_VERDICTS.items():
            actual = all_verdicts.get(verdict, 0)
            if actual != expected:
                failures.append(f"all-results verdict {verdict} should be {expected}, found {actual}")
        extra_verdicts = sorted(set(all_verdicts) - set(EXPECTED_ALL_VERDICTS))
        if extra_verdicts:
            failures.append("Unexpected all-results verdict(s): " + ", ".join(extra_verdicts))

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
