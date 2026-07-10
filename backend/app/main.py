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

from pathlib import Path

from fastapi.staticfiles import StaticFiles

from app.utils.config import get_settings
from app.database.session import init_db
from app.routes import auth_routes, profile_routes, predict_routes, history_routes
from app.services.model_service import ModelService

settings = get_settings()
UPLOAD_DIR = Path(__file__).resolve().parents[1] / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


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
    init_db()
    try:
        app.state.model_service = ModelService(model_path=settings.MODEL_PATH)
        print(f"Model loaded successfully ({app.state.model_service.num_classes} classes).")
    except FileNotFoundError as e:
        # Let the app boot anyway so /health, /signup, /login still work
        # while you're setting up the model file — /predict will 503 until fixed.
        print(f"WARNING: {e}")
        app.state.model_service = None
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
app.include_router(predict_routes.router, prefix="", tags=["prediction"])
app.include_router(history_routes.router, prefix="/history", tags=["history"])

# Serves uploaded leaf images back to the frontend at /uploads/<filename>
app.mount("/uploads", StaticFiles(directory=str(UPLOAD_DIR)), name="uploads")
