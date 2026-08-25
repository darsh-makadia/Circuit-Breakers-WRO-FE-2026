## v1.0.0-nationals — Final WRO Future Engineers 2026 Configuration

This entry records the final configuration submitted for the WRO Future Engineers 2026 Nationals documentation.

### Final hardware

- Raspberry Pi 5, 4 GB
- Two Raspberry Pi Camera Module 3 cameras
- JGB37-520 DC motor, 12 V, 600 RPM
- Servo steering
- MPU6050 IMU
- TB6612FNG motor driver
- 3S 2200 mAh LiPo battery
- CAD/PLA printed chassis and mounting components
- LEGO Technic drivetrain components and mechanical differentials

### Final software and control configuration

- Python software running on Raspberry Pi 5
- `RPi.GPIO` for Raspberry Pi GPIO control
- OpenCV-based colour segmentation and contour processing
- HSV and LAB colour information for perception
- Direction-dependent wall following
- Rising-edge marker detection and cooldown logic
- MPU6050 gyro-bias calibration and heading integration for parking
- Steering centre: 75°
- Steering minimum: 35°
- Steering maximum: 115°
- Open Challenge values: use the exact values recorded in the final source code and engineering documentation

### Repository evidence

The final configuration is supported by:

- Python source code in `src/`
- STL files in `models/`
- Electrical schematic in `schemes/schematic.jpg`
- Build and setup guides in `guide/`
- Test data and results in `testing/`
- Robot and team photographs in `v-photos/` and `t-photos/`
- Video evidence in `video/`

### Validation record

The final documentation and repository were checked for consistency across the hardware description, source code, wiring information, CAD files, testing records, and README. Open Challenge and Obstacle Challenge results are reported together with their test conditions and limitations.

The Open Challenge results were recorded as:

- 32 seconds
- 30 seconds
- 28 seconds
- 28 seconds
- 28 seconds
- 28 seconds

Best recorded Open Challenge time: **28 seconds**.

The Obstacle Challenge navigation results were recorded as:

- 2 minutes 10 seconds
- 2 minutes 9 seconds
- 2 minutes 11 seconds
- 2 minutes 20 seconds
- 2 minutes 15 seconds
- 2 minutes 13 seconds

These runs represent obstacle navigation up to the parking approach. The final parallel-parking manoeuvre remains under development and should not be described as completely reliable unless separate evidence confirms consistent completion without contact.

### Measurement policy

Measured values are identified as measured. Current draw was not directly measured with a current-logging instrument, so the repository does not present an estimated current value as a measured result. Voltage measurements and their test conditions are recorded in `testing/power_measurements.csv`.

### Final source of truth

The final engineering documentation is the source of truth for the submitted configuration. The README, source code, guides, testing records, CAD/STL files, schematic, and this changelog should remain consistent with that final documentation.
