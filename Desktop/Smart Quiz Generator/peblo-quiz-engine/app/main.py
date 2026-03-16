from fastapi import FastAPI, UploadFile, File
from sqlalchemy.orm import Session
import shutil
import os
import json

from .database import SessionLocal, engine
from .models import Base, ContentChunk, Question, StudentAnswer
from .ingestion.pdf_ingest import ingest_pdf
from .services.quiz_pipeline import process_chunk
from .services.adaptive_logic import adjust_difficulty

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Peblo Smart Quiz Engine")


# ---------------- DB SESSION ----------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- INGEST ----------------

@app.post("/ingest")
def ingest(file: UploadFile = File(...)):

    os.makedirs("data/pdfs", exist_ok=True)

    file_path = f"data/pdfs/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = ingest_pdf(file_path)

    db = SessionLocal()

    for chunk in chunks:
        db_chunk = ContentChunk(text=chunk)
        db.add(db_chunk)

    db.commit()
    db.close()

    return {
        "message": "PDF ingested successfully",
        "chunks_created": len(chunks)
    }


# ---------------- GENERATE QUIZ ----------------

@app.post("/generate-quiz")
def generate_quiz():

    db = SessionLocal()

    chunks = db.query(ContentChunk).all()

    questions_created = 0

    for chunk in chunks:

        questions = process_chunk(chunk.text)

        for q in questions:

            db_question = Question(
                chunk_id=chunk.id,
                question=q["question"],
                options=q["options"],
                answer=q["answer"],
                difficulty=q["difficulty"],
                type=q["type"]
            )

            db.add(db_question)
            questions_created += 1

    db.commit()
    db.close()

    return {
        "message": "Quiz generated",
        "questions_created": questions_created
    }


# ---------------- GET QUIZ ----------------

@app.get("/quiz")
def get_quiz(difficulty: str = "easy"):

    db = SessionLocal()

    questions = db.query(Question).filter(
        Question.difficulty == difficulty
    ).all()

    result = []

    for q in questions:

        result.append({
            "id": q.id,
            "question": q.question,
            "options": json.loads(q.options),
            "answer": q.answer,
            "difficulty": q.difficulty,
            "type": q.type,
            "source_chunk_id": q.chunk_id
        })

    db.close()

    return result


# ---------------- SUBMIT ANSWER ----------------

@app.post("/submit-answer")
def submit_answer(student_id: str, question_id: int, selected_answer: str):

    db = SessionLocal()

    question = db.query(Question).filter(
        Question.id == question_id
    ).first()

    correct = selected_answer == question.answer

    answer = StudentAnswer(
        student_id=student_id,
        question_id=question_id,
        selected_answer=selected_answer,
        correct=str(correct)
    )

    db.add(answer)
    db.commit()

    next_difficulty = adjust_difficulty(
        question.difficulty,
        correct
    )

    db.close()

    return {
        "correct": correct,
        "next_difficulty": next_difficulty
    }


# ---------------- DEBUG CHUNKS ----------------

@app.get("/chunks")
def view_chunks():

    db = SessionLocal()

    chunks = db.query(ContentChunk).all()

    result = []

    for c in chunks:
        result.append({
            "id": c.id,
            "text": c.text[:200]
        })

    db.close()

    return result