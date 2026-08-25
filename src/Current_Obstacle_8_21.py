import cv2
import time
from time import sleep
from heading import MPU6050Heading
import drive
import vision
import parking

imu = MPU6050Heading()
last_heading_time = 0

# ============================================================
# ROBOT CONTROL SETTINGS
# ============================================================
COOLDOWN = 7
total_lap = 1
lap_count = 0
inside_park = True
round_complete = False
last_purple_time = 0.0
purple_gone_time = None

rs = 43
KP = 0.028
RIGHT = drive.RIGHT
LEFT = drive.LEFT
CENTER = drive.CENTER

OBSTACLE_ACTION_AREA = 8000

CENTER = drive.CENTER
WIDTH = vision.WIDTH
HEIGHT = vision.HEIGHT
X_MID = vision.X_MID

# ============================================================
# CAMERA
# ============================================================

camera = vision.start_camera()

# ============================================================
# ROBOT START
# ============================================================

print("Robot Started - TEST LAP")
print("RED/GREEN = obstacle avoidance")
print("BLACK = wall following")
print("BLUE/ORANGE/MAGENTA = display only")
print("Q = stop")

CLOCKWISE = None
angle = CENTER

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

        # ----------------------------------------------------
        # CAMERA + DETECTION
        # ----------------------------------------------------

        frame = camera.capture_array()
        output = frame.copy()

        detections = vision.detect_all(frame)
        vision.draw_all(output, detections)

        # ----------------------------------------------------
        # LARGEST OBJECTS
        # ----------------------------------------------------

        red_blob = vision.largest_detection(detections["RED"])
        green_blob = vision.largest_detection(detections["GREEN"])
        black_blob = vision.largest_detection(detections["BLACK"])
        blue_blob = vision.largest_detection(detections["BLUE"])
        orange_blob = vision.largest_detection(detections["ORANGE"])
        magenta_blob = vision.largest_detection(detections["MAGENTA"])

        # ----------------------------------------------------
        # BLACK WALL
        # ----------------------------------------------------

        left_target = None
        right_target = None
        black_w = 0
        if black_blob:
            x = black_blob["x"]
            y = black_blob["y"]
            w = black_blob["w"]
            h = black_blob["h"]
            cx = black_blob["cx"]
            black_w = w
            black_target = (x, y + h)

            if CLOCKWISE is None:
                if cx < X_MID:
                    CLOCKWISE = True
                    print("CLOCKWISE")
                else:
                    CLOCKWISE = False
            else:
                if CLOCKWISE:
                    left_target = (x + w, y + h) if cx <= X_MID else None
                    right_target = (x, y + h) if cx > X_MID else None
                else:
                    right_target = (x, y + h) if cx >= X_MID else None
                    left_target = (x + w, y + h) if cx < X_MID else None

            vision.draw_target(output, black_target, vision.YELLOW, "BLACK")
        if round_complete:
            right_target = False
        # ----------------------------------------------------
        # GREEN
        # ----------------------------------------------------

        green_target = None

        if green_blob and green_blob["area"] > OBSTACLE_ACTION_AREA:
            x = green_blob["x"]
            y = green_blob["y"]
            h = green_blob["h"]
            green_target = (x, y + h)
            vision.draw_target(output, green_target, vision.DRAW_COLORS["GREEN"], "GREEN")
            if round_complete:
                if CLOCKWISE:
                    right_target = green_target
                    green_target = False
                else:
                    left_target = green_target
                    green_target = False
        # ----------------------------------------------------
        # RED
        # ----------------------------------------------------

        red_target = None

        if red_blob and red_blob["area"] > OBSTACLE_ACTION_AREA:
            x = red_blob["x"]
            y = red_blob["y"]
            w = red_blob["w"]
            h = red_blob["h"]
            red_target = (x + w, y + h)
            vision.draw_target(output, red_target, vision.DRAW_COLORS["RED"], "RED")
            if round_complete:
                if CLOCKWISE:
                    right_target = red_target
                    red_target = False
                else:
                    left_target = red_target
                    red_target = False

        # ----------------------------------------------------
        # DISPLAY COLORS
        # ----------------------------------------------------

        if magenta_blob:
            point = (magenta_blob["x"] + magenta_blob["w"], magenta_blob["y"])
            vision.draw_target(output, point, vision.DRAW_COLORS["MAGENTA"], "MAGENTA")

        if blue_blob:
            point = (blue_blob["x"] + blue_blob["w"], blue_blob["y"] + blue_blob["h"])
            vision.draw_target(output, point, vision.DRAW_COLORS["BLUE"], "BLUE")

        if orange_blob:
            point = (orange_blob["x"] + orange_blob["w"], orange_blob["y"] + orange_blob["h"])
            vision.draw_target(output, point, vision.DRAW_COLORS["ORANGE"], "ORANGE")

        # ----------------------------------------------------
        # ROI
        # ----------------------------------------------------

        cv2.line(output, (0, vision.ROI_Y), (WIDTH - 1, vision.ROI_Y), vision.YELLOW, 2)

        # ----------------------------------------------------
        # DRIVE
        # ----------------------------------------------------
        current_time = time.time()

        if magenta_blob and current_time - last_purple_time > COOLDOWN:
                    lap_count += 1
                    last_purple_time = current_time
                    #print("Line :", line_count)
        #     if orange_detected and current_time - last_orange_time > LINE_COOLDOWN:
        #             line_count += 1
        #             last_orange_time = current_time
        #             #print("Line :", line_count)
        #     
        #     if line_count == total_lines and current_time - last_orange_time > LINE_COOLDOWN:
        #         steer(CENTER)
        #         stop()
        #         sleep(2)
        #         forward(rs)
        #         final = True
        #         round_complete = True
        if lap_count == total_lap+1 and not magenta_blob and not round_complete:

            if purple_gone_time is None:
                purple_gone_time = time.time()
                print("Purple wall gone - 3 second timer started")

            elif time.time() - purple_gone_time >= 0.5:

                print("3 seconds complete - stopping")
                drive.steer(CENTER)
                drive.stop()
                sleep(2)
                drive.forward(rs)
                round_complete = True
                
    #         video.release()
    # break
        # print("Line", line_count)
        if inside_park:
            if CLOCKWISE:
                heading = imu.get_heading()
                drive.steer(LEFT)
                sleep(1)
                drive.backward(rs)
                sleep(0.5)
                drive.stop()
                drive.steer(RIGHT)
                sleep(1)
                drive.forward(rs)
                while heading > 320 or heading < 1: 
                    current_time = time.time()
                    if current_time-last_heading_time > 0.01:
                        heading = imu.get_heading()
                        last_heading_time = current_time
                        print(f"Heading: {heading:.5f}°")
                drive.stop()
                drive.steer(CENTER)
                sleep(0.1)
                drive.forward(rs)
                sleep(0.6)
                drive.stop()
                drive.steer(RIGHT)
                drive.backward(rs)
                heading = imu.get_heading()
                while heading < 355 : 
                    current_time = time.time()
                    if current_time-last_heading_time > 0.01:
                        heading = imu.get_heading()
                        last_heading_time = current_time
                        print(f"Heading: {heading:.5f}°")
            else:
                heading = imu.get_heading()
                drive.steer(RIGHT)
                sleep(1)
                drive.backward(rs)
                sleep(0.5)
                drive.stop()
                drive.steer(LEFT)
                sleep(1)
                drive.forward(rs)
                while heading < 40 or heading > 300: 
                    current_time = time.time()
                    if current_time-last_heading_time > 0.01:
                        heading = imu.get_heading()
                        last_heading_time = current_time
                        print(f"Heading: {heading:.5f}°")
                drive.stop()
                drive.steer(CENTER)
                sleep(0.1)
                drive.forward(rs)
                sleep(0.6)
                drive.stop()
                drive.steer(LEFT)
                drive.backward(rs)
                heading = imu.get_heading()
                while heading > 3: 
                    current_time = time.time()
                    if current_time-last_heading_time > 0.01:
                        heading = imu.get_heading()
                        last_heading_time = current_time
                        print(f"Heading: {heading:.5f}°")
            drive.stop()
            angle = CENTER
            inside_park = False
            drive.forward(rs)    
        # ====================================================
        # STEERING LOGIC
        # ====================================================
        if round_complete and black_w == WIDTH:
            drive.stop()
            drive.steer(CENTER)
            sleep(2)
            
            # FIrst Turnnot 
            drive.steer(LEFT)
            sleep(2)
            drive.forward(rs)
            heading = imu.get_heading()
            while heading < 90 or heading > 300: 
                current_time = time.time()
                if current_time-last_heading_time > 0.01:
                    heading = imu.get_heading()
                    last_heading_time = current_time
                    print(f"Heading: {heading:.5f}°")
            drive.stop()
            drive.steer(RIGHT)
            sleep(2)
            drive.backward(rs) 
            while heading < 180: 
                current_time = time.time()
                if current_time-last_heading_time > 0.01:
                    heading = imu.get_heading()
                    last_heading_time = current_time
                    print(f"Heading: {heading:.5f}°")
            drive.steer(CENTER)
            drive.stop()
            sleep(2)
            break
        elif green_target:
            green_x, green_y = green_target
            if CLOCKWISE:
                if green_y > 150:
                    angle = CENTER + (green_x - (WIDTH - 200)) * KP
                elif green_x > WIDTH / 2 and green_y < 150:
                    if left_target:
                        only_x, _ = left_target
                        angle = CENTER + only_x * KP

                    elif right_target:
                        only_x, _ = right_target
                        angle = CENTER + (only_x - (WIDTH - 50)) * KP
                    else:
                        angle = CENTER + 20

                else:
                    angle = CENTER + (green_x - WIDTH / 2) * KP
            else:
                angle = CENTER + (green_x - (WIDTH - 100)) * KP

        elif red_target:
            red_x, red_y = red_target

            if CLOCKWISE:
                if red_y > 210:
                    angle = CENTER + (red_x - 225) * KP
                    
                elif red_x > WIDTH / 2 and red_y < 210:
                    if left_target:
                        only_x, _ = left_target
                        angle = CENTER + only_x * KP

                    elif right_target:
                        only_x, _ = right_target
                        angle = CENTER + (only_x - (WIDTH - 50)) * KP

                    else:
                        angle = CENTER + 20
                else:
                    angle = CENTER + (red_x - WIDTH / 2) * KP

            else:
                angle = CENTER + (red_x - 100) * KP

        elif left_target and right_target:
            left_x, left_y = left_target
            right_x, right_y = right_target
    #         left_distance = left_x
    #         right_distance = WIDTH - right_x
    #         error = left_distance - right_distance
    #         angle = CENTER + error * KP
            if round_complete:
                if CLOCKWISE:
                    print("TWO_Target_Following")
                    angle = CENTER - 10
                else:
                    print("TWO_Target_Following")
                    angle = CENTER + 10
            elif CLOCKWISE:
                angle = CENTER + 20
            else:
                angle = CENTER - 20

        elif left_target:
            only_x, _ = left_target
            if round_complete and CLOCKWISE:
                print("LEFT_Target_Following..CLOCKWISE")
                angle = CENTER + (only_x - 300) * 0.018
            elif round_complete:
                print("LEFT_Target_Following..ENTICLOCKWISE")
                angle = CENTER + 10
            else:
                angle = CENTER + only_x * KP if CLOCKWISE else CENTER + (only_x - 20) * KP

        elif right_target:
            only_x, _ = right_target
            if round_complete and CLOCKWISE:
                print("RIGHT_Target_Following..CLOCKWISE")
                angle = CENTER - 10
            elif round_complete:
                print("RIGHT_Target_Following..ENTICLOCKWISE")
                angle = CENTER + (only_x - (WIDTH - 300)) * 0.018
            else:
                angle = CENTER + (only_x - (WIDTH - 300)) * KP if CLOCKWISE else CENTER + (only_x - WIDTH) * KP

        else:
            if round_complete and CLOCKWISE:
                print("CENTER_Target_Following")
                angle = CENTER - 10
            elif round_complete:
                angle = CENTER + 10
            else:
                angle = CENTER + 20 if CLOCKWISE else CENTER - 20

        drive.steer(angle)

        # ----------------------------------------------------
        # FPS
        # ----------------------------------------------------

        fps_frames += 1
        now = time.perf_counter()

        if now - fps_start >= 1.0:
            loop_fps = fps_frames / (now - fps_start)
            fps_frames = 0
            fps_start = now

        cv2.putText(output, f"FPS: {loop_fps:.1f}", (10, HEIGHT - 18), cv2.FONT_HERSHEY_SIMPLEX, 0.55, vision.WHITE, 2)

        # ----------------------------------------------------
        # DISPLAY
        # ----------------------------------------------------

        cv2.imshow("WRO TEST LAP", output)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# ============================================================
# SHUTDOWN
# ============================================================

finally:
    drive.steer(CENTER)
    sleep(2)
        
    camera.stop()
    camera.close()
    cv2.destroyAllWindows()

    time.sleep(1)
    if CLOCKWISE:
        parking.run_parking_clockwise()
    else:
        parking.run_parking_anticlockwise()

    print("TEST LAP STOPPED")

