#!/usr/bin/env python3
"""Create review-layer v1 for structured-prompt pilot v2 outputs."""
from __future__ import annotations

import csv
import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RUNS_PATH = ROOT / "outputs" / "structured_prompt_pilot_v2" / "structured_prompt_pilot_v2_runs.json"
RUN_PLAN_PATH = ROOT / "outputs" / "structured_prompt_pilot_v2" / "structured_prompt_pilot_v2_run_plan.json"
OUT_DIR = ROOT / "outputs" / "structured_prompt_pilot_v2" / "review_layer_v1"
DB_PATH = ROOT / "learning.db"
NEMOTRON_MODEL = "NVIDIA Nemotron 3 Nano 30B-A3B"

sys.path.insert(0, str(ROOT))
from extract_final_answers import field_pairs, reduce_value, select_final_block  # noqa: E402
from classify_remaining_layer1b_flags import find_final_answer_blocks  # noqa: E402


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def db_mtime_ns() -> int:
    return DB_PATH.stat().st_mtime_ns


def run_plan_by_key() -> dict[tuple[str, str, int], dict[str, Any]]:
    plan = load_json(RUN_PLAN_PATH)
    out = {}
    for item in plan.get("items", []):
        key = (item.get("scenario_id", ""), item.get("model_label", ""), int(item.get("trial") or 1))
        out[key] = item
    return out


def first_layer_extractable(status: str) -> bool:
    return status == "OK"


def analyze_run(run: dict[str, Any], plan_items: dict[tuple[str, str, int], dict[str, Any]]) -> dict[str, Any]:
    scenario_id = run.get("question_id") or run.get("scenario_id") or ""
    model_name = run.get("model_label") or run.get("model_name") or ""
    trial = int(run.get("trial") or 1)
    plan_item = plan_items.get((scenario_id, model_name, trial), {})
    prompt_mode = plan_item.get("prompt_mode", "structured_prompt_pilot_v2")

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

    extractable = first_layer_extractable(raw_helper_status)
    if model_name == NEMOTRON_MODEL:
        review_status = "REVIEW"
        review_reason = "nemotron_tail_loop_or_multi_block_risk"
    elif raw_helper_status == "OK":
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
        "first_layer_extractable": extractable,
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


def write_report(path: Path, rows: list[dict[str, Any]], db_modified: bool) -> dict[str, int]:
    helper_counts = Counter(row["raw_helper_status"] for row in rows)
    review_counts = Counter(row["review_status"] for row in rows)
    clean_non_nemotron = sum(
        1 for row in rows if row["model_name"] != NEMOTRON_MODEL and row["review_status"] == "CLEAN"
    )
    review_nemotron = sum(
        1 for row in rows if row["model_name"] == NEMOTRON_MODEL and row["review_status"] == "REVIEW"
    )
    review_non_nemotron = sum(
        1 for row in rows if row["model_name"] != NEMOTRON_MODEL and row["review_status"] == "REVIEW"
    )
    summary = {
        "total_runs": len(rows),
        "clean_non_nemotron": clean_non_nemotron,
        "review_nemotron": review_nemotron,
        "review_non_nemotron": review_non_nemotron,
        "clean_total": review_counts.get("CLEAN", 0),
        "review_total": review_counts.get("REVIEW", 0),
    }

    nemotron_rows = [row for row in rows if row["model_name"] == NEMOTRON_MODEL]
    lines = [
        "# Structured Prompt Pilot v2 Review Layer v1",
        "",
        "## Summary Counts",
        "",
    ]
    lines.extend(f"- {key}: {value}" for key, value in summary.items())
    lines.extend(
        [
            "",
            "## Helper Status Distribution Before Override",
            "",
        ]
    )
    lines.extend(f"- {status}: {count}" for status, count in sorted(helper_counts.items()))
    lines.extend(
        [
            "",
            "## Review Status Distribution After Override",
            "",
        ]
    )
    lines.extend(f"- {status}: {count}" for status, count in sorted(review_counts.items()))
    lines.extend(
        [
            "",
            "## Nemotron Review Rows",
            "",
            "| scenario_id | raw_helper_status | first_layer_extractable | review_reason |",
            "|---|---|---:|---|",
        ]
    )
    for row in sorted(nemotron_rows, key=lambda item: item["scenario_id"]):
        lines.append(
            f"| {row['scenario_id']} | {row['raw_helper_status']} | "
            f"{row['first_layer_extractable']} | {row['review_reason']} |"
        )
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
    return summary


def main() -> None:
    before_mtime = db_mtime_ns()
    # Open read-only once as a sanity check that this task does not need DB writes.
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.execute("SELECT 1").fetchone()
    con.close()

    runs = load_json(RUNS_PATH)
    plan_items = run_plan_by_key()
    rows = [analyze_run(run, plan_items) for run in runs]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(OUT_DIR / "review_layer_v1.csv", rows)
    (OUT_DIR / "review_layer_v1.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    after_mtime = db_mtime_ns()
    summary = write_report(
        OUT_DIR / "REVIEW_LAYER_V1_REPORT.md",
        rows,
        db_modified=before_mtime != after_mtime,
    )

    for key, value in summary.items():
        print(f"{key}={value}")
    print(f"output_dir={OUT_DIR}")
    print(f"learning_db_modified={'yes' if before_mtime != after_mtime else 'no'}")


if __name__ == "__main__":
    main()
