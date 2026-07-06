import strawberry
from pydantic import BaseModel


class TodoInputSchema(BaseModel):
    subject: str
    checked: bool = False


class TodoSchema(BaseModel):
    id: int
    subject: str
    checked: bool

    class Config:
        from_attributes = True


# =====================================================
# GraphQL Types
# =====================================================

@strawberry.type
class TodoType:
    id: int
    subject: str
    checked: bool


@strawberry.input
class TodoInput:
    subject: str
    checked: bool = False