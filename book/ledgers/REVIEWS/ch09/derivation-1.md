# Ch09 part 1 (ch09.tex, s9-1.tex, s9-2.tex): derivation check

Reviewer: derivation verifier (isolated), 2026-11-07. Inputs: the three tex files, NOTATION.md, STYLE.md, figscripts/ch09/fig9_1.{py,log}, the current tex of Ch01, 03, 05, 07, 08, 10–17, 20, 22, state/CORRECTIONS.md, state/SOTA.md, state/DC-RESULTS.md, and Kahn & Lin arXiv:2108.03239 (fetched to sources/review-ch09/; PDF deleted). Algebra was checked with sympy and numbers with numpy (scratch script, nothing heavy). The tex was not edited.

Verdict: the 9.2 algebra is correct throughout (eq:9.2-mch, all five cases, eq:9.2-halo). Every Table 9.2 number reproduces. Table 9.1 has three '—' cells whose section does compute the channel. Several symmetry-allowed cells are computed nowhere, and tab:22-gaps does not list them. Two counts in WE 9.1 are wrong. One convention drift in the new aluminum edge, and bare `c` against NOTATION.

## A. Section 9.1: Table 9.1 (tab:9-atlas)

Counts: 24 rows, 54 non-empty cells, column counts (14, 6, 8, 11, 10, 5). The prose's "54 of 144", "90 empty" and "eleven cells of the vector column" match the table as printed. They change if A2 is applied.

### A1. Non-empty cells against the home section's tex (CHECKED unless stated)
- Pairs: 10.1 density, 10.4 spin, 10.7 vector, 10.7 ALP/scalar (10.7-scalar subsection), 10.9 inelastic/boosted/fermionic. CHECKED.
- Plasmons: 10.3 density. 10.7 vector: the in-medium conversion at 16.4 eV is s10-7 l.23, CHECKED. 17.3 inelastic: the plasmon pole in eq:17.3, and tab:17-endo "Si plasmon closed", CHECKED.
- Excitons: 10.5 density and 10.5 spin (sec:10.5-triplet), CHECKED. 10.7 vector and ALP: **GAP (weak home).** 10.7 reaches excitons only through measured optical data (and the triplet/exchange remark at l.63). The computed excitonic absorption in Si is the phonon-assisted replica of 13.8. Keep the cell, but the text at l.69 or the caption should say that 10.7 uses measured ε.
- Core: 10.6 density. CHECKED.
- Single phonons: 11.1 nuclei, 11.6 spin, 11.8 vector and ALP/scalar (11.8 has the scalar-on-electrons line), 17.3 inelastic: all CHECKED. 11.2 density: **GAP (editor Q2).** 11.2 computes a *charge* coupling (dark photon, vertex Z*/ε_∞). The only *electron-only* single-phonon rate in the book is the acoustic peak of 10.2 (s10-2 l.30–33, l.95–97, model), which 17.1 uses (tab:22-gaps row "Electron-following density at finite q"). For an electron-only coupling the polar vertex is the electronic part of the Born charge, not Z*. Correction: home 10.2 (acoustic peak, model), with 11.2 for the charge-coupled polar case. Or keep 11.2 and say in l.69 that the electron-only acoustic part is in 10.2. At l.79, "In a polar crystal they enter through the Born effective charges" should read "through the electronic part of the Born charges".
- Multiphonons: 11.3 density (charge vertex Z_κ − f_κ(q), s11-3 l.150) and 11.3 nuclei, CHECKED. 11.6 spin: CHECKED. 11.6 uses the self response eq:11.3-inc at all phonon orders (s11-6 l.44–46).
- Free recoil: 11.4 nuclei and 11.4 inelastic (subsection "Fermionic absorption on nuclei"), CHECKED. 11.6 spin: CHECKED, but only implicitly. 11.6 never mentions the impulse regime, and the cell rests on the large-q limit of the incoherent self response. Suggest one clause in 11.6 or in the 9.1 prose.
- Solid He 11.5 nuclei: CHECKED.
- Migdal: 12.3 nuclei and 12.6 scalar absorption (Migdal-type absorption of a scalar), CHECKED.
- Phonon-assisted: 13.3 density, 13.8 vector, 13.8 ALP and scalar (s13-8 l.103–110), CHECKED.
- Magnons: 14.1 spin, 14.3 vector (B′ coupling, s14-3 l.16), 14.3 ALP, 17.3 inelastic, CHECKED.
- Two-magnon and magnon–phonon: 14.2 spin, CHECKED.
- Chiral/nonreciprocal: 14.5 spin and 14.5 ALP (single-molecule magnets l.142; multiferroic axion l.159), CHECKED.
- Precessing nuclear spins: 14.6 ALP, CHECKED.
- Superconductors: 15.1 density, 15.4 vector, 15.4 ALP (spin-current absorption), CHECKED. Sector "(2,0)" holds for impurity-assisted absorption. Phonon-assisted absorption in 15.4 is (2, m≥1). Write "(2,0), (2,m)" or add a note.
- Dirac: 16.1 density and 16.1 vector (s16-1 l.73), CHECKED. 16.2, 16.3 density and 16.3 vector (aligned tubes l.80, dots l.118), 16.4 density, 16.5 density and vector, 16.6 nuclei, 16.7 density (sec:16.7-scat, electron-density vertex f_TLS) and vector: all CHECKED.
- Acoustic body modes: 11.8 ALP/scalar, CHECKED.
- Mobile defects row (16.8, 19.6): **WRONG gloss (editor Q4).** s16-8 has no defectons. It treats TLS relaxation and mentions "crowdion" once, as an app:E.22 specification (l.37). Defectons (9 hits) and crowdions (7 hits) are in 19.6. Correction: cite 19.6 alone for defecton and crowdion kinetics, or "TLS kinetics 16.8; defectons, crowdions 19.6". The same applies at l.93: "through the defect kinetics of 16.8, 19.6" should become "of 19.6, and of two-level systems in 16.8".

### A2. '—' cells whose section does treat the channel: WRONG
1. **Core × vector abs.** 10.7 (s10-7 l.23) computes dark-photon absorption through the L and K edges ("agree to 10% for every mass above 63 eV"). Enter 10.7.
2. **Chiral/nonreciprocal × vector abs.** 14.5 l.142: single-molecule magnets absorb "a dark photon through its magnetic field, as in 14.3", and the ALP in a static field is treated as a dark photon with ζ = g_aγγB₀/m_φ. Enter 14.5.
3. **Acoustic modes of the whole body × vector abs.** 11.8 (sec:11.8-bar, l.116–125) derives dark-photon absorption by the modes of a finite body (eq:11.8-shape, depolarization factor, shield factor). Enter 11.8.

With these three entries: 57 of 144 cells, 87 empty, 14 cells in the vector column. Then update l.15 (54, 90), l.87 ("90 empty cells"), WE 9.1 l.114 ("eleven cells"), and s9-summary if it repeats the counts. If the editor rules instead that these are not one-excitation absorption channels, the text must say why. As printed, the caption claims "the one section that computes the rate".

### A3. Cells allowed at leading order but computed nowhere (ruling Q1, distinct mark)
I confirm the four proposed cells. In each, the spin density has a non-zero matrix element into the row's final states, and no section computes the rate:
- Core × spin (10.6 only notes that the spin current is a separate row, l.83).
- Superconductors × spin (s15-1: no "spin"; 15.4 spin current is ALP absorption only).
- Migdal × spin (Ch12: no spin coupling anywhere).
- Dirac × spin (s16-1: no "spin").

Add these cells, which meet the same criterion:
- Phonon-assisted × spin. A triplet sideband from a spin vertex plus the e–ph vertex is allowed. s13-3 l.9 says only that "neither vertex flips the spin" for the density case.
- Free recoil × n_e (editor Q3). The rigid-atom following density f_κ(q) of eq:8.6-follow and s11-3 l.150 gives a leading-order vertex at all q. It is allowed, and only the vertex is computed (app:E.17 core share). Mark it, do not leave it blank. Note: the same Z_κ − f_κ(q) vertex covers the dark-photon free-recoil and color-center cells, which WE 9.1 omits (see A5).
- Dopants × spin. s16-5 l.15 notes that the spin density enters unscreened but computes no rate.
- Frenkel × spin. s16-4 l.99: triplet excitons "enter only through the spin couplings of 10.4", with no rate.

**Cross-check against tab:22-gaps:** none of the cells above has a row there. The closest rows are "Triplet beyond independent particles" (10.5) and "Valence deformation above the zone" (11.3, which covers the charge vertex but not an electron-only free-recoil rate). Correction: add one tab:22-gaps row, "Symmetry-allowed atlas cells not computed (tab:9-atlas, ○)", that lists the cells, or add individual rows. Without it, the ○ mark points to nothing in Ch22. Also update l.97 ("these cells are allowed by symmetry ... entered as empty") to name the new mark and the full list.

### A4. Operator and sector columns against 8.1 and 8.6: CHECKED
- Column 1 (O₁ with c₁^(e) = Ṽ; density parts of O₅, O₈, O₁₁), column 3 (O₄, the spin-flip operators, current parts of O₂, O₅, O₈), dark-photon row −j_e + Σ Z_κ j_κ, ALP s_e and J^{αα}_e, scalar n_e − T_e/m_e: all match tab:8-operators and eqs. 8.1-alp and 8.1-scalar. O₂ also carries T_e. The column-3 header omits T and l.21 does not mention it. That is harmless, because the trace term is listed under the ALP/scalar column.
- Sectors (ad, 0, +, ad^s, qp, (2,0)) match eq:8.6-partition, tab:8-sectors, the magnet paragraph (s8-6 l.192) and the superconductor counting (l.202).
- l.81 says 17.4 computes the Migdal–recoil interference. tab:8-sectors cites 12.5 for the zero-phonon block and 12.5 plus 17.4 for the phonon-dressed block. **GAP:** cite 12.5 and 17.4.

### A5. WE 9.1 (dark photon)
- Scattering reduction −V⁻¹Ṽ n_Z, n_Z = −n_e + Σ Z_κ n_κ: matches we:8-darkphoton (c₁^(p) = −c₁^(e)). CHECKED. Absorption at ω_L = 36.35 meV (LO): for m_φ = ω, q → 0 the transverse self-energy gives κ_eff² Im Π ∝ Im(−1/ε), the same as the longitudinal one, so the peak is at the LO pole. CHECKED (also s11-8 l.3). B′ = i p_φ × ê A′, which is v times E′. CHECKED (s14-3 l.16).
- l.114, "two of the last": **WRONG.** The WE itself names 10.9 (pairs) and 17.3 (plasmons *and* optical phonons). These are three cells of the last column (pair, plasmon and single-phonon rows). Correction: "three of the last".
- l.114, "the eleven cells of the vector column": correct as printed. After A2 it becomes 14, since the dark photon reaches all three added cells.
- l.114, "the Migdal row of the nuclear column": **GAP.** l.108 says that in the lattice rows "the electron and nuclear blocks combine into the charge carried by a vibration". The dark photon therefore also populates the nuclear-column cells of single phonons (polar; zero in Si), multiphonons (Z_κ − f_κ), free recoil and color centers. Correction: "the lattice cells and the Migdal row of the nuclear column", or state the convention that a combined charge vertex is booked in the density column.

### A6. Other 9.1 statements
- c_ν "between 2×10⁻⁵ and 3×10⁻⁵ in silicon": the values are 1.95×10⁻⁵ (TA[100], 5.84 km/s) and 3.12×10⁻⁵ (LA[111]). CHECKED (rounding). c_ν v ≈ 3×10⁻⁸, which is "some 10⁻⁸", CHECKED. Free-nucleus absorption needs m_φ = 2M/v², which no halo mass satisfies. CHECKED.
- l.103: "in silicon its lowest-mass channel is the single acoustic phonon (11.1)" for a nucleon-coupled scalar. **GAP.** s11-6 l.48 shows that random-site couplings (spin and isotope disorder) reach the floor 2ω_th/v_max² = 0.28 keV at 1 meV, 21 times below the acoustic edge. For a coupling whose isotopes differ (c_p ≠ c_n), the isotope self response does the same. Correction: "its lowest-mass *coherent* channel", with a pointer to 11.6.

## B. Section 9.2

### B1. Algebra (sympy): all CHECKED
- eq:9.2-mch: the minimum of q²/2(qv − E₀) is at q̄ = 2E₀/v, giving the floor 2E₀/v². Since E_ch ≥ ω_th, every edge is ≥ the floor, with equality only if a state of energy ω_th exists at q = 2ω_th/v.
- Gapless linear: q/2(v − c) increases with q, so q̄ = ω_th/c and m = ω_th/[2c(v − c)]. The ratio to the floor is v²/[4c(v − c)], 21.496 for Si at 9.35 km/s (≈ v/4c = 21.24). Backscatter q̄ = 2m(v − c); the energy fraction given up is 4c(v − c)/v² ≈ 4c/v. CHECKED. Closed for c ≥ v. CHECKED.
- Gapped branch: the Dirac pair edge (v_D²q² + 4Δ_D²)^{1/2} is the minimum over k of E_{k+q} + E_k at k = −q/2, as in eq:7.3-edge. CHECKED.
- Quadratic: the q² term makes q̄ = 2μv, which reproduces E_R^max = 2μ²v²/M. The free-recoil curve meets the floor only at m = M (exact algebra: (m − M)² = 0). CHECKED.
- eq:9.2-halo: d ln m/d ln v = −qv/(qv − E) from the explicit dependence (envelope theorem). Stationarity gives qv = 2E − qE′, so E′ > 0 means E > qv/2 and |exponent| > 2, and E′ < 0 means |exponent| < 2, as stated. Limits: flat −2; linear −v/(v − c) = −1.0119; free nucleus −(m + M)/M → −1. Dirac: the log's numerical derivatives equal the formula (2.1157, 2.6017, 2.7438; isotropic 2.3651), giving the text's −2.12 to −2.74 and −2.37. CHECKED.
- Dimensions: every displayed mass is energy/velocity², with velocity dimensionless (c = 1). eq:9.2-abs is m_φ = ω. CHECKED.

### B2. Numbers against fig9_1.log and home sections
- Floors: Si 0.3329 (printed 0.333), Ge 0.2119, GaAs 0.4328, L 0.5168, Al 0.1025 keV, GaAs LO 10.351 keV, Si optical 18.25 keV (tab:17-endo 18.3), Ge 3d 8.527 and 8.698 MeV (10.6 doublet 29.2/29.8 eV + 0.744), 2/v² = 2.848×10⁵ (5.45 decades). CHECKED.
- New edge Si 2p: q = 38 keV (s10-6 l.3) gives E = 100.7 eV and 2q/v = 28.68 MeV. CHECKED.
- New edge ZrTe₅ floor: 4Δ_D/v² = 6.720 keV with Δ_D = 11.8 meV (s16-1 l.64, CORRECTIONS l.642). CHECKED. The axis minima 7.12/8.99/9.58 keV and the isotropic 8.04 keV with the geometric mean 7.91×10⁻⁴ match s16-1 l.64 and SOTA l.685. CHECKED. v_D/v_max is 0.170–0.415, CHECKED.
- New edge Al acoustic 8.6 keV: **WRONG convention (value survives).** 6.63 km/s is the Voigt *isotropic* LA speed of 20.3 (0 K constants C₁₁ 114.3, C₁₂ 61.9, C₄₄ 31.6 GPa at the room-temperature density 2.70). The acoustic edge (eq:11.1-edge, NOTATION c_LA,max), and the Si/Ge/GaAs entries beside it, use the *fastest direction*. For Al that is [111]: c_L = [(C₁₁ + 2C₁₂ + 4C₄₄)/3ρ]^{1/2} = 6.71 km/s at 2.70 (edge 8.50 keV) or 6.67 km/s at the 0 K density 2.73 (edge 8.56 keV). The Voigt value at 2.73 is 6.59 km/s (8.66 keV). Correction: quote c_LA,max = 6.67 km/s ([111], 0 K constants and 0 K density), which gives an edge of 8.6 keV. Change the Table 9.2 caption, the fig. 9.1 caption ("fastest longitudinal speeds of ... aluminum (6.63)" is false) and fig9_1.py (the Al line and the log row). The ordering in l.69 is unchanged. The "0 K constants 6.63/3.30" of the brief are a hybrid of 0 K constants and room-temperature density; s20-3 l.7 says so itself.
- Offset brackets: Si 0.474 CHECKED (eq. in s3-3 l.205). Ge 0.420 CHECKED against s3-3 l.221, which uses q = 1898 eV. fig9_1.py uses 1900 eV, which gives 0.4206 → "0.421". Change the input to 1898 eV so the log matches the text. GaAs L 0.5605, printed 0.560, matches s13-1 l.97. CHECKED.
- Phonon-assisted onsets: Si 0.3332/0.3374, Ge 0.2119–0.2141, GaAs 0.433–0.436 (13.1), and the Si zero-phonon 0.405–0.408 (13.9; SOTA l.637–638 marks these [CALC] "CLAIMED"). Ch9 quotes the accepted 13.x text, so CHECKED. Drift note (not Ch9's to fix): s13-1 l.77 computes with E_g = 1.17 eV, while 13.8, 10.7 and fig9_1 use E_g(0) = 1.1692 eV. With 1.1692 the onsets would be 0.3330 and 0.3371 MeV and the floor 0.3329. The Si points in fig. 9.1b therefore mix the two gaps. They are consistent at 3 decimals, and the 0.3332 exciton point sits 0.1% above the 1.1692 floor line.
- Ge zero-phonon "≈0.32 MeV, bounds in neither direction": s13-1 l.88, CHECKED. "A phonon can take up the mismatch for 15 meV or less": s13-1 (14.79–14.87 meV TA), CHECKED.
- Free recoil: 4 × 40.9 meV = 0.1636 eV gives 17.47 MeV and q = 92.5 keV (s11-4 l.39, l.93), CHECKED. Ge 21.3 MeV (estimate; s11-4 l.93, s17-1 l.70), CHECKED. Migdal at the floor 0.333 (17.1), CHECKED.
- Opening paragraph, "a free silicon nucleus takes up the gap only from about 45 MeV": 45 MeV is s1-3 l.112 for 1.11 eV. With the 1.17 eV gap that this paragraph uses, it is 46.8 MeV. **Minor:** write "about 47 MeV", or "45 MeV for the room-temperature gap". "Almost eight decades" (7.6) holds either way.
- Absorption: 1.1728 eV (13.8 l.3), ZrTe₅ 23.6 meV (16.1), Al 2Δ (15.4), GaAs 36.35 meV (11.8), 116 µeV/T = g_e μ_B (14.3), Ge 0.89 eV direct (s3-3 l.33), MnF₂ 1.1 meV (14.3), NiO 4.54 meV (14.1). CHECKED.
- Plasmon closed: "phase velocity stays above 9.54×10⁻³, or 3.6 v_max". **Minor:** s10-3 l.98 gives 9.54×10⁻³ (RPA edge) *or* 9.18×10⁻³ (quadratic dispersion with cutoff), "3.5 to 3.6 times". Write "above about 9.2×10⁻³, 3.5 v_max". The III–V value v_D ≈ 1.8 v_max (s7-3 l.30, l.68) is CHECKED.
- NiO: c_M = 1.36×10⁻⁴ gives 7.312 keV (s14-1 l.55; CORRECTIONS l.628, l.647). CHECKED. NOTATION's c_M entry already reads 1.29–1.36×10⁻⁴; only ledgers/SEAMS/14.1.md still says 7.2 keV. "Five times the sound speeds of silicon": 4.4 times the fastest LA. Acceptable.
- Acoustic edges: Si 6.121, Ge 10.19 (5.59 km/s, s17-1 l.70), GaAs 10.3–12.3 (s17-6 l.68), diamond 3.1 (s17-5 l.79), "within 10% only above 44 times the edge" (s11-1 l.129, l.136). CHECKED. Equivalent Si thresholds 1.69/1.31/1.19 meV and Al/Si = 1/59.7: CHECKED.
- Halo: δ ln v = 25/794.5 = 3.147%. Linearized: floor 6.29%, Si acoustic 3.18%, ZrTe₅ 7.44% (all CHECKED); free recoil 1.0005 × 3.147 = 3.15%. **Minor:** l.96 groups "the acoustic edge of silicon and the free-recoil edges by 3.2%"; the free recoil is 3.1%. Exact ±25 km/s floor shifts −6.01/+6.60, annual −3.89/+3.38 (= s1-3 l.65), acoustic −1.98/+1.70: CHECKED. Endothermic 12–28% and 1% match s17-3 l.130, CHECKED.
- WE 9.2: c = 3.1188×10⁻⁵, q̄ = 32.06 eV = 0.0140 (2π/a), with 2π/a = 2.283 keV. m = 6.121 keV; floor 0.2848 keV (ratio 21.5); ½mv² = 21.50 meV; mv = 16.22 eV; c·mv = 0.506 meV; keeps 20.5 meV. [100] TA gives 9.757 keV. At 0.1 and 10 meV: 0.612 and 61.2 keV, and 0.140 (2π/a). The 29% ASR figure matches s5-4 l.152. All CHECKED. WE 9.2's "6.12 keV" is CHECKED.
- Citations: Kahn & Lin Eq. (93) is ω ∼ 2c_s m_χ v; Eq. (94) is the flat optical branch, in Sect. IV.2 (journal IV B). CHECKED. Both attribute and carry nothing (STYLE).

### B3. Statements needing a correction
- **Table 9.2, ZrTe₅ "Pairs without a phonon: 8.0 keV (7.1–9.6 by axis)". GAP.** The caption defines an entry as "the lightest mass that reaches each channel". In the anisotropic crystal that is the minimum over q̂, 7.1 keV (q along the slow axis y). 8.0 keV is the edge of the isotropic geometric-mean cone that 16.1 uses as a proxy for the orientation average. The same applies to the l.69 statement "open at 8.0 keV, the silicon edge at 1.3 meV" (with 7.1 keV it is 1.16 meV). Correction: print 7.1 keV (axis y), with 8.0 keV marked as the isotropic proxy, or redefine the ZrTe₅ entry in the caption.
- **Missing edge class. GAP.** Random-site couplings (11.6: nuclear spin, isotopes) reach the floor (0.28 keV at 1 meV in Si). The two-magnon continuum (14.2) decouples energy from momentum, and the cited Esposito et al. reach is about 1 keV. Neither is placed on the map. Both are flat-onset-like and sit far below the acoustic and magnon edges. Correction: one sentence in "Flat onset" or l.39, and optionally a point in fig. 9.1a.
- l.22, "Two entries of tab:9-atlas are closed this way": the plasmon and the III–V pairs are parts of the cells "electron-gas continua and plasmons" and "Dirac and narrow-gap pairs", whose other parts are open. Write "two channels inside entries of ...". Minor.

### B4. Notation drift (NOTATION.md)
- **Bare `c` for a branch speed** throughout 9.2 (`cq`, `c < v_max`, `(c²q² + E₀²)^{1/2}`, WE 9.2 `c = 9.35/299792`). NOTATION l.516, 772 and 865 reserve bare c for the speed of light ("bare c is the speed of light"). Use c_ν (or c_LA,max) for phonons, c_M for magnons, and a generic symbol such as u for the linear case (fig9_1.py also uses u).
- The display in the "Gapless linear branch" paragraph is labelled `m_{\mathrm{min}}`. NOTATION gives m_min = 2E_th/v_max² (the floor), so this display clashes with that entry. Use m_min^ch, or m_min^ac where it applies.
- New symbols with no NOTATION entry: m_min^ch, E_ch(q), q̄, E₀ (generic onset energy). Add rows "first 9.2". ω_th (l.771) and m_min^ac (l.772) are listed. The text says ω_th is used "wherever the excitation is a phonon or a magnon", but eq:9.2-mch and the floor statements use ω_th for gaps and core shells as well. Either say that 9.2 uses ω_th generically, or write E_th there.
- No sign, π or factor-2 drift found: the half-gap convention (E₀ = 2Δ_D, floor 4Δ_D/v²), 2Δ_BCS, ζ (NOTATION l.86) and v_max = 794.5 km/s all match.

## C. Editor notes concerning these files
- 9.1 Q1: confirmed, with additions (A3), and tab:22-gaps lacks the cells. Q2: GAP (A1, single phonons). Q3: cell allowed, mark ○ (A3). Q4: WRONG gloss (A1). Q5 (float order) and the build overflows are not derivation items.
- 9.2 Q3: the three new edges are recomputed (B2). 2p and ZrTe₅ are CHECKED. The Al value is 8.6 keV only with the fastest-direction speed at the 0 K density; fix the speed and wording. Q2: the tex has 7.3 keV and NOTATION already agrees; only SEAMS/14.1.md still has 7.2. Q1: the s16-1 l.15 value of 31 meV was not checked here (light pass, LE-186).
- Campaign numbers: 0.3332/0.3374/0.405–0.408 (SOTA "CLAIMED", [CALC]), ZrTe₅ 8.0/7.1/9.0/9.6 (SOTA l.685) and NiO 7.31 (CORRECTIONS l.647) all agree. app:E.14 already carries the DC-2 caveat (HSE06+SOC fails for Ge), so the l.26 pointer is safe. No DC-RESULTS row is quoted.
