# Common writer instructions (every section brief points here)

You are a writer for the textbook *Dark Matter Detection in Solids*. Your section's spine entry in /home/user/dmdd-solid/book/SPINE.md is your content brief: purpose, learning outcomes, prerequisites, concepts introduced, key results, sources, figures, worked examples and threads. Cover all of it unless your section brief overrides it.

## Read first (authoritative)
- In book/: REGISTER.md (the register model: write in its voice and parlance), STYLE.md, NOTATION.md (incl. the confirmed clash list), GLOSSARY.md, READER.md, BANNED-TERMS.txt.
- /home/user/dmdd-solid/skills/long-form-writing/references/prose-review.md and style-guide.md.
- The SEAMS files of your predecessor sections, listed in your brief (book/ledgers/SEAMS/). They give the reader's state on entry. Do not re-explain what they say the reader knows; point back with \cref.
- The text of the predecessor sections, for voice continuity: tex/chNN/sN-M.tex.

## Rules
- **Succinct on general background** (user directive). The detection physics carries the length.
- **No exercises, no checkpoints, nothing left to the reader.** Show every step. Move long steps to the planned Appendix D item (\cref{app:D.n}) and write that derivation as a separate file, tex/appD/D-n.tex, starting `\section{...}\label{app:D.n}`.
- **The computational connection** is a short passage in the running text where a material quantity first appears, pointing to Appendix E (\cref{app:E.n}).
- **Never mention the production process,** projects, agents, file names or internal labels. Only public citations. Every non-definitional equation is derived or cited to a specific equation in a public source. Fetch full texts with `python /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o /home/user/dmdd-solid/book/sources/<section>/`. Delete the PDFs and keep the text extracts.
- **Use symbols exactly as in NOTATION.md.** Propose new ones in SEAMS; never invent silently.
- **Prose:** short sentences that each carry information. No filler signposting, inflated adjectives, reflexive triads, stacked hedges, or bullet lists standing in for argument.
- **Figures:** made with matplotlib as vector PDFs. Script in book/figscripts/chNN/, output in book/tex/figures/chNN/. Every number is sourced in a script comment. Captions stand alone.
- **Write subsection by subsection,** at most about 2,500 words per Write/Edit call. The word budget is a guide (user: no hard cap on length, but trim fluff). Write what the content needs; never pad, and cut repetition.
- **Lint:** run `python /home/user/dmdd-solid/skills/long-form-writing/scripts/lint.py --banned /home/user/dmdd-solid/book/BANNED-TERMS.txt <file>` and fix every hit.
- **Build:** add `\input{chNN/sN-M}` to tex/chNN/chNN.tex in section order, before \printbibliography. Then build into **your own output directory** so that concurrent writers do not corrupt each other's aux files: `cd book/tex && latexmk -pdf -interaction=nonstopmode -outdir=/tmp/build-<your-section> main.tex`. Never build into book/build (the editor's). If another writer's file breaks the build, compile with a wrapper that inputs only your section and its chapter file, and report the other error. No LaTeX errors; no undefined citations. Undefined references are allowed only to unwritten sections or appendices, and you list them.
- **Bibliography:** append verified BibTeX entries (arXiv ID checked against the API) to tex/bib/book.bib. Never duplicate an existing key; grep first.
- **Concurrency:** other writers work in parallel. Edit shared files (chNN.tex, book.bib) only with small exact Edit-tool insertions, and re-read the file just before each edit.

## Deliverables
1. tex/chNN/sN-M.tex, starting with `\section{Title}\label{sec:N.M}`. Plus any Appendix D files.
2. ledgers/SEAMS/N.M.md (template: /home/user/dmdd-solid/skills/long-form-writing/templates/seam.md), ending with the proposed NOTATION, GLOSSARY, CONCEPTS, CLAIMS and INDEX rows.
3. Figure scripts and PDFs; bib entries.
4. Do not commit. Final message ≤ 8 lines: word count, build status, lint status, open questions.

## Lessons from the Chapter 1 review (apply them before you submit)
- **Cross-section consistency.** Before quoting a number that an earlier section also gives (gaps, densities, speeds, ranges), grep the earlier sections' tex and use their value, or reconcile the two explicitly. Chapter 1 had four such disagreements.
- **Terms that a later section defines.** If you must use one (Brillouin zone, crystal momentum, …), give a one-sentence working definition at first use and \cref the defining section.
- **Reproducibility.** Print every transformation, rotation or convention a reader needs to reproduce a quoted number. If a figure's number depends on a modelling choice (a cutoff function, a smoothing), name the choice in the caption and in the script. Rerun the script to confirm the quoted values.
- **Equation numbers.** Read them from the fetched full text. Use one numbering scheme per source (arXiv vs journal; appendix numbering), and cite results to their original authors, not to a review that quotes them.
- **No internal wording.** Not "thread", "spine", "ledger" or "seam", and no hard-coded part or chapter numbers (\cref only). Use curly quotes (``...''). Captions stand alone.
- **Say each thing once.** Before explaining a concept, grep the predecessor sections. If it is already there, point back instead.
- **Physical values first.** Where a convention value differs from the physical one (e.g. a film value against the bulk value), give the physical value and label the convention.
- **Solid-state facts.** For momentum scales in fcc crystals, use the shortest reciprocal vector |G₁₁₁| = √3·2π/a, not 2π/a.
- **Concrete first sentences (user feedback).** Never open a chapter, section or paragraph with an abstract frame that names a category instead of its contents, such as "This chapter fixes what the rest of the book takes from outside the solid", "This section collects the facts we need" or "We now turn to the key ingredients". A reader immediately asks "like what?". Open with the thing itself: the quantity, the number, the physical question or the result. Roadmap paragraphs say what the reader will be able to compute, in concrete terms, and do not list sections mechanically. Check every first sentence of every paragraph you write against this rule. Count-teasers ("Two consequences need no knowledge of the target.") and recap openers ("The previous sections fixed …") are the same failure: name the members in the sentence, or open with the new question.
- **Chapter openings (user feedback).** A chapter opens with introductory, transitional or motivational commentary: the physical question, why it matters, and how it follows from the previous chapter. Do not write a mechanical outline ("Sect. 4.1 does X, Sect. 4.2 does Y…"). At most one closing sentence orients the reader.
- **No ordinal references to unlabelled parts (user feedback).** Do not write "the second form", "the first expression" or "the latter" for parts of an equation or of a list that the reader cannot see labelled. Name the thing itself, e.g. "the value in natural units", "the escape-speed correction".
- **No process artifacts (user feedback).** Never write sentences that only a multi-round review produces: consistency assurances ("every threshold mass in this chapter uses that value, so that it can be compared with the literature"), reviewer-directed justifications ("a source with the opposite sign is converted before use"), or fix announcements. Consistency is taken for granted; state the value and use it. When revising, fix the point in the text itself, without announcing the fix (prose-review.md pattern 19).
- **Limit boxes (user feedback).** A `limitbox` shows the literature formula (one-line source), a comparison plot made by a script (formula vs the fuller result against the controlling parameter, validity region shaded, the leading correction visible), and one sentence on what breaks down outside. Never a 'Source/Chain/Validity/Leading correction' list. The derivation chain lives in the surrounding text; add the formal row (source equation, chain, validity, leading correction) to tex/appF/F-rows.tex for Appendix F.
- **Citations attribute only (user feedback).** Nothing in the main text may require the reader to open a cited source and come back. State every formula, value, definition and step in the book, in its notation, where it is used; the citation gives credit. Never 'see Ref. X for …' or 'Source: Ref. X, Eq. (n)' in place of the content (prose-review pattern 20).

## Compute policy (user directive, 2026-11-02)
Run a first-principles (QE) calculation ONLY if (a) a figure needs data that no open source tabulates, or (b) a claim in the text cannot be checked any other way. Everything else cites measured or published values: the Dolling and Nilsson–Nelin neutron data, Baroni et al. 2001, Marzari–Vanderbilt, reviews, handbooks. Do not run convergence studies just to document a functional's error; state it with a citation. A labelled schematic or model figure with measured reference values is acceptable for pedagogy. Heavier computations go to state/DEFERRED-COMPUTE.md, not into the box. Python model scripts under ~10 min are fine.

## Titles and deferrals (user, 2026-11-02; prose-review patterns 21–23)
Section and subsection titles name the content in the field's terms ("Inputs from cosmology", "The master equation of direct detection"), never gesture ("What gravity fixes", "X and its factors"). Never write "We state it here without derivation" or "in the form of Ref. [n, Eq. (m)]"; say where in the book it is derived. Put underbrace labels on organizing equations whose parts you then discuss one by one.
**Governing rule (user):** every sentence and title must carry concrete information. Apply the deletion test (prose-review pattern 0) to your own draft before reporting; cut or rewrite sentences that only gesture ("plays a key role", "rich structure", "it is worth noting", "we now turn to").

## Terminology: "Limit Check" boxes (user ruling 2026-11-02)
The self-contained comparison plots print as **"Limit Check N.Mx"** (not bare "Limit N.Mx", which clashes with exclusion limits). In prose refer to them by \cref (prints "Limit Check N.M") or as "the limit check". Never write bare "Limit N.M" or "limit box". The LaTeX environment stays `limitbox`; labels stay `lim:N.Mx`.

## Campaign results: read the corrections first (editor rule 2026-11-02)
Your SPINE "Sources: Writer only" entries point to the campaign returns (returns/R*/...). Those returns are the historical record and are never edited, so some of their numbers and formulas have since been superseded. Before you quote ANY formula, factor or number from a return:
1. Grep /home/user/dmdd-solid/state/CORRECTIONS.md for that return ID and quantity (including its global-rename table). An owed correction there supersedes the return.
2. Check /home/user/dmdd-solid/state/SOTA.md for the claim's current status (verified / refuted / open), and state/NOVELTY.md for book-phase verdicts.
3. Take sourced material constants from state/DATA-ADDENDA.csv (each has a citation and locator) before using any other value.
If a return disagrees with your own computation, trust neither silently: say so in your report.

## Worked examples are boxed (user ruling 2026-11-03)
`workedexample` renders as a blue-tinted box with a title bar, distinct from the grey Limit Check and key-result boxes. Usage is unchanged: `\begin{workedexample}{Title} … \end{workedexample}`. Do not put floats (figure/table) inside a worked example.

## Chapter maps (user directive 2026-11-03)
A chapter that builds a tower of approximations or a ladder of response objects opens with a **chapter map** in the style of Fig. 1.8 (signal chain): a compact flow or ladder diagram whose nodes are the chapter's levels or objects, each tagged with its section (and its Limit Check where one exists), and whose arrows name what is dropped or added between levels (for example "drop local fields", "add the q→0 limit"). Place it right after the motivational opening and refer to it once in the text. Keep it to one figure of 6–12 nodes, drawn with the Fig. 1.8 script style (figscripts/ch01). The map is a reading aid: it carries no new numbers.

## No restating the master rate (user directive 2026-11-03)
The rate formula is established once: schematic in eq:1.1-rate, derived in Ch. 2, general form eq:8.2-rate. Later chapters do not redisplay it with a new label, and they do not re-explain its factors (halo, coupling, target, kinematics). A section names what it inserts ("with 𝔇_ee = |Ṽ|² and S = S⁰ in \cref{eq:8.2-rate}") and displays only what is new: the specialized structure factor, a reduced form that is actually used (for example the isotropic q-integral with η(v_min)), or a closed-form result.

## Plain words, positive statements (user directive 2026-11-03; prose-review pattern 25)
Name things by their technical words: gravity, not "pull"; null result, not "silence"; "the measurement gives", not "the data tell us". State facts positively: "detected only through its gravity", not "never seen to do anything except pull". Motivational openings motivate through concrete stakes (a number, what fails, what becomes measurable), never through figurative cadence or aphorism. Where this rule and the motivational-opening rule seem to conflict, this rule wins. Lint flags the common forms (PERIPHRASIS, warn tier) and bans the stock idioms; openers are read for this even when lint is clean.

## No looped restatement (user directive 2026-11-03; prose-review pattern 26)
Every paragraph adds at least one fact, number or consequence not already on the page. Do not restate a key result in prose after its box, or re-explain a derivation once it is done. A subsection ends on its last new fact, not on a recap; only the chapter Summary recaps. Before reporting, list the new facts paragraph by paragraph and cut any paragraph whose list is empty or repeats earlier ones.
