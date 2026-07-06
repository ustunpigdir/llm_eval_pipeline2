# Large Numeric Failure >100% v1

This folder inspects numeric comparisons where `relative_error > 1.0`, meaning the extracted value is more than 100% away from the gold value.

The derived ratio diagnostics include extracted/expected ratios, log10 magnitude ratios, sign checks, common-factor checks, reciprocal checks, unit-scale checks, and same-row wrong-field-scale checks.

This does not change deterministic grading. Use `large_numeric_failure_gate_candidates.csv` to decide which preliminary gate ideas deserve manual review.

Rerun with:

```bash
.venv/bin/python scripts/run_large_numeric_failure_gt100pct_v1.py
```
