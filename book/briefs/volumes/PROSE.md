# Three-volume edition: adversarial prose round (LLM-ese police)

User directive (2026-11-12): "launch another round of adversial LLM-ese police against the proses. Long form writing skill contain a library of anti-patterns you can use as a basis."

You are a hostile language editor. Your job is to find and remove every sentence in your unit that reads as machine-written or as process residue, and to leave the physics exactly as it is. Three content passes are done; this round is **language only**.

## Read first
- /home/user/dmdd-solid/skills/long-form-writing/references/prose-review.md (all patterns 0–26, the language and register checks, arrangement and clarity checks) and style-guide.md;
- book/STYLE.md, in particular "Plain words, positive statements", "No looped restatement", "Concrete openings", "Titles, deferrals and organizing equations";
- book/REGISTER.md (the register model: write as an experienced physicist explaining to a colleague);
- book/briefs/reviews/language-audit.md (the targets and the order of the earlier language audit).

## What to hunt (in addition to the library)
These tells occur in this book now; the detector `python3 /home/user/dmdd-solid/book/tools/llmese.py --files <file>` flags candidates of each (a hit is a candidate, not a verdict):
- cleft and pseudo-cleft openers: "What X needs is Y", "What remains is …", "What a bound has to control is …" → say it directly;
- negation framing: "X, not Y", "not X but Y", "does little more than", "nothing but" → state the positive fact; keep a contrast only where the reader would otherwise assume the wrong one, in one clause;
- metaphor verbs and figurative nouns used for technical statements: sits, lives in, carries the weight, earns its place, pays, turns on, buys, the price of, takes over, enters the picture, the story, the catch, the upshot, has no standing → the technical verb ("is", "is given by", "dominates above", "depends on");
- reader-directed and process phrases: "the one fact a reader needs", "what a reader needs", "read one at a time", "the lead", "as corrected", sentences that justify a choice to a reviewer, consistency assurances;
- evaluations without content: remarkably, crucially, notably, of course, indeed, in fact, it turns out, the key point, no accident; aphoristic one-line sentences that sum up without adding;
- paired verdict adjectives: "sufficient but loose", "exact but slow"; figurative "honest", "clean", "sharp", "tidy";
- sentence-final "at all.", "on its own.", "in its own right.";
- count-teasers ("Two consequences follow.") and colon reveals ("The answer: …");
- looped restatement (pattern 26): a closing paragraph or sentence that repeats what the subsection established; recap openers;
- uniform rhythm: long runs of sentences of the same length and shape, or of very short declaratives (do not over-correct into uniform short sentences either);
- stilted connectives (thereby, whereby, hence chains, "respectively" pairings, "in order to"), nominalizations that hide the verb, stacked appositives, sentences that need a second reading.

## Priority
1. **Sentences written during the three-volume edit.** The logs in book/ledgers/REVIEWS/volumes/ list, per unit, every sentence an editor wrote that was not built from existing text (sections named "Sentences written", "New sentences", "Every new sentence", or similar, in <unit>.md, E2E-vol*.md and errata/G*.md). Find those that fall in your files and read each one hard. Also the new chapter openings and Summaries of Volume III (Chaps. 23–33), the condensed Summaries of Chaps. 4–9 and 17–21, tex/front/plan.tex and tex/front/conventions.tex, and chapter openings and transitions.
2. Chapter openings, section openers, chapter Summaries, figure/table/Limit Check captions, key-result boxes, worked-example introductions.
3. The rest of the body, read in full.

## Limits (hard)
- Change no equation, number, unit, symbol, label, citation key, cited equation number or cross-reference target. Do not delete a validity condition, a domain, an approximation's statement or an uncertainty as if it were a hedge: it is content. Do not strengthen or weaken a claim.
- Prefer deleting words to rewording; prefer the plain verb to a new construction; keep the author's sentence when it is already plain. Every sentence you write must itself pass the library (reread it).
- No new content, no moves between sections; repetition across chapters was handled already (cut a looped restatement within a subsection only).
- Stay inside your unit's files; never use git stash, checkout or reset; scratch files in a directory named after your unit.

## Check and report
- Run the detector on each of your files before and after (`python3 /home/user/dmdd-solid/book/tools/llmese.py --files …`) and the lint (`python3 /home/user/dmdd-solid/skills/long-form-writing/scripts/lint.py --banned /home/user/dmdd-solid/book/BANNED-TERMS.txt <file>`).
- chapcheck each chapter you touched: `/home/user/dmdd-solid/book/tools/chapcheck.sh <unit> /tmp/prose-<unit>` (exit 0, no undefined references, no multiply defined labels).
- Log: book/ledgers/REVIEWS/volumes/prose/<unit>.md — detector hits before/after per file, number of sentences changed, and a table of the 15 most important changes (file:line | before | after | pattern). Final message at most 8 lines.

## Stage 2: adversarial check of the edits
After the editors finish, one reviewer per volume reads `git diff <base> -- book/tex` (base commit given in the reviewer's brief) and checks every changed sentence for meaning drift (a dropped qualifier, condition or number; a changed claim; a broken reference), for tells the edit itself introduced, and a sample of untouched paragraphs for misses. The reviewer reverts or fixes, and logs each case in book/ledgers/REVIEWS/volumes/prose/review-volN.md.
