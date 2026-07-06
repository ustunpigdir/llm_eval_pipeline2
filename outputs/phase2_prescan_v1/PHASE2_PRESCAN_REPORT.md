# Phase 2 Impact Pre-Scan

## Executive Summary

- Current CLEAN rows: 252
- Current REVIEW rows: 12
- Current PASS/FAIL: PASS=117, FAIL=135
- Predicted NOT_GRADEABLE under scan-only rule: 5
- Predicted remaining FAIL after NOT_GRADEABLE split: 130
- Predicted gradeable denominator: 247
- Predicted pass rate if only NOT_GRADEABLE semantics change: 0.473684

## Frozen Phase 1 Metrics

- total_structured_runs: 264
- CLEAN: 252
- REVIEW: 12
- PASS: 117
- FAIL: 135
- clean-row pass rate: 0.464286
- extraction_status_distribution: {"OK": 252}
- stability_decision: STABLE_NO_METRIC_CHANGE

## FAIL Error-Tag Distribution

| tag | count |
| --- | ---: |
| MISMATCH | 606 |
| UNPARSEABLE | 12 |
| UNPARSEABLE:parse-fail | 6 |
| UNPARSEABLE:parse-fail:TokenError | 4 |
| UNPARSEABLE:parse-fail:SympifyError | 2 |

## Predicted NOT_GRADEABLE Impact

- current_FAIL_count: 135
- predicted_NOT_GRADEABLE_count: 5
- predicted_FAIL_count_after_phase2: 130
- predicted_PASS_count_after_phase2: 117
- predicted_gradeable_denominator: 247
- predicted_phase2_pass_rate_if_only_NOT_GRADEABLE_semantics_change: 0.473684

## Explicit-Base Log Candidate Impact

- candidates: 13

## REVIEW Recovery Candidate Count

- REVIEW rows: 12
- safe_to_recover_candidate: 0
- recovery types: {'all_blank': 2, 'true_conflict': 1, 'blank_template_after_filled_block': 2, 'unknown': 2, 'no_valid_block': 5}

## Duplicate-Field Scan

- duplicate field entries: 0
- rows_with_duplicate_fields: 0
- rows_with_conflicting_duplicate_fields: 0
- rows_with_identical_duplicate_fields: 0

## Gold-Data Scan

- gold-data issue rows: 0

## Percent/Ellipsis Risk Scan

- affected field entries: 0
- risk types: {}

## BERTScore Block-Removal Mismatch Scan

- candidate removal mismatches: 5
- Reference no-final warnings are expected because the reference parser already stops before final-answer sections.

## Review/Autograder Version-Skew Risks

- scripts/autograde_structured_prompt_v2_no_bert.py contains local FIELD_SET_MISMATCH handling
- scripts/autograde_structured_prompt_v3_no_bert.py contains local FIELD_SET_MISMATCH handling
- scripts/autograde_structured_prompt_v4_no_bert.py contains local FIELD_SET_MISMATCH handling
- scripts/autograde_structured_prompt_v5_no_bert.py contains local FIELD_SET_MISMATCH handling
- scripts/run_bertscore_structured_all32_phase1_hardened_no_final_block.py contains local final-answer/block regex or marker logic

## Recommended Phase 2 Implementation Order

1. Centralize final-answer block locating/extraction and reuse it for BERTScore text transforms.
2. Add NOT_GRADEABLE semantics behind a reporting-only switch, using this pre-scan candidate list as a regression fixture.
3. Add explicit-base log parsing, then re-run the pre-scan before changing grades.
4. Add duplicate-field diagnostics before any numeric-aware conflict recovery.
5. Validate gold-field metadata stays clean before changing tolerance semantics.

## Phase 1 Freeze Recommendation

- Phase 1 metrics should remain frozen. This scan does not justify rewriting Phase 1 artifacts.

## Urgent Corrections Before Phase 2

- The BERTScore no-final block transform should reuse extractor block logic before future metric runs.
- No urgent DB or raw-output correction is indicated by this read-only scan.

## Manifest

```json
{
  "bertscore_block_removal_mismatches": 5,
  "bertscore_run": false,
  "counts_reconciled": {
    "CLEAN": true,
    "FAIL": true,
    "PASS": true,
    "REVIEW": true,
    "scenario_count": true,
    "total_structured_runs": true
  },
  "created_at": "2026-07-05T22:13:40+00:00",
  "duplicate_field_candidates": 0,
  "explicit_base_log_candidates": 13,
  "external_api_calls": false,
  "fail_count": 135,
  "fail_error_tag_distribution": {
    "": 309,
    "MISMATCH": 606,
    "UNPARSEABLE": 12,
    "UNPARSEABLE:parse-fail": 6,
    "UNPARSEABLE:parse-fail:SympifyError": 2,
    "UNPARSEABLE:parse-fail:TokenError": 4
  },
  "gold_data_issues": 0,
  "input_folders": [
    "outputs/structured_prompt_pilot_v2/",
    "outputs/structured_prompt_pilot_v3/",
    "outputs/structured_prompt_pilot_v4/",
    "outputs/structured_prompt_pilot_v5/",
    "outputs/structured_prompt_all32_summary_phase1_hardened/",
    "outputs/bertscore_structured_all32_phase1_hardened_no_final_block_v1/"
  ],
  "learning_db_modified": false,
  "output_files": [
    "PHASE2_PRESCAN_REPORT.md",
    "phase2_prescan_fail_error_tags.csv",
    "phase2_prescan_fail_to_not_gradeable_candidates.csv",
    "phase2_prescan_review_recovery_candidates.csv",
    "phase2_prescan_duplicate_field_candidates.csv",
    "phase2_prescan_gold_data_issues.csv",
    "phase2_prescan_tolerance_modes.csv",
    "phase2_prescan_bertscore_final_block_removal_mismatches.csv",
    "phase2_prescan_manifest.json",
    "phase2_prescan_additional_findings.json"
  ],
  "pass_count": 117,
  "percent_ellipsis_risks": 0,
  "phase2_semantics_implemented": false,
  "predicted_fail_count_after_phase2": 130,
  "predicted_gradeable_denominator": 247,
  "predicted_not_gradeable_count": 5,
  "predicted_pass_count_after_phase2": 117,
  "predicted_phase2_pass_rate_if_only_NOT_GRADEABLE_semantics_change": 0.47368421052631576,
  "raw_outputs_modified": false,
  "read_only": true,
  "review_recovery_candidates_safe": 0,
  "script": "scripts/prescan_phase2_impact.py",
  "total_clean_rows": 252,
  "total_review_rows": 12,
  "total_structured_runs": 264
}
```
