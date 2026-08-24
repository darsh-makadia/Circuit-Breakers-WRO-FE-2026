# Build The Dark Knight from zero

This is the shortest path from an empty workbench to the same **documented Nationals configuration** of Team Current's robot.

The important rule is simple: **do not guess a dimension, wiring connection or software value when this repository already contains the reference.** Use the CAD files for geometry, `schematics/schematic.png` for wiring, and `code/config.py` for software calibration values.

> This guide describes the configuration documented in the engineering report. It does not claim that the final parking manoeuvre is already competition-perfect. The parking subsystem is implemented and physically tested, but its final alignment still needs calibration.

---

## 1. What you are building

The final robot is a hybrid of CAD/PLA structure and LEGO Technic drivetrain parts:

- 4-wheel drive
- one JGB37-520 12 V 600 RPM drive motor
- one central driveshaft
- two LEGO mechanical differentials, one per axle
- servo steering
- Raspberry Pi 5 4 GB
- two Raspberry Pi Camera Module 3 cameras
- MPU6050 gyro
- TB6612FNG motor driver
- 3S LiPo, 2200 mAh, 11.1 V nominal
- two regulated power branches plus the raw motor branch
- PLA printed chassis, camera hardware and electronics enclosure

The confirmed overall size is **24 cm × 13 cm × 27.5 cm** and the documented mass is **863 g**.

---

## 2. Before buying or printing anything

### Read these files in this order

1. [`documentation/Team_Currents_Final_Document.pdf`](./documentation/Team_Currents_Final_Document.pdf)
2. [`cad/README.md`](./cad/README.md)
3. [`schematics/schematic.png`](./schematics/schematic.png)
4. [`models/`](./models/)
5. [`photos/differential.png`](./photos/differential.png)
6. [`code/README.md`](./code/README.md)
7. [`code/config.py`](./code/config.py)

The engineering PDF explains **why** the design is this way. The CAD and schematic show **what to physically build**. The code shows the **exact software configuration**.

---

## 3. Parts checklist

### Electronics

| Part | Documented configuration |
|---|---|
| Main computer | Raspberry Pi 5, 4 GB |
| Cameras | Raspberry Pi Camera Module 3 ×2 |
| Drive motor | JGB37-520 DC, 12 V, 600 RPM |
| Steering | Servo motor |
| Motor driver | TB6612FNG |
| IMU | MPU6050 |
| Battery | 3S LiPo, 2200 mAh, 11.1 V nominal |
| Buck converter 1 | Regulated 5 V rail for servo + motor-driver logic |
| Buck converter 2 | 5 V, 5 A rated Raspberry Pi supply |
| Display | OLED |
| Indicators | RGB LED + programmable LED |
| Start input | Push button |

### Mechanical / manufacturing

| Part | Documented configuration |
|---|---|
| Structural material | PLA |
| Printer | Anycubic Cobra 2 Neo |
| Main chassis | `cad/final_chassis.stl` |
| Chassis part 2 | `cad/final_chassis_part2.stl` |
| Dual camera mount | `cad/dual_camera_mount.stl` |
| Camera case | `cad/camera_case.stl` |
| Electronics box | `cad/circuit_box.stl` |
| Electronics box lid | `cad/circuit_box_lid.stl` |
| Custom drivetrain gear | 36-tooth printed gear |

### LEGO drivetrain inventory

The engineering document explicitly lists these LEGO component types:

- 2X4 L beam
- 9 beam
- bush
- half bush
- 2L axle connector
- 5L axle
- 6L axle
- 4L axle with stop
- 28-tooth differential
- 24-tooth gear
- 20-tooth gear
- 12-tooth bevel gear
- smooth pin
- friction pin
- universal joint
- 3L friction pin

**Important:** the engineering document lists the component types but does not give a complete per-part quantity table. Do not invent quantities. Match the final drivetrain to the CAD/photographs and the two-differential architecture.

---

## 4. Print the CAD parts

Print the six supplied STL files:

1. `final_chassis.stl`
2. `final_chassis_part2.stl`
3. `dual_camera_mount.stl`
4. `camera_case.stl`
5. `circuit_box.stl`
6. `circuit_box_lid.stl`

The repository also contains PNG previews in `models/` and `cad/` so you can identify each part before printing.

### Do not redesign these parts first

The team already changed the camera mount and chassis after testing. The adjustable camera mount exists because the first LEGO camera mount was too unstable. Start from the final CAD rather than rebuilding the earlier prototype.

---

## 5. Build the mechanical drivetrain

### Step 1 — Build the LEGO drivetrain

Use the listed LEGO beams, axles, gears, universal joints and differentials to reproduce the final drivetrain shown in the repository photographs.

The key layout is:

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

There are **two mechanical differentials, one per axle**. The final design does not use an electronic differential.

### Step 2 — Install the drive motor

Mount the JGB37-520 motor to the drivetrain/chassis assembly shown in the final CAD and photographs.

The final external gear pair is:

- custom 36-tooth printed gear
- LEGO 20-tooth gear
- documented tooth-count relationship: **1:1.8**

The engineering document explains that this was intentionally chosen for more wheel speed at the cost of available torque.

### Step 3 — Install steering

Mount the steering servo using the dedicated servo mounting geometry in the CAD.

Do not use the full theoretical servo travel as the robot's steering range. The tested software range is:

- minimum: **35°**
- centre: **75°**
- maximum: **115°**

---

## 6. Install the cameras

There are two Raspberry Pi Camera Module 3 cameras.

| Camera | Job | Documented lens-centre height |
|---|---|---:|
| Front / main | Track + obstacle perception | 25.0 cm |
| Rear / parking | Parking-area perception | 23.5 cm |

The front camera is configured at **1480 × 520** for the challenge programs. The rear parking camera is **640 × 480**.

Use the supplied adjustable dual-camera mount and camera case. The mount exists because camera height and angle changed the perception results during development.

### Camera connection

Both cameras use ribbon-cable connections to the Raspberry Pi camera interfaces.

The software opens:

- front camera as camera index `0`
- parking/rear camera as camera index `1`

If the physical camera order is reversed, swap the ribbon connections rather than silently changing the software configuration without documenting it.

---

## 7. Install the electronics

Put the Raspberry Pi, motor driver, buck converters, IMU and other electronics into the printed electronics enclosure shown in the CAD and photos.

Keep the high-current motor path separate from the regulated logic path.

The final power architecture is:

```text
                     3S LiPo 11.1 V nominal
                              │
                ┌─────────────┼─────────────┐
                │             │             │
             Buck 1       Motor driver    Buck 2
             5 V           VMOT = raw     5 V / 5 A
                │             │             │
        ┌───────┴──────┐      │        Raspberry Pi 5
        │              │      │              │
     Servo VCC   TB6612 logic  │        cameras/peripherals
                              │
                         JGB37-520
```

The Raspberry Pi's own 3.3 V rail supplies the documented I2C-side devices such as the MPU6050 and OLED.

### Critical power rule

**Do not power the drive motor from the Raspberry Pi.** The engineering development specifically moved away from that arrangement.

---

## 8. Wire the system

Use the enlarged [`schematics/schematic.png`](./schematics/schematic.png) as the authoritative wiring reference.

The final documented architecture is:

- raw battery → motor-driver VMOT
- raw battery → Buck 1 input
- raw battery → Buck 2 input
- Buck 1 5 V → servo VCC + motor-driver logic VCC/nSTBY
- Buck 2 5 V / 5 A → Raspberry Pi 5
- Raspberry Pi 3.3 V → MPU6050 and OLED-side logic
- common ground across the system

### Software GPIO values in this release

The code currently defines these BCM GPIO pins:

| Function | BCM GPIO |
|---|---:|
| Motor PWM | 13 |
| Motor direction 1 | 5 |
| Motor direction 2 | 6 |
| Steering servo | 22 |
| MPU6050 I2C bus | Bus 1 |
| MPU6050 address | `0x68` |

The motor-driver channel arrangement is shown in the schematic. The engineering document states that the motor-driver channels are wired in parallel for the single drive motor so the two channels share the motor load.

**If the schematic and this table ever disagree, use the schematic and then update this guide rather than guessing.**

---

## 9. Install the Raspberry Pi software

Install Raspberry Pi OS on the Raspberry Pi 5 and enable the interfaces required by the hardware, including I2C and the camera system.

The repository software uses Python and these documented libraries:

- OpenCV
- NumPy
- RPi.GPIO
- Picamera2
- smbus2

Install the repository requirements:

```bash
python3 -m pip install -r requirements.txt
```

Then enter the code directory:

```bash
cd code
```

Do **not** start with a moving robot. First test the camera, servo, motor and IMU independently.

---

## 10. First power-up checklist

Before connecting the battery:

- [ ] Wheels can rotate freely by hand.
- [ ] Steering linkage moves without binding.
- [ ] Motor cannot touch the chassis.
- [ ] Both cameras are firmly mounted.
- [ ] IMU is firmly mounted.
- [ ] Battery is secured.
- [ ] Motor and servo wiring are insulated and mechanically protected.
- [ ] Common ground is connected.
- [ ] Motor driver VMOT is on the raw battery branch.
- [ ] Raspberry Pi is on the regulated Buck 2 branch.
- [ ] No raw battery voltage is being fed into a 5 V input.

Power on with the drive wheels lifted from the floor for the first motor test.

---

## 11. Calibrate the steering

The software values are already in `code/config.py`:

```text
SERVO_MIN    = 35
SERVO_CENTER = 75
SERVO_MAX   = 115
```

With the robot stationary:

1. Run the steering test.
2. Confirm the centre position is mechanically straight.
3. Confirm 35° does not bind.
4. Confirm 115° does not bind.
5. Never increase the limits just because the servo can physically rotate farther.

These are the values used in the documented Nationals configuration.

---

## 12. Calibrate the MPU6050

The robot uses gyro-only Z-axis heading for the parking manoeuvre.

At startup the code:

1. waits for the IMU to settle;
2. keeps the robot stationary;
3. reads **1500 gyro samples**;
4. averages them to estimate Z-axis bias;
5. subtracts the bias from later readings;
6. integrates corrected angular velocity into a 0–360° heading.

The documented calibration sequence takes approximately three seconds including settling.

### Very important

**Do not move the robot during calibration.**

The code uses I2C bus 1 and address `0x68`.

---

## 13. Check the cameras

Run the camera system with the robot stationary.

Confirm:

### Front camera

- track is visible;
- black boundaries are visible;
- blue/orange markers can be seen;
- red/green obstacles can be seen;
- the robot body is not dominating the lower ROI.

### Rear camera

- parking structures are visible;
- magenta/purple parking structures are detected;
- the image is not rotated incorrectly.

The software uses the front camera at 1480 × 520 and the rear camera at 640 × 480.

---

## 14. Run the Open Challenge

The documented Open Challenge configuration is:

| Parameter | Value |
|---|---:|
| Image width | 1480 px |
| Image height | 520 px |
| Kp | 0.013 |
| Marker cooldown | 1.0 s |
| Laps | 3 |
| Relevant crossings/lap | 4 |
| Total counted crossings | 12 |
| Initial PWM | 40 |
| Steering | 35°–115°, centre 75° |

The first valid marker determines direction:

- **Blue → anticlockwise**
- **Orange → clockwise**

After direction is known, the software counts only that marker colour.

The marker detector uses rising-edge behaviour with a cooldown so one long visible marker is not counted repeatedly.

---

## 15. Run the Obstacle Challenge

The front camera detects green and red obstacles using colour segmentation, contours and the documented confidence pipeline.

The obstacle program also uses the rear camera for the magenta/purple parking marker.

The documented sequence is:

1. detect and avoid obstacles;
2. continue the three-lap sequence;
3. count the magenta/purple parking marker once per lap;
4. after the third marker, continue through the additional section;
5. perform the direction-dependent transition;
6. approach the parking area;
7. use the rear camera and IMU state machine for parking.

The final parking subsystem is **implemented and tested but not yet consistently reliable at final alignment**, so do not describe the 1:09 obstacle result as a fully completed competition parking time.

---

## 16. Test in the same order as the team

Do not jump directly to a full autonomous run.

### Test 1 — mechanical

- wheels free
- steering free
- drivetrain rotates
- differentials work

### Test 2 — electrical

Record the supply voltages and confirm:

- LiPo before run: **11.1 V**
- LiPo after multiple runs: **10.8 V**
- motor driver OFF: **11.1 V**
- motor driver ON: **10.8 V**
- Buck 1: **5.0 V**
- Pi supply: **5.0 V**

Current was not directly bench-measured as part of the final testing record. Do not invent a current value.

### Test 3 — steering

Confirm 35 / 75 / 115°.

### Test 4 — camera

Confirm front and rear detections.

### Test 5 — Open Challenge

Start at low speed and verify marker counting before attempting the recorded performance.

### Test 6 — Obstacle Challenge

Verify red/green avoidance and magenta marker counting.

### Test 7 — parking

Test the parking state machine separately. Record alignment/contact failures rather than hiding them.

---

## 17. Known measured performance

### Open Challenge

Recorded complete runs:

**32, 30, 28, 28, 28, 28 s**

Best recorded result: **28 s**.

### Obstacle Challenge navigation

Recorded navigation runs up to the parking approach:

**1:10, 1:09, 1:11, 1:20, 1:15, 1:13**

Best recorded navigation result: **1:09**.

These runs had slightly different obstacle placement, so they should not be treated as perfectly identical trials.

---

## 18. If something does not work

### Robot turns too far

Check:

1. servo centre = 75°;
2. steering limits = 35° and 115°;
3. mechanical linkage is centred;
4. servo horn is installed correctly.

### IMU heading jumps

Check:

1. robot is still during the 1500-sample calibration;
2. I2C wiring;
3. address `0x68`;
4. ground connection;
5. sensor mounting is rigid.

### Camera detects wrong colours

Check:

1. correct camera index;
2. camera orientation;
3. lighting;
4. threshold values in `code/vision.py`;
5. the colour-channel handling described in the engineering document.

### Obstacle detection is late

The measured Obstacle Challenge processing loop was about **11.25 FPS** in the recorded overlays. At about 0.93 m/s this is roughly 8 cm of travel per processed frame. Do not assume the configured 60 FPS target is the actual end-to-end processing rate.

### Parking fails

Do not simply increase time delays. The team moved away from timed turns because battery state, friction, motor speed and steering geometry change the actual rotation. Use the IMU/state-machine approach and recalibrate the turn sequence, heading thresholds and visual position thresholds.

---

## 19. Reproduction rule

If you are trying to reproduce the robot exactly, use this priority order when two files appear to disagree:

1. **Current physical robot**
2. **Current source code**
3. **Final schematic**
4. **Final CAD/STL**
5. **Engineering document**
6. **README explanations**

The README is a guide, not a replacement for the source files.

---

## 20. What is not specified

To keep this repository honest, some workshop-level details are intentionally not invented here:

- exact screw lengths and fastener quantities;
- exact quantity of every LEGO pin/beam/axle;
- exact print temperature/speed profile;
- exact servo stall current of the installed unit;
- a complete independent bench motor-characterisation dataset.

The engineering document does not provide those as verified values. Where they matter, use the actual CAD, schematic and photographs of the final robot.

---

## 21. Final build acceptance checklist

A reproduction should not be called "The Dark Knight final configuration" until all of these are true:

- [ ] 24 × 13 × 27.5 cm overall envelope is matched.
- [ ] 4WD is installed.
- [ ] Two mechanical LEGO differentials are installed, one per axle.
- [ ] Central driveshaft is installed.
- [ ] JGB37-520 12 V 600 RPM motor is installed.
- [ ] 36-tooth custom gear + LEGO 20-tooth gear are installed in the documented drivetrain.
- [ ] Steering is calibrated to 35° / 75° / 115°.
- [ ] Both Camera Module 3 cameras are installed.
- [ ] Front camera height is about 25.0 cm.
- [ ] Rear camera height is about 23.5 cm.
- [ ] MPU6050 is installed at I2C address 0x68.
- [ ] 1500-sample stationary calibration works.
- [ ] TB6612FNG and power branches match the schematic.
- [ ] Raspberry Pi receives regulated 5 V from Buck 2.
- [ ] Motor VMOT uses the raw battery branch.
- [ ] Open Challenge reaches the documented 12-crossing target.
- [ ] Obstacle detection identifies red/green targets.
- [ ] Rear camera identifies magenta/purple parking structures.
- [ ] Parking state machine reaches its tested states without unsafe indefinite motion.

Only after this checklist should performance comparisons be made.
