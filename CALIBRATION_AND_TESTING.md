# Calibration and testing procedure

This is the practical checklist for reproducing the tuning process.

## 1. Mechanical calibration

### Steering

Set and verify:

- minimum: 35°
- centre: 75°
- maximum: 115°

Check that the steering linkage is straight at 75° and does not bind at either limit.

### Drivetrain

Confirm:

- all four wheels are powered;
- both axle differentials rotate correctly;
- central driveshaft transfers motion to both axles;
- the 36-tooth / 20-tooth gear pair meshes without binding.

## 2. IMU calibration

Keep the robot stationary at startup.

The current source collects 1500 Z-axis gyro samples after a settling period, averages them, and subtracts the resulting bias.

If the robot moves during calibration, repeat the test.

## 3. Camera calibration

The final measured lens-centre heights are:

- front: 25.0 cm
- rear: 23.5 cm

Verify the camera mount is rigid before changing software thresholds.

## 4. Vision tuning

The team tuned:

- colour thresholds;
- contour-area thresholds;
- Kp;
- servo centre;
- servo limits;
- marker cooldown;
- camera angle;
- operating speed.

The documented obstacle confidence formula is:

`C = 0.65 CHSV + 0.20 CLAB + 0.15 Cgeometry`

## 5. Open Challenge baseline

Expected configuration:

| Parameter | Value |
|---|---:|
| Resolution | 1480 × 520 |
| Kp | 0.013 |
| Cooldown | 1.0 s |
| Laps | 3 |
| Crossings/lap | 4 |
| Total crossings | 12 |
| Initial PWM | 40 |
| Steering | 35° / 75° / 115° |

Recorded results:

`32, 30, 28, 28, 28, 28 s`

Best: **28 s**.

## 6. Obstacle baseline

The recorded obstacle-navigation times were:

`1:10, 1:09, 1:11, 1:20, 1:15, 1:13`

Best navigation time: **1:09**.

The updated engineering document explicitly states that these times cover navigation up to the parking approach. The final parking manoeuvre was tested separately and is still under calibration.

## 7. Power checks

Record only measured values:

- 11.1 V before run
- 10.8 V after multiple runs
- 11.1 V motor driver, motors OFF
- 10.8 V motor driver, motors ON
- 5.0 V Buck 1
- 5.0 V Pi supply

Do not invent current measurements. The final record does not contain a direct bench current measurement.

## 8. What counts as a successful reproduction

A successful reproduction is not just a robot that moves. It should reproduce the documented architecture, camera placement, steering calibration, perception roles, safety behaviour and test procedure.
