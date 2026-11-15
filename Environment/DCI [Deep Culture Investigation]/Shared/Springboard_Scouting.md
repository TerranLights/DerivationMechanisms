STATUS: v1 (2026-11-15). Author's request; nothing has been run at scale yet.

# Springboard scouting: where to begin looking

**What this is.** A first pass over every target nation, sign by sign, concept by concept (author, 2026-11-15). For each nation × concept, a short **springboard sheet** says **where a researcher should start looking**. **It is not research.** Real research is a later task (likely the next 6 to 10 months). A springboard answers one question: *if I sat down to research how this culture understands this concept, what would I search for, and where would I look first?*

**What a sheet holds:** only "surface data": names and pointers, no findings.
1. **Search terms:** the concept's words in the nation's main language(s), with a gloss, plus English keywords.
2. **Where to look first:** named datasets and surveys, institutions and archives, standard scholarly works and authors, publications and media, folk and popular forms. Each says what it would give and how it can be reached.
3. **Who to compare:** the regional cultures, ethnic or Indigenous peoples and groups inside the nation worth separating (candidate units, for the target's Stage 0).
4. **Flags:** is the data likely rich or thin? Which language is needed? Anything sensitive?
5. **First queries:** three to five concrete first steps.

**What a sheet must not hold:** findings, summaries of how the culture understands the concept, statistics, quotations, or any claim about the culture. If the agent finds itself writing "the culture values...", it should stop.

## How the scouting is done: no web
- **From the agent's own knowledge only. No web search, no web fetch, no reading of outside files** beyond the inputs listed in the brief. This is deliberate: it keeps the pass cheap and keeps it from drifting into research.
- **Never invent.** A title, author, URL, dataset name, institution or term that the agent is not confident exists is not written. Instead it writes the *type* of source and the query that would find it ("a national time-use survey; search the statistics office for 'time use'").
- **Everything named is marked *check*.** None of it has been verified; the later research verifies it.
- A thin answer is a good answer. "Unknown; likely thin; start with the language's own dictionary" is a valid sheet.

## The jobs, and the order
- **One job = one nation × one sign × one concept** (plus one per nation × sign for the sign's domain and folkways). A sign's jobs run in parallel; **signs run one at a time, Aries to Pisces; nations run one at a time**, in the master tracker's order (Cascadia first).
- **The concepts used are the current lists in `Shared/Avenues/`** (118 concepts, draft; only Aries's list is settled). The 650 candidate subtopics are not scouted separately; each is a facet of its parent concept until the author promotes it.

## Where the sheets go
`Targets/<region>/<nation>/Springboards/NN - <Sign>/` with `00 - Domain and folkways.md` and `NN - <Concept>.md` (the concept's number and name from its avenue file). Template: `Templates/T_Springboard.md`. Every sheet's first line is `STATUS: done <date>, not verified` (or `in progress`). The brief is `_dispatch/SPRINGBOARD_BRIEF.md`; progress is `SPRINGBOARD_PROGRESS.md` in the results root's `_dispatch/`, and `_dispatch/springboard_status.py` prints the grid.

## Rules every sheet follows (the method's standing rules)
- **American English.** **Native, Indigenous or Aboriginal, never "Indian"** (First Nations, Inuit or Métis in Canada); published titles and a nation's own name stay as published.
- **No South Asian works, scholars, communities or languages anywhere in a sheet** except the single "Held for review" line at the bottom, and there only as a category. (A pointer that would be set aside only because of a name goes there.)
- **No law outside Libra and Capricorn.** Libra's concepts take the letter of the law; Capricorn's take the spirit.
- **No national stereotypes.** A sheet names variation to check, never one voice for a people.
- **The target is the post-war nation,** not the old country: its tracker header lists the pre-war lands it carries. Search terms and sources follow its places.
- **The signs are research classifiers only.** Nothing zodiac-derived is a pointer.
- **Public repo:** pointers and short titles only. No quotation beyond a few words.
