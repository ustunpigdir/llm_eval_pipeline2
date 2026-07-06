import re

def normalize_answer(answer):
    if not answer:
        return ""
    answer = answer.strip()
    answer = re.sub(r"\s+", " ", answer)
    return answer
