# ParlAI ROSCOE Feasibility v1

This artifact corrects the prior ROSCOE dependency scan by looking specifically inside Meta AI's ParlAI repository.

The earlier scan rejected the unrelated PyPI `roscoe` package. That rejection still stands: the PyPI package is an LLM-agent orchestration SDK, not the ROSCOE paper metric suite.

This scan found a real ROSCOE implementation under `projects/roscoe` in `facebookresearch/ParlAI`, but it did not install dependencies, create `.venv_roscoe`, download models, or compute ROSCOE scores.

This is a dependency feasibility artifact only.
