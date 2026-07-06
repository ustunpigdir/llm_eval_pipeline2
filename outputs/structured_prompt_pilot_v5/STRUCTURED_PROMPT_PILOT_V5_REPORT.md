# Structured Prompt Pilot v5

- Created at: 2026-07-05T20:31:12+00:00
- Prompt mode: structured_prompt_pilot_v5
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
- remaining_scenario_count: 8
- remaining_scenarios_are_unused: True
- one_remaining_scenario_per_category: True
- passed: True

## Scenario Preflight Table

| scenario_id | category | assignment_count | original_question_present_count | final_answer_block_count_ok | final_answer_field_order_matches_db | leaked_final_gold_values_detected | placeholder_count |
|---|---|---:|---:|---:|---|---|---:|
| CM_TOP_001 | Classical Mechanics | 8 | 8 | 8 | True | False | 4 |
| COS_AGE_001 | Cosmology | 8 | 8 | 8 | True | False | 8 |
| GR_CHIRP_001 | General Relativity | 8 | 8 | 8 | True | False | 8 |
| QFT_YUKAWA_001 | Quantum Field Theory | 8 | 8 | 8 | True | False | 6 |
| QI_CLONE_001 | Quantum Information Theory | 8 | 8 | 8 | True | False | 3 |
| QM_RT_001 | Quantum Mechanics | 8 | 8 | 8 | True | False | 10 |
| SR_FIZEAU_001 | Special Relativity | 8 | 8 | 8 | True | False | 5 |
| STAT_NEGT_001 | Statistical Mechanics | 8 | 8 | 8 | True | False | 4 |

## Model Identities

- Gemma 3 12B IT
- Gemma 3 27B IT
- Gemma 4 31B IT
- Granite 4.1 8B
- Llama 3.1 8B Instruct
- Ministral 3 8B
- Mistral NeMo 12B
- Mistral Small 3.2 24B Instruct
