"""
Centralized settings loader.

Using pydantic-settings means every config value (secrets, DB URL, CORS
origins, JWT settings) is read from environment variables in ONE place,
validated, and typed — instead of scattering os.getenv() calls across
the codebase. This will be filled in fully in the "Auth + Config" step.
"""

from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- General ---
    ENV: str = "development"

    # --- CORS ---
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]

    # --- Database (filled in during DB step) ---
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/plant_disease_db"

    # --- JWT (filled in during Auth step) ---
    JWT_SECRET_KEY: str = "changeme"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # --- Model ---
    MODEL_PATH: str = "model/model.pth"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    """Cached so the .env file is parsed once, not on every request."""
    return Settings()
