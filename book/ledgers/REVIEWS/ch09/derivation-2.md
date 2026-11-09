# Ch09 part 2: derivation check (s9-3, s9-4, tab9-3, s9-summary, ch09.tex)

Reviewer: derivation verifier (isolated). Date 2026-11-07. Tex not edited, nothing committed.
How the check was done: fig9_2.py and fig9_3.py were rerun on a scratch copy of tex/ and of the cached inputs, and both
logs and tab9-3.tex came out byte-identical, path strings aside. Independent recomputation used numpy (constants:
ħc = 1973.27 eV Å, m_e = 510998.95 eV, M_Si = 26.161 GeV, v_max = 794.5/299792.458). F-row leading-correction columns
were extracted by a script for all 75 boxes. The cited sources (arXiv 1509.01598, 2101.08275, 2101.08263) were fetched
into sources/review-ch09/; PDFs deleted.
Verdicts: CHECKED = redone and agrees; WRONG = needs a fix; GAP = judgment or a missing link, with a proposed fix.

## Summary of non-CHECKED items
| # | Location | Verdict | Item |
|---|---|---|---|
| 1 | s9-4 l.3 | WRONG | "give 75 of them a box": 80 of the 90 formulas sit in the 75 boxes |
| 2 | s9-3 l.18 | WRONG (minor) | 46.7 MeV ignores the reduced mass; 46.8 MeV |
| 3 | tab9-3 / fig9_3.py, 11.5c | GAP | Markov–Krein band on n_A; its leading correction is not an anharmonic step |
| 4 | tab9-3, 12.4b (12.4a) | GAP | 𝔐 vs n_B: 8.5 says phonon-final-state formulas carry this on n_B |
| 5 | tab9-3, 10.3a | GAP | electron gas → crystal is a target-model step, not 𝒳 |
| 6 | s9-4 l.53 vs App F | GAP | 23 Part II boxed F rows do not name their Limit Check in column 1 |
| 7 | fig:9-qomega caption | GAP | plasmon drawn to 2.24 keV; the text says the line ends at q_c = 2.60 keV |
| 8 | s9-3 l.52 | GAP | "size is an open question" in GaAs, but 13.6 gives an estimate |
| 9 | WE 9.3, [111] | GAP (wording) | "inside the window" by only 11 meV |
| 10 | tab:9-supports, NiO | GAP (wording) | "gap 4.54 meV (model)": 4.54 meV is measured |
| 11 | s9-4 l.37 | GAP (wording) | "Every Migdal formula is already at n_B = 2": not 12.6a |
| 12 | s9-summary l.9 | GAP (wording) | the Limit Check definition omits the 48 qualifier boxes |
| 13 | fig9_3 header | GAP (minor) | n_T parameter shown as n_{Qν}; tab:8-params has T/ω_{Qν} |

## Section 9.3 and Fig. 9.2

### Fig. 9.2 data and fig9_2.log
- Rerun of fig9_2.py (cached npz only): log identical, 42 lines. CHECKED.
- 2π/a = 2282.9 eV, k_c = 0.85(2π/a) = 1940 eV, q_BZ = (6π²/Ω)^{1/3} with Ω = a³/4 = 2.25 keV (11.1 l.39). CHECKED.
- ⟨u_x²⟩ = ⟨ω⁻¹⟩/2M = (1973.27)²/(2·26.161e9·0.0304) = 2.448e-3 Å² (log 2.446e-3; 11.4 has 2.45e-3). CHECKED.
- 2W_κ = q²⟨u_x²⟩ (NOTATION: 2W_κ = q·B_κ·q, cubic): 0.0157, 0.0628, 1.005 at 5, 10, 40 keV. CHECKED. Dimensionless.
- E_R = q²/2M = 0.478 meV at 5 keV. CHECKED. x_R = 1 at q = (2M·40.9 meV)^{1/2} = 46.3 keV; x_R = 4 at 92.5 keV (11.4 l.93). CHECKED.
- Lattice-band quantiles 11–60 meV (q_BZ), 13–129 meV (46 keV), 46–311 meV (92.5 keV): reproduced by the rerun (Poisson
  compound of p₁ ∝ g/ω). CHECKED.
- Phonons: TA and LA at X 17.1 and 50.7 meV, optical at Γ 63.7 meV (PBE). The text's 17, 51, 64 meV CHECKED. In ch09.tex,
  64.1 meV is the measured value (NOTATION l.509). CHECKED.
- Free recoil crosses E_g: q = (2M·1.17 eV)^{1/2} = 247.4 keV. CHECKED. 95 % edge: solving E_R + 1.645(E_R⟨ω⟩)^{1/2} = 1.17 eV
  gives E_R = 0.861 eV, q = 212.3 keV. CHECKED.
- l.18 "heavier than 46.7 MeV": **WRONG (minor).** The log uses q/(2v_max). With the reduced mass, q_max = 2μv_max gives
  μ = 46.68 MeV and m_χ = μM/(M − μ) = 46.76 MeV. Write "46.8 MeV". Cross-file note: 9.2 l.3 quotes "about 45 MeV
  (Sect. 1.3)", which 1.3 computes with E_g = 1.11 eV; at 1.17 eV it is 46.8 MeV (for the 9.2 reviewer).
- Impulse band opens at 92.5/(2v_max) = 17.45 MeV (17.46 MeV with μ), printed as 17.5 MeV. CHECKED.
- E_min(0) = 3.17 eV and 1.77 eV at 1 keV (13.6 l.3: 1.77). CHECKED.
- Valley-image radii |k_c + G| (BCC reciprocal vectors, valleys at ±0.85 X): (−1.15,0,0) 2625 eV, (−0.15,1,1) 3247 eV,
  (0.85,2,0) 4961 eV, (−1.15,2,0) 5267 eV, (1.85,1,1) 5316 eV, all recomputed by hand. CHECKED. No radius between 3.25 and 4.96 keV.
- Gap of 0.72 keV above 6.4 keV; half of it: 360²/(2·1.193·m_e) = 0.106 eV ("about 0.11 eV"). Pair mass 1.19 m_e as 13.1/13.3. CHECKED.
- **3.25–4.96 keV, 2.07 eV upper bound.** max over q of min(E_[100], E_[110], E_[111]) = 2.065 eV at 4845 eV. The minimum
  over all directions is ≤ the minimum over three of them, so the value bounds the onset from above only, as the text says.
  CHECKED (the editor note accepts it as stated; agreed).
- Loss peak (DarkELF tables, RPA + LF): 18.9 eV at 0.49 keV; 22.3 eV in the 2.28 and 2.45 keV bins (recomputed from the
  npz); 18.9 − 16.4 = 2.5 eV. CHECKED. The global maximum of L is 3.74 (gray scale 1e-3 to 4). CHECKED.
- Plasmon: ω_p = 16.6 eV; q_c = 2.60 keV (4.5, 10.3 l.72, NOTATION l.377). CHECKED. ω_pl² = ω_p² + (3/5)q²v_F² is
  dimensionally consistent. Exciton 14.7 meV (10.5 l.3). 2p 99.4 eV, 2s 150 eV (3.5 l.101). Peaks 3.4 and 4.2 eV (4.4 l.96). CHECKED.
- Phonon-assisted onset E_g + ω_TA(k_c − q): 1.1871 eV (q → 0) and 1.1840 eV (1 keV); ≤ E_g + 63.7 meV = 1.234 eV.
  Matches the NOTATION definition E_min^PA = E_g + min_ν ω. CHECKED.
- Window along [100]: 1.184–1.467 eV at 1 keV; closes at 1.268 keV, reopens at 3.297 keV. These agree with 13.6 l.86
  (1.184–1.467, 1.27, 3.30). CHECKED.
- Caption v_max = 2.650e-3 = 794.5 km/s (NOTATION l.45). CHECKED.
- **Caption, plasmon** (#7): **GAP.** "dashed ... up to its cutoff at 2.24 keV" is the cutoff of the quadratic form
  (10.3 l.72). The prose (l.22, l.62) and WE 9.3 say the line ends at q_c = 2.60 keV. Both values are right, but a reader
  sees the dashed line stop at 2.24 keV. Fix: "up to 2.24 keV, where the quadratic form meets the pair continuum (the exact
  RPA zero ends at q_c = 2.60 keV)".

### No overlap between the phonon-assisted region and the multiphonon band in Si
- The phonon-assisted region lies at ω ≥ 1.184 eV for all q. The 95 % edge of the lattice band stays below 1.17 eV for
  q < 212 keV (above, solved), and the free recoil for q < 247 keV. So the drawn regions do not meet below 212 keV. Above
  212 keV the impulse band meets both electronic sectors (P_0 and P_+), which l.18 and l.38 say generically. Only the
  Poisson/Gaussian tail beyond the 95 % quantile reaches E_g at lower q, and the caption's "central 90 %" covers that.
  Consistent with Ch13 (no contrary statement in 13.1/13.6/13.9). CHECKED.

### tab:9-overlaps sizes vs 17.4 and 8.6
- Row 1: Z = 14 nucleus and 14 following electrons, so the charge vanishes at long wavelength; 196 + 196 = 14² + 14², and
  interference removes both. CHECKED against 11.2 (Born charge 0 in Si) and 17.4.
- Row 2: (1 + Z m_e/M)² − 1 = 2Z m_e/M + (Z m_e/M)² = 5.469e-4 + 7.5e-8 = 5.47e-4, with m_e/M = 1.953e-5 (17.4 l.11: 1.95e-5,
  5.47e-4). CHECKED. Note: the column says "Term: cross term S^0_eκ", and the cross cell alone is 2Z m_e/M = 5.469e-4; the
  number quoted also contains the Migdal cell (7.5e-8). They agree to three digits, so no change is needed.
- Row 3: "the same fraction, 5.47e-4" (17.4 l.85). CHECKED. "Vanishes for a coupling in proportion to mass" means a
  coupling to electrons and nuclei in proportion to mass (−λm_e + λm_e = 0, 17.4 l.13). CHECKED (the l.48 prose is clear).
- M_κ/m_e = 26.161e9/0.511e6 = 5.12e4. CHECKED.
- Row 4: "zero for every one-body self-energy ... nonzero in GaAs" (8.6 l.188, 13.6 l.116). CHECKED.
- l.52 (#8): **GAP.** "in GaAs ... their size is an open question that App E.14 specifies a calculation for". But 13.6
  l.116 already estimates |c^F_ν| ≲ 0.3 Γ_m/δ_F, which moves "a few percent at most" of first emissions. Fix: "estimated in
  13.6 to move a few percent at most of the first emissions; App E.14 specifies the calculation that sizes them".

### Reach (9.3-reach)
- ω_max = m v_max²/2 at q = m v_max: 1.054 eV at 0.795 keV, q ≤ 1.59 keV (0.3 MeV); 3.512 eV (1 MeV); 35.1 eV, 53.0 keV,
  2W = 1.765 (10 MeV). 2W ≤ 0.0016 (0.3 MeV) and 0.018 (1 MeV, at 5.3 keV). CHECKED.
- Gap crossing for 1 MeV: q = mv ± (m²v² − 2mE_g)^{1/2} = 2650 ± 2164 eV, i.e. 0.486–4.81 keV. CHECKED.
- q_c v_max = 2600 × 2.6502e-3 = 6.89 eV. CHECKED.

### WE 9.3 (q = 5 keV, ω = 2 eV) and its direction dependence vs 13.6
- qv_max = 13.251 eV; m ≥ q²/[2(qv − ω)] = 25e6/22.50 = 1.111 MeV. CHECKED. Dimensions: energy.
- v_min = ω/q + q/2m = 4.00e-4 + 2.50e-4 = 6.50e-4 = 194.9 km/s. CHECKED.
- 2/0.0637 = 31.4, so "at least 32 phonons". CHECKED.
- Edges 2.590, 2.015, 2.311 eV along [100], [110], [111] (cached PBE edges, rerun). Edge minus δ_w: 2.290, 1.715, 2.011 eV.
  The [100] and [111] points lie in the window and [110] in the margin, as stated. CHECKED.
- Image at 4.961 keV: (5000 − 4961)²/(2·1.193 m_e) = 1.2 meV ("about 1 meV"). CHECKED.
- L(2 eV) = 8.84e-4; the maximum is 0.326 at 35.7 eV (q bin 4959 eV, recomputed from the npz). CHECKED.
- Migdal moment estimate (E_R/6 eV)(Z m_e/M) = (4.78e-4/6)(2.735e-4) = 2.2e-8, dimensionless. CHECKED.
- Against 13.6: 13.6 l.90 applies the window "point by point ... for each bin of (|q|, q̂)", with the edge taken as the
  full-k-grid minimum, not a symmetry line. The WE's closing sentence matches this. CHECKED.
- [111] (#9): **GAP (wording).** The point lies inside the window by only 2.011 − 2.000 = 11 meV. That is less than the
  exciton binding (14.7 meV), and less than the difference between a symmetry-line edge and the full-grid minimum that 13.6
  prescribes. Suggest "just inside the window along [111] (by 11 meV)", so that a reader does not take [111] as robust.

### tab:9-supports, each number vs its home
- GaAs ω_L 36.35 meV (11.2 l.3). He below 3 meV (11.5 l.124). NiO top 118 meV (14.1 l.110). Two-magnon up to 236 meV
  = 2 × 118 (14.2 l.3, l.50). CHECKED. The convention ("to twice the band top") is stated in the Support column, as the
  editor note asks. CHECKED.
- NiO "gap 4.54 meV (model)" (#10): **GAP.** In 14.1 l.126, 4.54 meV is the far-infrared measured zone-center magnon,
  which the anisotropy K = 0.0973 meV is chosen to reproduce in an otherwise gapless model. Write "gap \SI{4.54}{meV}
  (measured; anisotropy added to the model)".
- α-quartz q g₃₃ = 7e-5 at 2.1 eV (14.5 l.3). ²⁰⁷Pb: 1 neV/h = 241.8 kHz; 241.8 kHz/9.034 MHz T⁻¹ = 26.8 mT (14.6 l.178). CHECKED.
- Al 2Δ_BCS = 0.36 meV (15.4 l.3; NOTATION l.621). ZrTe₅ Δ_D = 11.8 meV (16.1 l.64; CORRECTIONS l.642). CHECKED.
- Dirac continuum: min over k of E(k) + E(k+q) = 2(Δ² + v²q²/4)^{1/2} = (4Δ² + v²q²)^{1/2}. CHECKED.
- Particle–hole band ω ≤ qv_F + q²/2m: CHECKED. Nanotube plasmon 3.4–6.9 v_max, ω = v_D q/g_c (16.2 l.3, l.74). CHECKED.
- PbS dot 1.2 eV; graphene 4.3 eV (16.3 l.3, l.12). Anthracene 3.1 eV (16.4 l.3). Si:P 45.59 meV (16.5 l.3). H₂ 4.75 eV;
  displacement tens of eV (16.6 l.3). TLS 1.2e20 eV⁻¹ cm⁻³ (16.7 l.107). MHz/kHz (11.8 l.3). CHECKED.
- Absorption point q = m_φ v ≈ 1e-3 ω. CHECKED.

### 9.3 opening
- (50 keV, 50 meV): phonons only. (1 keV, 1.3 eV): inside the window, 1.184 < 1.3 < 1.467. (1 keV, 3 eV) > 1.77 eV, so a
  zero-phonon pair is open. CHECKED.
- ch09.tex: ½ m v_max² = 3.51 eV at 1 MeV; E_g 1.17 eV; Al 0.36 meV. CHECKED.

## Section 9.4, Fig. 9.3, Table 9.3

### fig9_3.py rerun
- Rerun on a copy: tab9-3.tex and fig9_3.log identical. 75 boxes; per chapter 15/20/9/2/8/3/17/1; nA 3, X 12, nT 1, K 6,
  M 3, nD 2 (27); LW 5, KH 9, DM 5, TM 29 (48); Ch10 8/15, Ch11 7/20, Ch12 7/9, Ch14 0/8, Ch16 2/17. Every count printed in
  9.4 l.37–39 and in the Summary matches the log. CHECKED.
- QUOTES (0.05/0.22/0.47; > 10⁴; x_R ≥ 2.3 at q ≥ 70 keV; 0.54 eV) are asserted present. 46.3·√2.3 = 70.2 keV. CHECKED.

### Axis assignment, sampled from each box's stated leading correction (all 75 read; ≥ 25 verified in detail)
Each bold \Fsize entry and plotted comparison of the F row was read against the axis and against 8.5 l.79–104 and 8.8 l.7.
CHECKED (axis follows from the leading correction): 10.1a (screening ×0.47, X); 10.5a (coupling block, X); 10.7a (vacuum
vs in-medium, X); 10.9a (screening ×9.4–18.5, X); 10.9d (medium n_r, X); 12.3a (local fields ×1.35, X); 12.6a (medium
factor, X); 13.5a (e–h attraction, X); 15.1a, 15.2a (pair-field ladder, X); 16.1a (remote-band ε_bg, X); 10.2b (relaxed
lattice, K); 11.3a (δ^coh, K); 11.4a, 11.4b (Doppler width / e^{−2W}, K); 11.3b (quantum occupations, nT); 11.5a (λ₃⁴k²,
nA); 11.5b (correlations beyond SCHA, nA); 12.2a, 12.2b (O(ξ_D²), nD); 12.3b (motion of the nucleus, M); 12.4a (Doppler
9/5 v_N²p²/ω_e², M, as placed by 12.4 l.77); 10.3b, 11.1a, 11.2a, 16.2a, 16.2c (LW); 10.8a, 11.1b, 11.2b, 11.7a, 11.8b,
12.3c, 14.6a–c (KH); 10.4a, 10.8b, 10.9b, 10.9c, 16.7c (DM); 10.7b, 11.1c, 11.2c, 11.2d, 11.6a, 11.6b, 11.8a (largest is
isotopic mass, 5 %), 11.8c, 12.3d, 13.7a (supercell convergence, off-label per 8.5 l.106), 14.1a (1/|S|), 14.3a–14.5b,
15.4a (normal → BCS reference), 16.2b, 16.3a, 16.3b, 16.4a, 16.5a, 16.7a, 16.7b, 16.7d, 16.8a–d, 17.5a (TM).
Judgment calls (editor Q1):
- **10.2 loss-function boxes → lattice (10.2a, 10.2b): CHECKED, with a note.** The correction is the acoustic peak of the
  following electrons, which comes from releasing the nuclei. 8.5 l.97 says 𝒦 "does not apply" without phonons, and 8.8 l.7
  defines the lattice step as the next term of the multiphonon series. So "clamped → one-phonon" is the n = 1 term entering
  from 𝒦 n/a, which is what WE 9.4 says. Acceptable.
- **Colour centres → lattice (16.6a): CHECKED.** The leading correction is the zero-point Doppler width (3.5–5.4 % of E_d),
  the impulse-width step, as in 11.4a. The step label "impulse → bound atom" is not a 𝒦 value. Suggest "impulse → finite
  width" or "impulse → multiphonon" (cosmetic, in the CLASS table).
- **Markov–Krein → anharmonic (11.5c), #3: GAP. Recommend TM.** The box plots the exact band width ϱ_MK against its
  tail form, for harmonic Si at 100 keV and for a Gaussian. Its leading correction is "the skewness, relative 1/ξ" (caption
  and F row), which is a term of the moment-problem asymptotics in ξ. No step along n_A is made. The F placement is "exact
  moments, no assumption on 𝒦", and 11.5 l.110 says the band is exact in n_A, so n_A is not the axis of the correction.
  If moved: nA 3→2; on a component 27→26; TM 29→30; qualifiers 48→49; Ch11 7→6 of 20. Fix 9.4 l.37 ("Twenty-six",
  "two on the anharmonic order"), l.39 (49, 30, "six of twenty"), Summary l.9 (26/49). Edit CLASS in fig9_3.py and rerun.
- **12.4b on 𝔐, #4: GAP (editor call).** 8.5 l.99: "Where the phonon final states are kept, at small x_R, the same physics
  is carried by n_B and 𝒦 instead". 12.4b keeps multiphonon final states. Its leading correction, 2⟨ω_ph²⟩/ω_e² = 2.9e-3, is
  the step that tab:8-params prices as "(ω_opt/E_g)² = 3×10⁻³ per step of n_B". But 12.4 l.137 places it at 𝔐 = sudden, and
  the script follows the home section. Options: (a) reclassify 12.4b as n_B: 2 → 4, and replace 9.4 l.37 "None of the boxes
  has its leading correction on n_B ... none has its next step in n_B" (Migdal axis 3→2); or (b) keep it, and add a clause
  in 9.4 saying that the home section labels the bound denominators as 𝔐 although 8.5 assigns that physics to n_B. 12.4a
  (moving-nucleus Doppler term) can stay on 𝔐.
- **10.3a on 𝒳, #5: GAP.** In the F row the correction is led by "the gap and the interband absorption peaks" (×24 at
  2 eV); local fields come only "then". Going from the homogeneous electron gas to crystal bands is not a step of 𝒳
  (8.5 l.93: the Lindhard function is the IP bubble of the gas). It is a change of target model. Recommend TM: X 12→11,
  Ch10 8→7 of 15. If #3 is also adopted, the totals become 25 on the label and 50 on qualifiers (TM 31). Otherwise give a
  reason in the 9.4 text.
- **Target-model group: CHECKED.** No other TM box has a leading correction on a component. The 11.8a static-vertex term
  (ω_L/E_g)², which is an n_B step, is 0.3 %, below the 5 % isotopic term. 13.7a's fourth-order (1 %) and nonadiabatic terms
  are secondary to the supercell convergence the box plots, and 8.5 puts numerical parameters off the label.

### No-box rows
- 10 rows; 13.3 phonon-assisted electron recoil is the only n_g = 4 step, consistent with l.37. CHECKED.

### WE 9.4 against the 𝔗 definition of 8.5
- Crystal form factor: all base values; n_D not applicable (the plane wave is kept whole); "𝔗₀, unscreened" = F row,
  8.5 l.104 (base point and qualifier). Numbers 0.05/0.22/0.47 = F row and 10.1a ("twentyfold", "fourfold" ≈ 1/0.22).
  Source Eqs. (3.13) and (3.17) of essig2016direct: the paper itself calls these "the key results" (PDF). CHECKED.
- Loss-function rate: exact identity, 𝒳 as computed; clamped lattice; the step to one phonon is a lattice step (see the
  judgment above). knapen2021dark Eqs. (6) (S through Im[−1/ε]) and (13) (rate), and hochberg2021determining Eq. (1)
  (rate through the ELF), all verified in the sources. "> 10⁴" = 10.2a. CHECKED.
- Free nuclear recoil: 𝒦 = impulse at zero width, n_B = 0. Mean exact by the sum rule; correction x_R^{−1/2} (8.5 eq.
  width). x_R ≥ 2.3 ↔ q ≥ 70 keV. For lim:1.3a, x_R ≥ 9 follows from (E_Rω₀)^{1/2} < E_R/3 ⇔ E_R/ω₀ > 9, and 9 × 60 meV =
  0.54 eV (9.4 l.3). CHECKED.

### App F counts (90/80/10/6)
- 90 Part II rows, 10 "(no box)", 6 with an unsized correction (10.9 ×2, 12.3d, 14.1 no-box, 15.4 no-box, 16.3 no-box).
  CHECKED. Count by label: 53 boxes are referenced in column 1 and 22 are not (below); five boxes have two rows (10.8b,
  14.3a, 14.5a, 16.6a, 16.8a), so 75 + 5 = 80 boxed rows. CHECKED.
- s9-4 l.3 (#1): **WRONG.** "recover 90 published formulas ... and give 75 of them a box". 9.4-appF and the count give 80
  formulas in 75 boxes. Fix: "... and test 80 of them in 75 boxes of the same kind".
- s9-4 l.53 vs App F (#6): **GAP.** The text says column 1 gives "its Limit Check if it has one". Yet 23 boxed rows (all
  16 Chapter 10 rows and the 7 rows of 11.1–11.2) cite no \cref{lim:...} in column 1. Fix at the App F completion (add the
  references). Suggest that fig9_3.py assert that every non-"(no box)" Part II row names a box, since 80 is now obtained by
  subtraction (90 − 10).
- 14.3a rows without a 𝔗 placement: known (editor Q2), not re-reported.

### Other 9.4 statements
- l.37 (#11): "Every Migdal formula is already at n_B = 2". 12.6a (Migdal-type absorption) is placed at "no
  Born–Oppenheimer truncation (exact identities)". Write "Every Migdal scattering formula". GAP (wording).
- 9.4-plot: 𝔗_k⁺ and δ_k as in 8.8 l.7–11; tolerance list 10 / 1 / 15 % (15 % occurs in two captions). CHECKED.
- 9.4-place: impulse width x_R^{−1/2}; Migdal at dipole order n_D = 2 vs ξ_D (8.5 l.101). CHECKED.
- Fig. 9.3 header (#13): the n_T column shows n_{Qν}, while tab:8-params lists T/ω_{Qν} as the parameter (n_{Qν} only as
  its value). Use T/ω_{Qν} in AXIS_PARAM. GAP (minor).

## Summary (s9-summary.tex) against final 9.1–9.4
- 24 × 6 = 144 cells; 54 filled, 90 empty; four reasons; four electronic rows as one S^0_ee (9.1 l.3, l.65, l.75). CHECKED.
- Floor 2ω_th/v_max²; excess of the acoustic edge v_max²/[4c(v_max − c)] ≈ v_max/4c; 6.12 keV = 1e-3/(2·3.119e-5·2.619e-3)
  eV; ratio to the floor 0.285 keV is 21.5. CHECKED (9.2 l.20, l.82). Plasmon closed at 3.6 v_max (9.2 l.22). CHECKED.
- 0.333 MeV onset and 0.405–0.408 MeV zero-phonon edge (9.2 table; CORRECTIONS l.314, l.335; SOTA l.637–638 [CALC]). CHECKED.
- Free nucleus ∝ √ω_th (q = (2Mω)^{1/2}, m = q/2v). 2/v_max² = 2.85e5, i.e. 5.45 decades ("five and a half"). Halo
  scaling v⁻² (flat) and ≈ v⁻¹ (acoustic, m = ω/2c(v − c)). CHECKED.
- 9.3 paragraph: matches the 9.3 text. CHECKED.
- 9.4 paragraph: 75/27/48, "every magnetic one" (Ch14 0/8), six of 90 unsized. CHECKED against the current log. These
  change if #3, #5 or #4(a) is adopted.
- l.9 (#12): **GAP (wording).** "compares a published formula ... with a fuller result one step further along one axis
  of the truncation label". That holds for 27 of 75. Add "or in a parameter that the label records in words".

## NOTATION and conventions
- E_g, E_min, E_min^PA, δ_w, 𝒫_ad/𝒫_0/𝒫_+, c^F_ν, S^A_ab, q_BZ, k_c, x_R, 2W_κ, v_max, ω_L, Δ_BCS, Δ_D, 𝔗, 𝔗₀, 𝔗_k⁺ are
  used as defined. No factor-of-2 drift: Δ_D is the half-gap, the Dirac continuum uses 4Δ_D², and the 9.2 floor uses
  4Δ_D/v². No 2π drift: 1 neV ↔ 241.8 kHz uses h, not ħ. No π or sign drift found. Dark-photon sign Ṽ_κ = −Z_κṼ_e with
  the amplitude 1 + Z m_e/M, as in 17.4.
- Campaign numbers (0.333, 0.3374, 0.405–0.408 MeV; Δ_D 11.8 meV; δ_w 0.3 eV) agree with CORRECTIONS and SOTA. No DC-RESULTS
  item is quoted in these files.
