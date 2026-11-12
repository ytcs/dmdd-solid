# House style for technical monographs (Springer-type default)

Projects may override any item in their STYLE.md. Where a publisher's own author instructions are
available (e.g. Springer's svmono class and "Instructions for Authors"), they take precedence.

## Information content
- Every sentence and title must carry concrete information: a fact, number, equation, definition, named object or argument step. Apply the deletion test (prose-review pattern 0); low-content "Claude-speak" is cut or rewritten to name the thing.

## Titles
- Book, part, chapter and section titles are short noun phrases (typically 1–5 words) that name the
  content. No subtitles unless the publisher requires one, no colon-joined pairs, no questions, puns or
  punchlines, and no epigraphs.
- A title names the content in the field's terms ("Inputs from experiment", "The Navier–Stokes
  equations"), never gestures at it ("What the data fix", "The rate and its factors", "Putting it
  together"). Test: the reader can predict the section's central result from the title.
- Organizing equations whose parts the text discusses one by one carry underbrace labels on those parts.
- Deferred derivations point inside the book ("derived in Chapter 2"), never to a source's equation number.

## Structure
- Front matter: title page, preface, contents, list of symbols or notation, acronyms.
- Body: parts (optional), chapters, sections, subsections, numbered decimally (Chapter 3, Sect. 3.2,
  Sect. 3.2.1). Do not number below the third level; use run-in headings instead.
- Every chapter begins with a short introductory paragraph (the question, why it matters, how it connects to the previous chapter; motivational or transitional commentary, not a mechanical section-by-section outline) and ends with a summary and
  references (per-chapter or one global bibliography: pick one). No problems or exercises.
- Appendices are lettered (Appendix A). Long derivations moved out of the main text go there and are
  pointed to explicitly.

## Equations
- Number every displayed equation that is referred to, as (3.12), by chapter. Refer to it as "Eq. (3.12)"
  in running text, or "(3.12)" where unambiguous. Be consistent.
- Equations are part of sentences: end them with a comma or full stop as grammar requires.
- Define every symbol at first use, in the sentence that introduces the equation, or in a "where …"
  clause directly after it.
- Vectors in bold upright or with arrows (pick one). Operators with hats, or explicitly declared.
  Use upright d for differentials, e and i if the style sheet says so, and upright text subscripts
  (E_\mathrm{g}, not E_g, when g is a label and not an index).
- Units: state the unit system once, e.g. "SI units unless stated". Give
  values in SI or the field's conventional units, with a thin space between number and unit (1.17 eV).

## Text
- Choose one spelling convention (American or British) and keep to it.
- Sentence construction (prose-review pattern 27): every pronoun, *such*, *both*, *the former/latter* and
  definite noun phrase has exactly one antecedent, written as a noun phrase, in the same or the previous
  sentence. Repeat the noun rather than risk two candidates. A technical object keeps one name. Relational
  nouns (*difference*, *mismatch*, *shift*, *missing*, *in between*) carry their arguments. No reduced
  relatives that read as a main verb, no subject heavier than about eight words, no chain of three or more
  prepositional phrases.
- Use "we" for the author and reader working together. Avoid "I". Avoid addressing the reader as "you",
  unless the style sheet allows it.
- Abbreviations are defined at first use in each chapter if chapters may be read independently, and
  listed in the front matter.
- Number style: words for one to nine in prose, numerals with units and in technical counts.
- Lists only for genuinely enumerable items (assumptions, steps of an algorithm, conditions). Never for
  argument.

## Figures and tables
- No figure or table may land between the parts of a boxed environment (worked example, key result, check
  box) that breaks across pages. Hold deferred floats while a box is set and release them when it ends, and
  forbid top floats on the page where a box ends; verify on every build by recording each box's page span.
- Every figure and table is cited in the text before it appears, and is numbered by chapter (Fig. 3.4,
  Table 3.1).
- Captions stand alone: a reader who sees only the figure and caption knows what is plotted, in what
  units, and for which parameters.
- Axis labels carry quantity and unit. The same quantity uses the same symbol as in the text.
- Prefer vector graphics. Every plotted number traces to a script.

## Citations
- One style throughout: numbered [12] or author–year (Smith 2020).
- **Per-chapter bibliographies are the default for book-length works.** Each chapter ends with its own
  numbered reference list, in order of first citation within that chapter (as Springer edited and
  monograph volumes commonly do). A source cited in several chapters appears in each of them.
  Implement this with one master .bib file, using biblatex `refsection` per chapter or `chapterbib`, so
  that entries are maintained once. A book-wide bibliography is used only if the project's STYLE.md asks
  for it.
- Cite specific equations or sections when using a result: "[12, Eq. (5)]". The citation is attribution only: state the result itself in the text, so the reader never needs the source to follow the argument.
- Cite preprint identifiers alongside the journal reference when both exist.
- Never cite anything a public reader cannot obtain.

## Cross-references
- Use labels; never hard-code numbers.
- Write "Sect. 4.3", "Chap. 7", "Fig. 2.1", "Table 5.2", "Appendix B", following the publisher's
  abbreviations, consistently.
