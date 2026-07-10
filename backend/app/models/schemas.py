"""
Pydantic schemas (request/response shapes) — kept separate from the
SQLAlchemy ORM models in app/models/*.py.

Why separate: ORM models describe DB tables (can have sensitive fields
like hashed_password). Schemas describe what the API accepts/returns,
so we never accidentally leak a password hash in a JSON response.
"""

import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class SignupRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # allows creation directly from ORM objects


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut


class TopPrediction(BaseModel):
    label: str
    confidence: float


class PredictResponse(BaseModel):
    id: uuid.UUID
    disease_name: str
    confidence: float
    top_predictions: list[TopPrediction]
    image_url: str
    created_at: datetime


class PredictionOut(BaseModel):
    id: uuid.UUID
    disease_name: str
    confidence: float
    image_url: str
    created_at: datetime

    class Config:
        from_attributes = True
