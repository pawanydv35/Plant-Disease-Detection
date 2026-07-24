import sys
import torch


def main(path: str):
    checkpoint = torch.load(path, map_location="cpu")

    if isinstance(checkpoint, dict) and "state_dict" not in checkpoint and not any(
        isinstance(v, torch.Tensor) for v in checkpoint.values()
    ):
        print("Checkpoint is a plain dict with these top-level keys:")
        print(list(checkpoint.keys()))
        for key in ("classes", "class_names", "labels", "idx_to_class"):
            if key in checkpoint:
                print(f"\nFound '{key}':")
                print(checkpoint[key])
        state_dict = checkpoint.get("state_dict") or checkpoint.get("model_state_dict") or checkpoint
    else:
        print("Checkpoint looks like a raw state_dict (no extra metadata saved).")
        state_dict = checkpoint

    print("\n--- Layer shapes (look at the LAST layer for output class count) ---")
    for name, tensor in state_dict.items():
        if hasattr(tensor, "shape"):
            print(f"{name}: {tuple(tensor.shape)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inspect_checkpoint.py path/to/model.pth")
        sys.exit(1)
    main(sys.argv[1])
