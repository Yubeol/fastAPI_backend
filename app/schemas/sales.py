from datetime import date
import strawberry
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


# =====================================================
# GraphQL Types
# =====================================================

@strawberry.type
class SaleType:
    id: int
    user_id: int
    product_id: int
    quantity: int
    discount_rate: float
    total_price: int
    created_at: date