from datetime import date
from pydantic import BaseModel


class SaleInputSchema(BaseModel):
    date: date
    product_code: int
    customer_code: int
    promotion_code: int
    channel_code: int
    quantity: int


class SaleSchema(BaseModel):
    id: int
    date: date
    product_code: int
    customer_code: int
    promotion_code: int
    channel_code: int
    quantity: int

    class Config:
        from_attributes = True