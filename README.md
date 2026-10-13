# IndieDuck by Armature AI Labs

The current design is **R25**, a reference-driven exterior on the R20 mechanism: a tapered helmet with a recessed dark camera face, orange optical rings and rims, shoulder-faceted torso with orange inlays, forward hip cowls, slotted thigh caps, shin caps and faceted feet with white toe caps. Adapted from Open Duck Mini and inspired by Pollen Robotics' MicroDuck. Servo and joint positions are unchanged from R20. Project lineage and credits are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

R25 is a **design-review CAD candidate, not a manufacturing release**. The previous release, R20, is available at the tag `r20-simulation-study-v1`.

![R25 assembled CAD](previews/R25-assembly.png)

**Credits.** [Zankar Savalia](https://www.linkedin.com/in/zankarvs/) contributed to the design of the R25 exterior and helped prepare it for publication. Thank you, Zankar. See [CONTRIBUTORS.md](CONTRIBUTORS.md).

## R25 files

| Path | Contents |
|---|---|
| `native/robot/IndieDuck_R25_HeadBase.FCStd` | The head base as an editable PartDesign body with a parameter sheet (see below) |
| `native/robot/IndieDuck_R25_Assembly.FCStd` | Complete R25 robot in its saved pose, FreeCAD 1.1.4, self-contained. Each part stores a `MovingBody` property naming the joint link it moves with. |
| `exports/R25/step/`, `exports/R25/stl/` | 51 printed-component candidates, STEP and STL, in assembly coordinates (millimetres) |
| `exports/R25/IndieDuck_R25_Assembly.step` | Full assembly, 161 solids including purchased-part reference envelopes |
| `exports/R25/print-oriented/R25_HelmetLower_upside-down.stl` | HelmetLower in its print orientation (see below) |
| `previews/R25-*.png` | Actual CAD views: assembly, front, side, rear |
| `validation/R25-fixes.json`, `validation/R25-export-readback.json` | Changes made for publication and the export readback checks |
| `COMPONENTS.csv` | Maps every printed component to its native object, material and exports |

**Editing.** The R25 assembly holds solids without construction history; the head base has its own editable PartDesign source. Edits to other R25 parts are direct solid edits for now. R20's history-bearing native documents are at the tag `r20-simulation-study-v1`.

## Changes made for publication (13 October 2026)

- **Neck clearance.** The R25 candidate's narrower torso neck opening collided with both neck servos at almost every neck angle. TorsoFront now has a 1 mm swept clearance channel, the trunk a matching relief, and the neck link a small trim where it passed the right hip-yaw servo. The neck is clear of every other part at every 2.5° step from **−65° (chin tuck, as used by the forward roll) to +27.5° (head back)**, simulator convention, axis (0, −1, 0). The head-back limit is set at +27.5° because the head base sweeps across the rear torso beyond it. The simulator currently allows −90° to +60°; it will be narrowed to this range in the next simulator update.
- **HelmetLower print orientation.** Its bottom edge follows the head base contour, so it has no flat underside and the slicer rejects it as exported. Print it **upside down** on its flat top edge; only five internal screw bosses, hidden inside the helmet, want support.

## Printing (provisional)

Sliced in Bambu Studio 2.08 for a Bambu Lab P2S, 0.4 mm nozzle, 0.20 mm layers, 3 walls, 20 % infill: 39 parts on seven plates, about **360 g PLA and 34 g TPU 95A, roughly 16½ hours**. The retained R20 head base, thighs, yaw links, head brackets and cradles are extra. White, orange and dark are appearance colours; use PLA for rigid parts and TPU 95A for the soles. Keep the four HelmetRoof, HelmetLower, FaceBezel and CameraCarrier parts on two plates; Bambu silently dropped one part when all four shared a plate.

## Head base redrawn (13 October 2026)

The head base (the head's chassis: the roll-servo cradle, mouth-servo cradle, jaw bearing tower and camera carrier all mount on it) was the last part built from XGO-Duck geometry. It is replaced by `A_HeadBase`, drawn by IndieDuck from our own parameters: the same footprint and mounting points, a 5 mm floor, a stiffening wall, and clearances taken from our neighbouring parts and from the swept paths of the head roll, head yaw and jaw. It is clear of every other part, and clear through head roll ±25°, head yaw ±90°, jaw 0° to 30° and the neck range. It prints flat with no supports (25.8 g, 56 min on a P2S). The front half is 7 mm narrower each side than before, where the jaw's sides pass. Editable source: `native/robot/IndieDuck_R25_HeadBase.FCStd`; comparison in `previews/R25-headbase-replacement.png`; record in `validation/R25-headbase-replacement.json`.

## R25 limits

Not yet resolved: camera module choice and its fit; a fastener bill of materials (cowls and toe caps have aligned screw provisions, lengths unconfirmed); retention for the 1 mm optical rings and the small torso inlays; printer-specific clearances on trim parts; strength of the added hip and shank mounts; real mass and balance. The exterior adds material: 482 cm³ of printed CAD volume against 434.5 cm³ for the earlier mechanical candidate. Checked: static clearance of every part, the neck range above, and the forward-roll tuck pose. Not checked: head yaw or roll combined with neck pitch, leg motion with the new covers, jaw motion with the jaw surrounds, cables, physical fit. The browser assembly guide and simulator still show R20 until their R25 update; the R20 display bundle they use is kept in those repositories.

## Earlier releases

R20 and earlier CAD studies are no longer on this branch. They remain available at the tags `r20-simulation-study-v1` and `cad-study-2026-10-09`. They contain third-party geometry under the notices recorded in those tags; the current R25 files do not.
