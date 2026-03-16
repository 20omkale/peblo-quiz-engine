# API Reference

Base URL

http://127.0.0.1:8000

---

# POST /ingest

Uploads a PDF and extracts content.

Response

{
 "message": "PDF ingested successfully",
 "chunks_created": 10
}

---

# POST /generate-quiz

Generates quiz questions from stored content.

Response

{
 "message": "Quiz generated",
 "questions_created": 20
}

---

# GET /quiz

Retrieve quiz questions.

Optional parameter:

difficulty

Example

GET /quiz?difficulty=easy

Response

[
{
 "id":1,
 "question":"How many sides does a triangle have?",
 "options":["2","3","4","5"],
 "answer":"3",
 "difficulty":"easy"
}
]

---

# POST /submit-answer

Submit a student answer.

Parameters

student_id  
question_id  
selected_answer  

Example

student_id=S001  
question_id=1  
selected_answer=3  

Response

{
 "correct": true,
 "next_difficulty": "medium"
}