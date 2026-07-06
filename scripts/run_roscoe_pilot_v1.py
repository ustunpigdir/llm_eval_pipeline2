#!/usr/bin/env python3
"""Run the 30-row ROSCOE pilot using the isolated py311 environment."""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import random
import statistics
import subprocess
import time
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "metric_comparison_analytics_roscoe_pilot_v1"
ROSCOE_PY = ROOT / ".venv_roscoe_py311" / "bin" / "python"
ROSCOE_RUNTIME = ROOT / "tmp" / "roscoe_parlai_runtime_v2"

CANONICAL = ROOT / "outputs" / "metric_text_artifacts_v1" / "canonical_reasoning_text_dataset.csv"
BERT = ROOT / "outputs" / "bertscore_reasoning_only_canonical_v2" / "bertscore_reasoning_only_canonical_v2.csv"
ROUGE = ROOT / "outputs" / "metric_comparison_analytics_rouge_l_v1" / "rouge_l_row_scores.csv"
CHRF = ROOT / "outputs" / "metric_comparison_analytics_chrf_v1" / "chrf_row_scores.csv"
BASE = ROOT / "outputs" / "metric_comparison_analytics_v1" / "metric_comparison_base_dataset.csv"

SEED = 20260706
ROSCOE_METRICS = [
    "informativeness_chain",
    "informativeness_step",
    "reasoning_alignment",
    "repetition_step",
    "semantic_coverage_chain",
    "semantic_coverage_step",
]
AGGREGATE_METRICS = [
    "informativeness_chain",
    "informativeness_step",
    "reasoning_alignment",
    "semantic_coverage_chain",
    "semantic_coverage_step",
]
SELECTED_METRIC = "reasoning_alignment"

PROTECTED_PATHS = [
    "learning.db",
    "outputs/structured_prompt_pilot_v2/structured_prompt_pilot_v2_runs.json",
    "outputs/structured_prompt_pilot_v3/structured_prompt_pilot_v3_runs.json",
    "outputs/structured_prompt_pilot_v4/structured_prompt_pilot_v4_runs.json",
    "outputs/structured_prompt_pilot_v5/structured_prompt_pilot_v5_runs.json",
    "outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def fnum(value: Any) -> float:
    try:
        if value is None or value == "":
            return float("nan")
        return float(value)
    except Exception:
        return float("nan")


def finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(value)


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def protected_stats() -> dict[str, dict[str, int]]:
    stats = {}
    for rel in PROTECTED_PATHS:
        path = ROOT / rel
        if path.exists():
            st = path.stat()
            stats[rel] = {"mtime": int(st.st_mtime), "size": st.st_size}
    return stats


def pearson(xs: list[float], ys: list[float]) -> float:
    pairs = [(x, y) for x, y in zip(xs, ys) if math.isfinite(x) and math.isfinite(y)]
    if len(pairs) < 2:
        return float("nan")
    xvals = [p[0] for p in pairs]
    yvals = [p[1] for p in pairs]
    mx = statistics.mean(xvals)
    my = statistics.mean(yvals)
    num = sum((x - mx) * (y - my) for x, y in pairs)
    denx = math.sqrt(sum((x - mx) ** 2 for x in xvals))
    deny = math.sqrt(sum((y - my) ** 2 for y in yvals))
    if denx == 0 or deny == 0:
        return float("nan")
    return num / (denx * deny)


def median(values: list[float]) -> float:
    vals = [v for v in values if math.isfinite(v)]
    return statistics.median(vals) if vals else float("nan")


def mean(values: list[float]) -> float:
    vals = [v for v in values if math.isfinite(v)]
    return statistics.mean(vals) if vals else float("nan")


def simple_effect_size(pass_vals: list[float], fail_vals: list[float]) -> float:
    p = [v for v in pass_vals if math.isfinite(v)]
    f = [v for v in fail_vals if math.isfinite(v)]
    if len(p) < 2 or len(f) < 2:
        return float("nan")
    pooled = math.sqrt((statistics.variance(p) + statistics.variance(f)) / 2)
    if pooled == 0:
        return float("nan")
    return (statistics.mean(p) - statistics.mean(f)) / pooled


def metric_summary(rows: list[dict[str, Any]], metric: str) -> dict[str, Any]:
    values = [fnum(r.get(metric)) for r in rows]
    pass_vals = [fnum(r.get(metric)) for r in rows if r.get("deterministic_grade") == "PASS"]
    fail_vals = [fnum(r.get(metric)) for r in rows if r.get("deterministic_grade") == "FAIL"]
    pass_mean = mean(pass_vals)
    fail_mean = mean(fail_vals)
    return {
        "metric": metric,
        "row_count": sum(1 for v in values if math.isfinite(v)),
        "pass_count": sum(1 for r in rows if r.get("deterministic_grade") == "PASS"),
        "fail_count": sum(1 for r in rows if r.get("deterministic_grade") == "FAIL"),
        "mean": mean(values),
        "median": median(values),
        "min": min([v for v in values if math.isfinite(v)], default=float("nan")),
        "max": max([v for v in values if math.isfinite(v)], default=float("nan")),
        "PASS_mean": pass_mean,
        "FAIL_mean": fail_mean,
        "PASS_minus_FAIL_mean_gap": pass_mean - fail_mean if math.isfinite(pass_mean) and math.isfinite(fail_mean) else float("nan"),
        "simple_effect_size": simple_effect_size(pass_vals, fail_vals),
        "correlation_with_deterministic_pass": pearson(
            [fnum(r.get("deterministic_pass_binary")) for r in rows],
            values,
        ),
    }


def load_inputs() -> tuple[list[dict[str, Any]], dict[str, dict[str, str]]]:
    canonical = read_csv(CANONICAL)
    by_id: dict[str, dict[str, Any]] = {r["source_run_id"]: dict(r) for r in canonical}
    sources = {
        "bert": {r["source_run_id"]: r for r in read_csv(BERT)},
        "rouge": {r["source_run_id"]: r for r in read_csv(ROUGE)},
        "chrf": {r["source_run_id"]: r for r in read_csv(CHRF)},
        "base": {r["source_run_id"]: r for r in read_csv(BASE)},
    }
    for sid, row in by_id.items():
        bert = sources["bert"].get(sid, {})
        rouge = sources["rouge"].get(sid, {})
        chrf = sources["chrf"].get(sid, {})
        base = sources["base"].get(sid, {})
        row["bertscore_reasoning_only_v2_f1"] = bert.get("bert_f1", "")
        row["rouge_l_f1"] = rouge.get("rouge_l_f1") or bert.get("rouge_l_f1") or base.get("rouge_l_f1", "")
        row["chrf_score"] = chrf.get("chrf_score") or bert.get("chrf_score") or base.get("chrf_score", "")
        row["candidate_reference_length_ratio"] = bert.get("candidate_reference_length_ratio") or rouge.get("candidate_reference_length_ratio") or chrf.get("candidate_reference_length_ratio") or base.get("candidate_reference_length_ratio", "")
    return list(by_id.values()), sources


def select_sample(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    fail_sorted = sorted(
        [r for r in rows if r["deterministic_grade"] == "FAIL"],
        key=lambda r: fnum(r["bertscore_reasoning_only_v2_f1"]),
        reverse=True,
    )
    pass_sorted = sorted(
        [r for r in rows if r["deterministic_grade"] == "PASS"],
        key=lambda r: fnum(r["bertscore_reasoning_only_v2_f1"]),
    )
    selected: list[dict[str, Any]] = []
    used: set[str] = set()
    for i, row in enumerate(fail_sorted[:10], start=1):
        out = dict(row)
        out["sample_group"] = "high_overlap_fail"
        out["sample_rank_or_seed"] = i
        out["reason_selected"] = "top_10_FAIL_by_bertscore_reasoning_only_v2_f1"
        selected.append(out)
        used.add(out["source_run_id"])
    for i, row in enumerate(pass_sorted[:10], start=1):
        out = dict(row)
        out["sample_group"] = "low_overlap_pass"
        out["sample_rank_or_seed"] = i
        out["reason_selected"] = "bottom_10_PASS_by_bertscore_reasoning_only_v2_f1"
        selected.append(out)
        used.add(out["source_run_id"])

    remaining = [r for r in rows if r["source_run_id"] not in used]
    rng = random.Random(SEED)
    buckets: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in remaining:
        buckets.setdefault((row["deterministic_grade"], row["batch"]), []).append(row)
    normal: list[dict[str, Any]] = []
    for key in sorted(buckets):
        rng.shuffle(buckets[key])
    target_order = sorted(buckets)
    while len(normal) < 10 and any(buckets.values()):
        for key in target_order:
            if buckets[key] and len(normal) < 10:
                normal.append(buckets[key].pop())
    for i, row in enumerate(normal, start=1):
        out = dict(row)
        out["sample_group"] = "stratified_normal"
        out["sample_rank_or_seed"] = SEED
        out["reason_selected"] = f"deterministic_seed_{SEED}_stratified_by_grade_and_batch_pick_{i}"
        selected.append(out)
    return selected


def score_with_roscoe(sample: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], str, float]:
    payload = [
        {
            "source_run_id": row["source_run_id"],
            "candidate_text": row["candidate_reasoning_text"],
            "reference_text": row["reference_reasoning_text"],
        }
        for row in sample
    ]
    input_path = OUT_DIR / "roscoe_pilot_scoring_input.json"
    output_path = OUT_DIR / "roscoe_pilot_scoring_output.json"
    write_json(input_path, payload)
    code = f"""
import json
import sys
sys.path.insert(0, {str(ROSCOE_RUNTIME)!r})
from projects.roscoe.score import Chain, Evaluator
import projects.roscoe.score as score

inp = {str(input_path)!r}
outp = {str(output_path)!r}
rows = json.load(open(inp, encoding="utf-8"))
score_types = [
    score.INFORM_CHAIN,
    score.INFORM_STEP,
    score.CHAIN_ALIGNMENT,
    score.REPETITION_SENT,
    score.SEMANTIC_COVERAGE_CHAIN,
    score.SEMANTIC_COVERAGE_STEP,
]
def steps(text):
    return [s.strip() for s in text.split(".") if s.strip()]
hypos = [Chain(steps(r["candidate_text"])) for r in rows]
refs = [Chain(steps(r["reference_text"])) for r in rows]
contexts = refs
ev = Evaluator(hypos=hypos, context=contexts, references=refs, score_types=score_types, transformer_model="all-MiniLM-L6-v2")
scores = ev.evaluate(score_types=score_types)
out = []
for i, row in enumerate(rows):
    metrics = {{}}
    for name, values in scores.items():
        val = values[i]
        metrics[name] = val if isinstance(val, str) else float(val)
    out.append({{"source_run_id": row["source_run_id"], "status": "scored", "metrics": metrics, "error": ""}})
json.dump(out, open(outp, "w", encoding="utf-8"), indent=2)
"""
    start = time.time()
    env = dict(os.environ)
    env["HF_HUB_OFFLINE"] = "1"
    env["TRANSFORMERS_OFFLINE"] = "1"
    proc = subprocess.run(
        [str(ROSCOE_PY), "-c", code],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        timeout=1800,
        env=env,
    )
    runtime = time.time() - start
    log = {
        "command": f"{ROSCOE_PY} -c <roscoe pilot scorer>",
        "returncode": proc.returncode,
        "stdout": proc.stdout[-8000:],
        "stderr": proc.stderr[-8000:],
        "duration_seconds": runtime,
    }
    write_json(OUT_DIR / "roscoe_pilot_runtime_log.json", log)
    if proc.returncode != 0:
        return [
            {"source_run_id": row["source_run_id"], "status": "failed", "metrics": {}, "error": proc.stderr[-2000:] or proc.stdout[-2000:]}
            for row in sample
        ], "failed", runtime
    return json.loads(output_path.read_text(encoding="utf-8")), "passed", runtime


def enrich_scores(sample: list[dict[str, Any]], scores: list[dict[str, Any]]) -> list[dict[str, Any]]:
    score_by_id = {s["source_run_id"]: s for s in scores}
    rows = []
    for row in sample:
        out = dict(row)
        score = score_by_id.get(row["source_run_id"], {"status": "failed", "metrics": {}, "error": "missing score"})
        metrics = score.get("metrics", {})
        for metric in ROSCOE_METRICS:
            out[metric] = metrics.get(metric, "")
        vals = [fnum(out.get(metric)) for metric in AGGREGATE_METRICS]
        vals = [v for v in vals if math.isfinite(v)]
        out["roscoe_available_mean"] = sum(vals) / len(vals) if vals else ""
        out["selected_roscoe_metric_name"] = SELECTED_METRIC
        out["selected_roscoe_score"] = out.get(SELECTED_METRIC, "")
        out["roscoe_scoring_status"] = score.get("status", "failed")
        out["roscoe_error_if_any"] = score.get("error", "")
        out["candidate_reasoning_text_length_chars"] = out.get("candidate_reasoning_text_length_chars") or len(out.get("candidate_reasoning_text", ""))
        out["reference_reasoning_text_length_chars"] = out.get("reference_reasoning_text_length_chars") or len(out.get("reference_reasoning_text", ""))
        if out.get("candidate_reasoning_text_sha256") != sha256(out.get("candidate_reasoning_text", "")):
            out["roscoe_error_if_any"] = (out["roscoe_error_if_any"] + " candidate_hash_mismatch").strip()
        if out.get("reference_reasoning_text_sha256") != sha256(out.get("reference_reasoning_text", "")):
            out["roscoe_error_if_any"] = (out["roscoe_error_if_any"] + " reference_hash_mismatch").strip()
        rows.append(out)
    return rows


def build_correlations(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cols = [
        "deterministic_pass_binary",
        "selected_roscoe_score",
        "roscoe_available_mean",
        *ROSCOE_METRICS,
        "bertscore_reasoning_only_v2_f1",
        "rouge_l_f1",
        "chrf_score",
        "candidate_reference_length_ratio",
        "candidate_reasoning_text_length_chars",
        "reference_reasoning_text_length_chars",
    ]
    matrix = []
    for c1 in cols:
        row = {"metric": c1}
        xs = [fnum(r.get(c1)) for r in rows]
        for c2 in cols:
            row[c2] = pearson(xs, [fnum(r.get(c2)) for r in rows])
        matrix.append(row)
    return matrix


def group_summary(rows: list[dict[str, Any]], group_col: str) -> list[dict[str, Any]]:
    out = []
    metrics = [*ROSCOE_METRICS, "roscoe_available_mean", "selected_roscoe_score"]
    groups = sorted(set(r[group_col] for r in rows))
    for group in groups:
        subset = [r for r in rows if r[group_col] == group]
        for metric in metrics:
            summary = metric_summary(subset, metric)
            summary[group_col] = group
            out.append(summary)
    return out


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    before = protected_stats()
    created_at = dt.datetime.now(dt.timezone.utc).isoformat()
    all_rows, _sources = load_inputs()
    sample = select_sample(all_rows)

    sample_fields = [
        "sample_group", "sample_rank_or_seed", "source_run_id", "batch", "scenario_id", "category", "model_name",
        "deterministic_grade", "bertscore_reasoning_only_v2_f1", "rouge_l_f1", "chrf_score", "reason_selected",
    ]
    write_csv(OUT_DIR / "roscoe_pilot_sample_selection.csv", sample, sample_fields)

    scores, scoring_status, runtime = score_with_roscoe(sample)
    rows = enrich_scores(sample, scores)
    pilot_rows_scored = sum(1 for r in rows if r["roscoe_scoring_status"] == "scored")
    metrics_available = [m for m in ROSCOE_METRICS if any(math.isfinite(fnum(r.get(m))) for r in rows)]
    selected_non_degenerate = len({fnum(r.get(SELECTED_METRIC)) for r in rows if math.isfinite(fnum(r.get(SELECTED_METRIC)))}) > 1
    pilot_status = "passed" if pilot_rows_scored == 30 and selected_non_degenerate else ("partial" if pilot_rows_scored else "failed")
    full_recommended = pilot_status == "passed" and runtime < 900

    row_fields = [
        "row_key", "source_run_id", "sample_group", "sample_rank_or_seed", "batch", "scenario_id", "category", "model_name",
        "deterministic_grade", "deterministic_pass_binary", "extraction_status", "helper_status", "error_tags", "failed_fields",
        "candidate_reasoning_text_sha256", "reference_reasoning_text_sha256",
        "candidate_reasoning_text_length_chars", "reference_reasoning_text_length_chars",
        *ROSCOE_METRICS,
        "roscoe_available_mean", "selected_roscoe_metric_name", "selected_roscoe_score", "roscoe_scoring_status", "roscoe_error_if_any",
        "bertscore_reasoning_only_v2_f1", "rouge_l_f1", "chrf_score", "candidate_reference_length_ratio",
    ]
    write_csv(OUT_DIR / "roscoe_pilot_row_scores.csv", rows, row_fields)
    write_json(OUT_DIR / "roscoe_pilot_row_scores.json", rows)

    summary_metrics = [*ROSCOE_METRICS, "roscoe_available_mean", "selected_roscoe_score"]
    by_grade = [metric_summary(rows, m) for m in summary_metrics]
    summary_fields = [
        "metric", "row_count", "pass_count", "fail_count", "mean", "median", "min", "max",
        "PASS_mean", "FAIL_mean", "PASS_minus_FAIL_mean_gap", "simple_effect_size", "correlation_with_deterministic_pass",
    ]
    write_csv(OUT_DIR / "roscoe_pilot_by_grade.csv", by_grade, summary_fields)
    by_group = group_summary(rows, "sample_group")
    write_csv(OUT_DIR / "roscoe_pilot_by_sample_group.csv", by_group, ["sample_group", *summary_fields])

    corr = build_correlations(rows)
    corr_fields = list(corr[0].keys()) if corr else ["metric"]
    write_csv(OUT_DIR / "roscoe_pilot_correlation_matrix.csv", corr, corr_fields)

    vs_fields = [
        "source_run_id", "sample_group", "deterministic_grade", "selected_roscoe_metric_name", "selected_roscoe_score",
        "roscoe_available_mean", *ROSCOE_METRICS, "bertscore_reasoning_only_v2_f1", "rouge_l_f1", "chrf_score",
        "candidate_reference_length_ratio",
    ]
    write_csv(OUT_DIR / "roscoe_pilot_vs_existing_metrics.csv", rows, vs_fields)

    outlier_fields = [
        "source_run_id", "sample_group", "batch", "scenario_id", "category", "model_name", "deterministic_grade",
        "error_tags", "failed_fields", "selected_roscoe_metric_name", "selected_roscoe_score", "roscoe_available_mean",
        "bertscore_reasoning_only_v2_f1", "rouge_l_f1", "chrf_score",
    ]
    high_fail = sorted([r for r in rows if r["deterministic_grade"] == "FAIL"], key=lambda r: fnum(r["selected_roscoe_score"]), reverse=True)[:10]
    low_pass = sorted([r for r in rows if r["deterministic_grade"] == "PASS"], key=lambda r: fnum(r["selected_roscoe_score"]))[:10]
    write_csv(OUT_DIR / "roscoe_pilot_outliers_high_roscoe_fail.csv", high_fail, outlier_fields)
    write_csv(OUT_DIR / "roscoe_pilot_outliers_low_roscoe_pass.csv", low_pass, outlier_fields)

    pass_count = sum(1 for r in rows if r["deterministic_grade"] == "PASS")
    fail_count = sum(1 for r in rows if r["deterministic_grade"] == "FAIL")
    group_counts = {g: sum(1 for r in rows if r["sample_group"] == g) for g in sorted(set(r["sample_group"] for r in rows))}
    selected_summary = next(s for s in by_grade if s["metric"] == "selected_roscoe_score")
    selected_corr_existing = {
        "bertscore_v2": pearson([fnum(r["selected_roscoe_score"]) for r in rows], [fnum(r["bertscore_reasoning_only_v2_f1"]) for r in rows]),
        "rouge_l": pearson([fnum(r["selected_roscoe_score"]) for r in rows], [fnum(r["rouge_l_f1"]) for r in rows]),
        "chrf": pearson([fnum(r["selected_roscoe_score"]) for r in rows], [fnum(r["chrf_score"]) for r in rows]),
    }

    readme = """# ROSCOE Pilot v1

This folder contains a 30-row ROSCOE pilot over canonical reasoning-only text.

It uses the isolated `.venv_roscoe_py311` environment and the Meta/ParlAI minimal embedding-metric route validated in smoke v2. It does not change grading, modify raw outputs, run BERTScore, call LLM APIs, or implement Phase 2 semantics.

Rerun with:

```bash
.venv/bin/python scripts/run_roscoe_pilot_v1.py
```

Interpret these results as a biased pilot only, not a full benchmark conclusion.
"""
    (OUT_DIR / "README.md").write_text(readme, encoding="utf-8")

    report = f"""# ROSCOE Pilot Report

## 1. Purpose

Score a controlled 30-row pilot from canonical reasoning-only benchmark text using Meta/ParlAI ROSCOE embedding metrics.

## 2. Why Pilot Follows Smoke v2

Smoke v2 passed in `.venv_roscoe_py311` with three toy pairs and finite numeric embedding metrics.

## 3. Inputs

- Text source: `{CANONICAL.relative_to(ROOT)}`
- Existing metrics aligned by `source_run_id`: BERTScore v2, ROUGE-L, chrF, base comparison dataset.

## 4. Pilot Sample Construction

- high_overlap_fail: {group_counts.get('high_overlap_fail', 0)}
- low_overlap_pass: {group_counts.get('low_overlap_pass', 0)}
- stratified_normal: {group_counts.get('stratified_normal', 0)}
- deterministic seed: {SEED}

## 5. ROSCOE Implementation Used

Meta/ParlAI `projects/roscoe/score.py`, via `tmp/roscoe_parlai_runtime_v2`, executed with `.venv_roscoe_py311`.

## 6. Metrics Available

{', '.join(metrics_available)}

## 7. Row Coverage

- attempted: 30
- scored: {pilot_rows_scored}
- PASS: {pass_count}
- FAIL: {fail_count}

## 8. Overall Pilot Summary

- pilot_status: `{pilot_status}`
- selected metric: `{SELECTED_METRIC}`
- roscoe_available_mean excludes `repetition_step` because its direction is less clearly quality-positive than the semantic/informativeness metrics.

## 9. Pilot Summary By Deterministic Grade

Selected metric PASS mean: {selected_summary['PASS_mean']:.6f}

Selected metric FAIL mean: {selected_summary['FAIL_mean']:.6f}

PASS-minus-FAIL gap: {selected_summary['PASS_minus_FAIL_mean_gap']:.6f}

Effect size: {selected_summary['simple_effect_size']:.6f}

Correlation with deterministic pass: {selected_summary['correlation_with_deterministic_pass']:.6f}

## 10. Pilot Summary By Sample Group

See `roscoe_pilot_by_sample_group.csv`.

## 11. High-ROSCOE FAIL Examples

{chr(10).join(f"- {r['source_run_id']} | {r['scenario_id']} | {r['model_name']} | {fnum(r['selected_roscoe_score']):.6f}" for r in high_fail[:5])}

## 12. Low-ROSCOE PASS Examples

{chr(10).join(f"- {r['source_run_id']} | {r['scenario_id']} | {r['model_name']} | {fnum(r['selected_roscoe_score']):.6f}" for r in low_pass[:5])}

## 13. Correlation With Deterministic PASS/FAIL

{selected_summary['correlation_with_deterministic_pass']:.6f}

## 14. Comparison With BERTScore v2

Pilot selected-ROSCOE correlation with BERTScore v2 F1: {selected_corr_existing['bertscore_v2']:.6f}. Full-dataset BERTScore baseline gap/effect/correlation: 0.070603 / 0.199942 / 0.099199.

## 15. Comparison With ROUGE-L

Pilot selected-ROSCOE correlation with ROUGE-L F1: {selected_corr_existing['rouge_l']:.6f}. Full-dataset ROUGE-L baseline gap/effect/correlation: 0.044352 / 0.209217 / 0.103759.

## 16. Comparison With chrF

Pilot selected-ROSCOE correlation with chrF: {selected_corr_existing['chrf']:.6f}. Full-dataset chrF baseline gap/effect/correlation: 0.065268 / 0.352804 / 0.172891.

## 17. Runtime/Resource Notes

Runtime seconds: {runtime:.3f}. No benchmark model calls or external LLM API calls were made.

## 18. Whether Full 252-Row ROSCOE Run Is Recommended

{full_recommended}

## 19. Limitations

This is a biased 30-row pilot. It uses only embedding metrics and excludes NLI, PPL, and grammar metrics. Deterministic PASS/FAIL remains the correctness anchor.

## 20. Recommended Next Step

{"Run the full 252-row ROSCOE embedding-metric layer." if full_recommended else "Do not run full 252 yet; inspect pilot failures or runtime first."}
"""
    (OUT_DIR / "ROSCOE_PILOT_REPORT.md").write_text(report, encoding="utf-8")

    after = protected_stats()
    manifest = {
        "artifact_name": "roscoe_pilot_v1",
        "created_at": created_at,
        "input_text_artifact": str(CANONICAL.relative_to(ROOT)),
        "roscoe_environment": ".venv_roscoe_py311",
        "read_only_project_data": True,
        "main_venv_modified": False,
        "learning_db_modified": before.get("learning.db") != after.get("learning.db"),
        "raw_outputs_modified": any(before.get(p) != after.get(p) for p in PROTECTED_PATHS if p != "learning.db"),
        "frozen_metric_artifacts_modified": before.get("outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv") != after.get("outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv"),
        "benchmark_rows_scored": 30,
        "full_252_run_completed": False,
        "model_calls_made": False,
        "external_llm_api_calls": False,
        "bertscore_run": False,
        "phase2_semantics_implemented": False,
        "sample_groups": group_counts,
        "deterministic_random_seed": SEED,
        "metrics_available": metrics_available,
        "selected_roscoe_metric": SELECTED_METRIC,
        "roscoe_available_mean_definition": "mean over informativeness_chain, informativeness_step, reasoning_alignment, semantic_coverage_chain, semantic_coverage_step; excludes repetition_step",
        "pilot_rows_attempted": 30,
        "pilot_rows_scored": pilot_rows_scored,
        "pilot_status": pilot_status,
        "full_252_recommended": full_recommended,
        "runtime_seconds": runtime,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "selected_metric_summary": selected_summary,
        "correlations_with_existing": selected_corr_existing,
        "output_files": [
            "README.md",
            "ROSCOE_PILOT_REPORT.md",
            "roscoe_pilot_sample_selection.csv",
            "roscoe_pilot_row_scores.csv",
            "roscoe_pilot_row_scores.json",
            "roscoe_pilot_by_grade.csv",
            "roscoe_pilot_by_sample_group.csv",
            "roscoe_pilot_vs_existing_metrics.csv",
            "roscoe_pilot_correlation_matrix.csv",
            "roscoe_pilot_outliers_high_roscoe_fail.csv",
            "roscoe_pilot_outliers_low_roscoe_pass.csv",
            "manifest.json",
        ],
    }
    write_json(OUT_DIR / "manifest.json", manifest)

    print(f"pilot_status={pilot_status}")
    print(f"pilot_rows_attempted=30")
    print(f"pilot_rows_scored={pilot_rows_scored}")
    print(f"pass_count={pass_count}")
    print(f"fail_count={fail_count}")
    print(f"selected_roscoe_metric={SELECTED_METRIC}")
    print(f"PASS_minus_FAIL_gap={selected_summary['PASS_minus_FAIL_mean_gap']}")
    print(f"simple_effect_size={selected_summary['simple_effect_size']}")
    print(f"correlation_with_deterministic_pass={selected_summary['correlation_with_deterministic_pass']}")
    print(f"full_252_recommended={full_recommended}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
