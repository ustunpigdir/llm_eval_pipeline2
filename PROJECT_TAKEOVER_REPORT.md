# PROJECT_TAKEOVER_REPORT

Date: 2026-07-04
Scope: `Pipeline SQL proj/` — the math-extraction / Layer 1B pipeline built on `learning.db`.
Method: read-only inspection. Nothing was edited, moved, or deleted.

---

## 1. Project state summary

This folder is a **script-based extraction pipeline**, not the FastAPI app. `app.py` is a
one-row normalizer, not a UI. The pipeline stores raw model answers and three additive
extraction layers (Markdown blocks, math spans, quality flags) in a single SQLite file,
`learning.db`.

Current stage of work: Qwen runs have been deleted, the post-Qwen dataset (641 runs) has
full extraction coverage, and the 34 remaining Layer 1B warning-flagged runs have been
manually triaged through three classification passes (v1 → v2 → v3). The v3 pass is the
current source of truth for usability. No numeric/gold comparison has been done yet.

All counts, span totals, flag totals, and the confirmed unusable set stated in the takeover
brief **match the database exactly**. No discrepancies found.

Two facts that differ from the brief's framing, worth flagging:

- The v3 classification lives **only in CSV/Markdown files**, not in `learning.db`. There is
  no label/classification column anywhere in the schema. Any downstream step must read the CSV.
- `questions.scenario_id` does not exist; the v3 CSV records `scenario_id = "unknown"` for
  every row. Scenario is only implicit inside the `question` text.

---

## 2. Database / table inventory

Active DB: `learning.db` (13.6 MB). Backup: `backups/pre_delete_qwen_20260704_135321.db`
(pre-Qwen-deletion snapshot, same size). 4 tables, 0 views.

| Table | Rows | Purpose | Join key |
|---|---|---|---|
| `questions` | 641 | one row per run: raw answer + metadata | `id` (= `run_id`) |
| `extracted_markdown_blocks` | 24,905 | Layer 1 Markdown block extraction | `run_id` |
| `extracted_math_spans` | 18,076 | Layer 1 math-span extraction | `run_id` |
| `extraction_quality_flags` | 35 | Layer 1B delimiter/structure flags | `run_id` |

`questions` columns: `id`(pk), `run_id`, `model_name`, `question`, `answer`,
`normalized_answer`, `reasoning_text`, `calculation_text`.
Note: `id == run_id` for all 641 rows, so either can be used as the join key.
`reasoning_text` and `calculation_text` columns exist but are **0/641 populated** (added, never filled).

`extracted_math_spans` columns: `run_id`, `span_index`, `span_type`, `source`,
`start_char`, `end_char`, `raw_text`, `normalized_text`, `created_at`.
`extraction_quality_flags` columns: `run_id`, `flag_type`, `severity`, `source`,
`detail`, `created_at`. All three extraction tables are indexed on `run_id`.

Key files in this folder:
- Classifier: `classify_remaining_layer1b_flags.py` (25 KB — the v3 detector logic).
- v3 outputs: `remaining_layer1b_flag_classification_v3.csv` / `.md` (also v1, v2 kept).
- Unusable inspection: `inspect_unusable_runs.py` / `.md` / `.csv`, plus per-run dumps
  `run_{185,187,188,214,256,286,380,514}_full_answer.txt`.
- Layer builders: `create_layer1b_tables.py`, `create_extraction_quality_flags_table.py`,
  `populate_layer1b_from_md.py`, `populate_extraction_quality_flags.py`.
- Raw answer exports: `raw_answers_md/` (709 `.md` files, includes pre-deletion Qwen files).

---

## 3. Current dataset counts (verified against DB)

| Metric | Value | Brief | Match |
|---|---|---|---|
| Total runs (`questions`) | 641 | 641 | ✓ |
| Non-empty raw answers | 641 | 641 | ✓ |
| Runs with ≥1 Markdown block | 641 | full | ✓ |
| Runs with ≥1 math span | 641 | full | ✓ |
| Remaining Qwen runs | 0 | 0 | ✓ |
| `normalized_answer` populated | 641 | — | — |
| Markdown blocks total | 24,905 | 24,905 | ✓ |
| Math spans total | 18,076 | 18,076 | ✓ |
| — display_math | 8,443 | 8,443 | ✓ |
| — inline_math | 9,545 | 9,545 | ✓ |
| — environment | 88 | 88 | ✓ |

`run_id` range is 1–704 with gaps (deleted Qwen rows). 13 models present; the five 8–12B
open models dominate (Mistral NeMo 101, Gemma 3 12B 100, Ministral 3 8B 99, Llama 3.1 8B 99,
Granite 4.1 8B 97). Paid/cloud models are sparse (Gemini 2.5 Pro 3, DeepSeek Reasoner 2).

---

## 4. Layer 1B audit status

| Metric | Value | Brief | Match |
|---|---|---|---|
| Total flags | 35 | 35 | ✓ |
| Distinct flagged runs | 34 | 34 | ✓ |
| Critical flags | 0 | 0 | ✓ |
| Warning flags | 35 | 35 | ✓ |

Flag types: `unmatched_bracket_display` 29, `odd_single_dollar` 4, `unmatched_environment` 2.
No `short_math_heavy_answer` and no `math_markers_but_zero_spans` cases exist, as expected.

Confirmed correction from the brief holds: these warning flags are **not all harmless**. Of
the 34 flagged runs, 7 are UNUSABLE and 3 are recoverable-with-warnings; the flag alone does
not determine usability, which is why the v3 structural pass was needed.

---

## 5. v3 classification summary

Source: `remaining_layer1b_flag_classification_v3.csv` (34 rows = the 34 flagged runs only).
The other 607 unflagged runs are implicitly clean.

| Category | Count (flagged set) |
|---|---|
| KEEP_CLEAN | 24 |
| KEEP_RECOVERABLE_WITH_WARNINGS | 3 |
| REVIEW | 0 |
| UNUSABLE | 7 |

- KEEP_RECOVERABLE (3): runs **214, 235, 290** — recoverable filled final block but
  structural pollution (repeated/blank/tail blocks, or display-span pollution near the final).
- KEEP_CLEAN (24) includes **496, 497, 498** (valid `&\approx` final blocks — correctly not
  penalized for intermediate aligned derivation blocks).

Report-vs-DB mismatch: the DB stores **no** classification. Whole-dataset usability =
607 unflagged (clean) + 24 flagged-clean + 3 recoverable = **634 usable**, 7 unusable.

---

## 6. Confirmed unusable runs (7)

`185, 187, 188, 256, 286, 380, 514` — matches the brief exactly. Each was inspected via its
`run_*_full_answer.txt` dump. None contains a complete, filled, field-bearing final-answer block.

| Run | Model | Len | Confirmed failure mode |
|---|---|---|---|
| 185 | Llama 3.1 8B | 24,938 | Repetition loop ("Simplifying…" ×37; identical m₁/m₂ lines); truncated mid-substitution. No final block, no stable value. |
| 187 | Ministral 3 8B | 28,413 | Repetition (×19); truncated mid-number (`≈ 8.73 ×`). No final block. |
| 188 | Ministral 3 8B | 23,990 | Repetition of prefactor line (×23); truncated mid-number. No final block. |
| 256 | Nemotron 3 Nano 30B | 913 | Early truncation — cuts off mid-calc (`=5.`). No final block. |
| 286 | Llama 3.1 8B | 27,129 | Severe repetition loop — same `|P|` line ×286. No final block, no stable value. |
| 380 | Ministral 3 8B | 38,889 | Self-rejection loop: 34 "Final Answer" headings, 177 `(no)` markers around a self-rejected formula. No valid block. |
| 514 | Gemma 3 12B | 25,613 | Repetition loop (`T e^{-2κL}` chained inline); nonsense intermediate value. No final block. |

Summary of causes: truncation (185, 187, 188, 256), repetition loop (185, 187, 188, 286, 514),
self-rejected final answer (380). No stable recoverable values in any of the 7.

---

## 7. Known pitfalls and corrected bugs (carry forward)

Final-answer detection must respect these, already learned by the v3 pass:

1. **Search the whole answer**, not just the last ~1200 chars, for final-answer blocks.
2. **Accept operator variants**, not literal `&=` only: `&=`, `& =`, `&\approx`, `& \approx`,
   `&\approxeq`, `&\sim`, `&\cong`.
3. **Not every `\begin{aligned}` is a final block.** Intermediate derivation aligned blocks are
   normal; only filled, field-bearing final-answer-like blocks affect classification.
4. **A "Final Answer" heading alone is insufficient** — a filled, field-bearing block is required
   (run 380 is the counter-example: many headings, no valid block).
5. **Recoverable ≠ clean.** A valid final block before tail garbage is
   KEEP_RECOVERABLE_WITH_WARNINGS, not UNUSABLE and not KEEP_CLEAN.

Prior extractor artifacts to avoid downstream: `local_total_queries` mistaken for
`extra_queries`; powers like `10^4` read as `10`; nearest-number extraction errors; dropped
provider reasoning content.

Hard constraints (unchanged): do not modify raw answers, Markdown blocks, or math spans; do
not delete runs; no LLM calls in the pipeline; no new dependencies; additive layers only;
idempotent scripts.

---

## 8. Recommended next step (single task)

Build a **simple, auditable final-answer value extractor** over the usable set only. Keep it
deterministic; no symbolic parsing yet.

Specification:
- Read `remaining_layer1b_flag_classification_v3.csv`; treat the 7 UNUSABLE run_ids as excluded.
  Target = all runs **except** those 7 (634 runs): 607 unflagged clean + 24 flagged-clean +
  3 recoverable.
- For each target run, locate the final-answer field block using the rules in §7 (whole-answer
  search, operator variants, field-bearing filled block required).
- **Preserve raw values verbatim.** Normalize only obvious numeric forms (plain decimals,
  simple `a × 10^b`). Do **not** attempt symbolic/LaTeX evaluation.
- Mark anything not confidently numeric as `unsupported_expression` explicitly — never guess.
- Write results to a **new additive table** (e.g. `final_answer_values`) plus a review CSV.
  Do not touch existing tables. Make the script idempotent (upsert per run_id).
- Do **not** compare to gold values in this step.

Why this and not more: it turns the human-reviewed v3 labels into a concrete, reviewable value
layer without building a compiler or symbolic engine, and it is the smallest step that unblocks
later numeric/gold comparison.

Note before implementing: because SQLite writes over the mounted folder can be flaky, run the
build against a copy in a local temp dir, then place the resulting DB/CSV back — and back up
`learning.db` first.

**Stopping here as instructed.** No code written. Awaiting explicit go-ahead to implement §8.

---

# PROJECT FREEZE & NEXT STEPS — 2026-07-04

**This part of the project is FROZEN.** The v1 tooling is complete and set aside:
extraction → normalization → body-merge → final-answer value extraction → deterministic
three-state grader (`grade_runs.py` + `symbolic_eval.py`) → severity metric. The 32 physics
scenarios and their gold keys are human-**LOCKED** (2026-07-04).

**The v1 response set is NOT used for conclusions.** The 641 `learning.db` runs predate the
locked gold, so they are confounded two ways: (a) parameter drift (old runs used different
inputs than the current gold), and (b) survivorship bias (runs with no final block were
excluded from grading, which flatters models that leave blanks — e.g. the Nemotron 0.05
"best" artifact). These numbers only proved the metric computes; they are not a fair baseline.

**Next step = data-analytic conclusions on a NEW, structured run set:**
- Re-run the **same 32 scenarios** with the **same locked gold**, but a more **structured**
  prompt approach: freer-form answers that make intermediate-step data easier to extract;
  built by iterative prompt engineering (first shot = ask + collect).
- Grade every error on a single **severity** scale (severe / high / mid / low; no
  numeric-vs-conceptual split), scored over **all expected fields with missing = severe**
  (fixes the survivorship bias). Severity decides LLM-correction routing.
- Experiment: give the model the gold key, **change only the numeric values** (re-derive the
  matched gold by rerunning the parametric generator), re-ask, compare error %, chart, publish.
  Hold the new numbers fixed and vary only key-provision so the key effect isn't confounded.
- **Analysis via peer clustering:** group models into capability peer-clusters (by size /
  family / tier) and compare **each model against its peers**, never across tiers — avoids the
  apples-to-oranges bias in cross-tier comparison. Then derive conclusions (per-cluster error
  profiles, failure patterns, response comparisons) and chart/publish.

Frozen deliverables live in: `Pipeline SQL proj/` (grader, symbolic_eval, extractors) and
`Desktop/Pipeline/Scenarios to Run/` (locked scenario JSONs, worked solutions, gold_normalized).
