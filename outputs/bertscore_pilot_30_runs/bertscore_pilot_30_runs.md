# Thirty-Run BERTScore Pilot

## Purpose

Test whether full-answer BERTScore separates deterministic outcome groups before building a broader semantic judge layer.

## Reference Source

- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch1.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch2.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch3.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch4.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch5.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch6.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch7.md`

Parsed scenario references: 32
Missing official references: none
Extra reference IDs: none

## Sampling Rules

- MATCH-heavy: exact all-match runs.
- MISMATCH-heavy: mismatch_count > 0, preferring mismatch_count >= match_count and no NOT_FOUND/REVIEW.
- NOT_FOUND/REVIEW-heavy: not_found_count > 0 or review_count > 0, preferring highest combined count.

Sampling notes: none

## Selected Run List

| group | run_id | scenario_id | model_name | MATCH | MISMATCH | NOT_FOUND | REVIEW | F1 |
| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| MATCH-heavy | 1 | CM_APSIDAL_001 | Gemma 3 12B IT | 4 | 0 | 0 | 0 | -0.009022 |
| MATCH-heavy | 2 | CM_APSIDAL_001 | Gemma 3 12B IT | 4 | 0 | 0 | 0 | -0.057700 |
| MATCH-heavy | 4 | CM_APSIDAL_001 | Gemma 3 12B IT | 4 | 0 | 0 | 0 | -0.054938 |
| MATCH-heavy | 5 | CM_APSIDAL_001 | Gemma 3 27B IT | 4 | 0 | 0 | 0 | -0.044420 |
| MATCH-heavy | 6 | CM_APSIDAL_001 | Gemma 3 27B IT | 4 | 0 | 0 | 0 | -0.024127 |
| MATCH-heavy | 7 | CM_APSIDAL_001 | Gemma 4 31B IT | 4 | 0 | 0 | 0 | -0.144526 |
| MATCH-heavy | 8 | CM_APSIDAL_001 | Gemma 4 31B IT | 4 | 0 | 0 | 0 | -0.120379 |
| MATCH-heavy | 10 | CM_APSIDAL_001 | Granite 4.1 8B | 4 | 0 | 0 | 0 | -0.219892 |
| MATCH-heavy | 11 | CM_APSIDAL_001 | Granite 4.1 8B | 4 | 0 | 0 | 0 | -0.213121 |
| MATCH-heavy | 25 | CM_APSIDAL_001 | Mistral Small 3.2 24B Instruct | 4 | 0 | 0 | 0 | -0.167973 |
| MISMATCH-heavy | 15 | CM_APSIDAL_001 | Llama 3.1 8B Instruct | 0 | 4 | 0 | 0 | -0.130714 |
| MISMATCH-heavy | 520 | QM_TUNNEL_001 | Llama 3.1 8B Instruct | 0 | 4 | 0 | 0 | -0.204253 |
| MISMATCH-heavy | 521 | QM_TUNNEL_001 | Llama 3.1 8B Instruct | 0 | 4 | 0 | 0 | -0.264177 |
| MISMATCH-heavy | 526 | QM_TUNNEL_001 | Mistral NeMo 12B | 0 | 4 | 0 | 0 | -0.242133 |
| MISMATCH-heavy | 527 | QM_TUNNEL_001 | Mistral NeMo 12B | 0 | 4 | 0 | 0 | -0.271000 |
| MISMATCH-heavy | 528 | QM_TUNNEL_001 | Mistral NeMo 12B | 0 | 4 | 0 | 0 | -0.274068 |
| MISMATCH-heavy | 42 | CM_FOUCAULT_001 | Llama 3.1 8B Instruct | 0 | 3 | 0 | 0 | -0.050978 |
| MISMATCH-heavy | 43 | CM_FOUCAULT_001 | Llama 3.1 8B Instruct | 0 | 3 | 0 | 0 | -0.188287 |
| MISMATCH-heavy | 47 | CM_FOUCAULT_001 | Mistral NeMo 12B | 0 | 3 | 0 | 0 | -0.055625 |
| MISMATCH-heavy | 48 | CM_FOUCAULT_001 | Mistral NeMo 12B | 0 | 3 | 0 | 0 | -0.101694 |
| NOT_FOUND/REVIEW-heavy | 530 | QM_TUNNEL_001 | NVIDIA Nemotron 3 Nano 30B-A3B | 0 | 0 | 4 | 0 | -0.287733 |
| NOT_FOUND/REVIEW-heavy | 41 | CM_FOUCAULT_001 | Llama 3.1 8B Instruct | 0 | 0 | 3 | 0 | -0.219776 |
| NOT_FOUND/REVIEW-heavy | 112 | COS_AGE_001 | NVIDIA Nemotron 3 Nano 30B-A3B | 0 | 0 | 3 | 0 | -0.304268 |
| NOT_FOUND/REVIEW-heavy | 144 | COS_DESITTER_001 | Llama 3.1 8B Instruct | 0 | 0 | 3 | 0 | -0.268124 |
| NOT_FOUND/REVIEW-heavy | 204 | GR_GPS_001 | Llama 3.1 8B Instruct | 0 | 0 | 3 | 0 | -0.246186 |
| NOT_FOUND/REVIEW-heavy | 226 | GR_ISCO_001 | Llama 3.1 8B Instruct | 0 | 0 | 3 | 0 | -0.198927 |
| NOT_FOUND/REVIEW-heavy | 379 | QI_CLONE_001 | Ministral 3 8B | 0 | 0 | 3 | 0 | -0.256984 |
| NOT_FOUND/REVIEW-heavy | 395 | QI_HOLEVO_001 | Llama 3.1 8B Instruct | 0 | 0 | 3 | 0 | -0.236492 |
| NOT_FOUND/REVIEW-heavy | 405 | QI_HOLEVO_001 | NVIDIA Nemotron 3 Nano 30B-A3B | 0 | 0 | 3 | 0 | -0.135657 |
| NOT_FOUND/REVIEW-heavy | 500 | QM_RT_001 | Llama 3.1 8B Instruct | 0 | 0 | 3 | 0 | -0.240258 |

## Group-Level BERTScore Summary

| group | n | mean_f1 | median_f1 | min_f1 | max_f1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| MATCH-heavy | 10 | -0.105610 | -0.089040 | -0.219892 | -0.009022 |
| MISMATCH-heavy | 10 | -0.178293 | -0.196270 | -0.274068 | -0.050978 |
| NOT_FOUND/REVIEW-heavy | 10 | -0.239440 | -0.243222 | -0.304268 | -0.135657 |

## Interpretation

Expected ordering held: yes.

MATCH-heavy should tend to be highest, MISMATCH-heavy lower, and NOT_FOUND/REVIEW-heavy lowest.

## Scenario Distribution

| scenario_id | n_selected_runs | groups_present |
| --- | ---: | --- |
| CM_APSIDAL_001 | 11 | MATCH-heavy;MISMATCH-heavy |
| CM_FOUCAULT_001 | 5 | MISMATCH-heavy;NOT_FOUND/REVIEW-heavy |
| COS_AGE_001 | 1 | NOT_FOUND/REVIEW-heavy |
| COS_DESITTER_001 | 1 | NOT_FOUND/REVIEW-heavy |
| GR_GPS_001 | 1 | NOT_FOUND/REVIEW-heavy |
| GR_ISCO_001 | 1 | NOT_FOUND/REVIEW-heavy |
| QI_CLONE_001 | 1 | NOT_FOUND/REVIEW-heavy |
| QI_HOLEVO_001 | 2 | NOT_FOUND/REVIEW-heavy |
| QM_RT_001 | 1 | NOT_FOUND/REVIEW-heavy |
| QM_TUNNEL_001 | 6 | MISMATCH-heavy;NOT_FOUND/REVIEW-heavy |

## Limitations

This pilot scores the full model answer, not a separately extracted concept-explanation span. Full-answer BERTScore may be inflated by copied formulas, repeated prompt text, or final-answer formatting.

## Recommendation

Continue to a full BERTScore judge layer only if the group separation is strong enough to add value over deterministic field grading.
