import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.base import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    image_url = Column(String, nullable=False)       # where the uploaded image is stored
    disease_name = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)        # 0.0 - 1.0
    top_predictions = Column(String, nullable=True)   # JSON-encoded list of {label, confidence}

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="predictions")
