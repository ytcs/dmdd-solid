# Ch. 3 (and Fig. 4.7) figure-compute pass: figures and numbers changed

Brief: briefs/reviews/ch03-figures.md. Representative calculation: QE 7.6 pw.x, PBE, SG15 ONCV (Si/Ge/Ga/As -1.2, Ge_FR-1.0 for SOC),
60 Ry / 240 Ry, Gamma-centred 12^3, a = 5.431 (Si), 5.658 (Ge), 5.653 (GaAs) A. Drivers: figscripts/ch03/qe_ch03.py (caches
qe_si_pbe.npz, qe_ge_gaas.npz, qe_si_lda.npz), figscripts/ch03/w90_verify.py (w90_verify.json), figscripts/ch04/fig4_7_data.py
(fig4_7_data.npz). Work dirs /root/work/F3, F3W, F47 (deleted after the pass). All QE runs through code/run-heavy.sh.

Anchors: Si PBE E_g at 5.431 A = 0.5569 eV (App. E.1 quotes 0.557, 40 Ry); ph.x eps_inf PBE 20^3 = 13.04 (E.1: 13.04, 18^3).

## Fig. 3.6 (fig3_6.py; s3-3.tex caption and text) -- empirical pseudopotential -> QE PBE (+ scissor in panel b)
| quantity | old (EPM) | new (QE PBE) |
|---|---|---|
| k_c (2pi/a), caption | 0.853 | 0.843 |
| E_g, caption | 0.82 eV | 0.557 eV |
| E_dir at Gamma, caption | 3.42 eV | 2.56 eV (now the smallest vertical gap) |
| smallest vertical gap / at L, caption | 3.12 eV at L | 2.70 eV at L (Gamma is smallest) |
| scissor in panel (b), caption | 0.35 eV | 0.61 eV |
| E_min(q = 0) scissored (new in caption) | - | 3.17 eV |
| text: E_min [110] lowest | 1.26 eV near 3.4 keV | 1.26 eV near 3.1 keV |
| text: E_min [111] lowest | 2.2 eV | 2.13 eV |
| text (WE m_min): E_min at q* = 0.88 keV | about 2.0 eV | about 1.9 eV |
| text Sect. 3.3 l.44: semilocal k_c / gap | 0.840, 0.60 eV (E.1 at a_PBE) | 0.843, 0.56 eV, m_l 0.95 (Fig. 3.6, a = 5.431) |
| text l.102: PBE masses (added) | - | m_l 0.95, m_t 0.193 |
EPM k.p sum-rule check (0.853, 0.872/0.184, 113 bands, 3.73 eV, 2.27 of 5.43) kept as explicitly labelled empirical-model
prose (the sum rule is exact only for a local potential); asserted in fig3_6.py in a separate text-check block.

## Sect. 3.6 Wannier verification (w90_verify.py -> w90_verify.json; independent re-run at 60 Ry, 12^3 SCF, 20 bands)
Verdict: the claim of s3-6 is CONFIRMED. The most localized 8-function sp3 set of Si (disentangled) points AWAY from the
bonds; the bond-directed set is a higher stationary point. No change to Fig. 3.11 or its numbers.
| grid / outer / frozen (eV above VBM) | Omega_I | A: along bonds | B: away | M: default Si:sp3 (mixed) | Si:s;p start | random start |
|---|---|---|---|---|---|---|
| 6^3 / 12 / 2.5 (book settings) | 13.97 | 19.84 | 16.20 | 18.02 (2.45/2.06 split) | 20.83 | 16.20 (= B) |
| 6^3 / 12 / 1.0 | 13.52 | 19.11 | 15.59 | | | |
| 6^3 / 14 / 2.5 | 12.48 | 17.90 | 14.34 | | | |
| 6^3 / 16 / 2.5 | 11.96 | 17.25 | 13.71 | | | |
| 6^3 / 12 / 2.5, 16 bands | 13.97 | 19.84 | 16.20 | | | |
| 8^3 / 12 / 2.5 | 15.87 | 21.81 | 18.20 | 20.00 | 22.86 | 18.20 (= B) |
| 8^3 / 14 / 2.5 | 14.02 | 19.70 | 16.02 | | | |
| 8^3 / 12 / 1.0 | 15.09 | 20.64 | 17.09 | | | |
(total spreads in A^2; B - A = -3.5 to -3.7 A^2 in every case; Omega_I identical for A and B, same subspace.)
wannier90 reference outputs (docs/tutorial_solutions, wannier90 develop branch): tutorial 3 (Si, 8 sp3 WFs, symmetric minimum)
has both groups centred 0.46 A from the atoms AWAY from the bonds, total 14.50 A^2; tutorial 11 (4^3, default mixed Si:sp3
start) stops at the mixed stationary point, 17.55 A^2 with 2.02 (away) / 2.37 (toward) A^2, the analogue of our M row.
Marzari-Vanderbilt Table I: valence (4 bond functions) only; our 6^3 valence total 7.58 A^2 (book 7.58; MV 7.61).
Text change, s3-6.tex after "same Omega_W^I = 14.0 A^2": one sentence added stating the robustness (windows up to 16 eV,
frozen 1 eV, 8^3 grid: totals move by up to 2.6 A^2, B stays lower by 3.5-3.7 A^2, random start ends in B; wannier90 example
reaches the same set). The 40 Ry calculation of Fig. 3.11 is reproduced at 60 Ry to 0.01 A^2 (16.20 / 19.84 / 13.97).
Valence interpolation errors (isolated 4-band group, bond-centred s starts): 350.4 / 123.0 / 50.5 meV on 4^3 / 6^3 / 8^3
(book: 350 / 120 / 51) -- CONFIRMED, not an artefact. H^W(R) along <110>: 0.121 eV at 7.68 A, 0.026 eV at 11.5 A on 8^3
(book 0.12 / 0.03), the same on 6^3 at 7.68 A (so physical, not aliasing). Cause: the isolated valence group of a
small-gap (PBE 0.56 eV) crystal has slowly decaying Wannier tails along the zigzag chains; the valence spread itself grows
with the grid (6.40 / 7.58 / 8.16 A^2). Disentanglement: none in the valence test; bands: exactly 1-4; k path: errors
are largest on Lambda near Gamma (0.075-0.14 (2pi/a)), off every grid point, as expected. Cross-check: the 8 sp3
functions on 8^3 give valence 39.9 meV and conduction below VBM + 1.5 eV 84.1 meV (book: 40 and 84) -- confirmed.
| text l.175/caption: E_dir at q = 0 of panel (b) | E_dir (3.42) | "vertical gap" (scissored 3.17 eV) |
Correction to the row above: X_1c = 0.69 eV (fig3_6.py path-index bug fixed before any tex used it; not quoted in tex).

## Fig. 3.7 (fig3_7.py; s3-3.tex caption and Kane paragraph) -- EPM -> QE PBE (Ge with SOC)
| quantity | old (EPM, a = 5.66/5.64) | new (QE PBE, a = 5.658/5.653) |
|---|---|---|
| Ge gap / minimum | 0.96 eV at L | semimetal: Gamma_7c (s) at -0.05 eV below Gamma_8v, L_6c at +0.10 eV (SOC) |
| Ge Gamma state | 1.22 eV (above Delta min 1.02) | -0.05 eV (inverted); without SOC +0.046, L +0.191 (= App. E.1) |
| Ge split-off (new) | - | 0.29 eV (measured 0.296); X 0.66 eV; 80 Ry: edges change < 2 meV |
| GaAs gap (direct) | 1.42 eV | 0.51 eV |
| GaAs L / X | 1.66 / 1.74 eV | 1.00 / 1.46 eV |
| text: Kane check | "band model of Fig. 3.7(b)": E_P 18.3, 0.0718/0.0721 | same numbers, now labelled empirical-model check |
| text: mass follows gap (added) | - | PBE GaAs Gamma mass 0.030 m_e at gap 0.51 eV |
Caption lattice constants are the room-temperature 5.658/5.653 A of the editor ruling; the s3-3 prose (l.33, l.35) still
quotes Ge 5.658 "extrapolated to zero temperature" and GaAs 5.648 A -- not changed here (outside this brief), flagged.

## Fig. 3.8 (fig3_8.py; s3-4.tex caption and l.84) -- PySCF/GTH-DZVP -> QE LDA (input_dft='pz', SG15)
| quantity | old | new |
|---|---|---|
| LDA minimum gap / position | 0.54 eV at 0.84 | 0.40 eV at 0.848 |
| convergence | +25 meV (6^3), -36 meV (TZV2P) | < 1 meV at 80 Ry and on 16^3 |
| Gamma / X / L conduction | 2.59 / 0.69 / 1.46 | 2.51 / 0.53 / 1.43 eV |
| scissor | 0.63 eV | 0.77 eV |
| G0W0 - LDA at conduction states (l.84) | 0.53 to 0.64 eV | 0.66 to 0.70 eV |
| panel (b) | LDA 0.52 (lit.), PBE 0.557/0.602 | adds QE LDA 0.402; PBE 0.557 now from Fig. 3.6's calculation |
Pseudopotential-functional mismatch (stated in the caption): SG15 is PBE-generated. LDA - PBE with SG15 = -0.155 eV, with a
Troullier-Martins pair generated in each functional (ld1.x, radii of Fig. 3.9's potential; cache qe_si_tm.npz) = -0.06 eV,
so a consistent LDA potential would give about 0.50 eV (tabulated 0.52). fig3_8_lda.py and its three PySCF npz caches deleted.

## Fig. 4.7 (scope change by the editor: first-principles redo DROPPED; model kept)
fig4_7_data.py / fig4_7.py restored to the empirical-model versions (commit c92d632e); fig4_7_data.npz unchanged.
Figure: measured references added (eps_inf = 11.7 against the three model static limits in panel a; measured loss peak
16.4 eV dotted in panel b) and the dark-matter window shaded in panel b (omega <= q v_max = 6.05 eV at q = 2pi/a).
s4-6.tex: "and and" typo fixed; WE 4.11 convergence sentences condensed (113 G unchanged to 3 digits; k grid < 0.1 %);
"fitted bands" wording -> "model whose form factors were fitted" (l.62 now points to the Cohen-Bergstresser potential of
3.3, which no longer draws Figs. 3.6/3.7); caption mentions the reference lines and the window. Model numbers
11.45/10.22/10.81 and the ~2 eV loss-peak offset unchanged (still asserted by fig4_7.py). s4-9 "17 % -> 11.9": unaffected.
Partial first-principles results obtained before the scope change (not used in the book; for the record): ph.x eps_inf,
Si, a = 5.431, 60 Ry, Gamma-centred 20^3: PBE IP 13.61 / RPA+LF 12.20 / adiabatic PBE 13.04 (12^3: 13.18, 16^3: 13.06);
LDA (on SG15-PBE) 14.30 / 12.84 / ALDA 13.56. The PBE 13.04 reproduces App. E.1. turbo_eels runs were stopped.
