# The Dark Knight

### Team Current · WRO Future Engineers 2026 · Nationals

> **Engineering idea:** use the materials we have intelligently, understand their limits, and improve the whole robot instead of chasing one perfect component.

<img src="./photos/front_view.png" alt="The Dark Knight - front view" width="900">

This repository is the complete working record for **The Dark Knight**. It is organised so that a judge can inspect the final robot quickly, while another team can follow the build guides and reproduce the documented configuration without having to guess what we meant.

**Team:** Current  
**Members:** Darsh Makadia · Ehan Mansuri  
**Coach:** Sunil Solanki  
**Category:** WRO Future Engineers  
**Level:** Nationals  
**Version:** `v1.0 – Nationals Configuration`

---

## If you know nothing about the robot, start here

**Do these in order:**

1. Read [`BUILD_FROM_ZERO.md`](./BUILD_FROM_ZERO.md) — the complete build path.
2. Use [`PARTS_CHECKLIST.md`](./PARTS_CHECKLIST.md) — what is needed.
3. Open [`schematics/schematic.png`](./schematics/schematic.png) — the wiring reference.
4. Open [`models/`](./models/) and [`photos/`](./photos/) — CAD previews and real robot photographs.
5. Build the drivetrain from the CAD/photos: **4WD + two mechanical LEGO differentials + central driveshaft**.
6. Follow [`SOFTWARE_SETUP.md`](./SOFTWARE_SETUP.md) — Raspberry Pi setup.
7. Follow [`CALIBRATION_AND_TESTING.md`](./CALIBRATION_AND_TESTING.md) — calibration and test order.

The goal is not to make the reader guess. Where the final document does not specify a workshop detail such as screw length or exact LEGO quantity, this repository says so instead of inventing a value.

---

## Quick view

| Area | Final documented configuration |
|---|---|
| Drive | 4WD, one drive motor, central driveshaft |
| Differential | 2 mechanical LEGO differentials, one per axle |
| Steering | Servo, 35°–115°, centre 75° |
| Computer | Raspberry Pi 5, 4 GB |
| Cameras | 2 × Raspberry Pi Camera Module 3 |
| IMU | MPU6050 gyro heading |
| Motor driver | TB6612FNG |
| Battery | 3S LiPo, 2200 mAh, 11.1 V nominal |
| Drive motor | JGB37-520, 12 V, 600 RPM |
| Structure | CAD/PLA + LEGO Technic drivetrain |
| Best Open result | **28 s** |
| Best Obstacle-navigation result | **1:09** |
| Parking | Implemented and physically tested; final alignment still needs reliable calibration |

The latest engineering document is the source for the current configuration. The repository source code is the authority for the exact software implementation.

---

## Table of Contents

- [1. Team](#1-team)
- [2. What we built](#2-what-we-built)
- [3. Final robot and CAD](#3-final-robot-and-cad)
  - [3.1 Final robot views](#31-final-robot-views)
  - [3.2 CAD previews](#32-cad-previews)
  - [3.3 Electrical schematic](#33-electrical-schematic)
  - [3.4 Final STL files](#34-final-stl-files)
- [4. Final robot specifications](#4-final-robot-specifications)
- [5. Mechanical design](#5-mechanical-design)
  - [5.1 CAD and LEGO hybrid](#51-cad-and-lego-hybrid)
  - [5.2 Four-wheel drive](#52-four-wheel-drive)
  - [5.3 Mechanical differentials](#53-mechanical-differentials)
  - [5.4 Steering](#54-steering)
  - [5.5 Gear ratio](#55-gear-ratio)
- [6. Cameras and sensor placement](#6-cameras-and-sensor-placement)
- [7. Computer vision](#7-computer-vision)
  - [7.1 Processing pipeline](#71-processing-pipeline)
  - [7.2 Confidence filtering](#72-confidence-filtering)
  - [7.3 Processing performance](#73-processing-performance)
- [8. Steering control](#8-steering-control)
- [9. Software architecture](#9-software-architecture)
- [10. Open Challenge](#10-open-challenge)
  - [10.1 Direction markers](#101-direction-markers)
  - [10.2 Rising-edge counting](#102-rising-edge-counting)
  - [10.3 Three laps and twelve crossings](#103-three-laps-and-twelve-crossings)
- [11. Obstacle Challenge](#11-obstacle-challenge)
- [12. Parking and IMU](#12-parking-and-imu)
  - [12.1 Why timed turns were insufficient](#121-why-timed-turns-were-insufficient)
  - [12.2 MPU6050 calibration](#122-mpu6050-calibration)
  - [12.3 Parking state machine](#123-parking-state-machine)
  - [12.4 Current parking status](#124-current-parking-status)
- [13. Power architecture](#13-power-architecture)
- [14. Measured power](#14-measured-power)
- [15. Software files](#15-software-files)
- [16. Testing and results](#16-testing-and-results)
- [17. Engineering evolution](#17-engineering-evolution)
- [18. Failure analysis and current risks](#18-failure-analysis-and-current-risks)
- [19. Repository and reproducibility](#19-repository-and-reproducibility)
- [20. Evidence included](#20-evidence-included)
- [21. Nationals configuration check](#21-nationals-configuration-check)
- [22. Version](#22-version)
- [23. Build from zero](#23-build-from-zero)
- [24. Wiring and pin reference](#24-wiring-and-pin-reference)
- [25. Software setup](#25-software-setup)
- [26. Calibration and testing](#26-calibration-and-testing)
- [27. Judge quick start](#27-judge-quick-start)

---

# 1. Team

**Team Current** built this robot for WRO Future Engineers 2026.

| Person | Main responsibility |
|---|---|
| Darsh Makadia | Programming and electronics |
| Ehan Mansuri | Mechanical design, CAD and documentation |
| Sunil Solanki | Coaching and technical guidance |

The work was split by subsystem, but the robot was tested as one system. Mechanical changes affected vision and steering, and software changes required physical calibration.

---

# 2. What we built

The Dark Knight is an autonomous vehicle using a **CAD/PLA structural chassis** together with LEGO Technic drivetrain components.

The final drivetrain is **4WD**. One JGB37-520 motor sends power through a central driveshaft to **two mechanical LEGO differentials**, one at each axle. A servo controls steering.

For perception, we use **two Raspberry Pi Camera Module 3 cameras**. The front camera handles track and obstacle perception. The rear camera gives the parking system a view of the area behind the robot.

A Raspberry Pi 5 (4 GB) runs the Python/OpenCV software. An MPU6050 provides gyro-based heading feedback for parking.

The design did not start like this. We went through a LEGO-heavy prototype, a LEGO/CAD hybrid, a motor change, power redesign, camera-mount changes, two-camera integration and several control iterations. Those changes are recorded in [`testing/engineering_evolution.md`](./testing/engineering_evolution.md) and the engineering document.

---

# 3. Final robot and CAD

## 3.1 Final robot views

<img src="./photos/front_view.png" alt="Front view of The Dark Knight" width="900">

<img src="./photos/back_view.png" alt="Rear view of The Dark Knight" width="900">

<img src="./photos/side_view_1.png" alt="Right side view of The Dark Knight" width="900">

<img src="./photos/side_view_2.png" alt="Left side view of The Dark Knight" width="900">

<img src="./photos/circuit_from_top.png" alt="Top view of the electronics and power layout" width="900">

More development photos are in [`photos/`](./photos/), including the motor, servo, differential and power-system views.

## 3.2 CAD previews

The printable files are in [`cad/`](./cad/). The preview renders are in [`models/`](./models/).

### Chassis

<img src="./models/chassis.png" alt="Chassis CAD model" width="800">

### Camera mount

<img src="./models/camera_mount.png" alt="Dual camera mount CAD model" width="700">

### Camera case

<img src="./models/camera_case.png" alt="Camera case CAD model" width="700">

### Electronics box

<img src="./models/circuit_box.png" alt="Circuit box CAD model" width="700">

### Electronics-box lid

<img src="./models/circuit_box_lid.png" alt="Circuit box lid CAD model" width="700">

## 3.3 Electrical schematic

<img src="./schematics/schematic.png" alt="Final electrical schematic" width="1000">

The enlarged schematic is the main electrical reference. It shows the Raspberry Pi, TB6612FNG, power branches, servo, MPU6050, OLED, LEDs and start button.

## 3.4 Final STL files

These are the actual STL exports included in this release. The geometry has not been changed just to make the links work; only filenames were cleaned for GitHub navigation.

| Model | File |
|---|---|
| Main chassis | [`final_chassis.stl`](./cad/final_chassis.stl) |
| Chassis part 2 | [`final_chassis_part2.stl`](./cad/final_chassis_part2.stl) |
| Dual-camera mount | [`dual_camera_mount.stl`](./cad/dual_camera_mount.stl) |
| Camera case | [`camera_case.stl`](./cad/camera_case.stl) |
| Circuit box | [`circuit_box.stl`](./cad/circuit_box.stl) |
| Circuit-box lid | [`circuit_box_lid.stl`](./cad/circuit_box_lid.stl) |

GitHub can show supported STL files in its model viewer. PNG previews are also provided so the design can still be understood if inline 3D rendering is unavailable.

---

# 4. Final robot specifications

| Specification | Final value |
|---|---:|
| Length | 24 cm |
| Width | 13 cm |
| Height | 27.5 cm |
| Mass | 863 g |
| Wheel diameter | 43.2 mm |
| Drive configuration | 4WD |
| Differentials | 2 mechanical LEGO differentials, one per axle |
| Drive motor | JGB37-520 DC, 12 V, 600 RPM |
| Steering | Servo |
| Main computer | Raspberry Pi 5, 4 GB |
| Cameras | 2 × Raspberry Pi Camera Module 3 |
| IMU | MPU6050 |
| Motor driver | TB6612FNG |
| Battery | 3S LiPo, 2200 mAh, 11.1 V nominal |
| Structural material | PLA / CAD printed parts |
| Printer | Anycubic Cobra 2 Neo |
| External gear pair | Custom 36-tooth + LEGO 20-tooth |

---

# 5. Mechanical design

## 5.1 CAD and LEGO hybrid

We did not replace LEGO just because CAD was available. LEGO was useful for the drivetrain, gears, axles and differentials. CAD solved the problems that were more specific to our robot: a rigid chassis, camera mounting and electronics protection.

This made the final robot a hybrid rather than a completely CAD-built drivetrain.

## 5.2 Four-wheel drive

The final robot is **4WD**. One motor drives all four wheels through the central mechanical drivetrain.

With all four wheels powered, the steered wheels also receive drive force during large-angle turns. This reduced the tendency for the robot to push or slip compared with the earlier two-wheel-drive idea.

## 5.3 Mechanical differentials

The final drivetrain has **two LEGO mechanical differentials**, one on the front axle and one on the rear axle. The central driveshaft transfers motor power to both axles, while each differential allows the left and right wheels on that axle to rotate at different speeds in a turn.

An electronic differential is not used.

## 5.4 Steering

The steering servo is calibrated in software to the physical mechanism:

- **35° minimum**
- **75° centre**
- **115° maximum**

These values were experimentally tuned rather than taken only from the servo datasheet.

## 5.5 Gear ratio

The final external gear pair uses a custom **36-tooth** printed gear and a LEGO **20-tooth** gear.

The documented tooth-count relationship is:

**20 / 36 = 1 : 1.8**

The design intentionally trades some available torque for more wheel speed. The engineering document estimates a theoretical wheel speed of about 1080 RPM from the 600 RPM motor rating and this gear relationship, while the measured robot speed at the initial PWM was much lower in real operation.

---

# 6. Cameras and sensor placement

| Camera | Main job | Lens-centre height |
|---|---|---:|
| Front | Track + obstacle perception | 25.0 cm |
| Rear | Parking perception | 23.5 cm |

Final challenge configuration:

- front camera: **1480 × 520**, 60 FPS target;
- rear camera: **640 × 480**, 60 FPS target.

The final arrangement was chosen experimentally. Camera height and angle changed what the robot could see, so the mount was made adjustable.

---

# 7. Computer vision

## 7.1 Processing pipeline

### Open Challenge

```text
Camera frame
    ↓
HSV conversion
    ↓
Colour mask
    ↓
Opening / closing
    ↓
Contours
    ↓
Target point
```

### Obstacle Challenge

```text
Camera frame
    ↓
ROI crop
    ↓
HSV conversion
    ↓
Colour mask
    ↓
Opening / closing
    ↓
Contours
    ↓
Confidence filter
    ↓
Target point
```

## 7.2 Confidence filtering

The Obstacle Challenge uses:

**C = 0.65 C_HSV + 0.20 C_LAB + 0.15 C_geometry**

HSV coverage is the main colour evidence. LAB provides an additional colour-consistency check. Rectangularity contributes the geometry term.

Morphological opening and closing are used before contour extraction.

## 7.3 Processing performance

The recorded on-robot tests showed approximately:

| Challenge | Observed loop rate |
|---|---:|
| Open | 14.1 Hz mean |
| Obstacle | 11.25 Hz mean |

These are measured samples, not claims that the robot always runs at exactly those rates. The configured camera target remains 60 FPS.

At about 0.93 m/s and about 11 FPS, the robot travels roughly 8 cm between processed frames during the recorded obstacle-processing tests.

---

# 8. Steering control

The steering controller uses the image target position and direction-dependent behaviour.

The final physical steering calibration is:

```text
LEFT   = 35°
CENTER = 75°
RIGHT  = 115°
```

Open Challenge proportional gain:

```text
Kp = 0.013
```

These are the values documented and used for this release.

---

# 9. Software architecture

The software is split into small modules so the hardware, perception and challenge logic are not all mixed into one file.

| File | Purpose |
|---|---|
| `config.py` | Shared calibration and safety values |
| `drive.py` | Motor and steering output |
| `heading.py` | MPU6050 calibration and gyro heading |
| `vision.py` | Camera processing and detection helpers |
| `openVision.py` | Open Challenge vision |
| `open_challenge.py` | Open Challenge navigation and marker counting |
| `obstacle_challenge.py` | Obstacle detection, avoidance and lap-marker handling |
| `parking.py` | Parking approach, rear-camera detection and IMU-guided turns |
| `run_open.py` | Open Challenge launcher |
| `run_obstacle.py` | Obstacle Challenge launcher |

Safety behaviour in the current code includes IMU/I2C error handling, bounded IMU turns, parking timeout, temporal obstacle confirmation and cleanup that stops the robot.

---

# 10. Open Challenge

## 10.1 Direction markers

The first valid marker determines direction:

- **Blue → anticlockwise**
- **Orange → clockwise**

After direction is known, the program counts only the relevant marker colour.

## 10.2 Rising-edge counting

The marker should be counted when it changes from **not detected → detected**. A cooldown prevents a single marker from being counted repeatedly while it remains visible.

The documented cooldown is **1.0 s**.

## 10.3 Three laps and twelve crossings

The final configuration uses:

- 3 laps
- 4 relevant crossings per lap
- 12 total counted crossings

Open Challenge code values:

```text
LAPS_TO_COMPLETE = 3
LINES_PER_LAP    = 4
LINE_COOLDOWN    = 1
KP               = 0.013
CENTER           = 75
LEFT             = 35
RIGHT            = 115
```

---

# 11. Obstacle Challenge

The front camera identifies red and green obstacles and generates direction-dependent steering targets.

The rear camera is used for the magenta/purple parking marker.

The documented flow is:

1. avoid obstacles;
2. count the three lap markers using the rear camera;
3. after the third marker, continue through the extra section;
4. make the direction-dependent transition;
5. approach the parking area;
6. enter the parking state machine.

The robot does not use one universal obstacle-steering formula because the same image coordinate can require a different manoeuvre in the opposite direction.

---

# 12. Parking and IMU

## 12.1 Why timed turns were insufficient

An early approach used turn duration as a proxy for rotation. That changed with battery condition, motor speed, friction, wheel contact, steering geometry and acceleration.

The team therefore moved to IMU-based heading feedback.

## 12.2 MPU6050 calibration

At startup the code:

1. waits for the sensor to settle;
2. keeps the robot stationary;
3. collects **1500** Z-axis gyro samples;
4. averages them into a bias;
5. subtracts that bias from later readings;
6. integrates the corrected angular velocity into a 0–360° heading.

The IMU is read over I2C at the documented ±250°/s sensitivity and uses address `0x68`.

## 12.3 Parking state machine

The parking system is not one long timed manoeuvre. Its logic can be simplified to:

```text
Enter parking condition
        ↓
Parking approach
        ↓
Align
        ↓
Heading aligned?
   ↙          ↘
 no            yes
 ↓              ↓
IMU correction  Final manoeuvre
                 ↓
             Round complete
```

The rear camera provides the parking-area visual information and the IMU provides heading feedback during the manoeuvre.

## 12.4 Current parking status

The parking subsystem is **implemented and physically tested** using the rear camera, state machine and MPU6050 heading feedback.

The latest engineering document also states that the complete final parking manoeuvre **does not yet consistently achieve the required final position and alignment without contact**. The remaining engineering problem is calibration and reliable execution of the final manoeuvre.

That limitation is intentionally shown here rather than hidden.

---

# 13. Power architecture

The final power system separates the motor branch from the regulated logic branches.

```text
                         3S LiPo
                           │
            ┌──────────────┼──────────────┐
            │              │              │
          Buck 1        Motor driver     Buck 2
          5 V rail       raw VMOT       5 V / 5 A
            │              │              │
      Servo + logic     JGB37-520     Raspberry Pi 5
```

The Raspberry Pi is not used as the motor power source.

The final schematic shows the complete connection architecture.

---

# 14. Measured power

| Point | Condition | Measured value |
|---|---|---:|
| LiPo | Before run | 11.1 V |
| LiPo | After multiple runs | 10.8 V |
| Motor driver | Motors OFF | 11.1 V |
| Motor driver | Motors ON | 10.8 V |
| Buck 1 | Tested output | 5.0 V |
| Pi supply | Tested output | 5.0 V |

The final record does **not** contain a direct bench current measurement. No current value is invented here.

---

# 15. Software files

The exact source is in [`code/`](./code/).

The most important starting point is [`code/config.py`](./code/config.py), because it contains the calibrated steering, challenge and safety values.

For a first-time builder, follow [`SOFTWARE_SETUP.md`](./SOFTWARE_SETUP.md) instead of trying to run a challenge immediately.

---

# 16. Testing and results

## Open Challenge

Recorded complete runs:

**32, 30, 28, 28, 28, 28 s**

Best recorded result: **28 s**.

## Obstacle Challenge navigation

Recorded navigation runs:

**1:10, 1:09, 1:11, 1:20, 1:15, 1:13**

Best recorded navigation result: **1:09**.

The latest engineering document defines these obstacle times as navigation **up to the parking approach**. The final parking manoeuvre was tested separately and is still under development.

Raw evidence and CSV files are in [`testing/`](./testing/).

---

# 17. Engineering evolution

The most useful part of this project is not only the final robot. It is the chain of changes that produced it.

| Problem | Change | What we tested | Result |
|---|---|---|---|
| LEGO-heavy structure became difficult to rigidly mount | Added CAD/PLA structural parts | Chassis and mounting tests | More rigid custom structure |
| Two-wheel drive was not ideal for large steering angles | Moved to 4WD | Physical turning tests | Powered steered wheels |
| Differential requirement had to remain mechanical | Used two LEGO mechanical differentials | Drivetrain integration | Mechanical left/right speed difference |
| Johnson motor created stalling/current concern | Changed to JGB37-520 600 RPM | Motor and drivetrain testing | Lower-risk final drive motor |
| Pi could not safely power motor system | Separated power branches | Voltage measurements | Stable measured supply rails |
| First camera mount was too unstable | Designed adjustable CAD mount | Camera-view testing | More stable camera placement |
| One camera was not enough for rear parking information | Added second camera | Front/rear perception tests | Separate forward and parking views |
| Visual detections were sensitive to colour/geometry | HSV + LAB + morphology + confidence | On-robot vision tests | More controlled candidate rejection |
| Marker could be counted repeatedly | Rising-edge + cooldown | Repeated marker tests | 1 s cooldown, 12-crossing target |
| Timed turns varied with conditions | Added MPU6050 heading feedback | Parking tests | IMU-guided state machine |

The engineering document describes this as:

**Problem → Constraint → Design decision → Implementation → Test → Observation → Next iteration**

---

# 18. Failure analysis and current risks

We do not want this repository to pretend the robot is perfect.

### Current known risks

- final parking alignment still needs reliable calibration;
- gyro-only heading can accumulate drift over long periods;
- camera segmentation depends on lighting;
- obstacle processing is around 11 FPS in the recorded tests rather than the 60 FPS camera target;
- the servo/logic 5 V rail has limited headroom under some published servo stall-current estimates;
- exact installed servo stall current has not been directly bench-measured;
- obstacle test times were recorded with slightly different obstacle placement.

These are engineering observations, not reasons to hide the test data.

---

# 19. Repository and reproducibility

The repository is organised as:

```text
README.md
BUILD_FROM_ZERO.md
PARTS_CHECKLIST.md
WIRING_AND_PIN_REFERENCE.md
SOFTWARE_SETUP.md
CALIBRATION_AND_TESTING.md
JUDGE_QUICKSTART.md
code/
cad/
models/
schematics/
photos/
v-photos/
t-photos/
testing/
documentation/
```

### Reproducibility rule

For someone trying to reproduce the robot:

1. CAD/STL controls geometry.
2. Schematic controls wiring.
3. Source code controls software implementation.
4. The engineering PDF explains the design decisions and measured development history.
5. README and build guides explain how to navigate all of it.

### Native files

The repository contains the final STL exports and schematic render. The engineering document does not provide a verified native CAD project file or a complete per-fastener/per-LEGO-quantity assembly list, so those are not fabricated here.

---

# 20. Evidence included

The repository contains:

- final engineering document;
- Python source;
- final STL exports;
- CAD preview renders;
- electrical schematic;
- final robot views;
- development photos;
- testing video;
- Open Challenge results;
- processing observations;
- power measurements;
- engineering evolution notes.

See [`README_IMAGE_MANIFEST.md`](./README_IMAGE_MANIFEST.md) for the README visual-file map.

---

# 21. Nationals configuration check

This release is intended to represent the documented Nationals configuration.

- [x] 4WD drivetrain
- [x] Two mechanical LEGO differentials
- [x] Central driveshaft
- [x] JGB37-520 12 V 600 RPM motor
- [x] Raspberry Pi 5 4 GB
- [x] Two Camera Module 3 cameras
- [x] MPU6050
- [x] TB6612FNG
- [x] 3S 2200 mAh LiPo
- [x] CAD/PLA structural parts
- [x] 35° / 75° / 115° steering calibration
- [x] Open Challenge 3 laps / 12 crossings
- [x] 1.0 s marker cooldown
- [x] Obstacle red/green detection
- [x] Rear-camera magenta parking detection
- [x] IMU-guided parking state machine
- [x] Measured voltage evidence
- [x] Current left as not measured rather than fabricated
- [x] Final engineering PDF included

**Parking status:** implemented and physically tested, but final alignment remains an active calibration problem according to the latest engineering document.

---

# 22. Version

**v1.0 – Nationals Configuration**

The goal of this version is not to claim that every subsystem is perfect. The goal is that the repository describes the robot we actually built, the measurements we actually took, the code we actually run, and the problems we still know about.

---

# 23. Build from zero

For the complete beginner-friendly build sequence, use [`BUILD_FROM_ZERO.md`](./BUILD_FROM_ZERO.md).

It covers:

- parts;
- printing;
- drivetrain assembly;
- camera placement;
- electronics placement;
- power architecture;
- wiring;
- Raspberry Pi setup;
- steering calibration;
- IMU calibration;
- camera checks;
- challenge setup;
- testing order;
- troubleshooting;
- final acceptance checklist.

---

# 24. Wiring and pin reference

Use [`WIRING_AND_PIN_REFERENCE.md`](./WIRING_AND_PIN_REFERENCE.md) for the quick wiring reference and the software GPIO values.

The full schematic remains the authority for physical wiring.

---

# 25. Software setup

Use [`SOFTWARE_SETUP.md`](./SOFTWARE_SETUP.md) for the Raspberry Pi installation and dependency sequence.

---

# 26. Calibration and testing

Use [`CALIBRATION_AND_TESTING.md`](./CALIBRATION_AND_TESTING.md) for the exact order used to calibrate and test the documented configuration.

---

# 27. Judge quick start

Use [`JUDGE_QUICKSTART.md`](./JUDGE_QUICKSTART.md) for a five-minute tour of the robot, evidence, code, CAD and engineering story.

---

## Final note

We built The Dark Knight by changing things when testing showed a problem. The final repository is meant to show that process clearly instead of making the robot look like it worked perfectly on the first attempt.

**Use the materials we have intelligently, understand their limitations, and optimise the complete system rather than one component.**
