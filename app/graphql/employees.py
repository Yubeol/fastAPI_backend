import strawberry
from fastapi import HTTPException

from app.database import SessionLocal
from app.schemas.employees import EmployeeType, EmployeeInputGQL, EmployeeInput as EmployeeInputSchema
from app.services import employees as employee_service


def _to_employee_type(employee) -> EmployeeType:
    return EmployeeType(
        id=employee.id,
        name=employee.name,
        email=employee.email,
        job=employee.job,
        pay=employee.pay,
    )


@strawberry.type
class EmployeeQuery:

    @strawberry.field
    def employees(self) -> list[EmployeeType]:
        db = SessionLocal()
        try:
            employees = employee_service.get_all_employee(db)
            return [_to_employee_type(e) for e in employees]
        finally:
            db.close()

    @strawberry.field
    def employee(self, id: int) -> EmployeeType | None:
        db = SessionLocal()
        try:
            try:
                employee = employee_service.get_one_employee(db, id)
            except HTTPException:
                return None
            return _to_employee_type(employee)
        finally:
            db.close()


@strawberry.type
class EmployeeMutation:

    @strawberry.mutation
    def create_employee(self, input: EmployeeInputGQL) -> EmployeeType:
        db = SessionLocal()
        try:
            employee_input = EmployeeInputSchema(
                name=input.name,
                email=input.email,
                job=input.job,
                pay=input.pay,
            )
            employee = employee_service.create_employee(db, employee_input)
            return _to_employee_type(employee)
        finally:
            db.close()

    @strawberry.mutation
    def update_employee(self, id: int, input: EmployeeInputGQL) -> EmployeeType:
        db = SessionLocal()
        try:
            employee_input = EmployeeInputSchema(
                name=input.name,
                email=input.email,
                job=input.job,
                pay=input.pay,
            )
            employee = employee_service.update_employee(db, id, employee_input)
            return _to_employee_type(employee)
        finally:
            db.close()

    @strawberry.mutation
    def delete_employee(self, id: int) -> bool:
        db = SessionLocal()
        try:
            employee_service.delete_employee(db, id)
            return True
        except HTTPException:
            return False
        finally:
            db.close()