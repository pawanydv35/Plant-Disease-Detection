"""
Thin wrapper around model/predict.py so main.py's lifespan hook can
load the model ONCE and store it on app.state, instead of every
request re-reading model.pth from disk (which would be slow and
would defeat the purpose of a "load once at startup" design).
"""

import sys
from pathlib import Path

# model/ lives outside the app/ package, so we add backend/ to the
# import path and import predict.py directly by file path.
_BACKEND_ROOT = Path(__file__).resolve().parents[2]
if str(_BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(_BACKEND_ROOT))

from model.predict import load_model, predict_image  # noqa: E402


class ModelService:
    def __init__(self, model_path: str):
        full_path = _BACKEND_ROOT / model_path
        if not full_path.exists():
            raise FileNotFoundError(
                f"Model file not found at {full_path}. "
                "Place your trained .pth file at backend/model/model.pth."
            )
        self.model, self.num_classes = load_model(str(full_path))

    def predict(self, image, top_k: int = 3) -> dict:
        return predict_image(self.model, image, top_k=top_k)
