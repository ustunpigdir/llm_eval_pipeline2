# ROSCOE Metric Report

## Purpose

Evaluate whether ROSCOE-style reasoning metrics can be added as a metric-behavior layer.

## Setup Status

- ROSCOE importable: False
- sentence_transformers importable: False
- Run mode: setup_only
- Blocker: roscoe package is not importable in the project virtual environment

## Inputs

- Canonical reasoning-only text artifact
- Existing BERTScore/ROUGE-L/chrF metric artifacts were detected for future alignment.

## ROSCOE Implementation Used

None. ROSCOE is not importable in the current project virtual environment.

## Row Coverage

- Rows available for future scoring: 252
- PASS/FAIL available: 117/135

## Available ROSCOE Metrics

No ROSCOE metrics available.

## Overall ROSCOE Summary

Not computed.

## Interpretation

Setup stopped before scoring. No conclusions can be drawn about ROSCOE separation on the 252-row dataset.

## Limitations

- ROSCOE package is unavailable.
- sentence_transformers is unavailable.
- No model download or package installation was attempted.

## Recommended Next Step

Decide whether to add ROSCOE and sentence-transformer dependencies through an approved dependency workflow, then rerun this script.
