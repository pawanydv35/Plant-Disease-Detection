from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.models.schemas import PredictionOut
from app.models.user import User
from app.services import prediction_service

router = APIRouter()


@router.get("", response_model=list[PredictionOut])
def get_history(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return prediction_service.list_history(db, current_user)


@router.delete("/{prediction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_history_item(
    prediction_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    deleted = prediction_service.delete_prediction(db, current_user, prediction_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prediction not found.")
