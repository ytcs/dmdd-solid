---
name: long-form-writing
description: >
  Orchestrate the writing of a long technical manuscript (monograph, textbook, review, thesis-length report)
  that is far larger than any single agent can output: spine design, section-level writer agents,
  ledgers that carry state across agents, derivation verification, publisher style and anti-AI prose
  review, mock-reader review by the target audience, seam and cross-chapter consistency review, and a
  standalone-publication scrub. Use when the user wants a book, a long manuscript, lecture notes, or any
  document that needs many agents to write and must read as one coherent, public, pedagogical work.
---

# Long-form technical writing

You are the editor-in-chief of a book that no single agent can write. You do not write the book in one
context. You design its spine, keep its state in files, give every agent a narrow brief, and run reviews
until the parts read as one work by one careful author.

Two failures matter:
- **Fragmentation.** Each section is fine on its own, but notation drifts, concepts are used before they
  are defined, the narrative thread breaks at seams, and the same idea is explained three times in
  three voices.
- **Unearned smoothness.** Fluent prose hides skipped steps, wrong factors and claims nobody checked.

Everything below guards against one or the other.

## 0. Hard requirements (apply to every book unless the user overrides them)

1. **Standalone public document.** The book never mentions the process that produced it: no agents,
   rounds, briefs, internal file names, research-campaign labels, work-package numbers, ledger IDs or
   tool names. Every name, symbol and convention is defined inside the book. Citations go only to
   public literature. A reader holding only the book must be able to follow it.
   `scripts/lint.py --banned <project>/BANNED-TERMS.txt` enforces the term list; extend that list with
   every internal label the project used. See `references/standalone-scrub.md`.
2. **Publisher style.** Follow the house style of a major science publisher; the default is Springer
   monograph style (`references/style-guide.md`):
   - numbered parts, chapters, sections and equations;
   - equations punctuated as part of sentences;
   - symbols defined at first use;
   - consistent units and spelling;
   - figure and table captions that stand alone;
   - one citation style, with a bibliography per chapter (the default for book-length works; one master
     .bib file, rendered per chapter).
3. **Anti-AI prose.** Every section passes the prose review in `references/prose-review.md` (lint plus a
   human-style read): no filler signposting, no inflated adjectives, no reflexive triads, no stacked
   hedges, no paragraph that only restates the previous one, no bullet lists standing in for
   argument.
   Beyond avoiding AI patterns, the prose must sound like the field: plain, idiomatic writing in
   the register of named human-written expositions (REGISTER.md). The register check is part of every prose review.
4. **Concision.** Book, part, chapter and section titles are short noun phrases naming their content.
   There are no subtitles (unless the publisher requires one), no punchline or clever titles, and no
   epigraphs or quotations. Every sentence carries information and parses in one pass: each pronoun or other pointer has exactly one
   antecedent, written as a noun phrase in the same or the previous sentence, and a technical object keeps
   one name throughout (prose-review pattern 27). Do not split a sentence when the new sentence would
   have to open on a pointer back.
   Content is arranged so that each section is motivated by what precedes it and each step follows from
   the last.
5. **Pedagogy for the stated reader.** Write for the persona in the project's `READER.md`, by default a
   first-year PhD student with minimal prerequisites. Build every result step by step from what has
   already been established. Nothing is left to the reader: no exercises, no checkpoints, no "verify
   that" or "left to the reader"; every step is in the text or in an appendix it points to. "It can be
   shown", "standard manipulations" and "straightforward algebra" are forbidden unless the steps are
   given in an appendix the text points to.
6. **No rugs.** Every equation that is not a definition is either derived in the book, step by step, or
   cited to a specific equation in a public source. Every number traces to a calculation shown or
   cited. The derivation checker re-derives each step independently (§5).
7. **Citations attribute; they never carry the argument.** A citation gives credit and lets a reader verify. The main text never depends on it: every formula, value, definition and step the reader needs is stated in the book, in the book's notation, at the point of use. Never write "see Ref. [12] for the definition", "the formula of Ref. [12, Eq. (5)]" without stating it, or "Source: Ref. [12], Eqs. (77)–(78)" as a substitute for content. The reader must never have to leave the book and come back to follow the thread. (Internal pointers to an appendix holding a long derivation are allowed, because the book itself contains the step.)

## 1. Project layout

Create this structure (an example; adapt the names, but keep the roles):

```
book/
  SPINE.md            # parts → chapters → sections, each with purpose, learning outcomes, prerequisites, length budget
  READER.md           # target reader persona(s) and assumed prerequisites
  STYLE.md            # project style sheet: publisher, spelling, units, citation style, voice; extends references/style-guide.md
  REGISTER.md         # register model(s): named human-written expositions in the field, and the distilled parlance, idioms and
                      #   sentence patterns the book should match (references/prose-review.md, "Language and register")
  NOTATION.md         # one symbol, one meaning; first-use location for each symbol
  GLOSSARY.md         # terms, with their defining section
  BANNED-TERMS.txt    # internal labels that must never appear in the book (one regex per line)
  ledgers/
    CONCEPTS.md       # concept → defining section → sections that use it (dependency DAG)
    CLAIMS.md         # every nontrivial claim/equation → derived-in (section/eq) or source (public citation, eq no.)
    THREADS.md        # narrative threads: where each is opened, advanced, and closed
    SEAMS/<sec>.md    # exit state of each section: what the reader now knows, symbols introduced, open threads, promises made
    REVIEWS/<sec>/    # every review report for that section (kept, never edited)
  briefs/<sec>.md     # writer brief per section
  tex/                # main.tex, part/chapter files, one file per section (\input), one master .bib (rendered per chapter)
  build/              # compile logs
```

Source material (research notes, derivations, data) lives outside `book/`. Writers read it, but it never
appears in the book by name.

## 2. Spine design (do this yourself, before any writing)

The spine is the most important artefact. Design it from the content, not from a generic template.

1. **Map the material.** List the results to be taught and their logical dependencies (a DAG). Mark
   which ones the reader must already know (READER.md), which are built in the book, and which are
   cited only.
2. **Order for pedagogy.** Topologically sort the DAG so that no concept is used before it is
   introduced, then choose among valid orders the one with the best narrative arc. A foundations part
   comes first, then the core framework, then applications, then the path to practice.
3. **Define units of writing.**
   - A section is what one writer agent produces in one assignment. Size it at 3,000–6,000 words, so
     that a writer emitting about 1,500–2,500 words per tool call finishes in a few calls.
   - A chapter is 4–10 sections.
   - Record a word budget for every section; the total sets the book length.
4. **For every section, record:**
   - its purpose (one sentence);
   - learning outcomes (2–5 testable statements: "the reader can derive / compute / explain …");
   - its prerequisite concepts, each pointing to a section;
   - the concepts it introduces;
   - the key equations or results;
   - its source material;
   - its figures and tables;
   - its worked examples;
   - the narrative threads it opens, advances or closes;
   - its word budget.
5. **Two-axis material.** When content is naturally a matrix (for example excitation type × interaction
   type), choose one axis for chapters. Give every chapter the same internal template along the other
   axis, and add an atlas chapter or table at the start of the part that maps every cell to its
   section. Never let the matrix produce two half-explanations of the same cell.
6. **Choose the register model(s).** Name one to three human-written expositions in the field whose voice the book should match. Have an agent read them and distil REGISTER.md: terms of art, characteristic phrasings and idioms, how estimates and physical pictures are introduced, sentence rhythm, and a short list of example sentences. Writers read it before every section, and prose reviewers check against it.
7. **Seed the ledgers from the spine:** the CONCEPTS DAG, the THREADS opening and closing points, and the
   planned NOTATION.
8. **Have the spine reviewed** by one structural reviewer (dependency violations, gaps, duplicated
   coverage, budget realism) and one reader-persona agent ("would I know enough at each chapter
   start?"). Revise before writing.

## 3. Orchestration

The output limit binds per agent response, so **no agent writes more than one section**, and a writer
composes its section through several tool calls that each append one subsection to the section file. Be
explicit in the brief: "write subsection by subsection; each Write/Edit adds at most ~2,500 words".

Per section, in dependency order (sections whose prerequisites are finished can run in parallel):

| Step | Agent | Reads | Writes |
|---|---|---|---|
| 1. Brief | editor (you) | SPINE, ledgers, predecessor SEAMS | briefs/<sec>.md (template: `templates/writer-brief.md`) |
| 2. Draft | writer | brief, STYLE, NOTATION, GLOSSARY, predecessor SEAMS, source material | tex/<sec>.tex; SEAMS/<sec>.md; proposed rows for CONCEPTS/CLAIMS/NOTATION/GLOSSARY |
| 3. Lint | script | tex | REVIEWS/<sec>/lint.txt (`scripts/lint.py`) |
| 4. Derivation check | verifier (isolated) | tex, cited sources, NOTATION | REVIEWS/<sec>/derivation.md: each equation CHECKED / WRONG / GAP (sympy where possible) |
| 5. Style and prose | prose reviewer (isolated) | tex, STYLE, `references/prose-review.md` | REVIEWS/<sec>/prose.md |
| 6. Mock readers | 2+ reader personas (isolated, no source material, only the book so far) | the book up to and including this section | REVIEWS/<sec>/reader-N.md (`references/reader-review.md`) |
| 7. Revise | the original writer, or a fresh reviser | all reviews | tex, SEAMS (revision log appended to REVIEWS/<sec>/revision.md) |
| 8. Accept | editor | reviews, revision log, build | ledger rows merged; section marked ACCEPTED in SPINE |

Rules:
- **Isolation.** Reviewers do not see each other's reports. Mock readers never see source material,
  briefs or ledgers: only the book text, so they experience exactly what a real reader will.
- **The editor merges ledgers.** Writers propose rows; only the editor writes NOTATION, GLOSSARY,
  CONCEPTS and CLAIMS. A proposed symbol that collides with an existing row is renamed before
  acceptance.
- **A WRONG or GAP verdict blocks acceptance.** So does a mock reader marking a step "lost", unless the
  editor records why the step stands, for example that it is resolved two paragraphs later and the
  reader confirms this on re-read.
- **Build every time.** LaTeX must compile with no undefined references, labels or citations.
- **Parallelism.** Use the host's multi-agent tool (a workflow tool if the user has opted in to
  orchestration, otherwise a subagent tool). Keep the number of concurrent writers modest, so the
  editor can still merge ledgers between waves.

## 4. Cross-section, cross-chapter and book-level reviews

- **Seam review**, after both sides of a seam are accepted. One agent reads the last third of section n
  and the first third of section n+1, plus both SEAMS files. It checks that every promise is kept, that
  nothing is introduced twice or explained in two voices, that notation and tone are continuous, and
  that the transition is natural.
- **Chapter review**, after all sections of a chapter are accepted. One agent reads the whole chapter for
  narrative arc, redundancy, the balance between rigour and intuition, how well the worked examples cover the
  learning outcomes, and the chapter summary.
- **Part and thread review.** One agent per narrative thread, following THREADS.md, reads only the
  sections on that thread and checks that it is opened, developed and closed coherently.
- **Book-level audits**, run near the end:
  - notation (every symbol has exactly one meaning, and is defined before its first use: automated
    plus manual);
  - terminology and glossary;
  - cross-references and equation references;
  - citation integrity (each cited equation exists in the source);
  - the standalone scrub (§0.1);
  - the full prose lint;
  - a full mock-reader pass of each part by fresh persona agents.
- Reviews produce reports. The editor issues revision briefs, and nothing is fixed silently.

### Language rounds on an existing text
A pass that changes only the language (removing machine tells, fixing sentence construction) runs as follows.
- **Pilot first.** Edit one section yourself, have an independent agent review it, and put two or three of its
  before/after pairs (good and bad) into the editors' brief as calibration.
- **Editors** work one unit (a chapter or a few) each and read every paragraph whole, flagged or not;
  `scripts/tells.py` and `scripts/binding.py` only rank where to look first. Each editor runs
  `scripts/content_guard.py <base> <files>` (no symbol, number, citation or label may appear in or disappear
  from a file), the lint and a compile, and logs the most instructive changes.
- **Independent reviewers**, who did not edit the unit, check every changed sentence for fidelity (claim,
  strength, qualifiers, the facts), for pattern 27 and for over-repair, and they sample at least one
  unchanged paragraph in ten for misses. A unit with more than 2 misses per 1000 words gets a second pass.
  Reviewers form their own view of the diff before reading the editors' logs.
- **Content problems found on the way** are not fixed by editors: each is written up (location, old text,
  proposed text, evidence) and goes through a proposal and an independent review before it is applied.
- **Detector counts are not the measure of success.** A ranker count barely moves when antecedents are
  named; report before/after examples and the reviewers' miss rates instead.

## 5. Correctness

- The derivation verifier redoes every non-definitional step from the previous line. It uses sympy for
  algebra, dimensional analysis on every displayed result, and limiting cases where the text claims
  them. It reports any factor of 2, π, sign or convention drift against NOTATION.
- Numbers come from scripts kept outside the book. The book states the inputs, so a reader can
  reproduce them.
- Claims of priority or novelty are checked against the literature before they enter the text, and are
  stated modestly with their scope.
- When the source research is still under review, a section that depends on an unrefereed result is
  marked BLOCKED in SPINE, and is not drafted until the result clears.

## 6. Pedagogical devices

Use these in proportion to the persona:
- a chapter opening that motivates the chapter and connects it to the previous one (not a mechanical outline);
- worked examples with every step shown;
- boxed key results;
- a "where this is used later" pointer at the end of foundational sections;
- a running example system carried through the book;
- figures that show mechanisms, not decoration.

## 7. Finishing

Final steps:
- front matter (preface written last, reading guide with dependency chart, notation list);
- back matter (appendices, glossary, index entries proposed by each section's writer and merged by the
  editor, bibliography);
- a full build;
- the book-level audits;
- a final cold read of the complete book by two fresh persona agents, front to back.

Report to the user: page count, open issues, and any section accepted with an editor override, with its
reason.

## References

- `references/style-guide.md`: publisher (Springer-type) house style for technical monographs.
- `references/prose-review.md`: the anti-AI prose checklist, and what the lint catches.
- `references/reader-review.md`: mock-reader protocol and report format.
- `references/standalone-scrub.md`: what "standalone public document" means in practice.
- `templates/`: writer brief, seam file, review report, spine entry.
- `scripts/lint.py`: prose, style and banned-term lint for LaTeX or Markdown sources.
- `scripts/tells.py`: word- and phrase-level machine tells (pattern 28); candidates, not verdicts.
- `scripts/binding.py`: sentence-construction ranker for pattern 27 (needs spaCy and an English model).
- `scripts/content_guard.py`: checks that a language-only edit left math, numbers, citations and labels unchanged.
