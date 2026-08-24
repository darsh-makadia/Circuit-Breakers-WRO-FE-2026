# The Dark Knight
## WRO Future Engineers 2026 — Team Current
### v1.0 — Nationals Configuration

This is the GitHub repository for **The Dark Knight**, our WRO Future Engineers 2026 robot.

We have kept the final robot information, code, CAD, photos, testing files and engineering documentation here so that everything for our Nationals version is in one place.

## Table of Contents

- [1. Team](#1-team)
- [2. Final Robot Overview](#2-final-robot-overview)
- [3. Robot and CAD Visual Reference](#3-robot-and-cad-visual-reference)
  - [Final STL Files](#final-stl-files)
- [4. Final Robot Specifications](#4-final-robot-specifications)
- [5. Mechanical Design](#5-mechanical-design)
  - [5.1 CAD + LEGO hybrid architecture](#51-cad--lego-hybrid-architecture)
  - [5.2 Four-wheel drive](#52-four-wheel-drive)
  - [5.3 Gear ratio](#53-gear-ratio)
- [6. Cameras and Perception](#6-cameras-and-perception)
- [7. Computer Vision](#7-computer-vision)
- [8. Steering](#8-steering)
- [9. Software Architecture](#9-software-architecture)
- [10. Open Challenge](#10-open-challenge)
  - [10.1 Navigation](#101-navigation)
  - [10.2 Direction markers](#102-direction-markers)
  - [10.3 Marker counting](#103-marker-counting)
  - [10.4 Recorded results](#104-recorded-results)
- [11. Obstacle Challenge](#11-obstacle-challenge)
- [12. Parking and MPU6050](#12-parking-and-mpu6050)
- [13. Power Architecture](#13-power-architecture)
- [14. Measured Power Results](#14-measured-power-results)
- [15. Engineering Evolution](#15-engineering-evolution)
- [16. Recorded Challenge Performance](#16-recorded-challenge-performance)
- [17. Development Notes](#17-development-notes)
- [18. Repository Structure](#18-repository-structure)
- [19. Reproducibility](#19-reproducibility)
- [20. Evidence Included in This Repository](#20-evidence-included-in-this-repository)
- [21. Final Nationals Configuration Verification](#21-final-nationals-configuration-verification)
- [22. Version](#22-version)

---

# 1. Team

| Name | Role |
|---|---|
| **Darsh Makadia** | Programming & Electronics |
| **Ehan Mansuri** | Mechanical Design & 3D Modelling |
| **Sunil Solanki** | Coach |

**Robot:** The Dark Knight  
**Team:** Team Current  
**Competition:** WRO Future Engineers 2026

---

# 2. Final Robot Overview

The Dark Knight is our autonomous four-wheel-drive robot for WRO Future Engineers.

The final robot uses:

- Raspberry Pi 5 (4 GB)
- Two Raspberry Pi Camera Module 3 cameras
- JGB37-520 DC motor, 12 V, 600 RPM
- Servo steering
- MPU6050 IMU
- TB6612FNG motor driver
- 3S 2200 mAh LiPo battery
- CAD/PLA printed parts
- LEGO Technic drivetrain parts
- Mechanical LEGO differential
- Central driveshaft

We did not build the final version in one step. We changed the motor, chassis, camera setup, power system and software after testing the robot and seeing what was actually causing problems.

---

# 3. Robot and CAD Visual Reference

These are the robot photos and CAD views used in this repository. The vehicle photos are kept in `photos/` and the CAD previews are in `models/`.

## Robot Photos

### Front View

<img src="./photos/front_view.png" alt="The Dark Knight front view" width="600">

### Back View

<img src="./photos/back_view.png" alt="The Dark Knight back view" width="600">

### Side Views

<p align="center">
  <img src="./photos/side_view_1.png" alt="The Dark Knight side view 1" width="45%">
  <img src="./photos/side_view_2.png" alt="The Dark Knight side view 2" width="45%">
</p>

### Motor and Steering

<p align="center">
  <img src="./photos/motor_close_up.png" alt="JGB37-520 drive motor" width="45%">
  <img src="./photos/servo_close_up.png" alt="Steering servo" width="45%">
</p>

### Differential and Electronics

<p align="center">
  <img src="./photos/differential.png" alt="Mechanical LEGO differential" width="45%">
  <img src="./photos/circuit_case_and_battery.png" alt="Electronics and battery" width="45%">
</p>

### Electronics From Above

<p align="center">
  <img src="./photos/circuit_from_top.png" alt="Electronics from above" width="700">
</p>

## CAD Models

### Final Chassis

<img src="./models/chassis.png" alt="Final CAD chassis" width="700">

### Circuit Box

<img src="./models/circuit_box.png" alt="Circuit box CAD" width="700">

### Circuit Box Lid

<img src="./models/circuit_box_lid.png" alt="Circuit box lid CAD" width="700">

### Camera Mount

<img src="./models/camera_mount.png" alt="Camera mount CAD" width="700">

### Camera Case

<img src="./models/camera_case.png" alt="Camera case CAD" width="600">

## Circuit Schematic

<img src="./schemes/schematic.png" alt="Final circuit schematic" width="1000">

## Final STL Files

The final STL exports are in [`cad/`](./cad/). These are the actual STL files supplied with this version of the project.

| Model | STL file | Purpose |
|---|---|---|
| Final chassis | [`final_chassis.stl`](./cad/final_chassis.stl) | Main custom chassis |
| Final chassis — Part 2 | [`final_chassis_part2.stl`](./cad/final_chassis_part2.stl) | Additional chassis component |
| Dual-camera mount | [`dual_camera_mount.stl`](./cad/dual_camera_mount.stl) | Camera mounting component |
| Camera case | [`camera_case.stl`](./cad/camera_case.stl) | Camera protection/enclosure |
| Circuit box | [`circuit_box.stl`](./cad/circuit_box.stl) | Electronics enclosure |
| Circuit box lid | [`circuit_box_lid.stl`](./cad/circuit_box_lid.stl) | Electronics enclosure lid |

GitHub may not preview every STL directly in the README, so the links above open the actual files in `cad/`.

---

# 4. Final Robot Specifications

| Specification | Final value |
|---|---:|
| Length | **24 cm** |
| Width | **13 cm** |
| Height | **27.5 cm** |
| Mass | **863 g** |
| Wheel diameter | **43.2 mm** |
| Gear ratio | **1.8:1** |
| Drive configuration | **4WD** |
| Differential | **Mechanical LEGO differential** |
| Drive motor | **JGB37-520 DC 12 V, 600 RPM** |
| Steering | **Servo steering** |
| Main computer | **Raspberry Pi 5, 4 GB** |
| Cameras | **2 × Raspberry Pi Camera Module 3** |
| Orientation sensor | **MPU6050** |
| Motor driver | **TB6612FNG** |
| Battery | **3S LiPo, 2200 mAh** |
| Structural material | **PLA / CAD printed parts** |

---

# 5. Mechanical Design

## 5.1 CAD + LEGO hybrid architecture

We used CAD and LEGO for different parts of the robot instead of trying to make everything from one system.

**CAD/PLA:**
- chassis
- electronics/circuit box
- camera mount
- camera case
- custom mounting parts
- 36-tooth gear

**LEGO Technic:**
- drivetrain components
- mechanical differential
- gears
- shafts and connectors
- other small mechanical parts

This made it easier to keep the drivetrain modular while still getting a rigid chassis and proper mounting points for the electronics and cameras.

## 5.2 Four-wheel drive

The final robot is **4WD**.

One drive motor sends power through the central driveshaft and the mechanical drivetrain. The LEGO mechanical differential lets the wheels on the left and right sides rotate at different speeds when the robot turns.

We kept the mechanical differential instead of making an electronic differential because the drivetrain had to use a mechanical solution.

The 4WD setup was especially useful during the large steering angles used in parking because the steered wheels are also powered.

## 5.3 Gear ratio

The final external gear pair uses a 36-tooth gear and a 20-tooth gear, giving a **1.8:1** tooth-count ratio.

We chose this setup because, for our robot, the extra wheel speed was more useful than having the maximum possible torque.

In our recorded speed test, the robot travelled **3 m in 2.25 s**, which is about **1.33 m/s (4.8 km/h)**.

---

# 6. Cameras and Perception

The final robot uses **two Raspberry Pi Camera Module 3 cameras**.

### Front camera

Used for:
- track/line perception
- blue and orange direction markers
- red obstacles
- green obstacles

Documented setup:
- **1480 × 520**
- target **60 FPS**
- lens-centre height approximately **25.0 cm**

### Rear / parking camera

Used mainly for:
- parking-area perception
- parking marker detection
- the parking sequence

Documented setup:
- **640 × 480**
- target **60 FPS**
- lens-centre height approximately **23.5 cm**

The two-camera setup was added because the front camera is needed for normal driving while parking needs useful information from behind the robot.

---

# 7. Computer Vision

We use **OpenCV** with both **HSV and LAB** colour information.

For the documented colour/obstacle confidence calculation, the final document gives:

**Confidence = 0.65 × HSV + 0.20 × LAB + 0.15 × geometry**

The general process is:

1. capture the camera frame;
2. create colour masks;
3. clean the masks with morphology;
4. find contours;
5. reject contours below the configured area;
6. check colour coverage and similarity;
7. check contour geometry and position;
8. calculate confidence;
9. choose the useful target for steering.

The software handles:

- black track boundaries
- blue markers
- orange markers
- green obstacles
- red obstacles
- magenta/purple parking structures

The thresholds are calibration values. They were changed during testing and should only be changed again after testing on the real robot.

---

# 8. Steering

The final software uses these steering values:

| Setting | Value |
|---|---:|
| Centre | **75°** |
| Minimum | **35°** |
| Maximum | **115°** |

The drive code clamps requested steering angles to this range.

These are the values used for the final configuration and the values documented in the engineering PDF.

---

# 9. Software Architecture

The software is written in **Python** and runs on the Raspberry Pi 5.

| File | What it does |
|---|---|
| `config.py` | Main calibration and configuration values |
| `drive.py` | Motor and steering control |
| `heading.py` | MPU6050 heading and calibration |
| `vision.py` | Camera and colour/target processing |
| `openVision.py` | Open Challenge vision processing |
| `open_challenge.py` | Open Challenge navigation and marker/lap logic |
| `obstacle_challenge.py` | Obstacle detection and avoidance |
| `parking.py` | Parking state machine and IMU-guided turns |
| `run_open.py` | Open Challenge launcher |
| `run_obstacle.py` | Obstacle Challenge launcher |

The current code also has safety handling for IMU/I2C errors, bounded IMU turns, obstacle confirmation and safe stopping.

---

# 10. Open Challenge

## 10.1 Navigation

The final navigation uses direction-dependent wall following:

- **Clockwise → right wall**
- **Anticlockwise → left wall**

We used this approach because relying on the centre between two walls became unreliable when one wall temporarily disappeared from the camera view.

## 10.2 Direction markers

The first valid direction marker tells the robot which way the track is running:

- **Blue → Anticlockwise**
- **Orange → Clockwise**

After the direction is known, the program counts the marker colour for that direction.

## 10.3 Marker counting

Final Open Challenge settings:

| Parameter | Value |
|---|---:|
| `KP` | **0.013** |
| Laps | **3** |
| Relevant crossings per lap | **4** |
| Total counted crossings | **12** |
| Marker cooldown | **1.0 s** |
| Servo centre | **75°** |
| Servo limits | **35°–115°** |
| Initial motor PWM | **40** |

The marker counter uses rising-edge detection:

```text
not detected → detected = count once
detected → detected = do not count again
detected → disappears = ready for next marker
```

This was added because the same physical marker can stay visible for several camera frames.

## 10.4 Recorded results

The six recorded Open Challenge runs were:

**32, 30, 28, 28, 28, 28 seconds**

**Best recorded time: 28 seconds.**

The final four recorded runs were all 28 seconds under the tested conditions.

---

# 11. Obstacle Challenge

Obstacle detection is given priority over normal wall following.

The documented priority is roughly:

1. green obstacle;
2. red obstacle;
3. both useful boundaries;
4. left boundary;
5. right boundary;
6. conservative fallback.

The obstacle code also uses temporal confirmation so one bad camera frame does not immediately start an avoidance manoeuvre.

The obstacle steering response depends on the direction of travel because the same image position can require a different correction in clockwise and anticlockwise runs.

### Parking-marker transition

The magenta/purple parking marker is used in the final obstacle sequence. The rear camera detects the marker, and the third relevant detection starts the transition toward parking.

Parking is **implemented and tested**. It is not a planned/future feature in the Nationals version.

---

# 12. Parking and MPU6050

Parking uses the **rear camera, a parking state machine and MPU6050 heading feedback**.

Timed turns alone were not reliable enough because the actual turn could change with battery state, wheel contact, friction, servo position and speed.

### MPU6050 calibration

The documented calibration uses:

- an initial settling period;
- **1500 stationary Z-axis gyro samples**;
- average gyro bias calculation;
- bias subtraction during operation;
- heading integration and 0–360° wrapping.

The current source also stops safely if the IMU/I2C system fails and uses time limits on turning loops.

### Parking status

**Parking is working in the current tested configuration.**

The six recorded Obstacle Challenge runs included the complete sequence with parking.

---

# 13. Power Architecture

The final robot uses a **3S 2200 mAh LiPo** with separate power branches.

### Main battery branch

The battery supplies the motor-driver motor voltage and the inputs to the buck converters.

### Buck 1

Provides the regulated 5 V branch used for the servo and motor-driver logic connections shown in the final schematic.

### Buck 2

Provides the regulated 5 V supply for the Raspberry Pi 5 and its connected peripherals.

### Raspberry Pi 3.3 V

The Pi provides the 3.3 V rail used by the documented low-voltage devices such as the MPU6050 and OLED.

All parts share a common ground.

---

# 14. Measured Power Results

These are the voltage values we actually recorded in the final documentation:

| Point | Condition | Measured |
|---|---|---:|
| LiPo battery | Before run | **11.1 V** |
| LiPo battery | After multiple runs | **10.8 V** |
| Buck 1 output | Motors OFF | **5.0 V** |
| Buck 1 output | Robot moving | **5.0 V** |
| Pi supply | Idle | **5.0 V** |
| Pi supply | Moving | **5.0 V** |
| Motor driver | Motors OFF | **11.1 V** |
| Motor driver | Motors ON | **10.8 V** |

**Current was not measured.** We did not have a proper current-logging setup, so no current number has been added.

The voltage measurements show the values seen with the multimeter during the recorded tests. They do not measure short transient voltage drops or current spikes.

---

# 15. Engineering Evolution

Most of the final design came from problems we saw while testing.

| Area | Problem | What we changed | Testing / result |
|---|---|---|---|
| Motor | Johnson 1000 RPM motor caused stalling/current and stability concerns | Changed to JGB37-520 12 V 600 RPM | Repeated drive and power testing; final motor selected |
| Chassis | LEGO-heavy structure made rigid/custom mounting difficult | Added CAD/PLA structural parts while keeping LEGO drivetrain parts | Final chassis measured 24 × 13 × 27.5 cm and 863 g |
| Camera | Early mount was unstable and placement affected vision | Redesigned mount in CAD and moved to two cameras | Better forward perception plus rear parking view |
| Power | Pi should not supply the motor system | Separated motor and regulated logic/Pi branches | Recorded voltage measurements stayed at the documented values |
| Navigation | One marker could be detected more than once | Rising-edge detection + 1.0 s cooldown | Final 3-lap / 12-crossing logic |
| Obstacle avoidance | Colour/position mistakes could cause late steering | HSV + LAB + geometry scoring, contour filtering and temporal confirmation | Full obstacle sequence completed in recorded tests |
| Parking | Timed turns did not give reliable orientation | Rear camera + parking states + MPU6050 heading | Parking worked in the complete recorded runs |

---

# 16. Recorded Challenge Performance

## Open Challenge

| Run | Time |
|---:|---:|
| 1 | 32 s |
| 2 | 30 s |
| 3 | 28 s |
| 4 | 28 s |
| 5 | 28 s |
| 6 | 28 s |

**Best: 28 s**

## Obstacle Challenge

| Run | Time |
|---:|---:|
| 1 | 1:10 |
| 2 | 1:09 |
| 3 | 1:11 |
| 4 | 1:20 |
| 5 | 1:15 |
| 6 | 1:13 |

**Best: 1:09**

Obstacle placement was slightly different between runs, so these are kept exactly as recorded rather than trying to normalise the times.

---

# 17. Development Notes

The final robot was built through repeated testing rather than one fixed design. We changed the motor, chassis, camera arrangement, power layout and control logic when testing showed that the earlier setup was not working well enough.

The main development decisions are already recorded in **Section 15: Engineering Evolution**. The important point for the Nationals version is that the hardware and software described in Sections 2–14 are the current configuration.

# 18. Repository Structure

```text
Team_Currents_Nationals_v1.0/
│
├── README.md
├── VERSION
├── CHANGELOG.md
├── COMMIT_PLAN.md
│
├── code/
├── cad/
├── schematics/
├── photos/
├── testing/
└── documentation/
```

The main folders are kept separate so it is easy to find the code, CAD, photos, testing material and final engineering PDF.

---

# 19. Reproducibility

To build a robot similar to this version, the main hardware is:

- Raspberry Pi 5, 4 GB
- 2 × Raspberry Pi Camera Module 3
- JGB37-520 12 V 600 RPM motor
- servo motor
- MPU6050
- TB6612FNG motor driver
- 3S 2200 mAh LiPo
- buck converter(s)
- PLA printed parts
- required LEGO Technic drivetrain/differential parts

The software is Python-based. The repository source uses the Raspberry Pi camera environment and libraries including OpenCV, NumPy, RPi.GPIO and Picamera2.

The important final control values are in `code/config.py` and the challenge source files.

---

# 20. Evidence Included in This Repository

The repository currently contains:

- final engineering PDF;
- final Python source;
- final STL exports supplied by us;
- CAD preview images;
- schematic preview;
- robot photographs;
- Open Challenge test video;
- recorded challenge results;
- measured power-voltage results;
- engineering evolution notes.

The native CAD and schematic source files should only be added if we actually have the editable files. We have not made replacement source files from screenshots or STL exports.

---

# 21. Final Nationals Configuration Verification

Before using this as the Nationals version, we checked the main robot details against the final engineering document and the current code.

| Item | Final version |
|---|---|
| Drivetrain | **4WD** |
| Differential | **Mechanical LEGO differential + central driveshaft** |
| Cameras | **2 × Raspberry Pi Camera Module 3** |
| Orientation | **MPU6050** |
| Steering | **35° min / 75° centre / 115° max** |
| Open Challenge | **3 laps / 4 relevant crossings per lap / 12 total** |
| Marker cooldown | **1.0 s** |
| Direction markers | **Blue = anticlockwise / Orange = clockwise** |
| Obstacle parking marker | **Magenta / purple** |
| Parking | **Implemented and tested** |
| Open Challenge best | **28 s** |
| Obstacle Challenge best | **1:09** |
| Current measurement | **Not measured** |
| Final PDF | **Included in `documentation/`** |
| Final STL exports | **Included in `cad/`** |
| Open Challenge video | **Included in `testing/`** |

If we change the physical robot after this version, the code and documentation need to be changed as well. Otherwise, this is the configuration we are using as the Nationals baseline.

---

# 22. Version

**v1.0 — Nationals Configuration**

Recommended commit names from now on:

- `Fix parking state machine`
- `Update obstacle avoidance`
- `Add final testing results`
- `Update final drivetrain`
- `Add power measurements`
- `Update two-camera architecture`
- `Add final CAD exports`
- `Add Nationals configuration`

Avoid generic messages like `Add files via upload` when the commit is actually fixing or adding a specific part of the robot.

---

## Final note

This README is meant to document the robot we actually built and tested. We have kept the recorded results and measurements as they are. If something was not measured, it is marked that way instead of adding an estimate. If the robot changes after this version, the code and documentation should be updated together.
