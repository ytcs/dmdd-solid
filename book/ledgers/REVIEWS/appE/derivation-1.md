# App E derivation check, part 1 (E.1–E.6), isolated verifier
Scope: tex/appE/E-1.tex … E-6.tex against NOTATION, STYLE, App. A.6 and the cited sources (25 arXiv texts fetched with lit.py into
sources/review-appE/; PDFs deleted afterwards). Algebra was re-derived in sympy and the numbers recomputed in numpy; the key formulas and values are given inline.
Representative-calculation numbers (E.1–E.3: gaps, masses, ε∞ grid scan, pressures, f-sum ratios) are, per the editor notes, checked
for internal consistency only. Verdicts: WRONG = must change; GAP = missing or unsupported step; CHECKED = verified.

## Summary of actions (WRONG / GAP first)
1. E.1 l.20 WRONG (source): Garza–Scuseria HSE MAE. Correction below.
2. E.2 l.42 WRONG (source): PseudoDojo Δ average is not 1.4 meV.
3. E.4 l.70 WRONG (source): Poncé 2018 rescales the screening to 11.94, not to the book's 11.7.
4. E.5 l.90 WRONG (cost): 10¹⁶ op at 10¹³ op/s is about 17 min, not "hours".
5. E.1 l.54, E.2 l.31, E.2 l.104 WRONG (rounding): 270.3 bohr³; 1.88 Å; v_max = 2.65×10⁻³.
6. E.4 l.85 GAP: the frozen-phonon and DFPT cost laws use inconsistent powers of N_at (inherited from the source).
7. E.5 l.90 GAP: the window count omits the split-off band, and the per-pair cost omits the R_p stage.
8. E.3 tab:E-gw GAP: the source has Si core-polarization values; "--" implies that none exist.
9. NOTATION drift: v_C italic (E.1, E.3); n_B/n_T italic versus upright; n_at versus N_at; N_f clash; bare η.

## E.1 Density-functional theory in practice
- l.20 WRONG. Garza 2016 Table I and text give HSE MAE = 0.37 eV on the **27**-compound common subset and 0.38 eV on all **41**
  compounds; the gaps are a mix of low- and room-temperature values. Only the 0.18 eV figure (group 1 of SC40, typical semiconductors)
  refers to low-temperature gaps. The sentence also says "40 semiconductors and insulators" twice. Fix: "Against measured gaps of 41
  semiconductors and insulators, HSE has a mean absolute error of 0.38 eV, falling to 0.18 eV for the typical semiconductors of the
  set, whose gaps are measured at low temperature [Table I and text]."
- l.54 WRONG (minor). Ω = 40.048 Å³ = 270.26 bohr³, so write "270.3" (270.2 is a truncation). N_PW = 2121.05 is unaffected.
- l.106 CHECKED with a convention note. δ𝓃_out = R⁰v_C δ𝓃_in, so the error operator on densities is 1 − R⁰v_C, the transpose of
  ε = 1 − v_C R⁰. The eigenvalues are the same, so Eq. E.1-mixing and the bound β < 2/max ε_λ stand. Suggest "the output error is
  (1 − ε^T)δ𝓃_in, with ε^T = 1 − R⁰v_C the same matrix acting on densities", or a footnote.
- l.106, 111 NOTATION: write v_C as v_{\mathrm{C}} (editor ruling: upright C book-wide; E.4 and E.6 already comply).
- l.14 NOTATION: $n_B = 0$, $n_T = 0$ have italic subscripts, while E.4 and E.6 write n_{\mathrm{B}}, n_{\mathrm{A}}. Pick one form for the
  𝔗 components across App. E (STYLE: upright label subscripts).
- l.122 NOTATION: n_{\mathrm{at}} (E.1, E.3) against N_{\mathrm{at}} (E.4) for the number of atoms per cell. Neither is in NOTATION; unify
  and add a row.
- Eq. E.1-density CHECKED. With ∫_Ω|u|² = 1 (the plane-wave form, Σ|c|² = 1), ∫_Ω𝓃 = 2·(occupied bands) = 8 for Si.
- Eq. E.1-npw CHECKED: (4π/3)k³Ω/(2π)³ = Ωk³/6π², dimensionless. 60 Ry gives 2121.05; the density has 8× as many, 16 968 ≈ 1.7×10⁴;
  |m_i| ≤ 17.89 for |a_i| = a/√2 = 7.257 bohr, so ≥ 37 points and a 40³ grid; 60 Ry = 816.3 eV; density cutoff 240 Ry = 4 × 60.
- l.20 lattice trends CHECKED against Csonka Table II (measured 5.416/5.640/5.638 with ZPAE removed). LDA −0.24/−0.30/−0.59 %, so
  "0.2 to 0.6" holds. PBE +0.92/+2.11/+1.92 %, so "0.9 to 2.1" holds. HSE Si +0.646 % is printed as "0.6 percent" (correct, since
  0.646 %, so 0.6 is correct rounding). Gap 1.22 − 1.17 = 0.05. Ge HSE 0.54 against 0.74 is 0.20 too small.
- l.20 Lejaeghere 2014 Table IV: V₀ +3.6 % (VASP-PBE, elemental crystals) CHECKED; 1.036^{1/3} − 1 = 1.19 %, so "about 1.2 %".
- tab:E-functionals CHECKED, every entry. LDA and PBE a are from Csonka Table II (5.403/5.466, 5.623/5.759, 5.605/5.746). HSE a, the
  LDA (LSDA) gaps, the HSE gaps and the LT measured gaps are from Lucero Table I (5.451/5.706/5.711; 0.51/0.00/0.43; 1.22/0.54/1.18;
  1.17/0.74/1.52), "at the relaxed geometries". Note: Lucero's LSDA gaps are at Lucero's own LSDA lattice constants, not at Csonka's
  LDA values, so the caption's "each functional's own relaxed lattice constant" is correct only per source.
- l.39 hybrid cost CHECKED: n_kN_occ = 512×4 = 2048 ≈ 2×10³. Coarse k′ grid gives 10–10³ times; HSE range 1/ω ≈ 4.8 Å ("a few Å").
- tab:E-cutoff and the l.56 prose CHECKED for consistency: 1 meV at 50 Ry (0.71); 0.14 at 60 ("about 0.1"); Ge 0.22 at 80; 2.88 eV at
  30 Ry; Si P within 23.4–23.7 (0.3 kbar); Ge P negative at 30 Ry; 24 and 38 kbar. E.2 l.48's "8 meV at 30 Ry" matches 8.36.
- l.83 k sampling CHECKED: Γ-centered 12³ under the 48 operations of O_h gives **72** irreducible points (computed by orbit count).
  1.6 + 0.3 + 0.06 ≈ 2 meV matches l.163's "8³ … 2 meV per atom".
- l.85 ε∞ scan CHECKED for consistency. 14.36/13.20 = +8.8 % ("nine percent too high", l.163). ε at PBE a > ε at measured a,
  consistent with the direct gaps shrinking on expansion.
- Eq. E.1-sommerfeld CHECKED (sympy). With g = 2Ω𝒩_F per cell: E − E₀ = (π²/6)gσ² = (π²/3)Ω𝒩_Fσ²; S = (π²/3)gσ = (2π²/3)Ω𝒩_Fσ
  (∫ −[f ln f + (1−f)ln(1−f)] = π²/3 = 3.2899, numeric); F = E₀ − (π²/3)Ω𝒩_Fσ². Units eV³·eV⁻³… → eV. Numerically, with a
  sloped DOS and μ adjusted, FD gives E and F coefficients ±1.645 = ±π²/6 per unit DOS. ½(E+F) = O(σ⁴) and forces = ∂F CHECKED.
- Eq. E.1-cold CHECKED against Marzari–Vanderbilt 1999 Eq. (1), with x = (μ−ε)/σ: δ̃ = π^{−1/2}e^{−(x−1/√2)²}(2−√2x). Numeric: ∫δ̃ = 1,
  zero first and second moments, occupations in [0, 1.083] ("never negative, can exceed one"). E − E₀ and F − E₀ are both O(σ³)
  (computed 0.0035σ, −0.0018σ per σ²). MV text: "zero first and second moments, so that the free energy does not have any quadratic
  dependence … neither do its derivatives".
- l.111 CHECKED: |1−βε_λ| < 1 ⇒ β < 2/max ε; TF max ε ≈ (k_TF L/2π)² ⇒ β ≲ 2(2π/k_TF L)²; Kerker β G²/(G²+k_TF²) cancels the 1/G².
- Eq. E.1-cost CHECKED: the scaling (N_b, N_PW, N_proj ∝ n_at gives n_at³) and (4/3)^{3/2} = 1.54. SOC: 2 × 2² = 8 on the
  N_b²N_PW term (the first two terms get ×4; not stated, acceptable).
- Eq. E.1-fd CHECKED (sympy series): second difference = ε″ + h²ε⁗/12 + O(h⁴); worst-case noise (1+2+1)δε/h² = 4δε/h².
- we:E-si-bands CHECKED for consistency: 5.477/5.431 = +0.847 %; 1 − 0.602/1.17 = 48.5 % ("49 %"); 0.602 − 0.557 = 0.045;
  0.955/0.92 = +3.8 % ("4 %"); Hensel m_l = 0.916 ≈ 0.92. The sign of the gap shift with expansion agrees with Si's negative
  dE_g/dP (estimate ≈ +35 meV for ΔlnV = 2.5 %; the 45 meV includes the 40 versus 60 Ry difference, acceptable).
- l.157 CHECKED: Δ_SO 0.29 (Ge) and 0.044 (Si); Lucero L gap 0.74. The Ge PBE Γ/L values (0.047/0.191) are representative-calc, consistent.
- l.159 CHECKED: 13.04/11.7 = +11.5 % ("11 percent"). Si numbers agree across sections: ε∞ 11.7, gap 1.17 (Ramanathan Eq. (11):
  E_g(0) = 1.1692 eV), PBE 13.04 (E.1, E.3 l.15, E.4 l.164).

## E.2 Pseudopotentials and all-electron reconstruction
- l.42 WRONG (source). van Setten 2018 gives 1.4 meV as "the average delta of the NCPP tables w.r.t. Wien2k" (excluding old FHI;
  footnote 7). This is the prior norm-conserving tables, not PseudoDojo. PseudoDojo's own mean Δ is **0.70 (standard) and 0.64 meV
  (stringent)**, excluding Cr, Mn, Fe. Fix: "the norm-conserving PseudoDojo tables reach a mean of about 0.7 meV per atom (excluding
  the magnetic Cr, Mn and Fe), against 1.4 meV for earlier norm-conserving tables". The 0.3–0.5 meV for AE codes is CHECKED.
- l.31 WRONG (minor): 3.56 bohr = 1.884 Å, so "1.88 Å", not 1.89. 2.40 bohr = 1.270 Å CHECKED.
- l.31 GAP (source). SG15 r_c, q_opt, projector counts and the "no NLCC" flag are not in Schlipf–Gygi 2015, which does not tabulate
  per-element parameters. They live in the UPF file headers, and the fetch failed here (DNS). Cite the SG15 v1.x UPF files explicitly,
  or state "from the input parameters distributed with the file" (the text half-says this). Arithmetic CHECKED: 5.11² = 26.1 Ry,
  3.50² = 12.25 Ry, 6.36² = 40.4 Ry.
- l.104 WRONG (minor): use v_max = 2.65×10⁻³ (Sect. 1.2: 794.5 km/s = 2.650×10⁻³). 2×10 MeV×2.6×10⁻³ = 52 keV, while 2.65 gives 53
  keV as printed and matches E.6 l.81 "5.3 keV per MeV".
- l.3, 18 GAP (wording). The Si 2p binding is ≈ 100 eV (Griffin Fig. 1: −116 eV from the VBM; 2s −170; 1s −1.9 keV). "Bound by more
  than 100 eV" is fine against Griffin; "hundreds of eV below the gap" overstates for 2p. Suggest "more than a hundred eV".
- l.3 CHECKED: a₀/14 = 0.0378 Å; 42² = 1764 Ry ≈ 1800; N_PW = 3.38×10⁵ ("3×10⁵"); 3.38×10⁵/2121 = 159 ("160").
- l.18 CHECKED: Ge 3d at −28 eV from the VBM (Griffin Fig. 1). 14 valence electrons give 7 occupied bands per atom (2 for 4 electrons).
- Eq. E.2-KB CHECKED (standard form). p̃ is shared with PAW; the editor accepts this.
- Eq. E.2-residual CHECKED against Hamann 2013 Eqs. (1)–(2): E^r = ∫_{q_c}^∞ q⁴|φ(q)|²dq, φ(q) = 4π∫j_l(qr)φ(r)r²dr. The units
  are Å⁻² (kinetic energy up to 1/2m and (2π)⁻³), as the text says ("up to a constant").
- l.42 CHECKED against Hamann Table I: Si LDA AE/OV 10.21/10.21 bohr, B 97.11/95.80 GPa (1.35 %, "1.3 %"). All of Hamann's
  calculations are LDA. The PBE-potential-in-LDA remark is verbatim in substance.
- Eq. E.2-delta CHECKED against Lejaeghere: the Eq. (15) number and the ±6 % window (0.94–1.06 V₀) are confirmed; output meV/atom.
- l.35 CHECKED: PseudoDojo scanned ghosts up to ~200 eV; Table 8 heavy elements at 20–80 eV; higher ghosts "unavoidable".
- Eq. E.2-PAW, E.2-rhoPAW, E.2-onecentre CHECKED. e^{iq·r} = e^{iq·τ}e^{iq·x}. The Bloch phases e^{−i(k+q)·R}e^{iq·R}e^{ik·R} cancel,
  so all cells contribute equally. The Rayleigh expansion has correct signs. The zeroth order vanishes for (generalized) norm
  conservation.
- l.79 CHECKED: 2k_cut at 60 Ry = 2√60 bohr⁻¹ × 3.729 keV = 57.8 keV ("58").
- l.81 CHECKED against Griffin Sect. 2.1: PAW (VASP), 1 keV, 10³ k, AE to 2 keV. 1 keV = 73.5 Ry; 2 keV = 147 Ry; √(2m_e·2 keV) =
  45.2 keV (Griffin rounds to "≃50"; the book's 45 is exact). The rate excess above ω ≈ 15 eV is CHECKED. The Ge 3d dominance for
  heavy mediators is CHECKED (Fig. 8). "2p and below (Si), 3d and below (Ge)" as core is CHECKED (Sect. 2.2).
- Eq. E.2-dc CHECKED (sympy): Σ(ε_m−ε_n)|⟨m|e^{iqr}|n⟩|² = ⟨n|e^{−iqr}He^{iqr} − H|n⟩. Symmetrizing removes the q·⟨p⟩/m term;
  [(p+q)² + (p−q)² − 2p²]/2 = q², so the kinetic part is q²/2m_e. Units eV both sides.
- Eq. E.2-fsumNL CHECKED: δ_NL is even in q (symmetrized) and so O(q²). The conjugated projectors e^{−iq·r}p̃ are right.
- l.98 CHECKED for consistency (representative): monotone 0.81 → 0.88 with bands.
- l.100 CHECKED: v = i[H,r] = p/m + i[V_NL,r]. Ismail-Beigi Eq. (5): H_A = Π²/2m + U + W(r,Π) + φ(r,t), with the scalar potential
  entering by multiplication (Eq. (5) is the right number).
- l.104 CHECKED: 1/r_c = 1.55 and 1.05 keV ("1.6", "1.0"); q_opt = 19.05 and 13.05 keV; αm_e = 3.73 keV.

## E.3 Quasiparticle corrections
- tab:E-gw GAP. Aryasetiawan Table II (Shirley–Zhu–Louie) also lists Si, Γ8v→0.85X5c: 1.29 (core in LDA) and 1.16 (CPP), and GaAs
  Γ8v→X6c: 1.02/1.42. The "--" entries for Si suggest that no value exists. Either fill Si (1.29 / 1.16, exp 1.17) or say "Ge only shown".
- tab:E-gw values CHECKED against Aryasetiawan Table I: Si LDA 0.52, GW 1.29/1.24/1.25, exp 1.17; Ge <0, 0.75/0.65, 0.744;
  GaAs 0.67, 1.58/1.32/1.22, 1.52. Table II: Ge Γ 0.53/0.85 and L 0.58/0.73 (exp 0.89/0.744). The prose (overshoot 0.07–0.12, scatter
  0.10 and 0.36, both CPP gaps within 0.04) is CHECKED. Footnotes a/b/c/e = Hybertsen–Louie / Godby / Rohlfing / Zhu–Louie
  match the caption: Si a, b, c; Ge a, c; GaAs b, c, e. CHECKED.
- l.3, 28, 32, 82 NOTATION: v_C must be v_{\mathrm{C}} (eight occurrences in E.3).
- l.11 CHECKED: 1.170 − 0.602 = 0.568 and 1.170 − 0.557 = 0.613. Scissor accuracy 0.1/0.2/0.4 eV (Si/GaAs/diamond, Godby) and the Si
  "fortuitous" cancellation are verbatim in Aryasetiawan Sect. V B. Godby 1988 itself was not fetched (not on arXiv).
- l.13 CHECKED: scissor velocity factor; f-sum excess Δ_scis Σ_c|ρ_cv|².
- l.15 CHECKED (sign): raising every denominator at fixed |ρ|² lowers ε∞ − 1.
- l.17 CHECKED against van Schilfgaarde 2006: ZPR ~0.3 eV in diamond and ≲0.1 eV in heavier compounds (verbatim).
- l.30 CHECKED against Aryasetiawan Eqs. (83)–(86): the GPP form, and the f-sum −(π/2)ω_p²[(q+G)·(q+G′)/|q+G|²]𝓃(G−G′)/𝓃(0), sign
  and factor included. No adjustable parameters. ω_p = 16.60 eV for 8 e⁻ in 40.05 Å³ (ω_p² = e²𝓃_e/m_e, HL; NOTATION) CHECKED.
- Eq. E.3-M CHECKED: it is the density vertex at q+G in the periodic gauge. Deslippe Eqs. (7), (8), (12) give W = ε⁻¹v(q+G′), matching l.28.
- Eq. E.3-qp CHECKED against Aryasetiawan Eqs. (57)–(58). z_qp = 0.7–0.8 (Sect. V B, Hybertsen–Louie); Z < 1 reduces the correction;
  COHSEX overestimates. Units eV.
- l.61 CHECKED against van Schilfgaarde: one-shot GW underestimates when cores are treated adequately; it can fail in TM compounds;
  QSGW Γ–Γ +0.2 eV, others +0.1 eV, ε∞ slightly low, attributed to the RPA omitting e–h correlation.
- l.65 CHECKED: E = ε + z(ReΔΣ + i ImΣ), so |⟨ψ|ψ(t)⟩|² ∝ e^{−2z|ImΣ|t} and the rate is 2z|ImΣ| (ħ = 1). The impact threshold is E − E_c ≥ E_g.
- l.67 CHECKED: the plasmon pole gives no lifetimes (Aryasetiawan Sect. III C).
- Eq. E.3-vrescale CHECKED: r_mn = −iv_mn/(ε_m−ε_n). The optical limit q·v_mn/(ε_m−ε_n) is invariant under the rescaling (NOTATION
  row ρ_mn).
- l.78 CHECKED against van Schilfgaarde Fig. 2: GaAs QSGW 1.77 eV and 0.077 m₀, against 1.52 eV and 0.065 m₀.
- l.82 CHECKED: N_G(10 Ry) = 144.3 and N_G(15 Ry) = 265.1. Deslippe Sect. 4: "highest empty state … at least the dielectric energy
  cutoff"; the slow Coulomb-hole convergence relative to the polarizability (Fig. 8).
- l.84 CHECKED against Deslippe Sect. 4: matrix elements N³logN; χ N⁴; Σ per pair N³, with ×N for a window. The book's
  "n_at³ log n_at" for all pairs agrees with BerkeleyGW's epsilon stage.
- we:E-si-gap CHECKED: the j = 3/2 quartet at +Δ/3 and the doublet at −2Δ/3; 4(Δ/3) − 2(2Δ/3) = 0; the gap closes by Δ/3 = 14.7 meV (Si)
  and 97 meV (Ge). This matches l.92 "0.1 eV". The three corrections agree to ~0.1 eV (1.17, 1.22, 1.24–1.29 − 0.015 − ZPR).

## E.4 DFPT in practice
- l.70 WRONG (source). Poncé 2018 gives ε_DFT = 12.89 against a measured **11.94** and modifies the screening to that value. The book's
  "rescales … to it", after "the measured 11.7", implies 11.7. Keep 11.7 as the book value (editor ruling) and fix: "Ref. [ponce]
  rescales the screening of the electron–phonon vertex to the measured dielectric constant (11.94 in that work)". Alternatively, drop
  the target value.
- l.85 GAP. The supercell holds N_at R³ atoms, so the cost is (N_at R³)³ × 3N_at = 3N_at⁴R⁹ against DFPT 3N_at⁴R³. The text pairs
  "3N_at R⁹" with "3N_at⁴R³". Baroni Sect. IV.B has the same "3N_at × R⁹" (it takes N_at^SC ~ R³ and drops N_at³), so the book inherits
  an inconsistent comparison. Fix: "3N_at⁴R⁹_IFC … against 3N_at⁴R³_IFC: a factor R⁶ in favor of DFPT".
- l.160 GAP (minor). Noffsinger 2012 says "plane-wave pseudopotential approach", LDA, 35 Ry, 14³, 6³ Q; it does not say
  "norm-conserving". Drop the word, or cite the EPW setup for it. The other settings are CHECKED.
- Eq. E.4-sth, E.4-dV CHECKED against Baroni Eq. (30) and Giustino Eqs. (48)–(49). a_sh larger than the valence bandwidth suffices
  for positivity (ε_min + a_sh − ε_v > 0).
- l.20 CHECKED: 2n+1 theorem with n = 1 gives third order; D^dyn needs only ∂𝓃.
- Eq. E.4-rcomm CHECKED (Baroni Eq. (37)). [p²/2m, r] = −ip/m. Baroni Eq. (44) is the r-Sternheimer equation.
- Eq. E.4-epsZ CHECKED (HL: D = ℰ + P; Baroni Eqs. (94)–(96) with 4π). eZ* = Ω∂P/∂u = ∂F/∂ℰ, both of charge dimension.
- Eq. E.4-na CHECKED against Baroni Eq. (98): 4πe²_G → e²_HL; 1/√(MM′) from Eq. A.6-Ddyn. Units eV², as for D^dyn.
- Eq. E.4-LOTO CHECKED (sympy): e₁ = √(M₂/M), e₂ = −√(M₁/M), Σ|e|² = 1, (e₁/√M₁ − e₂/√M₂)² = 1/μ_red. Units eV². Relative rate error
  2δZ*/|Z−Z*| CHECKED.
- Eq. E.4-berry CHECKED against Marzari 2012 Eq. (90) (spinless; g_deg = 2 added). Wannier-center form; quantum e g_deg R/Ω.
- Eq. E.4-kk CHECKED: ε₁(0) − 1 = (2/π)∫ε₂/ω′; a downshift at fixed weight raises it.
- l.70 CHECKED: 12.89 (Poncé). 12.89/11.7 = +10.2 % ("about 10 %", l.164). 13.04/12.89 = +1.2 % ("within about one percent").
- Eq. E.4-ifc CHECKED: the exact inverse of Eq. A.6-Ddyn (√MM′/N_Q³, e^{−iQ·R}). ⟨110⟩ long range CHECKED (Baroni Sect. V.A).
- Eq. E.4-B CHECKED from Eq. A.6-u and ⟨BB⟩ = 2n+1. Units eV⁻² = Å².
- Eq. E.4-dBgamma CHECKED (sympy, both limits): Ω/(2π²)∫Q²dQ (1/3)Σ(2n+1)/(2M c Q) → ΩQ_c²Σc⁻¹/(24π²M) and ΩQ_cTΣc⁻²/(6π²M).
  Scaling N_Q⁻² and N_Q⁻¹. Numbers: Q_c = 0.1424 Å⁻¹; ΔB(300 K) = 3.56×10⁻⁴ Å²; ΔB(0) = 1.94×10⁻⁵ Å² (ratio 18.4, "twenty");
  cQ_c = 65.3 K.
- l.111 CHECKED: 6 × 10⁵ × 16 B = 9.6 MB.
- l.147 CHECKED: ρc_LA² = C₁₁ and ρc_TA² = C₄₄ along [100]; relaxed ≤ clamped.
- l.155 CHECKED against Baroni Sect. V.A: GGA lowers positive-Grüneisen branches; Si is the exception where GGA slightly worsens LDA.
- l.157 CHECKED: the 8³ fcc grid has **29** irreducible Q (orbit count); 29×6 + 3 = 177 ≤ "about 180".
- we:E-dfpt-si CHECKED against Poncé: 35 Ry PBE, 45 Ry LDA, 6³ Q, 18³ k for vanishing Born charges. 35 Ry = 476.2 eV; |G| = 22.06 keV;
  |G₁₁₁| = 3.954 keV; ratio 5.58.
- l.162 CHECKED: inversion, the tetrahedral site and neutrality give Z* = 0.
- Eq. E.4-dpsi, E.4-dpsic, E.4-dpsiperp, E.4-sthw CHECKED for sign and definiteness. The occupied–occupied cancellation in 𝓃 is
  right (antisymmetric denominators).
- l.3/164 CHECKED: 15.5 THz Γ optic (Nilsson 1972, not fetched; standard 15.53 THz).

## E.5 Wannier functions in practice
- l.90 WRONG (cost). 2×10¹³ op per q × several hundred targets ≈ 10¹⁶ op, and at 10¹³ op/s that is **10³ s ≈ 17 min**, not
  "hours". At 5×10¹⁰ op/s it is 2×10⁵ s = 2.3 days (CHECKED). Fix: "a quarter of an hour … days", or state an efficiency factor.
- l.90 GAP (count). Three valence bands lie within 0.1 eV of the VBM with or without SOC: the triply degenerate VBM without SOC;
  heavy hole, light hole and split-off (44 meV) with SOC. "The two upper valence bands" undercounts by 3/2 (≈3×10⁷ pairs), and it is
  inconsistent with the one-valence-band count of we:E-counts. State the band choice.
- l.90 GAP (cost). The per-pair figure 4×216×26×6 counts only the R_e sum, which assumes the R_p sum is already done for that Q. Each
  pair has its own Q = k′−k−q, so the R_p stage (216²×N_W×6 per Q and external band) runs once per distinct Q of the pocket-difference
  set. It is subdominant for ≲10⁵ distinct Q (≈10¹² op per q) but should be stated.
- l.67, 90 NOTATION clash: N_f (fine-grid points per direction) against the NOTATION row N_f, "number of final states (2.1)". Rename
  it (e.g. N_{\mathrm{fine}}) and add a row.
- l.3, 54–56 CHECKED: 40³ = 64 000; 64 000² = 4.10×10⁹; N_W²×6 = 4056; 1.66×10¹³ numbers = 266 TB ("270"); one Q = 4.15 GB.
- l.58 CHECKED: 216²×676×6 = 1.89×10⁸, 3.03 GB.
- l.60 CHECKED: 216×676×6 = 8.76×10⁵; × 4.10×10⁹ = 3.59×10¹⁵ MAC ≈ 2.9×10¹⁶ flop; /48 = 6×10¹⁴. Stage 1 (1.9×10⁸ × 64 000 =
  1.2×10¹³) is smaller, as stated.
- l.62 CHECKED: V_BZ = 6.194 Å⁻³; k_δ(0.5, 0.3 eV) = 0.198 Å⁻¹ gives 5.28×10⁻³; (0.32) 2.70×10⁻³, ×6 = 1.62×10⁻². 338 and 1039 points;
  3.5×10⁵ pairs; 1.2×10⁴ reduction ("four orders"). The 0.32 m_e is the per-valley DOS mass (0.92·0.19²)^{1/3}; this is worth stating.
- l.90 CHECKED (other numbers): 3^{3/2} = 5.20; 120³ grid: 1757 valence and 5397 conduction points; 2×1757×5397 = 1.9×10⁷; per pair
  1.35×10⁵ MAC ≈ 1.1×10⁶ flop; δ³ and N_f⁶ scaling.
- Eq. E.5-ginterp CHECKED against Giustino Eqs. (177)–(179) and A.6 normalization (1/√(2M_κω)).
- Eq. E.5-gL CHECKED against Giustino Eq. (180): (4π/Ω)(e²/4πε₀) → e²_HL/Ω, with 1/√N_p absorbed into the A.6 normalization; G ≠ −Q.
  Units: e²/(Ω Q √(Mω)) = eV.
- l.24 CHECKED against Noffsinger: 34 bands, 26 WFs, −10/+30 eV. l.26: Poncé 12³ k for the conduction minimum at ≈0.85 ΓX; 6³ Q.
- l.30 CHECKED against Giustino Sect. VI.A.2 (decay at least as R_p⁻³) and Fig. 6 (diamond 4³/6³/8³, highest optical branch).
- l.41 CHECKED against Brunin 2020: denser grids localize but do not reduce the spurious oscillations; mobility error ≈10 % in Si and
  32 % in GaAs ("about 30 %"; GaP 28 %).
- l.47 CHECKED: bond √3a/4 = 2.352 Å; 1 keV × 2.35 Å = 1.19.
- l.69 CHECKED against Poncé 2016 Sect./Fig. 12 (Pb): 14³ k, 10³ q, 0.025 Ry, 6³ coarse, 400 000 Sobol k and 27 000 random q.
- l.73–75 CHECKED against Noffsinger: 14 meV with 40³; 30 meV with 24³; Γ = 100 meV; shift 0.15–0.23 eV; GW accuracy ~0.1 eV;
  e–ph renormalization 0.05–0.1 eV over 0–400 K.

## E.6 Dielectric response from first principles
- l.36 note: "At T = 0" before the f-sum is unnecessary (editor ruling: the rule holds at any T). The statement itself is CHECKED.
- l.38, 14 NOTATION: bare η (broadening, Eq. E.6-R0; also E.4 l.143) clashes with NOTATION entries 39/52, which reserve η for η(v_min)
  and η_anh. Use 0⁺/η_{\mathrm{b}}, or add a row.
- Eq. E.6-R0 CHECKED (Adler–Wiser sign; ⟨n|e^{−i(q+G)r}|m⟩ = ρ_mn(q+G)*). Units: (eV³/1)/eV = eV², so v_C R⁰ is dimensionless.
- Eq. E.6-dyson, ε⁻¹ = 1 + v_C R, E.6-L CHECKED. With f_xc = 0 the result reduces to RPA. Umklapp q = q_r + G_q.
- l.3 CHECKED: ω_p = (4πα𝓃_e/m_e)^{1/2} = 16.60 eV (NOTATION ω_p² = e²𝓃_e/m_e).
- l.32, 81 CHECKED: k_cut(500 eV) = 22.6 keV (Knapen: "≲22 keV").
- l.36 CHECKED: the free-electron count for 70 bands gives k = 4.695 Å⁻¹ and k²/2m = 84.0 eV. 84 − 12 ≈ 70 eV above the VBM matches
  Knapen's "does not capture … ω > ~70 eV".
- l.40 CHECKED: ∫ω ε₂^KS(ω−Δ) = (π/2)ω_p² + Δ∫ε₂; the unrescaled-velocity factor is [(ω−Δ)/ω]².
- l.46, 86 CHECKED against Albrecht 1998: local fields shift the strength up and lower E₁ and E₂, which is worse; BSE restores the line
  shape and intensity. Knapen: the difference with and without local fields in the rate is small.
- l.48 CHECKED against Reining 2002: TDLDA ≈ RPA+LF for absorption; EELS satisfactory because RPA+LF already is;
  f_xc = −α/(4π|r−r′|) ↔ −α/|q+G|² (FT of 1/4πr is 1/q²); α = 0.2 with GW-shifted χ⁰.
- l.54 CHECKED: 30 keV / 3.954 keV = 7.6 ("more than seven").
- Eq. E.6-Hexc CHECKED: (ε_c−ε_v) + 2K^x − K^d for singlets, TDA; K^x without G = 0.
- l.66–68 CHECKED against Albrecht: NC, 15 Ry, up to 2048 k; 864-k tests; 4v+2c sufficient below 4.5 eV; diagonal ε⁻¹ indistinguishable;
  phase sensitivity and abelian subgroup; k points (not cutoff) the bottleneck; 3.8 eV structure slightly overestimated.
  2048×4×2 = 16 384; 16 384³ = 4.4×10¹² ("~10¹³").
- l.70 CHECKED (sympy): μ_x = 2ε²E_b/α² = ε²E_b/Ry = 0.106 m_e; a_x = εa₀m_e/μ_x = 60.0 Å; 1/a_x = 0.0167 Å⁻¹; |b| = 2.004 Å⁻¹;
  ratio 120, so ~1.7×10⁶ points. (E_b ~10 meV is a round number; the measured Si value is 14.7 meV. This is acceptable as an estimate.)
- l.74 CHECKED against Blase 2020: average error 0.2 eV on the Thiel set (~200 singlets); O(N_orb⁴) with RI; reaction field. The
  "0.1–0.3 eV typical" and "few tenths for GW" claims are consistent with the source text.
- we:E-elf-si CHECKED against Knapen Sect. III: 500 eV, Γ-centered 8³ (Si), 70 bands per spin, TB09 + scissor to the T = 0 gap, RPA with
  LF at all q, angular average Eq. (24). |b|/8 = 0.2505 Å⁻¹ = 0.494 keV; (π/2)ω_p² = 432.7 eV² ("433").

## Editor-notes items for E.1–E.6 (SEAMS/E.1-E.3.md, item 3: cross-chapter values)
- Ω = 40.05 Å³: matches Sect. 3.1 (s3-1 l.47). LDA Si a: 3.1 quotes 5.401 Å (Poncé), tab:E-functionals 5.403 Å (Csonka); the two agree
  within rounding, from different sources. ω_p = 16.6 eV and measured ε∞ = 11.7: match Sect. 4.3 (s4-3 l.87, 89). E_g(0) = 1.17
  (1.1692): matches Sect. 1.3. Δ_SO 0.044/0.29 and k_c ≈ 0.85 (3.3) and ε∞ in 4.4: those chapter sections are not yet written, so
  re-check them then.
- Accepted per the editor notes: representative-calculation numbers uncited; LDA Si gap 0.51 (tab:E-functionals) against 0.52
  (tab:E-gw); p̃ shared by KB and PAW; 𝔗 as \mathfrak{T}; Si ε∞ = 11.7 book-wide (E.4 complies, except the Poncé target, see E.4 l.70).
- SEAMS E.1–E.3 "HSE gap MAE 0.37 eV" and "NC tables 1.4" inherit the E.1 l.20 and E.2 l.42 errors; update the SEAM with the fixes.

## Not verifiable from open sources (one line each)
Godby 1988 (via Aryasetiawan only); Shirley 1992 (via Aryasetiawan Table II); Hensel 1965 (m_l = 0.916, standard); Nilsson 1972
(15.53 THz, standard); Kleinman–Bylander, Hamann 1979, Louie 1982, Vanderbilt 1990, Blöchl 1994, Kresse–Joubert, Kerker, Johnson,
Payne, Monkhorst–Pack, Methfessel–Paxton, Ceperley–Alder, Perdew–Zunger, PBE, HSE, Adler, Wiser, Hedin, Hybertsen–Louie, Souza,
Verdi (cited for standard content only; statements consistent with textbook forms); SG15 UPF parameters (see the E.2 l.31 GAP).
