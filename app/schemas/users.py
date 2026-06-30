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