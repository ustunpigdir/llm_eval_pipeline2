# Full Usable BERTScore Report

## Purpose

Freeze the current natural-answer usable official runs before a future structured-prompt rerun.

## Counts

- Usable official runs: 617
- BERTScore result rows: 617
- Scenario references parsed: 32
- Rescale with baseline: True

## Overall F1

- Mean: -0.163535
- Median: -0.167048
- Min: -0.406720
- Max: 0.082070

## Summary By Deterministic Group

| group | n_runs | mean_f1 | min_f1 | max_f1 |
| --- | ---: | ---: | ---: | ---: |
| MATCH_HEAVY | 251 | -0.144806 | -0.389750 | 0.078615 |
| MISMATCH_HEAVY | 265 | -0.171889 | -0.371168 | 0.082070 |
| MIXED | 68 | -0.184224 | -0.406720 | -0.030141 |
| NOT_FOUND_REVIEW_HEAVY | 33 | -0.196265 | -0.364747 | -0.015494 |

## Outputs

- `bertscore_full_usable_results.csv`
- `bertscore_summary_by_model.csv`
- `bertscore_summary_by_scenario.csv`
- `bertscore_summary_by_deterministic_group.csv`
- `manifest.json`
