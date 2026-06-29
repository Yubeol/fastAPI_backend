from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas import EmployeeInput as EmployeeInputSchema,Employee as EmployeeSchema
from app.models import Employees
from database import get_db

router = APIRouter(
    prefix="/employees",
    tags=["employees"],
)


@router.get("", response_model=List[EmployeeSchema])
def read_employees(db: Session = Depends(get_db)):
    return db.query(Employees).all()


@router.get("/{id}", response_model=EmployeeSchema)
def read_employee(id: str, db: Session = Depends(get_db)):
    employee = db.query(Employees).filter(Employees.id == id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.post("", response_model=EmployeeSchema)
def create_employee(
        employee_input: EmployeeInputSchema,
        db: Session = Depends(get_db)
):
    created_employee = Employee(**employee_input.model_dump())
    db.add(created_employee)
    db.commit()
    db.refresh(created_employee)
    return created_employee


@router.put("/{id}", response_model=EmployeeSchema)
def update_employee(
        id: str,
        employee_input: EmployeeInputSchema,
        db: Session = Depends(get_db)
):
    updated_employee = db.query(Employees).filter(Employees.id == id).first()
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    for key, value in employee_input.model_dump().items():
        setattr(updated_employee, key, value)
    db.commit()
    db.refresh(updated_employee)
    return updated_employee


@router.delete("/{id}")
def delete_employee(id: str, db: Session = Depends(get_db)):
    employee = db.query(Employees).filter(Employees.id == id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()
    return {"message": f"Employee {id} deleted"}