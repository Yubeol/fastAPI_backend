from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import ProductModel
from app.schemas import ProductInputSchema
from app.repositories import product_repository


def get_all_product(db: Session):
    return product_repository.get_all(db)


def get_one_product(db: Session, id: int):
    product = product_repository.get_one_by_id(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def create_product(db: Session, product_input: ProductInputSchema):
    product = ProductModel(**product_input.model_dump())
    return product_repository.create(db, product)


def update_product(db: Session, product_id: int, product_input: ProductInputSchema):
    product = product_repository.get_one_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product_input.model_dump().items():
        setattr(product, key, value)
    return product_repository.update(db, product)


def delete_product(db: Session, product_id: int):
    product = product_repository.get_one_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product_repository.delete(db, product)
    return product_id