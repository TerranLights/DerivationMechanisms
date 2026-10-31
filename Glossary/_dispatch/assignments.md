# Assignments: the glossary harvest (2026-10-30)

All agents follow `brief.md`. Media root: `/home/kuroskalacs/Documents/Doll-Fi/media/`. Harvest files go in `Reference/DerivationMechanisms/Glossary/_harvest/<area>.md`.

| Area | Agent covers | Candidate list |
|---|---|---|
| **T** | TepenianUniverseTimeline, the whole repo: `Reference/TepenianUniverseTimeline/` (the canonical layer: eras, events, treaties, nations, Megacorps, Laws of Robotics, Robot Universals, Universal Design Laws) | `candidates/T.txt` |
| **G1** | InnerTepeniaGDD `Background-Lore/` | `candidates/G1.txt` |
| **G2** | InnerTepeniaGDD `Worldspace/Robot_Biology_and_Culture/`, `Worldspace/Factions/`, `Worldspace/Characters/` (group terms only), `Worldspace/Canon_Gap_Resolution_Method/`, `Neo-Races-and-Cultures/`, `Game-Mechanics/`, `General-Overview-Notes/`, `Theoretical-Calculations/` | `candidates/G2.txt` |
| **G3a** | InnerTepeniaGDD `Worldspace/Locations-and-Levels/` **except** `Universal_Location_Methodology/` and `Outside-World/Tepenian-Federation/Locations/Cities/`. It covers Concordia (district in-fiction names, institutions), Infrastructure, Towns, Per-Subnet guides, the Falkland Treaty and the Super Ultra Megasheet | `candidates/G3a.txt` |
| **G3b** | InnerTepeniaGDD `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`: city names, subnets, city-level institutions that recur. Start from the city specs and per-city READMEs; the development-pass and reader files are run data | `candidates/G3b.txt` |
| **G4** | InnerTepeniaGDD `Storyline/`, `Dev-Road-Map/`, `Reference/` (in-universe and design material only, not the Real-World extractions), and the root files (`README.md`, `TODO.md` and so on) | `candidates/G4.txt` |
| **C** | CurrentNovelDocs: `Literature/books/CurrentNovelDocs/` (worldbuilding, every novel folder, the Gilgamesh film, Maritza, `reference/`). Skip `z-archive`, `worldbuilding/extractions/` and the map-data CSV folders | `candidates/C.txt` |
| **S** | The Cryptograph Helix series (`Literature/books/The Cryptograph Helix series/`), the Outer Tepenia series (`games/Outer Tepenia series/`), SouthernLights (`TV/SouthernLights/`), `Literature/books/z-staging (pre-template projects)/`, `TV/ElvenSteel/`, `TV/Tuned/` | `candidates/S.txt` |
| **O** | `games/Toronto Fell Out/TorontoFellOutGDD/`, `games/Safety Code Violator/SafetyCodeViolatorGDD/`, `games/Plot Hole/PlotHoleGDD/`. Say which universe each project belongs to | `candidates/O.txt` |
| **M** | Method terms, out of fiction: Derivation Mechanisms (`Reference/DerivationMechanisms/`: Environment, Characters, Data_Reference; skip Stories/Story_Structure), InnerTepeniaGDD `Worldspace/Locations-and-Levels/Universal_Location_Methodology/`, plus `Reference/TepenianHawaiian/`, `Reference/Hybrid-Anthro_Culture/`, `Reference/slang-synthesis/` (system and register names only, no vocabulary) and `Reference/Textbooks/` | `candidates/M.txt` |

**Repo roots** for grepping "Used in":
- InnerTepeniaGDD: `games/Inner Tepenia/InnerTepeniaGDD/`
- TepenianUniverseTimeline: `Reference/TepenianUniverseTimeline/`
- CurrentNovelDocs: `Literature/books/CurrentNovelDocs/`
- TheCryptographHelixDD: `Literature/books/The Cryptograph Helix series/TheCryptographHelixDD/`
- SouthernLights: `TV/SouthernLights/`
- Outer Tepenia: `games/Outer Tepenia series/`
- TorontoFellOutGDD: `games/Toronto Fell Out/TorontoFellOutGDD/`
- SafetyCodeViolatorGDD: `games/Safety Code Violator/SafetyCodeViolatorGDD/`
- DerivationMechanisms: `Reference/DerivationMechanisms/`

**Always skip** `graphify-out/`, `.git/` and the GDD's `Archive/`.
