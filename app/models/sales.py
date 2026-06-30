from sqlalchemy import Column, Integer, Date

from app.database import Base


class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    product_code = Column(Integer)
    customer_code = Column(Integer)
    promotion_code = Column(Integer)
    channel_code = Column(Integer)
    quantity = Column(Integer)