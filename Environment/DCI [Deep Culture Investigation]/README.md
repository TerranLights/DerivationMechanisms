# DCI: Deep Culture Investigation

STATUS: method v1 (2026-11-02). All proposals adopted by the author; the repeatable system is in place (see "The system"). No research has run yet. The pilot is Cascadia.

## The system
| File | What it is |
|---|---|
| `RUNBOOK.md` | **The procedure:** eight stages, the same for every target culture. Start here. |
| `Templates/` | One template per stage (`T0`-`T7`), plus the master tracker and the per-target tracker |
| `Shared/Concept_Lists_by_Sign.md` | The concepts researched under each sign, in tiers, with what to settle before each sign |
| `Shared/Folkways_Crosswalk.md` | Fischer's 24 folkways placed under the signs (placements proposed) |
| `Shared/Sources_and_Datasets.md` | The source registry: datasets, lineage sources and qualitative sources |
| `Shared/Regional_Frameworks.md` | Which framework defines the units in each world region |
| `Shared/Investigation_Sheet.md` | **The step-by-step sheet for Stage 4:** how to investigate each meta-category and each of its concepts, through every angle (draft v0, for the author to review) |
| `Shared/Avenues/` | **Every avenue of investigation for each concept,** one file per sign (`01 - Aries.md` to `12 - Pisces.md`), making the investigation sheet specific to each concept (draft v0, 2026-11-10). Law is researched only in Libra (the letter of the law) and Capricorn (the spirit of the law); each has a companion file holding the law avenues moved there from the other signs |
| `Shared/Source_Types.md` | **The kinds of sources** that record how a culture understands its concepts, grouped by how widely they exist (everywhere; writing; the state; mass media; online; outsiders; scholarship and data). Each concept's own source types are in its avenue file (draft v0, 2026-11-10; Aries done) |
| `Shared/Regional_Appendix_North_America.md` | The pilot region's languages, dictionaries, archives, the nations' own sources and datasets, kept out of the investigation sheet so that the sheet stays the same everywhere |
| `Shared/held_for_review_Sources.md` | Sources set aside for the author's ruling under the rule against South Asian works |
| `Shared/Permission_Share_List.md` | The fixed activity list and scoring for the permission share, the author's measure of the libertarian-authoritarian axis (draft v0, for the author to settle) |
| `_dispatch/` | The agent brief template and the resume procedure |

This README explains what DCI is and why it works the way it does; the runbook says how to run it.

## What it is
A compartmentalized series of categories for understanding a particular culture (author, 2026-11-02): how the people of that culture interpret, understand and approach concepts such as reciprocity, recognition, responsibility, idealism, learning, security, leadership and competition.

- **Categories:** the twelve zodiac signs are the top-level categories. The concepts under each sign are its subcategories. Both are bouncing-off points for investigating how a culture understands and processes each thing.
- **The signs are research classifiers only.** Nothing zodiac-derived appears in any fiction.
- **Scope:** every nation represented in the Tepenian Federation, each at full depth (author). The work is expected to take months.
- **Two lists, both researched** (author):
  - the **pre-war countries** the exiles came from, as the real-world stock that is researched;
  - the **post-war successor nations** (as the census now names them), as the layer derived from that stock.

## Inputs
- **The concept list:** the per-sign concept tables and the merged index in CurrentNovelDocs `worldbuilding/Robot_Fundamental_Concepts/` (`02 - Concepts/00 - Concept index (2026-10-30).md`, which also holds each sign's ten most central concepts).
- **The nations:** the Census I origin table in the Inner Tepenia GDD, `Official_Population_Census.md`. As of 2026-11-02 it lists 81 nations, plus Sicilia (an autonomous zone within Meridia) and the southern Ontario DMZ (not a nation).
- **The source peoples of each successor nation:** the world nations roster and the regional map research in CurrentNovelDocs `worldbuilding/`.
- **Rules that bind this work:**
  - No National Stereotypes: who a people descend from tells you where they started; time and place make the culture.
  - No South Asian works as sources.
  - Two kinds of source authority, neither ranked above the other: classics that have lasted, and modern scholarship.

## 1. What to know
### 1a. The concepts, in tiers
The full matrix is about 1,000 concepts for each nation, so the work goes in order:
- **Tier 1:** each sign's ten most central concepts (120).
- **Tier 2:** the concepts that appear under six or more signs (60).
- **Tier 3:** the rest, pulled in where a culture turns out to have something distinct.
- **First:** settle the near-synonym groups listed in the concept index, so nothing is researched twice under two names. Drop anything that exists only in astrology (decans, rulerships and the like).

### 1b. The same questions for every concept in every culture
- **Words:** what the language calls it, including words with no English equivalent.
- **Value:** whether it is admired, feared, mocked or taken for granted.
- **Practice:** how it shows in daily life, customs and institutions.
- **Breach:** what happens when someone fails at it (shame, guilt, gossip).
- **Sayings:** proverbs and idioms.
- **Exemplars:** the figures and stories that embody it.
- **Variation:** by region, class, generation, gender and religion, and who disagrees.
- **Change:** what is shifting now.

### 1c. Rules
- **Honest null:** if a culture has nothing distinct for a concept, the entry says so on its own line instead of forcing a match.
- **Variation is always required.** A nation is never one voice.
- **Tag every finding by kind of evidence:** measured, official, scholarly, synthesis, classic, practitioner or claim. Record disagreements between sources instead of resolving them.

## 2. Where to find it
Sources from strongest to weakest:

| | Kind | Examples |
|---|---|---|
| A | **Measured cross-national data.** One pass covers every nation at once. | Global Preferences Survey (reciprocity, trust, patience, risk, altruism); World Values Survey and European Values Study (trust, faith, work, family, raising children); Hofstede and the GLOBE study (authority, achievement, assertiveness, care); Gelfand's tight and loose cultures (rules, order, duty); honor, dignity and face research; Trompenaars (universal rules against personal ties); corruption indexes; display-rule studies of emotion |
| B | **The language itself** | native words, untranslatables, proverb collections; searching in the language |
| C | **The culture's own classics and scholarship** | each culture's canonical texts about itself |
| D | **Ethnography** | the Human Relations Area Files, searched by the Outline of Cultural Materials categories |
| F | **Practitioner guides** | country culture guides; used last |

**To build:** a crosswalk file mapping each concept to the measures and the Outline of Cultural Materials categories that cover it.

**Successor nations with no sources under their own names** take two steps:
1. **Source peoples (research, any hour):** list the real-world peoples and regions the nation grew from, and research those with the kinds above.
2. **Divergence (derivation, 05:00-14:59, the author decides):** how the 2083 war, statehood and the centuries since changed each answer.

## 3. The lineage profiles (adopted 2026-11-02)
Each profile asks what a part of the culture is based on and where it came from. Each is one per regional culture, and most have data below the national level.

| Profile | What it asks | Signs it feeds | Where to find it |
|---|---|---|---|
| **Family system** | Do married children live with their parents? Is inheritance split equally among siblings or not? | Cancer, Scorpio, Capricorn, Aquarius | Emmanuel Todd's family types (*The Explanation of Ideology*; later world-wide work), mapped by region |
| **Kinship intensity** | Clans, cousin marriage, lineages: how far loyalty to kin outranks strangers and rules | Scorpio (trust), Libra (justice, partiality), Aquarius | Murdock's *Ethnographic Atlas* by ethnic group (in the D-PLACE database); Schulz and Henrich's kinship-intensity index; Henrich, *The WEIRDest People in the World* |
| **Religious lineage** | Tradition, branch and school (for example, a denomination and its schools), plus folk layers | Sagittarius, Pisces, Scorpio (death rites) | ARDA, Pew, the World Religion Database; census religion data by region |
| **Subsistence lineage** | What the ancestors lived by: herding, rice, wheat, plow farming, fishing, plantation, mining, frontier ranching | Leo and Aries (honor, anger), Aquarius, Taurus, Virgo | Measured links: herding and honor culture (Nisbett and Cohen, *Culture of Honor*); rice against wheat (Talhelm 2014); frontier exposure and individualism by U.S. county (Bazzi, Fiszbein and Gebresilasse 2020); the plow and gender roles (Alesina, Giuliano and Nunn 2013) |
| **Land and inheritance** | How land was held and passed on: primogeniture or partible inheritance, communal tenure, homesteads, land grants | Taurus, Scorpio, Cancer | Land-tenure histories; for the pilot candidates: Mexico's *ejidos*, Spanish and Mexican land grants in California, Alaska Native corporations (ANCSA, 1971) |
| **Political culture** | How authority, participation and the public good are understood | Capricorn, Aquarius, Libra | Elazar's three American political cultures (moralistic, individualistic, traditionalistic); Woodard's *American Character* |
| **Education lineage** | Which school and university models it follows | Gemini, Sagittarius, Virgo | Histories of national school systems |
| **Language lineage** | The language family; which outside languages supplied its words for money, religion and so on; which concepts share one word | Gemini, and the Words question for every concept | the World Loanword Database; etymological dictionaries; the CLICS colexification database (Jackson et al. 2019 used it for emotion words across about 2,400 languages) |
| **Story lineage** | Which tale types and myth motifs a people carry | Leo, Sagittarius, Pisces; the Exemplars question | the Aarne-Thompson-Uther tale-type index; Thompson's *Motif-Index*; Berezkin's mapped catalog of mythological motifs |
| **Song lineage** | Song style and the social structure it goes with | Leo, Aquarius | Lomax's Cantometrics (the Global Jukebox) |
| **Formative events** | The wars, famines, revolutions and colonizations whose effects are measured centuries later | Scorpio, Capricorn | the persistence literature: Dell on the mining *mita* (already in the Latin America survey), Nunn and Wantchekon on the slave trade and mistrust, Guiso, Sapienza and Zingales on Italian free cities and civic capital |

**Fischer's folkways.** David Hackett Fischer's *Albion's Seed*, one of Woodard's own sources, describes four founding British cultures through 24 "folkways" (speech, building, family, marriage, gender, sex, child-rearing, naming, age, death, religion, magic, learning, food, dress, sport, work, time, wealth, rank, social, order, power and freedom ways). It is the closest existing precedent for DCI: his chapters on freedom give one concept four different regional meanings. **Adopted:** the 24 folkways are a second checklist, crosswalked to the twelve signs in `Shared/Folkways_Crosswalk.md` (placements proposed, settled sign by sign).

## 3b. The map method's principles, applied (adopted 2026-11-02)
The nation maps were drawn on Woodard's *American Nations* and the regional frameworks built for the rest of the world (`Nation_Drawing_Method/`; the regional surveys in CurrentNovelDocs `worldbuilding/extractions/`). Applied to DCI:

1. **The research unit is the regional culture, not the country.** A successor nation is researched as the regional cultures it contains. National political borders are reference lines only.
2. **Founders first.** By the Doctrine of First Effective Settlement, the first group to build a lasting society sets the template that later arrivals assimilate into. Research the founding culture's understanding of each concept first, then the later layers.
3. **Where there was no founding settlement** (East Asia, Russia, Central Asia and most of the old world), use tiered ethnic identity instead: tier 1 the major grouping, tier 2 the identities within it. Tier 2 is evidence to compress, not a list to honor.
4. **Present-day data corroborates; it doesn't decide.** Where the founding culture's reading and today's survey data agree, the finding is solid. Where they disagree, it is a decision for the author.
5. **Independent convergence:** two unrelated sources reaching the same reading is the strongest evidence.
6. **Zones, not lines.** Each regional culture has a core, a domain and a sphere. Border areas under several cultures at once are recorded as such.
7. **Seams are marked, not resolved.** Where a concept splits inside a nation, record both readings and don't average them. Use the four-part value from the per-subnet personality guide: dominant, shared floor, outliers, confidence.
8. **Indigenous peoples are cultures in their own right,** researched on the same footing, not background.
9. **Environment-defined cultures** (Woodard's Far West; Alaska) are researched for how a hostile land shapes the concepts.
10. **Each region's own frameworks supply its units:** for example, Ribeiro's Brazils and Wagley's culture spheres for Latin America; Lattimore, the Hu Line and Skinner's macroregions for East Asia; the mandala and the massif for Southeast Asia; tiered ethnicity for Russia and Central Asia.
11. **Woodard's core axes first, as a quick pass:** attitude to authority and hierarchy; individual against communal; the kind of religious worldview; equality against deference; economic base. They map onto Capricorn, Aquarius, Sagittarius, Libra, and Taurus and Virgo.

## 4. Order of work
See `RUNBOOK.md`. In short: scope the target; build lineage profiles, measured data and the five axes for each unit; then go sign by sign from Aries to Pisces, combining the units after each sign; divergence into the successor nation is the author's, in the morning window.

## 5. Decisions (author, 2026-11-02)
- The zodiac signs are the categories and their concepts the subcategories.
- Research every nation represented in the Tepenian Federation.
- Both lists: pre-war countries as the researched stock, successor nations as the derived layer.
- Every nation at full depth, including the smallest populations.
- The pilot is a nation where the first novels are set: **Cascadia** (chosen 2026-11-02).
- **All proposals adopted:** the lineage profiles, Fischer's folkways, and the map-method principles ("Everything here is useful").
- **The signs are worked one at a time, in order, starting with Aries.**
- **A structured, repeatable system** is required before any research, the same for every target culture (`RUNBOOK.md`).
- **Results live in CurrentNovelDocs `worldbuilding/Deep_Culture_Investigation/` for now,** and move into this repo once the methodology is sorted.

## 6. Open
- **The name:** "Deep Culture" is also the hidden layer of Hall's cultural iceberg (`../Neo-Races_and_Cultures_Method/Cultural_Iceberg_Method.md`). Is the overlap intended?
