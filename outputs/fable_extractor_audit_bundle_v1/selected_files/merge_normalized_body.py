#!/usr/bin/env python3
"""
merge_normalized_body.py  --  Layer 3a: merge normalized math back into the body.

Produces, per run, a readable "normalized body": the raw answer text with every
math region replaced by its normalized form, prose untouched. Feeds the later
sentence-split + logic-gate stages.

Math regions:
  * display / environment  -> located by exact start_char/end_char offsets in
    extracted_math_spans (reliable), outer-span-wins on overlap. Wrapped in  U+27E6..U+27E7  (dbl sq brackets).
  * inline ($...$, \\(...\\)) -> located by regex re-scan (inline spans carry no
    offsets). Wrapped in  U+27E8..U+27E9  (angle brackets).

All regions are normalized on the fly with normalize_real() from
normalize_math_spans.py (the SAME deterministic function used to build
math_span_normalization), so output is identical to the stored spans and the
merge does not depend on that table being populated.

Additive + idempotent. Writes ONLY the new table answer_body_normalized.
No LLM calls. No new dependencies (pylatexenc already in the venv).

Usage:
  python3 merge_normalized_body.py                 # build from ./learning.db
  python3 merge_normalized_body.py --db path.db
  python3 merge_normalized_body.py --report
  python3 merge_normalized_body.py --show RUN_ID   # print one merged body
  python3 merge_normalized_body.py --dry-run
"""
from __future__ import annotations
import argparse
import re
import sqlite3
import sys
from datetime import datetime, timezone

try:
    from normalize_math_spans import normalize_real
except ImportError:
    sys.exit("normalize_math_spans.py not found / pylatexenc missing (run inside the venv).")

TABLE = "answer_body_normalized"
METHOD_VERSION = "layer3a_merge_v1"

DISP_OPEN, DISP_CLOSE = "⟦", "⟧"   # display / environment math
INL_OPEN, INL_CLOSE = "⟨", "⟩"     # inline math
INLINE = re.compile(r"\$([^$]+)\$|\\\((.+?)\\\)", re.DOTALL)
_RESIDUAL = re.compile(r"\\begin\{aligned\}|\\\[|\$\$")
_WS = re.compile(r"[ \t]+")


def _norm(raw: str) -> str:
    out, _ = normalize_real(raw)
    return out if out.strip() else raw.strip()


def merge_one(answer: str, spans) -> tuple[str, int, int]:
    """spans: list of (start_char, end_char, raw_text) for display/environment."""
    # keep only offset-verified spans, resolve overlaps outer-first
    cand = sorted(
        ((so, eo, raw) for so, eo, raw in spans
         if so is not None and eo is not None and answer[so:eo] == raw),
        key=lambda x: (x[0], -(x[1] - x[0])),
    )
    chosen, last = [], -1
    for so, eo, raw in cand:
        if so >= last:
            chosen.append((so, eo, raw))
            last = eo
    body = answer
    for so, eo, raw in sorted(chosen, key=lambda x: -x[0]):
        body = f"{body[:so]} {DISP_OPEN}{_norm(raw)}{DISP_CLOSE} {body[eo:]}"
    n_disp = len(chosen)

    n_inl = 0
    def _sub(m):
        nonlocal n_inl
        n_inl += 1
        return f" {INL_OPEN}{_norm(m.group(0))}{INL_CLOSE} "
    body = INLINE.sub(_sub, body)
    body = _WS.sub(" ", body)
    return body, n_disp, n_inl


DDL = f"""
CREATE TABLE IF NOT EXISTS {TABLE} (
    run_id            INTEGER PRIMARY KEY,
    body_normalized   TEXT,
    n_display_merged  INTEGER,
    n_inline_merged   INTEGER,
    n_residual_markup INTEGER,     -- leftover raw \\[ / \\begin{{aligned}} / $$ (quality flag)
    orig_len          INTEGER,
    merged_len        INTEGER,
    method_version    TEXT,
    created_at        TEXT
);
"""


def process(con: sqlite3.Connection, dry_run: bool) -> dict:
    con.executescript(DDL)
    cur = con.cursor()
    runs = cur.execute("SELECT id, answer FROM questions ORDER BY id").fetchall()
    # preload display/environment spans grouped by run
    spans_by_run: dict = {}
    for rid, so, eo, raw in cur.execute(
        """SELECT run_id, start_char, end_char, raw_text FROM extracted_math_spans
           WHERE span_type IN ('display_math','environment')
             AND start_char IS NOT NULL AND end_char IS NOT NULL"""):
        spans_by_run.setdefault(rid, []).append((so, eo, raw))

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rows = []
    tot_d = tot_i = tot_r = 0
    for rid, answer in runs:
        answer = answer or ""
        body, nd, ni = merge_one(answer, spans_by_run.get(rid, []))
        nr = len(_RESIDUAL.findall(body))
        tot_d += nd; tot_i += ni; tot_r += nr
        rows.append((rid, body, nd, ni, nr, len(answer), len(body), METHOD_VERSION, now))

    if not dry_run:
        cur.executemany(
            f"""INSERT OR REPLACE INTO {TABLE}
                (run_id, body_normalized, n_display_merged, n_inline_merged,
                 n_residual_markup, orig_len, merged_len, method_version, created_at)
                VALUES (?,?,?,?,?,?,?,?,?)""", rows)
        con.commit()
    return {"runs": len(rows), "display": tot_d, "inline": tot_i, "residual": tot_r}


def report(con: sqlite3.Connection) -> None:
    cur = con.cursor()
    tot = cur.execute(f"SELECT COUNT(*) FROM {TABLE}").fetchone()[0]
    d, i, r = cur.execute(
        f"SELECT SUM(n_display_merged), SUM(n_inline_merged), SUM(n_residual_markup) FROM {TABLE}"
    ).fetchone()
    print(f"\n{TABLE}: {tot} runs  display/env merged={d}  inline merged={i}  residual markup={r}")
    aff = cur.execute(f"SELECT COUNT(*) FROM {TABLE} WHERE n_residual_markup>0").fetchone()[0]
    print(f"  runs with residual raw markup: {aff}")
    for rid, nr in cur.execute(
        f"SELECT run_id, n_residual_markup FROM {TABLE} WHERE n_residual_markup>0 ORDER BY n_residual_markup DESC LIMIT 8"):
        print(f"    run {rid}: {nr}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Merge normalized math back into the answer body.")
    ap.add_argument("--db", default="learning.db")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--show", type=int, metavar="RUN_ID")
    args = ap.parse_args()

    con = sqlite3.connect(args.db)
    try:
        if args.show is not None:
            con.executescript(DDL)
            row = con.execute(
                f"SELECT body_normalized FROM {TABLE} WHERE run_id=?", (args.show,)).fetchone()
            print(row[0] if row else f"(run {args.show} not built yet)")
            return
        s = process(con, dry_run=args.dry_run)
        print(f"runs={s['runs']} display/env merged={s['display']} "
              f"inline merged={s['inline']} residual markup={s['residual']}")
        if args.report or args.dry_run:
            report(con)
    finally:
        con.close()


if __name__ == "__main__":
    main()
