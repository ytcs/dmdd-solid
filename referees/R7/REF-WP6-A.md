# R7 / REF-WP6-A: hostile referee of returns/R6/WP6-v2.md (isolated)

Read: WP6-v2.md, code/WP6-v2/checks.py (re-run: 27/27 PASS, about 25 s), CONVENTIONS, NOTATION v4, CONTROLS, DONE, LIMITS, WP0-v2 (interfaces only).
Full text fetched and then deleted: 2311.04957v2 and 1509.01598 (arXiv HTML equation numbering, which matches the package's citations).
Own checks: sympy/mpmath one-liners (< 1 min) for the T_d invariant counts and the nonlinear η sensitivities. No simulations.

## Verdict table
| # | Claim (WP6-v2 location) | Verdict | One-line reason |
|---|---|---|---|
| 1 | General halo functional f̂^{(0,1,2)} (1.1)–(1.2) | STANDS | On-shell algebra re-derived (§A1); 𝔇 is quadratic in v_T because 𝒱 is affine in it |
| 2 | Isotropic reduction, n = 1 drops, ξ = 2∫_u u′η du′ (1.3)–(1.4) | STANDS WITH CORRECTION | Correct, but for tensor S_ab "angle average" must mean the SO(3) orientation average with indices co-rotated, and that is not stated (§A2) |
| 3 | Anisotropy: ℓ = 4 first for cubic P- or T-symmetric targets; odd ℓ for P,T-broken targets (1.5), (2.4a) | STANDS WITH CORRECTION | TR removes *all* odd-ℓ T_d invariants (ℓ = 3, 7, 9, 11, 13), not only ℓ = 3. The "S_4 × ℓ = 4 Radon moment" holds for the n = 0 term only. Cubic groups have no ℓ = 1 invariant (§A3) |
| 4 | Dictionary (1.6) and per-cell / per-target factors | STANDS | Re-derived from 1509.01598 Eq. (61) with S^{IP} (§A4) |
| 5 | μ_i linear in S and η; seeding inside the q integral (1.7), (4.1) | STANDS | Linear by construction; agrees with WP0-v2 (7.3) |
| 6 | L24 chain, sources, validity, corrections (§2) | STANDS WITH CORRECTION | Source quotes verified FT. (V2) mixes a model choice with a small parameter. The V4/§3.2 sensitivities are linearised beyond their range (§B) |
| 7 | WP6-D1 (2311.04957 Eq. (3) is per cell) | CONFIRMED | Eq. (3) with (4) equals 1509.01598 Eq. (17)/N_cell; "cell" never appears in 2311.04957 |
| 8 | WP6-D2 (Eq. (13): [q₋,q₊] together with Θ) | CONFIRMED as an ambiguity, not an error | q±(v) of Eq. (7) is evaluated at an unstated v; the Θ makes the result correct for any v ≥ v_i |
| 9 | WP6-D4 (1509.01598 Eq. (67) sign) | CONFIRMED, incomplete | Eq. (67) also writes Θ(v_esc − v_χ) where Eq. (65) needs Θ(v_esc − \|v_χ + v_E\|). Eq. (68) is correct for (65) (C4a) |
| 10 | WP6-D3, D5 (halo values; E_gap = 1.2, ε = 3.8 eV; 776 km/s) | CONFIRMED | 2311.04957 §2.2 and §3: {1.2, 3.8} eV, 220/544/232, ρ = 0.4. 1509.01598: 230/600/240 |
| 11 | "η̃ profile is unique (as 2311.04957 states)" (4.2a) | FALLS (REFUTED attribution) | 2311.04957 says "any minimum … is a global minimum", not that it is unique. The minimiser is not unique because ker 𝒜 ≠ 0, which the package itself states in (4.3) (§C3) |
| 12 | m_min values and the E_th convention (3.1) | STANDS WITH CORRECTION | The numbers are right (0.333, 0.338, 0.212 MeV). But (3.1) assumes a q-independent E_th. For the indirect gaps of Si and Ge, 0.333 and 0.212 MeV are kinematic lower bounds that no T = 0 channel reaches (§D1) |
| 13 | Regimes of η, δ_v,× = 173 km/s (3.2) | STANDS WITH CORRECTION | The series is exact. "v_esc ± 25 km/s gives e^{±1.17}" at v_min = 760 is wrong: the exact factors are ×2.26 and ×0.100 (§B2) |
| 14 | Edge exponent 7/2 + k_tail + p_on (3.3)–(3.4) | STANDS | Re-derived. It survives a q-dependent threshold by a tangency argument (§D2). The degeneracy needs a single-bin qualifier |
| 15 | PAER p_on (3, 4, 4–5, 3/2–5/2; none in the edge shell) | STANDS (arithmetic); physics owned by WP3 | The exponents add correctly. The +1 relative to the optical 2, 3, ½ is what the q̂ average over a quadratic threshold minimum gives (§D3) |
| 16 | Hypothesis (P) and the halo-independent bound (4.2) | STANDS WITH CORRECTION | "Minimum at a single step because 𝒜 ≥ 0" is a non sequitur. It needs 𝒜_i(v) to be non-decreasing in v. The sufficiency argument for (P) adds an unstated hypothesis (§C1–C2) |
| 17 | Nuisance types M/A/E/Δ (5.1) | STANDS | PSD for M and A; the shift of 𝓜¹ under E is correct |
| 18 | Constraint-preserving anharmonic form (5.1′) | STANDS WITH CORRECTION | The moment constraints hold exactly (re-derived). But for any S^τ with unbounded tails, positivity forces θ_δ (and generically θ_A) to one sign. The label "type A" contradicts (5.1). "Π_mom[X] ∝ S^τ × quadratic" is false (§E) |
| 19 | Profile vs envelope, closed forms (6.2) | STANDS WITH CORRECTION | The formulas are re-derived. "×1.8 (2.0/1.112)" divides a *linear* envelope by a *log-normal* profile. Like for like gives ×1.35 (M) or ×1.57 (linear). The error is copied into WP0-v2 (8.3) (§F) |
| 20 | Library, reporting, combination (§6.3–§7) | STANDS | Specification is sufficient; "exact recast" needs the qualifier in §G |
| 21 | Gap closures G8 (formula + spec) and G4 | STANDS WITH CORRECTION | G8 is closed under (I), PSD and monotonicity (§C). G8′ is honestly left open. G4 is closed as a specification |
| 22 | "No deviations" from NOTATION (§15) | STANDS WITH CORRECTION | K (τ slot only, NOTATION) reused for phonon wavevectors; δ (off-shell distance) reused as the fractional nuisance size in (6.2); d has no row |
| 23 | Contested corrections: none (§12) | STANDS | The −0.4 % remark is correct: (794.5/796.1)² = 0.996 |

---
## A. Halo reduction (focus item 1)
**A1.** ω_q = q·v − q²/2m_χ − Δ_χ gives δ(ω − ω_q) = q⁻¹δ(q̂·v − v_min), with v_min = (ω+Δ_χ)/q + q/2m_χ. On shell q̂·v = v_min, so
v_χ = v − q/2m_χ = v_∥q̂ + v_T with v_∥ = (ω+Δ_χ)/q. 𝔇 = 𝒱†𝒱 with 𝒱 = 𝒱₀ + 𝒱₁·v_T, so 𝔇^{(2)} = 𝒱₁†𝒱₁ is PSD. (1.2) holds.
Prefactor: ∫d³q/(2π)³ q⁻¹ ⟨f̂^{(0)}⟩_q̂ = ∫q²dq·4π·η/(2q·q)/(8π³) = (4π²)⁻¹∫q dq η, which is (1.4) and agrees with WP0-v2 (9.2) after |Ṽ|² = πσ̄_eF²/μ².
**A2.** ⟨δ(q̂·v−u)⟩ = Θ(v−u)/2v. On shell |v_T|² = v² − u², hence ξ. Leibniz rule: dξ/du = −2uη − (boundary term (v²−u²)/v at v = u, which is 0), and
ξ(v_max) = 0, so ξ = 2∫_u u′η du′ for any f_χ. **Correct.** The claim that the n = 1 term drops is right: the only rotation scalars linear in v_T
built from q̂ and v_T are ∝ q̂·v_T = 0, and a pseudoscalar ε(q̂, v_T, ·) needs a third vector.
*Correction:* for S_ab with vector or axial O_a, "S → S̄(|q|,ω)" must be defined as the orientation average
S̄_ab(q) = ∫dR D(R)_{aa′}S_{a′b′}(R⁻¹q)D(R)⁻¹_{b′b}, which gives isotropic tensor structures such as α δ_cd + β q̂_cq̂_d + γ ε_cde q̂_e.
A component-wise q̂-average at fixed lab indices is wrong: it mixes the longitudinal and transverse current responses. The step
𝔇^{(2)} → d₂δ + d₂′q̂q̂ is valid only with the orientation average.
**A3.** Invariant counts (character formula, recomputed). O_h (even ℓ): 1,0,1,1,1,1,2 for ℓ = 0,…,12 (C11 confirmed). T_d, all ℓ: A1 count at
ℓ = 3, 4, 6, 7, 8, 9, 10, 11, 12, 13 = 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, and 0 at ℓ = 1, 2, 5. TR (S(q) = S(−q)) removes **every** odd ℓ
(3, 7, 9, 11, 13 …), not only "the ℓ = 3 invariant xyz". For a P,T-broken target the effective group acting on S(q̂) is
H ∪ (−1)·(G∖H), where H is the unitary subgroup and the antiunitary gT act as q → −gq. A cubic H has no ℓ = 1 invariant, so for cubic magnetic
targets the leading odd term is ℓ = 3, and ℓ = 1 needs H polar. If the magnetic group contains PT, S(q) ≠ S(−q) is still allowed; if it contains
the product of T with inversion as −1 in the effective group, only even ℓ survive. Write "odd ℓ allowed by the effective group".
*Second correction:* "(1.2) = Σ_ℓ S_ℓ f̂^{(0)}_ℓ" and (2.4a) "S_4 × the ℓ = 4 moment of the Radon transform" hold only for the n = 0 term. For
velocity-dependent operators the n = 2 term pairs the crystal tensor field T_cd(q̂) = Σ_ab 𝔇^{(2)}_{ab,cd}S_ab with f̂^{(2)}_cd. Its first
cubic anisotropy is again total angular momentum 4, because the lowest non-isotropic cubic invariant tensor has rank 4. But the halo factor is
then a rank-2 moment with orbital ℓ = 2, 4, 6, not the ℓ = 4 moment of f̂^{(0)}. Statement (2.4a) needs this extension.

## B. L24 chain (rubric b)
**B1.** These source quotes were verified in FT. 1509.01598 Eq. (15) η; (16) v_min; (17) prefactor (ρ/m)N_cell σ̄αm_e²/μ²∫d ln q (E/q)ηF²|f|².
(21) = (64); (65) g_χ with the boosted cutoff; (66) K; (68) η₁, η₂. 2311.04957 Eqs. (3), (4), (9)–(13), (19)–(20). The halo values are
as quoted. The chain steps 1–7 are valid; C1/C3a are algebraically correct.
(V2) is mis-stated. "Other 𝔇_ab suppressed by v² or (q/m_e)²" is true only *within* a model whose leading coefficient is c₁. A DM model with c₃
or c₁₁ dominant receives no suppression. "Only 𝒪₁" is therefore a model hypothesis, not a validity condition with a small parameter. Rewrite it as
"hypothesis: the leading NR coefficient is c₁; the corrections are then O(v², q²/m_e²) from 𝒪₁'s own expansion plus the ξ term."
**B2.** The nonlinear SHM sensitivities were computed exactly from η₂ (2105.00599 values, v_E^ref = 250.5).
| v_min | v_esc ± 25 | v_E ± 15 | v₀ ± 6 |
|---|---|---|---|
| 600 | ×1.059 / ×0.920 | ×1.201 / ×0.824 | ×1.109 / ×0.893 |
| 760 | **×2.26 / ×0.100** | ×2.13 / ×0.310 | ×1.19 / ×0.83 |
At 600 km/s the package's ±19 % and ±11 % are fine. At 760 km/s the claim "v_esc ± 25 gives e^{±1.17} ≈ ×3.2" is **wrong**. The derivative is
evaluated at δ_v = 34.5 km/s, while the shift is comparable to δ_v. The true response is asymmetric: ×2.3 up and ×10 down. "Annual ±15 km/s is a factor
≈ 2.5" should read ×2.1 up and ×3.2 down. Since the package's own message is that the edge is a power law in δ_v, it should quote
(1 ± Δv_max/δ_v)^{2+k_tail} and not e^{(∂ln η)Δ}.
**B3.** §3.5 sizes. v_esc = 600 against 544 gives δ ln v_max = ln(850.5/794.5) = 6.8 %, so 13.6 % in m_min, not "3–6 %, 6–12 %". The step-model
E_th offset is 2.6 % against the campaign default 1.170 eV (1.2/1.17); the 7 % in the text is 1.2 against 1.12, a labelled comparison.

## C. Halo-independent bound, hypothesis (P) (focus item 4, G8)
**C1. The logic of the single-step minimum.** Write a non-increasing η̃ = Σ_j η̃_jΘ(v_j − u), η̃_j ≥ 0. The constraint η̃(u₀) ≥ h is Σ_{v_j ≥ u₀} η̃_j ≥ h.
Then μ_i ≥ Σ_{v_j≥u₀} 𝒜_ijη̃_j ≥ h·min_{v ≥ u₀}𝒜_i(v). The bound (4.2) with 𝒜_i(u₀) therefore needs **𝒜_i(v) non-decreasing in v** on
[u₀, v_max]. 𝒜 ≥ 0 is not sufficient. Monotonicity does hold: 𝒜_i(v) = ∫[A^{(0)} + A^{(2)}(v² − v_min²)]Θ(v − v_min) is non-decreasing whenever
A^{(0)} ≥ 0 and A^{(2)} ≥ 0 pointwise. Both follow from PSD of the weighted S: A^{(0)} = tr(𝒱₀†𝒱₀ S) ≥ 0, and v_T·tr(𝒱₁†𝒱₁ S)·v_T ≥ 0 gives d₂ ≥ 0.
Correct statement: "under (P), A^{(0)}, A^{(2)} ≥ 0 pointwise, hence 𝒜_i(v) is non-decreasing in v, hence the minimum is at a single step at u₀."
**C2. Sufficiency of (P).** The package argues that outside the window, "where per-sector positivity fails, P(i|Λ) is constant over the split".
This is an additional hypothesis (call it P′), not a consequence. X0 and X+ final states differ in e–h energy by ω_Q ≤ ω_max ≈ 60 meV. A step
or thresholded cascade, N_eh^{step} = 1 + ⌊(E − E_g)/ε_eh⌋, has jumps, so P(i|X0) ≠ P(i|X+) whenever a jump lies within ω_max. Write
Σ_Λ P S(Λ) = P_{X0}S_tot + (P_{X+} − P_{X0})S_{X+}. Outside the window S_{X+} contains the DC Hadamard finite part, which can be negative, so the
sum can fail PSD at such (q,ω). Corrections owed:
- (i) state P′ explicitly;
- (ii) note that only the **integrated** kernels are needed: K^{(n)}_i(v_min) ≡ ∫ over the (q,ω) with v_min(q,ω) = v_min of A^{(n)}P ≥ 0 (n = 0, 2),
  pointwise in v_min, which is weaker than pointwise PSD;
- (iii) add a `checks` gate: min over v_min of K^{(0)}_i, K^{(2)}_i ≥ 0 for every bin and cascade model. Without it, (4.2) is not guaranteed
  for the step cascade near bin edges. The impact is probably small, but it is not derived.
**C3. Uniqueness (4.2a).** −ln ℒ is convex in η̃ and strictly convex in μ = 𝒜η̃ (for bins with N_i > 0). The optimum μ̂ is unique; the
optimum η̃ is unique only modulo ker 𝒜, which has dimension ≥ N_v − N_bins (≥ 98 for two bins, as (4.3) itself says). 2311.04957 [FT, §2.3]:
"The linearity of the rate … ensures that any minimum of the likelihood in η̃ space is a global minimum", followed by the SVD and flat
directions of §2.4. The attribution is REFUTED and the uniqueness claim is false. Replace it with "every local minimum is global; μ̂ is unique".
**C4. Cost (4.4).** 10 × 100 × 300 × 2500 × 10 ≈ 7.5×10⁹ is correct. Because Θ(v_j − v_min) is cumulative, sorting the (q,ω) cells by v_min and
taking prefix sums removes the N_v factor (≈ 10⁸ operations). Not an error.

## D. Edge, m_min and E_th (focus items 2, 3)
**D1. The q-independent threshold is a hidden hypothesis.** (3.1) treats E_th as a constant. The general condition is
min_q[E_th(q)/q + q/2m_χ] = v_max, where E_th(q) is the onset of S̄(q,·). (3.1) is the special case E_th(q) ≡ E_th; otherwise
2E_th^{glob}/v_max² is a strict *lower bound*. For indirect gaps this matters. At m_χ = 0.333 MeV, q_* = m_χv_max ≈ 0.88 keV ≈ 0.45 Å⁻¹, while
the Si gap is reached at |q| ≈ 0.85·2π/a ≈ 0.98 Å⁻¹ (mod G; no G brings 0.98 x̂ to 0.45 Å⁻¹). The X0 onset therefore satisfies
E_min(q_*) > E_g(0), and S̄_X0(q_*, ω → E_g⁺) = 0. Evaluating at |q| = |K|: v_min = E_g/|K| + |K|/2m_χ ≤ v_max requires
m_χ ≳ |K|/[2(v_max − E_g/|K|)] ≈ 0.47 MeV, the campaign's upper PAER-window edge, consistent. So "Si at mK, E_th = 1.170 eV: m_min = 0.333 MeV" is the edge
of no T = 0 channel. It is a kinematic bound, approached only by phonon-assisted channels in the limit of zero phonon energy, or by the T > 0
absorption branch. The same holds for Ge: 0.212 MeV with q_* ≈ 0.56 keV, far from |K_L|. *Correction:* label 0.333 and 0.212 MeV as
"kinematic lower bounds at E_g". State that the physical edge of each channel is min_q[E_th^{ch}(q)/q + q/2m_χ] = v_max. For PAER, with the
package's own onset E_g^{ren} + c_TA·d(q), d = |K| − |q| for |q| < |K|, minimising (E_g + c_TA|K|)/q − c_TA + q/2m_χ gives
m_min^{PAER} = 2(E_g + c_TA|K|)/(v_max + c_TA)². My estimate: c_TA|K| ≈ 37 meV and c_TA ≈ 5.8 km/s give ≈ 0.339 MeV, within 0.3 % of the quoted 0.338 MeV.
So the number survives, but "E_th = E_g + ω_TA = 1.188 eV" is not the right construction. Likewise "halo and theory enter only through
E_th/v_max², exactly degenerate" holds only for a q-independent E_th, and only for the edge *position*. δ_v,0^{n} = v_max^n(1 − √(m_min/m_χ))^n and
the prefactor e^{−v_esc²/v₀²}/(v_E N_esc) depend on v_esc and v_E separately.
**D2. Exponent survives a q-dependent onset.** Let ω_kin(q) = qv_max − q²/2m_χ touch E_th(q) at q₀ (smooth E_th). Just above the edge,
ω_kin − E_th ≈ ε − c(q−q₀)² with ε ∝ δ_v,0. With v_max − v_min = (ω_kin − ω)/q, the rate is
∫dq∫_{E_th}^{ω_kin}dω (ω−E_th)^{p}(ω_kin−ω)^{2+k} ∝ ∫dq (ε − c x²)^{p+k+3} ∝ ε^{p+k+7/2}. This is the same exponent as (3.3), now without the
"smooth in q" hypothesis on E_th. The (3.3) derivation with the Beta function is correct as written (C5a, C5b re-derived by hand:
∫(Δ − cx²)^{2+k}dx ∝ Δ^{5/2+k}, then ∫y^p(Δ−y)^{5/2+k}dy = B(p+1, 7/2+k)Δ^{p+k+7/2}). A kink in E_th(q) at the tangency point (the d = 0 shell)
changes the exponent; the package correctly excludes the edge shell.
*Degeneracy qualifier (3.4):* dℛ/dω ∝ (ω − E_th)^{p}(ω_max − ω)^{5/2+k}, so p and k enter the ω-shape differently. They are degenerate only
for the edge rate integrated over a bin wider than ω_max − E_th ∝ δ_v,0, which is always the case with ε_eh ≈ 3.75 eV bins. Say so.
**D3. p_on arithmetic.** 7/2 + {3, 4, 4–5, 3/2–5/2} = {13/2, 15/2, 15/2–17/2, 5–6}, all correct. Plausibility check: at fixed q the indirect
e–h pair density near onset is ∝ (ω − E_g − ω_ν)² (allowed). The onset E_g + ω_ν(|K − q|) has a quadratic minimum on the q̂ sphere, so the
2-D angular average adds 1, giving 3. The same +1 turns forbidden 3 → 4 and exciton ½ → 3/2. Bound exciton *lines* (the §5.2 ladder (ii)) have
p_on = −1 and edge exponent 5/2 + k_tail, at E_th − E_x^b. C5b does not cover p_on = −1 (B(0, ·) diverges; use the δ-function directly).
Add that case to (3.3).

## E. Nuisance algebra, (5.1′) (focus item 5)
Constraints: ∫y_R^a Π_mom[X] = ∫y_R^aX − Σ_b c_b𝔪_{a+b} = 0 for a = 0, 1, 2. 𝔪 is a positive Hankel matrix, invertible when S^τ has ≥ 3 support
points. The third constraint matches the impulse second moment q²⟨p_q̂²⟩/M_κ² = 2q²E^kin_q̂/M_κ. **The constraint part is correct** (C15a re-derived).
The M-type violation θ(θ−1)(r^M)²/… is correct.
Defects:
- (i) **Positivity collapses the prior.** S(θ) is affine in (θ_A, θ_δ), so {S ≥ 0} is convex, as claimed. But θ_δS^τP_δ ∼ θ_δ p₂y_R²S^τ and
  −θ_AS^τΣc_by_R^b dominate wherever S^τ ≫ the Δ terms, in particular in the Gaussian (impulse) tails, which are unbounded in y_R. There
  S ≥ 0 for all large |y_R| forces sign(θ_δ) = sign(p₂), and likewise for θ_A unless Δ′_A dominates the tails. The admissible set is then a
  half-line, so "θ_δ ~ 𝒩(0,1)" cannot be realised, and the profile sits on the boundary for half of the prior (non-standard asymptotics). On a
  finite binned grid it is a cut-dependent half-space.
  *Remedy (derivable):* exponential tilting, S(θ) = (S^τ + Δ^τ_A)·exp(Σ_{b=0}^{2}λ_b(θ)y_R^b) together with the shape term. The λ_b(θ) are fixed by
  the three moment equations, which are a convex dual problem with a unique solution when the targets lie inside the moment cone. This gives
  PSD for all θ, exact constraints, and is smooth in θ. Alternatively, apply the quadratic correction on a compact y_R window and state the
  truncation.
- (ii) "θ_A ~ 𝒩(0,1) is type A" contradicts (5.1)(A), which defines A as a^A_k > 0 log-normal. The (5.1′) form is the withdrawn additive Gaussian
  (WP6-W2) restricted to a positivity support. Call it a fifth type (affine, support-restricted) and record that it is the only non-PSD-by-construction type.
- (iii) "Π_mom[X] ∝ S^τ × quadratic, so the projection opens no new support" is false. Π_mom[X] = X − S^τ×quadratic; only the subtracted part
  is ∝ S^τ. The correct statement is supp Π_mom[X] ⊆ supp X ∪ supp S^τ.

## F. Profile vs envelope (focus item 6)
Re-derived. −2ln ℒ = 2sμ(θ) + θ². Linear case: θ̂ = −sδ and s²δ² − 2s + 2.71 = 0, so the ratio is 2(1−√(1−2.71δ²))/(2.71δ²) = 1.276 at 0.5. There is no limit
for δ > 2.71^{−1/2} = 0.61, which is not stated. Log-normal: θ̂ = −W_Lam/k_δ with W_Lam = √(1+2.71k_δ²) − 1, ratio 2W_Lam e^{W_Lam}/(2.71k_δ²) =
1.006, 1.047, 1.112, all correct. Expansion: 1 + (2.71/4)δ² + O(δ³). **Error:** the envelope 1/(1−δ) is the *linear* worst case. For the M-type
(1+δ)^θ at |θ| ≤ 1 the envelope is 1+δ = 1.1, 1.3, 1.5. Like-for-like spreads at δ = 0.5 are 1.5/1.112 = **1.35** (M-type) and 2.0/1.276 = **1.57**
(linear). "Up to ×1.8 (2.0/1.112)" compares different nuisance models and must be withdrawn here and in WP0-v2 (8.3) and C8c.
The O(δ²) vs O(δ) conclusion stands.

## G. Remaining items
- (6.4) "exact recast σ̄^{up,lib} = min_i N_i^up/s_i^lib" is exact only for a limit *defined* as the minimum over per-bin limits (no trials
  correction). It is not a recast of a combined-bin CL. Add that qualifier.
- (6.1) The attribution of "two-sided PLR … PCL at −1σ" to 2105.00599 was not checked (not fetched). UNRESOLVED; not a wrongness claim.
- (2.5) WP6-D6 quotes 2105.00599/2011.12896. Not fetched; not a wrongness claim.
- Notation (rubric d). NOTATION v4 reserves K for "kinematic regime label inside τ (only)", but (3.3) and §15 use K for the connecting phonon
  wavevectors. δ ("off-shell distance", NOTATION §A) is used in (4.2) correctly and again in (6.2) as the fractional nuisance size. d (the edge
  distance) has no row. Contrary to the claim "no deviations": rename them (e.g. K_ph, δ_θ, d_K).
- WP0-v2 interfaces: (8.1) and (8.3) mirror (5.1) and (6.1)–(6.3), including the ×1.8 (§F). (9.2) = (1.4) is verified. F9 τ string: C13 confirmed.
- Controls: the reduction to L24 is visible (C1). CONTROLS C5 (no PAER below E_g + min ω_Q at T = 0) is consistent with §D1, but (3.1)'s
  0.333 MeV must not be presented as a channel edge.

## H. Required corrections (summary)
1. §D1: state that E_th(q) is q-independent as a hypothesis in (3.1). Give the general min_q condition, and relabel 0.333 and 0.212 MeV as kinematic bounds.
2. §B2: replace the linearised edge sensitivities (e^{±1.17}, "≈ 2.5") by the exact asymmetric factors, or by (1 ± Δv_max/δ_v)^{2+k}.
3. §C1–C2: base the single-step minimum on the monotonicity of 𝒜_i(v). State P′, the integrated-kernel condition, and its check gate.
4. §C3: withdraw the uniqueness claim and its attribution to 2311.04957.
5. §E: fix the positivity, typing and support statements of (5.1′); exponential tilting is recommended.
6. §F: replace ×1.8 by 1.35 (M) or 1.57 (linear), here and in WP0-v2 (8.3).
7. §A2–A3: define the orientation average for tensor S_ab. Say that TR removes all odd ℓ, that cubic groups have no ℓ = 1 invariant, and give the n = 2 anisotropy form.
8. WP6-D4: add the Θ(v_esc − v_χ) typo of 1509.01598 Eq. (67). (V2) rewording; §3.5 sizes (6.8 %/13.6 %; 2.6 %); notation K, δ, d.
