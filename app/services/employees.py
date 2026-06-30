from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import EmployeeModel
from app.schemas import EmployeeInputSchema
from app.repositories import employee_repository


def get_all_employee(db: Session):
    return employee_repository.get_all(db)


def get_one_employee(db: Session, id: int):
    employee = employee_repository.get_one_by_id(db, id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )
    return employee


def create_employee(db: Session, employee_input: EmployeeInputSchema):
    employee = EmployeeModel(**employee_input.model_dump())
    return employee_repository.create(db, employee)


def update_employee(
        db: Session,
        employee_id: int,
        employee_input: EmployeeInputSchema
):
    employee = employee_repository.get_one_by_id(db, employee_id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )
    for key, value in employee_input.model_dump().items():
        setattr(employee, key, value)
    return employee_repository.update(db, employee)


def delete_employee(db: Session, employee_id: int):
    employee = employee_repository.get_one_by_id(db, employee_id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )
    employee_repository.delete(db, employee)
    return employee_id