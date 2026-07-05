#!/usr/bin/env python3
"""Add usable-only analysis views for official benchmark results."""
from __future__ import annotations

import argparse
import sqlite3
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"


VIEW_SQL = """
CREATE VIEW IF NOT EXISTS official_usable_gradeable_runs AS
SELECT
    ogr.run_id,
    ogr.model_name,
    ogr.scenario_id
FROM official_gradeable_runs AS ogr
JOIN run_quality_status AS rqs
    ON rqs.run_id = ogr.run_id
WHERE rqs.usability_status = 'USABLE';

CREATE VIEW IF NOT EXISTS usable_grading_results AS
SELECT
    gr.*
FROM grading_results AS gr
JOIN run_quality_status AS rqs
    ON rqs.run_id = gr.run_id
WHERE rqs.usability_status = 'USABLE';

CREATE VIEW IF NOT EXISTS usable_grading_summary_overall AS
SELECT
    COUNT(*) AS total_rows,
    SUM(CASE WHEN verdict = 'MATCH' THEN 1 ELSE 0 END) AS match_count,
    SUM(CASE WHEN verdict = 'MISMATCH' THEN 1 ELSE 0 END) AS mismatch_count,
    SUM(CASE WHEN verdict = 'NOT_FOUND' THEN 1 ELSE 0 END) AS not_found_count,
    SUM(CASE WHEN verdict = 'REVIEW' THEN 1 ELSE 0 END) AS review_count,
    1.0 * SUM(CASE WHEN verdict = 'MATCH' THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0) AS match_rate_all_rows,
    1.0 * SUM(CASE WHEN verdict = 'MATCH' THEN 1 ELSE 0 END)
        / NULLIF(SUM(CASE WHEN verdict <> 'NOT_FOUND' THEN 1 ELSE 0 END), 0) AS match_rate_found_rows
FROM usable_grading_results;

CREATE VIEW IF NOT EXISTS usable_grading_summary_by_model AS
SELECT
    COALESCE(model_name, 'unknown') AS model_name,
    COUNT(*) AS total_graded_fields,
    SUM(CASE WHEN verdict = 'MATCH' THEN 1 ELSE 0 END) AS match_count,
    SUM(CASE WHEN verdict = 'MISMATCH' THEN 1 ELSE 0 END) AS mismatch_count,
    SUM(CASE WHEN verdict = 'NOT_FOUND' THEN 1 ELSE 0 END) AS not_found_count,
    SUM(CASE WHEN verdict = 'REVIEW' THEN 1 ELSE 0 END) AS review_count,
    1.0 * SUM(CASE WHEN verdict = 'MATCH' THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0) AS match_rate_all_rows,
    1.0 * SUM(CASE WHEN verdict = 'MATCH' THEN 1 ELSE 0 END)
        / NULLIF(SUM(CASE WHEN verdict <> 'NOT_FOUND' THEN 1 ELSE 0 END), 0) AS match_rate_found_rows
FROM usable_grading_results
GROUP BY COALESCE(model_name, 'unknown');

CREATE VIEW IF NOT EXISTS usable_grading_summary_by_scenario AS
SELECT
    ugr.scenario_id,
    s.title AS scenario_title,
    COUNT(*) AS total_graded_fields,
    SUM(CASE WHEN ugr.verdict = 'MATCH' THEN 1 ELSE 0 END) AS match_count,
    SUM(CASE WHEN ugr.verdict = 'MISMATCH' THEN 1 ELSE 0 END) AS mismatch_count,
    SUM(CASE WHEN ugr.verdict = 'NOT_FOUND' THEN 1 ELSE 0 END) AS not_found_count,
    SUM(CASE WHEN ugr.verdict = 'REVIEW' THEN 1 ELSE 0 END) AS review_count,
    1.0 * SUM(CASE WHEN ugr.verdict = 'MATCH' THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0) AS match_rate_all_rows,
    1.0 * SUM(CASE WHEN ugr.verdict = 'MATCH' THEN 1 ELSE 0 END)
        / NULLIF(SUM(CASE WHEN ugr.verdict <> 'NOT_FOUND' THEN 1 ELSE 0 END), 0) AS match_rate_found_rows
FROM usable_grading_results AS ugr
LEFT JOIN scenarios AS s
    ON s.scenario_id = ugr.scenario_id
GROUP BY ugr.scenario_id, s.title;

CREATE VIEW IF NOT EXISTS unusable_official_runs AS
SELECT
    ogr.run_id,
    ogr.model_name,
    ogr.scenario_id,
    rqs.quality_status,
    rqs.usability_status,
    rqs.rationale,
    rqs.source_artifact
FROM official_gradeable_runs AS ogr
JOIN run_quality_status AS rqs
    ON rqs.run_id = ogr.run_id
WHERE rqs.usability_status = 'UNUSABLE';
"""


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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    args = parser.parse_args()

    con = sqlite3.connect(args.db)
    try:
        with con:
            con.executescript(VIEW_SQL)

        official_count = count(con, "official_gradeable_runs")
        usable_official_count = count(con, "official_usable_gradeable_runs")
        unusable_official_count = count(con, "unusable_official_runs")
        grading_count = count(con, "grading_results")
        usable_grading_count = count(con, "usable_grading_results")

        print(f"official_gradeable_runs={official_count}")
        print(f"official_usable_gradeable_runs={usable_official_count}")
        print(f"unusable_official_runs={unusable_official_count}")
        print(f"grading_results={grading_count}")
        print(f"usable_grading_results={usable_grading_count}")
        print("usable_results_verdict_distribution")
        for verdict, row_count in sorted(verdict_distribution(con, "usable_grading_results").items()):
            print(f"  {verdict}={row_count}")
    finally:
        con.close()


if __name__ == "__main__":
    main()
