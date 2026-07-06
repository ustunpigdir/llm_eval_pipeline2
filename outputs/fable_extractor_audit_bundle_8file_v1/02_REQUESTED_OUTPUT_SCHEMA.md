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
