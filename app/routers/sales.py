from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import SaleInputSchema, SaleSchema
from app.database import get_db
from app.services import *

router = APIRouter(
    prefix="/sales",
    tags=["sales"],
)


@router.get("", response_model=List[SaleSchema])
def web_read_sales(db: Session = Depends(get_db)):
    return get_all_sale(db)


@router.get("/{id}", response_model=SaleSchema)
def web_read_sale(id: int, db: Session = Depends(get_db)):
    return get_one_sale(db, id)


@router.post("", response_model=SaleSchema)
def web_create_sale(
        sale_input: SaleInputSchema,
        db: Session = Depends(get_db)
):
    return create_sale(db, sale_input)


@router.put("/{id}", response_model=SaleSchema)
def web_update_sale(
        id: int,
        sale_input: SaleInputSchema,
        db: Session = Depends(get_db)
):
    return update_sale(db, id, sale_input)


@router.delete("/{id}")
def web_delete_sale(id: int, db: Session = Depends(get_db)):
    return delete_sale(db, id)