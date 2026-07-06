import strawberry
from fastapi import HTTPException

from app.database import SessionLocal
from app.schemas.users import UserType, UserInputType, UserInput
from app.services import users as user_service


def _to_user_type(user) -> UserType:
    return UserType(
        id=user.id,
        username=user.username,
        age=user.age,
        email=user.email,
        city=user.city,
    )


@strawberry.type
class UserQuery:

    @strawberry.field
    def users(self) -> list[UserType]:
        db = SessionLocal()
        try:
            users = user_service.get_all_users(db)
            return [_to_user_type(u) for u in users]
        finally:
            db.close()

    @strawberry.field
    def user(self, id: int) -> UserType | None:
        db = SessionLocal()
        try:
            try:
                user = user_service.get_user(db, id)
            except HTTPException:
                return None
            return _to_user_type(user)
        finally:
            db.close()


@strawberry.type
class UserMutation:

    @strawberry.mutation
    def create_user(self, input: UserInputType) -> UserType:
        db = SessionLocal()
        try:
            user_input = UserInput(
                username=input.username,
                password=input.password,
                age=input.age,
                email=input.email,
                city=input.city,
            )
            user = user_service.create_user(db, user_input)
            return _to_user_type(user)
        finally:
            db.close()

    @strawberry.mutation
    def update_user(self, id: int, input: UserInputType) -> UserType:
        db = SessionLocal()
        try:
            user_input = UserInput(
                username=input.username,
                password=input.password,
                age=input.age,
                email=input.email,
                city=input.city,
            )
            user = user_service.update_user(db, id, user_input)
            return _to_user_type(user)
        finally:
            db.close()

    @strawberry.mutation
    def delete_user(self, id: int) -> bool:
        db = SessionLocal()
        try:
            user_service.delete_user(db, id)
            return True
        except HTTPException:
            return False
        finally:
            db.close()