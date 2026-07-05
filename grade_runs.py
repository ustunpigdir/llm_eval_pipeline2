#!/usr/bin/env python3
"""
grade_runs.py  --  deterministic final-answer grader (final block only).

Per gold field, against a model run's FINAL ANSWER block:
  MATCH      the model's value equals the gold value within the scenario tolerance
             (the value is evaluated first: plain number OR symbolic pi/2, 1/sqrt2,
             \\frac{5}{6}, 180\\sqrt2-360, ... via symbolic_eval).
  MISMATCH   the model gave a value for the field, it evaluates, but != gold.
  REVIEW     the model gave a value but it can't be evaluated to a number
             (a free variable / unit / ln / trig) -> a human decides.
  NOT_FOUND  the field is absent from the model's final block.

No intermediate-step / body search. No per-scenario fingerprints. No LLM.
Numbers are compared within the scenario's relative tolerance (models round).

Usage:
  python3 grade_runs.py --db grade.db --gold "/path/Scenarios to Run" --report --csv out.csv
"""
from __future__ import annotations
import argparse, glob, json, os, sqlite3
from collections import Counter, defaultdict
from symbolic_eval import eval_value


def near(x, g, rel):
    tol = abs(g) * rel if g != 0 else rel
    return abs(x - g) <= max(tol, 1e-12)


def load_gold(gold_dir):
    gold = {}
    for path in glob.glob(os.path.join(gold_dir, "*.json")):
        if os.path.basename(path).startswith("gold_normalized"):
            continue
        try:
            data = json.load(open(path))
        except Exception:
            continue
        if not isinstance(data, list):
            continue
        for s in data:
            g = s.get("gold", {})
            if "expected_values" not in g:
                continue
            gold[s["id"]] = {"fields": [(v["name"], v["value"]) for v in g["expected_values"]],
                             "rel": float(g.get("tolerance", 0.01))}
    return gold


def field_index(gold):
    idx = defaultdict(set)
    for sid, g in gold.items():
        for name, _ in g["fields"]:
            idx[name].add(sid)
    return idx


def match_scenario(run_fields, gold, idx):
    votes = Counter()
    for f in run_fields:
        for sid in idx.get(f, ()):
            votes[sid] += 1
    if not votes:
        return None, 0
    best = max(votes.items(),
               key=lambda kv: (kv[1], -abs(len(gold[kv[0]]["fields"]) - len(run_fields))))
    return best[0], best[1]


def grade(con, gold):
    cur = con.cursor()
    idx = field_index(gold)
    run_raw = defaultdict(dict)                         # run -> {field: raw_value}
    for rid, fname, raw in cur.execute(
        "SELECT run_id, field_name, raw_value FROM final_answer_values"):
        run_raw[rid][fname] = raw
    models = dict(cur.execute("SELECT id, model_name FROM questions"))

    rows, per_state = [], Counter()
    matched = unmatched = 0
    for rid, fields in run_raw.items():
        sid, overlap = match_scenario(set(fields), gold, idx)
        if sid is None or overlap < 2:
            unmatched += 1
            continue
        matched += 1
        rel = gold[sid]["rel"]
        for gname, gv in gold[sid]["fields"]:
            if gname not in fields:
                state, note, mv = "NOT_FOUND", "-", None
            else:
                v, note = eval_value(fields[gname])
                if v is None:
                    state, mv = "REVIEW", None
                elif near(v, gv, rel):
                    state, mv = "MATCH", v
                else:
                    state, mv = "MISMATCH", v
            per_state[state] += 1
            rows.append((rid, models.get(rid, "?"), sid, gname, gv,
                         fields.get(gname), mv, state, note))
    return rows, per_state, matched, unmatched


def report(rows, per_state, matched, unmatched):
    total = sum(per_state.values())
    print(f"\nruns matched to a scenario: {matched}  (unmatched: {unmatched})")
    print(f"field verdicts: {total}")
    for st in ("MATCH", "MISMATCH", "REVIEW", "NOT_FOUND"):
        n = per_state.get(st, 0)
        print(f"   {st:10} {n:5}  ({100*n/total:.1f}%)" if total else f"   {st}")
    print("\n  sample MISMATCH (evaluated model value vs gold):")
    for r in [x for x in rows if x[7] == "MISMATCH"][:8]:
        print(f"    run {r[0]:>3} {r[2]:<16} {r[3]:<22} model={r[5]!r} -> {r[6]}  gold={r[4]}")
    print("\n  sample REVIEW (couldn't evaluate the model's value):")
    for r in [x for x in rows if x[7] == "REVIEW"][:6]:
        print(f"    run {r[0]:>3} {r[2]:<16} {r[3]:<22} model={r[5]!r} [{r[8]}]")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="learning.db")
    ap.add_argument("--gold", required=True)
    ap.add_argument("--csv")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    gold = load_gold(a.gold)
    print(f"loaded gold: {len(gold)} scenarios, {sum(len(g['fields']) for g in gold.values())} fields")
    con = sqlite3.connect(a.db)
    rows, per_state, matched, unmatched = grade(con, gold)
    if a.report:
        report(rows, per_state, matched, unmatched)
    if a.csv:
        import csv
        with open(a.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["run_id", "model", "scenario_id", "field", "gold_value",
                        "model_raw", "model_eval", "verdict", "note"])
            w.writerows(rows)
        print(f"\nwrote {len(rows)} rows -> {a.csv}")
    con.close()


if __name__ == "__main__":
    main()
