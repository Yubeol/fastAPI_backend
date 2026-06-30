from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import UserInputSchema, UserSchema
from app.database import get_db
from app.services import *

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("", response_model=List[UserSchema])
def web_read_users(db: Session = Depends(get_db)):
    return get_all_user(db)


@router.get("/{id}", response_model=UserSchema)
def web_read_user(id: int, db: Session = Depends(get_db)):
    return get_one_user(db, id)


@router.post("", response_model=UserSchema)
def web_create_user(
        user_input: UserInputSchema,
        db: Session = Depends(get_db)
):
    return create_user(db, user_input)


@router.put("/{id}", response_model=UserSchema)
def web_update_user(
        id: int,
        user_input: UserInputSchema,
        db: Session = Depends(get_db)
):
    return update_user(db, id, user_input)


@router.delete("/{id}")
def web_delete_user(id: int, db: Session = Depends(get_db)):
    return delete_user(db, id)
