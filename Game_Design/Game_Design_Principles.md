# Game Design Principles

Core design decisions and guiding principles that apply across the entire game and its DLCs. These are binding design commitments, not suggestions. When in doubt about a design direction, check here first.

**Two games' versions.** Unlabeled text is Inner Tepenia's, and holds for Outer Tepenia 1 too unless a variant follows it. Where Outer Tepenia 1's text differs or adds to it, it is kept and labeled as the Outer Tepenia variant; a variant that names the whole series says so in its own text.

*Outer Tepenia variant:* principles are carried over directly where the philosophy is identical, and reworked where Outer Tepenia's shape (open-world, orbital/Jovian setting, real-time 1st-/3rd-person) differs from Inner Tepenia's (city-scale, isometric, turn-based).

---

## Absolute Laws (Outer Tepenia variant)

These three are laws, not principles: they are not allowed to be broken, superseded, or exception-cased. Everything else in this document is downstream of them.

### Law 1 — Player Freedom & Agency Reigns Supreme
Nothing is obligatory. No mandatory content, no forced choices, no artificial gates on how the player engages with the game.

### Law 2 — Old-School Fallout Is the Base Reference
Fallout 1, 2, and New Vegas together form the central base reference for game design. Other games' features may be incorporated, but only on a case-by-case, gap-filling basis:
- If another game has **[A]** and old-school Fallout has no equivalent, **[A]** is a viable option to consider.
- If another game has **[A]** and old-school Fallout has **[B]** for the same thing, **[B]** wins, every single time, no exceptions.

### Law 3 — New Vegas Is the Gold Standard Within Fallout
Within the old-school Fallout reference (Law 2), New Vegas is the ruling standard:
- If Fallout 1/2 have **[A]** and New Vegas has no equivalent, **[A]** is a viable option to consider.
- If Fallout 1/2 have **[A]** and New Vegas has **[B]** for the same thing, **[B]** wins, every single time, no exceptions.

---

## Narrative Principles

### No Good Endings
All endings — main story paths, secret endings, faction devotion endings, pariah failsafes — are bittersweet at best. There are no clean victories, no unambiguous triumphs. The player can do meaningful things and make things better than they would otherwise be, but the world is too damaged and the stakes are too high for any outcome to be uncomplicated. *Inner Tepenia variant:* this applies to all endings across all 116+ resolution paths.

### The Player Is a Witness as Much as an Agent
The game presents a world with its own momentum, its own grief, its own history. The player acts within that world and changes things — but the world is not a backdrop waiting for the player to give it meaning. It has meaning already. Player agency is real and consequential; it is not the only thing that matters.

---

## Reference Principles

### Fallout Precedence Law
When Fallout 1/2 and Fallout: New Vegas conflict as design references, New Vegas always wins. No exceptions. This applies to mechanics, tone, quest design, companion design, and any area where the two games make different choices. Fallout 1/2 remain relevant as spiritual predecessors, but New Vegas is the binding reference.

*Outer Tepenia variant:* governed by Absolute Laws 2 and 3 above: old-school Fallout (1/2/NV) is the base reference for tone, quest design, companion design, and RPG structure, with New Vegas as the gold standard where Fallout 1/2 and New Vegas differ. This does not govern space flight or zero-g mechanics, which fall under a separate reference below.

*Outer Tepenia variant:* **Confirmed gap-fill case — Romanceable Companions:** old-school Fallout has no romanceable companion system, so this is a case of "another game has [A], Fallout does not" under Law 2. Romanceable companions are confirmed as a feature Outer Tepenia 1 will use. This is the first confirmed instance of the general rule: any feature where another game has [A] and Fallout has no equivalent is to be considered viable on the same case-by-case basis, and adopted when it fits.

*Outer Tepenia variant:* **Confirmed application — AP Combat System:** this is a direct application of Law 3, not a gap-fill case. Fallout 1/2 have a turn-based grid-AP combat model; Fallout: New Vegas has a real-time combat model with an AP-gated VATS system layered on top. Per Law 3, New Vegas's model wins: **New Vegas's AP/VATS system is the fundamental basis for Outer Tepenia 1's AP system**, not Fallout 1/2's turn-based grid model. Adjustments for an outer-space/zero-g context are expected and permitted — this is the starting point, not a rigid, unadaptable copy.

### Flight Reference Standard (Outer Tepenia variant)
Space flight and zero-g mechanics are gameplay systems, not narrative or thematic centerpieces, and sit outside the Fallout Precedence Law. **Everspace 2**, **CHORVS**, and **No Man's Sky** are the binding design references for these systems specifically. No Man's Sky is a flight-mechanics reference only — it does not inform tone, narrative, or thematic design, which remain governed by the Absolute Laws and Fallout Precedence Law above. Where flight/zero-g design questions arise, check these references before inventing a new approach.

### Camera Reference Standard (Outer Tepenia variant)
This is a gap-fill case under Law 2 — old-school Fallout's camera systems (isometric-era, and New Vegas's limited third-person) don't cover what's needed here, so an outside reference applies.

- **3rd-person mode:** free camera, able to swivel a full 360 degrees around the player character. Primary reference: **Fallout 4**. Secondary/exploratory references for camera feel: **No Man's Sky**, **Horizon: Zero Dawn**, and possibly others as they come up.
- **1st-person mode:** standard 1st-person camera — no special reference needed.
- The player can toggle between 1st- and 3rd-person freely (per the existing Fallout: New Vegas-style toggle already established for this game).

---

## Content Scope Principles

### Main Game Scope Standard
The base game (no DLCs) targets:
- **Main story (critical path, trigger → final resolution):** approximately 15–25 hours
- **Optional side-content (exploration, side quests, companion questlines, faction content, lore, collectibles, alternate paths):** 200+ hours
- **Speedrun ceiling:** it must be realistically possible — for a player who thoroughly knows the game's mechanics and uses them creatively and deliberately — to complete the main story in under one hour; this is not an exploit or a bug but a legitimate expression of deep game knowledge; it requires absolutely knowing what you are doing

The speedrun possibility is a design commitment, not an accident. It implies: no mandatory content that cannot be bypassed through skill and knowledge; no artificial locks that force playtime regardless of player competence; mechanics deep enough that mastery genuinely compresses time; a critical path that is achievable without side content. The game respects player knowledge. A first-time player who stumbles through in 25 hours and a master player who completes it in under an hour are both playing the same game correctly.

*Outer Tepenia variant:*
- **Optional side-content (exploration, side quests, companion questlines, faction content, lore, collectibles, alternate paths):** 800+ hours
- **Speedrun ceiling:** the aspirational target is a critical path completable in **under 15 minutes** by a player with deep, deliberate mastery of the game's mechanics — more aggressive than Inner Tepenia's sub-1-hour ceiling — provided this is realistically achievable given the game's actual systems. If 15 minutes proves infeasible once mechanics are built out, sub-1-hour is the fallback floor, not sub-15-minutes as a hard requirement regardless of cost.
- A first-time player who stumbles through in 25 hours and a master player who completes it in minutes are both playing the same game correctly.

### DLC Scope Standard
Each of the seven DLCs follows a consistent scope target:
- **Main questline (trigger → completion of central problem):** approximately 4–6 hours
- **Optional side-content (exploration, side quests, lore, collectibles):** approximately 10–20 hours
- **Total potential playtime per DLC:** approximately 14–26 hours

*Outer Tepenia variant:* each DLC follows the same scope target as Inner Tepenia's.

The main questline should be tight, purposeful, and completable in a single extended session or two shorter ones. The optional content should reward players who want to live in the region — not padding, but genuinely interesting material that deepens the world without being required to understand the main story.

**The guiding standard for both main game and DLCs:** a player who completes only the main questline should feel satisfied; a player who does everything should feel like they have inhabited a place.

---

## Series-Wide Systems (Outer Tepenia variant)

### MACHINE Stats Are Identical Across the Whole Series
The MACHINE stat system (the 7 attributes and their effects, determinative skills/abilities/areas) is not adapted or reinterpreted for Outer Tepenia — it carries over **directly and identically** from Inner Tepenia, and will remain identical across the entire "[...] Tepenia" series: Inner Tepenia, Outer Tepenia 1, Outer Tepenia 2, and Outer Tepenia: New Centauri. Unlike the rest of the copied Game-Mechanics folder, MACHINE stats are not reference-only — they are binding, canonical, and series-wide. See `Game-Mechanics/Character-Creation/MACHINE_Stats.md` and `MACHINE_Stat_Influence_Map.md`.

### Perks and Skills Carry Over, Subject to Contextual Adjustment
The perk and skill system stays generally and mostly the same as Inner Tepenia's, but — unlike MACHINE stats — it is not frozen. Individual perks/skills may be adjusted, added, or cut depending on what each specific game's context (genre, setting, mechanics) requires. Treat Inner Tepenia's perk/skill design as the strong default, not an untouchable constant.

### NODE Targeting System — Shared Identity, Format-Specific Implementation
NODE (Neural Operating Directive Enhancement), Tepenia's equivalent of Fallout's VATS, is shared across the series by name, core identity (AP-gated, body-part targeting, MACHINE stat integration), and conceptual model (see `Game-Mechanics/Combat/Targeting_System.md`). How it actually plays is format-specific: Inner Tepenia's is turn-based; Outer Tepenia's games use it the way VATS works in Fallout: New Vegas — a real-time-with-pause targeting mode — per the AP Combat System reference above (Reference Principles).

### Item Degradation and Repair
Weapons, armor, and clothing degrade with use, and a repair system exists to offset that degradation. This is largely an inheritance of old-school Fallout's existing condition/repair model under the Fallout Precedence Law — New Vegas's approach (repair kits, cross-category repair) is the default starting reference per Absolute Law 3 unless a specific difference is called out. Confirmed as a feature 2026-06-30; full mechanical design (degradation rates, repair costs/methods, whether clothing degrades as its own slot distinct from armor) not yet done.

---

## World Design Principles

### Geography Is Character
Every city in Tepenia has a specific geographic identity that shapes its culture, architecture, economy, and psychology. Climate, latitude, elevation, coastal vs. inland position, proximity to other cities — these are not background details. They are the primary reason each city is the way it is. Design decisions about cities should start with geography.

### Environment, Control, and Access Are Character (Outer Tepenia variant)
Every settlement in Outer Tepenia — moon colony, orbital station, shellworld, ring habitat — is shaped by three named primary drivers, none of which are background detail:
- **Physical environment:** radiation exposure, tidal heating, gravity well, distance from Jupiter, degree of isolation, orbital mechanics.
- **Faction/founder control:** who built it, who governs it now, and what kind of power (corporate, resistance, independent, criminal, other) that implies.
- **DNA-tech access:** how widespread, restricted, or absent DNA-as-tech is in that settlement, and what that does to its economy, culture, and psychology.

Design decisions about any location should start from these three factors, the way Inner Tepenia's cities start from geography.

### The Subnets Are Six Different Truths
After the Planetary Split Brain, each Arcanet subnet holds an isolated version of post-war history. These versions are not simply incomplete — they may actively contradict each other. Each DLC is an encounter with a different subnet's truth. The player, who moves between subnets, is the only entity in Tepenia who can hold all six versions simultaneously.

### Multiple Truths — status: undecided (Outer Tepenia variant)
Inner Tepenia's "Subnets Are Six Different Truths" principle — contradictory histories held by different DLC subnets, with the player as the only entity who can hold them all — has no confirmed Outer Tepenia equivalent yet. Whether Outer Tepenia needs its own version of this device (DNA-as-tech is a plausible mechanism for it) is an open question, not yet decided. Revisit once more of the plot/DLC structure exists — do not assume this principle applies until it's explicitly confirmed.

---

## Technical Principles (Outer Tepenia variant)

### Full Mod Support
The game is designed for full mod support from the ground up, not bolted on after release. This is a binding production commitment, confirmed 2026-06-30, intended across the series (Inner Tepenia and the Outer Tepenia games). Specific technical implementation (modding API, tooling, what's exposed to modders) is not yet designed — this principle establishes the commitment, not the architecture.

---

*This document should grow as new binding design decisions are made. Add a principle here when it is explicitly confirmed — not when it seems likely, not as a best guess, but when the developer has stated it clearly and it should govern future decisions.*
