# R11 referee report REF-WP7-T-B (hostile, isolated) on returns/R10/WP7-T.md

Scope: returns/R10/WP7-T.md, code/WP7-T/checks.py (re-run: 46/46 PASS, about 3 s), WP0-v3, CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS.
Full texts fetched with lit.py into literature/papers-r11-WP7-T-B/ (1705.01108, 2103.06977, 1610.03974, cond-mat/9409105, 1806.11002,
2409.02820, cond-mat/0310283, 2009.03804) and deleted after use. One sympy check (crowdion mass identity) and one 41×41 matrix
diagonalisation (Mathieu band width, below 1 s) were run. No simulations.

## Verdict table
| # | Claim (return §) | Verdict | Reason |
|---|---|---|---|
| 1 | Defect = reference-state choice, `ref=def(·)`, new K value `def` (§1.1, IF-T1) | STANDS WITH CORRECTION | The ref metadata is fine. **K=def is a category error:** K is the kinematic regime (CONVENTIONS §11). Keep K = − (or the host's regime). Also scr=− in the τ string contradicts CONVENTIONS §7 for the n_e row (C-8) |
| 2 | Two-configuration reduction (1.1), eigenbasis elements (C1) | STANDS | Checked: ¼\|𝔣\|²(Δ_tun/E)² and (Δ_as/E)² are correct |
| 3 | Elastic-dipole vertex (1.2), static q-independence (1.4)(i) | STANDS WITH CORRECTION | The propagator contraction is right (C5). The relative sign of the core and host terms is not checked (C-9). The static window needs q ≪ 1/r_core *and* q < q_×, which fails at the §2.4 benchmark (C-3) |
| 4 | Pole assignment rule (1.4)(iii), "PV stays in S^{def}" | FALLS as written | S ∝ \|𝔣\|² has a **double** pole. A PV prescription for 1/(c²q²−ω²)² does not exist. CONVENTIONS §10 DC requires the Hadamard finite part plus a δ part with a 1/η coefficient. The §2.7 spec ("PV with analytic subtraction") is therefore ill-defined (C-4) |
| 5 | TLS response (2.1); STM S flat in ω (2.2) | STANDS | Re-derived: (π/2)P̄\|𝔣\|²/(1+e^{−ω/T}), detailed balance and Im R/tanh relation all correct |
| 6 | 1/𝔔_ph, 1/𝔔_el (§2.3a,b; L25) | STANDS WITH CORRECTION | Derivations correct (match Hunklinger–Arnold πC tanh). Source misprint claim CONFIRMED (C-1). The tanδ input attribution is wrong (C-6) |
| 7 | Dark-photon absorption on TLS (2.3), L32 | STANDS WITH CORRECTION | Formula correct, = WP0 (3.5)/L9b. The quoted "a-SiO2 tanδ ≈ 1.6×10⁻³ at 4.2 K per 1705.01108 §VI" is false (C-6) |
| 8 | DM rate on TLS (2.4) and the number 1.1×10⁻³ /(kg day meV) | STANDS WITH CORRECTION | (2.4) holds only for m_χ ≪ m_e, but it is evaluated at m_χ = 1 MeV > m_e. The missing factor is (m_χ/μ_χe)² = 8.7. The benchmark also lies outside the static window (q > q_×) and has no screening. Corrected number ≈ 10⁻² (O(1) uncertain) (C-2, C-3, C-8) |
| 9 | Metastable trigger suppression "≪ 10⁻²⁰" (§2.5) | STANDS WITH CORRECTION | With the return's own numbers the ratio is ≈ 2×10⁻²⁰ at Γ_↓ = 10⁻⁸ s⁻¹ (×9 at 1 MeV, C-2), so "≪" should read "≲ 10⁻¹⁹". The conclusion is unaffected |
| 10 | Defecton response (3.1), limits (ii)–(iii) | STANDS WITH CORRECTION | Kernels are correct. "Replaces the bare-mass share of WP0 (4.6b)" is wrong: the f-sum is an exact commutator identity, and the band only redistributes weight (C-10) |
| 11 | Crowdion translation mass M_cr = 2μ_FKa₁₁₁m/π² "**New [D]**" (3.2), L31 | STANDS WITH CORRECTION (formula); novelty REFUTED | The formula is correct, but M_cr ≡ E₀/c_s² is the sine-Gordon/Frenkel–Kontorova kink rest mass, a textbook result (C-5) |
| 12 | W crowdion "coherent 1D defecton at mK with a (sub-)meV band" (§3.2) | STANDS WITH CORRECTION → [C] | For E_mig/E_rec = 6.8 the Mathieu band is 0.024 meV (0.28 K), not sub-meV. Polaron narrowing and strain-disorder localisation are omitted (C-11) |
| 13 | Golden-rule/NIBA hop rate (4.1)–(4.3) and limits (a)–(d) | STANDS | J_ph, J_el, 𝒬(t), detailed balance and the closed form (4.3) re-derived. cond-mat/9409105 Eqs. (8)–(9), Δ̃ after Eq. (10), 2103.06977 Eqs. (7)–(9) and 2409.02820 Eqs. (1)–(3) verified against full text. One normalisation needs restating (C-12) |
| 14 | Jäckle-rate source discrepancy (2103.06977 Eq. (2) vs (7)) | STANDS; claim CONFIRMED | See C-1(b) |
| 15 | mK tunnelling window λ ≲ 24, V ≲ 41 meV(1 Å/d)²; Si FP λ ≈ 55, Al λ ≈ 50 "frozen" (§4.2, §5.1) | STANDS WITH CORRECTION | λ uses the 1705.01108 Eq. (7) convention, which is 2× the Phillips/Jäckle/2103.06977 λ. Harmonic-well geometry gives the latter. Si FP and Al become λ ≈ 25–37, at the window edge. The criterion also ignores the energy-gap law for ε ≫ ω_D (C-7) |
| 16 | Correlated recombination t^{−3/2} vs broad-λ 1/t discriminant (§4.3) | STANDS WITH CORRECTION | 3D Smoluchowski is fine. In 1D the crowdion moves in its own vacancy's strain field, far stronger than the band width, so the first passage is drift-dominated, not force-free t^{−3/2} (C-11) |
| 17 | FC energy-conditioned occupation (4.4); photon branch 5×10⁻¹⁴ | STANDS WITH CORRECTION | (4.4) is exact only at T = 0 (the C12 check uses Poisson weights). The ratio formula (8π/3)αd²ρc_t⁵/γ² was re-derived correctly |
| 18 | STM heat release (4.5) = 1610.03974 Eq. (6), L29 | STANDS | Quote verified. λ-integral and π²/12 correct |
| 19 | Release kernel/interface (5.1)–(5.2); "calibration source fixes it for DM" | STANDS WITH CORRECTION | The λ ≤ 24 class split inherits C-7. The calibration claim needs near-threshold recoils, because the class mix and the local strain differ between keV cascades and E_R ≈ E_d (C-13) |
| 20 | Computation specs §2.7, §3.4, §4.6, §5.4 (gap closure, rubric e) | §2.7 INSUFFICIENT; others STAND | §2.7 has an ill-defined pole prescription (C-4), and 10⁴–10⁵ candidate pairs give ≪ 10³ TLS per decade (C-14) |
| 21 | Checks "46 checks, all PASS" | STANDS WITH CORRECTION | At least 5 checks are vacuous (C-15). C14b carries the C-2 error |

## (c) Claims that a published paper is wrong — verified against full text
**C-1(a) 1705.01108 Eq. (20), phonon loss a factor ½ too small — CONFIRMED.**
- What the full text says: Eq. (20) is "1/Q_{i,el} = π|p|²D₀/(3ε_i), 1/Q_{i,ph} = π|γ|²D₀/(2ρv²)". The same paper's Eq. (16) fixes
  ε = 2γ·S + 2p·E + ε₀.
- With that convention, golden rule plus travelling-wave energy ½ρc²S₀² gives πγ²P̄ tanh/(ρc²). The electric form of the same Eq. (20)
  follows from the 2p·E convention with no ½. So the ½ in the phonon form is internally inconsistent with Eq. (16) and with the electric
  form, and it disagrees with the standard Hunklinger–Arnold Q⁻¹ = πC tanh.
- Two further defects in Eq. (20), both acknowledged by the return: it has no tanh, and it uses D₀, the log-enhanced DOS of Eq. (9),
  where the (Δ₀/E)² weighting gives P₀. The return's statement stands.

**C-1(b) 2103.06977 Eq. (2) vs Eq. (7) — CONFIRMED.**
- The full text writes "δε = γ·S" and "H^{LR}_int = 1/2(γ·S)σ_z^{LR}", with M = γΔ/2E. Eq. (7) is Jäckle's rate
  (γ_l²/v_l⁵ + 2γ_t²/v_t⁵)(Δ/E)²E³coth/(2πρħ⁴).
- I re-derived Eq. (7) with H_int = γSσ_z, i.e. δε = 2γS (C3a re-done by hand: E³/(2πρc⁵) per branch). With Eq. (2) read literally, the
  rate is Eq. (7)/4.
- Caveat: C3d in the script is a tautology (Gdown/4 − jaeckle/4 = 0 given C3a). The confirmation rests on my derivation, not on C3d.

**New source-level inconsistency the return missed (relevant to C-7):**
- 1705.01108 Eq. (7) defines λ = d√(2mV)/ħ.
- 2103.06977 (following Jäckle/Phillips) defines λ = (d/2ħ)√(2mV).
- 1610.03974 Eq. (13) gives λ₀ = V/E₀. For two intersecting harmonic wells this equals mωd²/4ħ = (d/2ħ)√(2mV), the Phillips value.
- So 1705.01108 Eq. (7) overestimates the exponent of a harmonic double well by a factor 2. A quartic well gives (2/3)d√(2mV)/ħ.

## Corrections (numbered; cited in the table)
**C-2 (substantive, number) — (2.4) applied outside its hypothesis.**
- WP0 (9.2) carries 1/μ_χe², and ∫q dq η(q/2m_χ) = 2m_χ²⟨|v|⟩. The bound target's kinematics use m_χ, not μ.
- The general result is therefore dℛ/dω = (ρ_χ/m_χ)⟨|v|⟩σ̄_e(m_χ/μ_χe)²P̄⟨|𝔣_e|²⟩/[4ρ_T(1+e^{−ω/T})] = (1 + m_χ/m_e)² × (2.4).
- At the stated benchmark m_χ = 1 MeV this factor is 8.74. C14b omits it, so the a-SiO2 figure should be ≈ 9.6×10⁻³ /(kg day meV)
  before C-3/C-8.
- The per-TLS cross-section must read σ̄_e(1 + m_χ/m_e)²|𝔣_e|²(Δ_tun/E)²/4.
- Minor: "m_χ ≫ ω/v² ≈ 0.1 keV" holds only for v at the escape-plus-Earth edge. For ⟨v⟩ ≈ 10⁻³, ω/v² ≈ 1 keV.

**C-3 (validity) — the benchmark is not in the static window.**
- At m_χ = 1 MeV the q-weight peaks at q ≈ 1–2 keV (0.5–1 Å⁻¹).
- That is above the return's own q_× ≈ 0.6 keV, where the core term 2i c_κ sin(q·d/2) dominates (|𝔣^{core}_e| ≈ 16 sin(qd/2) for one O
  moving 1 Å, versus |𝔣^{host}| ≈ 2.9).
- It is also at or above 1/r_core for a multi-atom TLS core (r_core ≈ 3–5 Å), where continuum elasticity fails.
- State the window as ω/c_l ≪ q ≪ min(q_×, 1/r_core), i.e. 50 keV ≪ m_χ ≲ 0.3 MeV for host-term dominance. Outside it, use the full
  core + host |𝔣|².
- The 1 MeV number is then uncertain by up to ×(16 sin(qd/2)/2.9)² ≈ ×10 upward. It is [E] at the order-of-magnitude level only.

**C-4 (substantive, rule and spec) — pole of |𝔣|².**
- With retarded G, |𝔣_host|² ∝ |c²q² − (ω+iη)²|⁻². The split is fp(1/x²) + (π/2η)δ(x)-type, not PV + δ.
- The δ coefficient diverges as the phonon width η → 0. Physically that is real-phonon emission times the TLS absorption branching, i.e.
  the cascade term.
- The core–host interference term has a simple pole and does take PV.
- Rewrite §1.4(iii) as: "finite part (Hadamard) and PV parts → S^{def}; the 1/η δ part → S^{GS} ⊗ P_casc with η = c_l/ℓ_TLS + anharmonic
  width". The `tls_response` module must implement fp, as CONVENTIONS §10 already prescribes. "PV prescription at the pole with analytic
  subtraction" is insufficient.

**C-5 (novelty REFUTED, rubric f) — crowdion mass.**
- Using 1806.11002 Eqs. (1)–(3): from Eq. (3), μ = π√(2V₀/β)/a². With c_s² = βa²/m from the continuum Lagrangian (1), sympy gives
  2μam/π² ≡ E₀/c_s² identically.
- This is the Lorentz-invariant sine-Gordon kink rest mass, the textbook FK kink mass m_k = 2m_a/(π²d) (Braun & Kivshar, *The
  Frenkel–Kontorova model*, Springer 2004, which is ref. [3] of 1806.11002 itself [UNVERIFIED page]).
- Drop "New [D]" in §3.2 and L31. Credit the FK/sine-Gordon literature and keep the formula as DERIVED (re-derivation).

**C-6 (misquote) — tanδ input.**
- 1705.01108 §VI full text: "for thin AlOx layers formed by plasma oxidation, Deng et al. obtained the large value tan δ ≈ 1.6·10⁻³". The
  4.2 K value in the same paragraph is a-Si:H, tan δ = 2.5·10⁻⁵.
- No a-SiO2 value at 4.2 K is given there. Correct the attribution in §2.3(d) and L32.
- Note also that a 4.2 K loss tangent is thermally saturated (tanh(ω/2T) ≈ 0.03 at 5 GHz). It is not the low-T, low-power TLS loss
  needed in (2.3).
- Minor: §2.4 cites "(2.3a)" for ℓ_TLS. Equation (2.3) is the dark-photon rate; the reference should be §2.3(a).

**C-7 (substantive, §4.2, §5.1, (5.1)) — tunnelling window.**
- (i) Convention. With the Phillips/harmonic λ (see §(c)), H in Nb has λ ≈ 4, Si close FP λ ≈ 27, Al SIA λ ≈ 25, and the Si-mass bound
  becomes V ≲ 166 meV(1 Å/d)². A quartic well gives Si FP λ ≈ 37. The "frozen" verdicts for Si close pairs and the Al SIA are therefore
  not robust. Mark them [E, convention-dependent ×2 in λ].
- (ii) Prefactor. Γ ~ ω₀e^{−2λ} ignores that for ε ≫ ω_D the one-phonon δ(ε − ω) in (4.2) vanishes. The rate is then multiphonon
  (energy-gap law), suppressed by many orders unless S_HR is large.
- Hence the window must be λ ≲ ½ ln(ω₀ t_obs) − ½ ln(1/F(ε)), with F(ε) the FC/energy-gap factor from (4.2). A pure λ ≤ 24 cut in
  (5.1) is not derived.
- The "𝒮_inst(T→0) = 2λ_ij" identification holds only if λ is the true WKB integral, not the square-barrier d√(2MV).

**C-8 (consistency, CONVENTIONS §7, §9) — screening.**
- CONVENTIONS: "screening lives only in S", and n_e is always screened. The τ string has scr=−, and (2.4) has no ε_e⁻¹(q,ω).
- In a-SiO2 at q ≈ 1–2 keV, 1/|ε_e(q,0)|² is O(0.3–0.7) [E]. Add scr=ext and the factor, or state why it is absent.
- The acoustic-sum-rule step w_e = Ω⁻¹ΣZ_κ uses q → 0 Born charges (WP0 (4.8)(i)). It needs q ≪ 1/a, which is marginal at the benchmark
  q (C-3).

**C-9 (unchecked sign, DONE rung-4 "sign of q").** No script fixes the sign of the host term relative to 𝔣^{core} under the CONVENTIONS §3
e^{+iq·r} convention. Physically, R − L with γ > 0 compresses the host, so the host δn_e should be positive. The interference near q_× is
sign-sensitive. Add a check.

**C-10 (§3.1 f-sum wording).** ∫ω S_κκ = π𝓃q²/M_κ is an exact commutator (WP0 (4.6)). The defecton band carries a partial first moment
|𝔣^{loc}|²q²/2m^{dfn}, with the weight redistributed from the host phonon part. It does not "replace" the bare-mass share. C11c only checks
the first moment of a unit Gaussian. Also Σw_i ≤ Δ_dfn (not 2Δ_dfn) for simple cubic.

**C-11 (§3.2, §4.3a; downgrade to [C]).**
- Band: Mathieu ground band for E_mig = 1 meV, E_rec = 0.147 meV is 0.024 meV (my diagonalisation; ground level 0.33 meV above the
  minimum, consistent with the return's ħω₀/2 = 0.38 meV).
- Disorder: cond-mat/0310283 (Eqs. (17)–(19)) gives localisation of a defecton band by strain sources when |∇φ|a > Δ, i.e. above
  x_c ≈ (Δ/3V₀)^{3/4} ≈ 10⁻⁴ for Δ = 25 μeV, V₀ ≈ 1 eV. The parent vacancy's 1/r³ field exceeds Δ within ~ (V₀/Δ)^{1/3} ≈ 30 a.
- Polaron: lattice-dressing (polaron) band narrowing is omitted entirely.
- Consequently, "coherent 1D defecton at mK" and "ballistic recombination, t = d/v_g" are [C]. The correlated 1D recombination near its
  vacancy is drift/phonon-assisted, so the time distribution is peaked, not a force-free t^{−3/2} tail.
- The 3D t^{−3/2} (C9c,d) stands.

**C-12 (normalisation).** 2009.03804 Eq. (4) reads τ_el⁻¹ = (4πK/ħ)(Δ₀²/ε)coth. So α_ohm = 4K₂₀₀₉ (and W_el² = 16K₂₀₀₉). Replace "up to its
coupling normalisation" with this identity in §4.1(b) and L26.

**C-13 (§5.3 overclaim).** 𝒦^{rel}(·|c,T) is seed-independent per class, but P(c|E_R, r̂_R) and the local strain are not. A calibration fixes
the DM kernel only with near-threshold recoils (E_R ≲ few E_d). Reword.

**C-14 (§2.7 sampling, rubric e) [E].**
- With P̄ = 1.6×10¹⁹ eV⁻¹cm⁻³ per unit λ, the TLS with |Δ_as| < 1 meV and λ < 20 number ≈ 6×10¹⁷ cm⁻³ ≈ 10⁻⁵ per atom.
- A 10⁴-atom cell holds ≈ 0.1 such TLS, so "10⁴–10⁵ candidate pairs in 3000–10⁴-atom cells" cannot deliver "≥ 10³ sampled TLS per energy
  decade". That needs ≳ 10⁸ minima pairs (swap-MC or landscape filtering).
- Also: P̄ = 10⁴⁴ J⁻¹m⁻³ (C14c) with C_TLS = 3×10⁻⁴ implies γ_l ≈ 2.9 eV, not the 1 eV used in §1.4. Literature a-SiO2 has P̄ ≈ 8×10⁴⁴
  J⁻¹m⁻³ with γ_l ≈ 1 eV. The rate (C14b) uses only C_TLS and is unaffected.
- The STM flat band "ω ≲ 1 meV" for a-SiO2 is overstated: C ∝ T holds below ~1 K (~0.1 meV). Above that, soft modes take over [E].

**C-15 (checks).** The following are vacuous or irrelevant:
- C3d (tautology);
- C4c (ratio of two hand-typed expressions; it does not read the source);
- C7c (sin π = 0);
- C13a (arithmetic);
- C14f ((c_l/c)⁵, unrelated to the ratio actually used, C14h).

Report them as "46 checks, of which 41 non-trivial". Add: (m_χ/μ)² in C14b, the C-9 sign, and C-11's band width.

## (b) LIMITS rows L25–L32
| Row | Quote (FT) | Chain | Validity / leading correction | Verdict |
|---|---|---|---|---|
| L25 | 1705.01108 Eq. (20) verified; 2103.06977 Eqs. (4)–(6) verified | valid | T → 0 / D₀ → P̄ correctly flagged; add "source ½ CONFIRMED" | DERIVED ✎ (C-1) |
| L26 | 2103.06977 Eqs. (7)–(9), 1610.03974 Eqs. (4)–(5), 2009.03804 Eq. (4) verified | valid | E ≪ Δ_BCS for (9) correctly stated; fix α_ohm = 4K (C-12) | DERIVED ✎ |
| L27 | cond-mat/9409105 Eqs. (8)–(9), Δ̃ after (10) verified (K ≤ ½) | valid (identity checked analytically) | Δ₁ correction correctly attributed | DERIVED |
| L28 | 2409.02820 Eqs. (1)–(4) verified | valid | — | DERIVED |
| L29 | 1610.03974 Eqs. (1), (6)–(8) verified | valid | — | DERIVED |
| L30 | cond-mat/0310283 Eqs. (1)–(4), (7), (11)–(12) verified; Δ ≈ 10⁻⁴ K (³He) verified | valid | add the localisation criterion Eqs. (17)–(19) as the leading correction | DERIVED (+ C-11) |
| L31 | 1806.11002 Eqs. (2), (3), (6) verified | valid | drop "(new)" (C-5); the band width is 0.024 meV, not sub-meV | DERIVED ✎ |
| L32 | formula = WP0 (3.5), L9b | valid | tanδ input misattributed (C-6); screening/transverse mixing correctly listed | DERIVED ✎ |

## (d) Consistency notes (WP0-v3, CONVENTIONS, NOTATION)
- WP0 (3.1), (3.5)–(3.6), (4.3), (4.4), (7.3), (9.2), Theorem D/(H2) and D-g are used consistently.
- (9.2) is used without its 1/μ² consequence (C-2).
- CONVENTIONS §10 (DC with Hadamard fp) is invoked but not followed (C-4). §7 screening is omitted (C-8). §11 K misuse (verdict 1).
- NOTATION: 𝔣_s collides with the existing 𝔣_Lin (W4-v3 §4.5), so a decoration is needed. w_e, w_N, w_c vs w_κ is flagged by the return.
  λ_ij vs the exciton λ is flagged (IF-T4).

## Summary for the coordinator
Physics core stands: the two-state reduction, STM response, the Jäckle/Black/NIBA rate family, heat release, Vineyard/Wigner.
Both source-misprint claims are CONFIRMED.

Required before REFEREED:
- (i) the (1 + m_χ/m_e)² factor and the window/core caveats on the DM-on-TLS number (≈ ×9, then O(1)–×10 uncertain);
- (ii) rewrite the pole rule with the Hadamard finite part;
- (iii) withdraw the "new" crowdion-mass claim;
- (iv) the λ-convention and energy-gap caveats on the mK window and the frozen/relaxing classes;
- (v) fix the tanδ misquote;
- (vi) downgrade crowdion coherence and ballistic recombination to [C].
