#!/usr/bin/env python3
"""Inspect large numeric failures above 100% relative error."""
from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from typing import Any

from run_soft_numeric_fail_layer_v1 import PROTECTED_PATHS, ROOT, fstr, path_state, read_csv, write_csv, write_json


INPUT_PATH = ROOT / "outputs" / "numeric_relative_error_distribution_v1" / "numeric_relative_error_field_level.csv"
PLUS_ONE_PATH = ROOT / "outputs" / "plus_one_percentage_point_numeric_tolerance_layer_v1" / "plus_one_pp_numeric_row_labels.csv"
OUT_DIR = ROOT / "outputs" / "large_numeric_failure_gt100pct_v1"
GT100_THRESHOLD = 1.0
GT1000_THRESHOLD = 10.0
NEAR_ZERO_ABS = 1e-12

FIELD_FIELDS = [
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
    "field_name",
    "expected_value",
    "extracted_value",
    "expected_abs_value",
    "abs_error",
    "rel_error",
    "rel_error_percent",
    "signed_error",
    "signed_rel_error",
    "original_rel_tolerance",
    "original_abs_tolerance",
    "original_field_pass",
    "failure_type",
    "abs_extracted_over_expected_ratio",
    "signed_extracted_over_expected_ratio",
    "log10_abs_ratio",
    "sign_match",
    "expected_sign",
    "extracted_sign",
    "expected_is_zero_or_near_zero",
    "extracted_is_zero_or_near_zero",
    "possible_factor_2_error",
    "possible_factor_pi_error",
    "possible_factor_10_error",
    "possible_factor_100_error",
    "possible_factor_1000_error",
    "possible_reciprocal_error",
    "possible_sign_flip",
    "possible_zero_substitution",
    "possible_unit_scale_error",
    "possible_wrong_field_scale",
    "wrong_field_scale_closest_field",
    "preliminary_failure_pattern",
    "notes",
]

ROW_FIELDS = [
    "source_run_id",
    "batch",
    "scenario_id",
    "category",
    "model_name",
    "original_deterministic_grade",
    "plus_one_pp_secondary_category",
    "gt100_field_count",
    "gt1000_field_count",
    "total_numeric_fields",
    "max_rel_error",
    "median_rel_error_for_gt100_fields",
    "affected_fields",
    "primary_failure_patterns",
    "mixed_patterns_present",
    "non_numeric_failures_present",
    "extraction_or_format_failure_present",
    "conceptual_failure_present",
    "candidate_gate_suggestions",
    "bertscore_reasoning_only_v2_f1",
    "rouge_l_f1",
    "chrf_score",
    "roscoe_reasoning_alignment",
]


def safe_float(raw: Any) -> float | None:
    try:
        value = float(raw)
    except (TypeError, ValueError):
        return None
    return value if math.isfinite(value) else None


def numeric_expected_extracted(row: dict[str, str]) -> tuple[float | None, float | None]:
    expected = safe_float(row.get("expected_value"))
    extracted = safe_float(row.get("extracted_value"))
    if extracted is None and expected is not None:
        signed_error = safe_float(row.get("signed_error"))
        if signed_error is not None:
            extracted = expected + signed_error
    return expected, extracted


def sign(value: float | None) -> str:
    if value is None:
        return "unknown"
    if abs(value) <= NEAR_ZERO_ABS:
        return "zero"
    return "positive" if value > 0 else "negative"


def boolstr(value: bool) -> str:
    return "true" if value else "false"


def close_ratio(value: float | None, targets: list[float], rel_tol: float = 0.05) -> bool:
    if value is None or value <= 0:
        return False
    return any(abs(value - target) / target <= rel_tol for target in targets if target > 0)


def load_metric_context() -> dict[str, dict[str, str]]:
    specs = [
        (
            ROOT / "outputs" / "bertscore_reasoning_only_canonical_v2" / "bertscore_reasoning_only_canonical_v2.csv",
            {"bert_f1": "bertscore_reasoning_only_v2_f1"},
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
    out: dict[str, dict[str, str]] = defaultdict(dict)
    for path, mapping in specs:
        if not path.exists():
            continue
        for row in read_csv(path):
            run_id = row.get("source_run_id", "")
            for src, dst in mapping.items():
                out[run_id][dst] = row.get(src, "")
    return dict(out)


def load_plus_one_labels() -> dict[str, str]:
    if not PLUS_ONE_PATH.exists():
        return {}
    return {
        row["source_run_id"]: row.get("secondary_numeric_category", "")
        for row in read_csv(PLUS_ONE_PATH)
        if row.get("source_run_id")
    }


def row_hard_flags(source_rows: list[dict[str, str]]) -> tuple[bool, bool, bool]:
    non_numeric = any(
        row.get("failure_type") not in {"none", "numeric_mismatch"}
        for row in source_rows
        if row.get("original_field_pass") == "false"
    )
    extraction = any(
        row.get("extraction_status") != "OK"
        or row.get("helper_status") != "OK"
        or any(bit in row.get("original_error_tags", "").upper() for bit in ("NOT_FOUND", "UNPARSEABLE", "NO_VALID_BLOCK", "FIELD_SET", "PARSER", "EXTRACTION", "MISSING"))
        for row in source_rows
    )
    conceptual = any(
        any(bit in row.get("original_error_tags", "").upper() for bit in ("CONCEPT", "CRITICAL", "WRONG_FORMULA", "SYMBOLIC", "UNSUPPORTED", "INVALID_REPAIR"))
        for row in source_rows
    )
    return non_numeric, extraction, conceptual


def build_expected_lookup(source_rows: list[dict[str, str]]) -> dict[str, list[tuple[str, float]]]:
    lookup: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for row in source_rows:
        expected = safe_float(row.get("expected_value"))
        if expected is not None:
            lookup[row["source_run_id"]].append((row["field_name"], expected))
    return lookup


def closest_wrong_field(row: dict[str, str], expected_lookup: dict[str, list[tuple[str, float]]]) -> tuple[bool, str]:
    expected, extracted = numeric_expected_extracted(row)
    if extracted is None or expected is None:
        return False, ""
    own_error = abs(extracted - expected)
    best_field = ""
    best_error = own_error
    for field_name, other_expected in expected_lookup.get(row["source_run_id"], []):
        if field_name == row["field_name"]:
            continue
        err = abs(extracted - other_expected)
        if err < best_error:
            best_error = err
            best_field = field_name
    if not best_field:
        return False, ""
    # Require materially closer to another field to reduce noisy flags.
    return best_error <= max(own_error * 0.25, NEAR_ZERO_ABS), best_field


def derive_field(row: dict[str, str], expected_lookup: dict[str, list[tuple[str, float]]]) -> dict[str, Any]:
    expected, extracted = numeric_expected_extracted(row)
    rel_error = safe_float(row.get("rel_error"))
    expected_zero = expected is None or abs(expected) <= NEAR_ZERO_ABS
    extracted_zero = extracted is None or abs(extracted) <= NEAR_ZERO_ABS
    if expected is not None and extracted is not None and not expected_zero:
        signed_ratio = extracted / expected
        abs_ratio = abs(extracted) / abs(expected)
        log10_abs_ratio = math.log10(abs_ratio) if abs_ratio > 0 else math.nan
    else:
        signed_ratio = math.nan
        abs_ratio = math.nan
        log10_abs_ratio = math.nan
    expected_sign = sign(expected)
    extracted_sign = sign(extracted)
    sign_match = expected_sign == extracted_sign and expected_sign not in {"zero", "unknown"}
    factor_2 = close_ratio(abs_ratio, [2, 0.5])
    factor_pi = close_ratio(abs_ratio, [math.pi, 1 / math.pi, 2 * math.pi, 1 / (2 * math.pi)])
    factor_10 = close_ratio(abs_ratio, [10, 0.1])
    factor_100 = close_ratio(abs_ratio, [100, 0.01])
    factor_1000 = close_ratio(abs_ratio, [1000, 0.001])
    unit_scale = close_ratio(abs_ratio, [1000, 0.001, 1e6, 1e-6, 3600, 1 / 3600, 24, 1 / 24, 365.25, 1 / 365.25])
    reciprocal = False
    if expected is not None and extracted is not None and abs(expected) > NEAR_ZERO_ABS:
        reciprocal = abs(extracted - (1 / expected)) / max(abs(1 / expected), NEAR_ZERO_ABS) <= 0.05
        reciprocal = reciprocal or abs((expected * extracted) - 1) <= 0.05
    sign_flip = bool(expected is not None and extracted is not None and not sign_match and close_ratio(abs_ratio, [1], 0.05))
    zero_sub = bool(extracted_zero and not expected_zero)
    wrong_field, closest_field = closest_wrong_field(row, expected_lookup)
    if sign_flip:
        pattern = "SIGN_FLIP"
    elif zero_sub:
        pattern = "ZERO_SUBSTITUTION"
    elif reciprocal:
        pattern = "RECIPROCAL_OR_INVERSION"
    elif factor_2 or factor_pi:
        pattern = "COMMON_FACTOR_2_OR_PI"
    elif factor_10 or factor_100 or factor_1000:
        pattern = "DECIMAL_OR_POWER_OF_TEN_SCALE"
    elif unit_scale:
        pattern = "UNIT_SCALE"
    elif wrong_field:
        pattern = "WRONG_FIELD_SCALE"
    elif log10_abs_ratio is not None and math.isfinite(log10_abs_ratio) and abs(log10_abs_ratio) >= 1:
        pattern = "ORDER_OF_MAGNITUDE_GT10X"
    else:
        pattern = "LARGE_NUMERIC_GT100PCT_UNCLASSIFIED"
    notes = []
    if closest_field:
        notes.append(f"closest_other_field={closest_field}")
    if rel_error is not None and rel_error > GT1000_THRESHOLD:
        notes.append("gt1000_extreme_subset")
    return {
        **{field: row.get(field, "") for field in FIELD_FIELDS if field in row},
        "abs_extracted_over_expected_ratio": fstr(abs_ratio),
        "signed_extracted_over_expected_ratio": fstr(signed_ratio),
        "log10_abs_ratio": fstr(log10_abs_ratio),
        "sign_match": boolstr(sign_match),
        "expected_sign": expected_sign,
        "extracted_sign": extracted_sign,
        "expected_is_zero_or_near_zero": boolstr(expected_zero),
        "extracted_is_zero_or_near_zero": boolstr(extracted_zero),
        "possible_factor_2_error": boolstr(factor_2),
        "possible_factor_pi_error": boolstr(factor_pi),
        "possible_factor_10_error": boolstr(factor_10),
        "possible_factor_100_error": boolstr(factor_100),
        "possible_factor_1000_error": boolstr(factor_1000),
        "possible_reciprocal_error": boolstr(reciprocal),
        "possible_sign_flip": boolstr(sign_flip),
        "possible_zero_substitution": boolstr(zero_sub),
        "possible_unit_scale_error": boolstr(unit_scale),
        "possible_wrong_field_scale": boolstr(wrong_field),
        "wrong_field_scale_closest_field": closest_field,
        "preliminary_failure_pattern": pattern,
        "notes": ";".join(notes),
    }


def select_fields(source_rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    expected_lookup = build_expected_lookup(source_rows)
    selected = []
    for row in source_rows:
        rel_error = safe_float(row.get("rel_error"))
        if row.get("included_in_distribution") == "true" and row.get("numeric_comparison_available") == "true" and rel_error is not None and rel_error > GT100_THRESHOLD:
            selected.append(derive_field(row, expected_lookup))
    return selected


def build_row_level(source_rows: list[dict[str, str]], selected: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_run_all: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in source_rows:
        by_run_all[row["source_run_id"]].append(row)
    by_run_selected: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in selected:
        by_run_selected[row["source_run_id"]].append(row)
    plus_one = load_plus_one_labels()
    metrics = load_metric_context()
    out = []
    for run_id, rows in sorted(by_run_selected.items()):
        base = rows[0]
        all_rows = by_run_all[run_id]
        rels = [float(row["rel_error"]) for row in rows]
        patterns = sorted(set(row["preliminary_failure_pattern"] for row in rows))
        non_numeric, extraction, conceptual = row_hard_flags(all_rows)
        gate_suggestions = sorted(
            pattern_to_gate(row["preliminary_failure_pattern"])
            for row in rows
            if pattern_to_gate(row["preliminary_failure_pattern"])
        )
        metric = metrics.get(run_id, {})
        out.append(
            {
                "source_run_id": run_id,
                "batch": base["batch"],
                "scenario_id": base["scenario_id"],
                "category": base["category"],
                "model_name": base["model_name"],
                "original_deterministic_grade": base["original_deterministic_grade"],
                "plus_one_pp_secondary_category": plus_one.get(run_id, ""),
                "gt100_field_count": len(rows),
                "gt1000_field_count": sum(1 for row in rows if float(row["rel_error"]) > GT1000_THRESHOLD),
                "total_numeric_fields": len(all_rows),
                "max_rel_error": fstr(max(rels)),
                "median_rel_error_for_gt100_fields": fstr(median(rels)),
                "affected_fields": ";".join(row["field_name"] for row in rows),
                "primary_failure_patterns": ";".join(patterns),
                "mixed_patterns_present": boolstr(len(patterns) > 1),
                "non_numeric_failures_present": boolstr(non_numeric),
                "extraction_or_format_failure_present": boolstr(extraction),
                "conceptual_failure_present": boolstr(conceptual),
                "candidate_gate_suggestions": ";".join(dict.fromkeys(gate_suggestions)),
                "bertscore_reasoning_only_v2_f1": metric.get("bertscore_reasoning_only_v2_f1", ""),
                "rouge_l_f1": metric.get("rouge_l_f1", ""),
                "chrf_score": metric.get("chrf_score", ""),
                "roscoe_reasoning_alignment": metric.get("roscoe_reasoning_alignment", ""),
            }
        )
    return out


def pattern_to_gate(pattern: str) -> str:
    return {
        "SIGN_FLIP": "SIGN_FLIP_GATE",
        "ZERO_SUBSTITUTION": "ZERO_SUBSTITUTION_GATE",
        "RECIPROCAL_OR_INVERSION": "RECIPROCAL_INVERSION_GATE",
        "DECIMAL_OR_POWER_OF_TEN_SCALE": "POWER_OF_TEN_SCALE_GATE",
        "UNIT_SCALE": "UNIT_SCALE_GATE",
        "WRONG_FIELD_SCALE": "WRONG_FIELD_SCALE_GATE",
        "ORDER_OF_MAGNITUDE_GT10X": "ORDER_OF_MAGNITUDE_GATE",
    }.get(pattern, "")


def summarize_group(rows: list[dict[str, Any]], key: str, affected_output_key: str, affected_source_key: str) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[row[key]].append(row)
    out = []
    for value, group_rows in sorted(groups.items()):
        rels = [float(row["rel_error"]) for row in group_rows]
        patterns = Counter(row["preliminary_failure_pattern"] for row in group_rows)
        out.append(
            {
                key: value,
                "row_count_with_gt100_failure": len({row["source_run_id"] for row in group_rows}),
                "field_count_gt100": len(group_rows),
                "field_count_gt1000": sum(1 for row in group_rows if float(row["rel_error"]) > GT1000_THRESHOLD),
                "max_rel_error": fstr(max(rels)),
                "median_gt100_rel_error": fstr(median(rels)),
                "most_common_pattern": patterns.most_common(1)[0][0] if patterns else "",
                affected_output_key: ";".join(sorted({row[affected_source_key] for row in group_rows})),
            }
        )
    return out


def summarize_field(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[(row["scenario_id"], row["field_name"])].append(row)
    out = []
    for (scenario_id, field_name), group_rows in sorted(groups.items()):
        rels = [float(row["rel_error"]) for row in group_rows]
        patterns = Counter(row["preliminary_failure_pattern"] for row in group_rows)
        out.append(
            {
                "scenario_id": scenario_id,
                "field_name": field_name,
                "field_count_gt100": len(group_rows),
                "field_count_gt1000": sum(1 for row in group_rows if float(row["rel_error"]) > GT1000_THRESHOLD),
                "max_rel_error": fstr(max(rels)),
                "median_gt100_rel_error": fstr(median(rels)),
                "most_common_pattern": patterns.most_common(1)[0][0],
                "affected_models": ";".join(sorted({row["model_name"] for row in group_rows})),
            }
        )
    return out


def pattern_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[row["preliminary_failure_pattern"]].append(row)
    total = len(rows)
    out = []
    for pattern, group_rows in sorted(groups.items()):
        rels = [float(row["rel_error"]) for row in group_rows]
        out.append(
            {
                "preliminary_failure_pattern": pattern,
                "field_count": len(group_rows),
                "row_count": len({row["source_run_id"] for row in group_rows}),
                "share_of_gt100_fields": fstr(len(group_rows) / total if total else 0),
                "median_rel_error": fstr(median(rels)),
                "max_rel_error": fstr(max(rels)),
                "example_source_run_ids": ";".join(sorted({row["source_run_id"] for row in group_rows})[:5]),
                "example_scenarios": ";".join(sorted({row["scenario_id"] for row in group_rows})[:5]),
                "example_models": ";".join(sorted({row["model_name"] for row in group_rows})[:5]),
            }
        )
    return out


def gate_candidates(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    gate_defs = [
        ("SIGN_FLIP_GATE", "Opposite sign with approximately matching magnitude.", "expected_value, extracted_value", "possible_sign_flip == true"),
        ("ZERO_SUBSTITUTION_GATE", "Extracted value is zero or near-zero while expected is nonzero.", "expected_value, extracted_value", "possible_zero_substitution == true"),
        ("RECIPROCAL_INVERSION_GATE", "Extracted value resembles reciprocal of expected value.", "expected_value, extracted_value", "possible_reciprocal_error == true"),
        ("POWER_OF_TEN_SCALE_GATE", "Answer is near a factor of 10, 100, or 1000 away.", "ratio diagnostics", "possible_factor_10/100/1000_error == true"),
        ("UNIT_SCALE_GATE", "Answer is near common unit conversion factors.", "ratio diagnostics", "possible_unit_scale_error == true"),
        ("WRONG_FIELD_SCALE_GATE", "Extracted value is closer to another expected field in the same row.", "same-row expected values", "possible_wrong_field_scale == true"),
        ("ORDER_OF_MAGNITUDE_GATE", "Absolute log10 ratio is at least one.", "log10_abs_ratio", "abs(log10_abs_ratio) >= 1"),
        ("EXTREME_EXPLOSION_GATE", "Relative error or absolute ratio exceeds 10.", "rel_error, abs_ratio", "rel_error > 10 or abs_ratio > 10"),
    ]
    checks = {
        "SIGN_FLIP_GATE": lambda r: r["possible_sign_flip"] == "true",
        "ZERO_SUBSTITUTION_GATE": lambda r: r["possible_zero_substitution"] == "true",
        "RECIPROCAL_INVERSION_GATE": lambda r: r["possible_reciprocal_error"] == "true",
        "POWER_OF_TEN_SCALE_GATE": lambda r: r["possible_factor_10_error"] == "true" or r["possible_factor_100_error"] == "true" or r["possible_factor_1000_error"] == "true",
        "UNIT_SCALE_GATE": lambda r: r["possible_unit_scale_error"] == "true",
        "WRONG_FIELD_SCALE_GATE": lambda r: r["possible_wrong_field_scale"] == "true",
        "ORDER_OF_MAGNITUDE_GATE": lambda r: safe_float(r["log10_abs_ratio"]) is not None and abs(float(r["log10_abs_ratio"])) >= 1,
        "EXTREME_EXPLOSION_GATE": lambda r: float(r["rel_error"]) > GT1000_THRESHOLD or (safe_float(r["abs_extracted_over_expected_ratio"]) or 0) > GT1000_THRESHOLD,
    }
    out = []
    for name, description, required_inputs, condition_logic in gate_defs:
        detected = [row for row in rows if checks[name](row)]
        if name in {"ORDER_OF_MAGNITUDE_GATE", "EXTREME_EXPLOSION_GATE"}:
            risk = "low"
        elif len(detected) >= 5:
            risk = "medium"
        else:
            risk = "high"
        recommendation = "useful_candidate" if detected else "not_observed_in_current_data"
        out.append(
            {
                "gate_name": name,
                "description": description,
                "required_inputs": required_inputs,
                "condition_logic": condition_logic,
                "fields_detected_count": len(detected),
                "rows_detected_count": len({row["source_run_id"] for row in detected}),
                "likely_false_positive_risk": risk,
                "example_rows": ";".join(sorted({row["source_run_id"] for row in detected})[:5]),
                "recommendation": recommendation,
            }
        )
    return out


def metric_interaction(row_level: list[dict[str, Any]]) -> list[dict[str, Any]]:
    metrics = ["bertscore_reasoning_only_v2_f1", "rouge_l_f1", "chrf_score", "roscoe_reasoning_alignment"]
    out = []
    for metric in metrics:
        vals = []
        for row in row_level:
            value = safe_float(row.get(metric))
            if value is not None:
                vals.append(value)
        out.append(
            {
                "metric": metric,
                "rows_with_metric": len(vals),
                "mean_for_rows_with_gt100_failure": fstr(sum(vals) / len(vals) if vals else math.nan),
                "median_for_rows_with_gt100_failure": fstr(median(vals) if vals else math.nan),
            }
        )
    return out


def write_report(
    source_rows: list[dict[str, str]],
    selected: list[dict[str, Any]],
    row_level: list[dict[str, Any]],
    by_scenario: list[dict[str, Any]],
    by_model: list[dict[str, Any]],
    by_field: list[dict[str, Any]],
    by_pattern: list[dict[str, Any]],
    gates: list[dict[str, Any]],
    metric_rows: list[dict[str, Any]],
    protected_unchanged: bool,
) -> None:
    included = [row for row in source_rows if row.get("included_in_distribution") == "true"]
    gt1000 = [row for row in selected if float(row["rel_error"]) > GT1000_THRESHOLD]
    lines = [
        "# Large Numeric Failure >100% v1 Report",
        "",
        "## 1. Purpose",
        "",
        "Inspect numeric comparisons where relative error is greater than 100% to identify preliminary scenario-independent logical gates.",
        "",
        "## 2. Inputs",
        "",
        f"- input_artifact: {INPUT_PATH.relative_to(ROOT)}",
        "- optional metric/context artifacts aligned by source_run_id",
        "",
        "## 3. Definition of >100% Relative-Error Failure",
        "",
        "`abs(extracted_value - expected_value) / abs(expected_value) > 1.0`.",
        "",
        "## 4. Coverage",
        "",
        f"- source field comparisons: {len(source_rows)}",
        f"- included numeric comparisons: {len(included)}",
        f"- rows with >100% numeric failure: {len(row_level)}",
        f"- protected inputs unchanged: {'yes' if protected_unchanged else 'no'}",
        "",
        "## 5. Overall Count of >100% Failures",
        "",
        f"- gt100_field_count: {len(selected)}",
        "",
        "## 6. >1000% Extreme Subset",
        "",
        f"- gt1000_field_count: {len(gt1000)}",
        "",
        "## 7. Results by Scenario",
        "",
        "| scenario | rows | fields >100% | fields >1000% | median rel_error | pattern |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in by_scenario:
        lines.append(f"| {row['scenario_id']} | {row['row_count_with_gt100_failure']} | {row['field_count_gt100']} | {row['field_count_gt1000']} | {row['median_gt100_rel_error']} | {row['most_common_pattern']} |")
    lines.extend(["", "## 8. Results by Model", "", "| model | rows | fields >100% | fields >1000% | median rel_error | pattern |", "| --- | ---: | ---: | ---: | ---: | --- |"])
    for row in by_model:
        lines.append(f"| {row['model_name']} | {row['row_count_with_gt100_failure']} | {row['field_count_gt100']} | {row['field_count_gt1000']} | {row['median_gt100_rel_error']} | {row['most_common_pattern']} |")
    lines.extend(["", "## 9. Results by Field", "", "See `large_numeric_failure_by_field.csv`.", "", "## 10. Preliminary Failure-Pattern Taxonomy", "", "| pattern | fields | rows | median rel_error | max rel_error |", "| --- | ---: | ---: | ---: | ---: |"])
    for row in by_pattern:
        lines.append(f"| {row['preliminary_failure_pattern']} | {row['field_count']} | {row['row_count']} | {row['median_rel_error']} | {row['max_rel_error']} |")
    lines.extend(["", "## 11. Scenario-Independent Gate Candidates", "", "| gate | fields | rows | risk | recommendation |", "| --- | ---: | ---: | --- | --- |"])
    for row in gates:
        lines.append(f"| {row['gate_name']} | {row['fields_detected_count']} | {row['rows_detected_count']} | {row['likely_false_positive_risk']} | {row['recommendation']} |")
    lines.extend(["", "## 12. Extreme Examples", ""])
    for row in sorted(selected, key=lambda r: float(r["rel_error"]), reverse=True)[:10]:
        lines.append(f"- {row['batch']} / {row['scenario_id']} / {row['model_name']} / {row['field_name']}: rel_error={row['rel_error']}, pattern={row['preliminary_failure_pattern']}")
    lines.extend(["", "## 13. Interaction With Text/Reasoning Metrics", "", "| metric | rows | mean | median |", "| --- | ---: | ---: | ---: |"])
    for row in metric_rows:
        lines.append(f"| {row['metric']} | {row['rows_with_metric']} | {row['mean_for_rows_with_gt100_failure']} | {row['median_for_rows_with_gt100_failure']} |")
    lines.extend(
        [
            "",
            "## 14. Interpretation",
            "",
            "These are not tolerance-boundary failures. They are large numeric-distance cases where ratio heuristics can suggest structural mistakes, but all pattern labels are preliminary.",
            "",
            "## 15. Limitations",
            "",
            "- Ratio heuristics do not prove cause.",
            "- This layer does not change grades or implement Phase 2 semantics.",
            "- It only inspects numeric comparisons with rel_error > 1.0.",
            "",
            "## 16. Recommended Next Layer",
            "",
            "Manually audit the high-count gate candidates, then convert only robust, low-risk checks into scenario-independent diagnostic flags.",
        ]
    )
    (OUT_DIR / "LARGE_NUMERIC_FAILURE_GT100PCT_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme() -> None:
    lines = [
        "# Large Numeric Failure >100% v1",
        "",
        "This folder inspects numeric comparisons where `relative_error > 1.0`, meaning the extracted value is more than 100% away from the gold value.",
        "",
        "The derived ratio diagnostics include extracted/expected ratios, log10 magnitude ratios, sign checks, common-factor checks, reciprocal checks, unit-scale checks, and same-row wrong-field-scale checks.",
        "",
        "This does not change deterministic grading. Use `large_numeric_failure_gate_candidates.csv` to decide which preliminary gate ideas deserve manual review.",
        "",
        "Rerun with:",
        "",
        "```bash",
        ".venv/bin/python scripts/run_large_numeric_failure_gt100pct_v1.py",
        "```",
    ]
    (OUT_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    before = {str(path.relative_to(ROOT)): path_state(path) for path in PROTECTED_PATHS}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    source_rows = read_csv(INPUT_PATH)
    selected = select_fields(source_rows)
    row_level = build_row_level(source_rows, selected)
    by_scenario = summarize_group(selected, "scenario_id", "affected_models", "model_name")
    by_model = summarize_group(selected, "model_name", "affected_scenarios", "scenario_id")
    by_field = summarize_field(selected)
    by_pattern = pattern_summary(selected)
    gates = gate_candidates(selected)
    metric_rows = metric_interaction(row_level)
    extreme = sorted(selected, key=lambda row: float(row["rel_error"]), reverse=True)[:30]
    after = {str(path.relative_to(ROOT)): path_state(path) for path in PROTECTED_PATHS}
    protected_unchanged = before == after

    write_csv(OUT_DIR / "large_numeric_failure_field_level.csv", selected, FIELD_FIELDS)
    write_json(OUT_DIR / "large_numeric_failure_field_level.json", selected)
    write_csv(OUT_DIR / "large_numeric_failure_row_level.csv", row_level, ROW_FIELDS)
    write_csv(OUT_DIR / "large_numeric_failure_by_scenario.csv", by_scenario, list(by_scenario[0].keys()) if by_scenario else [])
    write_csv(OUT_DIR / "large_numeric_failure_by_model.csv", by_model, list(by_model[0].keys()) if by_model else [])
    write_csv(OUT_DIR / "large_numeric_failure_by_field.csv", by_field, list(by_field[0].keys()) if by_field else [])
    write_csv(OUT_DIR / "large_numeric_failure_by_failure_pattern.csv", by_pattern, list(by_pattern[0].keys()) if by_pattern else [])
    write_csv(OUT_DIR / "large_numeric_failure_gate_candidates.csv", gates, list(gates[0].keys()))
    write_csv(
        OUT_DIR / "large_numeric_failure_extreme_examples.csv",
        extreme,
        [
            "source_run_id",
            "batch",
            "scenario_id",
            "category",
            "model_name",
            "field_name",
            "expected_value",
            "extracted_value",
            "rel_error",
            "rel_error_percent",
            "abs_extracted_over_expected_ratio",
            "log10_abs_ratio",
            "preliminary_failure_pattern",
            "original_error_tags",
            "original_failed_fields",
        ],
    )
    write_readme()
    write_report(source_rows, selected, row_level, by_scenario, by_model, by_field, by_pattern, gates, metric_rows, protected_unchanged)

    included = sum(1 for row in source_rows if row.get("included_in_distribution") == "true")
    gt1000 = sum(1 for row in selected if float(row["rel_error"]) > GT1000_THRESHOLD)
    manifest = {
        "artifact_name": "large_numeric_failure_gt100pct_v1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "input_artifact": str(INPUT_PATH.relative_to(ROOT)),
        "read_only": True,
        "learning_db_modified": False,
        "raw_outputs_modified": False,
        "frozen_metric_artifacts_modified": False,
        "model_calls_made": False,
        "external_llm_api_calls": False,
        "bertscore_run": False,
        "roscoe_run": False,
        "phase2_semantics_implemented": False,
        "numeric_field_comparisons_total": len(source_rows),
        "numeric_field_comparisons_included": included,
        "numeric_field_comparisons_excluded": len(source_rows) - included,
        "gt100_field_count": len(selected),
        "gt1000_field_count": gt1000,
        "rows_with_gt100_failure": len(row_level),
        "source_scenario_count": len({row["scenario_id"] for row in source_rows}),
        "source_model_count": len({row["model_name"] for row in source_rows}),
        "selection_rule": "included_in_distribution == true and numeric_comparison_available == true and rel_error > 1.0",
        "gt1000_selection_rule": "rel_error > 10.0",
        "protected_input_states_before": before,
        "protected_input_states_after": after,
        "protected_inputs_unchanged": protected_unchanged,
        "output_files": [
            "README.md",
            "LARGE_NUMERIC_FAILURE_GT100PCT_REPORT.md",
            "large_numeric_failure_field_level.csv",
            "large_numeric_failure_field_level.json",
            "large_numeric_failure_row_level.csv",
            "large_numeric_failure_by_scenario.csv",
            "large_numeric_failure_by_model.csv",
            "large_numeric_failure_by_field.csv",
            "large_numeric_failure_by_failure_pattern.csv",
            "large_numeric_failure_gate_candidates.csv",
            "large_numeric_failure_extreme_examples.csv",
            "large_numeric_failure_manifest.json",
        ],
    }
    write_json(OUT_DIR / "large_numeric_failure_manifest.json", manifest)

    print(f"source_field_count={len(source_rows)}")
    print(f"included_numeric_count={included}")
    print(f"gt100_field_count={len(selected)}")
    print(f"gt1000_field_count={gt1000}")
    print(f"rows_with_gt100_failure={len(row_level)}")
    print(f"pattern_distribution={json.dumps(dict(Counter(row['preliminary_failure_pattern'] for row in selected)), sort_keys=True)}")
    print(f"protected_inputs_unchanged={protected_unchanged}")
    print(f"output_dir={OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
