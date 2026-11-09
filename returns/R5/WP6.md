# R5 / WP6: rate assembly and uncertainty quantification

Isolated theory agent, working in the read scope set by the brief. Theory only. The identity checks are in
`code/WP6/checks.py`: 16 checks, all PASS, in under 60 s. They are algebra and quadrature of closed forms, with no simulation.
Literature (§10): full text [FT] was read for 1509.01598, 2311.04957, 2105.00599, 2011.12896, 1011.1915 and 2101.08275. Every
other ID was checked against the arXiv API. Tags: **[D]** DERIVED (hypotheses stated), **[E]** ESTIMATED, **[C]** CONJECTURED.
Notation follows NOTATION v2 / WP0 §10, and WP0 equations are cited as WP0 (s.n). Assigned work: L24, G4 and G8.

---
## 1. Rate assembly from WP0 (3.4): the general halo functional

**(1.1) On-shell kinematics [D].** Hypotheses: WP0 (3.3)–(3.4) (Born approximation, Gibbs target state, unpolarised DM) and a lab-frame
velocity distribution f(v). With ω_q from WP0 (2.1),

  δ(ω − ω_q) = q^{-1} δ(q̂·v − v_min),   v_min(q,ω) = (ω + Δ_χ)/q + q/2m_χ.                                          (1.1)

On shell, write v = v_min q̂ + v_⊥ with q̂·v_⊥ = 0. The DM-side velocity of WP0 (2.1) is then v_χ = v − q/2m_χ = u_∥ q̂ + v_⊥,
with **u_∥ = (ω+Δ_χ)/q fixed by kinematics**. The halo enters only through the transverse velocity v_⊥.

**(1.2) Velocity polynomial [D].** Every Fitzpatrick operator is at most linear in v^⊥ (WP0 (2.2)–(2.3)). So 𝒱_a is affine in v_χ, and
𝔇_ab (WP0 (2.3)) is a polynomial of degree ≤ 2 in v_⊥: 𝔇 = 𝔇⁽⁰⁾ + 𝔇⁽¹⁾_c v_⊥^c + 𝔇⁽²⁾_cd v_⊥^c v_⊥^d, with u_∥ absorbed into the
coefficients. Inserting this in WP0 (3.4):

  dR/dω = (ρ_χ/m_χρ_T) ∫d³q/(2π)³ q^{-1} Σ_{n=0}^{2} tr[𝔇⁽ⁿ⁾(q,ω) S(q,ω)] · f̂⁽ⁿ⁾(q̂, v_min),
  f̂⁽ⁿ⁾(q̂,u) ≡ ∫d³v f(v) v_⊥^{⊗n} δ(q̂·v − u).                                                                           (1.2)

f̂⁽⁰⁾ is the Radon transform of f (Gondolo, hep-ph/0209110 [ABS]). (1.2) is the most general halo object for any operator class, any
anisotropic target and inelastic DM. **Halo independence in the strict sense means bounding f̂⁽⁰⁾, f̂⁽¹⁾ and f̂⁽²⁾, not η.**

**(1.3) Isotropic reduction [D].** Hypothesis (I): the S entering (1.2) is angle-averaged (S → S̄(|q|,ω)), or the target is isotropic.
After the DM-spin trace, 𝔇⁽¹⁾ can be built only from q̂, and q̂·v_⊥ = 0, so the n = 1 term drops. The q̂-averages are:
- ⟨δ(q̂·v − u)⟩_q̂ = Θ(v−u)/2v (C10a);
- ⟨|v_⊥|²δ⟩_q̂ = (v²−u²)Θ(v−u)/2v (C10b).
The rate therefore needs only

  η(u) = ∫d³v f(v) Θ(v−u)/v,    ξ(u) = ∫d³v f(v)(v²−u²) Θ(v−u)/v,    **dξ/du = −2u η(u) ⇒ ξ(u) = 2∫_u^∞ u′η(u′)du′.** (C12)  (1.3)

The boundary term vanishes because the integrand of ξ is zero at v = u. **So velocity-dependent operators add no new halo freedom
under (I): ξ is a functional of η.** The resulting rate is

  dR/dω = (ρ_χ/4π² m_χρ_T) ∫ q dq [A₀(q,ω) η(v_min) + A₂(q,ω) ξ(v_min)],   A₀ = Σ_ab 𝔇⁽⁰⁾_ab S̄_ab,   A₂ = Σ_ab d₂,ab S̄_ab,      (1.4)

where 𝔇⁽²⁾_cd v_⊥^c v_⊥^d ≡ d₂|v_⊥|² (the q̂q̂ part of 𝔇⁽²⁾ annihilates v_⊥). Check: for n_e alone, A₀ = |Ṽ|²S̄ = πσ̄_eF²S̄/μ²_χe, and
(1.4) becomes exactly WP0 (9.2): ρ_χσ̄_e/(4π m_χρ_Tμ²_χe)∫q dq F²ηS̄, with 𝒢 = η/2q (confirmed). WP0's
hypothesis "isotropic f_χ" is stronger than needed: the lab-frame SHM is anisotropic, and (I) on S is what is used (§9, W5).

**(1.5) Anisotropic targets [D].** For a crystal with point group P, time reversal gives S(q) = S(−q). The direction dependence of S
expands in the even-ℓ harmonics invariant under P. For O_h (Si, Ge, GaAs at the level of S_ee), the invariant harmonics are ℓ = 0, 4, 6, 8, 10
and two at ℓ = 12 (C11, character formula). The rate (1.2) is then Σ_ℓ ∫ S_ℓ(q,ω) f̂⁽⁰⁾_ℓ(v_min). **The first correction to the
η-only rate is ℓ = 4 (a cubic harmonic)**, and there is no ℓ = 2 term. This fixes the library compression in §7.

**(1.6) Conventions dictionary [D] (C1–C3).** With S̄ the angle-averaged S_ee of WP0 (3.1), spin included:

  |f_crystal(q,ω)|² = Ω q³ S̄_ee(q,ω)/(4π α m_e²)                       [1509.01598 eq. (21)/(64) normalisation]
                    = Ω q⁵ L̄(q,ω)/(8π² α² m_e²)   (T = 0, ELF form WP0 (5.4)/(9.3); unscreened: L → ε₂)   [= 2101.08275 eq. (16)]
  |f_res(q,ω)|²     = (8α m_e² ω/q³)|f_crystal|² = 2Ωω S̄_ee/π           [2311.04957 eq. (4)]                                  (1.5)

Rate normalisations: 1509.01598 eq. (17) is per target (×N_cell); 2311.04957 eq. (3) is **per unit cell** (C3; see §2.5 D1); WP0 (9.2) is
per unit target mass. Library tables carry Ω S̄ (per cell, units eV⁻¹), so that all three follow by fixed factors.

**(1.7) Measured observable [D given WP0 (7.2)].** μ_i = 𝔈_i ∫dω ∫d³q (…) Σ_Λ S(q,ω;Λ) P_det(i | N_eh) P_casc(N_eh | Λ), where 𝔈_i is
the exposure times efficiency. **μ_i is linear in S, and therefore linear in η (or in the f̂⁽ⁿ⁾).** The halo-independent and nuisance
machinery below rests on this linearity.

---
## 2. L24 derived: SHM rate with η(v_min), and halo-independent bounds

**(2.1) Source formulas [FT].**
- *1509.01598 eq. (17):* dR_crystal/d ln E_e = (ρ_χ/m_χ) N_cell σ̄_e α (m_e²/μ_χe²) ∫ d ln q (E_e/q) η(v_min(q,E_e)) F_DM(q)² |f_crystal(q,E_e)|².
  Also eq. (15), η(v_min) = ∫ d³v g_χ(v) Θ(v − v_min)/v, and eq. (16), v_min = E_e/q + q/2m_χ. SHM: eq. (65),
  g_χ ∝ e^{−|v+v_E|²/v₀²}Θ(v_esc − |v+v_E|), with K given by eq. (66) and the closed forms η₁, η₂ by eq. (68). Values used there: v₀ = 230,
  v_esc = 600, v_E = 240 km/s, ρ_χ = 0.4 GeV/cm³.
- *2311.04957 eqs. (9)–(11), (13), (19)–(20):* dR/d ln E_e = (8μ²_χe)^{-1}∫dq q |F_DM|²|f_res|² η̃(v_min), with η̃ = (ρ_χσ̄_e/m_χ)η and
  the step ansatz η̃ = Σ_i η̃_i Θ(v_i − v_min). Binned rate (13) uses n_e = 1 + ⌊(E_e − E_gap)/ε⌋ (12). The linear map is
  R_i = Σ_j 𝒜_ij η̃_j (19), with 𝒜_ij given by (20). Values used there: SHM v₀ = 220, v_esc = 544, v_E = 232 km/s, ρ_χ = 0.4.

**(2.2) Truncation chain from WP0 [D].**
1. WP0 (3.4).
2. Single operator n_e (L0 chain, WP0 (9.1)); Δ_χ = 0.
3. Hypothesis (I) of (1.3): S → S̄, giving η(v_min)/2q (C10a; WP0 (9.2)).
4. f = SHM (1509.01598 eq. (65)), giving η₁ and η₂ of eq. (68) (closed form verified against quadrature to 10⁻¹³, C4a).
5. Conventions dictionary (1.5), which gives 1509.01598 eq. (17) exactly (C1).
6. Optionally, P_casc(N_eh|Λ) → step model (L21's Λ-marginalised kernel, WP0 (7.3)), which gives 2311.04957 eq. (13).
7. Step basis for η̃, which gives (19)–(20).

As a τ point (WP0 (6.1)), L24 is the L1 truncation (n_B = 0, X = IP, no screening) composed with the halo choice. Every WP1–WP3 upgrade
of S enters only through S̄ in step 3.

**(2.3) Validity conditions, with numbers [D/E].**
- (V1) *Born:* |Ṽ|μ_χe q/4π ≪ 1. This holds by many orders for σ̄_e ≲ 10⁻³⁰ cm² [E].
- (V2) *Only O₁:* the other 𝔇_ab are suppressed by v² ~ 10⁻⁶ or (q/m_e)² ~ 10⁻⁴–10⁻³ at q ~ 1–4 αm_e [E]. Under (I) they would enter
  only through ξ, which is fixed by η (1.3).
- (V3) *Angle average:* for O_h targets the first neglected term is ℓ = 4 (1.5). Its size on the day-averaged rate is [E] a few % in the bulk
  and larger near the edge (daily-modulation studies 2607.06005 and 2411.03433, titles verified only).
- (V4) *Time-averaged v_E:* the 2105.00599 inputs give |v_⊙| = 250.5 km/s and an Earth speed of 237–266 km/s, mean 252.1 (C6). The
  sensitivity is ∂ln η/∂v_E = 0.013 per km/s at v_min = 600 and 0.061 per km/s at v_min = 760 (C4). So the annual ±15 km/s is ±19% at
  v_min = 600 and a factor ≈ 2.5 at the edge [D for the SHM].
- (V5) *SHM shape with a hard cutoff:* this sets the edge exponent (§3).
- (V6) *T > 0 branch:* the ω < 0 weight is e^{−E_g/T}, which is negligible.
- (V7) *No Earth stopping:* this fails at the large-σ ceiling. WP6 does not quantify it.
- (V8) *S_ee clamped-lattice IP* (L1). The ELF form needs WP0 (5.5)(i) or (ii).

**(2.4) Leading corrections the URF predicts [D].**
- (a) Anisotropy: η/2q → f̂⁽⁰⁾(q̂,v_min)/q in (1.2). The first term is ℓ = 4, with coefficient S_4(q,ω) × the ℓ = 4 moment of the lab-frame
  Radon transform. This links L24 to L19.
- (b) Velocity-dependent operators: the A₂ξ term of (1.4), where ξ = 2∫u′η du′. This requires no new halo input.
- (c) Halo tails beyond the SHM change the edge exponent (§3.4).
- (d) Annual modulation (V4).
- (e) Yield: P(n_e | Λ) replaces P(n_e | ω) (WP0 (7.2)). This is the G1 hand-off to WP5.
- (f) Theory nuisances θ enter 𝒜_ij linearly or log-linearly (§5).

**(2.5) Discrepancies in the sources [D].**
- **D1** 2311.04957 eq. (3) equals 1509.01598 eq. (17) *without* N_cell (C3). It is a rate per unit cell, and the text does not say
  so. The step heights η̃_i (17) are quoted in yr⁻¹, which absorbs the target size. Recasts must restore N_cell.
- **D2** 2311.04957 eq. (13) integrates q over [q₋, q₊] *and* multiplies by Θ(v_i − v_min). q± (7) depend on a speed that is not
  specified, and the Θ already enforces kinematics. The consistent form is ∫₀^∞dq … Θ(v_i − v_min(q,E_e)), or equivalently
  q ∈ [q₋(v_i), q₊(v_i)] for each step.
- **D3** Halo conventions are mixed:
  - 1509.01598: 230/600/240, ρ_χ = 0.4;
  - 2311.04957: 220/544/232, ρ_χ = 0.4;
  - 2105.00599: v₀ = 238, v_esc = 544, v_⊙ = (11.1, 12.2, 7.3), ⟨|v_⊕|⟩ = 29.8, ρ_χ = 0.3;
  - **NOTATION.md: v_E = 250 and ρ_χ = 0.4.** NOTATION's v_E = 250 is |v₀ + v_⊙| = 250.5, the Sun's speed. The annual-mean Earth
    speed is 252.1 (C6). NOTATION's ρ_χ = 0.4 differs from the 2105.00599 recommendation of 0.3, a pure rescaling but a convention clash.
- **D4** In 1509.01598, eq. (67) writes the exponent with −2vv_E c_θ, while eq. (65) implies +2vv_E c_θ. This is harmless, since the
  integral is over a full range symmetric under c_θ → −c_θ.
- **D5** Gap in the step model: 2311.04957 uses E_gap = 1.2 eV, while scissor-corrected codes use about 1.11–1.12 eV. That moves
  m_min by 12% (0.358 vs 0.319 MeV, C7) before any halo difference.
- **D6** 2105.00599 §3.1 recommends that SHM parameters be **fixed, not profiled**: "quoted uncertainties … [do not] represent likelihood
  distributions that can be meaningfully profiled over" [FT]. 2011.12896 instead shows bands from varying v_esc = 528⁺²⁴₋₂₅ and
  v₀ = 233 ± 6 [FT]. §6 reconciles the two by reporting separate objects.

**Status L24: DERIVED** (chain, conditions and corrections). The prefactor matches 1509.01598 (C1) and 2101.08275 (C2).

---
## 3. The kinematic edge: what the "exponential sensitivity" actually is

**(3.1) Edge mass [D].** The kinematic minimum of v_min(q,ω) is v_* = √(2ω/m_χ) at q_* = m_χv_* (2311.04957 eq. (8)). For a hard cutoff
v ≤ v_max ≡ v_esc + |v_E|, scattering at threshold E_th requires

  m_χ ≥ m_min = 2E_th/v_max²,   δ ln m_min = δ ln E_th − 2 δ ln v_max.                                                 (3.1)

C7 gives m_min = 0.319 MeV (Si, E_th = 1.12 eV, v_max = 794), 0.285 MeV (v_max = 840, which reproduces EXCEED-DM's 0.28 MeV), 0.358 MeV
(2311.04957 conventions) and 0.191 MeV (Ge). **The halo (v_max) and theory (E_th) uncertainties enter through one combination,
E_th/v_max², so they are exactly degenerate at the edge. They must be profiled jointly and cannot be quoted separately.**

**(3.2) Two regimes of η [D].**
- *Regime A, v_E + v₀ ≲ v_min < v_esc − v_E:* η ≈ erfc-type, ∝ e^{−(v_min − v_E)²/v₀²}. This is exponential in v_min. The log-sensitivities
  per km/s at v_min = 600 are 0.018 (v₀), 0.0028 (v_esc) and 0.013 (v_E) (C4). With v₀ = 233 ± 6 (2011.12896), this gives ±11%.
- *Regime B, v_min → v_max:* with δ ≡ v_max − v_min,

  η = π v_esc e^{−v_esc²/v₀²} δ²/(|v_E| K) + O(δ³)     (C4b).                                                              (3.2)

  This is a **power law in δ** times a fixed exponential. ∂ln η/∂v_esc ≈ 2/δ diverges at the edge. Numerically it is 0.048 per km/s at
  v_min = 760, so v_esc ± 25 km/s gives e^{±1.2} ≈ ×3.3.

**(3.3) Near-threshold rate [D].** Hypotheses: regime B, and S̄(q,ω) ∝ (ω − E_th)^p smooth in q near q_*. Then
v_min ≈ v_* + (ω/q_*³)(q−q_*)², and the q-integral of (Δ − cx²)² gives (16/15)Δ^{5/2}c^{−1/2} (C5a). The ω-integral adds p + 1, so

  R(m_χ) ∝ Δ₀^{7/2+p},   Δ₀ ≡ v_max − √(2E_th/m_χ),   ∂ln R/∂ln v_max = (7/2+p)v_max/Δ₀.                              (3.3)

The exponent fitted from the closed-form integrals is 3.49 for p = 0 and 4.49 for p = 1 (C5b). So the lowest-mass part of every ER curve
is controlled by three things:
- the edge position m_min, from (3.1);
- the halo exponent (2 for a hard cutoff);
- **the response onset exponent p**, a property of S near threshold: ZPL onset, PAER sideband, excitons (WP1/WP3).

**(3.4) Smooth truncations [D, given the form].** For a tail of the form f ∝ (e^{−v²/v₀²} − e^{−v_esc²/v₀²})^k (King/Lisanti-type,
1010.4300; the form is quoted from memory, so [E] for the attribution), η ∝ δ^{2+k} and R ∝ Δ₀^{7/2+k+p}. **The halo-tail exponent k
and the response-onset exponent p are degenerate at the edge.** A null result at the edge constrains only the combination. This is the
precise content of G8's "50%–×10" claim.

**(3.5) Size of the edge nuisances for Si [E].**
- v_esc: 544 vs 528 ± 25 (2011.12896) vs 600 (QROCODILE/QEdark). This gives δ ln v_max ≈ 3–6%, so 6–12% in m_min.
- E_th from the step-model convention (D5): 7%.
- Clamped versus ZPR-renormalised gap: Si ZPR ≈ −60 meV, about 5%, if the code is not scissored to the measured E_g(T).
- Operating temperature: Varshni gives E_g(130 K) − E_g(0) ≈ −10 meV, about 1%.
- The PAER window (SOTA: m_χ ≈ 0.34–0.47 MeV) lies in regime B, so its rate carries the (3.3) sensitivity with p from S^{X+}.

---
## 4. G8 closed: halo-independent ER analysis in the URF

**(4.1) Formula [D].** Hypothesis (I) and (1.7). Then

  μ_i(m_χ, η̃, θ) = Σ_j 𝒜_ij(m_χ; θ) η̃_j,
  𝒜_ij = 𝔈_i (4π²ρ_T)^{-1}∫dω P_i(ω;θ) ∫q dq [A₀(q,ω;θ) + A₂(q,ω;θ)(v_j² − v_min²)] Θ(v_j − v_min(q,ω)).                    (4.1)

Here A₀, A₂ are taken per unit σ̄_e, and η̃ ≡ (ρ_χσ̄_e/m_χ)η absorbs the remaining factors. This follows from (1.3)–(1.4) with η̃ = Σ_j η̃_jΘ(v_j − u), which implies ξ̃ = Σ_j η̃_j(v_j² − u²)Θ(v_j − u). It generalises 2311.04957
(19)–(20) in three ways: to all operator classes (the A₂ term), to any library response S (WP1–WP3) and to the theory nuisances θ (§5).

**(4.2) Positivity [D].** WP0 (4.4) gives tr(𝔇S) ≥ 0, so A₀ + A₂(v_j² − v_min²) ≥ 0, and with P_i ≥ 0 this gives 𝒜_ij ≥ 0. Two
consequences:
- *(a) Convexity.* −ln ℒ is convex in η̃ at fixed (m_χ, θ), because μ is linear and the Poisson log-likelihood is concave. The η̃ profile
  is therefore unique (as 2311.04957 states, here with θ included).
- *(b) Conservative halo-independent bound.* η̃ is non-increasing and ≥ 0. So η̃(u₀) = h implies η̃(u) ≥ h for all u ≤ u₀, and the
  smallest rate compatible with h is h·A_i(u₀), with A_i(u₀) ≡ 𝒜_i evaluated for a single step at v_j = u₀. Hence

  η̃(u₀) ≤ min_i N_i^up(θ)/A_i(u₀; m_χ, θ)   for every u₀,                                                               (4.2)

  where N_i^up is the per-bin upper limit on counts. This is the ER and URF form of the NR construction of 1111.0292 (title verified),
  integrated over q. It needs (4.2a): the minimal rate is reached by a single step **because 𝒜 ≥ 0**. Without positivity
  (for example, a truncated S with negative pieces, §9 W2) the bound is invalid.

**(4.3) Mass degeneracy [D].** rank 𝒜 ≤ N_bins with populated counts. When only 1–2 bins are populated (light mediator), the kernel of 𝒜
is (N_v − 2)-dimensional, and the edge degeneracy (3.4) makes m_χ undeterminable halo-independently. This is consistent with
2311.04957 §3 [FT] and explained here by (3.3)–(3.4).

**(4.4) Computation specification.**
- *Inputs:* the library S̄ (and A₂ tables for non-O₁ operators) on (q,ω); P(N_eh|q,ω) per yield model (WP5); detector P_det(i|N_eh) and
  𝔈_i from each experiment; nuisance templates Δ_k (§5).
- *Grid:* v_j at 10 km/s spacing over 0–1000 km/s (N_v = 100, as in 2311.04957); q on the library grid (§7); ω on the library grid.
- *Cost:* 𝒜 is N_bins × N_v × N_q × N_ω ≈ 10 × 100 × 300 × 2500 ≈ 10⁹ operations per (m_χ, θ) point, which is seconds. The θ-derivatives
  ∂𝒜/∂θ_k come from the same contraction with Δ_k.
- *Outputs:*
  - the bound (4.2) as a curve η̃_max(u₀; m_χ) with theory band;
  - the η̃ profile and the 1σ/2σ regions (SVD flat directions, 2311.04957 eqs. (21)–(24));
  - compatibility p-values for pairs of experiments with shared θ.

**(4.5) Exact remaining gap (G8′).** For anisotropic targets beyond (I), with daily-modulation analyses or non-cubic or thin-film
targets, the halo object is f̂⁽⁰⁾(q̂,u,t) on the sphere, in the lab frame, as a function of time. It obeys no scalar monotonicity, so
(4.2) does not apply. Only its A1g projection, the ℓ = 0 part, reduces to η. A conservative halo-independent bound for anisotropic
responses needs a convex characterisation of the set of Radon transforms of non-negative f with |v| ≤ v_max. That is a moment
problem and is not derived here [OPEN].

---
## 5. Nuisance-parameter structure for every approximation level (G4, part 1)

**(5.1) Parametrisation [D].** WP0 (8.1) is additive and Gaussian, and that violates positivity (§9 W2). Three types are used instead:
- *(M) Multiplicative, log-normal:* S(q,ω;θ) = S^τ(q,ω) Π_k [1 + r_k(q,ω)]^{θ_k}, with r_k = Δ_k/S^τ and θ_k ~ 𝒩(0,1). It is PSD
  for all θ and agrees with WP0 (8.1) at first order in θ.
- *(A) Additive, for support-opening truncations* where S^τ = 0 on part of (q,ω), such as the PAER window: S = S^τ + a_k Δ_k with
  a_k > 0 log-normal. The central value includes Δ_k as soon as it is computed (a_k = 1), and the prior width is the stated residual
  uncertainty.
- *(E) Energy shift:* S(q,ω;θ_E) = S^τ(q, ω − θ_E σ_E). This is the edge nuisance of (3.1). It shifts M¹ by θσ_E∫S, which is
  inside the truncation error.
- *(Δ) Discrete* model choices are handled by discrete profiling (1408.6865, title verified) or by an envelope (§6).

One θ_k per truncation is applied coherently across all (q,ω), bins, and experiments that use the same target (WP0 (8.2)).

**(5.2) Table.** Sizes are [E] unless a source is given. "Central" is the recommended τ* of the library.

| Level (WP0 τ index) | Template Δ_k | Type | Prior | Correlation | Source of Δ_k |
|---|---|---|---|---|---|
| XC functional (ground state) | spread over a functional ensemble {PBE+scissor, SCAN, HSE, G₀W₀ bands}: principal components of the covariance in ln S | M (per PC) + E (gap) | 𝒩(0,1) per PC; σ_E = 0 if scissored to measured E_g(T_op), else \|E_g^DFT − E_g^exp\| | all experiments with that material; ρ_mat = 0 across materials by default (show 1 as a variant) | ≥ 3 functional runs. Ge 3d is misplaced by about 4.5 eV (2306.14944) and gets its own E-type nuisance on core weight |
| Kernel ladder X | S^{X+1} − S^X: central RPA+LFE, so Δ = (BSE or TDDFT-kernel) − (RPA+LFE). If not computed, η_xc·S, with η_xc = E_b/E_g near the gap | M | 𝒩(0,1) | material-wide | Yambo/BerkeleyGW BSE at finite q (WP1). LFE alone is 20–50% (2603.12326) and belongs in the central value, not the nuisance |
| q_max / high-q cutoff | Θ(q−q_max) S_IA(q,ω), with S_IA = 2πn_s(m_e/q)J_s(p_z) per shell (impulse approximation; satisfies the f-sum, C9) | added to the central value; residual M on the tail | residual width ⟨E_B⟩/(q²/2m_e) per shell | material-wide | Compton profiles J_s from all-electron atoms in the crystal (QCDark/EXCEED-DM core). The truncation is then **closed analytically, not left as a nuisance** |
| k-grid / basis / PAW (numerical) | difference between successive grids or bases | M | 𝒩(0,1) | run-specific | convergence pair. The rate falls monotonically with k-density (2105.05253): use a one-sided (half-normal) prior |
| BO order n_B | κ_BO⁴ weight shift (WP0 Theorem D(iii)) | M | width 2×10⁻⁵ (Si); negligible | — | analytic |
| e–ph order n_g | n_g = 0 → 2: PAER sideband S^{X+} (A-type in the window), ZPR shift (E-type), Franck–Condon reduction e^{−2W} of the ZPL (M) | A + E + M | A: a ~ ln𝒩 with 68% range [0.5, 1.2] (SOTA X2 interim). E: σ_E = \|ZPR\| ≈ 60 meV (Si) if unrenormalised. M: η_ep | material and temperature | EPW/ZG (WP3, X1/X2 specification) |
| Screening channel (pair channel, external LFE in X+) | X2 classes | M | interim factor [0.5, 1.2] | material | X2-N1..N4 |
| Anharmonic n_A | η_anh S_κκ (L18) | M | η_anh = 0.01–0.03 (T = 0) | NR channels only; negligible for ER | WP2 |
| Temperature n_T | dS/dT·σ_T: E_g(T) shift (Varshni, about −1.5×10⁻⁴ eV/K at 130 K) plus the phonon-absorption sideband n_Q (TA at 130 K: n ≈ 0.25) | E + M | σ_T = sensor uncertainty (about 1 K) | per experiment | analytic, plus the WP3 sideband |
| Yield model (WP5) | {step(ε), R&K, URF cascade} | Δ (discrete) + M on ε | ε: 𝒩(3.75, 0.05) eV for Si at 130 K [E] | material-wide | WP5 (G1). R&K's tuned A parameter is "non-physical" (2004.10709) |
| Fano factor F | width of P(N_eh\|Λ) | M on the variance | F = 0.119 ± 0.002 at 5.9 keV (2004.11499); near-gap prior uniform on [0.1, 0.2] [E] until L23 is computed | material-wide | WP5 L23 |
| E_g(T) | E-type | E | σ_E: 1 meV if scissored to measured E_g(T_op); 60 meV if clamped and unscissored; plus the D5 convention (0.08 eV) must be **removed** by convention, not profiled | material-wide | measured E_g(T) |
| Halo | fixed nominal (2105.00599) for the headline; halo band from (v₀, v_esc, v_E) | separate object | v_esc 528⁺²⁴₋₂₅, v₀ 233 ± 6 (2011.12896); annual v_E 237–266 (C6) | all experiments | §6 |

**(5.3) Sum-rule constraints [D].** The f-sum constraint of WP0 (8.2) holds only with the normalisation ∫_{−∞}^{∞}dω ω S = π n_e q²/m_e
(§9 W1). It carries information only for **non-conserving** truncations: q/band cutoffs, nonlocal pseudopotentials (WP0 (4.6) with
(L) violated), and the sideband without its Fan/vertex compensation (SOTA #3). Every rung of the X ladder with local potentials is
conserving, so it gives ∫ωΔ_X = 0 identically. Positivity holds automatically for M and A. The L17 bounds (WP0 (9.6)) give a hard upper
limit on ∫ω^n S(θ). It is used as a support restriction on θ, and is not a prior.

---
## 6. Statistical treatment and combination (G4, part 2)

**(6.1) Likelihood [D as a definition].** For experiments e, bins i, signal strength σ = σ̄_e, theory θ and detector nuisances ν_e:

  ℒ(σ,θ,ν | m_χ) = Π_e Π_i Pois(n_ei | σ s_ei(m_χ;θ,ν_e) + b_ei(ν_e)) · Π_k π_k(θ_k) · Π_e π_e(ν_e).                   (6.1)

Here s_ei = 𝔈_ei ∫ (rate (1.4) per unit σ) P_det P_casc, with the halo fixed. Test statistic: the two-sided profile-likelihood ratio,
toy MC rather than asymptotics, and a power-constrained limit at −1σ (2105.00599 §2 [FT]).

**(6.2) Profile, envelope and Bayesian treatments differ at different orders [D] (C8).** Take a zero-count bin with b = 0, the asymptotic
statistic, and one theory nuisance of fractional size δ.
- *Linear:* −2ln ℒ = 2σA(1+θδ) + θ². Profiling θ gives σ_up(δ)/σ_up(0) = 2(1 − √(1−cδ²))/(cδ²) = 1 + cδ²/4 + O(δ⁴), with c = 2.71.
- *Log-normal* (5.1 M): 1.006, 1.047 and 1.112 for δ = 0.1, 0.3 and 0.5.
- *Envelope* WP0 (8.3), worst case at |θ| ≤ 1: 1/(1−δ), which is 1.11, 1.43 and 2.0.

**Profiling a theory nuisance in a null result costs O(δ²). The envelope costs O(δ).** A Bayesian marginal with π_k = 𝒩 behaves like
the profile at small δ [E]. Theory priors are not auxiliary measurements, so this choice is a convention, and it moves the published
curve by up to ×1.8 at δ = 0.5.

**(6.3) Recommendation: report three objects [D as a protocol].**
- **(R1)** The nominal limit: θ = 0, central τ*, halo fixed to 2105.00599. This is the comparability curve.
- **(R2)** The theory-profiled limit: θ profiled with (5.2) priors and log-normal M-types. This is the headline physics result.
- **(R3)** The theory band: the envelope over |θ_k| ≤ 1 applied one at a time and in quadrature, drawn around R1, together with a
  separate halo band and the halo-independent bound (4.2).

This reconciles D6: the halo is fixed in R1 and R2 and varied only in R3. The edge degeneracy (3.1) means that E_th and v_max must be
varied together in R3.

**(6.4) Combining experiments that used different codes and conventions [D].**
- *Step 1, common response.* Recompute each s_ei from the library at one τ* and one version. The code differences (SENSEI: QEdark main;
  DAMIC-M: QCDark + MTF; CDEX: EXCEED-DM) then become θ-values at matched τ, not "spread". The residual after matching τ is a
  numerical/convergence nuisance. This answers SENSEI's "the code spread should not be taken as an uncertainty": decomposed by τ,
  it is a set of correlated nuisances, plus D5-type convention offsets that are removed rather than profiled.
- *Step 2, shared θ.* θ_k is common to every experiment on the same material. Across materials, use the ρ_mat option.
- *Step 3, conventions.* Rescale ρ_χ (linear). Recompute with the fixed halo. Use one E_th convention (measured E_g(T_op) at each
  experiment's T).
- *Step 4, the likelihood product* (6.1), which is (15) of 2311.04957 with θ shared.
- *If only limits are public (recast) [D].* For an analysis that sets its limit from per-bin Poisson upper limits N_i^up, the exact
  recast is σ_up^lib(m_χ) = min_i N_i^up/s_i^lib(m_χ). This needs N_i^up and 𝔈_i. For a single-bin analysis it reduces to
  σ_up^C·s^C/s^lib. Optimum-interval and PLR analyses cannot be recast exactly without the binned likelihood.

**(6.5) Minimum publication standard (what experiments must release) [D: the minimal sufficient set for (6.1)].**
- per bin: n_i, b_i with covariance, and 𝔈_i;
- the detector matrix P_det(i | N_eh) with its ν-dependence;
- per-bin N_i^up;
- the library version, τ* and θ̂;
- the halo convention used;
- the full likelihood in machine-readable form (pyhf/HEPData-style JSON).

---
## 7. The shared, versioned response library (G4, part 3)

**(7.1) Content and axes [D as a specification].** One container per (material, temperature, τ, version), in HDF5 or NetCDF4 with JSON
metadata:

| Dataset | Axes (shape) | Units / normalisation | Notes |
|---|---|---|---|
| `S_iso/ee` | q (N_q), ω (N_ω) | Ω S̄_ee [eV⁻¹], spin included, T as labelled | the L24/L1–L3 workhorse; converts to \|f_crys\|², \|f_res\|² and L by (1.5) |
| `S_iso/ab` | a, b (16×16 per species, Hermitian; upper triangle stored), q, ω | same | WP0 basis (2.2); needed for non-O₁ couplings (G10); A₀, A₂ of (1.4) follow by contraction with 𝔇 |
| `S_aniso/ee` | ℓ-invariant index (7 for O_h up to ℓ = 12; C11), q, ω | coefficients of P-invariant harmonics | L19, daily modulation, (1.2) beyond (I). Non-cubic groups: count by the Molien series |
| `eps` | G, G′ (small), q, ω | ε_{GG′}(q,ω), ε_e; ε(q,0) | screening (WP0 (5.2)–(5.5)), L17 diagnostics, channel choice |
| `S_Lambda` | Λ-marginals: (ε_e, ε_h) coarse grid or N_ph, q, ω | Ω S(q,ω;Λ) | WP0 (7.1) hand-off to WP5 (G1) |
| `P_Neh/<model>` | N_eh (≤ 20), q, ω | probability | per yield model (step, R&K, URF cascade), with F, ε metadata |
| `Delta/<k>` | as the S it modifies | same, plus type ∈ {M, A, E, Δ}, prior, correlation group | the §5 templates, one per active truncation |
| `checks` | q | ratios | f-sum fraction (π n_e q²/m_e normalisation; WP0 (4.6)), min eigenvalue of S_ab (WP0 (4.4)), KK residual between S and Im R (WP0 (4.1)–(4.2)), detailed-balance residual (WP0 (4.3)), L17 saturation K_n/bound (WP0 (9.6)), convergence deltas |
| `derived/A` | bin set, m_χ, v_j | 𝒜_ij of (4.1) for standard binnings and halo steps | halo-independent analyses without rerunning |
| `derived/edge` | — | E_th(q), onset exponent p fit, ZPR | the edge parameters of (3.3) |

**(7.2) Grids [E].**
- q: 0.1–30 αm_e (0.37–112 keV), N_q ≈ 300, log-spaced below 2αm_e and linear above. This covers q_* = √(2m_χE_g) down to 0.3 MeV
  and the all-electron range of 2603.12326 (25 αm_e). The tail beyond comes from S_IA (§5).
- ω: 0–100 eV. Δω = 10 meV within 5 eV of E_g, where the edge (3.3) needs it, and 50 meV above. N_ω ≈ 2.5×10³.
- T ∈ {0, 0.05, 4, 77, 130, 300} K as needed.
- *Sizes:* S_iso/ee is 300 × 2500 × 8 B ≈ 6 MB. The full 16×16 is 1.5 GB per species. The anisotropic set is ×7. Each Delta set has the
  size of its parent.

**(7.3) Provenance and versioning [D as a specification].**
- *Content addressing:* every dataset carries a SHA-256 of its array and a PROV-style parent list: input structure (CIF hash),
  pseudopotential/basis hashes, code name and commit, run cards, and the hashes of parent tables.
- *Mandatory metadata:*
  - the τ multi-index string (WP0 (6.1)), e.g. `nB0|ng0|nA0|X=RPA+LFE|nT=130K|K=-|M=-|nD=-`;
  - the functional and scissor ΔE;
  - k-grid, cutoffs, q_max and the band count;
  - convention flags: q from DM to target; spin included; per-cell; units; CODATA set; S_ab ordering as in WP0 (3.1);
  - the checks summary.
- *Semantic versioning:* MAJOR for any change of τ* or of convention, MINOR for added tables or materials, PATCH for numerical refinement
  within the stated tolerances. Published limits cite version + τ* + θ̂. Old versions stay immutable and DOI-minted.

**(7.4) Computation specification (library build).** For each material:
- the central run τ* and one run per active truncation, τ* + e_k (§5.2: about 6–9 runs);
- codes:
  - QE/VASP + Yambo/BerkeleyGW for RPA+LFE and BSE ε_{GG′} (WP1);
  - QCDark2/EXCEED-DM-type all-electron reconstruction for high q and cores (G7);
  - EPW/ZG for the X+ and ZPR templates (WP3, X1/X2 specification);
  - WP5 cascade for P_Neh.
- *Cost:* the WP1–WP3 runs dominate. Library assembly, checks and the derived 𝒜 are under 1 CPU-hour per material [E].
- *Validation gates* before release, all in `checks`:
  - f-sum within 2% for q below the band cutoff;
  - min eigenvalue ≥ −10⁻⁶ of the trace;
  - KK residual below 1%;
  - agreement with NIXS/EELS where data exist (2603.12326 compares at q < 3αm_e).

**(7.5) G4 status.** The fix is the formula set (5.1)–(5.3), (6.1)–(6.5) and the library (7.1)–(7.4). Exact remaining gaps:
- (i) The prior widths of *estimated* (uncomputed) truncations are conventions (η^{n+1} rules, WP0 (8.1)) and are not derivable.
- (ii) Cross-material correlations of functional and kernel nuisances are not derivable, so they are given as a declared option.
- (iii) The discrete yield models need discrete profiling until WP5 supplies a continuous cascade with errors.
- (iv) The combination needs experiments to publish (6.5), which is outside theory.

---
## 8. Summary of new content
- (1.2) The general halo functional for all operators and anisotropic targets. (1.3) **ξ = 2∫u′η du′: velocity-dependent operators
  need no halo input beyond η** under (I).
- (1.5) Cubic-harmonic compression: the first anisotropic correction is ℓ = 4.
- (3.1)–(3.4) **The edge is a power law Δ₀^{7/2+k+p}, not an exponential.** The halo-tail exponent k and the response-onset exponent p
  are degenerate, and E_th/v_max² is the only edge variable, so halo and gap nuisances must be profiled jointly.
- (4.1)–(4.2) The URF halo-independent bound. Its validity rests on WP0 positivity, 𝒜 ≥ 0.
- (5.1) A positivity-preserving nuisance algebra (M/A/E/Δ types) replacing WP0 (8.1). q_max is closed by the impulse tail.
- (6.2) Profile versus envelope differ at O(δ²) versus O(δ): a declared convention that moves curves by up to ×1.8.
- (7) The library schema, with sum-rule validation gates taken from WP0 §4.

---
## 9. WP0 defects
- **W1 (normalisation).** WP0 (8.2) writes the f-sum constraint as Σθ_k∫ωΔ_k = n_e q²/m_e·(2π) − ∫ωS^τ. WP0 (4.5) with S[O†] = S[O]
  (densities with inversion) gives ∫_{−∞}^{∞}dω ω S = π n_e q²/m_e, consistent with WP0 (9.5): ∫₀^∞ωL = (π/2)ω_p² with S = 2q²L/e² at
  T = 0. The factor 2π is wrong by a factor 2. The integral must also run over negative ω at T > 0.
- **W2 (positivity).** WP0 (8.1), additive with θ ~ 𝒩(0,1), violates WP0 (4.4) wherever |Δ_k| ≳ S^τ. Examples: the LFE changes Si's DSF
  by up to a factor ≈ 6 at low ω (2603.12326: reduced to 15%), and in the PAER window S^τ = 0. Replace it by the M/A types of (5.1). This
  matters for (4.2), whose validity requires 𝒜 ≥ 0.
- **W3 (over-claim).** WP0 (8.2) presents the f-sum as constraining θ. For conserving truncations (the whole X ladder with local
  potentials), ∫ωΔ_k = 0 identically, so the constraint is vacuous there (§5.3).
- **W4 (inconsistency).** WP0 (8.3) defines the theory band as the |θ_k| ≤ 1 envelope next to a profile-likelihood exclusion. These
  differ at O(δ) versus O(δ²) (C8). Both must be specified, as in (6.3).
- **W5 (hypothesis).** WP0 (9.1) says "isotropic f_χ gives η/2q". The lab-frame SHM is not isotropic. The result requires the angle
  average of S (hypothesis (I)), with η built from the full anisotropic f (C10a). The formula is right and the stated hypothesis is wrong.
- **N1 (NOTATION).** v_E = 250 km/s is the Sun's speed |v₀ + v_⊙| = 250.5. The annual-mean Earth speed from 2105.00599 is 252.1 (C6).
  ρ_χ = 0.4 differs from the 2105.00599 recommendation (0.3). Proposal: NOTATION adopts 2105.00599 Table 1 verbatim, ρ_χ = 0.3, with the
  time-dependent v_E(t) from their eq. (11).

## 10. Literature (all IDs verified against the arXiv API, 2026-10-31)
- [FT] 1509.01598 (Essig et al.): eqs. (15)–(17), (21), (58)–(68).
- [FT] 2311.04957 (Bernreuther, Fox, Lillard, Taki, Yu): eqs. (1)–(26).
- [FT] 2105.00599 (Baxter et al., conventions): eqs. (10)–(14), Tables 1–2, §2.
- [FT] 2011.12896 (Maity, Ray, Sarkar): abstract and §3 values.
- [FT] 1011.1915 (Fox, Liu, Weiner).
- [FT] 2101.08275 (Knapen et al.): eqs. (10)–(16).
- [title/abstract] hep-ph/0209110, 1111.0292, 1408.6865, 1007.1727, 1010.4300, 1904.04781, 2001.09156, 2004.10709, 2004.11499,
  2105.05253, 2210.14917, 2104.12786, 2306.14944, 2603.12326, 2312.13342, 2503.14617, 2509.03608, 2411.03433, 2607.06005, 1203.3542.
- Survey values (catalog-analysis-and-gaps §1) are cited as given there.
- PDFs and HTML were deleted after reading, as the brief requires.

## 11. Open items handed on
- O6-1: G8′ (4.5), the moment-problem characterisation of Radon transforms for anisotropic halo-independent bounds.
- O6-2: WP1 to supply the onset exponent p(q) near E_th for Si and Ge (ZPL and excitons); WP3 to supply p for S^{X+}. These feed (3.3).
- O6-3: WP5 to supply a continuous P(N_eh|Λ; θ) with F and ε nuisances, to replace the discrete yield models.
- O6-4: decide ρ_mat (cross-material nuisance correlation) and the profile-versus-envelope convention (6.2) at the synthesis stage (M4).
- O6-5: a WP0 erratum for W1–W5, and the NOTATION update N1.
