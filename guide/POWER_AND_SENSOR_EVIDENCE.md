# Power & Sensor Architecture Evidence
## WRO Future Engineers 2026 — Team Current

This document is an evidence-focused supplement for judging. It separates **measured robot data** from **manufacturer/design data** so that no unmeasured current value is presented as a test result.

---

## 1. Final power architecture

The Nationals robot uses a **3S 2200 mAh LiPo** as the primary energy source.

Power is separated into three functional branches:

1. **Motor branch** — battery voltage is supplied to the TB6612FNG motor supply.
2. **Servo / logic branch** — regulated 5 V from a buck converter.
3. **Raspberry Pi branch** — regulated 5 V from a separate buck converter for the Raspberry Pi 5 and camera peripherals.

The Raspberry Pi 3.3 V rail is used for low-voltage devices such as the MPU6050 and OLED. All branches share a common ground.

### Why we separated the power branches

The Raspberry Pi should not be used as the motor-power source. Motor switching and load changes can disturb the logic supply, so the final design gives the Pi its own regulated branch while the motor driver receives the battery-side motor supply.

---

## 2. Measured voltage evidence

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

**Important:** current was not directly measured during these tests. Therefore this repository does not claim a measured whole-robot current draw.

---

## 3. Electrical design budget

The table below is a **design-reference budget**, not a measured robot-current table.

| Load | Supply branch | Reference / limit | Status |
|---|---|---:|---|
| Raspberry Pi 5 | Regulated 5 V | 800 mA typical bare-board active current; 5 A PSU capacity recommended by Raspberry Pi documentation | Manufacturer reference |
| DS3225 servo | Regulated 5 V | 1.9 A stall current at 5 V | Manufacturer reference |
| TB6612FNG | Motor + 5 V logic | 1.2 A average / 3.2 A peak output-current rating per channel | Driver rating, not motor draw |
| Drive motor | Motor branch | Actual operating current not measured in this project | Measurement gap |
| Camera modules | Raspberry Pi branch | Powered through the final Pi/camera architecture | Current not measured |
| MPU6050 / OLED | 3.3 V logic | Low-voltage sensor branch | Current not measured |

Manufacturer ratings are **not** presented as measured robot consumption.

### Nominal battery energy

**11.1 V × 2.2 Ah = 24.42 Wh**

This is nominal stored energy, not guaranteed usable energy.

---

## 4. Remaining electrical evidence

The main remaining electrical measurement is **whole-robot current under real operating conditions**.

Do not invent this value.

For the next validation session, record:

- battery current at idle;
- battery current while driving straight;
- battery current during maximum steering;
- battery current during obstacle avoidance;
- battery current during parking;
- peak battery current during acceleration/turning;
- minimum 5 V rail voltage during the same run.

Use the same test conditions for repeated runs and record date, battery state and configuration.

---

## 5. Sensor architecture and trade-offs

| Decision | Alternative considered | Why the final choice was made | Failure / mitigation |
|---|---|---|---|
| Two cameras | One camera | Front camera is needed for normal navigation while a rear view is useful for parking | Camera-dependent states are bounded and should fail safely |
| Front camera at ~25.0 cm | Lower/less stable mount | The final mount gives a repeatable view of track boundaries and challenge markers | Mount was redesigned after early placement problems |
| Rear camera at ~23.5 cm | Front-only parking | Rear view gives direct information about the parking area and marker | Parking is controlled by a state machine and timeout |
| MPU6050 heading feedback | Timed turns only | Timed turns varied with battery state, friction, wheel contact and speed | Gyro bias is calibrated and turns are time-bounded |
| HSV + LAB + geometry | Single colour space | Combining colour spaces with geometry reduces dependence on one threshold | Contour filtering and temporal confirmation reject unstable detections |

---

## 6. Calibration evidence

### MPU6050

1. settling period;
2. **1500 stationary Z-axis gyro samples**;
3. average gyro-bias calculation;
4. bias subtraction during operation;
5. heading integration with 0–360° wrapping;
6. safe stopping on IMU/I2C failure;
7. time limits on turning loops.

### Vision

The pipeline uses calibrated HSV/LAB thresholds, morphology, contour filtering, colour coverage, geometry and confidence scoring.

**Confidence = 0.65 × HSV + 0.20 × LAB + 0.15 × geometry**

Thresholds are treated as calibration values and are changed only after testing on the real robot.

---

## 7. Sensor failure and interference considerations

| Failure mode | Effect | Mitigation |
|---|---|---|
| Camera frame contains noise | Wrong colour/contour candidate | Morphology + contour filtering + temporal confirmation |
| One marker remains visible across frames | Same marker counted repeatedly | Rising-edge detection + 1.0 s cooldown |
| One wall disappears | Wall-following error | Direction-dependent wall following + fallback priorities |
| IMU/I2C error | Heading feedback unavailable | Safe stop + bounded turn loops |
| Battery voltage changes | Timed-turn accuracy changes | MPU6050 heading feedback for parking |
| Motor switching affects logic supply | Pi instability risk | Separate regulated Pi power branch |

---

## Judge-facing conclusion

The final architecture is based on measured voltage stability, sensor-placement testing, camera-role separation, IMU calibration and software-level failure handling.

Where a direct current measurement does not exist, the repository explicitly says **not measured**. Manufacturer ratings are included only as design references.
