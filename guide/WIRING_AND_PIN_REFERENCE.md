# Wiring & Pin Reference

This is a quick reference for the robot's power architecture, physical wiring, and software GPIO assignments. The [final schematic](../schemes/schematic.png) is the authority for physical wiring.

## Power Architecture

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

## Software GPIO Values

These values are taken from the actual source files in [`../src/`](../src/).

| Function | BCM GPIO | Actual source |
|---|---:|---|
| Motor PWM | 13 | [`src/drive.py`](../src/drive.py) |
| Motor direction 1 | 5 | [`src/drive.py`](../src/drive.py) |
| Motor direction 2 | 6 | [`src/drive.py`](../src/drive.py) |
| Steering servo | 22 | [`src/drive.py`](../src/drive.py) |
| MPU6050 I2C bus | 1 | [`src/heading.py`](../src/heading.py) |
| MPU6050 address | `0x68` | [`src/heading.py`](../src/heading.py) |

## Steering Values in the Actual Drive Code

The current `src/drive.py` defines:

- Centre: 75°
- Left: 35°
- Right: 105°

Do not silently replace these values with values from an older guide.

## Cameras

The documented software configuration uses:

| Camera | Index | Use |
|---|---:|---|
| Front | 0 | Open + Obstacle Challenge perception |
| Rear | 1 | Parking |

## Important Electrical Notes

- The drive motor uses the raw battery motor branch through the driver.
- Raspberry Pi uses the regulated Buck 2 branch.
- Buck 1 provides the documented 5 V servo and motor-driver logic rail.
- Do not feed raw LiPo voltage into a 5 V input.
- Common ground is used across the system.
- The documented motor-driver channels are wired in parallel for the single drive motor.
- Current was not directly bench-measured in the final testing record.

## Measured Voltages

| Measurement point | Condition | Value |
|---|---|---:|
| LiPo | Before run | 11.1 V |
| LiPo | After multiple runs | 10.8 V |
| Motor driver | Motors OFF | 11.1 V |
| Motor driver | Motors ON | 10.8 V |
| Buck 1 | Tested output | 5.0 V |
| Pi supply | Tested output | 5.0 V |

## Related Resources

- [Open the final schematic](../schemes/schematic.png)
- [Back to Start Here](./START_HERE.md)
