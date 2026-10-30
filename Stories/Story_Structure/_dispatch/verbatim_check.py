#!/usr/bin/env python3
"""Share of an output file's words that sit inside 6-word runs copied verbatim from the
local source texts (Truby, Snyder, Harmon worksheets). Run from Stories/Story_Structure/:
    python3 _dispatch/verbatim_check.py "<file.md>" [more files...]
    python3 _dispatch/verbatim_check.py --all
Target for this repo (public): FILE 8% or less."""
import glob, os, re, sys
SRC = "source_reference (local only, not in git)/text/"
N = 6
norm = lambda t: re.findall(r"[a-z0-9’']+", re.sub(r"\{[^}]*\}", " ", t.lower()))
src = norm(" ".join(open(f, encoding="utf-8", errors="replace").read() for f in glob.glob(SRC + "*.txt")))
grams = {tuple(src[i:i + N]) for i in range(len(src) - N + 1)}
files = sys.argv[1:]
if files == ["--all"]:
    files = [f for d in ("John Truby - The Anatomy of Story", "Blake Snyder - Save the Cat", "Dan Harmon - Story Circle")
             for f in sorted(glob.glob(d + "/**/*.md", recursive=True))]
for f in files:
    w = norm(open(f, encoding="utf-8").read()); hit = [False] * len(w)
    for i in range(len(w) - N + 1):
        if tuple(w[i:i + N]) in grams:
            for j in range(i, i + N): hit[j] = True
    print("FILE %5.1f%%  %6d words  %s" % (100 * sum(hit) / max(len(w), 1), len(w), f))
