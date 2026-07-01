from datetime import date
from pydantic import BaseModel, ConfigDict


class SaleInputSchema(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    discount_rate: float
    total_price: int
    created_at: date


class SaleSchema(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    discount_rate: float
    total_price: int
    created_at: date

    model_config = ConfigDict(from_attributes=True)