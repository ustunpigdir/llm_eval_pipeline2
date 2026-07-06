#!/usr/bin/env python3
"""Create a +1 percentage-point numeric tolerance recategorization layer."""
from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from run_soft_numeric_fail_layer_v1 import (
    EXPECTED_FAIL,
    EXPECTED_PASS,
    EXPECTED_ROWS,
    PROTECTED_PATHS,
    ROOT,
    field_failure_type,
    fstr,
    has_conceptual_failure,
    has_extraction_or_format_failure,
    load_autograde_rows,
    load_gold_and_categories,
    load_metric_context,
    parse_float,
    parse_normalized_values,
    path_state,
    read_csv,
    write_csv,
    write_json,
)


OUT_DIR = ROOT / "outputs" / "plus_one_percentage_point_numeric_tolerance_layer_v1"
PREVIOUS_LAYER_PATH = ROOT / "outputs" / "soft_numeric_fail_layer_v1" / "soft_numeric_fail_row_labels.csv"
RELATIVE_TOLERANCE_ADDITION = 0.01

ROW_FIELDS = [
    "source_run_id",
    "batch",
    "scenario_id",
    "category",
    "model_name",
    "original_deterministic_grade",
    "original_error_tags",
    "original_failed_fields",
    "extraction_status",
    "helper_status",
    "secondary_numeric_category",
    "plus_one_pp_numeric_eligible",
    "numeric_fields_total",
    "numeric_fields_failed_original",
    "numeric_fields_passed_after_plus_one_pp",
    "non_numeric_failures_present",
    "extraction_or_format_failure_present",
    "conceptual_failure_present",
    "plus_one_pp_tolerance_changed_result",
    "reason",
    "bertscore_reasoning_only_v2_f1",
    "rouge_l_f1",
    "chrf_score",
    "roscoe_reasoning_alignment",
    "candidate_reference_length_ratio",
]

FIELD_FIELDS = [
    "source_run_id",
    "batch",
    "scenario_id",
    "category",
    "model_name",
    "field_name",
    "expected_value",
    "extracted_value",
    "original_abs_error",
    "original_rel_error",
    "original_abs_tolerance",
    "original_rel_tolerance",
    "effective_plus_one_pp_abs_tolerance",
    "effective_plus_one_pp_rel_tolerance",
    "original_field_pass",
    "plus_one_pp_field_pass",
    "failure_type",
    "eligible_for_plus_one_pp_rescue",
    "notes",
]


def original_abs_tolerance(expected: float, tolerance: float, mode: str) -> float:
    if mode == "relative":
        return max(abs(expected) * tolerance if expected != 0 else tolerance, 1e-12)
    return tolerance


def plus_one_abs_tolerance(expected: float, tolerance: float, mode: str) -> float:
    if mode == "relative":
        effective_rel = tolerance + RELATIVE_TOLERANCE_ADDITION
        return max(abs(expected) * effective_rel if expected != 0 else effective_rel, 1e-12)
    return tolerance


def previous_plus_25_count() -> int | None:
    if not PREVIOUS_LAYER_PATH.exists():
        return None
    return sum(
        1
        for row in read_csv(PREVIOUS_LAYER_PATH)
        if row.get("secondary_numeric_category") == "SOFT_NUMERIC_FAIL"
    )


def build_layer() -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    gold_by_scenario, categories = load_gold_and_categories()
    metrics = load_metric_context()
    input_rows = load_autograde_rows()
    row_labels: list[dict[str, Any]] = []
    field_rows: list[dict[str, Any]] = []

    for row in input_rows:
        scenario_id = row["scenario_id"]
        source_run_id = row["source_run_id"]
        category = categories.get(scenario_id, "")
        values = parse_normalized_values(row)
        tags = [tag.strip() for tag in (row.get("error_tags") or "").split(";") if tag.strip()]
        gold_rows = gold_by_scenario.get(scenario_id, [])
        numeric_fields_total = len(gold_rows)
        numeric_failed_original = 0
        numeric_failed_passed_plus_one = 0
        non_numeric_failures_present = False
        all_original_failed_numeric_pass_plus_one = True

        for gold in gold_rows:
            field_name = str(gold["field_name"])
            expected = float(gold["expected_value_num"]) if gold["expected_value_num"] is not None else None
            tolerance = float(gold["tolerance"])
            mode = str(gold["tolerance_mode"])
            raw_extracted = values.get(field_name, "")
            extracted, parse_note = parse_float(raw_extracted)
            original_abs_tol = original_abs_tolerance(expected, tolerance, mode) if expected is not None else math.nan
            plus_one_abs_tol = plus_one_abs_tolerance(expected, tolerance, mode) if expected is not None else math.nan
            original_rel_tol = tolerance if mode == "relative" else math.nan
            plus_one_rel_tol = tolerance + RELATIVE_TOLERANCE_ADDITION if mode == "relative" else math.nan

            if expected is None or extracted is None:
                abs_error = math.nan
                rel_error = math.nan
                original_pass = False
                plus_one_pass = False
            else:
                abs_error = abs(extracted - expected)
                rel_error = abs_error / abs(expected) if expected != 0 else math.nan
                original_pass = abs_error <= original_abs_tol
                plus_one_pass = abs_error <= plus_one_abs_tol

            failure_type = field_failure_type(tags, field_name, original_pass)
            eligible_field = failure_type in {"none", "numeric_mismatch"}
            if not original_pass:
                numeric_failed_original += 1
                if failure_type == "numeric_mismatch" and plus_one_pass:
                    numeric_failed_passed_plus_one += 1
                else:
                    all_original_failed_numeric_pass_plus_one = False
                if failure_type != "numeric_mismatch":
                    non_numeric_failures_present = True

            if parse_note:
                notes = parse_note
            elif mode == "relative":
                notes = "relative_tolerance_plus_0_01_percentage_point"
            else:
                notes = "absolute_tolerance_preserved"

            field_rows.append(
                {
                    "source_run_id": source_run_id,
                    "batch": row["batch"],
                    "scenario_id": scenario_id,
                    "category": category,
                    "model_name": row["model_name"],
                    "field_name": field_name,
                    "expected_value": fstr(expected),
                    "extracted_value": raw_extracted,
                    "original_abs_error": fstr(abs_error),
                    "original_rel_error": fstr(rel_error),
                    "original_abs_tolerance": fstr(original_abs_tol),
                    "original_rel_tolerance": fstr(original_rel_tol),
                    "effective_plus_one_pp_abs_tolerance": fstr(plus_one_abs_tol),
                    "effective_plus_one_pp_rel_tolerance": fstr(plus_one_rel_tol),
                    "original_field_pass": fstr(original_pass),
                    "plus_one_pp_field_pass": fstr(plus_one_pass),
                    "failure_type": failure_type,
                    "eligible_for_plus_one_pp_rescue": fstr(eligible_field),
                    "notes": notes,
                }
            )

        extraction_or_format_failure = has_extraction_or_format_failure(row, tags)
        conceptual_failure = has_conceptual_failure(tags)
        grade = row["deterministic_grade"]
        if grade == "PASS":
            secondary = "PASS_ORIGINAL"
            eligible = False
            changed = False
            reason = "original_pass_preserved"
        else:
            eligible = (
                row.get("extraction_status") == "OK"
                and row.get("helper_status") == "OK"
                and numeric_failed_original > 0
                and numeric_failed_passed_plus_one == numeric_failed_original
                and all_original_failed_numeric_pass_plus_one
                and not non_numeric_failures_present
                and not extraction_or_format_failure
                and not conceptual_failure
            )
            if eligible:
                secondary = "PLUS_ONE_PP_NUMERIC_RESCUE"
                changed = True
                reason = "all_original_numeric_mismatches_pass_under_plus_one_percentage_point_tolerance"
            else:
                secondary = "HARD_FAIL"
                changed = False
                if extraction_or_format_failure:
                    reason = "extraction_or_format_failure_present"
                elif conceptual_failure:
                    reason = "ambiguous_non_numeric_failure_tag"
                elif non_numeric_failures_present:
                    reason = "non_numeric_failure_present"
                elif numeric_failed_original == 0:
                    reason = "no_numeric_failed_fields"
                else:
                    reason = "numeric_mismatch_exceeds_plus_one_percentage_point_tolerance"

        metric_context = metrics.get(source_run_id, {})
        row_labels.append(
            {
                "source_run_id": source_run_id,
                "batch": row["batch"],
                "scenario_id": scenario_id,
                "category": category,
                "model_name": row["model_name"],
                "original_deterministic_grade": grade,
                "original_error_tags": row.get("error_tags", ""),
                "original_failed_fields": row.get("failed_fields", ""),
                "extraction_status": row.get("extraction_status", ""),
                "helper_status": row.get("helper_status", ""),
                "secondary_numeric_category": secondary,
                "plus_one_pp_numeric_eligible": fstr(eligible),
                "numeric_fields_total": numeric_fields_total,
                "numeric_fields_failed_original": numeric_failed_original,
                "numeric_fields_passed_after_plus_one_pp": numeric_failed_passed_plus_one,
                "non_numeric_failures_present": fstr(non_numeric_failures_present),
                "extraction_or_format_failure_present": fstr(extraction_or_format_failure),
                "conceptual_failure_present": fstr(conceptual_failure),
                "plus_one_pp_tolerance_changed_result": fstr(changed),
                "reason": reason,
                "bertscore_reasoning_only_v2_f1": metric_context.get("bertscore_reasoning_only_v2_f1", ""),
                "rouge_l_f1": metric_context.get("rouge_l_f1", ""),
                "chrf_score": metric_context.get("chrf_score", ""),
                "roscoe_reasoning_alignment": metric_context.get("roscoe_reasoning_alignment", ""),
                "candidate_reference_length_ratio": metric_context.get("candidate_reference_length_ratio", ""),
            }
        )

    diagnostics = {
        "previous_plus_25_percent_soft_numeric_count": previous_plus_25_count(),
        "previous_layer_path": str(PREVIOUS_LAYER_PATH.relative_to(ROOT)) if PREVIOUS_LAYER_PATH.exists() else "",
    }
    return row_labels, field_rows, diagnostics


def summarize(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[row[key]].append(row)
    out = []
    for group_key, group_rows in sorted(groups.items()):
        original_pass = sum(1 for row in group_rows if row["original_deterministic_grade"] == "PASS")
        original_fail = sum(1 for row in group_rows if row["original_deterministic_grade"] == "FAIL")
        rescued = sum(1 for row in group_rows if row["secondary_numeric_category"] == "PLUS_ONE_PP_NUMERIC_RESCUE")
        hard = sum(1 for row in group_rows if row["secondary_numeric_category"] == "HARD_FAIL")
        out.append(
            {
                key: group_key,
                "total_rows": len(group_rows),
                "original_pass_count": original_pass,
                "original_fail_count": original_fail,
                "plus_one_pp_numeric_rescue_count": rescued,
                "hard_fail_count": hard,
                "rescue_share_of_fails": round(rescued / original_fail, 6) if original_fail else 0,
            }
        )
    return out


def metric_interaction(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    metrics = [
        "bertscore_reasoning_only_v2_f1",
        "rouge_l_f1",
        "chrf_score",
        "roscoe_reasoning_alignment",
        "candidate_reference_length_ratio",
    ]
    out = []
    for category in ("PASS_ORIGINAL", "PLUS_ONE_PP_NUMERIC_RESCUE", "HARD_FAIL"):
        subset = [row for row in rows if row["secondary_numeric_category"] == category]
        record: dict[str, Any] = {"secondary_numeric_category": category, "row_count": len(subset)}
        for metric in metrics:
            vals = []
            for row in subset:
                try:
                    vals.append(float(row.get(metric) or ""))
                except ValueError:
                    pass
            record[f"mean_{metric}"] = round(sum(vals) / len(vals), 6) if vals else ""
        out.append(record)
    return out


def write_changed_rows(path: Path, row_labels: list[dict[str, Any]], field_rows: list[dict[str, Any]]) -> None:
    fields_by_run: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for field in field_rows:
        if field["failure_type"] == "numeric_mismatch":
            fields_by_run[field["source_run_id"]].append(field)
    changed_rows = []
    for row in row_labels:
        if row["secondary_numeric_category"] != "PLUS_ONE_PP_NUMERIC_RESCUE":
            continue
        details = [
            f"{field['field_name']} extracted={field['extracted_value']} expected={field['expected_value']} "
            f"abs_error={field['original_abs_error']} effective_abs_tol={field['effective_plus_one_pp_abs_tolerance']}"
            for field in fields_by_run[row["source_run_id"]]
            if field["original_field_pass"] == "false" and field["plus_one_pp_field_pass"] == "true"
        ]
        changed_rows.append({**row, "field_level_detail": " | ".join(details)})
    write_csv(path, changed_rows, ROW_FIELDS + ["field_level_detail"])


def write_report(
    row_labels: list[dict[str, Any]],
    field_rows: list[dict[str, Any]],
    by_grade: list[dict[str, Any]],
    by_batch: list[dict[str, Any]],
    by_scenario: list[dict[str, Any]],
    by_model: list[dict[str, Any]],
    metric_rows: list[dict[str, Any]],
    diagnostics: dict[str, Any],
    protected_unchanged: bool,
) -> None:
    grades = Counter(row["original_deterministic_grade"] for row in row_labels)
    secondary = Counter(row["secondary_numeric_category"] for row in row_labels)
    rescued = [row for row in row_labels if row["secondary_numeric_category"] == "PLUS_ONE_PP_NUMERIC_RESCUE"]
    hard = [row for row in row_labels if row["secondary_numeric_category"] == "HARD_FAIL"]
    field_failures = Counter(row["failure_type"] for row in field_rows if row["failure_type"] != "none")
    previous_count = diagnostics.get("previous_plus_25_percent_soft_numeric_count")
    lines = [
        "# +1 Percentage-Point Numeric Tolerance Layer v1 Report",
        "",
        "## 1. Purpose",
        "",
        "Create a read-only post-autograde secondary label that tests whether strict numeric FAIL rows are rescued by adding one percentage point to each original relative tolerance.",
        "",
        "## 2. Input Artifacts",
        "",
        "- structured_prompt_pilot_v2..v5 clean autograde CSVs",
        "- gold_fields from learning.db opened read-only",
        "- existing metric row-score CSVs for context",
        "",
        "## 3. Original Deterministic Baseline",
        "",
        f"- total clean graded rows: {len(row_labels)}",
        f"- PASS: {grades.get('PASS', 0)}",
        f"- FAIL: {grades.get('FAIL', 0)}",
        "- REVIEW rows: excluded upstream",
        "",
        "## 4. Difference from +25% Tolerance Multiplier Layer",
        "",
        f"- previous +25% rescued rows: {previous_count if previous_count is not None else 'not available'}",
        "- +25% changed 1% to 1.25%; this layer changes 1% to 2% and 2% to 3%.",
        "",
        "## 5. +1 Percentage-Point Tolerance Definition",
        "",
        "- effective_rel_tolerance = original_rel_tolerance + 0.01",
        "- absolute-only tolerances are preserved.",
        "",
        "## 6. Eligibility Rules",
        "",
        "- PASS rows are preserved as PASS_ORIGINAL.",
        "- FAIL rows are rescued only when all originally failed numeric mismatches pass under +1 percentage-point relative tolerance.",
        "- Missing, unparseable, extraction, format, conceptual, symbolic, formula, or ambiguous failures remain HARD_FAIL.",
        "",
        "## 7. Row Coverage",
        "",
        f"- scenarios represented: {len({row['scenario_id'] for row in row_labels})}",
        f"- models represented: {len({row['model_name'] for row in row_labels})}",
        f"- protected inputs unchanged: {'yes' if protected_unchanged else 'no'}",
        "",
        "## 8. Overall Results",
        "",
    ]
    lines.extend(f"- {key}: {value}" for key, value in sorted(secondary.items()))
    fail_count = grades.get("FAIL", 0)
    rescue_count = secondary.get("PLUS_ONE_PP_NUMERIC_RESCUE", 0)
    lines.append(f"- rescue_share_of_original_fails: {rescue_count / fail_count:.6f}" if fail_count else "- rescue_share_of_original_fails: 0")
    lines.extend(["", "## 9. Results by Batch", "", "| batch | total | original PASS | original FAIL | rescued | hard fail | rescue share |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for row in by_batch:
        lines.append(f"| {row['batch']} | {row['total_rows']} | {row['original_pass_count']} | {row['original_fail_count']} | {row['plus_one_pp_numeric_rescue_count']} | {row['hard_fail_count']} | {row['rescue_share_of_fails']} |")
    lines.extend(["", "## 10. Results by Scenario", "", "| scenario | total | original PASS | original FAIL | rescued | hard fail | rescue share |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for row in by_scenario:
        lines.append(f"| {row['scenario_id']} | {row['total_rows']} | {row['original_pass_count']} | {row['original_fail_count']} | {row['plus_one_pp_numeric_rescue_count']} | {row['hard_fail_count']} | {row['rescue_share_of_fails']} |")
    lines.extend(["", "## 11. Results by Model", "", "| model | total | original PASS | original FAIL | rescued | hard fail | rescue share |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for row in by_model:
        lines.append(f"| {row['model_name']} | {row['total_rows']} | {row['original_pass_count']} | {row['original_fail_count']} | {row['plus_one_pp_numeric_rescue_count']} | {row['hard_fail_count']} | {row['rescue_share_of_fails']} |")
    lines.extend(["", "## 12. Rows Reclassified as PLUS_ONE_PP_NUMERIC_RESCUE", ""])
    if rescued:
        for row in rescued:
            lines.append(f"- {row['batch']} / {row['scenario_id']} / {row['model_name']}: {row['reason']}")
    else:
        lines.append("- none")
    lines.extend(["", "## 13. Examples of HARD_FAIL Rows That Remained Hard", ""])
    for row in hard[:10]:
        lines.append(f"- {row['batch']} / {row['scenario_id']} / {row['model_name']}: {row['reason']}; tags={row['original_error_tags']}")
    lines.extend(
        [
            "",
            "## 14. Comparison with +25% Layer",
            "",
            f"- previous SOFT_NUMERIC_FAIL count: {previous_count if previous_count is not None else 'not available'}",
            f"- new PLUS_ONE_PP_NUMERIC_RESCUE count: {rescue_count}",
            f"- rows newly rescued by +1 percentage-point tolerance: {rescue_count}",
            "",
            "## 15. Interaction With Metric Scores",
            "",
            "| category | rows | mean BERTScore F1 | mean ROUGE-L F1 | mean chrF | mean ROSCOE reasoning_alignment |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in metric_rows:
        lines.append(
            f"| {row['secondary_numeric_category']} | {row['row_count']} | {row['mean_bertscore_reasoning_only_v2_f1']} | "
            f"{row['mean_rouge_l_f1']} | {row['mean_chrf_score']} | {row['mean_roscoe_reasoning_alignment']} |"
        )
    lines.extend(
        [
            "",
            "## 16. Interpretation",
            "",
            "PLUS_ONE_PP_NUMERIC_RESCUE is not a pass. It means the row failed strict numeric grading but every numeric failure passes after adding one percentage point to the original relative tolerance, with no independent hard-fail reason.",
            "",
            "## 17. Limitations",
            "",
            "- Uses existing normalized final-answer fields only.",
            "- Does not revisit raw outputs or evaluate conceptual reasoning.",
            "- Absolute-only tolerance fields are left unchanged.",
            "",
            "## 18. Recommended Next Categorization Layer",
            "",
            "Separate HARD_FAIL into numeric-too-far, unparseable, missing-field, and structurally invalid extraction categories.",
            "",
            "## Field-Level Failure Summary",
            "",
        ]
    )
    lines.extend(f"- {key}: {value}" for key, value in sorted(field_failures.items())) if field_failures else lines.append("- none")
    (OUT_DIR / "PLUS_ONE_PERCENTAGE_POINT_NUMERIC_TOLERANCE_LAYER_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme() -> None:
    lines = [
        "# +1 Percentage-Point Numeric Tolerance Layer v1",
        "",
        "This folder contains a read-only post-autograde categorization layer for the 252 clean structured Phase 1 hardened rows.",
        "",
        "Original deterministic PASS/FAIL grading is unchanged.",
        "",
        "This layer uses `effective_rel_tolerance = original_rel_tolerance + 0.01`, so 1% becomes 2% and 2% becomes 3%. This differs from the previous +25% multiplier layer, where 1% became only 1.25%.",
        "",
        "`PLUS_ONE_PP_NUMERIC_RESCUE` is not a pass. It means a strict FAIL was purely numeric and all failed numeric fields pass under the +1 percentage-point tolerance.",
        "",
        "Rerun with:",
        "",
        "```bash",
        ".venv/bin/python scripts/run_plus_one_percentage_point_numeric_tolerance_layer_v1.py",
        "```",
    ]
    (OUT_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    before = {str(path.relative_to(ROOT)): path_state(path) for path in PROTECTED_PATHS}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    row_labels, field_rows, diagnostics = build_layer()
    grades = Counter(row["original_deterministic_grade"] for row in row_labels)
    secondary = Counter(row["secondary_numeric_category"] for row in row_labels)

    if len(row_labels) != EXPECTED_ROWS:
        raise SystemExit(f"Expected {EXPECTED_ROWS} rows, found {len(row_labels)}")
    if grades.get("PASS", 0) != EXPECTED_PASS or grades.get("FAIL", 0) != EXPECTED_FAIL:
        raise SystemExit(f"Expected PASS={EXPECTED_PASS}, FAIL={EXPECTED_FAIL}; found {dict(grades)}")
    if secondary.get("PASS_ORIGINAL", 0) + secondary.get("PLUS_ONE_PP_NUMERIC_RESCUE", 0) + secondary.get("HARD_FAIL", 0) != EXPECTED_ROWS:
        raise SystemExit(f"Secondary categories do not sum to {EXPECTED_ROWS}: {dict(secondary)}")
    if secondary.get("PLUS_ONE_PP_NUMERIC_RESCUE", 0) + secondary.get("HARD_FAIL", 0) != EXPECTED_FAIL:
        raise SystemExit(f"FAIL secondary categories do not sum to {EXPECTED_FAIL}: {dict(secondary)}")

    by_grade = [
        {
            "total_rows": len(row_labels),
            "original_pass_count": grades.get("PASS", 0),
            "original_fail_count": grades.get("FAIL", 0),
            "pass_original_count": secondary.get("PASS_ORIGINAL", 0),
            "plus_one_pp_numeric_rescue_count": secondary.get("PLUS_ONE_PP_NUMERIC_RESCUE", 0),
            "hard_fail_count": secondary.get("HARD_FAIL", 0),
            "rescue_share_of_original_fails": round(secondary.get("PLUS_ONE_PP_NUMERIC_RESCUE", 0) / grades.get("FAIL", 1), 6),
        }
    ]
    by_batch = summarize(row_labels, "batch")
    by_scenario = summarize(row_labels, "scenario_id")
    by_model = summarize(row_labels, "model_name")
    metric_rows = metric_interaction(row_labels)

    write_csv(OUT_DIR / "plus_one_pp_numeric_row_labels.csv", row_labels, ROW_FIELDS)
    write_json(OUT_DIR / "plus_one_pp_numeric_row_labels.json", row_labels)
    write_csv(OUT_DIR / "plus_one_pp_numeric_by_grade.csv", by_grade, list(by_grade[0].keys()))
    write_csv(OUT_DIR / "plus_one_pp_numeric_by_batch.csv", by_batch, list(by_batch[0].keys()))
    write_csv(OUT_DIR / "plus_one_pp_numeric_by_scenario.csv", by_scenario, list(by_scenario[0].keys()))
    write_csv(OUT_DIR / "plus_one_pp_numeric_by_model.csv", by_model, list(by_model[0].keys()))
    write_csv(OUT_DIR / "plus_one_pp_numeric_field_level.csv", field_rows, FIELD_FIELDS)
    write_changed_rows(OUT_DIR / "plus_one_pp_numeric_changed_rows.csv", row_labels, field_rows)

    after = {str(path.relative_to(ROOT)): path_state(path) for path in PROTECTED_PATHS}
    protected_unchanged = before == after
    manifest = {
        "artifact_name": "plus_one_percentage_point_numeric_tolerance_layer_v1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "read_only": True,
        "learning_db_modified": False,
        "raw_outputs_modified": False,
        "frozen_metric_artifacts_modified": False,
        "model_calls_made": False,
        "external_llm_api_calls": False,
        "bertscore_run": False,
        "roscoe_run": False,
        "phase2_semantics_implemented": False,
        "original_clean_rows": len(row_labels),
        "original_pass_count": grades.get("PASS", 0),
        "original_fail_count": grades.get("FAIL", 0),
        "relative_tolerance_addition": RELATIVE_TOLERANCE_ADDITION,
        "pass_original_count": secondary.get("PASS_ORIGINAL", 0),
        "plus_one_pp_numeric_rescue_count": secondary.get("PLUS_ONE_PP_NUMERIC_RESCUE", 0),
        "hard_fail_count": secondary.get("HARD_FAIL", 0),
        "previous_plus_25_percent_soft_numeric_count": diagnostics.get("previous_plus_25_percent_soft_numeric_count"),
        "secondary_category_distribution": dict(sorted(secondary.items())),
        "scenario_count": len({row["scenario_id"] for row in row_labels}),
        "model_count": len({row["model_name"] for row in row_labels}),
        "review_rows_included": 0,
        "protected_input_states_before": before,
        "protected_input_states_after": after,
        "protected_inputs_unchanged": protected_unchanged,
        "output_files": [
            "README.md",
            "PLUS_ONE_PERCENTAGE_POINT_NUMERIC_TOLERANCE_LAYER_REPORT.md",
            "plus_one_pp_numeric_row_labels.csv",
            "plus_one_pp_numeric_row_labels.json",
            "plus_one_pp_numeric_by_grade.csv",
            "plus_one_pp_numeric_by_batch.csv",
            "plus_one_pp_numeric_by_scenario.csv",
            "plus_one_pp_numeric_by_model.csv",
            "plus_one_pp_numeric_field_level.csv",
            "plus_one_pp_numeric_changed_rows.csv",
            "plus_one_pp_numeric_manifest.json",
        ],
    }
    write_json(OUT_DIR / "plus_one_pp_numeric_manifest.json", manifest)
    write_readme()
    write_report(row_labels, field_rows, by_grade, by_batch, by_scenario, by_model, metric_rows, diagnostics, protected_unchanged)

    print(f"row_count={len(row_labels)}")
    print(f"original_grade_distribution={json.dumps(dict(sorted(grades.items())), sort_keys=True)}")
    print(f"secondary_category_distribution={json.dumps(dict(sorted(secondary.items())), sort_keys=True)}")
    print(f"rescue_share_of_original_fails={by_grade[0]['rescue_share_of_original_fails']}")
    print(f"previous_plus_25_percent_soft_numeric_count={diagnostics.get('previous_plus_25_percent_soft_numeric_count')}")
    print(f"field_level_rows={len(field_rows)}")
    print(f"protected_inputs_unchanged={protected_unchanged}")
    print(f"output_dir={OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
