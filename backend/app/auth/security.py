"""
Low-level security primitives: password hashing (bcrypt) and JWT
encode/decode. No FastAPI-specific code here (no Depends, no routes) —
keeps this module easy to unit test in isolation.
"""

from datetime import datetime, timedelta, timezone
from typing import Any

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.utils.config import get_settings

settings = get_settings()

# bcrypt is the requested hashing scheme. passlib handles salting
# automatically, so we don't manage salts ourselves.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(subject: str, expires_delta: timedelta | None = None) -> str:
    """
    `subject` is the value that identifies the user inside the token —
    we use the user's id (as a string) so we never need to trust a
    user-supplied email at request time.
    """
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    )
    to_encode: dict[str, Any] = {"sub": subject, "exp": expire}
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decode_access_token(token: str) -> str | None:
    """Returns the user id (sub claim) if the token is valid, else None."""
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None
