def classify_difficulty(question):

    length = len(question.split())

    if length < 7:
        return "easy"

    if length < 12:
        return "medium"

    return "hard"