from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import TodoInputSchema, TodoSchema
from database import get_db
from app.services import *

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)

@router.get("", response_model=List[TodoSchema])
def web_read_todos(db: Session = Depends(get_db)):
    return get_all_todo(db)


@router.get("/{id}", response_model=TodoSchema)
def web_read_todo(id: int, db: Session = Depends(get_db)):
    return get_one_todo(db, id)


@router.post("", response_model=TodoSchema)
def web_create_todo(
        todo_input: TodoInputSchema,
        db: Session = Depends(get_db)
):
    return create_todo(db, todo_input)


@router.put("/{id}", response_model=TodoSchema)
def web_update_todo(
        id: int,
        todo_input: TodoInputSchema,
        db: Session = Depends(get_db)
):
    return update_todo(db, id, todo_input)


@router.patch("/{id}/toggle", response_model=TodoSchema)
def web_toggle_todo(id: int, db: Session = Depends(get_db)):
    return toggle_todo(db, id)


@router.delete("/{id}")
def web_delete_todo(id: int, db: Session = Depends(get_db)):
    return delete_todo(db, id)

