
# 3D Printing Settings

All structural parts (chassis, camera mount, camera case, circuit box, circuit box lid, and the 36-tooth gear) are printed in PLA on an **Anycubic Kobra 2 Neo**, 0.4 mm brass nozzle.

Two profiles are used depending on the purpose of the print: a fast profile for testing fit and iteration, and a stronger profile for final competition parts.

---

## Printer / Filament

| | |
|---|---|
| Printer | Anycubic Kobra 2 Neo |
| Nozzle | 0.4 mm, brass |
| Filament | Generic PLA |

---

## Profile 1 — Rapid Testing

Use this profile when checking fit, tolerances, or iterating on a design — not for the final competition part.

| Setting | Value |
|---|---|
| Wall loops | 2 |
| Infill density | 10% |
| Infill pattern | Grid or Lines |

---

## Profile 2 — Final Strong Print

Use this profile for any part going on the competition robot.

| Setting | Value |
|---|---|
| Wall loops | 4 |
| Infill density | 15% |
| Infill pattern | Gyroid |

---

## Settings that apply to both profiles

### Layer height
- **Layer height / First layer height:** 0.2 mm as a starting point — increase for faster prints, decrease for smoother visible surfaces depending on the part.
- **Seam position:** Nearest — reduces visible scar lines on the printed surface.
- Everything else under Quality → Layer height/Line width: left at slicer default.

### Precision (X-Y fit)
- **X-Y hole compensation / X-Y contour compensation:** adjust from -0.1 mm depending on whether a hole or fitted joint needs to be tighter or looser. Start at -0.1 mm and tune per part if screws/pins are too tight or too loose.
- **Precise wall** and **Precise Z height:** both enabled — lets the slicer auto-adjust for more dimensionally accurate parts.

### Top/Bottom shells
- Top shell layers: 3 (0.6 mm)
- Bottom shell layers: 3
- Top/bottom surface density: 100%, pattern Monotonic

### Support
- **Enable support:** on, for any part with an overhang that needs it (e.g. the camera mount's angled bracket).
- **Type / Style:** Tree (auto), Tree Slim.
- **On build plate only:** enabled — this restricts support material to parts of the print actually in a critical overhang position, rather than supporting everything indiscriminately.
- **Threshold angle:** 30°.
- **Top Z distance:** keep between 0.2–0.256 mm (controls how easily support detaches from the printed surface without damaging it).

### Skirt / Brim
- **Skirt:** 3 loops, combined type, 2 mm distance — standard bed-adhesion/purge skirt.
- **Brim:** for larger parts (e.g. the chassis base), set brim type to Outer and adjust brim width upward from the 5 mm default for better first-layer adhesion on bigger prints. Not needed for small parts.

### Orientation
- **Always auto-arrange objects** before slicing — gives faster print times and requires less support material than manual placement.

---

## Per-part notes

| Part | Profile | Notes |
|---|---|---|
| Chassis | Final Strong Print | Larger part — increase brim width |
| Camera mount | Final Strong Print | Needs support on the angled bracket |
| Camera case | Final Strong Print | |
| Circuit box + lid | Final Strong Print | |
| 36-tooth gear | Final Strong Print | Tune X-Y compensation for a tight fit against the 20-tooth LEGO gear |
