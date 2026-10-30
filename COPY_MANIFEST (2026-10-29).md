# Copy manifest (2026-10-29)

**Copied, not moved,** at the author's instruction. Every original is untouched in its own repo, and those repos stay the working copies until the author decides otherwise. Each destination folder has a `COPIED_FROM.md` naming the source path, the source repo's commit (HEAD) and the file counts. **484 files** that can be committed, plus 6 local-only files (one `COPIED_FROM.md` per destination folder besides).

## What went where
| Destination | Source |
|---|---|
| `Characters/Enneagram/from InnerTepeniaGDD/` | GDD `Worldspace/Enneagram/` (60 files, the canonical set) |
| `Characters/Enneagram/from TepenianUniverseTimeline/` | Timeline `Worldspace/Characters/Character_Creation_Methodology/Enneagram/` (41) |
| `Characters/Character_Development_Methodology/from InnerTepeniaGDD/` | GDD `Worldspace/Characters/Dolls/Methodology/` and the two DRAFT Ideas files (14) |
| `Characters/Character_Development_Methodology/from TepenianUniverseTimeline/` | Timeline `Character_Creation_Methodology/`, minus its Enneagram folder (35) |
| `Characters/Character_Development_Methodology/from CurrentNovelDocs/` | `reference/character-methodology/`, the prose fork (21) |
| `Characters/Robot-specific/from TepenianUniverseTimeline/` | Timeline `Reference/Robot_Universals/` and `Doll_Height_Transposition.md` (34) |
| `Environment/ULM [...]/from InnerTepeniaGDD/` | GDD `Universal_Location_Methodology/` (129) |
| `Environment/RWBEM [...]/from InnerTepeniaGDD/` | The RWBEM files from inside ULM (2) |
| `Environment/CST [...]/from InnerTepeniaGDD/` | The CST files from inside ULM (3) |
| `Environment/OOLSD [...]/from InnerTepeniaGDD/` and `from CurrentNovelDocs/` | GDD `Object_Oriented_Location_Synthesis/` (1); CurrentNovelDocs `worldbuilding/Object_Oriented_Location_Synthesis/` (93) |
| `Data_Reference/Symbolism/Planetary_Symbols/` and `Robot-Elementals/` | GDD `City_Symbolic_Substrate/` (1 each) |
| `Data_Reference/Symbolism/from InnerTepeniaGDD (City_Symbolic_Substrate)/` | That folder's README and per-city assignments (2) |
| `Data_Reference/Symbolism/Zodiac/from InnerTepeniaGDD/` | `Zodiac_Signs_Full_Attributes.md`, the Concordia districts' `Zodiac_Personality_Substrate/`, the ULM zodiac quick-reference sheet (24) |
| `Environment/Local_Robot_Culture_Methodology/from InnerTepeniaGDD/` | GDD `.../Cities/Local_Robot_Culture_Methodology/` (4). The author confirmed it applies everywhere, not only in games. |
| `Stories/Story_Structure/from CurrentNovelDocs/` | CurrentNovelDocs `reference/story-structure-definitions.md` (1). Story structures count as mechanisms for creating stories (author). |
| `Stories/Story_Structure/from TepenianUniverseTimeline/definitions/` | Timeline `definitions/README.md` (1). This is the Timeline's synced copy of the story-structure definitions, used for each era's centerpoint. It has drifted from the CurrentNovelDocs version. |
| `Stories/Templates/from CurrentNovelDocs/y-template/structure/` | CurrentNovelDocs `y-template/structure/` (17): the Save the Cat beat sheet, the composite robot arc and Harmon human arc templates, the outline template, the development roadmap. |
| `Stories/Story_Structure/source_reference (local only, not in git)/` | CurrentNovelDocs `reference/story-structure-source-videos/` (6, **git-ignored here**): the Bookfox "middle of a novel" video and its auto-captions. The creator's copyrighted material; never committed. |

## What was left out, and why
- **Copyrighted books.** Anything the source repo git-ignores was left out. That includes the copyrighted book scans in CurrentNovelDocs' `reference/character-methodology/source-books/`. No book or media file (PDF, EPUB, video, audio) was copied; the GDD's zodiac and Enneagram book folders were not touched. This repo is public.
- **Generated files.** Graph caches (`graphify-out/`) and Python caches (`__pycache__/`).

## Not copied yet
The author is still deciding on these, so they were left in place:
- the `methodology-observations/` folders of the language repos, TepenianHawaiian and slang-synthesis;
- Hybrid-Anthro_Culture's `methods/` and `methodology-observations/`.

## Still to sort out (for the author)
1. **One canonical version per method.** The character methodology now sits here three times and the Enneagram material twice, from drifted copies. Each needs merging into one.
2. **Method versus project data.** The ULM copy still mixes the method with Inner Tepenia's own run data: city audits, trackers, the Santa Luce scenario. The same goes for the Timeline's `Tepenia_Worked_Examples/` and the per-city symbol assignments.
3. **Deliberate duplicates.** The RWBEM, CST and zodiac files also sit inside the ULM copy. They were duplicated so each folder holds its own material.
4. **Pointers.** Once this repo becomes the canonical home, the pointers in the Timeline (`Universal Design Laws/`, `Reference/Repo_Scope.md`) and in the projects' files need updating.
