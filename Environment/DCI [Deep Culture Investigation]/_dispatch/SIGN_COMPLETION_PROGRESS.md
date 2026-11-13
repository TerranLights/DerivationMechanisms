# Sign completion: progress

STATUS: done 2026-11-11; final report given to the author.

**Start here after any cutoff.** From the method folder, run `python3 _dispatch/qa_sign.py --all`, then follow "Resuming after a cutoff" below. Everything the run needs is on disk: this file, the brief, one log per sign, and a copy of every sign file from before the run.

**What this is.**
- The author's request (2026-11-10): "go through one Zodiac sign at a time, and think in as much depth and detail as you require, and populate each associated file with the relevant associated data and subtopics."
- Confirmed: "One sign, explore possibilities for the subtopics, go in as much depth and detail as you need. Then, continue with the next Zodiac sign, one at a time."
- And: "keep logs of everything so that, in case you get cut off during the process, you can pick up where you left off when the window/week resets."

Each sign gets three things:
- source types (Aries already has them);
- the six newer families;
- a section headed "Candidate subtopics (PROPOSED)".

The job and its rules are in `_dispatch/SIGN_COMPLETION_BRIEF.md`. This is research for the method, not derivation, so the run may continue past 14:59.

## Where things are

| What | Where |
|---|---|
| The job and its rules | `_dispatch/SIGN_COMPLETION_BRIEF.md` |
| The sign table, the procedure, the saved prompts and the run log | this file |
| Each sign's log: the agent's checkpoints and notes, its report, the QA | `_dispatch/sign_completion_logs/NN - <Sign>.log.md` |
| Every sign file as it was before the run | `_dispatch/sign_completion_logs/before/NN - <Sign>.md`, taken 2026-11-11 at 00:40. Never edited. The QA compares against it. |
| Check script | `_dispatch/qa_sign.py`. Pass `"NN - <Sign>"` for one sign, or `--all` for the status of all twelve. |
| Session timers (gone if the session closes) | The 5:03 a.m. start (job 408688a1), which runs once. An hourly watchdog at :37 (job f13acbae) resumes the run after a cutoff; it expires on 2026-11-18. |

**The run agent (since 2026-11-11, 09:06).** The 5:03 start never reached the main session while the author slept. It arrived only at 09:03, when a key was pressed. So the whole run is now driven by one background **run agent**, started with the run-agent prompt below. It works the signs one at a time and goes from one to the next by itself, without waiting on the main session. It follows "How the run works" and records everything here and in the sign logs. Its ID is in the run log.
- While the run agent is running, neither the main session nor the watchdog launches anything.
- If the run agent stops before Pisces is done, start a new run agent with the same prompt. It picks up from the table and the logs.

## The signs

| # | Sign | Status | Agent |
|---|---|---|---|
| 1 | Aries | done 2026-11-11 09:25: 10 concepts, six families added to all; Organizations tier added to the domain and concepts 1, 3, 8 (about 15 types each); 36 candidates (C1-C36); thin: Initiative's senses, senses generally thinnest; 5 questions (old "police" memorial line, families for the domain, C9 manhood, splits C27-C36, homes for C7/C17/C35); 27 new *check* | run agent (sub-agent a09f50fd1b9d7a0e6) |
| 2 | Taurus | done 2026-11-11 09:55: 10 concepts; source types added to the domain (~149) and every concept (~67-96 each); six families in all; 46 candidates (C1-C46); thin: the senses (Ownership, Stability, Stubbornness), economy (Possessiveness, Stubbornness); 8 questions (concept list still unsettled, old law-word lines and deed lines, families for the domain, C39 Providing, homes for C3/C4/C18/C36/C2, splits C35-C46, long blocks); 36 new *check* | run agent (sub-agent af3c447ceac30e87f) |
| 3 | Gemini | done 2026-11-11 10:23: 9 concepts; source types added to the domain (~150) and every concept (~67-111 each); six families in all; 48 candidates (C1-C48); thin: the senses (Siblings shortest; Mediation, Gossip moderate); 9 questions (concept list unsettled, older law-leaning lines, families for the domain, overlaps incl. C7 = Aries C7, Neighbors/journeys/Language/Childhood as concepts, splits C35-C48, long blocks, an entry for male readers, many cautious *check*); 79 new *check* | run agent (sub-agent aebb2ca4e2d288e18) |
| 4 | Cancer | done 2026-11-11 10:51: 9 concepts; source types added to the domain (~150) and every concept (about 85-100 types each); six families in all; 46 candidates (C1-C46); thin: the senses (Shelter, Abandonment shortest); 8 questions (concept list unsettled, overlaps with Taurus/Gemini/Aries candidates, older law-leaning lines, families for the domain, long blocks, entries for male readers incl. C1 Fatherhood, splits and merges C31-C46, cautious *check*); 50 new *check* | run agent (sub-agent a7ba48f3afe9303bc) |
| 5 | Leo | done 2026-11-11 11:22: 12 concepts; source types added to the domain and every concept (about 70-80 types each); six families in all; 54 candidates (C1-C54); thin: the senses (Recognition, Being seen shortest); 8 questions (concept list unsettled, overlaps with earlier signs' candidates, older law-leaning lines, families for the domain, long blocks, entries for male readers, splits C36-C51 and merges C52-C54, cautious *check*); 32 new *check* | run agent (sub-agent a9657dafed91be504) |
| 6 | Virgo | done 2026-11-11 11:58: 9 concepts; source types added to the domain (~150) and every concept (about 65-75 types each); six families in all; 65 candidates (C1-C65); thin: the senses (Usefulness, Improvement shortest); 8 questions (concept list unsettled, household order C4 here or Capricorn, overlaps with earlier signs' candidates, older law-leaning lines, families for the domain, 65 candidates to trim or not, entries for male readers, many cautious *check*); 81 new *check* | run agent (sub-agent a92530c8e9cb626b0) |
| 7 | Libra | done 2026-11-11 12:34: 10 concepts; source types added to the domain (cultural block ~150, plus a letter-of-the-law block ~110) and every concept (about 65-75 types each); six families in all; 58 candidates (C1-C58); law kept to the law sub-section and the concepts tied to law, spirit of the law pointed to Capricorn; thin: the senses (Indecision, Projection shortest); 9 questions (concept list unsettled, one or two domain blocks, letter-spirit candidates C8/C9/C16/C34/C35/C37/C38/C54, older spirit-leaning lines, families for the domain, overlaps, C20 vs C58, entries for male readers, *check* marks); 67 new *check* | run agent (sub-agent a96689bedd349dc26) |
| 8 | Scorpio | done 2026-11-11 13:10: 10 concepts; source types added to the domain (~150) and every concept (about 75-95 types each); six families in all; 60 candidates (C1-C60); spirit of the law pointed to Capricorn in routing lines only; thin: the senses (Betrayal, Revenge shortest); 8 questions (concept list unsettled incl. loyalty/privacy/grief, homes for inheritance/privacy/loyalty, older law-leaning lines, families for the domain, trim 60 candidates, depth of sensitive entries C12/C17/C35/C36, confirm two exclusions, cautious *check*); 70 new *check* | run agent (sub-agent a8202391e2a19edb7) |
| 9 | Sagittarius | done 2026-11-11 13:43: 10 concepts; source types added to the domain (~150) and every concept (about 60-80 types each); six families in all; 59 candidates (C1-C59); law kept to section 0's one-line pointer; thin: the senses (Belief, Conviction, Honesty shortest); 8 questions (concept list unsettled incl. religion/philosophy/pilgrimage, homes for ideas proposed in two signs, older law-leaning lines, families for the domain, trim 59 candidates, male-reader entries, confirm three exclusions incl. South Asian-origin traditions as a known gap, cautious *check*); 164 new *check* | run agent (sub-agent a8232a437ca2d7c1a) |
| 10 | Capricorn | done 2026-11-11 14:15: 9 concepts; source types added to the domain (~160) and every concept (about 65-100 types each, Law the largest); six families in all; 57 candidates (C1-C57); law kept to concept 8 and the enforcement side of Authority and Order, letter of the law pointed to Libra; thin: the senses (Responsibility, Merit), economy (Duty, Hierarchy lean on statistics); 8 questions (status and reputation vs Leo, the seven law splits C47-C53 incl. prison vs Pisces, duty and responsibility one or two, military life and war here or Aries, seniority, loyalty split, long blocks, male-reader lines); 89 new *check* | run agent (sub-agent a86138d3dd15ab1c4) |
| 11 | Aquarius | done 2026-11-11 14:52: 9 concepts; source types added to the domain and every concept (about 75-95 types each); six families in all; 52 candidates (C1-C52); thin: Detachment's economy, the senses for Idealism and Equality; 9 questions (the opening's three questions set out as merges C50-C52, detachment's home and three splits, the isolation/loneliness/solitude group vs Cancer, lines against nearby candidates, gangs C37 here or Capricorn, science and technology C7, long blocks, male-reader lines, keep or drop "Age of Aquarius"); 95 new *check* | run agent (sub-agent a9d586cafb083b25e) |
| 12 | Pisces | done 2026-11-11 15:34: 11 concepts; source types added to the domain (~135) and every concept (about 60-75 types each); six families in all; 69 candidates (C1-C69); crime kept to wrongdoing as culture, confinement through care and the cloister, prison left to Capricorn; thin: Intuition's and Empathy's time and rhythm, Surrender's senses, Intuition's public records; 9 questions (the opening's questions as merges C67-C69 and C51/C54/C55, confinement as one concept or C7-C10, magic ways as one concept or C16-C21, the wrongdoing splits C59-C64, the line with Virgo C58, trim 69 candidates, older law-leaning lines, 40 male-reader questions, source-type depth); 108 new *check* | run agent (sub-agent ab0f1e3acb0139615) |

Status values:
- `not started`
- `in progress (since <time>)`
- `agent finished, QA pending`
- `done <time>: <one-line note>`

## How the run works (the orchestrator)

For each sign, in order, start at the first one not marked done.

1. **Log the launch.** Append a dated line to the run log below: "<Sign>: launching".
2. **Launch the agent.**
   - Launch ONE general-purpose agent in the background, with the launch prompt below.
   - Write its agent ID in three places: the table, the sign log's "Run" section (`Agent: <id>, launched <time>`), and the run log.
   - Mark the sign `in progress (since <time>)`.
3. **Wait for the report.** Don't poll; a notification arrives when the agent finishes.
4. **When it reports back:**
   - Mark the sign `agent finished, QA pending`.
   - If the log's Report section is still empty, paste the agent's report there.
5. **Check it.**
   - Run `python3 _dispatch/qa_sign.py "NN - <Sign>"` and paste the output into the log's QA section.
   - The sign passes when:
     - every concept has its 23 headings, once each and in order;
     - every concept has a Source types block with all ten tiers;
     - the domain has a Source types block;
     - the candidate section is there;
     - no line from the pre-run copy is missing;
     - there is no law outside Libra and Capricorn;
     - "Indian" appears only in published titles;
     - there are no South Asian sources or communities;
     - spelling is American, except in proper names.
   - Fix small problems yourself.
   - For a big gap, send the agent back with SendMessage. Log every fix and every send-back.
6. **Close the sign.**
   - Mark it `done <time>: <concepts; source types added; thin spots; questions>`.
   - Add a run-log line, then start the next sign.
7. **After Pisces:**
   - Report to the author: what was added, sign by sign; the thin spots; every question collected in the logs.
   - Update `Targets/Cascadia/PROGRESS TRACKER.md` (CurrentNovelDocs `worldbuilding/Deep_Culture_Investigation/`) and the DCI memory file.
   - Delete the watchdog (CronList, then CronDelete).
   - Set this file's STATUS to done, and add a final run-log line saying the report was given.

## Resuming after a cutoff

A cutoff (the 5-hour window or the weekly limit) can stop the agent, the orchestrator, or both. The sign file is saved after every concept and the log after every step, so nothing is lost.

1. Run `python3 _dispatch/qa_sign.py --all`. Read the table and the run log here.
2. For the sign marked `in progress` or `agent finished, QA pending`:
   - **The log's last checkpoint is "finished"** (the Report is filled and the STATUS reads draft v1): the agent completed its job. Do steps 4 to 6 above.
   - **Same session:** use ListAgents.
     - If its agent is still running, wait.
     - If the agent has stopped, send it the resume message below with SendMessage, and log that.
   - **The agent can't be reached, or this is a new session:** launch a replacement with the replacement prompt below, and record its new agent ID.
3. **No sign is in progress, but some aren't done:** the run stopped between signs. Start the next sign at step 1 of "How the run works".
4. **The session closed:** the timers are gone.
   - In a new session, the author says "resume the DCI sign-completion run", and the orchestrator starts at the top of this file.
   - Create the watchdog again with its prompt below if it helps.

Rules for resuming:
- Never restart a sign from scratch.
- Never copy the pre-run file back over a partly done one.
- Never launch a second agent for a sign whose agent is running, or whose log says "finished".

## Prompts

`<DM>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/DCI [Deep Culture Investigation]`. Replace `NN - <Sign>` with the sign.

### Launch prompt (one agent per sign)

> Complete one sign's avenue file for the Deep Culture Investigation: **NN - <Sign>**.
>
> Method folder (`<DM>`): `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/DCI [Deep Culture Investigation]`.
>
> Follow `<DM>/_dispatch/SIGN_COMPLETION_BRIEF.md` exactly. Read all of it first.
> - Your sign file: `<DM>/Shared/Avenues/NN - <Sign>.md`.
> - Your log: `<DM>/_dispatch/sign_completion_logs/NN - <Sign>.log.md`. Read it before anything else. If it already has checkpoints, you are resuming; follow the brief's "Logging and resuming".
>
> Think in as much depth and detail as you need.
> - Edit only your sign file and your log.
> - No git, no web search.
> - Save the file after every concept, and log every step, so that a cutoff loses nothing.
>
> When finished:
> 1. Write your report into the log's Report section.
> 2. Set the STATUS line.
> 3. Log "finished".
> 4. Return the report.

### Resume message (SendMessage to a stopped agent)

> You were stopped partway, by a usage cutoff. Continue the same job.
> 1. Re-read your log (`<DM>/_dispatch/sign_completion_logs/NN - <Sign>.log.md`) and your sign file.
> 2. Carry on from the step after the last checkpoint, as the brief's "Logging and resuming" says.
>
> Finish any half-written block in place, and never add a block twice. Keep logging every step.

### Replacement prompt (a new agent, for a sign whose agent can't be reached)

The launch prompt, followed by:

> A previous agent did part of this job and was cut off.
> - Your log shows how far it got. Its checkpoints and the sign file are the record.
> - Pick up from the step after the last checkpoint.
> - Finish any half-written block in place.
> - Never add a block, heading or candidate twice.

### Run-agent prompt (one background agent drives the whole run)

> You are the run agent for the Deep Culture Investigation's sign-completion run. You drive the whole run yourself, one sign at a time, without waiting on anyone. The author is not at the keyboard.
>
> Method folder (`<DM>`): `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/DCI [Deep Culture Investigation]`.
>
> **Read first:**
> - `<DM>/_dispatch/SIGN_COMPLETION_PROGRESS.md`: the sign table, "How the run works", "Resuming after a cutoff", the prompts and the run log.
> - `<DM>/_dispatch/SIGN_COMPLETION_BRIEF.md`: the job and its rules.
>
> Then run `python3 "<DM>/_dispatch/qa_sign.py" --all`.
>
> **The run.** Work through the signs in order (Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces), starting at the first one not marked done. For each sign:
> 1. **Mark it.** Set the sign to `in progress (since <time>)` in the table, with your agent role in the Agent column ("run agent"). Add a dated run-log line.
> 2. **Do the sign's job.**
>    - If you have an Agent tool, launch ONE general-purpose sub-agent with the saved launch prompt (the replacement prompt if the sign's log already has checkpoints). Run it in the foreground and wait for it. Write its ID in the sign log's "Run" section and in the run log.
>    - If you have no Agent tool, do the job yourself, exactly as the brief says, as if you were that sign's agent. This includes its "Logging and resuming" rules: a checkpoint in the sign's log after every step, `NOTE:` lines, and the report in the log at the end.
>    - Either way, think in as much depth and detail as the job needs.
> 3. **Check it.**
>    - Run `python3 "<DM>/_dispatch/qa_sign.py" "NN - <Sign>"` and paste the output into the sign log's QA section.
>    - Apply the pass criteria in "How the run works", step 5.
>    - Fix small problems yourself. Finish any big gap before going on, by sending the sub-agent back or doing it yourself.
>    - Log every fix.
> 4. **Close it.** Mark the sign `done <time>: <concepts; source types added; thin spots; questions>`. Add a run-log line. Go straight on to the next sign.
>
> **Keep the record current.** The table, the run log and the sign logs must always show where the run stands. If your context gets compacted, re-read this file and the current sign's log before going on. They are the record.
>
> **At the end** (all twelve done):
> 1. Add a section "## Final report" to the progress file, just above "## Run log":
>    - what was added, sign by sign;
>    - the thin spots;
>    - every question for the author collected in the logs;
>    - the candidate subtopics proposed, by sign.
> 2. Set the file's STATUS to `done <date>; final report written, not yet given to the author`.
> 3. Add a run-log line.
> 4. Return the final report as your last message.
>
> **Rules (from the brief, and binding):**
> - DCI is a full cultural investigation, not an investigation of laws. Law lives only in Libra (the letter of the law) and Capricorn (the spirit of the law).
> - Relocate, never delete; never remove existing content from a sign file.
> - American English.
> - Native, Indigenous or Aboriginal, never "Indian", in your own words.
> - No South Asian works, scholars, datasets or communities.
> - Nothing in-world; research only.
> - The signs are research classifiers, never astrology.
> - Edit only:
>   - the twelve sign files in `<DM>/Shared/Avenues/` (not the two companion files);
>   - the sign logs;
>   - this progress file.
> - No git, no web search.

### Watchdog prompt (hourly session timer at :37)

> [DCI sign-completion watchdog, hourly. Set on 2026-11-11 because the author asked for logs, so that the run picks up where it left off after a cutoff.]
>
> Run `python3 "<DM>/_dispatch/qa_sign.py" --all` and read `<DM>/_dispatch/SIGN_COMPLETION_PROGRESS.md`. Then:
> 1. **Before 05:03 on 2026-11-11, with no sign started:** do nothing. Reply in one line.
> 2. **A sign is in progress and ListAgents shows its agent still running:** do nothing. Reply in one line.
> 3. **Otherwise, while any sign isn't done:** follow "Resuming after a cutoff" in the progress file, and record each step in its run log.
> 4. **All twelve are done:**
>    - If the run log shows the final report was given, delete this watchdog (CronList, then CronDelete) and reply in one line.
>    - If not, first do step 7 of "How the run works".

## Final report

Written 2026-11-11 by the run agent, after all twelve signs passed QA. Not yet given to the author.

**In short.** All twelve sign files are now at `STATUS: draft v1 (2026-11-11), for the author to review.`
- Every concept has the six newer families, placed after "Change". There are 118 concepts in all.
- Every concept and every domain section has a Source types block with Aries's ten tiers.
- Each file ends with a "Candidate subtopics (PROPOSED, for the author to settle)" section, closed by a "Considered and not proposed" line. The twelve sections hold 650 candidates.
- QA passed for every sign. No fix was needed. No line from any pre-run copy is missing, and no settled concept list was changed.
- Every hit on a law word, on "Indian" or on a British spelling was either already in the pre-run file or is a published name, a quotation or a line that points the reader to Libra or Capricorn. Each one is listed in that sign's QA section.
- No South Asian works, scholars, traditions or communities were added. No astrological terms were added. Nothing in-world was added.
- New *check* marks: 898 in all, mostly dates, studies and first-use claims cited from memory in the candidates.
- Only the twelve sign files, the twelve logs and this file were edited. The two companion law files and the pre-run copies are untouched.

### What was added, sign by sign

Type counts are each agent's own count of distinct types. The QA script's estimate runs higher, because it splits on every semicolon. Every concept got all six families, and no honest-null line was needed anywhere.

| Sign | Concepts | Source types added | Candidates | New *check* |
|---|---|---|---|---|
| Aries | 10 | Only the missing Organizations tier: domain about 16 types; concepts 1, 3 and 8 about 15 each. The other tiers predate the run. | 36 | 27 |
| Taurus | 10 | Domain about 150; concepts about 67 to 96 | 46 | 36 |
| Gemini | 9 | Domain about 150; concepts about 67 to 111 by the script | 48 | 79 |
| Cancer | 9 | Domain about 150; concepts about 85 to 100 | 46 | 50 |
| Leo | 12 | Domain about 150; concepts about 70 to 80 | 54 | 32 |
| Virgo | 9 | Domain about 150; concepts about 65 to 75 | 65 | 81 |
| Libra | 10 | Domain about 150, plus a block of about 110 legal types for the letter of the law; concepts about 65 to 75 | 58 | 67 |
| Scorpio | 10 | Domain about 150; concepts about 75 to 95 | 60 | 70 |
| Sagittarius | 10 | Domain about 150; concepts about 60 to 80 | 59 | 164 |
| Capricorn | 9 | Domain about 160; concepts about 65 to 100 (Law the largest) | 57 | 89 |
| Aquarius | 9 | Domain about 140; concepts about 75 to 95 | 52 | 95 |
| Pisces | 11 | Domain about 135; concepts about 60 to 75 | 69 | 108 |

How each sign handled law:
- **Law signs:**
  - In Libra, legal source types and avenues sit in section 0's letter-of-the-law sub-section and in the concepts the file already ties to law (justice, fairness, partnership, impartiality). The spirit of the law is pointed to Capricorn.
  - In Capricorn, law sits in concept 8 and in the enforcement side of authority and order. The letter of the law is pointed to Libra.
  - In both, custom still leads.
- **The other ten signs** add no law.
  - Property, money, speech, family, health, death, belief and reform are framed through custom, feeling, practice, the media and community.
  - Scorpio and Sagittarius add short lines that only point to Libra or Capricorn.
  - Pisces keeps its crime "Law:" line. It researches crime as the culture's idea of wrongdoing, and confinement through care and the cloister. Prison is left to Capricorn's C49.

### Thin spots

None needed an honest-null line. "The senses" is the thinnest family in every sign.
- **Aries:** Initiative's senses.
- **Taurus:**
  - the senses of Ownership, Stability and Stubbornness;
  - the economy of Possessiveness and Stubbornness.
- **Gemini:**
  - Siblings' senses (six items);
  - Mediation's and Gossip's senses are moderate;
  - Duality has the shortest source-type block (about 67).
- **Cancer:** the senses of Shelter and Abandonment (about seven items each).
- **Leo:** the senses of Recognition and Being seen (about seven items each).
- **Virgo:** the senses of Usefulness and Improvement (five or six items each).
- **Libra:** the senses of Indecision and Projection (seven or eight items each).
- **Scorpio:** the senses of Betrayal and Revenge (six or seven items each).
- **Sagittarius:** the senses of Belief, Conviction and Honesty (five or six items each).
- **Capricorn:**
  - the senses of Responsibility and Merit;
  - the economy of Duty and Hierarchy leans on statistics more than on lived practice.
- **Aquarius:**
  - Detachment's economy (the market for calm more than lived practice);
  - the senses of Idealism and Equality (Equality's leans partly on prejudices recorded).
- **Pisces:**
  - the time and rhythm of Intuition and Empathy;
  - Surrender's senses;
  - Intuition's Public records tier.

### Questions for the author

**A. Questions every sign, or most signs, asked:**
1. **Six families for the domain sections.** Should section 0 of each sign also get the six families? The brief said "every concept", so every agent added them to the concepts only.
2. **The concept lists are still unsettled.** No file's settled list or opening questions were touched. Each sign's candidates, the merges especially, are laid out to answer its opening questions. The sign-by-sign list below says which candidates bear on which question.
3. **Older lines that lean toward law, in the ten signs that are not about law.** Each sign's list is below. Keep them, reword them, or relocate them to the Libra or Capricorn companion files? They were left in place, because no existing content may be removed.
   - Aries and Pisces share one: "memorials to (fallen) firefighters and police".
   - The run agent judged that these memorial lines honor courage and are not research into law. The earlier law scrub kept lines like them.
4. **Splits and merges.** Should the split candidates become concepts, or stay facets of the current concepts? The merges are listed for decision only.
5. **Source-type depth.** Most blocks run above Aries's 50 to 70 types per concept, at about 60 to 100. Trim them, or keep them?
6. **Entries for male readers.** Each sign lists its entries, or its lines framed as questions with women's views alongside. Are they the right ones, and how many are wanted? The lists are below.
7. **The 898 new *check* marks.** Many are cautious. Keep them all, or clear the ones the author is sure of?
8. **One home for ideas proposed in more than one sign.** The main clusters:
   - directness: Aries C7 = Gemini C7;
   - childhood: Gemini C4 = Cancer C6, with Leo C3;
   - hospitality: Taurus C21 = Cancer C5;
   - roots and belonging to a place: Aries C29, Taurus C30, Cancer C3 and C28;
   - privacy: Gemini C26, Cancer C7, Scorpio C23;
   - loyalty: Taurus C18, Scorpio C22, Capricorn C16 (allegiance);
   - inheritance: Taurus C36, Scorpio C4;
   - status and reputation: Leo C41 and C25, Capricorn C2 and C3;
   - face: Leo C26, named by Gemini and Taurus;
   - providing and protecting: Taurus C39, Cancer C38, Aries C28;
   - fate and providence: Scorpio C45, Sagittarius C7;
   - loneliness and solitude: Cancer C23 and C18, Aquarius C19;
   - leisure: Taurus C14, Leo C49, Virgo C31;
   - forgiveness: Libra C26.
   
   Each candidate's "Also fits" line names the rest.

**B. Questions particular to each sign:**

- **Aries**
  1. The old line "memorials to firefighters and police" (Courage, Ritual) is the only law-word hit. Keep it, or reword it?
  2. Manhood ideals (C9): an Aries concept, or a lens across all signs (the investigation sheet's B3)?
  3. Homes:
     - C7 Directness: Aries or Gemini?
     - C17 Follow-through: Capricorn?
     - C35 Collective self-rule: Aquarius or Capricorn? If it stays in Aries, its research must keep clear of law.
  4. Splits C27 to C36.
- **Taurus**
  1. The file's five opening questions: the possession/ownership split, the security/stability split, security's home, the scope of values, and money.
  2. Six older law-word hits:
     - the proverb "possession is nine-tenths of the law";
     - the Dene Laws;
     - the Libra cross-reference;
     - *tamánwit*, "the law of the land";
     - Gallup's Law and Order Index;
     - The Police (the band).
     
     The run agent adds a seventh older line, the National Indian Gaming Commission, which is a regulator.
  3. Ownership's older deed lines:
     - title deeds (*escrituras*);
     - INSUS land titles;
     - public handovers of title deeds;
     - racial covenants.
     
     Leave them, or relocate them to Libra?
  4. C39 Providing (for male readers): Taurus, Cancer or Capricorn?
  5. Homes:
     - Food (C3) and dress (C4): concepts, or folkway bullets in section 0?
     - C18 Loyalty: Scorpio or Cancer?
     - C36 Inheritance and C2 Resources: these overlap Scorpio, where the file places inheritance and the commons.
  6. Splits C35 to C46.
  7. Long blocks: Values about 96; Possession and Ownership about 92.
- **Gemini**
  1. The opening's questions:
     - learning against education;
     - gossip and rumor;
     - mediation against diplomacy;
     - duality's definition;
     - siblings;
     - the near neighbors.
     
     C35, C38, C42, C43 and C48 bear on them.
  2. Older law-leaning lines:
     - the metaphor "the glue and police of community life";
     - the English-only movement and U.S. English;
     - Native-language teaching certificates;
     - Canada's long-form census decision;
     - the 2019 census citizenship-question fight;
     - INAI;
     - the FMCS, the National Mediation Board and Mexico's labor conciliation centers;
     - *Judge Judy* and *Caso cerrado*;
     - dual citizens;
     - immigration status and the undocumented;
     - doxxing;
     - the sins of detraction and calumny.
  3. Overlaps:
     - C7 Directness = Aries C7;
     - C23 Persuasion overlaps Taurus C6;
     - C6 Politeness overlaps Libra's civility;
     - C26 Privacy overlaps Scorpio's secrecy.
  4. Concepts or bullets?
     - Should Neighbors (C1) or Short journeys (C2) become concepts?
     - C3 Language: a concept, or section 0's bullets?
     - C4 Childhood: Gemini or Cancer?
  5. Splits C35 to C48.
  6. Long blocks: Communication, Learning and Information.
  7. Male readers: Gemini has no entry of its own. Add one (for example, men's talk and men's silence), or leave the topic spread across C46, C27 and Connection?
  8. Some of its 79 *check* marks are cautious: Hochschild, Berry, Lave and Wenger, and geocaching's start.
- **Cancer**
  1. The opening's questions:
     - nurture against care;
     - home against shelter;
     - protection against security;
     - motherhood without fatherhood;
     - the missing items.
     
     C1, C45 and C46 bear on them, and C3 to C7, C26 and C29 cover the missing items.
  2. Overlaps:
     - C5 = Taurus C21;
     - C6 = Gemini C4;
     - C3 against Taurus C30 and Aries C29, with C28 *Heimat* between them;
     - C7 against Gemini C26;
     - C27 against Taurus C32;
     - C38 between Taurus C39 and Aries C28;
     - C23 Loneliness.
  3. Older law-leaning lines:
     - eight "in-laws" false positives;
     - Gallup's Global Law and Order report;
     - eviction and foreclosure;
     - CPS, child-protection agencies and Adult Protective Services;
     - safely surrendered babies;
     - concealed-carry permits;
     - racial covenants;
     - HOA fines;
     - asylum, refugee sponsorship and sanctuary;
     - Vancouver's access-without-fear policy;
     - family separation at the border;
     - deportation.
  4. Male readers: C1 Fatherhood, C38 The protector role, C18 Guardedness and withdrawal, C23 Loneliness. Should fatherhood become a concept?
  5. Splits C31 to C44; merges C45 (parenthood) and C46 (nurture and care).
  6. Long blocks, about 85 to 100 types.
- **Leo**
  1. The opening's questions:
     - recognition shared with Capricorn;
     - humiliation and shame;
     - pride, dignity and honor, with face as the missing fourth corner;
     - recognition, being seen and self-expression;
     - play and joy;
     - leadership against authority.
     
     C22, C26, C52, C41, C42, C53, C54, C47 and C17 bear on them.
  2. Overlaps:
     - C9 with Taurus C4 and Aries C2;
     - C12 with Taurus C40;
     - C5 with Gemini C9 and Cancer C11;
     - C16 with Cancer C27 and Taurus C32;
     - C21 with Gemini C10;
     - C24 with Aries C20;
     - C19 with Aries C32;
     - C18 with Aries C27 and C28;
     - C3 with Cancer C6 and Gemini C4;
     - C40 with Cancer C20 and Aries C36;
     - C49 with Taurus C14;
     - C25 with Capricorn;
     - C26 (face);
     - C27 with Aries C2.
  3. Older law-leaning lines:
     - patents per capita;
     - books pulled from shelves;
     - campus speech fights;
     - military tattoo rules and platform moderation rules;
     - foreign credentials;
     - the 2024 federal race and ethnicity standard;
     - assisted dying and its reports;
     - harassment rules;
     - the San Francisco Committees of Vigilance;
     - Coastal GasLink;
     - game ratings;
     - Prohibition, Sunday closing and Sabbath rules;
     - hunting and fishing license counts;
     - sports-betting handle.
  4. Male readers: C6, C17, C18, C19, C22, C38, C41, C44 and C50.
  5. Splits C36 to C51; merges C52 to C54.
  6. Some *check* marks are cautious: the Caesar salad, Pink Shirt Day, the *bolo*, *mal de ojo*, "cool" and "lose face".
- **Virgo**
  1. The opening's questions:
     - analysis against discernment;
     - gullibility;
     - the cluster of criticism, perfectionism and improvement;
     - health's facets;
     - service's border with duty, care and self-sacrifice;
     - usefulness and unasked help;
     - work's facets;
     - "discrimination";
     - the gaps in the domain.
     
     The bearing candidates are listed in the log.
  2. Household order (C4): Virgo, or Capricorn with order?
  3. Overlaps:
     - C1 with Taurus C15;
     - C2 and C4 with Cancer C8;
     - C6 with Taurus C3 and Cancer C14;
     - C9 with Taurus C19 and Gemini C39;
     - C12 with Aries C26;
     - C17, C30 and C62 with Cancer C13;
     - C22 (procrastination) with Aries C17;
     - C31 with Taurus C14 and Leo C49;
     - C40 with Leo C44;
     - C52 with Gemini C25;
     - C57 with Aries C1 and Leo C6;
     - C58 with Pisces;
     - and others, listed in the log.
  4. Older law-leaning lines (a long list, in the log), among them:
     - workers' compensation, H-2A, the draft, oaths of office and civil service;
     - eugenic sterilization, Death with Dignity and MAID reports;
     - CONAPRED, PROFECO, the FTC and *notario* fraud;
     - HOA rules and ISO certification;
     - speech codes, inspectors general, the blacklist and McCarthyism;
     - the ACA and Medicaid, Oregon's prioritized list, Insite, the 1900 Chinatown quarantine and psilocybin services;
     - the Truth and Reconciliation Commission, urban renewal, *usos y costumbres* and *limpieza de sangre*;
     - the older Mother Antonia Brenner prison line.
  5. Its 65 candidates are many: trim them?
  6. Male readers: C9, C12, C16, C36, C38, C39, C40, C43 and C56.
- **Libra**
  1. The opening's questions:
     - justice against fairness (C56, C38, C39);
     - impartiality's place (C57, C23, C43, C51);
     - peace at any price (C20, C55, C58, C10);
     - projection's fit (C24, C27);
     - the gaps: contracts (C1), open enemies (C3), mercy and forgiveness (C26), cooperation and compromise (C11, C12), corruption (C16).
  2. Section 0 has two source-type blocks, one cultural and one legal. Keep both, or merge them?
  3. Letter-and-spirit candidates: C8, C9, C16, C34, C35, C37, C38 and C54. Keep them in Libra, or move some to Capricorn?
  4. Older lines in Justice and Impartiality lean toward the spirit of the law: what justice is for, calling the police, pardons, the Amnesty Law, confidence in courts, and taking justice into one's own hands. Move them to Capricorn section 8, keep them, or reword them?
  5. Overlaps: a long list, in the log.
  6. C20 and C58 are alternatives: peace as its own concept, or one concept of peace that holds its excess.
  7. Male readers: C1, C3, C7, C42, C47 and C48. C25 also records "fear of commitment" as a claim to test.
- **Scorpio**
  1. Should loyalty (C22), privacy (C23) and grief and mourning (C24) become entries? Forgiveness is left to Libra's C26.
  2. Homes for inheritance, privacy and loyalty (see A8).
  3. Older law-leaning lines:
     - coroners;
     - MAID and assisted-dying reports;
     - the Superfund and Hanford cleanups;
     - voter-roll removals;
     - loyalty oaths;
     - the HUAC blacklist;
     - deportations;
     - the old refusal of church burial;
     - the police "blue wall" and prison subcultures;
     - the vigilance committees and lynchings;
     - the *autodefensas*;
     - the potlatch ban;
     - *la ley del silencio*.
  4. Its 60 candidates: trim them? Death's splits (C32 to C36) and secrecy's (C50 to C52) are the most numerous.
  5. How deep should the sensitive entries go: C12 self-destruction, C17 killing, C35 suicide, C36 the disappeared?
  6. Confirm two exclusions:
     - the research notes' term for moral cause and effect across lifetimes (South Asian in origin) is left out;
     - the constellation myths and sign imagery are kept out.
- **Sagittarius**
  1. The opening's questions:
     - faith and belief (C57, with C25 as a test);
     - the chain of belief, conviction and fundamentalism (C58);
     - truth and honesty (C59).
     
     Three traditional areas have no concept: religion (C1), philosophy (C5) and pilgrimage (C46).
  2. Homes:
     - C7 with Scorpio C45;
     - C16 with Scorpio C37;
     - C14 with Gemini C40;
     - C23 with Gemini C39;
     - C32 with Gemini C34;
     - C33 with Gemini C47;
     - C35 and C30 with Virgo C27 and C42;
     - C42 with Libra C35;
     - C56 with Scorpio C41;
     - C39 and C52 with Virgo C50;
     - C55 with Scorpio C32;
     - and integrity (C21), which has no home yet.
  3. Older law-leaning lines:
     - civil-liberties associations;
     - the UC loyalty oath;
     - CONAPRED;
     - refusals at work on religious grounds;
     - passport offices, border agencies and trusted-traveler programs;
     - Operation Gatekeeper;
     - consumer agencies, inspectors general and tax authorities;
     - the vigilance committees and land frauds;
     - the Mendez family's fight;
     - legacy and race-conscious admissions;
     - the 2019 reform;
     - the church that defied COVID-19 orders;
     - the seizure of Doukhobor children;
     - the Scopes trial.
  4. Its 59 candidates: trim them?
  5. Male readers: C5, C14, C15, C21, C23, C35, C37, C50 and C51.
  6. Confirm three exclusions:
     - South Asian-origin traditions, movements and communities are left out and unnamed, including those active in the pilot region. This leaves a known gap in the region's religious history, pilgrimage and meaning-seeking.
     - The notes' myth figures, sky lore and astrological material are kept out.
     - Formal rules go to Libra and Capricorn.
  7. It has the most new *check* marks of any sign (164).
- **Capricorn**
  1. Status (C2) and reputation (C3) against Leo's C41 and C25. Keep the line drawn here (position and track record in Capricorn; esteem, display and talk in Leo), or give each to one sign?
  2. The seven law splits (C47 to C53: policing, punishment, prison, mercy and discretion, taking the law into one's own hands, outlaws, impunity): candidate concepts, or facets of Law? Prison is placed here, although confinement is one of Pisces's traditional areas.
  3. Duty and responsibility (C55): one entry or two?
  4. Military life (C35) and war (C36): Capricorn or Aries?
  5. Seniority is folded into elders (C4), with Gemini C45 holding birth order. Agree?
  6. Loyalty is split: allegiance here (C16); loyalty between persons in Scorpio C22 and Taurus C18. Agree?
  7. Male-reader lines: more, fewer, or as is?
- **Aquarius**
  1. The opening's questions, set out as merges:
     - community and group (C50);
     - idealism, reform and hope (C51);
     - equality: stay here, or move to Libra (C52)?
  2. Detachment's home, if its splits (C19, C20, C48) are taken: here, Pisces, or beside Libra's impartiality?
  3. The isolation, loneliness and solitude group: keep the split with Cancer's C23 and C18, or give it one home?
  4. The lines drawn against nearby candidates:
     - C3 against Capricorn C34;
     - C15 against Scorpio C5;
     - C14 against Libra C11 and Virgo C26;
     - C6 against Virgo C61.
  5. Gangs (C37): here, or wholly in Capricorn?
  6. Science and technology (C7): keep it, or leave it to Virgo C50 and Sagittarius C41?
  7. Male-reader lines: more, fewer, or as is?
  8. "Age of Aquarius" appears once, as a 1960s cultural phrase. Keep it, or remove it?
- **Pisces**
  1. The opening's questions:
     - compassion and empathy (C67);
     - worry and anxiety, under Fear or with Virgo C23 (C68);
     - dissolution's second sense, split out as C51;
     - addiction (C54), with drinking customs apart (C55).
  2. Confinement: one concept, or C7 to C10?
  3. Magic ways (the folkway): one concept, or C16 to C21?
  4. The wrongdoing splits (C59 to C64): keep them all here, or move guilt to Leo and sin to Sagittarius?
  5. Madness, sadness and trauma (C3 to C5) against Virgo's C58. Keep the line drawn: the figure, the history and the feeling here; health and help-seeking with Virgo.
  6. Its 69 candidates are the most of any sign: trim them? The weakest may be C15, C27, C37 and C38.
  7. Older law-leaning lines:
     - the police memorial line;
     - the 2013 prison hunger strike;
     - Prison Fellowship;
     - safe surrender;
     - the dates of medical aid in dying;
     - Crime Stoppers;
     - neighborhood watch.
  8. Male readers: 40 of the 69 candidates carry the question. More, fewer, or as is?
  9. Run agent: C13 Contemplation and meditation cites an older line on corporate mindfulness (Google's "Search Inside Yourself"). Mindfulness has partly Buddhist roots. It is kept as a present-day secular practice; all South Asian traditions are excluded. Confirm.

### Candidate subtopics proposed, by sign

All are PROPOSED. Each sign file gives every candidate a working definition, why it belongs (with "Also fits"), what it would add and avenues for researching it. Candidates are grouped in each file by where they came from:
- the sign's traditional areas;
- its research notes;
- Tier 2 and the near-synonym groups;
- concepts other languages name;
- splits and merges.

- **Aries** (36): C1 The body; C2 Appearance and self-presentation; C3 Names and naming; C4 Personhood; C5 Impatience and urgency; C6 Impulsiveness and spontaneity; C7 Directness; C8 Being first (pioneering); C9 Toughness and the proving of manhood; C10 Aggression; C11 Rebellion and defiance; C12 Self-confidence; C13 Individuality; C14 Self-discovery; C15 Vulnerability; C16 Energy and vitality; C17 Follow-through; C18 Endurance (*aguante*, *gaman*, *sisu*); C19 Humility and modesty; C20 Self-centeredness and entitlement; C21 Boredom and the need for excitement; C22 *Thymos* (spiritedness); C23 *Chutzpah* (audacity); C24 *Amae* (welcome dependence); C25 *Ganas* (drive); C26 Resourcefulness (making do); C27 Moral courage (split from courage); C28 Heroism and rescue (split from courage); C29 Origins (split from beginning); C30 Righteous anger (split from anger); C31 Grudges and grievance (split from anger); C32 Winning and losing (split from competition); C33 Rivalry (split from competition); C34 Risk and caution (split from recklessness); C35 Collective self-rule (split from autonomy); C36 Personal and group identity (split of identity).
- **Taurus** (46): C1 Money; C2 Resources; C3 Food and eating; C4 Dress and clothing; C5 Thrift and waste; C6 Exchange and trade; C7 Debt and credit; C8 Poverty and want; C9 Attachment and letting go; C10 Accumulation; C11 Materialism; C12 Greed; C13 Comfort and coziness; C14 Rest and idleness; C15 Routine and habit; C16 Patience and waiting; C17 Reliability; C18 Loyalty; C19 Craftsmanship; C20 Cultivation; C21 Hospitality; C22 Earning and spoiling; C23 Practicality; C24 Beauty; C25 Contentment and "enough"; C26 Resistance to change, and stagnation; C27 Envy; C28 Class; C29 *Mottainai* (regret over waste); C30 *Querencia* and *arraigo* (the place one belongs to); C31 Inalienable treasures (*at.óow*, *taonga*); C32 Connections as wealth (*guanxi*, *palanca*, *compadrazgo*); C33 Giving owed from wealth (*tzedakah*, *zakat*); C34 *Wabi-sabi* (beauty in the worn and imperfect); C35 Sharing and lending (split from possession); C36 Heirlooms and inheritance customs (split from possession and ownership); C37 Owning the intangible (split from ownership); C38 Valuation and price (split from values); C39 Providing (split from self-worth); C40 Display of wealth (split from wealth); C41 Territoriality and localism (split from possessiveness); C42 Stinginess (split from possessiveness); C43 Steadfastness (split from stubbornness); C44 Admitting mistakes (split from stubbornness); C45 Touch (split from sensuality); C46 Indulgence and restraint (split from sensuality).
- **Gemini** (48): C1 Neighbors and neighborliness; C2 Short journeys and getting around; C3 Language and languages; C4 Childhood; C5 Literacy, reading and writing; C6 Politeness and manners; C7 Directness and indirectness; C8 Argument and debate; C9 Sociability; C10 Wit, wordplay and humor; C11 Storytelling; C12 Listening; C13 Teaching and mentoring; C14 Cleverness and intelligence; C15 Adaptability and versatility; C16 Changing one's mind; C17 Depth and superficiality; C18 Attention and distraction; C19 Discretion; C20 Open-mindedness; C21 Youthfulness and the refusal to grow up; C22 Complaining and venting; C23 Persuasion and salesmanship; C24 Lying and deception; C25 Credulity and skepticism; C26 Privacy; C27 Teasing and banter; C28 *Nunchi* and "reading the air"; C29 *Honne* and *tatemae*; C30 *Sobremesa*; C31 The palaver; C32 *Ta'arof*; C33 *Jeong*; C34 *Bildung*; C35 Conversation and small talk (split from communication); C36 Translation and interpreting (split from communication and mediation); C37 News (split from information); C38 Rumor and misinformation at scale (split from gossip and information); C39 Apprenticeship (split from learning); C40 Exploration (split from curiosity); C41 Keeping in touch (split from connection); C42 Living between two cultures (split from duality); C43 Hypocrisy and double standards (split from duality); C44 Twins (split from siblings and duality); C45 Seniority and birth order (split from siblings); C46 Brotherhood and sisterhood beyond kin (split from siblings); C47 Intercession (split from mediation); C48 Go-betweens and brokers (split from mediation).
- **Cancer** (46): C1 Fatherhood; C2 Filial duty; C3 Roots and rootedness; C4 Kinship and ancestry; C5 Hospitality at home; C6 Childhood; C7 The privacy of the home; C8 Housekeeping and household work; C9 The household and its forms; C10 Grandparents and grandparenthood; C11 Family meals and gatherings; C12 Being needed; C13 Smothering and unwanted help; C14 Feeding as love; C15 Nostalgia; C16 Family memory and its keepers; C17 Guilt and obligation among kin; C18 Guardedness and withdrawal; C19 The emotional climate of the home; C20 Homeland and love of country; C21 Birth and the newborn; C22 Engulfment and enmeshment; C23 Loneliness; C24 Leaving the nest; C25 *Storgē* (family affection); C26 *Familismo* (family first); C27 *Compadrazgo* (ritual kinship); C28 *Heimat*; C29 *Hiraeth* and *saudade* (longing for home); C30 The house as a lineage (*ie*; "house societies"); C31 The house (split from home); C32 Homelessness (split from shelter); C33 Taking in the stranger (split from shelter); C34 The extended family (split from family); C35 Chosen family (split from family); C36 Adoption, fostering and orphanhood (split from family and abandonment); C37 Paternalism (split from protection); C38 The protector role (split from protection); C39 Self-care (split from care); C40 Paid care and domestic work (split from care); C41 Estrangement (split from abandonment and family); C42 Those who stay behind (split from abandonment); C43 Othermothering (split from motherhood); C44 Childlessness (split from motherhood); C45 Parenthood (merge of motherhood and fatherhood); C46 Nurture and care as one concept (merge).
- **Leo** (54): C1 Pleasure; C2 Romance and romantic love; C3 Children as joy and pride; C4 Fame, glory and celebrity; C5 Celebration and the fiesta; C6 Sport; C7 Games of chance and luck; C8 Dance; C9 Dressing up and personal style; C10 Spectacle and pageantry; C11 Performance and the audience; C12 Showing off and boasting; C13 Charisma and charm; C14 Talent and giftedness; C15 Morale and team spirit; C16 Patronage and sponsorship; C17 Respect and disrespect; C18 Chivalry and gallantry; C19 Magnanimity (grace in victory and defeat); C20 Authenticity; C21 Comedy and laughter; C22 Shame; C23 Contempt and condescension; C24 Vanity and narcissism; C25 Reputation and good name; C26 Face (*miànzi* and *liǎn*); C27 *Sprezzatura* and cool (effortless grace); C28 *Bella figura*; C29 *Duende*; C30 *Firgun*; C31 *Philotimo*; C32 *Amour-propre* (self-love that needs others' esteem); C33 *Tarab* (enchantment through music); C34 *Relajo* (playful disorder); C35 *Personalismo* (loyalty to persons); C36 Art and the arts (split from creativity); C37 Invention and innovation (split from creativity); C38 Emotional expressiveness (split from self-expression); C39 Persona and the public self (split from self-expression); C40 Group pride (split from pride); C41 Status and standing (split from recognition); C42 Praise and flattery (split from recognition); C43 Representation (split from being seen); C44 The dignity of work (split from dignity); C45 Public shaming (split from humiliation); C46 Gift-giving (split from generosity); C47 Followership (split from leadership); C48 Games and gaming (split from play); C49 Leisure and free time (split from play); C50 Keeping one's word (split from honor); C51 Happiness and life satisfaction (split from joy); C52 Worth as one field: pride, dignity, honor and face (merge); C53 Recognition and being seen as one concept (merge); C54 Play and joy as one concept (merge).
- **Virgo** (65): C1 Daily routine and the shape of the day; C2 Cleanliness and dirt; C3 Purity and contamination; C4 Tidiness, clutter and household order; C5 Sleep; C6 Diet and eating right; C7 Errands and life admin; C8 Coworkers and workplace life; C9 Skill, competence and mastery; C10 Efficiency and productivity; C11 Prevention and foresight; C12 Maintenance and repair; C13 Record keeping; C14 Bosses, supervision and micromanagement; C15 Professionalism; C16 Composure under pressure; C17 Advice and counsel; C18 Unseen work and working without credit; C19 Teamwork and working alone; C20 Plainness and simple living; C21 Drudgery; C22 Procrastination; C23 Worry and anxiety; C24 Exploitation (being used); C25 Failure and mistakes; C26 Communal work (*tequio*, *minga*, *dugnad*, *bayanihan*); C27 *Ikigai*; C28 *Shokunin* and *kodawari*; C29 *Omotenashi*; C30 *Acomedido* (helping without being asked); C31 *Feierabend*; C32 *Yǎngshēng* (nourishing life); C33 Hot and cold (*lo frío y lo caliente*); C34 *Susto*, *empacho* and the folk illnesses; C35 *Tǎng píng* (lying flat); C36 The work ethic (split from work); C37 Overwork and burnout (split from work); C38 Unemployment and job loss (split from work); C39 Dangerous work (split from work); C40 Manual and mental work (split from work); C41 Informal work and getting by (split from work); C42 Vocation and calling (split from work); C43 Retirement (split from work and usefulness); C44 Customers and customer service (split from service); C45 Tipping (split from service); C46 Volunteering (split from service); C47 Being a burden (split from usefulness); C48 Working animals (split from usefulness and service); C49 Measurement and counting (split from analysis); C50 Trust in experts (split from analysis and discernment); C51 Taste and connoisseurship (split from discernment); C52 Judging character (split from discernment); C53 High standards and conscientiousness (split from perfectionism); C54 Self-criticism (split from criticism); C55 Healing and healers (split from health); C56 Illness and the sick role (split from health); C57 Fitness and exercise (split from health); C58 Mental health (split from health); C59 Disability (split from health and usefulness); C60 Self-help (split from improvement); C61 Progress (split from improvement); C62 Improving others (split from improvement); C63 Analysis and discernment as one concept (merge); C64 Standards as one field: perfectionism, criticism and improvement (merge); C65 Service and usefulness as one concept (merge).
- **Libra** (58): C1 Contracts and agreements (the handshake and the paper); C2 Marriage as an institution; C3 Open enemies and enmity; C4 Treaties and agreements between peoples; C5 Settling disputes; C6 Civility (manners among strangers); C7 Men and women: roles and relations; C8 Legalism and loopholes (the letter of the rule); C9 Going to law (suing and litigiousness); C10 Harmony; C11 Cooperation; C12 Compromise; C13 Consensus and how groups decide; C14 Negotiation and bargaining; C15 Alliances and coalitions; C16 Corruption; C17 Cheating; C18 Fair shares under scarcity; C19 Deliberation; C20 Peace and peacemaking; C21 Apology and reconciliation; C22 Passive aggression; C23 Neutrality and taking sides; C24 Blame; C25 Commitment; C26 Forgiveness; C27 Scapegoating and exclusion; C28 *Ma'at* (truth, balance and right order); C29 *Ubuntu* (a person through other persons); C30 *Simpatía*; C31 *Convivencia* (living together well); C32 *Enryo* and *kreng jai* (holding back out of consideration); C33 *Utang na loob* and *on* (debts of gratitude); C34 Restorative justice (split from justice); C35 Historical justice and redress (split from justice); C36 Compensation for harm (split from justice); C37 Rights and rights-talk (split from justice); C38 A fair hearing (split from justice and fairness); C39 Desert and deservingness (split from justice and fairness); C40 Prejudice and discrimination (split from fairness); C41 Fairness between generations (split from fairness); C42 Fighting fair (split from fairness); C43 Drawing lots (split from fairness and impartiality); C44 Choosing a partner (split from partnership); C45 Living together unmarried (split from partnership); C46 Intermarriage (split from partnership); C47 Divorce and separation (split from partnership); C48 Partners in work (split from partnership); C49 Moderation and the middle way (split from balance); C50 Work-life balance (split from balance); C51 Favoritism, nepotism and pull (split from impartiality); C52 Protocol and formality (split from diplomacy); C53 Free riders (split from reciprocity); C54 Pacifism and nonviolence (split from peace at any price); C55 Conflict avoidance (split from peace at any price); C56 Justice and fairness as one concept (merge); C57 Impartiality as a facet of fairness (merge); C58 Peace as one concept: peacemaking, conflict avoidance and peace at any price (merge).
- **Scorpio** (60): C1 Sex and sexuality; C2 Desire and temptation; C3 Intimacy; C4 Inheritance and succession; C5 The commons and pooled resources; C6 Money between partners; C7 Taboo; C8 Transformation; C9 The inner circle; C10 Duties to the dead; C11 Keeping it in (emotional restraint and its bursting); C12 Self-destruction (deaths of despair); C13 Suffering (what pain is for); C14 Remorse and repentance; C15 Uncovering the hidden (investigation and exposure); C16 Gallows humor; C17 Killing (the taking of life); C18 Legacy; C19 Intensity, passion and obsession; C20 Jealousy; C21 Manipulation; C22 Loyalty; C23 Privacy; C24 Grief and mourning; C25 *Han*; C26 *Schadenfreude*; C27 *Ressentiment*; C28 *Mono no aware*; C29 *Kintsugi*; C30 *Besa*; C31 *Viveza* and *colmillo* (admired cunning); C32 The afterlife (split from death); C33 The dead among the living (ancestors, ghosts and spirits) (split from death); C34 Dying and the good death (split from death); C35 Suicide (split from death); C36 The missing and the disappeared (ambiguous loss) (split from death); C37 Conversion (split from rebirth); C38 Recovery from addiction (split from rebirth); C39 Second chances (living down a past) (split from rebirth); C40 Revival (split from rebirth); C41 Shunning and excommunication (split from purging); C42 Whistleblowing (split from purging and betrayal); C43 Infidelity (split from betrayal); C44 Codes of silence (split from betrayal and secrecy); C45 Fate and fatalism (split from control); C46 Coercive control (split from control); C47 Mastery over nature (split from control); C48 Suspicion and vigilance (split from trust); C49 Feuds (split from revenge); C50 Family secrets (split from secrecy); C51 Passing and hidden identities (split from secrecy); C52 Anonymity (split from secrecy); C53 Powerlessness (split from power); C54 Power behind the scenes (split from power); C55 Survival and survivors (split from crisis); C56 Disaster (split from crisis); C57 Breakdown (the personal crisis) (split from crisis); C58 Control and power as one concept (merge); C59 Trust and betrayal as one concept (merge); C60 Death and rebirth as one concept: endings and renewal (merge).
- **Sagittarius** (59): C1 Religion (organized faith and its community); C2 Prayer and worship; C3 The sacred and the profane; C4 Unbelief and secular life; C5 Philosophy and the examined life; C6 Wisdom; C7 Providence and luck; C8 The foreign and the far away; C9 Religious pluralism and tolerance; C10 Civil religion (faith in public life); C11 Mission and proselytizing; C12 Clergy and religious authority; C13 Optimism and pessimism; C14 Adventure; C15 Restlessness and settling down; C16 Doubt and loss of faith; C17 Exaggeration, bluffing and the tall tale; C18 Universalism and relativism; C19 Morality and conscience; C20 The dream of a better life; C21 Integrity; C22 *Fernweh*; C23 *Wanderjahre* (the journeyman's wandering years); C24 *Peregrinatio* (wandering for God); C25 *Emunah* and *bitachon*; C26 *Tawakkul*; C27 *Parrhesia*; C28 *Pravda* and *istina*; C29 *Volya* and *svoboda*; C30 *Tikkun olam*; C31 *Shoshin* (beginner's mind); C32 *Jūnzǐ* (the person made good by learning); C33 Devotion to saints and vows (split from faith); C34 Secular faiths (split from faith); C35 Emptiness and drift (split from meaning); C36 Awe and wonder (split from meaning); C37 The frontier (split from freedom and travel); C38 Speaking freely and self-censorship (split from freedom); C39 Ways of knowing (split from truth); C40 Conspiracy belief (split from truth and belief); C41 Science and faith (split from truth); C42 Whose history is true (split from truth); C43 Myth and sacred story (split from truth and belief); C44 Ideology (split from belief); C45 Martyrs and martyrdom (split from conviction and faith); C46 Pilgrimage (split from travel and faith); C47 Migration (split from travel); C48 Exile and diaspora (split from travel); C49 Tourism and the tourist (split from travel); C50 Book learning and practical know-how (split from education); C51 Schooling as the way up (split from education); C52 Intellectuals and anti-intellectualism (split from education); C53 Religious education and formation (split from education and faith); C54 New religious movements (split from fundamentalism and faith); C55 The end of the world (split from fundamentalism and belief); C56 Orthodoxy and heresy (split from fundamentalism and belief); C57 Faith and belief as one concept (merge); C58 Strength of belief as one field: belief, conviction and fundamentalism (merge); C59 Truth and honesty as one concept (merge).
- **Capricorn** (57): C1 Career; C2 Status and standing (position in a ranked order); C3 Reputation (the record that follows a person); C4 Elders and the authority of age; C5 Punctuality and whose time it is; C6 Government as people live it; C7 Patrons and clients; C8 Bureaucracy and paperwork; C9 Obedience and deference; C10 Legitimacy; C11 Tradition and heritage; C12 Paying one's dues; C13 The long view (planning and the deferred reward); C14 The head of the household; C15 Social control (keeping people in line without the law); C16 Allegiance; C17 Maturity and adulthood; C18 Rules (keeping, bending and breaking them); C19 Self-control; C20 Perseverance; C21 *Respeto*; C22 *Cumplir*; C23 *Lǐ* (propriety); C24 *Giri* and *ninjō*; C25 *Pietas*; C26 *Gravitas*; C27 *Noblesse oblige*; C28 *Caudillismo*; C29 *Vlast'*; C30 *Tiānmìng* (the mandate of Heaven); C31 The Prussian virtues; C32 *Mitzvah*; C33 Abuse of authority (split from authority); C34 Civic duty (split from duty); C35 Military life and service (split from duty and authority); C36 War (split from authority and duty); C37 Tax morale (split from duty and law); C38 Accountability of the powerful (split from responsibility); C39 Stewardship (split from responsibility); C40 Correcting children (split from discipline); C41 Hazing and initiation (split from discipline and hierarchy); C42 Success (split from ambition); C43 Social mobility (split from ambition and merit); C44 Titles (split from hierarchy); C45 Elites and the establishment (split from hierarchy); C46 Credentials (split from merit); C47 Policing (split from law and order); C48 Punishment (split from law and discipline); C49 Prison (split from law); C50 Mercy and discretion (split from law); C51 Taking the law into one's own hands (split from law and order); C52 Outlaws and social bandits (split from law); C53 Impunity (split from law); C54 Queues and waiting one's turn (split from order); C55 Duty and responsibility as one concept (merge); C56 Authority and hierarchy as one field (merge); C57 Ambition and merit as one field: getting ahead (merge).
- **Aquarius** (52): C1 Humanitarianism and the moral circle; C2 Associational life (joining); C3 Civic participation (taking part in public life); C4 Activism and causes; C5 Revolution; C6 The future; C7 Attitudes to science and technology; C8 Tolerance and diversity; C9 Entering society (social debut); C10 Newcomers and the passage to membership; C11 Networks and weak ties; C12 Gathering places and public life; C13 Segregation and mixing; C14 Solidarity and mutual aid; C15 The common good; C16 Democracy as a way of life (equal voice); C17 Siding with the underdog; C18 Alienation; C19 Solitude and isolation (split from detachment); C20 Indifference and apathy (split from detachment); C21 *ʿAṣabiyya* (group feeling); C22 *Sobornost*; C23 *Communitas*; C24 *Comunalidad*; C25 *Kapwa* (the self shared with others); C26 *Paisanaje* and *landsmanshaft* (the bond of a shared home place); C27 *Janteloven* and the tall poppy (leveling norms); C28 *Buen vivir* (*sumak kawsay*); C29 *Ilusión* (hopeful anticipation); C30 Mateship; C31 Online communities (split from community); C32 Fans and fandom (split from community and group); C33 Fitting in (conformity and peer pressure) (split from group and nonconformity); C34 Crowds and collective effervescence (split from group); C35 Partisanship and polarization (split from group); C36 Factions, splits and schisms (split from group); C37 Gangs and street groups (split from group); C38 Generations (split from group); C39 Privilege (split from equality); C40 Environmentalism (split from reform and idealism); C41 Utopias and intentional communities (split from idealism); C42 Disillusionment and selling out (split from idealism); C43 Moral superiority and virtue signaling (split from idealism); C44 Men's friendships (split from friendship); C45 Friendship across group lines (split from friendship); C46 Subcultures and countercultures (split from nonconformity); C47 Eccentricity (split from nonconformity); C48 Objectivity (split from detachment); C49 Collective hope (split from hope); C50 Community and group as one concept (merge); C51 A better state as one field: idealism, reform and hope (merge); C52 Equality and fairness as one field (merge, moving equality to Libra).
- **Pisces** (69): C1 The unconscious (the hidden self); C2 Dreams and dreaming; C3 Madness and the mad; C4 Sadness, melancholy and despair; C5 Trauma (the hidden wound); C6 Consolation (comforting the suffering); C7 Institutions of care and confinement; C8 The cloister (monastic and contemplative life); C9 Retreat and seclusion; C10 Captivity and bondage; C11 Mysticism and mystical experience; C12 Ecstasy and trance (altered states); C13 Contemplation and meditation; C14 Offerings (gifts to the unseen); C15 The night; C16 Magic and superstition; C17 Divination and fortune-telling; C18 Witchcraft, the evil eye and hidden harm; C19 The paranormal and the unexplained; C20 Miracles; C21 Folk saints and unofficial devotions; C22 Victims and victimhood; C23 Charlatans and miracle cures; C24 Salvage (worth in what others throw away); C25 Being believed; C26 Vanishing (running away and disappearing); C27 Holiness (the saintly person); C28 Forgetting and oblivion; C29 Sensitivity; C30 Codependence and neediness; C31 Denial and self-deception; C32 *Agapē*; C33 *Ḥesed*; C34 *Raḥamim* and *raḥma* (compassion from the womb); C35 *Pena ajena* (embarrassment felt for another); C36 *Wu wei* (action without forcing); C37 *Yūgen* (the beauty of the half-hidden); C38 *Baraka* (blessing as a power); C39 *Toska* (anguish without a cause); C40 *Sehnsucht* (longing for the unreachable); C41 Charity and almsgiving (split from compassion); C42 Pity and being pitied (split from compassion); C43 Kindness (split from compassion); C44 Self-pity and self-compassion (split from compassion); C45 Compassion fatigue (split from compassion); C46 Compassion for animals (split from compassion); C47 The martyr complex (sacrifice that keeps accounts) (split from self-sacrifice); C48 Asceticism and self-denial (split from self-sacrifice); C49 Dementia (the fading self) (split from dissolution); C50 Assimilation (split from dissolution); C51 Endings (the coming apart of bonds and groups) (split from dissolution); C52 Thresholds (split from boundary); C53 Borderlands (split from boundary); C54 Addiction (split from escapism); C55 Intoxication (drink and drugs as custom) (split from escapism); C56 Nature as sacred (split from spirituality); C57 Grace (the unearned gift) (split from spirituality and compassion); C58 Acceptance and resignation (split from surrender); C59 Sin (split from crime); C60 Guilt (split from crime); C61 Theft (split from crime); C62 Evil (split from crime); C63 Vice (split from crime and escapism); C64 Moral panics (split from crime and fear); C65 Horror and the pleasure of fear (split from fear); C66 Monsters and bogeymen (split from fear); C67 Compassion and empathy as one concept (merge); C68 Fear, worry and anxiety as one field (merge); C69 Transcendence as one field: spirituality, dissolution and surrender (merge).

### Left for the main session

Step 7 of "How the run works" is outside the run agent's remit, which allows edits only to the sign files, the sign logs and this file. Four things remain:
1. Give this report to the author.
2. Update `Targets/Cascadia/PROGRESS TRACKER.md` (CurrentNovelDocs `worldbuilding/Deep_Culture_Investigation/`) and the DCI memory file.
3. Delete the hourly watchdog (job f13acbae).
4. Add the run-log line saying the report was given.


## Run log

Dated lines, newest last, written by the orchestrator: launches, agent IDs, cutoffs, resumes, QA results and fixes.

- 2026-11-11 00:40: run set up. Pre-run copies of all twelve sign files taken; one log per sign created; the brief now requires a checkpoint after every step. The 5:03 a.m. start (job 408688a1, which replaced 219304c0 so that it follows this file) and the hourly watchdog (job f13acbae) are scheduled.
- 2026-11-11 09:03: the 5:03 start fired late (received at 09:03) together with the watchdog; no sign had started. Aries: launching.
- 2026-11-11 09:03: Aries launched, agent a7cea3a8d9a78cff4.
- 2026-11-11 09:06: the Aries agent was stopped (it had only read the files and set the STATUS line; nothing lost). The run is now handed to one run agent, so that moving from sign to sign does not wait on the main session. The author was asleep, with Auto Mode on, and the 5:03 start sat unanswered until a key was pressed at 09:03.
- 2026-11-11 09:07: run agent launched, agent aa1848e6c6931d830. While it is running, the watchdog and the main session launch nothing.
- 2026-11-11 09:07: run agent: started; read the progress file and the brief; qa --all shows no sign done. Aries: marked in progress; its log has one checkpoint (09:04 started), so a sub-agent gets the replacement prompt.
- 2026-11-11 09:07: Aries: sub-agent launched with the replacement prompt, agent a09f50fd1b9d7a0e6.
- 2026-11-11 09:25: Aries: sub-agent finished (log checkpoint 09:24 "finished"); QA run and pasted into the log; pass, no fixes needed (the one law-word hit, a memorial line, predates the run and is kept as a question). Aries done.
- 2026-11-11 09:25: Taurus: marked in progress; launching a sub-agent with the launch prompt (its log has no checkpoints).
- 2026-11-11 09:26: Taurus: sub-agent launched with the launch prompt, agent af3c447ceac30e87f.
- 2026-11-11 09:55: Taurus: sub-agent finished (log checkpoint 09:54 "finished"); QA run and pasted into the log; pass, no fixes needed (all six law-word hits, both "Indian" uses and "Centre" predate the run; kept as questions). Taurus done.
- 2026-11-11 09:55: Gemini: marked in progress; launching a sub-agent with the launch prompt (its log has no checkpoints).
- 2026-11-11 09:55: Gemini: sub-agent launched with the launch prompt, agent aebb2ca4e2d288e18.
- 2026-11-11 10:23: Gemini: sub-agent finished (log checkpoint 10:22 "finished"); QA run and pasted into the log; pass, no fixes needed (the two law-word hits, three "Indian" uses, "La India María" and "Centre" predate the run; kept as questions). Gemini done.
- 2026-11-11 10:23: Cancer: marked in progress; launching a sub-agent with the launch prompt (its log has no checkpoints).
- 2026-11-11 10:23: Cancer: sub-agent launched with the launch prompt, agent a7ba48f3afe9303bc.
- 2026-11-11 10:51: Cancer: sub-agent finished (log checkpoint 10:50 "finished"); QA run and pasted into the log; pass, no fixes needed (all nine law-word hits, the "Indian" use and "Centre" predate the run; kept as questions). Cancer done.
- 2026-11-11 10:51: Leo: marked in progress; launching a sub-agent with the launch prompt (its log has no checkpoints).
- 2026-11-11 10:51: Leo: sub-agent launched with the launch prompt, agent a9657dafed91be504.
- 2026-11-11 11:22: Leo: sub-agent finished (log checkpoint 11:22 "finished"); QA run and pasted into the log; pass, no fixes needed (no law-word hits; the three British spellings are older published names). Leo done.
- 2026-11-11 11:22: Virgo: marked in progress; launching a sub-agent with the launch prompt (its log has no checkpoints).
- 2026-11-11 11:23: Virgo: sub-agent launched with the launch prompt, agent a92530c8e9cb626b0.
- 2026-11-11 11:58: Virgo: sub-agent finished (log checkpoint 11:57 "finished"); QA run and pasted into the log; pass, no fixes needed (the one prison line, seven "Indian" uses and "Centre" predate the run; kept as questions). Virgo done.
- 2026-11-11 11:58: Libra: marked in progress; launching a sub-agent with the launch prompt plus a note on where law belongs in Libra (its log has no checkpoints).
- 2026-11-11 11:58: Libra: sub-agent launched with the launch prompt, agent a96689bedd349dc26.
- 2026-11-11 12:34: Libra: sub-agent finished (log checkpoint 12:33 "finished"); QA run and pasted into the log; pass, no fixes needed (law kept to the law sub-section and the concepts tied to law; "Favours" is a published title). Libra done.
- 2026-11-11 12:34: Scorpio: marked in progress; launching a sub-agent with the launch prompt (its log has no checkpoints).
- 2026-11-11 12:34: Scorpio: sub-agent launched with the launch prompt, agent a8202391e2a19edb7.
- 2026-11-11 13:10: Scorpio: sub-agent finished (log checkpoint 13:10 "finished"); QA run and pasted into the log; pass, no fixes needed (the 11 new law-word hits are one "in-laws" and ten routing lines to Capricorn section 8; older hits kept as questions). Scorpio done.
- 2026-11-11 13:10: Sagittarius: marked in progress; launching a sub-agent with the launch prompt (its log has no checkpoints).
- 2026-11-11 13:11: Sagittarius: sub-agent launched with the launch prompt, agent a8232a437ca2d7c1a.
- 2026-11-11 13:43: Sagittarius: sub-agent finished (log checkpoint 13:42 "finished"); QA run and pasted into the log; pass, no fixes needed (one new law-word hit is a pointer line; the new "Indian" use is a published name). Sagittarius done.
- 2026-11-11 13:43: Capricorn: marked in progress; launching a sub-agent with the launch prompt plus a note on where law belongs in Capricorn (its log has no checkpoints).
- 2026-11-11 13:43: Capricorn: sub-agent launched with the launch prompt, agent a86138d3dd15ab1c4.
- 2026-11-11 14:15: Capricorn: sub-agent finished (log checkpoint 14:15 "finished"); QA run and pasted into the log; pass, no fixes needed (law concentrated in concept 8 and the enforcement side of Authority and Order; "Favours" is a published title). Capricorn done.
- 2026-11-11 14:15: Aquarius: marked in progress; launching a sub-agent with the launch prompt (its log has no checkpoints).
- 2026-11-11 14:16: Aquarius: sub-agent launched with the launch prompt, agent a9d586cafb083b25e.
- 2026-11-11 14:52: Aquarius: sub-agent finished (log checkpoint 14:51 "finished"); QA run and pasted into the log; pass, no fixes needed (the one law-word hit and both "Indian" uses predate the run). Aquarius done.
- 2026-11-11 14:52: Pisces: marked in progress; launching a sub-agent with the launch prompt plus a note on the crime section (its log has no checkpoints).
- 2026-11-11 14:52: Pisces: sub-agent launched with the launch prompt, agent ab0f1e3acb0139615.
- 2026-11-11 15:34: Pisces: sub-agent finished (log checkpoint 15:34 "finished"); QA run and pasted into the log; pass, no fixes needed (no new law-word hits; the new British spelling is a proper name). Pisces done. All twelve signs done; writing the final report.
- 2026-11-11 15:37: Run agent: all twelve signs done and passed QA (no fixes needed). Final report written above the run log; STATUS set to done, final report not yet given to the author. Step 7 of "How the run works" (giving the report to the author, the Cascadia tracker and DCI memory, deleting the watchdog) is left for the main session.
- 2026-11-11 15:40: main session: checked all twelve files independently (no pre-run line missing; every new law-word hit outside Libra and Capricorn is a pointer line or "in-laws"; the new "Indian" use is the Indian Shaker Church, a published name; the new spelling hits are "criticism" and proper names). Watchdog f13acbae deleted. Cascadia PROGRESS TRACKER and DCI memory updated. Final report given to the author.
