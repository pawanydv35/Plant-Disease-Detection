"""
AlexNet inference logic.

IMPORTANT — fill in CLASS_NAMES below with your model's exact ordered
class list before deploying. If you trained with
`torchvision.datasets.ImageFolder`, this is `train_dataset.classes`
in your training script (alphabetically sorted folder names). You can
also run `inspect_checkpoint.py` against your model.pth to see if the
class list was saved inside the checkpoint itself.

The number of output classes does NOT need to be hardcoded here — it's
inferred automatically from the shape of the final classifier layer in
your saved state_dict, so the architecture always matches your weights.
"""

import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

from model.disease_info import NOT_A_LEAF_LABEL

# --- 1. Fill this in with your real class names, in the SAME ORDER
#     used during training. Placeholder values below will make
#     predictions run, but the disease names will be meaningless
#     until you replace this list. ---
CLASS_NAMES: list[str] = [
    # "Apple___Apple_scab",
    # "Apple___Black_rot",
    # ... replace with your real, ordered class list
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
