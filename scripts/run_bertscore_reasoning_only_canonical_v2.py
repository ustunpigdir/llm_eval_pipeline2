#!/usr/bin/env python3
"""Run BERTScore over canonical reasoning-only structured text."""
from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median, pstdev
from typing import Any

from run_bertscore_structured_all32_phase1_hardened import compute_bertscore_batches


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "outputs" / "metric_text_artifacts_v1" / "canonical_reasoning_text_dataset.csv"
METRIC_BASE_PATH = ROOT / "outputs" / "metric_comparison_analytics_v1" / "metric_comparison_base_dataset.csv"
ROUGE_PATH = ROOT / "outputs" / "metric_comparison_analytics_rouge_l_v1" / "rouge_l_row_scores.csv"
CHRF_PATH = ROOT / "outputs" / "metric_comparison_analytics_chrf_v1" / "chrf_row_scores.csv"
NO_FINAL_V1_PATH = ROOT / "outputs" / "bertscore_structured_all32_phase1_hardened_no_final_block_v1" / "bertscore_structured_all32_phase1_hardened_no_final_block.csv"
OUTPUT_DIR = ROOT / "outputs" / "bertscore_reasoning_only_canonical_v2"

EXPECTED_ROWS = 252
EXPECTED_PASS = 117
EXPECTED_FAIL = 135
EXPECTED_SCENARIOS = 32
EXPECTED_MODELS = 8
BERTSCORE_MODEL_TYPE = "lang=en default (roberta-large)"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def by_run_id(path: Path) -> dict[str, dict[str, str]]:
    return {row["source_run_id"]: row for row in read_csv(path)}


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


def std(values: list[float]) -> float:
    return pstdev(values) if len(values) > 1 else 0.0


def effect_size(pass_vals: list[float], fail_vals: list[float]) -> float | str:
    if not pass_vals or not fail_vals:
        return ""
    pooled = math.sqrt((std(pass_vals) ** 2 + std(fail_vals) ** 2) / 2)
    return (mean(pass_vals) - mean(fail_vals)) / pooled if pooled else ""


def group_stats(rows: list[dict[str, Any]]) -> dict[str, Any]:
    vals = [float(row["bert_f1"]) for row in rows]
    pass_vals = [float(row["bert_f1"]) for row in rows if row["deterministic_grade"] == "PASS"]
    fail_vals = [float(row["bert_f1"]) for row in rows if row["deterministic_grade"] == "FAIL"]
    pass_mean = mean(pass_vals) if pass_vals else ""
    fail_mean = mean(fail_vals) if fail_vals else ""
    return {
        "row_count": len(rows),
        "pass_count": len(pass_vals),
        "fail_count": len(fail_vals),
        "mean_bert_f1": mean(vals) if vals else "",
        "median_bert_f1": median(vals) if vals else "",
        "min_bert_f1": min(vals) if vals else "",
        "max_bert_f1": max(vals) if vals else "",
        "PASS_mean_bert_f1": pass_mean,
        "FAIL_mean_bert_f1": fail_mean,
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
    mean_x, mean_y = mean(xs), mean(ys)
    denom_x = math.sqrt(sum((x - mean_x) ** 2 for x in xs))
    denom_y = math.sqrt(sum((y - mean_y) ** 2 for y in ys))
    denom = denom_x * denom_y
    if denom == 0:
        return ""
    return sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)) / denom


def correlation_matrix(rows: list[dict[str, Any]], cols: list[str]) -> list[dict[str, Any]]:
    out = []
    for a in cols:
        item: dict[str, Any] = {"metric": a}
        for b in cols:
            pairs = [(f(row.get(a)), f(row.get(b))) for row in rows]
            pairs = [(x, y) for x, y in pairs if x is not None and y is not None]
            item[b] = pearson([x for x, _ in pairs], [y for _, y in pairs])
        out.append(item)
    return out


def outliers(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    fields = ["batch", "scenario_id", "category", "model_name", "deterministic_grade", "error_tags", "failed_fields", "bert_f1", "bert_precision", "bert_recall", "rouge_l_f1", "chrf_score", "source_run_id"]
    high_fail = sorted([r for r in rows if r["deterministic_grade"] == "FAIL"], key=lambda r: float(r["bert_f1"]), reverse=True)[:20]
    low_pass = sorted([r for r in rows if r["deterministic_grade"] == "PASS"], key=lambda r: float(r["bert_f1"]))[:20]
    return [{k: row[k] for k in fields} for row in high_fail], [{k: row[k] for k in fields} for row in low_pass]


def build_output_rows(batch_size: int) -> tuple[list[dict[str, Any]], str, bool, str]:
    canonical = read_csv(INPUT_PATH)
    base = by_run_id(METRIC_BASE_PATH)
    rouge = by_run_id(ROUGE_PATH)
    chrf = by_run_id(CHRF_PATH)
    no_final_v1 = by_run_id(NO_FINAL_V1_PATH)

    precision, recall, f1s, model_hash, rescale, notes = compute_bertscore_batches(
        [row["candidate_reasoning_text"] for row in canonical],
        [row["reference_reasoning_text"] for row in canonical],
        batch_size,
    )
    rows: list[dict[str, Any]] = []
    for idx, row in enumerate(canonical):
        run_id = row["source_run_id"]
        base_row = base.get(run_id, {})
        rouge_row = rouge.get(run_id, {})
        chrf_row = chrf.get(run_id, {})
        v1_row = no_final_v1.get(run_id, {})
        v1_f1 = base_row.get("bertscore_no_final_f1", v1_row.get("bert_f1", ""))
        rows.append(
            {
                "row_key": row["row_key"],
                "source_run_id": run_id,
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
                "bert_precision": precision[idx],
                "bert_recall": recall[idx],
                "bert_f1": f1s[idx],
                "bertscore_model_type": BERTSCORE_MODEL_TYPE,
                "bertscore_model_hash": model_hash,
                "rescale_with_baseline": rescale,
                "bertscore_full_f1": base_row.get("bertscore_full_f1", ""),
                "bertscore_no_final_v1_f1": v1_f1,
                "rouge_l_f1": rouge_row.get("rouge_l_f1", ""),
                "chrf_score": chrf_row.get("chrf_score", ""),
                "candidate_reference_length_ratio": base_row.get("candidate_reference_length_ratio", ""),
            }
        )
    return rows, model_hash, rescale, notes


def comparison_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for row in rows:
        v1 = f(row.get("bertscore_no_final_v1_f1"))
        v2 = f(row.get("bert_f1"))
        out.append(
            {
                "source_run_id": row["source_run_id"],
                "deterministic_grade": row["deterministic_grade"],
                "bertscore_reasoning_only_v2_f1": row["bert_f1"],
                "bertscore_no_final_v1_f1": row["bertscore_no_final_v1_f1"],
                "bertscore_full_f1": row["bertscore_full_f1"],
                "rouge_l_f1": row["rouge_l_f1"],
                "chrf_score": row["chrf_score"],
                "candidate_reference_length_ratio": row["candidate_reference_length_ratio"],
                "v2_minus_no_final_v1_f1": (v2 - v1) if v1 is not None and v2 is not None else "",
            }
        )
    return out


def write_readme(files: list[str]) -> None:
    lines = [
        "# BERTScore Reasoning-Only Canonical v2",
        "",
        "This folder contains the corrected reasoning-only BERTScore run using the canonical text artifact.",
        "",
        "v2 exists because no-final-block v1 used a separate regex remover and missed 5 candidate final-answer blocks. This run reads `candidate_reasoning_text` and `reference_reasoning_text` directly from `metric_text_artifacts_v1`.",
        "",
        "It does not change grading, call LLM APIs, rerun models, overwrite old BERTScore outputs, or implement Phase 2 semantics.",
        "",
        "Rerun with:",
        "",
        "```bash",
        ".venv/bin/python scripts/run_bertscore_reasoning_only_canonical_v2.py",
        "```",
        "",
        "BERTScore is descriptive and secondary; deterministic PASS/FAIL remains the correctness anchor.",
        "",
        "Files:",
    ]
    lines.extend(f"- `{name}`" for name in files)
    (OUTPUT_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(rows: list[dict[str, Any]], by_grade: list[dict[str, Any]], by_batch: list[dict[str, Any]], by_scenario: list[dict[str, Any]], by_model: list[dict[str, Any]], high_fail: list[dict[str, Any]], low_pass: list[dict[str, Any]], corr: list[dict[str, Any]], model_hash: str, rescale: bool, v1_changed: int) -> None:
    overall = group_stats(rows)
    det_corr = next(r for r in corr if r["metric"] == "deterministic_pass_binary")["bertscore_reasoning_only_v2_f1"]
    rouge_corr = next(r for r in corr if r["metric"] == "bertscore_reasoning_only_v2_f1")["rouge_l_f1"]
    chrf_corr = next(r for r in corr if r["metric"] == "bertscore_reasoning_only_v2_f1")["chrf_score"]
    v1_corr = next(r for r in corr if r["metric"] == "bertscore_reasoning_only_v2_f1")["bertscore_no_final_v1_f1"]
    lines = [
        "# BERTScore Reasoning-Only Canonical v2 Report",
        "",
        "## Purpose",
        "",
        "Run BERTScore on canonical extractor-span reasoning-only text.",
        "",
        "## Inputs",
        "",
        "- `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv`",
        "",
        "## BERTScore Config",
        "",
        f"- Model type: {BERTSCORE_MODEL_TYPE}",
        f"- Model hash: {model_hash}",
        f"- rescale_with_baseline: {rescale}",
        "",
        "## Why This Is v2",
        "",
        "v1 no-final-block BERTScore had a 5-row final-block removal caveat. v2 uses canonical candidate/reference reasoning text where extractor-span removal succeeded for 252/252 rows.",
        "",
        "## Row Coverage",
        "",
        f"- Rows: {len(rows)}",
        f"- PASS: {sum(1 for r in rows if r['deterministic_grade'] == 'PASS')}",
        f"- FAIL: {sum(1 for r in rows if r['deterministic_grade'] == 'FAIL')}",
        "",
        "## Overall BERTScore Summary",
        "",
        f"- Mean F1: {float(overall['mean_bert_f1']):.6f}",
        f"- Median F1: {float(overall['median_bert_f1']):.6f}",
        f"- Min F1: {float(overall['min_bert_f1']):.6f}",
        f"- Max F1: {float(overall['max_bert_f1']):.6f}",
        "",
        "## BERTScore By Deterministic Grade",
        "",
        "| grade | rows | mean_f1 | median_f1 |",
        "| --- | ---: | ---: | ---: |",
    ]
    for row in by_grade:
        lines.append(f"| {row['deterministic_grade']} | {row['row_count']} | {float(row['mean_bert_f1']):.6f} | {float(row['median_bert_f1']):.6f} |")
    lines.extend(["", "## BERTScore By Batch", "", "| batch | rows | mean_f1 | PASS-FAIL gap |", "| --- | ---: | ---: | ---: |"])
    for row in by_batch:
        gap = row["PASS_minus_FAIL_mean_gap"]
        lines.append(f"| {row['batch']} | {row['row_count']} | {float(row['mean_bert_f1']):.6f} | {float(gap):.6f} |")
    lines.extend(["", "## BERTScore By Scenario", ""])
    for row in sorted(by_scenario, key=lambda r: float(r["mean_bert_f1"]))[:5]:
        lines.append(f"- {row['scenario_id']}: mean F1 {float(row['mean_bert_f1']):.6f}")
    lines.extend(["", "## BERTScore By Model", ""])
    for row in sorted(by_model, key=lambda r: float(r["mean_bert_f1"]), reverse=True)[:5]:
        lines.append(f"- {row['model_name']}: mean F1 {float(row['mean_bert_f1']):.6f}")
    lines.extend(
        [
            "",
            "## High-BERTScore FAIL Examples",
            "",
            f"- {high_fail[0]['scenario_id']} / {high_fail[0]['model_name']}: {float(high_fail[0]['bert_f1']):.6f}",
            "",
            "## Low-BERTScore PASS Examples",
            "",
            f"- {low_pass[0]['scenario_id']} / {low_pass[0]['model_name']}: {float(low_pass[0]['bert_f1']):.6f}",
            "",
            "## Comparison With No-Final BERTScore v1",
            "",
            f"- Rows with changed F1 vs v1: {v1_changed}",
            f"- Correlation with v1 F1: {float(v1_corr):.6f}",
            "",
            "## Comparison With ROUGE-L",
            "",
            f"- Correlation with ROUGE-L F1: {float(rouge_corr):.6f}",
            "",
            "## Comparison With chrF",
            "",
            f"- Correlation with chrF score: {float(chrf_corr):.6f}",
            "",
            "## Correlation With Deterministic PASS/FAIL",
            "",
            f"- deterministic_pass_binary vs canonical BERTScore F1: {float(det_corr):.6f}",
            "",
            "## Interpretation",
            "",
            "This v2 run is the valid reasoning-only BERTScore run. It remains descriptive and secondary; deterministic PASS/FAIL remains the correctness anchor.",
            "",
            "## Limitations",
            "",
            "- BERTScore does not measure scientific correctness.",
            "- High-BERTScore FAIL rows can still be numerically/physically wrong.",
            "- Low-BERTScore PASS rows can still be correct with different phrasing.",
            "",
            "## Recommended Next Metric",
            "",
            "Use the canonical text artifact for any NLI/ROSCOE experiment, after cheap lexical/BERTScore behavior is fully characterized.",
        ]
    )
    (OUTPUT_DIR / "BERTSCORE_REASONING_ONLY_CANONICAL_V2_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if any(OUTPUT_DIR.iterdir()):
        raise SystemExit(f"Output directory is not empty: {OUTPUT_DIR}")
    rows, model_hash, rescale, notes = build_output_rows(batch_size=16)
    grades = Counter(r["deterministic_grade"] for r in rows)
    if len(rows) != EXPECTED_ROWS or grades["PASS"] != EXPECTED_PASS or grades["FAIL"] != EXPECTED_FAIL:
        raise SystemExit(f"Unexpected counts: rows={len(rows)} grades={dict(grades)}")
    if len({r["scenario_id"] for r in rows}) != EXPECTED_SCENARIOS:
        raise SystemExit("Expected 32 scenarios")
    if len({r["model_name"] for r in rows}) != EXPECTED_MODELS:
        raise SystemExit("Expected 8 models")

    by_grade = summarize(rows, ("deterministic_grade",))
    by_batch = summarize(rows, ("batch",))
    by_scenario = summarize(rows, ("scenario_id", "category"))
    by_model = summarize(rows, ("model_name",))
    high_fail, low_pass = outliers(rows)
    comp_rows = comparison_rows(rows)
    changed_vs_v1 = sum(1 for r in comp_rows if f(r["v2_minus_no_final_v1_f1"]) is not None and abs(float(r["v2_minus_no_final_v1_f1"])) > 1e-9)
    corr_cols = ["deterministic_pass_binary", "bertscore_reasoning_only_v2_f1", "bertscore_no_final_v1_f1", "bertscore_full_f1", "rouge_l_f1", "chrf_score", "candidate_reference_length_ratio", "candidate_reasoning_text_length_chars", "reference_reasoning_text_length_chars"]
    corr_source = []
    comp_by_id = {r["source_run_id"]: r for r in comp_rows}
    for row in rows:
        comp = comp_by_id[row["source_run_id"]]
        corr_source.append({**row, **comp, "bertscore_reasoning_only_v2_f1": row["bert_f1"]})
    corr = correlation_matrix(corr_source, corr_cols)

    row_fields = ["row_key", "source_run_id", "batch", "scenario_id", "category", "model_name", "deterministic_grade", "deterministic_pass_binary", "extraction_status", "helper_status", "error_tags", "failed_fields", "candidate_reasoning_text_sha256", "reference_reasoning_text_sha256", "candidate_reasoning_text_length_chars", "reference_reasoning_text_length_chars", "bert_precision", "bert_recall", "bert_f1", "bertscore_model_type", "bertscore_model_hash", "rescale_with_baseline", "bertscore_full_f1", "bertscore_no_final_v1_f1", "rouge_l_f1", "chrf_score", "candidate_reference_length_ratio"]
    write_csv(OUTPUT_DIR / "bertscore_reasoning_only_canonical_v2.csv", rows, row_fields)
    (OUTPUT_DIR / "bertscore_reasoning_only_canonical_v2.json").write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(OUTPUT_DIR / "bertscore_reasoning_only_canonical_v2_by_grade.csv", by_grade)
    write_csv(OUTPUT_DIR / "bertscore_reasoning_only_canonical_v2_by_batch.csv", by_batch)
    write_csv(OUTPUT_DIR / "bertscore_reasoning_only_canonical_v2_by_scenario.csv", by_scenario)
    write_csv(OUTPUT_DIR / "bertscore_reasoning_only_canonical_v2_by_model.csv", by_model)
    write_csv(OUTPUT_DIR / "bertscore_reasoning_only_canonical_v2_outliers_high_fail.csv", high_fail)
    write_csv(OUTPUT_DIR / "bertscore_reasoning_only_canonical_v2_outliers_low_pass.csv", low_pass)
    write_csv(OUTPUT_DIR / "bertscore_reasoning_only_canonical_v2_vs_prior_metrics.csv", comp_rows)
    write_csv(OUTPUT_DIR / "bertscore_reasoning_only_canonical_v2_correlation_matrix.csv", corr, ["metric", *corr_cols])

    files = ["README.md", "BERTSCORE_REASONING_ONLY_CANONICAL_V2_REPORT.md", "bertscore_reasoning_only_canonical_v2.csv", "bertscore_reasoning_only_canonical_v2.json", "bertscore_reasoning_only_canonical_v2_by_grade.csv", "bertscore_reasoning_only_canonical_v2_by_batch.csv", "bertscore_reasoning_only_canonical_v2_by_scenario.csv", "bertscore_reasoning_only_canonical_v2_by_model.csv", "bertscore_reasoning_only_canonical_v2_outliers_high_fail.csv", "bertscore_reasoning_only_canonical_v2_outliers_low_pass.csv", "bertscore_reasoning_only_canonical_v2_vs_prior_metrics.csv", "bertscore_reasoning_only_canonical_v2_correlation_matrix.csv", "manifest.json"]
    overall = group_stats(rows)
    manifest = {
        "artifact_name": "bertscore_reasoning_only_canonical_v2",
        "created_at": utc_now(),
        "input_text_artifact": "outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv",
        "read_only": True,
        "learning_db_modified": False,
        "raw_outputs_modified": False,
        "model_calls_made": False,
        "external_llm_api_calls": False,
        "bertscore_run": True,
        "roscoe_run": False,
        "nli_run": False,
        "phase2_semantics_implemented": False,
        "expected_rows": EXPECTED_ROWS,
        "actual_rows": len(rows),
        "pass_count": grades["PASS"],
        "fail_count": grades["FAIL"],
        "candidate_final_block_removed_by_extractor_span": "252/252 in input artifact",
        "rescale_with_baseline": rescale,
        "bertscore_model_type": BERTSCORE_MODEL_TYPE,
        "bertscore_model_hash": model_hash,
        "bertscore_notes": notes,
        "metrics_computed": ["bert_precision", "bert_recall", "bert_f1"],
        "overall": overall,
        "v2_minus_no_final_v1_changed_rows": changed_vs_v1,
        "output_files": files,
    }
    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_readme(files)
    write_report(rows, by_grade, by_batch, by_scenario, by_model, high_fail, low_pass, corr, model_hash, rescale, changed_vs_v1)

    print(f"output_dir={OUTPUT_DIR}")
    print(f"row_count={len(rows)}")
    print(f"pass_count={grades['PASS']}")
    print(f"fail_count={grades['FAIL']}")
    print(f"mean_bert_f1={float(overall['mean_bert_f1']):.6f}")
    print(f"pass_fail_gap={float(overall['PASS_minus_FAIL_mean_gap']):.6f}")
    print(f"simple_effect_size={float(overall['simple_effect_size']):.6f}")
    print(f"changed_vs_no_final_v1={changed_vs_v1}")
    print(f"rescale_with_baseline={rescale}")
    print(f"model_hash={model_hash}")


if __name__ == "__main__":
    main()
