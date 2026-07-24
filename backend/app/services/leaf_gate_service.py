import torch
from transformers import CLIPModel, CLIPProcessor
from PIL import Image

_MODEL_NAME = "openai/clip-vit-base-patch32"

# Multiple phrasings per side improves robustness vs. a single prompt.
LEAF_PROMPTS = [
    "a close-up photo of a plant leaf",
    "a photo of a green leaf",
    "a photo of a leaf with disease spots or damage",
]
NOT_LEAF_PROMPTS = [
    "a photo of a person",
    "a photo of an animal",
    "a photo of a random object, not a plant",
    "a photo of food",
    "a blank or unclear image",
]

# How much combined leaf-prompt probability is required to accept the
# image as a leaf. Tune this based on real testing — start conservative.
LEAF_ACCEPT_THRESHOLD = 0.55


class LeafGateService:
    def __init__(self):
        self.model = CLIPModel.from_pretrained(_MODEL_NAME)
        self.processor = CLIPProcessor.from_pretrained(_MODEL_NAME)
        self.model.eval()
        self._prompts = LEAF_PROMPTS + NOT_LEAF_PROMPTS
        self._num_leaf_prompts = len(LEAF_PROMPTS)

    def is_leaf(self, image: Image.Image) -> tuple[bool, float]:
       
        inputs = self.processor(
            text=self._prompts,
            images=image.convert("RGB"),
            return_tensors="pt",
            padding=True,
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = outputs.logits_per_image.softmax(dim=1)[0]

        leaf_score = probs[: self._num_leaf_prompts].sum().item()
        return leaf_score >= LEAF_ACCEPT_THRESHOLD, leaf_score
