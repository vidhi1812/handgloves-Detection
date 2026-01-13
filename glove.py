import cv2
from ultralytics import YOLO

# ================= CONFIG ================= #
MODEL_PATH = r"runs\detect\runs\train\ppe_yolov11s\weights\last.pt"

CONF_THRESHOLD = 0.49
IOU_THRESHOLD = 0.45
CAMERA_ID = 0   # 0 = default webcam
# ========================================== #

# Load model
model = YOLO(MODEL_PATH)

# Open webcam
cap = cv2.VideoCapture(CAMERA_ID)

if not cap.isOpened():
    print("❌ Webcam not accessible")
    exit()

print("🎥 Webcam started — Press 'q' to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    results = model(
        frame,
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
        # ✅ Gloves → GREEN box
        for x1, y1, x2, y2, conf in gloves_boxes:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
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
        # ❌ No gloves → RED box (hand region approx)
        margin = 40
        cv2.rectangle(
            frame,
            (margin, margin),
            (w - margin, h - margin),
            (0, 0, 255),
            3
        )

        cv2.putText(
            frame,
            "NO GLOVES",
            (margin + 10, margin + 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

        status = "NO GLOVES"
        status_color = (0, 0, 255)

    # --------- STATUS LABEL --------- #
    cv2.putText(
        frame,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        status_color,
        3
    )

    cv2.imshow("Gloves Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

import cv2
from ultralytics import YOLO

# ================= CONFIG ================= #
MODEL_PATH = r"runs\detect\runs\train\ppe_yolov11s\weights\last.pt"

CONF_THRESHOLD = 0.49
IOU_THRESHOLD = 0.45
CAMERA_ID = 0   # 0 = default webcam
# ========================================== #

# Load model
model = YOLO(MODEL_PATH)

# Open webcam
cap = cv2.VideoCapture(CAMERA_ID)

if not cap.isOpened():
    print("❌ Webcam not accessible")
    exit()

print("🎥 Webcam started — Press 'q' to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    results = model(
        frame,
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
        # ✅ Gloves → GREEN box
        for x1, y1, x2, y2, conf in gloves_boxes:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
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
        # ❌ No gloves → RED box (hand region approx)
        margin = 40
        cv2.rectangle(
            frame,
            (margin, margin),
            (w - margin, h - margin),
            (0, 0, 255),
            3
        )

        cv2.putText(
            frame,
            "NO GLOVES",
            (margin + 10, margin + 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

        status = "NO GLOVES"
        status_color = (0, 0, 255)

    # --------- STATUS LABEL --------- #
    cv2.putText(
        frame,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        status_color,
        3
    )

    cv2.imshow("Gloves Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
