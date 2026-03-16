# System Architecture

The Peblo Smart Quiz Engine is designed as a modular AI backend.

Pipeline:

PDF → Text Extraction → Chunking → LLM Quiz Generation → Database → API

---

# Architecture Flow

Educational PDFs

↓

PDF Ingestion

↓

Text Extraction

↓

Chunking

↓

LLM Question Generation

↓

Database Storage

↓

API Endpoints

↓

Student Answer Tracking

↓

Adaptive Difficulty

---

# Components

## PDF Ingestion

Responsible for reading educational PDFs and extracting text.

Library used: PyMuPDF

---

## Chunking

Large text is split into smaller chunks so the LLM can process them effectively.

---

## Quiz Generation

An LLM converts text chunks into structured quiz questions.

Question format:

MCQ  
True/False  
Fill in the blank

---

## Database

SQLite database stores:

content chunks  
generated questions  
student answers

---

## API Layer

FastAPI exposes REST endpoints.

POST /ingest  
POST /generate-quiz  
GET /quiz  
POST /submit-answer

---

## Adaptive Learning

Difficulty is adjusted based on performance.

correct → harder question  
incorrect → easier question