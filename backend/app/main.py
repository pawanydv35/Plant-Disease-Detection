from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path

from fastapi.staticfiles import StaticFiles

from app.utils.config import get_settings
from app.database.session import init_db
from app.routes import auth_routes, profile_routes, predict_routes, history_routes
from app.services.model_service import ModelService
from app.services.leaf_gate_service import LeafGateService

settings = get_settings()
UPLOAD_DIR = Path(__file__).resolve().parents[1] / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup ---
    init_db()
    try:
        app.state.model_service = ModelService(model_path=settings.MODEL_PATH)
        print(f"Model loaded successfully ({app.state.model_service.num_classes} classes).")
    except FileNotFoundError as e:
        print(f"WARNING: {e}")
        app.state.model_service = None

    try:
        app.state.leaf_gate_service = LeafGateService()
        print("Leaf gate (CLIP) loaded successfully.")
    except Exception as e:
        print(f"WARNING: Leaf gate failed to load: {e}")
        app.state.leaf_gate_service = None

    yield
    # --- Shutdown ---


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


app.mount("/uploads", StaticFiles(directory=str(UPLOAD_DIR)), name="uploads")
