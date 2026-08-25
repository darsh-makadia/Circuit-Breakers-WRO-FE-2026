# Power & Sensor Architecture Evidence
## WRO Future Engineers 2026 — Team Current

This document provides an evidence-focused record of the robot's final power and sensor architecture. It distinguishes **directly measured robot data** from **manufacturer specifications and design-reference values**, so that unmeasured quantities are not presented as experimental results.

---

## 1. Final Power Architecture

The final robot uses a **3S 2200 mAh LiPo battery** as its primary energy source. Power is separated into three functional branches:

1. **Motor branch** — battery voltage is supplied to the TB6612FNG motor supply (`VMOT`).
2. **Servo and motor-driver logic branch** — regulated 5 V from Buck Converter 1 supplies the steering servo and the TB6612FNG logic rail.
3. **Raspberry Pi branch** — a separate regulated 5 V supply from Buck Converter 2 powers the Raspberry Pi 5 and its camera peripherals.

The Raspberry Pi 3.3 V rail supplies low-voltage devices including the MPU6050 IMU and OLED display. All branches share a common ground.

### Why the Power Branches Are Separated

The Raspberry Pi is not used as the source of motor power. Motor switching and changing drivetrain loads can disturb a shared logic supply, so the final architecture gives the Raspberry Pi its own regulated 5 V branch while the motor driver receives its motor supply directly from the battery-side branch.

The resulting architecture separates high-power drivetrain loading from the Raspberry Pi supply while maintaining a common electrical reference through shared ground.

---

## 2. Measured Voltage Evidence

The following values were directly recorded on the physical robot during testing.

| Measurement point | Condition | Recorded value | Evidence type |
|---|---|---:|---|
| LiPo | Before run | 11.1 V | Measured |
| LiPo | After multiple runs | 10.8 V | Measured |
| Buck 1 | Motors OFF | 5.0 V | Measured |
| Buck 1 | Robot moving | 5.0 V | Measured |
| Raspberry Pi supply | Idle | 5.0 V | Measured |
| Raspberry Pi supply | Moving | 5.0 V | Measured |
| Motor-driver supply | Motors OFF | 11.1 V | Measured |
| Motor-driver supply | Motors ON | 10.8 V | Measured |

### Interpretation

During the recorded tests, both regulated 5 V branches remained at the recorded 5.0 V value under the listed conditions. The battery and motor-driver supply decreased from 11.1 V to 10.8 V across the tested operating conditions.

These measurements describe the recorded test conditions only; they are not presented as guaranteed voltage behaviour for every battery state, load condition or competition run.

**Important measurement limitation:** whole-robot current was not directly measured during these tests. Therefore, this repository does not claim a measured whole-robot current draw.

Supporting measurement photographs and test evidence are stored in the repository's [`../v-photos/`](../v-photos/) directory where applicable.

---

## 3. Electrical Design Reference Budget

The following table is a **design-reference budget**, not a measured robot-current table.

| Load | Supply branch | Reference / limit | Evidence status |
|---|---|---|---|
| Raspberry Pi 5 | Regulated 5 V | 800 mA typical bare-board active current; 5 A PSU capacity recommended by Raspberry Pi documentation | Manufacturer reference |
| DS3225 steering servo | Regulated 5 V | 1.9 A stall current at 5 V | Manufacturer reference |
| TB6612FNG | Motor + 5 V logic | 1.2 A average / 3.2 A peak output-current rating per channel | Driver rating, not motor draw |
| JGB37-520 drive motor | Motor branch | Actual operating current not directly measured in this project | Measurement gap |
| Camera modules | Raspberry Pi branch | Powered through the final Raspberry Pi/camera architecture | Current not measured |
| MPU6050 / OLED | 3.3 V logic | Low-voltage sensor branch | Current not measured |

Manufacturer ratings and component limits are included as design references only. They are **not presented as measured robot consumption**.

### Nominal Battery Energy

**11.1 V × 2.2 Ah = 24.42 Wh**

This is nominal stored energy calculated from the battery's nominal voltage and stated capacity. It is not presented as guaranteed usable energy.

---

## 4. Measurement Limitations and Future Validation

The main remaining electrical measurement is **whole-robot current under real operating conditions**. This quantity has not yet been directly measured and is therefore not claimed elsewhere in the repository.

A future validation session should record:

- battery current at idle;
- battery current while driving straight;
- battery current during maximum steering;
- battery current during obstacle avoidance;
- battery current during parking;
- peak battery current during acceleration and turning;
- minimum regulated 5 V rail voltage during the same run.

Repeated measurements should use documented test conditions and record:

- test date;
- battery state;
- robot configuration;
- challenge program;
- relevant operating condition.

This would allow future electrical measurements to be compared without confusing them with the voltage evidence currently available.

---

## 5. Sensor Architecture and Engineering Trade-offs

The final sensor architecture was selected through subsystem testing and calibration rather than by adding sensors without a defined role.

| Decision | Alternative considered | Why the final choice was made | Failure / mitigation |
|---|---|---|---|
| Two cameras | One camera | The front camera supports normal navigation and challenge perception, while the rear camera provides a dedicated view for parking | Camera-dependent states are bounded and should fail safely |
| Front camera at ~25.0 cm | Lower or less stable mount | The final mount provides a repeatable view of track boundaries and challenge markers | Mount placement was redesigned after early placement problems |
| Rear camera at ~23.5 cm | Front-only parking | A rear-facing view provides direct information about the parking area and marker | Parking is controlled by a bounded state machine and timeout |
| MPU6050 heading feedback | Timed turns only | Timed turns varied with battery state, friction, wheel contact and speed | Gyro bias is calibrated and turning loops are time-bounded |
| HSV + LAB + geometry | Single colour space | Combining colour evidence with geometry reduces dependence on a single threshold | Contour filtering and temporal confirmation reject unstable detections |

The front and rear cameras therefore have separate functional roles rather than serving as redundant copies of the same sensor.

---

## 6. Calibration Evidence

### MPU6050 Heading System

The implemented heading procedure includes:

1. an initial settling period;
2. **1500 stationary Z-axis gyro samples**;
3. average gyro-bias calculation;
4. bias subtraction during operation;
5. heading integration with 0–360° wrapping;
6. safe stopping on IMU/I2C failure;
7. time limits on turning loops.

This calibration procedure reduces the effect of the stationary gyro bias measured during startup. The implementation and related source code are available in [`../src/`](../src/).

### Vision Pipeline

The vision system uses calibrated:

- HSV thresholds;
- LAB colour checks;
- morphological processing;
- contour filtering;
- colour coverage;
- geometric scoring;
- combined confidence scoring.

The implemented confidence expression is:

**Confidence = 0.65 × HSV + 0.20 × LAB + 0.15 × geometry**

Thresholds are treated as calibration values and are adjusted only through testing on the physical robot rather than being presented as universal values.

---

## 7. Sensor Failure and Interference Considerations

| Failure mode | Effect | Implemented mitigation |
|---|---|---|
| Camera frame contains noise | Wrong colour or contour candidate | Morphology, contour filtering and temporal confirmation |
| One marker remains visible across frames | Same marker may be counted repeatedly | Rising-edge detection and a 1.0 s cooldown |
| One wall disappears from the camera view | Wall-following error | Direction-dependent wall following and fallback priorities |
| IMU/I2C error | Heading feedback unavailable | Safe stop and bounded turning loops |
| Battery voltage changes | Timed-turn accuracy can change | MPU6050 heading feedback is used where heading correction is required |
| Motor switching affects logic supply | Raspberry Pi instability risk | Separate regulated Raspberry Pi power branch |

The architecture therefore combines sensor-level filtering, state-machine bounds and electrical separation rather than relying on a single mitigation for each failure mode.

---

## 8. Evidence Scope

This document intentionally distinguishes three categories of information:

- **Measured evidence** — values directly recorded on the physical robot.
- **Manufacturer/design reference** — component specifications, ratings and nominal calculations.
- **Measurement gaps** — quantities that have not yet been directly measured.

This distinction is maintained throughout the document to avoid presenting specification values as experimental results.

---

## Judge-Facing Conclusion

The final architecture is supported by:

- measured voltage evidence on the physical robot;
- separated power branches for the motor system, servo/logic rail and Raspberry Pi;
- documented sensor roles and placement decisions;
- MPU6050 bias calibration and bounded heading control;
- calibrated computer-vision processing;
- software-level handling for selected sensor and detection failures.

Where direct current measurements do not exist, the repository explicitly identifies the quantity as **not measured**. Manufacturer ratings are retained only as design references.

This evidence record is intended to make clear both **what has been validated experimentally** and **what remains outside the current measurement record**.
