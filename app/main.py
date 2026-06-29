from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List
from starlette.middleware.cors import CORSMiddleware
from app.routers import router as emp_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

# ===== model 계층 =====
# --- Todo ---
class Todo(BaseModel):
    id: int
    subject: str
    checked: bool = False


class TodoInput(BaseModel):
    subject: str
    checked: bool = False



TODO_TABLE: List[Todo] = [
    Todo(id=1, subject="HTML 공부", checked=True),
    Todo(id=2, subject="CSS 공부", checked=False),
    Todo(id=3, subject="JavaScript 공부", checked=False),
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(emp_router)



# ===== web 계층 - Todo =====
@app.get("/todos", response_model=List[Todo])
def read_todos():
    return TODO_TABLE


@app.get("/todos/{id}", response_model=Todo)
def read_todo(id: int):
    todo = next((t for t in TODO_TABLE if t.id == id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.post("/todos", response_model=Todo)
def create_todo(todo_input: TodoInput):
    global TODO_TABLE
    new_id = max((t.id for t in TODO_TABLE), default=0) + 1
    created_todo = Todo(
        id=new_id,
        **todo_input.model_dump(),
    )
    TODO_TABLE = [*TODO_TABLE, created_todo]
    return created_todo


@app.put("/todos/{id}", response_model=Todo)
def update_todo(id: int, todo_input: TodoInput):
    global TODO_TABLE
    todo = next((t for t in TODO_TABLE if t.id == id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    updated_todo = Todo(id=id, **todo_input.model_dump())
    TODO_TABLE = [
        updated_todo if t.id == id else t for t in TODO_TABLE
    ]
    return updated_todo


@app.patch("/todos/{id}/toggle", response_model=Todo)
def toggle_todo(id: int):
    global TODO_TABLE
    todo = next((t for t in TODO_TABLE if t.id == id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    toggled_todo = todo.model_copy(update={"checked": not todo.checked})
    TODO_TABLE = [
        toggled_todo if t.id == id else t for t in TODO_TABLE
    ]
    return toggled_todo


@app.delete("/todos/{id}")
def delete_todo(id: int):
    global TODO_TABLE
    todo = next((t for t in TODO_TABLE if t.id == id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    TODO_TABLE = [t for t in TODO_TABLE if t.id != id]
    return {"message": f"Todo {id} deleted"}


if __name__ == '__main__':
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)