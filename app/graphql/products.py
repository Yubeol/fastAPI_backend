import strawberry
from fastapi import HTTPException

from app.database import SessionLocal
from app.schemas.products import ProductType, ProductInput, ProductInputSchema
from app.services import products as product_service


def _to_product_type(product) -> ProductType:
    return ProductType(
        id=product.id,
        product_name=product.product_name,
        color=product.color,
        price=product.price,
        sale_price=product.sale_price,
        category_code=product.category_code,
    )


@strawberry.type
class ProductQuery:

    @strawberry.field
    def products(self) -> list[ProductType]:
        db = SessionLocal()
        try:
            products = product_service.get_all_product(db)
            return [_to_product_type(p) for p in products]
        finally:
            db.close()

    @strawberry.field
    def product(self, id: int) -> ProductType | None:
        db = SessionLocal()
        try:
            try:
                product = product_service.get_one_product(db, id)
            except HTTPException:
                return None
            return _to_product_type(product)
        finally:
            db.close()


@strawberry.type
class ProductMutation:

    @strawberry.mutation
    def create_product(self, input: ProductInput) -> ProductType:
        db = SessionLocal()
        try:
            product_input = ProductInputSchema(
                product_name=input.product_name,
                color=input.color,
                price=input.price,
                sale_price=input.sale_price,
                category_code=input.category_code,
            )
            product = product_service.create_product(db, product_input)
            return _to_product_type(product)
        finally:
            db.close()

    @strawberry.mutation
    def update_product(self, id: int, input: ProductInput) -> ProductType:
        db = SessionLocal()
        try:
            product_input = ProductInputSchema(
                product_name=input.product_name,
                color=input.color,
                price=input.price,
                sale_price=input.sale_price,
                category_code=input.category_code,
            )
            product = product_service.update_product(db, id, product_input)
            return _to_product_type(product)
        finally:
            db.close()

    @strawberry.mutation
    def delete_product(self, id: int) -> bool:
        db = SessionLocal()
        try:
            product_service.delete_product(db, id)
            return True
        except HTTPException:
            return False
        finally:
            db.close()