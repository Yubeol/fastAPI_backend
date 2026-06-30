from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import ProductInputSchema, ProductSchema
from database import get_db
from app.services import *

router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("", response_model=List[ProductSchema])
def web_read_products(db: Session = Depends(get_db)):
    return get_all_product(db)


@router.get("/{id}", response_model=ProductSchema)
def web_read_product(id: int, db: Session = Depends(get_db)):
    return get_one_product(db, id)


@router.post("", response_model=ProductSchema)
def web_create_product(
        product_input: ProductInputSchema,
        db: Session = Depends(get_db)
):
    return create_product(db, product_input)


@router.put("/{id}", response_model=ProductSchema)
def web_update_product(
        id: int,
        product_input: ProductInputSchema,
        db: Session = Depends(get_db)
):
    return update_product(db, id, product_input)


@router.delete("/{id}")
def web_delete_product(id: int, db: Session = Depends(get_db)):
    return delete_product(db, id)