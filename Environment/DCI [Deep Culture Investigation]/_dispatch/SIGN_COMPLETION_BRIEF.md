# Brief: complete one sign's avenue file

Saved 2026-11-10 for the run that starts at 5:03 a.m. on 2026-11-11 (author's request: "go through one Zodiac sign at a time, and think in as much depth and detail as you require, and populate each associated file with the relevant associated data and subtopics"). One agent per sign, one sign at a time, in order. Progress is tracked in `_dispatch/SIGN_COMPLETION_PROGRESS.md`.

**Paths:** `<DM>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/DCI [Deep Culture Investigation]`. Your file: `<DM>/Shared/Avenues/NN - <Sign>.md`. Edit only that file. No git, no web search; work from your own knowledge, marking anything uncertain *(check)*.

**Read first:**
1. **The model:** `<DM>/Shared/Avenues/01 - Aries.md`. Look especially at its "Source types" blocks: their ten tiers, their depth, and their plain style.
2. `<DM>/Shared/Investigation_Sheet.md`, Part B: the families of angles, including the six newer ones (B4 the senses; B6 space, place and things; B7 time and rhythm; B11 the economy of the concept; B13 conflict, violence and crisis; B19 margins and extremes).
3. `<DM>/Shared/Source_Types.md`: the catalog of kinds of sources.
4. Your whole sign file.

**The job: bring your sign's file to full depth.**
1. **Source types** (skip if your sign is Aries, which has them, except that Aries's domain and its concepts 1, 3 and 8 lack the *Organizations* tier: add that tier there, with no law in it):
   - Add a "**Source types**" block to section 0 (the domain) and to every concept, placed just before "**Key questions:**".
   - Use exactly Aries's header line and its ten tiers, in order: *Everywhere; Writing; Public records; Mass media; Online; Commerce; Organizations; The people who handle it; Outsiders; Scholarship and data.*
   - These are **types** of sources, not titles. Specific sources are chosen only when a particular culture is researched.
   - **Favor types that exist as widely as possible,** in every culture, with or without writing.
   - Think hard and widely, aiming at Aries's depth: about 50 to 70 types per concept. Include the less obvious ones: who handles the concept every day, what people pay for, children's own culture, objects, sounds, rituals, what outsiders record.
2. **The six newer families** (all twelve signs, Aries included):
   - Add six headings to every concept, after "**Change:**" and before the source types: **The senses; Space, place and things; Time and rhythm; The economy of it; Conflict and crisis; Margins and extremes.**
   - Fill each with concrete avenues for that concept, as the investigation sheet describes the family.
   - Where nothing distinct exists, write one honest-null line saying what was looked for.
3. **Explore the possibilities for the subtopics** (author, 2026-11-10: "One sign, explore possibilities for the subtopics, go in as much depth and detail as you need").
   - Add a section at the end of the file, before any duplicates section: "## Candidate subtopics (PROPOSED, for the author to settle)".
   - In it, explore every subtopic this meta-category could hold beyond its current concepts:
     - the sign's traditional areas that have no concept yet;
     - concepts in the sign's own research material (the Robot Fundamental Concepts folder for the sign: `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Robot_Fundamental_Concepts/01 - The twelve meta-categories/`);
     - the Tier 2 and near-synonym groups in `<DM>/Shared/Concept_Lists_by_Sign.md`;
     - concepts other cultures name that English lacks;
     - splits and merges of the current concepts.
   - For each candidate, give:
     - a working definition;
     - why it belongs in this sign, and any other sign it could belong to;
     - what it would add that the current concepts don't;
     - a few avenues for researching it.
   - Mark them all PROPOSED. Don't change the settled concept list or turn candidates into full sections; the author settles each list.

**Rules:**
- **Law:**
  - DCI is a full cultural investigation, not an investigation of laws.
  - Law is researched **only in Libra** (the letter of the law) **and Capricorn** (the spirit of the law).
  - In every other sign, add nothing about law: no statutes, courts, legal cases, legal doctrines, police, prisons or legal status.
  - In Libra and Capricorn, law-related source types and avenues belong in the law sections and the concepts tied to law.
- **Wording and rules carried over from the earlier work:**
  - American English. Plain, short sentences.
  - Native, Indigenous or Aboriginal, never "Indian", in your own words. Published titles and names keep their wording.
  - No South Asian works, scholars, datasets or communities.
  - Indigenous ceremonies, stories and practices only as the nations themselves share them.
  - No stereotypes: frame group differences as questions to research.
- **What not to touch:**
  - Research only, up to the present day: nothing in-world, nothing after 2026. AI and robots appear only as present-day human attitudes.
  - The signs are research classifiers only. No astrology as evidence or avenue.
  - Keep the file's structure: the STATUS line first, every existing heading, every *(check)* mark. Never remove existing content, and leave no notes about what was changed.
- **When finished,** set the STATUS line to `STATUS: draft v1 (2026-11-11), for the author to review.`

**Order of the three parts:** source types, the six families, then the candidate subtopics. Work through one concept at a time in the first two.

**Logging and resuming** (author, 2026-11-10: keep logs of everything, so that a cutoff mid-run loses nothing and the work picks up where it stopped):
- **Your log** is `<DM>/_dispatch/sign_completion_logs/NN - <Sign>.log.md`. Read it before anything else. Your file's state before the run is saved at `<DM>/_dispatch/sign_completion_logs/before/NN - <Sign>.md`. Never edit the backup.
- **If the log already has checkpoints, you are resuming.**
  - Open your sign file at the point after the last checkpoint.
  - Look at the next step: a block may be half written. For example, a Source types block may have fewer than ten tiers, or only some of the six headings may be there. Finish it in place rather than starting it again.
  - Never add a block, heading or candidate that is already in the file.
  - The log and the file are the record. If your memory of earlier work disagrees with them, trust them. The same holds if your context was compacted.
- **When you start,** set the file's first line to `STATUS: in progress (sign-completion run, 2026-11-11); log: _dispatch/sign_completion_logs/NN - <Sign>.log.md`.
- **Save as you go, never all at the end.**
  - Edit the file one concept at a time; each edit saves it.
  - After each step, append a dated checkpoint line to the end of the log (its last section, "Checkpoints and notes") with Bash, for example:
    `printf -- '- %s %s\n' "$(date '+%Y-%m-%d %H:%M')" "source types: 3. Autonomy done (about 60 types)" >> "<log path>"`
  - The steps are:
    - the domain's source types;
    - each concept's source types;
    - each concept's six families;
    - every two or three candidate subtopics, naming them;
    - the candidate section complete;
    - STATUS set.
- **Notes as you go.** Whenever you notice something the report will need, append it to the log at once, as a dated line starting `NOTE:`: a thin heading, a question for the author, a running count of new *(check)* marks. A cutoff then loses none of it.
- **When finished:**
  1. Write the full report (below) into the log's "Report" section, replacing its placeholder line.
  2. Set the STATUS line to `STATUS: draft v1 (2026-11-11), for the author to review.`
  3. Append the checkpoint "finished".
  4. Return the same report as your final message.

**Report back:**
- Concepts done.
- The candidate subtopics proposed, listed by name.
- Source types added per concept (rough count).
- Any heading that came out thin.
- Questions for the author.
- The number of new *(check)* marks.
