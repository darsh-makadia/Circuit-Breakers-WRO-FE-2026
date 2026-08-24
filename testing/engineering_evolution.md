# Engineering Evolution

This section records the main engineering loop without inventing measurements.

| Area | Problem observed | What changed | Testing / evidence | Result |
|---|---|---|---|---|
| Motor | Earlier motor created stalling/current and stability concerns | Replaced Johnson 1000 RPM motor with JGB37-520 12 V 600 RPM | Motor and drive testing | Lower-risk final motor selected |
| Chassis | LEGO-heavy structure limited rigidity and custom mounting | Introduced CAD/PLA structural parts while retaining LEGO drivetrain precision | Mechanical iterations and final dimensional measurement | 24 × 13 × 27.5 cm, 863 g final chassis |
| Camera | Early mount was unstable and placement affected perception | Redesigned mount in CAD and adopted two-camera architecture | Camera placement experiments and obstacle/track tests | More stable forward perception plus rear parking view |
| Power | Pi should not supply the motor system | Separated raw motor power and regulated logic/Pi branches | Multimeter voltage measurements | Stable measured voltages at documented points |
| Navigation | Duplicate marker detections could count one crossing repeatedly | Rising-edge detection + 1.0 s cooldown; direction selected from marker colour | Repeated Open Challenge runs | Final documented 3-lap / 12-crossing logic |
| Obstacle avoidance | Colour/position errors could cause late or incorrect steering | HSV + LAB + geometry confidence, contour filtering, temporal confirmation and direction-dependent steering | Obstacle Challenge navigation runs | Autonomous navigation demonstrated up to parking approach |
| Parking | Timed turns did not provide reliable orientation | Rear-camera detection + explicit parking states + MPU6050 heading feedback | Separate physical parking tests | Implemented and tested, but final position/alignment still needs calibration for reliable completion |
