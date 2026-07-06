# ROSCOE Smoke Test Report

## 1. Purpose

Test whether the real Meta/ParlAI ROSCOE implementation can run locally in an isolated environment.

## 2. Environment Isolation

- `.venv_roscoe` created/used: True
- Main `.venv` modified: false
- Python executable: `/Users/upigdir/Desktop/Pipeline SQL proj/.venv_roscoe/bin/python`
- Python version: `Python 3.12.13`

## 3. Dependency Path Attempted

Minimal dependency route was attempted first. The install command failed because `simcse` pulled an old SciPy/Numpy build path incompatible with Python 3.12.

## 4. ParlAI/ROSCOE Source Used

- Source: `https://github.com/facebookresearch/ParlAI`
- Commit: `6c802418e93a51cbb746b011439ab783dd136de8`
- Runtime source directory: `tmp/roscoe_parlai_runtime`
- Files used: projects/roscoe/README.md, projects/roscoe/score.py, projects/roscoe/roscoe.py, projects/roscoe/utils.py, tests/nightly/cpu/test_roscoe.py

## 5. Import Results

Import status: `failed`

See `roscoe_smoke_import_log.txt`.

## 6. Smoke Test Input Pairs

Three required toy pairs were registered in `roscoe_smoke_test_results.json`.

## 7. Metrics Available

None; import failed before ROSCOE could expose runnable metrics in `.venv_roscoe`.

## 8. Smoke Test Results

- Status: `failed`
- Pairs attempted: 3
- Pairs scored: 0

## 9. Non-Degeneracy Check

- good vs unrelated: `not_available`
- arithmetic contradiction behavior: `not_available`

## 10. Runtime and Resource Notes

No benchmark rows were scored. No Hugging Face model weights were downloaded by the smoke runner because dependency import failed before scoring.

## 11. Whether Pilot 30 Rows Is Safe

No. Pilot 30 is not safe until `.venv_roscoe` can import `projects.roscoe.score` and score all three toy pairs.

## 12. Limitations

- Python 3.10/3.11 was not available on PATH.
- Python 3.12 dependency resolution failed at `simcse`/old `scipy`.
- No fake or substitute ROSCOE metrics were produced.

## 13. Recommended Next Step

Retry in an isolated Python 3.10 or 3.11 environment, or patch a local copy of ParlAI ROSCOE to make `simcse` optional when using sentence-transformer-only metrics. Do not proceed to pilot rows until the three-pair smoke test returns finite numeric scores.
