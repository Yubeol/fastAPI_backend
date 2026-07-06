from fastapi import Request
from strawberry.fastapi import BaseContext

from app.database import SessionLocal
from app.utils.security import decode_access_token
from app.repositories import users as user_repository


class GraphQLContext(BaseContext):
    def __init__(self, db, current_user):
        self.db = db
        self.current_user = current_user


def get_context(request: Request):
    db = SessionLocal()
    current_user = None

    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.removeprefix("Bearer ")
        payload = decode_access_token(token)
        if payload:
            username = payload.get("sub")
            if username:
                current_user = user_repository.get_by_name(db, username)

    try:
        yield GraphQLContext(db=db, current_user=current_user)
    finally:
        db.close()