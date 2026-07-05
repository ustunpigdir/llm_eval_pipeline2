# Scientific Reasoning Benchmark Pipeline

A local SQLite-backed pipeline for collecting, extracting, normalizing, quality-gating, and grading LLM answers to scientific reasoning benchmark scenarios.

## Current Status

- Raw answers are stored in SQLite.
- Markdown block extraction is implemented.
- Math-span extraction is implemented.
- Deterministic math-span normalization is implemented.
- Final-answer field extraction is implemented.
- Layer 1B structural quality artifacts exist.
- The older field-overlap grading path exists for comparison.
- The official benchmark layer has been integrated additively into the live SQLite database.

## Current Database

Main database:

`learning.db`

Known live extraction tables include:

- `questions`
- `extracted_markdown_blocks`
- `extracted_math_spans`
- `extraction_quality_flags`
- `math_span_normalization`
- `final_answer_runs`
- `final_answer_values`

Official benchmark tables include:

- `scenarios`
- `benchmark_scenarios`
- `gold_fields`
- `run_scenarios`
- `run_exclusions`
- `grading_results`

## Important Warning

The official benchmark layer is now present in the live database, but Layer 1B final quality classifications still live primarily in CSV/Markdown review artifacts. Human review overrides and correction history are not yet represented as first-class database tables.

## Main Scripts

- `import_answers.py`: imports raw answer rows from `existing_answers.csv` into `learning.db`.
- `export_raw_answers_to_md.py`: exports raw DB answers to `raw_answers_md/`.
- `populate_layer1b_from_md.py`: extracts Markdown blocks and math spans from raw Markdown answer exports.
- `populate_extraction_quality_flags.py`: creates delimiter and structural extraction quality flags.
- `classify_remaining_layer1b_flags.py`: classifies flagged Layer 1B runs into clean, recoverable, review, or unusable categories.
- `normalize_math_spans.py`: normalizes extracted math spans deterministically.
- `extract_final_answers.py`: extracts final-answer field/value rows into SQLite.
- `grade_runs.py`: older deterministic grader that infers scenario identity from final-answer field overlap.
- `scripts/import_official_benchmark.py`: imports official benchmark scenario identity and explicit run-to-scenario mappings.
- `scripts/grade_official_runs.py`: grades official benchmark runs using explicit `run_scenarios.scenario_id`.
- `scripts/verify_official_benchmark_layer.py`: prints a compact read-only audit of the official benchmark layer.

## Next Planned Step

Add first-class database tables for Layer 1B quality status, human review overrides, and correction history so review decisions are reproducible without relying on CSV/Markdown artifacts.
