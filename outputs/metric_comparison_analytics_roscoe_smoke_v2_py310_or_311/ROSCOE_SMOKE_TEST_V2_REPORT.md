# ROSCOE Smoke Test v2 Report

## 1. Purpose

Retry the Meta/ParlAI ROSCOE smoke test using Route A: a compatible Python 3.10 or 3.11 isolated runtime.

## 2. Why v2 Exists

Smoke v1 used Python 3.12 and was blocked by the ParlAI ROSCOE / `simcse` dependency path.

## Patch Update

- Root cause of previous `not_run`: The previous v2 script set smoke_status='not_run' whenever a compatible Python was found, but had no execution branch for creating the isolated venv, installing dependencies, importing ROSCOE, or scoring the smoke pairs.
- Patch made: added venv creation, pip upgrade, minimal dependency installation, ParlAI ROSCOE source fetch, import attempt, and three-pair smoke scoring.

## 3. Python Runtime Discovery

See `python_runtime_discovery.md`.

Selected executable: `python3.11`

Selected version: `Python 3.11.15`

## 4. Environment Isolation

- Main `.venv` modified: false
- New ROSCOE venv created: True
- Venv path: `.venv_roscoe_py311`
- Existing `.venv_roscoe` reused: false

## 5. Dependency Path Attempted

- Install status: `dependencies_installed`
- Dependencies installed in ROSCOE venv: True
- See `roscoe_smoke_v2_dependency_log.txt`.

## 6. ParlAI/ROSCOE Source Used

- Source: `https://github.com/facebookresearch/ParlAI`
- Commit: `6c802418e93a51cbb746b011439ab783dd136de8`
- ROSCOE files used: projects/roscoe/README.md, projects/roscoe/score.py, projects/roscoe/roscoe.py, projects/roscoe/utils.py, tests/nightly/cpu/test_roscoe.py

## 7. Import Results

- Import status: `ok`
- Import-visible embedding metrics: faithfulness, faithfulness_ww, repetition_word, repetition_step, informativeness_step, informativeness_chain, reasoning_alignment, external_hallucination, redundancy, common_sense_error, missing_step, semantic_coverage_step, semantic_coverage_chain

## 8. Smoke Test Input Pairs

The three required toy pairs are recorded in `roscoe_smoke_v2_results.json`.

## 9. Metrics Available

informativeness_chain, informativeness_step, reasoning_alignment, repetition_step, semantic_coverage_chain, semantic_coverage_step

## 10. Smoke Test Results

- Status: `passed`
- Pairs attempted: 3
- Pairs scored: 3

## 11. Non-Degeneracy Check

`passed`

## 12. Arithmetic Contradiction Behavior

0.8100435137748718 on reasoning_alignment; overlap-based semantic metrics can remain high despite the arithmetic contradiction.

## 13. Runtime and Resource Notes

No benchmark rows were scored. No external LLM API calls were made. No BERTScore run was performed.

## 14. Whether Pilot 30 Rows Is Safe

True

## 15. Limitations

This smoke test uses the minimal embedding metric route. NLI, PPL, and grammar metrics remain intentionally excluded.

## 16. Recommended Next Step

Proceed to a 30-row ROSCOE pilot using this isolated venv.
