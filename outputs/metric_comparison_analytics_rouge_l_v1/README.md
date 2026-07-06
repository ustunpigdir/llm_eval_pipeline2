# ROUGE-L Metric v1

This folder contains deterministic ROUGE-L scores computed from canonical reasoning-only text.

It uses `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv` as the only text source.

It does not change grading, modify raw outputs, call APIs, run BERTScore, run ROSCOE/NLI, or implement Phase 2 semantics.

Rerun with:

```bash
.venv/bin/python scripts/run_rouge_l_metric_v1.py
```

Interpret ROUGE-L as lexical sequence overlap, not correctness.

Files:
- `README.md`
- `ROUGE_L_METRIC_REPORT.md`
- `rouge_l_row_scores.csv`
- `rouge_l_row_scores.json`
- `rouge_l_by_grade.csv`
- `rouge_l_by_batch.csv`
- `rouge_l_by_scenario.csv`
- `rouge_l_by_model.csv`
- `rouge_l_outliers_high_rouge_fail.csv`
- `rouge_l_outliers_low_rouge_pass.csv`
- `rouge_l_vs_existing_metrics.csv`
- `rouge_l_correlation_matrix.csv`
- `manifest.json`
