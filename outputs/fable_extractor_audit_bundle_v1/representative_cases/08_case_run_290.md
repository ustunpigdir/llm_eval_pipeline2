# LaTeX text units and display-span pollution recoverable

- case_id: `case_run_290`
- scenario_id: `unknown`
- model_name: `Mistral NeMo 12B`
- source_batch: `original_layer1b`
- helper_status: `KEEP_RECOVERABLE_WITH_WARNINGS`
- deterministic_grade: ``
- why_included: Local full answer not present; classification table preserves compact audited evidence.
- source_paths: remaining_layer1b_flag_classification_v3.csv

## Raw Final-Answer / Evidence Excerpt

```text
classification=KEEP_RECOVERABLE_WITH_WARNINGS
reason=filled final-answer block is recoverable (values: 1.3 \times 10^{-3} \text{ Pa}, 3.9 \times 10^{-5} \text{ μJ/m}^2, 1.56 \times 10^{-4} \text{ Pa}) but answer has structural pollution: the stored display_math span for this block also swallowed surrounding prose
filled_final_block_count=1 blank_template_block_count=0 distinct_filled_final_block_count=1
```

## Extracted Fields

```json
[]
```

## Expected / Gold Fields

```json
[]
```
