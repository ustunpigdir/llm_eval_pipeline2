# chrF Metric Report

## Purpose

Add a deterministic character n-gram lexical metric over canonical reasoning-only structured rows.

## Inputs

- `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv`

## chrF Implementation

- Character n-gram orders: 1 through 6
- Beta: 2.0
- Lowercase text and normalize whitespace to single spaces.
- Keep punctuation and math symbols.
- Use multiset n-gram overlap and aggregate mean precision/recall before F-score.

## Row Coverage

- Rows: 252
- PASS: 117
- FAIL: 135

## Overall chrF Summary

- Mean score: 0.801425
- Median score: 0.890255
- Min score: 0.246440
- Max score: 0.991419

## chrF By Deterministic Grade

| grade | rows | mean_chrf | median_chrf |
| --- | ---: | ---: | ---: |
| FAIL | 135 | 0.771122 | 0.864642 |
| PASS | 117 | 0.836390 | 0.932676 |

## chrF By Batch

| batch | rows | mean_chrf | PASS-FAIL gap |
| --- | ---: | ---: | ---: |
| V2 | 64 | 0.827633 | 0.031286 |
| V3 | 61 | 0.755579 | 0.168922 |
| V4 | 63 | 0.818961 | 0.037087 |
| V5 | 64 | 0.801652 | 0.028213 |

## chrF By Scenario

- GR_GPS_001: mean score 0.464853
- STAT_NEGT_001: mean score 0.520105
- QFT_CASIMIR_001: mean score 0.521822
- COS_DESITTER_001: mean score 0.722536
- GR_PERI_001: mean score 0.729104

## chrF By Model

- Mistral Small 3.2 24B Instruct: mean score 0.901024
- Gemma 3 27B IT: mean score 0.878089
- Gemma 4 31B IT: mean score 0.862124
- Gemma 3 12B IT: mean score 0.853502
- Mistral NeMo 12B: mean score 0.851504

## High-chrF FAIL Examples

- SR_TWIN_001 / Gemma 3 27B IT: 0.975108

## Low-chrF PASS Examples

- QM_BERRY_001 / Granite 4.1 8B: 0.406447

## Correlation With Deterministic PASS/FAIL

- deterministic_pass_binary vs chrF score: 0.172891

## Comparison With ROUGE-L

- chrF PASS-minus-FAIL mean gap: 0.065268
- chrF simple effect size: 0.352804
- ROUGE-L PASS-minus-FAIL mean gap: 0.044352
- ROUGE-L simple effect size: 0.209217
- chrF vs ROUGE-L correlation: 0.948782
- chrF separation is stronger than ROUGE-L by mean gap.

## Comparison With No-Final BERTScore

- no-final BERTScore PASS-minus-FAIL mean gap: 0.081370
- no-final BERTScore simple effect size: 0.219251
- chrF vs no-final BERTScore correlation: 0.919249
- chrF separation is weaker than no-final BERTScore by mean gap.

## Interpretation

chrF is deterministic and reproducible. It measures character n-gram overlap, not scientific correctness.

High chrF FAIL rows show character-level similarity can coexist with wrong scientific answers. Low chrF PASS rows show correct answers can differ textually from the reference.

## Limitations

- Character overlap is sensitive to notation and phrasing.
- It does not evaluate numeric correctness or physical reasoning validity.
- Deterministic grading remains the correctness anchor.

## Recommended Next Metric

Compute a combined lexical dashboard from ROUGE-L and chrF, then consider NLI/ROSCOE only after the cheap metrics are fully characterized.
