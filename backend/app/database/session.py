from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.utils.config import get_settings
from app.models.base import Base

settings = get_settings()


engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db() -> None:
    from app.models import user, prediction  # noqa: F401

    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
