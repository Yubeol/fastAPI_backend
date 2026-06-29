from pydantic import BaseModel
from database import Base
from sqlalchemy import Column, Integer, String

# ORM => Object Relation Mapping
# ===== model 계층 =====
# --- Employee ---
class Employees(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    job = Column(String(50))
    language = Column(String(50))
    pay = Column(Integer)

