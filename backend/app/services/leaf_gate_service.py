"""
"Is this actually a leaf?" gate, using CLIP (openai/clip-vit-base-patch32)
for zero-shot image classification.

WHY CLIP INSTEAD OF A THRESHOLD ON THE DISEASE MODEL:
Your AlexNet disease classifier was only ever trained to choose among
your 3 disease classes — it has no real concept of "not a leaf" and
will confidently misclassify a photo of a dog as some disease. CLIP,
on the other hand, was trained on hundreds of millions of image-text
pairs and genuinely understands what "a plant leaf" looks like versus
everything else, with zero extra training required from you.

HOW IT WORKS:
We give CLIP the image plus a few candidate text descriptions, and it
scores how well the image matches each one. If "a photo of a plant
leaf" scores higher than the "not a leaf" descriptions by enough
margin, we call it a leaf and proceed to the disease model. Otherwise
we short-circuit and tell the user their image doesn't look like a
plant leaf — without running (and getting a bogus answer from) the
disease classifier at all.

FIRST RUN NOTE: the CLIP model (~600MB) downloads automatically from
Hugging Face the first time this runs, and is cached locally after
that. This requires internet access on first startup only.
"""

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
        """
        Returns (is_leaf, leaf_score) where leaf_score is the combined
        probability mass assigned to the leaf-side prompts (0-1).
        """
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
