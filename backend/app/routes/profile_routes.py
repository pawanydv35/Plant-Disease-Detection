"""
Profile routes. GET /profile is trivial given get_current_user, so it's
included now. Edit-profile and change-password are added alongside the
frontend Profile page in a later step (they need extra validation
around re-authentication for password changes).
"""

from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models.schemas import UserOut
from app.models.user import User

router = APIRouter()


@router.get("", response_model=UserOut)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user
