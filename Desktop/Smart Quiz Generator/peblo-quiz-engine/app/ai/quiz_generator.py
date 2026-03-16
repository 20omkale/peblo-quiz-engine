import os
import json
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_questions(chunk_text: str):

    prompt = f"""
You are an educational quiz generator.

Generate quiz questions STRICTLY based on the provided content.

Rules:
- Only use information from the content
- Do not invent information
- Create 3 MCQ questions
- Each question must have exactly 4 options
- Return ONLY valid JSON

Format:

[
{{
"question": "...",
"type": "MCQ",
"options": ["option1","option2","option3","option4"],
"answer": "correct option",
"difficulty": "easy"
}}
]

Content:
{chunk_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    content = response.choices[0].message.content

    try:
        start = content.index("[")
        end = content.rindex("]") + 1
        clean_json = content[start:end]

        questions = json.loads(clean_json)
        return questions

    except Exception:
        return []