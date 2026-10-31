import os,re,collections,json,sys
M="/home/kuroskalacs/Documents/Doll-Fi/media/"
ROOTS={"GDD":"games/Inner Tepenia/InnerTepeniaGDD","Timeline":"Reference/TepenianUniverseTimeline",
"CryptographHelix":"Literature/books/The Cryptograph Helix series","CurrentNovelDocs":"Literature/books/CurrentNovelDocs",
"z-staging":"Literature/books/z-staging (pre-template projects)","SouthernLights":"TV/SouthernLights","ElvenSteel":"TV/ElvenSteel","Tuned":"TV/Tuned",
"OuterTepenia":"games/Outer Tepenia series","TorontoFellOut":"games/Toronto Fell Out/TorontoFellOutGDD","SafetyCodeViolator":"games/Safety Code Violator/SafetyCodeViolatorGDD",
"PlotHole":"games/Plot Hole/PlotHoleGDD","TepenianHawaiian":"Reference/TepenianHawaiian","Hybrid-Anthro":"Reference/Hybrid-Anthro_Culture","DM-Glossary":"Reference/DerivationMechanisms/Glossary"}
EXCL=re.compile(r"graphify-out|/\.git/|/Archive/|Real-World|source_reference|source-books|oral_histor|transcripts|Dark_Humor|to-be-integrated|_safeguard_probe|/\.t8_|Jung_Extractions|/extractions/|book-extractions|Book_Extractions|Story_Structure|/research/0[1-4]|Human_Universals|Robot_Fundamental_Concepts|map-data|_source_text|z-archive|/datasets/|Zodiac_Personality_Substrate|reference/character-methodology|Inspiration_Place_Research|/dispatch|_dispatch",re.I)
words=set(w.strip().lower() for w in open("/usr/share/dict/american-english",encoding="utf-8",errors="ignore"))
def indict(w):
    l=w.lower()
    if l in words: return True
    for suf in ("s","es","ed","ing","'s","ly","er","ers"):
        if l.endswith(suf) and l[:-len(suf)] in words: return True
    return False
STOPAC=set("TODO TBD TBN README NOTE OK US USA UK EU AI PDF CSV MLA ISBN URL HTML CSS JSON API ID IDS FAQ PS AM PM BC AD BCE CE II III IV VI VII VIII IX XI XII XIII XIV XV XVI XVII XVIII XIX XX NB DO NOT NEVER ALL AND THE OR IS IT YES NO NA WIP AND OF IN ON TO A I FIRST NEW MUST EPUB PNG JPG SVG GPS DNA UN NATO USSR PRC ROC DPRK CIA FBI NASA GDP CEO CIO TV HP XP RPG CRPG NPC NPCS UI UX QA DLC MP SP FPS PC MS VS ETC IE EG".split())
tok=re.compile(r"\b[A-Za-z][A-Za-z'\-]{3,}\b")
acr=re.compile(r"\b(?:[A-Z]\.){2,}[A-Z]?\.?|\b[A-Z][A-Za-z]?[A-Z]{1,6}\b")
bold=re.compile(r"\*\*([^*\n]{2,40}?)\*\*")
cap=re.compile(r"\b(?:[A-Z][a-z'\-]+)(?:\s+(?:of|the|and|&|de|del|la|di|von)?\s*[A-Z][a-z'\-]+){1,4}\b")
D={k:collections.defaultdict(set) for k in "WABP"}
nfiles=collections.Counter()
for repo,rel in ROOTS.items():
    base=M+rel
    if not os.path.isdir(base): continue
    for dp,dn,fn in os.walk(base):
        if EXCL.search(dp+"/"): dn[:]=[]; continue
        for f in fn:
            if not f.endswith(".md"): continue
            p=os.path.join(dp,f)
            if EXCL.search(p): continue
            try: t=open(p,encoding="utf-8",errors="ignore").read()
            except: continue
            nfiles[repo]+=1
            key=(repo,p[len(M):])
            for w in set(tok.findall(t)):
                if w[0].isupper() and not indict(w) and not w.isupper(): D["W"][w].add(key)
            for a in set(acr.findall(t)):
                if a.replace(".","") not in STOPAC and len(a.replace(".",""))>=2: D["A"][a].add(key)
            for b in set(bold.findall(t)):
                b=b.strip()
                if ":" in b or len(b.split())>4 or b.endswith((".","?","!")) or b[0] in "0123456789(⚠⭐⛔✅❌[": continue
                D["B"][b].add(key)
            for c in set(cap.findall(t)):
                if len(c.split())>=2: D["P"][c].add(key)
json.dump({k:{t:sorted(v) for t,v in D[k].items()} for k in D},open("raw.json","w"))
print(dict(nfiles))
for k in "WABP":
    tot=len(D[k]); ge3=sum(1 for v in D[k].values() if len(v)>=3); ge2r=sum(1 for v in D[k].values() if len({r for r,_ in v})>=2)
    print(k,tot,"files>=3:",ge3,"repos>=2:",ge2r)
