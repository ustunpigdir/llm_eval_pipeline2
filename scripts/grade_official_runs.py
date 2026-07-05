#!/usr/bin/env python3
"""
Grade only the locked official benchmark runs.

Requires the DB to have been prepared by:
  scripts/import_official_benchmark.py

This grader differs from grade_runs.py in one important way:
it does NOT infer scenario identity from final-answer field overlap. It uses
run_scenarios.scenario_id and official_gradeable_runs.

Example:
  python3 scripts/grade_official_runs.py --db learning.db --report --csv official_grade.csv --write-db
"""
from __future__ import annotations

import argparse
import csv
import sqlite3
from collections import Counter
from pathlib import Path
import sys

# Allow running from scripts/ while importing project-level symbolic_eval.py
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from symbolic_eval import eval_value  # noqa: E402


DEFAULT_BENCHMARK_ID = "scientific_reasoning_32_v1"
METHOD_VERSION = "official_scenario_id_v1"


def near(x: float, g: float, rel: float) -> bool:
    tol = abs(g) * rel if g != 0 else rel
    return abs(x - g) <= max(tol, 1e-12)


def ensure_schema(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS grading_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            benchmark_id TEXT NOT NULL,
            run_id INTEGER NOT NULL,
            model_name TEXT,
            scenario_id TEXT NOT NULL,
            field_name TEXT NOT NULL,
            gold_value_raw TEXT,
            gold_value_num REAL,
            model_value_raw TEXT,
            model_value_num REAL,
            verdict TEXT NOT NULL,
            tolerance REAL,
            tolerance_mode TEXT,
            evaluator_note TEXT,
            method_version TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        DROP VIEW IF EXISTS grading_summary;
        CREATE VIEW grading_summary AS
        SELECT
            benchmark_id,
            model_name,
            verdict,
            COUNT(*) AS n
        FROM grading_results
        GROUP BY benchmark_id, model_name, verdict;

        DROP VIEW IF EXISTS grading_model_scores;
        CREATE VIEW grading_model_scores AS
        SELECT
            benchmark_id,
            model_name,
            SUM(CASE WHEN verdict = 'MATCH' THEN 1 ELSE 0 END) AS matches,
            SUM(CASE WHEN verdict IN ('MATCH','MISMATCH','REVIEW','NOT_FOUND') THEN 1 ELSE 0 END) AS total_fields,
            ROUND(
              1.0 * SUM(CASE WHEN verdict = 'MATCH' THEN 1 ELSE 0 END) /
              NULLIF(SUM(CASE WHEN verdict IN ('MATCH','MISMATCH','REVIEW','NOT_FOUND') THEN 1 ELSE 0 END), 0),
              4
            ) AS match_rate
        FROM grading_results
        GROUP BY benchmark_id, model_name;

        DROP VIEW IF EXISTS grading_scenario_scores;
        CREATE VIEW grading_scenario_scores AS
        SELECT
            benchmark_id,
            scenario_id,
            SUM(CASE WHEN verdict = 'MATCH' THEN 1 ELSE 0 END) AS matches,
            SUM(CASE WHEN verdict IN ('MATCH','MISMATCH','REVIEW','NOT_FOUND') THEN 1 ELSE 0 END) AS total_fields,
            ROUND(
              1.0 * SUM(CASE WHEN verdict = 'MATCH' THEN 1 ELSE 0 END) /
              NULLIF(SUM(CASE WHEN verdict IN ('MATCH','MISMATCH','REVIEW','NOT_FOUND') THEN 1 ELSE 0 END), 0),
              4
            ) AS match_rate
        FROM grading_results
        GROUP BY benchmark_id, scenario_id;

        DROP VIEW IF EXISTS grading_summary_by_scenario;
        CREATE VIEW grading_summary_by_scenario AS
        SELECT
            benchmark_id,
            scenario_id,
            verdict,
            COUNT(*) AS n
        FROM grading_results
        GROUP BY benchmark_id, scenario_id, verdict;

        DROP VIEW IF EXISTS grading_summary_by_model;
        CREATE VIEW grading_summary_by_model AS
        SELECT
            benchmark_id,
            model_name,
            verdict,
            COUNT(*) AS n
        FROM grading_results
        GROUP BY benchmark_id, model_name, verdict;

        DROP VIEW IF EXISTS grading_summary_overall;
        CREATE VIEW grading_summary_overall AS
        SELECT
            benchmark_id,
            verdict,
            COUNT(*) AS n
        FROM grading_results
        GROUP BY benchmark_id, verdict;
        """
    )


def load_model_values(con: sqlite3.Connection) -> dict[int, dict[str, str]]:
    values: dict[int, dict[str, str]] = {}
    for run_id, field_name, raw_value in con.execute(
        """
        SELECT run_id, field_name, raw_value
        FROM final_answer_values
        WHERE field_name IS NOT NULL
        """
    ):
        values.setdefault(run_id, {})[field_name] = raw_value
    return values


def grade(con: sqlite3.Connection, benchmark_id: str):
    model_values = load_model_values(con)
    rows = []
    states = Counter()

    run_rows = con.execute(
        """
        SELECT run_id, model_name, scenario_id
        FROM official_gradeable_runs
        ORDER BY run_id
        """
    ).fetchall()

    for run_id, model_name, scenario_id in run_rows:
        fields = model_values.get(run_id, {})
        gold_rows = con.execute(
            """
            SELECT field_name, expected_value_raw, expected_value_num, tolerance, tolerance_mode
            FROM gold_fields
            WHERE benchmark_id = ? AND scenario_id = ?
            ORDER BY field_index
            """,
            (benchmark_id, scenario_id),
        ).fetchall()

        for field_name, gold_raw, gold_num, tolerance, tolerance_mode in gold_rows:
            model_raw = fields.get(field_name)
            model_num = None
            note = "-"
            if model_raw is None:
                verdict = "NOT_FOUND"
            else:
                val, note = eval_value(model_raw)
                if val is None:
                    verdict = "REVIEW"
                else:
                    model_num = float(val)
                    if gold_num is None:
                        verdict = "REVIEW"
                        note = "gold value is non-numeric or missing"
                    elif tolerance_mode != "relative":
                        # Current historical grader used relative tolerance.
                        # Keep non-relative modes visible for reviewer until implemented.
                        verdict = "REVIEW"
                        note = f"unsupported tolerance_mode={tolerance_mode!r}"
                    elif near(model_num, float(gold_num), float(tolerance)):
                        verdict = "MATCH"
                    else:
                        verdict = "MISMATCH"

            states[verdict] += 1
            rows.append(
                {
                    "benchmark_id": benchmark_id,
                    "run_id": run_id,
                    "model_name": model_name,
                    "scenario_id": scenario_id,
                    "field_name": field_name,
                    "gold_value_raw": gold_raw,
                    "gold_value_num": gold_num,
                    "model_value_raw": model_raw,
                    "model_value_num": model_num,
                    "verdict": verdict,
                    "tolerance": tolerance,
                    "tolerance_mode": tolerance_mode,
                    "evaluator_note": note,
                    "method_version": METHOD_VERSION,
                }
            )

    return rows, states, len(run_rows)


def write_db(con: sqlite3.Connection, rows: list[dict], benchmark_id: str) -> None:
    con.execute("DELETE FROM grading_results WHERE benchmark_id = ?", (benchmark_id,))
    con.executemany(
        """
        INSERT INTO grading_results
          (benchmark_id, run_id, model_name, scenario_id, field_name,
           gold_value_raw, gold_value_num, model_value_raw, model_value_num,
           verdict, tolerance, tolerance_mode, evaluator_note, method_version, created_at)
        VALUES
          (:benchmark_id, :run_id, :model_name, :scenario_id, :field_name,
           :gold_value_raw, :gold_value_num, :model_value_raw, :model_value_num,
           :verdict, :tolerance, :tolerance_mode, :evaluator_note, :method_version,
           CURRENT_TIMESTAMP)
        """,
        rows,
    )
    con.commit()


def write_csv(path: str, rows: list[dict]) -> None:
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def print_report(rows: list[dict], states: Counter, run_count: int) -> None:
    total = sum(states.values())
    print(f"\nofficial gradeable runs: {run_count}")
    print(f"field verdicts: {total}")
    for state in ("MATCH", "MISMATCH", "REVIEW", "NOT_FOUND"):
        n = states.get(state, 0)
        pct = 100 * n / total if total else 0
        print(f"  {state:10} {n:5} ({pct:5.1f}%)")

    print("\nSample mismatches:")
    for r in [x for x in rows if x["verdict"] == "MISMATCH"][:8]:
        print(
            f"  run {r['run_id']:>3} {r['scenario_id']:<18} {r['field_name']:<24} "
            f"model={r['model_value_raw']!r} -> {r['model_value_num']} gold={r['gold_value_num']}"
        )

    print("\nSample review:")
    for r in [x for x in rows if x["verdict"] == "REVIEW"][:8]:
        print(
            f"  run {r['run_id']:>3} {r['scenario_id']:<18} {r['field_name']:<24} "
            f"model={r['model_value_raw']!r} note={r['evaluator_note']}"
        )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="learning.db")
    ap.add_argument("--benchmark-id", default=DEFAULT_BENCHMARK_ID)
    ap.add_argument("--csv")
    ap.add_argument("--write-db", action="store_true")
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    con = sqlite3.connect(args.db)
    try:
        ensure_schema(con)
        rows, states, run_count = grade(con, args.benchmark_id)
        if args.write_db:
            write_db(con, rows, args.benchmark_id)
        if args.csv:
            write_csv(args.csv, rows)
        if args.report:
            print_report(rows, states, run_count)
    finally:
        con.close()

    if args.write_db:
        print(f"\nwrote {len(rows)} rows into grading_results")
    if args.csv:
        print(f"wrote CSV: {args.csv}")


if __name__ == "__main__":
    main()
