#!/usr/bin/env python3
"""Checks for the DCI sign-completion run.

  python3 qa_sign.py "NN - Sign"   full check of one sign file
  python3 qa_sign.py --all         one line per sign, for resuming after a cutoff
"""
import os
import re
import sys

DM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AV = os.path.join(DM, 'Shared', 'Avenues')
LOGS = os.path.join(DM, '_dispatch', 'sign_completion_logs')
BEFORE = os.path.join(LOGS, 'before')
PROGRESS = os.path.join(DM, '_dispatch', 'SIGN_COMPLETION_PROGRESS.md')

OLD = ['Words', 'Beliefs and standing', 'Feeling and the body', 'Everyday practice', 'Life course',
       'Ritual', 'Institutions', 'Rewards and sanctions', 'Expression', 'Exemplars', 'History',
       'Measures', 'Variation', 'Relations', 'Who it applies to', 'Silences', 'Change']
NEW = ['The senses', 'Space, place and things', 'Time and rhythm', 'The economy of it',
       'Conflict and crisis', 'Margins and extremes']
TIERS = ['Everywhere', 'Writing', 'Public records', 'Mass media', 'Online', 'Commerce',
         'Organizations', 'The people who handle it', 'Outsiders', 'Scholarship and data']


def signs():
    return sorted(f[:-3] for f in os.listdir(AV) if re.fullmatch(r'\d\d - [A-Za-z]+\.md', f))


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def split(t):
    secs = re.split(r'\n## ', t)
    dom = next((s for s in secs if s.startswith('0.')), '')
    cons = [s for s in secs[1:] if re.match(r'\d+\.', s) and not s.startswith('0.')]
    return dom, cons


def heading(h):
    return re.compile(r'\*\*' + re.escape(h) + r':?\*\*')


def tiers(s):
    return re.findall(r'^  - \*([^*]+):\*', s, re.M)


def concept_ok(s):
    return all(len(heading(h).findall(s)) == 1 for h in OLD + NEW) and s.count('**Source types**') == 1 \
        and not [x for x in TIERS if x not in tiers(s)]


def checks(t):
    return len(re.findall(r'\*check\*|\(check\)', t))


def progress_status():
    out = {}
    if os.path.exists(PROGRESS):
        for line in read(PROGRESS).split('\n'):
            m = re.match(r'\|\s*\d+\s*\|\s*([A-Za-z]+)\s*\|\s*([^|]*)\|', line)
            if m:
                out[m.group(1)] = m.group(2).strip()
    return out


def last_checkpoint(name):
    p = os.path.join(LOGS, name + '.log.md')
    if not os.path.exists(p):
        return '(no log)'
    lines = [l for l in read(p).split('\n') if re.match(r'- \d{4}-\d\d-\d\d', l) and 'NOTE:' not in l]
    return lines[-1][2:] if lines else '(no checkpoints yet)'


def summary():
    prog = progress_status()
    for name in signs():
        t = read(os.path.join(AV, name + '.md'))
        dom, cons = split(t)
        ok = sum(concept_ok(s) for s in cons)
        cand = bool(re.search(r'\n## Candidate subtopics', t))
        sign = name[5:]
        print(f'{name:16} progress: {prog.get(sign, "?")}')
        print(f'{"":16} file: {t.split(chr(10))[0][:60]} | concepts complete {ok}/{len(cons)} '
              f'| domain source types {"**Source types**" in dom} | candidates {cand}')
        print(f'{"":16} log: {last_checkpoint(name)}')


def full(name):
    t = read(os.path.join(AV, name + '.md'))
    dom, cons = split(t)
    print(name, '| line 1:', t.split('\n')[0][:80], '| words', len(t.split()))
    print('domain: source types', '**Source types**' in dom, '| missing tiers', [x for x in TIERS if x not in tiers(dom)] or '-')
    for s in cons:
        title = s.split('\n')[0][:28]
        miss = [h for h in OLD + NEW if not heading(h).search(s)]
        dup = [h for h in OLD + NEW if len(heading(h).findall(s)) > 1]
        if s.count('**Source types**') > 1:
            dup.append('Source types')
        mt = [x for x in TIERS if x not in tiers(s)]
        order = [heading(h).search(s) for h in ['Change'] + NEW]
        pos = [m.start() for m in order if m]
        st, kq = s.find('**Source types**'), s.find('**Key questions')
        seq = pos + [p for p in (st, kq) if p >= 0]
        in_order = seq == sorted(seq)
        items = sum(len([x for x in re.split(r';', l) if x.strip()]) for l in re.findall(r'^  - \*[^*]+:\*(.*)$', s, re.M))
        print(f'  {title:28} missing:{miss or "-"} dup:{dup or "-"} tiers-missing:{mt or "-"} '
              f'order-ok:{in_order} source-type items:~{items}')
    if not name.startswith(('07', '10')):
        law = [m.group(0) for m in re.finditer(r'.{0,40}\b(laws?|legal|courts?|statutes?|police|prisons?|lawyers?|litigation)\b.{0,30}', t, re.I)]
        print('law-word hits (review each):', len(law))
        for x in law[:15]:
            print('   ', x.replace('\n', ' '))
    print('"Indian" uses (titles only):', [m.group(0) for m in re.finditer(r'.{0,25}\bIndian\b.{0,20}', t)])
    sa = sorted(set(m.group(0) for m in re.finditer(
        r'\b(India|Hindu\w*|Sikh\w*|Punjab\w*|karma|yoga|Rajneesh\w*|Komagata|Chetty|Banaji|Iyengar|Mullainathan|Murthy|Iyer)\b', t)))
    print('South Asian hits:', sa)
    br = sorted(set(m.group(0).lower() for m in re.finditer(
        r'\b(colour\w*|behaviour\w*|honour\w*|organis\w+|recognis\w+|favour\w*|defence|licence|programme|travelling|neighbour\w*|analyse|centre\w*|catalogue)\b', t, re.I)))
    print('British spellings (check proper names):', br)
    cand = re.search(r'\n## Candidate subtopics', t)
    print('candidate-subtopics section:', bool(cand), '| entries (### or bold bullets):',
          len(re.findall(r'^(?:### |- \*\*)', t[cand.start():], re.M)) if cand else 0)
    b = os.path.join(BEFORE, name + '.md')
    if os.path.exists(b):
        bt = read(b)
        cur = set(l.strip() for l in t.split('\n'))
        gone = [l for l in bt.split('\n')[1:] if l.strip() and l.strip() not in cur]
        print(f'lines from the pre-run backup no longer present (should be 0): {len(gone)}')
        for l in gone[:8]:
            print('   ', l[:150])
        print(f'*check* marks: before {checks(bt)}, now {checks(t)}, new {checks(t) - checks(bt)}')
    else:
        print('no pre-run backup found in', BEFORE)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == '--all':
        summary()
    else:
        full(sys.argv[1])
