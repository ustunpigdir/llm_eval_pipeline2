# Metric Comparison Analytics v1

This folder is a read-only analytics layer for comparing saved automatic metrics with frozen deterministic labels.

It does not change grades, implement Phase 2 semantics, rerun models, call LLM APIs, rerun BERTScore, or modify `learning.db`.

Frozen inputs include the Phase-1-hardened structured summaries, V2-V5 clean autograde files, and the two saved BERTScore runs.

Rerun with:

```bash
.venv/bin/python scripts/build_metric_comparison_analytics_v1.py
```

Current metrics: full-answer BERTScore F1, no-final-block BERTScore F1, and candidate/reference length ratio.

ROUGE-L, chrF, ROSCOE, NLI, and human-label alignment should be added later from an artifact that safely exposes candidate/reference text and aligned human labels.

Outputs:
- `README.md`
- `METRIC_COMPARISON_ANALYTICS_REPORT.md`
- `metric_comparison_base_dataset.csv`
- `metric_comparison_base_dataset.json`
- `metric_comparison_by_metric.csv`
- `metric_comparison_by_grade.csv`
- `metric_comparison_by_scenario.csv`
- `metric_comparison_by_model.csv`
- `metric_comparison_outliers_high_metric_fail.csv`
- `metric_comparison_outliers_low_metric_pass.csv`
- `metric_correlation_matrix.csv`
- `manifest.json`
