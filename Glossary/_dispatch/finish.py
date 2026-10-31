#!/usr/bin/env python3
"""Post-merge finishing for the glossary.

1. Reads every letter file (A.md ... Z.md, 0-9.md).
2. Adds a cross-reference stub ("### Name" + "- **See:** [Title](X.md#anchor)") for every
   "Also called" name that has no entry of its own, in the letter file where that name sorts.
3. Re-sorts each letter file's entries (a leading "The"/"A"/"An" is ignored).
4. Writes CATEGORY INDEX.md (every entry, grouped by category) and refreshes the
   category table and counts in README.md between the INDEX markers.

Run from anywhere: python3 Glossary/_dispatch/finish.py [--dry-run]
"""
import glob, os, re, sys, collections

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv
CATS = ["organization", "company", "polity", "place", "era or event", "law or rule", "robot biology",
        "technology", "culture and society", "group or people", "language", "unit or measure",
        "game term", "method term"]

def sortkey(title):
    t = re.sub(r"^(the|a|an)\s+", "", title.strip(), flags=re.I)
    return re.sub(r"[^a-z0-9 ]", "", t.lower())

def file_for(title):
    ch = sortkey(title)[:1].upper()
    return f"{ch}.md" if "A" <= ch <= "Z" else "0-9.md"

def anchor(title):
    a = title.strip().lower()
    a = re.sub(r"[^\w\- ]", "", a, flags=re.UNICODE)
    return a.replace(" ", "-")

def parse(path):
    text = open(path, encoding="utf-8").read()
    head, *parts = re.split(r"(?m)^### ", text)
    entries = []
    for p in parts:
        title, _, body = p.partition("\n")
        entries.append({"title": title.strip(), "body": body.rstrip() + "\n"})
    return head.rstrip() + "\n", entries

files = sorted(glob.glob(os.path.join(G, "[A-Z].md")) + glob.glob(os.path.join(G, "0-9.md")))
data = {os.path.basename(f): parse(f) for f in files}

titles = {}
for fn, (_, ents) in data.items():
    for e in ents:
        titles.setdefault(e["title"].lower(), (fn, e))

stubs = 0
for fn, (_, ents) in list(data.items()):
    for e in list(ents):
        if "**See:**" in e["body"]:
            continue
        m = re.search(r"(?m)^- \*\*Also called:\*\*\s*(.+)$", e["body"])
        if not m:
            continue
        names, depth, cur = [], 0, ""
        for ch in m.group(1):
            depth += (ch == "(") - (ch == ")")
            if ch == ";" and depth == 0:
                names.append(cur); cur = ""
            else:
                cur += ch
        names.append(cur)
        for name in names:
            bare = re.sub(r"\s*\([^)]*\)\s*", " ", name).strip(" .")
            if not bare or bare.lower() in titles:
                continue
            target = file_for(bare)
            stub = {"title": bare, "body": f"- **See:** [{e['title']}]({fn}#{anchor(e['title'])})\n"}
            if target not in data:
                data[target] = (f"# Glossary: {target[:-3]}\n", [])
            data[target][1].append(stub)
            titles[bare.lower()] = (target, stub)
            stubs += 1

catmap = collections.defaultdict(list)
total = 0
for fn, (head, ents) in sorted(data.items()):
    ents.sort(key=lambda e: sortkey(e["title"]))
    for e in ents:
        if "**See:**" in e["body"]:
            continue
        total += 1
        m = re.search(r"(?m)^- \*\*Category:\*\*\s*(.+)$", e["body"])
        cat = (m.group(1).strip().lower() if m else "uncategorized")
        ALIAS = {"megacorporation": "company", "corporation": "company", "agency": "organization",
                 "nation": "polity", "city": "place", "event": "era or event", "era": "era or event"}
        main = next((c for c in CATS if cat.startswith(c)), None) or next(
            (v for k, v in ALIAS.items() if k in cat), cat.split(";")[0].split(",")[0].strip())
        catmap[main].append((e["title"], fn))
    if not DRY:
        with open(os.path.join(G, fn), "w", encoding="utf-8") as f:
            f.write(head + "\n" + "\n".join(f"### {e['title']}\n{e['body']}" for e in ents))

allstubs = sum(1 for _, (_, ents) in data.items() for e in ents if "**See:**" in e["body"])
order = [c for c in CATS if c in catmap] + sorted(c for c in catmap if c not in CATS)
idx = ["# Category index", "", f"Every glossary entry ({total}), grouped by category. Cross-reference stubs are not listed.", ""]
for c in order:
    items = sorted(catmap[c], key=lambda t: sortkey(t[0]))
    idx.append(f"## {c[:1].upper() + c[1:]} ({len(items)})")
    idx.append(" · ".join(f"[{t}]({fn}#{anchor(t)})" for t, fn in items))
    idx.append("")
table = ["| Category | Entries |", "|---|---|"] + [f"| {c[:1].upper() + c[1:]} | {len(catmap[c])} |" for c in order]
if not DRY:
    open(os.path.join(G, "CATEGORY INDEX.md"), "w", encoding="utf-8").write("\n".join(idx) + "\n")
    readme = open(os.path.join(G, "README.md"), encoding="utf-8").read()
    block = ("<!-- INDEX START -->\n"
             f"**{total} entries** in {len(data)} letter files, plus {allstubs} cross-reference stubs for alternate names. "
             "The full list by category is `CATEGORY INDEX.md`.\n\n" + "\n".join(table) + "\n<!-- INDEX END -->")
    if "<!-- INDEX START -->" in readme:
        readme = re.sub(r"<!-- INDEX START -->.*?<!-- INDEX END -->", block, readme, flags=re.S)
    else:
        readme = re.sub(r"(?s)## Category index\n.*\Z", "## Category index\n" + block + "\n", readme)
    open(os.path.join(G, "README.md"), "w", encoding="utf-8").write(readme)
print(f"entries {total}, stubs added {stubs}, letter files {len(data)}")
for c in order:
    print(f"  {c}: {len(catmap[c])}")
