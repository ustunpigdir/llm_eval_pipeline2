# Structured Prompt Pilot v4 PDF Review Source

Scope: 64 total runs from structured_prompt_pilot_v4.

- CLEAN rows: 63
- REVIEW rows excluded from deterministic autograde: 1
- BERTScore was not run.
- learning.db was not modified.

Main files:

- runs/structured_prompt_pilot_v4_runs.json
- runs/structured_prompt_pilot_v4_run_plan.json
- runs/manifest.json
- review_layer/review_layer_v1.json
- review_layer/review_layer_v1.csv
- autograde/structured_prompt_v4_clean_autograde.json
- autograde/structured_prompt_v4_clean_autograde.csv
- autograde/STRUCTURED_PROMPT_V4_AUTOGRADE_NO_BERT_REPORT.md
- worked_solutions/worked_solutions_batch1.md through worked_solutions_batch7.md

Known state:

- One output is marked REVIEW because the first-layer helper status is NO_VALID_BLOCK.
- Deterministic autograding was applied only to CLEAN rows.
- Raw model responses are preserved unchanged in the runs JSON.
