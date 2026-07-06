# Metric Comparison Analytics Report

## Purpose

Compare available automatic text metrics against frozen deterministic PASS/FAIL labels without changing grading.

## Inputs Used

- Phase-1-hardened structured summaries
- Structured prompt V2-V5 clean autograde files
- Full-answer BERTScore v1
- No-final-block BERTScore v1

## Dataset Shape

- Rows: 252
- Scenarios: 32
- Models: 8
- Alignment: source_run_id, 252 rows

## Deterministic Label Distribution

- PASS: 117
- FAIL: 135

## Metrics Included

- Full-answer BERTScore F1: provenance/deprecated because references already exclude final-answer sections.
- No-final-block BERTScore F1: valid BERTScore comparison, with known 5-row final-block removal caveat.
- Candidate/reference length ratio: provenance diagnostic only.

## Metric Separation Summary

- Full-answer BERTScore mean gap PASS-FAIL: 0.029271
- No-final BERTScore mean gap PASS-FAIL: 0.081370
- No-final simple effect size: 0.219251

## Full-Answer vs No-Final-Block BERTScore

No-final-block BERTScore separates PASS/FAIL better than full-answer BERTScore in this saved dataset. Full-answer BERTScore is kept for provenance only.

## Scenario-Level Findings

Lowest no-final mean-F1 scenarios:
- GR_GPS_001: 0.253844
- COS_DESITTER_001: 0.307272
- QFT_CASIMIR_001: 0.391952

## Model-Level Findings

- Mistral Small 3.2 24B Instruct: mean no-final F1 0.887452
- Gemma 3 27B IT: mean no-final F1 0.821758
- Mistral NeMo 12B: mean no-final F1 0.794035

## Outlier Examples

- Highest-metric FAIL: COS_CMB_001 / Mistral NeMo 12B / F1 0.972873
- Lowest-metric PASS: CM_TOP_001 / Granite 4.1 8B / F1 -0.194096

## Correlation Findings

- Pearson correlation between deterministic pass binary and no-final BERTScore F1: 0.108686
- Correlation columns included: deterministic_pass_binary, bertscore_full_f1, bertscore_no_final_f1, candidate_reference_length_ratio, candidate_no_final_text_length_chars, reference_text_length_chars

## Human Label Alignment Status

No safely alignable human-reviewed labels were found for the 252 structured CLEAN rows; `human_label_available=false` for all rows.

## Limitations

- Automatic text metrics are secondary/descriptive and do not measure correctness.
- Deterministic PASS/FAIL remains the correctness anchor.
- ROUGE-L and chrF were not computed because saved metric CSVs do not contain candidate/reference text.
- No-final BERTScore v1 has a 5-row final-block removal caveat.

## Next Metrics To Add

- ROUGE-L and chrF from a safe text-bearing analysis artifact.
- Human-review labels if a stable alignment key exists.
- ROSCOE and NLI later, after this base layer is stable.

## Suggested LinkedIn Framing

Use this as a metric-behavior story: deterministic grading catches scientific correctness, while semantic metrics reveal overlap, style, and misleading high-score failures.
