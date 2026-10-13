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
| Roll-servo cradle | Changed between R20 and R25 without being listed in the R25 candidate: +96 mm³ and 2 mm further back (x −8.9 vs −6.9). Covered by the static and sweep checks above. |
| Slicing | Bambu Studio 2.08.02.61 CLI, P2S 0.4 mm, 0.20 mm, 3 walls, 20 % infill: 39 parts on seven plates sliced with no warnings, each plate's G-code object count checked against its part count. HelmetLower only in its upside-down orientation. |

Not verified: physical fit, fastener engagement, strength of added mounts, combined head motion, leg motion with the new covers, jaw motion, cables, mass and balance, any gait.

# R20 CAD verification (previous release)

This release combines the complete saved robot assembly and 41 current printed-component candidates in one R20 CAD package. Verification concerns this digital package. It does not establish a physically buildable or motion-qualified robot.

## Recorded checks

| Check | Evidence and scope |
|---|---|
| Isolated native reopening | PASS in the recorded copied-folder check. The original project was inaccessible. All dependencies resolved within the four packaged sibling FreeCAD documents. The assembly contained 135 links, with 124 visible. |
| Active geometry | The isolated check reported no active-shape failures. Native construction history remains present, including 29 thigh features, 17 neck features, 20 head-pitch base features and 29 band profile sections. Presence of that history is not a full parameter-change/recompute certification. |
| Head-yaw control | The assembled band followed the yaw group at -90°, 0° and +90°. Recorded point errors were below 0.000001 mm. This tests the CAD transform, not servo travel or cable freedom. |
| Added-band clearance | Exact overlap was 0 mm³ against the modified shell, head-roll servo reference, roll cradle and head-module fastener references. For pure vertical yaw at the tested base pose, invariant Z bounds separated the band from all 87 fixed parts by at least 9.2135 mm. This does not certify combined pitch/roll movement or removal travel. |
| STEP exports | All 41 individual STEP exports reopened as valid single solids. Maximum recorded volume drift from native geometry was 7.937 ppm. The assembled STEP used 124 visible assembly objects. |
| Initial STL export generation | The export-generation record reports closed meshes for all 41 parts. Independent saved-file readback and mesh precision are reported separately below. |

The new band checks supplement the inherited R19 rigid pure-yaw work. They do not extend that work to combined-joint trajectories, cable deformation or physical hardware.

## Saved-file and display checks

- All 41 saved STLs reopened as closed meshes. Forty had volume differences below 2% against the native CAD. The band's refined 49,552-facet STL is closed, consistently oriented, manifold and has no detected self-intersections. Its volume still differs by approximately 2.26% from the BRep value. Finer tessellation did not remove this discrepancy; its cause remains unresolved. This is not a band precision pass.
- The complete STEP reopens as a valid shape. Its volume differs by approximately 0.05275% from the sum of visible native shapes, above the initial 100 ppm comparison threshold. This numerical discrepancy is retained in `validation/export-readback.json`; no mass-property equivalence is claimed.
- A separate GUI reopen confirmed both leg structures, attached band and retained colours. Hidden Body final features were restored in the staged copies. Colours are stored on source parts to survive link reopening. Temporary diagnostic shapes were removed.
- `MANIFEST.json` records revision, role, size and SHA-256 for the packaged payload; `SHA256SUMS` also covers that manifest. Neither checksum file claims to hash itself.
- Post-publication anonymous download and reopen results are recorded in the release's separate verification asset. Keeping that receipt outside the ZIP avoids changing the archive after verification.

## Physical and manufacturing limits

No new slicing or printer job is included. STL files are in millimetres in their native CAD frames, without approved print orientation, support settings or printer-specific profiles. Initial rigid fit-test material is PLA; soles and lips are TPU 95A.

Inherited neck-motion collisions remain unresolved. Physical fit, structural strength, impact resistance, bearing preload, fastener engagement, continuous combined-joint motion, gait and dynamic cable routing are unverified. Drawings in this package are bounded review sheets, not a complete manufacturing drawing set.

The band's two screws, washers and captive nuts are not explicitly modelled in the assembly. Their provisional candidate is M2×10 with a nominal 0.5 mm washer, leaving approximately 0.492 mm screw-tip space in the centre-line CAD stack. Without the washer, the nominal screw reaches the blind end. Actual nut dimensions, printed fit, screw-head seating, screw length and driver access require a fit test. Shell removal is required for access, and full band-removal travel remains unchecked.

Source identity and licence status are recorded separately in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Geometry checks do not resolve source rights.

## R20 browser assembly bundle, 09-10-2026

Added 124 CAD display-reference meshes, including the same 41 printable candidates, with assembled coordinates and source identities. All mesh checksums match their generated manifest. The display bundle has 128,318 triangles and is not a manufacturing export. The original four native documents and 41 print STEP/STL pairs are unchanged from `cad-study-2026-10-09`.

Additional band screw, washer and nut records are labelled provisional presentation envelopes, separate from the 124 native references. They express the recorded two mounting axes and candidate stack; no manufacturer geometry, physical fastener fit or insertion clearance is certified.

The Three.js guide and physics simulator are separate tools. Browser assembly separation does not validate continuous insertion paths, structural loads or wired joint travel.
