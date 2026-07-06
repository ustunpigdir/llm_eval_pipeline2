# ROSCOE Full v1

This folder contains the full 252-row ROSCOE embedding-metric layer over canonical reasoning-only text.

It uses the isolated `.venv_roscoe_py311` environment and the Meta/ParlAI minimal embedding-metric route validated in smoke v2. It does not change grading, modify raw outputs, run BERTScore, call LLM APIs, or implement Phase 2 semantics.

Rerun with:

```bash
.venv/bin/python scripts/run_roscoe_full_v1.py
```

Interpret ROSCOE as a reasoning-trace diagnostic. Deterministic PASS/FAIL remains the correctness anchor.
