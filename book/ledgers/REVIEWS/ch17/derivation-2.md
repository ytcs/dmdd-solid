# Ch17 part 2 derivation check: s17-4, s17-5, s17-6, s17-summary (and ch17.tex)
Reviewer: derivation verifier (isolated). Date 2026-11-06. Tex not edited. Nothing heavy run: no QE, rank17_6.py not rerun.
Numbers come from the cached logs in figscripts/ch17 (interf17_4, fom17_5, fig17_window, pol17_5, limit17_5a, rank17_6;
fom17_5_rates.npz) and from figscripts/ch10/si_elf_binned.npz (KKL RPA+LF loss function). The algebra was checked with sympy where it was not trivial.
Sources were fetched with lit.py into sources/review-ch17/ and the PDFs deleted afterwards: 1910.10716, 2004.10709, 1110.1346,
cond-mat/0507217, 2508.08858, 1804.01033, cond-mat/9408044. Vallin 1964, Farley 1972, Franta 2017 and Henke 1993 have no arXiv copy and were not read.
Verdicts: CHECKED, WRONG (give the correction), GAP (a step or qualifier is missing).

## A. PRIORITY 1: the Ch12 tension (eq:8.3-boostward against 12.4)

**Verdict: the identity applies. 12.4 is wrong below about q_BZ for the coherent process, so a qualifier is not enough: raise a Ch12 erratum.**

1. Applicability. eq:8.3-boostward is exact as q → 0 for every final state at finite energy. It holds for zero-phonon pairs and for pairs with
   phonons alike, and it needs only pairwise interactions and the soft limit eq:8.3-soft. The DM couples to the coherent density Σ_I e^{iq·X_I},
   which is what the identity constrains. So the identity is not inapplicable. → CHECKED (identity), and it is binding at small q.
2. Mechanism. In the crystal frame of eq:12.1-amp the coherent zero-phonon amplitude is Σ_G A_G, with A_G ∝ (q·p_G) v(p_G) ρ(k, p_G) and
   p_G = q − G. That sum is (1/Mω²) q·⟨f|F(q)|0⟩, where F is the force between the electrons and the ion lattice. At q → 0 the electron–electron forces cancel,
   ⟨f|F|0⟩ = m_e ω² X_fi, and the sum collapses to (m_e/M)⟨f|n_e(q)|0⟩. The large Umklapp terms that carry 12.3-soft (median p = 5.7 keV)
   cancel among themselves. The cancellation lives entirely in the off-diagonal G ≠ G′ products. The diagonal form Σ_G|A_G|², and the
   incoherent zone average over p, do not see it. The force sum F(p₀) vanishes only near p₀ ≡ q (mod G) → 0, so a zone average over p₀ is not
   suppressed. This is also why the 12.3 off-diagonal model (×1.2–1.4, zone-averaged) does not contradict the identity.
3. Size, from the KKL RPA+LF table. The exact small-q Migdal probability per kicked nucleus is P = (m_e/M)²·(2q²/e²)(2π)⁻¹∫_{1.11}L(q,ω)dω / n_at.
   The diagonal value is 6.07e-5 E_R/eV (12.3). Both scale as q², so the ratio does not vanish as q → 0. The diagonal form is too high by:
   | q (keV) | 0.49 | 0.97 | 1.48 | 1.85 | 2.28 | 3.06 |
   | P_diag/P_exact | 14.9 | 15.3 | 16.1 | 16.8 | 17.7 | 20.2 |
   The editor's "≈16× at 2 keV" is confirmed, and the factor persists down to the lowest q allowed by kinematics (E_g/v_max = 0.44 keV). The
   shapes differ too: the exact spectrum is the loss function at q, median ω ≈ 17–19.5 eV (plasmon), whereas the diagonal spectrum has median 4.6 eV (ω⁻⁴, gap).
4. Remainder. The relative correction to the identity is of order q/(zone scale), or q·v_band/ω_f. At 0.5 keV and ω ≳ 3 eV this is ≈ 0.2–0.5. Crystal-momentum
   conservation makes zero-phonon pairs at q < k_c (1.94 keV) direct, with ω ≥ E_min(q) ≈ 3.2 eV, so the factor ≈ 15 is robust in order of magnitude
   below ≈ q_BZ. Near-gap (indirect) final states at q < k_c exist only with phonons, and eq:17.4-lock ties them to (m_e/M)²·S^PA.
5. Corrections to 12.4 (Ch12 erratum):
   - The key-result sentence "dP_Mig/dω_e is eq:12.3-soft at every q" holds for the incoherent diagonal form only. For the true response it holds only
     for q ≳ (2–3) q_BZ. Below q_BZ the correct statement is: for q ≪ 2π/a, dP_Mig/dω_e → (m_e/M)²(2q²/e²)L_tot(q,ω_e)/(2π n_at), with
     L_tot = zero-phonon + phonon-assisted electron response. That is ≈ 1/15 of eq:12.3-soft for Si (q = 0.5–2.3 keV), with the plasmon shape.
   - l.92 and l.157 ("zero-phonon line agrees with its Bragg sum within 8 %", "1.08/1.04/1.03"): this is GAP. The check used the direction-averaged L(|p|)
     and the diagonal response, which cannot test crystal-momentum conservation or the G ≠ G′ cancellation. Qualify it as "within the diagonal,
     direction-averaged approximation".
   - tab:12-nuisances and E.18: the off-diagonal size is not "≈1.2–1.4" at q < q_BZ. There it is a suppression by ≈ 15 (exact as q → 0).
   - Knock-on effects outside my files. The 17.1 Migdal crossovers at 1–3 MeV take part of their rate from q < q_BZ, and Migdal for
     m_χ ≤ q_BZ/2v_max = 0.42 MeV comes entirely from q < q_BZ. These need the same qualifier. A nuisance row should be added to tab:17-nuisances.

## B. s17-4 Interference between channels

- l.3 intro: "5.5 parts in 10⁴" → CHECKED (5.4698e-4).
- l.9 𝔇_eκ = Ṽ_e*Ṽ_κ, dark photon Ṽ_κ = −Z_κṼ, 2Re Σ𝔇S → CHECKED.
- l.11 electron-following cell. Z² : F² : −2ZF sums to (Z−F)² = Z*². Si: 196 + 196 − 392 = 0. Ga: F = 28.89, As: F = 35.11 (F = Z − Z*, Z*_Ga = +2.11).
  Cancelled 99.75 % and 99.81 %; 216 = Z²/Z*², 245 → all CHECKED (interf17_4.log).
- l.13 zero-phonon cell. m_e/M = 1.95e-5; amplitude Ṽ(1 + Zm_e/M)n_e; (1 + Zm_e/M)² − 1 = 5.47e-4; split 2Zm_e/M + (Zm_e/M)² = 7.5e-8;
  inertial argument (electron feels −m_e a = Z(m_e/M)·force, same sign) → CHECKED.
- l.15 polyatomic. Σ M_κ n_κ = −m_e n_e; λ = −z̄Ṽ; Z/M = 0.4446, 0.4405 /u (0.94 %); 2m_e z̄ = 4.83–4.88e-4 → CHECKED. Note: exactly,
  z̄ = Σ w_κ Z_κ/M_κ with state-dependent weights w_κ = −M_κ⟨n_κ⟩/(m_e⟨n_e⟩) summing to 1. "Positive weights" is a real assumption, and it is
  stated as one. OK.
- eq:17.4-Mmig. The one-phonon term of e^{iK·u} gives iK·e(Q)(2NMω)^{−1/2}(n+1)^{1/2} e^{i(K+Q)·R}. Σ_R gives K = −Q − G, so p_G = q + Q + G,
  and k + p_G ≡ k′ ✓. ∫d³p/(2π)³ → V⁻¹Σ with N/V = 1/Ω ✓. The amplitude is dimensionless: [Ω⁻¹]eV³·[Mω_e²]⁻¹eV⁻³·[(Mω)^{1/2}]⁻¹eV⁻¹·[(q·p)(K·e)]eV³·[v]eV⁻² = 1 ✓.
  e^{−W} at amplitude level ✓ → CHECKED.
  Phase: M^Mig carries +i. The g of eq:A.6-g/6.2-g is ∂_u of e^{−ip·X}v, which carries −i in Fourier form, so M^Mig/M^± is real, as eq:17.4-lock
  needs. CHECKED, but add one clause saying so. The campaign CORRECTIONS l.334 (IF-CW4-4, "carry the −i") is the same issue.
- eq:17.4-Sek. (2π/V)·2·N⁻¹·Σ_kQ = 4π/Ω, the same as eq:13.3-SPA. The order ⟨0|n_e†|f⟩⟨f|n_κ|0⟩ gives M*M^Mig ✓. δ(ω_l ∓ ω_Q) with the upper
  sign for emission ✓. Independent of phase conventions (each Bloch and polarization phase enters once in each factor) ✓. n_B = 1 matches the
  NOTATION ruling (interference terms only) ✓ → CHECKED.
- l.48 frame factor 2.4 = 3.8 %/1.6 % (12.4) → CHECKED.
- l.54–62 vanishing cases. Both amplitudes are linear in q (q·p_G with p_G → Q + G ≠ 0) ✓. 96 % one-phonon at 5 keV (12.4 WE) ✓ → CHECKED.
- eq:17.4-bound follows from eq:8.3-bound with Γ_A = 𝔇_ee S^PA and Γ_B = Σ𝔇_κκ′S_κκ′ → CHECKED. GAP (notation): S^+_eκ and S^+_κκ are joint responses
  (two δ's, units eV), while S^PA is single-δ (eV²). Write S^PA(q;ω_l,ω_e) in the inequality, or integrate over ω_l.
- eq:17.4-lock and eq:17.4-rate. |Ṽ_e|²S − 2Re(Ṽ_e*Ṽ_nuc)(m_e/M)S + |Ṽ_nuc|²(m_e/M)²S = |Ṽ_e − (m_e/M)Ṽ_nuc|²S (sympy) ✓. Rank one, so the bound is
  saturated ✓. Dark photon bracket 1 + Zm_e/M ✓. Mass-proportional coupling gives 0 ✓. Ṽ_nuc = −(M/m_e)Ṽ_e gives 4× and Γ_B = Γ_A, the upper edge ✓.
  (m_e/M)² = 3.8e-10 ✓ → CHECKED. GAP (wording): the lock is a property of the exact summed nuclear amplitude. The crystal-frame eq:17.4-Mmig need not
  satisfy it (frame, Herzberg–Teller term, §A). Write "the exact nuclear amplitude, in the notation of eq:17.4-Mmig".
- l.94 E_g/v_max = 441 eV = 0.193·(2π/a); GaAs 574 eV = 0.262; Si window q = 0.9–1.3 keV = 0.39–0.57; GaAs q* = 1.15 keV = 0.52 of 2.193 keV;
  q_BZ 2.248/2.160 keV → CHECKED. The "O(qa)" of eq:17.4-lock is loose: qa = 1.3 already at q = 0.2·(2π/a). Write O(q/q_BZ), or "the zone scale", as l.94 does.
- Fig. 17.4 caption. M_eh(GaAs) = 0.067 + 1/(γ₁ − 2γ₃) = 0.067 + 0.893 = 0.960 ✓; Γ-pair edge 1.348 eV above the gap at q* (log) ✓;
  L 1.815, X 1.981, |ΓL| 1.899 keV ✓ → CHECKED.
- l.100 windows: Si 0.3374–0.405 MeV (matches SOTA/CORRECTIONS l.314 [CALC]); GaAs 0.433 → 0.52–0.56 ✓ → CHECKED.
- WE 17.4, electron-following paragraph: "without the cross cell their rate would be 216 times (gallium) and 245 times (arsenic) larger" → **WRONG**.
  Without the cross cell the rate is (Z² + F²)/Z*² = 1795.6/4.452 = **403** (Ga) and 2321.7/4.452 = **521** (As). 216 and 245 are Z²/Z*², i.e.
  "the bare nuclear charges alone would give a rate 216 and 245 times larger", as the section text (l.11) correctly says. Use that wording.
- WE zero-phonon cell 4.83–4.88e-4 and (m_e z̄)² = 5.9e-8; phonon-dressed cell; screening cancels; verdict → CHECKED.
- l.124 M/m_e = 51197 → "5.1e4"; per nucleon ≈ m_u/m_e = 1823 → CHECKED.
- NOTATION: F_κ already means the Hellmann–Feynman force (NOTATION row l.473, 5.1), so 17.4's F_κ (following charge) clashes. Rename it (e.g.
  F^fol_κ) or add a clash note. K (local, "momentum the lattice keeps") is one more K; acceptable as local, but say so in NOTATION.

## C. s17-5 Figures of merit per channel

- l.3 plateaus 1102/654, ratio 1.686 → CHECKED.
- l.18 floors 0.333/0.212/0.433/0.316 MeV → CHECKED.
- Partial f-sum (eq:17.5-partial). Above the valence spectrum ε → ε_c(0) − ω_pv²/ω², so g = 1/ε − 1/ε_c ≈ ω_pv²/(ε_c²ω²). The large-ω argument then gives
  ∫ω Im(−g) = (π/2)ω_pv²/ε_c² (sign checked against ∫ω Im ε = (π/2)ω_p²). Im(−g) = L below ω_core → CHECKED. GAP (rigor): g does not → 0 at
  |ω| → ∞ (it tends to 1 − 1/ε_c with the core spectrum). The theorem holds for the model function ε_c(0) + ε_val − 1 at all ω, which
  equals ε below ω_core to O(ω²/ω_core²). Say "applies to the model function" instead of "applies unchanged".
- l.38 n_val = 2.00e23 gives 16.61 eV ✓; plasmon 16.6 ± 0.1 eV, 2004.10709 Table I (EELS) ✓ (source read); ε_c − 1 = 0.0154 → 0.970 ✓ → CHECKED.
- lim:17.5a and l.51. (π/2)ω_pv² = 432.8 eV² ✓; L-sum at 99 eV 0.9999, ε₂-sum 1.0316 ✓; 0.9 reached at 32.7 eV ✓; join 30/40 eV → 0.9923/1.0020 (≤ 0.8 %) ✓;
  all-electron sum 3.548 against 3.5 (1.4 %) ✓ → CHECKED.
- l.53 (31.1/16.6)² = 3.51 ✓; m < 28.42 MeV ✓; Z_val/A_cell 0.1424/0.0551/0.333/0.3084 ✓; "factor 10⁶" (4e6/3.5 ≈ 1.1e6) ✓ → CHECKED.
- l.57 edges 6.12/10.19/3.11 keV → CHECKED. l.68 c_NR1 8.956/5.313/18.157; within 1 % of c̄_LA (0.7/0.9/0.2 %) → CHECKED.
- eq:17.5-cNR1 plateau. 2ρσI₀/(m_u²c_NR1) with ρ = 0.3 GeV/cm³, I₀ = 5.3238e-7 gives 654 /kg/yr (recomputed) → CHECKED.
- l.70 u₋ = ω_th/(2mc) = (v_max − c)m_min^ac/m with m_min^ac = ω_th/[2c(v_max − c)] (partII note 9.2) ✓; m_hi = 0.424 MeV ✓ → CHECKED.
- l.72–85 shift (eq:17.5-shift). ∫_c^{vmax}(v − c)²η = I₀ − 2cI₁ + c²I₂ − ∫_0^c(…), where I₂ = ∫_0^∞η dv = ∫f d³v = 1 (log I₂ = 1.0000) and the
  last term is ≈ η(0)c³/3 (third order). Completeness Σ_ν(q̂·ê_ν)² = 1 ✓. 2I₁/I₀ = 5.879/v_max = 1/(135.1 km/s) ✓. Si 0.9337/0.9354 (largest 0.936) and
  C 0.8656/0.8725 (0.874) ✓. Dimensionless ✓ → CHECKED.
- l.89–91 pair formula 1 − Δc/135 and the "13.5 km/s" rule ✓. Ge/Si enters at 43.3 keV and settles at 1.0275; C/Si at 24.8 keV and 0.9327; CsI/Si at 97 keV and 1.045;
  C/CsI 87–227 keV (fig17_window.log, fom17_5.log) → CHECKED.
- WE 17.5. Plateaus 322.6/654.0; edges 3.19/6.39 keV; caps 0.65/0.42 MeV; all table entries and 1 + δ (6.12 … 0.933) ✓; u₋ = 251 km/s = 0.32 v_max,
  124 km/s ✓; crossing 1.1 at 24.8 keV = 3.9 edges ✓; first order 0.932 and exact 0.8724/0.9354 = 0.9327 ✓; C/Ge 0.908 with Δc = 12.84 ✓.
- WE l.121, "The figure of merit ranks the pair correctly, by a factor two, at every mass above the edges" → **WRONG**. At 10 keV, above both edges
  (6.39 and 3.19 keV), R_C/R_Si = 3.02, against the FOM's 0.49, which is the opposite order. From fom17_5_rates.npz the rates cross at
  m ≈ 14 keV (R_Si = 250, R_C = 246 at 14.07 keV), 2.2 Si edges. Correct to: "ranks the pair correctly above about 14 keV, twice the edge of
  silicon; below that the softer crystal's cut reverses the order."
- l.124–132 Griffin speeds. 1910.10716 Table I c_LA (units 1e-5 c): GaN 4.17 = 12.50, AlN 5.70 = 17.09, ZnO 4.18 = 12.53, CsI 0.46 = 1.379,
  CaWO₄ 1.42 = 4.257, Si 2.84 = 8.51 km/s. The App. A 3 definition (average of ω_LA/q on a sphere at q ≈ 10 eV) matches the text. Lopuszyński Table I
  recommended and Madelung values, Gopal–Spaldin Table III measured ZnO 206/118/211/118/44, and Buongiorno Nardelli Table I B₀ = 13.5 GPa
  (a₀ 4.56 Å) all agree with the script. Popova p. 16 quotes Farley's CaWO₄ C_ij exactly (C26 = −C16 is implied by 4/m) → all CHECKED. Christoffel results:
  maxima 8.08/11.02/6.10; ratios 1.547/1.551/2.055; handbook 1.589/1.523; CsI 2.37–2.46; CaWO₄ 4.36–5.17, mean 4.65 (−8.4 %);
  Si −5.6 % → CHECKED.
- l.128 "puts the floor at 1.726 km/s, 20 % above the tabulated value" → **WRONG**. 1.726/1.379 = 1.25, so the floor is **25 %** above. Equivalently,
  "the tabulated value lies 20 % below the floor" (the log's phrasing).
- l.132 CsI c_NR1 2.40, FOM 3.73 against 6.49, edge 23.1 keV; CaWO₄ 4.58, 1.96 against 2.10, edge 11.0 keV → CHECKED. DC-RESULTS DC-93 (VALIDATED)
  gives c_LA 2.32–2.46. The lower end 2.32 corresponds to the denser 4.734 g/cm³ cell (2.37·(4.529/4.734)^{1/2} = 2.318). The book's 2.37 is at 4.529. They are consistent;
  DC-93 says "FOM ≈ 3.7–3.9, quote as ≈", and the book's own Christoffel value 3.73 is an independent computation. Vallin was read in abstract only
  (DC-93, editor note); the citation should say "as given in the abstract" or the full text should be checked.
- l.136–142 polar. Ratio of K_η: 0.340/0.767/0.870; 0.9 at 51.5 MeV; sapphire 1.69 GeV; 18.99/0.1415 = 134; 134 × 0.767 = 103; dielectric/splitting 1.081
  → CHECKED. The displayed K ratio is exact for the single-speed form K = ln(q₊/q₋)/v → CHECKED.
- l.144 edges 10.35/21.98/32.01 keV; sapphire branches at 48.1–112.4 meV give 13.7–32.0 keV → CHECKED.
- eq:17.5-pole. The algebra ∫L/ω⁴ = (π/2)ω_pv²/ω_pl⁵ → (π/2)ω_pv⁻³ is CHECKED. Nuclear factor 0.570/1.928 (×3.384); LiF n_val = 4.926e23 gives 26.06 eV
  (8 valence electrons per formula unit and a = 4.020 Å, 1910.10716 Table III ✓); pole ratio 3.870 ("(26.1/16.6)³" with the rounded values gives 3.89; quote 3.87
  from the unrounded values); net 0.874; Ge 15.6 eV, net 0.466 → CHECKED.
  **GAP (physics).** The Migdal weight sits at p ≈ 3–9 keV, not at p → 0. The p-integral of the pole form depends on the material through the dispersion
  ω_pl(p). With a single pole ω_pl² = ω_p² + (p²/2m_e)², ∫p²dp ω_pv²/ω_pl⁵ ∝ ω_p^{−3/2} (sympy: (2m)^{3/2}ω^{−3/2}·Γ(3/4)²/(4√π)).
  The result becomes LiF/Si ≈ **1.72** and Ge/Si ≈ 0.42. A Bohm–Gross dispersion gives ∝ ω_p⁻², LiF/Si ≈ 1.37. So "0.87" holds only for a dispersionless pole
  at fixed p-range. State it that way, or give the range 0.87–1.7. The conclusion "ranking open" is reinforced.
- l.164 (ω_pv/E_g)⁵ = 5.75e5 ✓. "The bound of silicon is 1.1e5 times that of LiF": 1.07e5 is the ratio of the L-integral bounds alone, and with
  the nuclear factor F_Mig it is 3.2e4. Say which one is meant. The reversal holds either way.
- tab:17-fom → CHECKED against the text. The "about 4 edges" row matches the book halo (3.84–4.04).
- Dimensions: eq:17.5-window and eq:17.5-shift are dimensionless; F_Mig is in eV⁻³ → CHECKED.

## D. s17-6 Ranking under uncertainty

- l.3 TeO₂ c_NR1 3.754 and CaWO₄ 4.578; 2.386 and 1.2195 → CHECKED.
- l.7 Ge 131/49/68 GPa (McSkimin via 11.1) ✓. Open book-wide item: 11.1 uses a_Ge = 5.652 Å (ρ 5.34). With 5.658, c_NR1 rises by 0.16 %
  (5.313 → 5.321) and F_Ge goes from 1.686 to 1.683. No probability in 17.6 changes at the printed digits.
- tab:17-widths. The script uses Ipol_GaAs = 0.04, which is not in the table → GAP. Add "GaAs 𝓘_pol (dielectric/splitting spread): 0.04". Sapphire
  ln(3.3/3.1)/2 = 0.031 ✓.
- l.27 JARVIS (OptB88vdW, 1804.01033 ✓). DB/measured −2.9/−10.1/−1.0 %, rms 0.0638, mean −0.0484 → CHECKED. Gap shifts 0.05/0.084/0.10 eV
  (tab:3-materials) → CHECKED.
- l.31 gaps from 1910.10716 Table I: LiF 14.2, NaF 11.5 and CaWO₄ 5.2 at room temperature; diamond 5.47* at low temperature ✓. Polar 18.99/9.95 ✓ → CHECKED.
- l.47 sampling error √(0.25/2e4) = 0.0035 ✓; Δ = ln(4.782/3.754) = 0.2420, Φ(0.242/0.1216) = 0.977 against MC 0.976; CaWO₄/GaAs 0.689/0.688 → CHECKED.
- l.49–51 P(first) 0.968, interval [2.19, 2.60]; CaWO₄ [1.92, 2.00] and 0.010; doubled width 0.781/0.135/0.073; Si rank 8–8; shared 2–3 → CHECKED (rank17_6.log).
- Fig. 17.5 and l.60. PbSe 0.0484 MeV (0.17* eV), P = 1.000; Ge 5th, Si 7th; 21 tiers; Ge≻GaSb 0.973; unshifted GaSb 0.2051 MeV against 0.2119;
  U[0, 0.15] gives 0.837; ZnO≺GaN P = 0.898; NaF/CaF₂ ≈ 0.97 (recomputed by hand: Δln 0.026, σ 0.014) → CHECKED.
- l.62 pool floors 0.212 … 4.06 MeV, one place each → CHECKED.
- l.68 GaAs edge [10.3, 12.3] in tier 6, CaWO₄ [10.8, 11.2] in tier 7, Ge [9.99, 10.4]; the resolution statements → CHECKED.
- WE 17.6 intervals, heights, tiers, P(first) and rank intervals, the 0.001 margin and P(GaAs≻Ge) = 0.884 → CHECKED. The procedure is the interval-order height
  of eq:C.13 → CHECKED.
- eq:17.6-zmethod. Var = r + (1 − r) = 1 and Cov = r, so Var ln(x_A/x_B) = σ_A² + σ_B² − 2rσ_Aσ_B → CHECKED.
- l.93 TeO₂≻GaAs 0.976/0.997/1.000; P(first) 0.968/0.985/0.987; LiF≻NaF 0.987/1.000 → CHECKED.
- l.95 Migdal: six crystals in tier 1; P(first) 0.315/0.290/0.147; NaF 1.000 at r = 1; 1.024 → CHECKED. Wording: "pole-free value" should be "value at
  X_pole = 1" (it is the pole value without X).
- **X_pole prior (PRIORITY 4): not defensible as a description of the uncertainty, but the conclusion it supports survives.** X_pole is the ratio of true F_Mig to the pole form.
  For the one crystal with a computed spectrum, silicon, 12.3 puts 4 % of the Migdal probability in the plasmon, so X_Si ≈ 25. That lies outside [1, 3] by an
  order of magnitude. X also depends on the gap (17.5), so the medians and P(first) of the Migdal row are artifacts of the prior. Any wider or
  crystal-dependent prior only widens the intervals, so "no reading at r_mat = 0" is robust and "NaF 1.000 at r = 1" stays an artifact. Correction: say
  that the prior is a device, quote X_Si ≈ 25 from 12.3, and state in the tab:17-rank caption that the Migdal medians include the prior median √3 = 1.73. Otherwise
  "Si 1.73, relative to Si at X_pole = 1" reads as an error. Together with the p-integral GAP of §C, the medians (NaF 1.77, Si 1.73, LiF 1.51 …) carry no
  ordering information.
- l.97 Ge/GaAs tier change and caveat. Mean offset 0.0484 gives F_GaAs 1.784, Δ = 0.0565 and σ = (0.086² + 0.02²)^{1/2} = 0.0883, so Φ = 0.741 → CHECKED. The tier change
  (Ge in tier 3 under GaAs in tier 2) rests on a 0.001 margin and on a database tensor, and the text says both → CHECKED. Suggest adding that the same offset applied to TeO₂ lowers
  P(TeO₂≻CaWO₄) from 0.987 to ≈ 0.955 (Δ = 0.1986 − 0.0484). The sentence at l.97 invites the comparison.
- tab:17-rank: every entry matches rank17_6.log (r = 0, with r = 1 in parentheses) → CHECKED. GaAs "last in rate by a factor of 130" (l.122): against LiF it is 134;
  against the next crystal (sapphire) it is 65. Say "134 below LiF".
- l.124 sapphire/diamond 1.657; LiF/NaF 1.91 → CHECKED.
- l.126 CsI 2.40, and 2.35 at 4.734 g/cm³ (+4.5 %); F 3.73–3.81, ×1.56–1.60 TeO₂; Pb salts 2.57–4.38 → CHECKED. The "cold cell 4.5 % denser" is the editor's
  illustrative bound: CsI expands by ≈ 1.0–1.2 % linearly from 0 to 300 K, about 3–3.5 % in volume. Write "at most 4.5 % denser".
- **PRIORITY 5: book-halo window values.** 17.6 quotes no campaign window number. It cites W_AB and LiF/GaAs above 52 MeV, which is the book value (fom/pol logs) → CHECKED. The campaign
  values (onset 4.7–5.7 m_min, u₋ ≈ 0.21 v_max, CORRECTIONS l.593) appear nowhere in 17.5 or 17.6.
- Campaign check (SOTA l.649–653). The campaign has TeO₂ 2.31×Si (ρ proxy, before the shear-order fix of CORRECTIONS l.463/605) and Ge ER floor 0.210. The book's 2.39 (database
  density, corrected assignment, c̄_LA 4.094 = campaign's corrected 4.10) and 0.212 (v_max 2.650e-3) are the book's own values and supersede them → CHECKED, no superseded value is used.
  The CsI and Griffin errata follow CORRECTIONS §20.2 l.589 → CHECKED.
- NOTATION: σ_j is also the 13.7 symbol for the Gaussian widths of normal coordinates (NOTATION l.992). Add a clash note or rename it σ^prov_j. X_pole and the
  provenance rows are proposed in SEAM 17.6 and not yet in NOTATION.

## E. s17-summary and tab:17-nuisances against the final sections

- l.129 band top 63.7 meV; E_R^max = 2μ²v²/M = 0.0536 eV at 10 MeV; ½mv² = 35.1 eV; crossovers 0.178/0.307/5.33 eV (= 17.1 l.26); 17 against 8e5 → CHECKED.
- l.133 31×, 0.78–1.10, 1,810 against 842 (17.3, editor notes) → CHECKED.
- l.135 17.4 paragraph: −(m_e/M), the bracket, 5.47e-4, "a fifth to three fifths" → CHECKED against the final s17-4. The 17.5 part: 16.6 eV, 5.7e5, 1.73/0.46 against 1.69/0.49
  (1.0273 × 1.686 = 1.732; 0.4601) → CHECKED. The citation "(sec:11.1)" for 1.73/0.46 should be sec:17.5 (fom17_5.log computes these numbers).
- l.137 17.6 paragraph → CHECKED (0.968, 0.315, "1 to 10 %").
- Nuisance rows:
  - 17.4 row → CHECKED. Add a row, or extend the Migdal rows of 17.1, for §A: "coherent Migdal at q < q_BZ: diagonal soft limit ≈ 15× high (exact as
    q → 0, eq:8.3-boostward)".
  - "Shift of η … up to 6 % at 0.3 MeV" → **WRONG (rounding)**. Diamond/Si is 0.9328 at 0.3 MeV, a 6.7 % difference. Write "up to 7 %", matching 17.5 l.121
    ("biased by 7 %").
  - Migdal pole row → CHECKED. Add "pole form itself uncertain by ×2 in material scaling (dispersion)" (§C).
  - Provenance, offset, r_mat and GaSb rows → CHECKED (0.968 → 0.781, 0.884 → 0.741, 0.976 → 1.000, 0.315 → 1.000, 0.973/0.837).
  - The silicon-window row (lead to 0.43, band 0.43–0.51) matches SOTA's [E] table l.634–640 → CHECKED.

## F. DC-RESULTS / R18 cross-check
- DC-93 (CsI C_ij, VALIDATED) bears on 17.5 l.128–132 and 17.6 l.126. It is consistent; see §C. The quoting restriction is respected (3.7–3.8, "≈" in 17.6). Its
  note "the ranking rerun is owed" has been met by 17.5/17.6, which compute CsI directly.
- DC-2 and DC-2-alpha (Ge window [E]) do not touch my sections. The summary's "germanium zero-phonon edge … not known" agrees with them.
- No other DC item bears on s17-4 to s17-6.

## Summary of required changes
WRONG: (1) WE 17.4: "216/245 times larger without the cross cell" → 403/521, or reword as "bare nuclear charges alone". (2) WE 17.5 l.121
"ranks correctly at every mass above the edges" → only above ≈ 14 keV. (3) 17.5 l.128 "20 % above" → 25 % above (or "20 % below the floor").
(4) Nuisance row η-shift "up to 6 %" → 7 %.
GAP: the Ch12 erratum and qualifier (§A, the main finding); eq:17.5-pole p-integral and dispersion; the X_pole prior against X_Si ≈ 25 and the Migdal median caption; the S^PA
joint and single-δ notation in eq:17.4-bound; the lock read as an exact-amplitude statement; the GaAs 𝓘_pol width missing from tab:17-widths; the f-sum "model function"
wording; the F_κ and σ_j NOTATION clashes; the 1.1e5 bound ratio; "at most" for the cold CsI cell; the summary citation 11.1 → 17.5.
