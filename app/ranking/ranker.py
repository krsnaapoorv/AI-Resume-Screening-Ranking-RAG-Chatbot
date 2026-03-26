"""Candidate ranking against job description."""

from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(jd_embedding, resume_embeddings, resume_ids):
    scores = cosine_similarity(
        [jd_embedding], resume_embeddings
    )[0]

    results = [
        {"resume_id": int(resume_id), "score": float(score)}
        for resume_id, score in zip(resume_ids, scores)
    ]

    return sorted(results, key=lambda x: x["score"], reverse=True)
