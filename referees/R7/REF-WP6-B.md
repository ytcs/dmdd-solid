# R7 / REF-WP6-B: hostile referee report on returns/R6/WP6-v2.md

Referee B, isolated. I read only: WP6-v2, code/WP6-v2/checks.py, CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS, WP0-v2.
Full texts fetched and read for (c): 2311.04957v2 and 1509.01598 (both deleted afterwards). checks.py rerun: 27/27 PASS (≈ 30 s).
I ran no simulations. The only computation was a sympy/mpmath evaluation of the paper's own closed form for η (finite shifts, §B3).

## Verdict table
| # | Claim (WP6-v2 location) | Verdict | One-line reason |
|---|---|---|---|
| 1 | General halo functional, f̂^{(n)} Radon moments (1.1)–(1.2) | STANDS | Follows from (1.1) and the degree-2 polynomial in v_T |
| 2 | Isotropic reduction; n = 1 drops; ξ = 2∫u′η du′ (1.3)–(1.4) | STANDS WITH CORRECTION | Correct for v_min ≥ 0. For exothermic DM, v_min < 0 is possible and Θ(v − u) must be Θ(v − \|u\|) |
| 3 | Cubic: ℓ = 4 first; P,T-broken: odd ℓ "leading ℓ = 1" (1.5), (V3), (2.4a) | STANDS WITH CORRECTION | Counts are right. ℓ = 1 is forbidden in every cubic magnetic group. The ℓ = 1 axial projection survives the daily average, so it is not a "beyond (I)" effect only |
| 4 | Dictionary (1.6); per-target vs per-cell factors | STANDS | Algebra rechecked (C1–C3). 1509.01598 Eq. (17) carries N_cell (FT). Spin factor not re-audited (owned by AUDIT A2–A5) |
| 5 | μ_i linear in S; seeding inside the q integral (1.7) | STANDS | Identical to WP0-v2 (7.3) |
| 6 | L24 chain, validity, leading corrections (§2) | STANDS WITH CORRECTION | Chain is valid. The linearised v_esc ±25 km/s "×3.2" is wrong (exact: ×2.26 / ÷10.0). Equation-number convention must be declared |
| 7 | WP6-D1…D5 (claims against 2311.04957, 1509.01598) | D1–D5 CONFIRMED (D1 last sentence UNRESOLVED) | See §C. A new misattribution, "unique η̃ profile (as 2311.04957 states)", is REFUTED |
| 8 | m_min and the E_th convention (3.1): Si 0.333, PAER 0.338, Ge 0.212 MeV | STANDS WITH CORRECTION | Arithmetic exact. 0.333 and 0.212 are kinematic lower bounds that no channel reaches at T ≈ 0 in indirect-gap Si or Ge |
| 9 | Regimes of η, δ_v,× = 173 km/s (3.2) | STANDS WITH CORRECTION | Series exact (C4d). The finite-shift sensitivities are misquoted (item 6) |
| 10 | Edge exponent 7/2 + k_tail + p_on (3.3)–(3.4) | STANDS WITH CORRECTION | Holds for q-independent or smoothly q-dependent onsets; 4 + k_tail + p_on at a corner of E_th(q). Valid only within Δm/m ≲ 1–3%. The "Si TA p_on = 4" bullet cannot control δ_v,0 at m_min |
| 11 | 𝒜_ij formula (4.1) | STANDS | Units and the step algebra check (C14) |
| 12 | Positivity, hypothesis (P), and the halo-independent bound (4.2) | STANDS WITH CORRECTION | The bound is true, but "because 𝒜 ≥ 0" does not prove it: it needs monotonicity of the step column (derived in §D). The "proof of sufficiency" of (P) is a restatement. Uniqueness is false |
| 13 | Mass degeneracy (4.3) | STANDS | Write dim ker 𝒜 ≥ N_v − 2 (inequality) |
| 14 | Nuisance types M/A/E/Δ (5.1); "positivity automatic for M and A" (5.3) | STANDS WITH CORRECTION | M is not PSD-preserving for the matrix S_ab elementwise. A is not positive outside the window (DC X+ is not PSD). Two prior ranges are inconsistent with their types |
| 15 | Constraint-preserving anharmonic form (5.1′) | STANDS WITH CORRECTION | The construction is right (C15a). The sentence "Π_mom[X] ∝ S^τ × quadratic, so no new support" is false as written |
| 16 | f-sum informs only non-conserving truncations (5.3) | STANDS WITH CORRECTION | True with local potentials. The adopted rungs (scissor / GW–BSE) are non-local, so the check is informative there |
| 17 | Profile O(δ²) vs envelope O(δ); "up to ×1.8" (6.2) | STANDS WITH CORRECTION | Closed forms exact. ×1.8 compares a linear envelope with a log-normal profile; at the same type it is ×1.35 (M) or ×1.57 (linear). WP0-v2 (8.3) inherits the error |
| 18 | Three reported objects, combination, recast, publication standard (6.3)–(6.5) | STANDS | "Exact recast" holds only for the min-over-bins procedure, whose CL is below nominal |
| 19 | Library spec, grids, cost (§7, (4.4)) | STANDS WITH CORRECTION | Profiling with M-types needs a full recontraction per θ evaluation, not only ∂𝒜/∂θ |
| 20 | Gap closure: G8 "closed", G4 fix, G8′ exact gap | STANDS WITH CORRECTION | G8 needs the §D proof repair. G4 and the G8′ statement are adequate formula + spec + exact gaps |
| 21 | Contested corrections: none (§12) | STANDS | The 252.1 vs 250.5 remark is arithmetically right (−0.4%) |
| 22 | Checks script (27, "exact proofs") | STANDS WITH CORRECTION | All pass. C10a/b are single-point spot checks; C11 does not test the TR claim; C5b falls back to a numeric tolerance |

---
## A. Halo reduction (focus g1)

**A1. (1.3) is correct for v_min ≥ 0.** With v at polar angle θ to q̂, ⟨δ(q̂·v − u)⟩_q̂ = ½∫d cosθ δ(v cosθ − u) = Θ(v − |u|)/(2v).
Similarly ⟨|v_T|²δ⟩ = (v² − u²)Θ(v − |u|)/(2v). Leibniz on ξ(u) = ∫_{|u|}^{v_max} g(v)(v² − u²)dv gives dξ/du = −2uη (the boundary term vanishes).
Correction: §1.2 claims generality "for inelastic DM". For Δ_χ < 0, v_min = (ω + Δ_χ)/q + q/2m_χ can be negative, so η and ξ must be evaluated at
|v_min|. Equivalently, ξ = 2∫_{|u|}^∞u′η du′. The step basis (4.1) and the bound (4.2) carry the same |·|.
The angular factor (2π)⁻³·4π·½ = 1/(4π²) of (1.4) checks, and so does the n_e reduction to WP0-v2 (9.2).

**A2. n = 1 term and A^{(2)}.** Under (I), M_cd ≡ Σ_ab𝔇^{(2)}_{ab,cd}S̄_ab is a rank-2 tensor built from q̂ alone:
d₂δ + d₂′q̂q̂ + d₂″ε_cde q̂_e. Contracting with v_Tv_T kills the q̂q̂ and antisymmetric parts; the n = 1 scalar is ∝ q̂·v_T = 0. Correct.
I add a fact the package needs in §D: **A^{(0)} ≥ 0 and A^{(2)} ≥ 0 pointwise.** With 𝒱_a = α_a + β_a·v_T,
𝔇^{(2)} = ⟨β β†⟩ is PSD in the joint index. For any w ⊥ q̂, Σ w_cw_d M_cd = Σ_ab ⟨(β·w)_a*(β·w)_b⟩S̄_ab ≥ 0 when S̄ is PSD. Hence d₂ ≥ 0.
A^{(0)} = tr[𝔇(v_T = 0)S̄] ≥ 0.

**A3. Odd ℓ (1.5).** The O_h and T_d even-ℓ counts are right (C11 rerun: 1,0,1,1,1,1,2 for ℓ = 0…12). S(q) = S(−q) under either P or T kills odd ℓ.
Two corrections:
- (i) ℓ = 1 needs a polar vector invariant under the magnetic point group, and no cubic magnetic group has one. "Leading ℓ = 1" should read
  "lowest odd ℓ allowed by the magnetic group (ℓ = 1 only for polar groups)".
- (ii) The odd part is not removed by the day average. A crystal fixed in the lab samples the wind direction on a cone about the Earth's axis n̂.
  The m = 0 projection along n̂ of every ℓ (ℓ = 1 included) survives the daily mean. So for P,T-broken targets the error of (I) on the
  day-averaged rate is first order in 𝐛_NR, not the "few % ℓ = 4" of (V3). (V3) and (2.4a) must say so; the same holds for ℓ = 4 in cubic targets.

## B. L24 chain and numbers (rubric b)
The chain (2.2) steps 1–7 is valid. C4a proves the SHM closed form exactly. The source formulas match the full texts. The values 230/600/240 and
ρ_χ = 0.4 are in 1509.01598 App. B and Eq. (17) text; 220/544/232 and ρ_χ = 0.4 are in 2311.04957 §2.1 and §3.

**Equation numbering.** The package's numbers are the arXiv-HTML sequential tags. For 2311.04957, the PDF (v2, JCAP style) numbers Eq. (3)
as (2.1), (4) as (2.2), (13) as (2.11), (19)–(20) as (2.17)–(2.18) and (17) as (2.15). For 1509.01598, (65)–(68) are (B.1)–(B.5).
§10 must declare the convention, or a reader with the PDF cannot find the equations.

**Sensitivities (3.2), (V4), and C4c.** The derivatives are correct. The finite shifts are not linear. From the exact η₂ at v_min = 760 km/s
(δ_v = 34.5 km/s): v_esc +25 → ×2.26 and v_esc −25 → ×0.100 (÷10), not "e^{±1.17} ≈ ×3.2". The annual extremes give ×2.22 / ×0.373 at 760 and
+21.5% / −15.5% at 600; the package's "≈ 2.5" and "±19%" are acceptable. A linearised e^{±x} is invalid once |Δv| ~ δ_v, so state the
asymmetric exact factors.
"∂ln η/∂v_esc ≈ 2/δ_v … (the O(δ_v/δ_v,×) term included)" misattributes the gap between 2/δ_v = 0.058 and 0.047. The gap comes mainly from the
prefactor term −2v_esc/v₀² = −0.019 per km/s.
(3.5) "δ ln v_max ≈ 3–6%": 528 → 2.0%, 503 → 5.2%, 600 → 7.0%, so the range is 2–7%.

## C. Claims that published papers are wrong (rubric c; full texts read)
- **WP6-D1: CONFIRMED.** 2311.04957 Eq. (2.1), with |f_res|² = 8αm_e²E_e|f_crys|²/q³ (2.2), equals
  (ρ_χσ̄_eαm_e²/m_χμ²)∫d ln q (E_e/q)ηF²|f_crys|². That is 1509.01598 Eq. (17) without N_cell. The text does not say "per cell".
  The sentence "η̃_i in yr⁻¹ … absorbs the target size" is **UNRESOLVED**. η̃ = ρ_χσ̄_eη/m_χ has natural-unit dimension 1/time whatever the
  target, so yr⁻¹ absorbs nothing. Where N_cell entered their kg·yr fits cannot be read from the text. Downgrade it to [E].
- **WP6-D2: CONFIRMED, as an ambiguity, not an error.** (2.11) uses limits q± from (2.5), defined "for a fixed v", with v unspecified, and also
  includes Θ(v_i − v_min). For any v ≥ v_i the Θ makes the limits redundant, so this is harmless if v = v_max.
- **WP6-D3: CONFIRMED** (values as quoted).
- **WP6-D4: CONFIRMED.** (B.1) has |v_χ + v_E|²; (B.3) writes −2vv_Ec_θ. Add: (B.3) also writes Θ(v_esc − v_χ) where (B.1) has
  Θ(v_esc − |v_χ + v_E|). That one is harmless too, since (B.4)–(B.5) use the correct region.
- **WP6-D5: CONFIRMED.** E_gap = 1.2 eV and ε = 3.8 eV for Si; 0.67 / 3.0 for Ge. 2·1.2 eV/(776 km/s)² = 0.358 MeV. This is a convention
  difference, not an error.
- **New: (4.2a) "the η̃ profile is unique (as 2311.04957 states)": REFUTED.** The paper says only that "any minimum of the likelihood in η̃
  space is a global minimum" (§2.3), and §2.4 is devoted to the flat directions ker 𝒜. The Poisson −ln ℒ is strictly convex in μ, but
  μ = 𝒜η̃ with dim ker 𝒜 ≥ N_v − N_bins > 0. So the minimum value and μ̂ are unique, and η̃̂ is not. This contradicts (4.3) of the package itself.
  Two smaller points. Convexity needs only μ + b > 0, not 𝒜 ≥ 0, so it is not a "consequence" of positivity. And "here with θ included" is
  false jointly: 𝒜(θ)η̃ is bilinear and M-types are exponential in θ, so convexity holds only at fixed θ.

## D. The halo-independent bound and hypothesis (P) (focus g4; OW6-6)
**D1. The stated proof is insufficient.** Write a non-increasing η̃ ≥ 0 as η̃(u) = ∫Θ(v − u)dν(v) with ν ≥ 0, so μ_i = ∫𝒜_i(v)dν(v).
The constraint η̃(u₀) = h means ν([u₀,∞)) = h. Then

  μ_i ≥ ∫_{[u₀,∞)}𝒜_i(v)dν(v) ≥ h·inf_{v ≥ u₀}𝒜_i(v).

This equals h·𝒜_i(u₀), as (4.2) claims, **only if the step column 𝒜_i(v) is non-decreasing in v**. Positivity of the columns (𝒜_ij ≥ 0)
does not imply that: a column kernel negative on some v-interval but with positive cumulative integrals has 𝒜_ij ≥ 0 and still breaks (4.2).
**Repair (derived).** 𝒜_i(v) = 𝔈_i(4π²ρ_T)⁻¹∫dω∫q dq Σ_Λ[A^{(0)} + A^{(2)}(v² − v_min²)]P(i|Λ)Θ(v − v_min). This is non-decreasing in v
whenever Σ_Λ A^{(0)}(Λ)P(i|Λ) ≥ 0 and Σ_Λ A^{(2)}(Λ)P(i|Λ) ≥ 0 pointwise in (q,ω). By A2, both follow from (P) and the PSD of 𝔇.
So (4.2) holds under (P), with inf_{v≥u₀}𝒜_i(v) = 𝒜_i(u₀). Replace "because 𝒜 ≥ 0" with this argument.
**D2. (P).** The argument says "where per-sector positivity fails, P(i|Λ) is constant over the split". That is the hypothesis restated, not a
proof (closing-table row 13 calls it a "proof of sufficiency"). Under DC, the X0 seed (Λ₀, n_ph = 0) and the X+ seed (Λ₊, n_ph = 1) of the
same pair differ in electronic energy by ω_Q. P_casc(N_eh|Λ) differs between them whenever that energy straddles a cascade threshold:
a fraction O(ω_Q/ε_eh) ≈ 1–2% of pairs in Si, and every pair in the lowest bin near E_g. (P) is therefore guaranteed only:
- (i) inside the window;
- (ii) where P(i|·) is taken Λ-independent, as the package's d11 rule does in the edge shell;
- (iii) where X0 and X+ of one pair are seeded with a common P (summed per Λ₀).
State (P) as a hypothesis, with this as its sufficient condition. Report the O(ω_Q/ε_eh) leakage as unbounded in sign.
**D3. CL.** min_i N_i^up/𝒜_i over bins, each at 90% CL, has coverage below 90% (a trials factor). The same applies to the "exact recast" (6.4).
State the CL of the combined object.

## E. The edge (focus g2, g3)
**E1. m_min arithmetic (C7).** I rechecked it: 2·1.170 eV·(c/794.5 km/s)² = 0.333 MeV; 1.188 eV → 0.338 MeV; 0.744 eV → 0.212 MeV.
The annual range is 0.320–0.344 MeV. The E_th convention (measured E_g(T_op)) is applied consistently.
**Correction (physics).** The total S̄_ee of Si at T ≈ 0 vanishes at ω = E_g for every q that is kinematically available near 0.333 MeV:
- X0 (first order) needs |q| ≈ |K| = 0.85·2π/a = 0.983 Å⁻¹ = 1.94 keV. That requires |K|v_max − |K|²/2m_χ ≥ E_g, i.e. m_χ ≥ 0.474 MeV
  (the ZPL edge).
- X+ needs a phonon (CONTROLS C5), with onset E_g + ω_ν(K − q), q ≈ q_* = m_χv_max ≈ 0.45 Å⁻¹.
So 0.333 MeV is a strict kinematic lower bound that is never reached. The attainable Si edge is the PAER one, ≈ 0.337–0.338 MeV
(ω_TA at |Q| ≈ 0.53 Å⁻¹ may be a few meV below 18 meV; ≤ 0.5%, well inside the halo band).
Ge is the same: indirect L edge, direct E₀ ≈ 0.89 eV at q → 0; attainable ≈ 0.214 MeV with the L-point TA, not 0.212.
Label 0.333 and 0.212 "kinematic lower bounds at E_th = E_g". Generally, m_min = min_q q²/[2(qv_max − E_th(q))]. This depends on E_th(q), not on
E_th/v_max² alone, so the "exact degeneracy" of halo and gap holds for the edge position only to O(|dE_th/dq|/v_max) ~ c_ν/v_max ~ 1%.
It also does not hold for the edge amplitude, which depends on v_esc, v_E and a_lens separately.
**E2. Exponent with a q-dependent onset (derived).** Near the edge, η ∝ (v_max − v_min)^{2+k}, and v_max − v_min = (ω_kin(q) − ω)/q with
ω_kin = qv_max − q²/2m_χ. With S̄ ∝ (ω − E_th(q))^p:

  ∫dω (ω − E_th)^p(ω_kin − ω)^{2+k} = B(p+1, 3+k)·G(q)^{p+3+k},   G ≡ ω_kin(q) − E_th(q).

- **Smooth contact,** G ≈ ε − c(q − q_c)²: ∫dq G^{p+3+k} ∝ ε^{p+k+7/2}. This reproduces (3.3) and extends it to smooth E_th(q). ε ∝ δ_v,0.
- **Corner contact,** G ≈ ε − s_±|q − q_c| (a V-shaped onset such as E_g + c_TA·||q| − |K||): ∝ ε^{p+k+4}.

The package's hypothesis "smooth in q near q_*" is stated, but the bullet "Si TA edge: p_on = 4 at E_g^{ren} + c_TA·d" describes the fixed-q
onset at |q| ≈ |K|. That is kinematically inaccessible for m_χ < |K|/(2v_max) ≈ 0.366 MeV. So it does **not** set δ_v,0 at the window's lower
edge (0.338 MeV). There the contact is near q_* ≈ 0.45 Å⁻¹, a smooth interior minimum over (k, Q, q̂) (8 dimensions minus 1 δ-function
→ p_on = 3 for M̃ ≠ 0; this agrees with the package's "generic" value). Correction: at m_min the edge exponent is 13/2 + k_tail (15/2 on a
vertex zero). The TA value 15/2 applies only to the fixed-q ω-onset at |q| ≈ |K|. The p_on assignments themselves (WP3-owned) were not checked.
**E3. Validity window.** The power law needs ω_max − E_th = E_th·2δ_v,0/v_max (to first order) to lie inside the range where
S̄ ∝ (ω − E_th)^{p_on} holds. That range is ~ω_ph ≈ 10–60 meV (PAER) or ~E_x^b = 14.7 meV (excitons), so δ_v,0/v_max ≲ 0.5–3% and
Δm_χ/m_min ≲ 1–5%. "The lowest-mass part of every ER curve is controlled by …" overstates the reach. Quote this window, for example in (3.3)
and in §8 "not an exponential".
**E4. (3.4) lens.** Rederived. The thickness is δ_v − a_lensϱ² with a_lens = 1/(2v_esc) − 1/(2v_min) ≈ 1/(2v_esc) − 1/(2v_max) at leading order.
k = 0 reproduces (3.2) (C5c). It is correct for δ_v ≪ v_E, v_esc. The k_tail ↔ p_on degeneracy is a degeneracy of the exponent only.

## F. Nuisances (focus g5) and profiling cost (focus g6)
**F1. M type on matrices.** S_ab(θ) = S^τ_ab(1 + r_ab)^θ elementwise is not PSD-preserving for the 16×16 S_ab of §7.1. Elementwise powers of
a PSD matrix are not PSD in general, and r_ab is undefined where S^τ_ab = 0. "PSD for all θ" (5.1; WP0-v2 (8.1)) holds only for scalar
responses: S_ee, or A^{(n)} after contraction with a fixed 𝔇. Fix: apply M to contracted scalars (per operator class), or use the PSD geodesic
S^τ½(S^{τ−½}S^{τ+e_k}S^{τ−½})^θS^τ½.
**F2. A type is not automatically positive** ((5.3) "Positivity is automatic for M and A"). S^τ + a^A_kΔ^τ_k ≥ 0 for all a > 0 only if Δ^τ_k ≥ 0
(PSD). That holds for the in-window sideband and for new exciton lines. It fails outside the window, where the DC X+ part (Hadamard fp and PV
pieces) is not PSD (WP0-v2 §6.2(i)), and for any increment that carries its own ZPL-loss compensation. There, a^A_k must act on X0 + X+
jointly, or be restricted to the window. This interacts with (P) (§D2).
**F3. Prior ranges inconsistent with their types.**
- (a) Ladder row (i): M type with "68% range r^M_𝒳 ∈ [+0.3, +1.0]". Under (5.1), θ = 0 is S^τ (r = 0), which lies outside that range, and
  θ = ±1 is symmetric in log about S^τ. To encode it, put the central value at S^τ·√(1.3·2.0) ≈ 1.61 S^τ with log-width ln(2.0/1.3)/2 ≈ 0.22.
- (b) e–ph row: A type with "a^A_k log-normal, 68% range [0.5, 1.2]" and "central value a^A_k = 1". ln 0.5 = −0.69 and ln 1.2 = +0.18 are not
  symmetric, so the median is 0.77, not 1. State the median and log-width.

**F4. (5.1′).** C15a holds: ∫y_R^aΠ_mom[X] = ∫y_R^aX − Σ_b𝔪_{a+b}c_b = 0 for a = 0, 1, 2. P_δ is solvable with the same 𝔪. Positivity defines a
convex set, since S is affine in (θ_A, θ_δ). The O(θ(1 − θ)(r^M)²) violation of the M type is right (to second order the zeroth moment is
θ(θ−1)/2·∫r²S^τ). The Placzek second-moment constraint 2q²⟨T_q̂⟩/M_κ is right.
Correction: "Π_mom[X] ∝ S^τ × quadratic" is false. Only the subtracted part is ∝ S^τ × quadratic, so supp Π_mom[X] = supp X ∪ supp S^τ.
The no-new-support statement needs supp Δ′_A ⊆ supp S^τ. That is true for the NR self part, but it must be stated as a condition.
**F5. (5.3).** "Every rung of the 𝒳 ladder with local potentials is conserving" is true. The central τ* uses PBE + scissor, and Δ_𝒳 uses BSE on
GW or scissor bands. Both are non-local, and [H_QP, n] ≠ q·j. So the f-sum is informative for exactly the rungs adopted. Add it to the list of
non-conserving cases.
**F6. (6.2) closed forms (C8 rerun).**
- Linear: θ̂ = −sδ, ratio 2(1 − √(1 − 2.71δ²))/(2.71δ²). Correct; it has no solution for δ > 0.607 (the limit diverges).
- Log-normal: w = −θ̂k_δ = √(1 + 2.71k_δ²) − 1 is an explicit root of w² + 2w − 2.71k² = 0, so "Lambert-W" and W_Lam are misnomers.
  Ratios 1.006 / 1.047 / 1.112 are correct.
- **Error:** "×1.8 (2.0/1.112)" divides the *linear* envelope 1/(1 − δ) by the *log-normal* profile. With one type throughout:
  - M (the type the package mandates in R2/R3): envelope (1 + δ)^{+1} → 1.5 at δ = 0.5, so ×1.35.
  - Linear: 2.0/1.276, so ×1.57.
- "Profile O(δ²), envelope O(δ)" stands. Fix the number in (6.2), §8 and WP0-v2 (8.3).

**Profiling cost.** For M-types 𝒜(θ) is non-linear in θ. Each likelihood evaluation during profiling needs a fresh contraction
(≈ 10¹⁰ operations by (4.4)), so profiling over K nuisances costs ~10²–10³ evaluations, i.e. 10¹²–10¹³ operations per m_χ. "∂𝒜/∂θ_k from the
same contraction" gives only the linearisation at θ = 0, so state the cost or the linearisation. A cheaper route: the Θ(v_j − v_min) structure
makes 𝒜_i(v_j) a cumulative sum over a v_min-sorted (q,ω) list, which removes the N_v factor.

## G. Consistency (rubric d) and minor items
- WP0-v2 interfaces (3.4), (4.3), (4.4), §6.2(i), (7.1)–(7.3), (8.1)–(8.3), (9.1)–(9.2) are cited correctly. Two inherited defects:
  - (8.1) "M PSD for all θ" (F1);
  - (8.3) "×1.8" (F6).
- NOTATION collisions:
  - K (the "connecting phonon wavevectors" of (3.3) and §15) collides with the τ slot K;
  - δ is used both for the window detuning ((4.2) "bins coarser than δ") and for the fractional nuisance size in (6.2).
  Rename locally, e.g. 𝐊_c and δ_θ.
- (4.3) dim ker 𝒜 ≥ N_v − rank 𝒜: write "≥".
- Checks:
  - C10a/b test one point (v = 3, u = 1), not the identity;
  - C11 asserts the T_d ℓ = 3 invariant exists, but never tests "removed by TR" (that follows from S(q) = S(−q), §A3);
  - C5b accepts |Δ| < 10⁻²⁵ at Δ = 2 for some p.
  None is wrong, but "exact proofs" overstates these three.
- G8: closed by (4.1) + (4.2) + (4.4) once §D is repaired. G8′ (moment problem for Radon transforms on the sphere) is correctly an exact gap.
  G4: the formula, specification and exact remaining gaps (7.5) suffice, with F1–F3 fixed.

## H. Required corrections (summary)
1. (1.3): |v_min| for exothermic DM.
2. (1.5), (V3): ℓ = 1 is not generic. The axial m = 0 odd part survives the day average.
3. (3.2), (3.5): exact asymmetric finite-shift factors; δ ln v_max 2–7%.
4. §10: declare the equation-number convention (HTML sequential vs JCAP sectional).
5. WP6-D1: downgrade "absorbs the target size" to [E].
6. (4.2a): drop "unique (as 2311.04957 states)". Convexity holds at fixed θ only and does not need 𝒜 ≥ 0.
7. (4.2): replace the positivity argument with the monotone-column proof (§D1). State (P) with its sufficient conditions and the
   O(ω_Q/ε_eh) caveat (§D2), and the CL of min over bins.
8. (3.1): label 0.333 and 0.212 MeV as unattained kinematic bounds; give m_min = min_q q²/[2(qv_max − E_th(q))].
9. (3.3): at m_min the PAER exponent is 13/2 + k_tail (generic). The Si TA 15/2 is not an edge exponent. Add the corner case (4 + k + p) and the
   validity window Δm/m ≲ 1–5%.
10. (5.1), WP0-v2 (8.1): define M on scalars or on the PSD geodesic. A-type positivity only for PSD Δ (in window). Fix the two prior ranges.
11. (5.1′): correct the support sentence.
12. (5.3): scissor and GW–BSE rungs are non-conserving.
13. (6.2), §8, WP0-v2 (8.3): ×1.35 (M) / ×1.57 (linear), not ×1.8. Rename W_Lam.
14. (4.4): state the profiling cost.
