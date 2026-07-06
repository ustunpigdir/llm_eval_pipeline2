# ROSCOE Setup Status

## Environment

- Python: 3.12.13 (main, Mar  3 2026, 12:39:30) [Clang 21.0.0 (clang-2100.0.123.102)]
- Platform: macOS-26.3.1-arm64-arm-64bit
- Torch available: True
- Torch version: 2.12.1
- Device detected: cpu
- CUDA available: False
- MPS available: False

## Module Availability

| module | importable | version | origin |
| --- | ---: | --- | --- |
| roscoe | False |  |  |
| sentence_transformers | False |  |  |
| transformers | True | 5.13.0 | /Users/upigdir/Desktop/Pipeline SQL proj/.venv/lib/python3.12/site-packages/transformers/__init__.py |
| torch | True | 2.12.1 | /Users/upigdir/Desktop/Pipeline SQL proj/.venv/lib/python3.12/site-packages/torch/__init__.py |
| datasets | False |  |  |
| evaluate | False |  |  |

## Model/Cache Availability

- Hugging Face cache exists: True
- Hugging Face cache path: /Users/upigdir/.cache/huggingface
- sentence-transformers cache exists: False

## Input Coverage

- Rows: 252
- PASS: 117
- FAIL: 135
- REVIEW rows: 0
- Scenarios: 32
- Models: 8

## Decision

- ROSCOE available: False
- Estimated scoring mode: setup_only
- Setup blocker: roscoe package is not importable in the project virtual environment

No ROSCOE scores were computed because the ROSCOE package is unavailable. This follows the setup rule: do not install large packages automatically and do not fabricate metric scores.
