# Structured Prompt Pilot v2 PDF Review Source

This folder contains all files needed to generate the iPad review PDF for the structured-prompt pilot v2.

Scope:
- 72 total runs
- 64 CLEAN runs for PDF review
- 8 Nemotron REVIEW rows excluded from automatic autograde review
- BERTScore was not run

Main files:
- `runs/structured_prompt_pilot_v2_runs.json`: raw model outputs
- `autograde/structured_prompt_v2_clean_autograde.json`: field-level deterministic autograde for the 64 CLEAN rows
- `autograde/structured_prompt_v2_clean_autograde.csv`: tabular version
- `review_layer/review_layer_v1.json`: CLEAN/REVIEW split
- `worked_solutions/`: locked worked gold solutions for all 32 scenarios

Known state:
- `learning.db` was not modified during structured-prompt pilot v2 execution or autograding.
- Nemotron rows are marked REVIEW because of tail-loop / multi-block risk.
- The suspicious result to inspect manually is that GR_ISCO_001 has 0/8 pass and SR_ROCKET_001 has 1/8 pass under the structured scaffold.
