# Wiring and pin reference

This file is a quick reference. The **final schematic is the authority** for physical wiring.

## Power architecture

```text
3S LiPo 11.1 V nominal
        │
        ├──────────────► TB6612FNG VMOT ─────► JGB37-520 drive motor
        │
        ├──────────────► Buck 1 ── 5 V ─────► Servo VCC
        │                              └────► TB6612 logic VCC / nSTBY
        │
        └──────────────► Buck 2 ── 5 V / 5 A ─► Raspberry Pi 5
                                                    │
                                                    ├── Camera 0
                                                    ├── Camera 1
                                                    ├── 3.3 V ─► MPU6050
                                                    └── 3.3 V ─► OLED / low-power logic
```

All branches share a common ground.

## Software GPIO values

These values come directly from `code/config.py` in this release and use BCM numbering.

| Function | BCM GPIO | Software file |
|---|---:|---|
| Motor PWM | 13 | `code/config.py` |
| Motor direction 1 | 5 | `code/config.py` |
| Motor direction 2 | 6 | `code/config.py` |
| Steering servo | 22 | `code/config.py` |
| I2C bus | 1 | `code/heading.py` |
| MPU6050 address | `0x68` | `code/config.py` |

## Camera indexes

| Camera | Picamera2 index | Use |
|---|---:|---|
| Front | 0 | Open + Obstacle perception |
| Rear | 1 | Parking |

## Important electrical notes

- The drive motor is on the raw battery motor branch through the driver.
- The Raspberry Pi is on the separate regulated Buck 2 branch.
- Buck 1 provides the documented 5 V servo/motor-driver logic rail.
- Do not feed raw LiPo voltage into a 5 V input.
- The engineering document states the motor-driver channels are wired in parallel for the single drive motor.
- Current logging was not performed as a direct bench measurement in the final testing record.

## Measured voltages

| Measurement point | Condition | Value |
|---|---|---:|
| LiPo | Before run | 11.1 V |
| LiPo | After multiple runs | 10.8 V |
| Motor driver | Motors OFF | 11.1 V |
| Motor driver | Motors ON | 10.8 V |
| Buck 1 | Tested output | 5.0 V |
| Pi supply | Tested output | 5.0 V |

These are multimeter observations, not a full transient/current characterization.
