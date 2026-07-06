# ParlAI ROSCOE Install Plan

## Conservative Plan

1. Create `.venv_roscoe` using a Python version known to support the needed dependencies. Prefer Python 3.10 or 3.11 if available; use Python 3.12 only after a dry dependency resolution check.
2. Do not modify the main `.venv`.
3. Clone or sparse-checkout only the ParlAI files needed for `projects/roscoe`, `projects/__init__.py`, and minimal package imports into a temporary external folder.
4. Install minimal dependencies in `.venv_roscoe`: `torch`, `transformers`, `sentence-transformers`, `simcse`, `scipy`, `nltk`, and only enough ParlAI package/source context to satisfy imports.
5. Run a smoke test on two toy candidate/reference pairs using `projects.roscoe.score.Evaluator` directly.
6. Start with embedding-only scores to avoid NLI, PPL, and grammar model downloads.
7. Stop immediately if dependency resolution conflicts, import-time model loading fails, or CPU runtime is excessive.

## Full ParlAI Plan

Use this only if the conservative plan cannot import ROSCOE safely.

1. Create `.venv_roscoe`.
2. Clone ParlAI into a temporary external folder under `/tmp/roscoe_parlai_scan/` or another disposable path outside this repo.
3. Install ParlAI and ROSCOE README dependencies inside `.venv_roscoe`.
4. Download only the model weights needed for the first smoke test.
5. Run `tests/nightly/cpu/test_roscoe.py` or a smaller direct `Evaluator` smoke test.
6. Score a 30-row pilot from canonical reasoning-only text.
7. Run the full 252 rows only if all pilot rows score successfully and runtime is reasonable.

## Rollback / Cleanup

- Delete `.venv_roscoe` if dependency resolution fails.
- Delete the temporary ParlAI clone.
- Do not delete or modify project outputs, raw runs, `learning.db`, or frozen metric artifacts.
- Keep dependency reports and manifests only.
