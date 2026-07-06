#!/usr/bin/env python3
"""Build numeric relative-error distribution diagnostics for structured rows."""
from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median, pstdev
from typing import Any, Iterable

from run_plus_one_percentage_point_numeric_tolerance_layer_v1 import plus_one_abs_tolerance
from run_soft_numeric_fail_layer_v1 import (
    EXPECTED_FAIL,
    EXPECTED_PASS,
    EXPECTED_ROWS,
    PROTECTED_PATHS,
    ROOT,
    field_failure_type,
    fstr,
    load_autograde_rows,
    load_gold_and_categories,
    parse_float,
    parse_normalized_values,
    path_state,
    write_csv,
    write_json,
)


OUT_DIR = ROOT / "outputs" / "numeric_relative_error_distribution_v1"
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
    "plus_one_pp_field_pass",
    "failure_type",
    "parse_status",
    "included_in_distribution",
    "numeric_comparison_available",
    "expected_near_zero",
    "extracted_parseable",
    "notes",
]

BINS = [
    ("exact_or_zero_error", 0.0, 0.0),
    ("gt_0_to_0_1_percent", 0.0, 0.001),
    ("gt_0_1_to_0_5_percent", 0.001, 0.005),
    ("gt_0_5_to_1_percent", 0.005, 0.01),
    ("gt_1_to_1_25_percent", 0.01, 0.0125),
    ("gt_1_25_to_2_percent", 0.0125, 0.02),
    ("gt_2_to_3_percent", 0.02, 0.03),
    ("gt_3_to_5_percent", 0.03, 0.05),
    ("gt_5_to_10_percent", 0.05, 0.10),
    ("gt_10_to_25_percent", 0.10, 0.25),
    ("gt_25_to_50_percent", 0.25, 0.50),
    ("gt_50_to_100_percent", 0.50, 1.00),
    ("gt_100_to_1000_percent", 1.00, 10.00),
    ("gt_1000_percent", 10.00, math.inf),
]

PERCENTILES = [0, 1, 5, 10, 25, 50, 75, 90, 95, 99, 100]
THRESHOLDS = [0.0125, 0.02, 0.03, 0.05, 0.10, 0.25, 0.50, 1.00]


def original_abs_tolerance(expected: float, tolerance: float, mode: str) -> float:
    if mode == "relative":
        return max(abs(expected) * tolerance if expected != 0 else tolerance, NEAR_ZERO_ABS)
    return tolerance


def percentile(values: list[float], pct: float) -> float:
    if not values:
        return math.nan
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    pos = (len(ordered) - 1) * pct / 100
    lo = math.floor(pos)
    hi = math.ceil(pos)
    if lo == hi:
        return ordered[int(pos)]
    return ordered[lo] * (hi - pos) + ordered[hi] * (pos - lo)


def stats(values: list[float]) -> dict[str, Any]:
    if not values:
        return {
            "count": 0,
            "mean_rel_error": "",
            "median_rel_error": "",
            "min_rel_error": "",
            "max_rel_error": "",
            "stddev_rel_error": "",
        }
    return {
        "count": len(values),
        "mean_rel_error": fstr(mean(values)),
        "median_rel_error": fstr(median(values)),
        "min_rel_error": fstr(min(values)),
        "max_rel_error": fstr(max(values)),
        "stddev_rel_error": fstr(pstdev(values) if len(values) > 1 else 0.0),
    }


def stats_with_percentiles(name: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    values = [float(row["rel_error"]) for row in rows if row["included_in_distribution"] == "true"]
    out = {"subset": name, **stats(values)}
    for pct in PERCENTILES:
        out[f"p{pct}_rel_error"] = fstr(percentile(values, pct))
    return out


def bin_name(rel_error: float) -> str:
    if rel_error == 0:
        return "exact_or_zero_error"
    for name, lower, upper in BINS[1:]:
        if rel_error > lower and rel_error <= upper:
            return name
    return "gt_1000_percent"


def build_field_rows() -> list[dict[str, Any]]:
    gold_by_scenario, categories = load_gold_and_categories()
    rows = load_autograde_rows()
    field_rows: list[dict[str, Any]] = []
    for row in rows:
        scenario_id = row["scenario_id"]
        values = parse_normalized_values(row)
        tags = [tag.strip() for tag in (row.get("error_tags") or "").split(";") if tag.strip()]
        for gold in gold_by_scenario[scenario_id]:
            field_name = str(gold["field_name"])
            expected = float(gold["expected_value_num"]) if gold["expected_value_num"] is not None else None
            tolerance = float(gold["tolerance"])
            mode = str(gold["tolerance_mode"])
            extracted_raw = values.get(field_name, "")
            extracted, parse_note = parse_float(extracted_raw)
            expected_abs = abs(expected) if expected is not None else math.nan
            expected_near_zero = bool(expected is None or expected_abs <= NEAR_ZERO_ABS)
            extracted_parseable = extracted is not None
            numeric_available = expected is not None and extracted is not None
            if numeric_available:
                abs_error = abs(extracted - expected)
                signed_error = extracted - expected
                if expected_near_zero:
                    rel_error = math.nan
                    signed_rel_error = math.nan
                    included = False
                    notes = "expected_near_zero_relative_error_excluded"
                else:
                    rel_error = abs_error / expected_abs
                    signed_rel_error = signed_error / expected_abs
                    included = True
                    notes = "relative_error_computed"
            else:
                abs_error = math.nan
                signed_error = math.nan
                rel_error = math.nan
                signed_rel_error = math.nan
                included = False
                notes = parse_note or "numeric_comparison_unavailable"
            original_abs_tol = original_abs_tolerance(expected, tolerance, mode) if expected is not None else math.nan
            original_rel_tol = tolerance if mode == "relative" else math.nan
            plus_one_tol = plus_one_abs_tolerance(expected, tolerance, mode) if expected is not None else math.nan
            original_pass = bool(numeric_available and abs_error <= original_abs_tol)
            plus_one_pass = bool(numeric_available and abs_error <= plus_one_tol)
            failure_type = field_failure_type(tags, field_name, original_pass)
            parse_status = "OK" if extracted_parseable else (parse_note or "missing")
            field_rows.append(
                {
                    "source_run_id": row["source_run_id"],
                    "batch": row["batch"],
                    "scenario_id": scenario_id,
                    "category": categories.get(scenario_id, ""),
                    "model_name": row["model_name"],
                    "original_deterministic_grade": row["deterministic_grade"],
                    "original_error_tags": row.get("error_tags", ""),
                    "original_failed_fields": row.get("failed_fields", ""),
                    "extraction_status": row.get("extraction_status", ""),
                    "helper_status": row.get("helper_status", ""),
                    "field_name": field_name,
                    "expected_value": fstr(expected),
                    "extracted_value": extracted_raw,
                    "expected_abs_value": fstr(expected_abs),
                    "abs_error": fstr(abs_error),
                    "rel_error": fstr(rel_error),
                    "rel_error_percent": fstr(rel_error * 100 if math.isfinite(rel_error) else math.nan),
                    "signed_error": fstr(signed_error),
                    "signed_rel_error": fstr(signed_rel_error),
                    "original_rel_tolerance": fstr(original_rel_tol),
                    "original_abs_tolerance": fstr(original_abs_tol),
                    "original_field_pass": fstr(original_pass),
                    "plus_one_pp_field_pass": fstr(plus_one_pass),
                    "failure_type": failure_type,
                    "parse_status": parse_status,
                    "included_in_distribution": fstr(included),
                    "numeric_comparison_available": fstr(numeric_available),
                    "expected_near_zero": fstr(expected_near_zero),
                    "extracted_parseable": fstr(extracted_parseable),
                    "notes": notes,
                }
            )
    return field_rows


def group_summary(rows: list[dict[str, Any]], keys: tuple[str, ...]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[tuple(row[key] for key in keys)].append(row)
    out = []
    for group_key, group_rows in sorted(groups.items()):
        included = [row for row in group_rows if row["included_in_distribution"] == "true"]
        values = [float(row["rel_error"]) for row in included]
        rec = {key: value for key, value in zip(keys, group_key)}
        rec.update(
            {
                "numeric_field_count": len(group_rows),
                "included_count": len(included),
                "excluded_count": len(group_rows) - len(included),
                "mean_rel_error": fstr(mean(values)) if values else "",
                "median_rel_error": fstr(median(values)) if values else "",
                "p90_rel_error": fstr(percentile(values, 90)),
                "p95_rel_error": fstr(percentile(values, 95)),
                "max_rel_error": fstr(max(values)) if values else "",
                "fields_with_rel_error_lte_1_percent": sum(1 for v in values if v <= 0.01),
                "fields_with_rel_error_lte_1_25_percent": sum(1 for v in values if v <= 0.0125),
                "fields_with_rel_error_lte_2_percent": sum(1 for v in values if v <= 0.02),
                "fields_with_rel_error_lte_3_percent": sum(1 for v in values if v <= 0.03),
                "fields_with_rel_error_lte_5_percent": sum(1 for v in values if v <= 0.05),
                "fields_with_rel_error_gt_10_percent": sum(1 for v in values if v > 0.10),
                "fields_with_rel_error_gt_100_percent": sum(1 for v in values if v > 1.0),
            }
        )
        out.append(rec)
    return out


def bin_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    included = [row for row in rows if row["included_in_distribution"] == "true"]
    total = len(included)
    buckets: dict[str, list[dict[str, Any]]] = {name: [] for name, _, _ in BINS}
    for row in included:
        buckets[bin_name(float(row["rel_error"]))].append(row)
    out = []
    for name, lower, upper in BINS:
        bucket = buckets[name]
        out.append(
            {
                "bin_name": name,
                "lower_bound_exclusive": fstr(lower),
                "upper_bound_inclusive": "inf" if upper == math.inf else fstr(upper),
                "field_count": len(bucket),
                "share_of_included_fields": fstr(len(bucket) / total if total else 0),
                "original_pass_field_count": sum(1 for row in bucket if row["original_field_pass"] == "true"),
                "original_fail_field_count": sum(1 for row in bucket if row["original_field_pass"] == "false"),
                "original_row_pass_count": sum(1 for row in bucket if row["original_deterministic_grade"] == "PASS"),
                "original_row_fail_count": sum(1 for row in bucket if row["original_deterministic_grade"] == "FAIL"),
            }
        )
    return out


def threshold_table(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    fail_rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row["original_deterministic_grade"] == "FAIL":
            fail_rows[row["source_run_id"]].append(row)
    out = []
    for threshold in THRESHOLDS:
        qualifying = []
        with_blocker = 0
        for run_id, fields in fail_rows.items():
            failed_numeric = [
                field
                for field in fields
                if field["original_field_pass"] == "false"
                and field["included_in_distribution"] == "true"
                and field["failure_type"] == "numeric_mismatch"
            ]
            if not failed_numeric:
                continue
            if all(float(field["rel_error"]) <= threshold for field in failed_numeric):
                qualifying.append(run_id)
                if any(field["failure_type"] not in {"none", "numeric_mismatch"} for field in fields if field["original_field_pass"] == "false"):
                    with_blocker += 1
        out.append(
            {
                "threshold": fstr(threshold),
                "threshold_percent": fstr(threshold * 100),
                "fail_rows_with_all_failed_numeric_fields_within_threshold": len(qualifying),
                "share_of_original_fail_rows": fstr(len(qualifying) / EXPECTED_FAIL),
                "fail_rows_with_any_non_numeric_blocker": with_blocker,
                "fail_rows_without_non_numeric_blocker": len(qualifying) - with_blocker,
            }
        )
    return out


def percentile_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    subsets = {
        "all_numeric_comparisons": rows,
        "original_PASS_rows": [r for r in rows if r["original_deterministic_grade"] == "PASS"],
        "original_FAIL_rows": [r for r in rows if r["original_deterministic_grade"] == "FAIL"],
        "originally_failed_numeric_fields": [r for r in rows if r["original_field_pass"] == "false" and r["included_in_distribution"] == "true"],
        "originally_passed_numeric_fields": [r for r in rows if r["original_field_pass"] == "true" and r["included_in_distribution"] == "true"],
    }
    return [stats_with_percentiles(name, subset_rows) for name, subset_rows in subsets.items()]


def write_report(
    field_rows: list[dict[str, Any]],
    percentiles: list[dict[str, Any]],
    by_batch: list[dict[str, Any]],
    by_scenario: list[dict[str, Any]],
    by_model: list[dict[str, Any]],
    by_field: list[dict[str, Any]],
    bins: list[dict[str, Any]],
    fail_bins: list[dict[str, Any]],
    thresholds: list[dict[str, Any]],
    protected_unchanged: bool,
) -> None:
    rows_seen = {(r["source_run_id"], r["batch"], r["scenario_id"], r["model_name"]) for r in field_rows}
    grades_by_row = {}
    for r in field_rows:
        grades_by_row[r["source_run_id"]] = r["original_deterministic_grade"]
    grade_counts = Counter(grades_by_row.values())
    included = [r for r in field_rows if r["included_in_distribution"] == "true"]
    excluded = len(field_rows) - len(included)
    extreme = sorted(included, key=lambda r: float(r["rel_error"]), reverse=True)[:10]
    lines = [
        "# Numeric Relative-Error Distribution v1",
        "",
        "## 1. Purpose",
        "",
        "Analyze numeric distance between extracted final-answer fields and gold values without changing deterministic labels.",
        "",
        "## 2. Input Artifacts",
        "",
        "- structured_prompt_pilot_v2..v5 clean autograde CSVs",
        "- gold_fields from learning.db opened read-only",
        "- existing normalized final-answer fields only",
        "",
        "## 3. Row and Field Coverage",
        "",
        f"- clean rows represented: {len(rows_seen)}",
        f"- PASS rows: {grade_counts.get('PASS', 0)}",
        f"- FAIL rows: {grade_counts.get('FAIL', 0)}",
        f"- numeric field comparisons total: {len(field_rows)}",
        f"- included in distribution: {len(included)}",
        f"- excluded from distribution: {excluded}",
        f"- protected inputs unchanged: {'yes' if protected_unchanged else 'no'}",
        "",
        "## 4. Relative-Error Definition",
        "",
        "`relative_error = abs(extracted_value - expected_value) / abs(expected_value)`.",
        "",
        "## 5. Handling of Zero/Near-Zero Gold Values",
        "",
        f"Expected values with `abs(expected_value) <= {NEAR_ZERO_ABS}` are retained in the field-level file but excluded from relative-error distribution statistics. This mirrors the autograder's special absolute-tolerance handling near zero.",
        "",
        "## 6. Overall Numeric Error Distribution",
        "",
    ]
    for row in percentiles:
        if row["subset"] == "all_numeric_comparisons":
            lines.extend(f"- {k}: {v}" for k, v in row.items() if k != "subset")
    lines.extend(["", "## 7. Distribution by Original PASS/FAIL", "", "| subset | count | mean | median | p90 | p95 | max |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for row in percentiles:
        lines.append(f"| {row['subset']} | {row['count']} | {row['mean_rel_error']} | {row['median_rel_error']} | {row['p90_rel_error']} | {row['p95_rel_error']} | {row['max_rel_error']} |")
    lines.extend(["", "## 8. Distribution for Original FAIL Rows", ""])
    fail_subset = next(r for r in percentiles if r["subset"] == "original_FAIL_rows")
    lines.extend(f"- {k}: {v}" for k, v in fail_subset.items() if k != "subset")
    lines.extend(["", "## 9. Distribution by Batch", "", "| batch | included | median | p95 | max | <=1% | >10% |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for row in by_batch:
        lines.append(f"| {row['batch']} | {row['included_count']} | {row['median_rel_error']} | {row['p95_rel_error']} | {row['max_rel_error']} | {row['fields_with_rel_error_lte_1_percent']} | {row['fields_with_rel_error_gt_10_percent']} |")
    lines.extend(["", "## 10. Distribution by Scenario", "", "| scenario | included | median | p95 | max | >10% |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    for row in by_scenario:
        lines.append(f"| {row['scenario_id']} | {row['included_count']} | {row['median_rel_error']} | {row['p95_rel_error']} | {row['max_rel_error']} | {row['fields_with_rel_error_gt_10_percent']} |")
    lines.extend(["", "## 11. Distribution by Model", "", "| model | included | median | p95 | max | >10% |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    for row in by_model:
        lines.append(f"| {row['model_name']} | {row['included_count']} | {row['median_rel_error']} | {row['p95_rel_error']} | {row['max_rel_error']} | {row['fields_with_rel_error_gt_10_percent']} |")
    lines.extend(["", "## 12. Distribution by Field", "", "See `numeric_relative_error_by_field.csv` for scenario-field summaries."])
    lines.extend(["", "## 13. Relative-Error Bins", "", "| bin | fields | share | row FAIL fields |", "| --- | ---: | ---: | ---: |"])
    for row in bins:
        lines.append(f"| {row['bin_name']} | {row['field_count']} | {row['share_of_included_fields']} | {row['original_row_fail_count']} |")
    lines.extend(["", "## 14. Exploratory Threshold Table for Future Tolerance Layers", "", "| threshold % | qualifying FAIL rows | share of FAIL rows | without blocker | with blocker |", "| ---: | ---: | ---: | ---: | ---: |"])
    for row in thresholds:
        lines.append(f"| {row['threshold_percent']} | {row['fail_rows_with_all_failed_numeric_fields_within_threshold']} | {row['share_of_original_fail_rows']} | {row['fail_rows_without_non_numeric_blocker']} | {row['fail_rows_with_any_non_numeric_blocker']} |")
    lines.extend(["", "## 15. Extreme-Error Examples", ""])
    for row in extreme:
        lines.append(f"- {row['batch']} / {row['scenario_id']} / {row['model_name']} / {row['field_name']}: rel_error={row['rel_error']} extracted={row['extracted_value']} expected={row['expected_value']}")
    lines.extend(
        [
            "",
            "## 16. Interpretation",
            "",
            "This layer separates field-level numeric distance from row-level correctness. If failed numeric fields concentrate far above 10%, tolerance relaxation is not the main issue; if they cluster around 1-5%, future soft-fail layers may be useful.",
            "",
            "## 17. Limitations",
            "",
            "- Does not change labels.",
            "- Does not revisit raw outputs.",
            "- Non-numeric fields remain in field-level data but are excluded from numeric distribution statistics.",
            "- Charts were skipped; CSV summaries are the source of truth.",
            "",
            "## 18. Recommended Next Tolerance/Categorization Layer",
            "",
            "Use the threshold table to test a small set of explicit tolerance alternatives, then separately classify unparseable/missing-field failures.",
        ]
    )
    (OUT_DIR / "NUMERIC_RELATIVE_ERROR_DISTRIBUTION_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme() -> None:
    lines = [
        "# Numeric Relative-Error Distribution v1",
        "",
        "This folder contains a read-only diagnostic layer for numeric distance between extracted model final-answer fields and gold numeric values.",
        "",
        "`rel_error = abs(extracted_value - expected_value) / abs(expected_value)`.",
        "",
        "This does not change deterministic grading and does not create new pass/fail categories.",
        "",
        "Use the bin, percentile, scenario, model, and field summaries to design future tolerance or categorization layers.",
        "",
        "Rerun with:",
        "",
        "```bash",
        ".venv/bin/python scripts/run_numeric_relative_error_distribution_v1.py",
        "```",
    ]
    (OUT_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    before = {str(path.relative_to(ROOT)): path_state(path) for path in PROTECTED_PATHS}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    field_rows = build_field_rows()
    row_ids = {(r["source_run_id"], r["batch"], r["scenario_id"], r["model_name"]) for r in field_rows}
    grades_by_run = {}
    for row in field_rows:
        grades_by_run[row["source_run_id"]] = row["original_deterministic_grade"]
    grade_counts = Counter(grades_by_run.values())
    if len(row_ids) != EXPECTED_ROWS:
        raise SystemExit(f"Expected {EXPECTED_ROWS} rows, found {len(row_ids)}")
    if grade_counts.get("PASS", 0) != EXPECTED_PASS or grade_counts.get("FAIL", 0) != EXPECTED_FAIL:
        raise SystemExit(f"Expected PASS={EXPECTED_PASS}, FAIL={EXPECTED_FAIL}; found {dict(grade_counts)}")

    percentiles = percentile_rows(field_rows)
    by_grade = group_summary(field_rows, ("original_deterministic_grade",))
    by_batch = group_summary(field_rows, ("batch",))
    by_scenario = group_summary(field_rows, ("scenario_id",))
    by_model = group_summary(field_rows, ("model_name",))
    by_field = group_summary(field_rows, ("scenario_id", "field_name"))
    bins = bin_summary(field_rows)
    fail_bins = bin_summary([row for row in field_rows if row["original_deterministic_grade"] == "FAIL"])
    thresholds = threshold_table(field_rows)

    write_csv(OUT_DIR / "numeric_relative_error_field_level.csv", field_rows, FIELD_FIELDS)
    write_json(OUT_DIR / "numeric_relative_error_field_level.json", field_rows)
    write_csv(OUT_DIR / "numeric_relative_error_by_grade.csv", by_grade, list(by_grade[0].keys()))
    write_csv(OUT_DIR / "numeric_relative_error_by_batch.csv", by_batch, list(by_batch[0].keys()))
    write_csv(OUT_DIR / "numeric_relative_error_by_scenario.csv", by_scenario, list(by_scenario[0].keys()))
    write_csv(OUT_DIR / "numeric_relative_error_by_model.csv", by_model, list(by_model[0].keys()))
    write_csv(OUT_DIR / "numeric_relative_error_by_field.csv", by_field, list(by_field[0].keys()))
    write_csv(OUT_DIR / "numeric_relative_error_bins.csv", bins, list(bins[0].keys()))
    write_csv(OUT_DIR / "numeric_relative_error_fail_only_bins.csv", fail_bins, list(fail_bins[0].keys()))
    write_csv(OUT_DIR / "numeric_relative_error_percentiles.csv", percentiles, list(percentiles[0].keys()))

    after = {str(path.relative_to(ROOT)): path_state(path) for path in PROTECTED_PATHS}
    protected_unchanged = before == after
    included = sum(1 for row in field_rows if row["included_in_distribution"] == "true")
    excluded = len(field_rows) - included
    manifest = {
        "artifact_name": "numeric_relative_error_distribution_v1",
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
        "original_clean_rows": len(row_ids),
        "original_pass_count": grade_counts.get("PASS", 0),
        "original_fail_count": grade_counts.get("FAIL", 0),
        "numeric_field_comparisons_total": len(field_rows),
        "numeric_field_comparisons_included": included,
        "numeric_field_comparisons_excluded": excluded,
        "scenario_count": len({row["scenario_id"] for row in field_rows}),
        "model_count": len({row["model_name"] for row in field_rows}),
        "review_rows_included": 0,
        "near_zero_abs_threshold": NEAR_ZERO_ABS,
        "protected_input_states_before": before,
        "protected_input_states_after": after,
        "protected_inputs_unchanged": protected_unchanged,
        "output_files": [
            "README.md",
            "NUMERIC_RELATIVE_ERROR_DISTRIBUTION_REPORT.md",
            "numeric_relative_error_field_level.csv",
            "numeric_relative_error_field_level.json",
            "numeric_relative_error_by_grade.csv",
            "numeric_relative_error_by_batch.csv",
            "numeric_relative_error_by_scenario.csv",
            "numeric_relative_error_by_model.csv",
            "numeric_relative_error_by_field.csv",
            "numeric_relative_error_bins.csv",
            "numeric_relative_error_fail_only_bins.csv",
            "numeric_relative_error_percentiles.csv",
            "numeric_relative_error_manifest.json",
        ],
    }
    write_json(OUT_DIR / "numeric_relative_error_manifest.json", manifest)
    write_readme()
    write_report(field_rows, percentiles, by_batch, by_scenario, by_model, by_field, bins, fail_bins, thresholds, protected_unchanged)

    overall = next(row for row in percentiles if row["subset"] == "all_numeric_comparisons")
    fail = next(row for row in percentiles if row["subset"] == "original_FAIL_rows")
    failed_fields = next(row for row in percentiles if row["subset"] == "originally_failed_numeric_fields")
    print(f"row_count={len(row_ids)}")
    print(f"original_grade_distribution={json.dumps(dict(sorted(grade_counts.items())), sort_keys=True)}")
    print(f"numeric_field_comparisons_total={len(field_rows)}")
    print(f"numeric_field_comparisons_included={included}")
    print(f"numeric_field_comparisons_excluded={excluded}")
    print(f"overall_median_rel_error={overall['median_rel_error']}")
    print(f"fail_rows_median_rel_error={fail['median_rel_error']}")
    print(f"failed_numeric_fields_median_rel_error={failed_fields['median_rel_error']}")
    print(f"protected_inputs_unchanged={protected_unchanged}")
    print(f"output_dir={OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
