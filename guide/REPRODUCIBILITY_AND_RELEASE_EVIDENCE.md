# Reproducibility & Release Evidence
## WRO Future Engineers 2026 — Team Current

This document is the judge-facing reproducibility record for the Nationals configuration.

---

## 1. Versioned Nationals baseline

**Release:** v1.1 — Nationals Evidence Update

The documented baseline is:

- 4WD
- two mechanical LEGO differentials
- central driveshaft
- two Raspberry Pi Camera Module 3 cameras
- Raspberry Pi 5 4 GB
- MPU6050
- JGB37-520 12 V 600 RPM motor
- TB6612FNG motor driver
- 3S 2200 mAh LiPo
- CAD/PLA structural parts
- servo steering
- Python + OpenCV software

Any physical change after this baseline must be reflected in the code and documentation.

---

## 2. Repository structure

```text
Team-Current-WRO-FE-2026/
├── README.md
├── CHANGELOG.md
├── guide/
├── models/
├── schemes/
├── src/
├── testing/
├── v-photos/
└── video/
```

The repository separates source code, CAD/STL files, photographs, schematic evidence, testing material and build documentation.

---

## 3. Source-to-function mapping

| File | Function |
|---|---|
| `src/Current_Open_8_22.py` | Open Challenge program |
| `src/Current_Obstacle_8_21.py` | Obstacle Challenge program |
| `src/drive.py` | Motor and steering control |
| `src/heaeding.py` | MPU6050 heading/calibration |
| `src/vision.py` | Camera and colour/target processing |
| `src/openVision.py` | Open Challenge vision processing |
| `src/parking.py` | Parking state machine and IMU-guided turns |

The unusual filename `heaeding.py` is retained because it is the actual repository filename.

---

## 4. Hardware-to-evidence mapping

| Hardware | Evidence location |
|---|---|
| Custom chassis | `models/` + `v-photos/` |
| Camera mount/case | `models/` + `v-photos/` |
| Circuit enclosure | `models/` + `v-photos/` |
| Schematic | `schemes/schematic.png` |
| Final robot views | `v-photos/` |
| Final STL exports | `models/` |
| Challenge code | `src/` |
| Testing evidence | `testing/` |

---

## 5. Reproduction workflow

### Step 1 — Mechanical build

Use the final STL exports in `models/` and the documented LEGO Technic drivetrain/differential arrangement.

### Step 2 — Electrical build

Follow the final schematic in `schemes/schematic.png`.

Keep the Raspberry Pi on its regulated branch and keep the motor supply on the motor-driver branch.

### Step 3 — Software environment

The project uses Python and the documented Raspberry Pi software stack, including OpenCV, NumPy, RPi.GPIO and Picamera2.

### Step 4 — Calibration

Before challenge testing:

1. verify camera orientation and mounting height;
2. calibrate the vision thresholds on the real field;
3. perform MPU6050 stationary calibration;
4. verify steering centre and limits;
5. verify safe-stop behaviour.

### Step 5 — Open Challenge validation

Run repeated trials and record:

- direction selected;
- marker detections;
- lap count;
- completion status;
- total time;
- failure mode if unsuccessful.

Final documented result:

**28 s best time across six recorded runs.**

### Step 6 — Obstacle Challenge validation

Run repeated trials and record:

- obstacle detection;
- avoidance decision;
- direction;
- parking transition;
- parking completion;
- total time;
- failure mode.

Final documented result:

**1:09 best time across six recorded runs.**

---

## 6. Configuration lock

Before competition, record the exact values used in:

- steering centre/min/max;
- Open Challenge KP;
- marker cooldown;
- lap count;
- crossing count;
- camera resolution;
- camera mounting position;
- obstacle confidence thresholds;
- parking thresholds;
- IMU calibration values.

The README currently documents the final steering range as **35°–75°–115°**, Open Challenge `KP = 0.013`, three laps, 12 relevant crossings and a 1.0 s marker cooldown.

---

## 7. Testing evidence standard

For every important change, record:

**Problem → hypothesis → change → test conditions → result → decision**

Example:

**Problem:** One physical marker could remain visible for multiple frames.

**Hypothesis:** Frame-by-frame counting was creating duplicate detections.

**Change:** Added rising-edge detection and a 1.0 s cooldown.

**Test:** Repeated three-lap runs.

**Result:** Final marker-counting logic uses 12 relevant crossings.

**Decision:** Keep the rising-edge + cooldown approach.

---

## 8. Release discipline

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

This makes the engineering history understandable to a judge.

---

## 9. Final reproducibility checklist

- [x] Final robot configuration documented
- [x] Source code separated by function
- [x] CAD/STL files included
- [x] Schematic included
- [x] Robot photographs included
- [x] Recorded challenge results included
- [x] Engineering evolution documented
- [x] Calibration process documented
- [x] Failure handling documented
- [x] Version baseline defined
- [ ] Whole-robot current measurement added

The final unchecked item is intentionally left open rather than filled with an invented value.
