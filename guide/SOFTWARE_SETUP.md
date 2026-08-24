# Software Setup — Raspberry Pi 5

This guide points only to software paths that exist in the current repository.

## 1. Install Raspberry Pi OS

Use a Raspberry Pi OS installation appropriate for Raspberry Pi 5.

Enable the required interfaces, especially:

- I2C
- camera support

## 2. Clone the repository

```bash
git clone https://github.com/darsh-makadia/Team-Current-WRO-FE-2026.git
cd Team-Current-WRO-FE-2026
```

## 3. Python software

The repository's Python source is in [`../src/`](../src/).

The documented software stack includes:

- Python
- OpenCV
- NumPy
- RPi.GPIO
- Picamera2
- smbus2

### Important repository note

There is currently no `requirements.txt` in the repository, so this guide does **not** give a fake `pip install -r requirements.txt` command.

Install the libraries required by the actual source/environment, then verify imports on the Raspberry Pi.

## 4. Main source files

| Function | Actual file |
|---|---|
| Drive and steering | [`src/drive.py`](../src/drive.py) |
| Heading / MPU6050 | [`src/heaeding.py`](../src/heaeding.py) |
| Open challenge | [`src/Current_Open_8_22.py`](../src/Current_Open_8_22.py) |
| Obstacle challenge | [`src/Current_Obstacle_8_21.py`](../src/Current_Obstacle_8_21.py) |
| Open challenge module | [`src/open_challenge.py`](../src/open_challenge.py) |
| Obstacle challenge module | [`src/obstacle_challenge.py`](../src/obstacle_challenge.py) |
| Vision | [`src/vision.py`](../src/vision.py) |
| Open vision | [`src/openVision.py`](../src/openVision.py) |
| Parking | [`src/parking.py`](../src/parking.py) |

## 5. Verified drive configuration

The actual `src/drive.py` defines:

```text
PWM_PIN = 13
IN1_PIN = 5
IN2_PIN = 6
SERVO_PIN = 22

CENTER = 75
LEFT = 35
RIGHT = 105
```

## 6. MPU6050 configuration

The actual heading source uses:

```text
I2C bus = 1
Address = 0x68
Calibration samples = 1500
```

Keep the robot stationary during calibration.

## 7. Test order

Do not begin with a full autonomous run.

Recommended order:

1. Import/compile check
2. Camera detection
3. IMU detection
4. Steering test
5. Motor test with wheels lifted
6. Slow manual movement
7. Open Challenge
8. Obstacle Challenge
9. Parking calibration

## 8. Safety

The source includes cleanup/stop behaviour and bounded handling in the documented navigation systems. Always test with the robot secured and the drive wheels lifted for the first motor test.

## Source-of-truth rule

If a guide and the actual source disagree, inspect the actual source file first.

[Back to Start Here](./START_HERE.md)
