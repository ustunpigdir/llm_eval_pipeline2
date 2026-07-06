# Metric Text Artifacts v1

This folder contains the canonical text-bearing input layer for future non-correctness metric comparisons.

It differs from BERTScore outputs by storing the actual candidate full text, extractor-span reasoning-only text, and reference reasoning text, plus hashes and span metadata.

It does not change grading, compute correctness, rerun models, call APIs, modify raw outputs, or modify `learning.db`.

Future metrics should use `canonical_reasoning_text_dataset.csv` or `.json` and verify text hashes via `text_hashes.csv`.

Candidate reasoning text is derived only by removing the extractor-selected final-answer aligned block span from the saved raw model answer.

Rerun with:

```bash
.venv/bin/python scripts/build_metric_text_artifacts_v1.py
```

Files:
- `README.md`
- `CANONICAL_REASONING_TEXT_REPORT.md`
- `canonical_reasoning_text_dataset.csv`
- `canonical_reasoning_text_dataset.json`
- `canonical_reasoning_text_manifest.json`
- `final_block_span_validation.csv`
- `final_block_removal_failures.csv`
- `reference_text_validation.csv`
- `text_hashes.csv`
