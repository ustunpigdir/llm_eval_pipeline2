#!/usr/bin/env python3
"""Compute local ROUGE-L over canonical reasoning-only structured rows."""
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
OUTPUT_DIR = ROOT / "outputs" / "metric_comparison_analytics_rouge_l_v1"

EXPECTED_ROWS = 252
EXPECTED_PASS = 117
EXPECTED_FAIL = 135
EXPECTED_SCENARIOS = 32
EXPECTED_MODELS = 8
TOKENIZER_DESCRIPTION = r"lowercase regex tokens: [A-Za-z]+|[0-9]+(?:\.[0-9]+)?|[\\+\-*/=^_{}()[\],.]"
TOKEN_RE = re.compile(r"[A-Za-z]+|[0-9]+(?:\.[0-9]+)?|[\\+\-*/=^_{}()[\],.]")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall((text or "").lower())


def lcs_len(a: list[str], b: list[str]) -> int:
    if not a or not b:
        return 0
    prev = [0] * (len(b) + 1)
    for token_a in a:
        curr = [0] * (len(b) + 1)
        for j, token_b in enumerate(b, start=1):
            if token_a == token_b:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = curr[j - 1] if curr[j - 1] >= prev[j] else prev[j]
        prev = curr
    return prev[-1]


def rouge_l(candidate: str, reference: str) -> tuple[int, int, int, float, float, float]:
    cand_tokens = tokenize(candidate)
    ref_tokens = tokenize(reference)
    lcs = lcs_len(cand_tokens, ref_tokens)
    precision = lcs / len(cand_tokens) if cand_tokens else 0.0
    recall = lcs / len(ref_tokens) if ref_tokens else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if precision + recall else 0.0
    return len(cand_tokens), len(ref_tokens), lcs, precision, recall, f1


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
    vals = [float(row["rouge_l_f1"]) for row in rows]
    pass_vals = [float(row["rouge_l_f1"]) for row in rows if row["deterministic_grade"] == "PASS"]
    fail_vals = [float(row["rouge_l_f1"]) for row in rows if row["deterministic_grade"] == "FAIL"]
    pass_count = len(pass_vals)
    fail_count = len(fail_vals)
    pass_mean = mean(pass_vals) if pass_vals else ""
    fail_mean = mean(fail_vals) if fail_vals else ""
    return {
        "row_count": len(rows),
        "pass_count": pass_count,
        "fail_count": fail_count,
        "mean_rouge_l_f1": mean(vals) if vals else "",
        "median_rouge_l_f1": median(vals) if vals else "",
        "min_rouge_l_f1": min(vals) if vals else "",
        "max_rouge_l_f1": max(vals) if vals else "",
        "PASS_mean_rouge_l_f1": pass_mean,
        "FAIL_mean_rouge_l_f1": fail_mean,
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


def load_existing_metrics() -> dict[str, dict[str, str]]:
    if not EXISTING_METRICS_PATH.exists():
        return {}
    return {row["source_run_id"]: row for row in read_csv(EXISTING_METRICS_PATH)}


def build_rows() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    canonical = read_csv(INPUT_PATH)
    existing = load_existing_metrics()
    rows: list[dict[str, Any]] = []
    compare_rows: list[dict[str, Any]] = []
    for row in canonical:
        cand_n, ref_n, lcs_n, precision, recall, f1_score = rouge_l(
            row["candidate_reasoning_text"],
            row["reference_reasoning_text"],
        )
        metrics = existing.get(row["source_run_id"], {})
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
            "candidate_token_count": cand_n,
            "reference_token_count": ref_n,
            "lcs_token_count": lcs_n,
            "rouge_l_precision": precision,
            "rouge_l_recall": recall,
            "rouge_l_f1": f1_score,
            "bertscore_full_f1": metrics.get("bertscore_full_f1", row.get("bertscore_full_f1", "")),
            "bertscore_no_final_f1": metrics.get("bertscore_no_final_f1", row.get("bertscore_no_final_f1", "")),
            "candidate_reference_length_ratio": metrics.get("candidate_reference_length_ratio", ""),
        }
        rows.append(out)
        compare_rows.append(
            {
                "source_run_id": row["source_run_id"],
                "deterministic_grade": row["deterministic_grade"],
                "rouge_l_f1": f1_score,
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
        "rouge_l_f1",
        "rouge_l_precision",
        "rouge_l_recall",
        "bertscore_no_final_f1",
        "source_run_id",
    ]
    high_fail = sorted(
        [row for row in rows if row["deterministic_grade"] == "FAIL"],
        key=lambda row: float(row["rouge_l_f1"]),
        reverse=True,
    )[:20]
    low_pass = sorted(
        [row for row in rows if row["deterministic_grade"] == "PASS"],
        key=lambda row: float(row["rouge_l_f1"]),
    )[:20]
    return [{field: row[field] for field in fields} for row in high_fail], [{field: row[field] for field in fields} for row in low_pass]


def write_readme(output_files: list[str]) -> None:
    lines = [
        "# ROUGE-L Metric v1",
        "",
        "This folder contains deterministic ROUGE-L scores computed from canonical reasoning-only text.",
        "",
        "It uses `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv` as the only text source.",
        "",
        "It does not change grading, modify raw outputs, call APIs, run BERTScore, run ROSCOE/NLI, or implement Phase 2 semantics.",
        "",
        "Rerun with:",
        "",
        "```bash",
        ".venv/bin/python scripts/run_rouge_l_metric_v1.py",
        "```",
        "",
        "Interpret ROUGE-L as lexical sequence overlap, not correctness.",
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
    rouge_grade = overall["PASS_minus_FAIL_mean_gap"]
    no_final_gap = 0.081370
    no_final_effect = 0.219251
    rouge_effect = overall["simple_effect_size"]
    corr_row = next(row for row in corr if row["metric"] == "deterministic_pass_binary")
    rouge_corr = corr_row["rouge_l_f1"]
    rouge_bert_corr = next(row for row in corr if row["metric"] == "rouge_l_f1")["bertscore_no_final_f1"]
    comparison = "weaker" if abs(float(rouge_grade)) < abs(no_final_gap) else "stronger"
    lines = [
        "# ROUGE-L Metric Report",
        "",
        "## Purpose",
        "",
        "Add a cheap deterministic lexical metric over canonical reasoning-only structured rows.",
        "",
        "## Inputs",
        "",
        "- `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv`",
        "",
        "## Tokenizer",
        "",
        f"`{TOKENIZER_DESCRIPTION}`",
        "",
        "## Row Coverage",
        "",
        f"- Rows: {len(rows)}",
        f"- PASS: {sum(1 for row in rows if row['deterministic_grade'] == 'PASS')}",
        f"- FAIL: {sum(1 for row in rows if row['deterministic_grade'] == 'FAIL')}",
        "",
        "## Overall ROUGE-L Summary",
        "",
        f"- Mean F1: {float(overall['mean_rouge_l_f1']):.6f}",
        f"- Median F1: {float(overall['median_rouge_l_f1']):.6f}",
        f"- Min F1: {float(overall['min_rouge_l_f1']):.6f}",
        f"- Max F1: {float(overall['max_rouge_l_f1']):.6f}",
        "",
        "## ROUGE-L By Deterministic Grade",
        "",
        "| grade | rows | mean_f1 | median_f1 |",
        "| --- | ---: | ---: | ---: |",
    ]
    for row in by_grade:
        lines.append(f"| {row['deterministic_grade']} | {row['row_count']} | {float(row['mean_rouge_l_f1']):.6f} | {float(row['median_rouge_l_f1']):.6f} |")
    lines.extend(
        [
            "",
            "## ROUGE-L By Batch",
            "",
            "| batch | rows | mean_f1 | PASS-FAIL gap |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for row in by_batch:
        gap = row["PASS_minus_FAIL_mean_gap"]
        lines.append(f"| {row['batch']} | {row['row_count']} | {float(row['mean_rouge_l_f1']):.6f} | {float(gap):.6f} |")
    lowest_scenarios = sorted(by_scenario, key=lambda row: float(row["mean_rouge_l_f1"]))[:5]
    top_models = sorted(by_model, key=lambda row: float(row["mean_rouge_l_f1"]), reverse=True)[:5]
    lines.extend(["", "## ROUGE-L By Scenario", ""])
    lines.extend(f"- {row['scenario_id']}: mean F1 {float(row['mean_rouge_l_f1']):.6f}" for row in lowest_scenarios)
    lines.extend(["", "## ROUGE-L By Model", ""])
    lines.extend(f"- {row['model_name']}: mean F1 {float(row['mean_rouge_l_f1']):.6f}" for row in top_models)
    lines.extend(
        [
            "",
            "## High-ROUGE FAIL Examples",
            "",
            f"- {high_fail[0]['scenario_id']} / {high_fail[0]['model_name']}: {float(high_fail[0]['rouge_l_f1']):.6f}",
            "",
            "## Low-ROUGE PASS Examples",
            "",
            f"- {low_pass[0]['scenario_id']} / {low_pass[0]['model_name']}: {float(low_pass[0]['rouge_l_f1']):.6f}",
            "",
            "## Correlation With Deterministic PASS/FAIL",
            "",
            f"- deterministic_pass_binary vs ROUGE-L F1: {float(rouge_corr):.6f}",
            "",
            "## Comparison With No-Final BERTScore",
            "",
            f"- ROUGE-L PASS-minus-FAIL mean gap: {float(rouge_grade):.6f}",
            f"- ROUGE-L simple effect size: {float(rouge_effect):.6f}",
            f"- no-final BERTScore PASS-minus-FAIL mean gap: {no_final_gap:.6f}",
            f"- no-final BERTScore simple effect size: {no_final_effect:.6f}",
            f"- ROUGE-L vs no-final BERTScore correlation: {float(rouge_bert_corr):.6f}",
            f"- ROUGE-L separation is {comparison} than no-final BERTScore by mean gap.",
            "",
            "## Interpretation",
            "",
            "ROUGE-L is deterministic and reproducible. It measures lexical sequence overlap, not scientific correctness.",
            "",
            "High ROUGE-L FAIL rows show lexical similarity can coexist with wrong scientific answers. Low ROUGE-L PASS rows show correct answers can differ lexically from the reference.",
            "",
            "## Limitations",
            "",
            "- Lexical sequence overlap is sensitive to phrasing and length.",
            "- It does not evaluate numeric correctness or physical reasoning validity.",
            "- Deterministic grading remains the correctness anchor.",
            "",
            "## Recommended Next Metric",
            "",
            "Compute chrF from the same canonical text artifact as a complementary character-level lexical metric.",
        ]
    )
    (OUTPUT_DIR / "ROUGE_L_METRIC_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


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
        "rouge_l_f1",
        "rouge_l_precision",
        "rouge_l_recall",
        "bertscore_full_f1",
        "bertscore_no_final_f1",
        "candidate_reference_length_ratio",
        "candidate_token_count",
        "reference_token_count",
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
        "candidate_token_count",
        "reference_token_count",
        "lcs_token_count",
        "rouge_l_precision",
        "rouge_l_recall",
        "rouge_l_f1",
        "bertscore_full_f1",
        "bertscore_no_final_f1",
        "candidate_reference_length_ratio",
    ]
    write_csv(OUTPUT_DIR / "rouge_l_row_scores.csv", rows, row_fields)
    (OUTPUT_DIR / "rouge_l_row_scores.json").write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(OUTPUT_DIR / "rouge_l_by_grade.csv", by_grade)
    write_csv(OUTPUT_DIR / "rouge_l_by_batch.csv", by_batch)
    write_csv(OUTPUT_DIR / "rouge_l_by_scenario.csv", by_scenario)
    write_csv(OUTPUT_DIR / "rouge_l_by_model.csv", by_model)
    write_csv(OUTPUT_DIR / "rouge_l_outliers_high_rouge_fail.csv", high_fail)
    write_csv(OUTPUT_DIR / "rouge_l_outliers_low_rouge_pass.csv", low_pass)
    write_csv(OUTPUT_DIR / "rouge_l_vs_existing_metrics.csv", compare_rows)
    write_csv(OUTPUT_DIR / "rouge_l_correlation_matrix.csv", corr, ["metric", *corr_columns])

    output_files = [
        "README.md",
        "ROUGE_L_METRIC_REPORT.md",
        "rouge_l_row_scores.csv",
        "rouge_l_row_scores.json",
        "rouge_l_by_grade.csv",
        "rouge_l_by_batch.csv",
        "rouge_l_by_scenario.csv",
        "rouge_l_by_model.csv",
        "rouge_l_outliers_high_rouge_fail.csv",
        "rouge_l_outliers_low_rouge_pass.csv",
        "rouge_l_vs_existing_metrics.csv",
        "rouge_l_correlation_matrix.csv",
        "manifest.json",
    ]
    overall = group_stats(rows)
    manifest = {
        "artifact_name": "rouge_l_metric_v1",
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
        "tokenizer": TOKENIZER_DESCRIPTION,
        "metrics_computed": ["rouge_l_precision", "rouge_l_recall", "rouge_l_f1"],
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
    print(f"mean_rouge_l_f1={float(overall['mean_rouge_l_f1']):.6f}")
    print(f"pass_fail_gap={float(overall['PASS_minus_FAIL_mean_gap']):.6f}")
    print(f"simple_effect_size={float(overall['simple_effect_size']):.6f}")


if __name__ == "__main__":
    main()
