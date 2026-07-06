#!/usr/bin/env python3
"""Compute local chrF over canonical reasoning-only structured rows."""
from __future__ import annotations

import csv
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median, pstdev
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "outputs" / "metric_text_artifacts_v1" / "canonical_reasoning_text_dataset.csv"
EXISTING_METRICS_PATH = ROOT / "outputs" / "metric_comparison_analytics_v1" / "metric_comparison_base_dataset.csv"
ROUGE_PATH = ROOT / "outputs" / "metric_comparison_analytics_rouge_l_v1" / "rouge_l_row_scores.csv"
OUTPUT_DIR = ROOT / "outputs" / "metric_comparison_analytics_chrf_v1"

EXPECTED_ROWS = 252
EXPECTED_PASS = 117
EXPECTED_FAIL = 135
EXPECTED_SCENARIOS = 32
EXPECTED_MODELS = 8
CHRF_BETA = 2.0
CHRF_NGRAM_ORDER_MAX = 6


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").lower()).strip()


def ngram_counts(text: str, n: int) -> Counter[str]:
    if len(text) < n:
        return Counter()
    return Counter(text[i : i + n] for i in range(len(text) - n + 1))


def chrf(candidate: str, reference: str, beta: float = CHRF_BETA, max_order: int = CHRF_NGRAM_ORDER_MAX) -> tuple[float, float, float]:
    cand = normalize_text(candidate)
    ref = normalize_text(reference)
    if not cand or not ref:
        return 0.0, 0.0, 0.0
    precisions: list[float] = []
    recalls: list[float] = []
    for n in range(1, max_order + 1):
        cand_counts = ngram_counts(cand, n)
        ref_counts = ngram_counts(ref, n)
        cand_total = sum(cand_counts.values())
        ref_total = sum(ref_counts.values())
        if cand_total == 0 or ref_total == 0:
            continue
        overlap = sum(min(cand_counts[gram], ref_counts[gram]) for gram in cand_counts.keys() & ref_counts.keys())
        precisions.append(overlap / cand_total)
        recalls.append(overlap / ref_total)
    if not precisions or not recalls:
        return 0.0, 0.0, 0.0
    precision = mean(precisions)
    recall = mean(recalls)
    beta2 = beta * beta
    score = ((1 + beta2) * precision * recall / (beta2 * precision + recall)) if precision + recall else 0.0
    return precision, recall, score


def f(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except Exception:
        return None


def std(values: list[float]) -> float:
    return pstdev(values) if len(values) > 1 else 0.0


def effect_size(pass_vals: list[float], fail_vals: list[float]) -> float | str:
    if not pass_vals or not fail_vals:
        return ""
    pooled = math.sqrt((std(pass_vals) ** 2 + std(fail_vals) ** 2) / 2)
    return (mean(pass_vals) - mean(fail_vals)) / pooled if pooled else ""


def group_stats(rows: list[dict[str, Any]]) -> dict[str, Any]:
    vals = [float(row["chrf_score"]) for row in rows]
    pass_vals = [float(row["chrf_score"]) for row in rows if row["deterministic_grade"] == "PASS"]
    fail_vals = [float(row["chrf_score"]) for row in rows if row["deterministic_grade"] == "FAIL"]
    pass_mean = mean(pass_vals) if pass_vals else ""
    fail_mean = mean(fail_vals) if fail_vals else ""
    return {
        "row_count": len(rows),
        "pass_count": len(pass_vals),
        "fail_count": len(fail_vals),
        "mean_chrf_score": mean(vals) if vals else "",
        "median_chrf_score": median(vals) if vals else "",
        "min_chrf_score": min(vals) if vals else "",
        "max_chrf_score": max(vals) if vals else "",
        "PASS_mean_chrf_score": pass_mean,
        "FAIL_mean_chrf_score": fail_mean,
        "PASS_minus_FAIL_mean_gap": pass_mean - fail_mean if pass_vals and fail_vals else "",
        "simple_effect_size": effect_size(pass_vals, fail_vals),
    }


def summarize(rows: list[dict[str, Any]], keys: tuple[str, ...]) -> list[dict[str, Any]]:
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[tuple(row[key] for key in keys)].append(row)
    out: list[dict[str, Any]] = []
    for key_values, group in sorted(groups.items()):
        item = {keys[idx]: key_values[idx] for idx in range(len(keys))}
        item.update(group_stats(group))
        out.append(item)
    return out


def pearson(xs: list[float], ys: list[float]) -> float | str:
    if len(xs) < 2 or len(xs) != len(ys):
        return ""
    mean_x = mean(xs)
    mean_y = mean(ys)
    denom_x = math.sqrt(sum((x - mean_x) ** 2 for x in xs))
    denom_y = math.sqrt(sum((y - mean_y) ** 2 for y in ys))
    denom = denom_x * denom_y
    if denom == 0:
        return ""
    return sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)) / denom


def correlation_matrix(rows: list[dict[str, Any]], columns: list[str]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for a in columns:
        item: dict[str, Any] = {"metric": a}
        for b in columns:
            pairs = [(f(row.get(a)), f(row.get(b))) for row in rows]
            pairs = [(x, y) for x, y in pairs if x is not None and y is not None]
            item[b] = pearson([x for x, _ in pairs], [y for _, y in pairs])
        out.append(item)
    return out


def by_run_id(path: Path) -> dict[str, dict[str, str]]:
    return {row["source_run_id"]: row for row in read_csv(path)}


def build_rows() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    canonical = read_csv(INPUT_PATH)
    existing = by_run_id(EXISTING_METRICS_PATH)
    rouge = by_run_id(ROUGE_PATH)
    rows: list[dict[str, Any]] = []
    compare_rows: list[dict[str, Any]] = []
    for row in canonical:
        precision, recall, score = chrf(row["candidate_reasoning_text"], row["reference_reasoning_text"])
        metrics = existing.get(row["source_run_id"], {})
        rouge_metrics = rouge.get(row["source_run_id"], {})
        out = {
            "row_key": row["row_key"],
            "source_run_id": row["source_run_id"],
            "batch": row["batch"],
            "scenario_id": row["scenario_id"],
            "category": row["category"],
            "model_name": row["model_name"],
            "deterministic_grade": row["deterministic_grade"],
            "deterministic_pass_binary": row["deterministic_pass_binary"],
            "extraction_status": row["extraction_status"],
            "helper_status": row["helper_status"],
            "error_tags": row["error_tags"],
            "failed_fields": row["failed_fields"],
            "candidate_reasoning_text_sha256": row["candidate_reasoning_text_sha256"],
            "reference_reasoning_text_sha256": row["reference_reasoning_text_sha256"],
            "candidate_reasoning_text_length_chars": row["candidate_reasoning_text_length_chars"],
            "reference_reasoning_text_length_chars": row["reference_reasoning_text_length_chars"],
            "chrf_precision": precision,
            "chrf_recall": recall,
            "chrf_score": score,
            "chrf_beta": CHRF_BETA,
            "chrf_ngram_order_max": CHRF_NGRAM_ORDER_MAX,
            "bertscore_full_f1": metrics.get("bertscore_full_f1", row.get("bertscore_full_f1", "")),
            "bertscore_no_final_f1": metrics.get("bertscore_no_final_f1", row.get("bertscore_no_final_f1", "")),
            "rouge_l_f1": rouge_metrics.get("rouge_l_f1", ""),
            "candidate_reference_length_ratio": metrics.get("candidate_reference_length_ratio", ""),
        }
        rows.append(out)
        compare_rows.append(
            {
                "source_run_id": row["source_run_id"],
                "deterministic_grade": row["deterministic_grade"],
                "chrf_score": score,
                "chrf_precision": precision,
                "chrf_recall": recall,
                "rouge_l_f1": out["rouge_l_f1"],
                "bertscore_full_f1": out["bertscore_full_f1"],
                "bertscore_no_final_f1": out["bertscore_no_final_f1"],
                "candidate_reference_length_ratio": out["candidate_reference_length_ratio"],
            }
        )
    return rows, compare_rows


def outliers(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    fields = [
        "batch",
        "scenario_id",
        "category",
        "model_name",
        "deterministic_grade",
        "error_tags",
        "failed_fields",
        "chrf_score",
        "chrf_precision",
        "chrf_recall",
        "rouge_l_f1",
        "bertscore_no_final_f1",
        "source_run_id",
    ]
    high_fail = sorted(
        [row for row in rows if row["deterministic_grade"] == "FAIL"],
        key=lambda row: float(row["chrf_score"]),
        reverse=True,
    )[:20]
    low_pass = sorted(
        [row for row in rows if row["deterministic_grade"] == "PASS"],
        key=lambda row: float(row["chrf_score"]),
    )[:20]
    return [{field: row[field] for field in fields} for row in high_fail], [{field: row[field] for field in fields} for row in low_pass]


def write_readme(output_files: list[str]) -> None:
    lines = [
        "# chrF Metric v1",
        "",
        "This folder contains deterministic chrF scores computed from canonical reasoning-only text.",
        "",
        "It uses `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv` as the only text source.",
        "",
        "It does not change grading, modify raw outputs, call APIs, run BERTScore, run ROSCOE/NLI, or implement Phase 2 semantics.",
        "",
        "Rerun with:",
        "",
        "```bash",
        ".venv/bin/python scripts/run_chrf_metric_v1.py",
        "```",
        "",
        "Interpret chrF as character n-gram overlap, not correctness.",
        "",
        "Files:",
    ]
    lines.extend(f"- `{name}`" for name in output_files)
    (OUTPUT_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(
    rows: list[dict[str, Any]],
    by_grade: list[dict[str, Any]],
    by_batch: list[dict[str, Any]],
    by_scenario: list[dict[str, Any]],
    by_model: list[dict[str, Any]],
    high_fail: list[dict[str, Any]],
    low_pass: list[dict[str, Any]],
    corr: list[dict[str, Any]],
) -> None:
    overall = group_stats(rows)
    chrf_gap = float(overall["PASS_minus_FAIL_mean_gap"])
    rouge_gap = 0.044352
    bert_gap = 0.081370
    chrf_effect = float(overall["simple_effect_size"])
    rouge_effect = 0.209217
    bert_effect = 0.219251
    det_corr = next(row for row in corr if row["metric"] == "deterministic_pass_binary")["chrf_score"]
    rouge_corr = next(row for row in corr if row["metric"] == "chrf_score")["rouge_l_f1"]
    bert_corr = next(row for row in corr if row["metric"] == "chrf_score")["bertscore_no_final_f1"]
    rouge_cmp = "stronger" if abs(chrf_gap) > abs(rouge_gap) else "weaker"
    bert_cmp = "stronger" if abs(chrf_gap) > abs(bert_gap) else "weaker"
    lines = [
        "# chrF Metric Report",
        "",
        "## Purpose",
        "",
        "Add a deterministic character n-gram lexical metric over canonical reasoning-only structured rows.",
        "",
        "## Inputs",
        "",
        "- `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv`",
        "",
        "## chrF Implementation",
        "",
        f"- Character n-gram orders: 1 through {CHRF_NGRAM_ORDER_MAX}",
        f"- Beta: {CHRF_BETA}",
        "- Lowercase text and normalize whitespace to single spaces.",
        "- Keep punctuation and math symbols.",
        "- Use multiset n-gram overlap and aggregate mean precision/recall before F-score.",
        "",
        "## Row Coverage",
        "",
        f"- Rows: {len(rows)}",
        f"- PASS: {sum(1 for row in rows if row['deterministic_grade'] == 'PASS')}",
        f"- FAIL: {sum(1 for row in rows if row['deterministic_grade'] == 'FAIL')}",
        "",
        "## Overall chrF Summary",
        "",
        f"- Mean score: {float(overall['mean_chrf_score']):.6f}",
        f"- Median score: {float(overall['median_chrf_score']):.6f}",
        f"- Min score: {float(overall['min_chrf_score']):.6f}",
        f"- Max score: {float(overall['max_chrf_score']):.6f}",
        "",
        "## chrF By Deterministic Grade",
        "",
        "| grade | rows | mean_chrf | median_chrf |",
        "| --- | ---: | ---: | ---: |",
    ]
    for row in by_grade:
        lines.append(f"| {row['deterministic_grade']} | {row['row_count']} | {float(row['mean_chrf_score']):.6f} | {float(row['median_chrf_score']):.6f} |")
    lines.extend(["", "## chrF By Batch", "", "| batch | rows | mean_chrf | PASS-FAIL gap |", "| --- | ---: | ---: | ---: |"])
    for row in by_batch:
        lines.append(f"| {row['batch']} | {row['row_count']} | {float(row['mean_chrf_score']):.6f} | {float(row['PASS_minus_FAIL_mean_gap']):.6f} |")
    lowest_scenarios = sorted(by_scenario, key=lambda row: float(row["mean_chrf_score"]))[:5]
    top_models = sorted(by_model, key=lambda row: float(row["mean_chrf_score"]), reverse=True)[:5]
    lines.extend(["", "## chrF By Scenario", ""])
    lines.extend(f"- {row['scenario_id']}: mean score {float(row['mean_chrf_score']):.6f}" for row in lowest_scenarios)
    lines.extend(["", "## chrF By Model", ""])
    lines.extend(f"- {row['model_name']}: mean score {float(row['mean_chrf_score']):.6f}" for row in top_models)
    lines.extend(
        [
            "",
            "## High-chrF FAIL Examples",
            "",
            f"- {high_fail[0]['scenario_id']} / {high_fail[0]['model_name']}: {float(high_fail[0]['chrf_score']):.6f}",
            "",
            "## Low-chrF PASS Examples",
            "",
            f"- {low_pass[0]['scenario_id']} / {low_pass[0]['model_name']}: {float(low_pass[0]['chrf_score']):.6f}",
            "",
            "## Correlation With Deterministic PASS/FAIL",
            "",
            f"- deterministic_pass_binary vs chrF score: {float(det_corr):.6f}",
            "",
            "## Comparison With ROUGE-L",
            "",
            f"- chrF PASS-minus-FAIL mean gap: {chrf_gap:.6f}",
            f"- chrF simple effect size: {chrf_effect:.6f}",
            f"- ROUGE-L PASS-minus-FAIL mean gap: {rouge_gap:.6f}",
            f"- ROUGE-L simple effect size: {rouge_effect:.6f}",
            f"- chrF vs ROUGE-L correlation: {float(rouge_corr):.6f}",
            f"- chrF separation is {rouge_cmp} than ROUGE-L by mean gap.",
            "",
            "## Comparison With No-Final BERTScore",
            "",
            f"- no-final BERTScore PASS-minus-FAIL mean gap: {bert_gap:.6f}",
            f"- no-final BERTScore simple effect size: {bert_effect:.6f}",
            f"- chrF vs no-final BERTScore correlation: {float(bert_corr):.6f}",
            f"- chrF separation is {bert_cmp} than no-final BERTScore by mean gap.",
            "",
            "## Interpretation",
            "",
            "chrF is deterministic and reproducible. It measures character n-gram overlap, not scientific correctness.",
            "",
            "High chrF FAIL rows show character-level similarity can coexist with wrong scientific answers. Low chrF PASS rows show correct answers can differ textually from the reference.",
            "",
            "## Limitations",
            "",
            "- Character overlap is sensitive to notation and phrasing.",
            "- It does not evaluate numeric correctness or physical reasoning validity.",
            "- Deterministic grading remains the correctness anchor.",
            "",
            "## Recommended Next Metric",
            "",
            "Compute a combined lexical dashboard from ROUGE-L and chrF, then consider NLI/ROSCOE only after the cheap metrics are fully characterized.",
        ]
    )
    (OUTPUT_DIR / "CHRF_METRIC_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows, compare_rows = build_rows()
    grades = Counter(row["deterministic_grade"] for row in rows)
    if len(rows) != EXPECTED_ROWS:
        raise SystemExit(f"Expected {EXPECTED_ROWS} rows, found {len(rows)}")
    if grades["PASS"] != EXPECTED_PASS or grades["FAIL"] != EXPECTED_FAIL:
        raise SystemExit(f"Unexpected PASS/FAIL counts: {dict(grades)}")
    if len({row["scenario_id"] for row in rows}) != EXPECTED_SCENARIOS:
        raise SystemExit("Expected 32 scenarios")
    if len({row["model_name"] for row in rows}) != EXPECTED_MODELS:
        raise SystemExit("Expected 8 models")

    by_grade = summarize(rows, ("deterministic_grade",))
    by_batch = summarize(rows, ("batch",))
    by_scenario = summarize(rows, ("scenario_id", "category"))
    by_model = summarize(rows, ("model_name",))
    high_fail, low_pass = outliers(rows)
    corr_columns = [
        "deterministic_pass_binary",
        "chrf_score",
        "chrf_precision",
        "chrf_recall",
        "rouge_l_f1",
        "bertscore_full_f1",
        "bertscore_no_final_f1",
        "candidate_reference_length_ratio",
        "candidate_reasoning_text_length_chars",
        "reference_reasoning_text_length_chars",
    ]
    corr = correlation_matrix(rows, corr_columns)

    row_fields = [
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
        "error_tags",
        "failed_fields",
        "candidate_reasoning_text_sha256",
        "reference_reasoning_text_sha256",
        "candidate_reasoning_text_length_chars",
        "reference_reasoning_text_length_chars",
        "chrf_precision",
        "chrf_recall",
        "chrf_score",
        "chrf_beta",
        "chrf_ngram_order_max",
        "bertscore_full_f1",
        "bertscore_no_final_f1",
        "rouge_l_f1",
        "candidate_reference_length_ratio",
    ]
    write_csv(OUTPUT_DIR / "chrf_row_scores.csv", rows, row_fields)
    (OUTPUT_DIR / "chrf_row_scores.json").write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(OUTPUT_DIR / "chrf_by_grade.csv", by_grade)
    write_csv(OUTPUT_DIR / "chrf_by_batch.csv", by_batch)
    write_csv(OUTPUT_DIR / "chrf_by_scenario.csv", by_scenario)
    write_csv(OUTPUT_DIR / "chrf_by_model.csv", by_model)
    write_csv(OUTPUT_DIR / "chrf_outliers_high_chrf_fail.csv", high_fail)
    write_csv(OUTPUT_DIR / "chrf_outliers_low_chrf_pass.csv", low_pass)
    write_csv(OUTPUT_DIR / "chrf_vs_existing_metrics.csv", compare_rows)
    write_csv(OUTPUT_DIR / "chrf_correlation_matrix.csv", corr, ["metric", *corr_columns])

    output_files = [
        "README.md",
        "CHRF_METRIC_REPORT.md",
        "chrf_row_scores.csv",
        "chrf_row_scores.json",
        "chrf_by_grade.csv",
        "chrf_by_batch.csv",
        "chrf_by_scenario.csv",
        "chrf_by_model.csv",
        "chrf_outliers_high_chrf_fail.csv",
        "chrf_outliers_low_chrf_pass.csv",
        "chrf_vs_existing_metrics.csv",
        "chrf_correlation_matrix.csv",
        "manifest.json",
    ]
    overall = group_stats(rows)
    manifest = {
        "artifact_name": "chrf_metric_v1",
        "created_at": utc_now(),
        "input_text_artifact": "outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv",
        "read_only": True,
        "learning_db_modified": False,
        "raw_outputs_modified": False,
        "model_calls_made": False,
        "external_api_calls": False,
        "bertscore_run": False,
        "roscoe_run": False,
        "nli_run": False,
        "phase2_semantics_implemented": False,
        "expected_rows": EXPECTED_ROWS,
        "actual_rows": len(rows),
        "pass_count": grades["PASS"],
        "fail_count": grades["FAIL"],
        "chrf_beta": CHRF_BETA,
        "chrf_ngram_order_max": CHRF_NGRAM_ORDER_MAX,
        "metrics_computed": ["chrf_precision", "chrf_recall", "chrf_score"],
        "overall": overall,
        "output_files": output_files,
    }
    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_readme(output_files)
    write_report(rows, by_grade, by_batch, by_scenario, by_model, high_fail, low_pass, corr)

    print(f"output_dir={OUTPUT_DIR}")
    print(f"row_count={len(rows)}")
    print(f"pass_count={grades['PASS']}")
    print(f"fail_count={grades['FAIL']}")
    print(f"scenario_count={len({row['scenario_id'] for row in rows})}")
    print(f"model_count={len({row['model_name'] for row in rows})}")
    print(f"mean_chrf_score={float(overall['mean_chrf_score']):.6f}")
    print(f"pass_fail_gap={float(overall['PASS_minus_FAIL_mean_gap']):.6f}")
    print(f"simple_effect_size={float(overall['simple_effect_size']):.6f}")


if __name__ == "__main__":
    main()
