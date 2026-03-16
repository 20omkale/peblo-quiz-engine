import json
from ..ai.quiz_generator import generate_questions

def process_chunk(chunk_text):

    questions = generate_questions(chunk_text)

    clean_questions = []

    for q in questions:

        if "question" not in q or "options" not in q:
            continue

        if len(q["options"]) != 4:
            continue

        clean_questions.append({
            "question": q["question"],
            "options": json.dumps(q["options"]),
            "answer": q["answer"],
            "type": q.get("type", "MCQ"),
            "difficulty": q.get("difficulty", "easy")
        })

    return clean_questions