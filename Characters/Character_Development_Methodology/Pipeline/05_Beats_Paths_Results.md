# Character Development Methodology — Stage 5: Beats, Paths & Results

**Pipeline position:** all the possible beats, paths, and results of a character's story/questline/arc, built
from the story material produced in Stage 4 (`04_Story_Material.md`).

**Status:** consolidation pass complete (2026-08-09), plus full worked examples (Calethina and Ayako Hayashi,
continuing from Stage 4) — see `../Worked_Examples/` for the complete run-throughs, kept separate so this
Pipeline never depends on that specific setting to function. The Midpoint Menu, the full canonical beat
sequence with cross-source glossary, the Branching Investigation-Route Structure, the Act 3 micro-sequence,
arc-type beat-level implications, chiastic mirroring, and the Ending-Shape Cross-Mapping Table are all in place.
Two naming collisions caught and resolved along the way ("Point of No Return" and "False Victory," both
colliding across independently-mined sources — see the notes inline below). The Calethina worked example caught
a real structural flaw (an early-draft Inciting Event proposal that would have made her questline inaccessible
to some playthroughs — see `../Design_Principles/Always_Present_Gating.md`); the Ayako worked example produced a
second real-world confirmation of the Ending-Shape table's Disillusionment straddle case. Two open items remain,
see below.

> ⚠️ Versions differ: the game version says open items remain (see "Open, Undecided" below); the prose version
> says "No open items remain."

---

**Scope note:** everything in this Stage 5 file — Arc-Space Enumeration, the Midpoint Menu, the full beat
sequence, the Ending-Shape Cross-Mapping Table, Chiastic Mirroring — is Companion-questline scope (or, more
generally, scope for a character's one primary arc). If your project has a separate, secondary Romance layer,
it uses a different, deliberately lighter tool instead — see
`../Design_Principles/Companion_vs_Romance_Scoping.md`'s "Courtship Sequence."

## Arc-Space Enumeration — Generating Every Plausible Arc Before Choosing One

**What this is, and why it comes first:** every other tool in this stage (the Midpoint Menu, the beat
sequence, the Arc-Type beat-level implications, the Ending-Shape table) assumes a single Arc Type has already
been chosen for a given character. This section is the step that comes *before* that choice. For a character
whose Stage 3 Character Data and Stage 4 Story Material are already finished, and who has a concrete
in-context Goal and an established World/Setting-Context to operate within, this tool generates the full space
of arcs she could theoretically go through, before anything gets narrowed down to one.

**Required inputs, all already fixed by this point:** a finished Character Data profile (Stage 3 — her Ghost,
Lie/Flaw, Need/Truth, Want, Desire/Motive, Greatest Fear), her Story Material casting (Stage 4 — MICE
classification, Character Hierarchy, Impact Character/Revenant/Contagonist, antagonist selection), a specific
in-context Goal, and the surrounding World/Setting-Context she's operating in. None of these should change
across the candidates generated below — the whole point is holding the character and her circumstances fixed
and varying only the shape of the arc she goes through.

**Also required: the Story-Format Gate's answer** (`00a_Initial_Input.md`) — linear or non-linear — since it
determines which of the two exit paths at the end of this process actually applies.

### Step 1 — Generate One Full Candidate Arc Per Arc Type

Run this stage's own machinery once per Arc Type (Positive Change, Flat, Disillusionment, Fall, Corruption —
see "The Three Arc Types — beat-level implications," below) against the same fixed inputs: select the Arc
Type's natural Midpoint Menu entry, build out the 11-beat skeleton using that Arc Type's specific beat-level
implications, and note its likely Ending-Shape Cross-Mapping Table row. The output of this step is five full
candidate arcs, not five one-line summaries — each one should be developed far enough to actually judge (a
real Ghost-to-Lie-to-Midpoint-to-Climax throughline), even though most of them won't survive to final content.

### Step 2 — The Plausibility Screen

Not every Arc Type is actually available to every character — a candidate gets disqualified here, not just
deprioritized, when it directly contradicts something already fixed about her:

- **A Flat Arc candidate requires she already holds the Truth at the story's start.** If her Stage 3 Lie/Flaw
  material establishes she does *not* yet hold the Truth, disqualify the Flat Arc candidate outright rather
  than forcing it to work.
- **A Fall or Corruption Arc candidate requires a real, plausible path to her consciously rejecting the Truth
  (Refused Redemption) given her established psychology.** If nothing about her Ghost, Coping/Defense
  Mechanism tier, or Reasons She Can't Quit makes that rejection remotely plausible, disqualify it rather than
  manufacturing an out-of-character turn.
- **Check consistency against her Stage 3 Life Arc archetype, if one was already assigned.** Life Arc
  archetype (Maiden/Hero/Queen/King/Crone/Mage, or whichever set is in use) and Arc Type are different axes,
  but they should cohere — a candidate that fights her already-established archetype's natural shape needs a
  real justification, not just inclusion for completeness.
- **A surviving candidate doesn't need to be good, only genuinely possible.** This screen exists to cut what's
  actually impossible given already-fixed facts, not to pre-judge quality — quality judgment happens at the
  exit-path step below, using different criteria depending on linear vs. non-linear.

What survives this step is the actual, honest answer to "every possible arc she could theoretically go
through" — usually somewhere between two and five candidates, occasionally all five, occasionally as few as
one.

### Step 3 — Exit Path, Determined by the Story-Format Gate

**If Linear (a fixed, single telling):** collapse to one — but the collapse itself is a developer decision,
not something this methodology (or whoever/whatever is applying it) should make unilaterally. **Whoever is
running this process proposes the single strongest surviving candidate** — by thematic fit with the
surrounding story, tone, and what the established Goal and World-Context actually call for — and states
plainly why that one over the others, but the developer is the one who actually confirms it before it gets
built out in full using the rest of this stage's tools.

**Don't discard the losing candidates — write them to that character's own Overflow file.** The fullest worked
instance of `../Design_Principles/Preserve_Unchosen_Material.md`'s general rule (unselected, character-specific
candidates get preserved at every stage of this Pipeline, not just here): a dedicated file (e.g. `[Character
Name]_Arc_Overflow.md`, kept alongside the rest of her character material) capturing every surviving-but-
unselected candidate from Step 2 at the same level of detail Step 1 produced, not compressed summaries — each
one is a genuinely complete alternate arc, not a scrapped idea. This is real, reusable material: a sequel, an
alternate-universe version of the same character, a different character built from a similar seed later, or
simply a reconsideration if the chosen arc turns out not to work once written. Nothing generated at Step 1 is
wasted work, whether or not it was the one selected.

**If Non-Linear (a branching or interactive work):** don't collapse. Promote the surviving candidates directly
into `../Design_Principles/Dual_Outcome_Branching.md`'s mutually-exclusive branch structure, and build each
one out in full as its own complete branch.

- **If the surviving candidate count is within Dual-Outcome Branching's 2-5 range**, promote all of them
  directly — this is the clean case the two tools were designed to hand off to each other.
- **If more than 5 candidates survive the Plausibility Screen**, the 5-branch cap is a real constraint that has
  to be actively reconciled, not silently ignored: either (a) apply Dual-Outcome Branching's own
  distinctiveness standard — a branch earns its slot only if it's a genuine trade-off, not a flavor variant of
  another surviving candidate — and merge or cut down to the strongest 5, or (b) if the character is major
  enough to justify it, treat exceeding 5 as the same kind of deliberate, explicitly-flagged special case
  `../Design_Principles/Trigger_Type_Pattern.md` already carves out for its own scaled-up character — never
  break the cap silently.
- **If fewer than 2 candidates survive**, Dual-Outcome Branching doesn't apply at all for this character —
  build whichever single candidate survived as her sole arc, the same as the Linear case above, and treat that
  as a real, informative finding about her rather than a failure of this process. Some characters, given their
  fixed psychology and circumstances, genuinely only have one honest story.

---

## Reversal for Prose: Percentage/Page-Based Placement Is Usable Here

The source methodology's Standing Scope Note (kept below for the functional-role logic itself, which is still
useful) treats percentage-of-runtime beat placement as something to deliberately avoid, because a game is
non-linear — branching, replayable, no single fixed order or fixed length a story unfolds across. **A novel is
the opposite case: linear, single fixed reading order, and a knowable total length (word/page count) decided
before or during drafting.** For prose, percentage-of-manuscript placement isn't just usable, it's the more
natural default — a beat can genuinely be targeted at "~20% of the way through this book" in a way that never
made sense for a branching questline.

**The authoritative percentage skeleton for this project is the story-structure definitions in
`../../../Stories/Story_Structure/story-structure-definitions.md`** — the same fused Snyder/Bell/Truby/Campbell beat structure as below, but
already expressed with the placement percentages this file's own game-oriented version had to strip out. Use
that file's Summary Table for the actual page/percentage targets per beat; use this file's beat-by-beat
definitions and the Menu/Route material below for the content that goes *in* each slot.

**A concrete sub-beat pacing rule, usable now that fixed length is available:** place a story's first major
escalating reveal roughly a third of the way in, and a second, larger one around two-thirds through — a rough,
portable placement rule (from the same craft-book mining that built this methodology) for where a book's own
midpoint-and-late-point twists should land, distinct from but compatible with the Save the Cat percentage table
above.

---

## The Midpoint Menu — a menu of interchangeable mechanics, not a single canonical beat

**Framing:** per the main DRAFT file's own Standing Scope Note, "the Midpoint" was never meant to be a literal
50%-of-runtime timestamp in this project — it's whichever scene functions as this structural slot in a given
branch, wherever it actually lands in a specific playthrough. **For prose, both readings are available and
compatible**: target the Midpoint at ~50% of the manuscript per the story-structure definitions
(`../../../Stories/Story_Structure/story-structure-definitions.md`), *and* use the menu below to decide what actually happens in that slot.
Different writing scholars define what happens *in* that slot very differently (James Scott Bell's two-type
Mirror Moment, Blake Snyder's False Victory/False Defeat split, and more), and rather than picking one as
canonical, the developer's explicit call (2026-08-09): **include every mechanic as a selectable option.** For any
one specific Doll's specific questline branch, exactly one mechanic from this menu gets implemented — but the
full menu stays available, and which one gets picked depends entirely on that Doll's own context, not on a fixed
project-wide default.

> ⚠️ Versions differ: the game and medium-agnostic versions say the Midpoint is never a literal 50% timestamp
> (beats placed by function only); the prose version makes ~50%-of-manuscript placement the default for prose.

**Practical rule for Dual-Outcome Perk questlines** (see `../Design_Principles/Dual_Outcome_Branching.md`):
each branch is its own complete arc (per the Standing Scope Note), so each branch picks its own mechanic from
this menu independently. Two branches of the same Doll's questline can legitimately use two different
mechanics.

### From books already mined for this project (fully sourced, citable)

1. **Moral Mirror Moment** (Bell, *The Last Fifty Pages*) — self-confrontation: who am I / what have I become /
   what must I become. Can run negative→positive (most common), positive→negative, or the tragic variant where
   change is genuinely offered and consciously declined.
2. **Death-Stakes Mirror Moment** (Bell) — not moral at all: "I might not survive this." Produces a
   stasis→strength shift without requiring the character to change *who* she is. Best fit: Flat Arc companions,
   action-forward companions who don't need identity change, just to get tougher.
3. **Moment of Truth / Subconscious Turn** (Weiland, *Creating Character Arcs*) — the full psychological
   package: she doesn't consciously reject the Lie yet, but her actions start betraying the Truth she's secretly
   already accepted — the "caught between Lie and Truth" double-consciousness. The default, most versatile
   option for a standard Positive Change Arc.
4. **Refused Redemption** (Weiland's Workbook, Negative Arc variant) — she sees the Truth clearly enough for a
   real chance to embrace it, and consciously rejects it for a worse Lie. Fall/Corruption Arc companions
   specifically.

### Blake Snyder's *Save the Cat*, added per developer request (2026-08-09) — general craft knowledge, not yet
run through this project's own extraction process on the source book itself

5. **False Victory** (Snyder) — everything appears to be going great; she seems to have solved her problem or
   gotten what she wanted, but the win is built on the unaddressed Lie and will collapse later. Sets up a harder
   fall at the Third Plot Point; works well for a comedic or upbeat-toned first half.
   - **Naming-collision note (2026-08-09):** Weiland's own 11-beat skeleton (this project's canonical beat
     sequence — see the full sequence below) already has a beat named **False Victory**, but it sits *late*,
     immediately before the Third Plot Point, not at the Midpoint — an apparent win achieved through the wrong
     (Lie-aligned) methods, which curdles into a hollow victory that precipitates the real crisis. Same exact
     phrase, two different sources, two different structural positions. Resolved by keeping Snyder's paired
     terminology intact here (False Victory / False Defeat is a matched pair worth not breaking) and renaming
     Weiland's later beat instead — see **"The Later False Peak"** in the full beat sequence below.
6. **False Defeat** (Snyder) — the inverse: an early gut-punch that feels terminal but isn't the true climax,
   setting up a recovery arc. Fits darker-toned or thriller-adjacent questlines. No naming collision found for
   this one.

### From broader, well-known craft convention — general knowledge, not from a specifically mined book, flagged
honestly as lower evidentiary weight than the fully-mined entries above

7. **The External Commitment Event** (renamed from "Point of No Return" after a naming-collision check — see
   below) — the Midpoint defined by an external, irreversible plot event rather than internal realization at
   all — she's now in it, whether emotionally ready or not. Good fit for Event-type MICE Under-Questlines
   (cross-reference Card's MICE Quotient, Stage 4) that don't warrant full internal-arc treatment but still need
   a structural midpoint marker.
   - **Naming-collision note (2026-08-09):** this was originally listed as "The Point of No Return," but that
     exact phrase is already in use elsewhere in this project's own citation trail for two *different* beats —
     Alderson's *Writing Deep Scenes* (already mined) explicitly places its "Point of No Return" Energetic
     Marker at the Inciting Incident/First Plot Point, and Bell's *Last Fifty Pages* names a "Doorway of No
     Return #2" specifically at the transition into Act 3 (the Third Plot Point), implying a "#1" earlier still.
     Both already-mined sources bookend the *middle* with this language rather than using it for the middle
     itself. The underlying mechanic here is still valid for the Midpoint slot — this entry is renamed
     specifically to avoid colliding with how "point/doorway of no return" is already cited elsewhere in this
     methodology.
8. **The Recontextualizing Reveal** (mystery/thriller convention) — new information recasts everything before
   it (the trusted figure is the traitor; the goal she thought she had wasn't the real one). The character's
   *response* to the reveal generates the arc from here, not an internal shift at the moment it lands. Strong
   fit for betrayal-centric arcs or conspiracy Under-Questlines.
9. **Death and Rebirth / The Symbolic Death** (Campbell/Vogler-adjacent) — a symbolic (or briefly literal) death
   of the old self, emerging changed. Strong fit for Crone/Mage-stage companions and, notably, for Identity
   Fragmentation companions specifically. **Not a separate menu item from #3 so much as a vivid instance of
   it** — all six of Weiland's own Archetypal-book Midpoints (Maiden's Identities/Loyalties/Wants Conflict,
   Hero's "Remembering Who He Is," Queen's Leading the Charge, King's Witnesses True Supernatural Nature, Crone's
   Chooses to Seek Life, Mage's Confronting Evil in the Heart of Man) are pre-populated instances of #3 or #9,
   already baked into the Six Life Arc content library — not something to pick *in addition to* one of the
   twelve entries in this menu, but the specific flavor this menu takes once a Doll is already assigned one of
   the Six Life Arcs (Stage 3).
10. **The Dark Mirror Encounter** — the protagonist meets or confronts a figure embodying what she could become
    if she fails. Extends the "antagonist drawn from the next arc-stage" technique already captured under Stage
    4 into a Midpoint-specific device. Best for a companion teetering on the edge of a Fall/Corruption Arc.
11. **The Reactive-to-Proactive Shift, stripped-down** — the purely structural version, deliberately without
    Weiland's psychological apparatus attached: before this point things happen *to* her, after it she starts
    making things happen — full stop, no claim about subconscious Truth-acceptance required. Useful for a minor
    or Flat-Arc character who needs *some* Midpoint marker without the full Lie/Truth machinery.
12. **The Turn / Value-Polarity Flip** (Story Grid-adjacent) — the story's driving thematic value (life/death,
    freedom/slavery, love/hate) flips polarity at the Midpoint. Ties directly back to Truby's "split the theme
    into oppositions" material already captured in Stage 3/4. The **Public/Private Stakes Flip** (common in
    romance/rom-com beat-sheet convention — whatever was private about her struggle becomes public, or vice
    versa) nests under this as one specific, frequently-useful flavor rather than its own top-level entry.

### Supplementary cross-references — not competing menu items

Found during the follow-up re-check of the fully-mined books (2026-08-09), requested specifically to catch
anything missed on the first pass:

- **Erikson's later-life crisis stages** (Seger, *Creating Unforgettable Characters* — Generativity vs.
  Stagnation; Integrity vs. Despair) function the same way the Six Weiland Archetypal Midpoints already do above
  (see #9): pre-built *thematic content* for whichever mechanic from this menu gets chosen, specifically suited
  to flavoring a Queen/King-stage companion's Midpoint (Generativity vs. Stagnation) or a Crone/Mage-stage one's
  (Integrity vs. Despair) — not a competing mechanic in its own right.
- **The Preparation → Pressure → Realization → Validation model** (Kress, *Dynamic Characters*) is a general
  drafting *process* for actually constructing whichever menu item gets picked, not itself a 13th named beat —
  useful as the how-to-write-it method once a mechanic above has been selected.
- **Chiastic mirroring** (Weiland, *Next Level Plot Structure*) is a cross-cutting structural principle that
  applies to every entry in this menu equally, not a separate mechanic: whichever option is chosen, the Midpoint
  functions as the unpaired axis the rest of the beat structure pivots around and mirrors against.

*(Status: 12 primary entries, one renamed for a naming-collision fix, three supplementary cross-references
attached. This follow-up re-check found no wholly new Midpoint-specific mechanics hiding in the already-mined
books beyond what was already captured — menu can be treated as closed pending any further sources the developer
wants added.)*

---

## The Full Beat Sequence — canonical skeleton + cross-source glossary

Weiland's 11-beat skeleton (*Creating Character Arcs*) stays canonical, since it's the most structurally
complete of any source mined for this project. Every other source's name for the same beats folds in as a
glossary entry rather than competing:

1. **Normal World** — the opening world/circumstances, actively built to symbolically dramatize the Lie (Stage
   4). ≈ Alderson's "Beginning" quarter.
2. **Inciting Event** — an outside force or discovery that starts things moving. ≈ Alderson's "Point of No
   Return" Energetic Marker (see the naming-collision note already resolved in the Midpoint Menu above — this
   project does *not* use "Point of No Return" for this beat's name, to avoid re-triggering that same
   collision, but the equivalence is worth knowing since it's how Alderson's own book names it). **Refinement**
   (St. John): ensemble companions sharing a scene don't need the *same* Inciting Event — one companion's
   triggering event can be a different, downstream event from another's, even when both share the larger story.

   **The Trigger-Type Design Pattern (developer instruction, 2026-08-09, generalized from the Calethina worked
   example, `../Worked_Examples/Calethina_Case_Study.md`).** A standing design rule for constructing any
   companion's actual Inciting Event trigger, distinct from the beat's abstract definition above — see
   `../Design_Principles/Trigger_Type_Pattern.md` for the full generalized rule and its origin story:
   - **One consistent trigger *type* per companion, thematically and functionally matched to her established
     background and personality** — not an arbitrary or generic action, and not a different kind of trigger for
     each individual instance. Calethina's own type (network/connection-restoration events) is directly
     load-bearing on her signal/grid nature; a different companion's type should be derived the same way, from
     what's already established about *her* specifically, not copied from Calethina's.
   - **A minimum of 7 concrete in-world triggers of that one type, ideally 12-16.** The point of the volume is
     explicit: a player should never be funneled into one single required action to begin a companion's
     questline, since that constrains roleplay by forcing a specific playstyle or path. Many thematically
     identical options, not one solitary gate.
   - **Every companion should have *some* non-district-bound triggers within her total count, not just
     Calethina — but a small number, not a large dedicated pool.** Revised 2026-08-09, same day as the pattern
     itself: the primary reason is **roleplay flexibility**, not Pariah coverage — situations where the player
     has her as an active companion and they're off together somewhere not tied to any specific district. Pariah
     coverage turns out to need far less than it first seems: Pariah status logically implies Vilified status
     with all 13 districts simultaneously, so even a single non-district trigger already suffices for that edge
     case — a large dedicated pool isn't actually required by the Pariah scenario itself. These non-district
     triggers must stay characteristically consistent with the specific companion, same single trigger type as
     her district-bound ones, just not anchored to a location. The exact split between district-bound and
     non-district-bound triggers within a companion's total 7-16 is left as a per-companion design decision, not
     a fixed ratio.
   - **A character whose presence isn't tied to any one place should have *some* location-independent triggers
     within her total count** — a small number, not a large dedicated pool — for situations where she's already
     alongside the protagonist somewhere not anchored to her usual setting. These location-independent triggers
     must stay characteristically consistent with the character, same single trigger type as her location-bound
     ones, just not tied to a place. The exact split is a per-character design decision, not a fixed ratio.

     > ⚠️ Versions differ: the game version requires some non-district-bound triggers for every companion; the
     > prose version requires location-independent triggers only for a character whose presence isn't tied to
     > any one place.
   - **Calethina's own design (39+ district-bound triggers plus a separate 20-40 non-district-bound pool,
     written into her `Personal_Questline_Summary.md`) is a scaled-up special case of this general rule, not the
     default template.** Her count is larger and split into two tracks because of her own unusual structural
     requirements — she's present from the game's literal opening, and both her district and non-district pools
     were sized generously rather than to a strict minimum. A typical companion, recruited normally and without
     that kind of edge case, should default to the more modest 7-16-trigger range overall, with only a small
     subset of that total being non-district-bound.
3. **First Plot Point** — an irreversible first step out of the Normal World; chiastically paired with the
   Third Plot Point (see Chiastic Mirroring, below).
4. **First Pinch Point** — an early complication or pressure point that escalates the opposition.
5. **The Midpoint** — see the full Midpoint Menu above; twelve interchangeable mechanics, pick one per branch.
6. **Second Pinch Point** — a later complication, chiastically paired with the First Pinch Point.
7. **The Later False Peak** (renamed from "False Victory" 2026-08-09, to resolve the naming collision with
   Snyder's Midpoint-positioned beat of the same name — see the Midpoint Menu above) — an apparent win achieved
   through the wrong, Lie-aligned methods; it curdles into a hollow victory that precipitates the real crisis.
   Weiland's own six Archetypal-book templates give this consistent content across every Life Arc: the Hero's
   "wins against the Dragon, but only by compromising everything he's learned"; the Queen's "protects her
   children at the cost of their independence"; the King's "tries to stop the Cataclysm with kingly might"; the
   Crone's "seeks physical immortality."
8. **Third Plot Point** — see the Act 3 Micro-Sequence, immediately below; this is where Bell's more granular
   Act 3 material actually lives.
9. **Climax**
10. **Climactic Moment** — chiastically paired with the Inciting Event.
11. **Resolution** — see the New Normal World's five flavors, folded into the Ending-Shape Cross-Mapping Table
    below; chiastically paired with the Hook.

---

## The Branching Investigation-Route Structure

**Fully optional — a real, concrete example of adapting Stage 5 into a stat/skill-driven game system**, kept
here because it's genuinely useful precedent for a project with its own such system, not because every
project needs it.

Synthesized 2026-08-09 from `Companion_System.md`'s already-established "Personal Questline Design Rule" and a
read-through of the actual companion questline files already built on it (Favi della Torre, Vosora Lashár
Tanslock, Ayako Hayashi, and others) — mature, in-production methodology this project already runs on, not new
theory. **A distinct mechanic from the Trigger-Type Design Pattern above: that pattern gates questline *entry*
(how many ways can the Inciting Event fire); this one gates the *middle* (how many ways can the player actually
execute the Player-Necessity Rule's unique task once the questline has started).** (The Player-Necessity Rule,
if a project uses it, is in `04_Story_Material.md`.) The two are complementary, not competing, and a single
companion's questline legitimately uses both.

### The Route Counts

- **A minimum of 5 stat-based approaches**, deterministic (no randomness — a threshold is either met or it
  isn't), spread across different MACHINE stats, and — critically — **each one a different way of executing the
  *same* player-unique task established by the Player-Necessity Rule (Stage 4), not five different tasks.**
  Favi della Torre's five approaches to the same Bridge-Unit-only jack-in (Investigation-driven mapping,
  Calculation-driven pattern-matching, Nerve-driven brute force, Humanity-driven persuasion of a fragment-echo,
  Engine-driven endurance) is the clean worked model: one categorically-exclusive task, five distinct routes to
  succeeding at it.
  - The useful takeaway is the structural principle itself — give a character multiple genuinely different,
    in-character ways to resolve the same obstacle, rather than one linear path — not any specific gating
    mechanism.
- **Non-stat, world-state-based approaches at a floor of 3, target 7-12.** These exist specifically to prevent a
  soft-lock for a player who built entirely outside the 5 covered stats, and — because a companion's personal
  questline (Gate 1) must complete before her romance stat/trait check (Gate 2) can even fire — to guarantee
  romance eligibility and questline completion are never accidentally incompatible with each other.

### Two Standing Stat-Check Design Laws

Added 2026-08-09, directly governing how the 5 stat-based approaches above should actually be built. Both are
general, game-wide MACHINE-stat-check laws, not specific to personal questlines — recorded here because this is
where stat-based approaches are designed, but they apply everywhere a stat/skill check appears in the game.
**Now formally codified as project-wide canon** in `Game-Mechanics/Universal_Rules.md`'s new "Skill & Stat
Checks" section — that file, not this one, is the source of truth for actual implementation; this entry remains
here as the working-draft record and because it's the natural place to apply the laws when designing a
companion's stat-based approaches. A real, concrete example of project-specific mechanical rules that had to be
reconciled with the story-structure layer above — include only if your own project has a comparable
stat/skill-check system to reconcile against character content.

- **The Perfect-10 Mastery Dividend, scope confirmed 2026-08-09: the same questline, not game-wide.** When one of
  the 5 stat-based approaches offers a **Natural 10** option in a given MACHINE stat, choosing it should let the
  player "talk their way past" a real number of subsequent stat/skill/perk checks within that same questline —
  not a standing, permanent game-wide effect.
  - **Natural 10 vs. Adjusted 10, a real and load-bearing distinction.** A **Natural 10** is a *permanent* stat
    value of 10, reached only through starting character-creation allocation, spending Intense Training points,
    or installing a non-Dr.-Usanagi implant — the three established permanent-stat-increase paths. An
    **Adjusted 10** is a stat that merely reads 10 *right now* because of a temporary buff (food, chems, or
    similar — the Bighorner/Brahmin Steak example under the Buffable-Stat-Check Law below) stacked on top of a
    lower permanent value. The Mastery Dividend is earned only by the Natural 10, never the Adjusted one — a
    temporary buff can clear the threshold for a single check, exactly as the Buffable-Stat-Check Law requires,
    but it does not represent the genuine, rare, life-area mastery the Dividend exists to reward.
  - **Implementation: a Natural 10 option appears as its own separate dialogue choice**, distinct from an
    ordinary buffable stat check on the same stat, so the two are never conflated in the UI or the underlying
    check logic:
    ```
    {{NPC dialogue}}

    [10 STAT] {{dialogue}}
    [Nat 10 STAT] {{dialogue}}   // grants the Mastery Dividend for the rest of this questline
    [55 SKILL-A] {{dialogue}}
    [80 SKILL-B] {{dialogue}}
    [45 SKILL-C] {{dialogue}}
    ```
    The plain `[10 STAT]` option stays ordinarily buffable per the Buffable-Stat-Check Law below and only
    resolves the single check it's attached to; the separate `[Nat 10 STAT]` option is what actually gates the
    Dividend, and only a permanent Natural 10 can select it.
- **The Buffable-Stat-Check Law, with exactly one standing exception.** Every stat/skill check in the entire
  game should evaluate the player's *current, effective* stat total — inclusive of temporary buffs from food,
  chems, equipment, or any other stacking bonus — never the character's permanent, unadjusted base stat alone.
  **Precedent, Fallout: New Vegas** — during the Great Khans/Melissa questline, Tyrone (who has been skimming
  supplies from Chomps Lewis to cover for suspicious NCR superiors) can be talked down via a Strength check
  requiring 7 ("I'm sorry, I can't hear you over the sound of all these muscles"); a player with a natural 5
  Strength who eats Bighorner or Brahmin Steak for a temporary +2 Strength buff passes the check exactly as if
  the 7 were natural — the game does not distinguish. **Every stat/skill check in this game should work
  identically, with exactly one standing exception: Romance questline trigger checks (Gate 2, per
  `Companion_System.md`) check only the player's permanent, unadjusted MACHINE stat — temporary buffs never
  count toward a romance threshold.** This generalizes the Gate 2 rule already noted elsewhere in this project
  (that only permanent stats count toward romance) into the single, explicit, named exception across the entire
  game, rather than leaving it as an isolated romance-specific footnote that every other system might
  independently, and inconsistently, reinvent.

### The Route-Validity QA Check

A proposed non-stat route is invalid if the companion's own already-established standing would already
trivially provide the same access on its own — the route has to bypass something *she* genuinely can't already
get, not just offer the player a redundant path to something she could hand over directly. Two real, on-record
corrections worth keeping as the standard for this check: an early "Eyes of Gold reputation route" was removed
from Favi's design because her own loyal, established Eyes of Gold standing already secures anything that
faction could offer — gating it behind the player's separate reputation didn't hold up. And Vosora's "sympathetic
Libra official" route was explicitly corrected to be understood as a specific individual within the antagonist
institution who happens to disagree with the pressure campaign, *not* "Libra's own administrative reach" — a
different, easily-confused pattern that would have failed the same check. Watch especially for a route that
quietly depends on an existing relationship or resource of hers rather than the protagonist's own, and for a
route that names a whole faction/institution's reach when what's actually meant is one specific sympathetic
individual within it — a different, easily-confused pattern that fails the same check.

### A Menu of Recommended Non-Stat Route Archetypes

Reach for these where a companion's own established world genuinely supports them — never invent the underlying
lore just to manufacture the route:

- **The faction-antagonism route** — where a companion has an established negative or wary relationship with a
  specific faction or district, the player's own separate *positive* standing there (Accepted or better, not
  necessarily Idolized) opens a door she couldn't open herself, precisely because she's on the wrong side of
  that relationship.
- **The Wild Child route** — usable specifically by a player holding Wild Child status (Idolized + Vilified
  simultaneously with a relevant faction/district) — rare by design, and rewards that rare extreme playstyle
  with real companion-content payoff rather than only its own dedicated endings.
  - **Flavor taxonomy, to avoid defaulting to the same mechanic every time**: bureaucratic/records-gap (an
    institution can't file the player, so individualized handling surfaces information as a side effect —
    the *original* default, now flagged as overused if reached for reflexively), gossip/rumor (the player
    becomes unavoidable talk in an informal information economy), confessional/psychological (an institution
    built around sitting with irreconcilable truths engages with the player's own contradiction on its own
    terms), persuasion/leverage (someone gambles on the player specifically because their paradoxical
    reputation makes them worth the risk), fear/intimidation (refusing feels more dangerous than complying),
    and opportunism (someone tries to exploit the player's notoriety and the player can leverage that back).
    When designing a new Wild Child route, ask what kind of reaction *this specific* faction or district would
    actually have to an unresolvable contradiction, rather than reaching for the bureaucratic default again.
- **The Long Vigil route** — where a companion's own established psychology gives her a genuinely high
  Personality Grief-Multiplier (Ayako Hayashi is the first confirmed case), a route or full pathline reachable
  only by a player who has brought that companion to The Long Vigil (Grief Range 3 + Bond Range 3
  simultaneously) — content that can only exist because of that specific state, not a flavor variant reachable
  another way. Requires the base companion questline completed first, same prerequisite Romance Gate 3 already
  sits on top of; independent of the romance track itself, but both should stay cross-aware where they coexist
  in the same playthrough.

### Multi-Companion Non-Overlap Principle

When two companions investigate the same underlying mystery (Vosora Lashár Tanslock and Michelle Stanton, both
working the Great Corruption from different angles), their questlines need genuinely non-overlapping
deliverables and mechanisms — completing one must never shortcut or complete the other. The cleanest version of
this splits the shared mystery into structurally distinct halves (Vosora reconstructs destroyed content; Michelle
verifies the accident's cause and whereabouts of a surviving copy) rather than having both companions converge on
the identical deliverable through different routes.

---

## The Act 3 Micro-Sequence — Bell's granular elaboration, not competing vocabulary

Bell's Act 3 material turns out to be additive granularity rather than a competing beat sequence — it's a more
detailed breakdown of the space between The Later False Peak and the Climax:

1. **Doorway of No Return #2** (Bell) — the mechanical trigger into Act 3: a discovery, clue, or setback that
   makes the climax actually reachable, not just an emotional shift. (The "#2" implies a "#1" earlier, at the
   First Plot Point — consistent with the naming-collision note above; this project doesn't separately name a
   "Doorway of No Return #1," since that beat is already covered by the First Plot Point.)
2. **Mounting Forces** (Bell) — the antagonist escalates specifically because the protagonist's commitment to
   the fight is now unmistakable.
3. **The Third Plot Point / Black Moment / Lights Out** — one beat, three names (Weiland / St. John / Bell
   respectively). St. John's content rule is the sharpest of the three and worth using as the operative
   definition: the character's darkest fear comes to pass, and it must be engineered to match her specific,
   already-established Greatest Fear (Stage 3 node) precisely — not just "something bad happens." Weiland notes
   this beat is very often marked by an actual or symbolic death.
4. **The Q Factor** (Bell) — a specific emotional jolt, arriving right around the Black Moment, that supplies
   the courage to go into the final confrontation. Its defining feature: it works by calling back to something
   specific established early in the story (an object, a line, a promise), not a fresh burst of resolve invented
   on the spot — a concrete instance of chiastic mirroring (below), applied to emotional payoff specifically.

---

## The Three Arc Types — beat-level implications (full taxonomy already lives in Stage 3's Six Life Arc
content-library note; this section is Stage 5's specific job: what changes at the *beat* level per arc type)

- **Positive Change Arc** — the default assumption underlying the beat sequence above as written.
- **Flat Arc** — the Midpoint more naturally takes a Death-Stakes Mirror Moment or the stripped-down
  Reactive-to-Proactive Shift (Midpoint Menu #2 or #11) rather than the full Moment of Truth package, since a
  Flat Arc character already holds the Truth and isn't undergoing internal change.
- **Disillusionment Arc** — believes Lie → overcomes Lie → new Truth is tragic. Not morally negative; see the
  Ending-Shape Cross-Mapping Table below for why this variant is the one genuinely underdetermined case.
- **Fall Arc** — the Midpoint specifically takes the **Refused Redemption** mechanic (Midpoint Menu #4): she
  sees the Truth clearly enough for a real chance to embrace it, and consciously rejects it. The Third Plot
  Point/Black Moment for a Fall Arc should read as passive-denial curdling into open aggression (cross-reference
  the Passive→Aggressive shadow-archetype mapping already established).
- **Corruption Arc** — also takes Refused Redemption at the Midpoint. Its Third Plot Point is a precise
  inversion of the standard sequence: **an apparent *triumph* that is actually the true low point** (Weiland's
  Workbook) — she achieves real, tangible external victory, but the win is hollow and costs her soul. Two foil
  techniques for staging this beat: populate it with a supporting character who shows the better road not taken,
  *and* a separate one showing their own descent as a direct consequence of the protagonist's corrupting
  influence. The Third Act for both Fall and Corruption Arcs reads as "inverted resurrection" — the character
  rages against the loss rather than rising strengthened, blocking the pain with self-justification ("it was
  worth the price").

---

## Chiastic Mirroring — cross-cutting structural principle, applies to every arc type and Midpoint mechanic

Every major beat has a deliberate mirror partner on the opposite side of the story, with the Midpoint standing
alone as the unpaired axis everything pivots around: **Hook ↔ Resolution, Inciting Event ↔ Climactic Moment,
First Plot Point ↔ Third Plot Point, First Pinch Point ↔ Second Pinch Point.**

- **The mirroring is about contrast, not sameness** ("comparative symmetry") — a paired beat should read as a
  deliberate reversal of its partner (the Lie's symbol becomes the Truth's symbol; a scene that once trapped the
  character now frees her), not a repeat.
- **Lighter-weight fallback**: when full plot-level mirroring isn't feasible, mirror or invert specific symbols,
  settings, colors, or which named characters are present at paired beats instead.
- **Workflow note**: figure out the ending first, then retrofit the beginning to set it up — easier than forcing
  an already-written beginning to resolve into a mirrored ending after the fact. Lock the Climax/Resolution's
  content before finalizing the Normal World/Characteristic Moment content, not after.

---

## The Ending-Shape Cross-Mapping Table

Three taxonomies operate at three genuinely different scopes, so this is a cross-mapping, not a merge:
**Weiland's Arc Types** (whole-story arc shape), **Bell's Five Shapes of Endings** (climax outcome), and **the
New Normal World's five flavors** (resolution beat staging/texture, from *Next Level Plot Structure*: 1 — same
place, she sees it differently; 2 — same place, she actively improves it; 3 — same place, transformed by
others' actions; 4 — contrast between her change and an unchanged setting; 5 — a natural, permanent departure).
Mapped directly onto the already-codified Ending Distribution law's three categories (see
`../Design_Principles/No_Good_Endings.md`), so Stage 5 builds toward that law rather than just gesturing at it:

| Weiland Arc Type | Bell's Shape | New Normal World Flavor | Ending Distribution Category |
|---|---|---|---|
| Positive Change Arc | **Lead Sacrifices** (primary template — closest match to this project's own mutual-sacrifice mechanic) | 2 or 5 | Costly-positive |
| Flat Arc | Lead Wins (she already has the Truth, uses it to fix the world around her) | 2 or 3 | Costly-positive or bittersweet, depending on what fixing the world costs her |
| Disillusionment Arc | **Genuinely underdetermined** — wins internally (overcomes the Lie) while the external Want may still be lost; can legitimately straddle Lead Wins and Lead Loses rather than picking one cleanly | 4 (the tragic contrast) | Bittersweet |
| Fall Arc | **Lead Loses** (already the explicit Pariah Failsafe template) | 4, or a permanent negative departure | Negative |
| Corruption Arc | **Lead "Wins" But Really Loses** (already flagged as the same beat, two names, in the original book-mining) | 4 | Negative |

- **Disillusionment's straddle is worth stating as a real nuance, not smoothing it over** — it's the one arc
  type where a Doll's ending may need to be built as two simultaneous, partially-contradictory reads (an internal
  win layered under an external loss) rather than resolved to one shape. This is confirmed by real, independent
  worked examples — see `../Worked_Examples/`.
- **Bell's fifth shape, Open-Ended, deliberately has no row above** — already flagged in the original book-mining
  as a real caution specific to this project: a game audience expects definitive closure on a companion arc more
  strongly than a novel reader does, since the player invested active choices, not just reading time. Use
  sparingly and deliberately, not as a default escape from committing to one of the other four shapes.
- **This table is a menu, not a per-Doll distribution requirement — read it against `Companion_System.md`'s
  canonical "No Good Endings" law (see `../Design_Principles/No_Good_Endings.md`), not in isolation.** Two of the five rows above land in the Negative category,
  which could be misread as "40% of a Doll's endings should be negative" if this table were applied
  mechanically. It shouldn't be: the canonical law requires negative endings to be a minority of a *specific
  Doll's actual offered endings* (one, or at most a handful, out of her full set), with bittersweet as the
  largest category by a real margin — this table is the lookup for *characterizing* whichever arc types get
  chosen for a given Doll's branches, not a instruction to draw evenly from all five rows. Plan the actual
  distribution per Doll first (per the canonical law's own "plan the distribution explicitly, up front" step),
  then use this table to build out each chosen branch's specific shape.
- **Mechanical stakes on the Fall/Corruption rows, cross-referenced from `Companion_System.md`'s Double Gate**:
  a companion questline resolving into the Negative category (Fall or Corruption Arc, per this table)
  **permanently disqualifies that character's Romance questline for the rest of the playthrough**, regardless of
  MACHINE build or traits — this isn't a Stage 5 rule in its own right, just a reminder that picking a Negative
  row here has a real downstream mechanical consequence already codified elsewhere.

*(Canon cross-check performed 2026-08-09: this table's mappings were checked directly against
`Companion_System.md`'s "No Good Endings — Ending Distribution and Cost Calibration" section. No contradictions
found — the two notes above are clarifications to prevent misreading, not corrections to anything that was
actually wrong.)*

---

## Series-Spanning Arc Models

Directly relevant to this project's DLC structure. Two models, not competing — pick deliberately per recurring
companion:
1. **One overarching arc across the whole series** — the Lie introduced in the base game isn't fully resolved
   until a much later DLC; beats stretch proportionally across installments rather than compressing into one.
2. **A fresh arc per installment** — a returning companion gets a new, self-contained Lie each DLC, optionally
   building on Truths already secured earlier (Weiland's own example: Thor gets a Positive Change Arc in film
   one, then a Flat Arc in film two, using his already-won Truth to change the world around him).
- **Bonus layering technique**: even within one overarching arc, each installment can carry its own smaller,
  self-contained "mini-Lie" contributing to the larger Lie's eventual resolution, rather than each DLC being an
  unmarked slice of one continuous journey.

---

## Common Ending Failure Modes — standing pre-ship checklist

- **Deus ex machina** — any last-minute rescue or resolution must be set up by the protagonist's own prior
  actions, not arrive as unearned coincidence. **Cross-reference**: this is the same underlying failure as
  Lisle's "Brain Transplant" sin (already captured in Stage 3/4 material) viewed through the plot-mechanism lens
  rather than the character-consistency lens — never let a character solve the climax using a capability the
  story hasn't established she has, and never let the climax's resolution arrive from outside what the
  protagonist herself set in motion.
- **Loose ends** — route minor-character-fate wrap-up through a single returning secondary character in one
  focused late scene, rather than a clumsy info-dump through the main plot itself.
- **"Only a dream"** (or any twist retroactively invalidating everything already experienced) — a hard caution
  against ever using this shape for a full companion questline or DLC main questline; the identical device can
  work in short-form content where the twist is baked into the format's own expectations from the start.
- **The talkative villain** — never let a villain's expository monologue be the mechanism that buys the
  protagonist time to escape or be rescued; deliver any necessary exposition either well before the moment of
  maximum urgency, or after the villain has already been dealt with.

---

## QA Tools

- **The "same event, beginning vs. end" consistency check** (Weiland) — if she had to face the Climax's events
  back at the story's beginning, would she react the same way she does at the end? If yes, the arc isn't doing
  its job regardless of how much has "happened" to her along the way.
- **Rewards and Punishments as the branching-consequence engine** (Weiland) — Lie-aligned choices trend worse,
  Truth-aligned choices trend better, the gap narrowing toward "yes, but..." partial outcomes as the arc
  progresses. **Cross-reference**: this is the mechanical engine that should be producing the Ending Distribution
  law's actual outcome spread (minority-negative, majority-bittersweet, costly-positive) at the level of
  individual dialogue/quest choices, not just at the level of the final ending selection.

---

## A Known Limitation, Worth Keeping

For a Flat-Arc-adjacent character whose ending outcome is fundamentally reactive to another character's arc
rather than her own choices, the Ending-Shape Cross-Mapping Table may need to be read against that other
character's own arc type, not hers — she doesn't "fail," the other character's story does, and her ending
inherits that valence rather than generating it. This is a real, named limitation of the table as built, not
smoothed over.

Similarly: for a character whose full arc needs to remain reachable regardless of what else happens in the
story, none of her structurally load-bearing beats should be tied to something *entirely optional* that the
surrounding plot might skip or touch only once.

---

## Worked Examples

Two full, real-world run-throughs of this entire stage — every tool above applied to real, specific
characters, checked against their actual established material rather than invented fresh — live in
`../Worked_Examples/` (`Calethina_Case_Study.md` and `Ayako_Hayashi_Pipeline_Summary.md`), kept separate so this
Pipeline file itself never depends on knowing anything about those characters or their setting. One of them
caught and fixed a real structural accessibility flaw before it shipped (see
`../Design_Principles/Always_Present_Gating.md` for the generalized rule that came out of it); the other
independently confirmed the Disillusionment-straddle edge case in the Ending-Shape table above, a second
real-world data point for a genuine, still-open limitation of the table as built. Worth reading once, purely as
a demonstration of what "running the tools" actually looks like in practice — including what it looks like when
the methodology itself gets something wrong and has to be corrected — before applying this stage to your own
first character.

## Open, Undecided

> ⚠️ Versions differ: the game version lists the open items below; the prose version reads "No remaining open
> items for this stage."

- Calethina's Second Pinch Point (see `../Worked_Examples/Calethina_Case_Study.md`) — deliberately left open,
  not extended by the "Unusual Readings" Trigger System, which resolves only the Inciting Event through First
  Pinch Point.
- The specific trigger content for the "Unusual Readings" Trigger System's district-bound and non-district-bound
  pools — the system itself is resolved and written into `Personal_Questline_Summary.md`; the actual 39+ and
  20-40 individual triggers are not yet designed, deferred until the relevant districts and the wider world are
  further along.
- The Ending-Shape Cross-Mapping Table's blind spot for reactive/Flat-Arc-adjacent companions (see the Accord
  ending analysis in `../Worked_Examples/Calethina_Case_Study.md`, and "A Known Limitation, Worth Keeping"
  above) — not resolved, flagged as a known limitation of the table as currently built.

**Resolved 2026-08-09:** the canon cross-reference check against `Companion_System.md` (and by extension the
district/DLC/main-quest equivalents it points to) has been performed — see the note directly under the
Ending-Shape Cross-Mapping Table above. No contradictions found.
