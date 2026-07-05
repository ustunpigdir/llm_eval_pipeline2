#!/usr/bin/env python3
"""Generate the structured-prompt v2 clean-run iPad review PDF."""

from __future__ import annotations

import csv
import html
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


BASE = Path("outputs/structured_prompt_pilot_v2/pdf_review_source")
OUT_DIR = Path("outputs/structured_prompt_pilot_v2/pdf_review")
HTML_PATH = OUT_DIR / "structured_prompt_v2_clean_review_ipad.html"
PDF_PATH = OUT_DIR / "structured_prompt_v2_clean_review_ipad.pdf"
MANIFEST_PATH = OUT_DIR / "pdf_generation_manifest.json"
PROMPT_MODE = "structured_prompt_pilot_v2"
NEMOTRON = "NVIDIA Nemotron 3 Nano 30B-A3B"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_name(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip()).casefold()


def extract_question(prompt: str) -> str:
    marker = "Use the following answer structure."
    if marker in prompt:
        prompt = prompt.split(marker, 1)[0]
    prefix = "Solve the following scenario."
    prompt = prompt.strip()
    if prompt.startswith(prefix):
        prompt = prompt[len(prefix) :].strip()
    return prompt


def parse_worked_sections() -> dict[str, str]:
    sections: dict[str, str] = {}
    heading_re = re.compile(r"^##\s+([A-Z0-9_]+)\s+.*$", re.MULTILINE)
    for path in sorted((BASE / "worked_solutions").glob("worked_solutions_batch*.md")):
        text = path.read_text(encoding="utf-8")
        matches = list(heading_re.finditer(text))
        for idx, match in enumerate(matches):
            start = match.start()
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
            sections[match.group(1)] = text[start:end].strip()
    return sections


def extract_gold_fields(worked_section: str) -> list[tuple[str, str]]:
    fields: list[tuple[str, str]] = []
    block_match = re.search(
        r"\\begin\{aligned\}(.*?)\\end\{aligned\}",
        worked_section,
        flags=re.DOTALL,
    )
    if not block_match:
        return fields
    for line in block_match.group(1).splitlines():
        line = line.strip().rstrip("\\").strip()
        match = re.search(r"\\mathrm\{([^}]+)\}\s*&=\s*(.+)$", line)
        if match:
            fields.append((match.group(1).replace(r"\_", "_"), match.group(2).strip()))
    return fields


def simple_markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    in_code = False
    para: list[str] = []

    def flush_para() -> None:
        if para:
            text = " ".join(para)
            text = html.escape(text)
            text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
            out.append(f"<p>{text}</p>")
            para.clear()

    for line in lines:
        if line.strip().startswith("```"):
            flush_para()
            if in_code:
                out.append("</pre>")
            else:
                out.append("<pre>")
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        if not line.strip():
            flush_para()
            continue
        if line.startswith("## "):
            flush_para()
            out.append(f"<h3>{html.escape(line[3:].strip())}</h3>")
        elif line.startswith("**") and line.endswith("**"):
            flush_para()
            out.append(f"<h4>{html.escape(line.strip('*').strip())}</h4>")
        elif re.match(r"^\d+\.\s+", line):
            flush_para()
            text = html.escape(line)
            text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
            out.append(f"<p class=\"step\">{text}</p>")
        elif line.startswith("- "):
            flush_para()
            text = html.escape(line[2:].strip())
            text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
            out.append(f"<p class=\"bullet\">• {text}</p>")
        else:
            para.append(line.strip())
    flush_para()
    if in_code:
        out.append("</pre>")
    return "\n".join(out)


def parse_normalized_answer(raw: str) -> dict[str, str]:
    if not raw:
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    return {str(k): str(v) for k, v in data.items()}


def numeric_delta(expected: str, actual: str) -> str:
    try:
        exp = float(str(expected).replace(",", ""))
        act = float(str(actual).replace(",", ""))
    except (TypeError, ValueError):
        return ""
    return f"{act - exp:.6g}"


def comparison_rows(auto_row: dict, gold_fields: list[tuple[str, str]]) -> str:
    model_values = parse_normalized_answer(auto_row.get("normalized_final_answer", ""))
    failed = {
        item.strip()
        for item in str(auto_row.get("failed_fields", "")).split(";")
        if item.strip()
    }
    if not failed:
        failed = {
            item.strip()
            for item in str(auto_row.get("failed_fields", "")).split(",")
            if item.strip()
        }
    rows = []
    for field, expected in gold_fields:
        actual = model_values.get(field, "")
        match = "PASS" if field not in failed and actual != "" else "FAIL"
        if auto_row.get("deterministic_grade") == "PASS" and actual != "":
            match = "PASS"
        delta = numeric_delta(expected, actual)
        css = " class=\"failed\"" if match == "FAIL" else ""
        rows.append(
            "<tr{css}><td>{field}</td><td>{expected}</td><td>{actual}</td>"
            "<td>{match}</td><td>{delta}</td></tr>".format(
                css=css,
                field=html.escape(field),
                expected=html.escape(expected),
                actual=html.escape(actual),
                match=match,
                delta=html.escape(delta),
            )
        )
    return "\n".join(rows)


def suggested_labels(auto_row: dict) -> str:
    labels = []
    for key in ("error_tags", "primary_failure_mode", "suggested_error_labels"):
        value = str(auto_row.get(key, "") or "").strip()
        if value and value.lower() not in {"none", "nan"}:
            labels.append(value)
    if labels:
        return "; ".join(dict.fromkeys(labels))
    if auto_row.get("deterministic_grade") == "PASS":
        return "none"
    return "manual_review_needed"


def pdf_page_count(path: Path) -> int | None:
    data = path.read_bytes()
    matches = re.findall(rb"/Type\s*/Page\b", data)
    return len(matches) if matches else None


def build_records() -> tuple[list[dict], dict]:
    review_rows = load_json(BASE / "review_layer/review_layer_v1.json")
    autograde_rows = load_json(BASE / "autograde/structured_prompt_v2_clean_autograde.json")
    run_rows = load_json(BASE / "runs/structured_prompt_pilot_v2_runs.json")
    worked_sections = parse_worked_sections()

    clean_review = [row for row in review_rows if row.get("review_status") == "CLEAN"]
    nemotron_in_clean = [row for row in clean_review if row.get("model_name") == NEMOTRON]
    auto_by_run = {row["output_path_or_run_id"]: row for row in autograde_rows}
    run_by_id = {row["run_id"]: row for row in run_rows}

    records = []
    missing = []
    for row in clean_review:
        run_id = row["output_path_or_run_id"]
        auto = auto_by_run.get(run_id)
        run = run_by_id.get(run_id)
        if not auto or not run:
            missing.append({"scenario_id": row.get("scenario_id"), "model_name": row.get("model_name"), "run_id": run_id})
            continue
        scenario_id = row["scenario_id"]
        worked = worked_sections.get(scenario_id, "")
        question = extract_question(run.get("prompt", ""))
        response = run.get("response", "")
        gold_fields = extract_gold_fields(worked)
        records.append(
            {
                "review": row,
                "autograde": auto,
                "run": run,
                "scenario_id": scenario_id,
                "model_name": row["model_name"],
                "run_id": run_id,
                "question": question,
                "response": response,
                "worked": worked,
                "gold_fields": gold_fields,
            }
        )

    validation = {
        "clean_rows_from_review_layer": len(clean_review),
        "autograde_clean_rows": len(autograde_rows),
        "raw_responses_joined": len(records),
        "pages_to_generate": len(records),
        "nemotron_rows_in_main_pdf": len(nemotron_in_clean),
        "missing_join_records": missing,
        "missing_required_content": [],
    }
    for record in records:
        missing_bits = []
        for key in ("scenario_id", "model_name", "question", "response", "worked"):
            if not record.get(key):
                missing_bits.append(key)
        if not record.get("autograde", {}).get("deterministic_grade"):
            missing_bits.append("grade")
        if not record.get("gold_fields"):
            missing_bits.append("numeric_comparison")
        if missing_bits:
            validation["missing_required_content"].append(
                {
                    "scenario_id": record["scenario_id"],
                    "model_name": record["model_name"],
                    "run_id": record["run_id"],
                    "missing": missing_bits,
                }
            )

    expected = {
        "clean_rows_from_review_layer": 64,
        "autograde_clean_rows": 64,
        "raw_responses_joined": 64,
        "pages_to_generate": 64,
        "nemotron_rows_in_main_pdf": 0,
    }
    failures = {
        key: {"expected": value, "actual": validation[key]}
        for key, value in expected.items()
        if validation[key] != value
    }
    if validation["missing_join_records"]:
        failures["missing_join_records"] = validation["missing_join_records"]
    if validation["missing_required_content"]:
        failures["missing_required_content"] = validation["missing_required_content"]
    if failures:
        raise RuntimeError("PDF validation failed:\n" + json.dumps(failures, indent=2))

    records.sort(key=lambda r: (r["scenario_id"], normalize_name(r["model_name"])))
    return records, validation


def render_html(records: list[dict], validation: dict) -> str:
    suspicious = {"GR_ISCO_001", "SR_ROCKET_001"}
    weak_model = "Mistral NeMo 12B"
    toc_rows = []
    for idx, record in enumerate(records, start=1):
        grade = record["autograde"]["deterministic_grade"]
        marks = []
        if record["scenario_id"] in suspicious:
            marks.append("suspicious scenario")
        if weak_model in record["model_name"]:
            marks.append("low-pass model")
        if marks:
            toc_rows.append(
                f"<tr><td>{idx}</td><td>{html.escape(record['scenario_id'])}</td>"
                f"<td>{html.escape(record['model_name'])}</td><td>{grade}</td>"
                f"<td>{html.escape('; '.join(marks))}</td></tr>"
            )

    pages = []
    total = len(records)
    for idx, record in enumerate(records, start=1):
        auto = record["autograde"]
        grade = auto["deterministic_grade"]
        grade_class = "pass" if grade == "PASS" else "fail"
        failed_fields = str(auto.get("failed_fields") or "").strip() or "none"
        pages.append(
            f"""
<section class="run-page">
  <header class="run-header {grade_class}">
    <div><strong>Scenario:</strong> {html.escape(record['scenario_id'])}</div>
    <div><strong>Model:</strong> {html.escape(record['model_name'])}</div>
    <div><strong>Grade:</strong> {html.escape(grade)}</div>
    <div><strong>Prompt mode:</strong> {PROMPT_MODE}</div>
    <div><strong>Page:</strong> {idx}/{total}</div>
  </header>
  <main class="grid">
    <section class="panel question">
      <h2>Question</h2>
      <pre>{html.escape(record['question'])}</pre>
    </section>
    <section class="panel gold">
      <h2>Worked Gold Answer</h2>
      {simple_markdown_to_html(record['worked'])}
    </section>
    <section class="panel model-response">
      <h2>Full Raw Model Response</h2>
      <pre>{html.escape(record['response'])}</pre>
    </section>
    <section class="panel comparison">
      <h2>Numeric Comparison</h2>
      <table>
        <thead><tr><th>field_name</th><th>expected</th><th>model_value</th><th>match</th><th>delta_or_status</th></tr></thead>
        <tbody>{comparison_rows(auto, record['gold_fields'])}</tbody>
      </table>
      <div class="labels"><strong>Suggested error labels:</strong> {html.escape(suggested_labels(auto))}</div>
      <div class="labels"><strong>Failed fields:</strong> {html.escape(failed_fields)}</div>
      <div class="labels"><strong>Run ID:</strong> {html.escape(record['run_id'])}</div>
    </section>
  </main>
</section>
"""
        )

    toc = "\n".join(toc_rows) or "<tr><td colspan=\"5\">No suspicious entries marked.</td></tr>"
    return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Structured Prompt Pilot v2 Clean Review</title>
<style>
@page {{ size: letter landscape; margin: 0.25in; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Arial, Helvetica, sans-serif; font-size: 8.2pt; color: #111; }}
.summary-page, .run-page {{ page-break-after: always; min-height: 7.95in; }}
.summary-page {{ padding: 0.18in; }}
h1 {{ font-size: 18pt; margin: 0 0 0.15in; }}
h2 {{ font-size: 9.2pt; margin: 0 0 0.04in; border-bottom: 1px solid #888; }}
h3 {{ font-size: 8.2pt; margin: 0.04in 0; }}
h4 {{ font-size: 7.9pt; margin: 0.04in 0 0.02in; }}
p {{ margin: 0 0 0.035in; line-height: 1.18; }}
p.step, p.bullet {{ margin-left: 0.05in; }}
pre {{ margin: 0; white-space: pre-wrap; word-break: break-word; font-family: Menlo, Consolas, monospace; font-size: 6.1pt; line-height: 1.08; }}
.run-header {{ display: grid; grid-template-columns: 1fr 2.4fr 0.55fr 1.15fr 0.55fr; gap: 0.05in; padding: 0.045in 0.06in; border: 1px solid #777; margin-bottom: 0.045in; font-size: 8pt; }}
.run-header.pass {{ background: #e4f4e7; }}
.run-header.fail {{ background: #f8dddd; }}
.grid {{ display: grid; grid-template-columns: 1.05fr 1.25fr 1.35fr; grid-template-rows: 2.15in 5.24in; gap: 0.045in; }}
.panel {{ border: 1px solid #999; padding: 0.045in; overflow: hidden; }}
.question {{ grid-column: 1 / 2; grid-row: 1 / 2; }}
.gold {{ grid-column: 2 / 3; grid-row: 1 / 3; }}
.model-response {{ grid-column: 3 / 4; grid-row: 1 / 3; }}
.comparison {{ grid-column: 1 / 2; grid-row: 2 / 3; }}
.gold, .model-response {{ font-size: 6.45pt; line-height: 1.08; }}
.gold pre {{ font-size: 5.8pt; }}
.model-response pre {{ font-size: 6.05pt; }}
table {{ width: 100%; border-collapse: collapse; font-size: 6.4pt; }}
th, td {{ border: 1px solid #aaa; padding: 0.018in; text-align: left; vertical-align: top; }}
th {{ background: #efefef; }}
tr.failed td {{ background: #ffe5e5; }}
.labels {{ margin-top: 0.045in; font-size: 6.6pt; }}
.summary-table {{ width: 100%; font-size: 8.5pt; margin-top: 0.15in; }}
.summary-table th, .summary-table td {{ padding: 0.045in; }}
</style>
</head>
<body>
<section class="summary-page">
  <h1>Structured Prompt Pilot v2 Clean Review</h1>
  <p><strong>Scope:</strong> 64 CLEAN structured-prompt pilot v2 runs. Nemotron REVIEW rows are excluded.</p>
  <p><strong>Raw responses:</strong> Full raw model responses from <code>structured_prompt_pilot_v2_runs.json</code> are included, not extracted-final-answer substitutes.</p>
  <p><strong>Validation:</strong> clean_rows_from_review_layer={validation['clean_rows_from_review_layer']}; autograde_clean_rows={validation['autograde_clean_rows']}; raw_responses_joined={validation['raw_responses_joined']}; pages_to_generate={validation['pages_to_generate']}; nemotron_rows_in_main_pdf={validation['nemotron_rows_in_main_pdf']}.</p>
  <h2>Suspicious / Easy-Find Entries</h2>
  <table class="summary-table">
    <thead><tr><th>Run page</th><th>Scenario</th><th>Model</th><th>Grade</th><th>Marker</th></tr></thead>
    <tbody>{toc}</tbody>
  </table>
</section>
{''.join(pages)}
</body>
</html>
"""


def generate_pdf_with_chrome(html_path: Path, pdf_path: Path) -> str:
    chrome = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    if not chrome.exists():
        raise RuntimeError("Google Chrome not found and no Python PDF backend is installed")
    cmd = [
        str(chrome),
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={pdf_path.resolve()}",
        "--print-to-pdf-no-header",
        str(html_path.resolve()),
    ]
    subprocess.run(cmd, check=True)
    return "google_chrome_headless"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    records, validation = build_records()
    HTML_PATH.write_text(render_html(records, validation), encoding="utf-8")
    method = generate_pdf_with_chrome(HTML_PATH, PDF_PATH)
    page_count = pdf_page_count(PDF_PATH)
    manifest = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_folder": str(BASE),
        "html_path": str(HTML_PATH),
        "pdf_path": str(PDF_PATH),
        "pdf_generation_method": method,
        "page_count_detected": page_count,
        "clean_run_pages": len(records),
        "summary_pages": 1,
        "raw_model_responses_included": True,
        "nemotron_rows_excluded": True,
        "validation": validation,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
