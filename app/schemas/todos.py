from pydantic import BaseModel

# ===== model 계층 =====
# --- Todo ---
class TodoInputSchema(BaseModel):
    subject: str
    checked: bool = False

class TodoSchema(BaseModel):
    id: int
    subject: str
    checked: bool

    class Config:
        from_attributes =True