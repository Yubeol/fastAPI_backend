from sqlalchemy import Column, Integer, String
from app.database import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100))
    color = Column(String(30))
    price = Column(Integer)
    sale_price = Column(Integer)
    category_code = Column(String(20))