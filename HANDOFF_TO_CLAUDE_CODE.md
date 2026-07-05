# Handoff to Claude Code — PQS math-extraction pipeline (`learning.db`)

Paste this file (or point Claude Code at it) to continue the work.

## Context
Local, script-based LLM-evaluation pipeline for scientific reasoning. Single SQLite DB
`learning.db` (this folder). 641 runs (Qwen deleted), full extraction coverage. Tables:
- `questions` — 641 runs; `id` == `run_id`; raw `answer` (do not modify).
- `extracted_markdown_blocks` — 24,905 (Layer 1).
- `extracted_math_spans` — 18,076 (Layer 1: 9,545 inline / 8,443 display / 88 environment).
- `extraction_quality_flags` — 35 warning flags / 34 runs, 0 critical (Layer 1B).
- `math_span_normalization` — NEW (Layer 1C, below).

Usability lives only in `remaining_layer1b_flag_classification_v3.csv` (NOT in the DB):
24 KEEP_CLEAN, 3 KEEP_RECOVERABLE (214, 235, 290), 7 UNUSABLE (185,187,188,256,286,380,514).
See `PROJECT_TAKEOVER_REPORT.md` for full state.

## What was just built — Layer 1C: `normalize_math_spans.py`
Deterministic normalization of `extracted_math_spans.raw_text`.
- Writes ONLY to new additive table `math_span_normalization`
  (`span_id` PK = spans.id, `run_id`, `span_type`, `status`, `method`, `normalized_text`,
  `method_version`, `created_at`). Never modifies `extracted_math_spans`.
- Engine: `pylatexenc` (already in the venv) + a thin regex layer that strips delimiters
  (`$ $$ \[ \] \( \)`), format-only markup (`\left \right \, \; \quad`), and alignment
  (`&`, `\\`). No sympy, no LLM, no symbolic parsing.
- Status classes: REAL (normalized) / TRIVIAL / PROSE / ELIDED / EMPTY (noise, left NULL).

Run (inside the project venv):
```
python3 normalize_math_spans.py --report          # create + populate table (idempotent)
python3 normalize_math_spans.py --csv review.csv  # export raw vs normalized for review
python3 normalize_math_spans.py --force            # recompute all rows deterministically
python3 normalize_math_spans.py --dry-run          # compute + report, write nothing
```
Reversible: `DROP TABLE math_span_normalization;`

### Verification already done (on /var/tmp copies, not the live DB)
- 18,076 classified: REAL 16,554 (all pylatexenc, 0 fallbacks), TRIVIAL 925, PROSE 516,
  EMPTY 65, ELIDED 16.
- 0 digit-character loss across all 16,554 REAL spans (only 48 token diffs, all
  `\frac12` → `1/2` expansions).
- Deterministic: `--force` gives byte-identical output. Idempotent: 2nd run processes 0.

### Why sympy was rejected as the normalizer (don't reintroduce it here)
`sympy.parse_latex` "parses" 84% of spans but silently returns `False` on chained
equalities (`a=b=c`) and invents symbols on units (`\approx`, `\text{MeV}` → `approx`,
`text`). It would inject artifacts. Reserve sympy for a later, filtered, *verified*
numeric-value pass only.

## Hard constraints (unchanged — enforce these)
- Do not modify raw answers, markdown blocks, or math-span `raw_text`.
- Do not delete runs. Any destructive op needs explicit confirmation.
- No LLM calls in the pipeline. No new dependencies unless already installed or approved.
- Additive layers only. All scripts idempotent. Small, testable changes.
- Human (Ustun) is the final reviewer; do not treat autograder output as truth.
- SQLite over a synced/mounted folder can be flaky — prefer building against a local copy,
  back up `learning.db` first (backup dir: `backups/`).

## Next task (spec — not yet built)
Final-answer VALUE extractor over the 634 non-UNUSABLE runs (exclude the 7 UNUSABLE).
- Read `remaining_layer1b_flag_classification_v3.csv`; skip UNUSABLE.
- Locate the field-bearing final-answer block per run (rules in PROJECT_TAKEOVER_REPORT.md
  §7: whole-answer search; operators `&= & = &\approx &\sim &\cong`; a "Final Answer"
  heading alone is not enough; ignore intermediate `aligned` derivation blocks).
- Prefer `math_span_normalization.normalized_text` for the span values.
- Preserve raw values; normalize only obvious numeric forms (`a × 10^b`); mark anything
  non-numeric `unsupported_expression`. No symbolic eval. No gold comparison yet.
- Write a NEW additive table `final_answer_values` + a review CSV. Idempotent.

Stop after the extractor + its test command; report, don't chain further.
