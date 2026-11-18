#!/usr/bin/env python3
"""Rule scan for springboard sheets.

  python3 springboard_qa.py <Nation> [sign-number]     one nation (all signs, or one sign)
Prints one line per problem; ends with a count. Exit code 0 always (it reports, it does not judge).
Checks: STATUS line; the five sections; word count (> 1,300 flagged); South Asian words outside the
single 'Held for review' line; 'Indian' outside published titles; URLs (invented-link risk);
zodiac words used as pointers; web/'according to' findings phrases; no *check* marks at all.
"""
import os, re, sys
R = '/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation'
SOUTH_ASIAN = re.compile(r'\b(punjabi|sikh|hindi|urdu|bengali|bangla|tamil|gujarati|telugu|sinhala|nepali|pashto|south asian|desi\b|indo-)', re.I)
INDIAN_OK = re.compile(r'(Handbook of the Indians|Northwest Indian|Other Indian Languages|Indian Languages|Urban Indian|Indian Boarding|Indian Health Service|Indian Affairs|Indian Act|Indian Country|Indian Reorganization|Indians\b.*(Handbook|Handbook of North American)|Handbook of North American Indians|American Indian [A-Z]|Indian Residential|Indian Claims|Indian Gaming|Indian Child Welfare|Indian Self-Determination|Indian Law|Bureau of Indian|Indian Education|Indian Removal)')
ZOD = re.compile(r'\b(zodiac|astrolog|horoscope)', re.I)
FINDINGS = re.compile(r'\b(studies show|research shows|according to a|it is well known|the culture (values|believes|prizes)|people in (the|this) (nation|region) (tend|value|believe))', re.I)
SECTIONS = ['## 1. Search terms', '## 2. Where to look first', '## 3. Who to compare', '## 4. Flags', '## 5. First queries']

def nation_dir(name):
    for root, dirs, files in os.walk(os.path.join(R, 'Targets')):
        if os.path.basename(root) == name and 'PROGRESS TRACKER.md' in files:
            return root
    sys.exit('no such nation')

name = sys.argv[1]
only = int(sys.argv[2]) if len(sys.argv) > 2 else None
base = os.path.join(nation_dir(name), 'Springboards')
problems = 0
sheets = 0
if os.path.isdir(base):
    for sd in sorted(os.listdir(base)):
        if only and not sd.startswith('%02d - ' % only): continue
        for f in sorted(os.listdir(os.path.join(base, sd))):
            p = os.path.join(base, sd, f)
            t = open(p, encoding='utf-8').read()
            lines = t.split('\n')
            sheets += 1
            rel = f'{sd}/{f}'
            def bad(msg):
                global problems
                problems += 1
                print(f'{rel}: {msg}')
            if not lines[0].startswith('STATUS: done'): bad('first line is not "STATUS: done": ' + lines[0][:40])
            for s in SECTIONS:
                if s not in t: bad('missing section ' + s)
            w = len(t.split())
            if w > 1300: bad(f'long: {w} words')
            if '*check*' not in t: bad('no *check* marks')
            for i, l in enumerate(lines, 1):
                held = l.lstrip().startswith('- **Held for review')
                if SOUTH_ASIAN.search(l) and not held: bad(f'line {i}: South Asian word outside the held line: ' + l.strip()[:70])
                if held and re.search(r'punjabi|sikh|hindi|urdu|bengali|tamil|gujarati', l, re.I): bad(f'line {i}: held line names a community, not a category')
                if re.search(r'\bIndians?\b', l) and not INDIAN_OK.search(l) and not re.search(r'\*[^*]*\bIndians?\b[^*]*\*', l) and not re.search(r'Chemawa|Sherman Indian', l): bad(f'line {i}: "Indian" outside a published title: ' + l.strip()[:70])
                if re.search(r'https?://|www\.', l): bad(f'line {i}: URL (invented-link risk): ' + l.strip()[:70])
                if ZOD.search(l): bad(f'line {i}: zodiac word')
                if FINDINGS.search(l): bad(f'line {i}: reads like a finding: ' + l.strip()[:70])
print(f'{sheets} sheets scanned, {problems} problems')
