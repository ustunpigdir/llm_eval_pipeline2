# +1 Percentage-Point Numeric Tolerance Layer v1

This folder contains a read-only post-autograde categorization layer for the 252 clean structured Phase 1 hardened rows.

Original deterministic PASS/FAIL grading is unchanged.

This layer uses `effective_rel_tolerance = original_rel_tolerance + 0.01`, so 1% becomes 2% and 2% becomes 3%. This differs from the previous +25% multiplier layer, where 1% became only 1.25%.

`PLUS_ONE_PP_NUMERIC_RESCUE` is not a pass. It means a strict FAIL was purely numeric and all failed numeric fields pass under the +1 percentage-point tolerance.

Rerun with:

```bash
.venv/bin/python scripts/run_plus_one_percentage_point_numeric_tolerance_layer_v1.py
```
