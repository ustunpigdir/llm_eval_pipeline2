# BERTScore Structured All-32 Phase-1-Hardened No-Final-Block Report

## Scope

- Run name: `structured_prompt_all32_phase1_hardened_no_final_block_v1`
- Transformation: remove FINAL ANSWER aligned block from candidate and reference texts before scoring
- Rows scored: 252
- Rescale with baseline: True
- BERTScore model hash: unknown

## Final Block Removal

- Candidate blocks removed: 247
- Candidate warnings: 5
- Reference blocks removed: 0
- Reference warnings: 252

## Overall No-Final-Block BERTScore

- Mean F1: 0.646639
- Median F1: 0.854346
- Min F1: -0.381666
- Max F1: 0.993578

## By Deterministic Grade

| grade | rows | mean_f1 | median_f1 | min_f1 | max_f1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| FAIL | 135 | 0.608860 | 0.783607 | -0.381666 | 0.972873 |
| PASS | 117 | 0.690230 | 0.899380 | -0.194096 | 0.993578 |

## By Batch

| batch | rows | PASS | FAIL | mean_f1 | median_f1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| V2 | 64 | 37 | 27 | 0.666059 | 0.883931 |
| V3 | 61 | 24 | 37 | 0.628353 | 0.786629 |
| V4 | 63 | 19 | 44 | 0.623976 | 0.798722 |
| V5 | 64 | 37 | 27 | 0.666957 | 0.903366 |

## Full vs No-Final Comparison

- Row-level alignment status: aligned_by_source_run_id
- Full overall mean F1: 0.503559
- No-final overall mean F1: 0.646639
- Delta overall mean F1: 0.143081
- Full PASS-minus-FAIL gap: 0.029271
- No-final PASS-minus-FAIL gap: 0.081370
- Delta gap: 0.052099
- Rows increased: 188
- Rows decreased: 20

## Interpretation

1. Did removing the FINAL ANSWER block reduce overall BERTScore? No.
2. Did it increase or decrease PASS-vs-FAIL separation? Increased.
3. Does this make BERTScore more useful as a reasoning-overlap metric? Removing the FINAL ANSWER block did not materially improve PASS-vs-FAIL separation; the final block is not the main reason BERTScore weakly separates deterministic outcomes.
4. Does deterministic grading remain primary? Yes.
5. Future reporting recommendation: Report both if space permits; otherwise keep deterministic grading primary and treat BERTScore as context.

## Validation

- PASS/FAIL: PASS=117, FAIL=135
- Warning rows: 252
- learning.db modified: false
- raw outputs modified: false
- model/LLM API calls made: false
- old full-answer BERTScore outputs overwritten: false
