from pydantic import BaseModel, ConfigDict

# --- Pydantic Schema: 입력용 ---
class EmployeeInput(BaseModel):
    name: str
    age: int
    job: str
    language: str
    pay: int

# --- Pydantic Schema: 응답용 (DB 모델 → JSON 변환) ---
class Employee(BaseModel):
    id: int
    name: str
    age: int
    job: str
    language: str
    pay: int

    model_config = ConfigDict(from_attributes=True)