# Build From Zero

This guide describes how to assemble **The Dark Knight** from its individual mechanical, 3D-printed, electronic, and software components.

The build follows the same general order used during the robot's development:

1. Drivetrain and differentials
2. External motor gear stage
3. Chassis integration
4. Steering system
5. Camera installation
6. Electronics and wiring
7. Software setup and calibration

---

## Before You Start

### Parts and components

The complete parts list and purchase references are available in:

[`PARTS_AND_PURCHASE_LINKS.md`](PARTS_AND_PURCHASE_LINKS.md)

### 3D-printed components

Print the required components before beginning assembly. Printing information and recommended settings are available in:

[`3D_PRINTING_SETTINGS.md`](3D_PRINTING_SETTINGS.md)

The primary printed components are:

- Main chassis
- Upper chassis base
- Camera mount
- Camera case
- Circuit box
- Circuit-box lid
- Custom 36-tooth gear

The chassis and upper chassis base should be inspected after printing to ensure that the drivetrain, motor, servo and other components fit correctly before final assembly.

---

# Stage 1 — Drivetrain and Differentials

The drivetrain uses a central mechanical transmission connected to **two LEGO differentials**, allowing all four wheels to be driven.

The drivetrain is assembled from one end of the robot to the other. For the following instructions, begin at the **rear side** and progress toward the **front side**.

## Step 1 — Assemble the first differential

1. Place the **28-tooth LEGO differential** in position.
2. Connect the differential mechanism using **three 12-tooth bevel gears**.
3. Connect the differential outputs to the wheel axles.
4. Attach the wheels to the axle outputs.
5. Place a **1/2 bush** at the end of each wheel-side axle to retain the assembly.

This forms the first driven axle. The differential allows the left and right wheels on the same axle to rotate at different speeds while both remain connected to the drivetrain.

---

## Step 2 — Connect the first differential to the central drivetrain

1. Connect the differential output to a **20-tooth gear**.
2. Position the corresponding small chassis support around the drivetrain assembly.
3. Insert a **6L axle** through the drivetrain.
4. Retain this axle using **two half bushes**.
5. Connect the axle to a **2L axle connector**.
6. Connect the axle connector to another **6L axle**.
7. Add a **full bush** followed by a **20-tooth gear**.

Ensure that the axle rotates freely through the chassis support.

---

## Step 3 — Continue the central drivetrain

1. After the second 20-tooth gear, add another **full bush**.
2. Position the next small chassis support.
3. Add the next **20-tooth gear** to the drivetrain.

At this point, the central axle and gear train should provide a mechanical connection between the two ends of the drivetrain.

---

## Step 4 — Assemble the second differential and wheel connection

1. Connect the final **20-tooth gear** to the second **28-tooth LEGO differential**.
2. Assemble this differential using **three 12-tooth bevel gears**.
3. Connect the differential output toward the wheel assembly.
4. Attach a **universal joint**.
5. Connect the universal joint using a **4L axle**.
6. Transfer the drive to the wheel using an **axle with stop**.
7. Attach and secure the wheel.

The complete drivetrain should now mechanically connect the motor input to both axle differentials.

---

## Step 5 — Test the drivetrain

Before installing the motor permanently, manually rotate the central drivetrain.

Check that:

- Both axle assemblies receive rotational motion.
- All four wheels are mechanically driven.
- Both differentials can compensate for differences in left and right wheel rotation.
- The central axle rotates without significant binding.
- The gears remain properly meshed.
- The drivetrain does not interfere excessively with the chassis.

If the drivetrain does not rotate smoothly, inspect the alignment of the axles, bushes, gears and chassis supports before continuing.

---

# Stage 2 — External Motor Gear Stage

The drive motor transfers power to the central drivetrain through an external gear stage.

The motor is mounted so that its output shaft passes through a dedicated opening in the chassis.

## Step 1 — Install the motor

1. Position the drive motor in its dedicated location.
2. Pass the motor mounting beam through the corresponding hole in the chassis.
3. Secure the motor so that it remains stable during operation.

The fit should not be excessively tight or excessively loose. A very tight fit can introduce mechanical resistance, while a loose fit can allow the motor and gear assembly to move during operation.

---

## Step 2 — Install the custom motor gear

1. Attach the custom **36-tooth 3D-printed gear** to the motor output shaft.
2. Align the motor so that the 36-tooth gear meshes with the **20-tooth LEGO gear** connected to the drivetrain.
3. Ensure that the gears are aligned with each other and engage across their full usable width.

The resulting external gear stage transfers motor rotation into the central drivetrain.

---

## Step 3 — Check the gear mesh

1. Rotate the gear assembly manually.
2. Check that the 36-tooth and 20-tooth gears move smoothly.
3. Confirm that the gears do not bind against the chassis.
4. Confirm that the motor mounting position does not allow excessive gear separation.
5. Adjust the motor position if necessary.

The exact fit should be determined through physical testing. The gears should rotate smoothly without excessive resistance while remaining sufficiently engaged to prevent skipping under load.

---

# Stage 3 — Chassis Integration

The printed chassis forms the structural base of the robot and contains dedicated spaces and openings for the drivetrain and major mechanical components.

## Step 1 — Prepare the chassis

1. Inspect the printed main chassis.
2. Remove any printing residue or material that interferes with component placement.
3. Check that the drivetrain openings and mounting locations are clear.
4. Test-fit the drivetrain before permanently securing additional components.

---

## Step 2 — Position the drivetrain

1. Carefully lower the completed drivetrain into the main chassis.
2. Align the differential assemblies with their corresponding wheel positions.
3. Ensure that the central axle remains aligned with the motor gear stage.
4. Confirm that the wheels rotate without rubbing excessively against the chassis.

The drivetrain should sit naturally within the chassis without forcing the differential or axle assemblies out of alignment.

---

## Step 3 — Check chassis clearance

Before adding the upper chassis:

- Rotate all four wheels.
- Rotate the central drivetrain manually.
- Check that the differential assemblies are not obstructed.
- Check that the motor gear stage remains aligned.
- Confirm that no chassis component creates significant mechanical resistance.

If the drivetrain rotates smoothly inside the chassis, proceed to the upper chassis assembly.

---

## Step 4 — Install the upper chassis base

1. Position the upper chassis base above the main chassis.
2. Align the printed mounting points and component openings.
3. Ensure that the upper structure does not interfere with the drivetrain or steering system.
4. Secure the upper chassis base using its dedicated mounting locations.

The upper chassis provides the structural platform for the steering, cameras and electronic components.

---

# Stage 4 — Steering System

The robot uses a DS3225 servo motor for steering.

The upper chassis contains dedicated mounting holes that allow the steering system to be attached directly using screws.

## Step 1 — Position the steering servo

1. Place the DS3225 servo in its dedicated steering position.
2. Align the servo with the mounting holes in the upper chassis.
3. Secure the servo directly to the chassis using screws.

Ensure that the servo is firmly attached and cannot shift significantly during steering.

---

## Step 2 — Connect the steering mechanism

1. Attach the servo horn to the servo output.
2. Connect the servo horn to the steering linkage.
3. Ensure that the linkage can move through its full mechanical range.

Before final calibration, manually check that the steering mechanism does not bind at either extreme.

---

## Step 3 — Calibrate the steering range

After the mechanical steering system has been assembled, power the servo and test the software steering positions.

The current calibrated values are:

```python
CENTER = 75
LEFT = 35
RIGHT = 115
```

Check that:

- The centre value produces approximately straight wheel alignment.
- The left value produces the intended left steering position.
- The right value produces the intended right steering position.
- The steering mechanism does not force the servo beyond its mechanical limits.

If necessary, adjust the servo horn position, steering linkage or software calibration values.

---

# Stage 5 — Camera Mounts and Cameras

The robot uses two Raspberry Pi Camera Module 3 cameras for forward and rear-facing vision.

The camera mounts and cases are designed to fit the camera modules directly, without requiring additional mounting hardware.

## Step 1 — Install the camera mount

1. Attach the printed camera mount to its designated location on the robot.
2. Ensure that the mount is firmly connected and does not move during normal robot operation.

The camera mounting arrangement positions the two cameras in opposite viewing directions.

---

## Step 2 — Install the front-facing camera

1. Place the front-facing Raspberry Pi Camera Module 3 into its printed camera case.
2. Ensure that the camera fits fully into the dedicated geometry.
3. Attach the camera case to the camera mount.
4. Confirm that the camera lens has an unobstructed field of view.

The front-facing camera is used for challenge navigation and vision processing.

---

## Step 3 — Install the rear-facing camera

1. Place the second Raspberry Pi Camera Module 3 into its corresponding camera case or mounting position.
2. Install it so that it faces toward the rear of the robot.
3. Confirm that the rear-facing camera has an unobstructed field of view.

This camera is intended for parking-related visual feedback.

---

## Step 4 — Connect the camera cables

1. Connect each camera ribbon cable to the appropriate Raspberry Pi camera connector.
2. Route the cables so that they remain clear of:
   - Rotating drivetrain components
   - Wheels
   - Steering components
   - Moving mechanical assemblies
3. Avoid excessively sharp bends in the camera ribbon cables.

Before closing the electronics compartment, test that both cameras can be detected by the Raspberry Pi.

---

# Stage 6 — Electronics and Wiring

The electrical system is based on the robot's battery supply, two buck converters, the Raspberry Pi 5, motor driver, servo, sensors and other peripherals.

The complete electrical schematic is available in:

[`../schemes/`](../schemes/)

The software and interface setup are described in:

[`SOFTWARE_SETUP.md`](SOFTWARE_SETUP.md)

---

## Step 1 — Install the main electronics

Mount the following components in their designated positions:

- Raspberry Pi 5
- Motor driver
- Buck converter 1
- Buck converter 2
- MPU6050 IMU
- OLED display
- Push-button
- Circuit box and lid

Ensure that the electronics are protected from moving mechanical components.

---

## Step 2 — Connect the main power system

Connect the raw battery supply to:

- Buck converter 1 input
- Buck converter 2 input
- Motor driver `VMOT`

The motor driver `VMOT` receives the full approximately 12 V battery supply.

---

## Step 3 — Connect the 5 V logic and servo supply

Connect the appropriate 5 V buck converter output to:

- Servo power supply
- Motor driver `VCC`
- Motor driver `nSTBY`

This separates the motor driver's logic supply from the main motor power input.

---

## Step 4 — Connect the Raspberry Pi power supply

Connect the dedicated 5 V / 5 A buck converter output to the Raspberry Pi 5.

Before connecting the Raspberry Pi, verify the converter output voltage.

---

## Step 5 — Connect the motor driver GPIO signals

Connect the motor driver control signals as follows:

| Motor Driver Signal | Raspberry Pi GPIO |
| --- | --- |
| PWM A | GPIO 13 |
| PWM B | GPIO 13 |
| AIN1 | GPIO 6 |
| BIN1 | GPIO 6 |
| AIN2 | GPIO 5 |
| BIN2 | GPIO 5 |

This wiring allows the two motor control channels to share the same corresponding PWM and direction signals.

---

## Step 6 — Connect the 3.3 V peripherals

The Raspberry Pi 3.3 V rail supplies the low-power peripherals:

- OLED display
- LEDs
- MPU6050 IMU
- Push-button circuitry

The MPU6050 and OLED communicate with the Raspberry Pi using I2C.

---

## Step 7 — Connect the push-button

Connect the push-button to:

```text
GPIO18
```

The button is configured using an internal pull-up resistor in software.

The button launcher uses the following behaviour:

- First press: start the robot program
- Second press: stop the robot program

The launcher software can start and stop the selected challenge program as a separate process.

---

## Step 8 — Perform electrical checks

Before powering the complete robot:

1. Verify the battery polarity.
2. Verify the output voltage of both buck converters.
3. Confirm that the Raspberry Pi receives the correct 5 V supply.
4. Confirm that `VMOT` receives the battery voltage.
5. Confirm that the motor driver logic supply receives 5 V.
6. Check that there are no loose or exposed connections that can short against the chassis.
7. Confirm that all required GPIO connections match the software configuration.

Only then power the complete system.

---

# Stage 7 — Software Setup and Calibration

The software setup procedure is described in:

[`SOFTWARE_SETUP.md`](SOFTWARE_SETUP.md)

The source code is located in:

[`../src/`](../src/)

---

## Step 1 — Prepare the Raspberry Pi

Install the required Raspberry Pi operating system and software dependencies.

Enable the required interfaces, including:

- I2C
- Camera interfaces

Install the Python libraries required by the challenge programs.

---

## Step 2 — Verify both cameras

Before running a challenge program:

1. Confirm that both Raspberry Pi Camera Module 3 cameras are detected.
2. Test the front-facing camera.
3. Test the rear-facing camera.
4. Confirm that each camera provides the intended orientation and field of view.

---

## Step 3 — Test the IMU

Run the heading or IMU test program.

Confirm that:

- The MPU6050 is detected.
- The calibration procedure completes.
- The reported heading remains reasonably stable while the robot is stationary.
- Heading changes correspond to physical rotation of the robot.

---

## Step 4 — Calibrate steering

Run the steering or drive test program.

Verify the current calibrated positions:

```python
CENTER = 75
LEFT = 35
RIGHT = 115
```

Adjust these values if the physical steering positions no longer correspond to the intended directions.

---

## Step 5 — Test the drivetrain

Test the drive motor and drivetrain at low speed.

Check that:

- The motor rotates correctly.
- All four wheels receive power.
- Both axle differentials operate correctly.
- The drivetrain does not bind.
- The gear stage remains engaged under load.

Stop the test immediately if abnormal gear noise, slipping or excessive resistance occurs.

---

## Step 6 — Run the Open Challenge program

Run the Open Challenge program:

```text
Current_Open_8_22.py
```

Verify:

- Camera operation
- Wall following
- Blue and orange line detection
- Direction detection
- Steering response
- Motor control

Further calibration may be required depending on the physical test environment.

---

## Step 7 — Run the Obstacle Challenge program

Run the Obstacle Challenge program:

```text
Current_Obstacle_8_21.py
```

Verify:

- Obstacle colour detection
- Target selection
- Steering response
- Obstacle avoidance
- IMU heading behaviour
- Challenge-state transitions

The rear-facing camera and parking-related code can also be tested separately as part of the parking development sequence.

---

# Final Assembly Checklist

Before operating the completed robot, verify the following.

## Mechanical

- [ ] Both differentials are installed correctly.
- [ ] All four wheels rotate freely.
- [ ] The central drivetrain rotates smoothly.
- [ ] The motor gear meshes correctly with the drivetrain gear.
- [ ] No major drivetrain component binds against the chassis.
- [ ] The steering servo is firmly mounted.
- [ ] The steering linkage moves without binding.

## Cameras

- [ ] Both cameras are securely installed.
- [ ] Both camera lenses have unobstructed views.
- [ ] Camera ribbon cables are clear of moving components.
- [ ] Both cameras are detected by the Raspberry Pi.

## Electronics

- [ ] Battery polarity is correct.
- [ ] Buck converter outputs have been verified.
- [ ] Raspberry Pi receives the correct supply voltage.
- [ ] Motor driver `VMOT` receives battery voltage.
- [ ] Motor driver `VCC` and `nSTBY` receive 5 V.
- [ ] Motor driver GPIO connections match the software.
- [ ] GPIO18 push-button is connected correctly.
- [ ] I2C peripherals are detected.

## Software

- [ ] IMU calibration completes successfully.
- [ ] Steering centre, left and right values are calibrated.
- [ ] Drive motor direction is correct.
- [ ] Open Challenge program runs successfully.
- [ ] Obstacle Challenge program runs successfully.
- [ ] Camera detection and colour processing are functioning.

---

# Additional Documentation

For further information, see:

- [`PARTS_AND_PURCHASE_LINKS.md`](PARTS_AND_PURCHASE_LINKS.md)
- [`3D_PRINTING_SETTINGS.md`](3D_PRINTING_SETTINGS.md)
- [`SOFTWARE_SETUP.md`](SOFTWARE_SETUP.md)
- [`../schemes/`](../schemes/)
- [`../src/`](../src/)
- [`../testing/`](../testing/)

The engineering journal contains the detailed development history, design calculations, testing results, mechanical reasoning and software architecture behind the final robot.
