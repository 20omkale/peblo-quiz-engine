# Peblo Smart Quiz Engine

AI-powered backend that converts educational PDFs into adaptive quizzes.

This project was built for the **Peblo AI Backend Engineer Challenge**.

---

# Overview

The system ingests educational PDF content and automatically generates quiz questions using an LLM.

Main features:

- PDF ingestion
- automatic quiz generation
- MCQ question format
- difficulty classification
- student answer submission
- adaptive learning difficulty

---

# System Flow

PDF → Text Extraction → Chunking → LLM Question Generation → Database → API → Adaptive Quiz

---

# Tech Stack

Backend
- Python
- FastAPI

Database
- SQLite
- SQLAlchemy

LLM
- Groq (Llama 3)

PDF Processing
- PyMuPDF

Embeddings
- sentence-transformers

---

# Setup

## Install dependencies

pip install -r requirements.txt

---

## Configure environment

Create `.env`

GROQ_API_KEY=your_api_key_here

---

## Run server

uvicorn app.main:app --reload

---

# API Documentation

After starting the server open:

http://127.0.0.1:8000/docs

---

# API Endpoints

POST /ingest  
Upload PDF and extract text.

POST /generate-quiz  
Generate quiz questions using LLM.

GET /quiz  
Retrieve generated questions.

POST /submit-answer  
Submit student answer.

---

# Example Question

{
 "question": "How many sides does a triangle have?",
 "options": ["2","3","4","5"],
 "answer": "3",
 "difficulty": "easy"
}

---

# Adaptive Difficulty

Correct answer → difficulty increases  
Incorrect answer → difficulty decreases

---

# Demo

## Demo Video

Watch the demo here:

https://www.loom.com/share/12108ccdd1e44253adfc11868e5fede6

---

# License

Created for the Peblo AI Backend Engineer Challenge.

---

## Project Structure
                    ┌──────────────────────────┐
                    │   Educational PDFs       │
                    │  (Peblo sample content)  │
                    └─────────────┬────────────┘
                                  │
                                  ▼
                      ┌─────────────────────┐
                      │  Content Ingestion  │
                      │  POST /ingest       │
                      └──────────┬──────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ PDF Text Extraction     │
                    │ (PyMuPDF)               │
                    └──────────┬──────────────┘
                               │
                               ▼
                     ┌─────────────────────┐
                     │ Text Chunking       │
                     │ chunk_size = 500    │
                     └──────────┬──────────┘
                                │
                                ▼
                    ┌─────────────────────────┐
                    │ Structured Storage      │
                    │ SQLite / SQLAlchemy     │
                    │                         │
                    │ tables:                 │
                    │ - sources               │
                    │ - chunks                │
                    │ - questions             │
                    │ - student_answers       │
                    └──────────┬──────────────┘
                               │
                               ▼
                     ┌──────────────────────┐
                     │ LLM Quiz Generator   │
                     │ (Groq Llama-3)       │
                     │ POST /generate-quiz  │
                     └──────────┬───────────┘
                                │
                                ▼
                    ┌─────────────────────────┐
                    │ Question Validation     │
                    │                         │
                    │ - JSON parsing          │
                    │ - duplicate detection   │
                    │ - difficulty classifier │
                    └──────────┬──────────────┘
                               │
                               ▼
                    ┌─────────────────────────┐
                    │ Quiz Retrieval API      │
                    │ GET /quiz               │
                    │                         │
                    │ filters:                │
                    │ - difficulty            │
                    │ - semantic query        │
                    └──────────┬──────────────┘
                               │
                               ▼
                   ┌──────────────────────────┐
                   │ Student Interaction      │
                   │ POST /submit-answer     │
                   └──────────┬───────────────┘
                              │
                              ▼
                  ┌────────────────────────────┐
                  │ Adaptive Difficulty Engine │
                  │                            │
                  │ correct → harder           │
                  │ incorrect → easier         │
                  └────────────────────────────┘
