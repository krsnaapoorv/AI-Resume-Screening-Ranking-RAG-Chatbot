"""Authentication routes."""

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from app.auth.utils import hash_password, verify_password
from app.core.security import create_access_token
from app.db.database import SessionLocal
from app.auth.models import User

router = APIRouter(prefix="/auth", tags=["Auth"])


# -------------------------------
#  Pydantic Schemas
# -------------------------------
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# -------------------------------
#  DB Dependency
# -------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------------
#  Register
# -------------------------------
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(user.password)

    new_user = User(
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully",
        "user_id": new_user.id
    }


# -------------------------------
#  Login
# -------------------------------
@router.post("/login")
async def login(request: Request, db: Session = Depends(get_db)):
    """
    Accepts:
    - **application/x-www-form-urlencoded** (Swagger OAuth2): `username`, `password` (username = email).
    - **application/json**: `email`, `password` (e.g. Streamlit / httpx).
    """
    content_type = (request.headers.get("content-type") or "").lower()
    if "application/json" in content_type:
        body = await request.json()
        email = (body.get("email") or "").strip()
        password = body.get("password") or ""
    else:
        form = await request.form()
        email = (form.get("username") or "").strip()
        password = form.get("password") or ""

    if not email or not password:
        raise HTTPException(
            status_code=422,
            detail="Missing credentials: use JSON {email, password} or form fields username, password",
        )

    existing_user = db.query(User).filter(User.email == email).first()

    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(password, existing_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": existing_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
