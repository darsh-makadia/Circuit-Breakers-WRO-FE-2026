import cv2
import numpy as np
import time
from picamera2 import Picamera2


# ============================================================
# CAMERA
# ============================================================

WIDTH = 1480
HEIGHT = 520
FPS = 60

X_MID = WIDTH // 2


# ============================================================
# DETECTION SETTINGS
# ============================================================

BLACK_MIN_AREA = 120
BLUE_MIN_AREA = 300
ORANGE_MIN_AREA = 300


# ============================================================
# DRAW COLORS
# ============================================================

WHITE = (255, 255, 255)
YELLOW = (0, 255, 255)

DRAW_COLORS = {
    "BLACK": (80, 80, 80),
    "BLUE": (255, 0, 0),
    "ORANGE": (0, 165, 255)
}


# ============================================================
# HSV RANGES
# ============================================================

BLACK_LOWER = np.array([0, 0, 0])
BLACK_UPPER = np.array([179, 170, 75])

BLUE_LOWER = np.array([95, 100, 40])
BLUE_UPPER = np.array([130, 255, 230])

ORANGE_LOWER = np.array([5, 100, 70])
ORANGE_UPPER = np.array([27, 255, 255])


# ============================================================
# MORPHOLOGY
# ============================================================

NORMAL_KERNEL = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE,
    (3, 3)
)

LINE_KERNEL = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (9, 5)
)


# ============================================================
# CAMERA
# ============================================================

def start_camera():

    camera = Picamera2(0)

    config = camera.create_video_configuration(
        main={
            "size": (WIDTH, HEIGHT),
            "format": "RGB888"
        },
        controls={
            "FrameRate": FPS
        }
    )

    camera.configure(config)

    camera.start()

    time.sleep(2)

    print("Open Challenge camera started.")

    return camera


# ============================================================
# BLACK DETECTION
# ============================================================

def detect_black(hsv):

    mask = cv2.inRange(
        hsv,
        BLACK_LOWER,
        BLACK_UPPER
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        NORMAL_KERNEL
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        NORMAL_KERNEL
    )

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    detections = []

    for contour in contours:

        area = cv2.contourArea(contour)

        if area < BLACK_MIN_AREA:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        if w <= 0 or h <= 0:
            continue

        detections.append({
            "color": "BLACK",
            "x": x,
            "y": y,
            "w": w,
            "h": h,
            "cx": x + w // 2,
            "cy": y + h // 2,
            "area": area,
            "confidence": 1.0
        })

    return detections


# ============================================================
# BLUE / ORANGE LINE DETECTION
# ============================================================
def detect_line(hsv, lower, upper, color, min_area):

    mask = cv2.inRange(
        hsv,
        lower,
        upper
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        NORMAL_KERNEL
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        LINE_KERNEL
    )

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    candidates = []

    for contour in contours:

        area = cv2.contourArea(contour)

        if area < min_area:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        if w < 20 or h < 3:
            continue

        # Use rotated rectangle because the line can be diagonal
        rect = cv2.minAreaRect(contour)

        rw, rh = rect[1]

        if rw <= 0 or rh <= 0:
            continue

        long_side = max(rw, rh)
        short_side = min(rw, rh)

        aspect_ratio = (
            long_side /
            max(short_side, 1)
        )

        # Reject small/round color patches
        if aspect_ratio < 2.0:
            continue

        candidates.append({
            "color": color,
            "x": x,
            "y": y,
            "w": w,
            "h": h,
            "cx": x + w // 2,
            "cy": y + h // 2,
            "area": area,
            "confidence": 1.0
        })

    if not candidates:
        return []

    return [
        max(
            candidates,
            key=lambda d: d["area"]
        )
    ]
# ============================================================
# DETECT ALL
#
# ONLY BLACK / BLUE / ORANGE
# ============================================================

def detect_all(frame):

    # IMPORTANT:
    # Use the complete frame.
    # Do NOT remove the bottom 120 pixels.

    roi_frame = frame[
        0:HEIGHT,
        0:WIDTH
    ]

    # Camera format is RGB888
    hsv = cv2.cvtColor(
        roi_frame,
        cv2.COLOR_RGB2HSV
    )

    detections = {}

    # --------------------------------------------------------
    # BLACK
    # --------------------------------------------------------

    detections["BLACK"] = detect_black(
        hsv
    )

    # --------------------------------------------------------
    # BLUE
    # --------------------------------------------------------

    detections["BLUE"] = detect_line(
        hsv,
        BLUE_LOWER,
        BLUE_UPPER,
        "BLUE",
        BLUE_MIN_AREA
    )

    # --------------------------------------------------------
    # ORANGE
    # --------------------------------------------------------

    detections["ORANGE"] = detect_line(
        hsv,
        ORANGE_LOWER,
        ORANGE_UPPER,
        "ORANGE",
        ORANGE_MIN_AREA
    )

    return detections


# ============================================================
# LARGEST DETECTION
# ============================================================

def largest_detection(detections):

    if not detections:
        return None

    return max(
        detections,
        key=lambda d: d["area"]
    )


# ============================================================
# DRAW DETECTION
# ============================================================

def draw_detection(
    frame,
    detection
):

    color = detection["color"]

    draw_color = DRAW_COLORS[color]

    x = detection["x"]
    y = detection["y"]

    w = detection["w"]
    h = detection["h"]

    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        draw_color,
        2
    )

    cv2.circle(
        frame,
        (
            detection["cx"],
            detection["cy"]
        ),
        4,
        draw_color,
        -1
    )

    text = (
        f"{color} "
        f"A:{int(detection['area'])}"
    )

    cv2.putText(
        frame,
        text,
        (
            x,
            max(18, y - 6)
        ),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.42,
        draw_color,
        1
    )


# ============================================================
# DRAW ALL
# ============================================================

def draw_all(
    frame,
    detections
):

    for color in (
        "BLACK",
        "BLUE",
        "ORANGE"
    ):

        for detection in detections[color]:

            draw_detection(
                frame,
                detection
            )


# ============================================================
# DRAW TARGET
# ============================================================

def draw_target(
    frame,
    point,
    color,
    text
):

    if point is None:
        return

    x = int(point[0])
    y = int(point[1])

    cv2.circle(
        frame,
        (x, y),
        7,
        color,
        -1
    )

    cv2.putText(
        frame,
        f"{text} ({x},{y})",
        (
            x + 8,
            max(y - 8, 20)
        ),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.44,
        color,
        1
    )
