# Known Corrections Log

- Layer 1B flagged-run classifier updated to search whole answer for recoverable final-answer blocks rather than last 1200 characters.
- Run 214 reclassified from UNUSABLE to FORMAT_WARNING_KEEP / KEEP_RECOVERABLE_WITH_WARNINGS because complete GPS final-answer blocks existed before tail repetition and values did not conflict.
- Regex bug fixed: literal `&=` requirement misclassified Granite runs 496-498 using `&\approx`; operator matching now accepts `=`, `\approx`, `\approxeq`, `\sim`, `\cong`.
- Run 380 changed from FORMAT_WARNING_KEEP to UNUSABLE due to long invalid/meta output.
- Layer 1B classifier v3 separated clean versus recoverable results.
- Run 214 and run 235 are KEEP_RECOVERABLE_WITH_WARNINGS due to repeated identical filled blocks, blank templates, tail repetition, no conflicting values.
- Extraction Artifact Audit of 91 completed runs found 22 field-level artifacts across 11 runs.
- Cause: normalizer failed harmless formatting wrappers: degree notation, LaTeX text units, unicode/scientific notation.
- No old comma/brace partial-number bug found.
- STAT_ISING_001 `\sqrt2` implicit shorthand handling was not treated as a bug after methodological correction; it was classified as unsupported_expression_class because the declared normalizer grammar supports brace-group forms like `\sqrt{...}`.
- Any correction should be framed with issue, cause, fix, validation, and portfolio/debugging value.

Local artifact note: full answer files were found for runs 214, 380, and 514. Full local raw files for runs 235 and 496-498 were not found in root-level `run_*_full_answer.txt`; their compact audited evidence is included from `remaining_layer1b_flag_classification_v3.csv`.
