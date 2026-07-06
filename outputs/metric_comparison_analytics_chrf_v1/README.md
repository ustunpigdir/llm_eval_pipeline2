# chrF Metric v1

This folder contains deterministic chrF scores computed from canonical reasoning-only text.

It uses `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv` as the only text source.

It does not change grading, modify raw outputs, call APIs, run BERTScore, run ROSCOE/NLI, or implement Phase 2 semantics.

Rerun with:

```bash
.venv/bin/python scripts/run_chrf_metric_v1.py
```

Interpret chrF as character n-gram overlap, not correctness.

Files:
- `README.md`
- `CHRF_METRIC_REPORT.md`
- `chrf_row_scores.csv`
- `chrf_row_scores.json`
- `chrf_by_grade.csv`
- `chrf_by_batch.csv`
- `chrf_by_scenario.csv`
- `chrf_by_model.csv`
- `chrf_outliers_high_chrf_fail.csv`
- `chrf_outliers_low_chrf_pass.csv`
- `chrf_vs_existing_metrics.csv`
- `chrf_correlation_matrix.csv`
- `manifest.json`
