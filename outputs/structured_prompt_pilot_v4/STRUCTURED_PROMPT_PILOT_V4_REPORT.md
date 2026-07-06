# Structured Prompt Pilot v4

- Created at: 2026-07-05T11:47:41+00:00
- Prompt mode: structured_prompt_pilot_v4
- Scenarios: 8
- Model identities: 8
- Prompt assignments: 64
- Original question source: scenarios.prompt
- Scaffold source: locked worked_solutions_batch1.md through worked_solutions_batch7.md
- Final-answer field order source: gold_fields.field_index
- Nemotron excluded: yes

## Preflight Validation

- total_assignments: 64
- scenario_count: 8
- model_count: 8
- nemotron_assignments: 0
- original_question_present: 64/64
- exactly_one_final_answer_block: 64/64
- field_order_matches_db: 64/64
- leaked_final_gold_values: 0
- placeholder_count_gt_zero: 64/64
- prompt_does_not_begin_with_derivation: True
- passed: True

## Scenario Preflight Table

| scenario_id | assignment_count | original_question_present_count | final_answer_block_count_ok | final_answer_field_order_matches_db | leaked_final_gold_values_detected | placeholder_count |
|---|---:|---:|---:|---|---|---:|
| CM_KAPITZA_001 | 8 | 8 | 8 | True | False | 7 |
| COS_DESITTER_001 | 8 | 8 | 8 | True | False | 9 |
| GR_PERI_001 | 8 | 8 | 8 | True | False | 13 |
| QFT_UNRUH_001 | 8 | 8 | 8 | True | False | 9 |
| QI_HOLEVO_001 | 8 | 8 | 8 | True | False | 6 |
| QM_AB_001 | 8 | 8 | 8 | True | False | 8 |
| SR_TWIN_001 | 8 | 8 | 8 | True | False | 12 |
| STAT_LANDAUER_001 | 8 | 8 | 8 | True | False | 5 |

## Model Identities

- Gemma 3 12B IT
- Gemma 3 27B IT
- Gemma 4 31B IT
- Granite 4.1 8B
- Llama 3.1 8B Instruct
- Ministral 3 8B
- Mistral NeMo 12B
- Mistral Small 3.2 24B Instruct
