# IndieDuck platform P1

P1 is the mechanism every IndieDuck edition shares: the structure, joints, actuators, electronics, feet and soles. A change to the platform applies to every edition and gets a new platform version. The full contents of each platform version (mechanism, electronics and sensors) and its history are in the project hub: [platform/P1.yaml](https://github.com/armature-ai-labs/indieduck/blob/main/platform/P1.yaml) and [PLATFORM-CHANGELOG.md](https://github.com/armature-ai-labs/indieduck/blob/main/platform/PLATFORM-CHANGELOG.md).

## What P1 includes

- **Printed parts (27):** trunk, neck, head base, head pitch and yaw brackets, hip yaw and roll supports, thighs, shank structures, feet and soles, the roll and mouth servo cradles and keepers, the jaw bearing tower, keeper and plug, the neck bearing retainer, and the camera carrier. `COMPONENTS.csv` rows with `scope = platform`; exports in `platform/exports/`.
- **Actuators:** 15 Feetech HD-1910 servos on a regulated 5.0 V rail (hip yaw, roll, pitch, knee and ankle per leg; neck pitch; head pitch, yaw and roll; mouth).
- **Electronics:** Radxa Zero 3W, Pollen Robot HAT rev D1 (body IMU on board), head IMU, one camera, time-of-flight sensor. Full list in the project hub's `BOM.md`.
- **Editable source:** the head base, `platform/native/IndieDuck_P1_HeadBase.FCStd`. The other platform parts are solids inside each edition's assembly (Cyber: `editions/cyber/native/IndieDuck_Cyber_Assembly.FCStd`).

## Rules for an edition

An edition is a duck form factor on P1 that changes only the exterior.

1. **Leave platform parts unchanged.** Mechanism changes go to the platform and apply to every edition.
2. **Clear the joints.** Exterior parts must not limit any joint more than the mechanism does, or the edition records its own reduced ranges after a 1 degree sweep (see Cyber's `validation/R25-joint-ranges.json`).
3. **Fix covers with M2 self-tapping screws into printed posts on the platform**, never into a servo or the soft sole. Posts are 5.5 mm across with a 1.7 mm pilot, grow from the platform part that moves with the cover, and need a clear path (no servo, board or other moving part in the way); the cover gets a 2.4 mm hole. A trim piece with no structure behind it prints with the cover or part it sits on (`print_with`), and a panel may hook behind its neighbour, as Cyber's pelvis front does.
4. **The jaw** may be restyled but must use the platform's jaw pivot, bearing and horn interface.
5. **Record mass and centre of mass** of the exterior, because they change the simulation and the trained policies.
6. **Colour accents print with their panel.** IndieDuck is printed on multi-colour printers, so model each colour accent as its own solid sitting exactly on its panel (touching, no gap or overlap), name the panel in the `print_with` column of `COMPONENTS.csv`, and export the panel with its accents as one multi-solid STEP. Accents are never separate pieces fitted by hand.
7. **Licence and credits:** Apache-2.0 for submitted work, designers named in `edition.yaml`, any third-party source listed in `THIRD_PARTY_NOTICES.md`.

Check an edition with `EDITION=<id> freecadcmd tools/edition_verify.py`; it reads the joint chain and verified ranges from `platform/P1-kinematics.json`. How to submit an edition, step by step: [Submit an edition to IndieDuck](https://github.com/armature-ai-labs/indieduck/blob/main/SUBMIT-AN-EDITION.md).

Each edition gets its own model ID (`indieduck-<edition>`), training task and policies.
