#!/usr/bin/env python3
"""Test truncating structured-prompt outputs after the first complete final block."""
from __future__ import annotations

import csv
import json
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RUNS_PATH = ROOT / "outputs" / "structured_prompt_pilot_v2" / "structured_prompt_pilot_v2_runs.json"
OUT_DIR = ROOT / "outputs" / "structured_prompt_pilot_v2" / "truncation_test"
DB_PATH = ROOT / "learning.db"

sys.path.insert(0, str(ROOT))
from extract_final_answers import field_pairs, reduce_value, select_final_block  # noqa: E402
from classify_remaining_layer1b_flags import find_final_answer_blocks  # noqa: E402


FINAL_HEADING_RE = re.compile(r"FINAL ANSWER", re.I)
DISPLAY_ALIGNED_RE = re.compile(
    r"\\\[\s*\\begin\{aligned\}.*?\\end\{aligned\}\s*\\\]",
    re.S,
)
FIELD_RE = re.compile(r"\\mathrm\{([^}]+)\}\s*&\s*(.*?)(?=\\\\|\\end\{aligned\}|$)", re.S)

TARGET_CASES = {
    ("NVIDIA Nemotron 3 Nano 30B-A3B", "CM_FOUCAULT_001", "ALL_BLANK"),
    ("NVIDIA Nemotron 3 Nano 30B-A3B", "QI_TELEPORT_001", "ALL_BLANK"),
    ("NVIDIA Nemotron 3 Nano 30B-A3B", "SR_ROCKET_001", "NO_VALID_BLOCK"),
}


def load_runs() -> list[dict[str, Any]]:
    return json.loads(RUNS_PATH.read_text(encoding="utf-8"))


def load_gold_fields() -> dict[str, list[str]]:
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    rows = con.execute(
        """
        SELECT scenario_id, field_index, field_name
        FROM gold_fields
        ORDER BY scenario_id, field_index
        """
    ).fetchall()
    out: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        out[row["scenario_id"]].append(row["field_name"])
    con.close()
    return dict(out)


def truncate_after_first_complete_final_answer_block(text: str) -> tuple[str, bool]:
    heading = FINAL_HEADING_RE.search(text)
    if not heading:
        return text, False
    block = DISPLAY_ALIGNED_RE.search(text, heading.end())
    if not block:
        return text, False
    return text[: block.end()], True


def unlatex_field(name: str) -> str:
    return name.replace(r"\_", "_").replace(r"\,", "").strip()


def status_rank(status: str) -> int:
    if status == "OK":
        return 3
    if status == "CONFLICT":
        return 2
    return 1


def is_nemotron(model_name: str) -> bool:
    return model_name == "NVIDIA Nemotron 3 Nano 30B-A3B"


def analyze_text(text: str, expected_fields: list[str]) -> dict[str, Any]:
    final, status = select_final_block(text)
    blocks = find_final_answer_blocks(text)
    pairs = list(field_pairs(final["raw_text"])) if final else []
    field_names = [name for _, name, _ in pairs]
    value_rows = []
    numeric_count = 0
    values_present = bool(pairs)
    for _, name, raw_value in pairs:
        num, value_status = reduce_value(raw_value)
        value_rows.append(
            {
                "field_name": name,
                "raw_value": raw_value,
                "value_status": value_status,
                "value_num": num,
            }
        )
        if value_status == "NUMERIC":
            numeric_count += 1
        if raw_value is None or not raw_value.strip():
            values_present = False

    model_field_pairs = FIELD_RE.findall(text)
    all_field_names = [unlatex_field(name) for name, _ in model_field_pairs]
    field_set_matches = set(field_names) == set(expected_fields) if expected_fields else False
    field_order_matches = field_names == expected_fields if expected_fields else False
    field_name_aware_recoverable = (
        final is not None
        and field_set_matches
        and values_present
        and numeric_count == len(expected_fields)
    )

    return {
        "helper_status": status,
        "final_answer_block_count": len(blocks),
        "field_count": len(field_names),
        "numeric_field_count": numeric_count,
        "field_names": field_names,
        "all_field_names_detected": all_field_names,
        "field_order_matches_db": field_order_matches,
        "field_set_matches_db": field_set_matches,
        "values_present": values_present,
        "field_name_aware_recoverable": field_name_aware_recoverable,
        "value_rows": value_rows,
        "final_block_raw": final["raw_text"] if final else "",
    }


def diagnosis(row: dict[str, Any]) -> str:
    original = row["original_helper_status"]
    truncated = row["truncated_helper_status"]
    if not row["truncate_applied"]:
        return "no complete displayed aligned block after first FINAL ANSWER heading; unchanged"
    if status_rank(truncated) > status_rank(original):
        return f"improved from {original} to {truncated} by removing tail after first complete final block"
    if status_rank(truncated) < status_rank(original):
        return f"worsened from {original} to {truncated}; first block was less usable than later content"
    if original == "CONFLICT" and truncated == "OK":
        return "conflict resolved by dropping later duplicate/conflicting final blocks"
    if row["truncated_field_name_aware_recoverable"] and not row["field_order_matches_db"]:
        return "field names and numeric values are recoverable, but row order differs from DB order"
    return "unchanged helper status"


def snippet(text: str, limit: int = 2400) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + "\n...[truncated snippet]...\n" + text[-limit:]


def write_outputs(rows: list[dict[str, Any]], recovered: list[dict[str, Any]], inspected: list[dict[str, Any]], summary: dict[str, Any]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    csv_path = OUT_DIR / "truncation_comparison.csv"
    fieldnames = [
        "scenario_id",
        "model_name",
        "original_helper_status",
        "truncated_helper_status",
        "truncate_applied",
        "original_final_answer_block_count",
        "truncated_final_answer_block_count",
        "original_field_count",
        "truncated_field_count",
        "original_numeric_field_count",
        "truncated_numeric_field_count",
        "field_names_detected",
        "field_order_matches_db",
        "values_present_after_truncation",
        "diagnosis",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row[name] for name in fieldnames})

    (OUT_DIR / "truncation_comparison.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    with (OUT_DIR / "recovered_outputs.jsonl").open("w", encoding="utf-8") as handle:
        for item in recovered:
            handle.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")

    report_lines = [
        "# Structured Prompt v2 Truncation Test",
        "",
    ]
    for key, value in summary.items():
        report_lines.append(f"- {key}: {value}")
    report_lines.extend(["", "## Improved Or Worsened Cases", ""])
    changed = [row for row in rows if row["change"] in {"improved", "worsened"}]
    if changed:
        report_lines.extend(
            [
                "| scenario_id | model_name | original | truncated | truncate_applied | change | diagnosis |",
                "|---|---|---|---|---|---|---|",
            ]
        )
        for row in changed:
            report_lines.append(
                f"| {row['scenario_id']} | {row['model_name']} | {row['original_helper_status']} | "
                f"{row['truncated_helper_status']} | {row['truncate_applied']} | {row['change']} | {row['diagnosis']} |"
            )
    else:
        report_lines.append("No improved or worsened cases.")

    report_lines.extend(["", "## Specific Case Inspection", ""])
    for item in inspected:
        report_lines.extend(
            [
                f"### {item['scenario_id']} / {item['model_name']} / {item['original_helper_status']}",
                "",
                f"- truncated_helper_status: {item['truncated_helper_status']}",
                f"- truncate_applied: {item['truncate_applied']}",
                f"- original_blocks: {item['original_final_answer_block_count']}",
                f"- truncated_blocks: {item['truncated_final_answer_block_count']}",
                f"- field_names_detected: {', '.join(item['field_names_detected'])}",
                f"- field_order_matches_db: {item['field_order_matches_db']}",
                f"- values_present_after_truncation: {item['values_present_after_truncation']}",
                f"- diagnosis: {item['diagnosis']}",
                "",
                "#### Before Snippet",
                "",
                "```text",
                item["before_snippet"],
                "```",
                "",
                "#### After Snippet",
                "",
                "```text",
                item["after_snippet"],
                "```",
                "",
            ]
        )

    report_lines.extend(["", "## COS_CMB Field-Order Note", ""])
    report_lines.append(summary["cos_cmb_note"])
    (OUT_DIR / "TRUNCATION_TEST_REPORT.md").write_text(
        "\n".join(report_lines) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    runs = load_runs()
    gold_fields = load_gold_fields()

    rows: list[dict[str, Any]] = []
    recovered: list[dict[str, Any]] = []
    inspected: list[dict[str, Any]] = []

    for run in runs:
        scenario_id = run.get("question_id") or run.get("scenario_id")
        model_name = run.get("model_label") or run.get("model_name")
        text = run.get("response") or ""
        expected = gold_fields.get(scenario_id, [])
        truncated_text, truncate_applied = truncate_after_first_complete_final_answer_block(text)
        original = analyze_text(text, expected)
        truncated = analyze_text(truncated_text, expected)

        original_rank = status_rank(original["helper_status"])
        truncated_rank = status_rank(truncated["helper_status"])
        if truncated_rank > original_rank:
            change = "improved"
        elif truncated_rank < original_rank:
            change = "worsened"
        else:
            change = "unchanged"

        row = {
            "run_id": run.get("run_id"),
            "scenario_id": scenario_id,
            "model_name": model_name,
            "original_helper_status": original["helper_status"],
            "truncated_helper_status": truncated["helper_status"],
            "truncate_applied": truncate_applied,
            "original_final_answer_block_count": original["final_answer_block_count"],
            "truncated_final_answer_block_count": truncated["final_answer_block_count"],
            "original_field_count": original["field_count"],
            "truncated_field_count": truncated["field_count"],
            "original_numeric_field_count": original["numeric_field_count"],
            "truncated_numeric_field_count": truncated["numeric_field_count"],
            "field_names_detected": truncated["field_names"],
            "field_order_matches_db": truncated["field_order_matches_db"],
            "field_set_matches_db": truncated["field_set_matches_db"],
            "values_present_after_truncation": truncated["values_present"],
            "truncated_field_name_aware_recoverable": truncated["field_name_aware_recoverable"],
            "change": change,
        }
        row["diagnosis"] = diagnosis(row)
        rows.append(row)

        if change == "improved":
            recovered.append(
                {
                    "run_id": run.get("run_id"),
                    "scenario_id": scenario_id,
                    "model_name": model_name,
                    "original_helper_status": original["helper_status"],
                    "truncated_helper_status": truncated["helper_status"],
                    "truncated_response": truncated_text,
                }
            )

        is_target = (model_name, scenario_id, original["helper_status"]) in TARGET_CASES
        is_conflict = original["helper_status"] == "CONFLICT"
        if is_target or is_conflict:
            item = dict(row)
            item["before_snippet"] = snippet(text)
            item["after_snippet"] = snippet(truncated_text)
            inspected.append(item)

    counts = Counter(row["change"] for row in rows)
    original_status = Counter(row["original_helper_status"] for row in rows)
    truncated_status = Counter(row["truncated_helper_status"] for row in rows)
    nemotron_improved = sum(1 for row in rows if row["change"] == "improved" and is_nemotron(row["model_name"]))
    non_nemotron_worsened = sum(1 for row in rows if row["change"] == "worsened" and not is_nemotron(row["model_name"]))
    original_non_extractable = sum(1 for row in rows if row["original_helper_status"] in {"ALL_BLANK", "NO_VALID_BLOCK"})
    truncated_non_extractable = sum(1 for row in rows if row["truncated_helper_status"] in {"ALL_BLANK", "NO_VALID_BLOCK"})

    cos_rows = [
        row for row in rows
        if row["scenario_id"] == "COS_CMB_001" and row["model_name"] == "NVIDIA Nemotron 3 Nano 30B-A3B"
    ]
    cos = cos_rows[0] if cos_rows else None
    if cos:
        if cos["truncated_helper_status"] == "OK" and cos["truncated_field_name_aware_recoverable"]:
            if cos["field_order_matches_db"]:
                cos_note = (
                    "The COS_CMB_001 retained block is recoverable after truncation: all expected field names "
                    "and numeric values are present, and row order matches DB gold_fields.field_index. The original "
                    "problem was tail contamination/multiple later blocks, not field-name extraction, field order, "
                    "or numeric tolerance."
                )
            else:
                cos_note = (
                    "The COS_CMB_001 swapped number/energy-row block is recoverable by field-name-aware extraction: "
                    "all expected field names and numeric values are present. Any failure here is extractor_order_sensitive_failure, "
                    "not tail contamination, field-name extraction, or numeric tolerance."
                )
        elif cos["truncated_field_name_aware_recoverable"] and not cos["field_order_matches_db"]:
            cos_note = (
                "The COS_CMB_001 swapped number/energy-row block is recoverable by field-name-aware extraction: "
                "all expected field names and numeric values are present. Any failure here is extractor_order_sensitive_failure, "
                "not tail contamination, field-name extraction, or numeric tolerance."
            )
        else:
            cos_note = (
                "The COS_CMB_001 case did not meet field-name-aware recoverability after truncation; inspect comparison JSON for details."
            )
    else:
        cos_note = "COS_CMB_001 Nemotron case not found."

    summary = {
        "total_runs": len(rows),
        "truncate_applied_count": sum(1 for row in rows if row["truncate_applied"]),
        "original_clean_ok_count": original_status.get("OK", 0),
        "truncated_clean_ok_count": truncated_status.get("OK", 0),
        "original_recoverable_or_conflict_count": original_status.get("CONFLICT", 0),
        "truncated_recoverable_or_conflict_count": truncated_status.get("CONFLICT", 0),
        "original_non_extractable_count": original_non_extractable,
        "truncated_non_extractable_count": truncated_non_extractable,
        "improved_count": counts.get("improved", 0),
        "worsened_count": counts.get("worsened", 0),
        "unchanged_count": counts.get("unchanged", 0),
        "nemotron_improved_count": nemotron_improved,
        "non_nemotron_worsened_count": non_nemotron_worsened,
        "safety_criterion_met": (
            counts.get("improved", 0) > 0
            and counts.get("worsened", 0) == 0
            and non_nemotron_worsened == 0
        ),
        "cos_cmb_note": cos_note,
    }

    write_outputs(rows, recovered, inspected, summary)
    for key, value in summary.items():
        if key != "cos_cmb_note":
            print(f"{key}={value}")
    print(f"output_dir={OUT_DIR}")


if __name__ == "__main__":
    main()
