# Glossary: D

### Damage Resistance
- **See:** [Damage Threshold and Damage Resistance](D.md#damage-threshold-and-damage-resistance)

### Damage Threshold
- **See:** [Damage Threshold and Damage Resistance](D.md#damage-threshold-and-damage-resistance)

### Damage Threshold and Damage Resistance
- **Category:** game term
- **Also called:** Damage Threshold; Damage Resistance; DT (abbreviation); DR (abbreviation)
- **Definition:** Inner Tepenia: Fallout: New Vegas-style layered protection. Damage Resistance removes a percentage of each hit first, capped at 85% (base DR = floor(Calculation × 2)%); Damage Threshold then subtracts a flat amount (base DT = floor(Engine × 2.5 + Might × 1.5)), and a hit always deals at least 15% of its base damage. Armor-piercing ammunition lowers effective DT.
- **Status:** working (no explicit ruling; later combat files treat it as settled). Copied, not yet adapted, in Outer Tepenia 1.
- **Used in:** InnerTepeniaGDD; Outer Tepenia 1 (fork); TorontoFellOutGDD
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Combat/Damage_Threshold_and_Damage_Resistance.md`; Outer Tepenia 1, same path.
- **Open:** The file's six damage categories (Ballistic, Energy, Explosive, Melee, Disrupt/EMP, Radiation) conflict with `Damage_Types.md`. "DR" also abbreviates a developer ruling (see Developer Rulings Log).

### Damage Types
- **Category:** game term
- **Definition:** Inner Tepenia: a grounded sci-fi set of damage types adapted from Baldur's Gate 3's thirteen (Necrotic becomes molecular breakdown, Radiant becomes laser light, and so on), plus Radiation, EMP/Disrupt, Plasma, Nanotech, Gravitic/Inertial and Neural/Interface. They are sorted into anti-robot, anti-human and shared groups by district.
- **Status:** working
- **Used in:** InnerTepeniaGDD; Outer Tepenia 1 (fork)
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Combat/Damage_Types.md`
- **Open:** Gravitic is "possible," not confirmed. Siphon is a resource drain, not a damage type. The list conflicts with the six categories in `Damage_Threshold_and_Damage_Resistance.md`.

### Data Archaeologist
- **Category:** game term
- **Also called:** Data Archaeology (former skill name; still a skill in Outer Tepenia 1); Deep Archive (former perk name, renamed 2026-07-26)
- **Definition:** Inner Tepenia: a two-rank level-up perk (Calculation 7, Cryptography 80) for recovering data from badly corrupted sources; rank 2 recovers data otherwise considered lost, such as pre-war records and scrubbed histories. Outer Tepenia 1 keeps it as a skill (Calculation plus Investigation), matching the in-world recovery work around the Great Corruption.
- **Status:** working
- **Used in:** InnerTepeniaGDD; Outer Tepenia 1 (fork, as a skill); TorontoFellOutGDD (copy); CurrentNovelDocs (reference copy); TheCryptographHelixDD (in-world "data archaeology" at Concordia)
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Perks/Regular_Perks_-_Level-Up.md`; Outer Tepenia 1 `Game-Mechanics/Character-Creation/Skills.md`; TheCryptographHelixDD `world/orbital-origins.md`
- **Open:** The audit's decision note gives Calculation 8 / Cryptography 75 instead. `Challenge_Perks` has a different, three-rank Data Archaeologist.

### Data Archaeology
- **See:** [Data Archaeologist](D.md#data-archaeologist)

### data archive library
- **See:** [Hall of Archives](H.md#hall-of-archives)

### Data Ghost
- **Category:** game term
- **Definition:** Inner Tepenia: a hacking perk (Calculation 7, Hacking 55) that greatly reduces the trace hacks leave on low-level systems. Active hacks still leave a signature.
- **Status:** working
- **Used in:** InnerTepeniaGDD; Outer Tepenia 1 (copied)
- **Sources:** Outer Tepenia 1 `Game-Mechanics/Core-Mechanics/Hacking_and_Traceability_System.md`

### Data Leak
- **Category:** game term
- **Definition:** Toronto Fell Out: an action unlocked by the Information Warfare trait. It is a debuff that exposes a target's weakness (a temporary defense loss or a disabled tactical option) instead of dealing damage, at a cost in standing with whoever is exposed.
- **Status:** working: its exact effect is unresolved upstream.
- **Used in:** TorontoFellOutGDD; InnerTepeniaGDD; Outer Tepenia series
- **Sources:** TorontoFellOutGDD `Game-Mechanics/Character-Creation/Traits.md`

### data shard
- **See:** [Datashard](D.md#datashard)

### Datashard
- **Category:** technology
- **Also called:** data shard (spelling in some GDD files)
- **Definition:** A portable carrier of data recovered from the old pre-war internet. Couriers such as Salagéa Aparast collect datashards and carry them across Tepenia so the material can be logged and archived through the Arcanet; the GDD's overview notes list them among the pre-war records the International Data Syndicate recovers.
- **Status:** Timeline canon (used in a Timeline character file); used, never formally defined.
- **Used in:** TepenianUniverseTimeline; InnerTepeniaGDD (character files; Belgrano; Halley); CurrentNovelDocs (doll-music extraction); SouthernLights; DerivationMechanisms
- **Sources:** TepenianUniverseTimeline `Worldspace/Characters/Dolls/Salagéa Aparast/README.md`; InnerTepeniaGDD `General-Overview-Notes/aspects_of_consideration.md`; `Cities/Local_Cultures/Halley_Subnet/Belgrano.md` (Notable figures)
- **Open:** Villena's song-01 prompt carries a stray datashard sentence copied from the courier template.

### Datasheet
- **Category:** method term
- **Also called:** Datasheets
- **Definition:** Out of fiction: a ULM quick-reference input file (Tier C) that records only what a source states outright (numbers, names, status tokens, dates, law text), with citations and no interpretation, so later steps need not re-extract the same fact. Each city has 19, one per step or phase, and they may not contain any Long Night War or post-war content.
- **Status:** project canon (added 2026-09-15 at the developer's direction); 24 of the 33 full city sets are drafts generated 2026-10-21.
- **Used in:** InnerTepeniaGDD (ULM; city pass folders); DerivationMechanisms; CurrentNovelDocs
- **Sources:** InnerTepeniaGDD `ULM/Mechanical_Extraction_Field_Guide.md`; `ULM/Datasheet_and_PreTrip_Tracker.md` (The three artifacts); `ULM/Tools/build_datasheets.py`
- **Open:** The word has three senses in the GDD: this one, `DOCKET.md`'s "developer datasheet" for a Specs file, and the megasheets' description of themselves as "mega-datasheets."

### Datasheets
- **See:** [Datasheet](D.md#datasheet)

### Davis
- **Category:** place
- **Also called:** the Hills (colloquial name)
- **Definition:** A Mirny-subnet city on the Davis Station site in the Vestfold Hills, the largest ice-free coastal oasis in Antarctica (about 400 km², forming its downtown core, with lakes and fjord inlets), founded by Australia and named for John King Davis. Ruled "the Breadbasket of Tepenia," it is the nation's agricultural and lake-research city, with a norm of collective research credit. The GDD makes it the principal Indian Ocean import port, and the Timeline has Sinheung's raw materials trucked from it.
- **Status:** Timeline canon (name, subnet); project canon for its founders (DR-19) and role.
- **Used in:** InnerTepeniaGDD (DLC 7); TepenianUniverseTimeline; SouthernLights; CurrentNovelDocs (reference copy); TorontoFellOutGDD (basis copy); DerivationMechanisms (method copies)
- **Sources:** InnerTepeniaGDD `Cities/Specs/Mirny subnet/Davis.md`; `Cities/Founding_Register.md`; `Cities/City_Master_Reference/Mirny_Subnet_Reference.md`; `Cities/Overview.md` (core/outer model); `Cities/Local_Cultures/Mirny_Subnet/Davis.md` §5 (the colloquial name, an identity label with no explicit author ruling); TepenianUniverseTimeline `Worldspace/Locations/README.md`; `Reference/Amundsen_Station_Archive_and_Trucking_Network.md`; SouthernLights `Worldspace/Environments-Federation-Cities.md` (Davis)
- **Open:**
  - War outcome: the GDD spec has it damaged but partially operational; SouthernLights calls it undamaged in 2812.
  - Its vision notes first framed it as mining-dominant; the mining role moved to Mirny (2026-07-16).
  - SouthernLights notes that an earlier brief wrongly put Davis in the Mawson subnet.
  - Demonym: see Davisite.

### Davisite
- **Category:** group or people
- **Definition:** The working demonym for a person from Davis.
- **Status:** working: placeholder
- **Used in:** InnerTepeniaGDD (Davis megasheet and Neo-Races catalog; Mawson files); CurrentNovelDocs (reference copy)
- **Sources:** InnerTepeniaGDD `Neo-Races-and-Cultures/Mirny_Subnet/Davis/Davis_Catalog.md`; `Cities/City_Megasheets/Mirny_Subnet/Davis/README.md` §V
- **Open:** `Cities/Specs/Mawson subnet/Mawson.md` cites Davisite as an established pattern, but Davis's own spec still says TBD ("Davisians?").

### The Day We Didn't Wait
- **Category:** culture and society
- **Definition:** The proposed name for Palmer City's Founding Day, June 21, commemorating that in 2564 the exiles arrived the same day the treaty was signed, without hesitation.
- **Status:** working: megasheet proposal
- **Used in:** InnerTepeniaGDD (Palmer megasheets); SouthernLights; CurrentNovelDocs (reference copy)
- **Sources:** InnerTepeniaGDD `Cities/City_Megasheets/Palmer_Subnet/Palmer_City/Palmer_City_Full_Extrapolation.md`; `Palmer_City_Community_Infrastructure.md` (same folder); SouthernLights `Worldspace/Environments-Federation-Cities.md` (Palmer City)
- **Open:** It falls on the same day as Tepenian Independence Day. One source is a Course of Events file (`BL/Palmer_Subnet/Palmer_City/Palmer_City_Course_of_Events_Suggestions.md`, #1), which is not canon.

### DCH
- **See:** [Hwy 2 (Dumont Coast Highway)](H.md#hwy-2-dumont-coast-highway)

### Dead space
- **Category:** place
- **Definition:** Unregulated space beyond the navigation grid that TANA maintains. Mentioned, not defined: it appears only as the place where the ship in *The Not-Departure* series is destroyed.
- **Status:** working (mentioned, not defined)
- **Used in:** TheCryptographHelixDD
- **Sources:** TheCryptographHelixDD `characters/tana_controller.md`

### Death as a change of vantage
- **Category:** culture and society
- **Definition:** The central pastoral doctrine of Polydimensional Animism: death is a shift in vantage point, not an ending. It applies to robot deactivation as directly as to organic death.
- **Status:** working (part of a working-copy religion design)
- **Used in:** InnerTepeniaGDD; DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Worldspace/Factions/Robot_Religions/Polydimensional_Animism/README.md` (Part 4 §1); `Beliefs.md` (same folder)
- **Open:** The robot physiology file refers to a "Robot Death Doctrine" in the same religion; whether that is this doctrine is not stated.

### Death (robot)
- **Category:** robot biology
- **Also called:** robot death
- **Definition:** For a robot, genuine death is irreversible damage to her cognitive architecture (the gel brain) or to her energy-source architecture (the battery, her equivalent of a heart), with no way to bring her back online; anything short of that is ordinary, survivable damage. Robots do not age, so they die in incidents such as breaches, collapses and wars, many at once or none for a long while.
- **Status:** Timeline canon (Robot Universals, "Mortality & Integrity," moved to DerivationMechanisms on 2026-10-30); project canon in the GDD's physiology file.
- **Used in:** TepenianUniverseTimeline (summary); InnerTepeniaGDD; DerivationMechanisms (Robot Universals)
- **Sources:** DerivationMechanisms `Characters/Robot-specific/Robot_Universals/1_-_Part_I_Ground-Level_Fundamentals/04_Mortality_and_Integrity/README.md`; InnerTepeniaGDD `Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` ("What Counts as Death"; "What Happens After — Ossuaries")
- **Open:**
  - Whether sustained overwork can corrupt a gel brain is flagged, not ruled.
  - GDD `Worldspace/Characters/Dolls/Doll_Visual_Design_Canon.md` says corruption of the central personality module past a threshold is effectively death of the self even if the body works; the physiology file says a substantial change in who a robot is is not death-adjacent.
  - The physiology file says robots do not age; the media-root `Tepenian_Universe_Overview.md` says Dolls age and die, only much more slowly than humans.

### Death spiral (cold)
- **Category:** robot biology
- **Definition:** The cold-weather trap in which a robot's charge falls so low that she can no longer spend energy warming her cells enough to charge safely, so she cannot recover on her own. It explains warmed charging shelters, rescue work and what "properly equipped" means in the Frostlands; the same file notes that in deep cold a robot is safer moving than resting, the reverse of human cold survival.
- **Status:** working (research file written at the developer's direction, 2026-09-04; numbers not set for the game)
- **Used in:** InnerTepeniaGDD; DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md` §1

### Decentralized Systems
- **Category:** game term
- **Definition:** Inner Tepenia: a level-up perk (Calculation 7, Hacking 75) giving +30% when designing or linking decentralized power nodes. It is the core perk for the Independent Lattice.
- **Status:** working (flagged for review)
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Perks/Regular_Perks_-_Level-Up.md`
- **Open:** It comes from the cut skill "Decentralized Systems Design," which `Character_Creation_Overview` still tags in sample builds.

### Deception
- **Category:** game term
- **Definition:** Inner Tepenia: a skill governed by Nerve. The skill list gives no further description.
- **Status:** project canon
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Character-Creation/Skills.md`
- **Open:** It was split from the former combined skill "Deception & Narrative Crafting."

### Deep Archive
- **See:** [Data Archaeologist](D.md#data-archaeologist)

### Deep Culture
- **Category:** method term
- **Definition:** Out of fiction: in the Cultural Iceberg Method, the invisible layer (about 90%) that actually makes a distinct people. It has 17 sub-items under five headers: communication styles and rules, notions of, concepts of, attitudes toward, and approaches to.
- **Status:** project canon
- **Used in:** InnerTepeniaGDD; TheCryptographHelixDD; DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Neo-Races-and-Cultures/_Method/Cultural_Iceberg_Method.md`; `Neo-Races-and-Cultures/_Method/City_Catalog_Template.md`

### Deep Dives (district)
- **Category:** method term
- **Definition:** Out of fiction: per-district analyses that read each Concordia district's history through the Two-Stage Methodology and settle open mechanisms, for example the Flood, the black-market origin and the Tolerance Pact.
- **Status:** project canon (method)
- **Used in:** InnerTepeniaGDD; DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Districts/Deep_Dives/`

### Deep Frostlands
- **See:** [The Frostlands](F.md#the-frostlands)

### Deep Level
- **Category:** place
- **Definition:** Unmapped chambers and passages below Concordia's Undergrid (Virgo, District 12), beneath its utility tunnels, waste systems and backup Arcanet nodes, that predate the city. No central record holds them; only Virgo crews know them and pass the knowledge on in person.
- **Status:** project canon (existence); its nature is deliberately open (pre-Falkland war infrastructure, something older, or navigable geology).
- **Used in:** InnerTepeniaGDD; SouthernLights; CurrentNovelDocs; TorontoFellOutGDD; DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Districts/District_Canon_Reference.md` (District 12, "The Deep Level"); `Worldspace/Characters/Character_Concept_Bank.md`; SouthernLights `Worldspace/Locations.md` (Virgo); `Worldspace/Environments-Concordia-Districts.md`
- **Open:** SouthernLights has it guarded by a single Virgo "Deep Level Keeper," possibly the oldest active Doll. See also Deep Level Keepers and Deep Level Custodians.

### Deep Level Custodians
- **Category:** group or people
- **Definition:** A proposed small group entrusted with what is known about the Deep Level, small only because few need to know. It serves as a non-stat route in Favi della Torre's questline.
- **Status:** working: listed as a lore prospect.
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `Districts/Cross_District_Additive_Lore_Prospects.md`; `Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Favi della Torre/Questlines/README.md`
- **Open:** It overlaps the Character Concept Bank's "The Oldest Maps" and the district faction Deep Level Keepers; neither overlap has been reconciled.

### Deep Level Keepers
- **Category:** group or people
- **Definition:** The Undergrid (Virgo) faction whose members know the Deep Level and pass that knowledge on only within the district, as its ultimate reserve.
- **Status:** project canon
- **Used in:** InnerTepeniaGDD; SouthernLights; copies
- **Sources:** InnerTepeniaGDD `Districts/District_Unity_of_Opposites.md` (District 12)
- **Open:** How it relates to the proposed Deep Level Custodians is not stated.

### Deep System Purge
- **Category:** game term
- **Definition:** Inner Tepenia: the Undergrid's (Virgo's) district re-spec method, with its own heavy trade-off costs. See District re-spec methods.
- **Status:** working
- **Used in:** InnerTepeniaGDD; Outer Tepenia 1 (copied)
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Core-Mechanics/Player_Re-Spec_-_Complete_Design.md`; Outer Tepenia 1 `Game-Mechanics/Core-Mechanics/Player_Re-Spec_-_Costs_and_Trade-Offs.md`

### Deepest Cold
- **Category:** culture and society
- **Definition:** The chief communal observance of Ice-Cold Buddhism, held at Dome Fuji at or near the coldest point of polar night (June or July), the closest approach to the conditions the faith venerates. Kunlun keeps it too, possibly with more weight.
- **Status:** project canon that the observance exists (Dome Fuji's culture files); working: the name is a placeholder and the timing is unsettled.
- **Used in:** InnerTepeniaGDD (Dome Fuji; Kunlun; National_Holidays; TODO; Neo-Races); CurrentNovelDocs (reference copy); SouthernLights; TorontoFellOutGDD (basis copy)
- **Sources:** InnerTepeniaGDD `Cities/Local_Cultures/Mawson_Subnet/Dome_Fuji.md` §26; `Cities/Local_Cultures/Mirny_Subnet/Kunlun.md` §26; `Worldspace/National_Holidays.md` (Category 4); `TODO.md` (National Holidays); SouthernLights `Worldspace/Environments-Federation-Cities.md` (Dome Fuji)
- **Open:**
  - **Timing.** `Local_Cultures` gives only "June/July." `National_Holidays.md` fixes it as the first calm, clear night after the winter solstice, calls it mandatory, and makes its unpredictable date a doctrinal dispute; that version comes from `BL/Mawson_Subnet/Dome_Fuji/Course_of_Events/Dome_Fuji_06_Deepest_Cold.md`, a non-canon vignette (GDD TODO ruling 2026-09-30/10-01). SouthernLights has it tracked meteorologically, shifting by days each year.
  - The Dome Fuji catalog's preamble still calls it "speculated."
  - "Ice Cold Buddhism" is itself a placeholder name.

### deep-synthesis hours law
- **See:** [Operating-hours law](O.md#operating-hours-law)

### De-Escalator
- **See:** [Empathic Bridge](E.md#empathic-bridge)

### Default frame (Second Interwar)
- **Category:** method term
- **Definition:** Out of fiction: the ULM rule that a location pass defaults to the setting's last fully functioning era, written neutrally rather than in its damaged present; for Tepenia that is the Second Interwar Period (2564 to 2812), with the Tepenian Federation a working country. Post-war spec fields (Status, Current Status, Legacy, Connection to Concordia) are never inputs, and datasheets may not mention the Long Night War at all. Standing exception: Concordia's thirteen districts are written post-war, since their civic identity is a post-war formation.
- **Status:** project canon (developer instructions, 2026-08-31 and 2026-09-15)
- **Used in:** InnerTepeniaGDD; DerivationMechanisms
- **Sources:** InnerTepeniaGDD `ULM/01_Frame_Typology_and_Inheritance.md` §4.1; `ULM/00_RUNBOOK.md` §C.8a; `ULM/Mechanical_Extraction_Field_Guide.md`

### deficit address
- **See:** [Address axis](A.md#address-axis)

### Delivery Resolution
- **Category:** game term
- **Definition:** Plot Hole (no stated universe): on every delivery, right or wrong, a flat chance of about 5 percent flips the result, so a perfect delivery can read as a failure and a wrong one as a success.
- **Status:** working (pre-production concept)
- **Used in:** PlotHoleGDD
- **Sources:** PlotHoleGDD `quick-rundown.md` (Delivery Resolution)

### Demagogue
- **Category:** game term
- **Also called:** Crowd Pleaser (former name)
- **Definition:** Inner Tepenia and Toronto Fell Out: a trait giving +20% Speech (and, in Inner Tepenia, Narrative) when addressing groups, at the cost that every NPC's first impression starts out skeptical.
- **Status:** working (depends on there being enough crowd-address content); the Toronto Fell Out name is tentative.
- **Used in:** InnerTepeniaGDD; TorontoFellOutGDD
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Character-Creation/Traits.md`; TorontoFellOutGDD `Game-Mechanics/Character-Creation/Traits.md`
- **Open:** Toronto Fell Out lists alternate names Soapbox, Rabble-Rouser and Loudmouth. In the GDD it is forbidden for Trisha Miller, Majyao Bisyugota and Flora.

### Denison
- **Category:** place
- **Also called:** Windbreak City (nickname)
- **Definition:** A Janbogo-subnet city at Cape Denison on Commonwealth Bay, on the site of Mawson's expedition base ("Home of the Blizzard"), the windiest sea-level habitation on Earth; founded by Australia. It was built as one continuous, interlinked, load-sharing structure, its civic identity was open pride in extreme wind (the one city that broke the national habit of not talking about its own toughness), and it was a historical fabrication-chamber manufacturer. It was destroyed outright in the Long Night War.
- **Status:** Timeline canon (name, subnet, chamber manufacturing, destruction); project canon for its founders (DR-44).
- **Used in:** InnerTepeniaGDD (DLC 6); TepenianUniverseTimeline; SouthernLights; CurrentNovelDocs (reference copy); TorontoFellOutGDD (basis copy); DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Cities/Specs/Janbogo subnet/Denison.md`; `Cities/Founding_Register.md`; `Cities/Local_Cultures/Janbogo_Subnet/Denison.md` §5; TepenianUniverseTimeline `Timeline Eras/2 The Second Interwar Period/Timeline.md` (END); `Reference/Amundsen_Station_Archive_and_Trucking_Network.md`; SouthernLights `Worldspace/Locations.md`; `Worldspace/Environments-Federation-Cities.md`
- **Open:** The developer has floated re-founding one Australian-founded city to ease Australia's share (FQ-20); not ruled. Demonym open (see Denisonian).

### Denisonian
- **Category:** group or people
- **Definition:** The Neo-Races working name for the people of Denison.
- **Status:** working: placeholder
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `Neo-Races-and-Cultures/Janbogo_Subnet/Denison/Denison_Catalog.md`
- **Open:** The city spec and the megasheet both say TBD.

### Deposit discipline (CGRM)
- **Category:** method term
- **Definition:** Out of fiction: the Canon Gap Resolution Method's rule that every acquired fact is classified before it is written into canon, as an attribute (a property anyone could accept), a conclusion (an interpretation of what the subject is like) or a decision (an authored choice such as a name or date), because each kind belongs in a different tier. Its founding failure case is the "Cape Adare deposit chain" (2026-07-05).
- **Status:** project canon (2026-08-31)
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `Worldspace/Canon_Gap_Resolution_Method/03_Deposit_Discipline.md`

### depth over speed
- **See:** [LAW 0](L.md#law-0)

### Depth standard (12+17 items)
- **Category:** method term
- **Definition:** Out of fiction: the rule, finalized 2026-07-16 on the developer's instruction, that every nation entry in a Neo-Races city catalog addresses all 12 Surface Culture items and all 17 Deep Culture sub-items individually, with an honest null line where nothing distinct surfaced. Davis is the reference example.
- **Status:** project canon; it supersedes the earlier "Deep Culture quality bar."
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `Neo-Races-and-Cultures/_Method/City_Catalog_Template.md` (DEPTH REQUIREMENT); `Neo-Races-and-Cultures/_Method/Progress_Tracker.md`

### The Depths
- **See:** [The Undergrid](U.md#the-undergrid)

### Derelict's Eye
- **Category:** game term
- **Definition:** Inner Tepenia and Toronto Fell Out: a discovery perk earned by restoring a truly derelict pre-war structure that no quest marker points to. Afterward the player can tell at a glance what any such ruin was and what restoring it would take; in the GDD it means a pre-exile (Upper Earth era) structure, and it pairs with Reclaimer's Hands.
- **Status:** project canon in Toronto Fell Out's perk list (numbers are placeholders); working in the GDD (decorative until a present-day derelict site exists in quests).
- **Used in:** InnerTepeniaGDD; TorontoFellOutGDD
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Perks/World_and_Discovery_Perks.md`; TorontoFellOutGDD `Game-Mechanics/Perks/Perks.md` (Discovery)

### Derivation Mechanisms
- **Category:** method term
- **Definition:** Out of fiction: the author's universe-wide repo of mechanisms for deriving in-universe details (characters, locations, symbols, stories). It was created 2026-10-29 by copying, not moving, methods from InnerTepeniaGDD, TepenianUniverseTimeline and CurrentNovelDocs (later also TorontoFellOutGDD and TheCryptographHelixDD). On 2026-10-30 each mechanism was combined into one version written to apply everywhere, with no folder named for a source repo; where everything came from is kept in the root sync record. The same day, the Timeline moved its generic methodology (Robot Universals, Doll Height Transposition, the character creation methodology) into it.
- **Status:** project canon (author, 2026-10-29)
- **Used in:** DerivationMechanisms; InnerTepeniaGDD and CurrentNovelDocs (pointer lines); TepenianUniverseTimeline (moved material)
- **Sources:** DerivationMechanisms `README.md`; `SYNC_RECORD.md`
- **Open:** Per the sync record, still open: separating method from project run data, deliberate duplicates (RWBEM, CST and the zodiac sheet inside the ULM folder), a setting-agnostic pass on the character methodology, and the pointers in the GDD and the Timeline marked for review.

### Derivation pass
- **Category:** method term
- **Definition:** Out of fiction: the later session that turns extracted facts into new character or world details, held only in the 05:00 to 14:59 window and only on the author's decisions. Extraction files end each section with questions held for it.
- **Status:** project canon (convention)
- **Used in:** CurrentNovelDocs (doll-music extraction); InnerTepeniaGDD (religion derivation; symbolic substrate; canon-gap method); DerivationMechanisms
- **Sources:** CurrentNovelDocs `worldbuilding/characters/doll-music extraction (2026-10-23)/00 - Index.md`

### Derivation Protocol
- **Category:** method term
- **Definition:** Out of fiction: part of the character methodology's step 00a. It rebuilds all 25 Stage 1 categories from a small seed (name, robot or human, Personal Vision, Enneagram percentage and Undercurrent, origin, timeframe) plus folder materials, project canon and inference, deferring what isn't needed yet; with the Clarification Protocol (00b) it yields a Stage 1 Derived Input Sheet that tags each field SOURCED, ENNEAGRAM, PROPOSED or BLOCKED.
- **Status:** project canon (method) in CurrentNovelDocs' copy; the GDD's copy is marked working.
- **Used in:** CurrentNovelDocs (root seed file; Starlit Engines; Maggie Aarden notes); DerivationMechanisms; InnerTepeniaGDD; TepenianUniverseTimeline
- **Sources:** DerivationMechanisms `Characters/Character_Development_Methodology/Pipeline/00a_Initial_Input.md`; InnerTepeniaGDD `Worldspace/Characters/Dolls/Methodology/00a_Initial_Input.md`; CurrentNovelDocs `character_seed-input.txt`; `Starlit Engines (Alaska Rescue novel)/background notes/characters/Lucy Grayson - Stage 1 Derived Sheet.md`

### the desert collective
- **See:** [Arizona desert tribe](A.md#arizona-desert-tribe)

### de-stacked
- **See:** [De-stacking](D.md#de-stacking)

### De-stacking
- **Category:** method term
- **Also called:** de-stacked (form used in the tables)
- **Definition:** Out of fiction: a 2026-07-05 pass over every city spec's per-nation table that randomized shares within each population tier, so nations in the same tier no longer showed identical percentages. Each tier's total and order were kept.
- **Status:** project canon (DR-12)
- **Used in:** InnerTepeniaGDD (city specs; census; Full_City_Integrity_Check); CurrentNovelDocs (reference copy); DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Cities/Specs/Mirny subnet/Davis.md` (de-stacking note, repeated in every spec); `Official_Population_Census.md` (Section B, 2026-07-05 note); `ULM/DEVELOPER_RULINGS_LOG.md` (DR-12)
- **Open:** The specs say the full method is in `TODO.md` (not checked). Tier-order mismatches between the raw and de-stacked layers were flagged, not fixed (for example Davis).

### Detached Intellect
- **Category:** game term
- **Also called:** Cold Calculation (InnerTepeniaGDD name)
- **Definition:** Toronto Fell Out: a trait giving +2 Brains and -1 Determination, renamed from the GDD's Cold Calculation (+2 Calculation, -1 Humanity).
- **Status:** project canon in Toronto Fell Out; the GDD's Cold Calculation is working (a stat-gap trait that may be renamed).
- **Used in:** TorontoFellOutGDD; InnerTepeniaGDD (as Cold Calculation)
- **Sources:** TorontoFellOutGDD `Game-Mechanics/Character-Creation/Traits.md`; InnerTepeniaGDD `Game-Mechanics/Character-Creation/Traits.md`
- **Open:** Candidate perk names Cold Logic and Clinical Mind were split off from it.

### Determination
- **See:** [Humanity](H.md#humanity)

### developer ruling
- **See:** [Developer Rulings Log](D.md#developer-rulings-log)

### Developer Ruling Queue
- **Category:** method term
- **Also called:** DRQ (entry code; DRQ-01 onward)
- **Definition:** Out of fiction: the Canon Gap Resolution Method's live file of batched decisions that need the developer's authority. Each numbered entry arrives with the groundwork done (the question, why it is reserved, constraints, options, precedents, consequences and what is blocked) so a ruling is quick; the system prepares but never decides.
- **Status:** project canon (the queue); individual entries are working until ruled.
- **Used in:** InnerTepeniaGDD (CGRM; Division of Industry); DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md`; `Worldspace/Canon_Gap_Resolution_Method/02_Acquisition_Paths.md` (Path 6; §7)
- **Open:** It is a separate series from the Developer Rulings Log's DR numbers. Division of Industry cites DRQ-08 (answered by the caloric rebuild) and DRQ-09 (the baseline/distinctive convention), which its README still calls open.

### Developer Rulings Log
- **Category:** method term
- **Also called:** DR (ruling code; DR-1 onward); developer ruling; DRL; rulings log
- **Definition:** Out of fiction: the GDD's single log of the developer's binding rulings on location work, one numbered entry per ruling (DR-1, DR-2 and so on; follow-ons take a letter, as in DR-10a), written in the same turn the ruling is given. It opened 2026-09-13 and runs to DR-83 (2026-10-29). Its rulings, cited by number across the repos, cover method (for example DR-14: CST and RWBEM are not part of the ULM pass) and in-world facts such as founders (DR-19: founders stand on geography and access, never on the real station), renames, ports and census conventions.
- **Status:** project canon
- **Used in:** InnerTepeniaGDD (Cities; ULM; templates; CLAUDE.md); TepenianUniverseTimeline; CurrentNovelDocs; DerivationMechanisms (copied ULM files); Hybrid-Anthro_Culture (as a model)
- **Sources:** InnerTepeniaGDD `ULM/DEVELOPER_RULINGS_LOG.md` (cited from `Cities/Founding_Register.md`); TepenianUniverseTimeline `Reference/No_National_Stereotypes.md`
- **Open:**
  - Rulings from before 2026-09-13 are not back-filled. They remain in `ULM/00_RUNBOOK.md`, `CLAUDE.md` and `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`, so a missing ruling here does not mean there is no rule; some earlier rulings carry CGRM Path 6 tags instead.
  - Related codes: FQ-nn (open founder questions), R-nn (revisit items), DRQ-nn (see Developer Ruling Queue). "DR" also abbreviates Damage Resistance.

### Developer Vision Notes
- **See:** [City Vision Notes](C.md#city-vision-notes)

### Dev-Road-Map
- **Category:** method term
- **Definition:** Out of fiction: the planning-only roadmap each novel and film project uses, adapted from the GDD's: Blocking Decisions, then seven phases (Foundations, Characters, Supporting Cast, Story and Chapters, Theme, World Depth, Long-Term), plus a Craft Reference and a Completion Matrix. Its order rule is that character and setting create plot, and plot creates theme.
- **Status:** project canon (method)
- **Used in:** CurrentNovelDocs (every novel and film folder; y-template); InnerTepeniaGDD; TheCryptographHelixDD; SouthernLights; Outer Tepenia series; TorontoFellOutGDD; DerivationMechanisms; Hybrid-Anthro_Culture
- **Sources:** CurrentNovelDocs `Streetside Harmonies/structure/Dev-Road-Map/00-Overview.md`; `Gilgamesh Sci-Fi movie/structure/Dev-Road-Map/00-Overview.md`
- **Open:** It is still unfilled template text in the Gilgamesh, Maritza and Ricardo folders.

### Dhale (Disputed Territory)
- **Category:** place
- **Definition:** Yemen's Dhale governorate, stitched together from former North and South Yemen districts, which the post-war map officially records as Disputed Territory between North Yemen and South Yemen.
- **Status:** project canon (2026-09-28)
- **Used in:** CurrentNovelDocs (worldbuilding)
- **Sources:** CurrentNovelDocs `worldbuilding/STATUS - Cross-Session Progress Tracker.md` §4.8

### Diagnostic Tap
- **Category:** game term
- **Definition:** Inner Tepenia: a Drain Weapons item, field-medicine equipment for reading a human's body heat, hydration and stamina. It is the human-side counterpart of the coolant siphon and can be used offensively.
- **Status:** working: first-pass catalog item
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `Worldspace/Weapon_Item_Catalog.md`

### Differentiate locally, converge nationally
- **Category:** law or rule
- **Also called:** Pennsylvania/Virginia test (the check's name in No National Stereotypes and the ULM runbook)
- **Definition:** Out of fiction. The rule, part of No National Stereotypes, that Tepenian places may differ greatly in ethnic background and in local culture, conditions, struggles and habits while all being fundamentally Tepenian in national identity, as people from Pennsylvania and Virginia in the early 1800s had different backgrounds yet were all American. National identity is never a differentiator between cities, since every Tepenian city is Tepenian.
- **Status:** Timeline canon (No National Stereotypes, 2026-09-06; the Second Interwar Period README); project canon in the ULM (developer, 2026-09-06).
- **Used in:** TepenianUniverseTimeline; InnerTepeniaGDD; DerivationMechanisms (ULM); TepenianHawaiian (applied to dialects, Q-9); CurrentNovelDocs
- **Sources:** TepenianUniverseTimeline `Reference/No_National_Stereotypes.md`; `Timeline Eras/2 The Second Interwar Period/README.md`; InnerTepeniaGDD `CLAUDE.md`; `ULM/00_RUNBOOK.md` §C.9e (THE PENNSYLVANIA/VIRGINIA TEST); `Neo-Races-and-Cultures/_Method/Human_Universals_Culture_Framework.md` §6

### Differentiation Engine
- **Category:** method term
- **Definition:** Out of fiction: Robot Universals' method for deriving how a universal is expressed differently by different robot populations, by asking which concrete condition (a city, a locality, a class position, a specific history) shapes it. It includes the Universal Pool Mechanism (populations draw different selections from one shared pool, which can itself shift over time) and the Honesty Check (causes are always concrete conditions, never robot-ness, and a universal that shows no local variation is reported as such).
- **Status:** Timeline canon in origin (moved with Robot Universals to DerivationMechanisms, 2026-10-30)
- **Used in:** DerivationMechanisms; InnerTepeniaGDD (Local Robot Culture Methodology); TepenianUniverseTimeline; CurrentNovelDocs; Hybrid-Anthro_Culture
- **Sources:** DerivationMechanisms `Characters/Robot-specific/Robot_Universals/4_-_Part_IV_Applying_the_Universals/18_The_Differentiation_Engine/README.md`

### Differentiation table
- **Category:** method term
- **Also called:** Cross-City Culture Differentiation Table; sibling-differentiation instrument
- **Definition:** Out of fiction: the ULM's cross-city table to which each finished location pass adds its own entry at Step 6, write-only, without reading the other locations' entries. Comparison against siblings is deferred to a terminal check on the completed corpus.
- **Status:** project canon (write-only in-run since 2026-09-06; the table file was created empty 2026-09-04)
- **Used in:** InnerTepeniaGDD (Cities; ULM; passes); DerivationMechanisms
- **Sources:** InnerTepeniaGDD `ULM/04_QA_Gates_and_Differentiation.md` Part III; `Cities/Cross_City_Culture_Differentiation_Table.md`; `ULM/Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md`
- **Open:** Area M's harvest has each pass add a column, area G3b's a row. The Concordia districts have their own Cross-District Differentiation Table (Gate 6b), and Division of Industry has its own industry differentiation table (file 02), still empty.

### Difficulty (D)
- **Category:** method term
- **Definition:** Out of fiction: in the Division of Industry, a per-city multiplier on necessary industries for physical hardship (cold, wind, altitude, isolation, foundation), calibrated against published construction labor-productivity factors. Cities differ more by difficulty than by demand; examples are Concordia 1.67, Ariun Nuur 2.50 and Relung Panen 1.43 (by ruling, DR-72).
- **Status:** project canon
- **Used in:** InnerTepeniaGDD (Division of Industry; Relung Panen; ULM)
- **Sources:** InnerTepeniaGDD `Cities/Division_of_Industry/08_Volume_Based_Requirement_Reference.md` §6; `Cities/Division_of_Industry/09_Per_City_Baseline_Run.md` §2 (D column)

### Digital-Industrial
- **Category:** culture and society
- **Definition:** A music genre named, alongside Electronic and Metal, as Neumayer's dominant after-hours sound: machinery-adjacent and precision-coded. Mentioned, not otherwise defined.
- **Status:** project canon (resolved 2026-07-04)
- **Used in:** InnerTepeniaGDD; CurrentNovelDocs (reference copy); SouthernLights
- **Sources:** InnerTepeniaGDD `Cities/Local_Cultures/Halley_Subnet/Neumayer.md`; `Neo-Races-and-Cultures/Halley_Subnet/Neumayer/Neumayer_Catalog.md`
- **Open:** Whether it is an in-world genre or a real-world style is unclear.

### The Dimming
- **Category:** era or event
- **Definition:** Leo's most traumatic event: for six months in 2789 to 2790, during an energy crisis, Aries cut Leo's power, the lights and heat went down and hundreds of performers left, while those who stayed performed by candlelight. Leo remembers it as a sacred betrayal; it explains Leo's fierce fight for power priority and its reverence for small candlelit performances.
- **Status:** Timeline canon
- **Used in:** TepenianUniverseTimeline; InnerTepeniaGDD; SouthernLights; CurrentNovelDocs; TorontoFellOutGDD
- **Sources:** TepenianUniverseTimeline `Timeline Eras/2 The Second Interwar Period/Timeline.md`; InnerTepeniaGDD `Districts/District_Canon_Reference.md` (District 3, Leo)

### Diplomat
- **Category:** game term
- **Definition:** Toronto Fell Out: a perk under which, in formal negotiations (summits, treaty talks, faction leadership meetings), the player is treated as a legitimate party rather than a messenger.
- **Status:** project canon (perk list)
- **Used in:** TorontoFellOutGDD; InnerTepeniaGDD
- **Sources:** TorontoFellOutGDD `Game-Mechanics/Perks/Perks.md` (Social / Dialogue)

### Direct Transfer
- **Category:** method term
- **Also called:** Direct-Transfer (Timeline spelling)
- **Definition:** Out of fiction: an outcome of the human-versus-robot divergence step in the Human Universals Culture Framework. It is a universal of accident whose cause fully applies to robots, so it carries over unchanged (for example cooperation, reciprocity, governance).
- **Status:** Timeline canon
- **Used in:** InnerTepeniaGDD; TepenianUniverseTimeline; CurrentNovelDocs (worldbuilding OOLSD); DerivationMechanisms
- **Sources:** TepenianUniverseTimeline `Reference/Robot_Universals_Summary.md`; InnerTepeniaGDD `Neo-Races-and-Cultures/_Method/Human_Universals_Culture_Framework.md` (Part 2, step 4)

### Direct-Transfer
- **See:** [Direct Transfer](D.md#direct-transfer)

### Disputed Territory
- **Category:** polity
- **Definition:** A named status on the post-war world map for land that two states both claim and neither holds outright, drawn with a cross-hatch rather than given to either side. Settled cases include Dhale (between the two Yemens) and Diyala with Khanaqin in Iraq; Manipur's five Naga-core districts between two Madhyama zones are proposed. Its sister statuses are Unstable Territory (Khuzestan) and Uncertain Territory (the Fergana Valley).
- **Status:** project canon (each case ruled separately)
- **Used in:** CurrentNovelDocs (worldbuilding)
- **Sources:** CurrentNovelDocs `worldbuilding/STATUS - Cross-Session Progress Tracker.md` §4.8; `worldbuilding/nations/Madhyama and the Northeast - Decision Log and Open Items (working).md` §4

### District 1
- **See:** [The Sanctuary](S.md#the-sanctuary)

### District 11
- **See:** [The Frostlands](F.md#the-frostlands)

### District 13
- **See:** [Concordia Central Hub](C.md#concordia-central-hub)

### District 2
- **See:** [Taurus (Concordia district)](T.md#taurus-concordia-district)

### District 4
- **See:** [Scorpio (Concordia district)](S.md#scorpio-concordia-district)

### District 8
- **See:** [The Government District](G.md#the-government-district)

### District armor and augmentations
- **Category:** game term
- **Definition:** Inner Tepenia: protection comes mainly from the robot frame and installed augmentations, scaled by MACHINE stats. True wearable armor is rare, flavored by district, worn on top, and comes with trade-offs; post-Idolized capstone quests grant the top protective rewards.
- **Status:** working (draft with no recorded ruling)
- **Used in:** InnerTepeniaGDD; Outer Tepenia 1 (fork)
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Combat/District_Armor_Augmentations_and_Protection.md`
- **Open:** It uses the names "Official Clean Slate" and "Experimental Lattice Swap," which differ from the re-spec names Clean Slate and Lattice Swap.

### District Capstone Perks
- **Category:** game term
- **Also called:** post-Idolization questline perks
- **Definition:** Inner Tepenia: the strongest earned perks (Category D), awarded as mutually exclusive pairs at the end of each district's post-Idolized capstone questline. For example, Cancer gives No One Left Behind or Sanctuary Warden.
- **Status:** working (24 drafted; titles tentative)
- **Used in:** InnerTepeniaGDD; Outer Tepenia 1 (fork)
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Perks/post-Idolization_Questline_Perks.md`; `Game-Mechanics/Perks/Perk_Framework.md`
- **Open:** It covers 12 districts (no Hub), although Concordia has 13.

### District Culture Development Plan
- **See:** [District Synthesis Methodology](D.md#district-synthesis-methodology)

### District demonyms (Concordia)
- **Category:** group or people
- **Definition:** The words for a resident of each Concordia district. The district megasheets propose zodiac-based forms (Cancrian, Taurine, Leonian, Scorpian, Ariesian to avoid "Arian," Capricornian, Aquarian, Libran, Geminian, Piscean, Sagittarian, Virgoan) and, for the Hub, two terms: Hub-born and Hub-arrived.
- **Status:** working (proposed; a demonym field is a TODO before NPC dialogue)
- **Used in:** InnerTepeniaGDD; copies
- **Sources:** InnerTepeniaGDD `Districts/District_Megasheets/*/README.md` ("Demonym and Notable Figures"); `TODO.md` (district documentation template)
- **Open:** The TODO's own example is Sagittarius → "Frostlander," and later culture files use "Frostlanders," not "Sagittarian." Zodiac-based demonyms sit awkwardly with the ruling that the zodiac is not in-fiction. Alternates noted: Cancerian, Taurusian.

### District History Enhancement Opportunities
- **Category:** method term
- **Definition:** Out of fiction: a flag-only pass, run per Concordia district with a five-lens template, that looks for ways to enrich a district's pre-war history once its Deep Dive and pre-war megasheet exist.
- **Status:** project canon (official template, 2026-07-17)
- **Used in:** InnerTepeniaGDD; DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Districts/District_History_Enhancement_Opportunities_Template.md`; `Districts/District_History_Enhancement_Opportunities/`

### District Idolized Endings
- **Category:** game term
- **Also called:** District-Idolized ending (Toronto Fell Out category name)
- **Definition:** Inner Tepenia: thirteen secret endings, one per Concordia district including the Hub, unlocked by Idolized standing with the district, every district quest done, maximum standing with its signature companion and 80 or more in its key skill; each is built on total devotion to that place. Toronto Fell Out keeps the category (secret-ending category 4) as a framework only.
- **Status:** project canon in the GDD; working in Toronto Fell Out (framework only, blocked on districts).
- **Used in:** InnerTepeniaGDD; TorontoFellOutGDD; CurrentNovelDocs (`reference/` copy)
- **Sources:** InnerTepeniaGDD `Storyline/Endings/Secret-Endings/District_Idolized_Endings.md`; TorontoFellOutGDD `Storyline/Endings/Secret-Endings/Secret_Endings_Design_Framework.md` (category 4)

### District Internal Conflict Quests
- **See:** [District Main Questlines](D.md#district-main-questlines)

### District Main Questlines
- **Category:** game term
- **Also called:** District Internal Conflict Quests
- **Definition:** Inner Tepenia: one capstone quest per Concordia district, built from the internal conflict parties in `District_Unity_of_Opposites.md` and rewarding a district perk and possibly a district player home. Examples: Cancer's "The Night of Locked Doors," Aries' "Thirty-Seven Minutes."
- **Status:** project canon
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `Storyline/Side-Content/District_Main_Questlines.md`

### District Megasheet
- **See:** [Megasheet](M.md#megasheet)

### district methodology
- **See:** [District Synthesis Methodology](D.md#district-synthesis-methodology)

### District Quest Consequence Web
- **Category:** game term
- **Definition:** Inner Tepenia: the map of how each district main questline's resolution unlocks, blocks or alters quests in other districts and the Act 3 state. It is organized into major chains: the Libra, Truth, Transformation, Information Underground, Resource, Care and Recognition chains.
- **Status:** project canon (design reference)
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `Storyline/Side-Content/District_Quest_Consequence_Web.md`

### District re-spec methods
- **Category:** game term
- **Definition:** Inner Tepenia: besides Calethina's Lab, each of the 13 districts offers its own re-spec (14 options in all), each granting a unique district-flavored ability along with costs and district reactions. The methods are Sanctuary Rebinding (Cancer), Homebound Recalibration (Taurus), Spotlight Overhaul (Leo), Rebirth Ritual (Scorpio), Forge Rebuild (Aries), Production Overhaul (Capricorn), Lattice Swap (Aquarius), Oathbinding Pact (Libra), Subnet Integration (Gemini), Market Rebuild (Pisces), Frost-Forged (Sagittarius), Deep System Purge (Virgo) and Axis Recalibration (Hub).
- **Status:** project canon (structure, 2026-07-23); working (numbers deferred)
- **Used in:** InnerTepeniaGDD; Outer Tepenia 1 (fork)
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Core-Mechanics/Player_Re-Spec_-_Complete_Design.md`

### district runbook
- **See:** [District Synthesis Methodology](D.md#district-synthesis-methodology)

### District Synthesis Methodology
- **Category:** method term
- **Also called:** District Culture Development Plan (its phase plan); district methodology; district runbook; eight-phase sub-location methodology
- **Definition:** Out of fiction: the eight-phase procedure for developing each of Concordia's thirteen districts (lived-in texture, identity and meaning, Arcanet culture, visitor experience, ordinary daily life, thematic breadth, native culture, robot-specific culture); the plan file sets the phases and their order, and the runbook gives the procedure. It is the parent of the ULM: its disciplines (general population, shadow proportion, Review Panel) stay authoritative in the district folder, and the ULM reads its own interpreted copies.
- **Status:** project canon (completed for twelve of the thirteen districts; the Hub is deferred)
- **Used in:** InnerTepeniaGDD; DerivationMechanisms (via the ULM copy)
- **Sources:** InnerTepeniaGDD `Districts/District_Culture_Development_Plan.md`; `Districts/Phase_Instructions/00_Index.md` and `00_RUNBOOK.md`; `ULM/Disciplines/README.md`; `ULM/README.md`

### District Unity of Opposites
- **Category:** method term
- **Definition:** Out of fiction: the design reference that splits each Concordia district's internal conflict into parties and records what each side can only get from its opposite and from the districts it clashes with. It is the source of the district faction names and of the District Main Questlines.
- **Status:** project canon (design reference)
- **Used in:** InnerTepeniaGDD; DerivationMechanisms; copies
- **Sources:** InnerTepeniaGDD `Districts/District_Unity_of_Opposites.md`

### District Vision Notes
- **See:** [Vision Notes](V.md#vision-notes)

### District-Idolized ending
- **See:** [District Idolized Endings](D.md#district-idolized-endings)

### divergence operator
- **See:** [Divergence Principle](D.md#divergence-principle)

### Divergence Principle
- **Category:** method term
- **Also called:** divergence operator (its set of inputs)
- **Definition:** Out of fiction: the rule that a population's composition names only its starting stock, while time and place produce its culture. An origin culture is always changed, over about 250 years of local divergence, by the divergence operator's inputs (time, separation, local environment, local struggles and hardships, local goals, and local sensibilities and habits), so ethnic material is neither refused nor transplanted intact, and two cities founded from the same stock must still diverge.
- **Status:** Timeline canon (developer rulings, 2026-09-06); project canon in the ULM.
- **Used in:** TepenianUniverseTimeline; InnerTepeniaGDD (Cities; ULM; passes; CLAUDE.md); CurrentNovelDocs (worldbuilding OOLSD); DerivationMechanisms (ULM; CST; RWBEM; OOLSD); Hybrid-Anthro_Culture
- **Sources:** TepenianUniverseTimeline `Reference/No_National_Stereotypes.md` (The Divergence Principle); InnerTepeniaGDD `ULM/00_RUNBOOK.md` §C.9d; `ULM/ULM_Piece_Index.md` §6; `Neo-Races-and-Cultures/_Method/Human_Universals_Culture_Framework.md` §3; `CLAUDE.md` (Culture, ethnicity and the identity timeline)

### Divine Algorithm
- **Category:** culture and society
- **Definition:** Mentioned, not defined: a song prompt makes it the object of the robot Parvaneh Nouri's religious devotion.
- **Status:** working (song prompt only; in no canon file)
- **Used in:** CurrentNovelDocs (doll-music extraction)
- **Sources:** CurrentNovelDocs `worldbuilding/characters/doll-music extraction (2026-10-23)/3 - Characters I to R.md` (Parvaneh Nouri)
- **Open:** Its place among the GDD's robot religions is open.

### Division of Industry
- **Category:** method term
- **Definition:** Out of fiction: the GDD's analysis of how each city's workforce divides among industries and what each city must supply the nation, in baseline, mandated and free tiers. It is built from 22 necessary industries, sourced per-capita rates, a difficulty layer and a national supplier balance, describes only the Second Interwar Period (no war-damage factor), and also labels section 15 of every city spec and culture sheet.
- **Status:** project canon (marked RELIABLE 2026-09-01), with a food-layer carve-out; robot-keyed industries are open, and some figures are still estimates.
- **Used in:** InnerTepeniaGDD (Division_of_Industry; Specs; Local_Cultures; census; City_Master_Reference; ULM Phase 7); CurrentNovelDocs (reference copy); DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Cities/Division_of_Industry/README.md` and its numbered files; `Cities/Division_of_Industry_Sweep_2026-08-31.md`; `Cities/Local_Cultures/` §15
- **Open:**
  - Founders and station heritage never drive a sector (README banner).
  - Files 01, 03 and 07 are superseded; 09 is superseded by 16 but kept as an input. Folding the figures into Specs and Local_Cultures is a separate, pending task.
  - Area G1's harvest calls it working, area G3b's project canon. Background-Lore's megasheet sources call the section "Division of industry."

### DLC 1
- **See:** [Echoes of Amundsen](E.md#echoes-of-amundsen)

### DLC 2
- **See:** [Byrd DLC](B.md#byrd-dlc)

### DLC (Inner Tepenia)
- **Category:** game term
- **Definition:** Inner Tepenia: seven planned DLCs, one per subnet plus one for the South Pole: DLC 1 South Pole (Amundsen Station, Kendra Heinrich; released last), 2 Byrd, 3 Palmer, 4 Mawson, 5 Halley, 6 Janbogo, 7 Mirny. Each is a different, isolated account of post-Split-Brain history; "DLC 1" is a thematic label, not a release slot.
- **Status:** project canon (numbering); the release order of the subnet DLCs is undecided.
- **Used in:** InnerTepeniaGDD; copies
- **Sources:** InnerTepeniaGDD `Storyline/DLC_Overview.md`; `Outside-World/Tepenian-Federation/Locations/Per-Subnet_Overview_Reference_Data.md` §1

### DLC Main Questline Design Method
- **Category:** method term
- **Definition:** Out of fiction: a method for a DLC's main questline: gather the load-bearing facts already in canon, draft several But/Therefore chains from them, keep those that conflict with nothing and could only happen in that place, and prefer chains that grow out of established facts.
- **Status:** project canon in the GDD; working in Toronto Fell Out (skeleton; no DLC plan exists).
- **Used in:** InnerTepeniaGDD; TorontoFellOutGDD
- **Sources:** InnerTepeniaGDD `Storyline/DLC-Questlines/DLC_Main_Questline_Design_Method.md`; TorontoFellOutGDD, same path
- **Open:** The GDD's version asks for at least 10 candidates and names eight specific worldbuilding input sources, which Toronto Fell Out drops.

### DLC Scope Standard
- **Category:** method term
- **Definition:** Out of fiction: the design target for each of Inner Tepenia's seven DLCs: a main questline of about 4 to 6 hours and about 10 to 20 hours of optional content, roughly 14 to 26 hours in all.
- **Status:** project canon (binding design principle)
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `General-Overview-Notes/Game_Design_Principles.md` ("DLC Scope Standard")

### DLC-native companion
- **Category:** game term
- **Definition:** Inner Tepenia: a recruitable companion tied to a DLC's region. Every DLC must be completable with any, all or none of them, declining one is never a permanent lockout, and outside companions cannot enter a DLC on its first playthrough; DLCs 2 to 7 each get several, while DLC 1 has only Kendra Heinrich.
- **Status:** project canon (2026-07-10, 2026-07-20)
- **Used in:** InnerTepeniaGDD; DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Core-Mechanics/Companion_System.md` (Companions and DLCs; Multiple Native Companions Per DLC)

### DMZ
- **See:** [Great Lakes DMZ](G.md#great-lakes-dmz)

### the DMZ
- **See:** [Great Lakes DMZ](G.md#great-lakes-dmz)

### DNA-as-tech
- **Category:** game term
- **Definition:** Outer Tepenia 1: the series' DNA technology, carried over from *The Cryptograph Helix*, used as a real narrative thread; access to DNA tech is one of the three drivers shaping every settlement.
- **Status:** project canon
- **Used in:** Outer Tepenia 1
- **Sources:** Outer Tepenia 1 `README.md`; `Game_Design_Principles.md`
- **Open:** It is floated, not decided, as the mechanism for an Outer Tepenia version of Multiple Truths.

### Documentarians
- **Category:** group or people
- **Definition:** The Undergrid (Virgo) faction of meticulous record-keepers who see documentation as the district's only defense.
- **Status:** project canon
- **Used in:** InnerTepeniaGDD; copies
- **Sources:** InnerTepeniaGDD `Districts/District_Unity_of_Opposites.md` (District 12)

### Doll
- **Category:** group or people
- **Definition:** The in-world word for a sentient robot, of the kind first made in En.Ki.Du (2083). Every Doll built after that prototype has full synthetic skin and looks human, with luminescent irises as the only external tell, while En.Ki.Du alone looks noticeably robotic. Out of fiction, every character in the Dolliverse is based on a real, physically existing doll (the developer counts 1,185), which is why character folders keep doll photos.
- **Status:** Timeline canon
- **Used in:** essentially every repo, including TepenianUniverseTimeline; InnerTepeniaGDD; CurrentNovelDocs; DerivationMechanisms; SouthernLights; TheCryptographHelixDD; Outer Tepenia series; TorontoFellOutGDD; Hybrid-Anthro_Culture
- **Sources:** TepenianUniverseTimeline `Reference/World_History_Reference.md` (The Nuclear War of 2083); `Reference/Doll_Representation_Categories.md`; `Worldspace/Characters/Dolls/`; InnerTepeniaGDD `Worldspace/Characters/Dolls/Doll_Visual_Design_Canon.md`; media root `Tepenian_Universe_Overview.md`
- **Open:**
  - Character files mark "Type: Doll" or "Type: Gynoid" inconsistently, some read "Robot (Android / Gynoid — TBD)," and NPC sheets give "Species: Doll (Robot)."
  - The media-root overview says Dolls live much longer than humans but age and die; the GDD's physiology file says robots do not age (see Death (robot)).
  - Lowercase "doll" is also a y-template arc file (see doll, huMan-1 and huMan-2).

### Doll folder skeleton (composite z-template)
- **Category:** method term
- **Definition:** Out of fiction: the standard folder for each Doll character: README, Personal_Background/ (PreWar_History, Relationships, Loyalties, Timeline, War_Experiences, Logs), Questlines/ and Reference_Images/. The 2026-08-06 composite template merges the three roster templates and marks sections that don't apply as N/A.
- **Status:** working
- **Used in:** InnerTepeniaGDD; TepenianUniverseTimeline; CurrentNovelDocs
- **Sources:** InnerTepeniaGDD `Worldspace/Characters/Dolls/z-template/README.md`
- **Open:** The Timeline's template renames PreWar_History to Formative_History and War_Experiences to Conflict_Experiences, and adds Original Doll Model, Manufacturer and Catalog fields.

### Doll Height Transposition
- **See:** [Doll-to-Living Height Transposition](D.md#doll-to-living-height-transposition)

### doll, huMan-1 and huMan-2 (arc slots)
- **Category:** method term
- **Definition:** Out of fiction: the y-template's character-arc role files. `doll.md` is the robot lead's arc, built on the full composite structure (Save the Cat, Truby, Weiland, Campbell, Bell); `huMan-1.md` and `huMan-2.md` are the human companions' arcs on Dan Harmon's eight steps, and unnamed humans are written as "huMan" placeholders.
- **Status:** project canon (standing rule: foreground robots always get the composite structure)
- **Used in:** CurrentNovelDocs (every novel and film folder; y-template); z-staging; TheCryptographHelixDD (arc files); DerivationMechanisms
- **Sources:** CurrentNovelDocs `y-template/structure/character arcs/doll.md` and `huMan-1.md`; `reference/story-structure-definitions.md` (Which Structure Applies to Which Character); z-staging `Alaska-Cascadia Rescue/structure/character arcs/` and `Colorado ethics/structure/character arcs/`; DerivationMechanisms `Stories/Story_Structure/story-structure-definitions.md`
- **Open:** The z-staging copies of `doll.md` still contain a Magic Flight beat, which the author removed from the y-template on 2026-10-29 (Fantasy only). The "huMans" spelling already appears in the 2022 dream log at the CurrentNovelDocs root.

### Doll perks
- **See:** [Idolization and Companion-Arc Perks](I.md#idolization-and-companion-arc-perks)

### Doll Representation Categories
- **Category:** method term
- **Also called:** Cat. (abbreviation); Cat.s (abbreviation)
- **Definition:** Out of fiction: the four ways a character based on a real doll can be represented as an in-universe person: Robots (the only category in active use), Anthros (human-animal hybrids engineered by humans, which later became races), Elves (engineered by aliens on a parallel Earth) and Aliens (origin unknown). Categories 2 to 4 are canon but have no characters yet (as of 2026-08-09).
- **Status:** Timeline canon
- **Used in:** TepenianUniverseTimeline; InnerTepeniaGDD (ULM Phase 9 input); DerivationMechanisms; CurrentNovelDocs (doll-music extraction); Hybrid-Anthro_Culture
- **Sources:** TepenianUniverseTimeline `Reference/Doll_Representation_Categories.md`; InnerTepeniaGDD `ULM/Corpus_Reference_Sheets/Doll_Representation_Categories_Quick_Reference.md`
- **Open:** Songs call Elly a robot elf and Selandriel an elf princess. Calethina's template puts her on a doll body, while canon makes her a bodiless holographic AI.

### Doll Wiki
- **Category:** method term
- **Definition:** Out of fiction: a planned Fallout-Wiki-style website for which the Timeline compendium is to serve as the reference base. A doll's real model, manufacturer and catalog page are reserved for it.
- **Status:** working (future plan)
- **Used in:** TepenianUniverseTimeline; InnerTepeniaGDD; DerivationMechanisms
- **Sources:** TepenianUniverseTimeline `README.md` (Future Applications); InnerTepeniaGDD `Worldspace/Characters/Dolls/Character_Spec_Fill-In_Sheet_Template.md`
- **Open:** CurrentNovelDocs' memory calls the long-term goal a "Tepenian wiki atlas"; whether that is the same site is not stated.

### Dolliverse
- **Category:** method term
- **Definition:** Out of fiction: the author's umbrella name for the whole universe of his doll-based characters, across all projects; every character in it is based on a real, physically existing doll. Robot Universals are described as Dolliverse-wide, above Tepenia-wide and city-level canon, and music descriptions introduce each robot as living in the Dolliverse.
- **Status:** Timeline canon (used, not formally defined)
- **Used in:** TepenianUniverseTimeline; InnerTepeniaGDD; CurrentNovelDocs (doll-music extraction); DerivationMechanisms; Hybrid-Anthro_Culture
- **Sources:** TepenianUniverseTimeline `Reference/Doll_Representation_Categories.md`; DerivationMechanisms `Environment/Local_Robot_Culture_Methodology/00_DRAFT_Input_Categories_and_Approach.md` (Input Category E)
- **Open:** Its relation to the Tepenian universe (the same thing, or wider) is not stated.

### Doll-to-Living Height Transposition
- **Category:** method term
- **Also called:** Doll Height Transposition (file name)
- **Definition:** Out of fiction: the rule for reading a real doll's height as an in-universe woman's height. The doll world's typical range (about 158 to 165 cm) maps onto a normal in-universe female range of about 165 to 175 cm (5'5" to 5'9"), and each doll keeps her relative position in the distribution rather than getting a literal conversion.
- **Status:** project canon (developer-originated, 2026-09-18, universe-wide); filed in the Timeline until it moved to DerivationMechanisms on 2026-10-30 (Timeline commit 5d15159).
- **Used in:** DerivationMechanisms; CurrentNovelDocs; TepenianUniverseTimeline (formerly)
- **Sources:** DerivationMechanisms `Characters/Robot-specific/Doll_Height_Transposition.md`

### Dome Fuji
- **Category:** place
- **Also called:** The Temple (interim name); Valkyrie Dome (real-world alternate name)
- **Definition:** A Mawson-subnet city at Dome Fuji, about 3,810 m up on the East Antarctic plateau, Tepenia's highest. It was founded by devout Ice Cold Buddhism pilgrims tied to no country (DR-20) and is one of the faith's two primary sacred sites, a robot monastery; the altitude and cold are lethal to humans, so its whole population (55,072) is robot, and it could not shelter refugees as Concordia did. It survived the Long Night War, working at reduced capacity.
- **Status:** Timeline canon (name, subnet, altitude); project canon for its founders (DR-20) and for the interim name "The Temple" (developer, 2026-10-13; TepenianHawaiian D-2, C-10); working: its proper name is pending (DR-58).
- **Used in:** InnerTepeniaGDD (DLC 4); TepenianUniverseTimeline; SouthernLights; CurrentNovelDocs (reference copy); TorontoFellOutGDD (basis copy); TepenianHawaiian; Textbooks; DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Cities/Specs/Mawson subnet/Dome_Fuji.md`; `Cities/Local_Cultures/Mawson_Subnet/Dome_Fuji.md`; `Cities/Founding_Register.md`; `ULM/DEVELOPER_RULINGS_LOG.md` (DR-58); `Worldspace/Modern_Hawaiian_Language.md` §2; TepenianHawaiian `DECISIONS.md` (D-2); `CANON.md` (C-10); TepenianUniverseTimeline `Reference/World_History_Reference.md`; SouthernLights `Worldspace/Locations.md`; `Worldspace/Environments-Federation-Cities.md`
- **Open:**
  - **Name.** Until Modern Hawaiian is synthesized, the city is called "The Temple" (decided 2026-10-13; DR-58, 2026-10-18 to 10-21). Its proper name will be a Modern Hawaiian vocabulary word, the way Angkor Wat is both a temple's title and an ordinary Cambodian word, and no placeholder proper name may be coined until the language exists. "The Temple" also appears in other senses in some files, so context must be checked.
  - **Founders.** Japanese founders are ruled out (DR-20); older lore had a Japanese founding team that left after the Treaty.
  - Its own spec once said "no highway access"; `Highways.md` places it on Hwy 37.
  - Background-Lore names its sacred site "Nyakkyo" (not canon). "Ice Cold Buddhism" is itself a placeholder name.
  - DerivationMechanisms' Robot Universals call it the only city without its own fabrication chamber.

### Dominican Republic (all of Hispaniola)
- **Category:** polity
- **Definition:** After the 2083 war Haiti's population effectively dies out and the Dominican population expands to fill the island, so Hispaniola and its small surrounding islands are entirely the Dominican Republic.
- **Status:** project canon (2026-09-24; applied to the map data in the Caribbean round)
- **Used in:** CurrentNovelDocs (worldbuilding); InnerTepeniaGDD (Post-War Nations Founder Reference)
- **Sources:** CurrentNovelDocs `worldbuilding/STATUS - Cross-Session Progress Tracker.md` §3

### Donska-Kubania
- **Category:** polity
- **Definition:** One of the post-war Russian successor nations, covering the Don and Kuban region (Krasnodar, Adygea, Rostov, Stavropol, Kalmykia, Astrakhan, Volgograd), with its capital at Rostov-on-Don. Crimea, with Sevastopol, is attached to it as an Autonomous Zone.
- **Status:** working: CurrentNovelDocs' tracker records the name as set on 2026-09-27, but the map package still calls it a placeholder.
- **Used in:** CurrentNovelDocs (worldbuilding); InnerTepeniaGDD (Russia-split research logs)
- **Sources:** CurrentNovelDocs `worldbuilding/nations/World-Nations-Roster.md` (Russia); `worldbuilding/STATUS - Cross-Session Progress Tracker.md` §4.10; InnerTepeniaGDD `Cities/Research_Logs/Russia_Split_Proportions_RS1_Inventory_and_Method_2026-10-29.md`
- **Open:** The name's status conflicts between the tracker (named 2026-09-27) and the map package (placeholder); both sit outside the repos' canon files.

### Doris Morikawa's Hall of Archives
- **See:** [Hall of Archives](H.md#hall-of-archives)

### Double Gate
- **Category:** game term
- **Definition:** Inner Tepenia's romance rule, kept in its forks. Gate 1 is finishing the companion's relationship questline with a non-negative ending (a negative ending locks romance for good); Gate 2 checks the player's permanent MACHINE stats and traits against that character's own threshold, never perks or temporary buffs, in the normal visible stat-check format ([current/required]). Failing either gate closes the romance but not the relationship, and the character speaks "The Signal" line when Gate 2 fails; human men add a gender-presentation check, Kendra Heinrich has no stat gate, and Gate 3 is the Courtship Sequence.
- **Status:** project canon
- **Used in:** InnerTepeniaGDD; TorontoFellOutGDD; Outer Tepenia 1 (fork); DerivationMechanisms; CurrentNovelDocs (`reference/character-methodology/`); TepenianUniverseTimeline (Doll file)
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Core-Mechanics/Companion_System.md`; `Game-Mechanics/Universal_Rules.md`; TorontoFellOutGDD `Game-Mechanics/Core-Mechanics/Companion-System.md`; Outer Tepenia 1 `Game-Mechanics/Core-Mechanics/Companion_System.md`

### Double life
- **Category:** culture and society
- **Definition:** Zhongshan's daily dynamic: a shared public rhythm under the city's non-prying norm, with each family's own heritage kept quietly at home.
- **Status:** project canon
- **Used in:** InnerTepeniaGDD; CurrentNovelDocs (reference copy); SouthernLights
- **Sources:** InnerTepeniaGDD `Cities/Local_Cultures/Mirny_Subnet/Zhongshan.md`; `Neo-Races-and-Cultures/Mirny_Subnet/Zhongshan/Zhongshan_Catalog.md`

### The download
- **Category:** game term
- **Also called:** the personality download
- **Definition:** Inner Tepenia: the main-quest midpoint event in which Calethina is moved from her server into the player's wrist device, ending her dependence on the grid at a stat cost. It is separate from her romance.
- **Status:** project canon (event); its mechanics are partly open.
- **Used in:** InnerTepeniaGDD; TepenianUniverseTimeline; CurrentNovelDocs; Outer Tepenia series
- **Sources:** InnerTepeniaGDD `Dev-Road-Map/02-Blocking-Decisions.md` (Decision 3); `Game-Mechanics/Core-Mechanics/Companion_System.md`

### downtown core and outer area
- **See:** [Core/outer model](C.md#coreouter-model)

### DR
- **See:** [Damage Threshold and Damage Resistance](D.md#damage-threshold-and-damage-resistance)

### DR-19
- **See:** [Geography and access (founding rule)](G.md#geography-and-access-founding-rule)

### Drain Weapons
- **Category:** game term
- **Definition:** Inner Tepenia: a Tepenia-Original weapon category that removes a resource from the target (the Siphon mechanic) and deals Neural/Interface and Acid damage. Before the war the same tools served for coolant siphoning and diagnostics, an act of trust between a caretaker and the one cared for. It is built around the Coolant Siphon (draining a robot's coolant lowers Engine and can force a shutdown), with the Exposure Siphon as the human counterpart (heat, water, stamina) and glitch-coolant restoring drained coolant.
- **Status:** project canon (category philosophy); working (the item catalog is a first pass).
- **Used in:** InnerTepeniaGDD; SouthernLights; TorontoFellOutGDD (basis copy only)
- **Sources:** InnerTepeniaGDD `Worldspace/Weapons_and_Tools_Philosophy.md`; `Worldspace/Weapon_Item_Catalog.md`; `Game-Mechanics/Combat/Damage_Types.md`; SouthernLights `Storyline/Weapons-and-Tools-Philosophy.md`

### dream-inducers
- **See:** [Dream-tech](D.md#dream-tech)

### Dream-tech
- **Category:** technology
- **Also called:** dream-tech dens (its venues); dream-tech clinics; dream-inducers (the devices); dream-weavers (its operators)
- **Definition:** Pisces' (the Markets') signature technology: devices that induce dreams, used for purposes from therapy to recreation and offered in dream-tech dens, the district's most visible public institution. The dens descend from Prohibition-era speakeasy infrastructure and stand alongside underground clinics; some preserve curated, consensual memory fragments from The Flood.
- **Status:** project canon
- **Used in:** InnerTepeniaGDD; SouthernLights; TorontoFellOutGDD; CurrentNovelDocs
- **Sources:** InnerTepeniaGDD `Districts/District_Canon_Reference.md` (District 10, Pisces); `Climax_Structure_and_District_Ending_Consequences.md`; SouthernLights `Worldspace/Environments-Concordia-Districts.md` (10. Pisces)

### dream-tech clinics
- **See:** [Dream-tech](D.md#dream-tech)

### dream-tech dens
- **See:** [Dream-tech](D.md#dream-tech)

### dream-weavers
- **See:** [Dream-tech](D.md#dream-tech)

### DRL
- **See:** [Developer Rulings Log](D.md#developer-rulings-log)

### DRQ
- **See:** [Developer Ruling Queue](D.md#developer-ruling-queue)

### DT
- **See:** [Damage Threshold and Damage Resistance](D.md#damage-threshold-and-damage-resistance)

### Dual economy
- **Category:** culture and society
- **Definition:** The split between what humans and robots spend on in Tepenia: most services, culture and transit are shared, but food (human food versus siligel) and maintenance are entirely separate. Any Tepenian currency had to bridge this.
- **Status:** project canon (as an observation); working: how the money system handled it.
- **Used in:** InnerTepeniaGDD; CurrentNovelDocs (reference copies); SouthernLights; TorontoFellOutGDD (basis copy only); DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Worldspace/National_Economy_and_Currency.md`; `Worldspace/City_Logistics.md` (The Dual Economy)
- **Open:** How the currency bridged the split is not decided.

### Dual Tagging
- **Category:** method term
- **Also called:** Dual Tagging (Inheritance + Iceberg Layer)
- **Definition:** Out of fiction: Step 5 of the Local Robot Culture Methodology. Each finding is tagged twice, once for inheritance (directly inherited, adapted, or genuinely emergent and robot-only) and once for its iceberg layer (Surface or Deep Culture), so findings are more than the local human culture with robots added; the ULM's Phase 9 uses a related dual tag of inheritance and depth.
- **Status:** working
- **Used in:** InnerTepeniaGDD (Local Robot Culture; ULM Phase 9); DerivationMechanisms
- **Sources:** DerivationMechanisms `Environment/Local_Robot_Culture_Methodology/00_DRAFT_Input_Categories_and_Approach.md` (Step 5); InnerTepeniaGDD `Cities/Local_Robot_Culture_Methodology/00_DRAFT_Input_Categories_and_Approach.md`; `ULM/03_The_Phase_Spine.md` (Phase 9)

### Dual-Network Operators
- **Category:** group or people
- **Also called:** Network Operators
- **Definition:** The faction of Circuit (District 9) workers who run both the official Arcanet and the shadow network, sometimes on the same shift.
- **Status:** project canon
- **Used in:** InnerTepeniaGDD; SouthernLights; copies
- **Sources:** InnerTepeniaGDD `Districts/District_Unity_of_Opposites.md` (District 9)

### Dual-Outcome Branching
- **Category:** method term
- **Definition:** Out of fiction: the design principle that a character's personal arc resolves into two to five mutually exclusive outcome branches (three is the default, five the cap), each a genuinely different ending, so one choice forecloses the others. It generalizes Inner Tepenia's Dual-Outcome Companion Perks rule.
- **Status:** project canon (production rule; optional, for branching works)
- **Used in:** DerivationMechanisms; InnerTepeniaGDD; CurrentNovelDocs; TorontoFellOutGDD; TepenianUniverseTimeline
- **Sources:** DerivationMechanisms `Characters/Character_Development_Methodology/Design_Principles/Dual_Outcome_Branching.md`

### Dual-Outcome Companion Perks
- **Category:** game term
- **Definition:** Inner Tepenia and Toronto Fell Out: the binding perk rule that each companion questline ends in two to five mutually exclusive companion perks (three is the target), and the player's own perk is locked to the branch the companion got. It is modeled on Cass's Hand of Vengeance or Calm Heart in Fallout: New Vegas.
- **Status:** project canon (2026-07-03; individual perks provisional)
- **Used in:** InnerTepeniaGDD; TorontoFellOutGDD; TepenianUniverseTimeline (Doll file); DerivationMechanisms; CurrentNovelDocs (`reference/character-methodology/`)
- **Sources:** InnerTepeniaGDD `Game-Mechanics/Perks/Perk_Framework.md`; TorontoFellOutGDD `General-Overview-Notes/Design-Philosophy.md` (Perk Design Laws)

### Dual-Table Suppers
- **Category:** culture and society
- **Definition:** Mirny's informal daily meals at which Russian and Chinese dishes are served side by side, kept distinct rather than fused.
- **Status:** working: megasheet proposal
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `Cities/City_Megasheets/Mirny_Subnet/Mirny/Mirny_Community_Infrastructure.md`; `BL/Mirny_Subnet/Mirny/Mirny_Historical_Vignettes_and_Informational_Sheets.md` (a non-canon vignette file)
- **Open:** It builds on Russian and Chinese communities that the Founding Register now treats as exile groups rather than founders (the founder is Idelsk-Uralia).

### Dumont Coast Highway
- **See:** [Hwy 2 (Dumont Coast Highway)](H.md#hwy-2-dumont-coast-highway)

### Dumont d'Urville
- **Category:** place
- **Definition:** A Janbogo-subnet city on the Dumont d'Urville Station site, on Petrel Island off Adélie Land and facing the Dumont d'Urville Sea, among the windiest places on Earth and beside Adélie penguin colonies. St. Jules is its namesake Saint, it is a double highway terminus (Hwy 2 and Hwy 183), and the Founding Register gives Japan as its founder. It was damaged in the Long Night War but stayed partially operational after an organized wartime evacuation.
- **Status:** Timeline canon (name, subnet); project canon for its founders (DR-20, DR-44); working: a rename is ruled but no name is chosen (DR-58).
- **Used in:** InnerTepeniaGDD (DLC 6); TepenianUniverseTimeline; SouthernLights; CurrentNovelDocs (reference copy); TorontoFellOutGDD (basis copy); DerivationMechanisms
- **Sources:** InnerTepeniaGDD `Cities/Specs/Janbogo subnet/Dumont_dUrville.md`; `Cities/Founding_Register.md`; `ULM/DEVELOPER_RULINGS_LOG.md` (DR-58); TepenianUniverseTimeline `Reference/World_History_Reference.md`; `Worldspace/Locations/README.md`; SouthernLights `Worldspace/Environments-Federation-Cities.md`
- **Open:**
  - **Rename.** DR-58 rules it will get a new name in line with its Japanese founders; none is chosen, and no sweep is to run unprompted. Its St. Jules observances are affected, and its spec ties the demonym to the new name.
  - **Founders.** French founders are ruled out, but the `Local_Cultures` sheet, Background-Lore (for example chain #9 "Everyone Learns French Eventually") and SouthernLights (a francophone island city likened to a tiny New Orleans) still build on a French founding; a revisit item.
  - Whether it has a permanent mainland bridge or a seasonal crossing is deliberately open; SouthernLights gives it a bridge.

### d'Urvillean
- **Category:** group or people
- **Also called:** d'Urvillois (megasheet form); d'Urvilloise (feminine)
- **Definition:** The Neo-Races working name for the people of Dumont d'Urville.
- **Status:** working: placeholder
- **Used in:** InnerTepeniaGDD
- **Sources:** InnerTepeniaGDD `Neo-Races-and-Cultures/Janbogo_Subnet/Dumont_dUrville/Dumont_dUrville_Catalog.md`
- **Open:** The megasheet (§VI) resolves "d'Urvillois" (feminine "d'Urvilloise"), while the spec says TBD, depending on the city's new name (DR-58).

### d'Urvillois
- **See:** [d'Urvillean](D.md#durvillean)

### d'Urvilloise
- **See:** [d'Urvillean](D.md#durvillean)
