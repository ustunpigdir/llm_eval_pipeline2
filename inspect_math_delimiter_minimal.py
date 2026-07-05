from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin
from mdit_py_plugins.texmath import texmath_plugin


CASES = {
    "A": r"\[\begin{aligned} x &= 1 \end{aligned}\]",
    "B": r"\[ \begin{aligned} x &= 1 \end{aligned} \]",
    "C": r"$$\begin{aligned} x &= 1 \end{aligned}$$",
    "D": r"$x = 1$",
}


def print_tokens(label, parser, text):
    print(f"parser={label} case={text}")
    tokens = parser.parse(text)
    for idx, token in enumerate(tokens):
        content = getattr(token, "content", "") or ""
        markup = getattr(token, "markup", "") or ""
        print(
            f"  top[{idx}] type={getattr(token, 'type', '')} content={content!r} markup={markup!r}"
        )
        children = getattr(token, "children", None) or []
        for child_idx, child in enumerate(children):
            child_content = getattr(child, "content", "") or ""
            child_markup = getattr(child, "markup", "") or ""
            print(
                f"    child[{child_idx}] type={getattr(child, 'type', '')} content={child_content!r} markup={child_markup!r}"
            )
    print("---")


if __name__ == "__main__":
    parsers = [
        ("dollarmath", MarkdownIt().use(dollarmath_plugin)),
        ("texmath", MarkdownIt().use(texmath_plugin)),
    ]
    for parser_name, parser in parsers:
        for label, text in CASES.items():
            print_tokens(parser_name, parser, text)
