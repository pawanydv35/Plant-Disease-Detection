"""
Database engine + session management.

Why a dependency (`get_db`) instead of a global session: each request
gets its own SQLAlchemy session that is opened at the start of the
request and closed at the end, even if an error occurs. Sharing one
global session across requests would cause data leaking between users
under concurrent load.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.utils.config import get_settings
from app.models.base import Base

settings = get_settings()

# pool_pre_ping avoids "SSL connection has been closed unexpectedly"
# errors on managed Postgres instances (like Render) after idle periods.
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db() -> None:
    """
    Create tables if they don't exist yet.

    NOTE: this is fine for getting started, but for a real production
    app you'd switch to Alembic migrations (already in requirements.txt)
    so schema changes are versioned instead of silently auto-created.
    """
    # Import models here so they're registered on Base.metadata
    # before create_all() runs.
    from app.models import user, prediction  # noqa: F401

    Base.metadata.create_all(bind=engine)


def get_db():
    """FastAPI dependency: yields a DB session, always closes it after."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
