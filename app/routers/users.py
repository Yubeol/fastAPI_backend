from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import User, UserInput
from app.services import *

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("", response_model=List[User])
def web_read_users(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get("/{user_id}", response_model=User)
def web_read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)


@router.post("", response_model=User)
def web_create_user(user_input: UserInput, db: Session = Depends(get_db)):
    return create_user(db, user_input)


@router.put("/{user_id}", response_model=User)
def web_update_user(user_id: int, user_input: UserInput, db: Session = Depends(get_db)):
    return update_user(db, user_id, user_input)


@router.delete("/{user_id}")
def web_delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
