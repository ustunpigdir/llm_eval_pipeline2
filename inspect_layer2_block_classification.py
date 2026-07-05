import re
import sqlite3
from pathlib import Path

from markdown_it import MarkdownIt


DB_PATH = Path(__file__).resolve().parent / "learning.db"


def shorten(text, limit=300):
    if text is None:
        return ""
    text = " ".join(str(text).split())
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


def collect_inline_text(token):
    if token is None:
        return ""
    if token.type == "text":
        return token.content or ""
    if token.type in {"softbreak", "hardbreak"}:
        return "\n"
    if token.type == "code_inline":
        return token.content or ""
    if token.type == "code_block":
        return token.content or ""
    if getattr(token, "children", None):
        return "".join(collect_inline_text(child) for child in token.children)
    return token.content or ""


def extract_text_blocks(text):
    parser = MarkdownIt()
    tokens = parser.parse(text)
    blocks = []
    index = 0

    while index < len(tokens):
        token = tokens[index]

        if token.type == "paragraph_open":
            parts = []
            cursor = index + 1
            while cursor < len(tokens) and tokens[cursor].type != "paragraph_close":
                if tokens[cursor].type == "inline":
                    parts.append(collect_inline_text(tokens[cursor]))
                cursor += 1
            combined = " ".join(part.strip() for part in parts if part and part.strip())
            if combined:
                blocks.append(("paragraph", combined))
            index = cursor + 1
            continue

        if token.type == "ordered_list_open":
            cursor = index + 1
            while cursor < len(tokens) and tokens[cursor].type != "ordered_list_close":
                if tokens[cursor].type == "list_item_open":
                    item_parts = []
                    inner = cursor + 1
                    while inner < len(tokens) and tokens[inner].type != "list_item_close":
                        if tokens[inner].type == "inline":
                            item_parts.append(collect_inline_text(tokens[inner]))
                        inner += 1
                    combined = " ".join(part.strip() for part in item_parts if part and part.strip())
                    if combined:
                        blocks.append(("ordered_list_item", combined))
                    cursor = inner + 1
                    continue
                cursor += 1
            index = cursor + 1
            continue

        if token.type == "bullet_list_open":
            cursor = index + 1
            while cursor < len(tokens) and tokens[cursor].type != "bullet_list_close":
                if tokens[cursor].type == "list_item_open":
                    item_parts = []
                    inner = cursor + 1
                    while inner < len(tokens) and tokens[inner].type != "list_item_close":
                        if tokens[inner].type == "inline":
                            item_parts.append(collect_inline_text(tokens[inner]))
                        inner += 1
                    combined = " ".join(part.strip() for part in item_parts if part and part.strip())
                    if combined:
                        blocks.append(("bullet_list_item", combined))
                    cursor = inner + 1
                    continue
                cursor += 1
            index = cursor + 1
            continue

        index += 1

    return blocks


def classify_block(text):
    cleaned = " ".join(str(text).split())
    if not cleaned:
        return "unknown"

    if re.match(r"^\s*(?:\d+[.)]|[A-Za-z][A-Za-z0-9 /&()\-]{0,40})\s*(?::|$)", cleaned):
        return "heading"

    if re.match(r"^\s*(?:\d+[.)])\s+\S+", cleaned):
        words = re.findall(r"[A-Za-z]+", cleaned)
        if len(words) <= 8:
            return "heading"

    if cleaned.endswith(":") and len(re.findall(r"[A-Za-z]+", cleaned)) <= 8:
        return "heading"

    math_markers = sum(1 for marker in ["$", "\\(", "\\[", "\\begin", "\\frac", "\\sqrt", "^", "_", "=", "+", "-", "*", "/"] if marker in cleaned)
    math_symbols = len(re.findall(r"[=+\-*/^_{}\\%]", cleaned))
    word_count = len(re.findall(r"[A-Za-z]+", cleaned))

    if re.search(r"\\\[|\\begin|\\end", cleaned) or (math_markers >= 3 and word_count <= 8):
        return "calculation"

    if ("$" in cleaned and word_count >= 4 and math_symbols >= 4) or ("$" in cleaned and word_count >= 8):
        return "mixed"

    return "reasoning"


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, model_name, answer
        FROM questions
        WHERE answer IS NOT NULL AND answer != ''
        LIMIT 5
        """
    )
    rows = cursor.fetchall()

    for row in rows:
        print("ID:", row["id"])
        print("Model:", row["model_name"])
        blocks = extract_text_blocks(row["answer"])
        for index, (block_type, block_text) in enumerate(blocks, start=1):
            label = classify_block(block_text)
            print(f"Block {index}: original={block_type} label={label} text={shorten(block_text)}")
        print("---")

    conn.close()


if __name__ == "__main__":
    main()
