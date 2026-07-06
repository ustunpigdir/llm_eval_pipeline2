# BERTScore Reasoning-Only Canonical v2 Report

## Purpose

Run BERTScore on canonical extractor-span reasoning-only text.

## Inputs

- `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv`

## BERTScore Config

- Model type: lang=en default (roberta-large)
- Model hash: unknown
- rescale_with_baseline: True

## Why This Is v2

v1 no-final-block BERTScore had a 5-row final-block removal caveat. v2 uses canonical candidate/reference reasoning text where extractor-span removal succeeded for 252/252 rows.

## Row Coverage

- Rows: 252
- PASS: 117
- FAIL: 135

## Overall BERTScore Summary

- Mean F1: 0.623031
- Median F1: 0.815243
- Min F1: -0.381666
- Max F1: 0.940915

## BERTScore By Deterministic Grade

| grade | rows | mean_f1 | median_f1 |
| --- | ---: | ---: | ---: |
| FAIL | 135 | 0.590251 | 0.762946 |
| PASS | 117 | 0.660854 | 0.861585 |

## BERTScore By Batch

| batch | rows | mean_f1 | PASS-FAIL gap |
| --- | ---: | ---: | ---: |
| V2 | 64 | 0.635370 | 0.065941 |
| V3 | 61 | 0.613331 | 0.118366 |
| V4 | 63 | 0.598396 | -0.003465 |
| V5 | 64 | 0.644189 | 0.075623 |

## BERTScore By Scenario

- GR_GPS_001: mean F1 0.279954
- COS_DESITTER_001: mean F1 0.294589
- QFT_CASIMIR_001: mean F1 0.421599
- GR_ISCO_001: mean F1 0.455291
- STAT_NEGT_001: mean F1 0.458145

## BERTScore By Model

- Mistral Small 3.2 24B Instruct: mean F1 0.855550
- Gemma 3 27B IT: mean F1 0.791038
- Mistral NeMo 12B: mean F1 0.761717
- Gemma 3 12B IT: mean F1 0.728583
- Gemma 4 31B IT: mean F1 0.723618

## High-BERTScore FAIL Examples

- SR_ROCKET_001 / Mistral Small 3.2 24B Instruct: 0.932873

## Low-BERTScore PASS Examples

- CM_TOP_001 / Granite 4.1 8B: -0.194096

## Comparison With No-Final BERTScore v1

- Rows with changed F1 vs v1: 214
- Correlation with v1 F1: 0.998674

## Comparison With ROUGE-L

- Correlation with ROUGE-L F1: 0.975410

## Comparison With chrF

- Correlation with chrF score: 0.906473

## Correlation With Deterministic PASS/FAIL

- deterministic_pass_binary vs canonical BERTScore F1: 0.099199

## Interpretation

This v2 run is the valid reasoning-only BERTScore run. It remains descriptive and secondary; deterministic PASS/FAIL remains the correctness anchor.

## Limitations

- BERTScore does not measure scientific correctness.
- High-BERTScore FAIL rows can still be numerically/physically wrong.
- Low-BERTScore PASS rows can still be correct with different phrasing.

## Recommended Next Metric

Use the canonical text artifact for any NLI/ROSCOE experiment, after cheap lexical/BERTScore behavior is fully characterized.
