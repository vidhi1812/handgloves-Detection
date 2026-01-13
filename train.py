# train_yolov11.py
import os
import requests
from ultralytics import YOLO

DATA_YAML = r"dataset\data.yaml"
WEIGHTS = "yolov8n.pt"
# Hugging Face "resolve" URL for Ultralytics/YOLO11 repo
HF_URL = "https://huggingface.co/Ultralytics/YOLO11/resolve/main/yolo8n.pt"

def download_if_missing(path, url):
    if os.path.exists(path):
        print(f"[INFO] Found weights -> {path}")
        return path
    print(f"[INFO] Downloading weights from Hugging Face: {url}")
    try:
        r = requests.get(url, stream=True, timeout=120)
        r.raise_for_status()
        with open(path, "wb") as f:
            for chunk in r.iter_content(8192):
                if chunk:
                    f.write(chunk)
        print(f"[SUCCESS] Saved weights -> {path}")
        return path
    except Exception as e:
        print(f"[ERROR] download failed: {e}")
        return None

weights_src = download_if_missing(WEIGHTS, HF_URL)
if weights_src is None:
    # fallback: try ultralytics auto-download (only works if ultralytics supports it)
    print("[INFO] Falling back to ultralytics auto-download (YOLO('yolov8n))")
    weights_src = "yolov8n"

# create model and train
model = YOLO(weights_src)
model.train(
    data=DATA_YAML,
    epochs=50,
    imgsz=640,
    batch=16,
    project="runs/train",
    name="ppe_yolov11s",
    patience=50,
    lr0=0.01,
    pretrained=True,
    optimizer="SGD",
    workers=8,
    device='cpu'
)