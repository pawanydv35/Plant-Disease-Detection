"""
`get_current_user` is the dependency every protected route
(/predict, /history, /profile) will use:

    @router.get("/profile")
    def profile(current_user: User = Depends(get_current_user)):
        ...

It reads the `Authorization: Bearer <token>` header, validates the JWT,
and loads the corresponding User row from the DB — or raises 401.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.auth.security import decode_access_token
from app.database.session import get_db
from app.models.user import User

# tokenUrl is just used for the OpenAPI docs' "Authorize" button;
# our actual login endpoint is /login (JSON body, not OAuth2 form).
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", auto_error=False)


def get_current_user(
    token: str | None = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if token is None:
        raise credentials_exception

    user_id = decode_access_token(token)
    if user_id is None:
        raise credentials_exception

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception

    return user
