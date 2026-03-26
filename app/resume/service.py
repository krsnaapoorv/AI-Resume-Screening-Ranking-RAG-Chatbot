"""Resume ingestion and ranking orchestration."""
import os
import shutil
from app.core.config import UPLOAD_DIR
from app.ingestion.parser import extract_text
from app.ingestion.chunking import chunk_text
from app.ingestion.embedding import get_embeddings, model
from app.db.store import get_vector_store, set_vector_store
from app.db.vector_store import VectorStore
from app.ingestion.embedding import get_single_embedding
from app.resume.models import Resume
from sqlalchemy.orm import Session


def save_resume(file):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path


def process_resume(file_path: str, db: Session, user_id: int):
    print("Step 1: Extracting text...")
    text = extract_text(file_path)

    print("Step 2: Chunking...")
    chunks = chunk_text(text)

    print("Step 3: Generating embeddings...")
    embeddings = get_embeddings(chunks)

    print("Step 4: Save Resume in DB...")

    new_resume = Resume(
        file_name=os.path.basename(file_path),
        file_path=file_path,
        user_id=user_id
    )

    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)

    resume_id = new_resume.id  # 🔥 IMPORTANT

    print("Resume ID:", resume_id)

    print("Step 5: Store in FAISS...")

    vector_store = get_vector_store()

    if vector_store is None:
        vector_store = VectorStore(dim=len(embeddings[0]))
        set_vector_store(vector_store)

    vector_store.add(embeddings, chunks)

    # Resume-level embedding
    resume_embedding = get_single_embedding(text)

    vector_store.add_resume(resume_id, resume_embedding)

    print("✅ Resume processed successfully")

    return {
        "resume_id": resume_id,
        "chunks": len(chunks)
    }
