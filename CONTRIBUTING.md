# Contributing

**New edition?** Follow [Submit an edition to IndieDuck](https://github.com/armature-ai-labs/indieduck/blob/main/SUBMIT-AN-EDITION.md).

Read `platform/PLATFORM.md` first. Open `editions/cyber/native/IndieDuck_Cyber_Assembly.FCStd` for the complete robot; edit the head base in `platform/native/IndieDuck_P1_HeadBase.FCStd` (driven by its `Params` sheet). Platform changes apply to every edition; exterior changes belong to an edition (`editions/<id>/`, with an `edition.yaml`). Other parts are solids without history, so changes to them are direct solid edits until they are rebuilt as editable features. Keep each part's `MovingBody` property and object label, since the export and simulator tooling depend on them.

For a focused change:

1. Describe the mechanical problem, changed dimensions and affected parts. Preserve established joint centres and servo interfaces unless the change explicitly proposes a new interface revision.
2. Keep editable FreeCAD features, constraints and parameters. Do not replace editable construction history with a mesh-only result. A few surfaces are still faceted (triangulated) B-rep; describe that limitation accurately and prefer rebuilding them as exact features.
3. Recompute, check affected solids and inspect the assembled result. Reopen a copied folder to catch external links. Include matched before/after CAD views and relevant clearance checks, with joint angles and assumptions stated.
4. Regenerate affected STEP and STL exports in millimetres, preserving revision consistency. Record geometry and export checks separately from slicing or physical fit tests. Update the revision/checksum manifest and applicable drawings.
5. Open a pull request with the change, evidence and remaining limitations. Include only relevant native files, exports, drawings and documentation; exclude backups, rejected variants, machine configuration and temporary scripts.

Keep reference electronics and metal hardware distinct from printed parts. Colour changes should not silently change material specifications. For the rear band, check shell fit, nut loading and screw access as well as the exterior appearance.

Preserve upstream notices and source identity. Record any new external geometry, its repository, exact revision and licence in `THIRD_PARTY_NOTICES.md`. A geometric modification does not erase its source attribution or resolve an unclear reuse grant. Do not describe imported geometry as independently authored.

When reporting a test, state what was actually checked. A valid solid, closed STL or clear screenshot alone does not establish strength, tolerances, continuous motion or a working robot. Hardware measurements and failed checks are useful contributions when their setup and uncertainty are recorded.

## Part versions (required for every change to a printed part)

Every printed part has a revision (`part_rev` in `COMPONENTS.csv`), and [PARTS-CHANGELOG.md](PARTS-CHANGELOG.md) tells people who already printed which parts to reprint. When you change a part's geometry and re-export it:

1. Run `python3 tools/part_versions.py update --note "what changed and why"`. It finds every part whose shape changed, bumps its revision, records your note and rebuilds the report.
2. Commit `PART-VERSIONS.json`, `PARTS-CHANGELOG.md` and `COMPONENTS.csv` with your change.

Every new part also needs a unique `part_code` (P for platform, C or your edition's letter for an edition part) and a `location` in `COMPONENTS.csv`; the tool lists it in [PARTS-CATALOG.md](PARTS-CATALOG.md). The `Part versions` check runs on every push and pull request and fails if a part's geometry changed without a new revision, or a part has no code or shares one. Maintainers record each release with `python3 tools/part_versions.py release <name>`.

