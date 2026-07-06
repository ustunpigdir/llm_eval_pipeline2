#!/usr/bin/env python3
"""Create review-layer v1 for structured-prompt pilot v5 outputs."""
from __future__ import annotations

import csv
import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PILOT_NAME = "structured_prompt_pilot_v5"
RUNS_PATH = ROOT / "outputs" / PILOT_NAME / "structured_prompt_pilot_v5_runs.json"
RUN_PLAN_PATH = ROOT / "outputs" / PILOT_NAME / "structured_prompt_pilot_v5_run_plan.json"
OUT_DIR = ROOT / "outputs" / PILOT_NAME / "review_layer_v1"
DB_PATH = ROOT / "learning.db"

sys.path.insert(0, str(ROOT))
from classify_remaining_layer1b_flags import find_final_answer_blocks  # noqa: E402
from extract_final_answers import field_pairs, reduce_value, select_final_block  # noqa: E402


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def run_plan_by_key() -> dict[tuple[str, str, int], dict[str, Any]]:
    plan = load_json(RUN_PLAN_PATH)
    out = {}
    for item in plan.get("items", []):
        key = (item.get("scenario_id", ""), item.get("model_label", ""), int(item.get("trial") or 1))
        out[key] = item
    return out


def analyze_run(run: dict[str, Any], plan_items: dict[tuple[str, str, int], dict[str, Any]]) -> dict[str, Any]:
    scenario_id = run.get("question_id") or run.get("scenario_id") or ""
    model_name = run.get("model_label") or run.get("model_name") or ""
    trial = int(run.get("trial") or 1)
    plan_item = plan_items.get((scenario_id, model_name, trial), {})
    prompt_mode = plan_item.get("prompt_mode", PILOT_NAME)

    response = run.get("response") or ""
    final, raw_helper_status = select_final_block(response)
    blocks = find_final_answer_blocks(response)

    field_count = 0
    numeric_field_count = 0
    if final is not None:
        for _, _, raw_value in field_pairs(final["raw_text"]):
            field_count += 1
            _, value_status = reduce_value(raw_value)
            if value_status == "NUMERIC":
                numeric_field_count += 1

    if raw_helper_status == "OK":
        review_status = "CLEAN"
        review_reason = "clean_first_layer_ok"
    else:
        review_status = "REVIEW"
        review_reason = "non_clean_helper_status"

    return {
        "scenario_id": scenario_id,
        "model_name": model_name,
        "prompt_mode": prompt_mode,
        "raw_helper_status": raw_helper_status,
        "first_layer_extractable": raw_helper_status == "OK",
        "review_status": review_status,
        "review_reason": review_reason,
        "final_answer_block_count": len(blocks),
        "field_count": field_count,
        "numeric_field_count": numeric_field_count,
        "output_path_or_run_id": run.get("run_id") or str(RUNS_PATH),
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "scenario_id",
        "model_name",
        "prompt_mode",
        "raw_helper_status",
        "first_layer_extractable",
        "review_status",
        "review_reason",
        "final_answer_block_count",
        "field_count",
        "numeric_field_count",
        "output_path_or_run_id",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_report(path: Path, rows: list[dict[str, Any]], db_modified: bool) -> dict[str, Any]:
    helper_counts = Counter(row["raw_helper_status"] for row in rows)
    review_counts = Counter(row["review_status"] for row in rows)
    summary = {
        "total_runs": len(rows),
        "clean_total": review_counts.get("CLEAN", 0),
        "review_total": review_counts.get("REVIEW", 0),
    }
    lines = [
        "# Structured Prompt Pilot v5 Review Layer v1",
        "",
        "## Summary Counts",
        "",
    ]
    lines.extend(f"- {key}: {value}" for key, value in summary.items())
    lines.extend(["", "## Helper Status Distribution Before Review Layer", ""])
    lines.extend(f"- {status}: {count}" for status, count in sorted(helper_counts.items()))
    lines.extend(["", "## Review Status Distribution", ""])
    lines.extend(f"- {status}: {count}" for status, count in sorted(review_counts.items()))
    lines.extend(
        [
            "",
            "## Review Rows",
            "",
            "| scenario_id | model_name | raw_helper_status | first_layer_extractable | review_reason |",
            "|---|---|---|---:|---|",
        ]
    )
    for row in rows:
        if row["review_status"] == "REVIEW":
            lines.append(
                f"| {row['scenario_id']} | {row['model_name']} | {row['raw_helper_status']} | "
                f"{row['first_layer_extractable']} | {row['review_reason']} |"
            )
    if review_counts.get("REVIEW", 0) == 0:
        lines.append("| none | none | none | n/a | none |")
    lines.extend(
        [
            "",
            "## Safety Confirmations",
            "",
            "- raw_outputs_unchanged: yes",
            f"- learning_db_modified: {'yes' if db_modified else 'no'}",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"summary": summary, "helper_status_distribution": dict(helper_counts), "review_status_distribution": dict(review_counts)}


def main() -> None:
    if not RUNS_PATH.exists():
        raise SystemExit(f"Missing run output file: {RUNS_PATH}")
    before_mtime = DB_PATH.stat().st_mtime_ns
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.execute("SELECT 1").fetchone()
    con.close()

    runs = load_json(RUNS_PATH)
    if len(runs) != 64:
        raise SystemExit(f"Expected 64 v5 runs, found {len(runs)}")
    plan_items = run_plan_by_key()
    rows = [analyze_run(run, plan_items) for run in runs]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(OUT_DIR / "review_layer_v1.csv", rows)
    (OUT_DIR / "review_layer_v1.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    db_modified = before_mtime != DB_PATH.stat().st_mtime_ns
    result = write_report(OUT_DIR / "REVIEW_LAYER_V1_REPORT.md", rows, db_modified)
    for key, value in result["summary"].items():
        print(f"{key}={value}")
    print("helper_status_distribution=" + json.dumps(result["helper_status_distribution"], sort_keys=True))
    print("review_status_distribution=" + json.dumps(result["review_status_distribution"], sort_keys=True))
    print(f"learning_db_modified={'yes' if db_modified else 'no'}")
    print(f"output_dir={OUT_DIR}")


if __name__ == "__main__":
    main()
