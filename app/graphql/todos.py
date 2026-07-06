import strawberry
from fastapi import HTTPException

from app.database import SessionLocal
from app.schemas.todos import TodoType, TodoInput, TodoInputSchema
from app.services import todos as todo_service


def _to_todo_type(todo) -> TodoType:
    return TodoType(
        id=todo.id,
        subject=todo.subject,
        checked=todo.checked,
    )


@strawberry.type
class TodoQuery:

    @strawberry.field
    def todos(self) -> list[TodoType]:
        db = SessionLocal()
        try:
            todos = todo_service.get_all_todo(db)
            return [_to_todo_type(t) for t in todos]
        finally:
            db.close()

    @strawberry.field
    def todo(self, id: int) -> TodoType | None:
        db = SessionLocal()
        try:
            try:
                todo = todo_service.get_one_todo(db, id)
            except HTTPException:
                return None
            return _to_todo_type(todo)
        finally:
            db.close()


@strawberry.type
class TodoMutation:

    @strawberry.mutation
    def create_todo(self, input: TodoInput) -> TodoType:
        db = SessionLocal()
        try:
            todo_input = TodoInputSchema(
                subject=input.subject,
                checked=input.checked,
            )
            todo = todo_service.create_todo(db, todo_input)
            return _to_todo_type(todo)
        finally:
            db.close()

    @strawberry.mutation
    def update_todo(self, id: int, input: TodoInput) -> TodoType:
        db = SessionLocal()
        try:
            todo_input = TodoInputSchema(
                subject=input.subject,
                checked=input.checked,
            )
            todo = todo_service.update_todo(db, id, todo_input)
            return _to_todo_type(todo)
        finally:
            db.close()

    @strawberry.mutation
    def toggle_todo(self, id: int) -> TodoType:
        db = SessionLocal()
        try:
            todo = todo_service.toggle_todo(db, id)
            return _to_todo_type(todo)
        finally:
            db.close()

    @strawberry.mutation
    def delete_todo(self, id: int) -> bool:
        db = SessionLocal()
        try:
            todo_service.delete_todo(db, id)
            return True
        except HTTPException:
            return False
        finally:
            db.close()