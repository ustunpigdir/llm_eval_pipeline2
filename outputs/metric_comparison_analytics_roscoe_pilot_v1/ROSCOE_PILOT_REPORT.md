# ROSCOE Pilot Report

## 1. Purpose

Score a controlled 30-row pilot from canonical reasoning-only benchmark text using Meta/ParlAI ROSCOE embedding metrics.

## 2. Why Pilot Follows Smoke v2

Smoke v2 passed in `.venv_roscoe_py311` with three toy pairs and finite numeric embedding metrics.

## 3. Inputs

- Text source: `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv`
- Existing metrics aligned by `source_run_id`: BERTScore v2, ROUGE-L, chrF, base comparison dataset.

## 4. Pilot Sample Construction

- high_overlap_fail: 10
- low_overlap_pass: 10
- stratified_normal: 10
- deterministic seed: 20260706

## 5. ROSCOE Implementation Used

Meta/ParlAI `projects/roscoe/score.py`, via `tmp/roscoe_parlai_runtime_v2`, executed with `.venv_roscoe_py311`.

## 6. Metrics Available

informativeness_chain, informativeness_step, reasoning_alignment, repetition_step, semantic_coverage_chain, semantic_coverage_step

## 7. Row Coverage

- attempted: 30
- scored: 30
- PASS: 14
- FAIL: 16

## 8. Overall Pilot Summary

- pilot_status: `passed`
- selected metric: `reasoning_alignment`
- roscoe_available_mean excludes `repetition_step` because its direction is less clearly quality-positive than the semantic/informativeness metrics.

## 9. Pilot Summary By Deterministic Grade

Selected metric PASS mean: 0.874590

Selected metric FAIL mean: 0.928889

PASS-minus-FAIL gap: -0.054299

Effect size: -1.066610

Correlation with deterministic pass: -0.480862

## 10. Pilot Summary By Sample Group

See `roscoe_pilot_by_sample_group.csv`.

## 11. High-ROSCOE FAIL Examples

- e393f274-ca90-4884-a598-72d0a544a214 | SR_TWIN_001 | Gemma 3 27B IT | 0.977883
- 8dd9d539-5113-456a-ad1b-2987c0bf85c9 | SR_ROCKET_001 | Mistral Small 3.2 24B Instruct | 0.970309
- 672d5859-333f-4a64-a9bf-0605af9f8987 | COS_AGE_001 | Gemma 3 27B IT | 0.964262
- 0fdbc6f7-aa2f-4d13-85e3-1de67d52d0f1 | SR_ROCKET_001 | Gemma 3 27B IT | 0.963519
- 1c025782-1745-4b84-8da5-82a9a85a1fb9 | STAT_LANDAUER_001 | Gemma 3 27B IT | 0.958980

## 12. Low-ROSCOE PASS Examples

- 81351b41-e944-416c-979d-7650f60107cb | QFT_CASIMIR_001 | Granite 4.1 8B | 0.798134
- 9fc843b5-b6bd-412e-9421-9525b76fb61a | QM_AB_001 | Granite 4.1 8B | 0.841299
- 5662b68d-3be1-4094-aa82-9419c9d43619 | CM_TOP_001 | Granite 4.1 8B | 0.841398
- 491a2baf-b665-4ce6-837c-9a9d3c21f9ed | COS_DESITTER_001 | Gemma 4 31B IT | 0.842880
- 660bac8a-431e-4e1e-a1b0-4327460893b8 | SR_TWIN_001 | Granite 4.1 8B | 0.845699

## 13. Correlation With Deterministic PASS/FAIL

-0.480862

## 14. Comparison With BERTScore v2

Pilot selected-ROSCOE correlation with BERTScore v2 F1: 0.918663. Full-dataset BERTScore baseline gap/effect/correlation: 0.070603 / 0.199942 / 0.099199.

## 15. Comparison With ROUGE-L

Pilot selected-ROSCOE correlation with ROUGE-L F1: 0.933065. Full-dataset ROUGE-L baseline gap/effect/correlation: 0.044352 / 0.209217 / 0.103759.

## 16. Comparison With chrF

Pilot selected-ROSCOE correlation with chrF: 0.835203. Full-dataset chrF baseline gap/effect/correlation: 0.065268 / 0.352804 / 0.172891.

## 17. Runtime/Resource Notes

Runtime seconds: 9.226. No benchmark model calls or external LLM API calls were made.

## 18. Whether Full 252-Row ROSCOE Run Is Recommended

True

## 19. Limitations

This is a biased 30-row pilot. It uses only embedding metrics and excludes NLI, PPL, and grammar metrics. Deterministic PASS/FAIL remains the correctness anchor.

## 20. Recommended Next Step

Run the full 252-row ROSCOE embedding-metric layer.
