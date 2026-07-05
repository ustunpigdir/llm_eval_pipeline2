# Three-Run BERTScore Pilot

## Purpose

Compare gold worked-solution reference text against model answer text for a tiny usable-run pilot.

## Reference Source Files

- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch1.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch2.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch3.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch4.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch5.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch6.md`
- `/Users/upigdir/Desktop/Pipeline/Scenarios to Run/worked_solutions_batch7.md`

## Reference Parsing Result

- Parsed scenario references: 32
- Missing official references: none
- Extra reference IDs: none

## Selected 3 Runs

| run_id | scenario_id | model_name | MATCH | MISMATCH | NOT_FOUND | REVIEW |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | CM_APSIDAL_001 | Gemma 3 12B IT | 4 | 0 | 0 | 0 |
| 15 | CM_APSIDAL_001 | Llama 3.1 8B Instruct | 0 | 4 | 0 | 0 |
| 530 | QM_TUNNEL_001 | NVIDIA Nemotron 3 Nano 30B-A3B | 0 | 0 | 4 | 0 |

## BERTScore Results

| run_id | scenario_id | precision | recall | f1 |
| --- | --- | ---: | ---: | ---: |
| 1 | CM_APSIDAL_001 | -0.109246 | 0.092020 | -0.009022 |
| 15 | CM_APSIDAL_001 | -0.208209 | -0.054447 | -0.130714 |
| 530 | QM_TUNNEL_001 | -0.254910 | -0.324226 | -0.287733 |

## Interpretation

This pilot is meant to test whether semantic similarity offers a useful signal alongside deterministic verdict counts.

## Limitations

This pilot scores the full model answer, not a separately extracted concept-explanation span. Full-answer BERTScore may be inflated by copied formulas, repeated prompt text, or final-answer formatting.

## Recommendation

Continue only if the three-run scores separate the strong deterministic case from mismatch/not-found/review cases enough to justify a broader validation set.
