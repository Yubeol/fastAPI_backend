from app.database import Base
from sqlalchemy import Column, Integer, String

class Employees(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100))
    job = Column(String(100))
    pay = Column(Integer)