import re
import spacy
from pylatexenc.latex2text import LatexNodes2Text
from sympy import sympify, SympifyError


def make_nlp():
    nlp = spacy.blank("en")
    nlp.add_pipe("sentencizer")
    return nlp


def extract_math_candidates(sentence):
    candidates = re.findall(r"\$[^$]+\$|\\\(|\\\[|[A-Za-z0-9_]+\s*=\s*[^\s]+", sentence)
    return [c.strip() for c in candidates if c.strip()]


def is_latex_parseable(candidate):
    try:
        LatexNodes2Text().latex_to_text(candidate)
        return True
    except Exception:
        return False


def is_sympy_parseable(candidate):
    try:
        sympify(candidate)
        return True
    except (SympifyError, TypeError, ValueError):
        return False


def looks_like_calculation(sentence):
    candidates = extract_math_candidates(sentence)
    if not candidates:
        return False
    return any(is_latex_parseable(c) or is_sympy_parseable(c) for c in candidates)


def split_reasoning_and_calculation(text):
    nlp = make_nlp()
    reasoning_parts = []
    calculation_parts = []

    for sentence in nlp(text).sents:
        chunk = sentence.text.strip()
        if not chunk:
            continue
        if looks_like_calculation(chunk):
            calculation_parts.append(chunk)
        else:
            reasoning_parts.append(chunk)

    return " ".join(reasoning_parts), " ".join(calculation_parts)
