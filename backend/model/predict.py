import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

from model.disease_info import NOT_A_LEAF_LABEL

# --- 1. Standard PlantVillage / "New Plant Diseases Dataset" 38-class
CLASS_NAMES: list[str] = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]

# Standard ImageNet preprocessing — matches "224x224 with ImageNet
# normalization" as confirmed for this project.
_TRANSFORM = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


# Below this confidence, we treat the prediction as unreliable rather
LOW_CONFIDENCE_THRESHOLD = 0.40


def _infer_num_classes(state_dict: dict) -> int:
    final_weight_key = "classifier.6.weight"
    if final_weight_key not in state_dict:
        raise ValueError(
            f"Could not find '{final_weight_key}' in the checkpoint. "
            "This usually means the state_dict keys don't match a plain "
            "torchvision AlexNet — check inspect_checkpoint.py output."
        )
    return state_dict[final_weight_key].shape[0]


def build_model(num_classes: int) -> nn.Module:

    model = models.alexnet(weights=None)
    model.classifier[6] = nn.Linear(4096, num_classes)
    return model


def load_model(model_path: str) -> tuple[nn.Module, int]:
    checkpoint = torch.load(model_path, map_location="cpu")

    if isinstance(checkpoint, dict) and "classifier.6.weight" not in checkpoint:
        state_dict = checkpoint.get("state_dict") or checkpoint.get("model_state_dict") or checkpoint
    else:
        state_dict = checkpoint

    num_classes = _infer_num_classes(state_dict)
    model = build_model(num_classes)
    model.load_state_dict(state_dict)
    model.eval()
    return model, num_classes


def predict_image(model: nn.Module, image: Image.Image, top_k: int = 3) -> dict:
    tensor = _TRANSFORM(image.convert("RGB")).unsqueeze(0)  # add batch dim

    with torch.no_grad():
        logits = model(tensor)
        probabilities = torch.softmax(logits, dim=1)[0]

    top_probs, top_indices = torch.topk(probabilities, k=min(top_k, probabilities.shape[0]))

    def label_for(idx: int) -> str:
        if CLASS_NAMES and idx < len(CLASS_NAMES):
            return CLASS_NAMES[idx]
        return f"class_{idx}"  # fallback until CLASS_NAMES is filled in

    top_predictions = [
        {"label": label_for(idx.item()), "confidence": prob.item()}
        for prob, idx in zip(top_probs, top_indices)
    ]

    is_uncertain = top_predictions[0]["confidence"] < LOW_CONFIDENCE_THRESHOLD

    return {
        "disease_name": NOT_A_LEAF_LABEL if is_uncertain else top_predictions[0]["label"],
        "confidence": top_predictions[0]["confidence"],
        "top_predictions": top_predictions,
        "is_uncertain": is_uncertain,
    }