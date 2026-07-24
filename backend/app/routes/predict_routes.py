import json

from fastapi import APIRouter, Depends, File, HTTPException, Request, UploadFile, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.models.schemas import PredictResponse, TopPrediction
from app.models.user import User
from app.services import prediction_service
from app.services.prediction_service import InvalidImageError

router = APIRouter()


@router.post("/predict", response_model=PredictResponse)
def predict(
    request: Request,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    model_service = getattr(request.app.state, "model_service", None)
    if model_service is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model is not loaded. Check server startup logs.",
        )

    leaf_gate_service = getattr(request.app.state, "leaf_gate_service", None)

    try:
        prediction, info = prediction_service.run_prediction(
            db, current_user, file, model_service, leaf_gate_service
        )
    except InvalidImageError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return PredictResponse(
        id=prediction.id,
        disease_name=prediction.disease_name,
        confidence=prediction.confidence,
        top_predictions=[TopPrediction(**p) for p in json.loads(prediction.top_predictions)],
        image_url=prediction.image_url,
        created_at=prediction.created_at,
        causes=info["causes"],
        symptoms=info["symptoms"],
        treatment=info["treatment"],
        prevention=info["prevention"],
    )
