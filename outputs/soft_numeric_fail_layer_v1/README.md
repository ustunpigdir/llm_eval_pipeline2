# Soft Numeric Fail Layer v1

This folder contains a read-only post-autograde categorization layer for structured Phase 1 hardened rows.

Original deterministic PASS/FAIL grading is unchanged. PASS rows are labeled `PASS_ORIGINAL`. FAIL rows are labeled `SOFT_NUMERIC_FAIL` only if every originally failed numeric mismatch passes when the original tolerance is multiplied by 1.25; otherwise they remain `HARD_FAIL`.

`+25% tolerance` means `new_tolerance = original_tolerance * 1.25`, not a flat 25% numeric error margin.

Rerun with:

```bash
.venv/bin/python scripts/run_soft_numeric_fail_layer_v1.py
```
