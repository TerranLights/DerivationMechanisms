# Sync record

This repo holds each mechanism **once**, written to apply everywhere. No folder or file in it says which repo its material came from; that record is kept here, and only here.

## The rules
- **One version per mechanism.** Where copies of the same material had drifted apart, they were combined: whatever one copy had that the others lacked was folded in (author, 2026-10-30). Pure rewordings carry no extra information and were not duplicated.
- **Contradictions stay visible.** Where two copies disagree, the file keeps both readings, marked inline with **⚠️ Versions differ**. All 27 are listed, with suggestions, in `OPEN DECISIONS - Versions Differ (2026-10-30).md`.
- **Copy, don't move.** Nothing was removed from a source repo by this sync. The one exception is the Timeline, which moved its own generic methodology out on 2026-10-30 (its commit `5d15159`).
- **Pointers elsewhere are marked for review, not edited** (author, 2026-10-30). They are listed below.

## Where each mechanism came from
Commits are each source repo's HEAD at the time of the copy. GDD = InnerTepeniaGDD, TL = TepenianUniverseTimeline, CND = CurrentNovelDocs, TFO = TorontoFellOutGDD, Helix = TheCryptographHelixDD.

### Characters
| Here | Came from | How it was built |
|---|---|---|
| `Characters/Enneagram/` | GDD `Worldspace/Enneagram/` (`7daafad7`, 2026-10-29); TL `Worldspace/Characters/Character_Creation_Methodology/Enneagram/` (`e733abf`, 2026-10-29; removed from the TL 2026-10-30) | Combined. The 37 files identical in both copies are kept once. `README.md`, `Triads_Wings_and_Variants.md`, `Enneagram_Dynamics.md` and `Foundations_and_Practice.md` are combined from both. 1 ⚠️ spot. |
| `Characters/Enneagram/Enneagram_Is_the_Starting_Point.md` | Written 2026-10-29 for the TL's Universal Design Laws, then moved here the same day at the author's instruction (it is a mechanism, not lore) | Single source. |
| `Characters/Enneagram/Undercurrents.md` | GDD `Worldspace/Enneagram/Undercurrents.md` (`7daafad7`) | Changed here 2026-10-30: there is no fixed type/Undercurrent ratio (author). The originals still say 80/20; see "Content that now differs" below. |
| `Characters/Character_Development_Methodology/` | GDD `Worldspace/Characters/Dolls/Methodology/`, `Dolls/z-template/`, the two fill-in sheet templates, `Doll_Visual_Design_Canon.md`, both lead sheets, both DRAFT Ideas files, `Characters/Character_Concept_Bank.md` (`7daafad7`, 2026-10-29; refreshed at `c3e31166`, 2026-10-30); TL `Worldspace/Characters/Character_Creation_Methodology/` without its Enneagram folder (`e733abf`; removed from the TL 2026-10-30); CND `reference/character-methodology/`, the prose fork (`d4239ec`) | Combined: 87 files became 52. The GDD copy is the base (the live working copy, and the most complete). The TL's and CND's additions are folded in; their rewordings are not. The Calethina worked example moved out of stages 04 and 05 into `Worked_Examples/`. 7 identical duplicates dropped. 24 ⚠️ spots. |
| `Characters/Robot-specific/Robot_Universals/` | TL `Reference/Robot_Universals/` (`e733abf`; removed from the TL 2026-10-30, which keeps `Reference/Robot_Universals_Summary.md`) | Single source. |
| `Characters/Robot-specific/Doll_Height_Transposition.md` | TL `Reference/Doll_Height_Transposition.md` (`e733abf`; removed from the TL 2026-10-30) | Single source. |

### Data reference
| Here | Came from | How it was built |
|---|---|---|
| `Data_Reference/Symbolism/README.md`, `City_Symbol_Assignments.md` | GDD `…/Cities/City_Symbolic_Substrate/` (`7daafad7`) | Single source. |
| `Data_Reference/Symbolism/Planetary_Symbols/`, `Robot-Elementals/` | GDD `…/Cities/City_Symbolic_Substrate/Planetary_Symbols.md`, `Robot_Elementals.md` (`7daafad7`) | Single source. |
| `Data_Reference/Symbolism/Zodiac/` | GDD `Reference/Real-World/Zodiac_Signs_Full_Attributes.md`; GDD `…/Universal_Location_Methodology/Corpus_Reference_Sheets/Zodiac_Signs_Quick_Reference.md`; GDD `Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/` (22 files) (all `7daafad7`) | Single source per file. |

### Environment
| Here | Came from | How it was built |
|---|---|---|
| `Environment/ULM [Universal Location Methodology]/` | GDD `Worldspace/Locations-and-Levels/Universal_Location_Methodology/` (`7daafad7`; 129 files) | Single source, whole folder as it was. |
| `Environment/RWBEM [Real-World Basis Extrapolation Method]/` | GDD ULM `RWBEM_Progress.md`, `RealWorld_Basis_Input_Availability.md` (`7daafad7`) | Single source. Also inside the ULM folder. |
| `Environment/CST [Cultural Synthesis Techniques]/` | GDD ULM `CST_Progress.md`, `Cultural_Synthesis_Input_Availability.md`, `Disciplines/Cultural_Synthesis_Techniques.md` (`7daafad7`) | Single source. Also inside the ULM folder. |
| `Environment/OOLSD [Object-Oriented Location Synthesis and Derivation]/` | CND `worldbuilding/Object_Oriented_Location_Synthesis/` (`d4239ec`; 93 files); GDD `Worldspace/Locations-and-Levels/Object_Oriented_Location_Synthesis/` (`7daafad7`; 1 file) | Placed together; no file existed in both. |
| `Environment/Local_Robot_Culture_Methodology/` | GDD `…/Cities/Local_Robot_Culture_Methodology/` (`7daafad7`; 4 files) | Single source. The author confirmed it applies everywhere, not only in games. |
| `Environment/Concordia_District_Method/` | GDD `Worldspace/Locations-and-Levels/Concordia-City/Districts/Phase_Instructions/` (15), `Districts/_Method/` (2), `00b_Two_Stage_Methodology.md`, `District_History_Enhancement_Opportunities_Template.md` (`c3e31166`) | Single source. |
| `Environment/Neo-Races_and_Cultures_Method/` | GDD `Neo-Races-and-Cultures/_Method/` (`c3e31166`; 13 files) | Single source. |
| `Environment/Nation_Drawing_Method/` | CND `worldbuilding/METHOD - How Nations Get Drawn.md` (`bd6b1384`) | Single source. |

### Processes
| Here | Came from | How it was built |
|---|---|---|
| `Processes/Canon_Gap_Resolution_Method/` | GDD `Worldspace/Canon_Gap_Resolution_Method/` (`c3e31166`; 11 files) | Single source. |
| `Processes/Research_Protocols/` | GDD `Reference/Real-World/Inspiration_Place_Research/_PROTOCOL_AND_BRIEFS.md`, `_DISPATCH_TEMPLATES.md`, `districts/DISTRICT_LISTS_PROTOCOL.md` (`c3e31166`); CND `worldbuilding/Soil_and_Food_Production/research/_RESUME_PROTOCOL.md` (`bd6b1384`) | Placed together; no file existed in both. |

### Stories
| Here | Came from | How it was built |
|---|---|---|
| `Stories/Story_Structure/story-structure-definitions.md` | CND `reference/story-structure-definitions.md` (`d4239ec`); TL `definitions/README.md` (`e733abf`) | Combined. The CND file is the base; its source lines were corrected here 2026-10-29, so it is ahead of the CND original. From the TL copy: the blank beat-sheet template (now the appendix) and the Fox section's era reading. |
| `Stories/Story_Structure/` (the Snyder, Harmon and Truby extractions, the gap analysis, `_dispatch/`) | Written here, 2026-10-29 | — |
| `Stories/Story_Structure/source_reference (local only, not in git)/` | CND `reference/story-structure-source-videos/` (the Bookfox video and its captions) | Local only; git-ignored here. |
| `Stories/Templates/` | CND `y-template/structure/` (`d4239ec`; 17 files) | Single source. |
| `Stories/Quest_Design/But_Therefore_Quest_Design_Method.md` | GDD `Storyline/DLC-Questlines/` (`c3e31166`); TFO `Storyline/DLC-Questlines/` (`bb5a8ce6`) | Combined. Each game's examples and law lists are kept as labeled variants. |
| `Stories/Quest_Design/DLC_Main_Questline_Design_Method.md` | GDD `Storyline/DLC-Questlines/` (`c3e31166`); TFO `Storyline/DLC-Questlines/` (`bb5a8ce6`) | Combined. 2 ⚠️ spots (candidate count; whether emergence is required). |
| `Stories/Quest_Design/But_Therefore_Lore_Design_Method.md` | GDD `to-be-integrated/` (`c3e31166`, copied 2026-10-30) | Single source. |
| `Stories/Quest_Design/DLC_City_Under_Questline_Design_Method.md`, `District_Under_Questline_Design_Method.md`, `Minmax_Build_Template/` | GDD `Storyline/DLC-Questlines/`, `Storyline/Side-Content/`, `Storyline/Minmax-Builds/z-template/` (`c3e31166`) | Single source. |
| `Stories/Quest_Design/Secret_Endings_Design_Framework.md` | TFO `Storyline/Endings/Secret-Endings/` (`bb5a8ce6`) | Single source. |
| `Stories/Historical_Vignettes/` | GDD `Background-Lore/Cities/Historical_Vignettes_Synthesis_Method.md` (`c3e31166`) | Single source. The vignettes themselves are not canon; this is only the method. |
| `Stories/Continuity/` | Helix `reference/continuity-guidelines.md` (`dc94f4e1`) | Single source. |

### Game design
| Here | Came from | How it was built |
|---|---|---|
| `Game_Design/Design_Principles.md` | GDD `Worldspace/Design_Principles.md` (`c3e31166`); TFO `Worldspace/Design_Principles.md` (`bb5a8ce6`) | Combined. The GDD text is the base; TFO's applications are added as labeled variants. |
| `Game_Design/Forbidden_Trait_Design_Method.md`, `Perk_Framework.md`, `Game_Design_Principles.md` | GDD `Game-Mechanics/Core-Mechanics/`, `Game-Mechanics/Perks/`, `General-Overview-Notes/` (`c3e31166`) | Single source. |

### Glossary
`Glossary/` was built here on 2026-10-30 from a sweep of every repo; its README says how.

## Content that now differs from the original
These are deliberate changes made here. The originals were left as they are.
- **Undercurrent ratio.** This repo's `Characters/Enneagram/Undercurrents.md` and the Enneagram README say there is no fixed ratio (author, 2026-10-30). Still saying 80/20:
  - GDD `Worldspace/Enneagram/Undercurrents.md`, line 26;
  - GDD `Worldspace/Enneagram/README.md`, line 26;
  - TL `Reference/Enneagram_Undercurrents.md`, lines 25 and 53.
- **Story-structure source lines.** This repo's `story-structure-definitions.md` carries the 2026-10-29 source corrections; the CND original does not.

## Pointers in other repos (marked for review)
These files still name a `from …` folder or the old `COPY_MANIFEST (2026-10-29).md`, neither of which exists anymore. The right path in this repo is given for each. Nothing has been edited in those repos: the GDD is edited only when the author asks, and the TL only on an explicit instruction naming it.

### InnerTepeniaGDD: the 📎 lines at the end of method files (35)
Each was added 2026-10-29 and says "nothing was moved; this repo's file stays the working copy". Apart from the path, the review question is whether that sentence still holds, now that this repo holds the combined version.

| GDD file | Line | Path here now |
|---|---|---|
| `…/Cities/Local_Robot_Culture_Methodology/00_DRAFT_Input_Categories_and_Approach.md` | 375 | `Environment/Local_Robot_Culture_Methodology/` |
| `…/Universal_Location_Methodology/05_The_Input_Contract.md` | 823 | `Environment/ULM [Universal Location Methodology]/05_The_Input_Contract.md` |
| `…/Universal_Location_Methodology/00_RUNBOOK.md` | 3179 | `Environment/ULM [Universal Location Methodology]/00_RUNBOOK.md` |
| `…/Universal_Location_Methodology/Datasheet_and_PreTrip_Tracker.md` | 125 | `Environment/ULM [Universal Location Methodology]/Datasheet_and_PreTrip_Tracker.md` |
| `…/Universal_Location_Methodology/Stepwise_Execution/README.md` | 132 | `Environment/ULM [Universal Location Methodology]/Stepwise_Execution/README.md` |
| `…/Universal_Location_Methodology/Location_Data-Input_To-Do.md` | 491 | `Environment/ULM [Universal Location Methodology]/Location_Data-Input_To-Do.md` |
| `…/Universal_Location_Methodology/City_Input_Audit_2026-10-21.md` | 1466 | `Environment/ULM [Universal Location Methodology]/City_Input_Audit_2026-10-21.md` |
| `…/Universal_Location_Methodology/ULM_Piece_Index.md` | 143 | `Environment/ULM [Universal Location Methodology]/ULM_Piece_Index.md` |
| `…/Universal_Location_Methodology/ULM_Run_Progress.md` | 475 | `Environment/ULM [Universal Location Methodology]/ULM_Run_Progress.md` |
| `…/Universal_Location_Methodology/03_The_Phase_Spine.md` | 1200 | `Environment/ULM [Universal Location Methodology]/03_The_Phase_Spine.md` |
| `…/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md` | 928 | `Environment/ULM [Universal Location Methodology]/04_QA_Gates_and_Differentiation.md` |
| `…/Universal_Location_Methodology/Run_Modes_Warm_and_Cold.md` | 180 | `Environment/ULM [Universal Location Methodology]/Run_Modes_Warm_and_Cold.md` |
| `…/Universal_Location_Methodology/06_Worked_Example_Provenance.md` | 431 | `Environment/ULM [Universal Location Methodology]/06_Worked_Example_Provenance.md` |
| `…/Universal_Location_Methodology/RWBEM_Progress.md` | 206 | `Environment/ULM [Universal Location Methodology]/RWBEM_Progress.md` |
| `…/Universal_Location_Methodology/RWBEM_Progress.md` | 206 | `Environment/RWBEM [Real-World Basis Extrapolation Method]/RWBEM_Progress.md` |
| `…/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md` | 1513 | `Environment/ULM [Universal Location Methodology]/DEVELOPER_RULINGS_LOG.md` |
| `…/Universal_Location_Methodology/T8_Standing_Brief_Lines.md` | 40 | `Environment/ULM [Universal Location Methodology]/T8_Standing_Brief_Lines.md` |
| `…/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md` | 806 | `Environment/ULM [Universal Location Methodology]/02_Generators_Capability_and_Symbols.md` |
| `…/Universal_Location_Methodology/README.md` | 243 | `Environment/ULM [Universal Location Methodology]/README.md` |
| `…/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md` | 590 | `Environment/ULM [Universal Location Methodology]/01_Frame_Typology_and_Inheritance.md` |
| `…/Universal_Location_Methodology/Test_Runs/COLD_RUN_CHECKLIST.md` | 443 | `Environment/ULM [Universal Location Methodology]/Test_Runs/COLD_RUN_CHECKLIST.md` |
| `…/Universal_Location_Methodology/Test_Runs/RESUME_HERE.md` | 808 | `Environment/ULM [Universal Location Methodology]/Test_Runs/RESUME_HERE.md` |
| `…/Universal_Location_Methodology/Test_Runs/RUN_LOG.md` | 505 | `Environment/ULM [Universal Location Methodology]/Test_Runs/RUN_LOG.md` |
| `…/Universal_Location_Methodology/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | 8586 | `Environment/ULM [Universal Location Methodology]/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` |
| `…/Universal_Location_Methodology/PRE-TRIP_INSPECTION_RECIPE.md` | 249 | `Environment/ULM [Universal Location Methodology]/PRE-TRIP_INSPECTION_RECIPE.md` |
| `…/Universal_Location_Methodology/Disciplines/README.md` | 126 | `Environment/ULM [Universal Location Methodology]/Disciplines/README.md` |
| `…/Universal_Location_Methodology/MASTER_Process_Tracker.md` | 655 | `Environment/ULM [Universal Location Methodology]/MASTER_Process_Tracker.md` |
| `…/Universal_Location_Methodology/Extent_and_Area_APPROACH.md` | 375 | `Environment/ULM [Universal Location Methodology]/Extent_and_Area_APPROACH.md` |
| `…/Universal_Location_Methodology/City_Input_Gaps_2026-10-27.md` | 96 | `Environment/ULM [Universal Location Methodology]/City_Input_Gaps_2026-10-27.md` |
| `…/Universal_Location_Methodology/ULM_At_A_Glance.md` | 68 | `Environment/ULM [Universal Location Methodology]/ULM_At_A_Glance.md` |
| `…/Universal_Location_Methodology/CST_Progress.md` | 237 | `Environment/ULM [Universal Location Methodology]/CST_Progress.md` |
| `…/Universal_Location_Methodology/CST_Progress.md` | 237 | `Environment/CST [Cultural Synthesis Techniques]/CST_Progress.md` |
| `…/Universal_Location_Methodology/Mechanical_Extraction_Field_Guide.md` | 505 | `Environment/ULM [Universal Location Methodology]/Mechanical_Extraction_Field_Guide.md` |
| `Worldspace/Characters/Dolls/Methodology/00_Overall_Process_Scaffold.md` | 221 | `Characters/Character_Development_Methodology/Pipeline/` |
| `Worldspace/Enneagram/README.md` | 72 | `Characters/Enneagram/` |

### InnerTepeniaGDD: pointers to the old copy manifest (6)
Each says "see its `COPY_MANIFEST (2026-10-29).md`". It should now say `SYNC_RECORD.md`.

| GDD file | Line |
|---|---|
| `DONE.md` | 496 |
| `TODO.md` | 1827 |
| `CLAUDE.md` | 212 |
| `Dev-Road-Map/Location_and_Culture_Build_Tracker.md` | 209 |
| `Dev-Road-Map/November_To-Do.md` | 170 |
| `Dev-Road-Map/Weekly_To-Do_-_Current.md` | 985 |

### TepenianUniverseTimeline (5)
| TL file | Line | Path here now |
|---|---|---|
| `Reference/Doll_Representation_Categories.md` | 12 | `Characters/Robot-specific/Robot_Universals/` |
| `Reference/Robot_Universals_Summary.md` | 4 | `Characters/Robot-specific/Robot_Universals/` |
| `Worldspace/Characters/Dolls/Maggie Aarden/Personal_Background/Relationships.md` | 8 | `Characters/Character_Development_Methodology/Design_Principles/Placeholder_Naming_Convention.md` |
| `Worldspace/Characters/Dolls/Jasmine Blakeley/README.md` | 3 | `Characters/Character_Development_Methodology/Rapid_Intake/` |
| `Worldspace/Characters/Dolls/TBN [TCY-42 ravishing extravagant Lillian]/README.md` | 32 | `Characters/Character_Development_Methodology/Pipeline/03_Character_Data.md` |

## Not copied yet
The author is still deciding on these, so they stay where they are:
- the `methodology-observations/` folders of the language repos (TepenianHawaiian, slang-synthesis);
- Hybrid-Anthro_Culture's `methods/` and `methodology-observations/`.

## Left out on purpose
- **Copyrighted books and media.** Anything a source repo git-ignores was left out: book scans, PDFs, EPUBs, video and audio. That includes CND's `reference/character-methodology/source-books/` and the GDD's zodiac and Enneagram book folders. This repo is public.
- **Generated files.** Graph caches (`graphify-out/`) and Python caches (`__pycache__/`).

## Still open (for the author)
1. **Method versus project data.** Some folders still mix the method with one project's run data: the ULM folder (city audits, trackers, the Santa Luce scenario), the Canon Gap Resolution Method (its registry, log and ruling queue), the Neo-Races method (Phase 1c test runs, subnet summaries, trackers), the per-city symbol assignments, and the character methodology's worked examples.
2. **Deliberate duplicates.** The RWBEM and CST files and the zodiac quick-reference sheet also sit inside the ULM folder, so each folder holds its own material.
3. **A setting-agnostic pass on the character methodology.** The combined files keep the GDD's game- and Tepenia-specific wording wherever the other copies only reworded it. Rewriting it to read the same in any setting and medium would be new work.
4. **Links that only work inside the source repo.** About 90 relative links in copied GDD material still point at GDD locations that don't exist here, mostly in the Concordia district method, ULM, CST, the Canon Gap Resolution Method and the research protocols. They were already broken in the first copies. Fixing them goes with item 1, because many point at Inner Tepenia's own run data.
