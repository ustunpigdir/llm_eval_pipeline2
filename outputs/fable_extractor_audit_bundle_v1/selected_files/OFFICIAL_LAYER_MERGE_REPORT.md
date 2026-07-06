# Official Layer Merge Report

Date: 2026-07-05

## 1. Copied from zip

Source archive:

`/Users/upigdir/Desktop/Pipeline_SQL_proj_official_benchmark_layer.zip`

Copied into the live project:

- `scripts/import_official_benchmark.py`
- `scripts/grade_official_runs.py`

The original zip scripts were inspected along with:

- `official_benchmark_audit.md`
- `OFFICIAL_BENCHMARK_LAYER_NOTES.md`
- `official_grade.csv`

## 2. Tables and views added

Official benchmark tables now present in `learning.db`:

- `scenarios`
- `benchmark_scenarios`
- `gold_fields`
- `run_scenarios`
- `run_exclusions`
- `grading_results`

Official benchmark views now present:

- `official_gradeable_runs`
- `excluded_runs`
- `grading_summary`
- `grading_model_scores`
- `grading_scenario_scores`
- `grading_summary_by_scenario`
- `grading_summary_by_model`
- `grading_summary_overall`

Existing extraction tables were preserved:

- `questions`
- `extracted_markdown_blocks`
- `extracted_math_spans`
- `extraction_quality_flags`
- `math_span_normalization`
- `final_answer_runs`
- `final_answer_values`

## 3. Scripts added

- `scripts/import_official_benchmark.py`
- `scripts/grade_official_runs.py`
- `scripts/verify_official_benchmark_layer.py`

The older `grade_runs.py` remains intact.

## 4. Backup

Original DB backup:

`backups/pre_official_layer_merge_20260705_094701.db`

## 5. Verification counts

Post-import counts:

- `questions`: 641
- `scenarios`: 32
- `benchmark_scenarios`: 32
- `gold_fields`: 95
- `run_scenarios`: 624
- `run_exclusions`: 17
- `official_gradeable_runs`: 624
- `excluded_runs`: 17

Post-grading counts:

- `grading_results`: 1,861
- `MATCH`: 1,012
- `MISMATCH`: 742
- `REVIEW`: 44
- `NOT_FOUND`: 63

Verification script output:

```text
db_total_runs=641
official_scenarios=32
benchmark_scenarios=32
gold_fields=95
official_gradeable_runs=624
excluded_runs=17
final_answer_runs=641
final_answer_values=1862
grading_result_rows=1861
verdict_distribution=MATCH:1012, MISMATCH:742, NOT_FOUND:63, REVIEW:44
layer1b_raw_flag_count=35
layer1b_classified_unusable_count=7
```

## 6. Expected number match

All target official numbers matched:

- 641 total DB runs
- 32 official benchmark scenarios
- 624 official gradeable runs
- 17 excluded non-benchmark runs
- 95 gold fields
- 1,861 grading result rows

The official grader verdict distribution also matched the zip:

- `MATCH`: 1,012
- `MISMATCH`: 742
- `REVIEW`: 44
- `NOT_FOUND`: 63

## 7. Differences from zip version

The external `Scenarios to Run` directory was not present in the live folder or archive. To run the official import script without field-overlap inference, a temporary scenario directory was reconstructed from `existing_answers.csv` in:

`/tmp/official_scenarios_from_existing_answers`

This temporary input contained the same 32 official scenarios and 95 gold fields, excluding the 17 non-benchmark runs. Prompt matching produced the same official run mapping as the zip audit.

`scripts/grade_official_runs.py` also now creates three additional requested summary views:

- `grading_summary_by_scenario`
- `grading_summary_by_model`
- `grading_summary_overall`

The original zip views are still preserved.

## 8. Remaining architectural issues

Layer 1B final quality classifications still live in CSV/Markdown artifacts, not in a first-class DB table.

Human review overrides and correction history are not yet represented as structured database tables.

The official benchmark layer is now DB-backed, but review-state persistence remains the next design gap.
