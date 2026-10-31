# Brief: the glossary sweep, merge stage (2026-10-30)

## The job
Ten harvest agents each swept one area of the author's repos and wrote a table of terms (`../_harvest/<area>.md`). A script grouped every row by term: `../_merge/<range>.md` lists, for each term, every area's row. **You turn the groups for your letter range into the final glossary entries**, written into the letter files `../<L>.md` for your letters.

**Read first:**
- `../README.md`: the glossary's purpose, entry format, status levels and rules.
- the finished entries `../A.md`, `../H.md`, `../S.md`, `../T.md` (Abramentes, HyperHedral, Siligel, TANA);
- `brief.md`, the harvest brief: what counts as a term, and the known unnamed or non-canon items.

## For each group
1. **Decide whether it is a term,** using `brief.md`'s include and leave-out lists. Drop individual characters, real-world things in their ordinary meaning, and noise. List what you drop in your progress file.
2. **Decide whether two groups are one term.** Different names for the same thing become ONE entry. Check `../_merge/name_index.md`, because a variant may be filed under another letter range. Use the current or most authoritative name as the title, and list the others under **Also called**. If the other name falls outside your letters, still write the entry under your title. The coordinator adds the cross-reference stubs later.
3. **Write one entry** in the README format, plus the Also-called line:
```
### Term
- **Category:** ...
- **Also called:** other names, former names, spellings, separated by semicolons; each name bare, with any note in parentheses after it (omit the line if none)
- **Definition:** one to three plain sentences synthesized from the rows; nothing invented
- **Status:** Timeline canon / project canon / working (+ what is unsettled)
- **Used in:** union of the rows' Used in
- **Sources:** the defining sources, most authoritative first
- **Open:** conflicts between repos (who says what, which is newer), placeholders, gaps (omit if none)
```
   - **When rows disagree, never pick a side.** Give the definition the rows share, and put each disagreement under **Open**: which repo says what, and which is newer if known.
   - **Status:** use the most authoritative source (Timeline, then an author ruling, then project design). If another repo contradicts it, say so under Open.
   - **Keep every placeholder flag:**
     - Majyao's teahouse has no name yet.
     - Terms from non-canon GDD vignettes stay marked as such.
     - Placeholder names stay marked as placeholders.
   - **Renamed cities:** the title is the current name, the old names go under Also called, and the rename (date and repo) goes under Open if any repo still uses an old name.
4. **Category:** one of organization, company, polity, place, era or event, law or rule, robot biology, technology, culture and society, group or people, language, unit or measure, game term, method term. For game and method terms, start the Definition with the project, or with "(out of fiction)".

## Known cross-area conflict
Areas disagree on **Toronto Fell Out's universe**.
- **Area O:** Tepenian. The author confirmed on 2026-07-29 that the game is set in the Timeline's Great Lakes DMZ in 2097, citing TorontoFellOutGDD.
- **One of area G2's helpers:** not Tepenian, only reusing copied GDD material.

Wherever this matters, record both under Open, and cite area O's source as the stronger one.

## Held out: pre-Tepenian Cryptograph Helix details (author, 2026-10-30)
Many Cryptograph Helix world details predate the Tepenian universe. They will almost certainly change, and some may be scrapped, so **don't include them for now.** The author's examples are New Szolnok and the Altay Nation.
- **Hold (no entry):** every in-world term whose only source is TheCryptographHelixDD. That covers places, polities, societies, factions, mafias, technologies and customs, for example New Szolnok, Neo-Debrecen, the Altay Nation, the Resistance and the Mafias.
- **Keep:** the navigation cluster from `world/navigation.md` and the TANA controller file (TANA, the Polaris and Regulus Lines, the Solar Positioning System, Solar Latitude/Longitude, Sharp and Flat, the Navigational Almanac, Space Traffic Controller, dead space), and the series' out-of-fiction method terms.
- **A term that other repos also use** keeps its entry.
- **If you already wrote a held entry,** remove it cleanly. List held terms in your progress file under "Held: pre-Tepenian Cryptograph Helix".

## Brainstorm-only items
Area G3a kept 176 items whose only source is the 2026-07-29 "Community Infrastructure & Social Life" brainstorm lists, all marked `working`.
- **Don't give these their own entries** unless another source (a spec, canon reference, megasheet or another area's row) also names them.
- **Whoever owns the C range** writes one entry, "Community Infrastructure & Social Life brainstorm (2026-07-29)", as a method term. It says what the lists are, where they are, and that their items are proposals.
- List the dropped items by name in your progress file.

## Output
- **Write only the letter files for your letters:** `../<L>.md`, each starting `# Glossary: <L>`, entries sorted alphabetically by title (ignore a leading "The").
  - `A.md`, `H.md`, `S.md` and `T.md` already exist with one entry each. **Keep those entries** and fold any new harvest information into them.
  - Titles starting with a digit or symbol go in `../0-9.md`; that file is owned by the U-Z range.
- **Keep a progress file** `../_merge/<your range>.progress.md`:
  - first line `STATUS: IN PROGRESS (next: <letter or term>)`, then `STATUS: COMPLETE`;
  - then three lists: groups merged as one term (which names), groups dropped (term and reason), and conflicts the author should rule on (one line each).
- **Write a letter file in chunks as you go,** so a cutoff loses little. If you are resumed or are a replacement agent, read your progress file and the letter files, and continue. Never restart.

## Rules
- **Write only your letter files and your progress file.** Run no git commands that change anything, and never write to any other repo.
- **American English, plain language.**
- **Every definition traces to the harvest rows,** which trace to the repos. If something is unclear, grep the source file the row cites. Don't guess.
- **Keep it tight.** One to three sentences per definition. The detail lives in the sources.

## When done, reply with
- your letter files and their entry counts;
- the groups you merged;
- the conflicts the author should rule on, as a short list.
