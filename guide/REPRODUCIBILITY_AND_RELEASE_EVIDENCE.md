# Reproducibility & Release Evidence
## WRO Future Engineers 2026 — Team Current

This document records the versioned robot configuration and provides a reproducibility path from the repository files to the documented challenge-validation results.

---

## 1. Versioned Nationals Baseline

**Release:** v1.1 — Nationals Evidence Update

The documented baseline is:

- 4WD drivetrain
- Two mechanical LEGO differentials
- Central driveshaft
- Two Raspberry Pi Camera Module 3 cameras
- Raspberry Pi 5 (4 GB)
- MPU6050 IMU
- JGB37-520 12 V 600 RPM drive motor
- TB6612FNG motor driver
- 3S 2200 mAh LiPo battery
- CAD-designed PLA structural parts
- Servo steering
- Python + OpenCV software

Any change after this baseline must be recorded in the repository documentation and, where relevant, reflected in the corresponding source code, configuration, or test evidence.

---

## 2. Repository Structure

```text
Team-Current-WRO-FE-2026/
├── README.md
├── CHANGELOG.md
├── guide/
│   ├── START_HERE.md
│   ├── BUILD_FROM_ZERO.md
│   ├── WIRING_AND_PIN_REFERENCE.md
│   ├── POWER_AND_SENSOR_EVIDENCE.md
│   ├── 3D_PRINTING_SETTINGS.md
│   ├── REPRODUCIBILITY_AND_RELEASE_EVIDENCE.md
│   └── additional build and software documentation
├── models/
├── schemes/
├── src/
├── testing/
├── v-photos/
├── t-photos/
└── video/
```

The repository separates build instructions, electrical and sensor evidence, source code, CAD/STL files, schematics, testing evidence, robot photographs, team photographs, and challenge video material.

---

## 3. Source-to-Function Mapping

| File | Function |
| --- | --- |
| `src/Current_Open_8_22.py` | Open Challenge program |
| `src/Current_Obstacle_8_21.py` | Obstacle Challenge program |
| `src/drive.py` | Motor and steering control |
| `src/heaeding.py` | MPU6050 heading and calibration |
| `src/vision.py` | Camera and colour/target processing |
| `src/openVision.py` | Open Challenge vision processing |
| `src/parking.py` | Parking state machine and IMU-guided turns |

The unusual filename `heaeding.py` is retained because it is the actual repository filename.

---

## 4. Hardware-to-Evidence Mapping

| Hardware or subsystem | Evidence location |
| --- | --- |
| Custom chassis | `models/` + `v-photos/` |
| Drivetrain and differentials | `guide/BUILD_FROM_ZERO.md` + `v-photos/` |
| Camera mount and camera case | `models/` + `v-photos/` |
| Circuit enclosure | `models/` + `v-photos/` |
| 3D-printing configuration | `guide/3D_PRINTING_SETTINGS.md` |
| Wiring and GPIO configuration | `guide/WIRING_AND_PIN_REFERENCE.md` |
| Power and sensor architecture | `guide/POWER_AND_SENSOR_EVIDENCE.md` |
| Final electrical schematic | `schemes/` |
| Final robot views | `v-photos/` |
| Team photographs | `t-photos/` |
| Final STL exports | `models/` |
| Challenge programs | `src/` |
| Testing evidence | `testing/` |
| Challenge video evidence | `video/` |

---

## 5. Reproduction Workflow

The repository is organised so that a new builder can reproduce the documented configuration by following the stages below.

### Step 1 — Prepare the Printed Parts

Use:

- [`3D_PRINTING_SETTINGS.md`](3D_PRINTING_SETTINGS.md)
- The final STL files in [`models/`](../models/)

The printing guide documents the OrcaSlicer baseline, rapid-testing configuration, and stronger final-print configuration.

### Step 2 — Assemble the Robot

Follow:

[`BUILD_FROM_ZERO.md`](BUILD_FROM_ZERO.md)

This guide documents the drivetrain, differentials, external gear stage, chassis, steering, camera placement, electronics integration, and initial software setup.

### Step 3 — Complete the Electrical System

Follow:

- [`WIRING_AND_PIN_REFERENCE.md`](WIRING_AND_PIN_REFERENCE.md)
- [`POWER_AND_SENSOR_EVIDENCE.md`](POWER_AND_SENSOR_EVIDENCE.md)
- The final schematic in [`schemes/`](../schemes/)

The documented architecture keeps the Raspberry Pi on a separate regulated 5 V branch while the motor driver receives the battery-side motor supply. All branches share a common ground.

### Step 4 — Set Up the Software

Use the source files in [`src/`](../src/) and install the documented Raspberry Pi software dependencies.

The project uses Python with the Raspberry Pi camera and hardware stack, including:

- OpenCV
- NumPy
- RPi.GPIO
- Picamera2
- MPU6050 I2C communication

Confirm that both cameras, the MPU6050, motor control, and steering control operate before running a challenge program.

### Step 5 — Calibrate the Robot

Before challenge testing:

1. Verify camera orientation and mounting position.
2. Calibrate vision thresholds on the physical field.
3. Perform stationary MPU6050 gyro calibration.
4. Verify steering centre and steering limits.
5. Verify marker counting and cooldown behaviour.
6. Verify safe-stop behaviour for sensor or control failures.

### Step 6 — Validate the Open Challenge

Run repeated trials and record:

- Selected direction
- Marker detections
- Lap count
- Completion status
- Total time
- Failure mode, if unsuccessful

The documented best result is:

**28 s across six recorded runs.**

### Step 7 — Validate the Obstacle Challenge

Run repeated trials and record:

- Obstacle detection
- Avoidance decision
- Selected direction
- Obstacle-sequence completion
- Transition toward the parking area
- Total time
- Failure mode, if unsuccessful

The documented best result is:

**1:09 across six recorded runs.**

The six recorded obstacle runs measure the documented obstacle sequence without including a completed parallel-parking result. Parking development and validation are documented separately and should not be inferred from the timed obstacle results.

---

## 6. Configuration Lock

Before competition or a documented validation session, record the exact software and calibration values used for that specific configuration.

Record:

- Steering centre/min/max
- Open Challenge `KP`
- Marker cooldown
- Lap count
- Crossing count
- Camera resolution
- Camera mounting position
- Obstacle confidence thresholds
- Parking-state and heading thresholds, where parking is being tested
- MPU6050 calibration procedure and values used for the run

The documented baseline includes:

- Steering range: **35°–75°–115°**
- Open Challenge `KP = 0.013`
- Three laps
- 12 relevant crossings
- 1.0 s marker cooldown

Any changed configuration should be recorded together with the test result produced using that configuration.

---

## 7. Testing Evidence Standard

For every important engineering change, record:

> **Problem → Hypothesis → Change → Test Conditions → Result → Decision**

### Example

**Problem:** One physical marker could remain visible for multiple frames.

**Hypothesis:** Frame-by-frame counting was creating duplicate detections.

**Change:** Added rising-edge detection and a 1.0 s cooldown.

**Test:** Repeated three-lap runs.

**Result:** The final marker-counting logic uses 12 relevant crossings.

**Decision:** Keep the rising-edge and cooldown approach.

This structure makes engineering decisions reproducible and distinguishes tested changes from unverified assumptions.

---

## 8. Release Discipline

Future engineering commits should use descriptive messages rather than generic messages such as `Update README.md`.

Recommended format:

```text
mechanical: revise camera mount
vision: add LAB confidence weighting
navigation: add marker rising-edge detection
parking: add IMU turn timeout
power: separate Pi and motor branches
testing: record six obstacle runs
docs: publish Nationals evidence update
```

This makes the engineering history easier to trace and allows a future configuration to be connected to the change that produced it.

---

## 9. Final Reproducibility Checklist

- [x] Versioned baseline configuration documented
- [x] Mechanical build workflow documented
- [x] 3D-printing configuration documented
- [x] Source code separated by function
- [x] CAD/STL files included
- [x] Electrical schematic included
- [x] Wiring and GPIO reference documented
- [x] Power and sensor architecture documented
- [x] Robot photographs included
- [x] Team photographs included
- [x] Challenge testing evidence included
- [x] Engineering evolution documented
- [x] Calibration process documented
- [x] Failure handling documented
- [x] Configuration-lock procedure documented
- [ ] Whole-robot current measurement added
- [ ] Fully validated parallel-parking result added

The unchecked items are intentionally left open rather than being represented as completed engineering evidence.
