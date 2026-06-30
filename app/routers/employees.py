from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import EmployeeInputSchema, EmployeeSchema
from app.models import EmployeeModel
from database import get_db
from app.services import *

router = APIRouter(
    prefix="/employees",
    tags=["employees"],
)


@router.get("", response_model=List[EmployeeSchema])
def web_read_employees(db: Session = Depends(get_db)):
    return get_all_employee(db)


@router.get("/{id}", response_model=EmployeeSchema)
def web_read_employee(id: str, db: Session = Depends(get_db)):
    return get_one_employee(db, id)

@router.post("", response_model=EmployeeSchema)
def web_create_employee(
        employee_input: EmployeeInputSchema,
        db: Session = Depends(get_db)
):
    return create_employee(db, employee_input)


@router.put("/{id}", response_model=EmployeeSchema)
def web_update_employee(
        id: str,
        employee_input: EmployeeInputSchema,
        db: Session = Depends(get_db)
):
    return update_employee(db, id, employee_input)


@router.delete("/{id}")
def web_delete_employee(id: str, db: Session = Depends(get_db)):
    return delete_employee(db, id)