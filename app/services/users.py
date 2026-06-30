from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import UsersModel
from app.schemas import UserInputSchema
from app.repositories import user_repository
# from app.vtils.security import hash_password


def get_all_user(db: Session):
    return user_repository.get_all(db)


def get_one_user(db: Session, id: int):
    user = user_repository.get_one_by_id(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def create_user(db: Session, user_input: UserInputSchema):
    user = UsersModel(**user_input.model_dump())
    return user_repository.create(db, user)


def update_user(db: Session, user_id: int, user_input: UserInputSchema):
    user = user_repository.get_one_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_input.model_dump().items():
        setattr(user, key, value)
    return user_repository.update(db, user)


def delete_user(db: Session, user_id: int):
    user = user_repository.get_one_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_repository.delete(db, user)
    return user_id
