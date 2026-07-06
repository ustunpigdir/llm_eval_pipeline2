# Fable Extractor Audit Bundle v1

This is a compact curated bundle for expert review of the Pipeline extractor, normalizer, final-answer parser, quality/review layer, and deterministic autograder logic.

It excludes raw response folders, full databases, backups, virtual environments, cache folders, `.env` files, API keys, PDFs, and BERTScore outputs. Large CSVs are included only as excerpts when useful.

How to use with Fable:
1. Paste or attach `FABLE_AUDIT_PROMPT.md`.
2. Attach this bundle or selected files from it.
3. Ask Fable to follow `requested_output_schema.md` exactly.

Expected next step after Fable review: manually validate recommendations, implement only deterministic/testable changes, then add regression tests before touching benchmark results.

Warning: Fable output is advisory. Do not accept fixes without local validation against representative cases and existing official grading artifacts.
