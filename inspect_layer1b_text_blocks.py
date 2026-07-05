import re
import sqlite3
from pathlib import Path

from markdown_it import MarkdownIt


DB_PATH = Path(__file__).resolve().parent / "learning.db"


def normalize_extracted_block(text):
    if text is None:
        return ""
    text = str(text).strip()
    text = re.sub(r"[ \t]+", " ", text)
    text = text.replace("**", "")
    return text


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


def parse_text_blocks(text):
    parser = MarkdownIt()
    tokens = parser.parse(text)
    blocks = []
    index = 0

    while index < len(tokens):
        token = tokens[index]

        if token.type == "paragraph_open":
            block_text = []
            cursor = index + 1
            while cursor < len(tokens) and tokens[cursor].type != "paragraph_close":
                if tokens[cursor].type == "inline":
                    block_text.append(collect_inline_text(tokens[cursor]))
                cursor += 1
            combined = " ".join(part.strip() for part in block_text if part and part.strip())
            if combined:
                blocks.append(("paragraph", normalize_extracted_block(combined)))
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
                        blocks.append(("ordered_list_item", normalize_extracted_block(combined)))
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
                        blocks.append(("bullet_list_item", normalize_extracted_block(combined)))
                    cursor = inner + 1
                    continue
                cursor += 1
            index = cursor + 1
            continue

        if token.type in {"heading_open", "blockquote_open", "fence", "code_block"}:
            block_text = []
            cursor = index + 1
            while cursor < len(tokens) and tokens[cursor].type != token.type.replace("_open", "_close"):
                if tokens[cursor].type == "inline":
                    block_text.append(collect_inline_text(tokens[cursor]))
                elif tokens[cursor].content:
                    block_text.append(tokens[cursor].content)
                cursor += 1
            combined = " ".join(part.strip() for part in block_text if part and part.strip())
            if combined:
                blocks.append(("unknown", normalize_extracted_block(combined)))
            index = cursor + 1
            continue

        index += 1

    return blocks


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
        blocks = parse_text_blocks(row["answer"])
        for idx, (block_type, block_text) in enumerate(blocks, start=1):
            print(f"Block {idx}: type={block_type} text={shorten(block_text)}")
        print("---")

    conn.close()


if __name__ == "__main__":
    main()
