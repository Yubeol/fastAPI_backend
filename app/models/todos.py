from sqlalchemy import Boolean, Column, Integer, String, Date
from app.database import Base


class Todos(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    subject = Column(String(200))
    checked = Column(Boolean, default=False)
    created_at = Column(Date)   