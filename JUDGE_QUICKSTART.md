# Judge quick start

If a judge has five minutes, show these things in this order.

## 1. Final robot

Open the front/rear/side/top views in [`v-photos/`](./v-photos/).

## 2. Mechanical idea

Show:

- 4WD
- two mechanical LEGO differentials
- central driveshaft
- CAD/PLA chassis
- 36-tooth printed gear + 20-tooth LEGO gear

## 3. Electronics

Open [`schematics/schematic.png`](./schematics/schematic.png).

Point out:

- Raspberry Pi 5
- TB6612FNG
- two cameras
- MPU6050
- separate motor and Pi power branches

## 4. Software

Open [`code/config.py`](./code/config.py) and show the actual steering and Open Challenge values.

## 5. Evidence

Open:

- `testing/test_results.csv`
- `testing/processing_observations.csv`
- `testing/power_measurements.csv`
- `testing/Open_Challenge.mp4`

## 6. Be honest about parking

The parking subsystem is implemented and physically tested, but the latest engineering record says final alignment still needs reliable calibration. That is an engineering limitation, not something to hide.

## 7. Show the engineering loop

Use [`testing/engineering_evolution.md`](./testing/engineering_evolution.md):

**Problem → constraint → design decision → implementation → test → observation → next iteration.**

That is the strongest story in this project.
