import cv2
import time
from time import sleep

import drive
import openVision as vision

# ============================================================
# OPEN CHALLENGE SETTINGS
# ============================================================

LINE_COOLDOWN = 1.2

# Direct number of line crossings required
TOTAL_LINES = 13

last_line_time = 0
prev_marker_seen = False

blue_detected = False
orange_detected = False

line_count = 0

CLOCKWISE = None


# ============================================================
# ROBOT SETTINGS
# ============================================================

rs = 70
KP = 0.013

# Speed ramp settings
START_SPEED = 40
TARGET_SPEED = 70
ACCELERATION_TIME = 2.0

CENTER = drive.CENTER
LEFT = drive.LEFT
RIGHT = drive.RIGHT


# ============================================================
# CAMERA SETTINGS
# ============================================================

WIDTH = vision.WIDTH
HEIGHT = vision.HEIGHT
X_MID = vision.X_MID


# ============================================================
# START CAMERA
# ============================================================

camera = vision.start_camera()


# ============================================================
# ROBOT START
# ============================================================

print(
    f"Robot Started - will stop after "
    f"{TOTAL_LINES} line crossings"
)

print("Blue = ANTICLOCKWISE")
print("Orange = CLOCKWISE")
print("Black = wall following")
print("Q = stop")


drive.steer(CENTER)

sleep(1.9)

# Start robot at 40
drive.forward(START_SPEED)

# Start acceleration timer
acceleration_start = time.perf_counter()


# ============================================================
# FPS
# ============================================================

fps_frames = 0
fps_start = time.perf_counter()
loop_fps = 0.0


# ============================================================
# MAIN LOOP
# ============================================================

try:

    while True:

        # ====================================================
        # SPEED RAMP
        # 40 -> 70 in 2 seconds
        # ====================================================

        elapsed = (
            time.perf_counter()
            -
            acceleration_start
        )

        if elapsed < ACCELERATION_TIME:

            current_speed = (
                START_SPEED
                +
                (
                    TARGET_SPEED
                    -
                    START_SPEED
                )
                *
                (
                    elapsed
                    /
                    ACCELERATION_TIME
                )
            )

        else:

            current_speed = TARGET_SPEED

        drive.forward(current_speed)


        # ====================================================
        # CAMERA
        # ====================================================

        frame = camera.capture_array()

        output = frame.copy()


        # ====================================================
        # NEW VISION PROCESSING
        # ====================================================

        detections = vision.detect_all(
            frame
        )

        vision.draw_all(
            output,
            detections
        )


        # ====================================================
        # GET LARGEST DETECTIONS
        # ====================================================

        black_blob = vision.largest_detection(
            detections["BLACK"]
        )

        blue_blob = vision.largest_detection(
            detections["BLUE"]
        )

        orange_blob = vision.largest_detection(
            detections["ORANGE"]
        )


        # ====================================================
        # BLACK WALL
        # ====================================================

        left_target = None
        right_target = None

        if black_blob:

            x = black_blob["x"]
            y = black_blob["y"]
            w = black_blob["w"]
            h = black_blob["h"]
            cx = black_blob["cx"]


            black_target = (
                x,
                y + h
            )


            # ------------------------------------------------
            # Determine wall side
            # ------------------------------------------------

            if CLOCKWISE:
                left_target = (x + w, y + h) if cx <= X_MID else None
                right_target = (x, y + h) if cx > X_MID else None
            else:
                right_target = (x, y + h) if cx >= X_MID else None
                left_target = (x + w, y + h) if cx < X_MID else None

            vision.draw_target(
                output,
                black_target,
                vision.YELLOW,
                "BLACK"
            )


        # ====================================================
        # BLUE DETECTION
        # ====================================================

        blue_detected = False

        if blue_blob:

            blue_detected = True


        # ====================================================
        # ORANGE DETECTION
        # ====================================================

        orange_detected = False

        if orange_blob:

            orange_detected = True


        # ====================================================
        # DISPLAY BLUE
        # ====================================================

        if blue_blob:

            point = (
                blue_blob["x"] +
                blue_blob["w"],
                blue_blob["y"] +
                blue_blob["h"]
            )

            vision.draw_target(
                output,
                point,
                vision.DRAW_COLORS["BLUE"],
                "BLUE"
            )


        # ====================================================
        # DISPLAY ORANGE
        # ====================================================

        if orange_blob:

            point = (
                orange_blob["x"] +
                orange_blob["w"],
                orange_blob["y"] +
                orange_blob["h"]
            )

            vision.draw_target(
                output,
                point,
                vision.DRAW_COLORS["ORANGE"],
                "ORANGE"
            )


        # ====================================================
        # DETERMINE DIRECTION
        # ====================================================

        current_time = time.time()


        if CLOCKWISE is None:

            if blue_detected:

                CLOCKWISE = False

                last_line_time = (
                    current_time
                )

                print(
                    "ANTICLOCKWISE"
                )


            elif orange_detected:

                CLOCKWISE = True

                last_line_time = (
                    current_time
                )

                print(
                    "CLOCKWISE"
                )


        else:

            # ------------------------------------------------
            # Count only the same marker that selected
            # the direction
            # ------------------------------------------------

            marker_seen = (
                orange_detected
                if CLOCKWISE
                else blue_detected
            )


            # ------------------------------------------------
            # Rising-edge detection
            # ------------------------------------------------

            if (
                marker_seen
                and
                not prev_marker_seen
                and
                current_time -
                last_line_time >
                LINE_COOLDOWN
            ):

                line_count += 1

                last_line_time = (
                    current_time
                )

                print(
                    f"Line: "
                    f"{line_count}/"
                    f"{TOTAL_LINES}"
                )


            prev_marker_seen = marker_seen


        # ====================================================
        # CHECK TOTAL LINES
        # ====================================================

        if line_count >= TOTAL_LINES:

            drive.steer(
                CENTER
            )

            drive.stop()

            print(
                f"{TOTAL_LINES} "
                f"lines complete - stopping"
            )

            break


        # ====================================================
        # STEERING LOGIC
        # ====================================================

        if (left_target and right_target):
            left_x, left_y = (left_target)

            right_x, right_y = (right_target)

            left_distance = (left_x)

            right_distance = (WIDTH -right_x)

            error = (left_distance - right_distance)

            angle = (CENTER + error * KP)

        elif left_target:
            only_x, _ = (left_target)

            angle = (CENTER + (only_x - 50) * KP)

        elif right_target:

            only_x, _ = (right_target)

            angle = (CENTER + (only_x - (WIDTH - 50)) * KP)

        else:
            if CLOCKWISE:
                angle = CENTER + 5
            else:
                angle = CENTER - 5
        # ====================================================
        # STEER
        # ====================================================

        drive.steer(angle)

        # ====================================================
        # FPS
        # ====================================================

        fps_frames += 1

        now = time.perf_counter()


        if (
            now -
            fps_start
            >= 1.0
        ):

            loop_fps = (
                fps_frames /
                (
                    now -
                    fps_start
                )
            )

            fps_frames = 0

            fps_start = now


        # ====================================================
        # DISPLAY FPS
        # ====================================================

        cv2.putText(
            output,
            f"FPS: {loop_fps:.1f}",
            (
                10,
                HEIGHT - 18
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            vision.WHITE,
            2
        )


        # ====================================================
        # DISPLAY LINE COUNT
        # ====================================================

        if CLOCKWISE is True:

            direction_text = "CLOCKWISE"

        elif CLOCKWISE is False:

            direction_text = "ANTICLOCKWISE"

        else:

            direction_text = "WAITING"


        cv2.putText(
            output,
            f"Lines: {line_count}/{TOTAL_LINES}",
            (
                10,
                30
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            vision.WHITE,
            2
        )


        # ====================================================
        # DISPLAY DIRECTION
        # ====================================================

        cv2.putText(
            output,
            f"Direction: {direction_text}",
            (
                10,
                55
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            vision.WHITE,
            2
        )


        # ====================================================
        # DISPLAY SPEED
        # ====================================================

        cv2.putText(
            output,
            f"Speed: {current_speed:.1f}",
            (
                10,
                80
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            vision.WHITE,
            2
        )


        # ====================================================
        # DISPLAY CAMERA
        # ====================================================

        cv2.imshow(
            "WRO OPEN CHALLENGE",
            output
        )


        # ====================================================
        # QUIT
        # ====================================================

        if (
            cv2.waitKey(1) &
            0xFF
        ) == ord("q"):

            break


# ============================================================
# SHUTDOWN
# ============================================================

finally:

    drive.steer(
        CENTER
    )

    drive.stop()

    sleep(1)

    camera.stop()

    camera.close()

    cv2.destroyAllWindows()

    print(
        "OPEN CHALLENGE STOPPED"
    )

