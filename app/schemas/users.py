import strawberry
from pydantic import BaseModel, ConfigDict


class UserInput(BaseModel):
    username: str
    password: str
    age: int
    email: str
    city: str


class User(UserInput):
    id: int
    model_config = ConfigDict(from_attributes=True)


# =====================================================
# GraphQL Types
# =====================================================

@strawberry.type
class UserType:
    id: int
    username: str
    age: int
    email: str
    city: str
    # password는 보안상 GraphQL 응답에 노출하지 않음


@strawberry.input
class UserInputType:
    username: str
    password: str
    age: int
    email: str
    city: str