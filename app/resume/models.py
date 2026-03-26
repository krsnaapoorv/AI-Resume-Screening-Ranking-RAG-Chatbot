from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String)
    file_path = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
