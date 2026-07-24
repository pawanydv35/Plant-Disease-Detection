from sqlalchemy.orm import Session

from app.auth.security import hash_password, verify_password, create_access_token
from app.models.schemas import SignupRequest, LoginRequest
from app.models.user import User


class AuthError(Exception):
    """Raised for any auth failure; routes translate this into HTTP errors."""


def signup(db: Session, data: SignupRequest) -> tuple[User, str]:
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise AuthError("An account with this email already exists.")

    user = User(
        name=data.name,
        email=data.email,
        hashed_password=hash_password(data.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(subject=str(user.id))
    return user, token


def login(db: Session, data: LoginRequest) -> tuple[User, str]:
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.hashed_password):
        # Same error for "no such user" and "wrong password" —
        # avoids leaking which emails are registered.
        raise AuthError("Invalid email or password.")

    token = create_access_token(subject=str(user.id))
    return user, token
