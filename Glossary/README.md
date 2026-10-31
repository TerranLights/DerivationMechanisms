# Glossary

**What this is** (author, 2026-10-30): a dedicated glossary holding definitions of essentially every term that any of the repos needs access to. That includes organizations, robot-fabrication megacorporations, substances, technologies, and coined words in general, from every project and medium.

**How it's organized:**
- **One file per starting letter** (`A.md`, `H.md`, ...). A file is created when its first entry arrives. Entries within a file are alphabetical.
- **The category index below** lists every term by kind.

## Entry format
```
### Term
- **Category:** what kind of thing it is
- **Also called:** other names, former names and spellings (only if there are any)
- **Definition:** one to three plain sentences
- **Status:** how settled it is (see below)
- **Used in:** the repos and works that use it
- **Sources:** where the definition comes from, by repo and path
- **Open:** unsettled points, conflicts between repos, naming variants (if any)
```

**Status levels:**
- **Timeline canon:** recorded in the TepenianUniverseTimeline repo.
- **Project canon:** ruled by the author in a project repo, not yet in the Timeline.
- **Working:** proposed or unsettled. The definition says what is and isn't decided.

**Rules:**
- **Every definition comes from a source in the repos, or from the author.** Nothing is invented here.
- **Where repos disagree,** the entry records both versions and says which is newer. It does not pick one.
- **The glossary defines; it does not develop.** New detail is worked out in its home repo, then the entry is updated.

## Kept elsewhere
- **Individual characters** have their own character files.
- **Story-structure terms** (Save the Cat beats, Truby's steps, Harmon's circle) are in `../Stories/Story_Structure/`.
- **Enneagram terms** are in `../Characters/Enneagram/`.
- **Cryptograph Helix world details** (places, societies, factions) are held out for now, because the series predates the Tepenian universe and much of it will change (author, 2026-10-30). The held terms are listed in `_merge/*.progress.md`. Its navigation system (TANA and related terms) is included.

## How it was built
The 2026-10-30 sweep worked in three stages:
1. **Harvest:** ten agents each covered one area of the repos. Their raw tables (`_harvest/`) are kept locally, not in git.
2. **Merge:** six agents merged the results by letter range. Their progress files (`_merge/*.progress.md`) list every merge, drop and hold, and the conflicts between repos; the raw merge inputs are kept locally.
3. **Finish:** a script built the cross-reference stubs and the category index.

The tooling, briefs and resume steps are in `_dispatch/`. Every conflict found between repos is collected in `OPEN CONFLICTS (2026-10-30).md` for the author to rule on; each is also under **Open** in its entry.

## Path shorthand in Sources
Some entries shorten long InnerTepeniaGDD paths:

| Shorthand | Full path in InnerTepeniaGDD |
|---|---|
| `Cities/` | `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/` |
| `Specs/` | `Cities/Specs/` (as above) |
| `Infrastructure/` | `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/` |
| `Districts/` | `Worldspace/Locations-and-Levels/Concordia-City/Districts/` |
| `ULM/` | `Worldspace/Locations-and-Levels/Universal_Location_Methodology/` |
| `BL/` | `Background-Lore/Cities/` |
| `.../` | a path shortened in the middle; search the repo for the file name |

## Category index
<!-- INDEX START -->
**1607 entries** in 27 letter files, plus 578 cross-reference stubs for alternate names. The full list by category is `CATEGORY INDEX.md`.

| Category | Entries |
|---|---|
| Organization | 36 |
| Company | 7 |
| Polity | 65 |
| Place | 201 |
| Era or event | 63 |
| Law or rule | 20 |
| Robot biology | 30 |
| Technology | 53 |
| Culture and society | 215 |
| Group or people | 162 |
| Language | 4 |
| Unit or measure | 16 |
| Game term | 342 |
| Method term | 393 |
<!-- INDEX END -->
