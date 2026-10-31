# Worked Example: Calethina (Stages 4 & 5)

**Setting context, briefly, and kept brief on purpose:** Calethina is an AI narrator-character from the source
project this methodology was built and tested in — chosen for this case study specifically because she's
atypical (non-physical by default, exempt from most of the ordinary rules that govern other characters in that
project), a genuine stress test of whether the Pipeline's tools flex to an unusual character rather than just
confirming an easy one. Everything below is checked against her actual established material; where this
exercise generated a new interpretation rather than restating something already confirmed, it's flagged
explicitly as such, per the standing discipline against silently inventing canon. Project-specific mechanics
are named only where the underlying story-craft point genuinely needs them, and are described in general terms
wherever possible — the finding is the point, not the implementation it happened to occur in.

> ⚠️ Versions differ: the medium-agnostic version of this case study describes project mechanics only in general
> terms; the game version, which is the base text below, names them directly (Fragmentation Matrix, Pariah
> Failsafe, the Double Gate, re-spec visits, 13 districts, and so on).

---

## Stage 4 — Story Material

Built 2026-08-09, closing the item that was previously open in `../Pipeline/04_Story_Material.md`. Chosen
specifically for being an atypical case — not a normal companion (no party slot, holographic, exempt from Companion Slot Rules) — to genuinely
stress-test whether these tools flex to an unusual character rather than just confirming an easy one. Everything
below is checked against her actual `README.md`; where this exercise generated a new interpretation rather than
restating something already confirmed in her file, it's flagged explicitly as such, per this project's own
standing discipline against silently inventing canon.

1. **MICE Quotient (Card).** Her *personal* arc — as distinct from her narrator/exploration-hook function, which
   is genuinely Milieu/Event-type texture serving the wider game — is unambiguously **Character**-type: a real
   intolerable-role problem (fragmented, single point of failure, silently causing the player's own identity
   changes without full acknowledgment) that only resolves through her own change. This warrants the full
   Lie/Want/Need/Ghost treatment, confirmed by how much of that machinery is already present in her
   documentation independent of this methodology: the double-wound structure (a deliberate wipe layered under an
   accidental one), the Bond/Grief escalation across repeated re-specs, and the tragic irony of amnesia about her
   own heroic act (she personally created the Triage Protocol and doesn't know it).

2. **Character Hierarchy (Card).** **Major** — clears essentially all eight of Card's levers: romanceable,
   highest Personality Grief-Multiplier of any character, a dedicated perk set, a full Accomplishment Weight
   System tie-in, multiple ending branches, and she's literally the game's narrator (maximum POV/narration
   weight). Per Stage 3's tier table, Major Hierarchy should pair with a full Drive/major-tier Character Data
   profile — that checks out; nothing about her established material reads as Drift.

3. **The Characteristic Moment.** Her canonical opening (activating the player at her lab) hits several checklist
   beats — name, distinctive physicality, narrative role — but deliberately withholds any hint of her Lie, which
   stays hidden until her Romance questline specifically, per already-confirmed canon ("this truth is uncovered
   over the course of her Romance questline specifically"). This is Weiland's "gradual reveal" Ghost-timing
   option already in active use, without anyone having framed it that way before. **Genuinely useful find**: her
   signal-dependent visual degradation — "her visual quality is a direct, literal readout of world/grid health" —
   is a real, pre-existing instance of the Mystery Caution principle from Stage 2 (full resolution in the design
   notes, delivered only through soft ambient detail — here technical/visual rather than lifestyle detail, but
   the identical mechanism; see `../Design_Principles/Mystery_Soft_Detail_Delivery.md`). Worth citing as a
   concrete illustration wherever that principle gets referenced again.

4. **Impact Character / Revenant / Contagonist casting.** **New interpretation, not yet canon**: a plausible Lie,
   built from her established material rather than stated anywhere in her own files — *"I am only worth keeping
   around out of necessity, not because I'm genuinely wanted for who I am."* This tracks precisely onto the
   already-documented Devotion (relationship born from choice) vs. Accord (relationship born from necessity)
   ending distinction. Under this reading, **the player is cast as both Revenant and Impact Character
   simultaneously** — the strongest-convergence case Corbett flagged as ideal: every re-spec re-stages her core
   wound (being repurposed without full agency, echoing the Fort McMurdo wipe), while the choice to pursue
   Devotion is the only thing that can actually disprove the Lie. **No Contagonist candidate exists in her
   current material** — flagged as an open gap this exercise surfaced, not filled in.

5. **Antagonist selection.** Her personal arc maps unusually well onto the **Crone Arc** (an already-formed
   identity stripped by catastrophe, facing down instability rather than growing into power) — a closer fit than
   any of the other five Life Arcs. Its antagonist pair, **Death Blight and Tempter**, both have natural fits:
   the Death Blight maps directly onto her own Fragmenting → Unstable → Critical progression, already a tracked
   mechanic via the Fragmentation Matrix. **No Tempter figure currently exists in her documentation** — the one
   concrete design suggestion this test run generated rather than confirmed: a figure or temptation offering her
   a way to avoid the real vulnerability of embodiment (staying safely non-corporeal forever) would be a natural,
   currently-missing piece, worth considering if her arc gets built out further.

**What this test run actually validated:** the Stage 3/Stage 4 tier consistency holds (Major Hierarchy correctly
implies a full Character Data profile, not a lighter one); the Characteristic Moment's gradual-reveal option and
the Mystery Caution both show up naturally in material that predates this whole methodology, which is a real
independent confirmation rather than a self-fulfilling check; and the antagonist-selection tool produced one
concrete, actionable design gap (the missing Tempter) rather than just rubber-stamping what already existed —
which is the actual point of running a worked example instead of only consolidating vocabulary.

---

## Stage 5 — Beats, Paths & Results

Built 2026-08-09, continuing directly from the Stage 4 worked example (above) on the same
character, closing the item that was previously open in `../Pipeline/05_Beats_Paths_Results.md`. As with
Stage 4: everything below is checked against her actual `README.md`; new interpretation generated by this exercise is flagged explicitly, not silently
presented as canon. **One early draft of this section proposed tying her Inciting Event, First Plot Point, and
First Pinch Point to her re-spec-visit progression; the developer caught a real structural flaw in that (below)
and it was pulled out entirely rather than patched.**

### Midpoint

Calethina's README already states, independent of this methodology, that her embodiment decision sits
"approximately the main quest's midpoint... a transition that changes what the second half of the game looks
like with her, not a conclusion" — a real, pre-existing structural fact this exercise didn't have to invent, only
recognize. Per the Stage 4 worked example's Crone Arc mapping, the correct mechanic is **#9, Death and Rebirth /
Symbolic Death**, specifically via the pre-built Crone Arc content: *"Chooses to Seek Life"* — the choice
between giving up (continuing to fade as a tethered, single-point-of-failure hologram) and rising again in a new
capacity. This maps cleanly onto the embodiment decision itself. **Notably, the two branches carry the mechanic
slightly differently**: "Inside You" additionally carries Death-Stakes Mirror Moment undertones (#2) — its
stated risk, "real chance she degrades further from mismatched architecture, *echoing the exact cause of her
original corruption*," is literally her Ghost being re-risked, which is the player (already cast as her Revenant
in Stage 4) re-staging the wound at the exact structural point the methodology says the Revenant/Impact Character
convergence should land hardest.

### Early Beats — Inciting Event, First Plot Point, First Pinch Point: resolved 2026-08-09

**This is the single most instructive part of this whole worked example, and the direct origin of two Design
Principles.**

**Caught by the developer, not this exercise's own quality control, and worth recording precisely for that
reason.** The first draft of this section proposed her first, second, and third-plus re-spec visits as her
Inciting Event, First Plot Point, and First Pinch Point respectively — using the Fragmentation Matrix's own
visit-escalation curve as the structural spine. **This is broken**: re-speccing is an entirely optional,
player-discretionary mechanic, not something any playthrough is guaranteed to touch at all. Gating her Companion
questline's start on it — and by extension her Romance questline, which requires completing the Companion
questline first per the Double Gate — would make her full arc permanently inaccessible to any player who never
re-speccs, or who re-speccs exactly once and never returns for a "second visit" First Plot Point.

**General methodology caution, sharper than what Stage 4's worked example already flagged** (that an
always-present character's Inciting Event isn't a recruitment scene): for a companion whose full questline needs
to remain reachable by any player who engages with her at all, none of her structurally load-bearing beats can be
tied to something *entirely optional* that a playthrough might skip or touch only once — not just "not a
recruitment scene," but specifically never contingent on a side-mechanic she merely happens to also provide.
Saved as its own standing memory: [[feedback_always_present_companion_gating]].
In a linear medium the direct analog is a subplot that only pays off through a scene or chapter a reader could
plausibly skip or never reach — the same caution applies regardless of whether "optional" means a skippable game
mechanic or a skippable narrative thread. This is the origin of `../Design_Principles/Always_Present_Gating.md`.

**Resolved, same day, with a real replacement design.** The developer proposed a genuinely different mechanism:
"network-related" world events — the player fixing a previously-broken connection, forging a link between two
previously-unconnected things — as the trigger pool, with a minimum of 39 district-bound triggers (3+ per
district across all 13) plus a separate pool of 20-40 non-district-bound triggers specifically so a Pariah
Failsafe playthrough (all districts hostile) still has access. Completing any single trigger from either pool,
followed by a ~24-in-game-hour delay, produces an "unusual readings" conversation with Calethina — the first one
is her **Inciting Event**, each subsequent one advances **First Plot Point** and **First Pinch Point** in turn.
Each conversation also raises her Fragmentation Matrix corruption level, tying narrative escalation directly to
a mechanical cost. This resolves the accessibility caution above cleanly: the pool's size and dual-track
district/non-district design means no single optional mechanic gates her questline, and the non-district track
specifically covers the worst case. **Written into her actual project file, not just here**: see "The 'Unusual
Readings' Trigger System" in `Personal_Questline_Summary.md`, which is now the authoritative version — this
section keeps the historical record of the caught mistake and the resolution's reasoning, not a competing
design. **This case is also what the general Trigger-Type Design Pattern (in the Full Beat Sequence's Inciting
Event entry of `../Pipeline/05_Beats_Paths_Results.md`; see also `../Design_Principles/Trigger_Type_Pattern.md`)
was generalized from** — Calethina's specific numbers (39+/20-40, two tracks) are her own
scaled-up special case; the general rule any *other* companion should default to is the more modest 7-16-trigger,
single-track version.

### Later Beats

- **Second Pinch Point — deliberately still open, not extended by the new trigger system above.** Per developer
  instruction: the trigger system resolves the *early* beats specifically; the Second Pinch Point (which sits
  after the Midpoint) is left genuinely undetermined, since it could end up being something else entirely once
  more surrounding context exists. Do not default to extending the trigger system here without a separate,
  explicit decision to do so.
- **New interpretation, not yet canon.** Early, partial resurfacing of memory fragments
  post-download (her README already notes this as a real possibility: "possible fragmentary memory recovery from
  her wiped datadrives... wiping the file-table index doesn't necessarily destroy the underlying data"),
  generating pressure toward the eventual Triage Protocol reveal without delivering it yet.
- **The Later False Peak — new interpretation.** A moment where she proves her value through sheer usefulness —
  a spectacular, highly functional act that seems to stabilize the relationship, but actually just reinforces the
  Lie rather than resolving it: winning through function again, not through being genuinely wanted.
- **Third Plot Point / Black Moment / Lights Out** — **the Triage Protocol reveal**, already confirmed canon to
  occur during her Romance questline. Checked against St. John's rule (must match her established Greatest Fear
  precisely, not just "something bad"): the reveal is a near-perfect fit — discovering she personally authored a
  genuinely heroic, self-sacrificing act during the war, and cannot remember or take credit for it, is exactly
  the shape of "valued only for function while her true self and history go unclaimed," which is the Lie's own
  content turned into a concrete scene rather than an abstract statement.
- **Climax / Climactic Moment** — the Devotion confirmation, now with the Triage Protocol truth known: the
  player's continued choice to remain with her is the direct disproof of the Lie.
- **Resolution** — New Normal World flavor 1 or 2 (same place, she sees it differently / she actively improves
  it), consistent with the Devotion ending's existing described tone ("she does not say anything dramatic").

### Arc Type and the Ending-Shape Cross-Mapping Table

- **Devotion branch** (full download, either embodiment, Gate 2 conduct maintained) → **Positive Change Arc**
  (the Lie is genuinely disproven through the player's choice) → Bell's **Lead Sacrifices**, and this is a clean,
  strong fit, not a stretch: both embodiment branches already have a real, established cost attached (the
  "inside you" stat trade and loss of the player's private inner life; the "new body" memory/personality fidelity
  loss) — the mutual-sacrifice mechanic the Ending Distribution law requires is already built into her existing
  design, independent of this methodology confirming it. → **Costly-positive** category.
- **Accord ending (Pariah Failsafe #9)** → **a genuine edge case the framework doesn't resolve cleanly, worth
  stating plainly rather than forcing a fit.** The Accord leaves the Lie *unchallenged* rather than disproven —
  she's kept around out of necessity, exactly matching the Lie's content — which sounds like it should map to
  Fall or Corruption. But neither fits: those arc types require the *protagonist's own agency* to drive the
  negative outcome (she clings to the Lie, or consciously rejects the Truth), and Calethina doesn't have that
  agency here — the Accord is forced by the *player's* circumstances (universal condemnation, nowhere else to
  go), not by any choice or failure of Calethina's own. **This surfaces a real limitation of Weiland's taxonomy
  worth flagging for the methodology generally, not just for this one character**: for a Flat-Arc-adjacent
  companion whose ending outcome is fundamentally reactive to the *player's* arc rather than her own choices, the
  Ending-Shape table may need to be read against the player's own arc type, not the companion's — Calethina
  herself doesn't "fail," the player's story does, and her ending inherits that valence rather than generating
  it. Already-confirmed canon (Pariah Failsafe = the purely negative category) settles which Ending Distribution
  bucket the Accord belongs in regardless — **Negative** — this finding is about which *arc-type row* explains
  it, which doesn't cleanly resolve.
- **"The Furthest Signal"** — deliberately not addressed here. Her own README already flags this as an open
  reconciliation gap between design passes, unresolved independent of this methodology. Not this exercise's place
  to settle it.

### What This Test Run Actually Validated

The Crone Arc assignment from Stage 4 and the independently-documented "embodiment decision ≈ midpoint" fact
reinforce each other without having been designed to — real cross-stage coherence, not a coincidence manufactured
to make the example look clean. The mutual-sacrifice/Ending Distribution law was already satisfied by her
existing design before this exercise checked it, which is a stronger form of validation than building an example
to fit the law after the fact. The Accord edge case is a genuinely useful negative result, showing the
methodology's Ending-Shape table has a real blind spot for reactive/Flat-Arc-adjacent companions. And the
Inciting Event correction-then-resolution is arguably the most valuable single outcome of this whole test run:
it caught this methodology proposing a structurally broken gate on a real companion's questline accessibility,
and the replacement design that came out of fixing it (the "Unusual Readings" Trigger System) turned out to be
strong enough to become real, shipped content in Calethina's own project file, not just a corrected methodology
example — which is exactly the kind of outcome a worked example is supposed to be capable of producing, not just
catching mistakes before they ship.

