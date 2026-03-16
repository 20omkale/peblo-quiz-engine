from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


class VectorStore:

    def __init__(self):

        self.texts = []
        self.embeddings = []

    def add(self, text):

        emb = model.encode(text)

        self.texts.append(text)

        self.embeddings.append(emb)

    def search(self, query, k=3):

        if not self.texts:
            return []

        query_emb = model.encode(query)

        scores = cosine_similarity([query_emb], self.embeddings)[0]

        top_indices = np.argsort(scores)[::-1][:k]

        results = []

        for idx in top_indices:
            results.append(self.texts[idx])

        return results