# App E derivation check, part 2 (E.7–E.13)

Verifier: long-form-writing SKILL §5. Scope: tex/appE/E-7.tex … E-13.tex against NOTATION, STYLE and the cited public sources
(fetched to sources/review-appE/, PDFs deleted after extraction).
Methods:
- sympy for the symbolic identities: the QHA derivative → n+½; the scissor factor; the Heisenberg 3×3 mapping (with a common reference); the spiral identity; the f-sum kinetic expansion.
- numpy/scipy for the numbers.
- An exact one-magnon diagonalization.
- IBZ counts brute-forced with the 48 operations of O_h.
No tex edited.
Legend: CHECKED = redone and agrees; WRONG = error, with the correction; GAP = missing step, undefined convention or unsourced value.

## Summary of actionable items (detail below)
1. WRONG E.9 l.55: the ferromagnetic magnon and frozen-magnon relations are a factor 2 too large.
2. WRONG E.9 we:E-al: the T_c factors 0.63/1.59 do not match the quoted endpoints (0.60/1.53).
3. WRONG/GAP E.10 l.52–57: factor-2 conventions in δ̃ (eigenphase vs phase-shift difference) and in V_d (change vs half-difference).
4. WRONG (printed definition) E.12 l.26: ⟨c³⟩ is really ⟨c⁻³⟩⁻¹ (the number 2.13e11 is only right for that average).
5. WRONG E.7 l.113: "highest band left out" should be "lowest band left out" (57 eV).
6. WRONG E.7 l.132: 500×900 bins reach 67 keV; at q_max = 30 keV the table is about 500×400.
7. GAP E.7 l.130: the 0.6 eV gap is cited to the LDA Table V (0.463 eV). Use the book's own PBE calculation (0.602 eV).
8. GAP E.9 l.3, l.48: "11–27 meV, factor 2.5" holds only if the UHF entry of Fischer Table III (4.6 meV) is excluded.
9. GAP/likely WRONG E.7 l.89: "116/170/1900 eV below the valence maximum" appear to be RHF orbital energies relative to vacuum, not depths below the VBM (see the E.7 entry).
10. GAP E.13 Eq. (E.13-ab): A_AB in eV² makes the rate ratio carry eV⁻¹ (inherited from the source).
11. RESOLVED (editor note) E.13 l.36: z_qp ≈ 0.8 has a source, Kotani et al. 2010, Sect. II: "Typically Z_kn is ∼0.8".
12. Convention: J^ex is undefined in NOTATION; the Γ typography drifts in E.11–E.13; E.9 LKAG needs a conversion at the point of use.

## E.7 Crystal form factors and the density vertex
- l.3 term count 5×10¹¹ → CHECKED (10⁶·4·52·2376 = 4.94×10¹¹).
- l.9 vertex definition and l.11 placement on 𝔗₀ → CHECKED against NOTATION (f_crys, W^scr, z_qp rows).
- Eq. (E.7-pw) normalization; Eq. (E.7-rhopw) from the cell integral Ω δ_{G′,G+G_U} → CHECKED. It equals Essig et al. Eq. (3.16), with G′ = G_U and q = k′−k+G_U.
- l.29 N_FFT/N_pw: cube 64k_c³ → 8Ωk_c³/π³ points, sphere Ωk_c³/6π², ratio 48/π = 15.3 → CHECKED. The FFT route is in Griffin et al., below Eq. (3.15) → CHECKED.
- l.31 grid resolution and the 48-fold symmetry factor → CHECKED. Fractional-translation phase e^{−ik_rot·t_f}: sign is convention-dependent, acceptable.
- l.33 gauge invariance, Γ₈ threefold degeneracy → CHECKED.
- Eq. (E.7-v): i[p²/2m_e, r] = p/m_e (ħ=1) → CHECKED. ∇_k V_NL(k) = e^{−ikr} i[V_NL,r] e^{ikr} → CHECKED (sympy-free, one line: ∂_k e^{−ikr}Ve^{ikr} = e^{−ikr}(−irV+iVr)e^{ikr}). Eq. (E.7-vNL) → CHECKED.
- l.52 Ismail-Beigi et al. Fig. 1 (diamond, 15–20 %) and Eq. (20) (v = −i[r,H]) → CHECKED. Eqs. (18)–(19), the straight-line phase → CHECKED.
- l.54 the density-vertex optical limit uses only i[H,r] = v → CHECKED.
- Eq. (E.7-scis): ⟨c|r|v⟩ = −i v_cv/(ε_c−ε_v); ⟨c|i[P_c,r]|v⟩ = v_cv/(ε_c−ε_v) ⇒ factor (Δε+Δ)/Δε → CHECKED. The optical limit is unchanged → CHECKED.
  Note: Zacharias et al. 2016, Sect. VII prints the renormalization factor as (ε_c−ε_v)/(ε_c−ε_v+Δ). That factor applies to their oscillator-strength form. The book's factor applies to v_cv. Both are consistent, but a reader who compares them will be confused. Consider half a sentence.
- l.61 Δ_scis = 0.74 eV (Zacharias 2016, Sect. VII: "∆ = 0.74 eV … for Si") → CHECKED. LDA direct gap 2.567 eV (Poncé 2015, Table V) → CHECKED. Factor 1.288 → 1.29; squared 1.659 → "66 %" → CHECKED.
- Eq. (E.7-paw) = Griffin Eq. (2.6) → CHECKED. Eq. (E.7-pawO): cross terms cancel by completeness → CHECKED (standard Blöchl). Eq. (E.7-radial) → CHECKED.
- l.72 second cutoff 2 keV → q = (2m_e·2 keV)^{1/2} = 45.2 keV → CHECKED (Griffin Sect. 2.1.1, "E_AE = 2 keV").
- l.72 vs l.96 GAP (minor): the same √(2m_e E_AE) is "≈45 keV" at l.72 and "about 50 keV" at l.96. Griffin writes "≃ 50 keV". Use 45 keV in both places, or write "about 45 keV (≃50 keV in Ref.)".
- l.85 the claim from Griffin Sect. 3.1 (AE rate enhanced even at thresholds as low as ∼10 eV) → CHECKED (source l.987).
- l.89 core depths 116/170/1.9 keV (Si) and 28 eV (Ge 3d) agree with Griffin Fig. 1 → CHECKED as citations.
  GAP, likely WRONG: Griffin does not state the origin of these energies, and the origin is not uniform across the figure.
  The Si values match the Clementi–Roetti RHF orbital energies of the free atom: −4.256, −6.157 and −68.81 Ha, i.e. 115.8, 167.5 and 1872 eV relative to vacuum. These were recalled, not fetched; verify against bunge1993roothaan.
  Ge 3d at 28 eV does not fit RHF (≈44 eV).
  The nominal measured binding energies are ≈99 eV (2p), ≈150 eV (2s) and ≈1839 eV (1s) (tabulated values from memory, not verified here). No bib entry carries measured Si core levels, so the fix needs a citation.
  If the RHF reading holds, "below the valence maximum" is wrong.
  The kinematic numbers on this line follow from 116 eV. With ω = 1.17+116 eV and v_max = 794.5 km/s (2.650×10⁻³): m_χ = 33.4 MeV and q ≥ 44.2 keV → CHECKED.
  With the measured ~99 eV they become ≈28 MeV and ≈38 keV. Say "model (orbital) energies of Ref." or recompute. The same applies to the we:E-siff closing line, "q ≥ 44 keV, closed below 33 MeV".
  Ge 3d: ω = 0.74+28: 8.18 MeV and 10.8 keV → CHECKED.
- l.96 Eq. (E.7-core) = Griffin Eq. (2.8) → CHECKED. Griffin Sect. 2.2: atomic orbitals reproduce the DFT 2p/3d states → CHECKED.
  (Zα)²: Si 0.0104, Ge 0.0545, Xe 0.155 → "1 %, 5 %, 0.16" → CHECKED.
- Eq. (E.7-sto) normalization: (2Z)^{2n+1}/(2n)! · ∫x^{2n}e^{−2Zx}dx = 1 → CHECKED. It matches Catena et al. Eq. (B33).
  Z_eff = n(E_B/13.6 eV)^{1/2} = Catena Eqs. (B34)–(B35) → CHECKED. l′_max = 7 (Catena l.2309) → CHECKED. Two consecutive intervals → CHECKED.
- l.107 2m_χ v_max at 1 GeV = 5.30 MeV → CHECKED.
- l.113 (70 Ry → 952.4 eV → 31.2 keV); the Ecut scan 30–110 Ry with <O(1 %) at 70 Ry (Essig App. C) → CHECKED.
  Shaken grids: Δk = 0.08 a.u. against spacing 0.17 a.u., 10 runs → CHECKED.
  Bins 0.1 eV and 0.02 αm_e → CHECKED (Essig Sect. 4.2).
- l.113 WRONG: "with 52 conduction bands the highest band left out lies about 57 eV above the gap". Essig: "The lowest conduction states not included are about 57 eV above the band gap". Correction: "the lowest band left out".
- Eq. (E.7-fsum) CHECKED step by step.
  Completeness gives ⟨u|H(k+q)−H(k)|u⟩. The kinetic part gives q·(p+k)/m_e + q²/2m_e. Hellmann–Feynman gives q·v^g. δ_NL is defined as the beyond-linear remainder.
  Time-reversal pairing: ρ_nm(−k−q,q) = ⟨u_{n,−k}|u_{m,−k−q}⟩ = ⟨u_{m,k+q}|u_{nk}⟩ = ρ_mn(k,q), with the opposite energy difference → CHECKED.
  Dimensions [eV] → CHECKED.
- l.127 Essig Eq. (4.2), w_k = 2 (spin in the k weights) → CHECKED. Ge has no PBE gap (Griffin Sect. 2.1) → CHECKED.
- we:E-siff
  - Ω = 40.048 Å³; N_pw = 2673 ("≈2700"); 2.39 GB; BZ volume 47.59 keV³; N_G = 2376 ("≈2400") → CHECKED.
  - Transforms 2.08×10⁸; N_FFT = 4.08×10⁴; 5N log₂N = 3.13×10⁶ flop; total 6.5×10¹⁴ ≈ 1.8 h at 10¹¹ flop/s ("of order an hour") → CHECKED. Order of magnitude consistent.
  - Kinematics at 10 MeV with ω = 1.17 eV: q ∈ [0.445, 52.6] keV → "0.45 and 53" → CHECKED.
- we:E-siff l.130 GAP: "Kohn–Sham gap of a semilocal functional is about 0.6 eV [Poncé Table V]". Table V's own Si value is LDA 0.463 eV. The 0.612 in that table is another reference's number.
  Editor notes rule that E.1's PBE+SG15 calculation (indirect gap 0.602 eV, Δ_scis = 0.568 eV in E.3) is the book's representative calculation.
  Correction: "about 0.6 eV in the representative PBE calculation (\cref{we:E-si-bands})". Drop the Poncé citation here. This also removes the LDA/PBE mix with the LDA 0.74 eV scissor at l.61.
- we:E-siff l.132 WRONG: "the binned output … has 500×900 entries". That is Essig's published table. 900 q-bins of 0.02 αm_e = 74.6 eV reach 67 keV, beyond the 31 keV this calculation contains.
  At q_max = 30 keV the bin count is ≈ 500×400. Correction: "≈500×400 entries (the published table of Ref. has 500×900, reaching 67 keV)".
- Silicon constants in E.7 (gap 1.17 eV, a = 5.431 Å) → CHECKED against Sect. 1.3/E.1. ε∞ does not appear.

## E.8 Anharmonic and finite-temperature methods
- l.3 ZPR 62/64 meV (Poncé 2015, Table VI, experiment) → CHECKED. 1.17 → 1.12 eV is a 50 meV change → CHECKED.
- Eq. (E.8-qha) per cell; ∂_ω[ω/2 + T ln(1−e^{−ω/T})] = n + ½ → CHECKED.
  Eq. (E.8-beta): P_ph = (1/NΩ)Σγ^G ω(n+½) ⇒ α_th = (1/B)(∂P/∂T)_Ω → CHECKED against Baroni et al. Eqs. (6), (9).
  The Grüneisen rename to γ^G (editor ruling) is applied → CHECKED.
- l.24 δω/ω = −γ^G δΩ/Ω = −3γ^G δa/a → CHECKED. ZP lattice expansion +9 meV (Miglio et al. Table S2: "Si-dia … ZPR_lat +9") → CHECKED.
- l.22 negative TA Grüneisen and negative low-T expansion → CHECKED (Baroni Sect. 5.1).
- Eq. (E.8-scha), Gibbs–Bogoliubov (Monacelli Eq. (2)), trial H (Eqs. (4), (7)) → CHECKED. N_eff = (Σw)²/Σw² (Eq. (38)) → CHECKED.
- Eq. (E.8-tdep): the sign F = −Φu is consistent with the note on the opposite sign convention → CHECKED.
  Remark: Hellman 2011 Eq. (3) prints the unsquared |F−F̃|. The squared form in the book is the one the pseudo-inverse minimizes, so it is acceptable.
- l.48 classical/quantum MSD ratio 2T/[ω(2n+1)] → 2T/ω → CHECKED. At 10 mK and ω = 10 meV it is 1.72×10⁻⁴ ("< 2×10⁻⁴") → CHECKED.
- Eq. (E.8-fan): sign, (2n+1) weight and 1/N → CHECKED. Rigid-ion AH and non-adiabatic ±ω → CHECKED (Poncé Eqs. (11), (15), (16) cited).
- l.65 100³ grid = 22 776 irreducible points → CHECKED (brute-force O_h orbit count 22 776; Poncé: "100x100x100 q-grid (22776 q-points in the IBZ)").
- Eq. (E.8-wl) σ² = (2n+1)/2ω in mass-weighted coordinates (ħ=1) → CHECKED.
- Eq. (E.8-zg) prefactor [(2n+1)/(2NM_κω)]^{1/2}·2Re[…] = Zacharias 2020 Eq. (2) with σ = [(2n+1)/(2M_pω)]^{1/2} and (M_p/NM_κ)^{1/2} → CHECKED.
  The supercell-averaged MSD over B (half the Q) equals the thermal value → CHECKED.
- l.83 GaAs 6×6×6 = 432 atoms, within 10 % (Zacharias 2020 l.1227) → CHECKED. Si 8³ = 1024 and 4³ = 128 atoms; cost ratio 8³ = 512 for N³ scaling → CHECKED.
- l.85 8×8×8, 40 random k, scissor 0.74 eV, 30 meV, seven orders of magnitude (Zacharias 2016 Sects. II, VII) → CHECKED.
- l.87 "adiabatic and non-adiabatic differ by 8 meV" (64.3 − 56.2 = 8.1) → CHECKED. The editor wording is kept.
- we:E-zpr
  - −64.3 and −56.2 meV (Table VI) → CHECKED.
  - ZG −57 = −(35 + 22) meV, CBM at ≃0.87 ΓX, bracket 55–65 meV from 10³, 4³ within 10 % (Zacharias 2020 Sect. VII B) → CHECKED.
  - Overscreening attribution (same source, l.1137) → CHECKED. "About ten percent": 57 vs 62–64 is 8–11 % → CHECKED.
- we:E-zpr l.96 nit: "occupations below e^{−ω/T}". In fact n = e^{−x}/(1−e^{−x}) is slightly above e^{−x}. Write "of order e^{−ω/T}".
  ω/T at 1 K and 10 meV = 116 (≳10²) → CHECKED.

## E.9 Magnetic and superconducting parameters
- Eq. (E.9-U) = Cococcioni Eq. (9) → CHECKED. Eq. (E.9-Ulr) Eqs. (15), (18), (19) → CHECKED.
  NiO U = 4.6 eV (Cococcioni Sect. V) → CHECKED.
  Timrov Table I: NiO 7.895/7.900 (2×2×2) → 8.168/8.172 (4×4×4), routes agree within 5×10⁻³ eV → CHECKED.
  dos Santos 6.26 eV (Sect. II) → CHECKED.
- Eq. (E.9-map) energies per ion for FM/AFI/AFII (fcc, 12 NN, 6 NNN, pairs once) → CHECKED by counting.
  Eq. (E.9-J12) inverts it exactly → CHECKED.
  Fischer et al.: H = −Σ_{ij} J e_i·e_j (double counted), J₁ = (E_AFI−E_FM)/16, J₂ = (4E_AFII−3E_AFI−E_FM)/48 ⇒ ours = −2×theirs for |S| = 1 → CHECKED.
  Measured −8.66/−9.51 → 17.3/19.0 meV → CHECKED.
- l.3, l.48 GAP: "computed values … range from 11 to 27 meV" and "a factor of two and a half". Fischer Table III NiO J₂: −6.92, −9.54, −5.50, −9.35, −13.35 and UHF −2.30 → ours 13.8, 19.1, 11.0, 18.7, 26.7, 4.6 meV.
  The quoted range holds only if UHF is excluded. Either say "the DFT-based values (excluding unrestricted Hartree–Fock)" or quote 5–27 meV (factor ~6).
- Eq. (E.9-spiral): S_R·S₀ = S²(sin²θ cos QR + cos²θ); per ion ½Σ_R → (S² sin²θ/2)[J(Q)−J(0)] → CHECKED.
- l.55 WRONG (factor 2): "linear spin-wave theory gives ω(Q) = 2|S|[J^ex(Q) − J^ex(0)]" and "ω(Q) = 4[E(Q,θ)−E(0,θ)]/(|S| sin²θ)".
  For H = Σ_⟨ij⟩ J S_i·S_j (pairs once) the Holstein–Primakoff result is ω(Q) = |S|[J^ex(Q) − J^ex(0)]. Exact check: the one-magnon spectrum of an 8-site S = ½ ferromagnetic ring equals S[J(Q)−J(0)] to 10⁻⁴.
  The frozen-magnon relation is then ω(Q) = 2[E(Q,θ)−E(0,θ)]/(|S| sin²θ), i.e. 4ΔE/(m sin²θ) with m = 2|S| the moment in μ_B (Jacobsson Eq. (12), with |M| the moment).
  The book's 2|S| is the double-counting formula. Correct both expressions.
- l.59 GAP (STYLE "content at point of use"): Eq. (E.9-lkag) is left in TB2J's convention (H = −Σ_{i≠j} J e·e, unit spins; TB2J Table 1). Add: "in the convention of Eq. (E.9-heis), J^ex_ij = −2J_ij/|S|²."
  The formula itself (TB2J Eq. (19)) → CHECKED.
- l.62 dos Santos: ΔE-based LSWT overestimates by ~14 %, MFT by up to 40 % (46 meV) for NiO → CHECKED.
- Eqs. (E.9-Z), (E.9-Delta), (E.9-lambda): isotropic Matsubara Eliashberg, λ(0) = 2∫α²F/ω → CHECKED. Lee et al. Eqs. (41), (42), (48) → CHECKED.
  Eq. (E.9-AD) = Lee Eq. (30) → CHECKED. μ* 0.1–0.2 and the cutoff of 10× the maximum phonon frequency (Lee Sect. 4) → CHECKED.
- l.90 40.5 meV = 470.0 K; 10ω_max/(2πT) = 748 at 1 K and 7480 at 0.1 K ("750", "7500") → CHECKED. Savrasov ω_max ≈ 470 K → CHECKED.
- we:E-al
  - λ 0.44 and 0.42 (Table II); ω_log 270 K, T_c 1.18 K, μ* 0.12, Δ₀ 0.18/0.18 meV (Table III) → CHECKED.
  - 1.764·1.18 K = 0.1794 meV → CHECKED.
  - AD exponent 5.2134, T_c = 1.2248 K ("1.22"); 3.8 % ("within four percent") → CHECKED. ∂lnT_c/∂μ* = −23.1 → CHECKED.
  - T_c(0.14) = 0.738 K and T_c(0.10) = 1.872 K → CHECKED.
- we:E-al WRONG: "moves T_c by a factor of 0.63 or 1.59". Those are the linearized exp(∓0.46). The quoted endpoints give 0.738/1.225 = 0.60 and 1.872/1.225 = 1.53. Correction: "by a factor of 0.60 or 1.53".
- Convention (editor item, E.7–E.10 vs 7.1): E.9 is self-consistent with pairs counted once and J > 0 AFM.
  NOTATION row J^ex_ij (l.373) records no convention, and Sect. 7.1 is not yet written. Add the convention to the NOTATION row (pairs once, J > 0 AFM, spins of length |S|).
  Sect. 7.1 and worked example 7.2 (NiO magnon velocity) must then use ω = |S|[J(Q)−J(0)] (FM) and the corresponding AFM form, or the factor-2 error above will reappear there.

## E.10 Defects
- Eq. (E.10-form): signs with n_s > 0 for added atoms, μ_ch from the VBM → CHECKED. It matches Kim et al. Eq. (3) up to their sign of n_i.
- Eq. (E.10-level): A_z + zμ = A_z′ + z′μ ⇒ μ = (A_z−A_z′)/(z′−z) → CHECKED.
- Eq. (E.10-mp): HL units e² = 4πα; Makov–Payne q²α_M/(2εL); α_M = 2.8373 (Komsa Sect. II; Kim l.232) → CHECKED. Dimensions eV → CHECKED.
  ε₀ = ε∞ = 11.7 in Si (nonpolar) → CHECKED against the book-wide ruling.
- l.23 HSE Si gap 1.114 eV (Dhaliah) → CHECKED.
- l.36 NV: 1.757/2.035/1.945 eV, 512 sites (Alkauskas Sect. 4.1) → CHECKED.
  T center: 985 vs 935 meV, (0/−1) at 1.07 eV, 1.3–5 μs vs 0.9 μs (Dhaliah) → CHECKED.
- l.38 S_HR = Σω_kΔQ_k²/2 (ħ=1) → CHECKED. 3.02 vs 3.67 ("20 % smaller" in the source; actually 17.7 %); 10 648 sites; measured 3.85 ± 0.05 → CHECKED.
- l.44 GAP (cross-section): "trajectory … about 10 ps" matches Kadribasic 2018 ("simulated for 10 ps"), but E.11 l.79 quotes 20 ps (Sassi Table I). Both are correct for their sources. Attribute each to its study, or E.10 reads as contradicting E.11.
- l.46 E_d 17.5–63.5 eV (Kadribasic), min 18 eV, ~5 eV stored (Sassi Table II, Sect. III) → CHECKED.
- Eq. (E.10-ohm) and l.52 WRONG/GAP (factor-2 conventions). Maillet Eq. (4): τ⁻¹ = 4πKΔ₀²/(ħε) coth, K = (n₀VΩ)². The spin-boson golden rule gives Γ = παΔ₀²/ε coth, so α = 4K → CHECKED.
  - But α = 4K holds only if the TLS couples as σ_z·V, i.e. the two configurations have potentials ±V and differ by 2V. With V_d "the change of the contact potential between the configurations" (l.52), the same golden rule gives α_ohm = K_b.
  - Similarly: S = e^{2iδ}, so the eigenphases of S_R S_L† are 2Δδ, while Anderson's exponent is (Δδ/π)².
  - Born: Δδ = πN_F ΔV Ω. The stated δ̃ = 2πN_F V_d Ω and α = (1/2π²)Σδ̃² are consistent with α = 4K_b only if δ̃ is the phase-shift difference (S_R S_L† = e^{2iδ̃}) and V_d the half-difference.
  - Correction: define "eigenvalues e^{2iδ̃_ν} of S_R S_L†" and "V_d the half-difference of the contact potentials (configurations at ±V_d)", keeping α = 4K_b. Or keep the current words and write α_ohm = K_b and δ̃ = πN_F V_d Ω.
  - Propagate the same choice to the NOTATION row α_ohm, K_b (16.8) and to Sect. 16.8.
  - Anderson t^{−(δ/π)²} vs ohmic t^{−2α} (Leggett) → CHECKED.
- we:E-sidefect: 0.161, 0.107, 0.080 eV for n = 2, 3, 4 (64, 216, 512 atoms) → CHECKED. αħc = 14.40 eV Å → CHECKED. 1/L ∝ N^{−1/3}, ×8 atoms to halve → CHECKED. 80 > 50 meV → CHECKED.

## E.11 Molecular dynamics and learned potentials
- l.3 and l.77 speed at 100 eV: (2E/M)^{1/2} = 26.2 km/s = 0.262 Å/fs; at 1 keV 0.829 Å/fs → CHECKED. 0.05 Å steps: 0.19 and 0.060 fs → CHECKED.
- Eq. (E.11-zbl): a_U = 0.8854a₀/(2·14^{0.23}) = 0.1277 Å; Z²αħc = 2822 eV Å; V(1.0) = 51.0 eV, V(1.5) = 9.61 eV → CHECKED.
- r_min table, solving V(r) = E_R/2: 1.487, 1.201, 1.005, 0.828, 0.489, 0.179 Å → CHECKED for all six entries and in tab:E.11-si.
- l.44 kT at 2000 K = 0.172 eV; e^{−51/0.17} → CHECKED.
- l.42 Bartók Table I: 2475 cells, 171 815 environments, PW91, 250 eV → CHECKED. 5 Å cutoff → CHECKED.
  Defects within 7 % (Sect. III E) → CHECKED. 100 ms/atom → CHECKED (Bartók, concluding section; the location "Sect. V" should be checked).
  Hexagonal/tetrahedral interstitial ordering preserved, energy difference underestimated → CHECKED.
- l.77 1 fs ≈ 1/67 of the 15 THz period (66.7 fs) → CHECKED.
- l.79 Sassi Table I: 8×8×8 conventional cells = 4096 atoms, 6 Å border (40 mK), 20 ps, adaptive step; >5 ps tests, within 1 eV → CHECKED. 8a = 4.34 nm → CHECKED.
- l.85 binomial error max (0.25/1000)^{1/2} = 0.0158 → CHECKED. Si 18 eV, Ge 13 eV (Table II) → CHECKED.
- l.89 equipartition: E_pot = (3/2)Nk_BT; 1.5·4096·8.617×10⁻⁵ = 0.529 eV → CHECKED.
- l.102 k_BT at 10 mK = 0.862 μeV; 0.1 eV gives e^{−1.16×10⁵} → CHECKED.
- l.108 cost: 410 s/step; 8.2×10⁶ core-s = 2.3×10³ core-h; 2×10⁴ trajectories → 4.6×10⁷ core-h.
  The text says "4×10⁷" here and at l.140. Order of magnitude is OK; "5×10⁷" would round correctly.
- Typography (STYLE Γ rule): l.102 TST rate written \Gamma, \Gamma_0 → should be \varGamma.

## E.12 Phonon and charge transport Monte Carlo
- Eq. (E.12-iso) B_iso = 4π³gΩ_at/⟨c³⟩: the derivation from the Tamura/Klemens rate τ⁻¹ = (V₀g/4π)ω⁴⟨c⁻³⟩ gives B = 4π³gΩ_at⟨c⁻³⟩ → CHECKED.
  The arithmetic 124.0·2.02×10⁻⁴·2.00×10⁻²⁹/2.13×10¹¹ = 2.35×10⁻⁴² s³ → CHECKED. It matches Hernández Table 4 (2.33) and Leman Table I (2.43).
- l.26 GAP: "⟨c³⟩ a polarization average of the cubed sound speed". The number 2.13×10¹¹ m³ s⁻³ is ⟨c⁻³⟩⁻¹ = [(c_L⁻³ + 2c_T⁻³)/3]⁻¹ with 9.0 and 5.4 km/s, which gives 2.132×10¹¹. The plain average ⟨c³⟩ would be 3.48×10¹¹.
  Correction: write B_iso = 4π³gΩ_at⟨c⁻³⟩, with ⟨c⁻³⟩ = (1/3)Σ_s c_s⁻³ (= 1/2.13×10¹¹ s³ m⁻³). Also check the NOTATION row if one is proposed.
- tab:E.12-rates, all rows: Γ_iso 1.52×10⁵, 2.43×10⁶, 1.97×10⁸, 2.43×10¹⁰; mfp 3.56 cm, 2.22 mm, 27.4 μm, 0.222 μm; Γ_anh 2.32×10³, 7.41×10⁴, 1.80×10⁷, 7.41×10⁹; E_ph 2.07, 4.14, 12.4, 41.4 meV → CHECKED.
- l.16 1 THz ratio 3.9×10⁻⁷; 15 THz 1.3×10⁻³ (~10⁻³); λ = 5.4 nm; mfp/λ = 4.1×10⁵ → CHECKED.
- l.35 A/B → 32.8 THz ("33") → CHECKED. 10 THz: 0.135 ns; 3 THz: 55.5 ns and 11 isotope events; 1 THz: 13.5 μs (>10 μs) → CHECKED. Factor 1.15/0.741 = 1.55 → CHECKED.
- l.26 branch populations 55/35/10 (Leman Sect. III E) → CHECKED. A = 7.41×10⁻⁵⁶ s⁴ (Leman Table I), 1.15×10⁻⁵⁵ (Hernández Table 3) → CHECKED.
- l.61 P_escape = exp(−4d/λ) (G4CMP Eq. (17)) → CHECKED. The ⟨1/cos θ⟩ = 2 justification under cos-weighted flux → CHECKED.
- Eq. (E.12-luke) = G4CMP Eq. (8). l₀ = πρ/(2m³D²) in natural units [eV⁻¹ = length], rate [eV] → CHECKED dimensionally.
- l.73 Herring–Vogt, 3/m_c = 1/m∥ + 2/m⊥ → CHECKED.
- l.77 and l.93: 100 eV/2 meV = 5×10⁴ (G4CMP Sect. 3.4, "2 meV per phonon") → CHECKED. 10 keV/4.14 meV = 2.42×10⁶ → CHECKED. "CPU day … an hour per event" (G4CMP) → CHECKED.
- l.83 binomial error of a fraction → CHECKED.
- Typography: Γ_iso, Γ_anh (NOTATION row 11.6 says italic \varGamma) and Γ_L are written \Gamma → \varGamma.

## E.13 Hot-carrier cascades
- l.3 50 eV/3.75 eV = 13.3 pairs; 50 − 13·1.17 = 34.8 eV → CHECKED.
- Eq. (E.13-moments) → CHECKED. l.17 ħΓ = 0.0658 eV at 10¹⁴ s⁻¹ → CHECKED.
- l.21 QSGW 1.23 eV without SOC (Kotani Table I: "1.23(1.11)") → CHECKED. Within 0.2 eV → CHECKED.
- l.23 band counts with Ω = 40.0 Å³: 8.1, 32.2, 90.9 → "8, 32, 90" → CHECKED.
- Eq. (E.13-imsigma) (Kotani Eqs. (1)–(2)), Γ = 2z_qp|ImΣ| → CHECKED.
- l.36 z_qp ≈ 0.8, RESOLVED (editor note): Kotani et al. 2010, Sect. II states "Typically Z_kn is ∼0.8". Add \cite[Sect.~II]{kotani2010impact}; no new bib entry is needed. Plasmon 16.6 eV (Ramanathan Table I) → CHECKED.
- l.38 Kane |M|² = ½(|M_D|²+|M_E|²+|M_D−M_E|²) (Kotani Eq. (5)); factors 0.5–1 and "0.75 at most" (Sect. II) → CHECKED.
- Eq. (E.13-gph) emission/absorption weights → CHECKED.
- Eq. (E.13-ab) = Ramanathan Eq. (8) (ratio A(105/2π)(E−ω₀)^{1/2}/(E−E_g)^{7/2}) → CHECKED as transcription.
  GAP (dimensions): with A_AB in eV² the right side has dimension eV⁻¹. The inconsistency is inherited from the source (A = 5.2 eV², Table I).
  State "with E in eV and A_AB = 5.2 (in the units of Ref.)", or give A_AB in eV³ so that the ratio is dimensionless. The fit formulas (12)–(13) then use the same number.
- l.69 P_ii = 0.0527, 0.363, 0.773, 0.882 at 3, 5, 8, 10 eV; crossing at 5.76 eV ("about 6") → CHECKED.
- l.71 fits (Ramanathan Eqs. (12)–(13)): E_g(123 K) = 1.1692 − 4.9×10⁻⁴·123²/(123+655) = 1.1597 → "1.160" (Eq. (11)) → CHECKED.
  ε_eh = 3.709, F = 0.1153 → CHECKED.
  Rodrigues et al.: 3.749 ± 0.001 eV, 0.119 ± 0.002 at 123 K and 5.9 keV → CHECKED. 1.0 %, 2σ → CHECKED.
- l.75 1728 k points, factor ~2 below 10¹⁰ s⁻¹ (Kotani, Fig. 2 caption) → CHECKED.
- l.77 the variance relative error (2/N)^{1/2}; 0.002/0.119 = 1.68 %; N = 7.08×10³ → CHECKED. The mean error [F/(⟨N⟩N_casc)]^{1/2} → CHECKED.
- l.81 cost
  - 2k_E(50 eV) = 7.25 Å⁻¹; N_G = 257; 29 irreducible points of 8³ fcc (brute-force O_h count: 29) → CHECKED.
  - 29·260²·200·16 B = 6.27 GB → CHECKED. 100 eV: N_G = 728, ratio² = 8.0 → CHECKED.
  - 1728²·30² = 2.7×10⁹ → CHECKED.
  - 5 keV: 1333 pairs, ~5.5×10⁴ phonon events, 10⁴ cascades ≈ 5.6×10⁸ events → CHECKED.
- l.85 1.17 vs 1.12 eV (Ramanathan Table I) → CHECKED.
- tab:E.13-si: every entry matches the text → CHECKED.
- Typography: Γ_ii, Γ_ph, Γ_tot, Γ_max and ħΓ are written \Gamma → \varGamma.

## Cross-section silicon constants
- Gap 1.17 eV at low T: E.7, E.8, E.13 → consistent. 1.160 eV at 123 K and 1.12 eV at 300 K are labelled as such.
- ε∞ = 11.7: E.10 only (ε₀ = ε∞ = 11.7) → consistent with the ruling. PBE 13.04 does not appear in E.7–E.13.
- a = 5.431 Å, Ω = 40.05 Å³ (40.0 in E.13), Ω_at = 20.0 Å³ → consistent.
- Kohn–Sham gap: E.7 l.130 "0.6 eV" is correct as a PBE number but cited to an LDA table (see above). E.13 l.21 "about half the measured" → consistent with E.1 (0.602).

## Citation-audit notes (editor item: arXiv-only entries)
- kim2020quickstart (@misc, arXiv:2005.01941) appears to have a journal version (J. Phys.: Energy, 2020). Verify and add the journal reference.
- komsa2009comparison (@misc, arXiv:0906.1283): no journal version found. Keep as arXiv-only, or replace with Komsa, Rantala and Pasquarello, PRB 86, 045112 (2012), if that paper carries α_M and the comparison used.

## Cited but not verified against the source text (physics redone where applicable)
- Not fetched: Kumagai–Oba (arXiv:1402.1226: Gaussian model, alignment contained in the image-charge term); Holmström 2008; Tamura 1983/1985; Bunge 1993; Kane 1967; Fischetti–Laux 1988; Jacoboni–Reggiani 1983; Bernardi 2014; Swartz–Pohl 1989; Martinez 2019 (0.3–0.55); Kaplan 1976; Herring–Vogt 1956; Ziegler–Biersack–Littmark (ZBL coefficients used as printed); Stillinger–Weber 1985; Hellman 2013; kadribasic2020 (1003 directions); Anderson 1967; Hybertsen–Louie 1986; Blöchl 1994.
- Fetched but these passages not inspected: Hellman 2011, Fig. 1; Leman 2012, Eqs. (7)–(9) and Sects. V C–D (energy-preserving back-transform, half-mean-free-time step); Griffin Sects. 2.3/3.4 (Coulomb factor on plane-wave final states); Ponce 2015, Sect. III and below Eq. (16) (Sternheimer split, δ→0 extrapolation, residual Born charges); Monacelli Sect. IV (free-energy Hessian); Zacharias 2016 Sect. II (Monte Carlo samples, first-nonzero-component rule, seen only in part); Lee 2023 Sect. 4 (sparse sampling, energy window).
