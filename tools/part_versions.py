#!/usr/bin/env python3
"""Part versions for IndieDuck printed parts.

Every printed part in COMPONENTS.csv has a revision (part_rev). A part's revision goes up whenever
its geometry changes. PART-VERSIONS.json records each part's revision, its geometric fingerprint and
its history; PARTS-CHANGELOG.md is the public report of what changed and what to reprint.

Commands (run from the repository root; Python 3 only, no other dependencies):
  python3 tools/part_versions.py check                  fail if any part's geometry changed without a revision bump
  python3 tools/part_versions.py update --note "why"    bump every changed part, record why, rebuild the report
  python3 tools/part_versions.py release NAME           record a release (for example cyber-edition-v2) and rebuild the report
  python3 tools/part_versions.py report                 rebuild PARTS-CHANGELOG.md and the part_rev column

The fingerprint comes from the part's STL geometry (volume, surface area, bounding box and centre of mass),
so renaming a file or re-exporting unchanged geometry is not a change.
"""
import csv, io, json, os, struct, subprocess, sys, datetime

ROOT = os.getcwd()
VERS = os.path.join(ROOT, 'PART-VERSIONS.json')
REPORT = os.path.join(ROOT, 'PARTS-CHANGELOG.md')
COMP = os.path.join(ROOT, 'COMPONENTS.csv')


def stl_fingerprint(data):
    tris = []
    if data[:5].lower() == b'solid' and b'facet' in data[:2048]:
        pts = []
        for line in data.decode('utf-8', 'replace').splitlines():
            t = line.split()
            if t and t[0] == 'vertex':
                pts.append(tuple(float(x) for x in t[1:4]))
        tris = [pts[i:i + 3] for i in range(0, len(pts) - 2, 3)]
    else:
        n = struct.unpack('<I', data[80:84])[0]
        for i in range(n):
            o = 84 + i * 50
            v = struct.unpack('<12f', data[o:o + 48])
            tris.append((v[3:6], v[6:9], v[9:12]))
    vol = area = 0.0
    cx_ = cy_ = cz_ = 0.0
    lo = [1e9] * 3; hi = [-1e9] * 3
    for a, b, c in tris:
        dv = (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0])) / 6.0
        vol += dv
        cx_ += dv * (a[0] + b[0] + c[0]) / 4.0; cy_ += dv * (a[1] + b[1] + c[1]) / 4.0; cz_ += dv * (a[2] + b[2] + c[2]) / 4.0
        ux, uy, uz = b[0] - a[0], b[1] - a[1], b[2] - a[2]
        vx, vy, vz = c[0] - a[0], c[1] - a[1], c[2] - a[2]
        nx, ny, nz = uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx
        area += 0.5 * (nx * nx + ny * ny + nz * nz) ** 0.5
        for q in (a, b, c):
            for k in range(3):
                lo[k] = min(lo[k], q[k]); hi[k] = max(hi[k], q[k])
    # volume, area, bounding box and centre of mass: a moved or filled hole shifts the centre of mass
    # measurably, while re-meshing the same shape does not
    return {'volume_mm3': round(abs(vol), 1), 'area_mm2': round(area, 1),
            'bbox_mm': [round(x, 2) for x in lo + hi],
            'centroid_mm': [round(x / vol, 3) for x in (cx_, cy_, cz_)] if vol else [0, 0, 0]}


def same(a, b):
    if a is None or b is None or 'centroid_mm' not in b:
        return False
    if abs(a['volume_mm3'] - b['volume_mm3']) > max(1.0, 0.0005 * b['volume_mm3']):
        return False
    if abs(a['area_mm2'] - b['area_mm2']) > max(2.0, 0.001 * b['area_mm2']):
        return False
    if any(abs(x - y) > 0.1 for x, y in zip(a['bbox_mm'], b['bbox_mm'])):
        return False
    return all(abs(x - y) <= 0.02 for x, y in zip(a['centroid_mm'], b['centroid_mm']))


def components():
    raw = open(COMP, encoding='utf-8', newline='').read()
    nl = '\r\n' if '\r\n' in raw else '\n'
    rows = list(csv.DictReader(io.StringIO(raw, newline='')))
    return rows, nl


def current_parts():
    rows, _ = components()
    return {r['assembly_link']: r for r in rows if r.get('revision') == 'R25'}


def load():
    if os.path.exists(VERS):
        return json.load(open(VERS, encoding='utf-8'))
    return {'parts': {}, 'releases': []}


def save(v):
    json.dump(v, open(VERS, 'w', encoding='utf-8'), indent=1, sort_keys=True)
    open(VERS, 'a').write('\n')


def changed_parts(v):
    out = []
    for name, r in current_parts().items():
        fp = stl_fingerprint(open(os.path.join(ROOT, r['stl']), 'rb').read())
        rec = v['parts'].get(name)
        if rec is None or not same(fp, rec['fingerprint']):
            out.append((name, fp))
    return out


def write_rev_column(v):
    rows, nl = components()
    fields = list(rows[0].keys())
    if 'part_rev' not in fields:
        fields.append('part_rev')
    for r in rows:
        p = v['parts'].get(r['assembly_link'])
        r['part_rev'] = ('r%d' % p['rev']) if (p and r.get('revision') == 'R25') else r.get('part_rev', '')
    buf = io.StringIO(newline='')
    w = csv.DictWriter(buf, fieldnames=fields, lineterminator=nl)
    w.writeheader(); w.writerows(rows)
    open(COMP, 'w', encoding='utf-8', newline='').write(buf.getvalue())


def rev_at(part, release):
    return release['parts'].get(part)


def report(v):
    parts = current_parts()
    L = ['# What changed in the printed parts', '',
         'Every printed IndieDuck part has a revision (r1, r2, ...). A part\'s revision goes up whenever its shape changes; a print of an older revision may not fit the newer parts around it. This page is generated by `tools/part_versions.py` from `PART-VERSIONS.json`; the revision of each part is also in the `part_rev` column of `COMPONENTS.csv`.', '',
         '## What to reprint', '',
         'Find the release you printed from (the tag, or the date you downloaded or sliced the files). Reprint the parts listed for it.', '']
    for rel in reversed(v['releases']):
        stale = [(n, rel['parts'].get(n), v['parts'][n]['rev']) for n in sorted(parts) if n in v['parts'] and (rel['parts'].get(n) or 0) < v['parts'][n]['rev']]
        L.append('### Printed from %s (%s)' % (rel['name'], rel['date']))
        L.append('')
        if not stale:
            L.append('Nothing to reprint: every part is current.')
        else:
            L.append('Reprint %d of %d parts:' % (len(stale), len(parts)))
            L.append('')
            L.append('| Part | You have | Current | Changed because |')
            L.append('|---|---|---|---|')
            for n, old, new in stale:
                reasons = [h['note'] for h in v['parts'][n]['history'] if h['rev'] > (old or 0)]
                L.append('| %s | %s | r%d | %s |' % (n, ('r%d' % old) if old else 'not in that release', new, '; '.join(dict.fromkeys(reasons))))
        L.append('')
    L += ['## Every part', '', '| Part | Scope | Current | History |', '|---|---|---|---|']
    for n in sorted(parts, key=lambda x: (parts[x].get('scope', ''), x)):
        p = v['parts'].get(n)
        if not p:
            continue
        hist = '<br>'.join('r%d, %s: %s' % (h['rev'], h['date'], h['note']) for h in p['history'])
        L.append('| %s | %s | r%d | %s |' % (n, parts[n].get('scope', ''), p['rev'], hist))
    L.append('')
    open(REPORT, 'w', encoding='utf-8').write('\n'.join(L))
    write_rev_column(v)


def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    cmd = sys.argv[1]; v = load()
    if cmd == 'check':
        ch = changed_parts(v)
        missing = [n for n in current_parts() if n not in v['parts']]
        if ch or missing:
            print('Part geometry changed without a revision bump: %s' % ', '.join(sorted(set([c[0] for c in ch] + missing))))
            print('Run: python3 tools/part_versions.py update --note "what changed and why"')
            return 1
        print('PASS: %d printed parts, every revision matches its geometry' % len(current_parts()))
        return 0
    if cmd == 'update':
        if '--note' not in sys.argv:
            print('update needs --note "what changed and why"'); return 2
        note = sys.argv[sys.argv.index('--note') + 1]
        today = datetime.date.today().isoformat()
        ch = changed_parts(v)
        for name, fp in ch:
            p = v['parts'].setdefault(name, {'rev': 0, 'history': []})
            p['rev'] += 1; p['fingerprint'] = fp
            p['history'].append({'rev': p['rev'], 'date': today, 'note': note})
            print('%s -> r%d' % (name, p['rev']))
        save(v); report(v)
        print('%d parts bumped; report rebuilt' % len(ch)); return 0
    if cmd == 'release':
        name = sys.argv[2]
        v['releases'] = [r for r in v['releases'] if r['name'] != name]
        v['releases'].append({'name': name, 'date': datetime.date.today().isoformat(), 'parts': {n: p['rev'] for n, p in v['parts'].items()}})
        save(v); report(v); print('release %s recorded' % name); return 0
    if cmd == 'report':
        report(v); return 0
    print(__doc__); return 2


if __name__ == '__main__':
    sys.exit(main())
