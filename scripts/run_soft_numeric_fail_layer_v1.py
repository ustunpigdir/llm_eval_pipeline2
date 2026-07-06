#!/usr/bin/env python3
"""Create a soft numeric fail categorization layer for structured Phase 1 rows."""
from __future__ import annotations

import csv
import json
import math
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT))
from symbolic_eval import eval_value  # noqa: E402

DB_PATH = ROOT / "learning.db"
OUT_DIR = ROOT / "outputs" / "soft_numeric_fail_layer_v1"
BENCHMARK_ID = "scientific_reasoning_32_v1"
TOLERANCE_MULTIPLIER = 1.25
EXPECTED_ROWS = 252
EXPECTED_PASS = 117
EXPECTED_FAIL = 135

AUTOGRADE_INPUTS = {
    "V2": ROOT / "outputs" / "structured_prompt_pilot_v2" / "autograde_no_bert_v1" / "structured_prompt_v2_clean_autograde.csv",
    "V3": ROOT / "outputs" / "structured_prompt_pilot_v3" / "autograde_no_bert_v1" / "structured_prompt_v3_clean_autograde.csv",
    "V4": ROOT / "outputs" / "structured_prompt_pilot_v4" / "autograde_no_bert_v1" / "structured_prompt_v4_clean_autograde.csv",
    "V5": ROOT / "outputs" / "structured_prompt_pilot_v5" / "autograde_no_bert_v1" / "structured_prompt_v5_clean_autograde.csv",
}

PROTECTED_PATHS = [
    DB_PATH,
    ROOT / "outputs" / "structured_prompt_pilot_v2" / "structured_prompt_pilot_v2_runs.json",
    ROOT / "outputs" / "structured_prompt_pilot_v3" / "structured_prompt_pilot_v3_runs.json",
    ROOT / "outputs" / "structured_prompt_pilot_v4" / "structured_prompt_pilot_v4_runs.json",
    ROOT / "outputs" / "structured_prompt_pilot_v5" / "structured_prompt_pilot_v5_runs.json",
    ROOT / "outputs" / "metric_text_artifacts_v1" / "canonical_reasoning_text_dataset.csv",
    ROOT / "outputs" / "bertscore_reasoning_only_canonical_v2" / "bertscore_reasoning_only_canonical_v2.csv",
    ROOT / "outputs" / "metric_comparison_analytics_rouge_l_v1" / "rouge_l_row_scores.csv",
    ROOT / "outputs" / "metric_comparison_analytics_chrf_v1" / "chrf_row_scores.csv",
    ROOT / "outputs" / "metric_comparison_analytics_roscoe_full_v1" / "roscoe_full_row_scores.csv",
]

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
    "soft_numeric_eligible",
    "numeric_fields_total",
    "numeric_fields_failed_original",
    "numeric_fields_passed_after_increased_tolerance",
    "non_numeric_failures_present",
    "extraction_or_format_failure_present",
    "conceptual_failure_present",
    "increased_tolerance_changed_result",
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
    "increased_abs_tolerance",
    "increased_rel_tolerance",
    "original_field_pass",
    "increased_tolerance_field_pass",
    "failure_type",
    "eligible_for_soft_numeric",
    "notes",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def path_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"exists": False}
    stat = path.stat()
    return {"exists": True, "mtime_ns": stat.st_mtime_ns, "size": stat.st_size}


def connect_ro() -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def load_gold_and_categories() -> tuple[dict[str, list[dict[str, Any]]], dict[str, str]]:
    with connect_ro() as con:
        gold_rows = con.execute(
            """
            SELECT scenario_id, field_index, field_name, expected_value_num, tolerance, tolerance_mode
            FROM gold_fields
            WHERE benchmark_id = ?
            ORDER BY scenario_id, field_index
            """,
            (BENCHMARK_ID,),
        ).fetchall()
        scenarios = con.execute("SELECT scenario_id, category FROM scenarios ORDER BY scenario_id").fetchall()
    gold: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in gold_rows:
        gold[row["scenario_id"]].append(dict(row))
    categories = {row["scenario_id"]: row["category"] for row in scenarios}
    return dict(gold), categories


def load_autograde_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for batch, path in AUTOGRADE_INPUTS.items():
        for row in read_csv(path):
            source_run_id = row.get("output_path_or_run_id", "")
            rows.append(
                {
                    **row,
                    "batch": batch,
                    "source_run_id": source_run_id,
                    "helper_status": row.get("raw_helper_status", ""),
                }
            )
    return rows


def load_metric_context() -> dict[str, dict[str, str]]:
    context: dict[str, dict[str, str]] = defaultdict(dict)
    metric_specs = [
        (
            ROOT / "outputs" / "bertscore_reasoning_only_canonical_v2" / "bertscore_reasoning_only_canonical_v2.csv",
            {"bert_f1": "bertscore_reasoning_only_v2_f1", "candidate_reference_length_ratio": "candidate_reference_length_ratio"},
        ),
        (
            ROOT / "outputs" / "metric_comparison_analytics_rouge_l_v1" / "rouge_l_row_scores.csv",
            {"rouge_l_f1": "rouge_l_f1"},
        ),
        (
            ROOT / "outputs" / "metric_comparison_analytics_chrf_v1" / "chrf_row_scores.csv",
            {"chrf_score": "chrf_score"},
        ),
        (
            ROOT / "outputs" / "metric_comparison_analytics_roscoe_full_v1" / "roscoe_full_row_scores.csv",
            {"reasoning_alignment": "roscoe_reasoning_alignment"},
        ),
    ]
    for path, mapping in metric_specs:
        if not path.exists():
            continue
        for row in read_csv(path):
            run_id = row.get("source_run_id", "")
            if not run_id:
                continue
            for source, target in mapping.items():
                context[run_id][target] = row.get(source, "")
    return dict(context)


def fstr(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float):
        if not math.isfinite(value):
            return ""
        return f"{value:.12g}"
    return str(value)


def parse_normalized_values(row: dict[str, Any]) -> dict[str, str]:
    raw = row.get("normalized_final_answer") or "{}"
    try:
        loaded = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    if not isinstance(loaded, dict):
        return {}
    return {str(k): "" if v is None else str(v) for k, v in loaded.items()}


def parse_float(raw: str) -> tuple[float | None, str]:
    if raw is None or not str(raw).strip():
        return None, "missing"
    value, note = eval_value(str(raw).strip())
    if value is None:
        return None, f"unparseable:{note}"
    if not math.isfinite(value):
        return None, "non_finite"
    return value, ""


def abs_tolerance(expected: float, tolerance: float, mode: str) -> float:
    if mode == "relative":
        return max(abs(expected) * tolerance if expected != 0 else tolerance, 1e-12)
    return tolerance


def field_failure_type(error_tags: list[str], field_name: str, original_pass: bool) -> str:
    if original_pass:
        return "none"
    field_tags = [tag for tag in error_tags if tag.startswith(f"{field_name}:")]
    if not field_tags:
        return "unknown_failed_field"
    if any(":MISMATCH" in tag for tag in field_tags):
        return "numeric_mismatch"
    if any(":NOT_FOUND" in tag for tag in field_tags):
        return "missing_field"
    if any(":UNPARSEABLE" in tag for tag in field_tags):
        return "unparseable_value"
    if any(":GOLD_NON_NUMERIC" in tag for tag in field_tags):
        return "gold_non_numeric"
    return "non_numeric_or_ambiguous"


def has_conceptual_failure(tags: list[str]) -> bool:
    hard_needles = (
        "CONCEPT",
        "CRITICAL",
        "WRONG_FORMULA",
        "SYMBOLIC",
        "UNSUPPORTED",
        "INVALID_REPAIR",
        "UNIT",
    )
    return any(any(needle in tag.upper() for needle in hard_needles) for tag in tags)


def has_extraction_or_format_failure(row: dict[str, Any], tags: list[str]) -> bool:
    if row.get("extraction_status") != "OK" or row.get("helper_status") != "OK":
        return True
    hard_bits = ("NOT_FOUND", "UNPARSEABLE", "NO_VALID_BLOCK", "FIELD_SET", "PARSER", "EXTRACTION", "MISSING")
    return any(any(bit in tag.upper() for bit in hard_bits) for tag in tags)


def summarize(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[row[key]].append(row)
    out = []
    for group_key, group_rows in sorted(groups.items()):
        original_pass = sum(1 for row in group_rows if row["original_deterministic_grade"] == "PASS")
        original_fail = sum(1 for row in group_rows if row["original_deterministic_grade"] == "FAIL")
        soft = sum(1 for row in group_rows if row["secondary_numeric_category"] == "SOFT_NUMERIC_FAIL")
        hard = sum(1 for row in group_rows if row["secondary_numeric_category"] == "HARD_FAIL")
        out.append(
            {
                key: group_key,
                "total_rows": len(group_rows),
                "original_pass_count": original_pass,
                "original_fail_count": original_fail,
                "soft_numeric_fail_count": soft,
                "hard_fail_count": hard,
                "soft_numeric_share_of_fails": round(soft / original_fail, 6) if original_fail else 0,
            }
        )
    return out


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
        numeric_failed_passed_increased = 0
        non_numeric_failures_present = False
        all_original_failed_numeric_pass_increased = True

        for gold in gold_rows:
            field_name = str(gold["field_name"])
            expected = float(gold["expected_value_num"]) if gold["expected_value_num"] is not None else None
            tolerance = float(gold["tolerance"])
            mode = str(gold["tolerance_mode"])
            raw_extracted = values.get(field_name, "")
            extracted, parse_note = parse_float(raw_extracted)
            original_abs_tol = abs_tolerance(expected, tolerance, mode) if expected is not None else math.nan
            increased_abs_tol = original_abs_tol * TOLERANCE_MULTIPLIER if math.isfinite(original_abs_tol) else math.nan
            original_rel_tol = tolerance if mode == "relative" else math.nan
            increased_rel_tol = original_rel_tol * TOLERANCE_MULTIPLIER if math.isfinite(original_rel_tol) else math.nan
            if expected is None or extracted is None:
                abs_error = math.nan
                rel_error = math.nan
                original_pass = False
                increased_pass = False
            else:
                abs_error = abs(extracted - expected)
                rel_error = abs_error / abs(expected) if expected != 0 else math.nan
                original_pass = abs_error <= original_abs_tol
                increased_pass = abs_error <= increased_abs_tol
            failure_type = field_failure_type(tags, field_name, original_pass)
            eligible_field = failure_type in {"none", "numeric_mismatch"}
            if not original_pass:
                numeric_failed_original += 1
                if failure_type == "numeric_mismatch" and increased_pass:
                    numeric_failed_passed_increased += 1
                else:
                    all_original_failed_numeric_pass_increased = False
                if failure_type != "numeric_mismatch":
                    non_numeric_failures_present = True
            notes = ""
            if parse_note:
                notes = parse_note
            elif mode == "relative":
                notes = "relative_tolerance_scaled_from_expected_value"
            else:
                notes = "absolute_tolerance"
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
                    "increased_abs_tolerance": fstr(increased_abs_tol),
                    "increased_rel_tolerance": fstr(increased_rel_tol),
                    "original_field_pass": fstr(original_pass),
                    "increased_tolerance_field_pass": fstr(increased_pass),
                    "failure_type": failure_type,
                    "eligible_for_soft_numeric": fstr(eligible_field),
                    "notes": notes,
                }
            )

        extraction_or_format_failure = has_extraction_or_format_failure(row, tags)
        conceptual_failure = has_conceptual_failure(tags)
        grade = row["deterministic_grade"]
        if grade == "PASS":
            secondary = "PASS_ORIGINAL"
            soft_eligible = False
            changed = False
            reason = "original_pass_preserved"
        else:
            soft_eligible = (
                row.get("extraction_status") == "OK"
                and row.get("helper_status") == "OK"
                and numeric_failed_original > 0
                and numeric_failed_passed_increased == numeric_failed_original
                and all_original_failed_numeric_pass_increased
                and not non_numeric_failures_present
                and not extraction_or_format_failure
                and not conceptual_failure
            )
            if soft_eligible:
                secondary = "SOFT_NUMERIC_FAIL"
                changed = True
                reason = "all_original_numeric_mismatches_pass_under_1_25x_tolerance"
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
                    reason = "numeric_mismatch_exceeds_1_25x_tolerance"

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
                "soft_numeric_eligible": fstr(soft_eligible),
                "numeric_fields_total": numeric_fields_total,
                "numeric_fields_failed_original": numeric_failed_original,
                "numeric_fields_passed_after_increased_tolerance": numeric_failed_passed_increased,
                "non_numeric_failures_present": fstr(non_numeric_failures_present),
                "extraction_or_format_failure_present": fstr(extraction_or_format_failure),
                "conceptual_failure_present": fstr(conceptual_failure),
                "increased_tolerance_changed_result": fstr(changed),
                "reason": reason,
                "bertscore_reasoning_only_v2_f1": metric_context.get("bertscore_reasoning_only_v2_f1", ""),
                "rouge_l_f1": metric_context.get("rouge_l_f1", ""),
                "chrf_score": metric_context.get("chrf_score", ""),
                "roscoe_reasoning_alignment": metric_context.get("roscoe_reasoning_alignment", ""),
                "candidate_reference_length_ratio": metric_context.get("candidate_reference_length_ratio", ""),
            }
        )

    diagnostics = {
        "input_autograde_files": {batch: str(path.relative_to(ROOT)) for batch, path in AUTOGRADE_INPUTS.items()},
        "metric_context_rows_matched": sum(1 for row in row_labels if row["bertscore_reasoning_only_v2_f1"]),
    }
    return row_labels, field_rows, diagnostics


def metric_interaction(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    metrics = [
        "bertscore_reasoning_only_v2_f1",
        "rouge_l_f1",
        "chrf_score",
        "roscoe_reasoning_alignment",
        "candidate_reference_length_ratio",
    ]
    out = []
    for category in ("PASS_ORIGINAL", "SOFT_NUMERIC_FAIL", "HARD_FAIL"):
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
        if row["secondary_numeric_category"] != "SOFT_NUMERIC_FAIL":
            continue
        details = [
            f"{field['field_name']} extracted={field['extracted_value']} expected={field['expected_value']} "
            f"abs_error={field['original_abs_error']} increased_abs_tol={field['increased_abs_tolerance']}"
            for field in fields_by_run[row["source_run_id"]]
            if field["original_field_pass"] == "false" and field["increased_tolerance_field_pass"] == "true"
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
    metrics: list[dict[str, Any]],
    diagnostics: dict[str, Any],
    protected_unchanged: bool,
) -> None:
    grades = Counter(row["original_deterministic_grade"] for row in row_labels)
    secondary = Counter(row["secondary_numeric_category"] for row in row_labels)
    changed = [row for row in row_labels if row["secondary_numeric_category"] == "SOFT_NUMERIC_FAIL"]
    hard = [row for row in row_labels if row["secondary_numeric_category"] == "HARD_FAIL"]
    field_failures = Counter(row["failure_type"] for row in field_rows if row["failure_type"] != "none")
    lines = [
        "# Soft Numeric Fail Layer v1 Report",
        "",
        "## 1. Purpose",
        "",
        "Create a post-autograde secondary label that separates strict PASS rows, near-tolerance numeric FAIL rows, and harder FAIL rows. Original deterministic PASS/FAIL labels are unchanged.",
        "",
        "## 2. Input Artifacts",
        "",
    ]
    lines.extend(f"- {batch}: {path}" for batch, path in diagnostics["input_autograde_files"].items())
    lines.extend(
        [
            "- gold_fields: learning.db opened read-only",
            "- metric context: existing BERTScore, ROUGE-L, chrF, ROSCOE row-score CSVs",
            "",
            "## 3. Original Deterministic Baseline",
            "",
            f"- total clean graded rows: {len(row_labels)}",
            f"- PASS: {grades.get('PASS', 0)}",
            f"- FAIL: {grades.get('FAIL', 0)}",
            "- REVIEW rows: excluded upstream from the source clean autograde files",
            "",
            "## 4. Tolerance Increase Definition",
            "",
            f"- tolerance_multiplier: {TOLERANCE_MULTIPLIER}",
            "- relative and absolute tolerances are multiplied by 1.25; this is not a flat 25% error allowance.",
            "",
            "## 5. Eligibility Rules",
            "",
            "- PASS rows are labeled PASS_ORIGINAL and never reclassified.",
            "- FAIL rows become SOFT_NUMERIC_FAIL only when every originally failed numeric mismatch passes under 1.25x tolerance.",
            "- Missing, unparseable, extraction, format, conceptual, symbolic, or ambiguous failures remain HARD_FAIL.",
            "",
            "## 6. Row Coverage",
            "",
            f"- scenarios represented: {len({row['scenario_id'] for row in row_labels})}",
            f"- models represented: {len({row['model_name'] for row in row_labels})}",
            f"- protected inputs unchanged: {'yes' if protected_unchanged else 'no'}",
            "",
            "## 7. Overall Results",
            "",
        ]
    )
    lines.extend(f"- {key}: {value}" for key, value in sorted(secondary.items()))
    fail_count = grades.get("FAIL", 0)
    soft_count = secondary.get("SOFT_NUMERIC_FAIL", 0)
    lines.append(f"- soft_numeric_share_of_original_fails: {soft_count / fail_count:.6f}" if fail_count else "- soft_numeric_share_of_original_fails: 0")
    lines.extend(["", "## 8. Results by Batch", "", "| batch | total | original PASS | original FAIL | soft numeric | hard fail | soft share of fails |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for row in by_batch:
        lines.append(f"| {row['batch']} | {row['total_rows']} | {row['original_pass_count']} | {row['original_fail_count']} | {row['soft_numeric_fail_count']} | {row['hard_fail_count']} | {row['soft_numeric_share_of_fails']} |")
    lines.extend(["", "## 9. Results by Scenario", "", "| scenario | total | original PASS | original FAIL | soft numeric | hard fail | soft share of fails |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for row in by_scenario:
        lines.append(f"| {row['scenario_id']} | {row['total_rows']} | {row['original_pass_count']} | {row['original_fail_count']} | {row['soft_numeric_fail_count']} | {row['hard_fail_count']} | {row['soft_numeric_share_of_fails']} |")
    lines.extend(["", "## 10. Results by Model", "", "| model | total | original PASS | original FAIL | soft numeric | hard fail | soft share of fails |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for row in by_model:
        lines.append(f"| {row['model_name']} | {row['total_rows']} | {row['original_pass_count']} | {row['original_fail_count']} | {row['soft_numeric_fail_count']} | {row['hard_fail_count']} | {row['soft_numeric_share_of_fails']} |")
    lines.extend(["", "## 11. Rows Reclassified as SOFT_NUMERIC_FAIL", ""])
    if changed:
        for row in changed:
            lines.append(f"- {row['batch']} / {row['scenario_id']} / {row['model_name']}: {row['reason']}")
    else:
        lines.append("- none")
    lines.extend(["", "## 12. Examples of HARD_FAIL Rows That Remained Hard", ""])
    for row in hard[:10]:
        lines.append(f"- {row['batch']} / {row['scenario_id']} / {row['model_name']}: {row['reason']}; tags={row['original_error_tags']}")
    lines.extend(["", "## 13. Interaction With Metric Scores", "", "| category | rows | mean BERTScore F1 | mean ROUGE-L F1 | mean chrF | mean ROSCOE reasoning_alignment |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    for row in metrics:
        lines.append(
            f"| {row['secondary_numeric_category']} | {row['row_count']} | {row['mean_bertscore_reasoning_only_v2_f1']} | "
            f"{row['mean_rouge_l_f1']} | {row['mean_chrf_score']} | {row['mean_roscoe_reasoning_alignment']} |"
        )
    lines.extend(
        [
            "",
            "## 14. Interpretation",
            "",
            "SOFT_NUMERIC_FAIL is not a pass. It means the answer failed the strict numeric comparison but all failed numeric fields pass when the original tolerance is multiplied by 1.25.",
            "",
            "## 15. Limitations",
            "",
            "- This layer only uses existing extracted final-answer fields and gold numeric metadata.",
            "- It does not evaluate conceptual reasoning or implement Phase 2 semantics.",
            "- Ambiguous or non-numeric failures are conservatively labeled HARD_FAIL.",
            "",
            "## 16. Recommended Next Categorization Layer",
            "",
            "Add a separate non-grade-changing taxonomy for missing/unparseable/format failures versus wrong-but-extractable numeric answers.",
            "",
            "## Field-Level Failure Summary",
            "",
        ]
    )
    if field_failures:
        lines.extend(f"- {key}: {value}" for key, value in sorted(field_failures.items()))
    else:
        lines.append("- none")
    (OUT_DIR / "SOFT_NUMERIC_FAIL_LAYER_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme() -> None:
    lines = [
        "# Soft Numeric Fail Layer v1",
        "",
        "This folder contains a read-only post-autograde categorization layer for structured Phase 1 hardened rows.",
        "",
        "Original deterministic PASS/FAIL grading is unchanged. PASS rows are labeled `PASS_ORIGINAL`. FAIL rows are labeled `SOFT_NUMERIC_FAIL` only if every originally failed numeric mismatch passes when the original tolerance is multiplied by 1.25; otherwise they remain `HARD_FAIL`.",
        "",
        "`+25% tolerance` means `new_tolerance = original_tolerance * 1.25`, not a flat 25% numeric error margin.",
        "",
        "Rerun with:",
        "",
        "```bash",
        ".venv/bin/python scripts/run_soft_numeric_fail_layer_v1.py",
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
    if secondary.get("PASS_ORIGINAL", 0) + secondary.get("SOFT_NUMERIC_FAIL", 0) + secondary.get("HARD_FAIL", 0) != EXPECTED_ROWS:
        raise SystemExit(f"Secondary categories do not sum to {EXPECTED_ROWS}: {dict(secondary)}")
    if secondary.get("SOFT_NUMERIC_FAIL", 0) + secondary.get("HARD_FAIL", 0) != EXPECTED_FAIL:
        raise SystemExit(f"FAIL secondary categories do not sum to {EXPECTED_FAIL}: {dict(secondary)}")

    by_grade = [
        {
            "total_rows": len(row_labels),
            "original_pass_count": grades.get("PASS", 0),
            "original_fail_count": grades.get("FAIL", 0),
            "pass_original_count": secondary.get("PASS_ORIGINAL", 0),
            "soft_numeric_fail_count": secondary.get("SOFT_NUMERIC_FAIL", 0),
            "hard_fail_count": secondary.get("HARD_FAIL", 0),
            "soft_numeric_share_of_fails": round(secondary.get("SOFT_NUMERIC_FAIL", 0) / grades.get("FAIL", 1), 6),
        }
    ]
    by_batch = summarize(row_labels, "batch")
    by_scenario = summarize(row_labels, "scenario_id")
    by_model = summarize(row_labels, "model_name")
    metric_rows = metric_interaction(row_labels)

    write_csv(OUT_DIR / "soft_numeric_fail_row_labels.csv", row_labels, ROW_FIELDS)
    write_json(OUT_DIR / "soft_numeric_fail_row_labels.json", row_labels)
    write_csv(OUT_DIR / "soft_numeric_fail_by_grade.csv", by_grade, list(by_grade[0].keys()))
    write_csv(OUT_DIR / "soft_numeric_fail_by_batch.csv", by_batch, list(by_batch[0].keys()))
    write_csv(OUT_DIR / "soft_numeric_fail_by_scenario.csv", by_scenario, list(by_scenario[0].keys()))
    write_csv(OUT_DIR / "soft_numeric_fail_by_model.csv", by_model, list(by_model[0].keys()))
    write_csv(OUT_DIR / "soft_numeric_fail_field_level.csv", field_rows, FIELD_FIELDS)
    write_changed_rows(OUT_DIR / "soft_numeric_fail_changed_rows.csv", row_labels, field_rows)

    after = {str(path.relative_to(ROOT)): path_state(path) for path in PROTECTED_PATHS}
    protected_unchanged = before == after
    manifest = {
        "artifact_name": "soft_numeric_fail_layer_v1",
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
        "tolerance_multiplier": TOLERANCE_MULTIPLIER,
        "pass_original_count": secondary.get("PASS_ORIGINAL", 0),
        "soft_numeric_fail_count": secondary.get("SOFT_NUMERIC_FAIL", 0),
        "hard_fail_count": secondary.get("HARD_FAIL", 0),
        "secondary_category_distribution": dict(sorted(secondary.items())),
        "scenario_count": len({row["scenario_id"] for row in row_labels}),
        "model_count": len({row["model_name"] for row in row_labels}),
        "review_rows_included": 0,
        "protected_input_states_before": before,
        "protected_input_states_after": after,
        "protected_inputs_unchanged": protected_unchanged,
        "diagnostics": diagnostics,
        "output_files": [
            "README.md",
            "SOFT_NUMERIC_FAIL_LAYER_REPORT.md",
            "soft_numeric_fail_row_labels.csv",
            "soft_numeric_fail_row_labels.json",
            "soft_numeric_fail_by_grade.csv",
            "soft_numeric_fail_by_batch.csv",
            "soft_numeric_fail_by_scenario.csv",
            "soft_numeric_fail_by_model.csv",
            "soft_numeric_fail_field_level.csv",
            "soft_numeric_fail_changed_rows.csv",
            "soft_numeric_fail_manifest.json",
        ],
    }
    write_json(OUT_DIR / "soft_numeric_fail_manifest.json", manifest)
    write_readme()
    write_report(row_labels, field_rows, by_grade, by_batch, by_scenario, by_model, metric_rows, diagnostics, protected_unchanged)

    print(f"row_count={len(row_labels)}")
    print(f"original_grade_distribution={json.dumps(dict(sorted(grades.items())), sort_keys=True)}")
    print(f"secondary_category_distribution={json.dumps(dict(sorted(secondary.items())), sort_keys=True)}")
    print(f"soft_numeric_share_of_original_fails={by_grade[0]['soft_numeric_share_of_fails']}")
    print(f"field_level_rows={len(field_rows)}")
    print(f"protected_inputs_unchanged={protected_unchanged}")
    print(f"output_dir={OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
