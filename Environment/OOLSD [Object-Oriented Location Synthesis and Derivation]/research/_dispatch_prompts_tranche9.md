# Ninth research tranche (low Earth orbit infrastructure: from Antarctica to orbit, and from orbit to Mars): the exact dispatch prompts

**2026-11-01. Phase A (architecture, sections A1-A3) dispatched first, at the developer's direction, and done the same day: `leo_infrastructure_architecture.md`, `windows_views_and_sky_access_in_rotating_habitats.md`, `diamond_windows_and_fullerene_reinforcement.md`. The numbered sections (getting material up, building, running, Mars) wait for the developer's go-ahead; the developer expects to run them on 2026-11-02.** Triggered by the developer: *"we'll need to do a lot of research for Low-Earth Orbit infrastructure. This will be relevant to both Antarctica and to outer space, especially Mars, and so this will additionally tie in to the OOLSD."*

**Order (developer, 2026-11-01):** *"First, we should research and understand what kind of architecture Low-Earth Orbital Infrastructure would actually have, because then we can have a better idea of the logistics and getting materials up there, and then how to build it."* Phase A therefore comes first.

**A feature the developer has in mind, for later-stage infrastructure rather than early stations:** very large windows, because many people gain a psychological benefit from seeing the sky. In a wheel or cylinder the "sky" lies beneath the "ground", so seeing it means looking up through the floor on the far side of the wheel or cylinder. The windows would be lab-grown diamond, reinforced with fullerene ("C64/Fullerene") cables. A materials resource among the developer's PDF books is the basis of reference for the reinforcement: the *Graphene Science Handbook*, six volumes, in `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Materials/books/STEM/Graphene Science Handbook [Vol 1 - 6]/`. (The sections below test this physics-first; they do not assume it works.)

**What is already covered (do not redo):** the LEO environment, rotating habitats and their mass, human health, machines and launch cost (`leo_and_orbital_habitats.md`, `gap_retry_leo_human_machines_power.md`); the robot body in space (`robot_body_in_space.md`); life support and structures (`life_support_lowg_power_structures.md`); the Moon, Lagrange points and mass drivers (`moon_lagrange_and_comparables.md`); transport, processing and industrial ramps (`space_trucking_and_transport_infrastructure.md`, `space_processing_and_fabrication.md`, `industrial_ramp_timelines.md`); cyclers (`cyclers_and_large_slow_vehicles.md`); Mars and transfers (`mars_venus_and_transfer.md`). This tranche covers the **infrastructure layer**: how a society reaches LEO from Antarctica, where in LEO it builds, how it builds, supplies, powers and links it, and how LEO serves as the gateway to Mars. **Two delivery modes (developer, 2026-11-01):** construction takes place in LEO throughout. Construction begins with materials lifted off Earth "the more traditional way" (rockets); later, components are shuttled up through the Tower at the South Pole, and construction still takes place in LEO. "The traditional way" is not only rockets: mass drivers and other techniques are possible too, and a mass driver would likely sit near the equator. Its host would be one of the First Interwar Period's countries; the developer names Indonesia as one possibility, perhaps among others. Section 2 covers rockets, section 3 mass drivers and other ground launchers (with real candidate sites), section 1 the Tower, and section 4 the choice of an orbit all of them can serve. Matching candidate sites to First Interwar countries is canon work for the developer, done after this research and not by these agents. (This framing stays in this note; the sections below are written as physics only.) One gap is already on record: `canon_vs_physics_comparison.md` (open item 6) notes that no research file covers the consequences of launching from the South Pole, which reaches only polar orbits directly.

Each agent is told to read ONLY its own numbered section below plus the common rules, so the saved text and the dispatched text are the same.
**To re-dispatch a lost agent:** Agent tool, type general-purpose, background, with the one-line prompt: *"Your task is section N of /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/OOLSD [Object-Oriented Location Synthesis and Derivation]/research/_dispatch_prompts_tranche9.md . Read the common rules at the top and section N only, and follow them exactly. Your file may already exist from an interrupted run; if so, continue it."* (`SendMessage` resumes a live agent only.)

**Developer rulings that govern all of them:** research the physics on its own terms; do NOT force results into any story, timeline or canon; the briefs contain none. Report plainly anything that cuts against a premise in the question, with its numbers.

## COMMON RULES (apply to every section)

You are a research agent for the OOLSD library. Your shared brief is at /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/OOLSD [Object-Oriented Location Synthesis and Derivation]/research/_BRIEF.md . Read it first and follow it exactly (it is final; nothing in it changes), including the nine output sections, the search-log discipline, "no figure from memory", and the 120-word final reply.
- **Your output file** is the file named in your section's heading, in that same `research/` folder.
- Research physics and engineering only. Assume no story, timeline or setting. If a concept is infeasible, uneconomic or only a thought experiment, say so plainly and give the numbers that decide it. Mark each finding DEMONSTRATED, ENGINEERING-STUDIED, or SPECULATIVE.
- **Create your file FIRST** (heading plus `## SEARCH LOG`) and append as you go, so an interruption leaves something usable. If your file already exists, open it, read its SEARCH LOG, and continue from where it ends.
- **Scratch folder:** put any temporary file ONLY in /tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-Literature-books-CurrentNovelDocs/3d728365-b74f-46ea-8b81-16f2bbd67a4d/scratchpad/ in a subfolder named after your own file. **Never delete, move or overwrite any file in the research folder other than your own output file.** Other agents are writing there at the same time.
- Where an arithmetic result matters, run it (Python is available; run with `python3 -I`) and show the formula and inputs; inputs must be sourced constants. Paste the key output into your Derived figures section.
- Work breadth-first across the checklist, then go back and query each quantity from a second angle (LAW 0-R). A quantity found once is one source. Primary sources are papers, agency reports, handbooks and datasets; popular pages are leads only.
- **Sibling files** (read-only, to avoid repeating): you may read the files named in your section, in the same folder. Cite them; do not re-derive what they hold. Do not read or edit anything else in the repository. No git commands.
- No South Asian sources (a standing rule of the developer's).

---

# PHASE A: ARCHITECTURE (run first)

## A1. `research/leo_infrastructure_architecture.md`

TOPIC: what low Earth orbit infrastructure physically consists of, as architecture: the kinds of structures, how each is laid out, and how a small early station grows into a large later one.

Checklist (cover each, or list the gap under Open threads with the reason):
1. A typology of LEO infrastructure, flown and studied:
   - modular stations (Mir, the ISS, Tiangong) and the commercial stations planned for 2025-2030;
   - rotating habitats (wheel or torus, cylinder, Bernal sphere, Kalpana-type designs, tethered or dumbbell pairs);
   - non-habitat infrastructure (depots, shipyards and drydocks, power stations, docking hubs, tug bases, communication nodes, debris-removal platforms).

   For each: size, mass, crew or population, spin rate, shielding, and evidence level.
2. The anatomy of a rotating habitat:
   - hub, spokes and rim;
   - a non-rotating shield shell versus a rotating one;
   - counter-rotating pairs, and the bearings and seals at the rotating-to-static interface;
   - docking at the hub, and elevators in the spokes;
   - where machinery, storage, agriculture and housing sit, and why (gravity level by radius).
3. Interior architecture under spin: published guidance on floor area and volume per person, ceiling heights, Coriolis-aware layout (stairs, doors, ladders, sports), sightlines and the curved horizon (NASA SP-413, Hall's artificial-gravity architecture work, Globus, and others).
4. Light: how published designs bring in sunlight (mirrors, window strips, light pipes) or replace it with artificial light, and the power and mass of each approach.
5. Growth paths: published concepts for starting small and growing (non-spinning core first, adding ring segments, spinning up later, linking habitats), and what stays fixed from the first stage onward (spin axis, hub, docking).
6. Architecture driven by its site in LEO: what drag, debris, atomic oxygen and eclipse cycles force on outer surfaces, attitude and layout (cite `leo_and_orbital_habitats.md`; do not re-derive).

You may also read, read-only: `leo_and_orbital_habitats.md` (section D), `life_support_lowg_power_structures.md`, `../Orbital_Infrastructure/Orbital_Infrastructure_Mass_Budget.md`, `../classes/01_Robot-Only_Staging_Station.md`.

---

## A2. `research/windows_views_and_sky_access_in_rotating_habitats.md`

TOPIC: windows and views in a rotating orbital habitat: why people want them, what an occupant would actually see, and what large windows cost in safety and mass.

Checklist:
1. The human side, from measured evidence:
   - window and view studies from spaceflight (the ISS Cupola, crew reports, NASA habitability research);
   - analog environments: Antarctic winter-over stations, submarines, and other windowless or confined settings;
   - daylight and view research on Earth;
   - the "overview effect" literature.

   Separate measured effects from claims.
2. Window geometry in published rotating-habitat designs: O'Neill's cylinder with alternating land and window strips and its mirrors, the Stanford torus's mirror and chevron shield, the Bernal sphere, and any design with windows in the floor.
3. What an occupant sees:
   - through a floor window, the sky beneath their feet, and looking "up" across the cylinder or wheel toward the far side;
   - how fast the star field turns at the habitat's spin rate, and whether that disturbs people (vestibular and visual studies);
   - how often Earth and the Sun pass in LEO, and the 90-minute day.

   Show the arithmetic.
4. Hazards of large windows:
   - radiation dose through transparent material versus opaque shielding;
   - micrometeoroid and debris strikes on large panes (shutters, transparent shields, the ISS Cupola's covers and pane layers);
   - UV, glare and thermal loads.
5. Pressure loading: the thickness a pane needs to hold one atmosphere across spans of 1, 5 and 20 meters, by material, with the safety factors used for crewed windows (NASA standards) and for the largest pressure windows on Earth (large aquarium panels, deep-submergence viewports). Show the arithmetic, and say whether many small panes in a frame beat one large pane.

You may also read, read-only: `leo_and_orbital_habitats.md`, `life_support_lowg_power_structures.md`.

---

## A3. `research/diamond_windows_and_fullerene_reinforcement.md`

TOPIC: whether lab-grown diamond can make large windows for an orbital habitat, and whether fullerene-family fibers or cables can reinforce them.

Checklist:
1. Lab-grown (CVD and HPHT) diamond as a window material:
   - the largest single-crystal and polycrystalline plates made to date, and growth rates;
   - cost per area;
   - optical transmission, strength, fracture toughness, hardness and thermal conductivity;
   - radiation darkening, and erosion by atomic oxygen in LEO;
   - existing diamond windows: the Pioneer Venus probe window, gyrotron and high-power laser windows, and others.
2. Mounting and joining diamond: bonding, brazing, frames, and thermal-expansion mismatch.
3. Alternatives for comparison: sapphire, ALON, spinel, fused silica, borosilicate, acrylic and polycarbonate. Give the same properties, plus the largest sizes made.
4. Fullerene-family fibers and cables, testing the developer's term "C64/Fullerene cables":
   - which fullerene-family materials exist (C60, C70, higher fullerenes including reports of C64, fullerene polymers, carbon nanotubes as tubular fullerenes, graphene fibers);
   - which can form load-bearing fibers or cables, with measured strength at macroscopic lengths versus single-molecule values;
   - what is demonstrated and what is speculative.
5. Reinforcing large glazing: structural-glass engineering, cable-net facades, mullions, laminated panes, and composite frames. Where cable reinforcement helps a pressure window, and where it does not.
6. **The developer's book:** the *Graphene Science Handbook* (6 volumes, PDF) at `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Materials/books/STEM/Graphene Science Handbook [Vol 1 - 6]/`.
   - Use it as a primary source: Volume 4 (mechanical properties) first, then Volume 6 (applications) and any others that apply.
   - It is long (about 4,000 pages). Extract text with `pdftotext` into your scratch folder and search it (for fullerene, C60, nanotube, fiber, tensile, composite, transparent, window). Read the relevant chapters.
   - Cite volume, chapter and page. Quote only short phrases; the book is copyrighted and this repository is public.
   - This is the one file outside the research folder you may read.

You may also read, read-only: `life_support_lowg_power_structures.md`, `robot_body_in_space.md` (materials sections).

---

# PHASE B AND LATER: GETTING MATERIAL UP, BUILDING, RUNNING, MARS (after Phase A)

## 1. `research/polar_launch_and_ascent_from_antarctica.md`

TOPIC: reaching low Earth orbit from Antarctica, and from the South Pole in particular.

Checklist (cover each, or list the gap under Open threads with the reason):
1. Launch geometry from high southern latitudes: which inclinations are reachable directly from a given latitude, the loss of Earth's rotational velocity at the pole, and the delta-v cost of reaching other inclinations (plane changes, combined burns, dog-leg ascents). Show the arithmetic for launch sites at 90°S, 78°S and 70°S.
2. Using J2 nodal precession instead of thrust to reach other orbital planes: rates by altitude and inclination, and the waiting times involved.
3. High-latitude launch sites as real comparables (Plesetsk, Vandenberg, Andøya and Esrange, Kodiak, and any others): what inclinations they serve, payload penalties, range-safety corridors.
4. Rocketry in Antarctica itself: sounding-rocket and balloon campaigns (dates, sites, results), and the cold-weather constraints on vehicles, propellants, seals and ground systems (sourced figures).
5. Towers, fountains and launch-assist structures at a pole: the space-fountain literature (Forward, Bolonkin, Knapman and later), the launch loop (Lofstrom), and space elevators (Pearson; current fiber-strength figures), with what a structure at the rotation axis can and cannot provide. What the remaining velocity at a structure's top means for the final stage.
6. Air-launch and reusable-vehicle options from a polar ice runway: what is demonstrated (runways on ice, heavy aircraft operations in Antarctica) and what is not.

You may also read, read-only: `leo_and_orbital_habitats.md` (section F), `canon_vs_physics_comparison.md`, `canon_adjustment_proposals.md`, `space_trucking_and_transport_infrastructure.md`.

---

## 2. `research/conventional_heavy_lift_of_construction_material.md`

TOPIC: lifting construction material and prefabricated components from Earth's surface to LEO by rocket, before any launch-assist structure exists.

Checklist:
1. Heavy-lift vehicles, expendable and reusable: payload to LEO by inclination, cost per kilogram from published figures (historical and current), and the turnaround and production rates that cap cadence.
2. Launch sites by latitude: which inclinations each serves at full payload, the payload penalty for higher inclinations, and range-safety corridors. Include equatorial and sea-launch sites.
3. Payload size limits: fairing and cargo-bay dimensions and mass, and how they constrain component design (module diameters, truss segments, the ISS module precedent, inflatable and deployable structures).
4. Raw material versus finished components: published trades between launching finished modules, kits for assembly in orbit, and bulk raw stock for fabrication in orbit.
5. Two delivery modes, one after the other: a construction site first supplied from mid- and low-latitude sites (by rocket or by a ground launcher near the equator), and later by a launcher at the South Pole that reaches only polar orbits. Give the delta-v and propellant cost of serving one orbital plane from the other, and which construction-orbit inclinations keep both modes affordable. Show the arithmetic.
6. Building up a launch industry: published examples of cadence growth (the shuttle, Soyuz, Falcon 9, Starship plans) and what limited each.

You may also read, read-only: `space_trucking_and_transport_infrastructure.md`, `industrial_ramp_timelines.md`, `gap_retry_leo_human_machines_power.md` (section F), `canon_adjustment_proposals.md`.

---

## 3. `research/non_rocket_earth_launch_and_mass_driver_siting.md`

TOPIC: launching material from Earth's surface toward orbit without rockets, or with only a small final rocket stage, from a site near the equator, and where on Earth such a site physically fits.

Checklist:
1. Electromagnetic mass drivers from Earth's surface: StarTram (Powell, Maise, Paniagua) and its generations, NASA and Sandia coilgun and railgun studies, magnetic-levitation launch assist (NASA's MagLifter and similar). For each: exit velocity, track length, acceleration, power, cost per kilogram, and what hardware has actually been built (for example, electromagnetic aircraft catapults and naval railgun tests).
2. Getting through the atmosphere from the ground: exit at high altitude (a tube up a mountain, evacuated tubes and how their exits are sealed, elevated exit ramps), drag and heating losses, heat shields, the burn needed at apogee to reach orbit and the payload fraction left after it, and acceleration limits (cargo versus people).
3. Other non-rocket or partly non-rocket methods, each with evidence level, payload, cost and limits:
   - light-gas guns (SHARP, Quicklaunch);
   - SpinLaunch (test data, with claims kept apart from demonstrations);
   - launch loops (Lofstrom);
   - beamed-energy propulsion (laser and microwave thermal);
   - rotating tethers and skyhooks that catch suborbital payloads (HASTOL and others);
   - high-altitude balloon platforms and rockoons;
   - air-breathing first stages.
4. Siting physics, quantified: why near the equator (rotational velocity, which inclinations can be reached), elevation and air density, an eastward slope, a downrange ocean for safety, geology and earthquake risk, power supply, and weather (lightning, cloud, rain).
5. Real candidate sites: high terrain and coasts within the equatorial belt that meet those criteria, with coordinates, elevations, slopes and seismic hazard. Include any published proposal that names a site, and existing or planned equatorial launch sites (Kourou, Alcântara, Biak, the San Marco platform at Malindi, Sea Launch and others). Cover Indonesia's candidates (for example the Papua highlands and Biak) and the alternatives elsewhere in the belt. Physical and published facts only; no politics.
6. The two-route problem from the equator: which orbits an equatorial launcher reaches, and the delta-v and propellant cost of serving a construction orbit that a launcher at the South Pole (polar orbits only) will also supply later. Show the arithmetic.

You may also read, read-only: `moon_lagrange_and_comparables.md` (its mass-driver sections), `leo_and_orbital_habitats.md` (section F), `space_trucking_and_transport_infrastructure.md`.

---

## 4. `research/leo_orbit_selection_for_permanent_settlements.md`

TOPIC: where in LEO a large, permanent settlement should sit, and what each choice costs.

Checklist:
1. Radiation by altitude and inclination: the South Atlantic Anomaly, the outer-belt electrons and the "polar horns" met by high-inclination orbits, and solar particle access at high inclination, with dose figures for polar versus low-inclination orbits.
2. Drag, atomic oxygen and orbital lifetime by altitude through the solar cycle, for very large, low-density structures (ballistic coefficient), and the station-keeping propellant or power needed.
3. Debris and meteoroid flux by altitude and inclination (ORDEM and ESA MASTER figures), the busiest shells today, and collision risk between large structures in crossing planes.
4. Lighting: beta-angle behavior and eclipse fractions for polar and sun-synchronous orbits versus low inclinations; dawn-dusk orbits with near-continuous sunlight.
5. Relative motion of stations in different planes: how often they can meet, and the delta-v of transfers between them.
6. Shells and spacing: published proposals for sharing orbital shells among many large objects (constellation filings, traffic studies), and carrying-capacity estimates for LEO.
7. One orbit, two supply routes: which inclinations can be reached affordably both from low- and mid-latitude launch sites (including an equatorial ground launcher) and from a launcher at the South Pole (polar orbits only), and what a settlement gives up at each compromise inclination (radiation, debris, lighting, ground contact).

You may also read, read-only: `leo_and_orbital_habitats.md`, `gap_retry_leo_human_machines_power.md`.

---

## 5. `research/antarctic_ground_segment_and_polar_communications.md`

TOPIC: Antarctica's real relationship to low Earth orbit: ground stations, communications and re-entry.

Checklist:
1. Every polar orbit passes over both poles on each revolution: the contact time a polar ground station gets per orbit and per day, from real stations (McMurdo Ground Station, TrollSat, GARS O'Higgins, Syowa and any others), with antenna sizes and data rates.
2. Geostationary visibility limits at high latitudes: the latitude beyond which GEO satellites are below the horizon, and how South Pole station communicates today (inclined GEO satellites, TDRS, Iridium, LEO constellations), with bandwidth and outage figures.
3. LEO constellations over Antarctica: polar shells, laser inter-satellite links, what service has been demonstrated at Antarctic stations, and latency.
4. Optical ground stations and the polar plateau's sky for laser links (cloud cover, seeing), with sourced figures.
5. Re-entry and disposal: the South Pacific Ocean Uninhabited Area ("Point Nemo"), controlled re-entry practice, and debris-fall risk over high southern latitudes.
6. The legal frame, facts only: the Antarctic Treaty's provisions that bear on satellite ground stations and military use, and disputes about dual-use stations.

You may also read, read-only: `gap_retry_leo_human_machines_power.md` (section A, latency).

---

## 6. `research/building_large_structures_in_leo.md`

TOPIC: how very large structures are built in LEO, and where their mass comes from.

Checklist:
1. In-space assembly and manufacturing: what has flown or been tested (robotic assembly, truss fabrication, welding and 3D printing in orbit), program status as of 2025-2026, and measured or projected assembly rates.
2. Construction rates and labor: published estimates of how fast a large habitat can be assembled, by robots and by crews, and what limits them.
3. Orbital debris as material: active debris removal demonstrations, the composition of the large-debris mass (rocket bodies and satellites by alloy and material), the energy and delta-v to gather it, and recycling in orbit.
4. Material from the Moon to LEO: delivered cost and energy by mass driver plus aerobraking or aerocapture versus launch from Earth, with the published studies.
5. Asteroid material to LEO: retrieval studies (the Asteroid Redirect Mission and others), the mass that can be moved, and timescales.
6. Drydocks, shipyards and tethered construction platforms in published designs.

You may also read, read-only: `space_processing_and_fabrication.md`, `moon_lagrange_and_comparables.md`, `leo_and_orbital_habitats.md` (sections D6 and D7).

---

## 7. `research/leo_logistics_power_and_utilities.md`

TOPIC: supplying, fueling and powering a settled LEO.

Checklist:
1. Propellant depots: cryogenic storage and boil-off, transfer demonstrations, and depot studies.
2. Orbital transfer vehicles and tugs, docking and berthing standards (the International Docking System Standard), rendezvous phasing, and traffic management practice.
3. Tethers and momentum exchange in LEO: demonstrations and studies (the open thread in `leo_and_orbital_habitats.md` section 8).
4. Power at scale: large solar arrays, nuclear power in Earth orbit and the 1992 UN Principles on nuclear power sources, and published megawatt-class LEO power concepts.
5. Space-based solar power beamed to the ground: demonstrations (Caltech SSPD-1 and others) and studies (ESA SOLARIS, JAXA), with efficiency, beam size, receiver size and the effect of a high-latitude receiver.
6. Water, air and food resupply mass for a large orbital population, as published in station-logistics studies (ISS resupply figures as the measured baseline).

You may also read, read-only: `life_support_lowg_power_structures.md`, `space_trucking_and_transport_infrastructure.md`, `waste_heat_utilization.md`.

---

## 8. `research/moving_large_populations_to_orbit.md`

TOPIC: what it takes to move millions of people, and the cargo they need, from Earth's surface to LEO.

Checklist:
1. Launch cadence: records per vehicle and per year, published projections for fully reusable vehicles, and the turnaround times that limit them.
2. Energy and propellant per kilogram and per person to LEO, for rockets and for published non-rocket launch concepts.
3. Passenger vehicles: published crew and passenger capacities, and the cost per seat.
4. Ordinary passengers: g-loads, medical screening and outcomes from commercial suborbital and orbital flights so far.
5. Throughput arithmetic: the launch rate, propellant and energy needed to move 1, 5 and 10 million people (plus a stated cargo allowance per person) in 10, 25 and 50 years. Show the arithmetic.
6. Atmospheric and environmental effects of very high launch rates (soot, alumina, ozone), with sourced figures.

You may also read, read-only: `industrial_ramp_timelines.md`, `gap_retry_leo_human_machines_power.md` (section F), `canon_vs_physics_comparison.md`.

---

## 9. `research/leo_as_gateway_to_mars.md`

TOPIC: LEO as the assembly and departure point for travel to Mars.

Checklist:
1. Mars architectures staged from Earth orbit: NASA Design Reference Architecture 5.0, SpaceX Starship refilling (the number of tanker flights per departure), and others, with their aggregation orbits (LEO, high Earth orbit, near-rectilinear halo orbit) and why each was chosen.
2. Departure from LEO: C3 and delta-v by launch window, and the cost of departing from a polar or high-inclination orbit (aligning the departure asymptote with the orbital plane, waiting times, plane-change penalties).
3. Assembly in LEO versus higher orbits: the trade in drag, debris, radiation and delta-v.
4. Return and capture at Earth: aerocapture into LEO, propulsive capture, and published return-vehicle designs.
5. Mars orbital infrastructure as the mirror of LEO: areostationary orbit, Phobos and Deimos as stations, and Mars-orbit depots, with what `mars_venus_and_transfer.md` already holds left uncopied.

You may also read, read-only: `mars_venus_and_transfer.md`, `cyclers_and_large_slow_vehicles.md`, `inner_system_logistics_network.md`, `gap_retry_leo_human_machines_power.md` (section I).

---

## 10. `research/gap_retry_leo_tranche9.md`

TOPIC: close the open threads left by the first LEO research, from primary sources.

Checklist: work through `DEFERRED_RESEARCH.md` Batch 1 and section 8 of `leo_and_orbital_habitats.md`. In order:
1. Radiation dose at 600 km versus 400 km.
2. ORDEM 3.x fluxes.
3. ISS reboost propellant and decay rates from a NASA primary.
4. Sustained artificial-gravity data on humans.
5. NASA SP-413's appendices and SP-428.
6. Primary texts for the von Braun wheel (Collier's, 1952) and Noordung (1928).
7. 2024-2026 launch costs per kilogram.

For each item, record what was closed, what is still open, and why.

You may also read, read-only: `leo_and_orbital_habitats.md`, `gap_retry_leo_human_machines_power.md`, `DEFERRED_RESEARCH.md`.

---

## Resume procedure
1. For each section, check whether its output file exists and whether its last sections (Open threads, Rejected sources) are written.
2. Re-dispatch any unfinished section with the one-line prompt above. The agent continues from its SEARCH LOG.
3. When all are done, append their open threads to `DEFERRED_RESEARCH.md` as new batches. Then write a short synthesis, `leo_infrastructure_synthesis.md`, in the style of `starlifting_synthesis.md`.
