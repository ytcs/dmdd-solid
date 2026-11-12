# Book production: resume point (paused 2026-11-02 at user request; updated after the final round)

## State
- **Part I (Ch1–8): ACCEPTED.** (in the ch11 gate PDF). Accepted appendices: A, C.1–C.9, C.18, D.1–D.28, E.1–E.13 (E.14–E.27 specs revised; second pass pending).
- **Ch10 + D.29–D.30, Ch11 + D.31–D.32: ACCEPTED**, ledgers merged. Gate PDF: releases/book-gate-ch11.pdf (924 pp; Ch1–8, 10, 11). Keep ≤ 2 PDFs (superseded; see Ch12 line).
- **Ch12 + D.33–D.34: ACCEPTED**, ledgers merged. Gate PDF: releases/book-gate-ch12.pdf (1010 pp; Ch1–8, 10–12). Keep ≤ 2 PDFs (ch11, ch12 now). Off-diagonal G≠G′ ≈ 1.2–1.4 (EPM-RPA estimate) in text; full calc in DEFERRED-COMPUTE.
- **Ch13 + D.35–D.37: ACCEPTED** (2026-11-06), ledgers merged. Gate PDF: releases/book-gate-ch13.pdf (1096 pp; Ch1–8, 10–13); the only gate PDF kept. Review substance: the screening correction was rebuilt (0.3–2.6, replacing [0.4, 1.8]); the cold Si edge is on the Stanford 0.5 K fit (0.36 MeV reach is a band, ×15); the nonadiabatic ZPR is 8 meV (6.1 + 1.9). Campaign ledgers updated (CORRECTIONS, SOTA, LOOSE-ENDS LE-179/180, NOVELTY N7, CONTROLS C8).
- **Ch14 + D.38: ACCEPTED** (2026-11-06), ledgers merged. Gate PDF: releases/book-gate-ch14.pdf (1162 pp; Ch1–8, 10–14). Review substance: neutron no-go qualified (model-independent only); Neyman fixed-amplitude factor 1.99/2.73 reconciled with Centers et al.; MnF₂ ω_M/ω_E 4π fix; the summary sits in its own file s14-summary.tex. Pending light pass: X_αβ → strain-symbol rename in 14.2.
- **Ch15 + D.39–D.40: ACCEPTED** (2026-11-06), ledgers merged. Gate PDF: releases/book-gate-ch15.pdf (1216 pp; Ch1–8, 10–15). Review substance: the conserving edge response (DC-41) replaces the bare-bubble values; cut y < 3; one Al constant set (v_F = 6.753e-3); spin-current ALP absorption in clean singlet SCs verified with caveats (NOVELTY N-book-15); sheet screening credited to Lasenby–Prabhu.
- **Ch16 + D.41–D.42: ACCEPTED** (2026-11-06), ledgers merged. Gate PDF: releases/book-gate-ch16.pdf (1308 pp; Ch1–8, 10–16). Review substance: the Dirac ε_bg correction derived (D.41); ZrTe₅ on the whole 11.8 meV row (108 ev, 1.5e-40, factor 5200–6400); DM–TLS 2.3e-2 (C_l); graphene v_D 3.02e-3; corrected published values (Blanco Eq. (6), Du f-sum, Liu Born validity, Meißner and Qureshi factors). Pending light pass: Ch7 and E.20 ZrTe₅ 15.6 → 11.8 meV (LE-186).
- **Ch17: ACCEPTED** (2026-11-06), ledgers merged; PART II COMPLETE. Gate PDF: releases/book-gate-ch17.pdf (1358 pp; Ch1–8, 10–17). Ch12 Migdal erratum (verdict PARTLY): domain qualifiers only, no number changed; the diagonal soft-limit form holds for q ≳ 2 q_BZ; boost identity below ~0.75 keV; the band between is unsized and carries ≥ 99.8 % of the Si Migdal rate at 0.42–1 MeV (LE-188, DC-book-12).
- **Ch9 (atlas):** write last, after Ch10–16.
- **Part III (18–22), App B, App F completion, D.43–D.47:** not started. Briefs: briefs/sections/PARTII.md + COMMON.md; one writer per section (pattern in briefs/sections/10.x.md).
- **Book-wide audit: DONE** (ledgers/REVIEWS/title-audit.md: 53 titles renamed, 40 deferral sentences fixed, 5 equations underbraced, 13 deletion-test cuts). Appendices were checked by lint/grep only; a fuller deletion-test read of App A–E remains optional.

## Pending cross-cutting lists
- ledgers/REVIEWS/partII/editor-notes.md: commitments to later sections, and the App E pass-2 fix list.
- ledgers/REVIEWS/ch0N/editor-notes.md: per-chapter rulings.
- state/DEFERRED-COMPUTE.md: book-phase additions at the end.
- state/NOVELTY.md: book-phase findings (verified/unverified) at the end.
- Final passes: the citation audit (items logged in the editor notes), the final figure check (SPINE production directive), App B notation, and E pass 2.

## Rules in force
COMMON.md, PARTII.md, STYLE.md; the compute policy (cite literature; QE only if no open data and the claim is otherwise unverifiable); the information-content rule (prose-review pattern 0) and patterns 21–23; ≤ 2 read-along PDFs; stage with a safe add (exclude files > 5 MB, source PDFs and build output; campaign/ is gitignored, so add with -f).

## Added 2026-11-02 (late session)
- Boxes print as **"Limit Check N.Mx"** (user ruling); environment limitbox and labels lim: are unchanged.
- Writers must check state/CORRECTIONS.md, SOTA.md and DATA-ADDENDA.csv before quoting campaign returns (COMMON.md). The corrections audit of the written chapters is DONE and applied (ledgers/REVIEWS/corrections-audit.md). Remaining: the s6-5 ε_e/ε_h → E_e/E_h rename.
- App E pass 2 list: partII/editor-notes.md (E.17, E.18, E.19 items added).
- **Done 2026-11-03:** Ch12 R25 wording, the light passes (8.5, 8.8, 6.5, Limit Check labels, Ge a in Ch5) and App E pass 2. Still open: s11-1 l.168 Ge a = 5.652 → 5.658 (rerun the script).
- **Ch13:** 13.1–13.6 DRAFTED (+ opening, map, D.35–D.37). Notes in ledgers/REVIEWS/ch13/editor-notes.md. Next: 13.7–13.9 (briefs: copy briefs/sections/13.6.md pattern; 13.9 closes the chapter with the nuisance table and summary), then the Ch13 review. Widen the NOTATION row for M^± to the three-argument dimensionless form at the merge.
- **Late-session directives:**
  - "Limit Check" naming;
  - worked examples boxed in blue;
  - chapter maps (Ch2–6, 8, 10–12 done);
  - no restating the master rate;
  - "rung" banned (prose-review pattern 24);
  - App F format (landscape, name plus equation reference, bold size first);
  - title page: "Claude, edited by To Chin Yu".
- **Final passes, in order, once all chapters are ACCEPTED:**
  1. the citation audit;
  2. the **language-only audit** (briefs/reviews/language-audit.md; prose-review pattern 25 and the STYLE "Plain words, positive statements" rule);
  3. the final figure check.

## Session 2026-11-06
- New container: install latexmk, biber and the texlive packages (lmodern, latex-extra, fonts-recommended/extra, science, bibtex-extra, pictures, cm-super) before building.
- Next: Ch14 (magnetic excitations): one writer per section (copy briefs/sections/13.x.md), then the five-report review, a post-revision check and the ledger merge (briefs/ledger-merge-ch13.md pattern).
- A parallel compute agent posts results to state/DC-RESULTS.md and returns/R18 on the same branch; campaign_commit.sh merges concurrent work automatically (merge-tree) and fails loudly on conflict.
- **Ch18 + D.43–D.44: ACCEPTED** (2026-11-06), ledgers merged; Part III opened. Gate PDF: releases/book-gate-ch18.pdf (1426 pp; Ch1–8, 10–18). One continuum Si cascade set (A_AB = 5.703 eV³, E_g = 1.160 eV; F 0.114 at 2.4σ). The refereed full-band Si cascade (R19 FBC-v2) is integrated as a computed reference in 18.1/18.3/18.4. Open: Ge exciton binding 4.2 meV uncited; C.11 drafted.
- **Ch19 + D.45: ACCEPTED** (2026-11-06), ledgers merged. Gate PDF: releases/book-gate-ch19.pdf (1494 pp; Ch1–8, 10–19). Amended 2026-11-06 to the Ch20 final 𝔯_coll band (0.81–1.02): collection alone not reached by transport, not excluded until real-detector kernels; the two-bias measurement decides.
- **Ch20: ACCEPTED** (2026-11-06), ledgers merged (incl. the Ch19 amendment). Gate PDF: releases/book-gate-ch20.pdf (1546 pp; Ch1–8, 10–20). Final 𝔯_coll band 0.81–1.02 (selective-sink 1.05–1.53 an upper envelope); collection alone not reached by transport, not excluded until real-detector kernels; the two-bias measurement decides. Golden-rule Luke rate; E.12 fixed (Leman Eq. 21 / G4CMP Eq. 8 low by k_s/k).
- **Ch21:** 21.1–21.6 drafted; 21.7 (next-target guide + summary) running; then the five-report review.
- Light pass: Ch17 "up to 11.5 meV" and Fig. 15.3b plot the bare spin-current form; with 1/(1+λ) the crossing is 10.9 meV (15.4 now states it).
- Next: Part III (Ch18–22) per SPINE; then App. B, App. F completion, D.43–D.47, Ch9 (atlas) last, then the final passes. Light-pass queue: Ch7/E.20 ZrTe₅ 15.6 → 11.8 meV (LE-186); X_αβ → strain symbol (14.2); 12.3/12.6 σ_n → σ_p; room-temperature Al elastic constants in 6.4/C-18; E.14/E.20/E.21/E.26 items from the Ch13–16 notes.

- (from 22.2) s10-5 'interim statement' wording; s10-6 Ge HSE claim soften; ledgers/SEAMS/18.3.md 0.015→0.008 to match tex.
- (from 22.1) E.14: add Ge band-mass check alongside valley order.
- (from Ch21 rev) 10.2, 10.9, 17.1 still say tables' gap 1.11 eV — align with Ch21/Ch18 cascade; Ch16 minimum 9 vs 9.5 keV align.
- (DC-RESULTS sweep, 2026-11-07) Before the final audit, run one pass over the whole book against state/DC-RESULTS.md:
  - DC-93: CsI measured C_ij (the [E] B-floor/ν wording becomes measured values; FOM ≈ 3.7–3.9);
  - DC-41: conserving L^BCS/(𝔤_I L^nor) scope, i.e. ℓ_mfp in the same sentence; the clean table is not valid for films;
  - DC-91: ε∞/Z* for C, 3C-SiC, LiF, NaF with the PBE caveat; no GaAs ε∞ 21.8;
  - DC-67: Si ε 3.7468 eV and F 0.11398 (2.5σ); no P_casc_lib tables; the Gaussian tail law is C/x, not x^(−1/2);
  - DC-49/54/36: quote only REF §4 wording;
  - DC-2 and DC-2-alpha: Ge hybrid routes fail. E.14 and s10-6 are being fixed now; 22.1 gets R9.
- (Ge bands) E-15.tex:56 still 'reuses the HSE06+SOC run of app:E.14' — rewrite to 'the Ge bands that pass the E.14 check'; E-1.tex:147 'hybrid or quasiparticle' — align with E.14. GW result pending (DC-2): update E.14, s10-6, 22.1 when it lands.
- (from Ch22 rev) 8.6 stale drag-mass sentence (align to 12.5: 14 mₑ exact; on-site element 12–24); 21.7 Fermi-function wording (see ch22/revision.md); verify lee1974conductivity journal ref.

## Status 2026-11-07
- Ch21 ACCEPTED; gate = releases/book-gate-ch21.pdf (1610 pp). E.27 symbols (𝔎_i, 𝔥, ξ_i, λ_dec) owed NOTATION rows at App. E merge.
- Ch22 ACCEPTED; gate = releases/book-gate-ch22.pdf (1636 pp). Part III complete.
- Next: Ch9 atlas (briefs 9.1–9.4 written), then App B, App F completion, C.10–C.20 and E.14–E.27 second passes, DC-RESULTS sweep, light-pass queue, final audits. GW (DC-2) pending for Ge.
- (from 9.2) s16-1 l.15 ZrTe₅ pair cost 31 → 23.6 meV (half-gap 11.8; LE-186). NOTATION NiO magnon edge 7.2 → 7.3 keV.
- (from 9.4) App F: 14.3a rows need a 𝔗 placement; rerun figscripts/ch09/fig9_3.py at the end (box numbers from main.aux); front matter could point to 9.4 for reading a Limit Check.
- (from Ch9 rev) 12.4b Limit Check text and its F row: placement on n_B (per 8.5); Ch22 SPINE/CLAIMS counts 74/39/56 (at Ch9 merge).
- (App B) Drafted (about 58 pp; B.1 has 1491 symbol rows, generated). Rerun figscripts/appB/gen_B1.py and gen_B3.py after the last merge.
  - Acronym pass owed book-wide: 47 acronyms are never expanded (RPA, BCS, DFT, CDMS, HSE06, SOC, …) and 10 are expanded only after first use. List in figscripts/appB/gen_B3.log.
  - NOTATION triage owed: about 30 cross-row clashes and about 12 duplicates (ledgers/REVIEWS/appB/writer-notes.md).

## Status (Ch9 accepted)
- ALL CHAPTERS ACCEPTED (1–22). Gate = releases/book-gate-ch09.pdf (1728 pp, incl. App B draft). Remaining: App B fixes (rulings B1–B4), App C.10–C.20 and E.14–E.27 second passes (then add to gate), App F completion, DC-RESULTS sweep, acronym pass, NOTATION triage remnants, light-pass queue, final citation/language/figure audits, final full build. GW (DC-2) pending.
- (Zα)² xenon: (54/137.036)² = 0.155. 10.9 l.176, l.232 and 22.2 l.56 print 0.13 → 0.16 (E.26 is correct). Check that C.15 does not carry 0.13.
- s16-8 l.51 caption: Al 3.40 km/s and 2.73 g/cm³ → 3.30 km/s and 2.70 g/cm³ (Ch20 constants).
- (DC sweep) DC-4 VALIDATED (q-grid), TA fails INS: Ge PAER edges 0.21380 (continuum) / 0.21264 MeV (replica); compare with Ch13/22.1 '0.2119–0.2141 MeV' and E.14/E.17; quote TA frequencies only with the softness stated.
- (App F) Check the source equation numbers: 10.9d (box says Eqs. 2.1–2.2, row says 1–2) and 21.2a (box A1–A2, row A1). Fold into the citation audit.
- (NOTATION 100(d)) Four clashes remain in the tex: C.9 F̃_μν (shifted-photon field strength) vs 1.4 dual F̃^μν; ω_LO/ω_L; italic x_e vs bold 𝐱_e; λ_tr. Resolve after the light passes. 34 check_notation gaps remain book-wide (none new).
- Room-temperature Si gap quoted as both 1.11 and 1.12 eV: use 1.12 eV (300 K) book-wide where room temperature is meant (final pass).
- Si nuclear mass: ch01 and ch08 use 26.06 GeV (²⁸Si); D-13, C-6 and E-18 now use natural Si, 26.16 GeV. Align ch01/ch08 to natural Si unless the passage means ²⁸Si; rerun scripts (final pass).
- fig14_2 panel (a) legend collides with the red curve: move it to upper right (see ledgers/REVIEWS/figures/C.md). The script takes >25 min; run it in the background.
- fig11_2: legend ~5.4 pt and the light-mediator curve crosses an entry. Rerun needs QE matdyn.x (not installed); fix recipe in ledgers/REVIEWS/figures/B.md.

## Final status (2026-11-07, final ledger merge and release build)
- **The book is complete.** Chaps. 1–22 and Appendices A–F are ACCEPTED (SPINE status paragraph and rows; App. B, C.10–C.20, E.14–E.27 and the App. F completion set at this merge). The final passes are done: light passes A/B/C, final-consistency.md, the citation audit (citation-audit*.md, final-residuals.md), the language audit (ledgers/REVIEWS/language/) and the figure check (ledgers/REVIEWS/figures/).
- **Release:** releases/book-full.pdf, **1842 pages**, the full book from main.tex (latexmk, outdir /tmp/claude-0/build-release; settled, a further latexmk run reports "Nothing to do"). 0 LaTeX errors, 0 undefined citations, 0 undefined references, 0 multiply defined labels, 0 biber warnings. 54 overfull boxes > 5 pt (205 in all); the largest: s21-5 l.67 (83 pt), s17-4 l.33 (73 pt), D-28 l.11 (72 pt), s8-6 l.158 (55 pt), D-28 l.54 (54 pt), D-16 l.80 (50 pt), D-40 float (46 pt, ×2), s17-5 l.152–163 (42 pt); about 20 of 18.7 pt are raised on the output routine across Ch7 (running head or float). Cosmetic, not fixed (no tex edits at this merge). The old gate PDFs (book-gate-*.pdf) are deleted; book-full.pdf is the only release.
- **Ledgers:** SPINE C.10–C.20 "Used by" lists take the appC2/revision.md additions (the section Prerequisites now name the appendix, so rows and entries agree); 1.1 header corrected DRAFTED → ACCEPTED (the status paragraph had it accepted since 2026-11-02). CONCEPTS C.10–C.20 rows and CLAIMS C-10 to C-20 → WRITTEN; CLAIMS values restated from the final passes (I-83, I-120, I-127, I-131, I-239, I-281, I-283, II-28, II-282, II-346, II-366; note in CLAIMS after the Chap. 9 merge). check_concepts.py: 0 violations. check_notation.py on all tex: 34 gaps (30 in appF/F-rows.tex, a_Born also in s8-2; 𝒰, 𝒰^*, 𝒰^† in D-2; K̃ in D-3); same 34 as before the final passes, none new.
- **Open items:**
  - fig11_2 legend (5.3–5.7 pt at print size; the light-mediator curve crosses the "light, acoustic" entry): the rerun needs Quantum ESPRESSO matdyn.x (not installed); recipe in ledgers/REVIEWS/figures/B.md.
  - fig14_2 panel (a) legend → upper right: being rerun in the background (script > 25 min; not running in this container at the time of the build). When it lands, rebuild and replace releases/book-full.pdf.
  - GW result for Ge (DC-2-gw): pending. When it lands, E.14, s10-6 and 22.1 each take it in one sentence; then rebuild the release.
  - Citations: recheck the arXiv-only bib entries before release; debernardi1994anharmonic has no pages (Crossref has the proceedings only); key-year mismatches need no action (citation-audit-applied.md, final-residuals.md).
  - check_notation: CLOSED (2026-11-07, NOTATION clash entry 105; ledgers/REVIEWS/final-notation.md). The 34 gaps now give 0 book-wide: 7 symbols got rows (a_Born; ℛ_IP, ℛ_{RPA+LF}, ℛ_source; 𝒰 with 𝒰*, 𝒰†; K̃), 7 were rewritten in App. F in their home section's symbols (k_φ, v_F,x, v_F,z, κ_xx, M_χ, n_ph, n_eh), and 20 are file-keyed exceptions on appF/F-rows.tex (17 quoted source symbols, Y_ℓ0, Δω_eq, ΔE_zp). App. B.1 regenerated (0 unrendered); release rebuilt.
  - Editor's calls left open: appA, appC and appD have no opening paragraph (language G4, not applied); "hand-over" kept in 19.5 and E.23 (language Part III, optional); App. B chain symbols of C.20 (d_kink) keep C.20 as first use although 19.6 is first in reading order; generator heuristics in B.1 (bold-vector rule, e.g. 𝐩_j^α in 8.1) are cosmetic.
  - Overfull boxes > 5 pt (above), if a typographic pass is wanted.
  - Book content open problems (LE and XG labels, DEFERRED-COMPUTE) stay as printed in the open-problems fields.
- Nothing is committed.

- fig14_2 rerun completed 06:17 (legend upper right; log unchanged) and is included in releases/book-full.pdf (built 06:19). Remaining layout item: 54 overfull boxes > 5 pt (largest s21-5 83 pt, s17-4 73 pt, D-28 72 pt, s8-6 55 pt; ~20 at 18.7 pt in Ch7 page output).
- Layout: 0 overfull boxes > 5 pt (was 54); releases/book-full.pdf rebuilt (1842 pp, 0 errors, 0 undefined refs/cites).
- GW for Ge (DC-2-gw): DEFERRED by the user (2026-11-07), not awaited this round. The book already names GW as the next route with no verdict (E.14, s10-6, 22.1), and the Ge window stays an estimate, so no text change is needed.
- Notation gaps closed (entry 105): releases/book-full.pdf rebuilt 2026-11-07 07:06 (1842 pp, 0 errors, 0 undefined citations/references, largest overfull box 4.93 pt).

## Three-volume edition (2026-11-12)
- **Structure:** the book is now three volumes, built from tex/vol1.tex, vol2.tex, vol3.tex with `./build.sh [OUTDIR]` (latexmk per volume, then tools/xref.py, repeated until the cross-volume labels settle). Volume I *Foundations* (Chaps. 1–8; Apps. A–D), Volume II *Signals and Detection* (Chaps. 9–22; Apps. A, B, E (derivations, label app:D-II), F), Volume III *Computations* (Chaps. 23–33; Apps. A, B). Chapter numbers and appendix letters run through the volumes. book/VOLUMES.md maps every label to its printed number.
- **Labels and file names are stable identifiers, not numbers:** sec:5.5 prints Sect. 5.4; app:E.14 prints Sect. 31.1; app:D.29… print Appendix E.x. Volume III's chapter directories and chap: labels follow print order (renamed 2026-11-12 after the chapter reorder; logs written before then use the old names: old ch26→ch25, ch27→ch26, ch25→ch27, ch31→ch30, ch30→ch31). tools/chapcheck.sh <chNN|appX> [OUTDIR] compiles one unit with its true number.
- **Tools:** tools/volumes.py (source map), xref.py (cross-volume labels), split_B1.py (per-volume symbol lists from appB/B-1.tex; rerun figscripts/appB/gen_B1.py first after NOTATION.md changes), volmap.py, dups.py (cross-chapter duplicate finder), remap_maps.py (chapter-map tags; maps edited by hand are skipped and must be checked).
- **Edit record:** briefs/volumes/COMMON.md (with Addenda 1–4: user directives on style, appendices, Pareto models, no historical privilege, light forward citations, routine algebra in Vol II derivations), E2E.md, ERRATA.md; logs in ledgers/REVIEWS/volumes/ (unit logs, E2E-vol*.md, structure findings, ERRATA.md and errata/G1–G6.md with proposals, independent reviews and applications).
- **Release:** releases/vol1-foundations.pdf, vol2-signals-and-detection.pdf, vol3-computations.pdf replace book-full.pdf.
