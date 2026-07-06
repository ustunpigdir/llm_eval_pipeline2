# Python 3.11 Provision Report

## 1. Purpose

Provide a Python 3.11 runtime for the isolated Meta/ParlAI ROSCOE smoke test.

## 2. Previous ROSCOE Blocker

ROSCOE smoke v2 could not run because no Python 3.10/3.11 runtime was available. Python 3.12 hit the `simcse`/old SciPy dependency path.

## 3. Discovery Results

See `python311_discovery_log.txt`.

## 4. Install Method Used

- Python 3.11 found before install: False
- Install attempted: True
- Install method: `homebrew`

## 5. Python 3.11 Executable Selected

- Executable: `python3.11`
- Version: `Python 3.11.15`

## 6. Validation Results

- Validation status: True
- Temporary venv created: True
- Temporary venv deleted: True

See `python311_validation_log.txt`.

## 7. Whether ROSCOE Smoke v2 Can Now Be Retried

True

## 8. What Was Not Changed

- Main `.venv` modified: false
- ROSCOE dependencies installed: false
- `learning.db` modified: false
- Raw outputs modified: false
- Frozen metric artifacts modified: false
- Benchmark rows scored: false
- Model/API calls made: false
- BERTScore run: false
- Phase 2 semantics implemented: false

## 9. Recommended Next Command

```bash
.venv/bin/python scripts/run_roscoe_smoke_test_v2_py310_or_311.py
```
