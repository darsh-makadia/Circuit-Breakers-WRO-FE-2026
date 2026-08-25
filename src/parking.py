import cv2
import time
from time import sleep
from picamera2 import Picamera2
from heading import MPU6050Heading
import drive
import vision

clockwise = False

def run_parking_clockwise():

    imu = MPU6050Heading()
    last_heading_time = 0
    # ============================================================
    # SETTINGS
    # ============================================================

    RS = 25
    KP = 0.06

    WIDTH = vision.WIDTH
    HEIGHT = vision.HEIGHT
    X_MID = vision.X_MID

    BACK_WIDTH = 640
    BACK_HEIGHT = 480
    FPS = 60

    MAGENTA_STOP_Y = 220

    CENTER = drive.CENTER


    # ============================================================
    # START FRONT CAMERA
    # ============================================================

    front_cam = Picamera2(0)

    front_config = front_cam.create_video_configuration(
        main={
            "size": (WIDTH, HEIGHT),
            "format": "RGB888"
        },
        controls={
            "FrameRate": FPS
        }
    )

    front_cam.configure(front_config)


    # ============================================================
    # START BACK CAMERA
    # ============================================================

    back_cam = Picamera2(1)

    back_config = back_cam.create_video_configuration(
        main={
            "size": (BACK_WIDTH, BACK_HEIGHT),
            "format": "RGB888"
        },
        controls={
            "FrameRate": FPS
        }
    )

    back_cam.configure(back_config)


    front_cam.start()
    back_cam.start()

    time.sleep(2)


    # ============================================================
    # START
    # ============================================================

    print("RIGHT WALL FOLLOW TEST")
    print("Front camera : BLACK wall")
    print("Back camera  : MAGENTA")
    print("Q = STOP")

    drive.steer(CENTER)
    sleep(0.8)


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
            # FRONT CAMERA
            # ====================================================

            front_frame = front_cam.capture_array()

            # vision.py expects the same frame format used by
            # your reference code.
            output = front_frame.copy()

            # EXACT SAME DETECTION ALGORITHM
            front_detections = vision.detect_all(
                front_frame
            )

            vision.draw_all(
                output,
                front_detections
            )

            # EXACT SAME LARGEST-DETECTION METHOD
            black_blob = vision.largest_detection(
                front_detections["BLACK"]
            )

            # ====================================================
            # RIGHT BLACK WALL
            # ====================================================

            right_target = None
            left_target = None
            if black_blob:

                x = black_blob["x"]
                y = black_blob["y"]
                w = black_blob["w"]
                h = black_blob["h"]
                cx = black_blob["cx"]

                if cx >= X_MID:

                    right_target = (
                        x,
                        y + h
                    )

                    vision.draw_target(
                        output,
                        right_target,
                        vision.YELLOW,
                        "RIGHT BLACK"
                    )

            # ====================================================
            # BACK CAMERA
            # ====================================================

            back_frame = back_cam.capture_array()

            # Keep same image format as front camera.
            # Rotate only for the physical camera orientation.
            back_frame = cv2.rotate(
                back_frame,
                cv2.ROTATE_180
            )

            back_output = back_frame.copy()

            # ====================================================
            # EXACT SAME DETECTION ALGORITHM
            #
            # No separate magenta algorithm.
            # The same vision.detect_all() is used here.
            # ====================================================

            back_detections = vision.detect_all(
                back_frame
            )

            vision.draw_all(
                back_output,
                back_detections
            )

            # EXACT SAME LARGEST-DETECTION METHOD
            magenta_blob = vision.largest_detection(
                back_detections["MAGENTA"]
            )

            # ====================================================
            # MAGENTA TARGET
            # ====================================================

            magenta_detected = False
            magenta_point = None

            if magenta_blob:

                x = magenta_blob["x"]
                y = magenta_blob["y"]
                w = magenta_blob["w"]
                h = magenta_blob["h"]

                magenta_detected = True

                # Same target coordinate logic from your reference
                magenta_point = (
                    x + w,
                    y
                )

                vision.draw_target(
                    back_output,
                    magenta_point,
                    vision.DRAW_COLORS["MAGENTA"],
                    "MAGENTA"
                )

                cv2.putText(
                    back_output,
                    f"X: {magenta_point[0]}  Y: {magenta_point[1]}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.55,
                    vision.DRAW_COLORS["MAGENTA"],
                    2
                )

            # ====================================================
            # STOP WHEN BACK CAMERA SEES MAGENTA
            # ====================================================

            if (
                magenta_detected
                and magenta_blob["y"] < MAGENTA_STOP_Y
            ):

                drive.stop()
                drive.steer(CENTER)

                cv2.putText(
                    back_output,
                    "MAGENTA DETECTED - STOP",
                    (10, BACK_HEIGHT - 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.65,
                    vision.DRAW_COLORS["MAGENTA"],
                    2
                )

                cv2.imshow(
                    "FRONT CAMERA - RIGHT WALL",
                    output
                )

                cv2.imshow(
                    "BACK CAMERA - MAGENTA",
                    back_output
                )

                cv2.waitKey(1)

                print("MAGENTA DETECTED - ROBOT STOPPED")

                break

            # ====================================================
            # DRIVE
            # ====================================================

            drive.forward(RS)

            # ====================================================
            # RIGHT WALL STEERING
            # ====================================================

            if right_target:

                only_x, _ = right_target

                angle = (
                    CENTER
                    + (
                        only_x
                        - (WIDTH - 250)
                    )
                    * KP
                )

            else:

                angle = CENTER + 20

            drive.steer(angle)

            # ====================================================
            # FRONT DISPLAY
            # ====================================================

            cv2.line(
                output,
                (X_MID, 0),
                (X_MID, HEIGHT),
                vision.YELLOW,
                1
            )

            cv2.line(
                output,
                (0, vision.ROI_Y),
                (WIDTH - 1, vision.ROI_Y),
                vision.YELLOW,
                2
            )

            cv2.putText(
                output,
                "RIGHT BLACK WALL FOLLOW",
                (10, HEIGHT - 18),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                vision.WHITE,
                2
            )

            # ====================================================
            # BACK DISPLAY
            # ====================================================

            cv2.putText(
                back_output,
                "BACK CAMERA - MAGENTA",
                (10, BACK_HEIGHT - 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                vision.WHITE,
                2
            )

            # ====================================================
            # FPS
            # ====================================================

            fps_frames += 1
            now = time.perf_counter()

            if now - fps_start >= 1.0:

                loop_fps = (
                    fps_frames
                    /
                    (now - fps_start)
                )

                fps_frames = 0
                fps_start = now

            cv2.putText(
                output,
                f"FPS: {loop_fps:.1f}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                vision.WHITE,
                2
            )

            # ====================================================
            # DISPLAY BOTH CAMERAS
            # ====================================================

            cv2.imshow(
                "FRONT CAMERA - RIGHT WALL",
                output
            )

            cv2.imshow(
                "BACK CAMERA - MAGENTA",
                back_output
            )

            # ====================================================
            # EXIT
            # ====================================================

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break


    finally:

        drive.stop()
        drive.steer(drive.CENTER)

        front_cam.stop()
        front_cam.close()

        back_cam.stop()
        back_cam.close()

        drive.steer(drive.RIGHT)
        sleep(1)
        heading = imu.get_heading()
        drive.backward(33)
        while heading < 50 or heading > 330: 
            current_time = time.time()
            if current_time-last_heading_time > 0.01:
                heading = imu.get_heading()
                last_heading_time = current_time
                print(f"Heading: {heading:.5f}°")
        drive.stop()
        drive.steer(drive.CENTER)
        sleep(1)
        drive.backward(35)
        sleep(0.3)
        drive.stop()
        sleep(1)
        drive.steer(drive.LEFT)
        sleep(2)
        heading = imu.get_heading()
        drive.backward(33)
        while heading > 1.5: 
            current_time = time.time()
            if current_time-last_heading_time > 0.01:
                heading = imu.get_heading()
                last_heading_time = current_time
                print(f"Heading: {heading:.5f}°")

        drive.stop()
        drive.steer(85)
        sleep(2)
        drive.forward(35)
        sleep(0.4)
        drive.stop()

        drive.steer(drive.CENTER)
        sleep(2)
        cv2.destroyAllWindows()

        print("RIGHT WALL FOLLOW TEST STOPPED")

def run_parking_anticlockwise():

    imu = MPU6050Heading()
    last_heading_time = 0

    # ============================================================
    # SETTINGS
    # ============================================================

    RS = 25
    KP = 0.06

    WIDTH = vision.WIDTH
    HEIGHT = vision.HEIGHT
    X_MID = vision.X_MID

    BACK_WIDTH = 640
    BACK_HEIGHT = 480
    FPS = 60

    MAGENTA_STOP_Y = 220

    CENTER = drive.CENTER

    # ============================================================
    # START FRONT CAMERA
    # ============================================================

    front_cam = Picamera2(0)

    front_config = front_cam.create_video_configuration(
        main={
            "size": (WIDTH, HEIGHT),
            "format": "RGB888"
        },
        controls={
            "FrameRate": FPS
        }
    )

    front_cam.configure(front_config)

    # ============================================================
    # START BACK CAMERA
    # ============================================================

    back_cam = Picamera2(1)

    back_config = back_cam.create_video_configuration(
        main={
            "size": (BACK_WIDTH, BACK_HEIGHT),
            "format": "RGB888"
        },
        controls={
            "FrameRate": FPS
        }
    )

    back_cam.configure(back_config)

    front_cam.start()
    back_cam.start()

    time.sleep(2)

    # ============================================================
    # START
    # ============================================================

    print("LEFT WALL FOLLOW TEST")
    print("Front camera : BLACK wall")
    print("Back camera  : MAGENTA")
    print("Q = STOP")

    drive.steer(CENTER)
    sleep(0.8)

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
            # FRONT CAMERA
            # ====================================================

            front_frame = front_cam.capture_array()

            output = front_frame.copy()

            front_detections = vision.detect_all(
                front_frame
            )

            vision.draw_all(
                output,
                front_detections
            )

            black_blob = vision.largest_detection(
                front_detections["BLACK"]
            )

            # ====================================================
            # LEFT BLACK WALL
            # ====================================================

            left_target = None

            if black_blob:

                x = black_blob["x"]
                y = black_blob["y"]
                w = black_blob["w"]
                h = black_blob["h"]
                cx = black_blob["cx"]

                if cx <= X_MID:

                    left_target = (
                        x + w,
                        y + h
                    )

                    vision.draw_target(
                        output,
                        left_target,
                        vision.YELLOW,
                        "LEFT BLACK"
                    )

            # ====================================================
            # BACK CAMERA
            # ====================================================

            back_frame = back_cam.capture_array()

            back_frame = cv2.rotate(
                back_frame,
                cv2.ROTATE_180
            )

            back_output = back_frame.copy()

            back_detections = vision.detect_all(
                back_frame
            )

            vision.draw_all(
                back_output,
                back_detections
            )

            magenta_blob = vision.largest_detection(
                back_detections["MAGENTA"]
            )

            # ====================================================
            # MAGENTA TARGET
            # ====================================================

            magenta_detected = False
            magenta_point = None

            if magenta_blob:

                x = magenta_blob["x"]
                y = magenta_blob["y"]
                w = magenta_blob["w"]
                h = magenta_blob["h"]

                magenta_detected = True

                # MIRROR OF CLOCKWISE TARGET
                magenta_point = (
                    x,
                    y
                )

                vision.draw_target(
                    back_output,
                    magenta_point,
                    vision.DRAW_COLORS["MAGENTA"],
                    "MAGENTA"
                )

                cv2.putText(
                    back_output,
                    f"X: {magenta_point[0]}  Y: {magenta_point[1]}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.55,
                    vision.DRAW_COLORS["MAGENTA"],
                    2
                )

            # ====================================================
            # STOP WHEN BACK CAMERA SEES MAGENTA
            # ====================================================

            if (
                magenta_detected
                and magenta_blob["y"] < MAGENTA_STOP_Y
            ):

                drive.stop()
                drive.steer(CENTER)

                cv2.putText(
                    back_output,
                    "MAGENTA DETECTED - STOP",
                    (10, BACK_HEIGHT - 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.65,
                    vision.DRAW_COLORS["MAGENTA"],
                    2
                )

                cv2.imshow(
                    "FRONT CAMERA - LEFT WALL",
                    output
                )

                cv2.imshow(
                    "BACK CAMERA - MAGENTA",
                    back_output
                )

                cv2.waitKey(1)

                print("MAGENTA DETECTED - ROBOT STOPPED")

                break

            # ====================================================
            # DRIVE
            # ====================================================

            drive.forward(RS)

            # ====================================================
            # LEFT WALL STEERING
            # ====================================================

            if left_target:

                only_x, _ = left_target

                angle = (
                    CENTER
                    + (
                        only_x
                        - 250
                    )
                    * KP
                )

            else:

                angle = CENTER - 20

            drive.steer(angle)

            # ====================================================
            # FRONT DISPLAY
            # ====================================================

            cv2.line(
                output,
                (X_MID, 0),
                (X_MID, HEIGHT),
                vision.YELLOW,
                1
            )

            cv2.line(
                output,
                (0, vision.ROI_Y),
                (WIDTH - 1, vision.ROI_Y),
                vision.YELLOW,
                2
            )

            cv2.putText(
                output,
                "LEFT BLACK WALL FOLLOW",
                (10, HEIGHT - 18),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                vision.WHITE,
                2
            )

            # ====================================================
            # BACK DISPLAY
            # ====================================================

            cv2.putText(
                back_output,
                "BACK CAMERA - MAGENTA",
                (10, BACK_HEIGHT - 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                vision.WHITE,
                2
            )

            # ====================================================
            # FPS
            # ====================================================

            fps_frames += 1
            now = time.perf_counter()

            if now - fps_start >= 1.0:

                loop_fps = (
                    fps_frames
                    /
                    (now - fps_start)
                )

                fps_frames = 0
                fps_start = now

            cv2.putText(
                output,
                f"FPS: {loop_fps:.1f}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                vision.WHITE,
                2
            )

            # ====================================================
            # DISPLAY BOTH CAMERAS
            # ====================================================

            cv2.imshow(
                "FRONT CAMERA - LEFT WALL",
                output
            )

            cv2.imshow(
                "BACK CAMERA - MAGENTA",
                back_output
            )

            # ====================================================
            # EXIT
            # ====================================================

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:

        drive.stop()
        drive.steer(drive.CENTER)

        front_cam.stop()
        front_cam.close()

        back_cam.stop()
        back_cam.close()

        # ====================================================
        # ANTICLOCKWISE PARKING MANOEUVRE
        # MIRROR OF CLOCKWISE FUNCTION
        # ====================================================

        drive.steer(drive.LEFT)
        sleep(1)

        heading = imu.get_heading()

        drive.backward(33)

        while heading > 310 or heading < 30:

            current_time = time.time()

            if current_time - last_heading_time > 0.01:

                heading = imu.get_heading()
                last_heading_time = current_time

                print(f"Heading: {heading:.5f}°")

        drive.stop()
        drive.steer(drive.CENTER)
        sleep(1)

        drive.backward(35)
        sleep(0.3)

        drive.stop()
        sleep(1)

        drive.steer(drive.RIGHT)
        sleep(2)

        heading = imu.get_heading()

        drive.backward(33)

        while heading < 358:

            current_time = time.time()

            if current_time - last_heading_time > 0.01:

                heading = imu.get_heading()
                last_heading_time = current_time

                print(f"Heading: {heading:.5f}°")

        drive.stop()

        drive.steer(55)
        sleep(2)

        drive.forward(35)
        sleep(0.4)

        drive.stop()

        drive.steer(drive.CENTER)
        sleep(2)

        cv2.destroyAllWindows()

        print("LEFT WALL FOLLOW TEST STOPPED")

if __name__ == "__main__":
    if clockwise == True:
        run_parking_clockwise()
    else:
        run_parking_anticlockwise()
