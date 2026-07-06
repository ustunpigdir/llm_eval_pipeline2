# ROUGE-L Metric Report

## Purpose

Add a cheap deterministic lexical metric over canonical reasoning-only structured rows.

## Inputs

- `outputs/metric_text_artifacts_v1/canonical_reasoning_text_dataset.csv`

## Tokenizer

`lowercase regex tokens: [A-Za-z]+|[0-9]+(?:\.[0-9]+)?|[\\+\-*/=^_{}()[\],.]`

## Row Coverage

- Rows: 252
- PASS: 117
- FAIL: 135

## Overall ROUGE-L Summary

- Mean F1: 0.783609
- Median F1: 0.892443
- Min F1: 0.121683
- Max F1: 0.979817

## ROUGE-L By Deterministic Grade

| grade | rows | mean_f1 | median_f1 |
| --- | ---: | ---: | ---: |
| FAIL | 135 | 0.763017 | 0.853881 |
| PASS | 117 | 0.807369 | 0.918552 |

## ROUGE-L By Batch

| batch | rows | mean_f1 | PASS-FAIL gap |
| --- | ---: | ---: | ---: |
| V2 | 64 | 0.800273 | 0.032991 |
| V3 | 61 | 0.766759 | 0.094897 |
| V4 | 63 | 0.777277 | 0.006014 |
| V5 | 64 | 0.789237 | 0.032258 |

## ROUGE-L By Scenario

- GR_GPS_001: mean F1 0.521153
- QFT_CASIMIR_001: mean F1 0.594026
- STAT_NEGT_001: mean F1 0.617174
- COS_DESITTER_001: mean F1 0.629038
- GR_ISCO_001: mean F1 0.686682

## ROUGE-L By Model

- Mistral Small 3.2 24B Instruct: mean F1 0.912961
- Gemma 3 27B IT: mean F1 0.880469
- Mistral NeMo 12B: mean F1 0.865185
- Gemma 4 31B IT: mean F1 0.851478
- Gemma 3 12B IT: mean F1 0.847297

## High-ROUGE FAIL Examples

- SR_TWIN_001 / Gemma 3 27B IT: 0.965138

## Low-ROUGE PASS Examples

- CM_TOP_001 / Granite 4.1 8B: 0.245067

## Correlation With Deterministic PASS/FAIL

- deterministic_pass_binary vs ROUGE-L F1: 0.103759

## Comparison With No-Final BERTScore

- ROUGE-L PASS-minus-FAIL mean gap: 0.044352
- ROUGE-L simple effect size: 0.209217
- no-final BERTScore PASS-minus-FAIL mean gap: 0.081370
- no-final BERTScore simple effect size: 0.219251
- ROUGE-L vs no-final BERTScore correlation: 0.977968
- ROUGE-L separation is weaker than no-final BERTScore by mean gap.

## Interpretation

ROUGE-L is deterministic and reproducible. It measures lexical sequence overlap, not scientific correctness.

High ROUGE-L FAIL rows show lexical similarity can coexist with wrong scientific answers. Low ROUGE-L PASS rows show correct answers can differ lexically from the reference.

## Limitations

- Lexical sequence overlap is sensitive to phrasing and length.
- It does not evaluate numeric correctness or physical reasoning validity.
- Deterministic grading remains the correctness anchor.

## Recommended Next Metric

Compute chrF from the same canonical text artifact as a complementary character-level lexical metric.
