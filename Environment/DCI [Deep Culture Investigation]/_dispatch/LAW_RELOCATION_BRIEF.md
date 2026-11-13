# Brief: move the removed law avenues into Libra and Capricorn

Saved before launch, 2026-11-10.

**Background.**
- DCI researches law only in Libra and Capricorn (author, 2026-11-10). **Libra takes "the letter of the law"**: what the law says, and how it is applied as written. **Capricorn takes "the spirit of the law"**: what law is for, and how people relate to it beyond its wording. The author notes the two "can often tend to be two different things".
- An earlier cleanup removed the law avenues from the ten other signs' avenue files, but deleted them instead of moving them. The author's rule is to relocate, not delete. So every removed law avenue now moves to Libra or Capricorn.
- The removed material has been recovered exactly, one file per sign, in `<SCRATCH>/law_recovery/NN - <Sign>.removed.md`. Each entry gives the section, the heading, and the clauses that were removed or changed, separated by " | ". A clause that was only reworded, with no law in it, also appears there; ignore those.
- For full context, the pre-cleanup files are at `<SCRATCH>/law_recovery/NN - <Sign>.orig.md`.

`<SCRATCH>` = `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-Literature-books-CurrentNovelDocs/3d728365-b74f-46ea-8b81-16f2bbd67a4d/scratchpad`

**Read first:**
- The two homes, so the new material fits them: `<DM>/Shared/Avenues/07 - Libra.md`, section 0, the block "The letter of the law"; and `<DM>/Shared/Avenues/10 - Capricorn.md`, section 8, the block "The spirit of the law".
- `<DM>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/DCI [Deep Culture Investigation]`.

**Your job:**
1. For each of your signs, go through its `.removed.md` file and pick out **every item that is about law**: statutes and named laws, regulations, legal ages, constitutions and legal rights, court cases and rulings, courts, judges, juries and trials, lawyers and litigation, legal doctrines, legal status and recognition, treaties as legal instruments, legal claims and settlements, police, prisons and sentencing, criminal-justice statistics, the author's law-based measures, and sources about law. **Miss nothing.**
2. Sort each item:
   - **Letter of the law (Libra):** what the law says or requires, codes, statutes, cases, courts, procedure, legal status and recognition, rights as written, contracts, regulations, legal ages, legal doctrines.
   - **Spirit of the law (Capricorn):** what a law is for, its legitimacy, obedience and defiance, enforcement and policing, punishment and its purpose, prisons, mercy, pardons and discretion, trust in courts and police, settling things outside the law.
   - An item that fits both goes in both.
3. Write each item as a short avenue in plain words: what it is, keeping the specific name, date and place. Keep every *(check)* mark that belonged to it. Show which concept it came from and how it bears on that concept. For example, under "From Aries, autonomy": "informed-consent law: who may decide for a patient (bears on autonomy)".
4. **Write to one staging file only:** `<SCRATCH>/law_recovery/relocated_<your letter>.md`, with this layout:

```
# Law avenues relocated from <signs>, 2026-11-10

## The letter of the law (for Libra)
### From <Sign>
- **<concept> (<heading>):** item; item; item.

## The spirit of the law (for Capricorn)
### From <Sign>
- **<concept> (<heading>):** item; item.
```

Group by sign, then by concept, keeping the source file's order.

**Rules:**
- American English. Short, plain sentences.
- Native, Indigenous or Aboriginal, never "Indian", in your own words. Published titles and names keep their wording.
- No South Asian works or communities.
- Research only. Nothing in-world, nothing after 2026.
- Don't edit any file other than your staging file. No git. No web search.

**Report back:**
- How many items went to each side, per sign.
- Anything you weren't sure was law, and what you did with it.
- Anything you left out, and why.
