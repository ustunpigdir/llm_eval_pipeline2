# Numeric Relative-Error Distribution v1

This folder contains a read-only diagnostic layer for numeric distance between extracted model final-answer fields and gold numeric values.

`rel_error = abs(extracted_value - expected_value) / abs(expected_value)`.

This does not change deterministic grading and does not create new pass/fail categories.

Use the bin, percentile, scenario, model, and field summaries to design future tolerance or categorization layers.

Rerun with:

```bash
.venv/bin/python scripts/run_numeric_relative_error_distribution_v1.py
```
