"""RAG retrieval from vector store."""
from app.db.store import get_vector_store
from app.ingestion.embedding import model


def retrieve_chunks(query: str, k=3):
    vector_store = get_vector_store()

    if vector_store is None:
        print("❌ Vector store is None")
        return []

    print("Total chunks:", len(vector_store.text_chunks))

    query_embedding = model.encode([query])[0]
    results = vector_store.search(query_embedding, k=k)

    return results
