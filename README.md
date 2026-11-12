# Dark-Matter Detection in Solids

Source of the three-volume book on the theory of dark-matter scattering and absorption in solid-state targets.

| Volume | PDF |
|---|---|
| I. Foundations | book/releases/vol1-foundations.pdf |
| II. Signals and Detection | book/releases/vol2-signals-and-detection.pdf |
| III. Computations | book/releases/vol3-computations.pdf |

## Layout

| Path | What |
|---|---|
| book/tex/ | LaTeX source: vol1.tex, vol2.tex, vol3.tex (volume drivers), preamble.tex, macros.tex, chNN/ and appX/ (one file per section), front/, figures/, bib/, xref/ (generated cross-volume labels) |
| book/figscripts/ | one script per figure or generated table, with the cached data it reads; figures are written to book/tex/figures/ |
| book/tools/ | build helpers (below) |
| book/STYLE.md | the book's style sheet; it extends skills/long-form-writing/references/style-guide.md |
| book/NOTATION.md | symbol table, one meaning per symbol; source of the List of Symbols (App. B.1) |
| book/GLOSSARY.md | term → definition → defining section |
| book/READER.md, book/REGISTER.md | target reader; register model of the prose |
| book/BANNED-TERMS.txt | words that must not appear in the book (read by the lint) |
| skills/long-form-writing/ | writing and review rules, prose checklists and checking scripts |

## Building

Requirements: TeX Live with latexmk and biber, Python 3. Then

    cd book && ./build.sh            # PDFs in book/build/
    cp build/vol1.pdf releases/vol1-foundations.pdf   # and likewise for vol2, vol3, for a release

`build.sh` regenerates the per-volume symbol lists, builds the three volumes, refreshes the cross-volume labels in
tex/xref/ until they are stable, and reports page counts, undefined references and citations, and any figure or table
that lands between the parts of a box broken across pages. A release build has none of these, and no overfull box
(`grep -c 'Overfull' build/vol*.log`).

## Tools

| Tool | Use |
|---|---|
| book/tools/chapcheck.sh chNN | compile one chapter or appendix alone, with its true number; reports undefined references, duplicate labels and overfull boxes |
| book/tools/xref.py, volumes.py | cross-volume labels and the volume map (called by build.sh) |
| book/figscripts/appB/gen_B1.py, book/tools/split_B1.py | List of Symbols from NOTATION.md (gen_B1 after editing NOTATION.md; split_B1 is called by build.sh) |
| book/tools/check_notation.py | every symbol printed in the tex has a row in NOTATION.md |
| book/tools/floatsplit.py | floats inside broken boxes (called by build.sh) |
| book/tools/qe/ | environment and job wrapper for the few figure scripts that rerun Quantum ESPRESSO (see ENV.md) |
| skills/long-form-writing/scripts/lint.py | banned terms, filler, long sentences: `lint.py --banned book/BANNED-TERMS.txt FILE.tex` |
| skills/long-form-writing/scripts/tells.py | word-level machine tells (candidates) |
| skills/long-form-writing/scripts/binding.py | sentence construction: pointers without one antecedent, garden paths, heavy subjects (needs spaCy and en_core_web_sm) |
| skills/long-form-writing/scripts/content_guard.py | after a language-only edit: no math, number, citation or label added or lost (`content_guard.py <base commit> FILES`) |

## Changing the book

- Write and edit to book/STYLE.md and the skill's references (style-guide.md, prose-review.md: patterns 0–28,
  especially 27, sentence construction). Run lint.py, tells.py and binding.py on every changed file and read
  each flagged sentence; the scripts rank candidates, they do not replace reading the paragraph.
- A new symbol gets a NOTATION.md row; then run gen_B1.py. A new term gets a GLOSSARY.md row.
- Labels are stable identifiers; refer with \cref, never by a typed number.
- A correction of physics or a number is checked by someone other than its author before it goes in. A change of
  language only is checked with content_guard.py.
- Build with build.sh and check the report before copying PDFs to book/releases/.
