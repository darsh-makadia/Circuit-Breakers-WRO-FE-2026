# The Dark Knight
## WRO Future Engineers 2026 — Team Current
### v1.0 — Nationals Configuration

This is the GitHub repository for **The Dark Knight**, our WRO Future Engineers 2026 robot.

The repository contains our robot design, mechanical development, electronics, software, computer vision, challenge algorithms, CAD/STL files, testing evidence, photographs and build documentation.

---

# Table of Contents

- [1. Team](#1-team)
- [2. Final Robot Overview](#2-final-robot-overview)
- [3. Robot and CAD Visual Reference](#3-robot-and-cad-visual-reference)
  - [Robot Photos](#robot-photos)
  - [CAD Models](#cad-models)
  - [Circuit Schematic](#circuit-schematic)
  - [Final STL Files](#final-stl-files)
- [4. Final Robot Specifications](#4-final-robot-specifications)
- [5. Mechanical Design](#5-mechanical-design)
  - [5.1 CAD + LEGO Hybrid Architecture](#51-cad--lego-hybrid-architecture)
  - [5.2 Four-Wheel Drive](#52-four-wheel-drive)
  - [5.3 Gear Ratio](#53-gear-ratio)
- [6. Cameras and Perception](#6-cameras-and-perception)
- [7. Computer Vision](#7-computer-vision)
- [8. Steering](#8-steering)
- [9. Software Architecture](#9-software-architecture)
- [10. Open Challenge](#10-open-challenge)
  - [10.1 Navigation](#101-navigation)
  - [10.2 Direction Markers](#102-direction-markers)
  - [10.3 Marker Counting](#103-marker-counting)
  - [10.4 Recorded Results](#104-recorded-results)
- [11. Obstacle Challenge](#11-obstacle-challenge)
- [12. Parking and MPU6050](#12-parking-and-mpu6050)
- [13. Power Architecture](#13-power-architecture)
- [14. Measured Power Results](#14-measured-power-results)
- [15. Engineering Evolution](#15-engineering-evolution)
- [16. Recorded Challenge Performance](#16-recorded-challenge-performance)
- [17. Known Development History](#17-known-development-history)
- [18. Repository Structure](#18-repository-structure)
- [19. Documentation and Build Index](#19-documentation-and-build-index)
- [20. Evidence Included in This Repository](#20-evidence-included-in-this-repository)
- [21. Final Nationals Configuration Verification](#21-final-nationals-configuration-verification)
- [22. Version](#22-version)

---

# Repository Index

## 📖 Documentation & Guides

| Resource | Description |
|---|---|
| [🚀 Start Here](./guide/START_HERE.md) | Main navigation and recommended reading order |
| [🔧 Build From Zero](./guide/BUILD_FROM_ZERO.md) | Complete robot build and reproduction guide |
| [📦 Parts Checklist](./guide/PARTS_CHECKLIST.md) | Electronics, printed parts and drivetrain checklist |
| [⚡ Wiring & Pin Reference](./guide/WIRING_AND_PIN_REFERENCE.md) | Power architecture, wiring and GPIO reference |
| [💻 Software Setup](./guide/SOFTWARE_SETUP.md) | Raspberry Pi software and source setup |

## 🤖 Robot Resources

| Resource | Description |
|---|---|
| [Source Code](./src/) | Complete Python source |
| [CAD / STL Models](./models/) | Printable CAD files and model previews |
| [Robot Photos](./v-photos/) | Robot and development photographs |
| [Circuit Schematic](./schemes/schematic.png) | Final electrical schematic |

### Recommended Reading Order

**Start Here → Build From Zero → Parts Checklist → Wiring Reference → Software Setup → Source Code → CAD/STL → Photos → Schematic**

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

The Dark Knight is our autonomous four-wheel-drive robot developed for **WRO Future Engineers 2026**.

The final documented configuration combines custom 3D-printed mechanical components with a LEGO Technic drivetrain and Raspberry Pi based control.

### Main Systems

- Raspberry Pi 5 — 4 GB
- Two Raspberry Pi Camera Module 3 cameras
- JGB37-520 DC geared motor — 12 V, 600 RPM
- Servo steering
- MPU6050 IMU
- TB6612FNG motor driver
- 3S LiPo battery — 2200 mAh
- PLA 3D-printed structural components
- LEGO Technic drivetrain components
- Two mechanical differentials
- Central driveshaft

The robot was developed through multiple iterations. Mechanical geometry, drivetrain configuration, camera mounting, power distribution and software were repeatedly tested and improved before reaching the documented Nationals configuration.

---

# 3. Robot and CAD Visual Reference

All physical evidence and CAD resources are stored directly in the repository.

## Robot Photos

The complete collection is available in:

**[📸 Open Robot Photos →](./v-photos/)**

### Front View

<a href="./v-photos/front_view.png">
<img src="./v-photos/front_view.png" alt="The Dark Knight front view" width="700">
</a>

### Back View

<a href="./v-photos/back_view.png">
<img src="./v-photos/back_view.png" alt="The Dark Knight back view" width="700">
</a>

### Side Views

<p align="center">
  <a href="./v-photos/side_view_1.png">
    <img src="./v-photos/side_view_1.png" alt="The Dark Knight side view 1" width="45%">
  </a>
  <a href="./v-photos/side_view_2.png">
    <img src="./v-photos/side_view_2.png" alt="The Dark Knight side view 2" width="45%">
  </a>
</p>

### Motor and Steering

<p align="center">
  <a href="./v-photos/motor_close_up.png">
    <img src="./v-photos/motor_close_up.png" alt="JGB37-520 drive motor" width="45%">
  </a>
  <a href="./v-photos/servo_close_up.png">
    <img src="./v-photos/servo_close_up.png" alt="Steering servo" width="45%">
  </a>
</p>

### Differential and Electronics

<p align="center">
  <a href="./v-photos/differential.png">
    <img src="./v-photos/differential.png" alt="Mechanical differential" width="45%">
  </a>
  <a href="./v-photos/circuit_case_and_battery.png">
    <img src="./v-photos/circuit_case_and_battery.png" alt="Circuit case and battery" width="45%">
  </a>
</p>

### Electronics From Above

<a href="./v-photos/circuit_from_top.png">
<img src="./v-photos/circuit_from_top.png" alt="Electronics from above" width="800">
</a>

---

## CAD Models

All CAD/STL resources are stored in:

**[🧩 Open Models Folder →](./models/)**

### Final Chassis

<a href="./models/chassis.png">
<img src="./models/chassis.png" alt="Final CAD chassis" width="700">
</a>

### Final Chassis — Part 2

<a href="./models/Chassis%20pt2%20(1).png">
<img src="./models/Chassis%20pt2%20(1).png" alt="Final chassis part 2" width="700">
</a>

### Circuit Box

<a href="./models/circuit_box.png">
<img src="./models/circuit_box.png" alt="Circuit box CAD" width="700">
</a>

### Circuit Box Lid

<a href="./models/circuit_box_lid.png">
<img src="./models/circuit_box_lid.png" alt="Circuit box lid CAD" width="700">
</a>

### Camera Mount

<a href="./models/camera_mount.png">
<img src="./models/camera_mount.png" alt="Camera mount CAD" width="700">
</a>

### Camera Case

<a href="./models/camera_case.png">
<img src="./models/camera_case.png" alt="Camera case CAD" width="600">
</a>

---

## Circuit Schematic

The final electrical schematic is stored in the `schemes/` folder.

<a href="./schemes/schematic.png">
<img src="./schemes/schematic.png" alt="Final circuit schematic" width="1000">
</a>

**[⚡ Open Full Schematic →](./schemes/schematic.png)**

---

## Final STL Files

The following are the actual STL files stored in the repository.

| Model | Actual STL File | Purpose |
|---|---|---|
| Final chassis | [`currents final chassis (1).stl`](./models/currents%20final%20chassis%20(1).stl) | Main custom chassis |
| Final chassis — Part 2 | [`currents final chassis pt2 (1) (1).stl`](./models/currents%20final%20chassis%20pt2%20(1)%20(1).stl) | Additional chassis component |
| Dual camera mount | [`currnts dual camera mount (1).stl`](./models/currnts%20dual%20camera%20mount%20(1).stl) | Dual-camera mounting system |
| Camera case | [`camera case (1) (1).stl`](./models/camera%20case%20(1)%20(1).stl) | Camera enclosure |
| Circuit box | [`currents CB (1).stl`](./models/currents%20CB%20(1).stl) | Electronics enclosure |
| Circuit box lid | [`currents CB LID (1).stl`](./models/currents%20CB%20LID%20(1).stl) | Electronics enclosure lid |

GitHub may not render STL geometry directly in every view, but each filename links to the actual file stored in `models/`.

---

# 4. Final Robot Specifications

| Specification | Final Value |
|---|---:|
| Length | **24 cm** |
| Width | **13 cm** |
| Height | **27.5 cm** |
| Mass | **863 g** |
| Wheel diameter | **43.2 mm** |
| Gear ratio | **1.8:1** |
| Drive configuration | **4WD** |
| Differential | **Two mechanical LEGO differentials, one per axle** |
| Drive motor | **JGB37-520 DC, 12 V, 600 RPM** |
| Steering | **Servo steering** |
| Main computer | **Raspberry Pi 5, 4 GB** |
| Cameras | **2 × Raspberry Pi Camera Module 3** |
| Orientation sensor | **MPU6050** |
| Motor driver | **TB6612FNG** |
| Battery | **3S LiPo, 2200 mAh, 11.1 V nominal** |
| Structural material | **PLA / CAD printed parts** |

---

# 5. Mechanical Design

## 5.1 CAD + LEGO Hybrid Architecture

The final robot uses two complementary manufacturing systems.

### CAD / PLA

Custom 3D-printed components include:

- Main chassis
- Chassis extension
- Camera mount
- Camera case
- Electronics enclosure
- Electronics enclosure lid
- Custom drivetrain gear
- Other mounting components

### LEGO Technic

LEGO Technic components are used for the drivetrain, including:

- Beams
- Axles
- Bushes
- Gears
- Universal joints
- Differential assemblies
- Connectors
- Pins

This hybrid approach allowed us to maintain a modular drivetrain while using custom geometry for the chassis, electronics and camera systems.

---

## 5.2 Four-Wheel Drive

The final robot uses **four-wheel drive**.

Power is transferred through a central drivetrain and distributed through mechanical differentials.

The architecture uses:

- One central drive motor
- One central driveshaft
- One mechanical differential for the front axle
- One mechanical differential for the rear axle
- Four driven wheels

The mechanical differential allows the left and right wheels of an axle to rotate at different speeds while cornering.

This was particularly useful during high-steering-angle manoeuvres and parking.

---

## 5.3 Gear Ratio

The final external gear pair consists of:

- **36-tooth custom printed gear**
- **20-tooth LEGO gear**

This produces a documented tooth-count relationship of:

**36 : 20 = 1.8 : 1**

The design was selected to provide higher wheel speed while maintaining sufficient drivetrain performance for the competition surface.

A recorded speed test covered:

**3 m in 2.25 s**

which corresponds to approximately:

**1.33 m/s ≈ 4.8 km/h**

---

# 6. Cameras and Perception

The robot uses **two Raspberry Pi Camera Module 3 cameras**.

## Front Camera

Primary functions:

- Track perception
- Wall/boundary detection
- Blue marker detection
- Orange marker detection
- Green obstacle detection
- Red obstacle detection

Documented configuration:

- Resolution: **1480 × 520**
- Target frame rate: **60 FPS**
- Lens-centre height: approximately **25.0 cm**

## Rear Camera

Primary functions:

- Parking-area perception
- Parking marker detection
- Final parking alignment

Documented configuration:

- Resolution: **640 × 480**
- Target frame rate: **60 FPS**
- Lens-centre height: approximately **23.5 cm**

The camera system uses separate front and rear perception because the requirements of normal navigation and parking are different.

---

# 7. Computer Vision

The robot uses **OpenCV** for computer vision.

Main source modules:

- [`vision.py`](./src/vision.py)
- [`openVision.py`](./src/openVision.py)

The vision pipeline generally follows:

```text
Camera Frame
     │
     ▼
Colour Processing
     │
     ▼
Mask Generation
     │
     ▼
Morphological Filtering
     │
     ▼
Contour Detection
     │
     ▼
Geometric Filtering
     │
     ▼
Target Detection
     │
     ▼
Steering / Navigation
