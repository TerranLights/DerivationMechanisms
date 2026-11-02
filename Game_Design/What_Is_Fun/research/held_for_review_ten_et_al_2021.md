STATUS: held for author review
# Held for review: Ten, Kaushik, Oudeyer and Gottlieb (2021)

## Why this file is separate
Job 1 set this paper aside under the brief's rule on South Asian sources. Its only reason was one co-author's name. The study's content has no South Asian tie: it is a lab experiment by teams at Inria (Bordeaux, France) and Columbia University (New York), run on U.S. online participants. On November 1, 2026, the author asked for it to be written up as its own file, to be looked at later. Until then, the synthesis does not cite it.

## Source
- Alexandr Ten, Pramod Kaushik, Pierre-Yves Oudeyer and Jacqueline Gottlieb, "Humans monitor learning progress in curiosity-driven exploration," *Nature Communications* 12, article 5972 (2021). https://doi.org/10.1038/s41467-021-26196-w
- Open access under a Creative Commons Attribution 4.0 license. Full text read from Europe PMC (PMC8514490). The supplementary figures, including the subjective ratings, were not opened.
- Local copy of the publisher's PDF, unaltered: `sources/Ten_et_al_2021_Humans_monitor_learning_progress.pdf`. The repository's blanket rule on PDFs keeps it out of git.
- Data: https://osf.io/k2yur/. Code: https://github.com/flowersteam/Humans-monitor-LP
- Evidence kind: MEASURED.

## The study
- **Participants:** 400 recruited on Amazon Mechanical Turk (208 female, 187 male, 5 undisclosed; ages 19-71, mean 36). Eighteen were excluded for always giving the same answer, leaving 382.
- **Pay:** a flat $1 for 45-60 minutes, regardless of performance. The authors chose this to keep money out of the choices.
- **Task:** four "monster families." On each trial the participant picks a family, sees one monster, guesses which of two foods it likes, and is told whether the guess was right.
  - A1, easiest: one feature decides the food.
  - A2: two features vary, one decides.
  - A3, hardest learnable: a combination of two features decides.
  - A4: random. The food is assigned by chance, so it cannot be learned.
- **Procedure:** 15 required trials on each family, then 250 trials of free choice, then ratings.
- **Two groups:**
  - **Free choice** (N = 186): told only to complete 250 trials, with no goal.
  - **Instructed** (N = 196): told to "try to maximize your learning about all the 4 families," with a test at the end.
- **Measures:**
  - which families people chose;
  - how many of the three learnable families each person mastered (13 of 15 correct);
  - a self-challenge index, from 0 (always the easiest family) to 1 (always the hardest);
  - a model fitted to each person's choices, weighing recent accuracy (percent correct) against recent learning progress (how much accuracy changed).

## Findings
1. **Most people with no goal leaned toward the easy family, but a sizable minority challenged themselves.**
   - Free-choice time split: A1 33.0%, A2 21.4%, A3 22.2%, A4 23.4% (chance is 25%).
   - Instructed: A1 20.6%, A2 19.3%, A4 36.9%. They spent the most time on the random family.
   - Even with no goal, 64.5% mastered at least two families and 29.6% mastered all three, close to the instructed group's 74.5% and 36.6%.
   - In the authors' words, "a subset of participants spontaneously adopted intermediate self-challenge strategies and maximized learning regardless of external instructions."
2. **Learning was best at a middle level of self-challenge.**
   - Final performance against the self-challenge index forms an inverted U. A model with a squared term beat a straight line (adjusted R² = 0.159).
   - People who did not master all three fell short in opposite ways. In the instructed group they over-challenged themselves; in the free-choice group they under-challenged themselves.
3. **People track their own progress, not just their success rate.**
   - A model using both accuracy and learning progress fit choices better than either one alone, and better than random choice. It fit best for 70.7% of instructed and 74.0% of free-choice participants.
   - The two sensitivities were uncorrelated (r = −0.08 and 0.06), so they look like separate drives.
   - The instruction changed how much people weighed accuracy, but not how much they weighed progress.
4. **Tracking progress steers people away from the task that can't be learned.**
   - People driven mainly by accuracy kept moving to the random family once they had learned the others. From about trial 80 on, they chose it over the hardest learnable family.
   - People driven mainly by progress did not.
   - By the end, 64.3% of the progress-driven mastered all three families, against 35.0% of the accuracy-driven.
5. **An external goal both helped and hurt.**
   - Telling people to learn for a test raised self-challenge and final performance.
   - It also led some to "labor in vain on a random activity rather than learnable activity."
   - The authors credit the benefit to autonomy: the goal named the end but left the choice of activity to the participant.
6. **Interest followed time spent.** In the free-choice group, reported interest was "proportional to their time allocation." This comes from a supplementary figure that was not opened.

## Bearing on the author's claims
- **H1, the unit (refines).**
  - With no goal and no pay for performance, a sizable minority chose hard but learnable challenges.
  - The free-choice average leaned slightly toward the easiest task, so effortful challenge is not everyone's default.
- **H3, payoff (confirms, refines).**
  - Progress itself drew people back, with no material reward tied to it. That supports an inner payoff.
  - The payoff that steered choices was the change in performance, felt along the way, more than success at the end. This matches Job 1's refinement 4: the payoff can run during the effort.
- **H4, proportion (refines).**
  - Effort that could never pay off (the random family) was avoided by those who tracked progress.
  - Tasks already mastered gave no progress and were left too.
  - What drew people was the rate of return on effort, not the size of one reward. H4 could be restated in those terms.
  - Over- and under-challenge both lowered the outcome.
- **H4a, work versus play (refines).**
  - An imposed goal made people try harder.
  - It also led some to keep working at a task that gave nothing back. That fits the author's "too little reward is work," with the twist that the person did it willingly because of the goal.
- **H5, chains (confirms, weakly).** Progress-driven people moved from task to task as each was mastered, a simple chain. The authors link this to how sustained interest develops (Hidi and Renninger).
- **H6, fit (confirms).** People differed a lot in how much they weighed accuracy against progress, and that difference predicted what they chose and how much they learned.

## Limits
- It measures choice and learning, not fun or enjoyment. Choosing an activity is not the same as finding it fun.
- The task is a short, simple categorization game, played once, by online workers paid a flat $1.
- The paper is a little inconsistent about how many people mastered nothing: 8 and 9 in a figure caption, 5 and 5 in the Methods. It also gives p = 0.048 next to t = −3.910, which looks like a typo. Neither affects the main results.
- It complements Baranes, Oudeyer and Gottlieb (2014), cited in Job 1 (F7.3): there, people's conscious estimates of their own progress were poor. Here, their choices track progress anyway, so the progress signal may work below awareness.

## What the author may decide
- Whether this paper may be cited in the synthesis.
- Whether the rule on South Asian sources covers authors by name, or only works tied to South Asian nations in content. The brief says "works or authors"; the standing ruling says works.
