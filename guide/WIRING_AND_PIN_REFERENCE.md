# Power and Sensor Architecture Evidence

This document provides a quick reference for the robot's implemented power
distribution, sensor interfaces, software GPIO assignments, and measured
voltage evidence.

The [final schematic](../schemes/schematic.png) is the authority for physical
wiring. Values in this document are aligned with the final engineering
documentation and current implementation where available.

## Power architecture

```text
3S LiPo 11.1 V nominal
        │
        ├──────────────► TB6612FNG VMOT ─────► JGB37-520 drive motor
        │
        ├──────────────► Buck 1 ── 5 V ─────► Servo VCC
        │                              └────► TB6612FNG VCC / nSTBY
        │
        └──────────────► Buck 2 ── 5 V / 5 A ─► Raspberry Pi 5
                                                    │
                                                    ├── Camera 0
                                                    ├── Camera 1
                                                    ├── 3.3 V ─► MPU6050
                                                    └── 3.3 V ─► OLED / push-button logic
```

The raw battery rail supplies the motor-driver `VMOT` input and the inputs of
both buck converters. Buck 1 provides the regulated 5 V rail used for the
servo and motor-driver logic. Buck 2 forms a separate regulated 5 V branch for
the Raspberry Pi 5 and its connected peripherals. The Raspberry Pi provides
the regulated 3.3 V rail used by the OLED, MPU6050 and push-button logic.

All branches share a common ground.

## Software GPIO values

The following values are intended as a quick reference to the software and
schematic configuration.

| Function | BCM GPIO | Connection |
|---|---:|---|
| Motor PWM | 13 | PWMA + PWMB |
| Motor direction 1 | 5 | AIN2 + BIN2 |
| Motor direction 2 | 6 | AIN1 + BIN1 |
| Steering servo | 22 | Servo signal |
| Push-button | 18 | Start/stop input |
| MPU6050 I2C bus | 1 | I2C bus |
| MPU6050 address | `0x68` | I2C address |

The two TB6612FNG motor-driver channels are wired in parallel for the single
JGB37-520 drive motor. The duplicated motor-driver connections are
intentional: both channels are used together to share motor current rather than
to control two separate motors.

## Steering values

The current steering calibration used in the documented drive configuration is:

- Centre: 75°
- Left: 35°
- Right: 105°

These values should be checked against the current source code before changing
the steering linkage or replacing the servo.

## Sensor architecture

The robot uses the following sensing and perception hardware:

| Device | Interface | Raspberry Pi connection | Purpose |
|---|---|---|---|
| Front Raspberry Pi Camera Module 3 | CSI | Camera 0 | Open and Obstacle Challenge perception |
| Rear Raspberry Pi Camera Module 3 | CSI | Camera 1 | Parking-related visual feedback |
| MPU6050 | I2C | Bus 1, address `0x68` | Heading and rotational feedback |
| OLED display | I2C | Shared I2C bus | Robot status and debugging output |
| Push-button | GPIO | BCM GPIO18 | Start/stop control |

The two cameras provide forward and rearward visual information, while the
MPU6050 provides orientation feedback. The MPU6050 and OLED share the I2C bus.

## Cameras

The documented camera configuration is:

| Camera | Index | Use |
|---|---:|---|
| Front | 0 | Open and Obstacle Challenge perception |
| Rear | 1 | Parking-related visual feedback |

The forward-looking camera is primarily used for line and obstacle perception.
The second camera provides rearward information for parking-related
development.

## Important electrical notes

- The drive motor receives raw battery power through the TB6612FNG motor branch.
- Buck 1 provides the documented 5 V servo and motor-driver logic rail.
- Buck 2 provides a separate regulated 5 V branch rated at 5 A for the Raspberry Pi 5 and connected peripherals.
- The Raspberry Pi provides the documented 3.3 V rail for the OLED, MPU6050 and push-button logic.
- All electrical branches share a common ground.
- The two TB6612FNG motor channels are wired in parallel for the single drive motor.
- No direct bench measurement of motor current was included in the final testing record.
- Voltage measurements establish the stated values at the measured points, but do not characterise fast transient voltage drops or current spikes.

## Measured voltages

| Measurement point | Condition | Value |
|---|---|---:|
| LiPo battery | Before run | 11.1 V |
| LiPo battery | After multiple runs | 10.8 V |
| Buck 1 output | Motors OFF | 5.0 V |
| Buck 1 output | Robot moving | 5.0 V |
| Pi supply | Idle | 5.0 V |
| Pi supply | Moving | 5.0 V |
| Motor driver | Motors OFF | 11.1 V |
| Motor driver | Motors ON | 10.8 V |

Operation is stopped if the loaded battery voltage falls below approximately
10.5 V. During development, a battery was normally replaced with a fresh pack
once performance began to degrade rather than discharging a single pack toward
its cutoff.

## Low-voltage observation

Earlier in development, the Raspberry Pi produced a low-voltage warning. At
the latest documented state, this warning was no longer occurring. This issue
contributed to the decision to separate the high-power motor branch from the
Raspberry Pi power path.

## Power measurement limitations

The recorded voltage measurements were taken using the available test setup
while the robot operated from its battery. The measurements showed that the
supply voltages remained approximately stable at the measured points under the
tested conditions.

This does not prove that no transient voltage drops or current spikes occur.
A multimeter measurement alone is not sufficient to characterise every fast
electrical transient.

## Power budget note

The engineering documentation includes an estimated power budget because a
full bench current-logging setup was not available during development.

The +5 V servo/logic rail uses Buck 1, rated at 5 V / 3 A. Published DS3225
stall-current figures vary significantly across sources, approximately from
1.9 A to 3.5 A. The actual stall current of the installed servo therefore
remains an item for direct bench measurement.

The separate Raspberry Pi rail uses Buck 2, rated at 5 V / 5 A. The documented
estimated worst-case combined load for the Raspberry Pi 5 and two active camera
modules is approximately 2.8 A, leaving approximately 2.2 A of nominal
headroom against the 5 A rating.

## References

- [Open final schematic](../schemes/schematic.png)
- [Back to Start Here](./START_HERE.md)
