# Ch14 part 2 (14.4–14.6): derivation check

Reviewer: derivation verifier (isolated). Files: tex/ch14/ch14.tex, s14-4.tex, s14-5.tex, s14-6.tex.

Sources: fetched with lit.py into sources/review-ch14/. The PDFs were converted to .txt and then deleted. The sources are 2504.02927, 2304.00048, 2301.07617, 2511.20461, 2601.01043, 2102.10171, 1711.10489, 1306.6089, 1905.13650, 2101.01241, cond-mat/0003371 and cond-mat/0302052. Abragam & Bleaney, Fernandez et al. 1998, Lovesey Vol. 2 and Blume 1963 could not be opened.

Tools: sympy (scratchpad symchk.py); numpy against the cached IFCs and the coh14 functions. I ran no QE job and wrote no figscripts log.

Verdicts: CHECKED means the step was redone and agrees. WRONG means it must change. GAP means it is incomplete or unsupported, with a fix given.

## Priority items (verdicts)

| Item | Verdict |
|---|---|
| Neutron no-go (q̂·S·q̂ unreachable) | CHECKED for the exact response. **GAP** inside the localized-moment model that 14.4 itself uses (item 4.4 below). |
| C_sn(q, g) for Ni²⁺: 0.83, not 1.19 | CHECKED |
| S^z_tot zero of R_{s^z𝒥}(0, ω≠0) | CHECKED. Minor wording fix, item 5.7. |
| Enantiomer difference eq:14.5-enant | CHECKED (sympy) |
| GaAs ⟨\|L^ph\|⟩ 0.124 vs 0.07 | 0.124 CHECKED. Cause **not identified**, but the candidates were narrowed (item 5.2). "Factor-two dependence on force constants" is unsupported. |
| Alves et al. absorption-trigger claim | CHECKED for halo (nonrelativistic) DM. Wording fix, item 5.5. |
| Coherent-field formulas (Bloch, Rabi, ms average, Fejér) | CHECKED |
| t_coh convention | CHECKED in 14.6. Drift in E.26, 11.8 and 8.2 (item 6.6). |
| Gaussian-field spectrum | CHECKED |
| 1.99 vs 2.7–10 | CHECKED, independently reproduced, including 2.73 at the detection threshold (item 6.4) |
| Nuisance rows of 14.4/14.5 | Consistent with the sections. Computed 14.5 items are missing (item 6.9). |
| CORRECTIONS / SOTA | One superseded value used (YIG a = 12.56 Å inside q_1BZ = 987 eV, item 4.2). Everything else agrees (SOTA: Var N, min(t_coh, 1/Γ_T), CASPEr half-width, per-level amplitude, penalty not double-applied). |
| DC-RESULTS / returns/R18 | Nothing bears on 14.4–14.6. DC-37/46/84 are not in the table ("to write"). |

## 14.4 Spin responses from neutron data
### CHECKED
- l.3, kinematics: p_n(120 meV) = 15017 eV; m = p_n/v_max = 5.67 MeV; ½mv_max² = 19.9 eV.
- l.9 eq:14.4-PT. Dividing eq:C.19-cross by V N_fu/Ω gives Tr[P_T S] = 2πN_fu S^neu/((γ_n r_cl)²Ω). This equals Berlin Eq. (26) with χ'' = 2(1 − e^{−βω})S.
- l.12: (γ_n r_cl)² = (1.913 × 2.8179 fm)² = 0.2906 b. Also e⁴/[8m_e²(2π)³] = r_cl²/4π.
- l.14–17: the thermal correction (1 − e^{−βω})S is T-independent for free bosons.
- l.20–24: moment 2S j₀ + (g−2)S(j₀+j₂) = gS[j₀ + (1 − 2/g)j₂] (sympy). This is consistent with C.19's (2/g_J − 1) for J multiplets, since L = (2 − g_J)J there.
- l.27–31 eq:14.4-data: C_sn(0) = [λ_S/(g/2)]².
- l.33: Gd 1, Er 1/9, Sm 25 (Hund's rules).
- l.35–39, recomputed from the Brown coefficients:
  - 4/2.2² = 0.8264; λ_S = g − 1 gives (1.2/1.1)² = 1.190; the ratio of the two is 1.44, consistent with the 14.3 nuisance row.
  - |Q_AF| = (2π/a)(√3/2) = 2.575 keV; 2·(1 MeV)·v_max = 5.300 keV.
  - j₂/j₀ = 0.0352 and 0.1523.
  - C(q)/C(0) = 0.9936 and 0.9729; within 10 % of C(0) for q < 10.2 keV.
  - g = 2.34: C(0) = 0.7305, 0.884 of the g = 2.2 value.
  - Fig. caption gray band: g − 2 ≤ 0.0939.
- l.39 sources: Kwon & Min give L/S = 0.36 (DFT+U) and quote 0.34 for magnetic x-ray scattering. Their L/S is an angular-momentum ratio, so g = 2 + L/S = 2.34 is the right reading.
- l.53:
  - Berlin App. D gives MAPS detector coverage 3–60°, 5 meV resolution and rotation about one axis.
  - Berlin Fig. 3 shows agreement near 1 MeV; the Fe³⁺ form factor suppresses by an order of magnitude at q ≳ 10 keV.
  - Phonon weight (q/30 keV)²: q²/(Mω) = 1 at q = 31.6 keV for M = 50 GeV, ω = 20 meV.
- l.57: D tensors.
  - O₉: Tr_χ[(q×S_χ)_a(q×S_χ)_b]/2 = q²(P_T)_ab/4 (sympy).
  - O₄: δ/4. O₁₀: q_aq_b/m_e². O₆: q²q_aq_b/4m_e⁴.
- l.59 eq:14.4-split; l.64 Berlin Eqs. (15), (17) longitudinal; footnote 3 (permeability).
- l.68–76, perpendicular projection: at most 4 of 9 real numbers. The point-group argument is correct, including the transpose for antiunitary elements.
- l.89–95 eq:14.4-uniax (sympy): Tr[P_T S] = S∥sin²θ + S⊥(1+cos²θ); q̂·S·q̂ = S∥cos²θ + S⊥sin²θ; S_yy and S_zz as printed.
- l.99 eq:14.4-invert (sympy).
- l.104: Berlin Eqs. (35)–(37) reproduced with S∥ = S⊥ and with S∥ = 0.
- WE 14.4 (sympy): S∥ = P₁ − P₂/2; σ = 0.112 S₀; S⊥ 0.050 S₀; P₁/3 + P₂/6 with 3.7 %; 0.141 S₀; c₂ = 0.25 gives 2.5P₁ − 2P₂ and 0.320 S₀.
- l.97: YIG sphere saturates at μ₀M_s/3 = 82.0 mT.
### WRONG / GAP
4.1. **GAP, l.12.** The reason given for the factor 2 is incomplete. σ in place of σ/2 gives a factor 4. Berlin's normalization (π/V)Σ(p_e − p_e′) in Eq. (8)/(B4), against our (2π/V)Σp_i, gives ½. The product is χ''_B = 2(1 − e^{−βω})S. Fix: "the factor 2 = 4 × ½: their spin operator is σ (×4) and their χ'' carries π/V where S_ab carries 2π/V." C.19 l.26 has the same one-cause wording.

4.2. **WRONG/GAP, l.53, superseded value.** q_1BZ = 987 eV is Berlin's number and equals 2π/a with a = 12.56 Å. DATA-ADDENDA supersedes that value with 12.375 Å (2π/a = 1002 eV).
- 2π/a is the distance to the H corner of the bcc zone. It is neither "the edge" nor a radius inside which every q lies: the inscribed radius is π√2/a = 708 eV.
- "Below 186 keV every momentum transfer lies inside the first zone" is therefore false. It holds below 708 eV/(2v_max) = 134 keV.
- Fix: write "Berlin et al. stop the extrapolation at q_1BZ = 987 eV (2π/a for their a = 12.56 Å)". Then either drop "every" ("most of the kinematic region lies inside the first zone below about 200 keV", as Berlin say) or state 134 keV.

4.3. **GAP, l.53.** Spin-flip scattering with P ∥ q̂ excludes coherent nuclear scattering but contains 2/3 of the nuclear-spin-incoherent cross-section. So "removes the phonons without a model" holds up to the spin-incoherent phonon part, which is small for Y/Fe/O. Add "up to the spin-incoherent part".

4.4. **GAP (substantive), keyresult l.67–68, l.76, l.114, nuisance row l.209, summary l.249.** The no-go is right for the exact S_ab at one q. It is not right inside the localized-moment factorization that eq:14.4-data itself assumes, s_e(q) = F(q)Σ_j e^{iq·R_j}S_j.
- For one magnetic ion per primitive cell (NiO in its chemical cell), S_ab(k+G) = |F(|k+G|)|² e^{−2W} S^lat_ab(k).
- The transverse traces Tr S^lat − n̂_i·S^lat·n̂_i at six or more generic directions n̂_i = (k+G_i)^ fix all six components of the symmetric S^lat(k). That includes q̂·S·q̂ at the dark-matter q, and at k → 0 the tensor that absorption needs, resolution permitting. This is how neutron diffraction fixes moment directions.
- So "no data-only route" stands only in the strict sense. "Puts O₆, O₁₀ and ALP absorption out of reach of a data-driven calculation" (l.76) is too strong.
- Fix: restrict the keyresult to "at a given q, without a model of the spin density within the cell". Add the G-shift route as a third information route next to the isotropy hypothesis and the model fit, with its hypothesis (dipole-approximation form factor, known magnetic basis). Qualify the nuisance row the same way.

4.5. **GAP, l.87 and l.97.** "Only spin–orbit coupling breaks the hypothesis" is incomplete. The magnetic dipolar interaction also breaks spin-rotation invariance: the spin-wave term ω_M sin²θ_q depends on θ between q and m at fixed |q|. For YIG it is negligible at ω ≫ ω_M = 28.5 μeV (the data start at 5 meV). Add "and the dipolar interaction, negligible above ~0.1 meV in YIG".

4.6. **Notation drift.**
- Bare g is the spectroscopic g factor at l.20–39. NOTATION reserves bare g (entry 20: e–ph vertex; the g_J row says "subscript mandatory").
- l.72 reuses g for a point-group element.
- 14.5 uses g for the gyration tensor (the g_ml row of C.17 is fine).
- Fix: give the spectroscopic g a symbol and a row (e.g. g_s), and call the group element 𝗀 or R.
- The NOTATION λ_S row still reads "spin–lattice factor" (known item, still open).

4.7. Citations not verifiable offline: Abragam g ≈ 2.2; Fernandez 0.34 (only as quoted by Kwon & Min); Lovesey; Blume. These are known items, unchanged.

## 14.5 Chiral and nonreciprocal targets
### CHECKED
- l.7–15 eq:14.5-recip, rederived:
  - T: S_ab(q)* = σ^T_aσ^T_b S_ab(−q), then S_ab* = S_ba.
  - P: unitary.
  - Signs σ^T, σ^P for n, 𝒯, j, s, 𝒥 as printed.
- l.17–22: G_OA is odd under T and even under P. For opposite-T rows the symmetric part is odd in q; with σ^Pσ^P = −1 the block vanishes at q = 0. Table tab:14-odd agrees.
- l.43–47 (sympy): G_OA = −2 Im G_R/(1 − e^{−βω}), then eq:14.5-gyr.
- l.50–61 eq:14.5-helicity (sympy):
  - ê*±×ê± = ±iq̂; S± = S_T ∓ q̂·G.
  - The dissymmetry equals q Im g/ε₂^T.
  - n± = n ∓ gω/2; ρ = ω²g/2 (Zabalo Eq. (4), with c = 1).
  - Absorption coefficients differ by 2ω² Im g.
- Numbers:
  - ρ(2.105 eV) = 0.3764 rad/mm = 21.56°/mm.
  - q g₃₃ = 7.06×10⁻⁵ at the vacuum photon momentum and 0.0335 at 1 keV.
  - 1/v_max = 377.
  - Zabalo Table I: g₁₁ = −0.071 and g₃₃ = 0.125 bohr.
  - Orientation average −0.0057 bohr, −0.045 of g₃₃.
- WE 14.5: point group 32 counts 0 (ℓ = 1), 1 (ℓ = 3; characters 7, 1, −1), N_gyr = 2, g = diag(g₁₁, g₁₁, g₃₃). Td gives N_gyr = (9 + 0 + 3 − 6 − 6)/24 = 0.
- l.72–76 (sympy, with eq:8.1-D = ½Tr V_a†V_b and Σ_ab D_ab S_ab):
  - Interference D = −(i/2m_e)Re(c₅*c₈)ε_αβγq^γ.
  - Contraction (1/m_e)Re(c₅*c₈) q·G.
  - R − L doubles it, giving 1/2π² with the η/2q kernel of eq:A.8-eta.
  - The ratio to ½|c₈|²S_T is as printed.
- l.85: O₅ is P-even and O₈ is P-odd.
- l.102–105: L^ph of circular motion = 1; |L| ≤ 1; L(−Q) = −L(Q).
- l.116 (sympy): [H, L_z] = (i/2)u·[J_z, D]u.
- l.114: μ_N bound Z*m_p/M_Ga = 2.094 × 1.00728/69.723 = 0.0303. A mode with opposite sublattice L stays below it. The log gives a lowest-band maximum of 0.0150.
- l.116 sources:
  - Matas: κ = ⟨‖J₁‖⟩/ħ = 0.07, 0.22, 0.16; one phonon at random in the lowest band; MP dynamical matrix; 10³ grid.
  - Romao: κ = 0.15.
- l.120–140, Mn₁₂ (sympy + numeric):
  - 0.454 cm⁻¹ = 0.05629 meV; B₄⁰ = −2.48×10⁻⁶ meV (Edwards: D = −0.454 in the +DS_z² convention, so signs are consistent).
  - Quartic shift −58140 B₄⁰ = +0.144 meV.
  - Zero-field line 1.2137 meV; ω_meta(1 T) = 1.0979 meV = 12.74 K; next line 0.181 meV lower.
  - Barrier top m = −1 at 4.595 meV (53.3 K).
  - Line weight 2|S|. The sum rule Σ(p_m − p_{m+1})c_m = −2⟨S_z⟩ (sympy).
  - eq:14.5-smm prefactor π n λ²/2.
  - 90 % for ω/T ≥ 3.02, i.e. T ≤ 4.22 K.
- l.142: rate (ρ/mρ_T)ζ²α equals Alves Eqs. (9), (10), (17); the ratio to ζ²σ₁/|ε|² is n_r/|ε|². ζ = gB₀/m matches Alves Eq. (13).
- l.159–164: −iσ·∇/2m_e = Σp·S/m_e. The coupling is (g/m_e)(∂_tφ)𝒥, giving eq:14.5-cross with the eq:4.1-kubo sign convention.
- Lehmann form rederived from eq:4.1-kubo.
- l.166, S^z_tot zero: if [H, S^z_tot] = 0 and s^z = λS^z_tot, the matrix elements of s^z connect only degenerate levels, where p_i = p_n. So R ≡ 0 at ω ≠ 0 (and in the Kubo sense at ω = 0). T at q = 0 forces imaginary products, so R is odd in ω and the ω → 0 part needs T broken.
- l.173 / lim 14.5b against the log: Landau C/2(T_CM − T); 0.944; 0.369; Landau/SW 1.42 (0.3) and 4.45 (0.1); J|S| = 0.1429 T_CM is the mean-field relation for z = 6.
- l.144 / lim 14.5a(a) against the log: 0.124 (20³ shifted). Rate-weighted lowest band 0.112 within 10 % for m ≥ 2.19 MeV, where it carries 29–30 % of the rate. The lowest band has ≥ 1 % of the rate only from 0.784 MeV.
- Si control: |L| = 1.4×10⁻⁷ < 2×10⁻⁷.
### WRONG / GAP
5.1. **WRONG, l.144.** "All created phonons together carry less than 0.03 below 0.23 MeV." The log gives 0.0331 at 0.228 MeV and 0.0268 at 0.185 MeV, so 0.03 is crossed at about 0.21 MeV. Fix: "less than 0.03 below 0.2 MeV".

5.2. **GAP, l.144 ("so the estimate depends on the force constants at the factor-two level") and the 0.124 vs 0.07 cause.** Tests from the cached PBE IFCs (gaas_ifc14, scratchpad lph.py and lph2.py; lowest-band ⟨|L|⟩):

| Test | ⟨\|L\|⟩ |
|---|---|
| Grid 10³ Γ-centred / shifted (Matas' grid) | 0.126 / 0.118, so not the grid |
| Equal Ga/As masses | 0.115; swapped 0.112, so not the masses (the chirality comes from force-constant asymmetry) |
| Energy-weighted / 1/ω-weighted average | 0.135 / 0.117, so not the weighting |
| Long-range dipole sum ×0, ×0.5, ×1.5 | 0.175, 0.146, 0.107; reaching 0.07 would need it ×≳2.5 |
| Displacement-normalized (non-mass-weighted) vectors | 0.113 |
| Average of one Cartesian component, ⟨\|L_x\|⟩ | 0.062, the only simple variant near 0.07 |

So the force-constant dependence shown is ±40 %, not a factor two. Matas define ‖J₁‖ as a norm, but their J is plotted by components, and an average of one component is a hypothesis I could not verify. Fix: replace the clause with "the cause is not identified. A different grid, the mass ratio and the weighting are excluded, and the result moves by ±40 % when the long-range dipole part is varied. A single Cartesian component gives 0.062." Keep both numbers printed.

5.3. **Drift, l.114.** Z* = ±2.09 is the PBE DFPT value of the 5.5 run. The book value is Z* = 2.11 (App. E pass 2, Ch11). Label it "PBE, Sect. 5.5". The printed 0.015 and 0.030 μ_N do not change.

5.4. **GAP, l.125.** Alves Eq. (3) is only H ⊃ −DS_z². The quartic O₄⁰ and its coefficient are Edwards'. Move "[Eq. (3)]{alves}" to the −DS_z² term and cite Edwards for O₄⁰.

5.5. **GAP, l.142 (Alves claim).** The claim is true for halo dark matter: absorption deposits ω ≃ m_φ, so the trigger is a condition on m_φ. "Whatever the speed" is too broad, because a relativistic (boosted) boson deposits its total energy γm_φ. Alves (Results, Eq. (18)) scale even the absorption rate by the boosted fraction f, arguing that the deposit is ~10⁻⁷–10⁻⁶ eV. That is the kinetic energy of scattering, not of absorption. Fix: say "for any nonrelativistic speed", and add one clause: "so their boosted fraction f does not apply to absorption. For m_φ ≥ 10⁻² eV halo absorption triggers with f = 1; below it halo absorption cannot trigger, and a boosted population needs its own energy spectrum."

5.6. **GAP, l.159.** The 10.5 μC cm⁻² and 0.02 μ_B/Fe of Røising Sect. IV A are DFT values for hexagonal LuFeO₃ (x = 0), not for Lu₁₋ₓScₓFeO₃ with x ≈ 0.4. Say so.

5.7. **Minor, l.166.**
- "The response is therefore of second order in spin–orbit coupling" should read "at least second order": the vertex needs an odd crystal field and SOC, and S^z breaking is first order (DM) or second order (single-ion term).
- ω_M of eq:14.5-GL still clashes with 14.3's ω_M = 2μ_Bμ₀M_s (open editor note). Rename it, e.g. ω_mag.

5.8. **GAP, lim:14.5b caption.** The exchange is fixed by the mean-field relation T_CM = zJ|S|(|S|+1)/3. The actual Curie point of that simple-cubic S = 5/2 model is ≈0.72 T_CM, so the axis is in mean-field units. State this in the caption, since the 0.37 and 0.94 marks depend on it.

## 14.6 Coherent fields and precessing nuclear spins
### CHECKED
- l.3 and l.174:
  - 1 neV corresponds to 241.80 kHz; ²⁰⁷Pb at 26.77 mT.
  - γ/2π = 2 × 0.5926 × 7.6226 = 9.034 MHz/T (Aybas Eq. (S11)).
- l.7: quanta 4.61×10³⁹ (ρ_χ = 0.3 GeV cm⁻³, NOTATION).
- l.9–16 eq:14.6-Sphi: Fourier transform with eq:A.3 signs. The prefactor (2π)⁴/2 = π(2π)³. Positive frequency at k = −m v, and the target receives +m v.
- l.21: line edge v_max²/2 = 3.512×10⁻⁶.
- l.25: t_coh = 1.0444 s; the 2π convention gives 6.56 s; 1/(m v₀) = 249 km.
- l.28, line statistics (independent quadrature, scratchpad line.py): peak 0.5784/t_coh; mean 1.2671; Δω_eq = 2.6747; |C| = ½ at 1.46 t_coh (log 1.465, prints 1.47); halo rest frame [1 + (t/2t_coh)²]^{−3/4}.
- l.30–38 eq:14.6-fejer: |∫e^{iΔt′}|² = 2πt 𝒦_t and ∫𝒦_t = 1 (sympy). The golden-rule condition t ≫ min(t_coh, 1/Γ_T) agrees with SOTA.
- l.41: Var N = N̄ + N̄²/N_coh; 3600 s/1.044×10⁻⁴ s = 3.45×10⁷; 35 h⁻¹ (we14_3.log, which uses a = 12.375 Å, so not superseded).
- l.45: dJ/dt = J × b.
- l.47:
  - ω_Lar(4.4 T) = 0.1644 μeV; p = tanh(ω/2T) = 2.27×10⁻⁴.
  - μ₀M₀ = 2.90 nT; n = 3.4×10²⁷ m⁻³ (S12).
  - T₂ = 16.7 ms and Γ/2π = 78 kHz (Aybas); E* = 340 kV/cm ± 50 % (Aybas).
- l.56–58: R_{J−J−} = 2⟨J_z⟩/V/(ω − ω_Lar + i/T₂) from eq:4.1-kubo; Im R < 0 if ⟨J_z⟩ > 0.
- l.64–72:
  - b_φ = −(g/m_N)√(2ρ) v sin(mt).
  - Ω = b⊥/2; gradient form g√(2ρ)v⊥/2m_N; dipole form Ω = Δε with b = 2Δε.
  - Rotating-frame equation rederived, keeping the co-rotating ½.
- eq:14.6-mperp (sympy dsolve): both limits as printed.
- l.88: Budker envelope sin(δt)/δ, half as wide (SOTA confirmed). u_sp = π/(2π·78 kHz·16.7 ms) = 3.84×10⁻⁴ (S22–S25).
- eq:14.6-ms limits (sympy): ∫4sin²(Δt/2)/Δ² = 2πt; ∫1/(Δ² + T₂⁻²) = πT₂. The saturated rms/fixed is √(πF_pk/T₂) asymptotically; log 0.387 at T₂ = 10 t_coh; 1.58 t_coh; 0.6 %.
- l.107:
  - M₀ sin Ωt, fraction (Ωt)²/6.
  - Saturation M_z = M₀/(1 + Ω²T₁T₂) (sympy).
  - 30 % at Ω = 0.23 rad/s (Aybas Suppl.).
  - coth = 1/p, so the spin noise is independent of p (Budker App. A text).
- l.117–122: the periodogram mean is S ∗ 𝒦_t. Exponential bins. FRS Eq. (29) likelihood.
- l.139, lim 14.6b: t/(2πF_pk) at small t; leakage coefficient 1.2505 (independent); 13.3 t_coh; T₂ = t_coh → 6.49; T₂ = 0.1 t_coh → 1.0.
- l.147–157:
  - 𝗍 ≈ Σx² (sympy).
  - S_sig = 2πσ²F gives 𝗍 = 2πt_int σ⁴/(Δω_eq S_n²).
  - Both scalings of eq:14.6-scaling.
  - Budker (A7), (A8) exist.
- l.159 / l.171, independent Neyman construction (scratchpad neyman.py):
  - Median null data: s_up/b = 12.513 (Rayleigh), 3.166 (fixed); ratio √ = 1.988.
  - **Data at Centers' detection threshold (P/b = ln 20): 57.40 and 7.72, ratio 2.727.** This reproduces their frequentist 2.7, so the text's explanation is right.
  - Centers: 3.0 (Eq. (7)), 2.7, up to 10, 8.4.
  - Asymptotes meet at 135.9 and 8.70; long-record coefficient 1.0360.
- l.171 / lim 14.6c / WE 14.6, recomputed with the coh14 functions (scratchpad l6c.py):
  - Ratio 1.758 at t_coh and 1.015 at 100 t_coh.
  - Steepest slope −0.674 at 1.47 t_coh; −3/8 at 23.2 and 5.37 t_coh; bands t ≤ 1.0 and t ≥ 100 t_coh.
  - we14_6.log: 3.46, 2.24, 2.21, 82730, 3447, 1.99, < 0.1 %.
  - Δω_eq/2π = 0.41 Hz (1.7×10⁻⁶); 1/T₂ = 60 s⁻¹ against 0.958 s⁻¹ (63×).
- l.181: 1.04 ms at 1 μeV; 17 min at 1 peV.
- Dimensions: eq:14.6-Sphi, mperp, ms, scaling, 14.4-PT, 14.5-gyr, 14.5-smm and 14.5-enant are consistent (S_ab ~ energy²).
- tab:14-inputs: NiO Ω = 18.13 Å³, ρ = 6.84; YIG 947.6 Å³, 0.246 T; MnF₂ 0.0929|S|; ²⁰⁷Pb row — all match the sections.
### WRONG / GAP
6.1. **WRONG, l.47.** "μ₀M₀ = 2.9 nT, the value measured by Aybas" is wrong. 2.9 nT is their computed equilibrium value (Eq. (S13)); the magnetization they measured at initialization was (1.9 ± 0.2) nT (main text). Fix: "the equilibrium value of Aybas et al. [Eq. (S13)]; their prepared magnetization was 1.9 nT".

6.2. **GAP, l.90.** For the gradient coupling, putting ⟨v⊥²⟩ outside ∫F_φ dω ignores that v⊥² is correlated with speed, i.e. with ω. The exact form weights the line by ⟨v⊥²|v⟩: F_φ → F_φ^⊥ ∝ ∫d³v f v⊥² δ(ω − ω_v)/⟨v⊥²⟩. Call the printed form an approximation, or use F_φ^⊥.

6.3. **GAP, provenance.** figscripts/ch14/limit14_6c.log is truncated: 8 lines, stopping inside the table loop at x = 0.032. The printed 1.76, 1.015, −0.67, 23, 5.4 and the 1/100 t_coh band edges are not in it, and we14_6.log cites it for 23.3 t_coh. My recomputation agrees with every printed number. Rerun limit14_6c.py (seconds) to restore the log.

6.4. **Suggestion, l.171.** Print the 2.73 obtained from the same construction for data at the detection threshold. It turns "it is the same random amplitude, counted with a different statistic" into a demonstrated statement.

6.5. **Notation drift.**
- Γ_T (l.39, the target line width) clashes with NOTATION Γ_T (10.7: transverse dark-photon absorption rate).
- g_d (EDM coupling) collides with the local g_d of WE 8-sectors.
- 𝒢 (response kernel, l.113) is reused next to 14.5's 𝒢_OA.
- γ_n (resonator width, l.39) is the accepted ⚑ clash with 14.4's γ_n.
- Rename Γ_T, e.g. to Γ_tg.

6.6. **t_coh convention drift (outside my files; for the merge).**
- E.26 l.3: t_coh = 2π/(m v₀²) "≈ 6.6 ms", "over 1.6 km" (that is 2π/(m v₀)); line edge "3.6×10⁻⁶" (correct value 3.51×10⁻⁶); "factor 3 to 10" (book: 1.99 median, 2.7–10 at threshold). Fix: E.26 to 1/(m v₀²) = 1.04 ms and 249 m.
- s11-8 l.116: "1.05 ms at 1 μeV" should be 1.04 ms.
- s8-2 l.35 and l.81 require the record to be longer than t_coh *and* 1/Γ. 14.6 shows that the mean needs only the shorter, while a single record matches the ensemble only beyond t_coh (known editor item).

6.7. **Known items re-confirmed open:** NOTATION λ_S row wording; 14.5 ω_M clash; E.26 2π.

6.8. **Nuisance table vs 14.4.** The row "Conversion of neutron data" should add the g spread (0.83 at g = 2.2, 0.73 at 2.34, 12 %) and the q dependence (0.973 at 5.3 keV), both computed in 14.4. The row "Longitudinal spin response" needs the qualification of item 4.4.

6.9. **Nuisance table vs 14.5 (missing computed rows):**
- Chiral-phonon detection probability as a band average: within 10 % of the rate-weighted value only for m_χ ≥ 2.2 MeV; the lowest band takes < 1 % of the rate below 0.8 MeV; GaAs force-constant spread 0.124 vs 0.07 (computed/data).
- Thermal population of the Mn₁₂ upper well: 90 % of 2|S| for ω_meta/T ≥ 3.0, T ≤ 4.2 K at 1 T (computed).
- The two existing 14.5 rows agree with the text.
## Files
- Scratchpad scripts (not part of the book): /tmp/claude-0/-home-user-breakthrough-maths/30a63adb-c597-5cb8-b46c-4c5645c8b7d4/scratchpad/{symchk.py, c144.py, lph.py, lph2.py, line.py, neyman.py, l6c.py}
- Sources: campaign/paer/book/sources/review-ch14/ (txt and html only; PDFs deleted).
- No tex edited. Nothing committed.
