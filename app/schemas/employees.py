from pydantic import BaseModel, ConfigDict

class EmployeeInput(BaseModel):
    name: str
    email: str
    job: str
    pay: int
    model_config = ConfigDict(from_attributes=True)

class Employee(EmployeeInput):
    id: int
    model_config = ConfigDict(from_attributes=True)