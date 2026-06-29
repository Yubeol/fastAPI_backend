from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List


# model 계층
# Pydantic Model : Json => Python 객체
class Employee(BaseModel):
    id: str
    name: str
    age: int
    job: str
    language: str
    pay: int


# Pydantic Schema : Json => Python 객체 (입력용)
class EmployeeInput(BaseModel):
    name: str
    age: int
    job: str
    language: str
    pay: int


# Database 계층
EMPLOYEE_TABLE: List[Employee] = [
    Employee(id='1', name="John", age=24, job="frontend", language="react", pay=400),
    Employee(id='2', name="Peter", age=35, job="backend", language="python", pay=500),
    Employee(id='3', name="Susan", age=24, job="db", language="postgres", pay=600),
    Employee(id='4', name="Sue", age=24, job="ai", language="python", pay=700),
]

app = FastAPI()

# web 계층
@app.get("/employee", response_model=List[Employee])
def read_employees():
    global EMPLOYEE_TABLE
    return EMPLOYEE_TABLE

@app.get("/employee/{id}", response_model=Employee)
def read_employee(id: str):
    global EMPLOYEE_TABLE
    employee = next((emp for emp in EMPLOYEE_TABLE if emp.id == id), None)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.post("/employee",response_model=Employee)
def create_employee(employee_input: EmployeeInput):
    global EMPLOYEE_TABLE
    created_employee = Employee(
        id = str(max(int(emp.id) for emp in EMPLOYEE_TABLE) + 1),
        ** employee_input.model_dump(),
    )
    EMPLOYEE_TABLE = [
        *EMPLOYEE_TABLE,
        created_employee
    ]
    return created_employee

@app.put("/employee/{id}", response_model=Employee)
def update_employee(id: str, employee_input: EmployeeInput):
    global EMPLOYEE_TABLE
    updated_employee = Employee(
        id=id,
        **employee_input.model_dump()
    )
    EMPLOYEE_TABLE = [
        updated_employee if emp.id == id else emp for emp in EMPLOYEE_TABLE
    ]
    return updated_employee

@app.delete("/employee/{id}")
def delete_employee(id: str):
    global EMPLOYEE_TABLE
    EMPLOYEE_TABLE = [
        emp for emp in EMPLOYEE_TABLE if emp.id != id
    ]
    return id



if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)