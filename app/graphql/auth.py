import strawberry
from strawberry.types import Info

from app.database import SessionLocal
from app.schemas.auth import LoginInput, TokenType
from app.schemas.users import UserType
from app.services import auth as auth_service


def _to_user_type(user) -> UserType:
    return UserType(
        id=user.id,
        username=user.username,
        age=user.age,
        email=user.email,
        city=user.city,
    )


@strawberry.type
class AuthQuery:

    @strawberry.field
    def me(self, info: Info) -> UserType | None:
        current_user = info.context.current_user
        if current_user is None:
            return None
        return _to_user_type(current_user)


@strawberry.type
class AuthMutation:

    @strawberry.mutation
    def login(self, input: LoginInput) -> TokenType:
        db = SessionLocal()
        try:
            result = auth_service.login(db, input.name, input.password)
            return TokenType(
                access_token=result["access_token"],
                token_type=result["token_type"],
            )
        finally:
            db.close()