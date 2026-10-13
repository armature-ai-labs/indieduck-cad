# Third-party notices and source attribution

IndieDuck by Armature AI Labs, adapted from Open Duck Mini and inspired by Pollen Robotics' MicroDuck.

Copyright 2026 Armature AI Labs for our engineering modifications. Our independently authored contributions and documentation are offered under Apache-2.0, whose text is included below. This grant does not extend to underlying third-party geometry or replace its source-specific terms. This R25 CAD study combines separately authored structure and interfaces, project-lineage material, and our changes. It is not covered by a single blanket Apache-2.0 grant. The retained upstream texts below apply to their respective material; public availability does not supply any missing upstream permission. No sponsorship, endorsement or trademark rights are asserted.

## Source scope

| Source | Pinned revision | Included or referenced material | Recorded terms |
| --- | --- | --- | --- |
| [Open Duck Mini](https://github.com/apirrone/Open_Duck_Mini) by Antoine Pirrone and contributors | `b23317a485b3cec7d8417f352478778b3475173c` | Project basis and design lineage; Jaime Machuca's BD-X-style body-cover mod and Justin Andrews' Park Head mod are credited below as part of that lineage. | Apache-2.0, text retained below. |
| [MicroDuck / microduck_rl](https://github.com/pollen-robotics/microduck_rl) by Pollen Robotics | model reference `273afe0b31c4ab365b9ff806a927b63ac92b5ddd` | Robot inspiration and numerical joint, stance, foot and roller references. No original Pollen mesh files or policies are directly bundled. | Pinned repository distinguishes Apache-2.0 software from its model terms. Software permission is not asserted as a CAD grant. |
| Radxa ZERO 3W and Pollen RPI Robot HAT | Radxa V1.11 mechanical reference; HAT `78f60f711f519e8b57c4b1ea937bd2bb8249b1d3` | Numerical outline, mounting and component-envelope facts represented as reference shapes. | Original Radxa CAD and the HAT STEP's embedded Raspberry Pi model are not included. |
| Feetech HD-1910-C001 documentation | drawing/specification referenced in the project source register | Numerical servo interfaces and simplified hardware reference envelopes. | Manufacturer documentation is not relabelled as IndieDuck CAD. |

Armature contributions include the HD-1910 structure and interface features, compact joint supports, the R25 exterior and the R25 head base. An independently authored modification does not relicense any underlying third-party material.

**R25 and earlier releases (13 October 2026).** The current R25 robot (`native/robot/IndieDuck_R25_Assembly.FCStd`, `native/robot/IndieDuck_R25_HeadBase.FCStd` and `exports/R25/`) contains no geometry imported from XGO-Duck. Its head base, the last XGO-derived part, was replaced by an Armature-drawn part. R20 and earlier files, which did contain XGO-Duck geometry, have been removed from this branch; they remain available, with their own notices, at the tag `r20-simulation-study-v1`. Those notices are not repeated here because no current file depends on them.

For the active part-to-native-object mapping and material classification, use the package manifest. STEP/STL files inherit the provenance of their corresponding native objects. Assembly and review files combine those objects and do not broaden their permissions.

## Preserved contributor attribution

The following contributor README texts are reproduced verbatim from the pinned Open Duck Mini snapshot. Image links and references inside them describe the original upstream package, not files or verified print settings in this release.

### Jaime Machuca (jmachuca77)

```text
# Jaime's V2 BD‑X Style Body Covers Mod

![3D Model Overview](./3D%20Model.png)

Author: Jaime Machuca (jmachuca77)

## Purpose
This is an alternative set of v2 body/head cover parts for Open Duck Mini intended to more closely match the Disney BD‑X aesthetic and surface "skin" lines.

## Important Note on Balance & RL Policy
These covers shift the overall mass distribution and do not perfectly match the original center of gravity assumptions used when training the current reinforcement learning (RL) locomotion policy. The existing policy still works, but may exhibit slightly reduced stability (e.g. more wobble, occasional recovery steps). Monitor performance; if instability becomes an issue, consider fine‑tuning or retraining with updated inertial parameters.

## Printing Guidance
The file `Bambu_X1C_Project_File.3mf` contains suggested part orientations, plate groupings, and baseline settings optimized for a Bambu Labs X1C printer.

Recommended starting points (adjust to your material):
- Material: PETG or PLA-CF (for durability)
- Layer Height: 0.20 mm (features) / 0.28 mm (large flat shells optional)
- Infill: 15–20% gyroid or cubic
- Walls: 3 perimeters for strength on structural covers
- Supports: Only where unavoidable (check project file flags)
- Adhesion: Skirt or minimal brim for tall narrow pieces

![Print Orientation Reference](./Print%20Orientation%20Reference.png)

## Included Parts
Representative filenames (see folder for full list):
- Front/Back/Side body covers (`Front Cover.3mf`, `Back Panel.3mf`, `trunk_*`) 
- Leg covers and cable guides (`Left Leg Cover.3mf`, `Right Leg Cover.3mf`, upper/lower guides) 
- Greebles & panels (`Front Greeble.3mf`, `Front Panel V4.3mf`) 
- Safety / accessory plates (`E-Stop Panel.3mf`, `E-Stop Adapter Plate.3mf`) 
- Assembly helpers (`Hip Cable Holder.3mf`, `Top Body Support.3mf`)

## Usage & Attribution
Feel free to remix or adapt. Please retain attribution to Jaime Machuca (jmachuca77) and reference that this mod targets a closer Disney BD‑X visual style.

## Future Suggestions
- Retrain or fine‑tune RL policy with updated CAD mass properties.

---
If you encounter issues or improved orientations, open a PR or add notes here.
```

### Justin Andrews (Codezombie23)

```text
# Justin's Park Head Mod (BD‑X Style)

This mod updates the Open Duck Mini v2 head to more closely resemble the Disney BD‑X design.

![Park Head Mod Preview](./Park_Head.png)

- Author: Justin Andrews (Codezombie23)
- Project: Open Duck Mini v2 head mod

If you use or remix this, please credit the author above.
```

## Apache License 2.0 text for the Open Duck Mini material and separately designated Armature material

```text
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```


## Native source mapping

`native/robot/IndieDuck_R25_Assembly.FCStd` holds the complete R25 robot as solids, each with a `MovingBody` property naming its joint link. `native/robot/IndieDuck_R25_HeadBase.FCStd` is the head base as an editable PartDesign body. `COMPONENTS.csv` maps every printed part to its native object, material and exports. Retained R17 and R18 Armature support and interface parts keep their original identifiers.

## Active printable classification

Initial rigid fit tests: PLA. Soft soles: TPU 95A. The camera lens and other bought hardware are reference geometry. Exclude all `A_ref_*` items and purchased hardware from printable-part exports. All material choices remain prototype choices, not strength or print certification.

## Attribution scope

Open Duck Mini project lineage includes Antoine Pirrone and contributors, Jaime Machuca's BD-X-style cover mod, and Justin Andrews' Park Head mod. Credit remains even when an older source feature is hidden. Pollen Robotics' MicroDuck supplies inspiration and numerical references. Read THIRD_PARTY_NOTICES.md for the pinned records and preserved notices.
