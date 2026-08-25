# The Dark Knight
## WRO Future Engineers 2026 — Team Current
### v1.0 — Nationals Configuration

This is the GitHub repository for **The Dark Knight**, our WRO Future Engineers 2026 robot.

We have kept the final robot information, code, CAD, photos, testing files and engineering documentation here so that everything for our Nationals version is in one place.

For judging, the repository is organized around four things: **buildability, engineering decisions, software traceability and test evidence**. The files linked below are the actual project files used to document and reproduce the Nationals configuration.

## Table of Contents

- [Repository Index](#repository-index)
- [1. Team](#1-team)
- [2. Final Robot Overview](#2-final-robot-overview)
- [3. Robot and CAD Visual Reference](#3-robot-and-cad-visual-reference)
  - [Robot Photos](#robot-photos)
  - [CAD Models](#cad-models)
  - [Circuit Schematic](#circuit-schematic)
  - [Final STL Files](#final-stl-files)
- [4. Final Robot Specifications](#4-final-robot-specifications)
- [5. Mechanical Design](#5-mechanical-design)
- [6. Cameras and Perception](#6-cameras-and-perception)
- [7. Computer Vision](#7-computer-vision)
- [8. Steering](#8-steering)
- [9. Software Architecture](#9-software-architecture)
- [10. Open Challenge](#10-open-challenge)
- [11. Obstacle Challenge](#11-obstacle-challenge)
- [12. Parking and MPU6050](#12-parking-and-mpu6050)
- [13. Power Architecture](#13-power-architecture)
- [14. Measured Power Results](#14-measured-power-results)
- [15. Engineering Evolution](#15-engineering-evolution)
- [16. Recorded Challenge Performance](#16-recorded-challenge-performance)
- [17. Known Development History](#17-known-development-history)
- [18. Repository Structure](#18-repository-structure)
- [19. Reproducibility](#19-reproducibility)
- [20. Evidence Included in This Repository](#20-evidence-included-in-this-repository)
- [21. Final Nationals Configuration Verification](#21-final-nationals-configuration-verification)
- [22. Version](#22-version)

## Repository Index

### Start here

1. [Start Here](./guide/START_HERE.md)
2. [Build From Zero](./guide/BUILD_FROM_ZERO.md)
3. [Parts Checklist](./guide/PARTS_CHECKLIST.md)
4. [Wiring and Pin Reference](./guide/WIRING_AND_PIN_REFERENCE.md)
5. [Software Setup](./guide/SOFTWARE_SETUP.md)

### Engineering evidence

- [Power & Sensor Evidence](./guide/POWER_AND_SENSOR_EVIDENCE.md)
- [Reproducibility Evidence](./guide/REPRODUCIBILITY.md)
- [Changelog](./CHANGELOG.md)
- [Testing Evidence](./testing/)
- [Open Challenge Video](./testing/Open_Challenge.mp4)
- [Power Measurements](./testing/power_measurements.csv)
- [Test Results](./testing/test_results.csv)
- [Test Summary](./testing/test_summary.md)
- [Engineering Evolution](./testing/engineering_evolution.md)

### Robot files

- [Source Code](./src/)
- [CAD / STL Models](./models/)
- [Robot Photos](./v-photos/)
- [Circuit Schematic](./schemes/schematic.jpg)
- [Video Evidence](./video/)

### Recommended judge path

**Start Here → Build From Zero → Parts Checklist → Wiring Reference → Software Setup → README engineering sections → Testing Evidence → Source Code → CAD/STL → Changelog**

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
- Two mechanical LEGO differentials, one per axle
- Central driveshaft

We did not build the final version in one step. We changed the motor, chassis, camera setup, power system and software after testing the robot and seeing what was actually causing problems.

---

# 3. Robot and CAD Visual Reference

All images in this section use **real files currently present in the GitHub repository**. The previous version used placeholder filenames such as `front_view.png`, `back_view.png`, `chassis.png`, etc. Those files do not exist in the repository, so GitHub could not load them.

## Robot Photos

### Final Robot — Front
![The Dark Knight — final front view](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_03_FINAL_ROBOT_FRONT.jpg)

### Final Robot — Rear
![The Dark Knight — final rear view](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_04_FINAL_ROBOT_REAR.jpg)

### Final Robot — Top
![The Dark Knight — final top view](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_05_FINAL_ROBOT_TOP.jpg)

### Side Profile 1
![The Dark Knight — side profile 1](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/SIDE_PROFILE_1.png)

### Side Profile 2
![The Dark Knight — side profile 2](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/SIDE_PROFILE_2.png)

## Mechanical and Electronics Evidence

### Mechanical Differential
![Mechanical differential](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_06_MECHANICAL_DIFFERENTIAL.jpg)

### Differential Powertrain
![Differential powertrain](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_07_DIFFERENTIAL_POWERTRAIN.jpg)

### Steering Mechanism
![Steering mechanism](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_08_STEERING_MECHANISM.jpg)

### Motor Mount
![Motor mount](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_09_MOTOR_MOUNT.jpg)

### Camera Configuration
![Camera configuration](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_10_CAMERA_CONFIGURATION.jpg)

### Power Distribution
![Power distribution](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_20_POWER_DISTRIBUTION.jpg)

### Circuit Box — Open
![Circuit box open](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_21_CIRCUIT_BOX_OPEN.jpg)

### Circuit Box — Closed
![Circuit box closed](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_22_CIRCUIT_BOX_CLOSED.jpg)

### Battery Setup
![Battery setup](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/IMG_23_BATTERY_SETUP.jpg)

## CAD Visual References

The CAD preview images are stored in `v-photos/` as real JPG files. They are linked here instead of referencing nonexistent PNG files inside `models/`.

### Chassis
![CAD chassis](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/CAD_01_CHASSIS.jpg)

### Camera Mount
![CAD camera mount](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/CAD_02_CAMERA_MOUNT.jpg)

### Camera Case
![CAD camera case](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/CAD_03_CAMERA_CASE.jpg)

### Circuit Box
![CAD circuit box](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/CAD_04_CIRCUIT_BOX.jpg)

### Circuit Box Lid
![CAD circuit box lid](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/CAD_05_CIRCUIT_LID.jpg)

### Chassis — Part 2
![CAD chassis part 2](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/CAD_06_CHASSIS2.jpg)

### 36-Tooth Gear
![CAD 36-tooth gear](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/v-photos/CAD_07_36T_GEAR.jpg)

## Circuit Schematic

![Final circuit schematic](https://raw.githubusercontent.com/darsh-makadia/Team-Current-WRO-FE-2026/main/schemes/schematic.jpg)

## Final STL Files

The STL links below point to **actual filenames currently present in `models/`**.

| Model | Actual STL | Purpose |
|---|---|---|
| 36-tooth gear | [`36t gear.stl`](https://github.com/darsh-makadia/Team-Current-WRO-FE-2026/blob/main/models/36t%20gear.stl) | Custom drive gear |
| Circuit box | [`Circuit_Box.stl`](https://github.com/darsh-makadia/Team-Current-WRO-FE-2026/blob/main/models/Circuit_Box.stl) | Electronics enclosure |
| Circuit box lid | [`Circuit_Box_LID.stl`](https://github.com/darsh-makadia/Team-Current-WRO-FE-2026/blob/main/models/Circuit_Box_LID.stl) | Electronics enclosure lid |
| Camera case | [`camera case.stl`](https://github.com/darsh-makadia/Team-Current-WRO-FE-2026/blob/main/models/camera%20case.stl) | Camera enclosure |
| Chassis | [`chassis.stl`](https://github.com/darsh-makadia/Team-Current-WRO-FE-2026/blob/main/models/chassis.stl) | Main custom chassis |
| Chassis — Part 2 | [`chassis pt2.stl`](https://github.com/darsh-makadia/Team-Current-WRO-FE-2026/blob/main/models/chassis%20pt2.stl) | Additional chassis component |
| Dual camera mount | [`dual_camera_mount.stl`](https://github.com/darsh-makadia/Team-Current-WRO-FE-2026/blob/main/models/dual_camera_mount.stl) | Dual-camera mounting structure |

> **Important:** GitHub renders these STL files as downloadable model files rather than as README images. The image previews above are the repository's actual JPG/PNG evidence files.

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
| Differential | **Two mechanical LEGO differentials, one per axle** |
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

# 17. Known Development History

There are older descriptions in earlier project files because the robot changed during development.

Examples include:

- earlier RWD descriptions;
- earlier single-camera descriptions;
- older steering values;
- older wording saying parking was still planned;
- earlier power tables with values that were not measured.

Those are development-stage details. The Nationals version described in this repository is:

**4WD + mechanical LEGO differential + central driveshaft + two cameras + MPU6050 + CAD/PLA chassis + JGB37-520 + TB6612FNG + 3S LiPo.**

---

# 18. Repository Structure

```text
Team-Current-WRO-FE-2026/
│
├── README.md
├── CHANGELOG.md
│
├── guide/
│   ├── START_HERE.md
│   ├── BUILD_FROM_ZERO.md
│   ├── PARTS_CHECKLIST.md
│   ├── WIRING_AND_PIN_REFERENCE.md
│   ├── SOFTWARE_SETUP.md
│   ├── POWER_AND_SENSOR_EVIDENCE.md
│   └── REPRODUCIBILITY.md
│
├── models/
│   ├── CAD preview images
│   └── final STL exports
│
├── schemes/
│   └── schematic.png
│
├── src/
│   ├── Current_Open_8_22.py
│   ├── Current_Obstacle_8_21.py
│   ├── drive.py
│   ├── heaeding.py
│   ├── openVision.py
│   ├── parking.py
│   └── vision.py
│
├── testing/
│   ├── Open_Challenge.mp4
│   ├── engineering_evolution.md
│   ├── power_measurements.csv
│   ├── processing_observations.csv
│   ├── test_results.csv
│   └── test_summary.md
│
├── t-photos/
├── v-photos/
└── video/
```

The repository is separated by function so a judge can move from **how to build the robot**, to **how it is wired**, to **how the software runs**, to **the evidence from testing**, and finally to the **actual source and CAD files**.

The source filenames above match the current `src/` directory. The testing files listed above are the files used as evidence for the documented results.

---

# 19. Reproducibility

The repository is organized so another team, mentor or judge can trace the final Nationals configuration from the physical build to the software and the test evidence.

## 19.1 Build path

**Step 1 — Parts**

Use [`PARTS_CHECKLIST.md`](./guide/PARTS_CHECKLIST.md) to identify the documented components.

**Step 2 — Mechanical build**

Use [`BUILD_FROM_ZERO.md`](./guide/BUILD_FROM_ZERO.md) together with the CAD/STL files in [`models/`](./models/).

**Step 3 — Wiring**

Use [`WIRING_AND_PIN_REFERENCE.md`](./guide/WIRING_AND_PIN_REFERENCE.md) and the final [schematic](./schemes/schematic.jpg).

**Step 4 — Software**

Use [`SOFTWARE_SETUP.md`](./guide/SOFTWARE_SETUP.md), then use the programs and modules in [`src/`](./src/).

**Step 5 — Calibration**

Verify camera placement, steering centre/range, vision thresholds and MPU6050 calibration before challenge testing.

**Step 6 — Validation**

Use the files in [`testing/`](./testing/) to compare the rebuilt robot with the recorded Nationals configuration.

## 19.2 Source-to-function map

| Source file | Purpose |
|---|---|
| [`Current_Open_8_22.py`](./src/Current_Open_8_22.py) | Open Challenge program |
| [`Current_Obstacle_8_21.py`](./src/Current_Obstacle_8_21.py) | Obstacle Challenge program |
| [`drive.py`](./src/drive.py) | Motor and steering control |
| [`vision.py`](./src/vision.py) | Main vision processing |
| [`openVision.py`](./src/openVision.py) | Open Challenge vision processing |
| [`parking.py`](./src/parking.py) | Parking logic |
| [`heaeding.py`](./src/heaeding.py) | MPU6050 heading and calibration |

## 19.3 Testing workflow

Every important engineering change is evaluated using the same basic cycle:

**Problem → hypothesis → change → test → measured result → decision**

Examples documented in this repository include:

- motor/chassis changes after early drivetrain testing;
- camera-placement changes after perception testing;
- marker-counting changes after repeated detections;
- IMU-based parking control after timed turns proved less reliable;
- vision threshold changes after field testing.

The supporting records are kept in:

- [`engineering_evolution.md`](./testing/engineering_evolution.md)
- [`test_results.csv`](./testing/test_results.csv)
- [`processing_observations.csv`](./testing/processing_observations.csv)
- [`test_summary.md`](./testing/test_summary.md)
- [`power_measurements.csv`](./testing/power_measurements.csv)

## 19.4 Configuration traceability

The documented final configuration is kept consistent across:

- this README;
- the build and wiring guides;
- the source code;
- CAD/STL files;
- the schematic;
- testing records;
- [`CHANGELOG.md`](./CHANGELOG.md).

If a competition configuration changes, the corresponding source, guide and changelog entry should be updated together.

## 19.5 Versioning

The repository uses a Nationals configuration baseline and keeps a changelog at [`CHANGELOG.md`](./CHANGELOG.md).

For future engineering changes, commit messages should describe the actual change, for example:

```text
vision: improve obstacle confidence
parking: calibrate IMU turn
drive: update steering limits
mechanical: revise camera mount
testing: record obstacle challenge runs
docs: update Nationals configuration
```

This makes the engineering history easier to follow than generic file-upload messages.

## 19.6 Honest measurement policy

Measured values are labelled as measured.

Where a quantity has not been directly measured, the repository says **not measured** rather than presenting a manufacturer rating or an estimate as a robot test result.

This is particularly important for the current/power dataset in [`power_measurements.csv`](./testing/power_measurements.csv).

---

# 20. Evidence Included in This Repository

The repository currently contains:

- engineering documentation and index;
- final Python source;
- final STL exports supplied by us in `models/`;
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
| Documentation index | **Included at `guide/`** |
| Final STL exports | **Included in `models/`** |
| Open Challenge video | **Included in `testing/`** |

If we change the physical robot after this version, the code and documentation need to be changed as well. Otherwise, this is the configuration we are using as the Nationals baseline.

---

# 22. Version

**v1.0 — Nationals Configuration**
