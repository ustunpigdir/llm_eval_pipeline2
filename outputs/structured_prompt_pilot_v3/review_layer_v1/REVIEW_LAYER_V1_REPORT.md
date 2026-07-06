# Structured Prompt Pilot v3 Review Layer v1

## Summary Counts

- total_runs: 64
- clean_total: 61
- review_total: 3

## Helper Status Distribution Before Review Layer

- NO_VALID_BLOCK: 3
- OK: 61

## Review Status Distribution

- CLEAN: 61
- REVIEW: 3

## Review Rows

| scenario_id | model_name | raw_helper_status | first_layer_extractable | review_reason |
|---|---|---|---:|---|
| QM_TUNNEL_001 | Granite 4.1 8B | NO_VALID_BLOCK | False | non_clean_helper_status |
| STAT_BEC_001 | Granite 4.1 8B | NO_VALID_BLOCK | False | non_clean_helper_status |
| STAT_BEC_001 | Llama 3.1 8B Instruct | NO_VALID_BLOCK | False | non_clean_helper_status |

## Safety Confirmations

- raw_outputs_unchanged: yes
- learning_db_modified: no
