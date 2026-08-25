# Software Setup

Instructions for setting up a fresh Raspberry Pi 5 to run The Dark Knight's software.

## 1. Operating System

Run this on the Pi to confirm the exact OS version, then fill it in below:

```bash
cat /etc/os-release
```

**OS:** Debian GNU/Linux 13 (trixie), confirmed via `cat /etc/os-release` on the actual robot's Raspberry Pi 5.

*(Note: this reports as Debian 13/trixie, not "Raspberry Pi OS" by name in `PRETTY_NAME` — if reproducing this setup, flash whichever image was actually used rather than assuming a specific Raspberry Pi OS release, since Raspberry Pi OS naming/versioning can differ from the underlying Debian base shown here.)*

## 2. Enable I2C

I2C is disabled by default on a fresh Raspberry Pi OS install and is required for the MPU6050 IMU and the OLED display.

```bash
sudo raspi-config
```

Navigate to: **Interface Options → I2C → Enable**, then reboot:

```bash
sudo reboot
```

Confirm I2C devices are detected:

```bash
sudo apt install -y i2c-tools
i2cdetect -y 1
```

You should see the MPU6050 (typically address `0x68`) and the OLED (typically `0x3C`) listed.

## 3. Enable the Camera Interface

Both Raspberry Pi Camera Module 3 units connect via the CSI ribbon interface and require Picamera2.

```bash
sudo raspi-config
```

Navigate to: **Interface Options → Camera → Enable**, then reboot.

## 4. Install Python Dependencies

```bash
sudo apt update
sudo apt install -y python3-pip python3-opencv python3-picamera2

pip3 install --break-system-packages \
    numpy \
    smbus2 \
    RPi.GPIO
```

| Library | Purpose |
|---|---|
| `opencv-python` (via `python3-opencv`) | Colour segmentation, contour detection, all computer vision |
| `numpy` | Array/matrix operations used throughout the vision pipeline |
| `picamera2` | Camera capture (front + back cameras) |
| `smbus2` | I2C communication with the MPU6050 IMU |
| `RPi.GPIO` | Direct GPIO control — motor and steering pin control in `drive.py`, push-button input |

## 5. Clone the Repository

```bash
git clone https://github.com/darsh-makadia/Team-Current-WRO-FE-2026.git
cd Team-Current-WRO-FE-2026/src
```

## 6. Run

```bash
python3 Current_Open_8_22.py       # Open Challenge
python3 Current_Obstacle_8_21.py   # Obstacle Challenge
```

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| `ModuleNotFoundError: No module named 'picamera2'` | Camera interface not enabled, or Picamera2 not installed — repeat steps 3–4 |
| No I2C devices found in `i2cdetect` | I2C not enabled, or a wiring issue on the MPU6050/OLED — repeat step 2 and check physical connections |
| Camera fails to start / "Camera not found" | Ribbon cable seated incorrectly, or camera not enabled in `raspi-config` |
| Servo/motor doesn't respond | Check GPIO pin numbers in `drive.py` match physical wiring; confirm `RPi.GPIO` installed correctly |
