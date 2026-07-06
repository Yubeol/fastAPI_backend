import strawberry
from pydantic import BaseModel, ConfigDict

@strawberry.input
class LoginInput:
    name: str
    password: str


@strawberry.type
class TokenType:
    access_token: str
    token_type: str


@strawberry.type
class TokenDataType:
    name: str | None = None

# =====================================================
# Employee - GraphQL Types
# =====================================================

@strawberry.type
class EmployeeType:
    id: int
    name: str
    email: str
    job: str
    pay: int


@strawberry.input
class EmployeeInputGQL:
    name: str
    email: str
    job: str
    pay: int


# =====================================================
# Employee - Pydantic (services.py, __init__.py에서 사용)
# =====================================================

class EmployeeInput(BaseModel):
    name: str
    email: str
    job: str
    pay: int
    model_config = ConfigDict(from_attributes=True)


class Employee(EmployeeInput):
    id: int
    model_config = ConfigDict(from_attributes=True)