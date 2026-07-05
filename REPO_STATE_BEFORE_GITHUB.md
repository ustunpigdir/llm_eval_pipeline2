# Repo State Before GitHub

Date: 2026-07-05

## 1. Git repository status

This folder was not already a Git repository. It was initialized locally with `git init`.

## 2. Current branch

`main`

## 3. Remote URL

No Git remote is configured yet.

## 4. File count summary

Approximate project file count excluding `.git`, `.venv`, `__pycache__`, and `backups`:

`777`

Top-level summary:

- `raw_answers_md/`: 707 files
- `scripts/`: 3 files
- root project scripts, reports, CSV artifacts, JSON artifacts, text dumps, and `learning.db`: remaining files

## 5. Main database size

`learning.db`: 16 MB

This is small enough for normal GitHub hosting and is currently kept trackable because it is a reproducible benchmark artifact.

## 6. Sensitive file scan

Likely secret files found by filename search:

- `inspect_mdit_math_tokens.py`

This appears to be a false-positive filename match on `token`, not a secret file.

Lightweight text scan found references to words such as `token` and model/provider names in source files and Markdown reports. No `.env`, `*.key`, or `*.pem` files were found, and no actual secret values were printed or identified.

## 7. `.gitignore`

`.gitignore` was created.

It ignores Python caches, virtual environments, editor folders, environment files, key/pem files, logs/temp folders, backups, archives, and optional cache folders. It does not ignore `learning.db`.

## 8. `README.md`

`README.md` was created.

It documents the live SQL-backed scientific-reasoning benchmark pipeline, current DB tables, main scripts, and next architecture gap.

## 9. Official benchmark archive location

The official benchmark archive is outside the repo:

`/Users/upigdir/Desktop/Pipeline_SQL_proj_official_benchmark_layer.zip`

The live folder already contains the official benchmark scripts and DB layer from the prior additive merge.

## 10. Recommended GitHub repo name

`scientific-reasoning-benchmark-pipeline`
