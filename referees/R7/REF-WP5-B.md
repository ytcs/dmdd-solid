# R7 referee report REF-WP5-B (hostile, isolated) on returns/R6/WP5-v2.md

Read: WP5-v2.md, code/WP5-v2/checks.py (re-run: 37/37 PASS, ~3 s), CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS, WP0-v2.
Full texts fetched and read for this report (then deleted): 2004.10709 (R&K), 2001.06503, 2209.04503, 2506.03810, 2301.06592.
Scratch numerics: sympy only, < 5 s.

## Verdict table
| # | Claim | Verdict | One-line reason |
|---|---|---|---|
| V1 | Theorem C: (W1) = master formula with carrier projectile = 2\|Im Σ^GW\| | STANDS WITH CORRECTION | Exact for the scattering-out rate; at T > 0 2\|ImΣ\| = Γ_out + Γ_in. LFE form has the wrong Coulomb index; "Im" must be the anti-Hermitian part |
| V2 | Theorem C(c): four Coulomb-line classes applied to the carrier diagram | STANDS WITH CORRECTION | Assignment is right; a condition is missing: ε_ion and g^L must use the same Z*, Q_κ, ε_∞ and range separation |
| V3 | Theorem C(a): ii, plasmon emission and plasmon decay are one channel | STANDS WITH CORRECTION | True where the plasmon lies inside the e–h continuum (Si). False for an undamped RPA pole (Al, used in §5) |
| V4 | Theorem C(e)/§6.1: Born fails, "Z_κα/v_N ≈ 3.7×10²" | STANDS WITH CORRECTION | For v_N ≪ v_F the Born parameter is Z_κα/v_F ≈ 15 (Si). The conclusion stands; the number is about 25× too large |
| V5 | (W3) backward equation; first moments = Lindhard / R&K / Kinchin–Pease, second moments = Fano | STANDS | Standard first-step analysis; checked below. The L20 observable is mis-identified (V12) |
| V6 | (B2) dilute: "pair density ≲ 10¹⁹ cm⁻³ ≪ 𝓃_e" | STANDS WITH CORRECTION | Own numbers give 7×10¹⁹–3×10²⁰ cm⁻³. Also the right comparison is the Mott/plasma density, not 𝓃_e |
| V7 | (W4) exact bookkeeping and (W14) F_eh = (ε_eh/E_g − 1)𝔡_H | STANDS | Algebraically exact given (W4) (re-derived); a tautology of the definitions, correctly labelled |
| V8 | (W14)(i)–(iii): Klein 14/5, 54/175, F ≈ 0.121/0.155 | STANDS WITH CORRECTION | Arithmetic right. (ii) and (iii) are mutually inconsistent as "leading physics" ((iii) agreeing with data is not evidence) |
| V9 | Binary threshold E_R,th ≈ 375 eV (Si), 465 eV (Ge); "linear-response stopping vanishes below" | STANDS WITH CORRECTION | Ge used k_F = 1.60 Å⁻¹, not the free-electron 1.74 Å⁻¹ → 395 eV (Si → 352 eV). "Vanishes" is jellium-only; in a crystal it is suppressed |
| V10 | (W15) TV bound on the GaAs 𝔉 term; estimate \|ΔP\| ≲ 0.11 Γ/δ | STANDS (bound) / STANDS WITH CORRECTION (estimate) | Bound derived correctly. The estimate imports the **Si** Γ/δ map and an [UNVERIFIED] phase; the spread 0.36 is not derived |
| V11 | Migdal drag-energy subtraction in GS seeds | STANDS WITH CORRECTION | Moments agree with WP0-v2 (6.2)(iii). "Rescale the first moment" is not an operation on S. C20b and C20c are vacuous |
| V12 | L20 URF chain (Lindhard / 2209.04503) | STANDS WITH CORRECTION | ν ≠ ℋ + E_st: carrier-relaxation heat is in ℋ but not in Lindhard's ν. Truncation (A) is then not "exact". U is misassigned |
| V13 | L21 chain (R&K, step model) | STANDS (minor correction) | Phase space 2π/105 verified; "never accurate beyond ω < 2E_g" does not follow from n̄ ≳ 2 (that is ω ≳ 7.5 eV) |
| V14 | Claims against R&K (units of A; \|M\| vs \|M\|²; Δ; App. A Fano formula, "lower bound") | see §C | A units CONFIRMED; \|M\|² CONFIRMED; "Δ undefined" REFUTED (defined in words, units fix it); App. A CONFIRMED but the argument for the bound direction proves the wrong inequality |
| V15 | Claims against 2001.06503 / 2209.04503 | see §C | Reduced energy 10%: CONFIRMED. Boundary-condition inconsistency: CONFIRMED. "½εS_e not derived": REFUTED as worded (2001.06503 App. B). Migdal-in-U: CONFIRMED |
| V16 | Claims against 2506.03810, 2301.06592 | CONFIRMED | Quotes verified in full text |
| V17 | (W8) CSDA survival; (W9) IA Doppler width σ_ω² = 4E_R E^kin | STANDS | Re-derived |
| V18 | L23 asymptotics n̄ = ω/ε_eh + b_N + o(1) "[D, renewal theorem]" | STANDS WITH CORRECTION | Needs a non-arithmetic (non-lattice) loss kernel. The (R-k) Einstein-ω₀ truncation is lattice-like, which leaves a periodic term |
| V19 | Checks "37, all PASS" | STANDS WITH CORRECTION | Reproduced. C1c, C7b, C14e, C20b, C20c are tautologies or arithmetic restatements, not checks |
| V20 | §11 Contested corrections: "None" | n/a | Nothing to adjudicate |

## A. Theorem C and the Coulomb-line classes (focus g)

**A1 (V1). The rate.** CONVENTIONS §6 gives S_chch = (2q²/e²)L/(1 − e^{−βω}), so |v_C ρ|²S_cc = 2v_C|ρ|²L/(1 − e^{−βω}) (C13 is correct).
The golden-rule normalisation with S per volume (CONVENTIONS §6, (2π/V)Σ) gives Γ = ∫d³p/(2π)³|𝒱|²S; I re-derived this from
H_int = V⁻¹Σ_p v_C(p)ρ_proj(−p)ρ_med(p). Two corrections follow.
- (i) The GW identity. With 1/(1 − e^{−βω}) = 1 + n_B(ω), (W1) is Γ_out = Σ∫2v_C|ρ|²L(1 + n_B)(1 − f′). But
  2|ImΣ_nk| ∝ Σ∫2v_C|ρ|²L[1 + n_B(ω) − f′] = Γ_out + Γ_in, with Γ_in ∝ n_B f′. So "(W1) is 2|ImΣ^GW|" holds only at f′ = 0 or T = 0.
  For hot conduction electrons this is harmless. For holes written in electron language (f′ ≈ 1) the statement must use hole
  occupations. Reword it as "(W1) = Γ_out; 2|ImΣ| = Γ_out + Γ_in."
- (ii) Local fields. With WP0-v2's ε⁻¹_{GG′} = δ + v_C(p+G)R_{GG′}, the screened interaction is W_{GG′} = ε⁻¹_{GG′}v_C(p+G′). The kernel is
  Σρ*_G ε⁻¹_{GG′}v_C(p+G′)ρ_{G′}, not "ρ*_G v_C(p+G) Im(−ε⁻¹_{GG′}) ρ_{G′}". For a non-centrosymmetric target (GaAs), "Im" must be the
  anti-Hermitian part (W − W†)/2i, not the element-wise Im; this is the same issue as WP0-v2 CC-1.
- (iii) Notation. "Γ_{nk→n′,k−p} = ∫d³p…" integrates over the variable that labels the final state. Write the integrand as the
  differential rate.

**A2 (V2). Classes.** The WP0-v2 (5.5) classification is for O(g²) diagrams with one phonon line. Carried over to the carrier, the
assignments are correct:
- the O(g⁰) carrier kernel has only the external class;
- the phonon pole of the total ε gives the ionic/Fröhlich emission;
- the DFPT class is (W2);
- the pair class is phonon-assisted ii, O(g²W).

The double-counting argument (one Coulomb line, assigned once) is right. What is missing is the operational condition that makes it
true: ε_ion(p,ω) in (W1) and g^L subtracted in (W2) must be the same object. That means the same Z*_κ, the same quadrupoles Q_κ (§1.1
says Si quadrupoles are "included" in g), the same ε_∞, and the same range-separation and G-sum convention. Otherwise the subtraction
leaves a residual at p = Q + G ≠ Q. Add this as an O4-d2-type requirement.

**A3 (V3). Plasmons.** Im[−1/ε] = ε₂/|ε|². Where ε₂(ω_pl) > 0 (Si, interband), the plasmon peak is e–h weight, and (a) holds.
For q < q_c in a nearly-free-electron metal in RPA, the pole is undamped. Its spectral weight is then a δ-function with no e–h final
state at that order, and its decay is interband or beyond-RPA (two-pair). §5 asserts "(W1) applies unchanged, including the Al plasmon".
That needs either an explicit plasmon decay channel or a proof that the damping is interband at the relevant q. Consequence (a) should
be restricted to "pole inside the e–h continuum".

**A4 (V4). Born parameter.** For a slow ion in an electron gas, the electrons hit the ion at the relative velocity ≈ v_F. Lindhard
dielectric stopping is the Born limit in Z_κe²/ħv_F, not in Z_κe²/ħv_N. Si: Z_κα/v_F = 14.6, against the quoted 3.7×10². It is still
≫ 1, so "S_e ∝ v_N is a fit at keV" survives. The number must be replaced in §1.1(e), §6.1 Validity and C6.

**A5 (V5). (W3) and moments.**
- *First moment.* Differentiating (W3) at ϑ = 0 gives Γ_x m_x = Σ_c∫𝒦_c[δ𝐍_c + Σ_j m_{x′_j}]. Lindhard's Eq. (3) of 2001.06503 is exactly
  this form, with ∫dσ_{n,e} as a rate per unit path and terminal state ν̄(0) = 0. R&K Eq. (5), n = 1 + ∫dE P⟨N⟩, is the first moment of
  e^{ϑ_N}𝔊_e𝔊_h. I verified that R&K normalise P to 2 ("one electron and one hole"), so the single integral covers both carriers.
- *Second moment.* This is Var = E[Var | first step] + Var(E[· | first step]), plus zero sibling covariance by (B2) (C9 is the
  one-step case).

## B. (B2), bookkeeping, Fano (V6–V8, V18)
- **(B2).** 300 pairs in a sphere of radius 10 nm gives 7.2×10¹⁹ cm⁻³; in a 10 nm cube, 3×10²⁰ cm⁻³. Neither is "≲ 10¹⁹". Comparing with
  𝓃_e (2×10²³) does not test what (B2) neglects: Pauli blocking between cascade carriers and carrier–carrier Coulomb/Auger scattering.
  The scale for those is the e–h plasma screening (Mott) density, ~4×10¹⁸ cm⁻³ in Si [E]. That density is exceeded inside a keV
  track. (B2) is therefore an assumption whose error is unestimated at ≳ keV deposits; state it as such.
- **(W14).** Set N = (ω − ℋ)/E_g with E_st = E_esc = 0. Then Var N = Var ℋ/E_g², F_eh = Var ℋ/(E_g² n̄), ε_eh = E_g + ⟨ℋ⟩/n̄, and
  (ε_eh/E_g − 1)𝔡_H = (⟨ℋ⟩/(n̄E_g))·Var ℋ/(E_g⟨ℋ⟩) = F_eh. Exact.
- **Klein.** pdf ∝ √t on [0, a]: ⟨t⟩ = 3a/5, Var t = 12a²/175. With a = 3E_g/2: ε = E_g + 2(9/10)E_g = 14E_g/5, and
  F = 2Var t/E_g² = 54/175. Both are correct.
- **(ii) versus (iii).** (ii) says residual noise alone gives 0.31, 2.6× the data, so anti-correlation is essential. (iii) then adds a
  Poisson phonon term alone and gets 0.121. The two estimates cannot both be "leading"; (iii) ignores the residual term entirely. The
  Si agreement in (iii) carries no evidential weight; say so more strongly, or drop the number.
- **(V18) Renewal theorem.** The key renewal theorem needs a non-arithmetic inter-renewal law. With the (R-k) one-mode ω₀ kernel plus a
  fixed E_g, the losses lie on a lattice generated by {ω₀, E_g}. When that lattice is arithmetic, n̄(ω) − ω/ε_eh keeps a periodic
  component. Add "non-lattice kernel" to the hypotheses. The full band-structure kernels satisfy it generically.

## C. Claims that published papers are wrong (rubric c), verified against full text

**2004.10709 (R&K).**
1. *Units of A.* Eq. (8): Γ_ph/Γ_eh = A(105/2π)(E − ħω₀)^{1/2}/(E − E_g)^{7/2}; Table I: "A = 5.2 eV²". For a dimensionless ratio,
   [A] = E^{7/2−1/2} = E³. **CONFIRMED.** Eq. (9) with a dimensionless |M_ph|/|M_eh| and Δ a real-space volume does give E³, so the "eV²"
   is the error, not Eq. (9).
2. *|M| vs |M|².* Eq. (9) prints A = (|M_ph|/|M_eh|)(4π⁴/VΔ)(ħ²/2m)³ (HTML alttext checked). A ratio of golden-rule rates goes as |M|².
   **CONFIRMED.**
3. *"Δ undefined."* The text says "Δ is the volume per electronic state". Dimensional consistency of Eq. (8) forces the real-space
   reading (VΔ ~ L⁶). **REFUTED as worded**: Δ is defined, if loosely.
4. *App. A* (PDF (A1)–(A7) = HTML (19)–(23); WP5's "(22)–(23)" uses the HTML numbering). R&K write σ²_meas = F·n + ηn(1 − η), so
   F_meas ≈ F/η + 1 − η. Binomial thinning gives exactly Var n_meas = η²Fn + η(1 − η)n, so F_meas = ηF + 1 − η. **CONFIRMED.**
   - *The "lower bound" claim, where WP5's argument is wrong.* R&K say their approximation "makes this estimate a lower bound on the
     measured Fano factor". The relevant inequality compares R&K's formula with the exact one: F/η + 1 − η − (ηF + 1 − η) = F(1/η − η)
     ≥ 0. R&K's expression is therefore an **upper** bound on the exact F_meas, and their "lower bound" is wrong. WP5 instead cites
     F_meas − F_eh = (1 − ϵ)(1 − F) ≥ 0 (C2d). That inequality, measured ≥ intrinsic, says nothing about the direction of R&K's
     approximation. The verdict is right, but the stated reason must be replaced by the F(1/η − η) ≥ 0 inequality.
   - *Numbers.* R&K's 0.130 at η = 0.98 matches the exact formula with F = 0.112 (0.1298), the lower end of their Fig. 10 band. With
     F = 0.115 the exact value is 0.1327. Their own (A7) gives 0.134–0.137 and 0.168–0.171. WP5's "close to exact" holds.
5. *Symbol collision E_r* (Eqs. (5) vs (15)–(16)): **CONFIRMED.** Not raised by WP5: R&K also quote C ≈ 2.2–2.9 "eV" for a
   dimensionless C in Eq. (16).
6. *"Temperature only through E_g(T)"*: **CONFIRMED** ("purely through the variation of the gap energy", Eq. (11)).

**2001.06503 / 2209.04503.**
1. *Reduced-energy conventions.*
   - 2001.06503 uses c_Z = 11.5/Z^{7/3} keV⁻¹ (Si 0.0243).
   - 2209.04503 uses C = 16.2616/(ZZ₁Z₂), with Z = Z₁^{0.23} + Z₂^{0.23}, and Z₁ = 12 as "the effective number of valence electrons in the
     incident ion" (a stripping argument). This gives 0.0268 keV⁻¹.

   **CONFIRMED.** With Z₁ = 14 the ZBL value would be 0.0226; the 10% difference is driven by Z₁ = 12. Wording: "stripped Si ion" →
   "Bohr-stripped effective Z₁".
2. *Boundary-condition inconsistency* (ν̄′_L → 1 imposed, versus 0 from L'Hôpital on Eq. (5)): stated in 2001.06503. **CONFIRMED** as a
   correct quote.
3. *"½εS_e not derived in the text."* 2209.04503 says "following the arguments in [5]". [5] = 2001.06503, which derives the term in its
   App. B (Eqs. (28)–(29)): the mean-value theorem with t̄_n ≈ ⟨ε sin²(θ/2)⟩ = ε/2. **REFUTED as worded.** A sharper objection that WP5
   should make instead:
   - the cross term ∫dσ_{n,e}T_nΣT_e vanishes identically under approximation (D)/(III), "nuclear and electronic collisions
     separately", because no single event has both T_n ≠ 0 and T_e ≠ 0;
   - the ½εS_e term therefore contradicts the approximation used to obtain S_e;
   - the ε/2 average is unweighted by dσ_n, which is strongly forward-peaked.

   The straggling coefficient ½W is consistent with the expansion. I checked the sign: +½ν̄″(ΣT_e)² moves to −½Wν̄″ on the LHS.
4. *"U effectively incorporates the Migdal effect"*: **CONFIRMED** in 2209.04503, and stated identically in 2001.06503. The
   double-counting rule follows logically.
5. *Lindhard's hand-inserted Z^{1/6} (1.55 for Si)*: **CONFIRMED** (2209.04503).
6. *Validity ranges* (𝓔_red ≳ 0.1 ≈ 4 keV Si; ≳ 0.00088 ≈ 250 eV Ge) and *χ²/dof = 1870/101, 680 eV–3 MeV*: **CONFIRMED.**
7. *Missed by WP5.* In both papers f_n = (ε + u − ν̄)/(ε + u) counts u in the **electronic** fraction. 2209.04503 identifies u at low E
   with U_FP, the Frenkel-pair creation energy, which is a lattice stored energy. Counting U_FP as ionization is a source inconsistency
   that the URF (E_st ≠ charge) should flag. Near threshold it inflates f_n by up to u/(ε + u).

**2506.03810.** "halted when the energy of the most energetic atom falls below 10 eV_nr, as no ionization occurs below this
threshold", with Eq. (3) friction F_i = F_0i − (v/|v|)S_e(E). **CONFIRMED.** The [E] inference (sub-keV ionization is a friction-model
property) is fair.
**2301.06592.** v_min = √(2m_nE_r)/(2μ_{m_D−N}) needs the nucleus mass, while m_n is the nucleon in μ_{m_D−n} (Eq. (5)). "E_th …
assumed to be correlated with the threshold displacement energy." **CONFIRMED** (notational, and an unphysical identification).

## D. Thresholds, (W15), Migdal (V9–V11)

**D1 (V9).** Head-on scattering of a heavy ion (v_N) off an electron (v_F) transfers at most 2m_e v_N(v_N + v_F). Dropping v_N² gives
v_th = E_g/(2m_e v_F) and E_R,th = ½M v_th². Correct form.
- *Inputs.* C5 hard-codes k_F(Si) = 1.75 and k_F(Ge) = 1.60 Å⁻¹. The free-electron values for 4 e/atom are 1.808 (a = 5.431 Å) and
  1.736 Å⁻¹ (a = 5.658 Å). These give **352 eV (Si), 395 eV (Ge)**, or 336/382 eV keeping v_N². The Ge 465 eV is not the
  "free-electron v_F" value claimed. The 2405.10405 statement (254 eV_nr below threshold) survives.
- *"Vanishes".* "Below E_R,th the linear-response electronic stopping in a gapped crystal vanishes" is true for gapped jellium: L(k,ω)
  is supported in |ω − k²/2m| ≤ kv_F, which together with ω ≤ kv_N gives ω ≤ 2m v_N(v_N + v_F). In a crystal, L(k,ω ≥ E_g) has support
  at all k (Umklapp, and the high-momentum tails of valence states orthogonalised to the cores). The stopping is therefore suppressed,
  Compton-tail limited, but not zero. The threshold is soft, and the "sign-definite switch-off" in §6.1(a) should be "strong
  suppression".

**D2 (V10).**
- *Bound.* ΔP = Σ_ν(𝔉_ν/Γ^tot)P_ν. With Σ𝔉_ν = 0: |ΔP| ≤ Σ|𝔉_ν|/Γ^tot · ½·spread. Also Σ|𝔉_ν| = 2πΣΓ^{(ν)}|c̄ − c_ν| ≤ 4πΓ^ph max|c|.
  Both inequalities of (W15) hold.
- *Estimate.*
  - "Γ/δ ≈ 0.02 … 0.6" is WP0-v2's **Si** map (O4-d11); no GaAs map exists.
  - The phase |sin φ| ≲ 0.3 rests on an [UNVERIFIED] form-factor ratio and a heuristic identification.
  - "Spread ≲ 0.36" is 36 meV/0.1 eV. At the 1e⁻/2e⁻ boundary P_ν(N) can jump within the ii-onset width, which is not shown to be
    ≳ 0.1 eV.

  The only defensible statement is the rigorous |ΔP| ≤ 2π(Γ^ph/Γ^tot)max|c_ν^F|·spread ≤ 2π max|c_ν^F|, with 0.11Γ/δ an order-of-magnitude
  [E]. The θ_𝔉 prior in §8 should carry the bound, with 0.11Γ/δ as its central value at most.
- *Not addressed.* K_ν = (Γ^{(ν)} + 𝔉_ν)/Γ^tot can be negative. The cascade sampler needs a signed-weight or mixture scheme.

**D3 (V11).** The moments are consistent with WP0-v2 (6.2)(iii): GS first moment q²/2M − q·δM·q/2M², zeroth moment depleted by P_Mig.
Defects:
- *Not an operation on S.* "Rescale the first moment by 1 − δM/M" does not define a transformation of S^GS. A multiplicative rescaling
  of S changes the zeroth moment by the same factor. But P_Mig(q) ∝ q² while δM/M is q-independent, so no single rescaling achieves
  both. The consistent implementation is M_κ → M_κ + δM_κ in the harmonic GS response, then normalisation (1 − P_Mig), checked against
  both moments.
- *Size.* At δM/M ≤ 2.7×10⁻⁴ the effect is far below every listed nuisance. Say it is negligible rather than prescribing a procedure.
- *Checks.* C20b defines f_GS as q²/2M − E_Mig and then verifies that the sum is q²/2M. C20c is x − x = 0. Neither tests anything.

## E. L20–L23 chains (rubric b)

**L20 (V12).**
- *Observable.* WP5 sets "observable ν = ℋ + E_st", but (W4) puts all carrier-relaxation heat (≈ (ε_eh − E_g)/ε_eh ≈ 70% of E_el) into
  ℋ. Lindhard's ν̄ is the energy reaching atomic motion **through nuclear collisions only**. The identification must be ν = ℋ_nuc + E_st,
  where ℋ_nuc is the heat from the ion branch excluding the electronic sub-cascade.
- *Truncation (A).* Truncation (A) drops Σϕ̄_e, the electrons' contribution to ν. It is exact for that ν only by definition. It is
  **not** "exact below the 4m_eE/M_κ bound": that bound excludes displacements by electrons, not phonon emission by electrons, which is
  the dominant electron→lattice channel.
- *U.* "(+ U_bind)" in ν contradicts the source's QF definition, where u sits in η (C.7). State the URF assignment (U_FP → E_st,
  inner-shell excitation → electronic) and note the source inconsistency.
- *Born-parameter number.* As V4.
- *Reduced energy.* The 10% discrepancy is right (C10 reproduces it).

**L21 (V13).**
- *Phase space.* The three-body random-k phase space ∫√x√y√z δ(E′ − x − y − z) = Γ(3/2)³/Γ(9/2)E′^{7/2} = (2π/105)E′^{7/2}. Verified
  (C1a,b). This is the origin of 105/2π, and the 7/2 power fixes [A] = E³.
- *Step model.* The step-model mean (ω − E_g)/ε_eh + ½ and b_N = 0.188 are correct. But "fails for n̄ ≳ 1/(4F) ≈ 2, so never accurate
  beyond ω < 2E_g" is self-contradictory: n̄ ≈ 2 is at ω ≈ 2ε_eh ≈ 7.5 eV. Also √(F n̄) ≳ ½ is a heuristic, not a derived failure point.
- *Seed envelope.* "Bounded by R&K's own α envelope (≤ 50% in p₂)" uses a photon-seed model family to bound the DM-seed difference. A
  DM seed at q ~ keV need not lie inside the photon-Beta family. Mark it [E] and do not use it as a prior bound.

**L22.** NRT 0.8E_dam/2E_d and f_DF ≈ p_surv·0.4(E_dam/E_R)E_st,1/E_d are consistent. The σ ≈ √(E_d⟨ω⟩) ≈ 0.95 eV step width follows from
(W9), but it is the Doppler width of the seed energy only. The PES-intrinsic (direction-averaged, thermal-lattice) contribution to
the width is not estimated, so "~1 eV, predicted, not tuned" is a lower bound. The "Validity" line borrows ξ_Mas ≈ 15 at 20 eV, which
is right (C6).

**L23.** Source quotes are verified: Eq. (3), Eq. (16) with C ≈ 2.2–2.9, and F_∞ = 0.115. F_NR = F_eh + Var(E_el)/(ε_eh⟨E_el⟩) follows
from the law of total variance. The 25 keV numbers (E_el = 9.1 keV, σ/E ≈ 10%) are reproduced. On F_meas, see C.4 (reason to be
replaced).

## F. Consistency (rubric d) and gap closure (rubric e)
- *(d) Matches.* S_cc ≡ S_chch (CONVENTIONS §6) ≡ S_zz (WP0-v2 (5.4)): consistent. E^{Mig}_1, δM_κ and P_Mig match WP0-v2 (6.2)(iii).
  (W6) = WP0-v2 (7.3) verbatim. The (7.2) retarded out-state weight is cited correctly.
- *(d) The one inconsistency.* §1.5's Γ/δ values are WP0-v2's Si values, used for GaAs.
- *(e) G1.* Closed by formula plus specification (bands, W, ii kernel, EPW kernel, solve, validation). The spec is sufficient, but it
  inherits V1(ii) (the LFE index) and V2 (the g^L/ε_ion consistency condition), which must be written into the ii and e–ph kernel items.
- *(e) G3.* Specification sufficient. The charge channel below threshold rests on adiabatic-XC TDDFT and is correctly listed as an exact
  gap (R3).
- *(e) G12.* The kinetics spec is sufficient, but the e^{−E/E_slope} spectrum and the mK regime are [C] and correctly not claimed.
- *(f)* No contested corrections.

## Required corrections (minimal list)
1. V1: "(W1) = Γ_out; 2|ImΣ| = Γ_out + Γ_in". In the LFE kernel use ε⁻¹_{GG′}v_C(p+G′), and the anti-Hermitian part in GaAs.
2. V2: add the ε_ion ↔ g^L identity requirement (Z*, Q_κ, ε_∞, range separation).
3. V3: restrict consequence (a); in §5 give the Al plasmon a decay channel or argument.
4. V4/V12: Born parameter Z_κα/v_F ≈ 15 (Si) in §1.1(e), §6.1, C6.
5. V6: correct the density (≳ 10²⁰ cm⁻³ locally) and compare with the Mott density; (B2) error unestimated at ≳ keV.
6. V9: free-electron k_F → 352 eV (Si), 395 eV (Ge); "vanishes" → "suppressed (crystal L has Compton tails)".
7. V10: Γ/δ for GaAs is unknown; quote the rigorous bound, keep 0.11Γ/δ as [E] only; handle negative K_ν.
8. V11: implement as M → M + δM plus (1 − P_Mig); call it negligible; delete or replace C20b, C20c.
9. V12: ν = ℋ_nuc + E_st; truncation (A) is not justified by the 4m_eE/M bound; fix the U assignment and add C.7.
10. C.3: replace "not derived" by the (D)-inconsistency objection. C.4: replace the C2d argument by F(1/η − η) ≥ 0. C.3 (R&K Δ): withdraw "undefined".
11. V8, V13, V18: make (ii)/(iii) consistent; fix the step-model failure region; add non-lattice to the renewal hypotheses.
