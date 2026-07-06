# Canonical Reasoning Text Report

## Purpose

Create a canonical text-bearing artifact for future non-correctness text metrics.

## Inputs Used

- Structured prompt V2-V5 saved raw outputs
- Metric comparison analytics v1 base dataset
- Existing BERTScore full/no-final outputs for alignment metadata
- Existing BERTScore reference parser over worked solution Markdown files

## Row Counts

- Rows: 252
- Scenarios: 32
- Models: 8
- Batches: V2, V3, V4, V5

## PASS/FAIL Distribution

- PASS: 117
- FAIL: 135

## Final-Answer Block Removal Result

- Extractor span removal success: 252
- Extractor span removal failure: 0

## Comparison To BERTScore No-Final v1 Removal

- Disagreements: 5
- The disagreements are expected to be the 5 rows where BERTScore v1 regex removal missed a block but extractor-span removal succeeds.

## Reference Text Validation

- References resolved: 32/32
- References with final-answer marker warning: 3
- References with aligned final block warning: 3

## Text Length Summary

- Candidate full text mean/median chars: 1101.3 / 908.5
- Candidate reasoning text mean/median chars: 945.0 / 762.0
- Reference reasoning text mean/median chars: 746.6 / 670.0

## Hashing And Reproducibility

Every row stores SHA-256 hashes for candidate full text, candidate reasoning text, and reference reasoning text.

## Known Limitations

- Candidate reasoning text removes the extractor-selected aligned block span, not surrounding heading text.
- This artifact carries text for metric computation but does not decide correctness.
- Reference text follows the existing BERTScore reference extraction logic.

## Recommended Next Metrics

- ROUGE-L and chrF from `candidate_reasoning_text` vs `reference_reasoning_text`.
- Re-run BERTScore from this artifact if final-block removal needs to be fully canonical.
- Add ROSCOE/NLI only after this text layer is treated as the frozen source.
