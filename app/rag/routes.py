"""Chat Bot API routes."""
from fastapi import APIRouter
from app.rag.retriever import retrieve_chunks
from app.rag.generator import generate_answer

router = APIRouter(prefix="/chat", tags=["RAG"])


@router.post("/")
def chat(query: str):
    chunks = retrieve_chunks(query)
    answer = generate_answer(query, chunks)

    return {
        "query": query,
        "retrieved_chunks": chunks,
        "answer": answer
    }
