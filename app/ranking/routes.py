from fastapi import APIRouter
from app.ingestion.embedding import get_single_embedding
from app.db.store import get_vector_store
from app.ranking.ranker import rank_resumes

router = APIRouter(prefix="/ranking", tags=["Ranking"])


@router.post("/")
def rank_candidates(job_description: str):
    vector_store = get_vector_store()
    if vector_store is None or not vector_store.resume_ids:
        return {
            "ranked_candidates": [],
            "detail": (
                "No resume vectors in this server process yet. "
                "Call POST /resume/upload first; the FAISS index is in-memory and is empty after each restart."
            ),
        }

    jd_embedding = get_single_embedding(job_description)

    ranked = rank_resumes(
        jd_embedding,
        vector_store.resume_embeddings,
        vector_store.resume_ids,
    )

    return {
        "ranked_candidates": ranked,
    }