# Resuming the glossary harvest

1. Run `bash Glossary/_dispatch/check_status.sh` from the Derivation Mechanisms repo root.
2. For each area whose file is missing or not `STATUS: COMPLETE`:
   - if its agent is still reachable, resume it with SendMessage: "You were cut off. Read your harvest file's STATUS line and rows, and continue. Follow `Glossary/_dispatch/brief.md`."
   - otherwise launch a replacement with: "Read and follow `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Glossary/_dispatch/brief.md`. You are the agent for area <X> in `assignments.md` (same folder). Your harvest file may already exist: read its STATUS line and rows and continue; never restart."
3. When all ten are COMPLETE, run the merge stage (to be written: `merge_brief.md`).

# Resuming the merge
- Check each `_merge/<range>.progress.md` STATUS line (ranges in `merge_assignments.md`).
- Resume an unfinished agent with SendMessage, or launch a replacement: "Read and follow `.../Glossary/_dispatch/merge_brief.md`. You own range <X> in `merge_assignments.md`. Read your progress file and letter files and continue; never restart."
- After all six: run the post-merge script (category index and see-also stubs; coordinator).
