# STYLE (project style sheet; extends skills/long-form-writing/references/style-guide.md, which it overrides where they differ)

## House
- Springer monograph conventions on the LaTeX `book` class (tex/preamble.tex). British or American: **American spelling** throughout.
- Voice: "we" for author and reader together; never "I"; do not address the reader as "you".
- **No exercises, problems, checkpoints or tasks for the reader. Nothing is left to the reader** (user directive). Every step is written out in the text or in Appendix D, and the text points to it. Worked examples are demonstrations.
- No epigraphs, no subtitles, no colon titles. Titles are short noun phrases.
- Each chapter opens with a short introductory (motivational, transitional) paragraph and closes with a summary section; then its references.

## Units and numbers
- Natural units ħ = c = k_B = 1 unless stated; physical values in conventional units with a thin space: \SI{1.17}{eV}, \SI{0.3}{GeV.cm^{-3}}.
- Numbers: words for one to nine in prose; numerals with units and in technical counts.

## Mathematics
- Vectors bold italic (`\vect{q}`); operators with hats (`\op{H}`); upright d, e, i (`\dd`, `\ee`, `\ii`); upright text subscripts (`E_{\mathrm{g}}`, macro `\Eg`).
- Number every displayed equation that is referred to; refer as "Eq. (3.12)" via `\cref`. Equations are punctuated as part of the sentence.
- Every symbol is defined at first use and is listed in book/NOTATION.md (one symbol, one meaning). Propose new symbols; never invent silently.
- Fourier, sign and normalisation conventions follow Appendix A (from the campaign CONVENTIONS, made standalone).

## Structure and devices
- Literature formulas recovered as limits go in the `limitbox` environment: the formula with a one-line source citation, a comparison plot (literature formula vs the fuller result against the controlling parameter, validity region shaded, leading correction visible), and one sentence on what breaks down outside it. No 'Source/Chain/Validity/Leading correction' procedure list in the box; the chain is in the text and the formal record is in Appendix F (user directive).
- Key results in `keyresult`; worked examples in `workedexample`.
- Computational connection: where a material quantity first appears, a short passage in the running text says how it is computed and points to the method chapters of Volume III (Chaps. 23–29); no dedicated "how to compute" subsection.
- Running example: silicon. Contrasts: GaAs (polar, direct), Ge (heavier, indirect), Al (superconductor), NiO (antiferromagnet), one Dirac material.

## Citations
- biblatex numeric, **one bibliography per chapter** (refsection=chapter) from tex/bib/book.bib. Cite specific equations: `\cite[Eq.~(5)]{key}`. arXiv identifiers alongside journal references. Only public sources.
- Keys: firstauthorYEARfirstword, lowercase (e.g. `lindhard1954properties`).

## Cross-references
- Labels: `chap:N`, `sec:N.M`, `eq:N.M-short`, `fig:N-short`, `tab:N-short`, `app:X`. Never hard-code numbers. "Sect.", "Chap.", "Eq.", "Fig.", "Table", "Appendix" (cleveref, preamble).

## Files
- One file per section: tex/chNN/sN-M.tex, starting with `\section{Title}\label{sec:N.M}`; chapters \input accepted sections. Section files contain no preamble.
- Build: `cd book/tex && latexmk -pdf -outdir=../build main.tex` must finish with no undefined references, labels or citations.
- **Forward references:** use the planned labels (`sec:N.M`, `app:X`, `app:X.n`) with \cref even if the target is not written yet; undefined references to unwritten sections are allowed during drafting and are listed in the build report. The final build has none.
- **Number density:** `\nd` (script n, mathalpha boondoxo): `\nd_\chi`, `\nd_e`.
- **Worked examples:** `\begin{workedexample}{Title}\label{we:N-short}` (numbered by chapter; refer with \cref).
- **Appendix numbering:** an appendix section written ahead of its predecessors is preceded by `\setcounter{section}{n-1}` in appX.tex so that it prints with its planned number; the counter lines are removed once all sections exist.
- **Concrete openings.** First sentences of chapters, sections and paragraphs state concrete content (a quantity, number, question or result), never an abstract frame naming a category ("this chapter fixes what…", "we collect the facts…"). **Chapter openings are introductory and motivational, not outlines** (user, 2026-11-01): they set the physical question, why it matters, and how the chapter connects to what came before and what follows, in connected prose. At most one closing sentence orients the reader; never a section-by-section list.
- **Register (user, 2026-11-01).** The book's voice follows its register model, Lin's TASI lectures (arXiv:1904.07915), with Kahn & Lin (arXiv:2108.03239) and one condensed-matter exposition as secondary models. The distilled usage is in REGISTER.md; prose reviews check against it.
- **Citations attribute, they do not carry content (user, 2026-11-01: "citations is for credit attribution purposes and nothing in the main thread should require the reader to context switch e.g. jump to read something from cited source and back. The limit boxes were a violation of this").** Every formula, value, definition and step the reader needs is stated in the book at the point of use, in the book's notation. A citation gives credit (with equation number for precision) and never replaces content: no 'see Ref. X for …', no 'Source: Ref. X, Eq. (n)' standing in for a statement. Internal pointers to an appendix derivation are allowed.
- **Γ typography (editor, 2026-11-02):** rates and widths are italic `\varGamma` (Γ_w, decay rates); upright `\Gamma` is reserved for the zone-center point. Existing text is swept at each chapter's revision. The Euler gamma function is upright `\Gamma(z)`, always written with its argument (book-wide practice: 10.5, 21.7, 22.3, C.20).
- **Basis positions:** bold 𝛕_κ; plain τ is imaginary time. Basis structure factor S^{bas}(G).

## Titles, deferrals and organizing equations (user, 2026-11-02)
- Titles name the content in the field's terms. Bad: "The event rate and its factors", "What gravity fixes". Good: "The master equation of direct detection", "Inputs from cosmology". Test: a reader can predict the section's central result from the title and find it in an index.
- No self-narrating or provenance sentences ("We state it here without derivation, in the form of Ref. [1, Eq. (8)]"). When a derivation is deferred, point inside the book: "We will derive this in the chapters that follow."
- Organizing equations whose parts the text discusses one by one carry underbrace labels (halo, coupling, target, kinematics).
- **Information content (governing rule):** every sentence and title must carry concrete information. Apply the deletion test (prose-review pattern 0): if deleting a sentence loses no fact, number, equation, definition, named object or argument step, cut it or make it name the thing.

## Terminology: "Limit Check" boxes (user ruling 2026-11-02)
The self-contained comparison plots print as **"Limit Check N.Mx"** (not bare "Limit N.Mx", which clashes with exclusion limits). In prose refer to them by \cref (prints "Limit Check N.M") or as "the limit check". Never write bare "Limit N.M" or "limit box". The LaTeX environment stays `limitbox`; labels stay `lim:N.Mx`.

## Worked examples are boxed (user ruling 2026-11-03)
`workedexample` renders as a blue-tinted box with a title bar, distinct from the grey Limit Check and key-result boxes. Usage is unchanged: `\begin{workedexample}{Title} … \end{workedexample}`. Do not put floats (figure/table) inside a worked example.
- Display equations must fit the text width with margin to spare: break long ones with split/multline at a binary operator, or name a sub-expression. The final figure check also scans the log for overfull \hbox in display math.

## Chapter maps (user directive 2026-11-03)
A chapter that builds a tower of approximations or a ladder of response objects opens with a **chapter map** in the style of Fig. 1.8 (signal chain): a compact flow or ladder diagram whose nodes are the chapter's levels or objects, each tagged with its section (and its Limit Check where one exists), and whose arrows name what is dropped or added between levels (for example "drop local fields", "add the q→0 limit"). Place it right after the motivational opening and refer to it once in the text. Keep it to one figure of 6–12 nodes, drawn with the Fig. 1.8 script style (figscripts/ch01). The map is a reading aid: it carries no new numbers.

## No restating the master rate (user directive 2026-11-03)
The rate formula is established once: schematic in eq:1.1-rate, derived in Ch. 2, general form eq:8.2-rate. Later chapters do not redisplay it with a new label, and they do not re-explain its factors (halo, coupling, target, kinematics). A section names what it inserts ("with 𝔇_ee = |Ṽ|² and S = S⁰ in \cref{eq:8.2-rate}") and displays only what is new: the specialized structure factor, a reduced form that is actually used (for example the isotropic q-integral with η(v_min)), or a closed-form result.

## Plain words, positive statements (user directive 2026-11-03; prose-review pattern 25)
Name things by their technical words: gravity, not "pull"; null result, not "silence"; "the measurement gives", not "the data tell us". State facts positively: "detected only through its gravity", not "never seen to do anything except pull". Motivational openings motivate through concrete stakes (a number, what fails, what becomes measurable), never through figurative cadence or aphorism. Where this rule and the motivational-opening rule seem to conflict, this rule wins. Lint flags the common forms (PERIPHRASIS, warn tier) and bans the stock idioms; openers are read for this even when lint is clean.

## No looped restatement (user directive 2026-11-03; prose-review pattern 26)
Every paragraph adds at least one fact, number or consequence not already on the page. Do not restate a key result in prose after its box, or re-explain a derivation once it is done. A subsection ends on its last new fact, not on a recap; only the chapter Summary recaps. Before reporting, list the new facts paragraph by paragraph and cut any paragraph whose list is empty or repeats earlier ones.
