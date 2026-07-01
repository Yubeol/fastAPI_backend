from sqlalchemy import Column, Integer, Float, Date
from app.database import Base


class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)
    discount_rate = Column(Float)
    total_price = Column(Integer)
    created_at = Column(Date)