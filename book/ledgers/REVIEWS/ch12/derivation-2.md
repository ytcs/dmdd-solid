# Ch12 batch review, part 2: derivation check (12.4–12.6, D.34)

Reviewer: derivation verifier (long-form-writing SKILL §5), isolated. Date 2026-11-02.
Files: tex/ch12/ch12.tex, s12-4.tex, s12-5.tex, s12-6.tex, tex/appD/D-34.tex. Read with NOTATION.md and STYLE.md.
How it was checked:
- Sympy and mpmath, in scratchpad ch12d2.py. It checks the operator identities on test functions, the angle averages and series, the sum-rule limits, R_rel and every number listed below.
- Cached logs and npz: osc12_4, limit12_4a/b, fig12_4, we12_4, mom12_5, drag12_5, contact12_5, brems12_6, limit12_6a and limit12_3b.
- `coh_ratio` of fig12_4.py, re-evaluated without plotting at 1.5–10 keV.
- Sources, fetched to sources/review-ch12/d2/ with the PDFs deleted afterwards: 2210.06490, 2505.08864, 2205.03395, 2603.13052, 1607.01789, 2312.10566 and 2208.12222.
- Not fetched: Schwerdtfeger 2018 (no arXiv copy), Franta, Li, Skauli, Henke and Born–Huang. Their values are checked only through the scripts.
- QE was not run, and the tex was not edited.

Verdict counts: PRIORITY items R9 and R13(a–c) are all CONFIRMED. There are 4 WRONG items, all small, and 7 GAPs. Everything else is CHECKED.

## PRIORITY

**R9 (12.3 free-recoil bracket): CONFIRMED.** The bracket is an artefact.
- Two time orderings for a free nucleus. With E_f = (q−p)²/2M, the intermediate-state energies are q²/2M and p²/2M. The amplitude is 1/(ω+E_f−E_λ) − 1/(ω+p²/2M) = b/[(ω−b+a)(ω+a)], with b = q·p/M and a = p²/2M. Sympy confirms this identically.
- Angle average of the square, divided by the soft-limit form b²/ω⁴: the result is 1 − 2p²/(Mω) + (9/5)v_N²p²/ω² + (5/2)p⁴/(M²ω²) + …. There is **no p²/q² term**.
- eq:12.3-bracket, (1/(ω−y) − 1/ω) with y = (q−p)·p/M, gives a different average: 1 + 3p²/q² − 6p²/(Mω) + …. Its leading numerator is (b − 2a)/ω², and ⟨(b−2a)²⟩/⟨b²⟩ = 1 + 3p²/q². This term comes from keeping the −p²/M of the nucleus's final momentum while dropping the matching +p²/2M in both denominators.
- Numerical check at p = 5.7 keV and ω = 4.4 eV (mpmath quadrature):

  | q | 12.3 bracket / lead | exact / lead |
  |---|---|---|
  | 2 keV | 25.35 | 0.99944 |
  | 5 keV | 4.895 | 0.99944 |
  | 10 keV | 1.972 | 0.99944 |

  This reproduces osc12_4.log Check 2 to all printed digits.
- Artefacts: the "3p²/q²" correction, "within 10 % above m_χ = 16.5 MeV", lim:12.3b's 0.495 at 5 MeV and 1.2 at 12 MeV, and F-rows.tex l.335 ("rate low by 1.18 at 12 MeV, 2.0 at 5 MeV").
- Correction: replace eq:12.3-bracket with b/[(ω−b+a)(ω+a)] and its expansion, eq:12.4-corr. The rebuilt solid curve of Limit Check 12.3b will be ≈ 1 − 2.1×10⁻³ at low mass and rise only through the Doppler term (9/5)v_N²p²/ω² at high mass.
- The bound-lattice curve (<1e-5, R6) is unaffected. The 9/5 Doppler numbers of 12.3 (0.04, 0.13 and 0.42 at 0.1, 0.3 and 1 keV) are unaffected.

**R13(a) (finite-frequency Born-charge sum rule, eq:12.6-sum): CONFIRMED.**
- Derivation: the comoving frame gives the inertial force m_eω²u, equal to −eE_in, so E_in = −m_eω²u/e. With P = (ε−1)E_in at zero macroscopic field and a neutral rigid cell, ΣZ* = −Ωm_eω²(ε−1)/e². The signs and the HL units are consistent.
- Limits (sympy): ε = 1 − ω_p²/ω² gives N_e exactly. A dilute gas gives −m_eω²α_pol/e², which is eq:12.6-atom. At ω → 0 the sum gives neutrality.
- Sign check: the spring model gives a negative Z*_at at low ω, which agrees.
- Kouvaris–Pradler (1607.01789): Eq. (3) is dN/dω = (2α/3π)Z²v²/ω. Eq. (8) replaces Z² by |f|². Their α(ω) = −(α/m_eω²)f in Gaussian units, which is eq:12.6-atom in HL units. All agree.
- Numbers:
  - Ω_Si m_e/e² = 2.9046e-2 eV⁻². With ε(1 eV) = 12.365, Z*(1 eV) = −0.1651. C_κ = 0.1554 eV⁻².
  - Z*_at(Si, 37.3 au) = −0.0504.
  - Polarizability per atom 227.6 Å³ against 69.5 Å³ for the free atom.
  - Per-photon ratio n_r(Z*/Z*_at)² = 37.7 at 1 eV and 32.8 at 0.3 eV, so "33–38" holds. Ge gives 85.7–96, so "86–96" holds.
- The research note's |Z*| ≈ 0.05 is the free-atom value, and the "comparable" verdict is overturned. Logged in state/NOVELTY.md as derivation-verified (the novelty search is still owed).

**R13(b) (bremsstrahlung conditions): CONFIRMED.**
- The expansion of the two orderings gives A = −⟨[[H,D],K]⟩/ω_γ², with [H,u] = −iP/M and [P,e^{iqX}] = qe^{iqX}. The result ie(q/M)·Z*·E is exact for any potential.
- D changes the phonon number by one, so only ω_γ ≫ ω_ph is needed. The impulse condition is not.
- The incoherent sum needs q above the zone. This is stated.
- GaAs numbers: Z*_Ga = 1.9363 and Z*_As = −2.2837, so ΣZ*² = 8.965. The atomic charges are f_Ga = −0.0675 and f_As = −0.0405, with Σf² = 6.20e-3. The per-photon ratio is 3.4185 × 8.965 / 6.20e-3 = 4.94e3. The band integrals are 75.43 and 4.033e-3, a ratio of 1.87e4, and the full rate gives 1.88e4.
- The split identity 2(2.11+b)² + 2(0.174)² holds.
- Ga at 100 eV: v_N² = 3.080e-9, 2α/3π = 1.5485e-3, and the result is 1.70e-10 photons. The mean over the two sites is 1.73e-10.
- Band −19/+25 % (7.44 and 11.5 against 9.19e-7). Rates 9e-7 (GaAs) and 2e-9 (Si). Median photon 0.36 eV.

**R13(c) (mass-proportional scalar absorption): CONFIRMED.**
- [H,[H,X]] = ∇V/M, so ω²⟨X⟩ = ⟨∇V⟩/M. Translation invariance gives ΣM⟨e^{ikX}⟩ = −m_e⟨n_e⟩ + O(k²) at dipole order. This is also checked through the center of mass: ΣM_I X_I + m_eΣr = M_tot R_cm.
- Γ = S/(2m_φ) with S_ee = 2k²L/e² gives eq:12.6-absrate. Mapping to the dark-photon rate is consistent with ζ² = κ².
- Dilute limit: Γ = n_at v σ_φ with σ_φ = c̃²m_e²(p/m)σ_γ/e². With c̃ = g/m_p this is Dzuba et al. Eq. (17) of 2312.10566 exactly: σ_φ = g²m_e²kσ_γ/(m_p²ω·4πα).
- eq:12.6-medium: n_r/|ε|² = 1 + (3/2)ω_p²/ω² + (15/8)ω_p⁴/ω⁴. At 1 keV with 12 electrons, ω_p = 28.75 eV and the factor is 1 + 1.24e-3.
- limit12_6a.log: within 10 % for m_φ ≥ 57.3 eV, 417× at 4.3 eV and 7.65 at 17.1 eV. All agree.

## Sect. 12.4

- l.3: q = 2m_χv_max = 10.60 keV. E_R(10 keV) = 1.911 meV. 2W = 0.0628 and e^{−2W} = 0.939. ½m v_max² = 7.02 eV. The onset 92.5 keV corresponds to 17.45 MeV. CHECKED.
- eq:12.4-exact and eq:12.4-series: re-derived. The 1/ω expansion of both orderings gives [A,B]/ω + [[A,H],B]/ω² + [[[A,H],H],B]/ω³. The signs match Berghaus Eq. (3.1), whose second denominator is E_λi − E_λ − ω. CHECKED.
- [A,H] = (p·P/M + p²/2M)A and [[A,H],B] = (q·p/M)e^{i(q−p)X}: verified on test functions with arbitrary U(x). CHECKED.
- Third order: [[[A,H],H],B] = b(2X − b)BA, verified identically on test functions. The ∇U term commutes with B. ⟨2X − b⟩ in BA|0⟩ = p·(q−p)/M. CHECKED.
- eq:12.4-corr: free part −2p²/Mω + (9/5)v_N²p²/ω² (sympy). Binding part +2⟨ω²⟩/ω² from the squared propagator (sympy: 1 + 2ω_n²/ω² + 3ω_n⁴/ω⁴). The omitted (5/2)p⁴/M²ω² is about 1e-6. CHECKED.
- l.41 numbers:
  - Recoil term −2.07e-3. Binding term +2.78e-3 (⟨ω²⟩^{1/2} = 44.7 meV).
  - Doppler at the onset: v_Np/ω = 0.0168, so (9/5)ξ² = **5.1e-4**, not "at most 5e-4". This is cosmetic. Write "≈ 5×10⁻⁴" here and in tab:12-nuisances and F-rows l.356.
- lim:12.4a caption and box:
  - Squares offset 2p²/Mω − 2ω₀²/ω² = 0.031. The box writes 0.03, which is fine.
  - ξ ≤ 0.270 (limit12_4a.log). Fails at q = 1.49 MeV.
  - CHECKED.
- eq:12.4-harm: dimensions eV⁻². The sum rule over ω_l gives eq:12.3-soft. eq:12.4-rate: ρσ/(2mμ²M)∫q dq η, from dE_R = q dq/M. CHECKED.
- Berghaus 2210.06490 Eqs. (3.1), (3.6), (3.8), (4.1) and (4.5) are as cited. In Eq. (3.8) the diagonal is set by "small off-diagonal" ELF elements. CHECKED.
- l.77 (G ≠ G′): the text separates local fields inside the diagonal (the 35 %) from the off-diagonal (ε⁻¹)_{GG′} elements of the Migdal sum (unsized). That is physically right, and Liang Eq. (3.3) keeps G,G′. R1's sentence ("these are the local-field effects") conflates the two. Keep the book wording. **Editor note:** R1 should say "local fields in the diagonal, ≈35 %; G ≠ G′ unsized", as tab:12-nuisances already does.
- l.81 and l.90: all regime fractions, 6.13 keV, 2.50 E_R, 1.196 meV, 10.4 E_R at 2 keV, 3.79 % against 1.56 % and 48.5 meV match fig12_4.log. CHECKED.
- l.92 Bragg/incoherent: re-run coh_ratio gives 1.082 (1.5 keV), 1.043 (3), 1.027 (5), 0.987 (7.5) and 0.996 (10). Median p/q_BZ = 5.64/2.25 = 2.5. CHECKED.
- l.94 Ge:
  - Debye ⟨ω⁻¹⟩⁻¹ = (2/3)k_BΘ_D × 0.82 = 17.57 meV. The 0.82 factor is 30.4/37.05 for Si.
  - The half point is at 40.6 keV, or 7.66 MeV.
  - Onset: E_R = 4⟨ω⟩ with ⟨ω⟩ = (3/4)ω_D × 0.981 = 23.6 meV gives 113 keV and 21.3 MeV.
  - Mass ratio 2.59. Binding term 2.98e-3 at 0.67 eV.
  - CHECKED.
- eq:12.4-pm:
  - Re-derived. aB = B(a + β) with β = iq·ℓ*, and Ba† = (a† − β*)B, so the a†B terms cancel.
  - (p·ℓ)(q·ℓ*)/(ω−ω_ν) − (p·ℓ*)(q·ℓ)/(ω+ω_ν) = (q·e)(p·e)/[NM(ω²−ω_ν²)]. The sign is consistent with eq:12.4-lead.
  - The cubic projection uses g_ph,κ normalized to three (NOTATION l.521), so ∫g/3 = 1 and the ω_ν → 0 limit is q·p/(Mω²).
  - CHECKED.
- Liang 2205.03395: Eq. (3.1) propagator 1/[(ε_i−ε_j)² − ω²], Eq. (3.2) reduction, Eqs. (3.3)–(3.5) with Im ε̃⁻¹_{GG′} and constant Z_ion, T₀ = δ(E) and the Note added. All as cited. CHECKED.
- lim:12.4b: two-phonon weight p²/(2Mω₀) = 0.0204. Within 10 % for ω ≥ 4.22ω₀. Si DOS within 10 % above 0.200 eV. 0.99708 at 1.17 eV. CHECKED.
- l.139: 2.9e-3 (Si gap), ≈3e-3 (Ge with scaled spectrum) and 3e-4 averaged. CHECKED.
- WE 12-five-keV:
  - E_R = 0.4778 meV, v_N = 1.911e-7 (57.3 m/s), m ≥ 0.943 MeV, 0.75 and 7.00 eV, 2W = 0.0157, 2.22 q_BZ.
  - P = 2.899e-8, one in 3.45e7. 1.0029 and 1.0003.
  - 96.2 % and 2.79e-8. 1.10e-9 with 96 % one-phonon.
  - 30.4 and 21.7 meV, 64 E_R. Factor 26 and factor 2.43.
  - Check values 0.99934, 0.9980 and 0.967/0.984.
  - All CHECKED. The 2.95 q_BZ and 18 keV certification thresholds belong to 11.3 and were not re-derived.
- Esposito–Rocchi 2505.08864 Eq. (21) is q·⟨φ_n′|∇_X V_eN|φ_n⟩/ω² with M_ad = 0 for an infinite solid. CHECKED.
- **GAP (R14 pointer):** l.157 ends "(\cref{sec:12.6})". Point to \cref{tab:12-nuisances} instead.

## Sect. 12.5 and App. D.34

- eq:12.5-spectrum and D.34-moments: |q·F|²/(M²Δ⁴) from d = −F/Δ. δM = 2𝓘₃ gives E₁ = E_RδM/M. E_BH = 𝓘₂/2M gives E₂ = 4E_RE_BH. CHECKED.
- eq:12.5-dMval: M²ω⁴/q² × soft form gives 4α∫Z²(q̂·p)²L/p². The angle average 1/3 gives 8α/3. e²/π = 4α. Dimensions eV (mass). CHECKED.
- D.34-dynamic: χ = Σ|F|²[1/(Δ−ω) + 1/(Δ+ω)] = 2Δ/(Δ²−ω²). Expanding gives −ω²·2𝓘₃. At imaginary frequency the sign flips. CHECKED.
- D.34-trace:
  - Σ_J⟨a|∇_JV|0⟩ = −i⟨a|[P_e,H]|0⟩ = iΔ⟨P⟩, and ⟨P⟩ = im_eΔ⟨X⟩. This gives 2m_e²ΣΔ|X|² = N_em_e by TRK.
  - The signs and the factor 2 are consistent with eq:D.28-dM.
  - Chain model (drag12_5.log): 2.000, 1.290 at 8.09 eV, 0.922 at 5.35 eV, trace 2.0000.
  - CHECKED.
- **WRONG (small): l.65, l.69 and WE l.90.**
  - 10.1 + 18.6 = 28.7 m_e and M/m_e = 51 197 give δM_II/M = **5.61×10⁻⁴**, E₁ = **0.280 eV**, and an off-site sum of **−14.7 m_e**.
  - mom12_5.py l.180–182 uses a core value of exactly 10 m_e (28.55 m_e). That is where 5.58e-4, 0.279 eV and −14.6 come from.
  - The WE itself adds to 0.099 + 0.181 = 0.280.
  - Fix: either quote 5.60×10⁻⁴, 0.280 eV and −14.7 m_e, or fix the script to use the 10.12 m_e of its own core table. The bound 0.24 is unchanged.
- WE 12-drag, other numbers:
  - q = 5.115 MeV and v_N = 1.955e-4. Trace 2.735e-4.
  - Valence: 0.1812 eV, P ≤ 0.163, E₂ = 1.887 eV², P ≥ 0.0174, P = 0.0303.
  - Cores: bound 8.05e-4, P = 3.98e-4. Totals 0.031 and 0.164. Trace-value bound 0.117.
  - Width 500(0.0409/500)^{1/2} = 4.52 eV, and 0.28/4.5 ≈ 1/16.
  - CHECKED.
- l.85: 19 % and 1.74 (Si), 15 % and 1.92 (Ge), ⟨ω⟩ 5.97/5.07 eV, 2p 50 %. l.87: 10⁻³ at 16.5 eV. l.67: 96 %, 61 %, 67 %, ≤24 %, 11.8 and 24.0 m_e. All CHECKED.
- l.67 "momenta above 22.5 keV add <3 %": the log only gives 2.8 % for p > 10 keV inside the table, so the 22.5 keV statement is an extrapolation. **GAP:** state it as an estimate, or give the script line.
- **WRONG (comparison): l.69.** "Ge cores carry 26.8 m_e in the atomic tables without the 1s, close to the 28 m_e of a rigid core." A rigid core without 1s holds 26 electrons, since 28 includes the 1s. Correction: "close to the 26 m_e of a rigid core without the 1s" (26.8 against 26).
- Ge valence 39.5 with band 11.5–52.1, and table rows 6.07/5.89e-5, 5.97/5.07, 3.77/2.91e-3: mom12_5.log. CHECKED.
- l.85: "the exact free-recoil bracket of sec:12.3-validity ... about 20 % near 500 eV". The 20 % is the 9/5 Doppler term, which survives R9, but the pointer goes to the bracket R9 invalidates. **GAP:** cite eq:12.4-corr (Doppler term) instead.
- **GAP (R14):** l.69 "(\cref{sec:12.6})" should be \cref{tab:12-nuisances}. The NOTATION δM_κ row (l.895, "Si estimate 14 m_e") should read "trace value 14 m_e; on-site 28.7 m_e (12.5)".
- eq:12.5-cross and D.34-cross:
  - X = R_cm − (m_e/m_A)Σρ and r_e = R_cm + ρ_e − (m_e/m_A)Σρ re-derived.
  - Elastic moment 2n(q²/2m_A)Re[⟨A_e⟩*⟨A_κ⟩].
  - Small q: F_cr = Z − Z*, giving 14, 28.89 and 35.11.
  - Geometric mean: √(N_em_e/m_A² · N_e/m_e) = N_e/m_A. The symmetrized-moment convention is used consistently for the ee, κκ and eκ moments.
  - CHECKED.
- eq:12.5-third and D.34-third: E₃ = (q²/2M²)(⟨∂²V⟩ − ∂²E₀), and ∇²_R(−Ze²/4π|r−R|) = Ze²δ³. CHECKED.
- Third-moment numbers:
  - Ze²n/3M: Si 1497.0 eV², Ge 16 848.6 eV².
  - Lattice ratio 1.34e-6. Uniform term 2n_e/n^(κ) = 2 × 0.1036/1765 = 1.17e-4.
  - Table window 5.0e-5. Ge valence share 8.5e-4.
  - All CHECKED. The Si valence share of 0.43 % was not in the logs and is unverified.
- Relation to CORRECTIONS J8 / (4.7′): the returns quote NR coefficients of 1501 (Si) and 16 867 (Ge) at r = 0. The book's 1497 and 16 849 come from its own HF densities (1765 and 22 475 a₀⁻³), a difference of 0.3 % and 0.1 %. The book's numbers stand and are not superseded. The returns' "+37–45 %" is superseded by R16; the book's 40–45 % (Ge 42.5, Ga 39.7, As 45.4) is consistent.
- eq:12.5-Rrel and D.34-dirac:
  - Normalization ∫4πr²n = 1 checked. NR limit λ³/π. Sphere average 3R^{2γ−2}/(2γ+1).
  - Values: R_rel = 1.0823, 1.4249, 1.3972 and 1.4542. Log terms 0.0658 and 0.2811.
  - CHECKED.
- **WRONG (factor 2): l.137, radius sensitivity.**
  - Since R_rel ∝ R^{2γ−2}, a 10 % change in radius moves R_rel by (2γ−2)ln 1.1: **0.10 %** (Si) and **0.53 %** (Ge).
  - The text's 0.05 % and 0.3 % used γ−1 in place of 2γ−2 (mpmath: −0.0997 % and −0.526 %).
- **WRONG (small): D.34 l.80.**
  - "2λr ≤ 2ZR/a₀ ≈ 10⁻³" is actually 1.8e-3 (Si) and 5.8e-3 (Ge).
  - Dropping e^{−2λr} inside the nucleus overstates R_rel by 0.14 % (Si) and 0.43 % (Ge): the sphere average with the exponential kept gives 1.0808 and 1.4187.
  - Either keep the factor or state the bound correctly. The quoted 24 008 for Ge would move to 23 904.
- **GAP: D.34-dirac and 12.5.**
  - (i) Using the point-charge orbital inside the nucleus fixes only the log term. The non-log O((Zα)²) remainder (0.144 of 0.425 in Ge) depends on the model and should carry an uncertainty of O((Zα)²) ≈ 5 %.
  - (ii) Relativistically the 2p₁/₂ (and 3p₁/₂) small components are s-like at the origin and add contact density of relative order (Zα)² to the n = 2 s density, which is omitted.
  - State both in the open-problem paragraph and in the tab:12-nuisances row "Relativistic contact density".
- eq:12.5-Rrel second form "1 + (Zα)²ln + O((Zα)²)": the O((Zα)²) should be written as non-logarithmic, for example "+ O((Zα)²) without the logarithm". Notation only.

## Sect. 12.6

- eq:12.6-classical: (2α/3π)Z²v²/ω, KP Eq. (3) with v² = 2E_R/M. Dimensions eV⁻¹. CHECKED.
- l.19: spring amplitude ω_n²u/(ω_n² − ω²), dipole −euΣf_nω²/(ω_n² − ω²). Re-derived. CHECKED.
- eq:12.6-ZSi second form: Ωm_e/e² = N_v/ω_p,val², with ω_p(4 e/atom) = 16.60 eV. CHECKED.
- **Notation drift (NOTATION l.901, "Z*(ω) argument mandatory; Z*_κ is static"):**
  - l.71 writes "Z^* = −0.165" for the value at 1 eV. Write Z*(1 eV).
  - WE 12-gaas writes Z*_Ga = 1.936 and Z*_As = −2.284 for the values at 1 eV. Write Z*_Ga(1 eV) and Z*_As(1 eV).
- **GAP (wording): l.71.** "polarizability … 3.3 times … and the photon gains n_r = 3.5 on top" does not produce 33–38 unless the 3.3 is squared, because the emission goes as |Z*|². Add "squared, 10.7, times n_r".
- l.82 numbers: 4.03e-13, 1.73e-10, 9.2e-7, 2.1e-9, median 0.361 eV, seven orders (30/9e-7 = 3e7). CHECKED. The Si Migdal rate of 30 is from 12.3 and was not rechecked.
- WE 12-gaas:
  - Ω = 44.80 Å³ uses a = 5.638 Å, labelled "measured" in Chap. 5. The measured GaAs value is 5.653 Å (300 K) or 5.648 Å (low T), so Ω is 0.8 % low.
  - Ge uses a = 5.658 here against 5.652 in Table 5.x.
  - These are not errors of 12.6, but **flag for the Chap. 5 owner**: unify the lattice constants. Every 12.6 GaAs number moves by under 1 %.
- Medium factor "+1.2×10⁻³ at 1 keV" agrees with CORRECTIONS (WP7-B2 IF-B2-8). SOTA's "GaAs ~10³× atomic (est.)" is superseded by the computed 4.94e3 at 1 eV and 1.87e4 over the band. The book uses the computed values. CHECKED.
- l.110: "Its matrix element is the force … minus the force of the other nuclei". ∇_X V is minus the total force on nucleus I from the electrons and the other nuclei. Reword: "minus the total force on nucleus I". Wording only.
- l.104–108: c_κ = Zg_pp + (A−Z)g_nn carries the coupling. NOTATION l.869 defines c_κ dimensionless, in units of Ṽ_N ("A_κ for equal couplings"). The 12.6 usage (c_κ = A_κg_φnn) is a convention drift. Add "here in units of the coupling" to NOTATION, or rename it.
- l.102, l.154: k = 1 eV and recoil 1.9e-11 eV. kr = 2.4e-4 at 10 keV. Z/M: Ga 0.4446, As 0.4405. Si isotopes 6.7 %, given as "up to 7 %". CHECKED.
- Dimensions of eq:12.6-absrate: c̃ in eV⁻¹, c̃²m_e² dimensionless, Γ in eV and R per mass. CHECKED. ⟨v²⟩^{1/2} = 378.9 km/s. CHECKED.
- tab:12-nuisances: holds every R12 and R14 row. The values match the sources above, except the Doppler entry "at most 5×10⁻⁴" (5.1e-4, cosmetic) and the relativistic row, which should carry the GAP above. CHECKED with those two notes.
- Summary (l.200–210): its numbers repeat those checked above. They are consistent, and the summary quotes none of the R9 artefacts. CHECKED.

## Known items (editor-notes) for these files

- 12.4 writer CONFLICT: confirmed (R9 above).
- R10 attribution: no misattribution in 12.4–12.6. The F-row l.354 attributes to 2603.13052 correctly (I checked that 2603.13052 is the ten-operator paper).
- R11: 12.6 l.192 states that the headline numbers use 6.1 keV (Z_ion), and 5.6 keV is the point-ion value. Done.
- R12 and R14: table rows present. The pointers in 12.4 l.157 and 12.5 l.69 still go to sec:12.6 (GAP above).
- R15: 12.5 l.87 restricts the claim correctly ("10⁻³ at 16.5 eV"). The 8.6 and 12.1 edits are outside these files.
- Part II notes:
  - 12.5 keeps the 11.4 c₃ split: done.
  - 12.6 introduces c_κ: done, with the notation drift above.
  - Ge 3d 29.4 eV: done.
  - GaAs Z* = 2.11: done.
