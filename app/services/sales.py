from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import SalesModel
from app.schemas import SaleInputSchema
from app.repositories import sale_repository


def get_all_sale(db: Session):
    return sale_repository.get_all(db)


def get_one_sale(db: Session, id: int):
    sale = sale_repository.get_one_by_id(db, id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale


def create_sale(db: Session, sale_input: SaleInputSchema):
    sale = SalesModel(**sale_input.model_dump())
    return sale_repository.create(db, sale)


def update_sale(db: Session, sale_id: int, sale_input: SaleInputSchema):
    sale = sale_repository.get_one_by_id(db, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    for key, value in sale_input.model_dump().items():
        setattr(sale, key, value)
    return sale_repository.update(db, sale)


def delete_sale(db: Session, sale_id: int):
    sale = sale_repository.get_one_by_id(db, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    sale_repository.delete(db, sale)
    return sale_id