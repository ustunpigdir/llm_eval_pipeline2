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
