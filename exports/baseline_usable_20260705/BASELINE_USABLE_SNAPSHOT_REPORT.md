# Baseline Usable Snapshot Report

## Snapshot Purpose

This snapshot freezes the usable-only official benchmark state before the concept gate is added.

## Pipeline Stage

`post_official_grading_post_structural_quality_pre_concept_gate`

## Counts

- Official gradeable runs: 624
- Usable official gradeable runs: 617
- Unusable official runs: 7
- All grading rows: 1861
- Usable-only grading rows: 1839

## All-Results Verdict Distribution

- MATCH: 1012
- MISMATCH: 742
- NOT_FOUND: 63
- REVIEW: 44

## Usable-Only Verdict Distribution

- MATCH: 1012
- MISMATCH: 742
- NOT_FOUND: 41
- REVIEW: 44

## Change From All-Results To Usable-Only

- Removed grading rows: 22
- Removed NOT_FOUND rows: 22
- MATCH, MISMATCH, and REVIEW counts are unchanged in this baseline.

This snapshot is pre-concept-gate. It only excludes structurally unusable runs through run_quality_status.

## Exported CSV Files

- `all_grading_results_verdict_distribution.csv` (4 rows)
- `all_grading_summary_overall.csv` (4 rows)
- `official_usable_gradeable_runs.csv` (617 rows)
- `unusable_official_runs.csv` (7 rows)
- `usable_grading_results.csv` (1839 rows)
- `usable_grading_summary_by_model.csv` (9 rows)
- `usable_grading_summary_by_scenario.csv` (32 rows)
- `usable_grading_summary_overall.csv` (1 rows)
