"""
Disease knowledge base.

Keys MUST match the exact strings in predict.py's CLASS_NAMES list —
this is how a prediction result gets matched to its causes/symptoms/
treatment/prevention text.

TEMPLATE ONLY — replace the example keys below with your actual class
names once you've filled in CLASS_NAMES in predict.py, and write real
content for each. Any class not found here falls back to a generic
"not available" message (handled in prediction_service.py), so the
app won't crash if you haven't filled in every class yet — it'll just
show incomplete info for classes you haven't documented.
"""

NOT_A_LEAF_LABEL = "Unrecognized — doesn't look like a clear leaf photo"

DISEASE_INFO: dict[str, dict[str, str]] = {
    # --- EXAMPLE ENTRY — copy this shape for each of your real classes ---
    # "Apple___Apple_scab": {
    #     "causes": "Caused by the fungus Venturia inaequalis, which "
    #               "overwinters in fallen leaves and spreads via spores "
    #               "during wet spring weather.",
    #     "symptoms": "Olive-green to black velvety spots on leaves and "
    #                 "fruit, often with a scabby, rough texture.",
    #     "treatment": "Remove and destroy fallen leaves each autumn. "
    #                  "Apply a fungicide labeled for apple scab starting "
    #                  "at bud break and repeating on a 7-10 day schedule "
    #                  "during wet periods.",
    #     "prevention": "Choose scab-resistant apple varieties, prune for "
    #                   "good air circulation, and avoid overhead watering "
    #                   "that keeps foliage wet.",
    # },
    NOT_A_LEAF_LABEL: {
        "causes": "The model's top confidence for this image was below the "
                  "reliability threshold, meaning it doesn't closely "
                  "resemble any of the trained disease classes.",
        "symptoms": "N/A — no diagnosis was reliable enough to report.",
        "treatment": "Try a clearer photo: fill most of the frame with a "
                     "single leaf, use natural daylight, and avoid heavy "
                     "shadows or blur.",
        "prevention": "N/A",
    },
}


DEFAULT_INFO = {
    "causes": "Detailed information for this class hasn't been added yet.",
    "symptoms": "Detailed information for this class hasn't been added yet.",
    "treatment": "Detailed information for this class hasn't been added yet.",
    "prevention": "Detailed information for this class hasn't been added yet.",
}


def get_disease_info(disease_name: str) -> dict[str, str]:
    return DISEASE_INFO.get(disease_name, DEFAULT_INFO)
