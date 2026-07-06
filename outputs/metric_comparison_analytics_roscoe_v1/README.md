# ROSCOE Metric v1

This folder is the ROSCOE metric-comparison layer setup artifact.

ROSCOE was actually run: `False`.
Run mode: `setup_only`.

Input text source:
- `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv`

This does not change grading, modify raw outputs, call LLM APIs, run BERTScore, run NLI, or implement Phase 2 semantics.

Rerun setup inspection with:

```bash
.venv/bin/python scripts/run_roscoe_metric_v1.py
```

Interpretation: ROSCOE, when available, should be treated as a reasoning-trace diagnostic, not a correctness gate.
