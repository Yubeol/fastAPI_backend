from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import TodosModel
from app.schemas import TodoInputSchema
from app.repositories import todo_repository


def get_all_todo(db: Session):
    return todo_repository.get_all(db)


def get_one_todo(db: Session, todo_id: int):
    todo = todo_repository.get_one_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


def create_todo(db: Session, todo_input: TodoInputSchema):
    todo = TodosModel(**todo_input.model_dump())
    return todo_repository.create(db, todo)


def update_todo(db: Session, todo_id: int, todo_input: TodoInputSchema):
    todo = todo_repository.get_one_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo_input.model_dump().items():
        setattr(todo, key, value)
    return todo_repository.update(db, todo)


def toggle_todo(db: Session, todo_id: int):
    todo = todo_repository.get_one_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.checked = not todo.checked
    return todo_repository.update(db, todo)


def delete_todo(db: Session, todo_id: int):
    todo = todo_repository.get_one_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_repository.delete(db, todo)
    return todo_id