"""Verify an IndieDuck edition against platform P1.

Run from the indieduck-cad repository root with FreeCAD's command-line interpreter:

    EDITION=<id> freecadcmd tools/edition_verify.py

Options (environment variables): STEP_DEG (sweep step, default 2), JOINTS (comma-separated joint
names, default all), SKIP_SWEEPS=1 (paperwork, platform, part and standing-pose checks only).

Checks: edition.yaml and COMPONENTS.csv; platform parts unchanged against platform/exports; every
edition part a single valid solid with a valid MovingBody and matching STEP/STL exports; no overlap at
the standing pose; each joint's clear range from the standing pose compared with platform P1's verified
range. Contact means an overlap above 0.5 mm3 involving at least one edition part. Writes
editions/<id>/validation/edition-verify.json and prints CHECK lines and a final RESULT line.
"""
import FreeCAD as A, Part, Mesh, csv, json, math, os, re, time
V = A.Vector
ROOT = os.getcwd()
ED = os.environ.get('EDITION', '').strip()
STEP = float(os.environ.get('STEP_DEG', '2'))
ONLY = [j for j in os.environ.get('JOINTS', '').split(',') if j]
SKIP_SWEEPS = os.environ.get('SKIP_SWEEPS') == '1'
OVERLAP = 0.5
report = {'edition': ED, 'date': time.strftime('%Y-%m-%d'), 'step_deg': STEP, 'checks': {}, 'joints': {}}
problems, notes = [], []

def check(name, ok, detail):
    report['checks'][name] = {'ok': ok, 'detail': detail}
    print(f"\nCHECK {'PASS' if ok else 'FAIL'} {name}: {detail}", flush=True)
    if not ok: problems.append(name)

def load_yaml_top(path):
    out = {}
    for line in open(path):
        m = re.match(r'^([a-z_]+):\s*(.*?)\s*(#.*)?$', line)
        if m: out[m.group(1)] = m.group(2)
    return out

# 1. paperwork
edir = os.path.join(ROOT, 'editions', ED)
if not ED or not os.path.isdir(edir):
    print(f'\nRESULT FAIL no edition folder editions/{ED}', flush=True); raise SystemExit
y = load_yaml_top(os.path.join(edir, 'edition.yaml')) if os.path.isfile(os.path.join(edir, 'edition.yaml')) else {}
need = ['id', 'name', 'form_factor', 'platform', 'licence', 'maturity', 'native_assembly']
missing = [k for k in need if not y.get(k)] + ([] if 'designers' in y else ['designers'])
check('edition.yaml', not missing and y.get('id') == ED and y.get('form_factor') == 'duck' and y.get('platform') == 'P1' and y.get('licence') == 'Apache-2.0',
      f"missing {missing}" if missing else f"id {y.get('id')}, form_factor {y.get('form_factor')}, platform {y.get('platform')}, licence {y.get('licence')}")
K = json.load(open(os.path.join(ROOT, 'platform', 'P1-kinematics.json')))
BODIES = set(K['bodies'])
rows = list(csv.DictReader(open(os.path.join(ROOT, 'COMPONENTS.csv'))))
erows = [r for r in rows if r.get('scope') == 'edition' and r.get('edition') == ED]
prows = [r for r in rows if r.get('scope') == 'platform']
badpaths = [r[k] for r in erows for k in ('step', 'stl') if not os.path.isfile(os.path.join(ROOT, r[k]))]
check('COMPONENTS.csv', bool(erows) and not badpaths, f"{len(erows)} edition parts, {len(prows)} platform parts; missing exports: {badpaths[:5]}")

# 2. open the edition assembly
native = os.path.join(edir, y.get('native_assembly', ''))
doc = A.openDocument(native)
objs = {o.Label: o for o in doc.Objects if hasattr(o, 'Shape') and not o.Shape.isNull()}

# 3. platform parts unchanged
changed = []
for r in prows:
    o = objs.get(r['assembly_link'])
    if o is None: changed.append((r['assembly_link'], 'missing')); continue
    ref = Part.read(os.path.join(ROOT, r['step'])); s = o.Shape
    dv = abs(ref.Volume - s.Volume) / max(ref.Volume, 1e-9)
    bb, rb = s.BoundBox, ref.BoundBox
    db = max(abs(a - b) for a, b in zip((bb.XMin, bb.XMax, bb.YMin, bb.YMax, bb.ZMin, bb.ZMax), (rb.XMin, rb.XMax, rb.YMin, rb.YMax, rb.ZMin, rb.ZMax)))
    if dv > 1e-3 or db > 0.05: changed.append((r['assembly_link'], f'volume {dv*100:.3f} %, bounds {db:.3f} mm'))
check('platform unchanged', not changed, f"{len(prows)} platform parts compared with platform/exports; changed: {changed[:5]}")

# 4. edition parts
partprob = []
for r in erows:
    o = objs.get(r['assembly_link'])
    if o is None: partprob.append((r['assembly_link'], 'not in assembly')); continue
    s = o.Shape; mb = getattr(o, 'MovingBody', '')
    if mb not in BODIES: partprob.append((r['assembly_link'], f'MovingBody "{mb}"'))
    if not s.isValid() or len(s.Solids) != 1: partprob.append((r['assembly_link'], f'valid {s.isValid()}, solids {len(s.Solids)}'))
    st = Part.read(os.path.join(ROOT, r['step']))
    if abs(st.Volume - s.Volume) / s.Volume > 5e-4: partprob.append((r['assembly_link'], 'STEP volume differs'))
    m = Mesh.Mesh(os.path.join(ROOT, r['stl']))
    if not m.isSolid() or abs(m.Volume - s.Volume) / s.Volume > 0.01: partprob.append((r['assembly_link'], 'STL not closed or volume differs'))
check('edition parts', not partprob, f"{len(erows)} parts checked; problems: {partprob[:6]}")

# kinematics (world frames at the standing pose, as the assemblies are saved)
import numpy as np
J = {j['name']: j for j in K['joints']}
orig = {'trunk_base': np.array(K['root_origin_mm'], float)}
world = {'trunk_base': np.eye(4)}; world['trunk_base'][:3, 3] = np.array(K['standing_pose']['base_position_mm'], float)
for j in K['joints']:
    o = np.array(j['origin_mm'], float); orig[j['body']] = o; v = np.array(j['axis'], float)
    ang = math.radians(K['standing_pose']['joint_deg'][j['name']])
    kx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]]); r = np.eye(3) + math.sin(ang) * kx + (1 - math.cos(ang)) * (kx @ kx)
    t = np.eye(4); t[:3, :3] = r; t[:3, 3] = o - orig[j['parent_body']]; world[j['body']] = world[j['parent_body']] @ t
children = {}
for j in K['joints']: children.setdefault(j['parent_body'], []).append(j['body'])
def subtree(b):
    out = {b}
    for c in children.get(b, []): out |= subtree(c)
    return out
def axis_world(name):
    j = J[name]; T = world[j['body']]
    return V(*T[:3, 3]), V(*(world[j['parent_body']][:3, :3] @ np.array(j['axis'], float)))
IGNORE = [x for x in os.environ.get('IGNORE', 'Fasteners').split(',') if x]  # reference fastener envelopes sit inside the holes they fill
moving = [o for o in objs.values() if getattr(o, 'MovingBody', '') in BODIES and not any(k in o.Label for k in IGNORE)]
edset = {r['assembly_link'] for r in erows} | {x for x in os.environ.get('EXTRA', '').split(',') if x}
def contacts(mov, fix, rot=None):
    hits = []
    for o in mov:
        s = o.Shape
        if rot: s = s.copy(); s.rotate(*rot)
        bb = s.BoundBox
        for f in fix:
            if o.Label not in edset and f.Label not in edset: continue
            if not bb.intersect(f.Shape.BoundBox): continue
            v = s.common(f.Shape).Volume
            if v > OVERLAP: hits.append((o.Label, f.Label, round(v, 1)))
    return hits

# 5. standing pose
st_hits = []
eds = [o for o in moving if o.Label in edset]
for a in eds:
    for b in moving:
        if b is a or (b.Label in edset and b.Label < a.Label): continue
        if a.Shape.BoundBox.intersect(b.Shape.BoundBox):
            v = a.Shape.common(b.Shape).Volume
            if v > OVERLAP: st_hits.append((a.Label, b.Label, round(v, 1)))
check('standing pose', not st_hits, f"overlaps above {OVERLAP} mm3: {st_hits[:6]}")

# 6. joint sweeps
reduced = []
if not SKIP_SWEEPS:
    t0 = time.time()
    for name in (ONLY or [j['name'] for j in K['joints']]):
        j = J[name]; lo, hi = j['verified_range_deg']; q0 = K['standing_pose']['joint_deg'][name]
        sub = subtree(j['body']); mov = [o for o in moving if o.MovingBody in sub]; fix = [o for o in moving if o.MovingBody not in sub]
        pt, ax = axis_world(name); res = {'verified_range_deg': [lo, hi], 'standing_deg': q0}
        for sgn, lim, key in ((-1, lo, 'down'), (1, hi, 'up')):
            q = q0; by = None
            while True:
                qn = q + sgn * STEP
                if (sgn < 0 and qn < lim) or (sgn > 0 and qn > lim):
                    if abs(q - lim) > 1e-6:
                        h = contacts(mov, fix, (pt, ax, lim - q0))
                        if not h: q = lim
                        else: by = sorted(h, key=lambda x: -x[2])[:2]
                    break
                h = contacts(mov, fix, (pt, ax, qn - q0))
                if h: by = sorted(h, key=lambda x: -x[2])[:2]; break
                q = qn
            res[key] = round(q, 2); res[key + '_blocked_by'] = by
        full = abs(res['down'] - lo) < 1e-6 and abs(res['up'] - hi) < 1e-6
        res['full_range'] = full; report['joints'][name] = res
        if not full: reduced.append(name)
        print(f"\nJOINT {'FULL' if full else 'REDUCED'} {name}: clear {res['down']} to {res['up']} deg (P1 verified {lo} to {hi}); blocked by {res['down_blocked_by'] or '-'} / {res['up_blocked_by'] or '-'} [{round(time.time()-t0)} s]", flush=True)
    check('joint ranges', not reduced, f"{len(report['joints'])} joints swept in {STEP} deg steps; reduced: {reduced}")
else:
    notes.append('joint sweeps skipped')

report['result'] = 'PASS' if not problems else 'ATTENTION' if problems == ['joint ranges'] else 'FAIL'
report['problems'] = problems; report['notes'] = notes
os.makedirs(os.path.join(edir, 'validation'), exist_ok=True)
json.dump(report, open(os.path.join(edir, 'validation', 'edition-verify.json'), 'w'), indent=1, default=str)
print(f"\nRESULT {report['result']} edition {ED}: {len(problems)} problem(s) {problems}; report editions/{ED}/validation/edition-verify.json", flush=True)
