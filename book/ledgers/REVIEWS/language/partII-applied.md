# Language audit, Part II (tex/ch09–ch17): reviser log

Reviser. Brief: briefs/reviews/language-audit.md. Ledger: ledgers/REVIEWS/language/partII.md. Date: 2026-11-07.
Scope of edits: tex/ch09–ch17 only. No figscript needed a change. Each edit was an exact replacement of the quoted text, made after re-reading the line.

## MUST items (18 of 18 applied)
C10.1, C10.3, C10.6 (first sentence of s10-2:125 deleted), C10.8 (both sentences deleted), C10.10, C10.12, C10.14, C10.18, C11.1, C11.3 (split into three sentences), C11.7, C11.8, C11.11 (both sentences deleted), C12.1 (split at "interference."), C13.7, C13.8, C13.11 (second sentence deleted), C17.2.
Wording that differs from the ledger:
- C17.2: "For each coupling, the choice of target and threshold depends on where in mass and threshold these changes fall." (The ledger's version reads in an awkward order.)
- C10.6: deleted the sentence, so the "electrophilic" fallback does not apply.

## OPTIONAL items applied
- Ch. 9: C9.1; C9.2, written as "the hazard is counting a process twice or not at all", because the paragraph names both failures (double counting and omission); C9.3.
- Ch. 10: C10.2, C10.4, C10.5, C10.7, C10.9 (the ratio named in words, without $r$, which is first defined in a later caption), C10.11, C10.13, C10.15 (the dark-photon/ALP sentence dropped; the scalar and forward-pointer sentences kept), C10.16, C10.17, C10.19.
- Ch. 11: C11.2, C11.4, C11.5, C11.6, C11.9, C11.10, C11.12, C11.13, C11.14. C11.15: cut to one sentence, "Between the optical-phonon absorption at tens of meV and the response of a whole bar at a peV, the scalar field of \cref{sec:11.8-gaas} is classical, …", plus the existing pointer to Sect. 14.6.
- Ch. 12: C12.2, C12.3, C12.4, C12.6 (and "its valence electrons" → "the valence electrons" to keep the sentence grammatical). C12.5: "bookkeeping" → "the counting of Migdal and lattice events" at s12-1:133, s12-5:87, s12-6:192 and also s12-2:37. The table cell s12-6:174 now reads "normalization of the added lattice rate".
- Ch. 13: C13.1, C13.2, C13.3, C13.4, C13.6, C13.9, C13.10.
- Ch. 14: C14.1, C14.2.
- Ch. 15: C15.1, C15.2. C13.2 applied in ch15.tex.
- Ch. 16: C16.1 (all six "the book's halo" → "the standard halo"), C16.2, C16.3. C13.2 applied in ch16.tex.
- Ch. 17: C17.1, C17.3, C17.4, C17.5. C13.2 applied in ch17.tex.
- C-X.1 ("price"): rewrote 9 of the 13 uses: s10-8:58, s10-9:96, s11-6:48, s13-1:27, s13-1:32, s13-2:130, s16-2:14, s16-8:44, s17-6:124. Kept 4: s10-7:61, s13-6:77, s14-4:94, s16-summary:5.
- Display comma: added at ch13/s13-9 ($m_{\mathrm{min}}^{\mathrm{ZP}}$ display, followed by "with spin–orbit …").

## OPTIONAL items not applied
- C13.5: the previous sentence ("…its phonon must supply all of $\vect{k}_{\mathrm{c}}$") has no natural place for the credit clause, so the provenance sentence stays as it is.
- Display comma at ch10/s10-6.tex:115 (eq:10.6-oo): the next line continues the sentence ("is the relative shift …"), so no comma belongs there.

## Physics doubts: editor rulings applied
- D1, top of the silicon phonon band. Source: figscripts/ch05 (fig5_1.py, we5_5.py) and Sects. 5.2 and 5.4. 64.1 meV is the measured zone-center optical phonon (Nilsson and Nelin), which Sect. 5.2 calls the top of the band. 63.7 meV is the PBE/DFPT value; it is also where the PBE density of states ends, and the figscripts of ch11, ch12 and ch17 (iso11.py, imp11.py, sectors17.py, fig17_sectors.py) use it as the computed band top. Applied:
  - Wherever "top of the band" is meant generically, the text now gives 64.1 meV: s17-1:9 and s17-summary:3 (both were 63.7). The s10-2 caption already used 64.1.
  - Where the computed cutoff is meant, the text now names it: s11-6:175 caption "top of the PBE band, 63.7 meV (the measured band top is 64.1 meV)"; s12-4:131 caption "PBE band top 63.7 meV"; s17-1:20 caption "top of the PBE band, 63.7 meV"; s17-1:9 adds "the PBE density of states used for the maps ends at $\omega_{\mathrm{max}} = 63.7$ meV". s11-3:55 and s11-6:87 already named the PBE value and were left as they were.
- D2: s14-1:3 now says "can transfer up to 5.3 keV of momentum".
- D3, acoustic edge at 1 meV. Both numbers are correct, and neither was changed. Per figscripts/ch11/limit11_1b.py, 6.39 keV uses the polarization-weighted inverse speed $\langle\sum_\nu(\hat q\cdot\hat e_\nu)^2/c_\nu\rangle^{-1} = 8.956$ km/s. 6.1 keV uses the fastest longitudinal speed, 9.35 km/s along [111]. Checked by hand: 6.39 and 6.12 keV.
  - s11-1 caption (fig:11-limit-b): states that 6.39 keV is the edge for the polarization-weighted inverse speed 8.956 km/s of eq:11.1-heavy, and that the Sect. 9.2 convention (9.35 km/s) gives 6.1 keV.
  - s11-1 WE (we:11-light): "rate-weighted speed" → "polarization-weighted inverse speed 8.956 km/s of eq:11.1-heavy (6.1 keV for the fastest longitudinal speed)".
  - ch11 Summary (s11-9:98): "The acoustic edge, set by the fastest longitudinal sound speed, 6.1 keV …". The "44 times the edge" now names its reference: "the edge of the polarization-weighted speed (6.39 keV in silicon)".
  - s9-2:3: "needs 6.1 keV on its fastest longitudinal branch". s9-2:20 adds: "Every acoustic edge of this chapter uses this convention; Sect. 11.1 also quotes the edge for the polarization-weighted inverse speed of the rate, 6.39 keV in silicon at 1 meV."

## Checks
- Lint (lint.py --banned BANNED-TERMS.txt, 78 files in ch09–ch17): 469 hits, 0 blocking (406 LONG-SENT, 61 EQ-PUNCT, 2 DASH, 0 PERIPHRASIS). Before the edits: 471.
- Build: `latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-lang2 main.tex`. Exit code 0. 0 LaTeX errors, 0 undefined references, 0 undefined citations. latexmk reported all targets up to date, so no extra pass was needed.
- Not committed. tex/ and ledgers/ sit under the git-ignored campaign/ directory, so there is no git diff to inspect.
