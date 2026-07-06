# ROSCOE Pilot v1

This folder contains a 30-row ROSCOE pilot over canonical reasoning-only text.

It uses the isolated `.venv_roscoe_py311` environment and the Meta/ParlAI minimal embedding-metric route validated in smoke v2. It does not change grading, modify raw outputs, run BERTScore, call LLM APIs, or implement Phase 2 semantics.

Rerun with:

```bash
.venv/bin/python scripts/run_roscoe_pilot_v1.py
```

Interpret these results as a biased pilot only, not a full benchmark conclusion.
