# R20 CAD assembly display assets

Generated from the complete native R20 assembly at CAD commit `7bcdd1696516f9cff6bdefbc34e42f259c87749a`. The browser guide source lives in [indieduck](https://github.com/armature-ai-labs/indieduck/tree/main/assembly-guide).

`manifest.json` identifies 124 visible CAD component references, including 41 current printed components. Some hardware references are compound shapes, so 124 is not a physical procurement quantity. Meshes retain assembled CAD coordinates in millimetres: X forward, Y left, Z up, with the R12 natural standing pose. No mesh is centred independently.

These lightweight presentation meshes total 128,318 triangles. Their 0.15 mm linear / 0.35 rad angular tessellation settings differ from the manufacturing exports. Do not print this directory. Use `exports/R20/` and the native sources for mechanical work. Per-mesh SHA-256 values are in the manifest.

Colours describe saved CAD appearance, not measured material properties. Purchased references and unresolved dimensions remain provisional. Source-specific terms in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) apply to these derivatives too.

Regeneration uses `tools/export_r20_cad.py` in the matching [RL release](https://github.com/armature-ai-labs/indieduck-rl/releases/tag/r20-simulation-study-v1), under FreeCAD with NumPy available. Set `INDIEDUCK_CAD` to this repository and `INDIEDUCK_ASSETS` to a separate output directory. The script reads native geometry without saving changes. Its explicit component/body mapping fails if a component is unmapped.

The browser guide adds separately labelled provisional assembly markers. Those are not native CAD additions and must not be mistaken for verified hardware.
