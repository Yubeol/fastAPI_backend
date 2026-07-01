from sqlalchemy import Column, Integer, String
from app.database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(30), unique=True)
    password = Column(String(100))
    age = Column(Integer)
    email = Column(String(100))
    city = Column(String(50))