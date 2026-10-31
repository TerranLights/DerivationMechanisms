# Brief: the glossary sweep, harvest stage (2026-10-30)

## The project
The Derivation Mechanisms repo has a glossary, `Glossary/`, meant to define essentially every term any of the author's repos needs (author, 2026-10-30). The author's examples:
- TANA, the Tepenian Astrometric & Navigational Authority;
- Siligel, a type of robot food;
- HyperHedral and Abramentes, robot-fabrication megacorporations.

Most repos are set in the author's **Tepenian universe**, a robot-oriented science-fiction universe. A few projects may be set elsewhere; say so when you find one.

**This stage is the harvest.** Each agent covers one area of the repos and writes one harvest file. A later merge turns all the harvest files into the alphabetical glossary. Read `../README.md` (the glossary's entry format and status levels) and `../A.md`, `../S.md` (finished entries) first.

## What counts as a term
**Include:**
- **Organizations:** agencies, authorities, councils, courts, institutes.
- **Companies:** megacorporations, firms, brands.
- **Polities:** nations, republics, federations, unions, blocs.
- **Places in the universe:** cities, subnets, districts by their in-fiction names, regions, landmarks, stations, colonies.
  - A real-world place belongs **only** when the universe gives it its own name, role or meaning. For example, a Tepenian city sited at a real Antarctic station counts.
- **Eras and events:** periods, wars, treaties, disasters, migrations.
- **In-world laws and rules:** for example the Fundamental Laws of Robotics.
- **Robot biology:** anatomy, physiology, substances, life stages (for example the gel brain, siligel, activation).
- **Technology:** networks, devices, vehicles, materials (for example the Arcanet).
- **Culture and society:** customs, institutions, social categories, religions, in-world slang that is actually used.
- **Groups and peoples:** races, cultures, factions, demonyms.
- **Languages and registers.**
- **Units and measures:** time, currency, distance.
- **Game terms:** named mechanics and modes. Mark them as game-specific.
- **Method terms:** the author's own out-of-fiction design and method vocabulary, such as ULM, RWBEM, CST, Megasheet, Tier U and Mega-Init. Mark them as out of fiction.

**Leave out:**
- **Individual characters.** Their names have character files. Named groups and factions do count.
- **Real-world things used in their ordinary meaning.**
- **Vocabulary from real-language datasets.**
- **Story-structure and Enneagram framework terms** (Save the Cat beats, Truby steps, the nine types). The glossary points to their own folders in Derivation Mechanisms instead.
- **One-off names in working or run files** that are never defined and never recur.

## Known unnamed things (author, 2026-10-30)
- **The GDD's Background-Lore vignettes and every Course of Events file are not canon** (GDD `TODO.md`, developer ruling 2026-09-30/10-01). A term found only there is left out, or listed as `working: from a non-canon vignette`.
- **Majyao's teahouse in Janbogo has no actual name yet.** List it as "Majyao's teahouse (Janbogo)" with Status `working: name not yet chosen`. Any name a file gives it is a placeholder, not canon; record it under Variants and conflicts.

## How to work
**Your area is far too big to read word for word.** Work like this:
1. **Read the area's own indexes first:** READMEs, canon references, overview and summary files, rosters, status trackers. Canon tends to be stated there.
2. **Go through your candidate list,** `_dispatch/candidates/<your area>.txt`. These are words, acronyms, bold phrases and capitalized phrases mined from your area, most frequent first. Most are noise: real places, characters, ordinary words, headings. For each one that might be a term, grep the repos for its defining context and decide.
3. **Find terms the miner can't see:** ordinary words used in a special in-universe sense (for example "subnet", "the Hub", "Undercurrent", "activation"). Read the core lore files for them.

**Defining a term:**
- Find where it is defined, not just mentioned. Use the most authoritative source, in this order:
  1. TepenianUniverseTimeline, if it covers the term;
  2. an explicit author ruling in a project repo;
  3. a project's design files.
- Grep across **all** repos for the term, so that "Used in" is complete and conflicts surface. The repo roots are listed in `assignments.md`.
- **Never invent or fill in a definition.** If the repos only mention a term without defining it, say "mentioned, not defined" and cite where.

## Output
Write **one file:** `Glossary/_harvest/<your area>.md`.
- **First line:** `STATUS: IN PROGRESS (next: <what you're on>)`, updated as you go, then `STATUS: COMPLETE`.
- **Then a title and one line:** which area this covers.
- **Then ONE markdown table**, sorted alphabetically by term:

| Term | Category | Definition | Status | Used in | Sources | Variants and conflicts |
|---|---|---|---|---|---|---|

- **Term:** the name as the most authoritative source writes it. Put an acronym's expansion in the Definition.
- **Category:** one of organization, company, polity, place, era or event, law or rule, robot biology, technology, culture and society, group or people, language, unit or measure, game term, method term.
- **Definition:** one to three plain sentences, in your own words, with no quotations. A table cell can't hold a line break.
- **Status:** `Timeline canon`, `project canon` or `working`. A working term gets a few words on what is unsettled.
- **Used in:** the repos or works that use it, for example `GDD; CurrentNovelDocs (Streetside Harmonies); Timeline`.
- **Sources:** repo plus path of the defining file(s); add a section name if useful.
- **Variants and conflicts:** spellings, alternate names, and any disagreement between repos (which says what, and which is newer). Leave it empty if there are none.

**After the table, add a short "Not included" list:** candidates you judged out that a reader might expect, each with a reason (for example "Calethina: a character").

## Rules
- **Read-only everywhere except your harvest file.** Run no git commands that change anything, and never write to any other repo.
- **American English, plain language.**
- **Resumable:**
  - Create your file early. Add rows as you go and update the STATUS line.
  - If you are resumed or are a replacement agent, read your file's STATUS line and existing rows, and continue. Never restart.
- **Breadth before depth.** A complete set of terms with short, accurate definitions beats a few deep ones.

## When done, reply with
- your file, its STATUS and its row count;
- conflicts between repos that the author should rule on;
- terms whose status or meaning you couldn't establish.
