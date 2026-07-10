"""
Single shared declarative Base.

Kept in its own file (rather than defined in session.py or a model file)
so that any model module can `from app.models.base import Base` without
circular imports back to database/session.py.
"""

from sqlalchemy.orm import declarative_base

Base = declarative_base()
