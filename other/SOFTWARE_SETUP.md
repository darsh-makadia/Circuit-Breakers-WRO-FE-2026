# Software setup — Raspberry Pi 5

## 1. Install the operating system

Use a Raspberry Pi OS installation appropriate for the Raspberry Pi 5. Connect the Pi to a display/keyboard for the first setup if needed.

Enable the interfaces required by the hardware, especially:

- I2C
- camera support

## 2. Get the repository

Clone the repository and enter it:

```bash
git clone https://github.com/darsh-makadia/Team-Current-WRO-FE-2026.git
cd Team-Current-WRO-FE-2026
```

## 3. Install Python dependencies

```bash
python3 -m pip install -r requirements.txt
```

The documented software stack includes:

- Python
- OpenCV
- NumPy
- RPi.GPIO
- Picamera2
- smbus2

## 4. Check the source configuration

Open:

```text
code/config.py
```

The important documented values are:

```text
Servo: 35° to 115°, centre 75°
Open Kp: 0.013
Open cooldown: 1.0 s
Open laps: 3
Open crossings/lap: 4
Open total crossings: 12
Open initial PWM: 40
Front camera: 1480 × 520
Rear camera: 640 × 480
IMU calibration: 1500 samples
```

## 5. Test before moving

Do not start with a full autonomous run.

Recommended order:

1. import/compile check;
2. camera detection;
3. IMU detection;
4. steering test;
5. motor test with wheels lifted;
6. slow manual movement;
7. Open Challenge;
8. Obstacle Challenge;
9. parking calibration.

## 6. Safety behaviour already implemented

The source contains safe-stop handling for IMU/I2C failures, bounded IMU turns, a parking wall-follow timeout, temporal obstacle confirmation and cleanup that stops the robot rather than starting another manoeuvre.

## 7. Exact source of truth

If a README value and a source-code value disagree, inspect `code/config.py` and the actual challenge source before changing anything. The engineering document also says the repository source should be treated as the authoritative implementation.
