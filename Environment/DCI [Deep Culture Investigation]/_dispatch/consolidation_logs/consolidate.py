#!/usr/bin/env python3
"""Consolidate DCI candidate subtopics across the twelve avenue files (2026-11-15).

A. True duplicates (the same idea proposed in two signs): one home. The home entry keeps its text and gains
   the other entry's full text, word for word, under "Merged here". The other entry becomes a pointer.
B. Related ideas across signs: kept where they are; each candidate in the cluster gains a "See also" line.
Nothing is deleted. Before-copies are written first. Usage: consolidate.py <Avenues dir> <log dir> [--dry]
"""
import sys, re, os, glob, shutil, json

AV, LOG = sys.argv[1], sys.argv[2]
DRY = "--dry" in sys.argv
SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius",
         "Capricorn", "Aquarius", "Pisces"]
AB = {"Ari": "Aries", "Tau": "Taurus", "Gem": "Gemini", "Can": "Cancer", "Leo": "Leo", "Vir": "Virgo",
      "Lib": "Libra", "Sco": "Scorpio", "Sag": "Sagittarius", "Cap": "Capricorn", "Aqu": "Aquarius", "Pis": "Pisces"}
DATE = "2026-11-15"

# ---------------------------------------------------------------- A: one home (home, merged-in)
MERGES = [
    ("Can C6", "Gem C4"),     # Childhood
    ("Sco C23", "Gem C26"),   # Privacy
    ("Gem C7", "Ari C7"),     # Directness
    ("Sco C22", "Tau C18"),   # Loyalty
    ("Can C5", "Tau C21"),    # Hospitality
    ("Cap C2", "Leo C41"),    # Status and standing
    ("Leo C25", "Cap C3"),    # Reputation
    ("Vir C1", "Tau C15"),    # Routine
    ("Pis C41", "Tau C33"),   # Charity and almsgiving
    ("Sco C4", "Tau C36"),    # Inheritance
    ("Gem C6", "Lib C6"),     # Manners and civility
    ("Gem C10", "Leo C21"),   # Humor
    ("Can C3", "Tau C30"),    # Rootedness
    ("Sag C33", "Pis C21"),   # Devotion to saints
    ("Ari C2", "Leo C39"),    # Self-presentation and persona
    ("Tau C4", "Leo C9"),     # Dress
]

# ---------------------------------------------------------------- B: see-also clusters ("Sag #9" = settled concept 9)
CLUSTERS = [
    ("the privacy of the home", ["Can C7", "Sco C23"]),
    ("hospitality's neighbors", ["Can C5", "Can C33", "Vir C29"]),
    ("food", ["Tau C3", "Vir C6", "Can C14", "Can C11", "Gem C30"]),
    ("rest and leisure", ["Tau C14", "Leo C49", "Vir C31", "Vir C35", "Vir C5"]),
    ("craft and skill", ["Tau C19", "Vir C9", "Vir C28", "Leo C14"]),
    ("patience and time", ["Ari C5", "Tau C16", "Cap C5", "Cap C54", "Cap C13"]),
    ("thrift, waste and salvage", ["Tau C5", "Tau C29", "Pis C24", "Ari C26", "Vir C12"]),
    ("debts and gratitude", ["Tau C7", "Lib C33", "Cap C24"]),
    ("envy and jealousy", ["Tau C27", "Sco C20"]),
    ("class and getting ahead", ["Tau C28", "Cap C43", "Cap C45", "Cap C46", "Aqu C39", "Sag C51"]),
    ("giving", ["Leo C46", "Pis C41", "Pis C57", "Cap C32"]),
    ("sharing, the commons and mutual aid", ["Tau C35", "Sco C5", "Aqu C14", "Aqu C24", "Aqu C15", "Vir C26"]),
    ("heirlooms and legacy", ["Tau C31", "Sco C4", "Sco C18"]),
    ("mistakes, apology and forgiveness", ["Tau C44", "Vir C25", "Lib C21", "Lib C26", "Sco C14"]),
    ("pleasure and restraint", ["Tau C46", "Cap C19", "Pis C48", "Leo C1", "Lib C49", "Vir C20"]),
    ("arguing", ["Gem C8", "Lib C42", "Lib C19"]),
    ("story", ["Gem C11", "Sag C43", "Sag C17"]),
    ("knowledge and cleverness", ["Gem C14", "Sag C6", "Sag C50", "Sag C52", "Gem C39"]),
    ("teaching", ["Gem C13", "Sag #9", "Gem #3", "Vir C17"]),
    ("changing one's mind", ["Gem C16", "Tau C26", "Lib #8"]),
    ("secrets and silence", ["Gem C19", "Sco C44", "Sco C50", "Sco C52"]),
    ("tolerance and openness", ["Gem C20", "Aqu C8", "Sag C9", "Lib C40", "Aqu C13"]),
    ("youth and maturity", ["Gem C21", "Cap C17"]),
    ("persuasion and manipulation", ["Gem C23", "Sco C21"]),
    ("lying and honesty", ["Gem C24", "Sag #4", "Sag #8", "Gem C29", "Gem C43"]),
    ("belief and skepticism", ["Gem C25", "Sag C40", "Sag C39", "Vir C50"]),
    ("friendship and chosen kin", ["Gem C46", "Can C35", "Aqu C30", "Aqu C44"]),
    ("brokers and patrons (note: Leo's patronage is of the arts, Capricorn's is clientelism)",
     ["Gem C48", "Gem C47", "Cap C7", "Leo C16", "Leo C35", "Cap C28"]),
    ("homeland and group belonging", ["Can C20", "Can C28", "Aqu C26", "Cap C16", "Leo C40", "Aqu C21"]),
    ("longing", ["Can C15", "Can C29", "Sag C22", "Pis C40", "Pis C39"]),
    ("family memory and tradition", ["Can C16", "Sco C50", "Cap C11"]),
    ("guilt", ["Can C17", "Pis C60", "Pis C59", "Sag C19"]),
    ("loneliness and solitude", ["Can C23", "Aqu C19", "Aqu C18", "Pis C9", "Sag C35"]),
    ("elders", ["Can C10", "Cap C4"]),
    ("help that smothers", ["Can C37", "Can C13", "Can C22", "Vir C62", "Pis C30"]),
    ("protectors and rescuers", ["Can C38", "Ari C28"]),
    ("self-care", ["Can C39", "Vir C32", "Pis C44"]),
    ("care work", ["Can C40", "Can C8", "Vir C18"]),
    ("exclusion", ["Can C41", "Sco C41", "Lib C27", "Cap C15"]),
    ("migration and newcomers",
     ["Can C42", "Can C33", "Sag C47", "Sag C48", "Sag C8", "Gem C42", "Pis C50", "Pis C53", "Aqu C10", "Sco C51"]),
    ("romance and partnership", ["Leo C2", "Lib C44", "Lib C2", "Sco C1", "Sco C3", "Tau C45"]),
    ("celebration and crowds", ["Leo C5", "Aqu C34", "Aqu C23", "Aqu C12"]),
    ("sport and fitness", ["Leo C6", "Vir C57", "Ari C32", "Aqu C32"]),
    ("luck, fate and providence", ["Leo C7", "Sag C7", "Sco C45"]),
    ("showing off", ["Leo C12", "Tau C40", "Leo C24", "Ari C20"]),
    ("respect and deference", ["Leo C17", "Cap C21", "Cap C9", "Leo C47"]),
    ("chivalry and manhood", ["Leo C18", "Ari C9", "Lib C7"]),
    ("winning and losing", ["Leo C19", "Ari C32"]),
    ("authenticity and the public self", ["Leo C20", "Gem C29", "Ari C2"]),
    ("showing and holding back feeling", ["Leo C38", "Sco C11"]),
    ("the worth of work", ["Leo C44", "Vir C36", "Vir C40"]),
    ("happiness and enough", ["Leo C51", "Tau C25", "Aqu C28"]),
    ("working together", ["Vir C19", "Lib C11", "Leo C15"]),
    ("worry, madness and mental health", ["Vir C58", "Vir C23", "Pis C3", "Pis C5", "Sco C57", "Pis C68", "Pis #11"]),
    ("healing", ["Vir C55", "Vir C34", "Pis C23", "Pis C20", "Pis C18"]),
    ("civic life", ["Vir C46", "Aqu C2", "Aqu C3", "Cap C34"]),
    ("animals", ["Vir C48", "Pis C46"]),
    ("taste and beauty", ["Vir C51", "Tau C24"]),
    ("progress and the future", ["Vir C61", "Aqu C6", "Sag C55"]),
    ("enmity and feuds", ["Lib C3", "Sco C49", "Cap C51"]),
    ("corruption", ["Lib C16", "Lib C51", "Cap C33", "Cap C53"]),
    ("keeping one's word", ["Tau C17", "Leo C50", "Lib C25", "Cap C22", "Tau C43"]),
    ("endurance and perseverance", ["Ari C18", "Cap C20", "Tau C43", "Ari C17"]),
    ("the self through others", ["Lib C29", "Aqu C25"]),
    ("rules and loopholes", ["Cap C18", "Lib C8"]),
    ("addiction and recovery", ["Sco C38", "Pis C54", "Pis C55"]),
    ("conversion and revival", ["Sco C37", "Sco C40", "Sag C11", "Sag C54"]),
    ("speaking out", ["Sco C42", "Sag C38", "Sag C27"]),
    ("nature", ["Sco C47", "Pis C56", "Aqu C40", "Cap C39", "Tau C20"]),
    ("martyrs", ["Sag C45", "Pis C47"]),
    ("hope and optimism", ["Sag C13", "Aqu #9", "Aqu C29", "Aqu C49"]),
    ("exploration and frontiers", ["Gem C40", "Sag C14", "Sag C37", "Ari C8"]),
    ("better worlds", ["Sag C20", "Sag C30", "Aqu C41", "Aqu C1"]),
    ("rebellion and revolution", ["Aqu C5", "Ari C11"]),
    ("self-rule and how groups decide", ["Aqu C16", "Ari C35", "Lib C13"]),
    ("schism and heresy", ["Aqu C36", "Sag C56", "Sco C41"]),
    ("objectivity", ["Aqu C48", "Lib #5"]),
    ("networks and connections (compadrazgo's home is Cancer C27)", ["Aqu C11", "Tau C32", "Gem C41", "Can C27"]),
    ("outlaws", ["Cap C52", "Aqu C37", "Pis C61"]),
    ("initiation and entry", ["Cap C41", "Aqu C9", "Aqu C10"]),
    ("titles and names", ["Cap C44", "Ari C3"]),
    ("generations", ["Aqu C38", "Lib C41"]),
    ("merge proposals that touch each other (settle together)", ["Lib C56", "Lib C57", "Aqu C52"]),
]

# ---------------------------------------------------------------- parse
files = {}
for f in sorted(glob.glob(glob.escape(AV) + "/[01]* - *.md")):
    if "from the other signs" in f:
        continue
    sign = os.path.basename(f)[5:-3]
    files[sign] = f

def parse(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("## Candidate subtopics"))
    blocks, i = {}, start
    order = []
    while i < len(lines):
        m = re.match(r"### (C\d+)\. (.*)$", lines[i])
        if m:
            j = i + 1
            while j < len(lines) and not re.match(r"(### |## |\*\*Considered and not proposed)", lines[j]):
                j += 1
            k = j
            while k > i + 1 and lines[k - 1].strip() == "":
                k -= 1   # block body ends before trailing blank lines
            blocks[m.group(1)] = dict(s=i, e=k, title=m.group(2).strip())
            order.append(m.group(1))
            i = j
        else:
            i += 1
    return lines, blocks, order

data = {s: parse(p) for s, p in files.items()}

concepts = {}
for s, p in files.items():
    for n, name in re.findall(r"^## (\d+)\. (.*)$", open(p, encoding="utf-8").read(), re.M):
        concepts[(s, n)] = name

def ref(tok):
    ab, rest = tok.split(" ")
    s = AB[ab]
    if rest.startswith("#"):
        n = rest[1:]
        return s, None, f"{s} concept {n}, {concepts[(s, n)]}"
    cid = rest
    t = data[s][1][cid]["title"]
    return s, cid, f"{s} {cid}, {t}"

problems = []
moved = {}  # (sign, cid) -> (home sign, home cid)
for home, other in MERGES:
    hs, hc, _ = ref(home); os_, oc, _ = ref(other)
    moved[(os_, oc)] = (hs, hc)

append = {}   # (sign, cid) -> list of extra lines
replace = {}  # (sign, cid) -> new block lines

for home, other in MERGES:
    hs, hc, hlabel = ref(home); os_, oc, olabel = ref(other)
    lines, blocks, _ = data[os_]
    b = blocks[oc]
    body = lines[b["s"] + 1:b["e"]]
    nested = [("  " + l) if l.strip() else l for l in body]
    append.setdefault((hs, hc), []).extend(
        [f"- **Merged here (consolidation, {DATE}) from {olabel}.** Its full entry, word for word:"] + nested)
    replace[(os_, oc)] = [lines[b["s"]],
                          f"- **Consolidated {DATE}:** one home per idea. This entry now lives in {hlabel}, "
                          f"where its full text is kept word for word under \"Merged here\"."]

for name, toks in CLUSTERS:
    resolved = []
    for t in toks:
        s, cid, label = ref(t)
        if cid and (s, cid) in moved:   # point at the home instead of a merged-away entry
            hs, hc = moved[(s, cid)]
            s, cid, label = ref(f"{[k for k, v in AB.items() if v == hs][0]} {hc}")
        if (s, cid, label) not in resolved:
            resolved.append((s, cid, label))
    for s, cid, label in resolved:
        if cid is None:
            continue
        others = [l for (s2, c2, l) in resolved if (s2, c2) != (s, cid)]
        if not others:
            continue
        append.setdefault((s, cid), []).append(
            f"- *See also (consolidation, {DATE}; {name}):* " + "; ".join(others) + ".")

# ---------------------------------------------------------------- write
if not DRY:
    os.makedirs(LOG + "/before", exist_ok=True)
    for s, p in files.items():
        shutil.copy(p, LOG + "/before/" + os.path.basename(p))

summary = {}
for s, p in files.items():
    lines, blocks, order = data[s]
    out = list(lines)
    # apply from the bottom up so indices stay valid
    for cid in sorted(blocks, key=lambda c: blocks[c]["s"], reverse=True):
        key = (s, cid)
        b = blocks[cid]
        if key in replace:
            out[b["s"]:b["e"]] = replace[key]
        elif key in append:
            out[b["e"]:b["e"]] = append[key]
    summary[s] = dict(pointers=sum(1 for k in replace if k[0] == s),
                      homes=sum(1 for k, v in append.items() if k[0] == s and any("Merged here" in x for x in v)),
                      seealso=sum(1 for k, v in append.items() if k[0] == s and any("See also" in x for x in v)))
    if not DRY:
        open(p, "w", encoding="utf-8").write("\n".join(out))

print(json.dumps(summary, indent=0))
print("pointers", len(replace), "home entries", len({k for k, v in append.items() if any('Merged here' in x for x in v)}),
      "see-also entries", len({k for k, v in append.items() if any('See also' in x for x in v)}))
