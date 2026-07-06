# Structured Prompt Pilot v2 Review Layer v1

## Summary Counts

- total_runs: 72
- clean_non_nemotron: 64
- review_nemotron: 8
- review_non_nemotron: 0
- clean_total: 64
- review_total: 8

## Helper Status Distribution Before Override

- ALL_BLANK: 2
- CONFLICT: 1
- NO_VALID_BLOCK: 1
- OK: 68

## Review Status Distribution After Override

- CLEAN: 64
- REVIEW: 8

## Nemotron Review Rows

| scenario_id | raw_helper_status | first_layer_extractable | review_reason |
|---|---|---:|---|
| CM_FOUCAULT_001 | ALL_BLANK | False | nemotron_tail_loop_or_multi_block_risk |
| COS_CMB_001 | CONFLICT | False | nemotron_tail_loop_or_multi_block_risk |
| GR_ISCO_001 | OK | True | nemotron_tail_loop_or_multi_block_risk |
| QFT_G2_001 | OK | True | nemotron_tail_loop_or_multi_block_risk |
| QI_TELEPORT_001 | ALL_BLANK | False | nemotron_tail_loop_or_multi_block_risk |
| QM_BERRY_001 | OK | True | nemotron_tail_loop_or_multi_block_risk |
| SR_ROCKET_001 | NO_VALID_BLOCK | False | nemotron_tail_loop_or_multi_block_risk |
| STAT_ISING_001 | OK | True | nemotron_tail_loop_or_multi_block_risk |

## Safety Confirmations

- raw_outputs_unchanged: yes
- learning_db_modified: no
