from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

existing = []

def is_duplicate(question):

    if not existing:
        existing.append(question)
        return False

    embeddings = model.encode([question] + existing)

    scores = cosine_similarity([embeddings[0]], embeddings[1:])

    for s in scores[0]:
        if s > 0.85:
            return True

    existing.append(question)
    return False