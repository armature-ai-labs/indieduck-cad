# R25 CAD verification (13 October 2026)

R25 adds a reference-driven exterior to the R20 mechanism. Verification concerns this digital package, not a buildable or motion-qualified robot.

| Check | Result and scope |
|---|---|
| Native file | `IndieDuck_R25_Assembly.FCStd` opens in FreeCAD 1.1.4: 141 objects, 161 solids, all valid. Solid geometry only for the new exterior parts. |
| Static clearance | The 43 new exterior parts against every part at the saved pose: no overlap above 0.1 mm³ (240 candidate pairs). |
| Neck sweep | Every 2.5° from −65° to +27.5° (38 poses), all parts of the neck, head pitch, head yaw, head roll and mouth links against every other part: no overlap above 0.1 mm³. Forward-roll tuck (neck −65°, head pitch ±57°): clear. Head yaw and roll were at zero. |
| Publication changes | TorsoFront −1072 mm³, trunk −331 mm³ (including a detached 50.7 mm³ deck sliver removed), neck link −24 mm³. All one solid each. Details in `validation/R25-fixes.json`. |
| STEP exports | All 51 reopened as valid single solids. Volume drift below 10 ppm except four mirrored right-side parts: ShankStructure_R 399 ppm (4.4 mm³), ShinCap_R 178 ppm, ToeCap_R 72 ppm, ThighCap_R 55 ppm. Assembly STEP valid, 161 solids. |
| STL exports | All 51 read back closed. JawSurround_L read back open at a near-degenerate spot and was repaired (duplicate points, degenerate facets, non-manifold edges, hole fill), then re-verified. Largest STL volume difference 0.31 %. Details in `validation/R25-export-readback.json`. |
| Head base replacement | `A_HeadBase` (IndieDuck-drawn) replaces the XGO-derived `A_O2_HeadBase`: one valid solid, 34,078 mm³ (was 31,373), 586 faces (was 5,336 triangulated faces). No overlap above 0.1 mm³ with any part; clear through head roll ±25°, head yaw ±90° at roll −25°/0°/+25°, jaw 0° to 30° and neck −65° to +27.5°. Screw holes through the floor keep 94 to 97 % material in a 4 mm ring. STEP drift 0 ppm, STL closed. Slices flat, no supports, no warnings. `validation/R25-headbase-replacement.json`. |
| Faceted surfaces | No part contains tessellated geometry (test: three-sided planar faces sharing an edge with another such face). AngularJaw rebuilt exact: pivot hubs, bores, horn holes, plate edges and lower plate corners (532 triangular faces to 4 genuine chamfer-corner faces, volume within 0.06 %). JawSurround_L pins exact (177 to 0). Head base rebuilt against the clean jaw (no tessellation). HeadRim_L/R keep their deliberate low-poly bevels. Clearances re-checked. `validation/R25-face-cleanup.json`. |
| Support parts | Jaw bearing tower, keeper and plug, and neck bearing retainer exported and added to `COMPONENTS.csv` (55 printed parts): each a valid single solid, STEP drift 0 ppm, STL closed, no tessellated faces. |
| Joint ranges | Swept every joint in 1 deg steps with all parts present; three mislabelled hardware objects corrected; covers trimmed; all leg joints and the neck verified clear across the new ranges. See README and `validation/R25-joint-ranges.json`. |
| Roll-servo cradle | Changed between R20 and R25 without being listed in the R25 candidate: +96 mm³ and 2 mm further back (x −8.9 vs −6.9). Covered by the static and sweep checks above. |
| Slicing | Bambu Studio 2.08.02.61 CLI, P2S 0.4 mm, 0.20 mm, 3 walls, 20 % infill: 39 parts on seven plates sliced with no warnings, each plate's G-code object count checked against its part count. HelmetLower only in its upside-down orientation. |

Not verified: physical fit, fastener engagement, strength of added mounts, combined head motion, leg motion with the new covers, jaw motion, cables, mass and balance, any gait.

R20 verification records are available at the tag `r20-simulation-study-v1`.
