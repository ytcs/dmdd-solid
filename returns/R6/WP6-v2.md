# R6 / WP6-v2: rate assembly and uncertainty quantification (corrected standalone version)

Revision agent, brief R6/REV-WP6. Supersedes returns/R5/WP6.md (v1), which stays as the historical record. Applies every owed correction
in state/CORRECTIONS.md §0 and §12, the coordinator additions and WP0-v2 flags routed to WP6 (F9, F11), and resolves every inconsistency
with WP0-v2 and with the WP1–WP5/O4 interfaces recorded in SOTA/CORRECTIONS (closing table §14). Conventions: CONVENTIONS.md; symbols:
NOTATION v4. WP0 equations are cited as **WP0-v2 (s.n)**. Assigned work: L24, G4, G8.
Checks: `code/WP6-v2/checks.py`, sympy only (closed forms evaluated with evalf; no numpy/scipy, no simulation), 27 checks, all PASS,
≈ 26 s; cited as WP6v2-Cn. v1's numerical quadratures and fits are replaced by exact proofs (C4a, C5b, C8b, C12).
Tags: **[D]** derived (hypotheses stated), **[D, sketch]**, **[E]** estimated, **[C]** conjectured; literature **[FT]** full text, **[ABS]**
abstract/title only. Labels from other returns carry their prefix (CONVENTIONS §14). Status: CLAIMED, pending R×2.
Equation numbers: v2 keeps v1's numbers. v1 used "(1.5)" both for the dictionary equation and for the anisotropy section, and WP0-v2 cites
WP6 (1.5) = anisotropy and WP6 (1.6) = dictionary; v2 adopts that reading (equation number = section number throughout).

---
## 0. What changed (v1 → v2)
| v1 | v2 | change |
|---|---|---|
| v_⊥, u_∥, δ, Δ₀, K, A₀, A₂, p, k, ν_e, ρ_mat, r_k, ε, X, Δ_k, f, dR | v_T, v_∥, δ_v, δ_v,0, N_esc, A^{(0)}, A^{(2)}, p_on, k_tail, θ^det_ex, r_mat, r^M_k, ε_eh, 𝒳, Δ^τ_k, f_χ, dℛ | NOTATION v3 renames (CORRECTIONS §0, §12) |
| eq. (1.5) dictionary | (1.6) | renumbered so that WP0-v2's citations hold |
| (1.7), (4.1) P_i(ω) outside the q integral | (1.7), (4.1) | operator- and Λ-resolved seeding inside the q integral (WP0-v2 (7.3); WP5-1, WP5-2) |
| (4.2) 𝒜 ≥ 0 | (4.2) | per-sector positivity hypothesis added (WP0-v2 §6.2(i), O4) |
| §2.3 V4, §2.5 D3, §9 N1 v_E | §2.3, §2.5, §3, §6.3 | v_E(t) in integrals; v_E^ref = 250.5 km/s, v_max = 794.5 km/s; 252.1 and [781, 810] in the halo band |
| (3.2) regime A "v_E + v₀ ≲ v_min < v_esc − v_E" | (3.2) | that interval is empty; regimes set by δ_v vs δ_v,× = 173 km/s (WP6v2-C4c,d) |
| (3.4) tail exponent [D given form] | (3.4) | proved for any tail vanishing as (v_esc − |v + v_E|)^{k_tail} (WP6v2-C5c) |
| §5.2 table | §5.2 | n_T split (order vs T metadata); ladder error = computed next rung, interim BSE range [+0.3, +1.0] (M) + exciton lines (A) (WP1-v2 [E8]); WP5 and WP2 nuisances; F11 order |
| §7.3 `nT=130K`, `M=-` | §7.3 | `nT=0`, `Mg=-`, T/ref/scr/conv metadata (CONVENTIONS §11; WP0-v2 F9) |
| §7.1 S_Lambda, P_Neh | §7.1 | per-operator Λ-marginals, no plasmon label in RPA, retarded out-state LFE weight, O4 d1–d11 gates |
| §9 W1–W5, N1 | §9 | all applied in WP0-v2 (rows 23–27) and CONVENTIONS §8; kept as record |
| — | §12–§15 | contested corrections (none), interface flags, closing table, symbol table |

---
## 1. Rate assembly from WP0-v2 (3.4): the general halo functional

**(1.1) On-shell kinematics [D].** Hypotheses: WP0-v2 (3.3)–(3.4) (first Born, Gibbs target, unpolarised DM) and a lab-frame f_χ(v).
With ω_q from WP0-v2 (2.1),

  δ(ω − ω_q) = q^{-1} δ(q̂·v − v_min),   v_min(q,ω) = (ω + Δ_χ)/q + q/2m_χ.                                                    (1.1)

On shell write v = v_min q̂ + v_T, q̂·v_T = 0. The DM-side velocity of WP0-v2 (2.1) is v_χ = v − q/2m_χ = v_∥ q̂ + v_T with
**v_∥ = (ω + Δ_χ)/q fixed by kinematics**. The halo enters only through the transverse velocity v_T.

**(1.2) Velocity polynomial [D].** Every Fitzpatrick 𝒪_i is at most linear in v^⊥ (WP0-v2 (2.2)), so 𝒱_a is affine in v_χ and 𝔇_ab
(WP0-v2 (2.3)) is a polynomial of degree ≤ 2 in v_T: 𝔇 = 𝔇^{(0)} + 𝔇^{(1)}·v_T + v_T·𝔇^{(2)}·v_T, with v_∥ absorbed into the coefficients.
In WP0-v2 (3.4):

  dℛ/dω = (ρ_χ/m_χρ_T) ∫d³q/(2π)³ q^{-1} Σ_{n=0}^{2} tr[𝔇^{(n)}(q,ω) S(q,ω)] · f̂^{(n)}(q̂, v_min),
  f̂^{(n)}(q̂,u) ≡ ∫d³v f_χ(v) v_T^{⊗n} δ(q̂·v − u).                                                                                (1.2)

f̂^{(0)} is the Radon transform of f_χ (hep-ph/0209110 [ABS]); 𝒢(q,ω) = f̂^{(0)}(q̂,v_min)/q (CONVENTIONS §8). (1.2) is the most general halo
object for any operator class, any anisotropic target and inelastic DM. **Strict halo independence means bounding f̂^{(0)}, f̂^{(1)}, f̂^{(2)},
not η.** On shell, for local H and elastic DM, only P_Tv_χ and j_T, J_T survive (WP0-v2 (2.2); WP1 [E4]), consistent with (1.2).

**(1.3) Isotropic reduction [D].** Hypothesis (I): the S entering (1.2) is angle-averaged (S → S̄(|q|,ω)), or the target is isotropic
(not isotropic f_χ; WP0-v2 (9.1)). After the DM-spin trace, tr[𝔇^{(1)}·v_T S̄] is a rotation scalar linear in v_T built from q̂ alone, hence
∝ q̂·v_T = 0 (a pseudoscalar would need a third vector): the n = 1 term drops (its azimuthal mean vanishes, WP6v2-C10c). The q̂-averages are
⟨δ(q̂·v − u)⟩_q̂ = Θ(v − u)/2v (WP6v2-C10a) and ⟨|v_T|²δ(q̂·v − u)⟩_q̂ = (v² − u²)Θ(v − u)/2v (C10b). The rate needs only

  η(u) = ∫d³v f_χ Θ(v − u)/v,   ξ(u) = ∫d³v f_χ (v² − u²)Θ(v − u)/v,   **dξ/du = −2u η(u), ξ(v_max) = 0 ⇒ ξ(u) = 2∫_u^∞ u′η(u′)du′**   (1.3)

(WP6v2-C12: Leibniz rule for any radial density; the boundary term vanishes because the integrand of ξ is zero at v = u).
**Under (I) velocity-dependent operators add no halo freedom: ξ is a functional of η.** The rate is

  dℛ/dω = (ρ_χ/(4π²m_χρ_T)) ∫q dq [A^{(0)}(q,ω) η(v_min) + A^{(2)}(q,ω) ξ(v_min)],
  A^{(0)} = Σ_ab 𝔇^{(0)}_ab S̄_ab,   A^{(2)} = ½ Σ_ab tr_T[𝔇^{(2)}_ab] S̄_ab,   tr_T X ≡ (δ_cd − q̂_cq̂_d)X_cd.                          (1.4)

Under (I), 𝔇^{(2)}_cd = d₂δ_cd + d₂′q̂_cq̂_d (+ an antisymmetric part that v_Tv_T annihilates), ⟨v_T^cv_T^d⟩_az = ½|v_T|²(δ − q̂q̂), so
v_T·𝔇^{(2)}·v_T → d₂|v_T|² and A^{(2)} = d₂-contraction (WP6v2-C10c). Check: for n_e alone A^{(0)} = |Ṽ|²S̄ = πσ̄_eF_DM²S̄/μ_χe², and (1.4)
is exactly WP0-v2 (9.2), ρ_χσ̄_e/(4πm_χρ_Tμ_χe²)∫q dq F_DM²ηS̄, with 𝒢 = η/(2q) (CONVENTIONS §13 item 1). The lab-frame SHM is anisotropic;
(I) on S is what is used (WP6-W5, applied in WP0-v2 (9.1)).

**(1.5) Anisotropic targets [D].** With time reversal or inversion S(q) = S(−q) (WP0-v2 (4.3)), so the direction dependence of S expands in
even-ℓ harmonics invariant under the point group. For O_h (Si, Ge) and for T_d + TR (GaAs: the even-ℓ counts of T_d equal those of O_h,
and TR removes the ℓ = 3 invariant xyz), the invariants are ℓ = 0, 4, 6, 8, 10 and two at ℓ = 12: 7 coefficients up to ℓ = 12, none at ℓ = 2
(WP6v2-C11, character formula). Then (1.2) = Σ_ℓ ∫ S_ℓ(q,ω) f̂^{(0)}_ℓ(v_min). **For cubic targets that are P- or T-symmetric, the first
correction to the η-only rate is ℓ = 4.** **Targets breaking both P and T** have S(q) ≠ S(−q), S(q) − S(−q) = 2q·𝐛_NR(ω) + O(q³), and a rate
odd in the DM-wind direction (WP0-v2 (4.3); WP4-D6; L19; WP4-revision flag): there the anisotropic reduction **must keep all odd-ℓ
invariant harmonics** (leading ℓ = 1, then ℓ = 3, … as allowed by the magnetic point group), and the "ℓ = 4 first" statement does not apply. Consistent with WP1 (no ℓ = 2 in cubic crystals) and WP2 (the incoherent multiphonon S of cubic crystals is exactly isotropic).

**(1.6) Conventions dictionary [D]** (WP6v2-C1–C3). With S̄ the angle-averaged S_ee of WP0-v2 (3.1), spin included (CONVENTIONS §6):

  |f_crys(q,ω)|² = Ω q³ S̄_ee(q,ω)/(4παm_e²)                           [1509.01598 Eqs. (21), (64) normalisation]
                 = Ω q⁵ L̄(q,ω)/(8π²α²m_e²)   (T = 0, ELF form WP0-v2 (5.4)/(9.3); unscreened: L → ε₂)   [= 2101.08275 Eq. (16)]
  |f_res(q,ω)|²  = (8αm_e²ω/q³)|f_crys|² = 2ΩωS̄_ee/π                     [2311.04957 Eq. (4)]                                     (1.6)

1509.01598 Eq. (17) is per target (×N_cell); 2311.04957 Eq. (3) is **per unit cell** (C3a; WP6-D1); WP0-v2 (3.4)/(9.2) is per unit target
mass. Library tables carry ΩS̄ (per cell, eV⁻¹), so all three follow by fixed factors (CONVENTIONS §8).

**(1.7) Measured observable [D given WP0-v2 (7.1), (7.3)].** With P(i|Λ) ≡ Σ_{N_eh} P_det(i|N_eh)P_casc(N_eh|Λ) and 𝔈_i = exposure × efficiency,

  μ_i = 𝔈_i (ρ_χ/m_χρ_T) ∫d³v f_χ ∫dω ∫d³q/(2π)³ Σ_Λ tr[𝔇(q,v)S(q,ω;Λ)] P(i|Λ) δ(ω − ω_q).                                       (1.7)

The trace and the q integral sit inside the Λ sum (WP0-v2 (7.3); v1's form with a single-operator ratio P(N_eh|ω) integrated q out before
seeding, WP5-1, WP5-2). **μ_i is linear in S, hence linear in η (or in the f̂^{(n)}).** The halo-independent and nuisance machinery rests on this.

---
## 2. L24 derived: SHM rate with η(v_min), and halo-independent bounds

**(2.1) Source formulas [FT]** (quoted in source notation; source E_e ≡ ω, g_χ ≡ f_χ, K ≡ N_esc, n_e ≡ N_eh^{step}, ε ≡ ε_eh).
- *1509.01598 Eq. (17):* "dR_crystal/d ln E_e = (ρ_χ/m_χ) N_cell σ̄_e α (m_e²/μ_χe²) ∫ d ln q (E_e/q) η(v_min(q,E_e)) F_DM(q)² |f_crystal(q,E_e)|²",
  with Eq. (15) η(v_min) = ∫d³v g_χ(v)Θ(v − v_min)/v and Eq. (16) v_min = E_e/q + q/2m_χ. SHM: Eq. (65) g_χ ∝ e^{−|v+v_E|²/v₀²}Θ(v_esc − |v+v_E|),
  K from Eq. (66), closed forms η₁, η₂ in Eq. (68). Values there: v₀ = 230, v_esc = 600, v_E = 240 km/s, ρ_χ = 0.4 GeV/cm³.
- *2311.04957 Eqs. (9)–(11), (13), (19)–(20):* "dR/d ln E_e = (8μ²_χe)^{-1}∫dq q |F_DM|²|f_res|² η̃(v_min)", η̃ = (ρ_χσ̄_e/m_χ)η; step ansatz
  η̃ = Σ_i η̃_iΘ(v_i − v_min); binned rate (13) with n_e = 1 + ⌊(E_e − E_gap)/ε⌋ (12); linear map R_i = Σ_j 𝒜_ijη̃_j (19), 𝒜_ij in (20).
  Values there: v₀ = 220, v_esc = 544, v_E = 232 km/s, ρ_χ = 0.4.

**(2.2) Truncation chain from WP0-v2 [D].**
1. WP0-v2 (3.4).
2. Single operator n_e (L0 chain, WP0-v2 (9.1)); Δ_χ = 0.
3. Hypothesis (I): S → S̄, giving 𝒢 = η(v_min)/2q (C10a; WP0-v2 (9.2)).
4. f_χ = SHM (1509.01598 Eq. (65)) → η₁, η₂ of Eq. (68), proved exactly (dη/du = −g(u) on both branches, continuity, η(v_max) = 0; WP6v2-C4a).
5. Dictionary (1.6) → 1509.01598 Eq. (17) exactly (C1).
6. Optionally P_casc(N_eh|Λ) → step model N_eh^{step}; this is the Λ-marginal only for a photon-type seed (WP5-4; nuisance θ_seed, §5.2)
   → 2311.04957 Eq. (13).
7. Step basis for η̃ → Eqs. (19)–(20).
As a τ point (WP0-v2 §6.1): `nB=0|ng=0|nA=0|X=IP|nT=0|K=-|Mg=-|nD=-` + `T=0K;ref=normal;scr=-;conv=window` (L1 composed with the halo
choice; "-" = unused slot or empty set, as in CONVENTIONS §11). Every WP1–WP3 upgrade of S enters only through S̄ in step 3.

**(2.3) Validity conditions, with numbers [D/E].**
- (V1) *Born:* |Ṽ|μ_χe q/4π ≪ 1; holds by many orders for σ̄_e ≲ 10⁻³⁰ cm² [E].
- (V2) *Only 𝒪₁:* other 𝔇_ab are suppressed by v² ~ 10⁻⁶ or (q/m_e)² ~ 10⁻⁴–10⁻³ at q ~ 1–4 αm_e [E]; longitudinal velocity operators reduce
  to n exactly and only P_Tv_χ, j_T survive on shell (WP0-v2 (9.1)(α); WP1 [E4]). Under (I) they enter only through ξ, fixed by η (1.3).
- (V3) *Angle average:* for cubic targets the first neglected term is ℓ = 4 (1.5); its size on the day-averaged rate is a few % in the bulk
  and larger near the edge [E] (2607.06005 [FT via WP1]; 2411.03433 [ABS]).
- (V4) *Halo time dependence:* integrals use v_E(t) = v_⊙ + v_⊕(t) of 2105.00599 Eq. (11), averaged over the exposure (CONVENTIONS §8);
  reference scalars use v_E^ref = |v_⊙| = 250.5 km/s. |v_E(t)| spans 237.4–266.4 km/s, annual mean 252.1 (WP6v2-C6). At v_E^ref,
  ∂ln η/∂v_E = 0.0125 per km/s at v_min = 600 and 0.060 at v_min = 760 (C4c), so the annual ±15 km/s is ±19% at 600 and a factor ≈ 2.5 at
  760 km/s [D for the SHM]. The 252.1 mean and the annual range enter only the halo band (§6.3).
- (V5) *SHM shape with a hard cutoff:* sets the edge exponent (§3).
- (V6) *T > 0 branch:* the ω < 0 weight is ∝ e^{−E_g/T}, negligible (WP0-v2 (9.1)(γ)).
- (V7) *No Earth stopping:* fails at the large-σ̄_e ceiling; not quantified here.
- (V8) *S_ee clamped-lattice IP* (L1). The ELF form needs WP0-v2 (5.5)(i) or (ii).

**(2.4) Leading corrections the URF predicts [D].**
- (a) Anisotropy: η/2q → f̂^{(0)}(q̂,v_min)/q in (1.2); first term ℓ = 4 with coefficient S_4(q,ω) × the ℓ = 4 moment of the lab-frame Radon
  transform (links L24 to L19); for targets breaking both P and T, odd-ℓ terms from ℓ = 1 (1.5).
- (b) Velocity-dependent operators: the A^{(2)}ξ term of (1.4), ξ = 2∫u′η du′; no new halo input.
- (c) Halo tails beyond the SHM change the edge exponent (3.4).
- (d) Annual modulation (V4).
- (e) Yield: P(i|Λ) with the operator-resolved seeding (1.7) replaces P(N_eh|ω) (G1 hand-off to WP5).
- (f) Theory nuisances θ enter 𝒜_ij linearly or log-linearly (§5).

**(2.5) Discrepancies in the sources [D]** (labels WP6-D1…D6).
- **WP6-D1** 2311.04957 Eq. (3) equals 1509.01598 Eq. (17) *without* N_cell (C3a): a rate per unit cell, not stated in the text. The step heights
  η̃_i (Eq. (17)) are in yr⁻¹, which absorbs the target size. Recasts must restore N_cell.
- **WP6-D2** 2311.04957 Eq. (13) integrates q over [q₋, q₊] *and* multiplies by Θ(v_i − v_min); q± (Eq. (7)) depend on an unspecified speed
  and the Θ already enforces kinematics. Consistent form: ∫₀^∞dq … Θ(v_i − v_min(q,E_e)), or q ∈ [q₋(v_i), q₊(v_i)] per step.
- **WP6-D3** Halo conventions are mixed: 1509.01598 230/600/240, ρ_χ = 0.4; 2311.04957 220/544/232, ρ_χ = 0.4; 2105.00599 v₀ = 238,
  v_esc = 544, v_⊙ = (0, 238, 0) + (11.1, 12.2, 7.3), |v_⊕| = 29.8, ρ_χ = 0.3. **Resolved for the campaign** (CONVENTIONS §8, §13 items 2–3):
  2105.00599 values, ρ_χ = 0.3, v_E(t) in integrals, v_E^ref = |v_⊙| = 250.5 km/s (the old NOTATION "v_E = 250" was this Sun speed),
  v_max = 794.5 km/s; the annual mean 252.1 belongs to the halo band.
- **WP6-D4** 1509.01598 Eq. (67) writes −2vv_Ec_θ where Eq. (65) implies +2vv_Ec_θ; harmless (full c_θ range).
- **WP6-D5** Step-model gap: 2311.04957 uses E_gap = 1.2 eV, scissor-corrected codes ≈ 1.11–1.12 eV, measured E_g(0) = 1.170 eV (campaign
  default); m_min = 0.358 (2311.04957: 1.2 eV, 776 km/s) vs 0.319 (1.12 eV) vs 0.333 MeV (1.170 eV) (C7), before any halo difference.
- **WP6-D6** 2105.00599 §3.1: SHM parameters to be **fixed, not profiled** ("quoted uncertainties … [do not] represent likelihood
  distributions that can be meaningfully profiled over" [FT]); 2011.12896 shows bands from v_esc = 528⁺²⁴₋₂₅, v₀ = 233 ± 6 [FT]. §6.3 reports
  separate objects.

**Status L24: DERIVED** (chain, conditions, corrections). Prefactor = 1509.01598 Eq. (17) (C1) = 2101.08275 Eq. (16) (C2) = WP0-v2 (9.2).

---
## 3. The kinematic edge: what the "exponential sensitivity" is

**(3.1) Edge mass [D].** min_q v_min(q,ω) = v_* = √(2ω/m_χ) at q_* = m_χv_* (2311.04957 Eq. (8)). For a hard cutoff |v| ≤ v_max, scattering
at threshold E_th requires

  m_χ ≥ m_min = 2E_th/v_max²,   δ ln m_min = δ ln E_th − 2 δ ln v_max.                                                             (3.1)

**Campaign default E_th = measured E_g(T_op)** (AUDIT A9; §5.2 gap row); every threshold mass below names its E_th. With the reference
v_max = v_esc + v_E^ref = 794.5 km/s (CONVENTIONS §8; quoted 794):
- Si at mK, E_th = E_g(0) = 1.170 eV: **m_min = 0.333 MeV**. Annual range v_max ∈ [781, 810] km/s: m_min ∈ [0.320, 0.344] MeV, a
  halo-band entry (C6, C7).
- PAER window lower edge, E_th = E_g(0) + ω_TA = 1.188 eV: **0.338 MeV** (the 0.34 MeV of SOTA/L1).
- Ge at mK, E_th = E_g(0) = 0.744 eV: 0.212 MeV.
- Labelled comparisons only (not campaign values): scissor-code gap 1.12 eV gives 0.319 MeV; with 1.11 eV at v_max = 840 km/s it gives
  0.283 MeV (EXCEED-DM's 0.28 MeV); Ge at room temperature, 0.67 eV, gives 0.191 MeV; 2311.04957 conventions (1.2 eV, 776 km/s) give 0.358 MeV. **Halo (v_max) and theory (E_th) enter only
through E_th/v_max², so they are exactly degenerate at the edge: profile or vary them jointly, never quote them separately.**

**(3.2) Two regimes of η [D]** (SHM, 2105.00599 values at v_E^ref; C4b–d). For these parameters every v_min > v_esc − v_E^ref = 293.5 km/s lies
on the second branch η₂ of 1509.01598 Eq. (68); v1's regime-A interval "v_E + v₀ ≲ v_min < v_esc − v_E" is empty (488.5 > 293.5; C4c).
With δ_v ≡ v_max − v_min, the exact expansion is

  η = π v_esc e^{−v_esc²/v₀²} δ_v² [1 + δ_v/δ_v,× + O(δ_v²)]/(v_E N_esc),   δ_v,× = 3v_escv₀²/(2v_esc² − v₀²) = 173 km/s.            (3.2)

- *Regime A (Gaussian tail), δ_v ≳ δ_v,× (v_min ≲ 620 km/s):* the erf((v_min − v_E)/v₀) term dominates, η ∝ e^{−(v_min − v_E)²/v₀²} roughly.
  Log-sensitivities per km/s at v_min = 600: 0.018 (v₀), 0.0027 (v_esc), 0.0125 (v_E). With v₀ = 233 ± 6 (2011.12896): ±11%.
- *Regime B (edge), δ_v ≪ δ_v,×:* a **power law in δ_v** times a fixed exponential; ∂ln η/∂v_esc ≈ 2/δ_v diverges at the edge (0.047 per km/s at
  v_min = 760, δ_v = 34.5, the O(δ_v/δ_v,×) term included), so v_esc ± 25 km/s gives e^{±1.17} ≈ ×3.2.

**(3.3) Near-threshold rate [D].** Hypotheses: regime B; S̄(q,ω) ∝ (ω − E_th)^{p_on}, smooth in q near q_*. Then
v_min ≈ v_* + (ω/q_*³)(q − q_*)², and ∫dq (v_max − v_* − (ω/q_*³)(q − q_*)²)² = (16/15)(v_max − v_*)^{5/2}(q_*³/ω)^{1/2} (C5a). Near E_th,
v_max − v_*(ω) is linear in ω − E_th, and the ω integral is a Beta function that adds p_on + 1 (C5b, exact):

  ℛ(m_χ) ∝ δ_v,0^{7/2+p_on},   δ_v,0 ≡ v_max − √(2E_th/m_χ),   ∂ln ℛ/∂ln v_max = (7/2 + p_on)v_max/δ_v,0.                          (3.3)

The lowest-mass part of every ER curve is controlled by: the edge position m_min (3.1); the halo exponent (2 for a hard cutoff); and **the
response onset exponent p_on**, a property of S near threshold (ZPL onset, PAER sideband, excitons; WP1/WP3). Uncomputed excitonic
effects change p_on (Sommerfeld factor near E_min) and add sub-threshold lines: §5.2 ladder row (interim M + A).
**PAER channel (WP3-v2 §M3, §7, recomputed for the angle-averaged S̄^{X+}; AUDIT A1).** The edge exponent of (3.3) is
7/2 + k_tail + p_on:
- **generic vertex: p_on = 3**, so ℛ ∝ δ_v,0^{13/2+k_tail}; if M̃ vanishes on the minimising direction, p_on = 4 and δ_v,0^{15/2+k_tail};
- **Si TA edge: p_on = 4** (δ_v,0^{15/2+k_tail}). It sits at E_g^{ren} + c_TA·d with d = min_K ||q| − |K||, K over the connecting phonon
  wavevectors. The LA edge is a kink with exponent 3; TO/LO edges are kinks with exponent 3, or 4 on a vertex zero;
- **symmetry-forbidden pockets: p_on = 4–5** (δ_v,0^{15/2…17/2+k_tail});
- **exciton replicas: p_on = 3/2–5/2** (δ_v,0^{5…6+k_tail}), with onset lowered by E_x^b (≈ 14.7 meV in Si);
- **edge shell:** shells with d < Q_w ≈ 0.2 Å⁻¹ (Si) are treated in the Dyson convention (O4 d11): only the total X0 + X+ has an onset
  exponent there, and no PAER-only exponent is quoted.
At T > 0 an absorption branch opens ω_{Qν} lower, weighted by n_{Qν}. The case that applies is part of the τ* metadata; the choice between
cases is a type-Δ nuisance (§5.2).

**(3.4) Smooth truncations [D].** Hypothesis: near the escape boundary f_χ ∝ (v_esc − |v + v_E|)^{k_tail} (as for King/Lisanti-type forms
(e^{−v²/v₀²} − e^{−v_esc²/v₀²})^{k_tail}, 1010.4300 [ABS]; the attribution of the form is [E], from memory). The region |v| ≥ v_min inside the
escape sphere is a lens of depth δ_v around the far point; with ϱ the distance from the axis and a_lens ≡ 1/(2v_esc) − 1/(2v_max),

  η ∝ ∫2πϱ dϱ (δ_v − a_lensϱ²)^{k_tail+1}/(k_tail + 1) = π δ_v^{k_tail+2}/(a_lens(k_tail + 1)(k_tail + 2)),                         (3.4)

which reproduces (3.2) at k_tail = 0 (C5c); the q and ω integrals then give ℛ ∝ δ_v,0^{7/2+k_tail+p_on} (C5b). **The halo-tail exponent k_tail and
the response-onset exponent p_on are degenerate at the edge:** a null result there constrains only k_tail + p_on. This is the precise
content of G8's "50%–×10" claim.

**(3.5) Size of the edge nuisances for Si [E].**
- v_esc: 544 vs 528 ± 25 (2011.12896) vs 600 (QROCODILE/QEdark): δ ln v_max ≈ 3–6%, so 6–12% in m_min.
- Annual v_E(t): v_max ±1.8%, m_min ±3.6% (0.320–0.344 MeV at E_th = 1.170 eV; C6–C7), halo band.
- E_th from the step-model convention (WP6-D5): 7%.
- Clamped versus ZPR-renormalised gap: Si ZPR ≈ −60 meV, about 5%, if the code is not scissored to the measured E_g(T).
- Operating temperature: Varshni E_g(130 K) − E_g(0) ≈ −10 meV, about 1%.
- The PAER window (m_χ ≈ 0.338–0.47 MeV; lower edge at E_th = 1.188 eV, SOTA/L1) lies in regime B, so its rate carries the (3.3) sensitivity with p_on from S^{X+}.

---
## 4. G8 closed: halo-independent ER analysis in the URF

**(4.1) Formula [D].** Hypothesis (I) and (1.7). With η̃ ≡ (ρ_χσ̄_e/m_χ)η = Σ_j η̃_jΘ(v_j − u), (1.3) gives
ξ̃ = Σ_j η̃_j(v_j² − u²)Θ(v_j − u) (WP6v2-C14), and

  μ_i(m_χ, η̃, θ) = Σ_j 𝒜_ij(m_χ; θ) η̃_j,
  𝒜_ij = 𝔈_i (4π²ρ_T)^{-1} ∫dω ∫q dq Σ_Λ [A^{(0)}(q,ω;Λ,θ) + A^{(2)}(q,ω;Λ,θ)(v_j² − v_min²)] P(i|Λ;θ) Θ(v_j − v_min(q,ω)),          (4.1)

where A^{(n)}(q,ω;Λ) are (1.4) with S̄_ab → S̄_ab(q,ω;Λ), per unit σ̄_e. It generalises 2311.04957 Eqs. (19)–(20) to all operator classes
(A^{(2)}), to any library response (WP1–WP3), to the operator-resolved seeding of WP0-v2 (7.3), and to the theory nuisances θ (§5).

**(4.2) Positivity [D].** A single step at v_j is the rate of a physical isotropic shell |v| = v_j; by WP0-v2 (4.4) tr(𝔇S) ≥ 0 for every v.
**Hypothesis (P):** each Σ_Λ S(q,ω;Λ)P(i|Λ) is PSD. It holds for the total S (P(i|Λ) independent of Λ), and with Λ-resolved seeding inside
the window or for detector bins coarser than δ: outside the window the X0/X+ split under DC is not separately PSD (WP0-v2 §6.2(i), O4),
but where per-sector positivity fails P(i|Λ) is constant over the split, so the sum is P(i|·)Σ_ΛS(Λ) ≥ 0. In the O4 d11 edge shell only
totals are used. Then 𝒜_ij ≥ 0. Consequences:
- *(a) Convexity.* −ln ℒ is convex in η̃ at fixed (m_χ, θ) (μ linear, Poisson log-likelihood concave); the η̃ profile is unique (as 2311.04957
  states), here with θ included.
- *(b) Conservative halo-independent bound.* η̃ is non-increasing and ≥ 0, so η̃(u₀) = h implies η̃(u) ≥ h for u ≤ u₀; the smallest rate
  compatible with h is h·𝒜_i(u₀), with 𝒜_i(u₀) ≡ 𝒜_ij at v_j = u₀ (a single step). Hence

  η̃(u₀) ≤ min_i N_i^up(θ)/𝒜_i(u₀; m_χ, θ)   for every u₀,                                                                         (4.2)

  N_i^up the per-bin upper limit on counts. This is the ER/URF form of the NR construction of 1111.0292 [ABS], integrated over q. The
  minimum is reached by a single step **because 𝒜 ≥ 0**; without positivity (a truncated S with negative pieces, WP6-W2, or a Λ split
  violating (P)) the bound is invalid.

**(4.3) Mass degeneracy [D].** rank 𝒜 ≤ number of populated bins. With 1–2 populated bins (light mediator) the kernel of 𝒜 is
(N_v − 2)-dimensional, and the edge degeneracy (3.4) makes m_χ undeterminable halo-independently; consistent with 2311.04957 §3 [FT] and
explained by (3.3)–(3.4).

**(4.4) Computation specification.**
- *Inputs:* library S̄ and Λ-resolved A^{(0)}, A^{(2)} tables per operator class (§7.1); P_casc(N_eh|Λ) per cascade model (WP5); P_det(i|N_eh)
  and 𝔈_i per experiment; nuisance templates Δ^τ_k (§5).
- *Grid:* v_j at 10 km/s over 0–1000 km/s (N_v = 100, as 2311.04957); q and ω on the library grid (§7.2).
- *Cost:* 𝒜 is N_bins × N_v × N_q × N_ω × N_Λ-marginal ≈ 10 × 100 × 300 × 2500 × O(10) ≈ 10¹⁰ operations per (m_χ, θ): seconds to a minute.
  ∂𝒜/∂θ_k from the same contraction with Δ^τ_k.
- *Outputs:* the bound (4.2) as a curve η̃_max(u₀; m_χ) with theory band; the η̃ profile and 1σ/2σ regions (SVD flat directions, 2311.04957
  Eqs. (21)–(24)); compatibility p-values for experiment pairs with shared θ.

**(4.5) Exact remaining gap (G8′).** For anisotropic targets beyond (I) (daily modulation, non-cubic or thin-film targets, P,T-broken
targets), the halo object is f̂^{(0)}(q̂,u,t) on the sphere, in the lab frame, in time. It obeys no scalar monotonicity, so (4.2) does not
apply; only its A1g (ℓ = 0) projection reduces to η. A conservative bound needs a convex characterisation of the Radon transforms of
non-negative f_χ with |v| ≤ v_max: a moment problem, not derived here [OPEN].

---
## 5. Nuisance structure for every approximation level (G4, part 1)

**(5.1) Parametrisation [D]** (adopted as WP0-v2 (8.1)). For each active truncation k of τ, Δ^τ_k = S^{τ+e_k} − S^τ, r^M_k = Δ^τ_k/S^τ:
- *(M) multiplicative, log-normal:* S(θ) = S^τ Π_k(1 + r^M_k)^{θ_k}, θ_k ~ 𝒩(0,1). PSD for all θ; equal to the additive form at first order.
- *(A) additive, support-opening* (S^τ = 0 on part of (q,ω), e.g. the PAER window): S = S^τ + a^A_kΔ^τ_k, a^A_k > 0 log-normal; the central value
  includes Δ^τ_k once computed (a^A_k = 1); the prior width is the stated residual uncertainty.
- *(E) energy shift:* S(q, ω − θ_Eσ_E): the edge nuisance of (3.1); it shifts 𝓜¹ by θ_Eσ_E∫S, inside the truncation error.
- *(Δ) discrete* model choices: discrete profiling (1408.6865 [ABS]) or envelope (§6).
The v1-WP0 additive Gaussian S^τ + Σθ_kΔ_k violates WP0-v2 (4.4) wherever |Δ_k| ≳ S^τ (WP6-W2) and is withdrawn (WP0-v2 (8.1)). One θ_k
per truncation, applied coherently across (q,ω), bins, targets and experiments sharing the physics (WP0-v2 (8.1)).

**(5.1′) Constrained truncations: the anharmonic order [D]** (WP2-v2 (6.1), (6.1′), IF-4). At fixed q, with E_R = q²/2M_κ and
y_R ≡ ω − E_R, the anharmonic increment of the self part obeys three linear constraints: ∫Δ^τ_A = 0, ∫y_RΔ^τ_A = 0 (the first moment),
∫y_R²Δ^τ_A = 2q²δE^kin_q̂/M_κ. The M type S^τ(1 + r^M_A)^{θ_A} satisfies them only at θ_A ∈ {0, 1}; the violation is O(θ_A(1 − θ_A)(r^M_A)²)
(WP6v2-C15b). The parametrisation used instead holds them for every θ:

  S(θ_A, θ_δ) = S^τ + Δ^τ_A + θ_A Π_mom[Δ′_A] + θ_δ S^τ P_δ(y_R),   Π_mom[X] ≡ X − S^τ Σ_{b=0}^{2} c_b(X) y_R^b,   Σ_b 𝔪_{a+b} c_b = ∫y_R^a X  (a = 0, 1, 2),   (5.1′)

with 𝔪_n ≡ ∫y_R^n S^τ dω (the 3×3 moment matrix of S^τ, invertible whenever S^τ has at least three support points).
- The central value includes the computed Δ^τ_A at amplitude 1, as required by the third constraint when δE^kin_q̂ comes from PIMD.
- Δ′_A is the shape template: the n_A = 2 increment, or the spread between anharmonic methods (MLIP vs DFT PIMD). Π_mom removes its
  moments 0, 1, 2, so ∫y_R^aΠ_mom[Δ′_A] = 0 for a = 0, 1, 2 and every θ_A (WP6v2-C15a). θ_A ~ 𝒩(0,1) is type A on a constraint-preserving
  basis function.
- θ_δ carries only the uncertainty of δE^kin_q̂ when it is not from PIMD. P_δ is the quadratic with ∫y_R^aS^τP_δ = (0, 0, 2q²σ_δE/M_κ),
  so the third moment moves by exactly θ_δ·2q²σ_δE/M_κ and the first two stay at zero.
- Positivity: S ≥ 0 restricts (θ_A, θ_δ) to a convex support (like L17, §5.3), not to the prior. Π_mom[X] ∝ S^τ × quadratic, so the
  projection opens no new support.
- The M type stays allowed only with this restriction stated, its O(θ(1 − θ)(r^M)²) moment violation recorded as a sub-percent
  systematic (η_anh ≤ 0.03).
- Any other truncation with exact linear moment constraints (e.g. n_ph truncations against WP2 (3.4)) uses the same projection.

**(5.2) Table.** Sizes [E] unless a source is given. "Central" is the library's τ*. Cross-material correlation r_mat = 0 by default (1 as a variant).

| Level (τ slot) | Template Δ^τ_k | Type | Prior | Correlation | Source of Δ^τ_k |
|---|---|---|---|---|---|
| XC functional (ground state) | spread over {PBE+scissor, SCAN, HSE, G₀W₀ bands}: principal components of the covariance of ln S | M (per PC) + E (gap) | 𝒩(0,1) per PC; σ_E = 0 if scissored to measured E_g(T_op), else \|E_g^DFT − E_g^exp\| | material-wide; r_mat across materials | ≥ 3 functional runs; Ge 3d misplaced by ≈ 4.5 eV (2306.14944) gets its own E-type nuisance on core weight |
| Kernel ladder 𝒳 | S^{𝒳+1} − S^𝒳, **computed** (η_xc is not small; WP0-v2 Table 6.1, (8.1)): central RPA+LFE, Δ = (BSE or TDDFT kernel) − (RPA+LFE). **Interim, while the finite-q BSE is uncomputed** (WP1-v2 [E8], §1.5): (i) Sommerfeld continuum, r^M_𝒳 ∈ [+0.3, +1.0] for E_min(q) ≤ ω ≲ E_min(q) + 1 eV, r^M_𝒳 = 0 above; (ii) bound-exciton lines below E_min(q) (E_min(q) − E_x^b ≲ ω < E_min(q)), new support, template from [E8] with ab initio μ_x, ε_∞, ρ_cv. v1's fallback η_xc·S ≈ 1% is withdrawn | (i) M; (ii) A | (i) log-normal with 68% range [+0.3, +1.0]; (ii) a_k log-normal [E] | material-wide | finite-q BSE (Yambo/BerkeleyGW, WP1); [E8]. ALDA few %; LFE −20…−50% (2603.12326 [ABS]) belongs in the central value |
| Screened operator rows | rows with R̃_ac ≠ 0 screened per WP0-v2 (5.3): n, j_L always; j_T via LFE (WP1-D4); spins f_xc^T-renormalised (WP1-D5) | in central value; residual M | 𝒩(0,1) | material | WP1 |
| q_max / high-q cutoff | Θ(q − q_max)S_IA(q,ω), S_IA = Σ_sh 2π𝓃_e^{(sh)}(m_e/q)J^{(sh)}(p_z) (impulse approximation; f-sum exact, C9) | added to central value; residual M on the tail | residual width E_B^{(sh)}/(q²/2m_e) per shell | material-wide | Compton profiles from all-electron atoms in the crystal (QCDark/EXCEED-DM core): **closed analytically, not a nuisance** |
| k-grid / basis / PAW | difference of successive grids or bases | M | half-normal (rate falls monotonically with k-density, 2105.05253 [ABS]) | run-specific | convergence pair |
| BO order n_B | κ_BO⁴ weight shift (WP0-v2 §6.2(iii)) | M | 2×10⁻⁵ (Si); negligible | — | analytic |
| e–ph order n_g | n_g = 0 → 2: PAER sideband S^{X+} (A in the window; onset exponent of S̄^{X+}: p_on = 3 generic (4 on a vertex zero), Si TA 4, forbidden pockets 4–5, exciton replicas 3/2–5/2, none in the edge shell d < Q_w; WP3-v2 §M3, §7; choice type Δ, (3.3)), ZPR shift (E), FC reduction e^{−2W} of the ZPL, 2W_κ = q·B_κ·q (M) | A + E + M | A: a_k log-normal, 68% range [0.5, 1.2] (X2 interim). E: σ_E = \|ZPR\| ≈ 60 meV (Si) if unrenormalised. M: η_ep | material and T | EPW/ZG (WP3; X1/X2 specification; ZG deterministic, WP3) |
| Screening channel (pair channel, external LFE in X+) | X2 classes (four, WP0-v2 (5.5)); static DFPT error O(ω_Q²/E_g²) ≈ 3×10⁻³ (X2; WP0-v2 F11), negligible | M | interim factor [0.5, 1.2] | material | X2-N1…N4 |
| Anharmonic n_A | computed Δ^τ_A at amplitude 1 (central) + Π-projected shape template Δ′_A + δE^kin term, (5.1′): WP2's three exact linear constraints hold for all θ | A (constraint-preserving) + A (θ_δ) | θ_A ~ 𝒩(0,1) scaled by η_anh = 0.01–0.03 (T = 0); θ_δ ~ 𝒩(0,1) on σ_δE (0 if PIMD) | NR only; negligible for ER | WP2 (6.1), PIMD |
| Phonon order / regime K (NR) | truncation at n_ph ≤ N loses P[Pois(2W) ≥ N] of the f-sum (WP2) | M (one-sided) | that fraction | material | WP2 recursion (all orders) |
| Thermal order n_T | S^{n_T+1} − S^{n_T}: phonon-absorption sideband ∝ n_{Qν} (TA at 130 K: n ≈ 0.25); t_g terms ∝ e^{−E_g/T} negligible | A (sideband) or M | log-normal | per T | WP3 sideband |
| Temperature T (metadata, not an order) | E_g(T) shift (Varshni ≈ −1.5×10⁻⁴ eV/K at 130 K) and ∂ln S/∂T | E + M | σ_T = sensor uncertainty (≈ 1 K) | per experiment | analytic |
| Gap convention E_g(T) | E-type | E | σ_E: 1 meV if scissored to measured E_g(T_op); 60 meV if clamped and unscissored; the WP6-D5 offset (0.08 eV) is **removed** by convention, not profiled | material-wide | measured E_g(T) |
| Yield / cascade (WP5) | {step(ε_eh), R&K, URF cascade} plus WP5 §8: θ_seed (photon vs DM seed; R&K is a photon-seed fit, WP5-4), θ_{R-k}, θ_GW (GW vs vertex ii), θ_exch (exchange), θ_PES, θ_LZ, θ_esc (WP5-v2 names) | Δ (discrete) + M | ε_eh: 𝒩(3.75, 0.05) eV (Si, 130 K) [E]; WP5 widths; WP5 (W4) ties θ_GW, θ_Rk to measured ε_eh, F_eh | material-wide | WP5 (G1); R&K's tuned A is "non-physical" (2004.10709) |
| Fano term 𝔉 (cascade first step, O4 d7) | θ_𝔉: interference correction to P_casc(N_eh\|Λ) | A on P_casc | \|ΔP\| ≤ 0.11 Γ/δ (WP5-v2); **0 for Si, Ge** (PT-symmetric) | material (GaAs) | O4 (O4.7), WP5-v2; export gated in §7.4 |
| Cascade band edge (WP5 θ_Eg) | θ_Eg: ZPR band-edge shift in the cascade (L12) | E | σ_E as the gap-convention row | material-wide, shared with the response's E-type gap nuisance (O4 d3) | WP5-v2 |
| Fano factor F_eh | width of P_casc(N_eh\|Λ) | M on the variance | F_eh = 0.119 ± 0.002 at 5.9 keV (2004.11499); near-gap prior uniform on [0.1, 0.2] [E] until L23 is computed | material-wide | WP5 L23 |
| Halo | fixed nominal (2105.00599) in headline; band from (v₀, v_esc, v_E(t)) | separate object | v_esc 528⁺²⁴₋₂₅, v₀ 233 ± 6 (2011.12896); |v_E(t)| 237.4–266.4 km/s, v_max ∈ [781, 810] (C6) | all experiments | §6.3 |

**(5.3) Sum-rule constraints [D]** (adopted as WP0-v2 (8.2)). The f-sum holds with ∫_{−∞}^{∞}dω ω S = π𝓃_eq²/m_e (densities with inversion;
ω < 0 included at T > 0; WP6-W1, WP0-v2 (4.6)), times the relativistic factor 1 − (5/3)⟨T⟩/m_e − q²/4m_e² for all-electron tables
(WP0-v2 (4.6′): −0.18% Si, −0.58% Ge). It informs only **non-conserving** truncations: q/band cutoffs (closed by S_IA), non-local
pseudopotentials (WP0-v2 (4.6), (L) violated), and a sideband without its Fan/vertex compensation (SOTA #3). Every rung of the 𝒳 ladder
with local potentials is conserving: ∫ωΔ^τ_𝒳 = 0 identically (WP6-W3). Positivity is automatic for M and A. L17 (WP0-v2 (9.6)) gives a hard
upper limit on ∫ω^n S(θ), used as a support restriction on θ, not a prior.

---
## 6. Statistical treatment and combination (G4, part 2)

**(6.1) Likelihood [D as a definition]** (= WP0-v2 (8.3)). Experiments ex, bins i, signal strength σ̄_e, theory θ, detector nuisances θ^det_ex:

  ℒ(σ̄_e, θ, θ^det | m_χ) = Π_ex Π_i Pois(N^obs_{ex,i} | σ̄_e s_{ex,i}(m_χ; θ, θ^det_ex) + b_{ex,i}(θ^det_ex)) · Π_k π_k(θ_k) · Π_ex π(θ^det_ex).   (6.1)

s_{ex,i} = μ_i of (1.7) per unit σ̄_e, halo fixed. Test statistic: two-sided profile-likelihood ratio with toy MC rather than asymptotics, and
a power-constrained limit at −1 standard deviation (2105.00599 §2 [FT]).

**(6.2) Profile, envelope and Bayesian treatments differ at different orders [D]** (WP6v2-C8, exact). Zero-count bin, b = 0, asymptotic
statistic −2ln ℒ = 2sμ(θ) + θ², limit at −2Δln ℒ = 2.71, one theory nuisance of fractional size δ:
- *Linear μ = 1 + θδ:* θ̂ = −sδ, σ̄_e^up(δ)/σ̄_e^up(0) = 2(1 − √(1 − 2.71δ²))/(2.71δ²) = 1 + (2.71/4)δ² + O(δ⁴); 1.28 at δ = 0.5.
- *Log-normal μ = (1 + δ)^θ (M-type):* with k_δ ≡ ln(1 + δ), θ̂k_δ = −W_Lam, W_Lam = √(1 + 2.71k_δ²) − 1 (Lambert-W solution), ratio = 2W_Lam e^{W_Lam}/(2.71k_δ²):
  1.006, 1.047, 1.112 at δ = 0.1, 0.3, 0.5.
- *Envelope* (worst case |θ| ≤ 1): 1/(1 − δ) = 1.11, 1.43, 2.0.
**Profiling a theory nuisance in a null result costs O(δ²); the envelope costs O(δ).** A Bayesian marginal with π_k = 𝒩 behaves like the profile
at small δ [E]. Theory priors are not auxiliary measurements, so this choice is a convention; it moves the published curve by up to ×1.8
(2.0/1.112) at δ = 0.5 and must be declared (WP6-W4, WP0-v2 (8.3)).

**(6.3) Recommendation: report three objects [D as a protocol]** (= WP0-v2 (8.3); CONVENTIONS §8).
- **WP6-R1** nominal limit: θ = 0, central τ*, halo fixed to 2105.00599 (v_E(t) averaged over the exposure). Comparability curve.
- **WP6-R2** theory-profiled limit: θ profiled with the §5.2 priors and M-types. Headline physics result.
- **WP6-R3** bands: the theory envelope over |θ_k| ≤ 1 (one at a time and in quadrature) around R1; a separate halo band (v₀, v_esc, the
  annual |v_E(t)| range, i.e. v_max ∈ [781, 810] km/s, and the 252.1 km/s annual-mean variant); and the halo-independent bound (4.2).
This reconciles WP6-D6: the halo is fixed in R1 and R2, varied only in R3. By (3.1), E_th and v_max are varied together in R3.

**(6.4) Combining experiments that used different codes and conventions [D].**
- *Step 1, common response.* Recompute each s_{ex,i} from the library at one τ* and one version. Code differences (SENSEI: QEdark; DAMIC-M:
  QCDark + MTF; CDEX: EXCEED-DM) become θ-values at matched τ, not "spread"; the residual after matching τ is a numerical nuisance. This
  answers SENSEI's "the code spread should not be taken as an uncertainty": decomposed by τ it is a set of correlated nuisances, plus
  WP6-D5-type convention offsets that are removed, not profiled.
- *Step 2, shared θ.* θ_k common to every experiment on the same material; across materials the r_mat option.
- *Step 3, conventions.* Rescale ρ_χ (linear) to 0.3; recompute with the fixed halo; one E_th convention (measured E_g(T_op) at each T).
- *Step 4, the likelihood product* (6.1) = 2311.04957 Eq. (15) with θ shared.
- *Recast if only limits are public [D].* For per-bin Poisson limits N_i^up the exact recast is σ̄_e^{up,lib}(m_χ) = min_i N_i^up/s_i^lib(m_χ)
  (needs N_i^up and 𝔈_i); single bin: σ̄_e^{up,C}s^C/s^lib. Optimum-interval and PLR analyses cannot be recast exactly without the binned likelihood.

**(6.5) Minimum publication standard [D: minimal sufficient set for (6.1)].** Per bin: N^obs_i, b_i with covariance, 𝔈_i; the detector matrix
P_det(i|N_eh) with its θ^det dependence; per-bin N_i^up; library version, τ* string + metadata and θ̂; the halo convention; the full
likelihood in machine-readable form (pyhf/HEPData-style JSON).

---
## 7. The shared, versioned response library (G4, part 3)

**(7.1) Content and axes [D as a specification].** One container per (material, T, τ, version), HDF5 or NetCDF4 with JSON metadata:

| Dataset | Axes (shape) | Units / normalisation | Notes |
|---|---|---|---|
| `S_iso/ee` | q (N_q), ω (N_ω) | ΩS̄_ee [eV⁻¹], spin included, T as labelled | L24/L1–L3 workhorse; → \|f_crys\|², \|f_res\|², L by (1.6) |
| `S_iso/ab` | a, b (16×16 per species, Hermitian, upper triangle), q, ω | same | WP0-v2 basis (2.2), screened per WP0-v2 (5.3); may be stored in WP1's minimal form (7 real functions per (q,ω), electrons, SOC = 0, unpolarised); A^{(0)}, A^{(2)} of (1.4) by contraction with 𝔇 |
| `S_aniso/ee` | invariant-harmonic index (7 for O_h up to ℓ = 12; C11), q, ω | coefficients of point-group-invariant harmonics | L19, daily modulation, (1.2) beyond (I); other groups by the Molien series; odd-ℓ blocks (ℓ = 1, 3, …) mandatory for targets breaking both P and T |
| `S_aniso/NN` | ℓ, m, q, ω | WP2 S_ℓm | NR anisotropy (WP2 G11) |
| `eps` | G, G′ (small), q, ω | ε_{GG′}(q,ω), ε_e; ε(q,0) | screening (WP0-v2 (5.2)–(5.5)), L17 diagnostics, channel choice |
| `S_Lambda/<class>` | Λ-marginals ((E_e, E_h) coarse grid, n_ph, ω_ph), q, ω | ΩA^{(0)}(q,ω;Λ), ΩA^{(2)}(q,ω;Λ) per 𝒪_i class, and ΩS_ee(q,ω;Λ) | WP0-v2 (7.1)–(7.3) hand-off to WP5; **no plasmon label within RPA** (WP0-v2 (7.1)); pair-resolved LFE weight = retarded (ε̃^{-1})_{G0} in WP0-v2 (3.2) order (WP0-v2 (7.2)); conv ∈ {window, DC} declared |
| `P_casc/<model>` | N_eh (≤ 20), Λ-marginal | probability | per cascade model (step, R&K, URF), with F_eh, ε_eh metadata; P(N_eh\|q,ω;𝔇) is formed at use time by WP0-v2 (7.3) |
| `Delta/<k>` | as the S it modifies | same, plus type ∈ {M, A, E, Δ}, prior, correlation group | the §5 templates, one per active truncation |
| `checks` | q | ratios | f-sum fraction (π𝓃_eq²/m_e, relativistic factor (4.6′)); min eigenvalue of S_ab (WP0-v2 (4.4)); KK residual S ↔ Im R (WP0-v2 (4.1)–(4.2)); detailed balance (WP0-v2 (4.3)); L17 saturation K_n/bound (WP0-v2 (9.6)); convergence deltas; O4 d1–d11 status |
| `derived/A` | bin set, m_χ, v_j | 𝒜_ij of (4.1) for standard binnings and steps | halo-independent analyses without rerunning |
| `derived/edge` | — | E_th(q), p_on fit, ZPR | edge parameters of (3.3) |

**(7.2) Grids [E].**
- q: 0.1–30 αm_e (0.37–112 keV), N_q ≈ 300, log-spaced below 2αm_e and linear above; covers q_* = √(2m_χE_g) down to 0.3 MeV and the
  all-electron range of 2603.12326 (25 αm_e). The tail beyond comes from S_IA (§5.2).
- ω: 0–100 eV; Δω = 10 meV within 5 eV of E_g (edge, (3.3)), 50 meV above; N_ω ≈ 2.5×10³.
- T ∈ {0, 0.05, 4, 77, 130, 300} K as needed (metadata, one container each).
- *Sizes:* S_iso/ee 300 × 2500 × 8 B ≈ 6 MB; the full 16×16 ≈ 1.5 GB per species; anisotropic ×7; each Delta set the size of its parent;
  S_Lambda ×N_Λ-marginal per class.

**(7.3) Provenance and versioning [D as a specification].**
- *Content addressing:* every dataset carries a SHA-256 of its array and a PROV-style parent list (CIF hash, pseudopotential/basis hashes,
  code name and commit, run cards, parent-table hashes).
- *Mandatory metadata:*
  - the τ string in the CONVENTIONS §11 slot order, **n_T a thermal order, never a temperature** (WP6v2-C13; WP0-v2 F9), e.g.
    `nB=0|ng=0|nA=0|X=RPA+LFE|nT=0|K=-|Mg=-|nD=-`, with metadata `T=130K;ref=normal;scr=ext,LFE;conv=window` ("X=" is the ASCII key of 𝒳);
  - the functional and scissor shift; k-grid, cutoffs, q_max, band count;
  - convention flags: q from DM to target (CONVENTIONS §3); spin included; per cell; units; CODATA set; S_ab ordering as WP0-v2 (3.1);
  - for every S_Lambda/P_casc pair, hashes proving O4 d2 (same g, gauge, ω_{Qν}), d3 (same energies), d8 (same smearing), d9 (same T);
  - the checks summary.
- *Semantic versioning:* MAJOR for any change of τ* or convention; MINOR for added tables or materials; PATCH for numerical refinement
  within tolerances. Published limits cite version + τ* + θ̂. Old versions immutable and DOI-minted.

**(7.4) Computation specification (library build).** Per material: the central run τ* and one run per active truncation τ* + e_k (about
6–9 runs; §5.2). Codes: QE/VASP + Yambo/BerkeleyGW for RPA+LFE and BSE ε_{GG′} (WP1); QCDark2/EXCEED-DM-type all-electron reconstruction
for high q and cores (G7); EPW/ZG for X+ and ZPR templates (WP3, X1/X2); WP2 recursion for NR multiphonon tables; WP5 cascade for P_casc.
*Cost:* the WP1–WP3 runs dominate; assembly, checks and derived 𝒜 take under 1 CPU-hour per material [E].
*Validation gates* before release (all in `checks`): f-sum within 2% below the band cutoff; min eigenvalue ≥ −10⁻⁶ of the trace; KK residual
< 1%; agreement with NIXS/EELS where data exist (2603.12326 compares at q < 3αm_e); O4 d1–d11 satisfied for each response/cascade pair,
d7 (𝔉 export) mandatory for non-PT targets (GaAs) — its size is open (WP0-v2 F8).

**(7.5) G4 status.** The fix is (5.1)–(5.3), (6.1)–(6.5) and the library (7.1)–(7.4). Exact remaining gaps: (i) prior widths of *estimated*
(uncomputed) truncations are conventions, not derivable; (ii) cross-material correlations (r_mat) are not derivable, so a declared option;
(iii) discrete yield models need discrete profiling until WP5 supplies a continuous cascade with errors; (iv) the combination needs
experiments to publish (6.5), outside theory.

---
## 8. Summary of new content
- (1.2) The general halo functional for all operators and anisotropic targets; (1.3) **ξ = 2∫u′η du′: velocity-dependent operators need no
  halo input beyond η** under (I), proved for any f_χ.
- (1.5) Invariant-harmonic compression: first anisotropic correction ℓ = 4 (cubic, P- or T-symmetric); with P and T both broken, odd ℓ (from ℓ = 1) must be kept.
- (3.1)–(3.4) **The edge is a power law δ_v,0^{7/2+k_tail+p_on}, not an exponential**, proved for any tail vanishing as a power;
  k_tail and p_on are degenerate and E_th/v_max² is the only edge variable, so halo and gap nuisances must be varied jointly.
- (4.1)–(4.2) The URF halo-independent bound with operator-resolved seeding; validity rests on WP0-v2 positivity and hypothesis (P).
- (5.1) A positivity-preserving nuisance algebra (M/A/E/Δ), adopted as WP0-v2 (8.1); q_max closed by the impulse tail.
- (6.2) Profile vs envelope: O(δ²) vs O(δ), closed forms; a declared convention moving curves by up to ×1.8.
- (7) The library schema with sum-rule and O4 code-pair validation gates.

---
## 9. WP0 defects reported in v1 (record; all now applied)
- **WP6-W1 (normalisation).** v1-WP0 (8.2) wrote 2π𝓃_eq²/m_e; WP0 (4.5) with S[O†] = S[O] gives ∫_ℝωS = π𝓃_eq²/m_e, consistent with ∫₀^∞ωL =
  (π/2)ω_p² and S = 2q²L/e² at T = 0; integral over ω < 0 at T > 0. → WP0-v2 (4.6), (8.2); CONVENTIONS §13 item 12.
- **WP6-W2 (positivity).** The additive Gaussian violates WP0 (4.4) where |Δ_k| ≳ S^τ (LFE changes Si's DSF by up to ≈ 6× at low ω, 2603.12326;
  S^τ = 0 in the PAER window). → WP0-v2 (8.1).
- **WP6-W3 (over-claim).** The f-sum constraint is vacuous for conserving truncations. → WP0-v2 (8.2).
- **WP6-W4 (inconsistency).** Envelope band next to a profile exclusion: O(δ) vs O(δ²). → WP0-v2 (8.3); CONVENTIONS §13 item 13.
- **WP6-W5 (hypothesis).** η/2q needs angle-averaged S, not isotropic f_χ. → WP0-v2 (9.1).
- **WP6-N1 (NOTATION).** v_E = 250 was |v_⊙|; ρ_χ = 0.4 vs 0.3. → CONVENTIONS §8, §13 items 2–3 (resolved; no further action).

## 10. Literature (IDs verified against the arXiv API in v1, 2026-10-31; not re-read for v2)
- [FT] 1509.01598 (Essig et al.): Eqs. (15)–(17), (21), (58)–(68). [FT] 2311.04957 (Bernreuther, Fox, Lillard, Taki, Yu): Eqs. (1)–(26).
- [FT] 2105.00599 (Baxter et al., conventions): Eqs. (10)–(14), Tables 1–2, §2–§3.1. [FT] 2011.12896 (Maity, Ray, Sarkar): abstract, §3 values.
- [FT] 1011.1915 (Fox, Liu, Weiner). [FT] 2101.08275 (Knapen et al.): Eqs. (10)–(16).
- [ABS] hep-ph/0209110, 1111.0292, 1408.6865, 1007.1727, 1010.4300, 1904.04781, 2001.09156, 2004.10709, 2004.11499, 2105.05253, 2210.14917,
  2104.12786, 2306.14944, 2603.12326, 2312.13342, 2503.14617, 2509.03608, 2411.03433, 1203.3542.
- [FT via WP1] 2607.06005 (WP1-v2 §6.2).
- Via owner returns: WP1 [E4], [E12]; WP2 (3.4), G11; WP5 §8, (W4); O4 §6 d1–d11; X2 interim factor.

## 11. Open items handed on (labels OW6-n; v1 "O6-n", renamed to avoid WP0's O6)
- OW6-1: G8′ (4.5), the moment-problem characterisation of Radon transforms for anisotropic halo-independent bounds.
- OW6-2: WP1 to supply p_on(q) near E_th for Si, Ge (ZPL, excitons). For S^{X+}: **supplied** by WP3-v2 for S̄^{X+} (row 33), used in (3.3).
- OW6-3: WP5 to supply a continuous P_casc(N_eh|Λ; θ) with F_eh and ε_eh nuisances, replacing the discrete yield models.
- OW6-4: decide r_mat and the profile-versus-envelope convention (6.2) at synthesis (M4).
- OW6-5: WP0 erratum for W1–W5 and NOTATION N1: **closed** (WP0-v2, CONVENTIONS §8).
- OW6-6: referee check of hypothesis (P) in (4.2) against O4's per-sector positivity map (Γ_Λ₀/δ over (q,ω) in Si, OW0-10).

---
## 12. Contested corrections
None. Every owed correction is applied as stated. One remark, not a contest: CONVENTIONS §8 fixes reference scalars at v_E^ref = 250.5 km/s
rather than the annual mean 252.1 that v1 recommended for integrals; v2 agrees (integrals already use v_E(t); scalars are frame quantities).
Using 252.1 would shift every threshold mass by −0.4% (m_min ∝ v_max^{-2}; v_max 796.1 vs 794.5) — inside the annual band of (3.5).

## 13. Interface flags
| # | Owner | Quantity | Recorded form | Mismatch / action |
|---|---|---|---|---|
| IF6-1 | WP5 | (R-k) nuisance | WP5-v2 θ_Rk | **closed** (AUDIT A12): WP5-v2 renamed θ_k → θ_Rk; WP6-v2 adopts θ_Rk, θ_GW, θ_exch |
| IF6-2 | WP0-v2 | (8.3) χ² quantile; (8.1) a_k; ℒ, π_k | "c = 2.71"; a_k; ℒ, π_k | bare c is reserved for the band subscript (CONVENTIONS §4): write 2.71 explicitly; a_k (A-type amplitude, distinct from magnon a_{kν}), ℒ, π_k need NOTATION rows. **Rows now in NOTATION v4 §M** (a^A_k, ℒ, π_k, 2.71); WP0-v2 and this return write a^A_k (CORRECTIONS §17) |
| IF6-3 | NOTATION | experiment index | §E "s_ei, b_ei" | e is the electron label; WP6-v2 and WP0-v2 (8.3) use ex (s_{ex,i}, b_{ex,i}, θ^det_ex); update the row |
| IF6-4 | WP0-v2, O4 | positivity of Λ-resolved 𝒜 | WP0-v2 §6.2(i): per-sector PSD only in the window or bins ≳ δ | (4.2) now carries hypothesis (P); referees to confirm (OW6-6) |
| IF6-5 | WP1, WP3 | pair-resolved LFE weight (GaAs) | WP0-v2 (7.2) retarded out-state vs WP1 [E2] (F1) | **closed** (AUDIT A12): F1 accepted; S_Lambda uses WP0-v2 (7.2); totals unaffected |
| IF6-6 | WP2 | NR tables, sector name | WP2 (2.2), (3.4), S_ℓm; "G sector" | **closed** (AUDIT A12): WP2-v2 uses GS; tables used as recorded (n_ph truncation, S_aniso/NN) |
| IF6-7 | WP5 | seeding | WP0-v2 (7.3) = WP5 (W6) | (1.7), (4.1), S_Lambda follow it; P_casc indexed by Λ, not (q,ω) |
| IF6-8 | WP3, WP5 | Fano term 𝔉 (GaAs) | O4 d7 [C] | library gate requires the export; size open (F8) |

## 14. Corrections applied (closing table)
| # | Correction (ID / source) | Where applied | How |
|---|---|---|---|
| 1 | Add "Symbols introduced/used" (CORRECTIONS §12 row 1; NOTATION-APPLY D8) | §15 | table, no deviations |
| 2 | τ string `nT=130K` → nT order + T metadata (CORRECTIONS §12; coordinator addition; WP0-v2 F9; NOTATION-APPLY D3) | §7.3, §2.2 | CONVENTIONS §11 string; `Mg` key; WP6v2-C13 |
| 3 | Thermal-order vs temperature in the nuisance table (same source, CONVENTIONS §11 "temperature-in-an-order-slot") | §5.2 | n_T row (order increment) and T row (metadata, σ_T) split |
| 4 | v_E: v_E(t) in integrals, v_E^ref = 250.5, 252.1 in halo band (CORRECTIONS §12 row 3; coordinator confirmation; CONVENTIONS §8) | §2.3 V4, §2.5 D3, §3.1, §3.5, §6.3 | all numbers recomputed at 250.5 / 794.5 (C4c, C6, C7); annual band [781, 810]; m_min at E_th per row 30 |
| 5 | ρ_χ flag resolved to 0.3 (CORRECTIONS §12 row 4, §15) | §2.5 D3, §6.4, §9 | stated as resolved |
| 6 | Renames v_⊥→v_T, u_∥→v_∥, δ/Δ₀→δ_v/δ_v,0, K→N_esc, A₀/A₂→A^{(0)}/A^{(2)}, p→p_on, ν_e→θ^det_ex, ρ_mat→r_mat, r_k→r^M_k, k→k_tail, ε→ε_eh, X→𝒳 (CORRECTIONS §12 row 5) | throughout | applied |
| 7 | Label prefixes C, D, W, N → WP6-… (CORRECTIONS §12 row 5; CONVENTIONS §14) | throughout | WP6-D1…D6, WP6-W1…W5, WP6-R1…R3, WP6v2-Cn; O6-n → OW6-n |
| 8 | Global renames (CORRECTIONS §0): Δ_k→Δ^τ_k, O_i→𝒪_i, n_e (density)→𝓃_e, R→ℛ, Fano F→F_eh, step Q/n_e→N_eh^{step}, M¹→𝓜¹; f→f_χ, F→F_DM | throughout | applied; source quotes keep source notation with a dictionary (§2.1) |
| 9 | Static DFPT error O(ω_Q²/E_g²) (WP0-v2 F11, X2) | §5.2 screening row | stated, negligible |
| 10 | Seeding inside the q integral, multi-operator weight (WP0-v2 (7.3); WP5-1, WP5-2) | (1.7), (4.1), §4.4, §7.1 | Σ_Λ tr[𝔇S(Λ)]P(i|Λ); Λ-resolved A^{(n)} tables |
| 11 | No plasmon label within RPA (WP0-v2 (7.1); WP5-3) | §7.1 | S_Lambda spec |
| 12 | R&K is a photon-seed fit (WP0-v2 (7.3); WP5-4) and WP5 §8 nuisances | §2.2 step 6, §5.2 | θ_seed, θ_Rk, θ_GW, θ_exch, θ_PES, θ_LZ, θ_esc (WP5-v2 names, row 31), (W4) constraint |
| 13 | Per-sector positivity only in the window / bins ≳ δ (WP0-v2 §6.2(i); O4) | (4.2) | hypothesis (P) with proof of sufficiency |
| 14 | Ladder error = computed next-rung difference (WP0-v2 Table 6.1, (8.1)) | §5.2 | v1 fallback withdrawn |
| 15 | Screening of non-density rows (WP0-v2 (5.3); WP1-D4, D5; CONVENTIONS §7) | §5.2, §7.1 | S_iso/ab screened per (5.3) |
| 16 | P,T-broken targets: nonreciprocal S, rate odd in the DM wind; keep odd-ℓ harmonics; ℓ = 4 statement only for P- or T-symmetric cubic targets (WP0-v2 (4.3); WP4-D6; WP4-revision interface flag, coordinator relay) | (1.5), (2.4a), §4.5, §7.1, §8 | stated explicitly; odd-ℓ library blocks |
| 17 | Retarded out-state LFE weight for pair-resolved tables (WP0-v2 (7.2), CC-1, F1) | §7.1 | S_Lambda spec |
| 18 | O4 code-pair conditions d1–d11 mandatory (CONVENTIONS §10; SOTA O4 (iv″d); WP0-v2 (7.3)) | §7.1, §7.3, §7.4 | metadata hashes and release gates; d11 in (4.2) |
| 19 | Relativistic f-sum factor (WP0-v2 (4.6′); WP1-D2) | §5.3, §7.1 checks | included in the gate |
| 20 | 2W_κ = q·B_κ·q direction-dependent (WP0-v2 Table 6.1; WP2-D2) | §5.2 e–ph row | stated |
| 21 | NR phonon-order truncation and K labels replace x_coh (WP0-v2 §6.1; WP2) | §5.2 | P[Pois(2W) ≥ N] row |
| 22 | WP0 citations renumbered to v2 ((7.2)→(7.1)/(7.3), Theorem D(iii)→§6.2(iii), (8.2)→(8.1), (6.1)→§6.1, ZG deterministic) | throughout | applied |
| 23 | Equation/section ambiguity of v1 (1.5)/(1.6) vs WP0-v2's citations [self, found in revision] | §1.5, (1.6), §0 | equation number = section number |
| 24 | v1 regime-A interval empty for the adopted halo [self] | (3.2) | regimes by δ_v,× = 173 km/s; exact next order (C4c, C4d) |
| 25 | (3.4) tail exponent only "[D, given the form]" [self] | (3.4) | proved for any power-law tail (C5c) |
| 26 | Checks script numerical (numpy/scipy) vs brief "sympy only" [self] | code/WP6-v2/checks.py | 27 exact/closed-form checks, all PASS |
| 27 | Uncomputed-BSE interim nuisance (WP1-v2 IF-3, [E8], §1.5; coordinator relay): η_xc·S ≈ 1% replaced | §5.2 ladder row, §0, §3.3 | type M r^M_𝒳 ∈ [+0.3, +1.0] for E_min(q) ≤ ω ≲ E_min(q) + 1 eV; type A bound-exciton lines below E_min(q) |
| 28 | Anharmonic nuisance must respect WP2's three linear constraints for all θ (WP2-v2 IF-4, (6.1′); coordinator relay) | (5.1′), §5.2 n_A row | moment projection Π onto the constraint-preserving subspace (type A) + δE^kin term; M type only with the stated O(θ(1−θ)(r^M)²) violation; WP6v2-C15 |
| 29 | PAER onset exponent supplied (superseded by row 33) (WP3-v2 IF-5, §M3, §7, WP3v2-C19; coordinator relay) | (3.3), §5.2 n_g row, OW6-2 | p_on = 2 (allowed, M̃ ≠ 0 at pockets), 3 (symmetry-forbidden, M̃ linear), ½ per exciton band; edge exponents 11/2, 13/2, 4 (+k_tail); choice type Δ |
| 30 | Threshold convention (AUDIT A9): default E_th = measured E_g(T_op); every m_min names its E_th | (3.1), (3.5), WP6-D5, C7 | Si 1.170 eV → 0.333 MeV (annual 0.320–0.344); PAER edge 1.188 eV → 0.338 MeV; Ge 0.744 eV → 0.212 MeV; 1.12 eV (0.319) kept as a labelled scissor-code comparison |
| 31 | WP5-v2 nuisance names; add θ_𝔉 and θ_Eg rows; close IF6-1, IF6-5, IF6-6 (AUDIT A12) | §5.2, §13, §15 | θ_Rk, θ_GW, θ_exch; θ_𝔉 type A on P_casc, \|ΔP\| ≤ 0.11Γ/δ, 0 for Si/Ge; θ_Eg type E |
| 32 | 2607.06005 tag (AUDIT A15) | §2.3 V3, §10 | [FT via WP1] |
| 33 | PAER onset exponents recomputed for the angle-averaged S̄^{X+} (AUDIT A1; WP3-v2 §M3, §7) | (3.3), §5.2 n_g row, OW6-2, C5b | supersedes row 29's 2/3/½: p_on = 3 generic (4 on a vertex zero), Si TA 4 at E_g^{ren} + c_TA·d (LA, TO/LO kinks 3), forbidden pockets 4–5, exciton replicas 3/2–5/2, none in the edge shell d < Q_w ≈ 0.2 Å⁻¹; edge exponent 7/2 + k_tail + p_on; choice type Δ |
| 34 | NOTATION v4 renames (CORRECTIONS §17) | §5.1 (A), (5.1′), (6.2), §5.2 yield row, IF6-2, §15 | y → y_R; Π[·] → Π_mom[·]; W (Lambert-W value) → W_Lam; a_k → a^A_k; θ_Rk → θ_{R-k} (WP5-v2 v4 name); θ_W, θ_X → θ_GW, θ_exch and J_s → J^{(sh)} already in place; rows 12, 31 and IF6-1 keep θ_Rk as history; §15 updated to v4. Notational only |

**Count:** 33 corrections applied (29 owed or interface-routed, 4 found in revision); 0 contested; 8 interface flags (§13), of which IF6-1, IF6-5, IF6-6 are closed. Row 34 (NOTATION v4 renames) is notational and outside this count.

## 15. Symbols introduced/used
All symbols follow NOTATION v4 and CONVENTIONS; **no deviations** (v4 renames: CORRECTIONS §17, closing-table row 34). Used as defined there: q, q̂, ω, ω_q, Δ_χ, v, v_χ, v^⊥, v_T, v_∥, v_min,
v_*, q_*, v_max, δ_v, δ_v,0, m_min, E_th, m_χ, μ_χe, 𝒪_i, 𝒱_a, 𝔇_ab, 𝔇^{(n)}, Ṽ, σ̄_e, F_DM, j_χ; ρ_χ, f_χ, v₀, v_esc, v_⊙, v_⊕(t), v_E(t),
v_E^ref, N_esc, η, ξ, η̃, 𝒢, f̂^{(n)}, k_tail; S, S_ab, S̄, S_ℓm, S(q,ω;Λ), S_IA, S^{X+}, R, R̃, ε, ε̃, ε_e, ε₂, L, 𝓜¹, ω_p, f_xc^T, ρ_cv,
O_a, j_T, J_T, n_e(q), 𝓃_e, ⟨T⟩, Ω, N, V, ρ_T, α, m_e, κ_BO, η_ep, η_anh, η_xc, E_x^b, t_g, 2W_κ, B_κ, n_{Qν}, ω_{Qν}, n_ph, S_κκ; τ, 𝒳, K, 𝔐,
n_B, n_g, n_A, n_T, n_D, θ_k, Δ^τ_k, r^M_k, σ_E, σ_T, r_mat, θ^det_ex, 𝔈_i, P_det, N_i^up, 𝒜_ij, A^{(0)}, A^{(2)}, p_on; GS, X0, X+, Λ,
Λ₀, DC, 𝔉_{Λ₀,ν}, Γ_Λ₀, δ; N_eh, N_eh^{step}, P_casc, ε_eh, F_eh; E_g, ZPR, ZPL, PAER, ZG; 𝐛_NR, ℓ, Y_ℓm, K^cub_ℓ, j₀.
Index names: ex (experiment; as in θ^det_ex and WP0-v2 (8.3)), i (bin), j (halo step), k (truncation), sh (core shell).
Introduced here (new objects, no collision; now NOTATION v4 §M rows):
- **A^{(n)}(q,ω;Λ)**: Λ-resolved A^{(0)}, A^{(2)} ((4.1)); **tr_T**: transverse trace (δ − q̂q̂):X ((1.4)); **d₂, d₂′**: isotropic coefficients of
  𝔇^{(2)} under (I) ((1.4));
- **Π_mom[·], c_b, 𝔪_n, y_R, Δ′_A, P_δ, θ_A, θ_δ, σ_δE**: moment projection, its coefficients, moments of S^τ, ω − E_R, shape template, δE^kin direction, amplitudes, δE^kin uncertainty ((5.1′));
- **P(i|Λ)** ≡ Σ P_det(i|N_eh)P_casc(N_eh|Λ) ((1.7)); **𝒜_i(u₀)**: single-step column of 𝒜 ((4.2)); **v_j, η̃_j, N_v**: halo steps (2311.04957);
- **δ_v,×**: regime crossover 3v_escv₀²/(2v_esc² − v₀²) ((3.2)); **a_lens, ϱ**: lens curvature and axial distance ((3.4));
- **c_TA, d, K, Q_w**: TA sound speed (NOTATION c_ν with ν = TA), distance min_K ||q| − |K||, connecting phonon wavevectors, edge-shell width (WP3-v2) ((3.3));
- **N^obs_{ex,i}, s_{ex,i}, b_{ex,i}**: observed counts, signal per unit σ̄_e, background ((6.1)); **ℒ, π_k, a^A_k**: likelihood, prior, A-type
  amplitude (as WP0-v2 (8.1), (8.3); IF6-2; v3 name a_k); **k_δ** = ln(1 + δ) and **W_Lam** (Lambert-W value) in (6.2), local (W stays Debye–Waller); **σ̄_e^up**: upper limit;
- **q_max** (library cutoff); **𝓃_e^{(sh)}, J^{(sh)}(p_z), E_B^{(sh)}**: shell density, Compton profile, mean binding energy ((5.2)); **p_z**:
  projected electron momentum;
- **θ_seed, θ_{R-k}, θ_GW, θ_exch, θ_PES, θ_LZ, θ_esc, θ_𝔉, θ_Eg**: WP5-v2 nuisances, WP5's names (AUDIT A12; v4 θ_{R-k} for v3 θ_Rk); **N_q, N_ω, N_bins**: grid sizes.
Labels: WP6v2-Cn (checks), WP6-D1…D6 (source discrepancies), WP6-W1…W5, WP6-N1 (WP0/NOTATION defects, closed), WP6-R1…R3 (report objects),
(I), (P), (V1)–(V8) (hypotheses/conditions), IF6-n (flags), OW6-n (open items), G8′ (gap).
