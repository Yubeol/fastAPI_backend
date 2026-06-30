from datetime import datetime, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_DELTA,
)

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


# ==========================
# Password
# ==========================

def hash_password(password: str) -> str:
    """
    비밀번호 암호화
    """
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    비밀번호 검증
    """
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


# ==========================
# JWT
# ==========================

def create_access_token(name: str) -> str:
    """
    JWT 생성
    """

    expire = datetime.now(timezone.utc) + ACCESS_TOKEN_EXPIRE_DELTA

    payload = {
        "sub": name,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_access_token(token: str):
    """
    JWT 검증
    """

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        return payload

    except JWTError:
        return None