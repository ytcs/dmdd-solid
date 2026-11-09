# App. E second pass, part 1: consistency of E.14–E.20 with the accepted book

Scope: tex/appE/E-14.tex … E-20.tex against chapters 1–22 as accepted (SPINE status line, 2026-11-07), state/DC-RESULTS.md, and every
chapter/App. D/Ch22 pointer into E.14–E.20 (154 chapter hits + 60 in ch22, grepped `app:E\.(1[4-9]|20)`). No tex edited, nothing run.
Verdicts: CHECKED (agrees), WRONG (disagrees with a governing value; correction given), GAP (a chapter says E.n specifies something E.n
does not, or a needed item is missing). Severity: **H** changes a prescribed route or a quoted number; M a missing specification item; L wording.
All 113 distinct \cref targets in E.14–E.20 resolve (lim:12.3a via limitbox option); BANNED-TERMS.txt regex scan: no hits; no DC-/LE-/CW/[CALC] tokens.

## Summary of WRONG and GAP items (fix list)

| # | Sev | Location | Verdict | Correction | Governing source |
|---|---|---|---|---|---|
| 1 | H | E.15 l.56 (Spin–orbit mixing at the band edges) | WRONG | "reuses the HSE06 run with spin–orbit coupling of E.14" prescribes the failed route; the Fock-cutoff 120→160 Ry / exchange-grid 3³→4³ convergence is hybrid-specific and also clashes with E.14's 160/320 Ry. Rewrite: the step runs on germanium bands that pass the E.14 check (order, both gaps, masses at L and Γ), next route quasiparticle GW with SOC; convergence on those bands (bands, screening cutoff); "once bands that pass exist, the step costs less than a core-hour". | DC-2 (HSE06+SOC FAILED-CONTROL), DC-2-alpha; E.14 Ge ¶; ch10 s10-6 ("HSE06 … put Γ about 0.1 eV below L … for bands that pass the check"); ch22 tab:22-gaps row "Ge bands with SOC in the measured valley order (E.15)" |
| 2 | H | E.1 l.147 (outside E.14–20, per brief) | WRONG | "needs a hybrid functional or a quasiparticle calculation, with spin–orbit coupling" → "needs a quasiparticle calculation with spin–orbit coupling whose bands pass the check of App. E.14; a hybrid at the standard exchange fraction inverts Γ and L even with SOC, and a 4s shift fitted to both gaps gets the masses wrong (App. E.14)". | DC-2, DC-2-alpha; E.14; ch22 s22-1 we:22-fsum l.97 |
| 3 | H | E.16 "The response library", ground state | WRONG for Ge | Library prescribes "PBE … with a scissor to the measured gap" for Si **and Ge** ("four times that for germanium"). A scissor on PBE keeps the wrong Ge order (E.1 l.147, E.14). Add: for germanium the ground state is bands that pass the E.14 check; until then the Ge library is not built (or is flagged). Same caveat for the candidate-target loss functions ("scissor or quasiparticle gap") wherever PBE order is wrong, as E.14's last ¶ already states. | E.1 l.147; E.14 Ge ¶ and last ¶; DC-2 |
| 4 | H | E.18 "Drag masses", inputs; "crystal Migdal rate" for Ge | GAP/WRONG | Only GaAs is flagged for a scissor/hybrid. PBE germanium at the measured lattice constant has Γ at 0.047 eV (E.1, E.14), so 𝓘₃ ∝ Δ⁻³ and 𝓘₄ ∝ Δ⁻⁴ on the shared PBE base are inflated far more than in GaAs, and a scissor cannot fix the order. Add Ge to the gap sentence with the E.14 band check (GW route); the electronic piece of the Ge Migdal rate likewise. | E.1 l.147; E.14; DC-2/DC-2-alpha |
| 5 | H | E.15 "Finite-momentum BSE", method | GAP | "PBE, then G0W0, then BSE" for Si and Ge with no Ge proviso; G0W0 on PBE Ge starts from inverted/near-metallic bands. Add: germanium quasiparticle bands must pass the E.14 check before the BSE (and the exciton dispersion "along Γ–L") is run. | E.14 ("GW … subject to the same check"); ch22 tab:22-calc row 33 |
| 6 | H | E.18 (whole section) vs ch22 tab:22-calc row "Coherent zero-phonon Migdal response of silicon from 0.75 keV to 2q_BZ, all cross-site terms and local fields (app:E.18)" | GAP | E.18 specifies only the self entry S_κκ with the incoherent multiphonon/impulse lattice piece. The Ch12 erratum band (diagonal form valid for q ≳ 2q_BZ, boost identity eq:8.3-boostward below ≈0.75 keV, band between unsized, "nearly all of the Si Migdal rate up to 1 MeV, 33 % at 2, 7 % at 3 MeV") needs its own subsection: coherent zero-phonon response with cross-site S_κκ′ terms, q from 0.75 keV to 2q_BZ, local fields; acceptance: boost limit as q→0 (diagonal form 14.9× too high there) and diagonal form above 2q_BZ. | ch12 tab:12-nuisances row "Coherent zero-phonon response at q < 2q_BZ"; ch12 s12-4; SPINE Ch12 erratum; ch22 tab:22-calc |
| 7 | H | E.20 "ZrTe₅ and corrected Dirac reaches" + tab:E20-dirac | WRONG | E.20 takes Δ_D = 15.6 meV, v = (11, 4.4, 9.1)×10⁻⁴ (relaxed-cell, "implemented" row) as *the* ZrTe₅ parameters. The book's central row is the measured-structure row: Δ_D = 11.8 meV (half of 23.6), v = 1.1×10⁻³, 4.5×10⁻⁴, 1.0×10⁻³, Λ̃ = 0.191 eV, g_deg = 2, same tensor 308.4/20.75/126.1; 15.6 meV is the relaxed-cell row the reference implements (use it only for reproducing the published curve). Recompute with the central row: v_D(geo) ≈ 7.9×10⁻⁴, α̃ ≈ 0.18, Ry_D ≈ 0.10 meV, a_D ≈ 1.4×10³ Å, grid ratio ≈ 27 (vs 0.19/0.14 meV/1.0×10³ Å/19). Add the measured-structure row to tab:E20-dirac (keep the relaxed row labelled "implemented, for the re-plot"). | ch16 s16-1 sec:16.1-zrte5 (11.8 meV central), s16-9 Table 16.1 and we "Gap" ¶, ch09 tab:9-overlaps (Δ_D = 11.8), SPINE Ch16 line |
| 8 | L | E.20 ZrTe₅ ¶3 "the factor 0.55–0.62 that a recalculation with only its imaginary part needs" | WRONG | Book gives 0.61 (hard cutoff) and 0.54 (subtraction-scheme cutoff) → "0.54–0.61". | ch16 we:16-factor "One point" |
| 9 | M | E.20 "The conserving response of aluminum" | GAP/WRONG | Section is "clean and quasiclassical" only; ch15 s15-1 says E.20 computes it "with impurity scattering" and s15-3 that "the same impurity ladder dresses the density vertex and the two pair vertices … (app:E.20)". Add the Born impurity ladder in Nambu space with the Mermin normal state (γ_rel = v_F/𝔩_e) and the mean-free-path grid (clean, 1 µm, 300 nm, 30 nm); acceptance against the conserving values 1.01–1.09 at y ≥ 3 and 0.87/0.60/0.38/0.19 at y = 2.2; state that the clean table holds at y ≤ 2.5 only for 𝔩 ≳ 10 µm, not for films. The sentence "the small-q region where the vertex dominates is not needed" holds only in the clean limit (q𝔩_e = 0.023 for a 30 nm film at y = 2.2). | DC-41 (quote REF-DC-41 §7 with the 𝔩_mfp scope); ch15 s15-1, s15-3; SPINE Ch15 line |
| 10 | M | E.20 "Holstein absorption" acceptance | GAP | ch22 tab:22-calc row "Transport function α²F_tr of aluminum below a few meV (app:E.20)" lists the tests "acoustic sum rule of the vertex; λ_tr against the resistivity value 0.39". E.20 has neither, and its 30³ Q grid does not resolve the ω′⁴ regime within a few meV of 2Δ that the edge rate needs. Add: low-frequency α²F_tr (ω′⁴ law, ch15 s15-4) on a refined small-Q grid, acoustic sum rule on the vertex, λ_tr vs 0.39; optionally quote the rate factor (1+λ_tr)⁻² = 0.52 beside "1/(1+λ_tr) in the current". Notation: ch15 writes (ω_p^intra)², E.20 ω_p². | ch15 s15-4 eq:15.4-holstein and ¶ after; ch22 tab:22-calc rows 67–68 |
| 11 | H | E.17 "Data for the candidate targets", last ¶ but one: "CsI … needs its full elastic tensor, computed with PBE and PBEsol" | WRONG | Measured CsI constants at 4.2 K exist (C₁₁ 27.37, C₁₂ 7.93, C₄₄ 8.25 GPa, Θ_D 125.6 K); the book enters CsI with measured constants; what is missing is the density of the cold cell. Replace with: use the measured 4.2 K tensor; the open input is the cold-cell density (thermal contraction row). | DC-93; ch21 s21-7 ("CsI and diamond enter with measured constants; for CsI the density of the cold cell is missing") |
| 12 | M | E.16 library f-sum acceptance "60 bands exhaust at least 95 %" | WRONG vs chapters | ch21 s21-6 (library checks) and ch22 we:22-fsum say the converged electronic table holds the f-sum to 2 % (app:E.16), and we:22-fsum's transfer rule needs that tolerance (1.25–2 θ_ep). Set the library acceptance to 2 % below the band cutoff (stored as a value per |q|), or state 95 % as the band-count gate and 2 % as the release tolerance. | ch21 sec:21.6; ch22 we:22-fsum |
| 13 | M | E.16 library vs ch21 s21-6 "Operator 𝒪₂ adds four functions in each version, through 𝒯_e" and Table "(12 real functions in Si and Ge, 20 with 𝒪₂) … app:E.16" | GAP | E.16 holds 12 functions only; the kinetic row subsection is q = 0 only. Add the 𝒯_e rows at finite q (four per version) as external rows of the Dyson solve, with the PAW/all-electron kinetic vertex. | ch21 sec:21.6; ch22 tab:22-calc row 34 ("current and kinetic rows as external rows") |
| 14 | H | E.16 "Anisotropy": "14 to 107 meV lower at its off-axis minima, 0.13 to 0.34 rad from the valley axis" | WRONG | Ch13.9: minima 0.13 to 0.22 rad in the {001} planes (shallower in {011}), 14 to 107 meV below the axis, at |q| = 1.2–1.48 keV. | ch13 s13-9 sec:13.9-edges ¶ "The joint minimum leaves the axis" |
| 15 | M | E.16 "A recast for boosted dark matter" | GAP | Acceptance "reproduce the published limit to 5 %" omits what decides the light-mediator result. Add, in REF §4 wording: the heavy-mediator limit is unchanged; for a light mediator below about 3 keV the density-row ratio is 0.05–0.93 at 1 keV depending on the low-energy treatment of the flux (the source's flux table starts at 10⁻⁸ GeV), so the recast must state that treatment; it is undetermined until then. Quote no withdrawn number (0.139, ×2.7). | DC-54 via REF-DC-49-54-36 §4; ch21 s21-5 sec:21.5-corrected; ch22 tab:22-calc row 74, tab:22-gaps |
| 16 | M | E.14 (whole) vs ch10 s10-7, ch13 s13-8, ch17 s17-2, ch21 s21-7 ("the phonon-assisted kinetic row of app:E.14"), and E.16 kinetic ¶ ("needs the phonon-assisted row of app:E.14") | GAP | E.14 specifies only the density vertex (L^PA). Add a short paragraph: the same four-path amplitude with the 𝒯_e (p²/2m_e) vertex at q→0, ω = m_φ below the direct gap, all-electron/PAW kinetic matrix elements (E.16), same Wannier gauge, Sternheimer remainder, and the q→0 optical limit as control. | ch10 sec:10.7; ch13 sec:13.8; ch17 s17-2; ch21 s21-7 table and ¶ |
| 17 | L | ch08 s8-4 (frozen-phonon supercell with local fields in the supercell basis contains all three classes … "(app:E.14)") | WRONG pointer | The supercell route is E.16 ("Local fields in the phonon-assisted window", second calculation); E.14 only points there. Ch8 text should read app:E.16 (or E.14 should carry the supercell). | E.14 l.13 "supercell route in App. E.16"; ch13 s13-4, s13-9, ch22 tab:22-calc row 32 |
| 18 | M | E.20-magnet vs ch14 s14-2 (magnetoelastic B₁, B₂ "computed with spin–orbit coupling in DFT + U at a few strained cells (app:E.20)") | GAP | E.20 has no magnetoelastic item. Add to the magnet-inputs subsection: B₁, B₂ from the strain derivative of the anisotropy energy, SOC, ±0.5 % strains, check against ultrasonic data where it exists. | ch14 s14-2 |
| 19 | L | E.20-magnet vs ch14 s14-5 ("exchange, Dzyaloshinskii–Moriya and anisotropy constants … for T ≪ T_CM come from the DFT + U energy mappings of app:E.20-magnet, with SOC for the vertex of 𝒥_e") | GAP | Add DM constants (four-state mapping with SOC) for Cr₂O₃ to the quantities list. | ch14 s14-5 |
| 20 | L | ch14 s14-3 ("app:E.20-magnet specifies the linear spin-wave calculation with shape and dipolar sums for real samples") | WRONG pointer / GAP | Uniform modes with demagnetization are in the "Two-magnon responses" subsection (unlabelled), and dipolar lattice sums are not mentioned. Either label that subsection and point there, or move the sentence into E.20-magnet and add "dipolar sums and the sample shape". | E.20 two-magnon ¶2 |
| 21 | M | E.17 "Nuclear momentum distributions" acceptance "statistical error below 1 %" | GAP | E.19 (weak anharmonicity) and ch22 tab:22-calc row 58 anchor the template on the path-integral kinetic energy "within ±0.2 %"; ch11.5 shows the anharmonic change of E_kin in Si is at most ±0.2 %. A 1 % statistical error cannot anchor it: require ≤ 0.1 % on E_kin (centroid-virial), or state that the anchor is the harmonic-difference-corrected value with its error. | ch11 s11-5 (±0.2 %); ch22 tab:22-calc row 58 |
| 22 | L | E.17 vs ch22 tab:22-gaps row "Measured elastic constants of TeO₂ (app:E.17)" and "computed tensors offset by 4.8 %" | GAP | E.17 does not name TeO₂ or the 4.8 % offset. Add one sentence: where a ranking turns on a computed tensor (TeO₂ vs CaWO₄), the measurement is the requirement and the computed-tensor offset (4.8 % on average) is the nuisance. | ch21 s21-7; ch22 tab:22-gaps |
| 23 | L | ch12 s12-3 ("app:E.18 specifies a single code path that … reproduces each truncation of tab:12-truncations from one set of inputs") | GAP | E.18 does not say it reproduces the truncations. Add one sentence to "The crystal Migdal rate" (reported at each truncation of tab:12-truncations). | ch12 s12-3 |
| 24 | L | E.14 "Germanium and gallium arsenide" ¶3 "Since PBE nearly closes the gap" (GaAs) vs E.18 "0.5 eV in PBE against 1.52 eV" | WRONG (internal) | Use one statement; E.18's 0.5 eV is the quantitative one ("PBE puts it at about 0.5 eV"). | E.18 drag ¶3 |
| 25 | L | E.14 Fano ¶2 vs ch13 s13-6 | L | E.14: ≈3 meV "just below the Γ–L onset, 0.3 eV above the conduction minimum", 20–60 meV above it; ch13.6: "a few meV just above the conduction minimum and 20 to 60 meV higher up". Align: a few meV from just above the minimum to the Γ–L onset (≈3 meV at 0.3 eV), 20–60 meV above the onset. | ch13 s13-6 |
| 26 | L | ch13 s13-5 ("calculation specified for silicon, germanium and GaAs in app:E.14 includes [the measured edge at the measurement temperature]"); s13-5 "ε₂^PA branch by branch (app:E.14)" | GAP | E.14 states the measured-edge control for Si at 20 K only and never asks for branch-resolved ε₂^PA. Add "per branch, and for Ge (80/77 K data) and GaAs at the temperature of the data". | ch13 s13-5 |

## E.14 Phonon-assisted electron recoil

- Mass band 0.333–0.405 MeV; onsets 0.3332/0.3374; neutron-scaled 16.1 meV → 0.3336/0.3378; δm = 8.5×10⁻⁵ MeV per 0.3 meV; E_g(0) 1.170; E_x^b 14.7;
  ω_TA(Q*) 14.79 meV at 0.53 Å⁻¹; k_c 1.94 keV (1.906 at PBE a) → CHECKED (ch13 s13-1 l.73/79, s13-9, ch22 rows 31, 78). Arithmetic re-done with
  2/v_max² = 2.848×10⁵: 0.33319, 0.33767, 0.33359, 0.33778 MeV.
- Si TA 8 % soft at X and L at the measured a → CHECKED (ch05 s5-2: 4.13/4.49 and 3.17/3.43 THz).
- Zero-phonon side: 0.405–0.408 (0.407), glide class; second heavy hole 0.415–0.420; (2̄00) X-face ≈0.50 MeV, Σ|ρ|² = 0.150; hole 0.06 eV below
  the VBM; SOC +15 meV on first-hole bins; lead ≈0.42–0.43, band to ≈0.51 → CHECKED (ch13 s13-9 l.3–17, 53, tab:13-window; 62 meV, 15.5 meV).
- Bins: 21 |q| × 30 directions = 630 targets, 0.49–2.47 keV, ×12³ ≈ 10⁶ diagonalizations; 0.5 αm_e = 1.86 keV → CHECKED (units/arithmetic).
- Screening correction 0.3–2.6, pair channel unsized, supercell route → E.16 → CHECKED (ch13 s13-9 l.89, tab:22-calc row 32).
- Ge: PBE order wrong; HSE06+SOC values 0.64–0.69/0.79–0.83 eV, inversion 0.09–0.15 eV; DFT+α 0.749/0.918 eV, masses 0.101/0.053 m_e (+24/+39 %);
  next route GW; edge stays 0.32 MeV in 0.212–0.420 → CHECKED against DC-2, DC-2-alpha (DC says m_t +23 %, 0.101/0.0815 = +24 %: fine), ch13 s13-1 l.88,
  ch22 s22-1 l.97. Ge TA 13.5 %/11.6 % low → CHECKED (ch13 s13-9 l.108).
- GaAs: Γ 1.519, L 1.815, X 1.981 eV low-T; band 0.43 to 0.52–0.56 MeV; M_x v_max²/2 ≈ 1.04 eV < 1.52 eV; Fröhlich ε∞, Z* from measurement via
  eq:E.17-lst; split-off 0.34 eV → CHECKED (ch13 s13-9 l.110, tab:13-window). "PBE ε∞ tens of percent too large" quotes no withdrawn GaAs value
  (DC-91: do not use 21.8) → CHECKED; unsourced, cite a literature PBE value or E.4's Si overscreening as analogy (L).
- Fano map: |c^F| ≲ 0.3Γ/δ_F, Γ/δ_F 0.01–0.2, Si control zero → CHECKED (ch13 s13-6); wording item 25.
- f-sum: 0.81 (16 bands) → 0.89 (100 bands) at 0.1–0.5 Å⁻¹; eq:E.14-remainder dimensions (energy × |overlap|²) → CHECKED (ch13 s13-9 l.188, tab row 177).
- Truncation label n_B = 0, n_g = 2, n_T = 0 → CHECKED (ch08 s8-5 l.130).
- Pointers into E.14 (ch08 s8-6, ch09 s9-2/s9-3, ch13 s13-1/-2/-3/-6/-9, ch17 s17-1, ch21 s21-6, ch22 rows 30, 31, 38, 78–84) → CHECKED, except items 16, 17, 26.
- Executability: inputs, codes (QE, W90, EPW, BerkeleyGW, long-wave DFPT), grids, tests, costs (350–450 core-h + accelerator hours) present → CHECKED.

## E.15 Excitons and core states

- TDA factor: ε₁ 4.45 vs ε₁^res 3.05 at 0.71 Å⁻¹, 1.3 eV → 2.1; single oscillator E₀ = 9.1 eV → 2.2; retarded TDA ≈10 % → CHECKED (ch10 s10-5 l.86: 2.12, 2.23).
- Safe arrangement (TDA without head for proper ε₂ + RPA-LF screening) → CHECKED (ch10 s10-5 l.93).
- a_x = 4.2 nm, E_x^b 14.7 meV, ε∞ 11.7, split-off 44 meV → CHECKED (ch10 s10-5, ch13 s13-9 l.15).
- Kernel/storage numbers (24 576 pairs, ≈10 GB; 6.6×10⁵ pairs, 7 TB never stored) → CHECKED (arithmetic).
- Replica edge 0.3332 MeV; 10³ k per pocket; two-pair model chain → CHECKED (ch13 s13-8 l.46, l.54; ch22 tab:22-gaps row 77).
- Migdal exciton lines: 29 irreducible points of 8³ (correct count), |p| ≤ 5 keV → CHECKED (ch12 s12-3 l.62).
- STE Poisson series eq:E.15-ste; relaxation to sec:18.5 (Capture and excitons) → CHECKED (ch10 s10-5 l.125; ch22 tab:22-gaps row 51).
- Ge 3d doublet 29.2/29.8 eV, centroid 29.4; projection error ≤ 2 %, central 10⁻³, (Zα)⁴ ≈ 10⁻⁶; MV shift −0.58 % of total −0.76 % → CHECKED
  (ch10 s10-6 l.46, l.123–133; ch12 s12-5 l.69; ch22 tab:22-gaps rows 52).
- SOC lifts 3.6×10⁻⁶ (axis, Γ₈ quartet) and 1.3×10⁻⁴ (plane) → CHECKED (ch13 s13-9 l.55). Ge route → item 1. BSE Ge proviso → item 5.

## E.16 Electronic response libraries

- 12 functions (6 screened singlet + 6 IP; triplet = ¼) → CHECKED (app D.30 l.62; ch10 s10-4 l.37). Grid 250 |q| × 30 × 1000 ω = 7.5×10⁶;
  ≈2300 G at 8 αm_e (sphere/BZ = 2283), 85 MB, 600 TB → CHECKED (ch21 s21-6 l.9, l.15: 4 × 56 band pairs from 60 bands).
- Current screening 10–30 % estimate; spin-channel control ¼ IP → CHECKED (ch10 s10-4 l.115, s10-5 l.119; ch22 tab:22-gaps rows 48, 50).
- Ω_P,e = 0.51 eV, unity at 18 keV, 3×10² at 1 keV, true ≳10² → CHECKED (ch10 s10-2 l.110). eq:E.16-step dimensionless → CHECKED.
- Relativistic f-sum: −0.24/−0.76 % total, MV −0.18/−0.58 %, TF −0.23/−0.73 %, orbit–orbit ≈0.31 of MV → CHECKED (ch10 s10-6 l.123–127; ch04 s4-3 1.8×10⁻³).
- Supercell route, eq:E.16-dLF ≈10 core-h, n = 2/3/4 momenta → CHECKED (ch13 s13-4 l.126–130).
- Recast factor (1 − ω²/q²)², ≤ 2 % at v ≲ 0.1; citation liang2025plasmon = arXiv 2401.11971 → CHECKED (ch10 s10-9 l.127). Items 12–15 above.
- Pointers (ch08 s8-1/s8-8, ch10 s10-2/-4/-5/-6/-7/-9/-10, ch11 s11-7/-9, ch13 s13-4/-8/-9, ch17 s17-1, ch19 s19-3, ch21 s21-2/-5/-6/-7, ch22) →
  CHECKED except items 12, 13, 16. ch17 s17-1 / ch22 tab:22-gaps row 116 ("following density to several zone momenta with Umklapp and
  multiphonon terms"): E.16 static-step cells are 1×1×N along [100] (first-zone q); the unreduced-q sentence covers Umklapp only implicitly →
  GAP (L): state the q range to several q_BZ (q_red + G).

## E.17 Lattice libraries

- Shared base PBE/SG15/60 Ry, a = 5.431/5.658/5.653 Å; GaAs printed at 5.638 Å; Si 12³/8³ (29 irreducible), Ge/GaAs 8³/6³; costs ≈100/15/20
  core-h → CHECKED (ch05 s5-5 l.64, l.104; E.14 table; E.18 2× base).
- Per-branch tolerance (TA Si 10 %, Ge 15 %) and "Ge 12 to 14 % soft" (E.14: 13.5/11.6 %) → CHECKED (L: "11.6 to 13.5 %" would match E.14 exactly).
- D/c_ν 300–350 keV with D ≈ 9 eV, c = 8.43 km/s → CHECKED (ch13 s13-6 l.27; ch05 s5-2 l.175). Galilean term → CHECKED (app D.37 l.65).
- S per cell (eV⁻¹) vs per volume (eV²); eq:E.17-Wn dimensionless; temperatures 10 mK/1 K/77 K → CHECKED (ch11 s11-3 l.34).
- Coherent two-phonon to 10 keV, δ^coh_n → CHECKED (ch11 s11-3 l.122, s11-9 l.7). Anisotropy S₄/S₀ 0.028 (measured), 0.025 (PBE, q ≤ 0.3 q_BZ),
  |S₆/S₀| < 10⁻³ → CHECKED (ch11 s11-7 l.75).
- Charge vertex: ≈725/821 G per Q at 20 keV (sphere/BZ 706/797) → CHECKED (arithmetic); translation sum rule → CHECKED (ch11 s11-3 l.150, ch22 row 59).
- Contact density: 1.3×10⁻³ anisotropy, 𝓡_rel 8 % Si, 40–45 % Ge/Ga/As → CHECKED (ch22 tab:22-gaps row 70; ch12 s12-5 l.163).
- Isotope: 4096 atoms, Lifshitz +8.0 % at 50 meV → CHECKED (ch11 s11-6 l.161). Two-phonon: 293 K control 40–60 meV, margin 5.0×10³ → CHECKED
  (ch11 s11-6 l.181; ch22 rows 60, 63).
- Z*(ω) bound 0.9(ω/1 eV)², sum rules → CHECKED (ch12 s12-6 l.71–73). GaAs d = −1.21×10⁻³ per u at Z* 2.11, ε∞ 10.88; 0.4446/0.4405; 44 % and
  2.3 % → CHECKED (ch11 s11-8 l.86: terms 3.4× and 4.4× the sum). eq:E.17-lst = ch05 eq:5.5-LOTO rearranged → CHECKED. No DC-91 value quoted → CHECKED.
- PIMD (ch11 s11-4 l.50, ch19 s19-1 l.31) → CHECKED except item 21. Elastic/CsI → item 11; TeO₂ → item 22.

## E.18 Migdal and nonadiabatic quantities

- Trace 14 m_e (2.73×10⁻⁴); on-site 28.7 m_e (5.60×10⁻⁴) = 10.1 cores + 18.6 valence; band 12–24 m_e (book: 11.8–24.0) → CHECKED (ch12 s12-5 l.65–69, l.90, l.151).
- P_Mig ≤ E_R δM/(M E_g): 10⁻³ reached at 2.09 eV (on-site), 4.29 eV (trace) → CHECKED (arithmetic, sec:12.5-bounds).
- Φ(iω) = Φ(0) + ω²δM → CHECKED (app D.34 l.32). Diagonal LF ×1.35, off-diagonal ×1.2–1.4 model → CHECKED (ch12 s12-3/-4; ch22 rows 41–42, tab:22-gaps row 69).
- Wannier coefficient 1.56 (20 eV), 0.54 (50 eV, implicit), 0.25 (100 eV) → CHECKED (ch22 row 43). (200) zero, |S^bas|² = 2, 4; ≈230 G → CHECKED.
- 72 irreducible points of 12³; 16 MB per matrix, 32 GB per p; 300–1000 PW for |G| ≤ 4–6 a₀⁻¹ (292/980) → CHECKED (arithmetic).
- Pointers (ch12 s12-1/-3/-4/-5/-6, ch17 s17-4, app D.34, ch22 rows 41–44, tab:22-gaps 68–72) → CHECKED except items 4, 6, 23.

## E.19 Anharmonic, disordered and quantum solids

- Lindemann ≈¼ (model 0.23 at 21 cm³/mol), ϱ_MK = 2/3 at the Gaussian mean, Aziz potential, 1–40 GPa → CHECKED (ch11 s11-5 l.82–126, l.139).
- P ≈ 80 (SrTiO₃, 50 K), cells 320/1080/2560 and 512/1728 atoms, 80 ps for 0.5 meV, βω_D ≈ 25 at 1 K → CHECKED (arithmetic). Kubo conversion and
  TDSCHA two-phonon limit → CHECKED (ch11 s11-5 l.143).
- Weak anharmonicity: first-order cubic term vanishes by time reversal; n_A = 2; 384³ entries = 0.45 GB → CHECKED (ch11 s11-5 l.76, s11-9 l.9).
- Glass: A^IR from k→0⁺ of S^Z; locally neutral model forbidden; 15552² = 1.9 GB → CHECKED (ch16 s16-7 l.206).
- Random medium: σ_crit ≈ 1.2×10⁻³⁸ cm² (book 1.16×10⁻³⁸ at v = 10⁻³, Ti–6Al–4V, 20 eV); λ_dB ≈ 60 µm; ρ_χv² ≈ 5×10⁻¹¹ Pa (4.8×10⁻¹¹);
  "any bound … is a conjecture" → CHECKED (ch16 s16-7 l.210, l.246; DC-49/54/36: no withdrawn number — no a_sat 1.04×10⁻¹²/4.2×10⁻¹³, no u = 98/119/131,
  no 306 km/s, no ≈170 eV). eq:E.19-wall has units of pressure → CHECKED.
- Chiral frameworks: (𝟙 − 𝖬)⁻¹b for InF₃(4,4′-bipyridine) → CHECKED (ch14 s14-5 l.116, l.144; ch22 tab:22-gaps row 91). Crystal-field derivatives → CHECKED (ch14 s14-5 l.114).

## E.20 Magnetic, superconducting and Dirac targets

- Al: Δ_BCS 0.18 meV, v_max/v_F ≈ 0.39 (book 0.392), qξ ≥ 1.6 → CHECKED (ch15 s15-1 l.126, l.151). Item 9 for disorder.
- Holstein eq:E.20-holstein = eq:15.4-holstein (S form) → CHECKED, dimensions as ch15. Item 10.
- WSi: k_F𝔩_e 1.8–5.5, ⟨L⟩ not L(⟨ε⟩), (ε⁻¹)₀₀ → CHECKED (ch15 s15-3 l.140; ch22 rows 66, tab:22-gaps 98).
- Magnets: list YIG/NiO/MnO/Cr₂O₃/NiPS₃, convention J > 0 AFM, each pair once → CHECKED (ch07 s7-1 l.45, l.80; ch14 s14-1 l.27). g-tensor/orbital moments
  with SOC → CHECKED (ch14 s14-4 l.39; the book's symbol there is g_ion, E.20 writes g: L). Items 18–20.
- Two-magnon: 0.146 (S = ½) to 0.029 (S = 5/2) consistent with ch14 s14-1 (15 % at S = ½, 7.3 % at S = 1); 30³–40³ ladder → CHECKED (ch14 s14-2 l.74; ch22 rows 63–64).
- Optical activity: Te/α-quartz, Cr₂O₃, zero in Si → CHECKED (ch14 s14-5 l.63; ch22 row 65).
- Dirac re-plots: 642/5.03 at ε_bg 25.34, 1600/6.3 at 40, axis factors 9.5×10⁴/431/1.6×10⁴, Eq. (3.14) per-component rule → CHECKED
  (ch16 s16-1 we:16-factor, sec:16.1-zrte5). Items 7, 8. Optional (L): quote the orientation-averaged factor 4800–6600 (5200–6400 central) of ch16.
- Sommerfeld region (factor > 1.5 up to 1.33× the edge) lies inside the E.20 box 2Δ_D … 2Δ_D + 50 meV → CHECKED (ch16 s16-1 l.79; ch22 row 69).
- 15.4 spin-current (ALP) result: E.20 does not touch it and no chapter points E.20 at it → CHECKED (no conflict).

## Compute-record cross-check (state/DC-RESULTS.md)

| DC | E.14–E.20 status |
|---|---|
| DC-2 / DC-2-alpha | E.14 CHECKED (both failures stated, GW next, Ge edge stays estimate). E.15 l.56 WRONG (item 1); E.1 l.147 WRONG (item 2); E.16, E.18, E.15-BSE Ge routes items 3–5. |
| DC-41 | E.20 Al lacks the 𝔩_mfp scope and impurity ladder (item 9); no "screens less" wording, no film claim for the clean table → otherwise CHECKED. |
| DC-67 | No cascade-library table, reader, accuracy or tail law in E.14–E.20 → CHECKED. |
| DC-91 | No GaAs ε∞ 21.8 or ω_LO; GaAs Fröhlich inputs measured (E.14, E.17) → CHECKED. |
| DC-93 | E.17 CsI WRONG (item 11). |
| DC-49/54/36 | E.19 CHECKED (no withdrawn numbers; conjecture wording). E.16 recast lacks the §4 low-energy-flux statement (item 15). |

## Notes for the reviser

- Items 1–7, 11, 14 change a route or a number and should be fixed before the App. E gate; 9, 10, 12, 13, 15, 16, 18, 21 add missing
  specification items that chapters already promise; the rest are wording/pointer fixes. Items 2, 17, 20, 23, 26 touch chapter or E.1 text,
  not E.14–E.20; they are listed so the pointer and the specification can be aligned from whichever side the editor prefers.
