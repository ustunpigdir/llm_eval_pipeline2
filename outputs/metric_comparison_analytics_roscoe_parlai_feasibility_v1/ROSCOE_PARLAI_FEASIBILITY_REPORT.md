# ROSCOE ParlAI Feasibility Report

## Feasibility Decision

`FEASIBLE_BUT_HEAVY`

The ROSCOE paper implementation appears to exist in Meta AI's ParlAI repository under `projects/roscoe`, but it is not a lightweight standalone package. It is feasible to attempt in an isolated environment, but the dependency and model burden is heavy enough that it should not be run before a public/intermediary analytics post unless ROSCOE is essential to that post.

## Answers

1. Does the ROSCOE paper implementation appear to exist in ParlAI?

   Yes. `projects/roscoe/README.md` is titled "ROSCOE: A Suite of Metrics for Scoring Step-by-Step Reasoning" and `projects/roscoe/score.py` implements the metric constants and `Evaluator`.

2. What exact files contain it?

   Core files:
   - `projects/roscoe/score.py`
   - `projects/roscoe/roscoe.py`
   - `projects/roscoe/utils.py`
   - `projects/roscoe/README.md`
   - `tests/nightly/cpu/test_roscoe.py`

   Supporting files are listed in `parlai_roscoe_file_inventory.csv`.

3. What are the import paths or command-line entry points?

   - CLI: `python projects/roscoe/roscoe.py --dataset-path PATH --datasets NAME --scores ...`
   - Programmatic: `from projects.roscoe.score import Chain, Evaluator`

4. Can it score arbitrary candidate/reference text pairs?

   Yes, but not directly from plain rows. A small adapter is needed to split candidate/reference/source text into `Chain` objects and choose which text becomes ROSCOE `context`, `hypos`, and `references`.

5. Does it support reference-based scoring?

   Yes. `SUPERVISED_SCORES` includes reasoning alignment, external hallucination, redundancy, common sense error, missing step, semantic coverage step, and semantic coverage chain.

6. Does it support reference-free scoring?

   Yes. `UNSUPERVISED_SCORES` includes faithfulness, repetition, informativeness, discourse representation, coherence, perplexity, and grammar metrics.

7. What metric families are implemented?

   - semantic alignment: yes
   - semantic similarity: yes
   - logical inference: yes
   - language coherence: yes
   - repetition: yes
   - other: informativeness, semantic coverage, hallucination/missing-step style scores

8. What model dependencies are required?

   - `sentence-transformers`
   - `simcse`
   - `transformers`
   - `torch`
   - NLI model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli`
   - PPL model: `gpt2-large`
   - grammar model: `cointegrated/roberta-large-cola-krishna2020`
   - embedding models including `all-mpnet-base-v2`, `all-MiniLM-L6-v2`, and `facebook/roscoe-512-roberta-base`

9. What Python version is likely required?

   ParlAI `setup.py` says Python `>=3.8`. Practical compatibility is uncertain with Python 3.12 because ROSCOE depends on older research-stack packages such as `simcse` and sentence-transformers.

10. Is it compatible with the current environment?

   Not as-is. Current `.venv` lacks `sentence_transformers` and `simcse`. `torch` and `transformers` are available, but this task explicitly forbids modifying `.venv`.

11. Can it be run without installing all of ParlAI?

   Possibly, but not cleanly. `score.py` imports `projects.roscoe.utils`; `roscoe.py` imports `parlai.core.params.ParlaiParser`. A direct `Evaluator` adapter may avoid the CLI and most ParlAI runtime, but still needs the source package layout and dependencies.

12. Can it be isolated into `.venv_roscoe` safely?

   Yes, as a next experiment, provided the install is treated as disposable and stopped on conflicts. No isolated environment was created in this scan.

13. What is the estimated engineering cost?

   Medium-high. A minimal direct-adapter route is likely 0.5-1 day if dependencies resolve; full ParlAI install plus model/runtime debugging could take longer.

14. Is this worth doing before the LinkedIn intermediary analytics post?

   Not recommended unless ROSCOE is central to the post. Existing BERTScore, ROUGE-L, chrF, and deterministic comparisons are already reproducible. ROSCOE is heavier and likely to distract from the current analytics story.

15. What is the safest next action?

   Create `.venv_roscoe` only in a dedicated follow-up task, try a minimal `Evaluator` smoke test with embedding-only metrics, and avoid full NLI/PPL/grammar metrics until the embedding path works.

## Metrics Detected

Metric constants detected in `score.py`:

reasoning_alignment, coherence_step_vs_step, common_sense_error, discourse_representation, external_hallucination, faithfulness, faithfulness_ww, grammar_step, grammar_step_max, informativeness_chain, informativeness_step, missing_step, perplexity_chain, perplexity_step, perplexity_step_max, redundancy, repetition_step, repetition_word, semantic_coverage_chain, semantic_coverage_step, sentence_transformer, sim_sce

## Source Fetch Status

- Network error: `none`
- ParlAI repo cloned: false
- Temporary clone path: none

## Validation

- Dependencies installed: false
- `.venv` modified: false
- `.venv_roscoe` created: false
- `learning.db` modified: false
- Raw outputs modified: false
- Model calls made: false
- External LLM API calls: false
- ROSCOE scores computed: false
- Phase 2 semantics implemented: false
