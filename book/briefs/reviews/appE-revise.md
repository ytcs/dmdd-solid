# Appendix E revision (one reviser for E.1–E.13)

Revise /home/user/dmdd-solid/book/tex/appE/appE.tex and E-1.tex … E-13.tex. Address **every** item of the four reports in /home/user/dmdd-solid/book/ledgers/REVIEWS/appE/: derivation-1.md, derivation-2.md, prose.md and reader-bc.md. Also address everything in ledgers/REVIEWS/appE/editor-notes.md, including its "Rulings for the reviser" section, which binds you.

Follow COMMON.md, STYLE.md, REGISTER.md, NOTATION.md and READER.md.

## Additional editor rulings
1. Appendix opening: use the prose reviewer's 143-word opening (adapted). It frames E.1–E.13 (methods) and E.14–E.27 (specifications, still to be written; give no forward list of their titles). It also says briefly what the truncation label 𝔗 records, with \cref{sec:8.5}. Delete the comment line in appE.tex. Add the short summary the prose review drafted, at the end of E.13 or as an unnumbered `\section*{Summary}` after E.13.
2. E.4, Poncé: Poncé et al. rescale to their measured value of 11.94. Say that, and quote the book value 11.7 as the low-temperature measurement. Do not misstate the source.
3. Source mismatches: Garza is 0.38 eV over 41 compounds. PseudoDojo's mean Δ is about 0.7 meV. For SG15, cite only what the paper states; drop parameters that cannot be verified, or present them as the inputs of the book's own calculation. Noffsinger: drop "norm-conserving" unless the paper says it.
4. Notation drift (derivation-1): v_C is upright. n_B, n_T, … follow the NOTATION form for 𝔗 (check the row; italic if no ruling, used consistently). One atom-count symbol, N_at. Rename N_f to avoid the NOTATION clash and propose a row. Name the broadening η_b or match NOTATION's row for broadening.
5. Si core depths (E.7): give binding energies relative to the VBM from a cited source (2p ≈ 99 eV, 2s ≈ 150 eV, 1s ≈ 1839 eV) and recompute the derived scales (the MeV and keV figures).
6. All numbers in tab:E-gw must come from their stated source (Si 1.29/1.16 from the source).
7. Spelling: American. Rates: \varGamma.

## Deliverables
- The revised files.
- A build in /tmp/build-appErev with no LaTeX errors and no undefined citations. Undefined refs only to unwritten sections are acceptable.
- Lint clean (real hits only).
- /home/user/dmdd-solid/book/ledgers/REVIEWS/appE/revision.md: one row per item → fix → location, with a reason for any declined item. Do not announce fixes in the text itself.
- Update the SEAMS files E.*.md where they repeat corrected errors.
- Other writers are working in tex/ch01, ch03, ch04, appC and appD. Do not touch those files.
- Do not commit. Final message ≤ 10 lines.
