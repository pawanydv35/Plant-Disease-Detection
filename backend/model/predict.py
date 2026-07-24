"""
AlexNet inference logic.

CLASS_NAMES below was inferred, not read from the checkpoint: running
inspect_checkpoint.py on plant_disease_alexnet.pth showed a raw
state_dict (no "classes" metadata saved) with a classifier.6 output
shape of (38, 4096) — i.e. 38 output classes. That count/architecture
combination (AlexNet, 38 classes) matches the widely-used PlantVillage
/ "New Plant Diseases Dataset" leaf-disease dataset, so the list below
is that dataset's standard alphabetical ImageFolder class order.

⚠️ VERIFY THIS before trusting predictions: if this model was trained
on a *different* 38-class dataset, or on PlantVillage with a different
train/val split tool that didn't sort alphabetically, this list will
be wrong and predictions will silently point to the wrong disease. The
only way to be 100% sure is to check `train_dataset.classes` from your
own training script and confirm it matches the order below.

The number of output classes does NOT need to be hardcoded here — it's
inferred automatically from the shape of the final classifier layer in
your saved state_dict, so the architecture always matches your weights.
"""

import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

from model.disease_info import NOT_A_LEAF_LABEL

# --- 1. Standard PlantVillage / "New Plant Diseases Dataset" 38-class
#     list, alphabetically sorted (ImageFolder default). See the
#     module docstring above for why this order was chosen and how
#     to double check it against your own training script. ---
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
# than showing a specific (likely wrong) disease name. This is a
# heuristic, NOT true "is this a leaf?" detection — the model was only
# ever trained to choose among your disease classes, so it has no real
# concept of "not a leaf." A low top confidence usually means the image
# doesn't resemble any training class well, which is the closest signal
# we have without training a separate leaf/not-leaf classifier.
LOW_CONFIDENCE_THRESHOLD = 0.40


def _infer_num_classes(state_dict: dict) -> int:
    """AlexNet's final layer is classifier.6 (a Linear layer)."""
    final_weight_key = "classifier.6.weight"
    if final_weight_key not in state_dict:
        raise ValueError(
            f"Could not find '{final_weight_key}' in the checkpoint. "
            "This usually means the state_dict keys don't match a plain "
            "torchvision AlexNet — check inspect_checkpoint.py output."
        )
    return state_dict[final_weight_key].shape[0]


def build_model(num_classes: int) -> nn.Module:
    """
    Recreate the AlexNet architecture with `weights=None` (we're loading
    our own trained weights, not ImageNet pretrained ones), and replace
    the final layer to output `num_classes` instead of AlexNet's
    default 1000 ImageNet classes.
    """
    model = models.alexnet(weights=None)
    model.classifier[6] = nn.Linear(4096, num_classes)
    return model


def load_model(model_path: str) -> tuple[nn.Module, int]:
    checkpoint = torch.load(model_path, map_location="cpu")

    # Handle both "raw state_dict" and "{'state_dict': ...}" /
    # "{'model_state_dict': ...}" save formats.
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
    """
    Runs inference on a single PIL image.

    Returns:
        {
            "disease_name": str,
            "confidence": float,          # 0-1
            "top_predictions": [{"label": str, "confidence": float}, ...]
        }
    """
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