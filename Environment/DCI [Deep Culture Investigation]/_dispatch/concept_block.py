#!/usr/bin/env python3
"""Print one concept's block (or a sign's domain block) from a sign's avenue file, and list a sign's concepts.

  python3 concept_block.py list <sign-number>                 # "N<TAB>Concept name" per line, plus the domain line
  python3 concept_block.py <sign-number> <concept-number|0>   # the block; 0 = the sign's domain section
"""
import os, re, sys
DM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AV = os.path.join(DM, 'Shared', 'Avenues')

def sign_file(n):
    for f in sorted(os.listdir(AV)):
        if re.fullmatch(r'%02d - [A-Za-z]+\.md' % int(n), f):
            return os.path.join(AV, f)
    sys.exit('no such sign')

def blocks(path):
    t = open(path, encoding='utf-8').read().split('\n')
    out, cur = [], None
    for l in t:
        m = re.match(r'## (\d+)\. (.*)$', l)
        if m:
            cur = [int(m.group(1)), m.group(2).strip(), [l]]
            out.append(cur)
        elif l.startswith('## ') or l.startswith('### C'):
            cur = None
        elif cur is not None:
            cur[2].append(l)
    return out

if sys.argv[1] == 'list':
    for n, name, _ in blocks(sign_file(sys.argv[2])):
        print(f'{n}\t{name}')
else:
    for n, name, body in blocks(sign_file(sys.argv[1])):
        if n == int(sys.argv[2]):
            print('\n'.join(body).rstrip('\n'))
            break
    else:
        sys.exit('no such concept')
