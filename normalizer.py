import re

def normalize_answer(answer):
    if answer is "":
        return ""
    answer = answer.strip()
    answer = re.sub(r"\s+", " ", answer)
    return answer
