# Three-volume edition: sentence-construction round (binding and parse depth)

User directive (2026-11-12): "Your sentence construction requires too many levels of parsing or too ambiguous in the analytical syntax sense. Carry out the sentence construction review and go through the whole book carefully to weed out any machine constructions."

The earlier prose round removed word-level tells. It missed the main one, which is syntactic. In this round you are a copy editor who reads like a parser: for every sentence you find each pointer and what it resolves to, and the point at which the parse is fixed. The physics, the numbers and the structure of the book stay exactly as they are.

## Read first
- /home/user/dmdd-solid/skills/long-form-writing/references/prose-review.md, **pattern 27** (end of file), in full, with its worked before/after; patterns 0, 25 and 26 for context.
- /home/user/dmdd-solid/book/STYLE.md, last section ("Sentence construction: binding and parse depth").
- /home/user/dmdd-solid/book/REGISTER.md (the register: an experienced physicist explaining to a colleague).
- The calibration section at the end of this brief.

## What to fix
Binding failures (a pointer without exactly one antecedent noun phrase in the same or previous sentence):
- pronouns *it, its, they, them, their, this, that, these, those, which* with two or more candidates, or whose intended antecedent is neither the nearest candidate nor the subject of the previous clause;
- *such X*, *all the same*, bare *this/that* standing for a whole proposition or a predicate, pointers to something stated only negatively ("not the momentum" → "the missing momentum");
- *both, either, the former, the latter, that of, those of, the one, the other, the rest*, unless they pick from one coordinated noun phrase in the same sentence;
- *the X* used before X has been introduced (in this section or by an explicit pointer back);
- relational nouns missing their arguments: *difference, mismatch, ratio, shift, excess, deficit, remainder, correction, denominator, missing, in between, cost, gain*;
- several names for one object in a paragraph ("a state that…", "the state in between", "it"): pick the field's term, already used in the book, and keep it;
- chains of sentences that each open on a pointer back, holding one proposition together by anaphora.
Parse-depth failures:
- reduced relatives that read first as the main verb ("a phonon emitted or absorbed a moment later takes it…");
- coordination whose scope can be read two ways;
- subjects longer than about eight words, or containing a clause, before the main verb;
- chains of three or more prepositional or genitive phrases;
- appositions that define their head noun with a second set of pointers;
- dangling modifiers ("Closing the contour there, the integral is…");
- sentences over about 35 words that need more than one parse.

## How to fix
- Repeat the noun instead of a pronoun with two candidates. A pronoun is fine when it has exactly one candidate and that candidate is the subject of the previous clause or the nearest noun of the right number.
- Name the object with the term the book already uses for it (grep the chapter and NOTATION.md), and keep that term.
- Give relational nouns their arguments; introduce an object before the first *the*.
- Merge fragments that only anaphora holds together; split a sentence that needs two parses, but only so that each new sentence opens on a named noun, never on a pointer back.
- Reorder within a paragraph when that resolves the binding. Do not move material between paragraphs or sections.
- **Fixing one axis must not break the other**: no 50-word sentences with nested relatives to avoid a pronoun; no robotic triple repetition of a long noun phrase where one pronoun with one candidate would do. Reread every sentence you write against pattern 27 and against the register. A good human physicist would have written it.

## Hard limits
- No new physics, claim, number, symbol, equation, citation or figure. Do not change an equation, number, unit, symbol, label, citation key, cited equation number or cross-reference target. Do not drop a qualifier, validity condition, domain or uncertainty; do not strengthen or weaken a claim.
- You may repeat a symbol or expression that already appears in the same file (to replace a pronoun), and add `\cref` to an existing label. Do not use a symbol before the text defines it.
- Run the content guard on every file you changed, against the base commit given in your assignment: `cd /home/user/dmdd-solid/book && python3 tools/invariant.py <BASE> tex/<file>.tex …`. Any `STOP` line must be fixed before you finish (an item new to the file or one that disappeared). `note` lines are allowed.
- Stay inside your unit's files. Never use git stash, checkout, reset or commit. Scratch files only in /tmp/claude-0/-home-user-dmdd-solid/d1725f47-7573-51dd-bf4b-00f15cc471f7/scratchpad/binding-<unit>/.
- Edit with exact string replacements (a Python script with old/new pairs that asserts each old string occurs once works well for many edits); never rewrite whole files.

## Method
1. Run the ranker on your files: `python3 /home/user/dmdd-solid/skills/long-form-writing/scripts/binding.py tex/<file>.tex` (a flagged sentence is a candidate, not a verdict; it misses many failures, so it only tells you where to look first). Record the summary (`--summary`).
2. Read **every paragraph whole**, flagged or not: body text, section openings, captions, key-result and Limit Check boxes, worked examples, footnotes, chapter summaries, prose cells of tables. Binding failures cross sentence boundaries, so patching single sentences does not fix them. For each sentence, list (mentally or in scratch) its pointers and their antecedents; rewrite those with zero or several candidates and those that need a second parse.
3. Apply the edits, run invariant.py, the lint (`python3 /home/user/dmdd-solid/skills/long-form-writing/scripts/lint.py --banned /home/user/dmdd-solid/book/BANNED-TERMS.txt <file>`; fix only hits your edits introduced), the ranker again, and chapcheck for each chapter or appendix you touched: `/home/user/dmdd-solid/book/tools/chapcheck.sh <chNN|appX> /tmp/binding-<unit>` (exit 0, no undefined references, no multiply defined labels).
4. Log to /home/user/dmdd-solid/book/ledgers/REVIEWS/volumes/binding/<unit>.md: per file the ranker count before/after and the number of sentences changed; then a table of the 15 most instructive changes (file:line | before | after | failure fixed). Final message to the lead at most 8 lines: files, sentences changed, ranker before/after, invariant and chapcheck status, anything you could not resolve.

## Calibration (from the reviewed pilot, Sect. 2.4; full review in ledgers/REVIEWS/volumes/binding/pilot-review.md)
The pilot reviewer found three kinds of editor error. Avoid all three.
1. **Meaning loss when removing a negation.** "a state that conserves crystal momentum but not energy … a final state that conserves both" was first rewritten as "an intermediate state with the same crystal momentum and a different energy … a final state with the energy and crystal momentum of the initial state plus the photon". That version dropped the claim that energy is not conserved in the intermediate step, and "the initial state plus the photon" made the initial state electron-only. Accepted version: "The photon first takes the system from the initial state to an intermediate state, in a transition that conserves crystal momentum but not energy. Emitting or absorbing a phonon then takes the system from the intermediate state to a final state, and the whole process, from the initial to the final state, conserves both energy and crystal momentum." When you restate a negated pair, keep each claim explicit; check that the physics is unchanged.
2. **One name, two referents.** The rewrite made "energy denominator" mean $E_i - E_m$ in one paragraph and $1/(E_i - E_m)$ in another. When you give an object its name, check every other use of that name in the section and chapter.
3. **Over-repair.** "The principal-value part collects the off-shell intermediate states and is real; the principal-value part shifts energies…" replaced a pronoun that had one candidate and was the subject of the previous clause. Keep such pronouns: "…and is real; it shifts energies…". The same applies to "of the fraction" three times in two sentences and to "the condition fails, and the condition is replaced by". Repeat a noun only when the pronoun has two candidates or the antecedent is not a noun phrase.
Good change, for comparison: "the decaying state has gone somewhere, and the golden-rule rate fixes both how fast and how sharply in energy" → "the probability that leaves the decaying state ends in the continuum, and the golden-rule rate fixes both the speed of the decay and the width of the line". The vague clauses became named noun phrases, so "both" picks from one coordinated phrase, and nothing is lost.
Other accepted examples: "Iterating it once" → "Iterating the Lippmann–Schwinger equation once" (two candidate equations); "The two terms of Eq. (split)" → "The delta term and the finite part of Eq. (split)" (the equation has four terms); "Inserting both into" → "Inserting both orderings into" (*both* picked from three sentences back); "the correction" → "the $\delta''$ term" (never introduced as a correction); "a ground level $a$" → "$i_{\mathrm{T}}$", the name used everywhere else (an intended symbol unification shows as a STOP in invariant.py; list it in your log).
Expected yield: the pilot changed about 60 sentences in 4,600 words of prose, and its reviewer still found 3 misses per 1000 words in untouched text. Read slowly.
