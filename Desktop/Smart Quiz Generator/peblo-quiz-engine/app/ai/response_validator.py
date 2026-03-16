def validate_questions(data):

    valid_questions = []

    for q in data:

        if "question" not in q:
            continue

        if "answer" not in q:
            continue

        if len(q["question"]) < 10:
            continue

        valid_questions.append(q)

    return valid_questions