#!/usr/bin/env python3
"""Springboard progress grid, read from the files themselves (so it survives any cutoff).

  python3 springboard_status.py                 one line per nation: signs done (of 12)
  python3 springboard_status.py <Nation>        per-sign counts for one nation, and any unfinished files
"""
import os, re, subprocess, sys
DM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = '/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation'
CB = os.path.join(DM, '_dispatch', 'concept_block.py')
SIGNS = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

def expected(n):
    out = subprocess.run([sys.executable, '-I', CB, 'list', str(n)], capture_output=True, text=True).stdout.split('\n')
    return len([l for l in out if l.strip()])          # domain + concepts

EXP = {n: expected(n) for n in range(1, 13)}

def nations():
    res = {}
    for root, dirs, files in os.walk(os.path.join(R, 'Targets')):
        if 'PROGRESS TRACKER.md' in files:
            res[os.path.basename(root)] = root
    return res

def status_of(path):
    try:
        return open(path, encoding='utf-8').readline().strip()
    except OSError:
        return ''

def sign_dir(base, n):
    d = os.path.join(base, 'Springboards')
    if os.path.isdir(d):
        for x in os.listdir(d):
            if x.startswith('%02d - ' % n):
                return os.path.join(d, x)
    return None

def count(base, n):
    d = sign_dir(base, n)
    done = prog = 0
    if d:
        for f in os.listdir(d):
            s = status_of(os.path.join(d, f))
            if s.startswith('STATUS: done'): done += 1
            elif s.startswith('STATUS: in progress'): prog += 1
    return done, prog

N = nations()
master = []
for l in open(os.path.join(R, 'MASTER TRACKER.md'), encoding='utf-8'):
    m = re.match(r'\| (\d+) \| ([^|]+?) \| ', l)
    if m: master.append(m.group(2))
folder = {'Argentina (without Patagonia)': 'Argentina', 'Russia (core state)': 'Russia',
          'Demilitarized Zone (s. Ontario; not a nation)': 'Demilitarized Zone',
          'Sicilia (autonomous zone within Meridia)': 'Sicilia'}
order = [folder.get(x, x) for x in master]

if len(sys.argv) > 1:
    name = sys.argv[1]
    base = N[name]
    for i, s in enumerate(SIGNS, 1):
        d, p = count(base, i)
        print(f'{i:2d} {s:12s} {d:3d}/{EXP[i]} done' + (f', {p} in progress' if p else ''))
    sys.exit()
total = 0
for nm in order:
    if nm not in N: print('MISSING FOLDER', nm); continue
    done_signs = 0
    cells = 0
    for i in range(1, 13):
        d, p = count(N[nm], i)
        cells += d
        if d == EXP[i]: done_signs += 1
    total += cells
    if cells: print(f'{nm:28s} signs complete {done_signs:2d}/12   sheets {cells}')
print('total sheets done:', total, 'of', sum(EXP.values()) * len(order))
