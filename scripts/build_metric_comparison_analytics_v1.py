#!/usr/bin/env python3
"""Build read-only metric-comparison analytics for structured-prompt rows."""
from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median, pstdev
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs" / "metric_comparison_analytics_v1"
FULL_DIR = ROOT / "outputs" / "bertscore_structured_all32_phase1_hardened_v1"
NO_FINAL_DIR = ROOT / "outputs" / "bertscore_structured_all32_phase1_hardened_no_final_block_v1"
SUMMARY_DIR = ROOT / "outputs" / "structured_prompt_all32_summary_phase1_hardened"

EXPECTED_ROWS = 252
EXPECTED_PASS = 117
EXPECTED_FAIL = 135
EXPECTED_SCENARIOS = 32

NUMERIC_METRICS = [
    "bertscore_full_f1",
    "bertscore_no_final_f1",
    "candidate_reference_length_ratio",
]
CORRELATION_COLUMNS = [
    "deterministic_pass_binary",
    "bertscore_full_f1",
    "bertscore_no_final_f1",
    "candidate_reference_length_ratio",
    "candidate_no_final_text_length_chars",
    "reference_text_length_chars",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def f(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except Exception:
        return None


def batch_dir(batch_num: int) -> Path:
    return ROOT / "outputs" / f"structured_prompt_pilot_v{batch_num}"


def load_clean_autograde() -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for batch_num in (2, 3, 4, 5):
        batch = f"V{batch_num}"
        path = batch_dir(batch_num) / "autograde_no_bert_v1" / f"structured_prompt_v{batch_num}_clean_autograde.json"
        for row in read_json(path):
            run_id = str(row["output_path_or_run_id"])
            rows[run_id] = {**row, "batch": batch}
    return rows


def load_review_statuses() -> dict[str, str]:
    statuses: dict[str, str] = {}
    for batch_num in (2, 3, 4, 5):
        path = batch_dir(batch_num) / "review_layer_v1" / "review_layer_v1.json"
        for row in read_json(path):
            statuses[str(row["output_path_or_run_id"])] = row.get("review_status", "")
    return statuses


def unique_by_source_run_id(rows: list[dict[str, str]], label: str) -> dict[str, dict[str, str]]:
    keys = [row.get("source_run_id", "") for row in rows]
    if any(not key for key in keys):
        raise SystemExit(f"{label} has blank source_run_id values")
    duplicates = [key for key, count in Counter(keys).items() if count > 1]
    if duplicates:
        raise SystemExit(f"{label} has duplicate source_run_id keys: {duplicates[:5]}")
    return {row["source_run_id"]: row for row in rows}


def build_base_dataset() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    autograde = load_clean_autograde()
    review_statuses = load_review_statuses()
    full_rows = unique_by_source_run_id(
        read_csv(FULL_DIR / "bertscore_structured_all32_phase1_hardened.csv"),
        "full-answer BERTScore",
    )
    no_final_rows = unique_by_source_run_id(
        read_csv(NO_FINAL_DIR / "bertscore_structured_all32_phase1_hardened_no_final_block.csv"),
        "no-final-block BERTScore",
    )
    common = sorted(set(autograde) & set(full_rows) & set(no_final_rows))
    missing = {
        "missing_autograde": sorted((set(full_rows) | set(no_final_rows)) - set(autograde)),
        "missing_full": sorted(set(autograde) - set(full_rows)),
        "missing_no_final": sorted(set(autograde) - set(no_final_rows)),
    }
    rows: list[dict[str, Any]] = []
    for run_id in common:
        auto = autograde[run_id]
        full = full_rows[run_id]
        no_final = no_final_rows[run_id]
        grade = auto.get("deterministic_grade", "")
        no_final_len = f(no_final.get("candidate_no_final_text_length_chars"))
        ref_len = f(no_final.get("reference_no_final_text_length_chars"))
        ratio = no_final_len / ref_len if no_final_len is not None and ref_len not in (None, 0) else ""
        row_key = f"{auto['batch']}|{auto['scenario_id']}|{auto['model_name']}|{run_id}"
        rows.append(
            {
                "row_key": row_key,
                "source_run_id": run_id,
                "batch": auto["batch"],
                "scenario_id": auto.get("scenario_id", ""),
                "category": full.get("category", ""),
                "model_name": auto.get("model_name", ""),
                "deterministic_grade": grade,
                "deterministic_pass_binary": 1 if grade == "PASS" else 0,
                "extraction_status": auto.get("extraction_status", ""),
                "helper_status": auto.get("raw_helper_status", ""),
                "review_status": review_statuses.get(run_id, "CLEAN"),
                "error_tags": auto.get("error_tags", ""),
                "failed_fields": auto.get("failed_fields", ""),
                "human_label_if_available": "",
                "human_label_available": False,
                "bertscore_full_precision": full.get("bert_precision", ""),
                "bertscore_full_recall": full.get("bert_recall", ""),
                "bertscore_full_f1": full.get("bert_f1", ""),
                "bertscore_no_final_precision": no_final.get("bert_precision", ""),
                "bertscore_no_final_recall": no_final.get("bert_recall", ""),
                "bertscore_no_final_f1": no_final.get("bert_f1", ""),
                "bertscore_full_minus_no_final_f1": (float(full["bert_f1"]) - float(no_final["bert_f1"])),
                "candidate_full_text_length_chars": no_final.get("candidate_full_text_length_chars", full.get("candidate_text_length_chars", "")),
                "candidate_no_final_text_length_chars": no_final.get("candidate_no_final_text_length_chars", ""),
                "reference_text_length_chars": no_final.get("reference_no_final_text_length_chars", full.get("reference_text_length_chars", "")),
                "final_block_removed_candidate": no_final.get("final_block_removed_candidate", ""),
                "final_block_removed_reference": no_final.get("final_block_removed_reference", ""),
                "rouge_l_f1": "",
                "chrf_score": "",
                "candidate_reference_length_ratio": ratio,
            }
        )
    alignment = {
        "alignment_key": "source_run_id",
        "full_bertscore_rows_aligned": len(common),
        "no_final_bertscore_rows_aligned": len(common),
        "missing": missing,
    }
    return rows, alignment


def metric_values(rows: list[dict[str, Any]], metric: str) -> list[float]:
    return [value for row in rows if (value := f(row.get(metric))) is not None]


def grade_values(rows: list[dict[str, Any]], metric: str, grade: str) -> list[float]:
    return [value for row in rows if row["deterministic_grade"] == grade and (value := f(row.get(metric))) is not None]


def std(values: list[float]) -> float:
    return pstdev(values) if len(values) > 1 else 0.0


def effect_size(pass_vals: list[float], fail_vals: list[float]) -> float | str:
    if not pass_vals or not fail_vals:
        return ""
    pooled = math.sqrt((std(pass_vals) ** 2 + std(fail_vals) ** 2) / 2)
    return (mean(pass_vals) - mean(fail_vals)) / pooled if pooled else ""


def interpretation_for_metric(metric: str, gap: float | str) -> str:
    if gap == "":
        return "not available"
    if metric == "candidate_reference_length_ratio":
        return "length/provenance diagnostic, not correctness metric"
    if abs(float(gap)) < 0.05:
        return "weak PASS/FAIL separation"
    if float(gap) > 0:
        return "PASS rows score higher on average, still secondary/descriptive"
    return "FAIL rows score higher on average; misleading as correctness proxy"


def by_metric(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for metric in NUMERIC_METRICS:
        vals = metric_values(rows, metric)
        pass_vals = grade_values(rows, metric, "PASS")
        fail_vals = grade_values(rows, metric, "FAIL")
        pass_mean = mean(pass_vals) if pass_vals else ""
        fail_mean = mean(fail_vals) if fail_vals else ""
        gap = pass_mean - fail_mean if pass_vals and fail_vals else ""
        out.append(
            {
                "metric": metric,
                "row_count": len(vals),
                "mean": mean(vals) if vals else "",
                "median": median(vals) if vals else "",
                "std": std(vals) if vals else "",
                "min": min(vals) if vals else "",
                "max": max(vals) if vals else "",
                "PASS_mean": pass_mean,
                "FAIL_mean": fail_mean,
                "PASS_minus_FAIL_mean_gap": gap,
                "PASS_median": median(pass_vals) if pass_vals else "",
                "FAIL_median": median(fail_vals) if fail_vals else "",
                "PASS_minus_FAIL_median_gap": (median(pass_vals) - median(fail_vals)) if pass_vals and fail_vals else "",
                "simple_effect_size": effect_size(pass_vals, fail_vals),
                "interpretation_short": interpretation_for_metric(metric, gap),
            }
        )
    return out


def aggregate(rows: list[dict[str, Any]], keys: tuple[str, ...]) -> list[dict[str, Any]]:
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[tuple(row[key] for key in keys)].append(row)
    out: list[dict[str, Any]] = []
    for key_values, group in sorted(groups.items()):
        item = {keys[idx]: key_values[idx] for idx in range(len(keys))}
        pass_count = sum(1 for row in group if row["deterministic_grade"] == "PASS")
        fail_count = sum(1 for row in group if row["deterministic_grade"] == "FAIL")
        item.update(
            {
                "row_count": len(group),
                "pass_count": pass_count,
                "fail_count": fail_count,
                "pass_rate": pass_count / len(group) if group else 0.0,
            }
        )
        for metric in NUMERIC_METRICS:
            vals = metric_values(group, metric)
            item[f"mean_{metric}"] = mean(vals) if vals else ""
            item[f"median_{metric}"] = median(vals) if vals else ""
            item[f"min_{metric}"] = min(vals) if vals else ""
            item[f"max_{metric}"] = max(vals) if vals else ""
        full_pass = grade_values(group, "bertscore_full_f1", "PASS")
        full_fail = grade_values(group, "bertscore_full_f1", "FAIL")
        no_pass = grade_values(group, "bertscore_no_final_f1", "PASS")
        no_fail = grade_values(group, "bertscore_no_final_f1", "FAIL")
        item["full_PASS_minus_FAIL_gap"] = mean(full_pass) - mean(full_fail) if full_pass and full_fail else ""
        item["no_final_PASS_minus_FAIL_gap"] = mean(no_pass) - mean(no_fail) if no_pass and no_fail else ""
        item["average_candidate_length"] = mean(metric_values(group, "candidate_no_final_text_length_chars")) if metric_values(group, "candidate_no_final_text_length_chars") else ""
        item["average_reference_length"] = mean(metric_values(group, "reference_text_length_chars")) if metric_values(group, "reference_text_length_chars") else ""
        out.append(item)
    return out


def pearson(xs: list[float], ys: list[float]) -> float | str:
    if len(xs) < 2 or len(ys) < 2 or len(xs) != len(ys):
        return ""
    mean_x = mean(xs)
    mean_y = mean(ys)
    denom_x = math.sqrt(sum((x - mean_x) ** 2 for x in xs))
    denom_y = math.sqrt(sum((y - mean_y) ** 2 for y in ys))
    denom = denom_x * denom_y
    if denom == 0:
        return ""
    return sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)) / denom


def correlation_matrix(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[str]]:
    included = [col for col in CORRELATION_COLUMNS if len(metric_values(rows, col)) >= len(rows) * 0.9]
    out: list[dict[str, Any]] = []
    for col_a in included:
        line: dict[str, Any] = {"metric": col_a}
        for col_b in included:
            pairs = [(f(row.get(col_a)), f(row.get(col_b))) for row in rows]
            pairs = [(a, b) for a, b in pairs if a is not None and b is not None]
            line[col_b] = pearson([a for a, _ in pairs], [b for _, b in pairs])
        out.append(line)
    return out, included


def outliers(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    fields = [
        "batch",
        "scenario_id",
        "category",
        "model_name",
        "deterministic_grade",
        "error_tags",
        "failed_fields",
        "bertscore_no_final_f1",
        "bertscore_full_f1",
        "human_label_if_available",
        "source_run_id",
    ]
    high_fail = sorted(
        [row for row in rows if row["deterministic_grade"] == "FAIL"],
        key=lambda row: float(row["bertscore_no_final_f1"]),
        reverse=True,
    )[:20]
    low_pass = sorted(
        [row for row in rows if row["deterministic_grade"] == "PASS"],
        key=lambda row: float(row["bertscore_no_final_f1"]),
    )[:20]
    return [{field: row[field] for field in fields} for row in high_fail], [{field: row[field] for field in fields} for row in low_pass]


def write_readme(output_files: list[str]) -> None:
    lines = [
        "# Metric Comparison Analytics v1",
        "",
        "This folder is a read-only analytics layer for comparing saved automatic metrics with frozen deterministic labels.",
        "",
        "It does not change grades, implement Phase 2 semantics, rerun models, call LLM APIs, rerun BERTScore, or modify `learning.db`.",
        "",
        "Frozen inputs include the Phase-1-hardened structured summaries, V2-V5 clean autograde files, and the two saved BERTScore runs.",
        "",
        "Rerun with:",
        "",
        "```bash",
        ".venv/bin/python scripts/build_metric_comparison_analytics_v1.py",
        "```",
        "",
        "Current metrics: full-answer BERTScore F1, no-final-block BERTScore F1, and candidate/reference length ratio.",
        "",
        "ROUGE-L, chrF, ROSCOE, NLI, and human-label alignment should be added later from an artifact that safely exposes candidate/reference text and aligned human labels.",
        "",
        "Outputs:",
    ]
    lines.extend(f"- `{name}`" for name in output_files)
    (OUTPUT_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(
    rows: list[dict[str, Any]],
    metric_rows: list[dict[str, Any]],
    grade_rows: list[dict[str, Any]],
    scenario_rows: list[dict[str, Any]],
    model_rows: list[dict[str, Any]],
    corr_rows: list[dict[str, Any]],
    corr_cols: list[str],
    high_fail: list[dict[str, Any]],
    low_pass: list[dict[str, Any]],
    alignment: dict[str, Any],
) -> None:
    grades = Counter(row["deterministic_grade"] for row in rows)
    scenarios = len({row["scenario_id"] for row in rows})
    models = len({row["model_name"] for row in rows})
    no_final = next(row for row in metric_rows if row["metric"] == "bertscore_no_final_f1")
    full = next(row for row in metric_rows if row["metric"] == "bertscore_full_f1")
    best_models = sorted(model_rows, key=lambda row: float(row["mean_bertscore_no_final_f1"]), reverse=True)[:3]
    weakest_scenarios = sorted(scenario_rows, key=lambda row: float(row["mean_bertscore_no_final_f1"]))[:3]
    det_corr = ""
    for row in corr_rows:
        if row["metric"] == "deterministic_pass_binary":
            det_corr = row.get("bertscore_no_final_f1", "")
    lines = [
        "# Metric Comparison Analytics Report",
        "",
        "## Purpose",
        "",
        "Compare available automatic text metrics against frozen deterministic PASS/FAIL labels without changing grading.",
        "",
        "## Inputs Used",
        "",
        "- Phase-1-hardened structured summaries",
        "- Structured prompt V2-V5 clean autograde files",
        "- Full-answer BERTScore v1",
        "- No-final-block BERTScore v1",
        "",
        "## Dataset Shape",
        "",
        f"- Rows: {len(rows)}",
        f"- Scenarios: {scenarios}",
        f"- Models: {models}",
        f"- Alignment: {alignment['alignment_key']}, {alignment['full_bertscore_rows_aligned']} rows",
        "",
        "## Deterministic Label Distribution",
        "",
        f"- PASS: {grades['PASS']}",
        f"- FAIL: {grades['FAIL']}",
        "",
        "## Metrics Included",
        "",
        "- Full-answer BERTScore F1: provenance/deprecated because references already exclude final-answer sections.",
        "- No-final-block BERTScore F1: valid BERTScore comparison, with known 5-row final-block removal caveat.",
        "- Candidate/reference length ratio: provenance diagnostic only.",
        "",
        "## Metric Separation Summary",
        "",
        f"- Full-answer BERTScore mean gap PASS-FAIL: {float(full['PASS_minus_FAIL_mean_gap']):.6f}",
        f"- No-final BERTScore mean gap PASS-FAIL: {float(no_final['PASS_minus_FAIL_mean_gap']):.6f}",
        f"- No-final simple effect size: {float(no_final['simple_effect_size']):.6f}",
        "",
        "## Full-Answer vs No-Final-Block BERTScore",
        "",
        "No-final-block BERTScore separates PASS/FAIL better than full-answer BERTScore in this saved dataset. Full-answer BERTScore is kept for provenance only.",
        "",
        "## Scenario-Level Findings",
        "",
        "Lowest no-final mean-F1 scenarios:",
    ]
    lines.extend(f"- {row['scenario_id']}: {float(row['mean_bertscore_no_final_f1']):.6f}" for row in weakest_scenarios)
    lines.extend(["", "## Model-Level Findings", ""])
    lines.extend(f"- {row['model_name']}: mean no-final F1 {float(row['mean_bertscore_no_final_f1']):.6f}" for row in best_models)
    lines.extend(
        [
            "",
            "## Outlier Examples",
            "",
            f"- Highest-metric FAIL: {high_fail[0]['scenario_id']} / {high_fail[0]['model_name']} / F1 {float(high_fail[0]['bertscore_no_final_f1']):.6f}",
            f"- Lowest-metric PASS: {low_pass[0]['scenario_id']} / {low_pass[0]['model_name']} / F1 {float(low_pass[0]['bertscore_no_final_f1']):.6f}",
            "",
            "## Correlation Findings",
            "",
            f"- Pearson correlation between deterministic pass binary and no-final BERTScore F1: {float(det_corr):.6f}",
            f"- Correlation columns included: {', '.join(corr_cols)}",
            "",
            "## Human Label Alignment Status",
            "",
            "No safely alignable human-reviewed labels were found for the 252 structured CLEAN rows; `human_label_available=false` for all rows.",
            "",
            "## Limitations",
            "",
            "- Automatic text metrics are secondary/descriptive and do not measure correctness.",
            "- Deterministic PASS/FAIL remains the correctness anchor.",
            "- ROUGE-L and chrF were not computed because saved metric CSVs do not contain candidate/reference text.",
            "- No-final BERTScore v1 has a 5-row final-block removal caveat.",
            "",
            "## Next Metrics To Add",
            "",
            "- ROUGE-L and chrF from a safe text-bearing analysis artifact.",
            "- Human-review labels if a stable alignment key exists.",
            "- ROSCOE and NLI later, after this base layer is stable.",
            "",
            "## Suggested LinkedIn Framing",
            "",
            "Use this as a metric-behavior story: deterministic grading catches scientific correctness, while semantic metrics reveal overlap, style, and misleading high-score failures.",
        ]
    )
    (OUTPUT_DIR / "METRIC_COMPARISON_ANALYTICS_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows, alignment = build_base_dataset()
    if len(rows) != EXPECTED_ROWS:
        raise SystemExit(f"Expected {EXPECTED_ROWS} rows, found {len(rows)}")
    grades = Counter(row["deterministic_grade"] for row in rows)
    if grades["PASS"] != EXPECTED_PASS or grades["FAIL"] != EXPECTED_FAIL:
        raise SystemExit(f"Unexpected PASS/FAIL counts: {dict(grades)}")
    if len({row["scenario_id"] for row in rows}) != EXPECTED_SCENARIOS:
        raise SystemExit("Expected all 32 scenarios")
    if any(row["review_status"] != "CLEAN" for row in rows):
        raise SystemExit("Unexpected non-CLEAN review row in base dataset")

    metric_rows = by_metric(rows)
    grade_rows = aggregate(rows, ("deterministic_grade",))
    scenario_rows = aggregate(rows, ("scenario_id", "category"))
    model_rows = aggregate(rows, ("model_name",))
    corr_rows, corr_cols = correlation_matrix(rows)
    high_fail, low_pass = outliers(rows)

    base_fields = [
        "row_key",
        "source_run_id",
        "batch",
        "scenario_id",
        "category",
        "model_name",
        "deterministic_grade",
        "deterministic_pass_binary",
        "extraction_status",
        "helper_status",
        "review_status",
        "error_tags",
        "failed_fields",
        "human_label_if_available",
        "human_label_available",
        "bertscore_full_precision",
        "bertscore_full_recall",
        "bertscore_full_f1",
        "bertscore_no_final_precision",
        "bertscore_no_final_recall",
        "bertscore_no_final_f1",
        "bertscore_full_minus_no_final_f1",
        "candidate_full_text_length_chars",
        "candidate_no_final_text_length_chars",
        "reference_text_length_chars",
        "final_block_removed_candidate",
        "final_block_removed_reference",
        "rouge_l_f1",
        "chrf_score",
        "candidate_reference_length_ratio",
    ]
    write_csv(OUTPUT_DIR / "metric_comparison_base_dataset.csv", rows, base_fields)
    (OUTPUT_DIR / "metric_comparison_base_dataset.json").write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(OUTPUT_DIR / "metric_comparison_by_metric.csv", metric_rows)
    write_csv(OUTPUT_DIR / "metric_comparison_by_grade.csv", grade_rows)
    write_csv(OUTPUT_DIR / "metric_comparison_by_scenario.csv", scenario_rows)
    write_csv(OUTPUT_DIR / "metric_comparison_by_model.csv", model_rows)
    write_csv(OUTPUT_DIR / "metric_comparison_outliers_high_metric_fail.csv", high_fail)
    write_csv(OUTPUT_DIR / "metric_comparison_outliers_low_metric_pass.csv", low_pass)
    write_csv(OUTPUT_DIR / "metric_correlation_matrix.csv", corr_rows, ["metric", *corr_cols])

    output_files = [
        "README.md",
        "METRIC_COMPARISON_ANALYTICS_REPORT.md",
        "metric_comparison_base_dataset.csv",
        "metric_comparison_base_dataset.json",
        "metric_comparison_by_metric.csv",
        "metric_comparison_by_grade.csv",
        "metric_comparison_by_scenario.csv",
        "metric_comparison_by_model.csv",
        "metric_comparison_outliers_high_metric_fail.csv",
        "metric_comparison_outliers_low_metric_pass.csv",
        "metric_correlation_matrix.csv",
        "manifest.json",
    ]
    manifest = {
        "artifact_name": "metric_comparison_analytics_v1",
        "created_at": utc_now(),
        "purpose": "compare automatic metrics against deterministic and human-reviewed labels",
        "read_only": True,
        "learning_db_modified": False,
        "raw_outputs_modified": False,
        "model_calls_made": False,
        "external_llm_api_calls": False,
        "phase2_semantics_implemented": False,
        "input_folders": [
            str(SUMMARY_DIR.relative_to(ROOT)) + "/",
            "outputs/structured_prompt_pilot_v2/",
            "outputs/structured_prompt_pilot_v3/",
            "outputs/structured_prompt_pilot_v4/",
            "outputs/structured_prompt_pilot_v5/",
            str(FULL_DIR.relative_to(ROOT)) + "/",
            str(NO_FINAL_DIR.relative_to(ROOT)) + "/",
        ],
        "output_files": output_files,
        "expected_rows": EXPECTED_ROWS,
        "actual_rows": len(rows),
        "deterministic_pass_count": grades["PASS"],
        "deterministic_fail_count": grades["FAIL"],
        "metrics_included": NUMERIC_METRICS,
        "alignment_status": alignment,
        "human_label_alignment_status": "not_available_for_structured_clean_rows",
        "known_limitations": [
            "automatic text metrics are secondary/descriptive and not correctness measures",
            "full-answer BERTScore is provenance-only because references already exclude final-answer sections",
            "no-final BERTScore v1 has a 5-row final-block-removal caveat",
            "ROUGE-L and chrF are blank because saved metric CSVs do not contain candidate/reference text",
            "no safely alignable human labels found for these 252 rows",
        ],
    }
    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_readme(output_files)
    write_report(rows, metric_rows, grade_rows, scenario_rows, model_rows, corr_rows, corr_cols, high_fail, low_pass, alignment)

    print(f"output_dir={OUTPUT_DIR}")
    print(f"row_count={len(rows)}")
    print(f"pass_count={grades['PASS']}")
    print(f"fail_count={grades['FAIL']}")
    print(f"scenario_count={len({row['scenario_id'] for row in rows})}")
    print(f"model_count={len({row['model_name'] for row in rows})}")
    print(f"metrics_included={json.dumps(NUMERIC_METRICS)}")
    print(f"alignment_status={json.dumps(alignment, sort_keys=True)}")
    print("human_label_alignment_status=not_available_for_structured_clean_rows")


if __name__ == "__main__":
    main()
