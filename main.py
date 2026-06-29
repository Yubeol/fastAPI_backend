from fastapi import FastAPI
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
EMPLOYEES: List[Employee] = [
    Employee(id='1', name="John", age=24, job="frontend", language="react", pay=400),
    Employee(id='2', name="Peter", age=35, job="backend", language="python", pay=500),
    Employee(id='3', name="Susan", age=24, job="db", language="postgres", pay=600),
    Employee(id='4', name="Sue", age=24, job="ai", language="python", pay=700),
]

app = FastAPI()


# web 계층
@app.get("/employee", response_model=List[Employee])
def read_employees():
    return EMPLOYEES


@app.get("/")
async def root():
    return {"message": "FastAPI RESTFul server running"}


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)