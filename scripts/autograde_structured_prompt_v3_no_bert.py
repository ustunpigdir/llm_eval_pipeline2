#!/usr/bin/env python3
"""Autograde structured-prompt pilot v3 CLEAN rows without BERTScore."""
from __future__ import annotations

import csv
import json
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PILOT_NAME = "structured_prompt_pilot_v3"
RUNS_PATH = ROOT / "outputs" / PILOT_NAME / "structured_prompt_pilot_v3_runs.json"
REVIEW_CSV = ROOT / "outputs" / PILOT_NAME / "review_layer_v1" / "review_layer_v1.csv"
REVIEW_JSON = ROOT / "outputs" / PILOT_NAME / "review_layer_v1" / "review_layer_v1.json"
OUT_DIR = ROOT / "outputs" / PILOT_NAME / "autograde_no_bert_v1"
DB_PATH = ROOT / "learning.db"
BENCHMARK_ID = "scientific_reasoning_32_v1"

sys.path.insert(0, str(ROOT))
from extract_final_answers import field_pairs, select_final_block  # noqa: E402
from symbolic_eval import eval_value  # noqa: E402


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_review_rows() -> list[dict[str, Any]]:
    with REVIEW_CSV.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_runs_by_id() -> dict[str, dict[str, Any]]:
    return {run["run_id"]: run for run in load_json(RUNS_PATH)}


def connect_ro() -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def load_gold_fields(con: sqlite3.Connection) -> dict[str, list[sqlite3.Row]]:
    rows = con.execute(
        """
        SELECT scenario_id, field_index, field_name, expected_value_raw, expected_value_num,
               tolerance, tolerance_mode
        FROM gold_fields
        WHERE benchmark_id = ?
        ORDER BY scenario_id, field_index
        """,
        (BENCHMARK_ID,),
    ).fetchall()
    out: dict[str, list[sqlite3.Row]] = defaultdict(list)
    for row in rows:
        out[row["scenario_id"]].append(row)
    return dict(out)


def near(model_value: float, gold_value: float, tolerance: float, tolerance_mode: str) -> bool:
    if tolerance_mode != "relative":
        return abs(model_value - gold_value) <= tolerance
    tol = abs(gold_value) * tolerance if gold_value != 0 else tolerance
    return abs(model_value - gold_value) <= max(tol, 1e-12)


def extract_values(response: str) -> tuple[str, dict[str, str]]:
    final, status = select_final_block(response)
    if final is None:
        return status, {}
    values = {field_name: raw_value for _, field_name, raw_value in field_pairs(final["raw_text"])}
    return status, values


def normalized_final_answer(values: dict[str, str], gold_rows: list[sqlite3.Row]) -> dict[str, str]:
    return {row["field_name"]: values.get(row["field_name"], "") for row in gold_rows}


def grade_row(review_row: dict[str, Any], run: dict[str, Any], gold_rows: list[sqlite3.Row]) -> dict[str, Any]:
    helper_status, values = extract_values(run.get("response") or "")
    normalized = normalized_final_answer(values, gold_rows)
    failed_fields: list[str] = []
    error_tags: list[str] = []
    numeric_match_count = 0
    numeric_total_count = len(gold_rows)

    for gold in gold_rows:
        field = gold["field_name"]
        raw_value = values.get(field)
        if raw_value is None or not raw_value.strip():
            failed_fields.append(field)
            error_tags.append(f"{field}:NOT_FOUND")
            continue
        model_num, note = eval_value(raw_value)
        if model_num is None:
            failed_fields.append(field)
            error_tags.append(f"{field}:UNPARSEABLE:{note}")
            continue
        gold_num = gold["expected_value_num"]
        if gold_num is None:
            failed_fields.append(field)
            error_tags.append(f"{field}:GOLD_NON_NUMERIC")
            continue
        if near(float(model_num), float(gold_num), float(gold["tolerance"]), str(gold["tolerance_mode"])):
            numeric_match_count += 1
        else:
            failed_fields.append(field)
            error_tags.append(f"{field}:MISMATCH")

    deterministic_grade = "PASS" if numeric_match_count == numeric_total_count else "FAIL"
    if not failed_fields:
        primary_failure_mode = "none"
    elif any("NOT_FOUND" in tag for tag in error_tags):
        primary_failure_mode = "missing_field"
    elif any("UNPARSEABLE" in tag for tag in error_tags):
        primary_failure_mode = "unparseable_value"
    elif any("MISMATCH" in tag for tag in error_tags):
        primary_failure_mode = "numeric_mismatch"
    else:
        primary_failure_mode = "other"

    extracted_field_names = set(values)
    gold_field_names = {row["field_name"] for row in gold_rows}
    if helper_status == "OK" and len(values) == len(gold_rows) and extracted_field_names == gold_field_names:
        extraction_status = "OK"
    elif helper_status == "OK":
        extraction_status = "FIELD_SET_MISMATCH"
    else:
        extraction_status = helper_status
    return {
        "scenario_id": review_row["scenario_id"],
        "model_name": review_row["model_name"],
        "prompt_mode": review_row["prompt_mode"],
        "raw_helper_status": review_row["raw_helper_status"],
        "review_status": review_row["review_status"],
        "field_count": int(review_row["field_count"]),
        "numeric_field_count": int(review_row["numeric_field_count"]),
        "normalized_final_answer": json.dumps(normalized, ensure_ascii=False, sort_keys=True),
        "extraction_status": extraction_status,
        "deterministic_grade": deterministic_grade,
        "numeric_match_count": numeric_match_count,
        "numeric_total_count": numeric_total_count,
        "failed_fields": ";".join(failed_fields),
        "error_tags": ";".join(error_tags),
        "primary_failure_mode": primary_failure_mode,
        "output_path_or_run_id": review_row["output_path_or_run_id"],
    }


def most_common_failure(rows: list[dict[str, Any]]) -> str:
    failures = [row["primary_failure_mode"] for row in rows if row["primary_failure_mode"] != "none"]
    if not failures:
        return "none"
    return Counter(failures).most_common(1)[0][0]


def summarize(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[row[key]].append(row)
    out = []
    for group_key, group_rows in sorted(groups.items()):
        pass_count = sum(1 for row in group_rows if row["deterministic_grade"] == "PASS")
        fail_count = len(group_rows) - pass_count
        out.append(
            {
                key: group_key,
                "clean_rows": len(group_rows),
                "pass_count": pass_count,
                "fail_count": fail_count,
                "pass_rate": round(pass_count / len(group_rows), 6) if group_rows else 0,
                "most_common_failure_mode": most_common_failure(group_rows),
            }
        )
    return out


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_report(
    autograde_rows: list[dict[str, Any]],
    scenario_summary: list[dict[str, Any]],
    model_summary: list[dict[str, Any]],
    review_rows: list[dict[str, Any]],
    db_modified: bool,
) -> None:
    grade_counts = Counter(row["deterministic_grade"] for row in autograde_rows)
    extraction_counts = Counter(row["extraction_status"] for row in autograde_rows)
    failure_counts = Counter(
        row["primary_failure_mode"] for row in autograde_rows if row["primary_failure_mode"] != "none"
    )
    pass_count = grade_counts.get("PASS", 0)
    total = len(autograde_rows)
    lines = [
        "# Structured Prompt v3 Autograde No BERT Report",
        "",
        "## Inputs",
        "",
        f"- raw_runs: {RUNS_PATH}",
        f"- review_layer_csv: {REVIEW_CSV}",
        f"- review_layer_json: {REVIEW_JSON}",
        "",
        "## Safety",
        "",
        f"- learning_db_modified: {'yes' if db_modified else 'no'}",
        "- db_backup_created: no",
        "- BERTScore was not run.",
        "",
        "## Counts",
        "",
        f"- CLEAN rows autograded: {len(autograde_rows)}",
        f"- REVIEW rows excluded: {len(review_rows)}",
        "",
        "## Extraction Status Distribution",
        "",
    ]
    lines.extend(f"- {status}: {count}" for status, count in sorted(extraction_counts.items()))
    lines.extend(["", "## Deterministic Grade Distribution", ""])
    lines.extend(f"- {grade}: {count}" for grade, count in sorted(grade_counts.items()))
    lines.extend(
        [
            f"- overall_pass_rate: {round(pass_count / total, 6) if total else 0}",
            "",
            "## Summary By Scenario",
            "",
            "| scenario_id | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for row in scenario_summary:
        lines.append(
            f"| {row['scenario_id']} | {row['clean_rows']} | {row['pass_count']} | "
            f"{row['fail_count']} | {row['pass_rate']} | {row['most_common_failure_mode']} |"
        )
    lines.extend(
        [
            "",
            "## Summary By Model",
            "",
            "| model_name | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for row in model_summary:
        lines.append(
            f"| {row['model_name']} | {row['clean_rows']} | {row['pass_count']} | "
            f"{row['fail_count']} | {row['pass_rate']} | {row['most_common_failure_mode']} |"
        )
    lines.extend(["", "## Failed Fields And Failure Tags", ""])
    if failure_counts:
        for mode, count in sorted(failure_counts.items()):
            lines.append(f"- {mode}: {count}")
        for row in autograde_rows:
            if row["deterministic_grade"] == "FAIL":
                lines.append(
                    f"- {row['scenario_id']} / {row['model_name']}: "
                    f"failed_fields={row['failed_fields']} error_tags={row['error_tags']}"
                )
    else:
        lines.append("- none")
    (OUT_DIR / "STRUCTURED_PROMPT_V3_AUTOGRADE_NO_BERT_REPORT.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    if not RUNS_PATH.exists():
        raise SystemExit(f"Missing run output file: {RUNS_PATH}")
    if not REVIEW_CSV.exists():
        raise SystemExit(f"Missing review layer file: {REVIEW_CSV}")
    before_mtime = DB_PATH.stat().st_mtime_ns
    con = connect_ro()
    gold_fields = load_gold_fields(con)
    con.close()
    review_rows = load_review_rows()
    runs_by_id = load_runs_by_id()

    clean_rows = [row for row in review_rows if row["review_status"] == "CLEAN"]
    excluded_rows = [row for row in review_rows if row["review_status"] == "REVIEW"]

    autograde_rows = []
    for row in clean_rows:
        run = runs_by_id[row["output_path_or_run_id"]]
        autograde_rows.append(grade_row(row, run, gold_fields[row["scenario_id"]]))

    scenario_summary = summarize(autograde_rows, "scenario_id")
    model_summary = summarize(autograde_rows, "model_name")
    db_modified = before_mtime != DB_PATH.stat().st_mtime_ns

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(OUT_DIR / "structured_prompt_v3_clean_autograde.csv", autograde_rows)
    (OUT_DIR / "structured_prompt_v3_clean_autograde.json").write_text(
        json.dumps(autograde_rows, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_csv(OUT_DIR / "structured_prompt_v3_summary_by_scenario.csv", scenario_summary)
    write_csv(OUT_DIR / "structured_prompt_v3_summary_by_model.csv", model_summary)
    write_csv(
        OUT_DIR / "structured_prompt_v3_review_excluded.csv",
        [
            {
                "scenario_id": row["scenario_id"],
                "model_name": row["model_name"],
                "raw_helper_status": row["raw_helper_status"],
                "review_status": row["review_status"],
                "review_reason": row["review_reason"],
                "autograded": "no",
            }
            for row in excluded_rows
        ],
    )
    write_report(autograde_rows, scenario_summary, model_summary, excluded_rows, db_modified)

    grade_counts = Counter(row["deterministic_grade"] for row in autograde_rows)
    extraction_counts = Counter(row["extraction_status"] for row in autograde_rows)
    pass_count = grade_counts.get("PASS", 0)
    total = len(autograde_rows)
    print(f"learning.db not modified" if not db_modified else "learning.db modified")
    print("db_backup_created=no")
    print(f"clean_rows_autograded={len(clean_rows)}")
    print(f"review_rows_excluded={len(excluded_rows)}")
    print("extraction_status_distribution=" + json.dumps(dict(extraction_counts), sort_keys=True))
    print("deterministic_grade_distribution=" + json.dumps(dict(grade_counts), sort_keys=True))
    print(f"overall_pass_rate={round(pass_count / total, 6) if total else 0}")
    print(f"output_dir={OUT_DIR}")


if __name__ == "__main__":
    main()
