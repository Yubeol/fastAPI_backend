from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.auth import LoginRequest, Token
from app.schemas import User
from app.services import auth as auth_service
from app.utils.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login", response_model=Token)
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    return auth_service.login(db, login_request.name, login_request.password)


@router.get("/me", response_model=User)
def read_me(current_user=Depends(get_current_user)):
    return current_user