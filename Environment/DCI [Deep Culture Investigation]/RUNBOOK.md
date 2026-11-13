# DCI runbook: the same procedure for every target culture

STATUS: v1.1 (2026-11-10). Written before the pilot (Cascadia); corrected as the pilot runs.

Every target culture goes through the same eight stages, in the same order, with the same templates. Nothing in this file is specific to any one culture. DCI is a full, in-depth cultural investigation.

## Terms
- **Target culture:** a successor nation as named in the Census I origin table (for example, Cascadia).
- **Unit:** a regional culture inside a target's stock, the thing actually researched. In settler regions it is a regional culture founded by a first effective settlement (for example, Woodard's Left Coast). Elsewhere it is a tier-1 or tier-2 ethnic identity. Indigenous peoples are units in their own right.
- **The unit library:** each unit is researched once and stored once. A unit that spans several targets (Woodard's Far West lies in Cascadia, Colorado and others) is reused, not repeated. Each unit file says which target's part of the unit (its lobe) the research was written from; a later target that shares the unit adds its own lobe rather than starting over.
- **Unit territories:** each unit's counties, census divisions or *municipios* are recorded once in the results root's `Data/Unit_Territories.md`.

## Where things live
- **This folder (the method):** this runbook, `README.md`, `Templates/`, `Shared/` (concept lists, the investigation sheet and the avenues of investigation, source types, crosswalks, the source registry, the regional frameworks index) and `_dispatch/` (the agent brief template and resume procedure).
- **The results root:** for now, CurrentNovelDocs `worldbuilding/Deep_Culture_Investigation/`. Once the methodology is sorted, it moves into this repo (author, 2026-11-02). Raw datasets downloaded for the work go in CurrentNovelDocs `worldbuilding/data/`, which is git-ignored. The results root holds:
  - `MASTER TRACKER.md`;
  - `Units/<unit>/` (the unit library);
  - `Targets/<target>/`;
  - `Data/` (extracted values from datasets, with citations; raw datasets stay out of git);
  - `_dispatch/` (the briefs actually sent, with their STATUS checks).

## The stages
| # | Stage | Done per | Kind | Template | Output |
|---|---|---|---|---|---|
| 0 | **Scope** | target | research; the author settles flagged choices | `T0_Scope.md` | `Targets/<target>/00 - Scope.md` |
| 1 | **Lineage profiles** | unit | research | `T1_Lineage_Profiles.md` | `Units/<unit>/01 - Lineage/` (one file per profile) |
| 2 | **Measured data** | unit | research | `T2_Measured_Data.md` | `Units/<unit>/02 - Measured data.md` |
| 3 | **Five axes** | unit | research | `T3_Five_Axes.md` | `Units/<unit>/03 - Five axes.md` |
| 4 | **Sign passes,** one sign at a time from Aries to Pisces | unit | research | `T4_Sign_Pass.md` | `Units/<unit>/04 - Signs/NN - <Sign>.md` |
| 5 | **Composite** | target, after each sign | research | `T5_Composite.md` | `Targets/<target>/05 - Composite/NN - <Sign>.md` |
| 6 | **Divergence** (the post-war order first) | target | **derivation: 05:00-14:59, the author decides** | `T6_Divergence.md` | `Targets/<target>/06 - Divergence/` (`00 - Post-war order.md`, then one file per sign) |
| 7 | **Verification** | every output | check | `T7_Verification_Checklist.md` | a `VERIFIED` line in the file's STATUS |

The pilot order (author, 2026-11-02): Stage 0 for Cascadia; Stages 1-3 for its units; then Stage 4 and Stage 5 sign by sign, starting with Aries.

### Stage 0: Scope
Answer, for the target:
1. **Territory:** the pre-war states, provinces and countries it covers (from the world nations roster and the territory definitions), and the Indigenous nations within it.
2. **Units:** the regional cultures inside it, from the regional frameworks index (`Shared/Regional_Frameworks.md`). For each: core, domain or sphere within the target; the founding population (first effective settlement) or tier-1 and tier-2 identities; later layers; Indigenous peoples.
3. **Weights:** the founders first, then present-day population shares as corroboration. Where the two disagree, flag it.
4. **Seams:** where units meet inside the target.
5. **Scope statement:** which smaller distinctions are left out, and why, stated explicitly.
6. **Era checkpoints** the work needs (for example, a novel's year, or the year of exile to Tepenia). The author confirms.
7. **Existing project material to read first,** listed with paths. Earlier proposals marked "author decides" are inputs, not canon.
8. **Decisions for the author,** numbered, each answerable in a sentence.

Throughout sections 1 and 2, note which units already exist in the unit library and can be reused. Stage 0 may also write `Data/Unit_Territories.md`.

The author confirms the unit list before Stage 1.

### Stage 1: Lineage profiles
Eleven profiles per unit, each answering **what it is based on and where it came from**, with sources: family system, kinship intensity, religious lineage, subsistence, land and inheritance, political culture, education, language, stories, song, formative events.

### Stage 2: Measured data
Values from the datasets in `Shared/Sources_and_Datasets.md`, at the finest level available (county, state, province or country), each with its year, sample and citation. A value for a whole country is never presented as a unit's value without saying so.

### Stage 3: Five axes
Woodard's five core axes, as a quick first reading of the unit: authority and hierarchy; individual against communal; the kind of religious worldview; equality against deference; economic base.

### Stage 4: Sign passes
**Before each sign, settle its concept list with the author:** the near-synonyms and duplicates flagged for that sign in `Shared/Concept_Lists_by_Sign.md`. Recording the author's answer can happen at any hour.

For each concept on the sign's list, and each unit, work through `Shared/Investigation_Sheet.md`, with the concept's own avenues and source types from `Shared/Avenues/NN - <Sign>.md`. Then cover the sign's folkways from `Shared/Folkways_Crosswalk.md`.

Rules:
- **Founders first:** give the founding culture's understanding, then the later layers.
- **Honest null:** if nothing distinct exists, say so on its own line.
- **Variation is required** in every entry.
- **Tag every claim:** measured, official, scholarly, synthesis, classic, practitioner or claim (defined in `Shared/Sources_and_Datasets.md`).
- **Disagreements between sources are recorded, not resolved.**

### Stage 5: Composite
For each concept, combine the target's units into four parts: **dominant, shared floor, outliers (the seams, named), confidence.** Never average away a seam. Weigh by founders first, with population as corroboration, and say which weighting was used.

### Stage 6: Divergence
How the 2083 war, statehood and the time since changed each composite reading, at each era checkpoint. **Derivation:** only 05:00-14:59, proposals marked PROPOSED, and the author decides. The No National Stereotypes rule applies: the stock is where a people started; time and place make the culture.

**The post-war order comes first,** as its own part of Stage 6. Once the pre-war country is no longer one connected whole, each successor nation sets itself up as it sees fit (author, 2026-11-02). Starting from the units' lineage profiles, decide for each area of life (family and kinship; religion and belief; economy and work; land and property; education; language; the arts, stories and song; community life; government; security):
- what it kept, blended or replaced;
- whose culture shaped it (founders first: the culture that built the new state's institutions);
- how the minority units fare inside it.

### Stage 7: Verification
Run `Templates/T7_Verification_Checklist.md` on every output before its STATUS says done.

## Running it with agents
- **One job = one unit × one stage**, or one unit × one sign at Stage 4. Small enough to finish and resume.
- **Briefs** are written from `_dispatch/BRIEF_TEMPLATE.md` and saved in the results root's `_dispatch/` before launch.
- **Every working file** has a `STATUS:` line as its first line, updated at each checkpoint (`STATUS: in progress, section N of M`).
- **Resume** per `_dispatch/RESUME.md`.
- **Waves:** run four or five agents at a time. The session's web-search cap (1,000 by default) is shared by all of them, so a wave's budgets must fit what's left in the session; a large stage may need a fresh session (pilot, 2026-11-03).

## Standing rules
- **American English.**
- **Native, Indigenous or Aboriginal, never "Indian"** (author, 2026-11-10, out of respect for the Indigenous peoples and nations of this land); in Canada also First Nations, Inuit or Métis. Published titles and names, a nation's own name, quotations and census category names stay as published; an official term that uses the word is described in our own words, with the term given once in quotes.
- **No South Asian works as sources.** A modern study that would be set aside only because of an author's name goes in a `held_for_review_*.md` file for the author.
- **Both kinds of authority count:** classics that have lasted, and modern scholarship. Neither outranks the other.
- **No national stereotypes.** Variation is part of every answer; a people is never one voice.
- **The signs are research classifiers only.** Nothing zodiac-derived appears in fiction.
- **The results repo is public:** short quotations only (a sentence or less), with citations; no copyrighted books, raw datasets or third-party images in git.
- **Hours:** Stages 0-5 and 7 are research (any hour); Stage 6 is derivation (05:00-14:59).
