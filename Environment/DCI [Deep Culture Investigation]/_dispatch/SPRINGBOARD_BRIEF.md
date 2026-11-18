# Brief: DCI springboard scouting (one nation × one sign × one concept)

Saved in the repo so a cutoff loses nothing. You are given **NATION**, **SIGN** (number and name) and **CONCEPT** (a number from that sign's avenue file; **0 = the sign's domain and folkways**).

**This is scouting, not research.** You write a short *springboard sheet*: where a researcher should start looking. You report **no findings** about the culture. Read `<DM>/Shared/Springboard_Scouting.md` first: it defines what a sheet is, what it must not hold, and the rules. Read it in full; it is short.

**Priority (author's ruling, 2026-11-15): accuracy and depth come before token economy.** This is the springboard stage, not the research stage, but the sheet is the first thing the later, in-depth research will start from, so make every pointer as helpful as you can toward detailed, thorough results. The earlier pilots were written to keep the run cheap; that is no longer the aim. Concretely:
- **Take the tokens and the time the sheet needs.** Never shorten, skip or hurry a sheet to save tokens. Do not trim a useful pointer to fit a word count; the length target below is a guide, not a ceiling to hit.
- **Read every input in full:** the spec, the template, the whole concept block (no `head -c` or other cutoffs; read it all, including the avenues and source types), and the tracker header. Run `concept_block.py` once per sheet and write that sheet before reading the next concept's block.
- **Think before writing each sheet:** which classical or founding sources, which modern scholarship, which primary-source collections and archives, which datasets, media and oral or folk traditions would best open *this* concept in *this* nation? Cover the full range of source types the concept block lists, not just the easiest few.
- **Depth inside the nation:** give pointers for the nation's own regions, minorities, Indigenous peoples and diasporas, not only the best-known two or three. Use the native-script forms of the search terms (for example hangul plus Hanja, Cyrillic, Arabic script) and the minority and Indigenous languages' terms, marked *check* where unsure. Include at least one pre-modern or classical pointer where the culture has a written or oral tradition that old.
- **Accuracy still beats count:** a real, well-known source is better than an obscure uncertain one, and a lesser-known real one you are confident about is better than a safe repeat. When you are not sure of a title, author or URL, give the source type and the query instead (never invent a name). Do not pad to reach a pointer count.
- **Give the reason for every pointer.** In "What it would give", say why this pointer matters for this concept: the question it helps answer. A later researcher will use the sheet as a starting point only, will not stay on it, and must know why each item is there. Keep the template's "Use" line.
- **Make each sheet its own:** write it from scratch for this nation and this concept; do not reuse sentences or whole table rows from your other sheets, and do not let the same few sources fill every sheet of a sign. The first queries must be concrete enough to run as written.

**Paths**
- `<DM>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/DCI [Deep Culture Investigation]`
- `<RESULTS>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation`

**Inputs: read only these**
1. `<DM>/Shared/Springboard_Scouting.md` and the template `<DM>/Templates/T_Springboard.md`.
2. The concept: `python3 -I "<DM>/_dispatch/concept_block.py" <sign number> <concept number>` prints its working definition, facets, avenues and source types. (Concept 0 prints the sign's domain.) Its avenues are prompts for where to look; they are not findings.
3. The nation: find its folder with `find "<RESULTS>/Targets" -type d -name "<NATION>" -exec test -f "{}/PROGRESS TRACKER.md" \; -print` (nations sit at `Targets/<region>/<nation>/`, or `Targets/Asia/<sub-region>/<nation>/` for the four Asian regions; the nation Russia sits at `Targets/Russia/Russia/`; the nine member states of the Sinian Federation sit at `Targets/Asia/East Asia/Sinian Federation/Subregions/<name>/` and are written as sub-units: for them the target is that member state's own lands and peoples, as its tracker header says, and the federation as a whole is mentioned only briefly), then read only the header of its `PROGRESS TRACKER.md` (region, pre-war lands carried). **The target is the post-war nation:** write for the lands it consists of, not the old country. If `00 - Scope.md` exists in the folder, you may read its units section. If it does not exist (the usual case), never tell the reader to read it or to check a scope file; if the header's pre-war lands are broad, say once, in the flags, that the nation's exact lands are still to be settled, and write the rest for the core lands without repeating the hedge in every section.
4. Nothing else. **No web search. No web fetch. No other files.**

**Write to:** `<RESULTS>/Targets/<region path>/<NATION>/Springboards/<NN> - <Sign>/<file>` where `<file>` is `00 - Domain and folkways.md` for concept 0, otherwise `<concept number, two digits> - <Concept name>.md`. Create the folders if needed. Touch no other file.

**Checkpoint:** write the file early with first line `STATUS: in progress`. Check its size and quality first; change the first line to `STATUS: done <today's date>, not verified` as your **very last write**, so the status grid is a reliable "finished" signal. Follow the template's five sections.

**How to write it**
- **Length:** aim for about 1,000 words per sheet, counting the table markup. Going a little over is fine, up to about 1,200; the scan flags anything over 1,300. Never pad a sheet, and never drop a useful pointer to save length; a sheet is shorter only when you honestly know little (see "A thin answer is fine"). Aim for 12 to 16 distinct pointers per sheet.
- **Search terms:** the concept's words in the nation's main language(s) (more than one if the nation is multilingual; include the main minority and Indigenous languages of its lands), with a gloss. English keywords too. Transliterate non-Latin scripts and give the native script when you are sure of it.
- **Where to look first:** name only what you are confident exists (a named survey, dataset, institution, archive, journal, standard work or author, newspaper, broadcaster, genre). If you are not sure of an exact title, author or URL, **write the type of source and the query that would find it instead. Never invent a name.** Mark every named item *check*. Say how it can be reached (open web, library, archive, paid, offline or in person, unknown).
- **Who to compare:** the regional cultures, ethnic and Indigenous peoples and other groups inside the nation worth separating. Say why, in a phrase.
- **Flags:** likely rich, mixed or thin data; languages needed; anything sensitive or restricted (a people's restricted knowledge, for example); pointers held for review under the standing rules.
- **First queries:** three to five concrete first steps, in order.
- **A thin answer is fine.** If you know little about where to look for this concept in this nation, say so and give the generic route (the language's dictionaries, the national statistics office, the main universities' collections, national library catalogs).

**Law:** if your sign is Libra, a law-related concept takes the *letter* of the law only (what the law says, contracts, courts as written); if Capricorn, the *spirit* (what law is for, obedience, discretion, legal culture). In every other sign, no law research: point to Libra or Capricorn.

**South Asian rule, strictly:** name no South Asian work, scholar, community or language anywhere in a sheet except the one "Held for review" line, and there only as a category ("South Asian-heritage communities in the nation's lands"). Not in "who to compare", not in search terms.

**Standing rules (also in the spec):** American English. Native, Indigenous or Aboriginal, never "Indian". No South Asian works or scholars as pointers. No law outside Libra and Capricorn. No national stereotypes: name variation, never one voice. No findings. The zodiac is a classifier only.

**Finish:** reply with one line: the file path and `done`, plus any problem. Do not summarize the content.
