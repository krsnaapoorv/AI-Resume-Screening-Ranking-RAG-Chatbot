"""Application entrypoint."""
from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.resume.routes import router as resume_router
from app.rag.routes import router as rag_router
from app.ranking.routes import router as ranking_router
from app.db.database import Base, engine

app = FastAPI(title="AI Resume System")

app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(rag_router)
app.include_router(ranking_router)


# 👇 IMPORTANT: import models before create_all
from app.auth.models import User
from app.resume.models import Resume


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
