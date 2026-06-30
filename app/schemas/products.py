from pydantic import BaseModel


class ProductInputSchema(BaseModel):
    product_name: str
    color: str
    cost_price: int
    sale_price: int
    category_code: str


class ProductSchema(BaseModel):
    id: int
    product_name: str
    color: str
    cost_price: int
    sale_price: int
    category_code: str

    class Config:
        from_attributes = True