# Repo Map For Extractor Audit

## Relevant directories and files
- Root Python scripts: extraction, normalization, symbolic evaluation, Layer 1B classification, and review-layer DB utilities.
- `scripts/`: structured-prompt exporters, review-layer creators, deterministic autograders, truncation test, review-layer setup/verification.
- `outputs/structured_prompt_pilot_v2` through `v5`: structured prompt run plans, review layers, deterministic autograde reports, and compact non-clean examples.
- `outputs/structured_prompt_all32_summary`: combined V2-V5 structured-prompt summaries.

## Model response storage
- Historical/original full examples: `run_*_full_answer.txt`, `raw_answers_md/` (not copied wholesale).
- Structured prompt responses: `outputs/structured_prompt_pilot_v*/structured_prompt_pilot_v*_runs.json` (not copied wholesale; sampled in representative cases).

## Extraction
- `extract_final_answers.py`: final block selection, `field_pairs`, value reduction, operator matching.
- `classify_remaining_layer1b_flags.py`: whole-answer classification of recoverable/nonrecoverable final blocks.

## Normalization
- `normalizer.py`, `normalize_math_spans.py`, `normalize_all_answers.py`, `merge_normalized_body.py`.
- `symbolic_eval.py`: deterministic evaluation used by structured autograding.

## Quality / review layer
- `populate_extraction_quality_flags.py`, `create_extraction_quality_flags_table.py`.
- `scripts/add_review_layer.py`, `scripts/verify_review_layer.py`.
- `scripts/create_structured_prompt*_review_layer_v1.py`.

## Deterministic autograding
- `scripts/autograde_structured_prompt_v5_no_bert.py` is the latest structured autograder.
- It grades only CLEAN rows and uses `gold_fields` plus deterministic numeric/symbolic evaluation.

## Gold fields and DB field order
- Source of truth is SQLite table `gold_fields`, ordered by `field_index`.
- Exporters rebuild final-answer blocks in DB order and validate field order.

## Reports
- Current state reports live under structured-prompt output folders and `outputs/structured_prompt_all32_summary/`.
