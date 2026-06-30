from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(200))
    checked = Column(Boolean, default=False)