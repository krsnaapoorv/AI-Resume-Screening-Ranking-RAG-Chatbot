"""Vector database client and operations."""

import faiss
import numpy as np


class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)

        # 🔹 For RAG
        self.text_chunks = []

        # 🔹 For Ranking
        self.resume_embeddings = []
        self.resume_ids = []

    # ---------------------------
    # 🔹 Chunk Storage (RAG)
    # ---------------------------
    def add(self, embeddings, chunks):
        self.index.add(np.array(embeddings))
        self.text_chunks.extend(chunks)

    # ---------------------------
    # 🔹 Resume Storage (Ranking)
    # ---------------------------
    def add_resume(self, resume_id, embedding):
        self.resume_ids.append(resume_id)
        self.resume_embeddings.append(np.array(embedding))

    # ---------------------------
    # 🔹 Search (RAG)
    # ---------------------------
    def search(self, query_embedding, k=3):
        distances, indices = self.index.search(
            np.array([query_embedding]), k
        )
        return [self.text_chunks[i] for i in indices[0]]
