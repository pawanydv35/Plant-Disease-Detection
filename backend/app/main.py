"""
Plant Disease Detection API — application entrypoint.

Responsibilities of this file ONLY:
  - Create the FastAPI app instance
  - Configure middleware (CORS, etc.)
  - Load the PyTorch model ONCE at startup (via services.model_service)
  - Register routers from app/routes/
  - Expose a health check endpoint

Everything else (business logic, DB access, inference) lives in
services/, models/, auth/, database/ — main.py should stay thin.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.utils.config import get_settings
from app.database.session import init_db
from app.routes import auth_routes, profile_routes

# NOTE: these will be implemented in the model-integration and history steps.
# from app.services.model_service import ModelService
# from app.routes import predict_routes, history_routes

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup/shutdown hook.

    Why lifespan instead of @app.on_event("startup"):
    on_event is deprecated in modern FastAPI; lifespan is the
    recommended way to run startup/shutdown code exactly once.

    This is where the PyTorch model gets loaded into memory ONE time,
    then stored on app.state so every request reuses it instead of
    re-loading the .pth file per request (which would be very slow).
    """
    # --- Startup ---
    # app.state.model_service = ModelService(model_path="model/model.pth")
    init_db()
    yield
    # --- Shutdown ---
    # (cleanup goes here if ever needed, e.g. closing DB pools)


app = FastAPI(
    title="Plant Disease Detection API",
    description="Upload a plant leaf image and get a disease prediction with treatment guidance.",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS: frontend (Vercel) and backend (Render) live on different origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,  # e.g. ["http://localhost:5173", "https://yourapp.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["system"])
def health_check():
    """Simple liveness check used by Render + uptime monitors."""
    return {"status": "ok"}


app.include_router(auth_routes.router, prefix="", tags=["auth"])
app.include_router(profile_routes.router, prefix="/profile", tags=["profile"])

# Wired up in later steps:
# app.include_router(predict_routes.router, prefix="", tags=["prediction"])
# app.include_router(history_routes.router, prefix="/history", tags=["history"])
