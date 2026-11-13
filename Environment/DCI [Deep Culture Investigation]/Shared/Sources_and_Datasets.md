# DCI source registry

STATUS: starting list, 2026-11-02. **Coverage, years and access are to be verified** the first time each source is used (in the pilot's Stage 1 and Stage 2), then recorded here. Add sources as they turn up.

**Kinds of evidence** (tag every claim): **measured** (surveys, experiments, census), **official** (government publications, lists, registers and records), **scholarly** (peer-reviewed or academic work), **synthesis** (well-sourced books for general readers that build on scholarship, such as Woodard's), **classic** (works that have lasted, fiction and non-fiction), **practitioner** (guides, journalism, encyclopedias, think-tank measures), **claim** (unsupported or single-source).

**Tagging conventions** (from the pilot, 2026-11-03):
- **A file's own reading** (a placement on a scale, a summary of a table, an inference across sources) is tagged **[synthesis: this file]**, so it can't be mistaken for a source's claim.
- **A measure reported by the press** keeps its tag (measured) with the read mark *(via the press)*.
- **A government's advocacy material** (a governor's fact sheet, a campaign page) is official in origin but not neutral: tag it official and say so.

**Rules:** no South Asian works; short quotations only; raw datasets stay out of git (record the values with citations instead).

## A. Measured, across countries
| Source | What it measures | Concepts and signs | Level | Access |
|---|---|---|---|---|
| Global Preferences Survey (Falk et al. 2018) | patience, risk-taking, positive and negative reciprocity, altruism, trust | Libra, Scorpio, Aries, Pisces | country (some regional) | free |
| World Values Survey / European Values Study | trust, religion, the importance of work, family, friends and leisure, child-rearing values, tolerance | most signs | country, some regions | free with registration |
| Hofstede's dimensions | power distance, individualism, masculinity, uncertainty avoidance, long-term orientation, indulgence | Capricorn, Aquarius, Aries, Pisces, Leo | country | free summaries |
| GLOBE study | power distance, performance orientation, assertiveness, humane orientation, in-group and institutional collectivism, future orientation, gender egalitarianism, uncertainty avoidance | Capricorn, Aries, Cancer, Aquarius | country (societies) | published |
| Gelfand's tightness-looseness | the strength of norms and tolerance of deviance | Capricorn, Virgo, Pisces | country | published |
| Moral Foundations data | care, fairness, loyalty, authority, sanctity, liberty | Cancer, Libra, Aquarius, Capricorn, Sagittarius | country (online samples) | published |
| Trompenaars' dimensions | universal rules against personal ties; achievement against ascribed status | Libra, Capricorn, Leo | country | published |
| Honor, dignity and face research | honor, pride, face, dignity | Leo, Aries | country and region | published |
| Emotion display-rule studies (Matsumoto) | when anger, fear and joy may be shown | Aries, Pisces, Leo | country | published |
| Rule-of-law and corruption indexes (World Justice Project; Transparency International) | the rule of law and corruption, as measured | Libra, Pisces, Capricorn | country | free |
| Regional barometers (AmericasBarometer, Latinobarómetro, Afrobarometer, Asian Barometer, Arab Barometer, Eurobarometer, European Social Survey) | trust, democracy, religion, corruption, values | many | country, often regions | mostly free |

**More candidates worldwide** (added 2026-11-10 from the review of the investigation sheet; access not yet checked):
- **Values:** the International Social Survey Programme (modules on national identity, work, the role of government, leisure and sport: the largest gap in this registry); Schwartz's values (in the European Social Survey and the WVS), which measure autonomy directly; the Inglehart-Welzel map and emancipative values.
- **Below the country, for many countries:** IPUMS International (census microdata with regional geography); DHS and MICS surveys (regions; women's say in household decisions); the Global Data Lab's subnational Human Development Index; OECD Regional Well-Being; IHME's Global Burden of Disease (subnational).
- **Emotion, risk and flourishing:** the Gallup World Poll and its Global Emotions report; the Lloyd's Register Foundation World Risk Poll; the Wellcome Global Monitor; the Global Flourishing Study.
- **Entrepreneurship and youth:** the Global Entrepreneurship Monitor (fear of failure); PISA 2018 (competitiveness, fear of failure); HBSC; the WHO's Global School-based Student Health Survey.
- **Crises:** the Oxford COVID-19 Government Response Tracker; Google's COVID-19 Community Mobility Reports (2020-2022).
- **Politics and events:** the Manifesto Project (party programs); GDELT; ACLED.
- **Time use:** the Multinational Time Use Study; HETUS (Europe).
- **Regional general social surveys:** the EBRD's Life in Transition Survey; the East Asian Social Survey and the Chinese, Japanese and Korean general social surveys; RLMS-HSE and the Levada Center (Russia).
- **Ethnographic and language codes:** D-PLACE (with the Standard Cross-Cultural Sample codes, including Barry, Child and Bacon, 1959, on training children for self-reliance against obedience); the Human Relations Area Files; WALS, Grambank, Glottolog.
- **Names and places:** OpenStreetMap street names (whom streets honor).
- **Image and robots:** the Anholt-Ipsos Nation Brands Index (commercial); Special Eurobarometers 382 and 460 on robots and automation.
- **Social ties:** Meta's Social Connectedness Index (worldwide).

## B. Measured, below the country
**Access note (2026-11-02):** the U.S. Census Bureau's API now requires a key; the Population Estimates (vintage) county files download without one.

| Source | What it measures | Level |
|---|---|---|
| Frontier-experience data (Bazzi, Fiszbein and Gebresilasse 2020) | years of frontier exposure; individualism measures | U.S. county |
| Rentfrow et al. 2013 | Big Five personality; three psychological regions | U.S. state |
| Harrington and Gelfand 2014 | tightness-looseness | U.S. state |
| Vandello and Cohen 1999 | collectivism | U.S. state |
| Elazar's political cultures | moralistic, individualistic, traditionalistic | U.S. state and substate |
| National censuses (U.S. Census Bureau, Statistics Canada, INEGI and others) | religion, language, ancestry, Indigenous identity, household structure | county, census division, *municipio* |
| European Quality of Government Index; European Social Survey regional data | trust, institutions, values | European region |
| Statements of Vote (state election offices) and provincial and Mexican electoral returns | county results on ballot measures and elections: how each unit's **electorate** votes | U.S. county; electoral district |

## C. Lineage sources (Stage 1)
| Profile | Sources |
|---|---|
| Family system | Emmanuel Todd, *The Explanation of Ideology* and later work |
| Kinship intensity | Murdock's *Ethnographic Atlas* (in D-PLACE); Schulz et al. 2019 (kinship intensity); Henrich, *The WEIRDest People in the World* |
| Religious lineage | ARDA; Pew Research Center; the World Religion Database (subscription); census religion tables |
| Subsistence | D-PLACE (subsistence codes by society); Nisbett and Cohen, *Culture of Honor*; Talhelm et al. 2014; Bazzi, Fiszbein and Gebresilasse 2020; Alesina, Giuliano and Nunn 2013 |
| Land and inheritance | land-tenure histories and records |
| Political culture | Elazar; Woodard, *American Nations* and *American Character* |
| Education | national education-system histories |
| Language | the World Loanword Database; etymological dictionaries; CLICS (colexification); Jackson et al. 2019 (emotion words across languages) |
| Stories | the Aarne-Thompson-Uther tale-type index; Thompson, *Motif-Index of Folk-Literature*; Berezkin's mythological motif catalog |
| Song | Lomax's Cantometrics (the Global Jukebox) |
| Formative events | the persistence literature, for example Dell 2010 (the mining *mita*), Nunn and Wantchekon 2011 (the slave trade and mistrust), Guiso, Sapienza and Zingales 2016 (Italian free cities and civic capital) |

## D. Qualitative sources (Stage 4)
| Kind | What to look for |
|---|---|
| The language | native words for the concept; untranslatables; proverb collections. Search in the language, not only in English. |
| The culture's own classics and scholarship | canonical texts the culture has written about itself; the national interpretive canon |
| Ethnography | the Human Relations Area Files (eHRAF; subscription), searched by Outline of Cultural Materials category (the outline itself is free) |
| Folkways | Fischer, *Albion's Seed*, and its equivalents for other regions |
| Practitioner guides | country culture guides; used last, tagged practitioner |

## E. Law: only for the concepts directly about law
**Used only in the law research of Libra and Capricorn** (author, 2026-11-10: research into law happens only in the meta-category subsections directly related to law). **Libra takes the letter of the law** (the legal system, what the law says, and the left-right readings of the law: `Shared/Avenues/07 - Libra.md`, section 0); **Capricorn takes its spirit** (legal culture: `Shared/Avenues/10 - Capricorn.md`, section 8). The author's measures of left and right and of authoritarian and libertarian have their own sections, G and H.

**What a place's law is based on, and how its people view law:**

| Kind | Sources |
|---|---|
| Legal system | JuriGlobe (University of Ottawa); the legal-origins datasets (La Porta, Lopez-de-Silanes and Shleifer); GlobaLex; the Library of Congress Guide to Law Online; the Constitute Project; Merryman, *The Civil Law Tradition*; Zweigert and Kötz, *An Introduction to Comparative Law*; Watson, *Legal Transplants* |
| Legal culture | Friedman's work on legal culture (*The Legal System: A Social Science Perspective*); Tyler, *Why People Obey the Law*; Woodard, *American Nations* and *American Character*; Elazar; Nisbett and Cohen, *Culture of Honor*; surveys of trust in courts and police (WVS, Gallup, national surveys) |
| Law and institutions | constitutions, criminal codes, family law |

**Tagging:** **A ruling or statute known only from a secondary page** keeps its tag (official) with the read mark *(search summary)* or *(via <the page>)*.

**What a state, province or country does with its law:** **Several come from think tanks with a declared orientation** (marked below): tag them practitioner, and check them against the academic measures and the laws themselves.

| Source | What it measures | Level |
|---|---|---|
| Caughey and Warshaw, policy liberalism in the American states | the left-right position of state policy, over time | U.S. state |
| Correlates of State Policy Project (Michigan State University) | hundreds of policy variables by state and year | U.S. state |
| Ruger and Sorens, *Freedom in the 50 States* (Cato Institute; libertarian) | fiscal, regulatory and personal freedom | U.S. state |
| *Economic Freedom of North America* (Fraser Institute; free-market) | economic freedom on one scale across the U.S., Canada and Mexico | U.S. state, Canadian province, Mexican state |
| State RegData (Mercatus Center; free-market) | the volume of regulation | U.S. state |
| RAND State Firearm Law Database | gun laws | U.S. state |
| Death Penalty Information Center | the death penalty: status and use | U.S. state |
| Bureau of Justice Statistics; Statistics Canada; INEGI | incarceration, sentencing, policing, victimization | state, province |
| World Justice Project, Mexico States Rule of Law Index | the rule of law | Mexican state |
| Cooperative Election Study; Gallup | public opinion and ideology | U.S. state |
| OECD Revenue Statistics and similar cross-national series | tax and spending levels, for reading a **national layer** against comparable democracies | country |

**Coverage (pilot, 2026-11-03):** the academic state-policy measures (Caughey and Warshaw, the Correlates of State Policy Project) cover U.S. states only, and they can't score a federal layer. For Canadian provinces and Mexican states only EFNA (practitioner), Statistics Canada, INEGI and the World Justice Project index were found, so the check of think-tank measures against academic ones can't yet be met there; check the laws themselves instead.

## F. Access notes (verified in the pilot, 2026-11-03)
- **The web-search cap is per session** (1,000 searches by default), shared by every agent running in it. Size waves to what's left; when it runs out, fetch known primary pages directly (this worked well for statutes and constitutions).
- **Caughey and Warshaw:** replication files on Harvard Dataverse (1936-2014); the Correlates of State Policy Project's core file carries their scores to 2014, with EFNA. Ranks have to be computed from the files (the book gives no per-state numbers). The 1936-2020 update sits behind a web app that agents couldn't reach.
- **Blocked for automated reading:** Cato (*Freedom in the 50 States*), the Fraser Institute (EFNA; third-party copies were readable), California's legislative code site, Alaska's dry-and-damp community list. Download these by hand if they're needed.
- **Certificate failures:** the Baja California Sur Congress (cbcs.gob.mx) and the BC courts' judgment site (bccourts.ca). Use another host (for BC rulings, CanLII; for Mexican state law, the federal legal compilations; check).
- **Good routes:** the U.S. Code at Cornell's LII; Alaska statutes through the legislature's print view; the Alaska Constitution through Wikisource (the official page sits behind a CAPTCHA); Mexico's consolidated constitution from the Chamber of Deputies; Baja California's Congress site; Statistics Canada's downloadable tables.
- **Discontinued:** the CIA World Factbook (February 4, 2026).

## G. The author's measure of left and right: government spending as a share of GDP (author, 2026-11-10)
**Interpreted in Taurus's ownership** (`Shared/Avenues/02 - Taurus.md`, section 2; author, 2026-11-10): who owns what a society produces. The numbers are collected at Stage 2.
**Where an area sits on the economic left-right axis is measured by how much of its GDP its government spends:** the government's total expenditure divided by the area's GDP, as a percentage. **0% is the far right** (anarchy: a government that owns nothing can't exist); **100% is the far left** (communism: the government owns everything that is produced). The arithmetic is the same at every level: a country's government against the country's GDP, California's state government against California's GDP, the City of Los Angeles's government against Los Angeles's GDP. Unlike the academic measures, it can be computed for every jurisdiction in every country. Tag it [measured: the author's measure], citing both the spending and the GDP source. **It is the headline figure for the economic left-right reading** (author, 2026-11-10); other measures stand beside it, and where they disagree with it, the disagreement is recorded, not resolved.

**How to compute it** (author, 2026-11-10):
- **Two figures.** (1) **Own level,** as the author defined it: one government's spending against its own area's GDP, compared only with governments at the same level in the same country, because countries split jobs between levels differently (Canada's provinces run health care; U.S. states don't run Medicare). (2) **All levels:** every government spending in the area (national, state or province, local) against the area's GDP. This is the figure that can be compared across countries, and the pre-war baseline for a successor nation's government at Stage 6.
- **Money passed between levels is counted once,** by the government that finally spends it (a federal grant spent by a state counts as the state's), so the all-levels figure doesn't double-count.
- **Spending means total expenditure,** payments to people (pensions, welfare) included, as the author's "total expenditures" says. Record the year and whether the figure is budgeted or actual.
- **Where an area's GDP isn't published** (most cities), use the smallest area that is (the county or metropolitan area), and say so.
- **Where the data are** (access not yet checked): U.S., the BEA's GDP by state, county and metropolitan area, and the Census Bureau's Annual Survey of State and Local Government Finances; Canada, Statistics Canada's GDP by province and by census metropolitan area, and its government finance statistics; Mexico, INEGI's GDP by state and its state and municipal public finance statistics (EFIPEM); national layers, the IMF's and the OECD's general-government expenditure series.

## H. The author's measures of authoritarian and libertarian (author, 2026-11-10)
**Interpreted in Capricorn's authority** (`Shared/Avenues/10 - Capricorn.md`, section 1; author, 2026-11-10); the numbers are collected at Stage 2. The permission share is scored by reading the law in force, as Libra's letter-of-the-law research does.

The second axis is measured the same way: simple arithmetic, the same answer whoever counts. The template defines the axis as how far the law reaches into an area and how hard it is enforced, so there are two measures, one for each.
- **Headline: the permission share** (how far the law reaches). Of a fixed list of activities, the share the law forbids (1) or requires permission for (½), averaged over the eight Part B domains. 0% is the far libertarian end, 100% the far authoritarian end. The list, the scoring and its rules are in `Shared/Permission_Share_List.md`. It is given twice, like the spending measure: own level and all levels. Tag it [measured: the author's measure], citing the laws scored.
- **Companion: the correctional-control share** (how hard the law is enforced). Adults in prison, in jail, on probation or on parole, as a share of all adults; each person counted once. 0% means the state punishes no one; 100% means every adult is under its control. It also rises with crime, not only with harsh law, so it stands beside the headline and doesn't replace it. Where the data are (access not yet checked): U.S., the Bureau of Justice Statistics (prisons, jails, probation and parole, by state; county jail figures in the Vera Institute's incarceration trends); Canada, Statistics Canada's adult correctional statistics (custody and community supervision, by province); Mexico, INEGI's national census of the prison system (by state), with community supervision to be found.
