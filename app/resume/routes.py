"""Resume upload and job-description API routes."""
from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
from app.resume.service import save_resume, process_resume
from app.db.database import SessionLocal
from app.core.security import get_current_user  # if you have JWT decode

router = APIRouter(prefix="/resume", tags=["Resume"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/upload")
def upload_resume(
        file: UploadFile,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):
    file_path = save_resume(file)

    result = process_resume(
        file_path,
        db,
        user_id=current_user.id
    )

    return result
