# IndieDuck platform P1

P1 is the mechanism every IndieDuck edition shares: the structure, joints, actuators, electronics, feet and soles. A change to P1 applies to every edition and gets a new platform version (P2, ...).

## What P1 includes

- **Printed parts (27):** trunk, neck, head base, head pitch and yaw brackets, hip yaw and roll supports, thighs, shank structures, feet and soles, the roll and mouth servo cradles and keepers, the jaw bearing tower, keeper and plug, the neck bearing retainer, and the camera carrier. `COMPONENTS.csv` rows with `scope = platform`; exports in `platform/exports/`.
- **Actuators:** 15 Feetech HD-1910 servos on a regulated 5.0 V rail (hip yaw, roll, pitch, knee and ankle per leg; neck pitch; head pitch, yaw and roll; mouth).
- **Electronics:** Radxa Zero 3W, Pollen Robot HAT rev D1 (body IMU on board), head IMU, one camera, time-of-flight sensor. Full list in the project hub's `BOM.md`.
- **Editable source:** the head base, `platform/native/IndieDuck_P1_HeadBase.FCStd`. The other platform parts are solids inside each edition's assembly (Cyber: `editions/cyber/native/IndieDuck_Cyber_Assembly.FCStd`).

## Rules for an edition

An edition is a duck form factor on P1 that changes only the exterior.

1. **Leave platform parts unchanged.** Mechanism changes go to the platform and apply to every edition.
2. **Clear the joints.** Exterior parts must not limit any joint more than the mechanism does, or the edition records its own reduced ranges after a 1 degree sweep (see Cyber's `validation/R25-joint-ranges.json`).
3. **Fix covers to the structure**, never to a servo body. Cover fixings on P1 are still being designed; until they are, state the fixing method in the edition.
4. **The jaw** may be restyled but must use the platform's jaw pivot, bearing and horn interface.
5. **Record mass and centre of mass** of the exterior, because they change the simulation and the trained policies.
6. **Licence and credits:** Apache-2.0 for submitted work, designers named in `edition.yaml`, any third-party source listed in `THIRD_PARTY_NOTICES.md`.

How to submit an edition, step by step: [Submit an edition to IndieDuck](https://github.com/armature-ai-labs/indieduck/blob/main/SUBMIT-AN-EDITION.md).

Each edition gets its own model ID (`indieduck-<edition>`), training task and policies.
