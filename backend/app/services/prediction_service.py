import json
import sys
import uuid
from pathlib import Path

from fastapi import UploadFile
from PIL import Image, UnidentifiedImageError
from sqlalchemy.orm import Session

from app.models.prediction import Prediction
from app.models.user import User

_BACKEND_ROOT = Path(__file__).resolve().parents[2]
if str(_BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(_BACKEND_ROOT))

from model.disease_info import get_disease_info, NOT_A_LEAF_LABEL  # noqa: E402

UPLOAD_DIR = Path(__file__).resolve().parents[2] / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10MB


class InvalidImageError(Exception):
    """Raised for any bad-upload case; routes translate this to HTTP 400."""


def _save_upload(file: UploadFile, raw_bytes: bytes) -> str:
    extension = Path(file.filename or "").suffix or ".jpg"
    filename = f"{uuid.uuid4()}{extension}"
    destination = UPLOAD_DIR / filename
    with open(destination, "wb") as f:
        f.write(raw_bytes)
    return filename


def run_prediction(
    db: Session,
    user: User,
    file: UploadFile,
    model_service,
    leaf_gate_service=None,
) -> tuple[Prediction, dict]:
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise InvalidImageError(f"Unsupported file type: {file.content_type}. Upload a JPEG, PNG, or WEBP image.")

    raw_bytes = file.file.read()
    if len(raw_bytes) > MAX_FILE_SIZE_BYTES:
        raise InvalidImageError("Image is too large. Maximum size is 10MB.")

    try:
        image = Image.open(__import__("io").BytesIO(raw_bytes))
        image.load()
    except UnidentifiedImageError:
        raise InvalidImageError("The uploaded file isn't a valid image.")

    filename = _save_upload(file, raw_bytes)

    # --- Leaf gate: reject non-leaf images before wasting a disease
    if leaf_gate_service is not None:
        is_leaf, leaf_score = leaf_gate_service.is_leaf(image)
        if not is_leaf:
            prediction = Prediction(
                user_id=user.id,
                image_url=f"/uploads/{filename}",
                disease_name=NOT_A_LEAF_LABEL,
                confidence=leaf_score,
                top_predictions=json.dumps([]),
            )
            db.add(prediction)
            db.commit()
            db.refresh(prediction)
            return prediction, get_disease_info(NOT_A_LEAF_LABEL)

    result = model_service.predict(image, top_k=3)

    prediction = Prediction(
        user_id=user.id,
        image_url=f"/uploads/{filename}",
        disease_name=result["disease_name"],
        confidence=result["confidence"],
        top_predictions=json.dumps(result["top_predictions"]),
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    info = get_disease_info(prediction.disease_name)
    return prediction, info


def list_history(db: Session, user: User) -> list[Prediction]:
    return (
        db.query(Prediction)
        .filter(Prediction.user_id == user.id)
        .order_by(Prediction.created_at.desc())
        .all()
    )


def delete_prediction(db: Session, user: User, prediction_id: str) -> bool:
    prediction = (
        db.query(Prediction)
        .filter(Prediction.id == prediction_id, Prediction.user_id == user.id)
        .first()
    )
    if not prediction:
        return False
    db.delete(prediction)
    db.commit()
    return True
