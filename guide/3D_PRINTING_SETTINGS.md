# 3D Printing Settings

This document provides the complete OrcaSlicer configuration and printing guidance used for the robot's custom 3D-printed parts. It is intended to be self-contained: the settings required to reproduce the documented baseline are recorded directly below.

**Printer:** Anycubic Kobra 2 Neo  
**Nozzle:** 0.4 mm  
**Filament:** Generic PLA

Unless specifically changed for a particular part or print purpose, use the baseline values listed in this document.

---

## 1. Quality Settings

### Layer height

| Setting | Value |
|---|---:|
| Layer height | 0.2 mm |
| First layer height | 0.2 mm |

**Guidance:** The standard configuration uses a **0.2 mm layer height**. Adjust layer height when a different surface quality, smoothness, detail level, or print time is required.

### Line width

| Setting | Value |
|---|---:|
| Default | 0.4 mm |
| First layer | 0.4 mm |
| Outer wall | 0.4 mm |
| Inner wall | 0.4 mm |
| Top surface | 0.4 mm |
| Sparse infill | 0.4 mm |
| Internal solid infill | 0.4 mm |
| Support | 0.4 mm |
| Bridge | 100% |

### Seam

| Setting | Value |
|---|---|
| Seam position | Nearest |
| Staggered inner seams | Disabled |
| Seam gap | 10% |
| Scarf joint seam (beta) | None |
| Role based wipe speed | Enabled |
| Wipe speed | 80% |
| Wipe on loops | Disabled |
| Wipe before external loop | Disabled |

**Guidance:** Keep the seam position set to **Nearest** to reduce visible seam/scar lines on the printed part. The remaining settings in this section can remain at the baseline values above.

---

## 2. Precision and Wall Settings

### Precision

| Setting | Value |
|---|---:|
| Slice gap closing radius | 0.049 mm |
| Resolution | 0.012 mm |
| Arc fitting | Enabled |
| X-Y hole compensation | -0.1 mm |
| X-Y contour compensation | -0.1 mm |
| Elephant foot compensation | 0.15 mm |
| Elephant foot layers density | 100% |
| Elephant foot compensation layers | 2 layers |
| Precise wall | Enabled |
| Precise Z height | Enabled |
| Convert holes to polyholes | Disabled |

### Ironing

| Setting | Value |
|---|---|
| Ironing type | No ironing |

### Z contouring

| Setting | Value |
|---|---|
| Z contouring enabled | Disabled |

### Wall generator

| Setting | Value |
|---|---|
| Wall generator | Arachne |
| Wall transitioning threshold angle | 10° |
| Wall transitioning filter margin | 25% |

**Guidance:** Adjust **X-Y hole compensation** and, where necessary, **X-Y contour compensation** according to whether a tighter or looser fit is required for holes and mating parts. Keep **Precise wall** and **Precise Z height** enabled for automatic dimensional adjustment.

---

## 3. Strength, Shell and Infill Settings

### Walls

| Setting | Value |
|---|---:|
| Wall loops | 4 |
| Alternate extra wall | Disabled |
| Detect thin walls | Disabled |

### Top/bottom shells

| Setting | Value |
|---|---:|
| Top shell layers | 3 layers |
| Top shell thickness | 0.6 mm |
| Top surface density | 100% |
| Top surface pattern | Monotonic |
| Bottom shell layers | 3 layers |
| Bottom shell thickness | 0 mm |
| Bottom surface density | 100% |
| Bottom surface pattern | Monotonic |
| Top/bottom solid infill/wall overlap | 25% |

### Infill

| Setting | Value |
|---|---:|
| Sparse infill density | 10% |
| Fill Multiline | 1 |
| Sparse infill pattern | Gyroid |
| Z-buckling bias optimization (experimental) | Disabled |
| Sparse infill direction | 45° |
| Sparse infill rotation | Not recorded in the available configuration notes |

### Rapid testing configuration

For rapid prototype, dimension and fit testing:

- **Wall loops:** 2
- **Sparse infill density:** 10%
- **Sparse infill pattern:** Grid or Lines

This configuration reduces print time and material use while testing the geometry and fit of a part.

### Final strong-print configuration

For final parts requiring greater structural strength:

- **Wall loops:** 4
- **Sparse infill density:** 15%
- **Sparse infill pattern:** Gyroid

The remaining settings in this section can remain at the baseline values unless a particular part requires a different strength, weight, or fit trade-off.

---

## 4. Support Settings

### Support

| Setting | Value |
|---|---|
| Enable support | Enabled when required by geometry |
| Type | Tree (auto) |
| Style | Tree Slim |
| Threshold angle | 30° |
| First layer density | 90% |
| First layer expansion | 2 mm |
| On build plate only | Enabled |
| Support critical regions only | Disabled |
| Ignore small overhangs | Enabled |

### Raft

| Setting | Value |
|---|---:|
| Raft layers | 0 layers |

### Filament for supports

| Setting | Value |
|---|---|
| Support/raft base | Default |
| Support/raft interface | Default |

### Support ironing

| Setting | Value |
|---|---|
| Ironing Support Interface | Disabled |

### Advanced support settings

| Setting | Value |
|---|---:|
| Top Z distance | 0.2 mm |
| Bottom Z distance | 0.2 mm |
| Support wall loops | 0 |
| Base pattern | Default |

**Guidance:** Use support for parts or regions containing critical overhangs.

Recommended support configuration:

- **Type:** Tree
- **Style:** Tree Slim
- **Placement:** On build plate only
- **Top Z distance:** Keep between **0.20 mm and 0.256 mm**

The **On build plate only** option limits support generation to structures that can begin from the build plate. Support should therefore be enabled only where required by the part geometry.

---

## 5. Skirt, Brim and Special-Mode Settings

### Skirt

| Setting | Value |
|---|---|
| Skirt loops | 3 |
| Skirt type | Combined |
| Skirt minimum extrusion length | 0 mm |
| Skirt distance | 2 mm |
| Skirt start point | -135° |
| Skirt speed | 50 mm/s |
| Skirt height | 1 layer |
| Draft shield | Disabled |
| Single loop after first layer | Disabled |

### Brim

| Setting | Value |
|---|---|
| Brim type | Outer and inner |
| Brim width | 5 mm |
| Brim-object gap | 0.1 mm |
| Brim flow ratio | 1 |
| Brim follows compensated outline | Enabled |
| Combine brims | Enabled |

### Special mode

| Setting | Value |
|---|---|
| Slicing Mode | Regular |
| Print sequence | By layer |
| Intra-layer order | Default |

**Guidance:** For large objects or parts requiring additional bed adhesion, use an **outer brim** and adjust the **brim width** according to the size and stability of the object. A wider brim can provide additional adhesion to the print bed.

The documented baseline uses a **5 mm brim width**, which may be increased or reduced depending on the object.

---

## 6. Object Arrangement Before Slicing

Before slicing, use OrcaSlicer's **Auto Arrange** function to arrange the objects on the build plate.

**Guidance:** Auto-arrange objects before slicing to help:

- use the available build plate efficiently;
- reduce unnecessary spacing between multiple objects;
- improve print planning and overall print time; and
- avoid unnecessary support where object placement allows a better orientation.

The resulting arrangement should still be checked before slicing, especially for large, tall, or unusually shaped parts.

---

## Quick Reference

### Rapid testing

| Setting | Recommended value |
|---|---|
| Wall loops | 2 |
| Sparse infill density | 10% |
| Infill pattern | Grid or Lines |

### Final strong print

| Setting | Recommended value |
|---|---|
| Wall loops | 4 |
| Sparse infill density | 15% |
| Infill pattern | Gyroid |

### General settings

| Setting | Recommended configuration |
|---|---|
| Layer height | 0.2 mm standard; adjust for required surface quality |
| First layer height | 0.2 mm |
| Seam position | Nearest |
| X-Y hole compensation | Adjust according to required tight/loose fit |
| Precise wall | Enabled |
| Precise Z height | Enabled |
| Support type | Tree |
| Support style | Tree Slim |
| Support placement | On build plate only |
| Top Z distance | 0.20–0.256 mm |
| Brim | Outer brim for larger objects; adjust width as needed |
| Object placement | Use Auto Arrange before slicing |

---

## Configuration Notes

This document records a practical baseline rather than requiring every part to be printed with exactly the same settings. The following values may be intentionally adjusted after evaluating the geometry and purpose of a specific part:

- **Layer height** may be changed to balance surface quality against print time.
- **X-Y compensation** may be adjusted after testing the fit of holes and mating parts.
- **Wall loops and infill** may be reduced for rapid prototypes and increased for final structural parts.
- **Support** should be enabled only where the geometry contains critical overhangs.
- **Brim width** may be adjusted according to object size and bed-adhesion requirements.
- **Object arrangement and orientation** should be checked before slicing to reduce unnecessary print time and support material.

For settings not specifically changed for a particular print, retain the baseline configuration recorded in this guide.
