from pydantic import BaseModel


class UserInputSchema(BaseModel):
    name: str
    password: str
    age: int
    email: str
    city: str


class UserSchema(BaseModel):
    id: int
    name: str
    password: str
    age: int
    email: str
    city: str

    class Config:
        from_attributes = True