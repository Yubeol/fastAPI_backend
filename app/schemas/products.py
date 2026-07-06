import strawberry
from pydantic import BaseModel, ConfigDict


class ProductInputSchema(BaseModel):
    product_name: str
    color: str
    price: int
    sale_price: int
    category_code: str


class ProductSchema(BaseModel):
    id: int
    product_name: str
    color: str
    price: int
    sale_price: int
    category_code: str

    model_config = ConfigDict(from_attributes=True)


# =====================================================
# GraphQL Types
# =====================================================

@strawberry.type
class ProductType:
    id: int
    product_name: str
    color: str
    price: int
    sale_price: int
    category_code: str


@strawberry.input
class ProductInput:
    product_name: str
    color: str
    price: int
    sale_price: int
    category_code: str