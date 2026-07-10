"""
This file will hold the low-level model loading + inference logic.

PLACEHOLDER — implemented fully in the "Model Integration" step, where
we will need YOU to tell us:
  1. What architecture the model uses (custom CNN? ResNet/EfficientNet
     backbone? something from timm?) — we need this to reconstruct the
     model class before loading state_dict from the .pth file.
  2. The exact image size / normalization used during training
     (e.g. 224x224, ImageNet mean/std, or custom).
  3. The ordered list of class names the model was trained on, so
     predictions map back to real disease labels.

Put your model.pth file in this folder (backend/model/model.pth).
"""
