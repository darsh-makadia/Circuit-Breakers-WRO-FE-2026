import cv2
import numpy as np
import time
from picamera2 import Picamera2


# ============================================================
# CAMERA / ROI
# ============================================================

WIDTH = 1480
HEIGHT = 520
FPS = 60

X_MID = WIDTH // 2

ROI_FROM_BOTTOM = 120
ROI_Y = HEIGHT - ROI_FROM_BOTTOM


# ============================================================
# DETECTION SETTINGS
# ============================================================

MIN_AREA = 120
MIN_CONFIDENCE = 0.55

HSV_WEIGHT = 0.65
LAB_WEIGHT = 0.20
GEOMETRY_WEIGHT = 0.15


# ============================================================
# COLORS - BGR
# ============================================================

WHITE = (255, 255, 255)
YELLOW = (0, 255, 255)

DRAW_COLORS = {
    "RED": (0, 0, 255),
    "GREEN": (0, 255, 0),
    "MAGENTA": (255, 0, 255),
    "BLUE": (255, 0, 0),
    "ORANGE": (0, 165, 255),
    "BLACK": (80, 80, 80),
}


# ============================================================
# HSV RANGES
# ============================================================

HSV_RANGES = {
    "RED": (np.array([0, 120, 70]), np.array([14, 230, 180])),
    "ORANGE": (np.array([14, 140, 135]), np.array([29, 240, 240])),
    "GREEN": (np.array([50, 90, 65]), np.array([70, 190, 175])),
    "BLUE": (np.array([98, 160, 70]), np.array([118, 255, 185])),
    "MAGENTA": (np.array([158, 170, 70]), np.array([179, 255, 190])),
    "BLACK": (np.array([0, 0, 0]), np.array([179, 170, 65])),
}


# ============================================================
# LAB REFERENCE
# ============================================================

LAB_REFERENCE = {
    "RED": {"L": 81, "A": 156, "B": 151},
    "ORANGE": {"L": 160, "A": 135, "B": 180},
    "GREEN": {"L": 106, "A": 95, "B": 155},
    "BLUE": {"L": 65, "A": 140, "B": 88},
    "MAGENTA": {"L": 69, "A": 176, "B": 131},
    "BLACK": {"L": 34, "A": 121, "B": 132},
}


LAB_TOLERANCE = {
    "RED": {"L": 55, "A": 30, "B": 30},
    "ORANGE": {"L": 55, "A": 30, "B": 35},
    "GREEN": {"L": 50, "A": 30, "B": 30},
    "BLUE": {"L": 50, "A": 30, "B": 30},
    "MAGENTA": {"L": 55, "A": 30, "B": 30},
    "BLACK": {"L": 40, "A": 35, "B": 35},
}


MORPH_KERNEL = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# ============================================================
# CAMERA
# ============================================================

def start_camera():
    camera = Picamera2(0)
    config = camera.create_video_configuration(main={"size": (WIDTH, HEIGHT), "format": "RGB888"}, controls={"FrameRate": FPS})
    camera.configure(config)
    camera.start()
    time.sleep(2)

    print("Front camera started.")
    return camera

# ============================================================
# MASK
# ============================================================

def clean_mask(mask):
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, MORPH_KERNEL)
    return cv2.morphologyEx(mask, cv2.MORPH_CLOSE, MORPH_KERNEL)


# ============================================================
# GEOMETRY SCORE
# ============================================================

def geometry_score(contour, w, h):
    rectangularity = cv2.contourArea(contour) / float(max(1, w * h))

    if rectangularity >= 0.70:
        return 1.0
    if rectangularity >= 0.50:
        return 0.75
    if rectangularity >= 0.35:
        return 0.50

    return 0.25


# ============================================================
# HSV SCORE
# ============================================================

def get_hsv_score(mask, x, y, w, h):
    roi = mask[y:y + h, x:x + w]

    if roi.size == 0:
        return 0.0

    coverage = cv2.countNonZero(roi) / float(max(1, w * h))
    return float(np.clip(coverage / 0.30, 0.0, 1.0))


# ============================================================
# LAB SCORE
# ============================================================

def get_lab_score(frame, x, y, w, h, color):
    pad = 2

    x1 = max(0, x - pad)
    y1 = max(0, y - pad)
    x2 = min(frame.shape[1], x + w + pad)
    y2 = min(frame.shape[0], y + h + pad)

    roi = frame[y1:y2, x1:x2]

    if roi.size == 0:
        return 0.5

    lab = cv2.cvtColor(roi, cv2.COLOR_BGR2LAB)

    L = float(np.median(lab[:, :, 0]))
    A = float(np.median(lab[:, :, 1]))
    B = float(np.median(lab[:, :, 2]))

    ref = LAB_REFERENCE[color]
    tol = LAB_TOLERANCE[color]

    dL = abs(L - ref["L"]) / tol["L"]
    dA = abs(A - ref["A"]) / tol["A"]
    dB = abs(B - ref["B"]) / tol["B"]

    difference = (dL + dA + dB) / 3.0
    return float(np.clip(1.0 - difference, 0.0, 1.0))


# ============================================================
# DETECT ONE COLOR
# ============================================================

def detect_class(roi_frame, hsv, color):
    lower, upper = HSV_RANGES[color]

    mask = cv2.inRange(hsv, lower, upper)
    mask = clean_mask(mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for contour in contours:
        area = cv2.contourArea(contour)

        if area < MIN_AREA:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        if w <= 0 or h <= 0:
            continue

        hsv_score = get_hsv_score(mask, x, y, w, h)
        lab_score = get_lab_score(roi_frame, x, y, w, h, color)
        geo_score = geometry_score(contour, w, h)

        confidence = HSV_WEIGHT * hsv_score + LAB_WEIGHT * lab_score + GEOMETRY_WEIGHT * geo_score

        if confidence < MIN_CONFIDENCE:
            continue

        detections.append({
            "color": color,
            "x": x,
            "y": y,
            "w": w,
            "h": h,
            "cx": x + w // 2,
            "cy": y + h // 2,
            "area": area,
            "confidence": confidence,
        })

    return detections


# ============================================================
# DETECT ALL COLORS
# ============================================================

def detect_all(frame):
    roi_frame = frame[0:ROI_Y, 0:WIDTH]
    hsv = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2HSV)

    detections = {}

    for color in ["RED", "GREEN", "BLACK", "BLUE", "ORANGE", "MAGENTA"]:
        detections[color] = detect_class(roi_frame, hsv, color)

    return detections


# ============================================================
# LARGEST DETECTION
# ============================================================

def largest_detection(detections):
    return max(detections, key=lambda d: d["area"]) if detections else None


# ============================================================
# DRAW DETECTION
# ============================================================

def draw_detection(frame, detection):
    color = detection["color"]
    draw_color = DRAW_COLORS[color]

    x = detection["x"]
    y = detection["y"]
    w = detection["w"]
    h = detection["h"]

    cv2.rectangle(frame, (x, y), (x + w, y + h), draw_color, 2)
    cv2.circle(frame, (detection["cx"], detection["cy"]), 4, draw_color, -1)

    text = f"{color} C:{detection['confidence']:.2f} A:{int(detection['area'])}"
    cv2.putText(frame, text, (x, max(18, y - 6)), cv2.FONT_HERSHEY_SIMPLEX, 0.42, draw_color, 1)


def draw_all(frame, detections):
    for color_detections in detections.values():
        for detection in color_detections:
            draw_detection(frame, detection)


# ============================================================
# DRAW TARGET
# ============================================================

def draw_target(frame, point, color, text):
    if point is None:
        return

    x, y = int(point[0]), int(point[1])

    cv2.circle(frame, (x, y), 7, color, -1)
    cv2.putText(frame, f"{text} ({x},{y})", (x + 8, max(y - 8, 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.44, color, 1)
    
    
# ============================================================
# BACK CAMERA FOR PARKING
# ============================================================

def start_back_camera():
    camera = Picamera2(1)

    config = camera.create_video_configuration(
        main={
            "size": (640, 480),
            "format": "RGB888"
        },
        controls={
            "FrameRate": 60
        }
    )

    camera.configure(config)
    camera.start()
    time.sleep(2)

    print("Back camera started.")
    return camera
