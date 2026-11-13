# DCI: how to resume after a cutoff

**The sign-completion run (2026-11-11)** has its own resume procedure. Open `_dispatch/SIGN_COMPLETION_PROGRESS.md` and run `python3 _dispatch/qa_sign.py --all`.

**Research on targets:**
1. Open the results root's `MASTER TRACKER.md`, then the target's `PROGRESS TRACKER.md`. They say which stage, unit and sign is current.
2. Check every output file in progress: `grep -rn "^STATUS:" <results root>/Units <results root>/Targets`.
   - `in progress, section K of M`: relaunch the same brief (saved in the results root's `_dispatch/`), telling the agent to keep sections 1 to K and continue from K+1.
   - `not started`, or a missing file: relaunch the brief as is.
   - `done, not yet verified`: run `Templates/T7_Verification_Checklist.md`.
3. Update both trackers before starting anything new.
4. Stage 6 (divergence) resumes only between 05:00 and 14:59, with the author.
