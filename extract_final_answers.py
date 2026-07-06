#!/usr/bin/env python3
"""
extract_final_answers.py  --  Layer 2: final-answer VALUE extraction.

Extracts the field->value pairs from each run's final-answer block and stores
them in the database. Reuses the EXISTING, human-trusted detector/parser in
classify_remaining_layer1b_flags.py (find_final_answer_blocks, FIELD_PATTERN,
extract_field_value) rather than re-implementing block finding.

Additive + idempotent. Writes ONLY two NEW tables:
  final_answer_runs    one row per run: was a block found, its status, evidence
  final_answer_values  one row per field: run_id, field_name, raw_value, value_num, status
Never modifies questions / extracted_* / math_span_normalization.

Value reduction (deterministic, conservative):
  NUMERIC      plain number, scientific a x 10^b, or the number after the model's
               own '= / \\approx' (e.g. '\\frac{2.725}{1101} \\approx 0.002475' -> 0.002475)
  UNSUPPORTED  symbolic value (\\sqrt, bare \\frac, \\pi, ...). Raw kept, value_num NULL.
  BLANK        empty value.
No symbolic evaluation. No gold comparison. Raw value is always preserved.

Usage:
  python3 extract_final_answers.py                 # rebuild tables from ./learning.db
  python3 extract_final_answers.py --db path.db
  python3 extract_final_answers.py --report
  python3 extract_final_answers.py --csv out.csv
  python3 extract_final_answers.py --dry-run
"""
from __future__ import annotations
import argparse
import re
import sqlite3
import sys
from datetime import datetime, timezone

try:
    from classify_remaining_layer1b_flags import (
        find_final_answer_blocks,
        normalized_field_values,
        extract_field_value,
        FIELD_PATTERN,
    )
except Exception as e:  # pragma: no cover
    sys.exit(f"could not import classifier helpers: {e}")

RUNS_TABLE = "final_answer_runs"
VALUES_TABLE = "final_answer_values"
METHOD_VERSION = "layer2_final_values_v2"

# --------------------------------------------------------------------------- #
# Block selection (mirrors classify_run_v2's logic exactly)                    #
# --------------------------------------------------------------------------- #
def select_final_block(answer: str):
    """Return (final_block_or_None, block_status)."""
    blocks = find_final_answer_blocks(answer)
    valid = [b for b in blocks if b["field_count"] >= 2]
    if not valid:
        return None, "NO_VALID_BLOCK"
    filled = [b for b in valid if b["has_values_after_equals"]]
    if not filled:
        partial = any(b["filled_field_count"] > 0 for b in valid)
        return None, "PARTIAL_BLANK" if partial else "ALL_BLANK"
    distinct = {normalized_field_values(b) for b in filled}
    final = max(filled, key=lambda b: b["end_char"])
    return final, ("CONFLICT" if len(distinct) > 1 else "OK")


# --------------------------------------------------------------------------- #
# Value reduction                                                             #
# --------------------------------------------------------------------------- #
_TEXT = re.compile(r"\\(?:text|mathrm|mathbf|mathit|operatorname)\s*\{[^}]*\}")
# \boxed{NUMBER} -> NUMBER (only when inner has no nested braces, i.e. a bare value;
# \boxed{\frac{1}{2}} intentionally does NOT match and stays UNSUPPORTED).
_BOXED = re.compile(r"\\boxed\s*\{([^{}]+)\}")
# Unit decorations to strip so the underlying number is exposed (NOT evaluation):
# degree symbol, percent, micro-prefix, unicode degree.
_DECOR = re.compile(r"\^\s*\{?\s*\\circ\s*\}?|°|\\degree|\\%|\\mu(?![a-zA-Z])")
_SPACE = re.compile(r"\\[,;:!>\s]|\\quad|\\qquad|\\!|\\left|\\right")
_SPLIT_OP = re.compile(r"\\approxeq|\\approx|\\simeq|\\sim|\\cong|=")
_SCI = re.compile(
    r"([+-]?\d*\.?\d+)\s*(?:\\times|\\cdot|\*|×|x)\s*10\s*\^?\s*\{?\s*([+-]?\d+)\}?\s*$"
)
_PLAIN = re.compile(r"^[+-]?\d*\.?\d+(?:[eE][+-]?\d+)?$")


def _parse_number(tok: str):
    t = tok.strip().strip("$").strip().rstrip(",.;").strip()
    m = _SCI.fullmatch(t)
    if m:
        try:
            return float(m.group(1)) * (10.0 ** int(m.group(2)))
        except ValueError:
            return None
    if _PLAIN.fullmatch(t):
        try:
            return float(t)
        except ValueError:
            return None
    return None


def reduce_value(raw: str):
    """Return (value_num_or_None, status)."""
    if raw is None or raw.strip() == "":
        return None, "BLANK"
    s = _BOXED.sub(r"\1", raw)
    s = _TEXT.sub(" ", s)
    s = _DECOR.sub(" ", s)
    s = _SPACE.sub(" ", s)
    s = s.replace("$", "").strip().rstrip(",.;/ ")   # drop trailing unit slash (e.g. 271.7°/day).strip()
    # prefer the number after the model's own last '=' / '\approx'
    parts = _SPLIT_OP.split(s)
    if len(parts) > 1:
        v = _parse_number(parts[-1])
        if v is not None:
            return v, "NUMERIC"
    v = _parse_number(s)
    if v is not None:
        return v, "NUMERIC"
    return None, "UNSUPPORTED"


def field_pairs(block_raw: str):
    """Yield (field_index, field_name, raw_value) from a final block."""
    for i, (name, value) in enumerate(FIELD_PATTERN.findall(block_raw)):
        field_name = name.replace("\\_", "_").replace("\\,", "").strip()
        raw_value = extract_field_value(value)
        yield i, field_name, raw_value


# --------------------------------------------------------------------------- #
# DB                                                                          #
# --------------------------------------------------------------------------- #
DDL = f"""
CREATE TABLE IF NOT EXISTS {RUNS_TABLE} (
    run_id          INTEGER PRIMARY KEY,
    model_name      TEXT,
    block_found     INTEGER NOT NULL,     -- 0/1
    block_status    TEXT NOT NULL,        -- OK/CONFLICT/PARTIAL_BLANK/ALL_BLANK/NO_VALID_BLOCK
    n_fields        INTEGER NOT NULL,
    n_numeric       INTEGER NOT NULL,
    n_unsupported   INTEGER NOT NULL,
    final_block_raw TEXT,
    method_version  TEXT,
    created_at      TEXT
);
CREATE TABLE IF NOT EXISTS {VALUES_TABLE} (
    id            INTEGER PRIMARY KEY,
    run_id        INTEGER NOT NULL,
    field_index   INTEGER NOT NULL,
    field_name    TEXT,
    raw_value     TEXT,
    value_num     REAL,
    value_status  TEXT NOT NULL,          -- NUMERIC/UNSUPPORTED/BLANK
    created_at    TEXT
);
CREATE INDEX IF NOT EXISTS idx_fav_run ON {VALUES_TABLE}(run_id);
CREATE INDEX IF NOT EXISTS idx_far_status ON {RUNS_TABLE}(block_status);
"""


def process(con: sqlite3.Connection, dry_run: bool) -> dict:
    con.executescript(DDL)
    cur = con.cursor()
    runs = cur.execute(
        "SELECT id, model_name, answer FROM questions ORDER BY id"
    ).fetchall()
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    run_rows, val_rows = [], []
    summary = {"runs": 0, "with_block": 0, "values": 0,
               "NUMERIC": 0, "UNSUPPORTED": 0, "BLANK": 0}
    status_counts: dict = {}
    for run_id, model, answer in runs:
        summary["runs"] += 1
        final, status = select_final_block(answer or "")
        status_counts[status] = status_counts.get(status, 0) + 1
        n_fields = n_num = n_uns = 0
        if final is not None:
            summary["with_block"] += 1
            for idx, fname, raw_value in field_pairs(final["raw_text"]):
                num, vstatus = reduce_value(raw_value)
                n_fields += 1
                summary["values"] += 1
                summary[vstatus] += 1
                if vstatus == "NUMERIC":
                    n_num += 1
                elif vstatus == "UNSUPPORTED":
                    n_uns += 1
                val_rows.append((run_id, idx, fname, raw_value, num, vstatus, now))
        run_rows.append((run_id, model, 1 if final else 0, status,
                         n_fields, n_num, n_uns,
                         final["raw_text"] if final else None, METHOD_VERSION, now))

    if not dry_run:
        cur.execute("BEGIN")
        cur.execute(f"DELETE FROM {VALUES_TABLE}")
        cur.execute(f"DELETE FROM {RUNS_TABLE}")
        cur.executemany(
            f"""INSERT INTO {RUNS_TABLE}
                (run_id, model_name, block_found, block_status, n_fields,
                 n_numeric, n_unsupported, final_block_raw, method_version, created_at)
                VALUES (?,?,?,?,?,?,?,?,?,?)""", run_rows)
        cur.executemany(
            f"""INSERT INTO {VALUES_TABLE}
                (run_id, field_index, field_name, raw_value, value_num, value_status, created_at)
                VALUES (?,?,?,?,?,?,?)""", val_rows)
        con.commit()
    summary["status_counts"] = status_counts
    return summary


def report(con: sqlite3.Connection) -> None:
    cur = con.cursor()
    tot = cur.execute(f"SELECT COUNT(*) FROM {RUNS_TABLE}").fetchone()[0]
    wb = cur.execute(f"SELECT COUNT(*) FROM {RUNS_TABLE} WHERE block_found=1").fetchone()[0]
    print(f"\nruns: {tot}  with final block: {wb} ({100*wb/tot:.1f}%)  without: {tot-wb}")
    print("  block_status:")
    for st, n in cur.execute(f"SELECT block_status, COUNT(*) FROM {RUNS_TABLE} GROUP BY block_status ORDER BY 2 DESC"):
        print(f"    {st:<16} {n}")
    print("  value_status:")
    for st, n in cur.execute(f"SELECT value_status, COUNT(*) FROM {VALUES_TABLE} GROUP BY value_status ORDER BY 2 DESC"):
        print(f"    {st:<12} {n}")
    print("\n  sample extracted values:")
    for rid, f, rv, vn, vs in cur.execute(
        f"""SELECT run_id, field_name, raw_value, value_num, value_status
            FROM {VALUES_TABLE} ORDER BY RANDOM() LIMIT 10"""):
        shown = vn if vs == "NUMERIC" else f"[{vs}]"
        print(f"    run {rid:>3} {f:<26} {str(rv)[:34]:<34} -> {shown}")


def export_csv(con: sqlite3.Connection, path: str) -> None:
    import csv
    cur = con.cursor()
    rows = cur.execute(
        f"""SELECT v.run_id, r.model_name, r.block_status, v.field_index,
                   v.field_name, v.raw_value, v.value_num, v.value_status
            FROM {VALUES_TABLE} v JOIN {RUNS_TABLE} r ON r.run_id = v.run_id
            ORDER BY v.run_id, v.field_index""").fetchall()
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["run_id", "model_name", "block_status", "field_index",
                    "field_name", "raw_value", "value_num", "value_status"])
        w.writerows(rows)
    print(f"wrote {len(rows)} value rows -> {path}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Extract final-answer field values into the DB.")
    ap.add_argument("--db", default="learning.db")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--csv", metavar="PATH")
    args = ap.parse_args()

    con = sqlite3.connect(args.db)
    try:
        s = process(con, dry_run=args.dry_run)
        print(f"runs={s['runs']} with_block={s['with_block']} values={s['values']} "
              f"(NUMERIC={s['NUMERIC']} UNSUPPORTED={s['UNSUPPORTED']} BLANK={s['BLANK']})")
        print("  block_status:", s["status_counts"])
        if args.report or args.dry_run:
            report(con)
        if args.csv:
            export_csv(con, args.csv)
    finally:
        con.close()


if __name__ == "__main__":
    main()
