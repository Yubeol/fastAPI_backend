from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import users as user_repository
from app.utils.security import (
    verify_password,
    create_access_token,
)


def login(
        db: Session,
        name: str,
        password: str,
):

    user = user_repository.get_by_name(db, name)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="아이디가 존재하지 않습니다."
        )

    if not verify_password(
            password,
            user.password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="비밀번호가 일치하지 않습니다."
        )

    token = create_access_token(user.username)

    return {
        "access_token": token,
        "token_type": "bearer",
    }


def me(
        db: Session,
        name: str,
):

    user = user_repository.get_by_name(
        db,
        name,
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user