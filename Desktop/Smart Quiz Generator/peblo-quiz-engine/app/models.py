from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class ContentChunk(Base):
    __tablename__ = "content_chunks"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    chunk_id = Column(Integer, ForeignKey("content_chunks.id"))

    question = Column(String)
    options = Column(String)
    answer = Column(String)
    difficulty = Column(String)
    type = Column(String)


class StudentAnswer(Base):
    __tablename__ = "student_answers"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(String)
    question_id = Column(Integer)
    selected_answer = Column(String)
    correct = Column(String)