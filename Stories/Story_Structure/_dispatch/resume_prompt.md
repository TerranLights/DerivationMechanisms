# Resume prompts (after a usage cutoff)

Run `bash _dispatch/check_status.sh` from `Stories/Story_Structure/` first.

**Same session, agent still known.** Send the agent:
> The usage window has reset. Continue your assignment under `_dispatch/brief.md` from the STATUS lines of your files. Don't restart completed files.

**New session, or the agent can't be reached.** Start a fresh general-purpose agent with this prompt:
> You are replacing Agent <ID> on a research extraction that was cut off. Read `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Stories/Story_Structure/_dispatch/brief.md` and your row in `assignments.md` (both binding). Some of your files exist. Read each one's STATUS line and continue from there, and create any files that don't exist yet. Never restart a file marked COMPLETE. Reply as the brief asks.

**If the source texts are missing** (`source_reference (local only, not in git)/text/`), recreate them from the originals in `CurrentNovelDocs/reference/character-methodology/source-books/long-term_reference/` and `Documents/Doll-Fi/writing guides/Dan Harmon cycle template worksheets/`:
- Truby PDF: `pdftotext -layout`, with `{p.N}` markers at page breaks.
- Snyder EPUB: spine order, with `{section N: file}` markers.
- StudioBinder PDFs: `pdftotext -layout`.

If anything here is unclear, ask the coordinator.
