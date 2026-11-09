# Part II writer addendum (read after COMMON.md)
- Read the "## Part II — Channels" header block and the Chapter 8 header in SPINE.md. The status tags (REF, VER, EST, CL, GAP, "new") are defined there. They are writer-side guidance only: never print them.
- **Limit boxes.** Each "Limit N.Mx" in your SPINE entry is a `limitbox`, and the box IS a self-contained comparison plot (STYLE.md). Each box needs:
  - a figure script in figscripts/chNN/;
  - one row in tex/appF/F-rows.tex with the formula in book notation, its 𝔗 point and the plot spec.
  - a label `lim:N.Mx`, given as the second optional argument, `\begin{limitbox}[Title][lim:11.2a]` (or a `\label` at the start of the body, before any `\captionof`); refer to it only with `\cref{lim:...}` (prints "Limit 11.4"), never by a hard-coded number.
  The 𝔗 orders count powers in the RATE (NOTATION ruling). Relabel any planned row that counts amplitude order; see ledgers/REVIEWS/partII/editor-notes.md.
- **Open problems.** Each "Open problems (exact gaps)" field names items your section must state in its open-problems passage, one home per label. Write them as physics, never as labels: no LE-/XG-/DC- identifiers. Each chapter gets one nuisance table (in its last section).
- **Prior commitments.** Read ledgers/REVIEWS/partII/editor-notes.md. It lists commitments earlier chapters and appendices made to your section (values, symbols, checks). Honor them.
- **Framework.** Chapter 8 (tex/ch08/) is drafted and under review; use its framework and notation as written: the master rate (8.2), exact relations and the 2×-geometric-mean bound (8.3), screening (8.4), 𝔗 (8.5), sectors (8.6), final-state response (8.7) and nuisances (8.8). App. E.14–E.27 specify the deferred calculations: point to them by content (\cref{app:E.n}) wherever a quantity "is computed".
- **Compute policy.** Cite published values. A QE run is allowed only if no open data exist AND the claim cannot otherwise be checked, and then only through code/run-heavy.sh. Python model scripts under 10 min are fine.

## Terminology: "Limit Check" boxes (user ruling 2026-11-02)
The self-contained comparison plots print as **"Limit Check N.Mx"** (not bare "Limit N.Mx", which clashes with exclusion limits). In prose refer to them by \cref (prints "Limit Check N.M") or as "the limit check". Never write bare "Limit N.M" or "limit box". The LaTeX environment stays `limitbox`; labels stay `lim:N.Mx`.

## Campaign results: read the corrections first (editor rule 2026-11-02)
Your SPINE "Sources: Writer only" entries point to the campaign returns (returns/R*/...). Those returns are the historical record and are never edited, so some of their numbers and formulas have since been superseded. Before you quote ANY formula, factor or number from a return:
1. Grep /home/user/dmdd-solid/state/CORRECTIONS.md for that return ID and quantity (including its global-rename table). An owed correction there supersedes the return.
2. Check /home/user/dmdd-solid/state/SOTA.md for the claim's current status (verified / refuted / open), and state/NOVELTY.md for book-phase verdicts.
3. Take sourced material constants from state/DATA-ADDENDA.csv (each has a citation and locator) before using any other value.
If a return disagrees with your own computation, trust neither silently: say so in your report.

## Chapter maps (user directive 2026-11-03)
A chapter that builds a tower of approximations or a ladder of response objects opens with a **chapter map** in the style of Fig. 1.8 (signal chain): a compact flow or ladder diagram whose nodes are the chapter's levels or objects, each tagged with its section (and its Limit Check where one exists), and whose arrows name what is dropped or added between levels (for example "drop local fields", "add the q→0 limit"). Place it right after the motivational opening and refer to it once in the text. Keep it to one figure of 6–12 nodes, drawn with the Fig. 1.8 script style (figscripts/ch01). The map is a reading aid: it carries no new numbers.

## No restating the master rate (user directive 2026-11-03)
The rate formula is established once: schematic in eq:1.1-rate, derived in Ch. 2, general form eq:8.2-rate. Later chapters do not redisplay it with a new label, and they do not re-explain its factors (halo, coupling, target, kinematics). A section names what it inserts ("with 𝔇_ee = |Ṽ|² and S = S⁰ in \cref{eq:8.2-rate}") and displays only what is new: the specialized structure factor, a reduced form that is actually used (for example the isotropic q-integral with η(v_min)), or a closed-form result.

## F-row format (user ruling 2026-11-03)
Each row of tex/appF/F-rows.tex (landscape longtable, tab:F-rows) follows one format:
- **Column 1 (Formula):** a short name of the formula plus its equation reference, e.g. `Elastic nuclear recoil, \cref{eq:1.3-ERmax,eq:1.3-vmin}`, and the limit label where one exists, `(\cref{lim:11.4a})`. Write the formula inline only when it is one short expression; never more than about two lines. A literature form with no book equation goes at the head of the Approximation-chain column ("Published form: ...").
- **Column 5 (Leading correction):** begins with the approximate size in bold via `\Fsize{...}`, e.g. `\Fsize{$\le$\,\SI{10}{\percent} for $q < 0.48\,q_{\mathrm{BZ}}$}.`, then the explanation. Take the number from the book (the row, the Limit Check and its caption, the figscripts log); never invent one. If the book gives none, write `\Fsize{unsized}` and add the row to "## Unsized leading corrections (App. F)" in state/DEFERRED-COMPUTE.md.
- Rows are separated by `\midrule`; keep every `\cref` and `\cite`.

## Plain words, positive statements (user directive 2026-11-03; prose-review pattern 25)
Name things by their technical words: gravity, not "pull"; null result, not "silence"; "the measurement gives", not "the data tell us". State facts positively: "detected only through its gravity", not "never seen to do anything except pull". Motivational openings motivate through concrete stakes (a number, what fails, what becomes measurable), never through figurative cadence or aphorism. Where this rule and the motivational-opening rule seem to conflict, this rule wins. Lint flags the common forms (PERIPHRASIS, warn tier) and bans the stock idioms; openers are read for this even when lint is clean.

## No looped restatement (user directive 2026-11-03; prose-review pattern 26)
Every paragraph adds at least one fact, number or consequence not already on the page. Do not restate a key result in prose after its box, or re-explain a derivation once it is done. A subsection ends on its last new fact, not on a recap; only the chapter Summary recaps. Before reporting, list the new facts paragraph by paragraph and cut any paragraph whose list is empty or repeats earlier ones.
