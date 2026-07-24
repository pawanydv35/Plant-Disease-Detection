import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

from model.disease_info import NOT_A_LEAF_LABEL

# --- 1. Standard PlantVillage / "New Plant Diseases Dataset" 38-class
CLASS_NAMES: list[str] = [
   "Apple: Apple Scab",
"Apple: Black Rot",
"Apple: Cedar Apple Rust",
"Apple: Healthy",
"Blueberry: Healthy",
"Cherry (Including Sour): Powdery Mildew",
"Cherry (Including Sour): Healthy",
"Corn (Maize): Cercospora Leaf Spot (Gray Leaf Spot)",
"Corn (Maize): Common Rust",
"Corn (Maize): Northern Leaf Blight",
"Corn (Maize): Healthy",
"Grape: Black Rot",
"Grape: Esca (Black Measles)",
"Grape: Leaf Blight (Isariopsis Leaf Spot)",
"Grape: Healthy",
"Orange: Huanglongbing (Citrus Greening)",
"Peach: Bacterial Spot",
"Peach: Healthy",
"Bell Pepper: Bacterial Spot",
"Bell Pepper: Healthy",
"Potato: Early Blight",
"Potato: Late Blight",
"Potato: Healthy",
"Raspberry: Healthy",
"Soybean: Healthy",
"Squash: Powdery Mildew",
"Strawberry: Leaf Scorch",
"Strawberry: Healthy",
"Tomato: Bacterial Spot",
"Tomato: Early Blight",
"Tomato: Late Blight",
"Tomato: Leaf Mold",
"Tomato: Septoria Leaf Spot",
"Tomato: Spider Mites (Two-Spotted Spider Mite)",
"Tomato: Target Spot",
"Tomato: Tomato Yellow Leaf Curl Virus",
"Tomato: Tomato Mosaic Virus",
"Tomato: Healthy"
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