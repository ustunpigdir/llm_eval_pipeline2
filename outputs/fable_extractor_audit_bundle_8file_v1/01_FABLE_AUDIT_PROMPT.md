# Prompt For Claude Fable 5

You are reviewing a scientific-reasoning LLM evaluation pipeline. The bundle contains selected extractor, normalizer, review-layer, and autograder files plus representative cases.

Your task is to audit, not rewrite. Prioritize deterministic, testable improvements. Do not suggest an LLM judge as the primary solution. Do not ask for the entire repo unless absolutely necessary. Do not propose broad rewrites. Use the requested output schema exactly.

Focus areas:
1. final-answer block extraction
2. LaTeX / numeric normalization
3. field-name matching
4. DB field-order validation
5. helper_status classification
6. CLEAN vs REVIEW logic
7. deterministic autograding interface
8. known extraction artifacts and previous fixes
9. current structured-prompt results showing extraction stability
10. remaining risks and improvement opportunities

Read these first:
- `README.md`
- `repo_map.md`
- `current_pipeline_findings.md`
- `known_corrections_log.md`
- `requested_output_schema.md`
- representative cases in `representative_cases/`

Then inspect only the selected source files needed for your findings.

# Fable Extractor Audit

## Executive summary
- highest priority finding
- overall risk level
- whether extractor is currently portfolio-safe

## Architecture understanding
Briefly restate how the extractor/review/autograde pipeline appears to work.

## Critical risks
For each:
- risk_id
- severity: HIGH/MEDIUM/LOW
- affected component
- evidence from bundle
- likely failure mode
- recommended fix
- test case to add

## Deterministic improvement opportunities
For each:
- improvement_id
- expected impact
- implementation difficulty
- files likely affected
- proposed logic
- regression tests

## Normalization grammar recommendations
- supported syntax to add
- syntax to explicitly reject
- syntax to classify as unsupported_expression_class
- examples

## Review-layer recommendations
- CLEAN criteria
- REVIEW criteria
- UNUSABLE criteria
- recoverable-with-warning criteria
- conflict detection improvements

## Autograder interface recommendations
- what should stay deterministic
- where symbolic equivalence is safe
- where symbolic equivalence is risky
- how to separate extraction failure from reasoning failure

## Test suite proposal
Table with:
- test_name
- input snippet
- expected extraction status
- expected normalized value
- expected classification
- why it matters

## Minimal implementation plan
Phase 1:
Phase 2:
Phase 3:

## What not to change
List things that are working and should not be rewritten.

## Open questions for the human owner
List only questions that block implementation.
