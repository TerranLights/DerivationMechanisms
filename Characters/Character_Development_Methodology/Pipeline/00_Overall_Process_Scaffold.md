# Character Development Methodology — Overall Process Scaffold

**What this is:** a broad-scale architecture map of the whole methodology pipeline. **Refreshed 2026-08-09** —
the original version of this file was written as a pre-consolidation map, pointing at roughly 3,459 lines of raw
material in `../Source_Material/Character_Development_Methodology_-_DRAFT_Ideas.md` and flagging what each
stage would eventually need to reconcile. All of that reconciliation is now done; every stage file is complete.
This refresh replaces the old "here's what needs sorting" framing with an accurate summary of what's actually in
each finished file, plus the intake layer (`00a`/`00b`) that didn't exist when this scaffold was first written.
This file is still the map, not the territory — full detail lives in each stage's own file.

**Portability note:** this whole system was built and battle-tested inside one specific fictional universe
(originally: a sci-fi CRPG's companion-character design), then deliberately generalized into this
self-contained form so it works for building *any* character, in *any* setting, at *any* point in a story —
linear or non-linear, any genre, any medium, with or without game mechanics attached. Nothing in this Pipeline
assumes a specific universe, species, technology level, or narrative format. Where a concrete, fully-worked
example would help, see the separate `../Worked_Examples/` folder — it's genuinely optional, kept apart
on purpose so this Pipeline never depends on knowing anything about that specific setting to function.

> ⚠️ Versions differ: the medium-agnostic version says nothing here assumes a specific universe or medium; the
> game version's text (the base of this file) still names its own project's mechanics, files and characters.

**Why five stages, and what each one actually does:**

1. **Input Information** — everything that has to already exist, or be gathered, before any generative work
   starts on a given Doll.
2. **Information Processing** — the diagnostic toolkit: techniques for interrogating raw inputs to surface a
   genuine, specific psychology, rather than starting from a blank page or a generic trait list.
3. **Character Data** — the actual structured output of Stage 2, written down as reusable fields on a Doll's
   psychological profile (as distinct from the existing `../Templates/Character_Spec_Fill-In_Sheet_Template.md`,
   which is surface/mechanical data, not this deep layer).
4. **Story Material** — converting a finished Character Data profile into actual story scaffolding: her role,
   her supporting cast, her thematic shape, what kind of story she's even in.
5. **Beats, Paths & Results** — the full beat-by-beat structural machinery, branching into every possible arc
   type, path, and ending a given Doll's story material can resolve into.

Downstream stages consume upstream ones. Stage 5 can't be built without Stage 4's story material; Stage 4 can't
be built without Stage 3's character data; and so on.

---

## The Intake Layer — `00a` and `00b`, Added After This Scaffold Was First Written

Not one of the five numbered stages — a compression layer sitting in front of Stage 1, built specifically for
scale: the developer's actual Doll count (1,185 and climbing toward the Outer Tepenia trilogy and Cryptograph
Helix) makes manually filling in Stage 1's full field set per Doll unworkable.

- **`00a_Initial_Input.md`** — the minimal seed-field intake (name, a doll-folder pointer if one exists, a rough
  vision statement, robot/human, Enneagram if known, location of origin if known — the last two with an explicit
  "you decide" escape hatch) plus the full Derivation Protocol mapping those six seeds onto every one of Stage
  1's 25 categories, deferring what genuinely doesn't need to exist yet (introduction-scene context, the full
  relationship web, exact ending concepts) rather than front-loading everything. Also carries the **Story-
  Format Gate** — a one-time, project-level (not per-character) linear/non-linear decision that determines how
  Stage 5's Arc-Space Enumeration tool resolves its output for every character processed afterward.
- **`00b_Clarification_Protocol.md`** — the repeatable algorithm for resolving whatever 00a's derivation leaves
  genuinely ambiguous, per Doll. Confidence-tags every derived field (Sourced / Strong Inference / Weak
  Inference / Blocked), only ever surfaces a question for a Section A field at Weak-Inference-or-worse with no
  safe default, ranks surviving gaps by downstream leverage (Enneagram highest, then Ghost, then robot/human
  status), and phrases whatever survives as closed-form multiple-choice with a "you decide" option. Validated in
  real use on Ayako Hayashi: zero clarification questions generated, one low-stakes proposed default.

---

## Cross-Cutting Constraints — apply at every stage, owned by none

These are the standing design disciplines this whole system was built under. The first three are genuinely
universal writing/game-design principles, worth adopting as defaults in any project. The rest are one
project's own specific implementation choices, kept here because they're a real, battle-tested example of how
a project can turn these principles into binding rules — adapt or discard them freely for a different project's
own needs.

- **This is a non-linear methodology** (the DRAFT file's own Standing Scope Note) — every beat is defined by
  functional role, never by fixed percentage-of-runtime placement.

  > ⚠️ Versions differ: the game and medium-agnostic versions define beats by functional role only; the prose
  > version, for a linear book of fixed length, adds percentage-of-manuscript placement (the bullet below).

- **(Prose version) For a linear medium with a fixed length** — every beat can and should be defined both by
  functional role *and* by percentage-of-manuscript placement, using the story-structure definitions' Summary
  Table (`../../../Stories/Story_Structure/story-structure-definitions.md`) as the actual placement reference. See Stage 5's "Reversal for
  Prose" section for the full reasoning.
- **Preserve Unchosen Material** (see `../Design_Principles/Preserve_Unchosen_Material.md`) — at every stage
  that produces more than one concrete, character-specific candidate (a psychological hypothesis, a casting
  choice, a full arc), the ones that don't get selected still get written down in full somewhere durable, not
  discarded. Whoever is applying this methodology proposes the strongest candidate at each fork; the developer
  confirms it.
- **No Good Endings / Ending Distribution law** (a genuinely portable principle, detailed in
  `../Design_Principles/No_Good_Endings.md`) — negative endings are a minority, bittersweet is the largest
  category, positive endings are real but never costless. Codified as canon in `Companion_System.md` and the
  district/DLC/main-quest equivalents; Stage 5's Ending-Shape Cross-Mapping Table builds toward this
  distribution. Discard it if a given project genuinely wants purer positive or purer tragic endings instead.
- **No National Stereotypes** — a character's origin, species, culture, or background should never be used as a
  shortcut for her personality. Applies most directly to the Background Taxonomy (Stage 3) and to any
  in-fiction regional-reputation shorthand (flagged explicitly where the villain/anti-hero sheet's Mordred/
  Cornwall example shows the failure mode to avoid).
- **No Level-Scaling** (a specific developer's own standing law across every one of their own game projects) —
  enemies, loot, and encounters don't scale to match the player's level; the world has a fixed, designed
  difficulty. Not a character-psychology concern directly, but a standing law all downstream content design
  still has to respect.
- **The Dual-Outcome Companion Perk law** (`Companion_System.md`; generalized in
  `../Design_Principles/Dual_Outcome_Branching.md`) — 2-5 mutually exclusive branches per questline, genuine
  trade-offs. The mechanical skeleton Stage 5's branching content serves, if the target project wants
  branching character resolutions at all.
- **Two stat-check design laws** (added 2026-08-09, synthesized into Stage 5 and now also codified project-wide
  in `Universal_Rules.md`): every skill/stat check in the game reads the player's current, effective stat total
  including temporary buffs, with exactly one exception — Romance Gate 2 checks permanent, unadjusted stats
  only; and a Natural 10 (permanent, never a buffed Adjusted 10) in a stat-based questline approach grants a
  Mastery Dividend, letting the player talk past a real number of subsequent checks within that same questline.
  Fully game-mechanic-specific — relevant only if the target project has its own stat/skill-check system to
  reconcile against character content; otherwise skip entirely.

---

## Stage 1 — Input Information: complete

**File status:** Section A (12 necessary-field categories, each citing the specific downstream node or tool
that needs it) and Section B (13 optional-but-enriching categories) are both fully built. No open items.

**What it actually contains:** foundational identity facts; the mandatory Enneagram assignment (this system
was built around the Enneagram — see the sibling `../../Enneagram/` folder — but any well-grounded typology
system could substitute); intended story
role/scope; existing biographical and historical material (the single most input-hungry category, feeding
Stage 3's Ghost node directly); existing mechanical/surface data; world-context reference access (Robot
Universals' Friction Bank chapters, relevant District Megasheets, faction/religious canon); the project's
standing design-law constraints; the writer's one-time Mirror Interview priming answers (not a per-Doll cost);
existing narrative introduction context; existing supporting cast; existing questline/ending concepts; and a
memory/prior-notes check. Section B covers soft-detail delivery material, speech/dialect notes, reputation,
a pre-existing Basic Headline if one exists, extended relationships, food/music preferences, "Tribe," existing
voice specimens, concept art, secondary foils, cross-media appearances, prior playtesting, and the developer's
own unformalized instincts.

---

## Stage 2 — Information Processing: complete

**File status:** Governing Principles, two consolidated technique-nodes, four standalone tools, and a
troubleshooting checklist are all built. The original scaffold's "three overlapping motivational-axis systems"
question is resolved: Enneagram stays the mandatory primary axis, Direction (Swain's five wishes) is an optional
secondary lens (moved to Stage 3 as a data field), and Compelling Need (Maslow) stays in Stage 2 specifically
because it's situational — what's driving her *right now* — not a fixed trait.

**What it actually contains:** four Governing Principles (Backstory Proportionality, the Consistency Caution,
the developer-refined Mystery Caution — full resolution stays in private design notes, delivered in media only
through soft ambient detail; see `../Design_Principles/Mystery_Soft_Detail_Delivery.md` — and the "Character Is
Not You" caution); two consolidated nodes (the Why Chain/
Interrogation Technique, merging Card and Boutros; Self-to-Character Memory Mining, merging Boutros's Mirror
Interview and Corbett's defense-mechanism excavation); and four standalone tools (the In-Voice Character
Interview, Obstacle Brainstorm-and-Triage, the Scenario Diagnostic Template — still the single most fully-built
tool in the whole methodology — and Compare-and-Contrast Self-Image, plus Compelling Need and the Public/Private
Values Gap).

---

## Stage 3 — Character Data: complete

**File status:** the vocabulary reconciliation flagged as "real, undone work" in the original scaffold is fully
resolved. Six previously-competing Want/Need-style triads are consolidated into seven canonical nodes, with
every source vocabulary named explicitly so nothing was silently lost. A full per-Doll fill-in worksheet
(tier determination, construction order, Stage 2 cross-references) exists on top of the vocabulary. No open
items.

**What it actually contains:** a front-gate tier system (walk-on/minor/major, bridging Stage 3's Drift-vs-Drive
question with Stage 4's Character Hierarchy); seven consolidated nodes (Want, Need/Truth, Lie/Flaw, Ghost,
Desire/Motive — including the flagged Boutros/Truby "Desire" terminology collision — Greatest Fear, and the
Background Taxonomy, spanning Body/Environment/Experience/Ideas); eight standalone fields (Strength, Reasons
She Can't Quit, Dominant Attitude + Contradictory Exception, Character Trait vs. Personality Trait, a four-tier
Coping/Defense Mechanism, a Speech-Pattern Correlation Table, the mandatory personality-type assignment, and an
optional secondary Direction/motivation field); a diagnostic test (Flaw vs. Personality Trait); a two-tier
coverage-checklist system (the
12-Category Notebook as master checklist, the Ten Ways as a separate delivery-channel audit); and the Six Life
Arc archetype assignment, explicitly flagged as pre-built content for the existing nodes, not a seventh
competing vocabulary.

---

## Stage 4 — Story Material: complete

**File status:** the consolidation pass, the Player-Necessity Rule (added 2026-08-09, synthesized from this
project's own already-mature `Companion_System.md` methodology, not book-mined), and a full worked example
(Calethina, now in `../Worked_Examples/Calethina_Case_Study.md`) are all in place. No open items.

**What it actually contains:** a three-step Front-Gate/Sequencing Trio (MICE Quotient → Character Hierarchy →
Story Problem vs. Character Problem); one genuine merge (Contagonist, absorbing Corbett's Counterweight); Impact
Character and Revenant kept deliberately separate after a near-merge turned out to lose real information, with
the non-Truth-aligned Revenant case routed to the villain/anti-hero sheet (see
`../Source_Material/Character_Development_Methodology_-_Villains_and_Antiheroes_-_DRAFT_Ideas.md`); standalone
tools (the Normal World,
the Characteristic Moment, Antagonist vs. Antagonistic Force, the Twelve Archetypal Antagonists, Four-Corner
Opposition, the Four Elements of Relationship Sizzle, Corbett's remaining functional-role catalog);
composability notes between orthogonal systems; two staging/sympathy techniques surfaced late (Card's general
sympathy-lever catalog, Boutros's cat-save/delay-the-worst-act); the Player-Necessity Rule and its four
supporting constraints (the categorical-block sanity check, the compounding-reasons technique, the no-escort-
quest constraint, retrofit discipline) — a project-specific, fully optional add-on, kept here as a real example
of what it looks like to adapt this methodology's story material into an actual companion-character game system
(see
`../Design_Principles/` for the generalized versions of the constraints worth carrying to a different
project); and the Calethina worked example, which surfaced a concrete design gap (a missing Tempter figure)
rather than just confirming what already existed.

---

## Stage 5 — Beats, Paths & Results: complete, three deliberately-deferred items

**File status:** the Midpoint Menu, the full canonical beat sequence, the Branching Investigation-Route
Structure (added 2026-08-09, alongside Stage 4's Player-Necessity Rule, both from the same source), the Act 3
micro-sequence, arc-type beat implications, chiastic mirroring, the Ending-Shape Cross-Mapping Table, and two
full worked examples (Calethina, Ayako Hayashi — now in `../Worked_Examples/`) are all in place. Three items
remain open, all Doll-specific real-world dependencies, not methodology gaps — see below.

> ⚠️ Versions differ: the game version lists three deliberately-deferred open items (below); the prose version
> marks Stage 5 "complete" with "No open items."

**What it actually contains:**
- **Arc-Space Enumeration** — the entry point to this whole stage: holding a character's already-finished
  Stage 3/4 material, Goal, and World-Context fixed, generate one full candidate arc per Arc Type, screen out
  whichever are genuinely implausible given her established psychology, then either collapse to the single
  strongest candidate (linear projects, per the Story-Format Gate in `00a`) or promote the survivors into real,
  mutually exclusive branches via `../Design_Principles/Dual_Outcome_Branching.md` (non-linear projects) —
  including how to handle more or fewer surviving candidates than that rule's 2-5 branch range.
- **The Midpoint Menu** — twelve interchangeable Midpoint mechanics (not one canonical beat), spanning fully-
  sourced entries (Bell's two-type Mirror Moment, Weiland's Moment of Truth, the Negative Arc's Refused
  Redemption), Snyder's False Victory/False Defeat, and broader craft-convention entries, plus three
  supplementary cross-references. Two naming collisions were caught and resolved during construction ("Point of
  No Return" and "False Victory," each independently colliding across two different mined sources).
- **The full beat sequence** — Weiland's 11-beat skeleton as the canonical spine (Normal World → Inciting Event →
  First Plot Point → First Pinch Point → Midpoint → Second Pinch Point → The Later False Peak → Third Plot Point
  → Climax → Climactic Moment → Resolution), with every other source's name for the same beats folded in as a
  glossary rather than treated as competing, plus the generalized Trigger-Type Design Pattern for Inciting Event
  construction (one thematically-matched trigger type per companion, 7-16 concrete instances, a small
  non-district-bound subset; see `../Design_Principles/Trigger_Type_Pattern.md`).
- **The Branching Investigation-Route Structure** — synthesized from `Companion_System.md`'s already
  in-production Personal Questline Design Rule, not book-mined: minimum 5 deterministic stat-based approaches to
  the same player-unique task, non-stat world-state approaches at a floor of 3 (target 7-12), a route-validity
  QA check, a menu of recommended non-stat route archetypes (faction-antagonism, Wild Child with a six-flavor
  taxonomy, Long Vigil), and a multi-companion non-overlap principle. Distinct from the Trigger-Type Design
  Pattern: that one gates questline *entry*, this one gates the *middle*. A project-specific, fully optional
  add-on (kept here as a worked example, generalized further in `../Design_Principles/Dual_Outcome_Branching.md`).
- The Act 3 micro-sequence, the Three Arc Types' beat-level implications (Positive Change, Flat,
  Disillusionment, Fall, Corruption), chiastic mirroring, the Ending-Shape Cross-Mapping Table (mapping Arc
  Types × Ending Shapes × Ending-Distribution categories, with its own flagged Disillusionment "straddle" case,
  now confirmed twice in independent real-world Doll data — Calethina's Accord ending and Ayako's own questline
  design — and a named blind spot for reactive/Flat-Arc-adjacent characters), series-spanning arc models, common ending failure modes (deus ex machina, loose ends, "only a dream,"
  the talkative villain), and QA tools.

**The three open items**, all deferred pending real-world context rather than unresolved methodology:
1. Calethina's Second Pinch Point — genuinely undetermined pending more district/world development.
2. The specific trigger content for Calethina's own "Unusual Readings" system (the system itself is resolved
   and written into her project file; the 39+ district and 20-40 non-district individual triggers are not yet
   designed).
3. The Ending-Shape Cross-Mapping Table's blind spot for reactive/Flat-Arc-adjacent companions (the Accord edge
   case) — a real, named limitation of the table as built, not smoothed over.

---

## Cross-Stage Notes

- **The vocabulary reconciliation the original scaffold flagged as undone is now fully resolved** — see Stage 3
  above. Nothing carries forward from the old "at least five different Want/Need-style triads" note.
- **Convergent-across-independent-sources findings kept accumulating past the original three**: beyond Truby/
  Corbett's split-theme technique and the coping-mechanism convergence already noted originally, real-world
  Doll data has now independently confirmed the Ending-Shape table's Disillusionment straddle twice (Calethina,
  Ayako) and turned up two beats (Ayako's Inciting Event and First Plot Point) that were already established
  canon before this methodology ever touched her file — worth continuing to treat this as validation, not
  coincidence, whenever it recurs.
- **Two genuinely different source types now feed this methodology, worth keeping distinct.** Stages 1-3 and
  most of 4-5 come from book-mining (the craft-theory DRAFT file; see `../Source_Material/` for the full raw
  mining this Pipeline was distilled from). The Player-Necessity Rule, the Branching
  Investigation-Route Structure, and the two stat-check laws come from a different source entirely: this
  project's own already-mature, in-production `Companion_System.md` methodology and the real companion files
  built on it. Both are legitimate, but they carry different evidentiary weight and different revision paths —
  the book-mined material can be re-checked against its source books; the in-production material should be kept
  in sync with `Companion_System.md` and `Universal_Rules.md` directly, since those files, not this methodology,
  are the actual source of truth for anything now codified as project-wide canon.
- **The villain/anti-hero supplement sheet remains a parallel, not subordinate, resource** — feeds Stage 4
  (antagonist/villain story material) and Stage 3 (irredeemability thresholds), kept deliberately separate. See
  `../Source_Material/Character_Development_Methodology_-_Villains_and_Antiheroes_-_DRAFT_Ideas.md`.
- **Two real worked examples now exist** (Calethina: Stages 4-5; Ayako Hayashi: full Stages 1-5), both
  documented in their respective stage files (now gathered in `../Worked_Examples/`) and cross-referenced in
  project memory
  ([[project_calethina_lie_and_tempter_gap]], [[project_ayako_hayashi_pipeline_findings]]). A third and fourth
  Tier-1 candidate (Vosora Lashár Tanslock, Ji-Eun Kim) were identified during the roster survey and are ready
  for the same treatment whenever useful.
- **This whole system was validated against real, fully-worked characters** before being generalized into this
  portable form — see `../Worked_Examples/` for the complete run-throughs, kept separate so this Pipeline never
  depends on that specific setting to function.

---

## What This File Is Not

Not the finished methodology in full — that's the seven files it maps (`00a`, `00b`, `01` through `05`). This
file is the navigational summary, refreshed to stay accurate as of 2026-08-09; if any stage file changes
substantially again, this scaffold should get another pass rather than being left to drift stale a second time.
