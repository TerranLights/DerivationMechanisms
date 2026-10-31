# Secret Endings — Design Framework

**Status:** binding design principles for Toronto Fell Out's eventual secret endings, with zero populated content. Adapted from Inner Tepenia's ten-file Secret-Endings folder (`Alternate_Minmax_Endings.md`, `Fast_Minmax_Endings.md`, `District_Idolized_Endings.md`, `Faction_Devotion_Endings.md`, `Failsafes.md`, `Near_Pariah_Endings.md`, `Wild_Child_Endings.md`, `Hidden_Paths_And_Secret_Endings.md`, `Mechanics_Creative_Combos.md`, `Remaining_Failsafe_Categories.md`), consolidated into this single file because Toronto Fell Out has no districts, factions, or NPCs yet to populate ten separate ending documents with. **This file replaces all ten** — it is the framework those files would eventually be written against, not a summary of Inner Tepenia's own endings.

Every specific ending name, trigger, district, and faction reference from the source material has been stripped. What's kept is the reusable design law (World Trigger), the reusable per-ending template, and the reusable taxonomy of reputation-extremity categories. **TBD placeholders throughout** — this file is a shape to fill in once Toronto Fell Out has its own districts, factions, and companions.

---

## The World Trigger Law (binding)

**Every secret ending's access point must be a physical, discoverable object or location in the world — never a hidden stat check, a popup notification, or an NPC who approaches the player first.**

The underlying discipline: a player who knows the *stat/reputation prerequisite* for a given secret ending should be able to figure out *where to look* for its trigger, the same way a player who knows they need a bobby pin and 40 Lockpick skill knows what a locked door represents. The trigger object itself is never hidden behind an additional, separate check — meeting the ending's real requirement (a reputation threshold, a stat combination, a completed questline) is what makes the trigger recognizable or reachable, not an extra roll bolted on top of it.

**What this rules out:**
- An NPC who walks up to the player and offers the ending directly, unprompted.
- A trigger locked behind a *second*, unrelated stat/skill check on top of the ending's actual requirement.
- A menu prompt, achievement popup, or other non-diegetic access point.

**What this allows:**
- A specific terminal, door, notice board, registry entry, or environmental state that exists in the world for every player, but is only *reachable* (or only *recognizable as significant*) once the player holds the relevant status.
- NPCs serving as points of contact **after** the player has found the trigger themselves — the trigger itself is just never NPC-initiated.

This law applies uniformly to every category below. It is the single most important reusable idea in this document — more important than any specific taxonomy tier, because it's what keeps every secret ending feeling like a genuine discovery rather than a hidden dice roll.

---

## The Per-Ending Template

Every individual secret ending, once designed, should be written to this five-part shape:

1. **Requirements** — the exact reputation tier(s), stat/skill threshold(s), questline completion(s), or combination thereof that qualify a player for this ending. Stated precisely, not vaguely ("Idolized with [district]," not "very well liked").
2. **World Trigger** — the specific physical object/location that grants access, per the law above. Described concretely enough that a designer could actually place it in the world.
3. **The End** — the specific moment and action that constitutes reaching this ending. Not a vague fade-to-black; a defined beat the player enacts or witnesses.
4. **Main Negative Effect** — the one structural, inevitable cost this ending's "victory" imposes on the wider world. Follows from the nature of the ending, not from bad luck or an antagonist's spite. This is the same "no matter which faction wins, something real is lost" law already established for main endings (see `Main-Endings/Climax_Structure_and_District_Ending_Consequences.md`) — secret endings are not exempt from it.
5. **Minor Negative Effects** — a handful of smaller, specific downstream consequences. Useful later as epilogue material, companion dialogue hooks, or seeds for further content.

**These are complete conclusions, not punishments.** An ending reached through a Pariah-tier reputation state, an extreme stat build, or total district devotion should read as a genuine, satisfying ending for that kind of playthrough — consistent with Toronto Fell Out's general design stance that maximum player agency (including "ignore the main story entirely") should still resolve into something real. They are bittersweet like every other ending in the game, not a game-over screen dressed up as content.

---

## The Taxonomy: Six Non-Overlapping Reputation/Achievement Categories

Each category below answers a different question about "how extreme was this playthrough," and — by design — a player can only ever qualify for one category's ending at a time (the disqualification rules under each entry make the categories mutually exclusive where their conditions could otherwise overlap).

### 1. Pariah (Full)

**Condition:** Hated or Vilified reputation — specifically those two tiers, not the lower Shunned/Sneering Punk negative tiers — with **every** district and faction in the game, no exceptions.

**Disqualifier:** Wild Child status (see below) in even one district breaks the "purely negative everywhere" requirement and disqualifies Pariah.

**Design intent:** the player who has made themselves an enemy of literally everyone still gets a real, complete ending — not a death screen. TBD: how many distinct Pariah endings Toronto Fell Out wants (Inner Tepenia had 27; that count was driven by having 13 districts plus assorted factions to hang individual endings on, which Toronto Fell Out doesn't have yet).

### 2. Near-Pariah

**Condition:** Hated or Vilified with all but 1–3 districts/factions — close enough to universal condemnation to be functionally isolated, but with a small number of remaining relationships that are the defining resource of this category's endings.

**Disqualifier:** Wild Child districts don't count toward the hostile tally, and don't count as a "remaining relationship" either — they're their own thing.

**Design intent:** distinct in flavor from full Pariah — these endings are about what's still possible with a thin, precious, actively-pressured remaining relationship, not about total isolation.

### 3. Wild Child

**Condition:** Already fully defined as Toronto Fell Out canon — see `Game-Mechanics/Core-Mechanics/Reputation-System.md`. Wild Child is the bottom-right cell of the Fame/Infamy grid: **Fame Range 3 + Infamy Range 3 simultaneously** with the same district/faction. Not mixed reputation across different districts — genuine saturation in both directions with the *same* community at once.

**Disqualifier (from the other categories):** Wild Child status in a district removes that district from both the Pariah tally (it's not purely negative) and the Near-Pariah "remaining relationship" pool (it's not a normal positive relationship either — it's its own unresolvable thing).

**Design intent:** per `Reputation-System.md`, this is "a real, distinct, permanent state a player can actually hold, not a contradiction the system resolves" — a strong candidate for dedicated late-game content specifically because the city genuinely cannot categorize the player, and that strain is itself the dramatic material. Tiering by *how many* districts/factions the player holds Wild Child with simultaneously (Inner Tepenia tiered 3–4 / 5–7 / 8–12 / all) is a reusable structural idea, though the actual tier bands depend on how many districts/factions Toronto Fell Out ends up with.

### 4. District-Idolized

**Condition:** Idolized reputation with a single district/location, full completion of that location's major and minor quest content, maximum standing with its signature companion NPC (if any), and a high threshold in that location's associated skill.

**Design intent:** the mirror image of Pariah — instead of universal hatred producing an escape route, total devotion to one place produces a path built entirely around that place's own flavor of "everything outside this doesn't matter to me anymore." **TBD — fully blocked on Toronto Fell Out's own districts being designed** (see the ground rule against inventing them). One ending per eventual district/location is the template shape to replicate.

### 5. Faction-Devotion

**Condition:** Maximum standing with one of Toronto Fell Out's eventual cross-cutting factions (organizations that span multiple districts/locations rather than being contained within one), plus full completion of that faction's internal questline and any faction-specific contribution threshold.

**Design intent:** distinct from District-Idolized in the same way a faction is distinct from a place — this is about total commitment to an idea, network, or cause that cuts across the map, not to a single community. **TBD — fully blocked on Toronto Fell Out's own factions being designed.**

### 6. Minmax (Stat-Combination)

**Condition:** An extreme, specialized stat build from character creation — historically three stats pushed to a high floor simultaneously, though the exact eligible stat pool for Toronto Fell Out's MAPLE-BUD system is itself an open question. See `Storyline/Minmax-Builds/README.md` for the full combinatorial discussion (the Luck/Utility inclusion question) — **not resolved here, and not resolved there either; flagged for the user.**

**Design intent:** rewards extreme specialization at character creation with paths that let that specialization bypass, escape, undermine, or transcend the main story's central conflicts. Every trigger still obeys the World Trigger law above — knowing the stat prerequisite should be enough to know where to look.

---

## Explicitly Not Carried Forward

- **Identity Fragmentation / Fragmentation Matrix-based endings.** Inner Tepenia's re-speccing mechanic (Bond/Grief tracking tied to a Fragmentation Matrix) has already been confirmed not to exist in Toronto Fell Out — see `Game-Mechanics/Core-Mechanics/Companion-System.md`. There is no re-speccing in Toronto Fell Out, so there is no category of ending built around it. Nothing here should be read as an oversight; it's a confirmed exclusion.
- **Any category built around a specific companion, robot, or faction.** Inner Tepenia's own "Calethina Devotion," "Robot-Aligned," and "Long Vigil" ending categories are tied to that game's specific always-present companion and its sentient-robot premise — neither exists in Toronto Fell Out (no sentient robots/androids anywhere in the setting; no companions designed yet). Not adapted, not renamed, not replaced with a placeholder — simply not applicable.
- **A dedicated "creative mechanical combos" showcase file.** Reusable in spirit (build-specific combos of stats/skills/perks solving a problem in an unusual way are good design texture generally), but not part of the six-category taxonomy above, and not something to invent examples for without Toronto Fell Out's own systems/locations to hang them on. Revisit if useful once real content exists.
- **A dedicated "Hidden Paths" bypass-the-main-crisis category.** Inner Tepenia's Hidden Paths content (decentralized-power / crisis-acceleration / self-sufficiency / narrative-management routes around its central energy crisis) is tightly bound to that game's specific crisis and districts. Toronto Fell Out's own "ignore the main story" agency is already a general design stance rather than a dedicated ending category — revisit only if the eventual buried-asset endgame (see below) calls for a dedicated bypass path of its own.

---

## Tie to Toronto Fell Out's Own Story

Toronto Fell Out doesn't have districts or factions yet, but it does have the closest thing to endgame-consequence material currently on the books: the combined structure in `Reference/Main-Storyline-Candidates.md`, where all four candidate real-objective directions converge on a buried asset under the city, with the quarantine authority, the awakened automated defense network, and the frequency-squatting faction all holding a stake in the outcome. Once any of District-Idolized, Faction-Devotion, Pariah, or Wild Child endings get real content, they should be checked against that combined structure for consistency — a District-Idolized ending, for instance, would need to account for whether that district also had a stake in the buried asset, the same way Inner Tepenia's own District Idolized endings each accounted for that district's relationship to its central energy-grid climax.

---

## What's Still Fully Open

- Toronto Fell Out's own districts, factions, and companions (blocks District-Idolized and Faction-Devotion entirely).
- The Luck/Utility Minmax combinatorial question (see `Storyline/Minmax-Builds/README.md`).
- Exact Pariah/Near-Pariah ending counts and names (driven by however many districts/factions eventually exist).
- Wild Child tier bands (3-4/5-7/8-12/all-of-them was Inner Tepenia's split across 13 districts; Toronto Fell Out's own bands depend on its own eventual district/faction count).
- Whether Toronto Fell Out wants a dedicated bypass-the-main-crisis category analogous to Inner Tepenia's Hidden Paths, once the buried-asset endgame has more shape.
