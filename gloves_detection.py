import os
import cv2
from ultralytics import YOLO


MODEL_PATH = r"runs\detect\runs\train\ppe_yolov8n\weights\last.pt"
INPUT_PATH = "input_images"  
OUTPUT_PATH = "output_images"

CONF_THRESHOLD = 0.49
IOU_THRESHOLD = 0.45


os.makedirs(OUTPUT_PATH, exist_ok=True)

model = YOLO(MODEL_PATH)

def detect_gloves(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f" Could not read image: {image_path}")
        return

    h, w, _ = img.shape

    results = model(
        img,
        conf=CONF_THRESHOLD,
        iou=IOU_THRESHOLD,
        verbose=False
    )

    boxes = results[0].boxes
    gloves_boxes = []

   
    if boxes is not None:
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            class_name = model.names[cls_id]

            if class_name.lower() == "gloves":
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                gloves_boxes.append((x1, y1, x2, y2, conf))

    if gloves_boxes:
        
        for x1, y1, x2, y2, conf in gloves_boxes:
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                img,
                f"Gloves {conf:.2f}",
                (x1, y1 - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        status = "GLOVES"
        status_color = (0, 255, 0)

    else:
       
        margin = 40
        x1, y1 = margin, margin
        x2, y2 = w - margin, h - margin

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
        cv2.putText(
            img,
            "NO GLOVES",
            (x1 + 10, y1 + 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

        status = "NO GLOVES"
        status_color = (0, 0, 255)

    cv2.putText(
        img,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        status_color,
        3
    )

    out_path = os.path.join(OUTPUT_PATH, os.path.basename(image_path))
    cv2.imwrite(out_path, img)

    print(f"{os.path.basename(image_path)} → {status}")


if os.path.isdir(INPUT_PATH):
    for file in os.listdir(INPUT_PATH):
        if file.lower().endswith((".jpg", ".png", ".jpeg")):
            detect_gloves(os.path.join(INPUT_PATH, file))
else:
    detect_gloves(INPUT_PATH)

import os
import cv2
from ultralytics import YOLO


MODEL_PATH = r"runs\detect\runs\train\ppe_yolov11s\weights\last.pt"
INPUT_PATH = "input_images"  
OUTPUT_PATH = "output_images"

CONF_THRESHOLD = 0.49
IOU_THRESHOLD = 0.45


os.makedirs(OUTPUT_PATH, exist_ok=True)

model = YOLO(MODEL_PATH)

def detect_gloves(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f" Could not read image: {image_path}")
        return

    h, w, _ = img.shape

    results = model(
        img,
        conf=CONF_THRESHOLD,
        iou=IOU_THRESHOLD,
        verbose=False
    )

    boxes = results[0].boxes
    gloves_boxes = []

    # --------- Check gloves --------- #
    if boxes is not None:
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            class_name = model.names[cls_id]

            if class_name.lower() == "gloves":
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                gloves_boxes.append((x1, y1, x2, y2, conf))

    # --------- DRAWING --------- #
    if gloves_boxes:
        
        for x1, y1, x2, y2, conf in gloves_boxes:
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                img,
                f"Gloves {conf:.2f}",
                (x1, y1 - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        status = "GLOVES"
        status_color = (0, 255, 0)

    else:
       
        margin = 40
        x1, y1 = margin, margin
        x2, y2 = w - margin, h - margin

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
        cv2.putText(
            img,
            "NO GLOVES",
            (x1 + 10, y1 + 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

        status = "NO GLOVES"
        status_color = (0, 0, 255)

    cv2.putText(
        img,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        status_color,
        3
    )

    out_path = os.path.join(OUTPUT_PATH, os.path.basename(image_path))
    cv2.imwrite(out_path, img)

    print(f"{os.path.basename(image_path)} → {status}")


if os.path.isdir(INPUT_PATH):
    for file in os.listdir(INPUT_PATH):
        if file.lower().endswith((".jpg", ".png", ".jpeg")):
            detect_gloves(os.path.join(INPUT_PATH, file))
else:
    detect_gloves(INPUT_PATH)
