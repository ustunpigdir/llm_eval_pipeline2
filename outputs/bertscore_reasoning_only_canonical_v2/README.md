# BERTScore Reasoning-Only Canonical v2

This folder contains the corrected reasoning-only BERTScore run using the canonical text artifact.

v2 exists because no-final-block v1 used a separate regex remover and missed 5 candidate final-answer blocks. This run reads `candidate_reasoning_text` and `reference_reasoning_text` directly from `metric_text_artifacts_v1`.

It does not change grading, call LLM APIs, rerun models, overwrite old BERTScore outputs, or implement Phase 2 semantics.

Rerun with:

```bash
.venv/bin/python scripts/run_bertscore_reasoning_only_canonical_v2.py
```

BERTScore is descriptive and secondary; deterministic PASS/FAIL remains the correctness anchor.

Files:
- `README.md`
- `BERTSCORE_REASONING_ONLY_CANONICAL_V2_REPORT.md`
- `bertscore_reasoning_only_canonical_v2.csv`
- `bertscore_reasoning_only_canonical_v2.json`
- `bertscore_reasoning_only_canonical_v2_by_grade.csv`
- `bertscore_reasoning_only_canonical_v2_by_batch.csv`
- `bertscore_reasoning_only_canonical_v2_by_scenario.csv`
- `bertscore_reasoning_only_canonical_v2_by_model.csv`
- `bertscore_reasoning_only_canonical_v2_outliers_high_fail.csv`
- `bertscore_reasoning_only_canonical_v2_outliers_low_pass.csv`
- `bertscore_reasoning_only_canonical_v2_vs_prior_metrics.csv`
- `bertscore_reasoning_only_canonical_v2_correlation_matrix.csv`
- `manifest.json`
