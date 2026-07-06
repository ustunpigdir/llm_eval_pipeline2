# Selected Source Digest

This file consolidates the most relevant code/report excerpts from the full bundle. Long files are truncated deliberately for chat upload.



## extract_final_answers.py

Reason: Core final-answer block selection, field-pair parsing, operator matching, value reduction.
Included in full bundle as: full_file

```text
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
_SPLIT_OP = re.compile(r"\\approx|\\approxeq|\\simeq|\\sim|\\cong|=")
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

```



## normalizer.py

Reason: Answer normalizer entry point; includes None guard and math/text cleanup.
Included in full bundle as: full_file

```text
import re

def normalize_answer(answer):
    if not answer:
        return ""
    answer = answer.strip()
    answer = re.sub(r"\s+", " ", answer)
    return answer

```



## symbolic_eval.py

Reason: Deterministic numeric/symbolic evaluator used by structured autograding.
Included in full bundle as: full_file

```text
#!/usr/bin/env python3
"""
symbolic_eval.py  --  evaluate a final-answer VALUE (numeric or symbolic) to a float.

Used by the grader so a model's symbolic final answer (pi/2, 1/sqrt(2), sqrt(7/3),
\\frac{5}{6}, 180\\sqrt{2}-360, ...) can be compared numerically against the gold.

Contract (grading integrity):
  * Deterministic. A controlled LaTeX -> expression conversion handles only known
    constructs (\\frac, \\sqrt, \\pi, ^, \\times, fractions); sympy does arithmetic
    with implicit multiplication.
  * Only pi and sqrt are known names. ANYTHING else (a variable, a unit, an
    unresolved e/trig/log) becomes a free symbol -> we return (None, reason).
    It NEVER guesses a number.

eval_value(raw) -> (float | None, note)
"""
from __future__ import annotations
import re
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, implicit_multiplication_application)

try:
    from extract_final_answers import reduce_value as _reduce_numeric   # plain-number fast path
except Exception:
    _reduce_numeric = None

_TRANS = standard_transformations + (implicit_multiplication_application,)
_ALLOWED = {"pi": sp.pi, "sqrt": sp.sqrt, "ln": sp.log}  # ln = natural log (unambiguous); \log left out (base ambiguity)

# Ambiguous forms we must NEVER silently compute (found via stress testing):
#   "2-3"  -> would be 2-3=-1 (it's a RANGE);  "1 000.5" -> would be 1*000.5=0.5 (thousands sep).
_RANGE = re.compile(r"^\s*[+-]?\d+(?:\.\d+)?\s*-\s*\d+(?:\.\d+)?\s*$")
def _is_ambiguous(s: str):
    if _RANGE.match(s):
        return "range"
    # only digits/dots/spaces (no operator, sqrt, pi, letters) but a space BETWEEN two digit runs
    if not re.search(r"[A-Za-z\\/*^]", s) and re.search(r"\d\s+\d", s):
        return "space-separated-numbers"
    return None

_STRIP = re.compile(r"\\left|\\right|\\!|\\,|\\;|\\:|\\quad|\\qquad|\$")
_TEXT  = re.compile(r"\\(?:text|mathrm|mathbf|mathit|operatorname)\s*\{[^{}]*\}")
_BOXED = re.compile(r"\\boxed\s*\{([^{}]+)\}")
_FRAC  = re.compile(r"\\[dt]?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}")
_SQRTN = re.compile(r"\\sqrt\s*\[\s*([^\[\]{}]*)\s*\]\s*\{([^{}]*)\}")
_SQRT  = re.compile(r"\\sqrt\s*\{([^{}]*)\}")
_SUPBR = re.compile(r"\^\s*\{([^{}]*)\}")
_SUP1  = re.compile(r"\^\s*([0-9A-Za-z.+\-]+)")


def _latex_to_expr(s: str) -> str:
    s = _BOXED.sub(r"(\1)", s)
    s = _TEXT.sub(" ", s)
    s = _STRIP.sub(" ", s)
    s = s.replace("\\cdot", "*").replace("\\times", "*").replace("\\pi", " pi ").replace("\\ln", " ln ")
    s = s.replace("\\approx", "=")
    if "=" in s:
        s = s.split("=")[-1]                 # keep the RHS if a relation slipped in
    for _ in range(12):                      # resolve \frac / \sqrt inside-out
        new = _FRAC.sub(r"((\1)/(\2))", s)
        new = _SQRTN.sub(r"((\2)**(1/(\1)))", new)
        new = _SQRT.sub(r"sqrt(\1)", new)
        new = re.sub(r"\\sqrt\s*([0-9A-Za-z.])", r"sqrt(\1)", new)   # brace-less \sqrt2 -> sqrt(2)
        if new == s:
            break
        s = new
    s = _SUPBR.sub(r"**(\1)", s)
    s = _SUP1.sub(r"**\1", s)
    s = s.replace("{", "(").replace("}", ")")
    return re.sub(r"\s+", " ", s).strip()


def eval_value(raw):
    """Return (float, note) or (None, reason)."""
    if raw is None or str(raw).strip() == "":
        return None, "blank"
    if _reduce_numeric is not None:                      # plain number / units / scientific / degrees
        num, st = _reduce_numeric(raw)
        if st == "NUMERIC":
            return num, "numeric"
    expr_str = _latex_to_expr(str(raw))
    if not expr_str:
        return None, "empty"
    try:
        expr = parse_expr(expr_str, local_dict=_ALLOWED, transformations=_TRANS, evaluate=True)
    except Exception as e:
        return None, f"parse-fail:{type(e).__name__}"
    free = {str(x) for x in getattr(expr, "free_symbols", set())}
    if free:
        return None, "free-symbols:" + ",".join(sorted(free))
    try:
        val = complex(expr.evalf())
    except Exception as e:
        return None, f"evalf-fail:{type(e).__name__}"
    if abs(val.imag) > 1e-9:
        return None, "non-real"
    v = val.real
    if v != v or abs(v) == float("inf"):
        return None, "non-finite"
    return float(v), "symbolic"


if __name__ == "__main__":
    import sys
    for a in sys.argv[1:]:
        print(repr(a), "->", eval_value(a))

```



## classify_remaining_layer1b_flags.py

Reason: Layer 1B final-block classifier and recoverability logic.
Included in full bundle as: full_file

```text
import csv
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "learning.db"
MANIFEST_PATH = ROOT / "raw_answers_md" / "manifest.csv"
MD_OUTPUT_PATH = ROOT / "remaining_layer1b_flag_classification_v3.md"
CSV_OUTPUT_PATH = ROOT / "remaining_layer1b_flag_classification_v3.csv"

RUNS_TABLE = "questions"

FINAL_ANSWER_TEXT_MARKERS = ["FINAL ANSWER", "Final Answer", "final answer"]
FINAL_ANSWER_WINDOW = 2000
KEEP_MIN_ANSWER_LENGTH = 1000
LAST_SNIPPET_LIMIT = 1200
LAST_DISPLAY_SPAN_COUNT = 3
MARKER_NEARBY_WINDOW = 500
POLLUTION_PROSE_LENGTH_THRESHOLD = 500

ALIGNED_BLOCK_PATTERN = re.compile(r"\\begin\{aligned\}.*?\\end\{aligned\}", re.DOTALL)
# Value may follow "&" via "=", "\approx", "\approxeq", "\sim", "\cong", etc., not only a literal "&=".
FIELD_PATTERN = re.compile(r"\\mathrm\{([^}]+)\}\s*&\s*(.*?)(?=\\\\|\\end\{aligned\}|$)", re.DOTALL)
FIELD_VALUE_OPERATOR_PREFIX = re.compile(r"^(=|\\approx|\\approxeq|\\sim|\\cong)\s*")
LOOP_PATTERN = re.compile(r"(.{15,100}?)\1{2,}", re.DOTALL)

META_DISCUSSION_PHRASES = [
    "now we need to",
    "we can output",
    "the template shows",
    "the final answer should be",
    "we need to ensure",
    "the problem says",
    "inside the final answer section",
]

DISPLAY_SPAN_POLLUTION_MARKERS = ["**", "FINAL ANSWER", "The problem says", "Now we need"]

FORMAT_WARNING_KEEP = "FORMAT_WARNING_KEEP"
FORMAT_WARNING_REVIEW = "FORMAT_WARNING_REVIEW"
UNUSABLE = "UNUSABLE"

KEEP_CLEAN = "KEEP_CLEAN"
KEEP_RECOVERABLE_WITH_WARNINGS = "KEEP_RECOVERABLE_WITH_WARNINGS"
REVIEW = "REVIEW"
UNUSABLE_V3 = "UNUSABLE"


def extract_field_value(raw_value):
    return FIELD_VALUE_OPERATOR_PREFIX.sub("", raw_value.strip(), count=1).strip()


def load_manifest_scenarios():
    scenarios = {}
    if MANIFEST_PATH.exists():
        with MANIFEST_PATH.open("r", encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                scenarios[int(row["run_id"])] = row.get("scenario_id", "")
    return scenarios


def find_final_answer_blocks(answer_text):
    """Find all \\begin{aligned}...\\end{aligned} candidate final-answer blocks anywhere in the text."""
    blocks = []
    for match in ALIGNED_BLOCK_PATTERN.finditer(answer_text):
        start_char, end_char = match.start(), match.end()
        raw_text = match.group(0)

        fields = FIELD_PATTERN.findall(raw_text)
        field_count = len(fields)
        filled_field_count = sum(1 for _, value in fields if extract_field_value(value))

        has_marker_before = any(
            marker in answer_text[:start_char] for marker in FINAL_ANSWER_TEXT_MARKERS
        )

        blocks.append(
            {
                "start_char": start_char,
                "end_char": end_char,
                "raw_text": raw_text,
                "field_count": field_count,
                "filled_field_count": filled_field_count,
                "complete_aligned_environment": True,
                "has_values_after_equals": field_count > 0 and filled_field_count == field_count,
                "has_final_answer_marker_before": has_marker_before,
            }
        )
    return blocks


def detect_repetition_regions(answer_text):
    """Detect repeated/looping phrases anywhere in the text (typically tail degeneration)."""
    matches = list(LOOP_PATTERN.finditer(answer_text))
    if not matches:
        return None
    return {
        "repetition_start_char": min(m.start() for m in matches),
        "repetition_end_char": max(m.end() for m in matches),
        "repeated_phrase": matches[0].group(1),
    }


def normalized_field_values(block):
    return tuple(extract_field_value(v) for _, v in FIELD_PATTERN.findall(block["raw_text"]))


def compute_display_span_pollution(display_spans, final_block_raw_text):
    """A run's final block is 'polluted' if the Layer 1B display_math span that stored it
    also swallowed large amounts of surrounding prose (a known regex-extraction artifact)."""
    needle = final_block_raw_text.strip()
    if not needle:
        return False
    for span_text in display_spans:
        if needle not in span_text:
            continue
        begin_idx = span_text.find("\\begin{aligned}")
        end_idx = span_text.rfind("\\end{aligned}")
        if begin_idx == -1 or end_idx == -1:
            continue
        prefix = span_text[:begin_idx]
        suffix = span_text[end_idx + len("\\end{aligned}"):]
        if len(prefix) > POLLUTION_PROSE_LENGTH_THRESHOLD or len(suffix) > POLLUTION_PROSE_LENGTH_THRESHOLD:
            return True
        if any(marker in prefix or marker in suffix for marker in DISPLAY_SPAN_POLLUTION_MARKERS):
            return True
    return False


def classify_run_v2(answer, severities):
    blocks = find_final_answer_blocks(answer)
    repetition = detect_repetition_regions(answer)

    valid_blocks = [b for b in blocks if b["field_count"] >= 2]

    if not valid_blocks:
        return UNUSABLE, "no complete final-answer block (\\begin{aligned}...\\end{aligned} with >=2 \\mathrm{} fields) found anywhere in the answer", blocks, repetition, None

    fully_filled_blocks = [b for b in valid_blocks if b["has_values_after_equals"]]
    partially_filled_blocks = [
        b for b in valid_blocks if not b["has_values_after_equals"] and b["filled_field_count"] > 0
    ]

    if not fully_filled_blocks:
        if partially_filled_blocks:
            return FORMAT_WARNING_REVIEW, "final-answer block(s) found but field values are partially blank", blocks, repetition, None
        return UNUSABLE, "final-answer block(s) found but all candidate field values are blank/template-only", blocks, repetition, None

    distinct_value_sets = {normalized_field_values(b) for b in fully_filled_blocks}
    if len(distinct_value_sets) > 1:
        return FORMAT_WARNING_REVIEW, "multiple final-answer blocks found with differing (conflicting) values", blocks, repetition, None

    final_block = max(fully_filled_blocks, key=lambda b: b["end_char"])

    if final_block["has_final_answer_marker_before"]:
        lookback_start = max(0, final_block["start_char"] - MARKER_NEARBY_WINDOW)
        marker_nearby = any(
            marker in answer[lookback_start:final_block["start_char"]] for marker in FINAL_ANSWER_TEXT_MARKERS
        )
        if not marker_nearby:
            return (
                FORMAT_WARNING_REVIEW,
                f"final-answer marker exists but not within {MARKER_NEARBY_WINDOW} chars before the aligned block",
                blocks,
                repetition,
                final_block,
            )

    if repetition is not None and repetition["repetition_start_char"] < final_block["end_char"]:
        return (
            FORMAT_WARNING_REVIEW,
            "repetition/looping region overlaps or occurs before the final-answer block",
            blocks,
            repetition,
            final_block,
        )

    if severities != {"warning"}:
        return (
            FORMAT_WARNING_REVIEW,
            "final-answer block is complete but severities include non-warning flags",
            blocks,
            repetition,
            final_block,
        )

    reason = "complete final-answer block with all fields filled"
    if repetition is not None:
        reason += "; repetition/looping detected but occurs entirely after the final-answer block"
    return FORMAT_WARNING_KEEP, reason, blocks, repetition, final_block


def classify_run_v3(answer, severities, display_spans):
    blocks = find_final_answer_blocks(answer)
    repetition = detect_repetition_regions(answer)

    total_aligned_candidate_count = len(blocks)
    valid_blocks = [b for b in blocks if b["field_count"] >= 2]

    filled_blocks = [b for b in valid_blocks if b["has_values_after_equals"]]
    blank_blocks = [b for b in valid_blocks if b["filled_field_count"] == 0]
    partial_blocks = [
        b for b in valid_blocks if 0 < b["filled_field_count"] < b["field_count"]
    ]

    filled_final_block_count = len(filled_blocks)
    blank_template_block_count = len(blank_blocks)
    distinct_value_sets = {normalized_field_values(b) for b in filled_blocks}
    distinct_filled_final_block_count = len(distinct_value_sets)
    has_multiple_distinct_filled_blocks = distinct_filled_final_block_count > 1

    base_diagnostics = {
        "total_aligned_candidate_count": total_aligned_candidate_count,
        "filled_final_block_count": filled_final_block_count,
        "blank_template_block_count": blank_template_block_count,
        "distinct_filled_final_block_count": distinct_filled_final_block_count,
        "last_filled_final_block_start_char": None,
        "last_filled_final_block_end_char": None,
        "chars_after_last_filled_final_block": None,
        "has_repetition_after_final_block": False,
        "has_repetition_before_or_overlapping_final_block": False,
        "has_blank_template_after_last_filled_block": False,
        "has_multiple_distinct_filled_blocks": has_multiple_distinct_filled_blocks,
        "has_meta_discussion_after_final_block": False,
        "display_span_pollution_near_final": False,
    }

    if not filled_blocks:
        reason = "no complete filled final-answer block found anywhere in the answer"
        if blank_template_block_count > 0:
            reason = "final-answer block(s) found but all are blank/template-only (no filled values)"
        if repetition is not None:
            reason += "; repetition/looping present, preventing resolution"
        return UNUSABLE_V3, reason, blocks, repetition, None, base_diagnostics

    final_block = max(filled_blocks, key=lambda b: b["end_char"])
    chars_after = len(answer) - final_block["end_char"]

    has_repetition_after = repetition is not None and repetition["repetition_start_char"] >= final_block["end_char"]
    has_repetition_before_or_overlap = repetition is not None and repetition["repetition_start_char"] < final_block["end_char"]
    has_blank_after = any(b["start_char"] > final_block["end_char"] for b in blank_blocks)
    has_partial_after = any(b["start_char"] > final_block["end_char"] for b in partial_blocks)

    tail_text_lower = answer[final_block["end_char"]:].lower()
    has_meta_after = any(phrase in tail_text_lower for phrase in META_DISCUSSION_PHRASES)

    pollution = compute_display_span_pollution(display_spans, final_block["raw_text"])

    diagnostics = dict(base_diagnostics)
    diagnostics.update(
        {
            "last_filled_final_block_start_char": final_block["start_char"],
            "last_filled_final_block_end_char": final_block["end_char"],
            "chars_after_last_filled_final_block": chars_after,
            "has_repetition_after_final_block": has_repetition_after,
            "has_repetition_before_or_overlapping_final_block": has_repetition_before_or_overlap,
            "has_blank_template_after_last_filled_block": has_blank_after,
            "has_meta_discussion_after_final_block": has_meta_after,
            "display_span_pollution_near_final": pollution,
        }
    )

    # --- Ambiguity / conflict => REVIEW ---
    if has_multiple_distinct_filled_blocks:
        return (
            REVIEW,
            "multiple filled final-answer blocks exist with differing (conflicting) values",
            blocks,
            repetition,
            final_block,
            diagnostics,
        )

    if partial_blocks:
        return (
            REVIEW,
            "a final-answer block has partially blank field values, creating ambiguity about the true final answer",
            blocks,
            repetition,
            final_block,
            diagnostics,
        )

    if has_repetition_before_or_overlap:
        return (
            REVIEW,
            "repetition/looping region overlaps or occurs before the chosen final-answer block",
            blocks,
            repetition,
            final_block,
            diagnostics,
        )

    if severities != {"warning"}:
        return (
            REVIEW,
            "final-answer block is complete but severities include non-warning flags",
            blocks,
            repetition,
            final_block,
            diagnostics,
        )

    # --- No conflicts: decide CLEAN vs RECOVERABLE_WITH_WARNINGS ---
    pollution_reasons = []
    if filled_final_block_count > 1:
        pollution_reasons.append(f"{filled_final_block_count} repeated identical filled final-answer blocks")
    if has_blank_after:
        pollution_reasons.append("blank template final-answer block(s) appear after the chosen final block")
    if blank_template_block_count > 0 and not has_blank_after:
        pollution_reasons.append(f"{blank_template_block_count} blank template block(s) elsewhere in the answer")
    if has_repetition_after:
        pollution_reasons.append("tail repetition/looping detected after the final-answer block")
    if has_meta_after:
        pollution_reasons.append("meta-discussion about the answer format continues after the final-answer block")
    if pollution:
        pollution_reasons.append("the stored display_math span for this block also swallowed surrounding prose")

    if not pollution_reasons:
        return (
            KEEP_CLEAN,
            "single clean filled final-answer block near the end, no repetition or pollution detected",
            blocks,
            repetition,
            final_block,
            diagnostics,
        )

    reason = "filled final-answer block is recoverable (values: " + ", ".join(normalized_field_values(final_block)) + ") but answer has structural pollution: " + "; ".join(pollution_reasons)
    return (
        KEEP_RECOVERABLE_WITH_WARNINGS,
        reason,
        blocks,
        repetition,
        final_block,
        diagnostics,
    )


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    scenarios = load_manifest_scenarios()

    flags_by_run = defaultdict(list)
    for row in cursor.execute(
        "SELECT run_id, flag_type, severity, detail FROM extraction_quality_flags ORDER BY run_id, id"
    ):
        flags_by_run[row[0]].append({"flag_type": row[1], "severity": row[2], "detail": row[3]})

    flagged_run_ids = sorted(flags_by_run.keys())

    display_spans_by_run = defaultdict(list)
    for row in cursor.execute(
        "SELECT run_id, raw_text FROM extracted_math_spans WHERE span_type = 'display_math' ORDER BY run_id, span_index"
    ):
        display_spans_by_run[row[0]].append(row[1])

    answers_by_run = {}
    for row in cursor.execute(f'SELECT run_id, model_name, answer FROM "{RUNS_TABLE}"'):
        answers_by_run[row[0]] = {"model_name": row[1], "answer": row[2]}

    classification_counts = Counter()
    csv_rows = []
    md_entries = []
    comparison_run_ids = {214, 235, 290, 380, 496, 497, 498}
    comparisons = {}

    for run_id in flagged_run_ids:
        flags = flags_by_run[run_id]
        flag_types = sorted({f["flag_type"] for f in flags})
        severities = {f["severity"] for f in flags}
        severity_list = sorted(severities)

        info = answers_by_run.get(run_id, {})
        model_name = info.get("model_name")
        answer = info.get("answer") or ""
        answer_length = len(answer)
        scenario_id = scenarios.get(run_id, "")
        display_spans = display_spans_by_run.get(run_id, [])

        classification, reason, blocks, repetition, final_block, diagnostics = classify_run_v3(
            answer, severities, display_spans
        )
        classification_counts[classification] += 1

        if run_id in comparison_run_ids:
            v2_classification, _, _, _, _ = classify_run_v2(answer, severities)
            comparisons[run_id] = (v2_classification, classification)

        last_display_spans = display_spans[-LAST_DISPLAY_SPAN_COUNT:]
        tail_answer = answer[-LAST_SNIPPET_LIMIT:] if len(answer) > LAST_SNIPPET_LIMIT else answer

        blank_blocks = [b for b in blocks if b["field_count"] >= 2 and b["filled_field_count"] == 0]

        csv_rows.append(
            {
                "run_id": run_id,
                "model_name": model_name,
                "scenario_id": scenario_id,
                "answer_length": answer_length,
                "flag_types": ";".join(flag_types),
                "severities": ";".join(severity_list),
                "classification": classification,
                "reason": reason,
                "total_aligned_candidate_count": diagnostics["total_aligned_candidate_count"],
                "filled_final_block_count": diagnostics["filled_final_block_count"],
                "blank_template_block_count": diagnostics["blank_template_block_count"],
                "distinct_filled_final_block_count": diagnostics["distinct_filled_final_block_count"],
                "chars_after_last_filled_final_block": diagnostics["chars_after_last_filled_final_block"],
                "has_repetition_after_final_block": diagnostics["has_repetition_after_final_block"],
                "has_blank_template_after_last_filled_block": diagnostics["has_blank_template_after_last_filled_block"],
                "has_multiple_distinct_filled_blocks": diagnostics["has_multiple_distinct_filled_blocks"],
                "has_meta_discussion_after_final_block": diagnostics["has_meta_discussion_after_final_block"],
                "display_span_pollution_near_final": diagnostics["display_span_pollution_near_final"],
            }
        )

        md_entries.append(
            {
                "run_id": run_id,
                "model_name": model_name,
                "scenario_id": scenario_id,
                "answer_length": answer_length,
                "flag_types": flag_types,
                "severity_list": severity_list,
                "classification": classification,
                "reason": reason,
                "diagnostics": diagnostics,
               

[excerpt truncated]

```



## scripts/create_structured_prompt_v5_review_layer_v1.py

Reason: Latest structured prompt review-layer logic.
Included in full bundle as: full_file

```text
#!/usr/bin/env python3
"""Create review-layer v1 for structured-prompt pilot v5 outputs."""
from __future__ import annotations

import csv
import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PILOT_NAME = "structured_prompt_pilot_v5"
RUNS_PATH = ROOT / "outputs" / PILOT_NAME / "structured_prompt_pilot_v5_runs.json"
RUN_PLAN_PATH = ROOT / "outputs" / PILOT_NAME / "structured_prompt_pilot_v5_run_plan.json"
OUT_DIR = ROOT / "outputs" / PILOT_NAME / "review_layer_v1"
DB_PATH = ROOT / "learning.db"

sys.path.insert(0, str(ROOT))
from classify_remaining_layer1b_flags import find_final_answer_blocks  # noqa: E402
from extract_final_answers import field_pairs, reduce_value, select_final_block  # noqa: E402


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def run_plan_by_key() -> dict[tuple[str, str, int], dict[str, Any]]:
    plan = load_json(RUN_PLAN_PATH)
    out = {}
    for item in plan.get("items", []):
        key = (item.get("scenario_id", ""), item.get("model_label", ""), int(item.get("trial") or 1))
        out[key] = item
    return out


def analyze_run(run: dict[str, Any], plan_items: dict[tuple[str, str, int], dict[str, Any]]) -> dict[str, Any]:
    scenario_id = run.get("question_id") or run.get("scenario_id") or ""
    model_name = run.get("model_label") or run.get("model_name") or ""
    trial = int(run.get("trial") or 1)
    plan_item = plan_items.get((scenario_id, model_name, trial), {})
    prompt_mode = plan_item.get("prompt_mode", PILOT_NAME)

    response = run.get("response") or ""
    final, raw_helper_status = select_final_block(response)
    blocks = find_final_answer_blocks(response)

    field_count = 0
    numeric_field_count = 0
    if final is not None:
        for _, _, raw_value in field_pairs(final["raw_text"]):
            field_count += 1
            _, value_status = reduce_value(raw_value)
            if value_status == "NUMERIC":
                numeric_field_count += 1

    if raw_helper_status == "OK":
        review_status = "CLEAN"
        review_reason = "clean_first_layer_ok"
    else:
        review_status = "REVIEW"
        review_reason = "non_clean_helper_status"

    return {
        "scenario_id": scenario_id,
        "model_name": model_name,
        "prompt_mode": prompt_mode,
        "raw_helper_status": raw_helper_status,
        "first_layer_extractable": raw_helper_status == "OK",
        "review_status": review_status,
        "review_reason": review_reason,
        "final_answer_block_count": len(blocks),
        "field_count": field_count,
        "numeric_field_count": numeric_field_count,
        "output_path_or_run_id": run.get("run_id") or str(RUNS_PATH),
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "scenario_id",
        "model_name",
        "prompt_mode",
        "raw_helper_status",
        "first_layer_extractable",
        "review_status",
        "review_reason",
        "final_answer_block_count",
        "field_count",
        "numeric_field_count",
        "output_path_or_run_id",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_report(path: Path, rows: list[dict[str, Any]], db_modified: bool) -> dict[str, Any]:
    helper_counts = Counter(row["raw_helper_status"] for row in rows)
    review_counts = Counter(row["review_status"] for row in rows)
    summary = {
        "total_runs": len(rows),
        "clean_total": review_counts.get("CLEAN", 0),
        "review_total": review_counts.get("REVIEW", 0),
    }
    lines = [
        "# Structured Prompt Pilot v5 Review Layer v1",
        "",
        "## Summary Counts",
        "",
    ]
    lines.extend(f"- {key}: {value}" for key, value in summary.items())
    lines.extend(["", "## Helper Status Distribution Before Review Layer", ""])
    lines.extend(f"- {status}: {count}" for status, count in sorted(helper_counts.items()))
    lines.extend(["", "## Review Status Distribution", ""])
    lines.extend(f"- {status}: {count}" for status, count in sorted(review_counts.items()))
    lines.extend(
        [
            "",
            "## Review Rows",
            "",
            "| scenario_id | model_name | raw_helper_status | first_layer_extractable | review_reason |",
            "|---|---|---|---:|---|",
        ]
    )
    for row in rows:
        if row["review_status"] == "REVIEW":
            lines.append(
                f"| {row['scenario_id']} | {row['model_name']} | {row['raw_helper_status']} | "
                f"{row['first_layer_extractable']} | {row['review_reason']} |"
            )
    if review_counts.get("REVIEW", 0) == 0:
        lines.append("| none | none | none | n/a | none |")
    lines.extend(
        [
            "",
            "## Safety Confirmations",
            "",
            "- raw_outputs_unchanged: yes",
            f"- learning_db_modified: {'yes' if db_modified else 'no'}",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"summary": summary, "helper_status_distribution": dict(helper_counts), "review_status_distribution": dict(review_counts)}


def main() -> None:
    if not RUNS_PATH.exists():
        raise SystemExit(f"Missing run output file: {RUNS_PATH}")
    before_mtime = DB_PATH.stat().st_mtime_ns
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.execute("SELECT 1").fetchone()
    con.close()

    runs = load_json(RUNS_PATH)
    if len(runs) != 64:
        raise SystemExit(f"Expected 64 v5 runs, found {len(runs)}")
    plan_items = run_plan_by_key()
    rows = [analyze_run(run, plan_items) for run in runs]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(OUT_DIR / "review_layer_v1.csv", rows)
    (OUT_DIR / "review_layer_v1.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    db_modified = before_mtime != DB_PATH.stat().st_mtime_ns
    result = write_report(OUT_DIR / "REVIEW_LAYER_V1_REPORT.md", rows, db_modified)
    for key, value in result["summary"].items():
        print(f"{key}={value}")
    print("helper_status_distribution=" + json.dumps(result["helper_status_distribution"], sort_keys=True))
    print("review_status_distribution=" + json.dumps(result["review_status_distribution"], sort_keys=True))
    print(f"learning_db_modified={'yes' if db_modified else 'no'}")
    print(f"output_dir={OUT_DIR}")


if __name__ == "__main__":
    main()

```



## scripts/autograde_structured_prompt_v5_no_bert.py

Reason: Latest deterministic autograder interface for CLEAN rows.
Included in full bundle as: full_file

```text
#!/usr/bin/env python3
"""Autograde structured-prompt pilot v5 CLEAN rows without BERTScore."""
from __future__ import annotations

import csv
import json
import shutil
import sqlite3
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PILOT_NAME = "structured_prompt_pilot_v5"
RUNS_PATH = ROOT / "outputs" / PILOT_NAME / "structured_prompt_pilot_v5_runs.json"
REVIEW_CSV = ROOT / "outputs" / PILOT_NAME / "review_layer_v1" / "review_layer_v1.csv"
REVIEW_JSON = ROOT / "outputs" / PILOT_NAME / "review_layer_v1" / "review_layer_v1.json"
OUT_DIR = ROOT / "outputs" / PILOT_NAME / "autograde_no_bert_v1"
PDF_SOURCE_DIR = ROOT / "outputs" / PILOT_NAME / "pdf_review_source"
ALL32_DIR = ROOT / "outputs" / "structured_prompt_all32_summary"
DB_PATH = ROOT / "learning.db"
BENCHMARK_ID = "scientific_reasoning_32_v1"

sys.path.insert(0, str(ROOT))
from extract_final_answers import field_pairs, select_final_block  # noqa: E402
from symbolic_eval import eval_value  # noqa: E402


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_review_rows() -> list[dict[str, Any]]:
    with REVIEW_CSV.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_runs_by_id() -> dict[str, dict[str, Any]]:
    return {run["run_id"]: run for run in load_json(RUNS_PATH)}


def connect_ro() -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def load_gold_fields(con: sqlite3.Connection) -> dict[str, list[sqlite3.Row]]:
    rows = con.execute(
        """
        SELECT scenario_id, field_index, field_name, expected_value_raw, expected_value_num,
               tolerance, tolerance_mode
        FROM gold_fields
        WHERE benchmark_id = ?
        ORDER BY scenario_id, field_index
        """,
        (BENCHMARK_ID,),
    ).fetchall()
    out: dict[str, list[sqlite3.Row]] = defaultdict(list)
    for row in rows:
        out[row["scenario_id"]].append(row)
    return dict(out)


def near(model_value: float, gold_value: float, tolerance: float, tolerance_mode: str) -> bool:
    if tolerance_mode != "relative":
        return abs(model_value - gold_value) <= tolerance
    tol = abs(gold_value) * tolerance if gold_value != 0 else tolerance
    return abs(model_value - gold_value) <= max(tol, 1e-12)


def extract_values(response: str) -> tuple[str, dict[str, str]]:
    final, status = select_final_block(response)
    if final is None:
        return status, {}
    values = {field_name: raw_value for _, field_name, raw_value in field_pairs(final["raw_text"])}
    return status, values


def normalized_final_answer(values: dict[str, str], gold_rows: list[sqlite3.Row]) -> dict[str, str]:
    return {row["field_name"]: values.get(row["field_name"], "") for row in gold_rows}


def grade_row(review_row: dict[str, Any], run: dict[str, Any], gold_rows: list[sqlite3.Row]) -> dict[str, Any]:
    helper_status, values = extract_values(run.get("response") or "")
    normalized = normalized_final_answer(values, gold_rows)
    failed_fields: list[str] = []
    error_tags: list[str] = []
    numeric_match_count = 0
    numeric_total_count = len(gold_rows)

    for gold in gold_rows:
        field = gold["field_name"]
        raw_value = values.get(field)
        if raw_value is None or not raw_value.strip():
            failed_fields.append(field)
            error_tags.append(f"{field}:NOT_FOUND")
            continue
        model_num, note = eval_value(raw_value)
        if model_num is None:
            failed_fields.append(field)
            error_tags.append(f"{field}:UNPARSEABLE:{note}")
            continue
        gold_num = gold["expected_value_num"]
        if gold_num is None:
            failed_fields.append(field)
            error_tags.append(f"{field}:GOLD_NON_NUMERIC")
            continue
        if near(float(model_num), float(gold_num), float(gold["tolerance"]), str(gold["tolerance_mode"])):
            numeric_match_count += 1
        else:
            failed_fields.append(field)
            error_tags.append(f"{field}:MISMATCH")

    deterministic_grade = "PASS" if numeric_match_count == numeric_total_count else "FAIL"
    if not failed_fields:
        primary_failure_mode = "none"
    elif any("NOT_FOUND" in tag for tag in error_tags):
        primary_failure_mode = "missing_field"
    elif any("UNPARSEABLE" in tag for tag in error_tags):
        primary_failure_mode = "unparseable_value"
    elif any("MISMATCH" in tag for tag in error_tags):
        primary_failure_mode = "numeric_mismatch"
    else:
        primary_failure_mode = "other"

    extraction_status = "OK" if helper_status == "OK" and len(values) == len(gold_rows) else helper_status
    return {
        "scenario_id": review_row["scenario_id"],
        "model_name": review_row["model_name"],
        "prompt_mode": review_row["prompt_mode"],
        "raw_helper_status": review_row["raw_helper_status"],
        "review_status": review_row["review_status"],
        "field_count": int(review_row["field_count"]),
        "numeric_field_count": int(review_row["numeric_field_count"]),
        "normalized_final_answer": json.dumps(normalized, ensure_ascii=False, sort_keys=True),
        "extraction_status": extraction_status,
        "deterministic_grade": deterministic_grade,
        "numeric_match_count": numeric_match_count,
        "numeric_total_count": numeric_total_count,
        "failed_fields": ";".join(failed_fields),
        "error_tags": ";".join(error_tags),
        "primary_failure_mode": primary_failure_mode,
        "output_path_or_run_id": review_row["output_path_or_run_id"],
    }


def most_common_failure(rows: list[dict[str, Any]]) -> str:
    failures = [row["primary_failure_mode"] for row in rows if row["primary_failure_mode"] != "none"]
    if not failures:
        return "none"
    return Counter(failures).most_common(1)[0][0]


def summarize(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[row[key]].append(row)
    out = []
    for group_key, group_rows in sorted(groups.items()):
        pass_count = sum(1 for row in group_rows if row["deterministic_grade"] == "PASS")
        fail_count = len(group_rows) - pass_count
        out.append(
            {
                key: group_key,
                "clean_rows": len(group_rows),
                "pass_count": pass_count,
                "fail_count": fail_count,
                "pass_rate": round(pass_count / len(group_rows), 6) if group_rows else 0,
                "most_common_failure_mode": most_common_failure(group_rows),
            }
        )
    return out


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_report(
    autograde_rows: list[dict[str, Any]],
    scenario_summary: list[dict[str, Any]],
    model_summary: list[dict[str, Any]],
    review_rows: list[dict[str, Any]],
    db_modified: bool,
) -> None:
    grade_counts = Counter(row["deterministic_grade"] for row in autograde_rows)
    extraction_counts = Counter(row["extraction_status"] for row in autograde_rows)
    failure_counts = Counter(
        row["primary_failure_mode"] for row in autograde_rows if row["primary_failure_mode"] != "none"
    )
    pass_count = grade_counts.get("PASS", 0)
    total = len(autograde_rows)
    lines = [
        "# Structured Prompt v5 Autograde No BERT Report",
        "",
        "## Inputs",
        "",
        f"- raw_runs: {RUNS_PATH}",
        f"- review_layer_csv: {REVIEW_CSV}",
        f"- review_layer_json: {REVIEW_JSON}",
        "",
        "## Safety",
        "",
        f"- learning_db_modified: {'yes' if db_modified else 'no'}",
        "- db_backup_created: no",
        "- BERTScore was not run.",
        "",
        "## Counts",
        "",
        f"- CLEAN rows autograded: {len(autograde_rows)}",
        f"- REVIEW rows excluded: {len(review_rows)}",
        "",
        "## Extraction Status Distribution",
        "",
    ]
    lines.extend(f"- {status}: {count}" for status, count in sorted(extraction_counts.items()))
    lines.extend(["", "## Deterministic Grade Distribution", ""])
    lines.extend(f"- {grade}: {count}" for grade, count in sorted(grade_counts.items()))
    lines.extend(
        [
            f"- overall_pass_rate: {round(pass_count / total, 6) if total else 0}",
            "",
            "## Summary By Scenario",
            "",
            "| scenario_id | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for row in scenario_summary:
        lines.append(
            f"| {row['scenario_id']} | {row['clean_rows']} | {row['pass_count']} | "
            f"{row['fail_count']} | {row['pass_rate']} | {row['most_common_failure_mode']} |"
        )
    lines.extend(
        [
            "",
            "## Summary By Model",
            "",
            "| model_name | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for row in model_summary:
        lines.append(
            f"| {row['model_name']} | {row['clean_rows']} | {row['pass_count']} | "
            f"{row['fail_count']} | {row['pass_rate']} | {row['most_common_failure_mode']} |"
        )
    lines.extend(["", "## Failed Fields And Failure Tags", ""])
    if failure_counts:
        for mode, count in sorted(failure_counts.items()):
            lines.append(f"- {mode}: {count}")
        for row in autograde_rows:
            if row["deterministic_grade"] == "FAIL":
                lines.append(
                    f"- {row['scenario_id']} / {row['model_name']}: "
                    f"failed_fields={row['failed_fields']} error_tags={row['error_tags']}"
                )
    else:
        lines.append("- none")
    (OUT_DIR / "STRUCTURED_PROMPT_V5_AUTOGRADE_NO_BERT_REPORT.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def copy_if_exists(src: Path, dst: Path) -> None:
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def create_pdf_review_source() -> Path:
    if PDF_SOURCE_DIR.exists():
        shutil.rmtree(PDF_SOURCE_DIR)
    (PDF_SOURCE_DIR / "runs").mkdir(parents=True, exist_ok=True)
    (PDF_SOURCE_DIR / "autograde").mkdir(parents=True, exist_ok=True)
    (PDF_SOURCE_DIR / "review_layer").mkdir(parents=True, exist_ok=True)
    (PDF_SOURCE_DIR / "worked_solutions").mkdir(parents=True, exist_ok=True)

    copy_if_exists(RUNS_PATH, PDF_SOURCE_DIR / "runs" / RUNS_PATH.name)
    copy_if_exists(ROOT / "outputs" / PILOT_NAME / "structured_prompt_pilot_v5_run_plan.json", PDF_SOURCE_DIR / "runs" / "structured_prompt_pilot_v5_run_plan.json")
    copy_if_exists(ROOT / "outputs" / PILOT_NAME / "manifest.json", PDF_SOURCE_DIR / "runs" / "manifest.json")
    for path in (ROOT / "outputs" / PILOT_NAME / "review_layer_v1").glob("*"):
        if path.is_file():
            copy_if_exists(path, PDF_SOURCE_DIR / "review_layer" / path.name)
    for path in OUT_DIR.glob("*"):
        if path.is_file():
            copy_if_exists(path, PDF_SOURCE_DIR / "autograde" / path.name)
    worked_dir = ROOT / "outputs" / "structured_prompt_pilot_v2" / "pdf_review_source" / "worked_solutions"
    for path in sorted(worked_dir.glob("worked_solutions_batch*.md")):
        copy_if_exists(path, PDF_SOURCE_DIR / "worked_solutions" / path.name)

    readme = [
        "# Structured Prompt Pilot v5 PDF Review Source",
        "",
        "Scope: 64 total runs from structured_prompt_pilot_v5.",
        "",
        "BERTScore was not run.",
        "Raw model outputs are unchanged.",
        "",
        "Contents:",
        "- runs/",
        "- autograde/",
        "- review_layer/",
        "- worked_solutions/",
    ]
    (PDF_SOURCE_DIR / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")

    zip_path = ROOT / "outputs" / PILOT_NAME / "pdf_review_source.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(PDF_SOURCE_DIR.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(PDF_SOURCE_DIR.parent))
    return zip_path


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def create_all32_summary() -> dict[str, Any]:
    ALL32_DIR.mkdir(parents=True, exist_ok=True)
    batch_rows = []
    clean_rows = []
    review_rows = []
    for batch in ("v2", "v3", "v4", "v5"):
        base = ROOT / "outputs" / f"structured_prompt_pilot_{batch}"
        autograde_dir = base / "autograde_no_bert_v1"
        review_path = base / "review_layer_v1" / "review_layer_v1.csv"
        clean = load_csv(autograde_dir / f"structured_prompt_{batch}_clean_autograde.csv")
        review = [row for row in load_csv(review_path) if row.get("review_status") == "REVIEW"]
        grade_counts = Counter(row["deterministic_grade"] for row in clean)
        pass_count = grade_counts.get("PASS", 0)
        fail_count = grade_counts.get("FAIL", 0)
        batch_rows.append(
            {
                "batch": batch.upper(),
                "total_runs": len(clean) + len(review),
                "clean_rows": len(clean),
                "review_rows": len(review),
                "pass_count": pass_count,
                "fail_count": fail_count,
                "pass_rate": round(pass_count / len(clean), 6) if clean else 0,
            }
        )
        clean_rows.extend({**row, "batch": batch.upper()} for row in clean)
        review_rows.extend({**row, "batch": batch.upper()} for row in review)

    scenario_summary = summarize(clean_rows, "scenario_id")
    model_summary = summarize(clean_rows, "model_name")
    for row in scenario_summary:
        row["review_rows"] = sum(1 for review in review_rows if review["scenario_id"] == row["scenario_id"])
    for row in model_summary:
        row["review_rows"] = sum(1 for review in review_rows if review["model_name"] == row["model_name"])

    write_csv(ALL32_DIR / "structured_prompt_all32_summary_by_batch.csv", batch_rows)
    write_csv(ALL32_DIR / "structured_prompt_all32_summary_by_scenario.csv", scenario_summary)
    write_csv(ALL32_DIR / "structured_prompt_all32_summary_by_model.csv", model_summary)

    total_clean = len(clean_rows)
    total_review = len(review_rows)
    total_pass = sum(1 for row in clean_rows if row["deterministic_grade"] == "PASS")
    total_fail = sum(1 for row in clean_rows if row["deterministic_grade"] == "FAIL")
    zero_scenarios = [row["scenario_id"] for row in scenario_summary if float(row["pass_rate"]) == 0]
    perfect_scenarios = [row["scenario_id"] for row in scenario_summary if float(row["pass_rate"]) == 1]
    sorted_models = sorted(model_summary, key=lambda row: (float(row["pass_rate"]), row["model_name"]))
    lowest_models = sorted_models[:3]
    highest_models = sorted_models[-3:][::-1]

    lines = [
        "# Structured Prompt All32 Summary",
        "",
        f"- total_structured_runs: {total_clean + total_review}",
        f"- total_CLEAN_rows: {total_clean}",
        f"- total_REVIEW_rows: {total_review}",
        f"- pass_count: {total_pass}",
        f"- fail_count: {total_fail}",
        f"- overall_pass_rate_across_clean_rows: {round(total_pass / total_clean, 6) if total_clean else 0}",
        "- BERTScore_status: not run",
        "",
        "## Pass Rate By Batch",
        "",
        "| batch | total_runs | clean_rows | review_rows | pass_count | fail_count | pass_rate |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in batch_rows:
        lines.append(
            f"| {row['batch']} | {row['total_runs']} | {row['clean_rows']} | {row['review_rows']} | "
            f"{row['pass_count']} | {row['fail_count']} | {row['pass_rate']} |"
        )
    lines.extend(["", "## Scenario Extremes", ""])
    lines.append("- scenarios_with_0_percent_pass: " + (", ".join(zero_scenarios) if zero_scenarios else "none"))
    lines.append("- scenarios_with_100_percent_pass: " + (", ".join(perfect_scenarios) if perfect_scenarios else "none"))
    lines.extend(["", "## Model Extremes", ""])
    lines.append("- lowest_pass_rate_models: " + "; ".join(f"{row['model_name']} ({row['pass_rate']})" for row in lowest_models))
    lines.append("- highest_pass_rate_models: " + "; ".join(f"{row['model_name']} ({row['pass_rate']})" for row in highest_models))
    lines.extend(["", "## Pass Rate By Scenario", ""])
    lines.extend(f"- {row['scenario_id']}: {row['pass_rate']} ({row['pass_count']}/{row['clean_rows']})" for row in scenario_summary)
    lines.extend(["", "## Pass Rate By Model", ""])
    lines.extend(f"- {row['model_name']}: {row['pass_rate']} ({row['pass_count']}/{row['clean_rows']})" for row in model_summary)
    (ALL32_DIR / "STRUCTURED_PROMPT_ALL32_SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "total_structured_runs": total_clean + total_review,
        "total_clean_rows": total_clean,
        "total_review_rows": total_review,
        "pass_count": total_pass,
        "fail_count": total_fail,
        "overall_pass_rate": round(total_pass / total_clean, 6) if total_clean 

[excerpt truncated]

```



## scripts/export_structured_prompt_pilot_v5.py

Reason: Prompt/export validation including field order from gold_fields.field_index.
Included in full bundle as: full_file

```text
#!/usr/bin/env python3
"""Export and preflight structured-prompt pilot v5."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "learning.db"
OUTPUT_DIR = ROOT / "outputs" / "structured_prompt_pilot_v5"
WORKED_DIR = ROOT / "outputs" / "structured_prompt_pilot_v2" / "pdf_review_source" / "worked_solutions"
PILOT_NAME = "structured_prompt_pilot_v5"
BENCHMARK_ID = "scientific_reasoning_32_v1"

SCENARIO_ORDER = [
    "CM_TOP_001",
    "COS_AGE_001",
    "GR_CHIRP_001",
    "QFT_YUKAWA_001",
    "QI_CLONE_001",
    "QM_RT_001",
    "SR_FIZEAU_001",
    "STAT_NEGT_001",
]

USED_SCENARIOS = {
    "CM_FOUCAULT_001",
    "COS_CMB_001",
    "GR_ISCO_001",
    "QFT_G2_001",
    "QI_TELEPORT_001",
    "QM_BERRY_001",
    "SR_ROCKET_001",
    "STAT_ISING_001",
    "CM_APSIDAL_001",
    "COS_DL_001",
    "GR_GPS_001",
    "QFT_CASIMIR_001",
    "QI_WERNER_001",
    "QM_TUNNEL_001",
    "SR_BELL_001",
    "STAT_BEC_001",
    "CM_KAPITZA_001",
    "COS_DESITTER_001",
    "GR_PERI_001",
    "QFT_UNRUH_001",
    "QI_HOLEVO_001",
    "QM_AB_001",
    "SR_TWIN_001",
    "STAT_LANDAUER_001",
}

EXPECTED_CATEGORIES = {
    "Classical Mechanics",
    "Special Relativity",
    "General Relativity",
    "Quantum Mechanics",
    "Quantum Information Theory",
    "Quantum Field Theory",
    "Cosmology",
    "Statistical Mechanics",
}

MODEL_IDENTITIES = [
    {
        "model_id": "model_gemma3_12b",
        "model_label": "Gemma 3 12B IT",
        "provider": "OpenAI-compatible",
        "model": "google/gemma-3-12b-it",
    },
    {
        "model_id": "model_gemma3_27b",
        "model_label": "Gemma 3 27B IT",
        "provider": "OpenAI-compatible",
        "model": "google/gemma-3-27b-it",
    },
    {
        "model_id": "model_gemma4_31b",
        "model_label": "Gemma 4 31B IT",
        "provider": "OpenAI-compatible",
        "model": "google/gemma-4-31b-it",
    },
    {
        "model_id": "model_granite_41_8b",
        "model_label": "Granite 4.1 8B",
        "provider": "OpenAI-compatible",
        "model": "ibm-granite/granite-4.1-8b",
    },
    {
        "model_id": "model_llama_31_8b",
        "model_label": "Llama 3.1 8B Instruct",
        "provider": "OpenAI-compatible",
        "model": "meta-llama/llama-3.1-8b-instruct",
    },
    {
        "model_id": "model_ministral_8b",
        "model_label": "Ministral 3 8B",
        "provider": "OpenAI-compatible",
        "model": "mistralai/ministral-8b-2512",
    },
    {
        "model_id": "model_mistral_nemo_12b",
        "model_label": "Mistral NeMo 12B",
        "provider": "OpenAI-compatible",
        "model": "mistralai/mistral-nemo",
    },
    {
        "model_id": "model_mistral_small_32",
        "model_label": "Mistral Small 3.2 24B Instruct",
        "provider": "OpenAI-compatible",
        "model": "mistral-small-2506",
    },
]

BENCHMARK_INSTRUCTION_MARKER = "\nYou are solving a scientific reasoning benchmark."
FINAL_ANSWER_RE = re.compile(r"\*\*FINAL ANSWER\*\*", re.IGNORECASE)
SECTION_RE = re.compile(r"^##\s+([A-Z0-9_]+)\b.*?(?=^##\s+|\Z)", re.MULTILINE | re.DOTALL)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def connect_ro() -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def latex_field_name(field_name: str) -> str:
    return field_name.replace("_", r"\_")


def original_question_text(db_prompt: str) -> str:
    prompt = db_prompt.strip()
    marker_index = prompt.find(BENCHMARK_INSTRUCTION_MARKER)
    if marker_index >= 0:
        return prompt[:marker_index].strip()
    return prompt


def load_scenarios(con: sqlite3.Connection) -> dict[str, sqlite3.Row]:
    if set(SCENARIO_ORDER) & USED_SCENARIOS:
        reused = sorted(set(SCENARIO_ORDER) & USED_SCENARIOS)
        raise SystemExit("v5 scenario set reuses prior scenario(s): " + ", ".join(reused))
    placeholders = ",".join("?" for _ in SCENARIO_ORDER)
    rows = con.execute(
        f"""
        SELECT scenario_id, title, category, prompt
        FROM scenarios
        WHERE scenario_id IN ({placeholders})
        """,
        SCENARIO_ORDER,
    ).fetchall()
    by_id = {row["scenario_id"]: row for row in rows}
    missing = [scenario_id for scenario_id in SCENARIO_ORDER if scenario_id not in by_id]
    if missing:
        raise SystemExit("Missing scenario(s) in DB: " + ", ".join(missing))
    categories = [by_id[scenario_id]["category"] for scenario_id in SCENARIO_ORDER]
    if len(SCENARIO_ORDER) != 8:
        raise SystemExit(f"Expected 8 remaining scenarios, found {len(SCENARIO_ORDER)}")
    if set(categories) != EXPECTED_CATEGORIES:
        raise SystemExit(
            "Remaining scenario categories do not match expected set: "
            + ", ".join(sorted(set(categories)))
        )
    duplicate_categories = sorted({category for category in categories if categories.count(category) > 1})
    if duplicate_categories:
        raise SystemExit("More than one remaining scenario for category: " + ", ".join(duplicate_categories))
    return by_id


def load_gold_fields(con: sqlite3.Connection) -> dict[str, list[sqlite3.Row]]:
    placeholders = ",".join("?" for _ in SCENARIO_ORDER)
    rows = con.execute(
        f"""
        SELECT scenario_id, field_index, field_name, expected_value_raw, expected_value_num
        FROM gold_fields
        WHERE benchmark_id = ? AND scenario_id IN ({placeholders})
        ORDER BY scenario_id, field_index
        """,
        (BENCHMARK_ID, *SCENARIO_ORDER),
    ).fetchall()
    by_scenario: dict[str, list[sqlite3.Row]] = {scenario_id: [] for scenario_id in SCENARIO_ORDER}
    for row in rows:
        by_scenario[row["scenario_id"]].append(row)
    missing = [scenario_id for scenario_id, fields in by_scenario.items() if not fields]
    if missing:
        raise SystemExit("Missing gold field(s) in DB: " + ", ".join(missing))
    return by_scenario


def load_worked_sections() -> dict[str, str]:
    sections: dict[str, str] = {}
    for path in sorted(WORKED_DIR.glob("worked_solutions_batch*.md")):
        text = path.read_text(encoding="utf-8")
        for match in SECTION_RE.finditer(text):
            sections[match.group(1)] = match.group(0).strip()
    missing = [scenario_id for scenario_id in SCENARIO_ORDER if scenario_id not in sections]
    if missing:
        raise SystemExit("Missing worked-solution section(s): " + ", ".join(missing))
    return sections


def derivation_from_worked_section(section: str) -> str:
    derivation_start = section.find("**Derivation**")
    final_match = FINAL_ANSWER_RE.search(section)
    if derivation_start < 0 or final_match is None:
        raise SystemExit("Worked solution is missing Derivation or FINAL ANSWER marker")
    return section[derivation_start:final_match.start()].strip()


def protected_tokens(text: str) -> tuple[str, dict[str, str]]:
    protected = [
        "2GM/c²",
        "3GM/c²",
        "6GM/c²",
        "a²ω² > 2gL",
        "2gL",
        "6π",
        "1/(1−e²)",
        "1/(1-e²)",
        "T = ℏH/(2πk_B)",
        "ℏH/(2πk_B)",
        "ℏa/(2πck_B)",
        "h/e",
        "kBT ln 2",
        "k_B T ln 2",
        "log₂",
        "log2",
        "2π",
        "1/2π",
        "1/d⁴",
        "α/(2π)",
        "2/3",
        "1/2",
        "ζ(3/2)",
        "ζ^{2/3}",
    ]
    replacements = {}
    for idx, value in enumerate(protected):
        token = f"@@PROTECTED_{idx}@@"
        text = text.replace(value, token)
        replacements[token] = value
    return text, replacements


def restore_tokens(text: str, replacements: dict[str, str]) -> str:
    for token, value in replacements.items():
        text = text.replace(token, value)
    return text


def expected_value_variants(value: str) -> set[str]:
    variants = {value.strip()}
    try:
        number = float(value)
    except (TypeError, ValueError):
        return {item for item in variants if item}
    variants.update(
        {
            f"{number}",
            f"{number:.1f}",
            f"{number:.2f}",
            f"{number:.3f}",
            f"{number:.4f}",
            f"{number:.5f}",
            f"{number:.6f}",
        }
    )
    if abs(number - round(number)) < 1e-12:
        variants.add(str(int(round(number))))
    return {item for item in variants if item}


def sanitize_derivation(derivation: str, fields: list[sqlite3.Row]) -> str:
    text, replacements = protected_tokens(derivation)
    for row in fields:
        for value in sorted(expected_value_variants(str(row["expected_value_raw"] or "")), key=len, reverse=True):
            text = re.sub(rf"(?<![\w.]){re.escape(value)}(?![\w.])", "____", text)

    # Blank explicit bold computed results and common evaluated RHS fragments while
    # leaving conceptual formulas and constants intact.
    text = re.sub(r"\*\*([+\-−]?\d[\d.,]*(?:\s*[×x]\s*10[⁻−-]?\d+)?(?:\s*[A-Za-zμ/²³⁴^._-]+)?)\*\*", "**____**", text)
    text = re.sub(r"=\s*\*\*p\s*>\s*([^*]+)\*\*", "= **p > ____**", text)
    text = re.sub(r"=\s*\*\*([^*]*\d[^*]*)\*\*", "= **____**", text)
    text = re.sub(r"⟹\s*\*\*([^*]*\d[^*]*)\*\*", "⟹ **____**", text)
    text = re.sub(r"→\s*\*\*([^*]*\d[^*]*)\*\*", "→ **____**", text)
    text = re.sub(r"≈\s*\*\*([^*]*\d[^*]*)\*\*", "≈ **____**", text)
    text = re.sub(r"\b\d+\.\d{3,}\b", "____", text)
    return restore_tokens(text, replacements)


def final_answer_block(fields: list[sqlite3.Row]) -> str:
    max_field_len = max(len(latex_field_name(row["field_name"])) for row in fields)
    lines = ["**FINAL ANSWER**", "", r"\[", r"\begin{aligned}"]
    for row in fields:
        field = latex_field_name(row["field_name"])
        padding = " " * (max_field_len - len(field) + 1)
        lines.append(rf"\mathrm{{{field}}}{padding}&=  \\")
    lines.extend([r"\end{aligned}", r"\]"])
    return "\n".join(lines)


def build_prompt(original_question: str, worked_section: str, fields: list[sqlite3.Row]) -> str:
    derivation = sanitize_derivation(derivation_from_worked_section(worked_section), fields)
    parts = [
        "Solve the following scenario.",
        original_question_text(original_question),
        "Use the following answer structure. Keep the same sections and step order. Fill in the missing values by doing the calculation.",
        "Do not copy the placeholders.",
        "Do not add extra final-answer fields.",
        "Do not include more than one FINAL ANSWER block.",
        "Keep the final answer field names exactly as shown.",
        "Keep the final answer row order exactly as shown.",
        derivation,
        final_answer_block(fields),
    ]
    return "\n".join(parts)


def final_answer_field_order(prompt: str) -> list[str]:
    match = re.search(r"\\begin\{aligned\}(.*?)\\end\{aligned\}", prompt, flags=re.DOTALL)
    if not match:
        return []
    fields = []
    for line in match.group(1).splitlines():
        field_match = re.search(r"\\mathrm\{([^}]+)\}", line)
        if field_match:
            fields.append(field_match.group(1).replace(r"\_", "_"))
    return fields


def leaked_gold_values(prompt: str, fields: list[sqlite3.Row]) -> list[str]:
    leaks = []
    question_start = prompt.find("Use the following answer structure.")
    scaffold = prompt[question_start:] if question_start >= 0 else prompt
    for row in fields:
        raw = str(row["expected_value_raw"] or "").strip()
        if raw and re.search(rf"(?<![\w.]){re.escape(raw)}(?![\w.])", scaffold):
            leaks.append(raw)
    return leaks


def build_rows(
    scenarios: dict[str, sqlite3.Row],
    gold_fields: dict[str, list[sqlite3.Row]],
    worked_sections: dict[str, str],
) -> list[dict[str, str]]:
    rows = []
    sequence = 1
    for scenario_id in SCENARIO_ORDER:
        scenario = scenarios[scenario_id]
        prompt = build_prompt(scenario["prompt"] or "", worked_sections[scenario_id], gold_fields[scenario_id])
        for model in MODEL_IDENTITIES:
            rows.append(
                {
                    "pilot_name": PILOT_NAME,
                    "prompt_mode": PILOT_NAME,
                    "prompt_sequence": str(sequence),
                    "scenario_id": scenario_id,
                    "scenario_title": scenario["title"] or "",
                    "category": scenario["category"] or "",
                    "model_id": model["model_id"],
                    "model_label": model["model_label"],
                    "provider": model["provider"],
                    "model": model["model"],
                    "trial": "1",
                    "prompt": prompt,
                    "prompt_sha256": sha256_text(prompt),
                }
            )
            sequence += 1
    return rows


def preflight(rows: list[dict[str, str]], scenarios: dict[str, sqlite3.Row], gold_fields: dict[str, list[sqlite3.Row]]) -> dict[str, Any]:
    scenario_summary: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "assignment_count": 0,
            "original_question_present_count": 0,
            "final_answer_block_count_ok": 0,
            "final_answer_field_order_matches_db": True,
            "leaked_final_gold_values_detected": False,
            "placeholder_count": 0,
        }
    )
    row_results = []
    for row in rows:
        sid = row["scenario_id"]
        prompt = row["prompt"]
        question = original_question_text(scenarios[sid]["prompt"] or "")
        expected_order = [field["field_name"] for field in gold_fields[sid]]
        actual_order = final_answer_field_order(prompt)
        leaks = leaked_gold_values(prompt, gold_fields[sid])
        final_blocks = len(FINAL_ANSWER_RE.findall(prompt))
        placeholder_count = prompt.count("____")
        question_present = question in prompt
        prompt_begins_ok = not prompt.lstrip().startswith("**Derivation**")
        result = {
            "scenario_id": sid,
            "model_id": row["model_id"],
            "prompt_mode": row["prompt_mode"],
            "final_answer_field_count": len(actual_order),
            "leaked_gold_values_detected": bool(leaks),
            "original_question_present": question_present,
            "exactly_one_final_answer_block": final_blocks == 1,
            "field_order_matches_db": actual_order == expected_order,
            "placeholder_count": placeholder_count,
            "prompt_does_not_begin_with_derivation": prompt_begins_ok,
            "leaked_values": leaks,
        }
        row_results.append(result)
        summary = scenario_summary[sid]
        summary["assignment_count"] += 1
        summary["original_question_present_count"] += int(question_present)
        summary["final_answer_block_count_ok"] += int(final_blocks == 1)
        summary["final_answer_field_order_matches_db"] = summary["final_answer_field_order_matches_db"] and actual_order == expected_order
        summary["leaked_final_gold_values_detected"] = summary["leaked_final_gold_values_detected"] or bool(leaks)
        summary["placeholder_count"] = min(summary["placeholder_count"] or placeholder_count, placeholder_count)

    total = len(rows)
    validation = {
        "total_assignments": total,
        "scenario_count": len({row["scenario_id"] for row in rows}),
        "model_count": len({row["model_label"] for row in rows}),
        "nemotron_assignments": sum(1 for row in rows if "Nemotron" in row["model_label"]),
        "original_question_present": f"{sum(r['original_question_present'] for r in row_results)}/{total}",
        "exactly_one_final_answer_block": f"{sum(r['exactly_one_final_answer_block'] for r in row_results)}/{total}",
        "field_order_matches_db": f"{sum(r['field_order_matches_db'] for r in row_results)}/{total}",
        "leaked_final_gold_values": sum(len(r["leaked_values"]) for r in row_results),
        "placeholder_count_gt_zero": f"{sum(r['placeholder_count'] > 0 for r in row_results)}/{total}",
        "prompt_does_not_begin_with_derivation": all(r["prompt_does_not_begin_with_derivation"] for r in row_results),
        "remaining_scenario_count": len(SCENARIO_ORDER),
        "remaining_scenarios_are_unused": not bool(set(SCENARIO_ORDER) & USED_SCENARIOS),
        "one_remaining_scenario_per_category": len({scenarios[sid]["category"] for sid in SCENARIO_ORDER}) == 8
        and {scenarios[sid]["category"] for sid in SCENARIO_ORDER} == EXPECTED_CATEGORIES,
        "scenario_summary": {sid: dict(scenario_summary[sid]) for sid in SCENARIO_ORDER},
        "row_results": row_results,
    }
    failures = []
    if validation["total_assignments"] != 64:
        failures.append("total_assignments")
    if validation["scenario_count"] != 8:
        failures.append("scenario_count")
    if validation["model_count"] != 8:
        failures.append("model_count")
    if validation["nemotron_assignments"] != 0:
        failures.append("nemotron_assignments")
    if validation["original_question_present"] != "64/64":
        failures.append("original_question_present")
    if validation["exactly_one_final_answer_block"] != "64/64":
        failures.append("exactly_one_final_answer_block")
    if validation["field_order_matches_db"] != "64/64":
        failures.append("field_order_matches_db")
    if validation["leaked_final_gold_values"] != 0:
        failures.append("leaked_final_gold_values")
    if validation["placeholder_count_gt_zero"] != "64/64":
        failures.append("placeholder_count_gt_zero")
    if not validation["prompt_does_not_begin_with_derivation"]:
        failures.append("prompt_does_not_begin_with_derivation")
    if validation["remaining_scenario_count"] != 8:
        

[excerpt truncated]

```



## scripts/add_review_layer.py

Reason: Database-backed review/usable layer policy and historical unusable IDs.
Included in full bundle as: full_file

```text
#!/usr/bin/env python3
"""Add and populate the database-backed review/correction layer."""
from __future__ import annotations

import argparse
import csv
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "learning.db"
DEFAULT_CLASSIFICATION_CSV = ROOT / "remaining_layer1b_flag_classification_v3.csv"
METHOD_VERSION = "review_layer_v1"
REVIEWER = "pipeline_manual_review"

STATUS_TO_USABILITY = {
    "KEEP_CLEAN": "USABLE",
    "KEEP_RECOVERABLE_WITH_WARNINGS": "USABLE",
    "REVIEW": "REVIEW",
    "UNUSABLE": "UNUSABLE",
}

EXPECTED_UNUSABLE_IDS = {185, 187, 188, 256, 286, 380, 514}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_header(value: str) -> str:
    return value.strip().lower().replace(" ", "_")


def find_column(headers: list[str], candidates: list[str]) -> str | None:
    normalized = {normalize_header(header): header for header in headers}
    for candidate in candidates:
        if candidate in normalized:
            return normalized[candidate]
    return None


def ensure_schema(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS run_quality_status (
            run_id INTEGER PRIMARY KEY,
            quality_status TEXT NOT NULL,
            usability_status TEXT NOT NULL,
            source_artifact TEXT,
            rationale TEXT,
            reviewer TEXT DEFAULT 'pipeline_manual_review',
            method_version TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY(run_id) REFERENCES questions(run_id)
        );

        CREATE TABLE IF NOT EXISTS review_overrides (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id INTEGER NOT NULL,
            target_table TEXT NOT NULL,
            target_id TEXT,
            field_name TEXT,
            original_value TEXT,
            override_value TEXT NOT NULL,
            override_reason TEXT NOT NULL,
            reviewer TEXT DEFAULT 'human',
            created_at TEXT NOT NULL,
            FOREIGN KEY(run_id) REFERENCES questions(run_id)
        );

        CREATE TABLE IF NOT EXISTS correction_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            correction_type TEXT NOT NULL,
            affected_layer TEXT NOT NULL,
            affected_table TEXT,
            affected_run_id INTEGER,
            summary TEXT NOT NULL,
            cause TEXT,
            fix TEXT,
            validation TEXT,
            source_artifact TEXT,
            created_at TEXT NOT NULL
        );
        """
    )


def load_classifications(csv_path: Path) -> tuple[list[str], dict[int, dict[str, str]]]:
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        print("classification_csv_headers=" + ", ".join(headers))

        run_id_col = find_column(headers, ["run_id", "run"])
        quality_col = find_column(headers, ["classification", "quality_status", "layer1b_classification"])
        rationale_col = find_column(headers, ["reason", "rationale", "review_reason", "notes"])

        missing = []
        if run_id_col is None:
            missing.append("run_id")
        if quality_col is None:
            missing.append("classification/quality_status")
        if missing:
            raise SystemExit(
                "Cannot populate run_quality_status: missing required CSV column(s): "
                + ", ".join(missing)
            )

        rows: dict[int, dict[str, str]] = {}
        for line_no, row in enumerate(reader, start=2):
            raw_run_id = (row.get(run_id_col) or "").strip()
            if not raw_run_id:
                raise SystemExit(f"Cannot populate run_quality_status: blank run_id at CSV line {line_no}")
            try:
                run_id = int(raw_run_id)
            except ValueError as exc:
                raise SystemExit(f"Cannot populate run_quality_status: invalid run_id {raw_run_id!r}") from exc

            quality_status = (row.get(quality_col) or "").strip()
            if quality_status not in STATUS_TO_USABILITY:
                raise SystemExit(
                    "Cannot populate run_quality_status: unsupported classification "
                    f"{quality_status!r} for run_id={run_id}"
                )

            rows[run_id] = {
                "quality_status": quality_status,
                "usability_status": STATUS_TO_USABILITY[quality_status],
                "rationale": (row.get(rationale_col) or "").strip() if rationale_col else None,
            }

    return headers, rows


def upsert_status(
    con: sqlite3.Connection,
    run_id: int,
    quality_status: str,
    usability_status: str,
    source_artifact: str | None,
    rationale: str | None,
    now: str,
) -> None:
    con.execute(
        """
        INSERT INTO run_quality_status (
            run_id,
            quality_status,
            usability_status,
            source_artifact,
            rationale,
            reviewer,
            method_version,
            created_at,
            updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(run_id) DO UPDATE SET
            quality_status = excluded.quality_status,
            usability_status = excluded.usability_status,
            source_artifact = excluded.source_artifact,
            rationale = excluded.rationale,
            reviewer = excluded.reviewer,
            method_version = excluded.method_version,
            updated_at = excluded.updated_at
        """,
        (
            run_id,
            quality_status,
            usability_status,
            source_artifact,
            rationale,
            REVIEWER,
            METHOD_VERSION,
            now,
            now,
        ),
    )


def populate_run_quality_status(con: sqlite3.Connection, csv_path: Path) -> None:
    if not csv_path.exists():
        raise SystemExit(f"Cannot populate run_quality_status: classification CSV not found: {csv_path}")

    _, classifications = load_classifications(csv_path)
    all_run_ids = {
        int(row[0])
        for row in con.execute("SELECT run_id FROM questions WHERE run_id IS NOT NULL ORDER BY run_id")
    }
    flagged_run_ids = {
        int(row[0])
        for row in con.execute("SELECT DISTINCT run_id FROM extraction_quality_flags ORDER BY run_id")
    }
    classified_run_ids = set(classifications)

    unclassified_flagged = flagged_run_ids - classified_run_ids
    if unclassified_flagged:
        raise SystemExit(
            "Cannot populate run_quality_status: flagged run(s) have no Layer 1B classification: "
            + ", ".join(str(run_id) for run_id in sorted(unclassified_flagged))
        )

    unknown_classified = classified_run_ids - all_run_ids
    if unknown_classified:
        raise SystemExit(
            "Cannot populate run_quality_status: classification CSV contains unknown run_id(s): "
            + ", ".join(str(run_id) for run_id in sorted(unknown_classified))
        )

    now = utc_now()
    source_artifact = csv_path.name
    for run_id, status in sorted(classifications.items()):
        upsert_status(
            con,
            run_id,
            status["quality_status"],
            status["usability_status"],
            source_artifact,
            status["rationale"],
            now,
        )

    default_run_ids = all_run_ids - classified_run_ids - flagged_run_ids
    for run_id in sorted(default_run_ids):
        upsert_status(
            con,
            run_id,
            "KEEP_CLEAN",
            "USABLE",
            "default_no_layer1b_flag",
            "No Layer 1B quality flag and no explicit classification artifact row.",
            now,
        )

    missing_rows = all_run_ids - {
        int(row[0]) for row in con.execute("SELECT run_id FROM run_quality_status")
    }
    if missing_rows:
        raise SystemExit(
            "Cannot populate run_quality_status: missing status row(s) after population: "
            + ", ".join(str(run_id) for run_id in sorted(missing_rows))
        )


def insert_correction_log(con: sqlite3.Connection) -> None:
    summary = (
        "Added database-backed review layer tables and populated run_quality_status "
        "from Layer 1B review artifacts."
    )
    existing = con.execute(
        """
        SELECT 1
        FROM correction_log
        WHERE correction_type = ?
          AND affected_layer = ?
          AND affected_table = ?
          AND summary = ?
        LIMIT 1
        """,
        ("schema_addition", "review_layer", "run_quality_status", summary),
    ).fetchone()
    if existing:
        return

    con.execute(
        """
        INSERT INTO correction_log (
            correction_type,
            affected_layer,
            affected_table,
            affected_run_id,
            summary,
            cause,
            fix,
            validation,
            source_artifact,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "schema_addition",
            "review_layer",
            "run_quality_status",
            None,
            summary,
            "Human review decisions and correction history previously lived only in CSV/Markdown artifacts.",
            "Created run_quality_status, review_overrides, and correction_log tables; populated one status row per run.",
            "verify_review_layer.py checks row coverage, expected unusable runs, and unchanged official grading counts.",
            DEFAULT_CLASSIFICATION_CSV.name,
            utc_now(),
        ),
    )


def print_verification(con: sqlite3.Connection) -> None:
    total = con.execute("SELECT COUNT(*) FROM run_quality_status").fetchone()[0]
    print(f"run_quality_status_rows={total}")
    print("quality_usability_distribution")
    for quality_status, usability_status, count in con.execute(
        """
        SELECT quality_status, usability_status, COUNT(*)
        FROM run_quality_status
        GROUP BY quality_status, usability_status
        ORDER BY quality_status, usability_status
        """
    ):
        print(f"  {quality_status}|{usability_status}|{count}")

    unusable_ids = [
        int(row[0])
        for row in con.execute(
            """
            SELECT run_id
            FROM run_quality_status
            WHERE usability_status = 'UNUSABLE'
            ORDER BY run_id
            """
        )
    ]
    print("unusable_run_ids=" + ", ".join(str(run_id) for run_id in unusable_ids))

    if total != 641:
        raise SystemExit(f"Expected 641 run_quality_status rows, found {total}")
    if set(unusable_ids) != EXPECTED_UNUSABLE_IDS:
        raise SystemExit(
            "Expected unusable run IDs "
            + ", ".join(str(run_id) for run_id in sorted(EXPECTED_UNUSABLE_IDS))
            + "; found "
            + ", ".join(str(run_id) for run_id in unusable_ids)
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(DEFAULT_DB))
    parser.add_argument("--classification-csv", default=str(DEFAULT_CLASSIFICATION_CSV))
    args = parser.parse_args()

    con = sqlite3.connect(args.db)
    try:
        with con:
            ensure_schema(con)
            populate_run_quality_status(con, Path(args.classification_csv))
            insert_correction_log(con)
        print_verification(con)
    finally:
        con.close()


if __name__ == "__main__":
    main()

```



## PROJECT_TAKEOVER_REPORT.md

Reason: Concise project history for Layer 1B classification fixes and known run IDs.
Included in full bundle as: full_file

```text
# PROJECT_TAKEOVER_REPORT

Date: 2026-07-04
Scope: `Pipeline SQL proj/` — the math-extraction / Layer 1B pipeline built on `learning.db`.
Method: read-only inspection. Nothing was edited, moved, or deleted.

---

## 1. Project state summary

This folder is a **script-based extraction pipeline**, not the FastAPI app. `app.py` is a
one-row normalizer, not a UI. The pipeline stores raw model answers and three additive
extraction layers (Markdown blocks, math spans, quality flags) in a single SQLite file,
`learning.db`.

Current stage of work: Qwen runs have been deleted, the post-Qwen dataset (641 runs) has
full extraction coverage, and the 34 remaining Layer 1B warning-flagged runs have been
manually triaged through three classification passes (v1 → v2 → v3). The v3 pass is the
current source of truth for usability. No numeric/gold comparison has been done yet.

All counts, span totals, flag totals, and the confirmed unusable set stated in the takeover
brief **match the database exactly**. No discrepancies found.

Two facts that differ from the brief's framing, worth flagging:

- The v3 classification lives **only in CSV/Markdown files**, not in `learning.db`. There is
  no label/classification column anywhere in the schema. Any downstream step must read the CSV.
- `questions.scenario_id` does not exist; the v3 CSV records `scenario_id = "unknown"` for
  every row. Scenario is only implicit inside the `question` text.

---

## 2. Database / table inventory

Active DB: `learning.db` (13.6 MB). Backup: `backups/pre_delete_qwen_20260704_135321.db`
(pre-Qwen-deletion snapshot, same size). 4 tables, 0 views.

| Table | Rows | Purpose | Join key |
|---|---|---|---|
| `questions` | 641 | one row per run: raw answer + metadata | `id` (= `run_id`) |
| `extracted_markdown_blocks` | 24,905 | Layer 1 Markdown block extraction | `run_id` |
| `extracted_math_spans` | 18,076 | Layer 1 math-span extraction | `run_id` |
| `extraction_quality_flags` | 35 | Layer 1B delimiter/structure flags | `run_id` |

`questions` columns: `id`(pk), `run_id`, `model_name`, `question`, `answer`,
`normalized_answer`, `reasoning_text`, `calculation_text`.
Note: `id == run_id` for all 641 rows, so either can be used as the join key.
`reasoning_text` and `calculation_text` columns exist but are **0/641 populated** (added, never filled).

`extracted_math_spans` columns: `run_id`, `span_index`, `span_type`, `source`,
`start_char`, `end_char`, `raw_text`, `normalized_text`, `created_at`.
`extraction_quality_flags` columns: `run_id`, `flag_type`, `severity`, `source`,
`detail`, `created_at`. All three extraction tables are indexed on `run_id`.

Key files in this folder:
- Classifier: `classify_remaining_layer1b_flags.py` (25 KB — the v3 detector logic).
- v3 outputs: `remaining_layer1b_flag_classification_v3.csv` / `.md` (also v1, v2 kept).
- Unusable inspection: `inspect_unusable_runs.py` / `.md` / `.csv`, plus per-run dumps
  `run_{185,187,188,214,256,286,380,514}_full_answer.txt`.
- Layer builders: `create_layer1b_tables.py`, `create_extraction_quality_flags_table.py`,
  `populate_layer1b_from_md.py`, `populate_extraction_quality_flags.py`.
- Raw answer exports: `raw_answers_md/` (709 `.md` files, includes pre-deletion Qwen files).

---

## 3. Current dataset counts (verified against DB)

| Metric | Value | Brief | Match |
|---|---|---|---|
| Total runs (`questions`) | 641 | 641 | ✓ |
| Non-empty raw answers | 641 | 641 | ✓ |
| Runs with ≥1 Markdown block | 641 | full | ✓ |
| Runs with ≥1 math span | 641 | full | ✓ |
| Remaining Qwen runs | 0 | 0 | ✓ |
| `normalized_answer` populated | 641 | — | — |
| Markdown blocks total | 24,905 | 24,905 | ✓ |
| Math spans total | 18,076 | 18,076 | ✓ |
| — display_math | 8,443 | 8,443 | ✓ |
| — inline_math | 9,545 | 9,545 | ✓ |
| — environment | 88 | 88 | ✓ |

`run_id` range is 1–704 with gaps (deleted Qwen rows). 13 models present; the five 8–12B
open models dominate (Mistral NeMo 101, Gemma 3 12B 100, Ministral 3 8B 99, Llama 3.1 8B 99,
Granite 4.1 8B 97). Paid/cloud models are sparse (Gemini 2.5 Pro 3, DeepSeek Reasoner 2).

---

## 4. Layer 1B audit status

| Metric | Value | Brief | Match |
|---|---|---|---|
| Total flags | 35 | 35 | ✓ |
| Distinct flagged runs | 34 | 34 | ✓ |
| Critical flags | 0 | 0 | ✓ |
| Warning flags | 35 | 35 | ✓ |

Flag types: `unmatched_bracket_display` 29, `odd_single_dollar` 4, `unmatched_environment` 2.
No `short_math_heavy_answer` and no `math_markers_but_zero_spans` cases exist, as expected.

Confirmed correction from the brief holds: these warning flags are **not all harmless**. Of
the 34 flagged runs, 7 are UNUSABLE and 3 are recoverable-with-warnings; the flag alone does
not determine usability, which is why the v3 structural pass was needed.

---

## 5. v3 classification summary

Source: `remaining_layer1b_flag_classification_v3.csv` (34 rows = the 34 flagged runs only).
The other 607 unflagged runs are implicitly clean.

| Category | Count (flagged set) |
|---|---|
| KEEP_CLEAN | 24 |
| KEEP_RECOVERABLE_WITH_WARNINGS | 3 |
| REVIEW | 0 |
| UNUSABLE | 7 |

- KEEP_RECOVERABLE (3): runs **214, 235, 290** — recoverable filled final block but
  structural pollution (repeated/blank/tail blocks, or display-span pollution near the final).
- KEEP_CLEAN (24) includes **496, 497, 498** (valid `&\approx` final blocks — correctly not
  penalized for intermediate aligned derivation blocks).

Report-vs-DB mismatch: the DB stores **no** classification. Whole-dataset usability =
607 unflagged (clean) + 24 flagged-clean + 3 recoverable = **634 usable**, 7 unusable.

---

## 6. Confirmed unusable runs (7)

`185, 187, 188, 256, 286, 380, 514` — matches the brief exactly. Each was inspected via its
`run_*_full_answer.txt` dump. None contains a complete, filled, field-bearing final-answer block.

| Run | Model | Len | Confirmed failure mode |
|---|---|---|---|
| 185 | Llama 3.1 8B | 24,938 | Repetition loop ("Simplifying…" ×37; identical m₁/m₂ lines); truncated mid-substitution. No final block, no stable value. |
| 187 | Ministral 3 8B | 28,413 | Repetition (×19); truncated mid-number (`≈ 8.73 ×`). No final block. |
| 188 | Ministral 3 8B | 23,990 | Repetition of prefactor line (×23); truncated mid-number. No final block. |
| 256 | Nemotron 3 Nano 30B | 913 | Early truncation — cuts off mid-calc (`=5.`). No final block. |
| 286 | Llama 3.1 8B | 27,129 | Severe repetition loop — same `|P|` line ×286. No final block, no stable value. |
| 380 | Ministral 3 8B | 38,889 | Self-rejection loop: 34 "Final Answer" headings, 177 `(no)` markers around a self-rejected formula. No valid block. |
| 514 | Gemma 3 12B | 25,613 | Repetition loop (`T e^{-2κL}` chained inline); nonsense intermediate value. No final block. |

Summary of causes: truncation (185, 187, 188, 256), repetition loop (185, 187, 188, 286, 514),
self-rejected final answer (380). No stable recoverable values in any of the 7.

---

## 7. Known pitfalls and corrected bugs (carry forward)

Final-answer 

[excerpt truncated]

```



## remaining_layer1b_flag_classification_v3.csv

Reason: Compact classification table for known recoverable/unusable/clean flagged runs.
Included in full bundle as: full_file

```text
run_id,model_name,scenario_id,answer_length,flag_types,severities,classification,reason,total_aligned_candidate_count,filled_final_block_count,blank_template_block_count,distinct_filled_final_block_count,chars_after_last_filled_final_block,has_repetition_after_final_block,has_blank_template_after_last_filled_block,has_multiple_distinct_filled_blocks,has_meta_discussion_after_final_block,display_span_pollution_near_final
120,Granite 4.1 8B,unknown,2751,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",1,1,0,1,3,False,False,False,False,False
121,Granite 4.1 8B,unknown,2886,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",1,1,0,1,3,False,False,False,False,False
122,Granite 4.1 8B,unknown,2912,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",1,1,0,1,3,False,False,False,False,False
181,Granite 4.1 8B,unknown,8590,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",3,1,0,1,3,False,False,False,False,False
185,Llama 3.1 8B Instruct,unknown,24938,odd_single_dollar,warning,UNUSABLE,no complete filled final-answer block found anywhere in the answer,0,0,0,0,,False,False,False,False,False
187,Ministral 3 8B,unknown,28413,unmatched_bracket_display,warning,UNUSABLE,no complete filled final-answer block found anywhere in the answer,0,0,0,0,,False,False,False,False,False
188,Ministral 3 8B,unknown,23990,unmatched_bracket_display,warning,UNUSABLE,no complete filled final-answer block found anywhere in the answer,0,0,0,0,,False,False,False,False,False
214,NVIDIA Nemotron 3 Nano 30B-A3B,unknown,32394,unmatched_environment,warning,KEEP_RECOVERABLE_WITH_WARNINGS,"filled final-answer block is recoverable (values: 45.73, -7.21, 38.52) but answer has structural pollution: 14 repeated identical filled final-answer blocks; 7 blank template block(s) elsewhere in the answer; tail repetition/looping detected after the final-answer block; meta-discussion about the answer format continues after the final-answer block",22,14,7,1,3513,True,False,False,True,False
223,Granite 4.1 8B,unknown,4588,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",2,1,0,1,3,False,False,False,False,False
224,Granite 4.1 8B,unknown,4518,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",2,1,0,1,3,False,False,False,False,False
235,NVIDIA Nemotron 3 Nano 30B-A3B,unknown,29048,unmatched_environment,warning,KEEP_RECOVERABLE_WITH_WARNINGS,"filled final-answer block is recoverable (values: 88.6, 219.9, 439.8) but answer has structural pollution: 9 repeated identical filled final-answer blocks; blank template final-answer block(s) appear after the chosen final block; meta-discussion about the answer format continues after the final-answer block",14,9,4,1,1386,False,True,False,True,False
256,NVIDIA Nemotron 3 Nano 30B-A3B,unknown,913,unmatched_bracket_display,warning,UNUSABLE,no complete filled final-answer block found anywhere in the answer,0,0,0,0,,False,False,False,False,False
286,Llama 3.1 8B Instruct,unknown,27129,odd_single_dollar,warning,UNUSABLE,"no complete filled final-answer block found anywhere in the answer; repetition/looping present, preventing resolution",0,0,0,0,,False,False,False,False,False
290,Mistral NeMo 12B,unknown,2655,odd_single_dollar;unmatched_bracket_display,warning,KEEP_RECOVERABLE_WITH_WARNINGS,"filled final-answer block is recoverable (values: 1.3 \times 10^{-3} \text{ Pa}, 3.9 \times 10^{-5} \text{ μJ/m}^2, 1.56 \times 10^{-4} \text{ Pa}) but answer has structural pollution: the stored display_math span for this block also swallowed surrounding prose",1,1,0,1,3,False,False,False,False,True
336,NVIDIA Nemotron 3 Nano 30B-A3B,unknown,2864,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",2,1,0,1,3,False,False,False,False,False
372,Granite 4.1 8B,unknown,3565,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",1,1,0,1,3,False,False,False,False,False
380,Ministral 3 8B,unknown,38889,unmatched_bracket_display,warning,UNUSABLE,no complete filled final-answer block found anywhere in the answer,0,0,0,0,,False,False,False,False,False
392,Granite 4.1 8B,unknown,5268,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",1,1,0,1,3,False,False,False,False,False
394,Granite 4.1 8B,unknown,5386,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",1,1,0,1,3,False,False,False,False,False
412,Granite 4.1 8B,unknown,2785,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",1,1,0,1,3,False,False,False,False,False
413,Granite 4.1 8B,unknown,2934,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",1,1,0,1,3,False,False,False,False,False
414,Granite 4.1 8B,unknown,2933,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",1,1,0,1,3,False,False,False,False,False
467,NVIDIA Nemotron 3 Nano 30B-A3B,unknown,3433,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",2,1,0,1,3,False,False,False,False,False
496,Granite 4.1 8B,unknown,3643,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",2,1,0,1,3,False,False,False,False,False
497,Granite 4.1 8B,unknown,3543,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",2,1,0,1,3,False,False,False,False,False
498,Granite 4.1 8B,unknown,3701,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",2,1,0,1,3,False,False,False,False,False
509,NVIDIA Nemotron 3 Nano 30B-A3B,unknown,3757,unmatched_bracket_display,warning,KEEP_CLEAN,"single clean filled final-answer block near the end, no repetition or pollution detected",3,1,0,1,3,False,False,False,False,False
514,Gemma 3 12B IT,unknown,25613,odd_single_dollar,warning,UNUSABLE,"no complete filled final-answer block found anywhere in the answer; repetition/looping present, preventing resolution",0,0,0,0,,False,False,False,False,False
559,Granite

[excerpt truncated]

```



## outputs/structured_prompt_all32_summary/STRUCTURED_PROMPT_ALL32_SUMMARY.md

Reason: Combined V2-V5 structured prompt summary.
Included in full bundle as: full_file

```text
# Structured Prompt All32 Summary

- total_structured_runs: 264
- total_CLEAN_rows: 252
- total_REVIEW_rows: 12
- pass_count: 117
- fail_count: 135
- overall_pass_rate_across_clean_rows: 0.464286
- BERTScore_status: not run

## Pass Rate By Batch

| batch | total_runs | clean_rows | review_rows | pass_count | fail_count | pass_rate |
|---|---:|---:|---:|---:|---:|---:|
| V2 | 72 | 64 | 8 | 37 | 27 | 0.578125 |
| V3 | 64 | 61 | 3 | 24 | 37 | 0.393443 |
| V4 | 64 | 63 | 1 | 19 | 44 | 0.301587 |
| V5 | 64 | 64 | 0 | 37 | 27 | 0.578125 |

## Scenario Extremes

- scenarios_with_0_percent_pass: GR_CHIRP_001, GR_GPS_001, GR_ISCO_001, STAT_BEC_001
- scenarios_with_100_percent_pass: QI_CLONE_001, QM_BERRY_001, SR_BELL_001, SR_FIZEAU_001

## Model Extremes

- lowest_pass_rate_models: Mistral NeMo 12B (0.125); Llama 3.1 8B Instruct (0.322581); Ministral 3 8B (0.375)
- highest_pass_rate_models: Gemma 4 31B IT (0.84375); Granite 4.1 8B (0.655172); Gemma 3 27B IT (0.5)

## Pass Rate By Scenario

- CM_APSIDAL_001: 0.375 (3/8)
- CM_FOUCAULT_001: 0.875 (7/8)
- CM_KAPITZA_001: 0.125 (1/8)
- CM_TOP_001: 0.75 (6/8)
- COS_AGE_001: 0.125 (1/8)
- COS_CMB_001: 0.625 (5/8)
- COS_DESITTER_001: 0.125 (1/8)
- COS_DL_001: 0.625 (5/8)
- GR_CHIRP_001: 0.0 (0/8)
- GR_GPS_001: 0.0 (0/8)
- GR_ISCO_001: 0.0 (0/8)
- GR_PERI_001: 0.125 (1/8)
- QFT_CASIMIR_001: 0.125 (1/8)
- QFT_G2_001: 0.375 (3/8)
- QFT_UNRUH_001: 0.285714 (2/7)
- QFT_YUKAWA_001: 0.875 (7/8)
- QI_CLONE_001: 1.0 (8/8)
- QI_HOLEVO_001: 0.25 (2/8)
- QI_TELEPORT_001: 0.75 (6/8)
- QI_WERNER_001: 0.75 (6/8)
- QM_AB_001: 0.5 (4/8)
- QM_BERRY_001: 1.0 (8/8)
- QM_RT_001: 0.125 (1/8)
- QM_TUNNEL_001: 0.142857 (1/7)
- SR_BELL_001: 1.0 (8/8)
- SR_FIZEAU_001: 1.0 (8/8)
- SR_ROCKET_001: 0.125 (1/8)
- SR_TWIN_001: 0.75 (6/8)
- STAT_BEC_001: 0.0 (0/6)
- STAT_ISING_001: 0.875 (7/8)
- STAT_LANDAUER_001: 0.25 (2/8)
- STAT_NEGT_001: 0.75 (6/8)

## Pass Rate By Model

- Gemma 3 12B IT: 0.46875 (15/32)
- Gemma 3 27B IT: 0.5 (16/32)
- Gemma 4 31B IT: 0.84375 (27/32)
- Granite 4.1 8B: 0.655172 (19/29)
- Llama 3.1 8B Instruct: 0.322581 (10/31)
- Ministral 3 8B: 0.375 (12/32)
- Mistral NeMo 12B: 0.125 (4/32)
- Mistral Small 3.2 24B Instruct: 0.4375 (14/32)

```



## outputs/structured_prompt_pilot_v5/review_layer_v1/REVIEW_LAYER_V1_REPORT.md

Reason: Latest V5 clean extraction status.
Included in full bundle as: full_file

```text
# Structured Prompt Pilot v5 Review Layer v1

## Summary Counts

- total_runs: 64
- clean_total: 64
- review_total: 0

## Helper Status Distribution Before Review Layer

- OK: 64

## Review Status Distribution

- CLEAN: 64

## Review Rows

| scenario_id | model_name | raw_helper_status | first_layer_extractable | review_reason |
|---|---|---|---:|---|
| none | none | none | n/a | none |

## Safety Confirmations

- raw_outputs_unchanged: yes
- learning_db_modified: no

```



## outputs/structured_prompt_pilot_v5/autograde_no_bert_v1/STRUCTURED_PROMPT_V5_AUTOGRADE_NO_BERT_REPORT.md

Reason: Latest deterministic structured autograde report.
Included in full bundle as: full_file

```text
# Structured Prompt v5 Autograde No BERT Report

## Inputs

- raw_runs: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v5/structured_prompt_pilot_v5_runs.json
- review_layer_csv: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v5/review_layer_v1/review_layer_v1.csv
- review_layer_json: /Users/upigdir/Desktop/Pipeline SQL proj/outputs/structured_prompt_pilot_v5/review_layer_v1/review_layer_v1.json

## Safety

- learning_db_modified: no
- db_backup_created: no
- BERTScore was not run.

## Counts

- CLEAN rows autograded: 64
- REVIEW rows excluded: 0

## Extraction Status Distribution

- OK: 64

## Deterministic Grade Distribution

- FAIL: 27
- PASS: 37
- overall_pass_rate: 0.578125

## Summary By Scenario

| scenario_id | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |
|---|---:|---:|---:|---:|---|
| CM_TOP_001 | 8 | 6 | 2 | 0.75 | numeric_mismatch |
| COS_AGE_001 | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| GR_CHIRP_001 | 8 | 0 | 8 | 0.0 | numeric_mismatch |
| QFT_YUKAWA_001 | 8 | 7 | 1 | 0.875 | numeric_mismatch |
| QI_CLONE_001 | 8 | 8 | 0 | 1.0 | none |
| QM_RT_001 | 8 | 1 | 7 | 0.125 | numeric_mismatch |
| SR_FIZEAU_001 | 8 | 8 | 0 | 1.0 | none |
| STAT_NEGT_001 | 8 | 6 | 2 | 0.75 | numeric_mismatch |

## Summary By Model

| model_name | clean_rows | pass_count | fail_count | pass_rate | most_common_failure_mode |
|---|---:|---:|---:|---:|---|
| Gemma 3 12B IT | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| Gemma 3 27B IT | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| Gemma 4 31B IT | 8 | 7 | 1 | 0.875 | numeric_mismatch |
| Granite 4.1 8B | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| Llama 3.1 8B Instruct | 8 | 3 | 5 | 0.375 | numeric_mismatch |
| Ministral 3 8B | 8 | 5 | 3 | 0.625 | numeric_mismatch |
| Mistral NeMo 12B | 8 | 2 | 6 | 0.25 | numeric_mismatch |
| Mistral Small 3.2 24B Instruct | 8 | 5 | 3 | 0.625 | numeric_mismatch |

## Failed Fields And Failure Tags

- numeric_mismatch: 26
- unparseable_value: 1
- CM_TOP_001 / Llama 3.1 8B Instruct: failed_fields=precession_double_spin;precession_period_s;precession_rad_s error_tags=precession_double_spin:MISMATCH;precession_period_s:MISMATCH;precession_rad_s:MISMATCH
- CM_TOP_001 / Mistral NeMo 12B: failed_fields=precession_double_spin;precession_period_s;precession_rad_s error_tags=precession_double_spin:MISMATCH;precession_period_s:MISMATCH;precession_rad_s:MISMATCH
- COS_AGE_001 / Gemma 3 12B IT: failed_fields=hubble_time_gyr;lcdm_age_gyr;matter_age_gyr error_tags=hubble_time_gyr:MISMATCH;lcdm_age_gyr:MISMATCH;matter_age_gyr:MISMATCH
- COS_AGE_001 / Gemma 3 27B IT: failed_fields=lcdm_age_gyr error_tags=lcdm_age_gyr:MISMATCH
- COS_AGE_001 / Granite 4.1 8B: failed_fields=lcdm_age_gyr error_tags=lcdm_age_gyr:MISMATCH
- COS_AGE_001 / Llama 3.1 8B Instruct: failed_fields=hubble_time_gyr;lcdm_age_gyr;matter_age_gyr error_tags=hubble_time_gyr:UNPARSEABLE:parse-fail:SympifyError;lcdm_age_gyr:MISMATCH;matter_age_gyr:MISMATCH
- COS_AGE_001 / Ministral 3 8B: failed_fields=lcdm_age_gyr error_tags=lcdm_age_gyr:MISMATCH
- COS_AGE_001 / Mistral NeMo 12B: failed_fields=hubble_time_gyr;lcdm_age_gyr;matter_age_gyr error_tags=hubble_time_gyr:MISMATCH;lcdm_age_gyr:MISMATCH;matter_age_gyr:MISMATCH
- COS_AGE_001 / Mistral Small 3.2 24B Instruct: failed_fields=lcdm_age_gyr error_tags=lcdm_age_gyr:MISMATCH
- GR_CHIRP_001 / Gemma 3 12B IT: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Gemma 3 27B IT: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Gemma 4 31B IT: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Granite 4.1 8B: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Llama 3.1 8B Instruct: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Ministral 3 8B: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Mistral NeMo 12B: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- GR_CHIRP_001 / Mistral Small 3.2 24B Instruct: failed_fields=chirp_mass_msun;each_mass_msun;total_mass_msun error_tags=chirp_mass_msun:MISMATCH;each_mass_msun:MISMATCH;total_mass_msun:MISMATCH
- QFT_YUKAWA_001 / Mistral NeMo 12B: failed_fields=nonreduced_fm error_tags=nonreduced_fm:MISMATCH
- QM_RT_001 / Gemma 3 12B IT: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- QM_RT_001 / Gemma 3 27B IT: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- QM_RT_001 / Granite 4.1 8B: failed_fields=energy_unit_ev;first_resonance_ev;n_lowest error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH;n_lowest:MISMATCH
- QM_RT_001 / Llama 3.1 8B Instruct: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- QM_RT_001 / Ministral 3 8B: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- QM_RT_001 / Mistral NeMo 12B: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- QM_RT_001 / Mistral Small 3.2 24B Instruct: failed_fields=energy_unit_ev;first_resonance_ev error_tags=energy_unit_ev:MISMATCH;first_resonance_ev:MISMATCH
- STAT_NEGT_001 / Llama 3.1 8B Instruct: failed_fields=abs_temperature_K;temperature_K error_tags=abs_temperature_K:MISMATCH;temperature_K:MISMATCH
- STAT_NEGT_001 / Mistral NeMo 12B: failed_fields=abs_temperature_K;temperature_K error_tags=abs_temperature_K:MISMATCH;temperature_K:MISMATCH

```
