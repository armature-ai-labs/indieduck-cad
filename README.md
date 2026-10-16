# IndieDuck CAD

IndieDuck is organised as one shared mechanism, the **platform**, and **editions** that give it different exteriors. A platform change applies to every edition. The current edition is **IndieDuck Cyber Edition** (`editions/cyber/`), designed by [Zankar Savalia](https://www.linkedin.com/in/zankarvs/), on platform **P1** (`platform/`). Its design was developed as R25; the R25 tags and records refer to it.

Cyber Edition is a **design-review CAD candidate, not a manufacturing release**. Earlier designs (R20 and before) are at the tag `r20-simulation-study-v1`.

![IndieDuck Cyber Edition, assembled CAD](editions/cyber/previews/cyber-assembly.png)

## Layout

| Path | Contents |
|---|---|
| `platform/PLATFORM.md` | What platform P1 is, and the rules an edition must follow |
| `platform/native/IndieDuck_P1_HeadBase.FCStd` | The head base as an editable PartDesign body with a parameter sheet |
| `platform/exports/step/`, `platform/exports/stl/` | The 27 platform printed parts (`P1_*`), STEP and STL, assembly coordinates in millimetres |
| `editions/cyber/edition.yaml` | Cyber Edition's description: designers, maturity, model ID, training task, open items |
| `editions/cyber/native/IndieDuck_Cyber_Assembly.FCStd` | The complete robot (platform P1 plus the Cyber exterior) in its saved pose, FreeCAD 1.1.4. Each part stores a `MovingBody` property naming the joint link it moves with. |
| `editions/cyber/exports/step/`, `editions/cyber/exports/stl/` | The 28 Cyber exterior parts (`Cyber_*`) |
| `editions/cyber/exports/IndieDuck_Cyber_Assembly.step` | Full assembly, 161 solids including purchased-part reference envelopes |
| `editions/cyber/exports/multicolour/` | Panels with their orange accents as one multi-colour print: the camera face with both optical rings, and the front and rear torso panels with their stripes. Load each into Bambu Studio as one object and give the accents orange |
| `editions/cyber/exports/print-oriented/` | Parts exported in their print orientation (HelmetLower prints upside down) |
| `editions/cyber/previews/`, `editions/cyber/validation/` | CAD views and verification records |
| `platform/P1-kinematics.json` | Platform P1's joint chain: joints, axes, standing pose and verified ranges, in assembly coordinates |
| `tools/edition_verify.py` | Verifies an edition against the platform (paperwork, unchanged platform, parts, standing-pose overlaps, joint sweeps): `EDITION=<id> freecadcmd tools/edition_verify.py` |
| `PARTS-CATALOG.md` | **Every printed part with its code** (for example `C-TORF`), revision, colour, location on the robot and file links |
| `PARTS-CHANGELOG.md` | **What changed and what to reprint**, for every release, with each part's revision history |
| `PART-VERSIONS.json`, `tools/part_versions.py` | Part revisions and geometric fingerprints; `check`, `update`, `release` and `report` commands |
| `COMPONENTS.csv` | Every printed part with its scope, and in `print_with` the panel a colour accent is printed with (`platform` or `edition`), edition, native object, material and exports |

**New editions** follow `platform/PLATFORM.md`: a duck form factor on P1 that changes only the exterior, submitted as `editions/<id>/` with its own `edition.yaml`.

**Editing.** The R25 assembly holds solids without construction history; the head base has its own editable PartDesign source. Edits to other R25 parts are direct solid edits for now. R20's history-bearing native documents are at the tag `r20-simulation-study-v1`.

## Changes made for publication (13 October 2026)

- **Neck clearance.** The R25 candidate's narrower torso neck opening collided with both neck servos at almost every neck angle. TorsoFront now has a 1 mm swept clearance channel, the trunk a matching relief, and the neck link a small trim where it passed the right hip-yaw servo. The neck is clear of every other part at every 2.5° step from **−65° (chin tuck, as used by the forward roll) to +27.5° (head back)**, simulator convention, axis (0, −1, 0). The head-back limit is set at +27.5° because the head base sweeps across the rear torso beyond it. The simulator currently allows −90° to +60°; it will be narrowed to this range in the next simulator update.
- **HelmetLower print orientation.** Its bottom edge follows the head base contour, so it has no flat underside and the slicer rejects it as exported. Print it **upside down** on its flat top edge; only five internal screw bosses, hidden inside the helmet, want support.

## Printing (provisional)

Sliced in Bambu Studio 2.08 for a Bambu Lab P2S, 0.4 mm nozzle, 0.20 mm layers, 3 walls, 20 % infill: 39 parts on seven plates, about **360 g PLA and 34 g TPU 95A, roughly 16½ hours**. The retained R20 head base, thighs, yaw links, head brackets and cradles are extra. White, orange and dark are appearance colours; use PLA for rigid parts and TPU 95A for the soles. Keep the four HelmetRoof, HelmetLower, FaceBezel and CameraCarrier parts on two plates; Bambu silently dropped one part when all four shared a plate.

## Joint ranges and cover trims (15 October 2026)

Every joint was swept in 1 degree steps against every other part. Three hardware objects had the wrong joint link (the camera-carrier screws belong to the head-yaw link; the hip-pitch clamp screws and nuts belong to the hip bracket) and are corrected. Covers that blocked joints were trimmed by the swept path of the part they hit, plus 1 mm: pelvis front panel (side wings notched for the hips, 19 %), hip cowls (3 %), toe caps (16 %), shin caps (11 %), pelvis rear panel (under 1 %). Verified ranges with all covers fitted: hip yaw -19 to 0 deg (left, mirrored right), hip roll -18 to 22, hip pitch -90 to 0, knee -85 to 46, ankle 0 to 78, neck -65 to +27.5 (+15 when the head is also turned or rolled), head pitch -35 to 85, head yaw +-90, head roll -25 to +11 (structural stop at the jaw bearing; full +25 needs the jaw bearing tower moved). Mouth (resolved 15 October 2026): the jaw surrounds are now round caps of 12 mm radius centred on the jaw pivot, and each head rim has a matching 13 mm arc, so the jaw opens 0 to 30 deg with no contact. Records: `editions/cyber/validation/R25-joint-ranges.json`.

## Cover fixings (15 October 2026)

Cyber's original cover holes mostly had nothing behind them (9 of 45 could take a boss). Covers are now held by 34 M2 x 8 self-tapping screws through 2.4 mm holes into 5.5 mm posts printed on the platform parts that move with each cover (trunk, head base, camera carrier, jaw bearing tower, hip brackets, thighs and shanks). Unused holes are filled. The pelvis front has no structure behind it (the hip brackets swing there), so it hooks behind the torso front's lower edge and two of the screws go through the torso front into bosses on its tongues: fit the pelvis front first, then the torso front. The face bezel prints with the camera face, the head rims and rear bumper with the helmet lower, and the toe caps with the feet (`print_with` in `COMPONENTS.csv`, files in `editions/cyber/exports/multicolour/`). The right shin cap was re-made as an exact mirror of the left with clean geometry (its printed shape is unchanged). Every post was checked for a clear path and swept through all joint ranges.

## Support parts added to the printed list (14 October 2026)

Four printed support parts were modelled in the assembly but missing from `COMPONENTS.csv`: the jaw bearing tower, jaw bearing keeper and jaw bearing plug, and the neck bearing retainer. They are now listed and exported (PLA, structural), bringing the printed set to 55. The full bill of materials, including purchased parts, fasteners, electronics and wiring, is in the project hub: `armature-ai-labs/indieduck` `BOM.md`.

## Head base redrawn (13 October 2026)

The head base (the head's chassis: the roll-servo cradle, mouth-servo cradle, jaw bearing tower and camera carrier all mount on it) was the last part built from XGO-Duck geometry. It is replaced by `A_HeadBase`, drawn by IndieDuck from our own parameters: the same footprint and mounting points, a 5 mm floor, a stiffening wall, and clearances taken from our neighbouring parts and from the swept paths of the head roll, head yaw and jaw. It is clear of every other part, and clear through head roll ±25°, head yaw ±90°, jaw 0° to 30° and the neck range. It prints flat with no supports (25.8 g, 56 min on a P2S). The front half is 7 mm narrower each side than before, where the jaw's sides pass. Editable source: `platform/native/IndieDuck_P1_HeadBase.FCStd`; comparison in `editions/cyber/previews/cyber-headbase-replacement.png`; record in `editions/cyber/validation/R25-headbase-replacement.json`.

## R25 limits

Not yet resolved: camera module choice and its fit; a fastener bill of materials (cowls and toe caps have aligned screw provisions, lengths unconfirmed); retention for the 1 mm optical rings and the small torso inlays; printer-specific clearances on trim parts; strength of the added hip and shank mounts; real mass and balance. The exterior adds material: 482 cm³ of printed CAD volume against 434.5 cm³ for the earlier mechanical candidate. Checked: static clearance of every part, the neck range above, and the forward-roll tuck pose. Not checked: head yaw or roll combined with neck pitch, leg motion with the new covers, jaw motion with the jaw surrounds, cables, physical fit. The browser assembly guide and simulator still show R20 until their R25 update; the R20 display bundle they use is kept in those repositories.

## Earlier releases

R20 and earlier CAD studies are no longer on this branch. They remain available at the tags `r20-simulation-study-v1` and `cad-study-2026-10-09`. They contain third-party geometry under the notices recorded in those tags; the current R25 files do not.
