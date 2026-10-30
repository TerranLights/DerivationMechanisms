# Brief: extracting the story-structure sources (2026-10-29)

## The project
The author keeps a composite story structure: Snyder's *Save the Cat*, James Scott Bell, John Truby and Joseph Campbell, plus Dan Harmon's Story Circle for minor characters. It is used across all their works, in every medium. The Derivation Mechanisms repo is building a full reference for each framework, with one folder per framework and one file per beat or step.

**This pass is research only:** what each source says, in our own words, cited.
- Do not write the author's own adjusted meanings.
- Do not invent extensions.
- Do not apply anything to the author's stories, and do not mention their fictional universe.

## The rule that matters most: our own words
**This repo is public on GitHub, and the books are copyrighted.**
- Write everything as paraphrase and synthesis.
- Use short quotations only: a phrase or a sentence where the exact wording matters (a coined term, a famous line). Each one is cited, and there should be few per file.
- Never reproduce lists, exercises or passages wholesale. Describe them.
- Run `python3 _dispatch/verbatim_check.py "<your file>"` from `Stories/Story_Structure/` after each file. **Target: FILE 8% or less.** That is the share of your file's words that sit inside 6-word runs copied from the source. Names and coined terms make up part of any score.

## The sources
These are local only and git-ignored. Never copy them anywhere else.
- **Folder:** `Stories/Story_Structure/source_reference (local only, not in git)/text/`
- **Truby:** `Truby - The Anatomy of Story (PDF pages).txt`. `{p.N}` marks the start of PDF page N. Cite as (Truby, PDF p. N).
- **Snyder:** `Snyder - Save the Cat (EPUB sections).txt`. There are no page numbers; cite by chapter title, e.g. (Snyder, ch. 4 "Let's Beat It Out!").
- **Harmon:** the two StudioBinder worksheet texts (`Harmon - ...`). Use web research too; see the Harmon assignment.
- **The author's composite master** (for the "In the composite" section): `Stories/Story_Structure/from CurrentNovelDocs/story-structure-definitions.md`.
- **The gap analysis** (what the master lacks): `Stories/Story_Structure/GAP ANALYSIS - sources vs definitions (2026-10-29).md`.

## What to write
**Every output file starts with a STATUS line:** `STATUS: IN PROGRESS (next: <section or step>)`, updated as you go, or `STATUS: COMPLETE`. Then the content.

**A chapter or topic extraction file** (for example `04 - Character.md`) has:
1. **Header:** title; a "Source:" line (author, book, chapter, PDF pages); and the line "Research extraction, 2026-10-29. The source's ideas in our own words; not the author's adjusted version."
2. **Every concept, technique, distinction, rule, step and warning in the chapter,** in the chapter's order. Each gets a sub-heading, a full explanation in your own words, and page citations.
   - Be complete. The author wants nothing important lost.
   - Cover the examples the source uses only briefly: name the work, and say in a line what point it illustrates.
3. **Exercises the chapter gives the writer:** describe what each asks the writer to do. Do not copy them.
4. **Terms introduced:** a glossary of the chapter's coined terms, each with a one-line meaning.

**A beat or step file** (for example `22 Steps/11 - Opponent's plan and main counterattack.md`) has:
1. `# <Beat name> (<Framework>, <step or beat number>)` and a "Source:" line with pages or chapter.
2. **What it is:** the source's meaning, in full, in your own words.
3. **How it works:** what the source says to do, what to avoid, its variations, and the examples it gives (briefly).
4. **Placement:** where it falls, in the source's own terms (percentages or pages if it gives them).
5. **Equivalents in other frameworks:** the matching beat in Snyder, Bell, Campbell, Truby, Harmon or Weiland, as far as you can establish them. Mark uncertain matches ⚠️.
6. **In the composite:** whether the author's master defines or uses this beat, and under what name. Give a pointer only, not a copy. Say "not yet in the composite" where that's the case.
7. **The author's adjusted meaning:** leave only the heading and the line "*To be drafted with the author (05:00-14:59 window).*"

## Rules
- Write only your assigned files, under `Stories/Story_Structure/`. Run no git commands that change anything.
- American English, plain language. Mark uncertainty with ⚠️.
- **Resumable:**
  - Create each file early and update its STATUS line as you go.
  - If you are resumed or are a replacement agent, read the STATUS lines of your files and continue from there. Never restart a completed file.
- **When done, reply with:**
  - your file list, each file's verbatim FILE score;
  - anything in your source that doesn't fit the template;
  - the three most important ideas in your part that the author's composite master lacks.
