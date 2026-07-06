# Large Numeric Failure Manual Audit Packet v1

## 1. Purpose

Review candidate logical gates before formalizing them. This packet does not change deterministic labels.

## 2. What This Packet Contains

- One compact Markdown report
- One audit-card file
- One Markdown file per gate
- CSV/JSON card data for later formal gate design

## 3. One-Screen Summary

- 98 fields above 100% relative error
- 62 rows affected
- 42 fields above 1000% relative error
- strongest candidate gates: ORDER_OF_MAGNITUDE_GATE, EXTREME_EXPLOSION_GATE, POWER_OF_TEN_SCALE_GATE, SIGN_FLIP_GATE, WRONG_FIELD_SCALE_GATE

## 4. Gate Candidates in Plain English

- **ORDER_OF_MAGNITUDE_GATE:** The answer is at least 10 times too large or too small.
- **EXTREME_EXPLOSION_GATE:** The answer is more than 1000% away from gold.
- **POWER_OF_TEN_SCALE_GATE:** The answer looks shifted by decimal or scientific-notation scale.
- **SIGN_FLIP_GATE:** The magnitude is similar but the sign is wrong.
- **WRONG_FIELD_SCALE_GATE:** The answer looks closer to another field's expected value than to its own.

## 5. How to Read an Audit Card

Start with the field, gold value, model value, relative error, ratio, and suggested gate. Then answer the audit question using the manual decision options.

## 6. Recommended Audit Order

1. ORDER_OF_MAGNITUDE_GATE
2. EXTREME_EXPLOSION_GATE
3. POWER_OF_TEN_SCALE_GATE
4. SIGN_FLIP_GATE
5. WRONG_FIELD_SCALE_GATE
6. UNCLASSIFIED_LARGE_GATE

## 7. Summary of Selected Examples

| Gate | Cards |
|---|---:|
| EXTREME_EXPLOSION_GATE | 10 |
| ORDER_OF_MAGNITUDE_GATE | 11 |
| POWER_OF_TEN_SCALE_GATE | 10 |
| SIGN_FLIP_GATE | 6 |
| UNCLASSIFIED_LARGE_GATE | 10 |
| WRONG_FIELD_SCALE_GATE | 5 |

## 8. Key Observations

- Order-of-magnitude and extreme-explosion candidates are the broadest high-signal groups.
- Sign-flip candidates are concentrated and easier to inspect manually.
- Wrong-field-scale examples need scenario context before formalizing.

## 9. Limitations

- Raw final-answer blocks were not reconstructed; cards show normalized extracted values.
- All gate labels are preliminary heuristic suggestions.
- No labels or source artifacts were changed.

## 10. Next Step After Manual Audit

Mark each card with CONFIRM_GATE, REJECT_GATE_FALSE_POSITIVE, REASSIGN_TO_DIFFERENT_GATE, NEEDS_SCENARIO_CONTEXT, or NEEDS_RAW_ANSWER_REVIEW.
