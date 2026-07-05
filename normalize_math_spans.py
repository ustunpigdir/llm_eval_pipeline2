#!/usr/bin/env python3
"""
normalize_math_spans.py  --  Layer 1C: deterministic math-span normalization.

Populates a normalized, canonical text form for every row in extracted_math_spans.

Design constraints (project rules):
  * Additive only. Writes ONLY to a NEW table `math_span_normalization`.
    extracted_math_spans is never modified (raw_text is preserved).
  * Idempotent. Deterministic output; re-running reproduces identical rows.
  * No LLM calls. No symbolic parsing (no sympy). pylatexenc (already in the
    project venv) does the LaTeX->text canonicalization; a thin regex layer
    strips delimiters and format-only markup first.
  * Noise is marked explicitly, never silently "normalized".

Status classes (one per span):
  REAL     normalized_text produced from real LaTeX
  TRIVIAL  single-symbol span (e.g. 'k', 'r'); not normalized
  PROSE    prose fragment mis-captured as inline math; not normalized
  ELIDED   placeholder such as '\\[ ... \\]' (content was never captured)
  EMPTY    blank / whitespace only

Usage:
  python3 normalize_math_spans.py                  # normalize ./learning.db (new rows only)
  python3 normalize_math_spans.py --db path.db     # target a specific DB
  python3 normalize_math_spans.py --force          # recompute every span
  python3 normalize_math_spans.py --report         # print summary + samples after run
  python3 normalize_math_spans.py --csv out.csv    # dump the table for human review
  python3 normalize_math_spans.py --dry-run        # compute + report, write nothing
"""
from __future__ import annotations
import argparse
import re
import sqlite3
import sys
from datetime import datetime, timezone

try:
    from pylatexenc.latex2text import LatexNodes2Text
except ImportError:
    sys.exit("pylatexenc not found. Run inside the project venv (it is installed there).")

TABLE = "math_span_normalization"
METHOD_VERSION = "layer1c_pylatexenc_v2"

# --------------------------------------------------------------------------- #
# Classification                                                              #
# --------------------------------------------------------------------------- #
# Math markers used to separate real (short) math from prose. Includes
# sub/superscripts, braces, inequalities and abs-value bars so symbolic spans
# like f_{min}, x < L, |P| are recognised as math. Parentheses are EXCLUDED on
# purpose: prose fragments such as "(deceleration)" contain them. This char
# class was validated on the full dataset (v2): 272 PROSE->REAL, 0 prose leaks.
_MATHOP = re.compile(r"[0-9=\\+\-*/^_{}<>|]")
_ELIDED = re.compile(r"\.\.\.")
_HAS_WRAPPER = re.compile(r"\\\[|\\begin|\$\$")


def classify(raw: str) -> str:
    """Deterministic status class for a raw span. Order matters."""
    s = raw.strip()
    if s == "":
        return "EMPTY"
    if _ELIDED.search(s) and _HAS_WRAPPER.search(s):
        return "ELIDED"
    if len(s) <= 2 and not any(c.isdigit() for c in s):
        return "TRIVIAL"
    if not _MATHOP.search(s):
        return "PROSE"
    return "REAL"


# --------------------------------------------------------------------------- #
# Normalization (REAL spans only)                                             #
# --------------------------------------------------------------------------- #
_DELIMS = [
    re.compile(r"^\$\$(?P<in>.*)\$\$$", re.S),
    re.compile(r"^\$(?P<in>.*)\$$", re.S),
    re.compile(r"^\\\[(?P<in>.*)\\\]$", re.S),
    re.compile(r"^\\\((?P<in>.*)\\\)$", re.S),
]
# Format-only commands that carry no mathematical meaning.
_SPACING = re.compile(r"\\[,;:!>]|\\quad|\\qquad|\\!|\\ ")
_FORMAT_CMD = re.compile(r"\\(left|right|displaystyle|nonumber|notag|limits)\b")
_WS = re.compile(r"\s+")

_L2T = LatexNodes2Text(math_mode="text", strict_latex_spaces=False, keep_comments=False)


def strip_delimiters(s: str) -> str:
    s = s.strip()
    for pat in _DELIMS:
        m = pat.match(s)
        if m:
            return m.group("in").strip()
    return s


def normalize_real(raw: str) -> tuple[str, str]:
    """
    Return (normalized_text, method).

    method = 'pylatexenc' on success, 'regex_fallback' if pylatexenc raises.
    """
    inner = strip_delimiters(raw)
    # drop alignment / format-only markup before conversion
    pre = _FORMAT_CMD.sub(" ", inner)
    pre = _SPACING.sub(" ", pre)
    pre = pre.replace("&", " ").replace(r"\\", " ")  # aligned/matrix separators
    try:
        text = _L2T.latex_to_text(pre)
        method = "pylatexenc"
    except Exception:
        # deterministic fallback: strip a few common commands, keep the rest
        text = re.sub(r"\\(frac|sqrt|text|mathrm|mathbf|boxed|operatorname)\b", " ", pre)
        text = text.replace("{", " ").replace("}", " ")
        method = "regex_fallback"
    text = _WS.sub(" ", text).strip()
    return text, method


# --------------------------------------------------------------------------- #
# DB layer                                                                    #
# --------------------------------------------------------------------------- #
DDL = f"""
CREATE TABLE IF NOT EXISTS {TABLE} (
    span_id         INTEGER PRIMARY KEY,   -- = extracted_math_spans.id
    run_id          INTEGER NOT NULL,
    span_type       TEXT,
    status          TEXT NOT NULL,         -- REAL / TRIVIAL / PROSE / ELIDED / EMPTY
    method          TEXT,                  -- pylatexenc / regex_fallback / none
    normalized_text TEXT,                  -- NULL for non-REAL statuses
    method_version  TEXT,
    created_at      TEXT
);
"""
DDL_IDX = [
    f"CREATE INDEX IF NOT EXISTS idx_msn_status ON {TABLE}(status)",
    f"CREATE INDEX IF NOT EXISTS idx_msn_run ON {TABLE}(run_id)",
]


def ensure_schema(con: sqlite3.Connection) -> None:
    con.execute(DDL)
    for stmt in DDL_IDX:
        con.execute(stmt)


def process(con: sqlite3.Connection, force: bool, dry_run: bool) -> dict:
    ensure_schema(con)
    cur = con.cursor()
    if force:
        todo = cur.execute(
            "SELECT id, run_id, span_type, raw_text FROM extracted_math_spans"
        ).fetchall()
    else:
        todo = cur.execute(
            f"""SELECT s.id, s.run_id, s.span_type, s.raw_text
                FROM extracted_math_spans s
                LEFT JOIN {TABLE} n ON n.span_id = s.id
                WHERE n.span_id IS NULL"""
        ).fetchall()

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    counts = {k: 0 for k in ("REAL", "TRIVIAL", "PROSE", "ELIDED", "EMPTY")}
    rows = []
    for span_id, run_id, span_type, raw in todo:
        status = classify(raw)
        counts[status] += 1
        if status == "REAL":
            norm, method = normalize_real(raw)
        else:
            norm, method = None, "none"
        rows.append((span_id, run_id, span_type, status, method, norm, METHOD_VERSION, now))

    if not dry_run and rows:
        cur.executemany(
            f"""INSERT OR REPLACE INTO {TABLE}
                (span_id, run_id, span_type, status, method, normalized_text,
                 method_version, created_at)
                VALUES (?,?,?,?,?,?,?,?)""",
            rows,
        )
        con.commit()
    return {"processed": len(rows), "counts": counts, "wrote": (not dry_run and bool(rows))}


# --------------------------------------------------------------------------- #
# Reporting                                                                   #
# --------------------------------------------------------------------------- #
def report(con: sqlite3.Connection) -> None:
    cur = con.cursor()
    total = cur.execute(f"SELECT COUNT(*) FROM {TABLE}").fetchone()[0]
    print(f"\n{TABLE}: {total} rows")
    print("  status breakdown:")
    for st, n in cur.execute(
        f"SELECT status, COUNT(*) FROM {TABLE} GROUP BY status ORDER BY 2 DESC"
    ):
        print(f"    {st:<9} {n:>6}  ({100*n/total:.1f}%)" if total else f"    {st}")
    print("  method breakdown (REAL only):")
    for m, n in cur.execute(
        f"SELECT method, COUNT(*) FROM {TABLE} WHERE status='REAL' GROUP BY method"
    ):
        print(f"    {m:<15} {n}")
    print("\n  sample REAL normalizations:")
    for raw, norm in cur.execute(
        f"""SELECT s.raw_text, n.normalized_text
            FROM {TABLE} n JOIN extracted_math_spans s ON s.id = n.span_id
            WHERE n.status='REAL' AND LENGTH(s.raw_text) BETWEEN 30 AND 110
            ORDER BY RANDOM() LIMIT 8"""
    ):
        print(f"    RAW : {raw[:90]}")
        print(f"    NORM: {norm[:90]}")


def export_csv(con: sqlite3.Connection, path: str) -> None:
    import csv
    cur = con.cursor()
    rows = cur.execute(
        f"""SELECT n.span_id, n.run_id, n.span_type, n.status, n.method,
                   s.raw_text, n.normalized_text
            FROM {TABLE} n JOIN extracted_math_spans s ON s.id = n.span_id
            ORDER BY n.run_id, n.span_id"""
    ).fetchall()
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["span_id", "run_id", "span_type", "status", "method",
                    "raw_text", "normalized_text"])
        w.writerows(rows)
    print(f"wrote {len(rows)} rows -> {path}")


# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(description="Deterministic normalization of extracted_math_spans.")
    ap.add_argument("--db", default="learning.db")
    ap.add_argument("--force", action="store_true", help="recompute every span")
    ap.add_argument("--dry-run", action="store_true", help="compute + report, write nothing")
    ap.add_argument("--report", action="store_true", help="print summary + samples")
    ap.add_argument("--csv", metavar="PATH", help="export the table to CSV for review")
    args = ap.parse_args()

    con = sqlite3.connect(args.db)
    try:
        res = process(con, force=args.force, dry_run=args.dry_run)
        print(f"processed {res['processed']} span(s); wrote={res['wrote']}")
        print("  " + "  ".join(f"{k}={v}" for k, v in res["counts"].items()))
        if args.report or args.dry_run:
            report(con)
        if args.csv:
            export_csv(con, args.csv)
    finally:
        con.close()


if __name__ == "__main__":
    main()
