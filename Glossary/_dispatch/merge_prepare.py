#!/usr/bin/env python3
"""Group the harvest rows by term, across all areas, for the merge stage.

Reads  Glossary/_harvest/*.md   (one table per area; 7 columns)
Writes Glossary/_merge/groups.json and Glossary/_merge/<range>.md
       (one file per letter range, listing each term group with every area's row)

Rows are grouped when their normalized names match, or when their word sets match
("Alaska Republic" / "Republic of Alaska"). Nothing is decided here; the merge
agents decide, including which differently named groups are really one term.
"""
import glob, json, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
G = os.path.dirname(HERE)
HARVEST = os.path.join(G, "_harvest")
OUT = os.path.join(G, "_merge")
RANGES = [("A-C", "ABC"), ("D-H", "DEFGH"), ("I-M", "IJKLM"), ("N-R", "NOPQR"), ("S-T", "ST"), ("U-Z and symbols", "UVWXYZ#")]
STOP = {"the", "of", "a", "an", "and", "&", "de", "del", "la", "le", "el"}

def clean(s):
    return re.sub(r"[`*_]", "", s).strip()

def norm(t):
    t = clean(t).lower()
    t = re.sub(r"^(the|a|an)\s+", "", t)
    return re.sub(r"[^a-z0-9]+", " ", t).strip()

def tokkey(t):
    return " ".join(sorted(w for w in norm(t).split() if w not in STOP))

rows, bad = [], []
for f in sorted(glob.glob(os.path.join(HARVEST, "*.md"))):
    area = os.path.basename(f)[:-3]
    for ln, line in enumerate(open(f, encoding="utf-8"), 1):
        if not line.startswith("| ") or re.match(r"^\|\s*(Term|-)", line):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
        if len(cells) != 7:
            bad.append((area, ln, len(cells)))
            if len(cells) > 7:  # extra pipes inside a cell: fold the overflow into Definition
                cells = cells[:2] + [" | ".join(cells[2:len(cells) - 4])] + cells[-4:]
            else:
                cells += [""] * (7 - len(cells))
        term, cat, defi, status, used, src, var = cells
        if not clean(term):
            continue
        rows.append(dict(area=area, line=ln, term=clean(term), category=cat, definition=defi,
                         status=status, used_in=used, sources=src, variants=var))

# union-find over rows
parent = list(range(len(rows)))
def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra

by_norm, by_tok = collections.defaultdict(list), collections.defaultdict(list)
for i, r in enumerate(rows):
    by_norm[norm(r["term"])].append(i)
    k = tokkey(r["term"])
    if k:
        by_tok[k].append(i)
for idx in list(by_norm.values()) + list(by_tok.values()):
    for j in idx[1:]:
        union(idx[0], j)
# Variant names in the "Variants" column are NOT used for grouping: common names such as
# Concordia or Tepenia appear in many variants cells and chain unrelated terms together.
# The merge agents handle variants, using the full name index.

groups = collections.defaultdict(list)
for i in range(len(rows)):
    groups[find(i)].append(rows[i])

def letter(g):
    # the letter of the most common name in the group
    c = collections.Counter(re.sub(r"^(the|a|an)\s+", "", r["term"], flags=re.I) for r in g)
    name = c.most_common(1)[0][0]
    ch = name[:1].upper()
    return ch if "A" <= ch <= "Z" else "#"

os.makedirs(OUT, exist_ok=True)
glist = sorted(groups.values(), key=lambda g: norm(collections.Counter(r["term"] for r in g).most_common(1)[0][0]))
json.dump(glist, open(os.path.join(OUT, "groups.json"), "w"), indent=1, ensure_ascii=False)
for label, letters in RANGES:
    sel = [g for g in glist if letter(g) in letters]
    with open(os.path.join(OUT, f"{label}.md"), "w", encoding="utf-8") as f:
        f.write(f"# Merge input: terms filed under {label}\n\n{len(sel)} term groups. Each group lists every area's row for that term (or its variants).\n\n")
        for g in sel:
            names_ = sorted({r["term"] for r in g})
            f.write(f"## {' / '.join(names_)}\n")
            for r in g:
                f.write(f"- **[{r['area']}]** {r['term']} | {r['category']} | {r['definition']} | {r['status']} | Used in: {r['used_in']} | Sources: {r['sources']} | Variants: {r['variants']}\n")
            f.write("\n")
    print(f"{label}: {len(sel)} groups")
with open(os.path.join(OUT, "name_index.md"), "w", encoding="utf-8") as f:
    f.write("# Every term name in the harvest, with the letter range it is filed under\n\nUse this to spot the same term under two names in different ranges.\n\n")
    for g in glist:
        L = letter(g)
        rng = next(lbl for lbl, ls in RANGES if L in ls)
        f.write(f"- {' / '.join(sorted({r['term'] for r in g}))} [{rng}]\n")
print(f"rows {len(rows)}, groups {len(glist)}, multi-area groups {sum(1 for g in glist if len({r['area'] for r in g}) > 1)}")
if bad:
    print(f"rows with an unexpected column count: {len(bad)} (first: {bad[:5]})")
