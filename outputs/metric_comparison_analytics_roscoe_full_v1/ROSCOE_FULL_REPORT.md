# ROSCOE Full Report

## 1. Purpose

Score all 252 canonical reasoning-only benchmark rows using Meta/ParlAI ROSCOE embedding metrics.

## 2. Why Full Run Follows Pilot v1

Smoke v2 passed and the 30-row pilot scored 30/30 rows successfully, so this full layer uses the same minimal embedding-metric route.

## 3. Inputs

- Text source: `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv`
- Existing metrics aligned by `source_run_id`: BERTScore v2, ROUGE-L, chrF, base comparison dataset.

## 4. Row Coverage

- attempted: 252
- scored: 252
- PASS: 117
- FAIL: 135
- batches: {'V2': 64, 'V3': 61, 'V4': 63, 'V5': 64}

## 5. ROSCOE Implementation Used

Meta/ParlAI `projects/roscoe/score.py`, via `tmp/roscoe_parlai_runtime_v2`, executed with `.venv_roscoe_py311`.

## 6. Metrics Available

informativeness_chain, informativeness_step, reasoning_alignment, repetition_step, semantic_coverage_chain, semantic_coverage_step

## 7. Overall Full Summary

- full_status: `passed`
- selected metric: `reasoning_alignment`
- roscoe_available_mean excludes `repetition_step` because its direction is less clearly quality-positive than the semantic/informativeness metrics.

## 8. Summary By Deterministic Grade

Selected metric PASS mean: 0.939940

Selected metric FAIL mean: 0.918146

PASS-minus-FAIL gap: 0.021794

Effect size: 0.482872

Correlation with deterministic pass: 0.234278

## 9. Summary By Batch, Scenario, And Model

See `roscoe_full_by_batch.csv`, `roscoe_full_by_scenario.csv`, and `roscoe_full_by_model.csv`.

## 10. High-ROSCOE FAIL Examples

- e393f274-ca90-4884-a598-72d0a544a214 | SR_TWIN_001 | Gemma 3 27B IT | 0.977883
- 9cabff0f-1401-4d81-a9ab-0c356b747793 | CM_TOP_001 | Mistral NeMo 12B | 0.972424
- 8dd9d539-5113-456a-ad1b-2987c0bf85c9 | SR_ROCKET_001 | Mistral Small 3.2 24B Instruct | 0.970309
- d678fa6d-f25c-4af8-bc83-9067f0531bcc | CM_APSIDAL_001 | Gemma 3 27B IT | 0.970179
- 4e065114-6895-4037-9f9c-d85e9790bfc5 | CM_APSIDAL_001 | Mistral NeMo 12B | 0.969695

## 11. Low-ROSCOE PASS Examples

- 81351b41-e944-416c-979d-7650f60107cb | QFT_CASIMIR_001 | Granite 4.1 8B | 0.798134
- 93598232-73aa-45f6-85f0-657ebcc3729c | STAT_NEGT_001 | Granite 4.1 8B | 0.830628
- 9fc843b5-b6bd-412e-9421-9525b76fb61a | QM_AB_001 | Granite 4.1 8B | 0.841299
- 5662b68d-3be1-4094-aa82-9419c9d43619 | CM_TOP_001 | Granite 4.1 8B | 0.841398
- 491a2baf-b665-4ce6-837c-9a9d3c21f9ed | COS_DESITTER_001 | Gemma 4 31B IT | 0.842880

## 12. Correlation With Deterministic PASS/FAIL

0.234278

## 13. Comparison With BERTScore v2

Selected-ROSCOE correlation with BERTScore v2 F1: 0.896465. BERTScore baseline gap/effect/correlation: 0.070603 / 0.199942 / 0.099199.

## 14. Comparison With ROUGE-L

Selected-ROSCOE correlation with ROUGE-L F1: 0.890442. ROUGE-L baseline gap/effect/correlation: 0.044352 / 0.209217 / 0.103759.

## 15. Comparison With chrF

Selected-ROSCOE correlation with chrF: 0.790308. chrF baseline gap/effect/correlation: 0.065268 / 0.352804 / 0.172891.

## 16. Runtime/Resource Notes

Runtime seconds: 42.686. No benchmark model calls or external LLM API calls were made.

## 17. Interpretation

ROSCOE is a reasoning-trace diagnostic, not a correctness gate. Its relationship to deterministic PASS/FAIL should be read alongside the outlier files and correlations.

## 18. Limitations

This layer uses only embedding metrics and excludes NLI, PPL, and grammar metrics. Deterministic PASS/FAIL remains the correctness anchor.

## 19. Recommended Next Step

Compare this full ROSCOE layer against BERTScore, ROUGE-L, and chrF in the metric-comparison dashboard.
