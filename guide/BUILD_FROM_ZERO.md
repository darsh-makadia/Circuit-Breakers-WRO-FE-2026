# Build The Dark Knight From Zero

This is the repository-linked build guide for the documented Team Current configuration.

## 1. What you are building

The documented robot combines:

- 4-wheel drive
- JGB37-520 12 V 600 RPM drive motor
- central driveshaft
- two mechanical LEGO differentials
- servo steering
- Raspberry Pi 5, 4 GB
- two Raspberry Pi Camera Module 3 cameras
- MPU6050
- TB6612FNG motor driver
- 3S LiPo, 2200 mAh, 11.1 V nominal
- regulated power branches
- PLA printed structure
- LEGO Technic drivetrain components

## 2. Read the repository files in this order

1. [Start Here](./START_HERE.md)
2. [Parts Checklist](./PARTS_CHECKLIST.md)
3. [Final schematic](../schemes/schematic.png)
4. [CAD/STL models](../models/)
5. [Robot photos](../v-photos/)
6. [Software Setup](./SOFTWARE_SETUP.md)
7. [Source code](../src/)

There is no engineering-document PDF currently stored in the repository, so this guide does not link to one.

## 3. Print the actual CAD files

Use the STL files in [`../models/`](../models/):

1. `currents final chassis (1).stl`
2. `currents final chassis pt2 (1) (1).stl`
3. `currnts dual camera mount (1).stl`
4. `camera case (1) (1).stl`
5. `currents CB (1).stl`
6. `currents CB LID (1).stl`

Use the PNG previews in the same folder to identify the parts before printing.

## 4. Build the drivetrain

The documented layout is:

```text
                 CENTRAL DRIVESHAFT
                        │
             ┌──────────┴──────────┐
             │                     │
       FRONT DIFFERENTIAL     REAR DIFFERENTIAL
             │                     │
        left + right           left + right
           wheel                  wheel
```

There are two mechanical differentials, one per axle.

Install the JGB37-520 motor using the final chassis/drivetrain arrangement shown in the repository photos and models.

The documented external gear pair is:

- custom 36-tooth printed gear
- LEGO 20-tooth gear
- 1:1.8 tooth-count relationship

## 5. Steering

Mount the servo using the final mechanical arrangement.

The actual drive source currently defines:

- centre: 75°
- left: 35°
- right: 105°

Do not increase the range simply because the servo can physically move farther.

## 6. Cameras

The documented configuration uses two Camera Module 3 cameras.

| Camera | Index | Main purpose |
|---|---:|---|
| Front | 0 | Track + obstacle perception |
| Rear | 1 | Parking |

Use the final dual-camera mount stored in [`../models/`](../models/).

## 7. Electronics and power

Use the [final schematic](../schemes/schematic.png) as the physical wiring authority.

Documented architecture:

- raw battery → motor-driver VMOT
- raw battery → Buck 1
- raw battery → Buck 2
- Buck 1 → servo + motor-driver logic
- Buck 2 → Raspberry Pi 5
- Raspberry Pi 3.3 V → MPU6050 and low-power I2C-side logic
- common ground

**Never feed raw battery voltage into a 5 V input.**

## 8. Raspberry Pi software

Follow [Software Setup](./SOFTWARE_SETUP.md).

The source is in [`../src/`](../src/).

Important files:

- [`drive.py`](../src/drive.py)
- [`heaeding.py`](../src/heaeding.py)
- [`Current_Open_8_22.py`](../src/Current_Open_8_22.py)
- [`Current_Obstacle_8_21.py`](../src/Current_Obstacle_8_21.py)
- [`vision.py`](../src/vision.py)
- [`parking.py`](../src/parking.py)

## 9. First power-up checklist

- [ ] Wheels rotate freely.
- [ ] Steering linkage moves without binding.
- [ ] Motor cannot contact the chassis.
- [ ] Both cameras are firmly mounted.
- [ ] IMU is firmly mounted.
- [ ] Battery is secured.
- [ ] Wiring is insulated and protected.
- [ ] Common ground is connected.
- [ ] Motor driver VMOT uses the motor branch.
- [ ] Raspberry Pi uses the regulated 5 V branch.
- [ ] No raw battery voltage reaches a 5 V input.

For the first motor test, keep the drive wheels lifted from the floor.

## 10. IMU calibration

The actual MPU6050 source:

- uses I2C bus 1
- uses address `0x68`
- collects 1500 samples
- estimates gyro Z-axis bias
- integrates corrected angular velocity into heading

Keep the robot completely still during calibration.

## 11. Challenge software

Open Challenge source:

[`src/Current_Open_8_22.py`](../src/Current_Open_8_22.py)

Obstacle Challenge source:

[`src/Current_Obstacle_8_21.py`](../src/Current_Obstacle_8_21.py)

Supporting modules are in [`src/`](../src/).

## 12. Testing order

1. Mechanical test
2. Electrical test
3. Steering test
4. Camera test
5. Open Challenge
6. Obstacle Challenge
7. Parking calibration

Record failures honestly instead of treating an unverified result as final performance.

## 13. Reproduction priority

When two repository references disagree, use:

1. Current physical robot
2. Current source code
3. Final schematic
4. Current CAD/STL files
5. Existing documentation

The guide is a navigation aid; it is not a replacement for the actual robot, source or schematic.

[Back to Start Here](./START_HERE.md)
