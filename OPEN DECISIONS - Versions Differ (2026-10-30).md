# Open decisions: where combined copies disagree (2026-10-30)

When the drifted copies of each mechanism were combined, every spot where they contradict each other kept both readings and got an inline **⚠️ Versions differ** mark. There are **27**, listed here so they can be decided in one pass. Many of them repeat the same question in several files, so they are grouped into **12 decisions**.

- **Version labels** are the ones used in the files: the **game version** (the base of most combined files), the **prose version** (written for linear, fixed-length books) and the **medium-agnostic version** (with project-specific terms stripped out). Which repo each came from is in `SYNC_RECORD.md`.
- **Paths:** `CDM/` = `Characters/Character_Development_Methodology/`. Line numbers are as of 2026-10-30.
- **"Suggested"** lines are only suggestions. Nothing is decided until the author says so.
- **Once a decision is made,** the file gets the chosen reading and its ⚠️ mark is removed.

---

## A. Does the character methodology stay game-flavored, or become setting-agnostic? (5 spots)
The combined files are built on the game version, so they still name one project's mechanics, files and characters. The medium-agnostic version had stripped those out; the prose version had moved them aside.
1. `CDM/README.md:12`, intro: the combined Pipeline carries that project's terminology, mechanics (stat checks, perks, companion questlines) and named-character illustrations.
2. `CDM/README.md:149`, "What Makes This Actually Portable": the portability bullets describe the medium-agnostic version, not the combined text.
3. `CDM/Pipeline/00_Overall_Process_Scaffold.md:19`, Portability note: the medium-agnostic version says nothing assumes a universe or medium, but the combined text does.
4. `CDM/Worked_Examples/Calethina_Case_Study.md:13`, intro: the medium-agnostic version describes the mechanics in general terms; the game version names them (Fragmentation Matrix, Pariah Failsafe, the Double Gate, re-spec visits, 13 districts).
5. `CDM/Worked_Examples/README.md:30`: the medium-agnostic case study left the game mechanics out; the combined one keeps them.

- **Suggested:** a setting-agnostic pass over the Pipeline, with the game-specific illustrations kept as clearly labeled examples. This is new writing, so it would happen in the 05:00-14:59 window. For the worked examples, keep the full game detail, since they are examples by design.
- **Decision:**

## B. Beat placement: by function only, or by percentage of the manuscript for prose? (4 spots)
The game and medium-agnostic versions place beats by their function, never by a fixed percentage. The prose version adds percentage-of-manuscript placement for a linear book of fixed length.
6. `CDM/README.md:173`, "Time/Length/Span-Based Structure".
7. `CDM/Pipeline/00_Overall_Process_Scaffold.md:74`, the Cross-Cutting non-linear bullet.
8. `CDM/Pipeline/01_Input_Information.md:245`, A7 Standing Design-Law Constraints: the Standing Scope Note versus the percentage skeleton.
9. `CDM/Pipeline/05_Beats_Paths_Results.md:158`, the Midpoint Menu framing: "never a literal 50% timestamp" versus "~50% of the manuscript by default for prose".

- **Suggested:** keep both, scoped by medium, and state the rule once: beats are placed by function in every medium; a linear book of fixed length also uses the percentage skeleton as its placement reference. The Story-Format Gate in `00a` already makes that linear-or-not choice.
- **Decision:**

## C. Are Stage 5's open items still open? (3 spots)
The game version lists three deliberately deferred open items. The prose version says Stage 5 is complete, with none.
10. `CDM/Pipeline/00_Overall_Process_Scaffold.md:209`, the Stage 5 status.
11. `CDM/Pipeline/05_Beats_Paths_Results.md:18`, Status.
12. `CDM/Pipeline/05_Beats_Paths_Results.md:673`, "Open, Undecided".

- **Note:** the game version's own status line says "Two open items remain" but lists three.
- **Suggested:** the author checks the three listed items. Any that are settled come out; any still open stay listed, with the count fixed.
- **Decision:**

## D. Is the Enneagram mandatory, or can another typology substitute? (2 spots)
The game version makes the Enneagram mandatory ("not one option among equals"). The medium-agnostic version lets any well-grounded typology of comparable structure stand in.
13. `CDM/Pipeline/01_Input_Information.md:79`, A2 Enneagram Assignment.
14. `CDM/Pipeline/03_Character_Data.md:149`, "Fields That Stay Standalone", the Enneagram field.

- **Suggested:** mandatory. The design law "Enneagram Is the Starting Point, Not the Result" (2026-10-29) says every character in every project starts from the Enneagram type files.
- **Decision:**

## E. A character's default role (1 spot)
15. `CDM/Pipeline/00a_Initial_Input.md:145`, Section A, A3. Game version: "recruitable, full companion, base game". Prose version: "a major recurring character, appearing throughout", with book or series placement left TBD unless the seed implies it.

- **Suggested:** keep both, scoped by medium: the game default for games, the prose default for books and series.
- **Decision:**

## F. The seed template's Type field (1 spot)
16. `CDM/Pipeline/00c_Quick_Capture_Seed_Template.txt:8`. Game version: "Type: Robot". Medium-agnostic version: "Core nature/type (leave blank if the setting has only one kind of being)".

- **Suggested:** the medium-agnostic wording. The project seed files already list several kinds (Elven Steel: Robot / Elf / Human / Orc / Alien).
- **Decision:**

## G. Trigger-type requirement (1 spot)
17. `CDM/Pipeline/05_Beats_Paths_Results.md:311`, the Trigger-Type Design Pattern. Game version: every companion needs some triggers that aren't tied to a district. Prose version: location-independent triggers are needed only for a character whose presence isn't tied to one place.

- **Suggested:** the general rule from the prose version, plus a note that in a district-based game it covers every companion.
- **Decision:**

## H. Older versus newer facts in the worked material (5 spots)
In each case one copy is newer than the other.
18. `CDM/Pipeline/00d_Quick_Capture_Seed_-_Ready-Made_Partial_Seeds_[rewritable].txt:106`, Calethina's origin. Newer: "stress-testing Contrapunto, shipped via Puerto Abrigo". Older: "stress-testing Sejong, shipped via Port Lockroy".
19. Same file, `:323`, the 5w4 Mirny seed's location. Newer: "Ariun Nuur, East Antarctic Plateau (Mirny subnet)". Older: "Vostok".
20. Same file, `:329`, the same seed's backstory. Newer: "the Mirny DLC's Ariun Nuur content". Older: "Vostok content".
21. `CDM/Worked_Examples/Initial_Character_Lead_Sheet.md:10`, Michelle Stanton. Newer: she operates "a Rastra". Older: "a Kharkovchanka".
22. `CDM/Pipeline/04_Story_Material.md:130`, the Player-Necessity retrofit illustration. Game version: "Vosora's existing Dual-Outcome Perk structure". Prose version: "dual-outcome branch structure".

- **Suggested:** the newer reading in 18-21, which reflect later renames. For 22, the game term in game work and the prose term elsewhere; it is the same illustration.
- **Decision:**

## I. Cartlidge read-depth note (1 spot)
23. `CDM/Source_Material/Character_Development_Methodology_-_Villains_and_Antiheroes_-_DRAFT_Ideas.md:1111`. The medium-agnostic copy ends the Cartlidge section with an earlier note: "read in substantial but not exhaustive depth". The game copy goes on to mine the remaining chapters and closes "now read in full".

- **Suggested:** keep "read in full" and drop the earlier note, which the later work superseded.
- **Decision:**

## J. Section number in the Character Spec sheet (1 spot)
24. `CDM/Templates/Character_Spec_Fill-In_Sheet_Template.md:33`, intro. The game copies say "Section 13 (Role in the Story / Companion Potential)". The medium-agnostic copy says "Section 12 (Role in the Story)". The heading itself is numbered 12 in every copy.

- **Suggested:** "Section 12 (Role in the Story / Companion Potential)", which matches the heading.
- **Decision:**

## K. What the Enneagram lookup table was built for (1 spot)
25. `Characters/Enneagram/Foundations_and_Practice.md:62`, the QUEST section. One version: the Hornevian/Harmonic lookup table was built for `seed-to-README-process.md`. The other: it was built for the Stage 1-5 character pipeline.

- **Suggested:** combine them. The table was built for the seed-to-README process (`CDM/Rapid_Intake/`), which feeds the Stage 1-5 pipeline. Both statements are then true.
- **Decision:**

## L. DLC main questline: candidate count and emergence (2 spots)
26. `Stories/Quest_Design/DLC_Main_Questline_Design_Method.md:90`, Step 2. Inner Tepenia requires at least 10 candidate chains. Toronto Fell Out asks for "several" and says the exact number matters less.
27. Same file, `:93`, Step 2. Inner Tepenia makes "actually emergent" a third required test. Toronto Fell Out filters on two criteria and treats emergence as a preference.

- **Suggested:** keep both as labeled per-game variants, like the rest of that file, and drop the ⚠️ marks. If one rule should be the default for new games, the author picks it.
- **Decision:**

---

## Other things the merges turned up
These are not ⚠️ spots, but they need a decision too.
- **A dangling pointer.** `CDM/Templates/Character_Spec_Fill-In_Sheet_Template.md` sends the reader to `../Design_Principles/` for an anti-stereotyping rule. None of the eight design-principle files holds one, although the Scaffold's Cross-Cutting rules include "No National Stereotypes". Point it there, or write the principle as its own file?
- **The beat-sheet appendix doesn't match its own note.** In `Stories/Story_Structure/story-structure-definitions.md`, the note puts OPPOSITION'S MAIN COUNTER-ATTACK and FAKE-ALLY ATTACK inside Bad Guys Close In, but the template lists them before PET THE DOG and MIDPOINT. The template also has no Self-Revelation, Finale or Closing Image slot, and it ends at FINAL BATTLE.
- **"Bittersweet at best" versus "No Good Endings".** `Game_Design/Game_Design_Principles.md` says all endings are "bittersweet at best". The quest-design methods say No Good Endings "does not mean no positive endings". This one is also in `Glossary/OPEN CONFLICTS (2026-10-30).md`.
