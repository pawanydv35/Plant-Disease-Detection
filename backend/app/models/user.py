"""
User table.

Password is stored ONLY as a bcrypt hash (`hashed_password`) — the
plaintext password is never persisted anywhere, including logs.
"""

import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    predictions = relationship(
        "Prediction", back_populates="user", cascade="all, delete-orphan"
    )
