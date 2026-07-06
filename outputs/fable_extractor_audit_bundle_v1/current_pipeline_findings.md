# Current Pipeline Findings

- Original benchmark had 641 answers.
- BERTScore full usable baseline scored 617 usable official runs.
- Structured prompt all-32 coverage is complete across V2-V5.
- Combined structured results:
  - total_structured_runs: 264
  - total_CLEAN_rows: 252
  - total_REVIEW_rows: 12
  - PASS: 117
  - FAIL: 135
  - overall clean-row pass rate: 0.464286
  - BERTScore not run for structured prompts
- V5 completed:
  - 64/64 completed
  - 64/64 extractable
  - 64 CLEAN
  - 0 REVIEW
  - PASS 37 / FAIL 27
  - pass rate 0.578125

Important methodological point: structured prompting improves measurability and extraction reliability, but does not make models reliably correct. Many failures are genuine reasoning/calculation failures under clean extraction.
