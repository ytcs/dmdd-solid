# R8 / WP6-v3: rate assembly and uncertainty quantification (corrected standalone version after the R7 hostile review)

Revision agent, brief R8/REV3-WP6. Supersedes returns/R6/WP6-v2.md (kept as the record). Applies every verdict of REF-WP6-A and REF-WP6-B
(referees/R7/), the coordinator notes in state/SOTA.md "R7 referee reports", and the interface flags addressed to WP6 in the R8 returns
WP0-v3 (G1, G4, G6, G7, G10, G12), WP1-v3 ([E13]; IF-3, IF-4, IF-6/6b, IF-10, IF-13), WP2-v3 (IF-4), WP3-v3 (final p̄_on table, IF-5, IF-8,
IF-10), WP4-v3 (I4, I11, I12, I13) and WP5-v3 (IF-R8-5, IF-R8-6). Conventions: CONVENTIONS.md; symbols: NOTATION v4 (new symbols in §15).
WP0 equations are cited as **WP0-v3 (s.n)** (their numbers equal WP0-v2's). Assigned work: L24, G4, G8.
Checks: `code/WP6-v3/checks.py`, sympy only (closed forms with evalf; one `nsolve` root of three moment equations in C24, no simulation),
**42 checks, all PASS** (≈ 2 min; §14 end; R9: C30 added); cited as WP6v3-Cn. C1–C15 keep their v2 numbers (C5b, C8c, C10a,b, C11 repaired); C16–C29 are new (C30 added in R9).
Tags: **[D]** derived (hypotheses stated), **[D, sketch]**, **[E]** estimated, **[C]** conjectured; literature status **CONFIRMED** (a referee checked
the full text), **UNRESOLVED** (not checked or not decidable from the text), **REFUTED** (dropped), plus [FT]/[ABS] as in v2 for unrefereed
items. Labels from other returns carry their prefix (CONVENTIONS §14). Equation number = section number, as in v2.
**Literature equation numbers** are the arXiv-HTML sequential tags (REF-WP6-B B). JCAP/PDF equivalents: 2311.04957 (3)→(2.1), (4)→(2.2),
(7)→(2.5), (13)→(2.11), (17)→(2.15), (19)–(20)→(2.17)–(2.18); 1509.01598 (65)→(B.1), (66)→(B.2), (67)→(B.3), (68)→(B.4)–(B.5).

---
## 0. What changed (v2 → v3)
| v2 | v3 | change (referee item) |
|---|---|---|
| (1.3) Θ(v − u) | (1.3) | Θ(v − \|u\|): exothermic DM, v_min < 0 (B-2) |
| (1.3)–(1.4) "S → S̄" | (1.3) | orientation average with co-rotated indices defined; component-wise average is wrong (A-2; C26) |
| (1.5) "TR removes the ℓ = 3 invariant"; "leading ℓ = 1" | (1.5) | TR or P removes **all** odd ℓ; no cubic group has ℓ = 1; lowest odd ℓ set by G_eff (3 for T, T_d; 9 for O); ℓ = 1 only for polar G_eff; odd part O(q³) for densities (WP4-v3 I4; WP0-v3 G12); n = 2 anisotropy form; the daily mean keeps the zonal projection (A-3, B-3; C11, C27, C28) |
| (1.2), (1.7), (4.1) tr[𝔇S] | same | **Σ_ab𝔇_abS_ab = tr[𝔇ᵀS]** (WP0-v3 G1) |
| (V2) "only 𝒪₁" as a small-parameter condition | (2.3) | hypothesis on the model (leading c₁) + its own corrections (A-6) |
| (V4), (3.2) e^{±1.17} ≈ ×3.2, "≈ 2.5" | (2.3), (3.2) | exact asymmetric factors ×2.26/×0.100 (v_esc ± 25), ×2.22/×0.373 (annual) at 760 km/s (A-13, B-6, B-9; C16) |
| (3.1) m_min = 2E_th/v_max² as the edge | (3.1), (3.1′) | **general edge min_q q²/[2(q v_max − E_th(q))]**; 0.333/0.212 MeV are unattained kinematic floors; PAER edges 0.337 (continuum) / 0.333 (exciton replica) MeV [E]; window from WP1-v3 [E13]/WP3-v3 IF-8 (A-12, B-8; C18) |
| (3.3) "Si TA p_on = 4" | (3.3) | WP3-v3 final p̄_on table (Si edge 3, LA kink 4, …); corner contact p + k + 4; bound lines; validity window Δm/m ≲ 1–5% (B-10, A-D3; C19, C20) |
| (3.5) 3–6% / 6–12%; 7% | (3.5) | 2–7% in v_max; 2.5% E_th offset vs the default (A-B3, B-9; C17) |
| (4.2) "single step because 𝒜 ≥ 0"; (P) "proof" | (4.2) | monotone step-column theorem; (P) a hypothesis with sufficient conditions and an O(ω_Q/ε_eh) leakage; library gate; Bonferroni CL (A-16, B-12; C21) |
| (4.2a) "η̃ profile unique (as 2311.04957 states)" | (4.2a) | **dropped (REFUTED)**: every local minimum is global, μ̂ unique, η̃̂ unique only mod ker 𝒜 (A-11, B-7) |
| (5.1) M "PSD for all θ"; "positivity automatic for M and A" | (5.1) | M acts on contracted scalars or on the PSD geodesic; A only on PSD increments (B-14; C22, C23) |
| (5.1′) "type A", θ_δ ~ 𝒩(0,1), support sentence | (5.1′), (5.1″) | renamed type L (affine, support-restricted); **exponential tilting (type T)** is the PSD, exact-constraint form; support ⊆ supp X ∪ supp S^τ; WP2-v3 (2π/Ω)\|c_κ\|² normalisation (A-18, B-15; WP2-v3 IF-4; C24) |
| (5.2) priors | (5.2) | log-symmetric encodings (ladder median 1.61 S^τ; PAER [0.4, 1.8]); WP1-v3 IF-3 (÷3), IF-13 (triplet ladder); WP4-v3 I12 (BCS); WP5-v3 θ_Z, θ_dense, θ_seed unbounded, θ_𝔉 bound (B-14; C25) |
| (5.3) f-sum informative only for non-conserving local truncations | (5.3) | scissor and GW–BSE rungs are non-local, hence informative (+3.5% scissor violation, WP1-v3); relativistic factor −0.23%/−0.73% (WP0-v3 G4); L17 support qualified (WP0-v3 G6) (B-16) |
| (6.2) "up to ×1.8"; W_Lam | (6.2) | ×1.35 (M) / ×1.57 (linear); no linear limit for δ_θ > 0.607; w_δ (quadratic root) (A-19, B-17; WP0-v3 G7; C8c) |
| (6.4) "exact recast" | (6.4) | qualified: exact only for the min-over-bins procedure, whose CL needs a trials correction (A-20, B-18) |
| (4.4) cost | (4.4) | prefix sums remove N_v; profiling cost with M types stated (B-19; C29) |
| K, δ (two meanings), d | 𝐊_pk, δ_θ, d_K | notation collisions removed (A-22, B-G) |
| WP6-D1 last sentence; D4 | §2.5 | D1 sentence → [E]/UNRESOLVED; D4 extended (Θ(v_esc − v_χ) typo) (A-9, B-7) |

---
## 1. Rate assembly from WP0-v3 (3.4): the general halo functional

**(1.1) On-shell kinematics [D].** Hypotheses: WP0-v3 (3.3)–(3.4) (first Born, Gibbs target, unpolarised DM) and a lab-frame f_χ(v).
With ω_q from WP0-v3 (2.1),

  δ(ω − ω_q) = q^{-1} δ(q̂·v − v_min),   v_min(q,ω) = (ω + Δ_χ)/q + q/2m_χ.                                                    (1.1)

For Δ_χ < 0 (exothermic DM) v_min can be negative (B-2). On shell v = v_min q̂ + v_T, q̂·v_T = 0; the DM-side velocity of WP0-v3 (2.1) is
v_χ = v − q/2m_χ = v_∥ q̂ + v_T with **v_∥ = (ω + Δ_χ)/q fixed by kinematics**. The halo enters only through v_T.

**(1.2) Velocity polynomial [D]** (STANDS, A-1, B-1). Every Fitzpatrick 𝒪_i is at most linear in v^⊥ (WP0-v3 (2.2)), so 𝒱_a is affine in v_χ:
𝒱 = 𝒱₀ + 𝒱₁·v_T and 𝔇 = 𝒱†𝒱 = 𝔇^{(0)} + 𝔇^{(1)}·v_T + v_T·𝔇^{(2)}·v_T with 𝔇^{(2)} = 𝒱₁†𝒱₁ PSD in the joint index. With the WP0-v3 contraction
Σ_ab𝔇_abS_ab = tr[𝔇ᵀS] (G1):

  dℛ/dω = (ρ_χ/m_χρ_T) ∫d³q/(2π)³ q^{-1} Σ_{n=0}^{2} tr[𝔇^{(n)ᵀ}(q,ω) S(q,ω)] · f̂^{(n)}(q̂, v_min),
  f̂^{(n)}(q̂,u) ≡ ∫d³v f_χ(v) v_T^{⊗n} δ(q̂·v − u).                                                                                (1.2)

f̂^{(0)} is the Radon transform of f_χ; 𝒢(q,ω) = f̂^{(0)}(q̂,v_min)/q (CONVENTIONS §8). **Strict halo independence means bounding f̂^{(0)},
f̂^{(1)}, f̂^{(2)}, not η.** On shell, for local H and elastic DM, only P_Tv_χ and j_T, J_T survive (WP0-v3 (2.2); WP1 [E4], which needs an
SU(2)-invariant H, WP0-v3 G13).

**(1.3) Isotropic reduction [D]** (STANDS WITH CORRECTION, A-2, B-2). *Hypothesis (I):* the S entering (1.2) is replaced by its **orientation
average with co-rotated indices**,

  S̄_ab(q,ω) ≡ ∫_{SO(3)} dR  D(R)_{aa′} S_{a′b′}(R^{-1}q, ω) D(R)^{-1}_{b′b},                                                        (1.3a)

D(R) the representation carried by the operator indices (scalar for n, vector for j, axial for s), or the target is isotropic (not isotropic
f_χ; WP0-v3 (9.1)). For a scalar response (S_ee) (1.3a) is the plain q̂-average. For vector/axial rows it yields isotropic structures
αδ_cd + βq̂_cq̂_d + γε_cdeq̂_e; a **component-wise q̂-average at fixed lab indices is wrong**: for S_cd = s_Lq̂q̂ + s_T(δ − q̂q̂) it gives
(s_L + 2s_T)δ/3, which mixes the longitudinal and transverse responses (WP6v3-C26). Under (1.3a) the n = 1 term drops (a rotation scalar linear
in v_T built from q̂ alone is ∝ q̂·v_T = 0; a pseudoscalar needs a third vector; C10c). The q̂-averages, for either sign of u (C10a,b), are

  ⟨δ(q̂·v − u)⟩_q̂ = Θ(v − |u|)/2v,   ⟨|v_T|²δ(q̂·v − u)⟩_q̂ = (v² − u²)Θ(v − |u|)/2v,

so the rate needs only

  η(u) = ∫d³v f_χ Θ(v − |u|)/v,   ξ(u) = ∫d³v f_χ (v² − u²)Θ(v − |u|)/v,   **dξ/d|u| = −2|u| η, ξ(v_max) = 0 ⇒ ξ(u) = 2∫_{|u|}^∞ u′η(u′)du′**   (1.3)

(Leibniz rule, any radial density; the boundary term vanishes because the integrand of ξ is zero at v = |u|; C12). **Under (I) velocity-dependent
operators add no halo freedom: ξ is a functional of η.** The rate is

  dℛ/dω = (ρ_χ/(4π²m_χρ_T)) ∫q dq [A^{(0)}(q,ω) η(v_min) + A^{(2)}(q,ω) ξ(v_min)],
  A^{(0)} = Σ_ab 𝔇^{(0)}_ab S̄_ab,   A^{(2)} = ½ Σ_ab tr_T[𝔇^{(2)}_ab] S̄_ab,   tr_T X ≡ (δ_cd − q̂_cq̂_d)X_cd.                          (1.4)

Under (1.3a), M_cd ≡ Σ_ab𝔇^{(2)}_{ab,cd}S̄_ab = d₂δ_cd + d₂′q̂_cq̂_d + d₂″ε_cdeq̂_e; v_Tv_T annihilates the last two, ⟨v_T^cv_T^d⟩_az =
½|v_T|²(δ − q̂q̂), so A^{(2)} = d₂ (C10c). **Positivity [D]** (from REF-WP6-B A2, needed in §4): for PSD S̄, A^{(0)} = tr[𝔇(v_T = 0)ᵀS̄] ≥ 0, and for
any w ⊥ q̂, w_cw_dM_cd = Σ_ab⟨(𝒱₁·w)_a*(𝒱₁·w)_b⟩S̄_ab ≥ 0, so d₂ = A^{(2)} ≥ 0. Check: for n_e alone A^{(0)} = |Ṽ|²S̄ = πσ̄_eF_DM²S̄/μ_χe², and (1.4) is
exactly WP0-v3 (9.2), with 𝒢 = η/(2q). The angular factor (2π)⁻³·4π·½ = 1/(4π²) is verified by both referees.

**(1.5) Anisotropic targets [D]** (STANDS WITH CORRECTION, A-3, B-3). Write S(q,ω) = Σ_{ℓ,μ} S_{ℓμ}(|q|,ω)K_{ℓμ}(q̂) in the invariant harmonics of
the **effective group** G_eff acting on q̂: G_eff = H ∪ {−g : g ∈ G∖H}, H the unitary part of the (magnetic) point group G and the antiunitary
elements gT acting as q → −gq (TR maps S(q) to S(−q) for densities).
- *P or T present* (−1 ∈ G_eff): S(q) = S(−q), so **every odd ℓ vanishes** (ℓ = 3, 7, 9, 11, 13 of T_d included, not only "xyz"; WP6v3-C11).
  For O_h (Si, Ge) and T_d + TR (GaAs) the invariants up to ℓ = 12 are ℓ = 0, 4, 6, 8, 10 and two at ℓ = 12: 7 coefficients, none at ℓ = 2.
  **The first correction to the η-only rate is ℓ = 4.**
- *P and T both broken* (−1 ∉ G_eff): odd ℓ allowed by G_eff are kept. **No cubic group has an ℓ = 1 invariant** (C28); the lowest odd ℓ is 3
  for G_eff ⊇ T or T_d and 9 for G_eff = O. **ℓ = 1 needs a polar G_eff** (1, 2, m, mm2, 4, 4mm, 3, 3m, 6, 6mm). For densities the odd part is
  S(q) − S(−q) = 2q^αq^βq^γb^{NR}_{αβγ}(ω)/ω² + O(q⁵) (WP4-v3 [3.2′]; WP0-v3 (4.3), G12; WP0's 𝐁^{NR}_{αβγ} ≡ b^{NR}_{αβγ}/ω², one object, AUDIT-2 m17): **O(q³), relative O(q)**, not q-linear; its angular
  content is ℓ = 1 ⊕ 3, of which only the G_eff-invariant part survives. The q-linear odd part exists only for the j and s rows (WP4-v3 I11).
  v2's "leading ℓ = 1" is replaced by "lowest odd ℓ allowed by G_eff".
- *Velocity-dependent operators* (A-3, second correction): (1.2) = Σ_ℓ S_ℓ f̂^{(0)}_ℓ holds for the n = 0 term only. The n = 2 term pairs the
  crystal tensor field T_cd(q̂) = Σ_ab𝔇^{(2)}_{ab,cd}S_ab with f̂^{(2)}_cd. Its first cubic anisotropy has total angular momentum J = 4 (the lowest
  non-isotropic cubic invariant tensor has rank 4), and coupling J = 4 to the rank-2 index gives orbital ℓ ∈ {2, 4, 6} (even by parity) in the
  halo factor, a rank-2 moment of f̂^{(2)}, not the ℓ = 4 moment of f̂^{(0)} [D, sketch].
- *Daily average* (B-3(ii)): a lab-fixed crystal sees the wind direction ŵ(t) on a cone of half-angle β about the Earth axis n̂ (crystal frame).
  The sidereal-day mean of K_ℓ(ŵ(t)) is P_ℓ(cos β)K_ℓ(n̂) (addition theorem; C27 for ℓ = 1, 3, 4). **The zonal projection of every ℓ survives the day
  average**: the ℓ = 4 term of cubic targets corrects the day-averaged rate, and for P,T-broken targets the odd part (first order in b^{NR}) does too.
  The day average therefore does not restore (I); (V3) is restated accordingly.

**(1.6) Conventions dictionary [D]** (STANDS, A-4, B-4; C1–C3). With S̄ the angle-averaged S_ee of WP0-v3 (3.1), spin included:

  |f_crys(q,ω)|² = Ω q³ S̄_ee(q,ω)/(4παm_e²)                           [1509.01598 Eqs. (21), (64) normalisation; CONFIRMED]
                 = Ω q⁵ L̄(q,ω)/(8π²α²m_e²)   (T = 0, ELF form WP0-v3 (5.4)/(9.3); unscreened: L → ε₂)   [= 2101.08275 Eq. (16)]
  |f_res(q,ω)|²  = (8αm_e²ω/q³)|f_crys|² = 2ΩωS̄_ee/π                     [2311.04957 Eq. (4); CONFIRMED]                         (1.6)

1509.01598 Eq. (17) is per target (×N_cell); 2311.04957 Eq. (3) is **per unit cell** (WP6-D1, CONFIRMED by both); WP0-v3 (3.4)/(9.2) is per unit
target mass. Library tables carry ΩS̄ (per cell, eV⁻¹).

**(1.7) Measured observable [D given WP0-v3 (7.1), (7.3)]** (STANDS, A-5, B-5). With P(i|Λ) ≡ Σ_{N_eh} P_det(i|N_eh)P_casc(N_eh|Λ) and 𝔈_i = exposure × efficiency,

  μ_i = 𝔈_i (ρ_χ/m_χρ_T) ∫d³v f_χ ∫dω ∫d³q/(2π)³ Σ_Λ tr[𝔇(q,v)ᵀS(q,ω;Λ)] P(i|Λ) δ(ω − ω_q).                                       (1.7)

The trace and q integral sit inside the Λ sum (WP0-v3 (7.3) = WP5 (W6)). **μ_i is linear in S, hence in η (or in the f̂^{(n)}).**

---
## 2. L24 derived: SHM rate with η(v_min), and halo-independent bounds

**(2.1) Source formulas [CONFIRMED in full text by REF-WP6-A and REF-WP6-B]** (source notation; E_e ≡ ω, g_χ ≡ f_χ, K ≡ N_esc, n_e ≡ N_eh^{step}, ε ≡ ε_eh).
- *1509.01598 Eq. (17):* "dR_crystal/d ln E_e = (ρ_χ/m_χ) N_cell σ̄_e α (m_e²/μ_χe²) ∫ d ln q (E_e/q) η(v_min(q,E_e)) F_DM(q)² |f_crystal(q,E_e)|²",
  Eq. (15) η(v_min) = ∫d³v g_χ(v)Θ(v − v_min)/v, Eq. (16) v_min = E_e/q + q/2m_χ; SHM Eq. (65) g_χ ∝ e^{−|v+v_E|²/v₀²}Θ(v_esc − |v+v_E|), K from
  Eq. (66), η₁, η₂ in Eq. (68). Values: v₀ = 230, v_esc = 600, v_E = 240 km/s, ρ_χ = 0.4 GeV/cm³.
- *2311.04957 Eqs. (9)–(11), (13), (19)–(20):* "dR/d ln E_e = (8μ²_χe)^{-1}∫dq q |F_DM|²|f_res|² η̃(v_min)", η̃ = (ρ_χσ̄_e/m_χ)η; step ansatz
  η̃ = Σ_i η̃_iΘ(v_i − v_min); binned rate (13) with n_e = 1 + ⌊(E_e − E_gap)/ε⌋ (12), E_gap = 1.2 eV, ε = 3.8 eV (Si; Ge 0.67/3.0); linear map
  R_i = Σ_j 𝒜_ijη̃_j (19), 𝒜_ij (20). Values: v₀ = 220, v_esc = 544, v_E = 232 km/s, ρ_χ = 0.4.

**(2.2) Truncation chain from WP0-v3 [D]** (STANDS, A-6, B-6).
1. WP0-v3 (3.4).
2. Single operator n_e (L0 chain, WP0-v3 (9.1)); Δ_χ = 0.
3. Hypothesis (I): S → S̄ (1.3a), giving 𝒢 = η(v_min)/2q (C10a; WP0-v3 (9.2)).
4. f_χ = SHM (1509.01598 Eq. (65)) → η₁, η₂ of Eq. (68), proved exactly (dη/du = −g(u) on both branches, continuity, η(v_max) = 0; C4a).
5. Dictionary (1.6) → 1509.01598 Eq. (17) exactly (C1).
6. Optionally P_casc(N_eh|Λ) → N_eh^{step}; this is the Λ-marginal only for a photon-type seed (WP5; θ_seed, §5.2) → 2311.04957 Eq. (13).
7. Step basis for η̃ → Eqs. (19)–(20).
τ point (WP0-v3 §6.1): `nB=0|ng=0|nA=0|X=IP|nT=0|K=-|Mg=-|nD=-` + `T=0K;ref=normal;scr=-;conv=window`.

**(2.3) Validity conditions, with numbers [D/E].**
- (V1) *Born:* |Ṽ|μ_χe q/4π ≪ 1; holds by many orders for σ̄_e ≲ 10⁻³⁰ cm² [E].
- (V2) *Leading coefficient c₁* (rewritten, A-6): **hypothesis on the DM model**: the leading NR coefficient is c₁ (𝒪₁). Within such a model the
  corrections are O(v², q²/m_e²) (≈ 10⁻⁶, 10⁻⁴–10⁻³ at q ~ 1–4 αm_e) from 𝒪₁'s own expansion, plus the A^{(2)}ξ term of (1.4). A model with c₃ or
  c₁₁ dominant is not suppressed: it is a different L-entry, not a small correction.
- (V3) *Angle average:* for P- or T-symmetric cubic targets the first neglected term is ℓ = 4 (1.5); size on the day-averaged rate a few % in the bulk
  and larger near the edge [E] (2607.06005 [FT via WP1]; 2411.03433 [ABS]). The day average does **not** remove it (it keeps P₄(cos β)K₄(n̂)), and
  for P,T-broken targets the odd part survives the day average at first order in b^{NR} (relative O(q) for densities) (1.5).
- (V4) *Halo time dependence:* integrals use v_E(t) = v_⊙ + v_⊕(t) of 2105.00599 Eq. (11), averaged over the exposure; reference scalars use
  v_E^ref = |v_⊙| = 250.5 km/s. |v_E(t)| spans 237.4–266.4 km/s, annual mean 252.1 (C6). **Exact SHM factors** (C16; both referees):

  | v_min | v_esc ± 25 | v_E ± 15 | annual extremes (266.4 / 237.4) | v₀ ± 6 |
  |---|---|---|---|---|
  | 600 km/s | ×1.059 / ×0.920 | ×1.201 / ×0.824 | ×1.215 / ×0.845 | ×1.109 / ×0.893 |
  | 760 km/s | **×2.26 / ×0.100** | ×2.13 / ×0.310 | **×2.22 / ×0.373** | ×1.19 / ×0.83 |

  At 600 km/s the linearised ±19% (annual) and ±11% (v₀) are adequate; at 760 km/s (δ_v = 34.5 km/s, comparable to the shifts) linearisation fails
  and the response is asymmetric. v2's "e^{±1.17} ≈ ×3.2" and "factor ≈ 2.5" are withdrawn.
- (V5) *SHM shape with a hard cutoff:* sets the edge exponent (§3).
- (V6) *T > 0 branch:* the ω < 0 weight is ∝ e^{−E_g/T}, negligible (WP0-v3 (9.1)(γ)).
- (V7) *No Earth stopping:* fails at the large-σ̄_e ceiling; not quantified here.
- (V8) *S_ee clamped-lattice IP* (L1). The ELF form needs WP0-v3 (5.5)(i) or (ii).

**(2.4) Leading corrections the URF predicts [D].**
- (a) Anisotropy: η/2q → f̂^{(0)}(q̂,v_min)/q in (1.2); first term ℓ = 4 (n = 0: S_4 × the ℓ = 4 moment of the lab-frame Radon transform; n = 2: a J = 4
  crystal tensor × an ℓ = 2, 4, 6 rank-2 moment of f̂^{(2)}); for P,T-broken targets, the lowest odd ℓ allowed by G_eff (1.5).
- (b) Velocity-dependent operators: the A^{(2)}ξ term of (1.4), ξ = 2∫u′η du′; no new halo input.
- (c) Halo tails beyond the SHM change the edge exponent (3.4).
- (d) Annual and daily modulation (V3, V4).
- (e) Yield: P(i|Λ) with operator-resolved seeding (1.7).
- (f) Theory nuisances θ enter 𝒜_ij (§5).

**(2.5) Discrepancies in the sources** (labels WP6-D1…D6; statuses from the R7 full-text checks).
- **WP6-D1 [CONFIRMED, both]** 2311.04957 Eq. (3) with (4) equals 1509.01598 Eq. (17)/N_cell (C3a): a rate per unit cell; "cell" never appears in
  2311.04957. Recasts must restore N_cell. v2's further sentence "η̃_i in yr⁻¹ absorbs the target size" is **UNRESOLVED** and downgraded to [E]
  (B-7): η̃ = ρ_χσ̄_eη/m_χ has dimension 1/time for any target, so yr⁻¹ by itself absorbs nothing; where N_cell entered their kg·yr fits cannot be
  read from the text.
- **WP6-D2 [CONFIRMED as an ambiguity, not an error, both]** Eq. (13) integrates q over [q₋, q₊] of Eq. (7), defined "for a fixed v" with v unstated,
  *and* multiplies by Θ(v_i − v_min). For any v ≥ v_i the Θ makes the limits redundant, so the result is right if v = v_max. Unambiguous form:
  ∫₀^∞dq … Θ(v_i − v_min(q,E_e)).
- **WP6-D3 [CONFIRMED]** Halo conventions are mixed: 1509.01598 230/600/240, ρ_χ = 0.4; 2311.04957 220/544/232, ρ_χ = 0.4; 2105.00599 v₀ = 238,
  v_esc = 544, ρ_χ = 0.3 [FT v1; not re-checked in R7]. Resolved for the campaign (CONVENTIONS §8): 2105.00599 values, v_E(t) in integrals,
  v_E^ref = 250.5 km/s, v_max = 794.5 km/s.
- **WP6-D4 [CONFIRMED, extended]** 1509.01598 Eq. (67) writes −2vv_Ec_θ where Eq. (65) implies +2vv_Ec_θ, and also Θ(v_esc − v_χ) where Eq. (65)
  has Θ(v_esc − |v_χ + v_E|). Both harmless: Eq. (68) is correct for Eq. (65) (C4a).
- **WP6-D5 [CONFIRMED]** Step-model gap: 2311.04957 uses E_gap = 1.2 eV (ε = 3.8 eV); campaign default E_g(0) = 1.170 eV; scissor codes 1.11–1.12 eV.
  2·1.2 eV/(776 km/s)² = 0.358 MeV. A convention difference, not an error.
- **WP6-D6 [UNRESOLVED in R7]** 2105.00599 §3.1: SHM parameters fixed, not profiled; 2011.12896: v_esc = 528⁺²⁴₋₂₅, v₀ = 233 ± 6. Quoted from the v1
  full-text reading; neither referee re-fetched these papers. §6.3 reports separate objects regardless.

**Status L24: DERIVED** (chain, conditions, corrections). Prefactor = 1509.01598 Eq. (17) (C1) = 2101.08275 Eq. (16) (C2) = WP0-v3 (9.2).

---
## 3. The kinematic edge

**(3.1) Edge mass for a q-independent threshold [D]** (STANDS WITH CORRECTION, A-12, B-8). min_q v_min(q,ω) = v_* = √(2ω/m_χ) at q_* = m_χv_*. **If the
onset E_th of S̄(q,·) does not depend on q** (hypothesis, now stated), scattering requires

  m_χ ≥ 2E_th/v_max²,   δ ln m_min = δ ln E_th − 2 δ ln v_max.                                                                     (3.1)

**(3.1′) General edge [D]** (A-D1, B-E1; = WP1-v3 [E13]). With E_th(q) the onset of S̄ at momentum q (minimised over q̂ and Umklapp copies),

  m_min = min_q q²/[2(q v_max − E_th(q))]   ⇔   min_q [E_th(q)/q + q/2m_χ] = v_max.                                             (3.1′)

(3.1) is the case E_th(q) ≡ E_th (C18); in general 2E_th^{glob}/v_max² (E_th^{glob} = min_q E_th(q)) is a strict lower bound. m_min is monotone in E_th(·)
pointwise. Two exact properties (C18): for a locally linear onset E_th(q) = A − c′q, m_min = 2A/(v_max + c′)²; and at the optimum the slope enters
only at second order, m_min = 2[E_0 + ω(Q*_0)]/v_max² × (1 + O(c′²/v_max²)) (tangency), Q*_0 the phonon momentum at the optimal q.

*Si and Ge at T ≈ 0 (E_th = measured E_g(T_op), CONVENTIONS default; v_max = 794.5 km/s).*
| quantity | Si | Ge | status |
|---|---|---|---|
| floor at E_g **for the e–h continuum**, 2E_g/v_max² | 0.333 MeV (0.3332; E_g = 1.170 eV) | 0.212 MeV (0.744 eV) | [D]; unattained **by the continuum** (free pairs need E_g + ω_ν(Q*)); **not a floor of the total S̄**: exciton replicas start at E_x + ω_TA(Q*), which can lie below E_g (R9, VER-B NEW-1; AUDIT-2 m2) |
| **floor of the total S̄**, 2E_x/v_max² (lowest excitation E_x = E_g − E_x^b) | **0.329** | **0.211** | [D]; WP1-v3 [E13]; reached only for a flat dispersion |
| PAER, exciton replica, E_x + ω_TA(Q*) | **≈ 0.3327 ± 0.0004** (1.1688 eV; ω_TA ≈ 13.5 ± 1.5 meV): at or below 0.3332, undecided within the ω_TA error | ≈ 0.213 (0.7475 eV; vs the 0.212 continuum floor: consistent) | [E]; p̄_on = 3/2 |
| PAER, continuum, E_g + ω_TA(Q*) | **≈ 0.337** (bracket 0.333–0.339) | ≈ 0.214 (ω_TA ≈ 7.5 meV) | [E]; p̄_on = 3 |
| zero-phonon line, forbidden class / allowed class | ≈ 0.42 / ≈ 0.54 | ≈ 0.32–0.36 (allowed, L) | WP1-v3 [E13] [E] |
| zero-phonon at \|q\| = \|𝐊_pk\| (X0 at the pocket) | 0.474 | — | [D] (C18); an upper bound by [E13] |

For Si the optimum is at |q| ≈ 0.9 keV, so |Q*| = |𝐊_pk| − |q| ≈ 0.53 Å⁻¹ ≥ Q_w = 0.33 Å⁻¹ (in the window; WP3-v3 §M3(c)) and the TA minimum is
on axis (|q| ≲ 1.0 keV, WP3-v3 §M3(e)). ω_TA(0.53 Å⁻¹ along [100]) ≈ 13.5 ± 1.5 meV is read from the measured Si dispersion [E]; a linear c_TA = 5.84 km/s
would give 20 meV and 0.339 MeV, an upper bound because acoustic branches are sublinear (ω_TA(Q) ≤ c_TAQ). The Si exciton replica uses E_x^b = 14.7 meV.
The Ge numbers use the L-valley pocket, |Q*| ≈ 0.68 Å⁻¹, ω_TA ≈ 7.5 meV [E] (Ge TA minima are off axis, WP3-v3 §M3(e); the shift is ≲ 1 meV).
**Consequences.** (i) 0.333 and 0.212 MeV are labelled "floors at E_g for the continuum", never channel edges; the floor of the total S̄ is
2E_x/v_max² = 0.329 (Si), 0.211 MeV (Ge). CONTROLS C5 ("no PAER below E_g + min ω_Q at T = 0") holds for the e–h continuum only: the exciton replica
E_x + ω_TA(Q*) (1.1688 eV in Si, since ω_TA(Q*) ≈ 13.5 meV < E_x^b = 14.7 meV) violates it as worded; scope flagged to the coordinator (IF6-18). (ii) The lower edge of the M1 window is the PAER edge, ≈ 0.333 MeV (exciton replica) to ≈ 0.337 MeV (continuum) [E]; the v2/SOTA 0.338 MeV
(E_g + ω_TA(K) = 1.188 eV) used the TA energy at the pocket instead of at Q*_0, in agreement with WP3-v3 §M9 (PAER edge bullet: free pairs 0.336–0.338 MeV, replicas 0.333 MeV).
The acoustic Q* → 0 infimum E_g belongs to WP3's fixed-q control C5 (reached only at |q| = |𝐊_pk|, m_χ ≥ 0.474 MeV) and is not an edge (R9: v3 wrongly
attributed WP3's 0.333 to that infimum; AUDIT-2 m3; no number changes) (flag IF6-11). (iii) The window (WP3-v3
IF-8, WP1-v3 IF-6/6b): **Si PAER-only ≈ 0.333–0.42 MeV; PAER-leading to ≈ 0.43; two-channel 0.43–0.54 (forbidden ZPL open; ratio ϖ_II ≈ 0.03–2 at
the edge, WP1-v3 [E14]); allowed ZPL above ≈ 0.54. Ge PAER-only ≈ 0.213–0.32 MeV.** All [E], pending ab initio E_min(q) and ω_ν(Q).
*Halo–gap degeneracy* (A-D1, B-E1). For a q-independent onset, E_th and v_max enter the edge position only through E_th/v_max². For a q-dependent onset the
scaling E_th → λ²E_th, v_max → λv_max moves m_min by d ln m_min/d ln λ = 2E_th′(q₀)/v_max ~ 2c′/v_max ≈ 1% [D] (C18). The edge **amplitude**
(prefactor e^{−v_esc²/v₀²}/(v_EN_esc), a_lens) depends on v_esc and v_E separately at any order. "Vary jointly" stays the rule; "exactly degenerate"
is withdrawn.
*Labelled comparisons (not campaign values):* scissor gap 1.12 eV → 0.319 MeV; 1.11 eV at 840 km/s → 0.283 MeV (EXCEED-DM's 0.28); Ge 0.67 eV → 0.191;
2311.04957 conventions → 0.358 MeV (C7). Annual v_max ∈ [781, 810] km/s moves every edge by ±3.6% (Si floor 0.320–0.344 MeV), a halo-band entry.

**(3.2) Two regimes of η [D]** (STANDS WITH CORRECTION, A-13, B-9; C4b–d). For the adopted halo every v_min > v_esc − v_E^ref = 293.5 km/s lies on
the second branch η₂; v1's regime-A interval is empty (C4c). With δ_v ≡ v_max − v_min,

  η = π v_esc e^{−v_esc²/v₀²} δ_v² [1 + δ_v/δ_v,× + O(δ_v²)]/(v_E N_esc),   δ_v,× = 3v_escv₀²/(2v_esc² − v₀²) = 173 km/s.            (3.2)

- *Regime A, δ_v ≳ δ_v,× (v_min ≲ 620 km/s):* η ∝ e^{−(v_min − v_E)²/v₀²} roughly; log-sensitivities per km/s at v_min = 600: 0.018 (v₀), 0.0027
  (v_esc), 0.0125 (v_E).
- *Regime B, δ_v ≪ δ_v,×:* a **power law in δ_v** times a fixed exponential. ∂ln η/∂v_esc = 0.047 per km/s at v_min = 760 (δ_v = 34.5): the leading
  2/δ_v = 0.058 is reduced mainly by the prefactor term −2v_esc/v₀² = −0.019 (B-9; C16), not by the O(δ_v/δ_v,×) term as v2 said. Finite shifts must
  use the exact η₂, or (δ_v′/δ_v)^{2+k_tail} times the change of the prefactor; the exact factors are the (V4) table.

**(3.3) Near-threshold rate [D]** (STANDS WITH CORRECTION, A-14, B-10; C5, C19). Hypotheses: regime B; S̄(|q|,ω) ∝ (ω − E_th(|q|))^{p̄_on}; the
maximum over q of G(q) ≡ ω_kin(q) − E_th(q), ω_kin = qv_max − q²/2m_χ, is a smooth (quadratic) contact. With v_max − v_min = (ω_kin − ω)/q,

  ∫dω (ω − E_th)^{p̄}(ω_kin − ω)^{2+k_tail} = B(p̄ + 1, 3 + k_tail)·G(q)^{p̄+3+k_tail},   G ≈ ε − c(q − q₀)²,  ε ∝ δ_v,0,

  ℛ(m_χ) ∝ δ_v,0^{7/2 + k_tail + p̄_on},   δ_v,0 ≡ v_max − √(2E_th/m_χ) (or its (3.1′) analogue),   ∂ln ℛ/∂ln v_max = (7/2 + k_tail + p̄_on)v_max/δ_v,0.   (3.3)

This needs no smoothness of E_th(q) beyond a smooth contact (A-D2, B-E2). Exceptions [D] (C19):
- **corner contact** (a V-shaped onset at the contact point, G ≈ ε − s_±|q − q₀|): ℛ ∝ δ_v,0^{4 + k_tail + p̄_on};
- **bound-exciton lines** (the §5.2 ladder (ii)): at fixed q a δ-line (p_on = −1). If the line energy has an isolated 3-D minimum (cubic crystals),
  S̄ has a step (p̄ = 0; WP1-v3 [E10]) and ℛ ∝ δ_v,0^{7/2+k_tail}; the Si G = 0 1s line enters S̄ with p̄ = 1 (forbidden on the axis), δ_v,0^{9/2+k_tail};
  only an isotropic line dispersion (minimum on a sphere) gives REF-A's δ_v,0^{5/2+k_tail} (Rebuttal R-A1, §12).
**Validity window** (B-E3; C20): the power law needs ω_max − E_th = E_th·2δ_v,0/v_max (first order) inside the range where S̄ ∝ (ω − E_th)^{p̄} holds,
≈ 10–60 meV (PAER, phonon energies) or ≈ E_x^b = 14.7 meV (excitons): δ_v,0/v_max ≲ 0.4–2.5%, i.e. **Δm_χ/m_min ≲ 1–5%** above the edge. "Controls the
lowest-mass part of every ER curve" is restricted to this window.
**Onset exponents (WP3-v3 §M3 final table, IF-5; replaces v2's bullets; "Si TA 4" withdrawn and not used):**
| target, branch | S̄ p̄_on | edge exponent 7/2 + k_tail + p̄_on | role |
|---|---|---|---|
| Si TA (G′ = 0) | 3 | 13/2 + k_tail | **the Si PAER edge** (smooth interior contact at \|q\| ≈ 0.9 keV) |
| Si LA kink (G′ = 0) | 4 | 15/2 + k_tail | kink above the edge (LA forbidden on the axis) |
| Si TO, LO kinks (G′ = 0) | 3 | 13/2 + k_tail | kinks |
| Si (2̄00) class, \|q\| > 2.28 keV | 3 (TA, TO, LA); 4 (LO on axis) | 13/2 / 15/2 | not at the edge |
| Ge, all branches | 3 | 13/2 + k_tail | Ge PAER edge |
| exciton replicas (W.14) | 3/2 (Si LA 5/2) | 5 + k_tail (6) | lowered by E_x^b |
| shells d_K < Q_w (Q_w = 0.33 Å⁻¹ at δ₀ = 0.3 eV) | none | — | mixed window + DC (O4 d11) |
At the Si edge (m_χ ≈ 0.333–0.337 MeV) the contact is at |Q*| ≈ 0.53 Å⁻¹, far from the pocket shell, so the exponent is 13/2 + k_tail for the continuum
and 5 + k_tail for the exciton replica (B-10). The fixed-q onset at |q| ≈ |𝐊_pk| is kinematically out of reach below ≈ 0.37 MeV and never sets δ_v,0
at the edge. At T > 0 an absorption branch opens ω_{Qν} lower, weighted by n_{Qν}. The choice between cases is a type-Δ nuisance (§5.2).

**(3.4) Smooth truncations [D]** (STANDS, A-14, B-10; C5c). Hypothesis: near the escape boundary f_χ ∝ (v_esc − |v + v_E|)^{k_tail} (King/Lisanti-type
forms, 1010.4300 [ABS]; attribution [E]). The region |v| ≥ v_min inside the escape sphere is a lens of depth δ_v; with ϱ the distance from the
axis and a_lens ≡ 1/(2v_esc) − 1/(2v_max) (leading order; exactly 1/(2v_esc) − 1/(2v_min), B-E4),

  η ∝ ∫2πϱ dϱ (δ_v − a_lensϱ²)^{k_tail+1}/(k_tail + 1) = π δ_v^{k_tail+2}/(a_lens(k_tail + 1)(k_tail + 2)),                          (3.4)

valid for δ_v ≪ v_E, v_esc; k_tail = 0 reproduces (3.2). **Degeneracy qualifier** (A-D2): dℛ/dω ∝ (ω − E_th)^{p̄}(ω_max − ω)^{5/2+k_tail}, so p̄_on
and k_tail enter the ω-shape differently; they are degenerate only for the edge rate integrated over a bin wider than ω_max − E_th ∝ δ_v,0, which is
always the case with ε_eh ≈ 3.75 eV bins. A null result in such a bin constrains only k_tail + p̄_on (the content of G8's "50%–×10" claim).

**(3.5) Size of the edge nuisances for Si [E]** (corrected, A-B3, B-9; C17).
- v_esc: 528⁺²⁴₋₂₅ (2011.12896, UNRESOLVED in R7) and 600 (QROCODILE/QEdark) vs 544: δ ln v_max = −2.0% (528), −5.3% (503), +6.8% (600; +7.0% as a fraction),
  i.e. **2–7%**, so 4–14% in m_min.
- Annual v_E(t): v_max ±1.8%, m_min ±3.6% (halo band).
- E_th from the step-model convention (WP6-D5): **2.5%** against the campaign default 1.170 eV (1.2/1.17); the 7% of v2 is 1.2 vs 1.12, a labelled comparison.
- Clamped versus ZPR-renormalised gap: Si ZPR ≈ −60 meV (≈ 5%) if the code is not scissored to the measured E_g(T).
- Operating temperature: E_g(130 K) − E_g(0) ≈ −10 meV (≈ 1%).
- q-dependent onset: the PAER edge sits 0–1.2% above the floor (0.333–0.337 MeV, (3.1′)), comparable to the halo band.

---
## 4. G8: halo-independent ER analysis in the URF

**(4.1) Formula [D]** (STANDS, B-11). Hypothesis (I) and (1.7). With η̃ ≡ (ρ_χσ̄_e/m_χ)η = Σ_j η̃_jΘ(v_j − |u|), (1.3) gives
ξ̃ = Σ_j η̃_j(v_j² − u²)Θ(v_j − |u|) (C14), and

  μ_i(m_χ, η̃, θ) = Σ_j 𝒜_ij(m_χ; θ) η̃_j,
  𝒜_ij = 𝔈_i (4π²ρ_T)^{-1} ∫dω ∫q dq Σ_Λ [A^{(0)}(q,ω;Λ,θ) + A^{(2)}(q,ω;Λ,θ)(v_j² − v_min²)] P(i|Λ;θ) Θ(v_j − |v_min(q,ω)|),       (4.1)

A^{(n)}(q,ω;Λ) as (1.4) with S̄_ab → S̄_ab(q,ω;Λ), per unit σ̄_e. It generalises 2311.04957 Eqs. (19)–(20) to all operator classes, any library
response, the operator-resolved seeding of WP0-v3 (7.3), the theory nuisances θ, and exothermic DM (|v_min|).

**(4.2) The bound and its hypotheses [D]** (STANDS WITH CORRECTION, A-16, B-12; C21).
*Hypothesis (P):* for every bin i, Σ_Λ A^{(0)}(q,ω;Λ)P(i|Λ) ≥ 0 and Σ_Λ A^{(2)}(q,ω;Λ)P(i|Λ) ≥ 0 pointwise in (q,ω). By (1.4) (positivity paragraph)
(P) holds wherever Σ_Λ S̄(Λ)P(i|Λ) is PSD. **Sufficient conditions** (B-D2): (i) inside the window (every Λ-sector PSD); (ii) where P(i|·) is
taken Λ-independent (the O4 d11 rule in the edge shell); (iii) where X0 and X+ of the same pair are seeded with a common P (summed per Λ₀).
Outside these, (P) is an assumption: under DC the X0 seed (Λ₀, n_ph = 0) and the X+ seed (Λ₊, n_ph = 1) differ in electronic energy by ω_Q ≤ ω_max
≈ 60 meV, so a step or thresholded cascade gives P(i|X0) ≠ P(i|X+) whenever a jump lies within ω_max: Σ_ΛPS = P_{X0}S_tot + (P_{X+} − P_{X0})S_{X+}, and
the DC part of S_{X+} (Hadamard finite part) can be negative. The affected fraction is O(ω_Q/ε_eh) ≈ 1–2% of pairs in Si (all pairs in the lowest bin
near E_g), **sign unbounded** (A-C2 = P′, B-D2). v2's "proof of sufficiency" restated the hypothesis and is withdrawn.
*Monotone step column (replaces "because 𝒜 ≥ 0").* Write a non-increasing η̃ ≥ 0 as η̃(u) = ∫Θ(v − |u|)dν(v), ν ≥ 0, so μ_i = ∫𝒜_i(v)dν(v) with
𝒜_i(v) the single-step column. The constraint η̃(u₀) = h is ν([u₀, ∞)) = h, hence μ_i ≥ h·inf_{v≥u₀}𝒜_i(v). For a single u₀ this equals h·𝒜_i(u₀) **iff 𝒜_i(u₀) ≤ 𝒜_i(v) for all
v ≥ u₀**; the bound holds **at every u₀ simultaneously iff 𝒜_i(v) is non-decreasing on [0, v_max]**, which is what the gate tests (R9, VER-A N4);
𝒜_ij ≥ 0 alone is not enough (C21 counterexample). Under (P),

  d𝒜_i/dv = 𝔈_i(4π²ρ_T)^{-1}∫dω∫q dq Σ_ΛP(i|Λ)[A^{(0)}δ(v − |v_min|) + 2vA^{(2)}Θ(v − |v_min|)] ≥ 0,

so the column is non-decreasing and

  η̃(u₀) ≤ min_i N_i^up(θ)/𝒜_i(u₀; m_χ, θ)   for every u₀.                                                                          (4.2)

This is the ER/URF form of the NR construction of 1111.0292 [ABS]. **Weaker exact condition and gate** (A-C2(ii)–(iii)): (4.2) needs only that
𝒜_i(v_j) be non-decreasing in j on the library grid; the `checks` group tests this for every bin, cascade model and m_χ (min_j[𝒜_i(v_{j+1}) − 𝒜_i(v_j)] ≥ 0),
and, as a diagnostic, the integrated kernels K^{(n)}_i(u) ≡ ∫dω∫q dq Σ_ΛA^{(n)}P(i|Λ)δ(u − |v_min|) ≥ 0. A failure flags a (P) violation at the
O(ω_Q/ε_eh) level.
**CL of the combined object** (B-D3). min_i of per-bin 90% limits has coverage below 90% (trials). Bonferroni: per-bin limits at 1 − 0.1/N_bins give
P(any bin fails) ≤ 0.1, hence ≥ 90% coverage of (4.2) (C21). State which is used.
*Consequences.*
- *(a) Convexity* (FALLS in part, A-11, B-7). At fixed (m_χ, θ), −ln ℒ is convex in η̃ (μ linear in η̃, Poisson −ln ℒ convex in μ; this needs
  only μ + b > 0, not 𝒜 ≥ 0). Hence **every local minimum is global**, and μ̂_i = (𝒜η̃̂)_i is unique **on the bins with N_i > 0** (strict convexity there); on zero-count bins
  −ln ℒ is linear in μ_i and μ̂_i may vary along a face of the minimiser set (R9, VER-B NEW-3).
  **η̃̂ is unique only modulo ker 𝒜** (dim ≥ N_v − rank 𝒜 ≥ N_v − N_bins), the flat directions of 2311.04957 §2.4. v2's "the η̃ profile is unique
  (as 2311.04957 states)" is **dropped**: the attribution is REFUTED (the paper says "any minimum … is a global minimum" [CONFIRMED quote]).
  Jointly in (η̃, θ) convexity fails: 𝒜(θ)η̃ is bilinear and M types are exponential in θ.
- *(b) Conservative bound:* (4.2), under (P) and the gate; without (P) (a truncated S with negative pieces, or a Λ split violating it) it is invalid.

**(4.3) Mass degeneracy [D]** (STANDS, B-13). rank 𝒜 ≤ number of populated bins; dim ker 𝒜 ≥ N_v − rank 𝒜. With 1–2 populated bins the kernel is at least
(N_v − 2)-dimensional and the edge degeneracy (3.4) makes m_χ undeterminable halo-independently (2311.04957 §3).

**(4.4) Computation specification** (B-19, A-C4; C29).
- *Inputs:* library S̄ and Λ-resolved A^{(0)}, A^{(2)} per operator class (§7.1); P_casc(N_eh|Λ) (WP5); P_det(i|N_eh), 𝔈_i; templates Δ^τ_k (§5).
- *Grid:* v_j at 10 km/s over 0–1000 km/s (N_v = 100); q, ω on the library grid.
- *Cost:* direct contraction N_bins × N_v × N_q × N_ω × N_Λ ≈ 7.5×10⁹ per (m_χ, θ). Because Θ(v_j − |v_min|) is cumulative, sorting the (q,ω,Λ) cells by
  |v_min| and taking prefix sums gives every column at once: ≈ 7.5×10⁷ per evaluation. **Profiling with M types** needs a fresh contraction per
  θ evaluation (𝒜 is non-linear in θ): with K nuisances ~10²–10³ evaluations, i.e. ≈ 10¹⁰–10¹¹ operations per m_χ with prefix sums (10¹²–10¹³ without).
  "∂𝒜/∂θ_k from the same contraction" is only the linearisation at θ = 0; a second-order expansion about θ̂ (∂𝒜, ∂²𝒜 stored) is the cheap
  alternative, with its error stated.
- *Outputs:* η̃_max(u₀; m_χ) with theory band and stated CL; the μ̂ fit and its η̃ flat directions (SVD, 2311.04957 Eqs. (21)–(24)); compatibility
  p-values for experiment pairs with shared θ; the monotonicity gate result.

**(4.5) Exact remaining gap (G8′)** (STANDS). For anisotropic targets beyond (I) (daily modulation, non-cubic or thin-film, P,T-broken), the
halo object is f̂^{(0)}(q̂,u,t), with no scalar monotonicity, so (4.2) does not apply; only its ℓ = 0 projection reduces to η. A conservative bound
needs a convex characterisation of the Radon transforms of non-negative f_χ with |v| ≤ v_max: a moment problem, not derived here [OPEN].

---
## 5. Nuisance structure for every approximation level (G4, part 1)

**(5.1) Parametrisation [D]** (STANDS for scalars, A-17; corrected for matrices and A, B-14). For each active truncation k, Δ^τ_k = S^{τ+e_k} − S^τ:
- *(M) multiplicative, log-normal,* **on scalar responses**: s(θ) = s^τΠ_k(1 + r^M_k)^{θ_k}, θ_k ~ 𝒩(0,1), with s = S_ee or a contracted A^{(n)} per
  operator class (r^M_k = Δs/s^τ). Positive for all θ. **On the matrix S_ab**, elementwise powers are not PSD-preserving (C22: a 2×2 PSD pair
  leaves the cone at θ = 2) and r_ab is undefined where S^τ_ab = 0. For matrices use the **PSD geodesic**
  S_ab(θ) = S^{τ½}(S^{τ−½}S^{τ+e_k}S^{τ−½})^θS^{τ½}, PSD for all θ, equal to S^τ, S^{τ+e_k} at θ = 0, 1 (C22), with pseudo-inverses on ker S^τ and
  supp S^{τ+e_k} ⊆ supp S^τ (otherwise the truncation is support-opening: type A).
- *(A) additive, support-opening:* S = S^τ + a^A_kΔ^τ_k, a^A_k > 0 log-normal; central value includes Δ^τ_k once computed. **PSD for all a > 0 iff
  Δ^τ_k is PSD** (C23): true for the in-window sideband and for new exciton lines; false outside the window, where the DC X+ part (Hadamard finite
  part, PV pieces) is not PSD (WP0-v3 §6.2(i)), and for increments that carry their own ZPL-loss compensation. There a^A_k acts on X0 + X+ jointly, or
  is restricted to the window (this interacts with (P), §4.2).
- *(E) energy shift:* S(q, ω − θ_Eσ_E); shifts 𝓜¹ by θ_Eσ_E∫S.
- *(Δ) discrete* model choices: discrete profiling (1408.6865 [ABS]) or envelope.
- *(L) affine, support-restricted* (new name for the v2 (5.1′) form; A-E(ii)): S^τ + Σθ_kX_k with θ_k ~ 𝒩(0,1) and the support {S ≥ 0} imposed;
  **the only type that is not PSD by construction**. It is kept only as the first-order linearisation of type T.
- *(T) exponentially tilted* (new, (5.1″)): PSD by construction and exact on linear moment constraints.
The v1 additive Gaussian is withdrawn (WP0-v3 (8.1)). One θ_k per truncation, coherent across (q,ω), bins, targets and experiments sharing the physics.

**(5.1′) Constrained truncations, first order (type L) [D]** (STANDS WITH CORRECTION, A-18, B-15; WP2-v3 (6.1), IF-4). At fixed q, E_R = q²/2M_κ,
y_R ≡ ω − E_R, the anharmonic increment of the self part obeys ∫Δ^τ_A = 0, ∫y_RΔ^τ_A = 0, and **∫y_R²Δ^τ_A = n_κ·2q²δE^kin_q̂/M_κ with
n_κ ≡ (2π/Ω)|c_κ|² = 2π𝓃_κ|c_κ|²** (WP2-v3 v3 normalisation; n_κ = 1 if Δ^τ_A is built from the normalised S_self/∫S_self). The M type satisfies them
only at θ_A ∈ {0, 1}, violation O(θ_A(1 − θ_A)(r^M_A)²) (C15b). The affine form

  S(θ_A, θ_δ) = S^τ + Δ^τ_A + θ_A Π_mom[Δ′_A] + θ_δ S^τ P_δ(y_R),   Π_mom[X] ≡ X − S^τ Σ_{b=0}^{2} c_b(X) y_R^b,   Σ_b 𝔪_{a+b} c_b = ∫y_R^a X  (a = 0, 1, 2),   (5.1′)

𝔪_n ≡ ∫y_R^nS^τdω (positive Hankel matrix, invertible for ≥ 3 support points), keeps all three constraints for every θ (C15a); P_δ is the quadratic with
∫y_R^aS^τP_δ = (0, 0, n_κ·2q²σ_δE/M_κ). Corrections (A-E, B-F4):
- **Support** (both): Π_mom[X] = X − S^τ × quadratic, so supp Π_mom[X] ⊆ supp X ∪ supp S^τ (only the subtracted part is ∝ S^τ). No new support iff
  supp Δ′_A ⊆ supp S^τ, a stated condition (true for the NR self part). v2's "Π_mom[X] ∝ S^τ × quadratic" is withdrawn.
- **Positivity** (A-E(i)): S is affine in (θ_A, θ_δ), so {S ≥ 0} is convex, but wherever S^τ dominates and y_R is large (impulse tails), the terms
  θ_δp₂y_R²S^τ and −θ_AS^τΣc_by_R^b force sign(θ_δ) = sign(p₂) (and generically a sign on θ_A). The admissible set is then a half-space and the
  𝒩(0,1) prior cannot be realised (profile on the boundary, non-standard asymptotics). C24 exhibits a negative bin at θ_δ = −4 (where type T stays positive with exact moments). Hence type L is
  only the linearisation; the nuisance used is (5.1″).
- **Typing** (A-E(ii)): v2 called this "type A"; it is type L.

**(5.1″) Exponentially tilted constrained nuisance (type T) [D]** (new; A-E remedy; C24). With S_c ≡ S^τ + Δ^τ_A (central, satisfying the constraints),
**ψ ≡ ln(1 + Δ′_A/S_c)** (requires supp Δ′_A ⊆ supp S_c and Δ′_A > −S_c; R9, VER-A N1: with v3's ψ = Δ′_A/S_c, θ_A = 1 reproduced S_c + Δ′_A only to
first order in Δ′_A/S_c, exponentially wrong in the tails) and φ(y_R) = (1, y_R, y_R²). The shape step is thus an M-type move to the template followed by
re-tilting: at θ_A = 1, S = (S_c + Δ′_A)e^{λ·φ}, i.e. one unit of θ_A is one template up to the moment re-projection (C24),

  S(θ_A, θ_δ) = S_c · exp[θ_Aψ + Σ_{b=0}^{2} λ_b(θ) y_R^b],   ∫y_R^a S(θ) dω = T_a(θ_δ) ≡ ∫y_R^aS_c + δ_{a2}θ_δ n_κ 2q²σ_δE/M_κ   (a = 0, 1, 2).   (5.1″)

- *Existence, uniqueness, smoothness:* λ(θ) minimises the strictly convex dual F(λ) = ∫S_ce^{θ_Aψ+λ·φ} − λ·T (Hessian = the moment matrix of φ under
  S(θ), positive definite for ≥ 3 support points). A unique minimiser exists iff T lies in the interior of the moment cone of supp S_c
  (R9, VER-A N2 = VER-B NEW-2). On a grid support [y_min, y_max] this is: T_0 > 0; y_min < ȳ ≡ T_1/T_0 < y_max; **0 < Var ≡ T_2/T_0 − ȳ² <
  (y_max − ȳ)(ȳ − y_min)**, i.e. T_2T_0 − T_1² > 0 **and** (y_min + y_max)T_1 − y_miny_maxT_0 − T_2 > 0 (variance below the endpoint maximum; C24). A
  negative θ_δ meets only the lower bound; a large positive θ_δ (or a narrow grid) can meet the upper one, so θ_δ is bounded on both sides, by bounds
  many σ out in practice (the prior is realisable to excellent approximation, not exactly). Smooth in θ by the implicit function theorem; λ(0) = 0.
- *Properties:* S(θ) ≥ 0 for every θ; constraints exact for every θ; no new support (supp S(θ) = supp S_c); θ_A, θ_δ ~ 𝒩(0,1) realisable inside
  the two moment-cone bounds above.
- *First order* (C24, exact): ∂S/∂θ_A|₀ = Π^{c}_mom[S_cψ] = Π^{c}_mom[Δ′_A] + O(Δ′_A²/S_c) and ∂S/∂θ_δ|₀ = S_cP_δ, where **Π^{c}_mom uses the moments of S_c**;
  (5.1′) defines Π_mom with the moments of S^τ, and the two differ at O(Δ^τ_A) (R9, VER-A N3). The type-L form used as the linearisation of (5.1″) is the
  one with Π^{c}_mom (moments of S_c).
- *Unbounded support:* raising the variance needs λ₂ > 0, integrable only if λ₂ is below the tail decay rate of S_c: with Gaussian tails
  e^{−y²/2σ²}, λ₂ < 1/(2σ²) (always attainable for small θ_δ); with power-law tails never, and the moments then depend on the grid cutoff (R9, N2). On the
  library grid the integrability condition is replaced by the endpoint bound above. Alternatively apply (5.1′) on a compact y_R window and state the truncation (A-E).
- Any other truncation with exact linear moment constraints (e.g. n_ph truncations against WP2 (3.4)) uses the same tilt.

**(5.2) Table.** Sizes [E] unless a source is given. Priors of log-normal types are stated as **median and log-width σ_ln** (68% range
[median·e^{−σ_ln}, median·e^{σ_ln}]; C25). "Central" is τ*. Cross-material correlation r_mat = 0 by default (1 as a variant).

| Level (τ slot) | Template Δ^τ_k | Type | Prior | Correlation | Source of Δ^τ_k |
|---|---|---|---|---|---|
| XC functional (ground state) | spread over {PBE+scissor, SCAN, HSE, G₀W₀ bands}: principal components of the covariance of ln s (scalars) | M (per PC, on scalars) + E (gap) | 𝒩(0,1) per PC; σ_E = 0 if scissored to measured E_g(T_op), else \|E_g^DFT − E_g^exp\| | material-wide; r_mat | ≥ 3 functional runs; Ge 3d misplaced by ≈ 4.5 eV (2306.14944) gets its own E-type nuisance on core weight |
| Kernel ladder 𝒳 | S^{𝒳+1} − S^𝒳, computed: central RPA+LFE, Δ = (BSE or TDDFT kernel) − (RPA+LFE). **Interim** (finite-q BSE uncomputed; WP1-v3 [E8], §5 item 2): (i) Sommerfeld continuum, factor ∈ [1.3, 2.0] for E_min(q) ≤ ω ≲ E_min(q) + 1 eV; (ii) bound-exciton lines below E_min(q), new support, template from [E8] with ab initio μ_x, ε_∞, ρ_cv; **Si second-class line amplitudes ÷3** (WP1-v3 IF-3: Elliott weight corrected) | (i) M on scalars; (ii) A (lines are PSD) | (i) **central s^τ × 1.61, σ_ln = 0.22** (encodes the 68% range [1.3, 2.0]; B-14 F3(a)); (ii) a^A_k median 1, σ_ln 0.5 [E] | material-wide | finite-q BSE (Yambo/BerkeleyGW, WP1); [E8]. ALDA few %; LFE −20…−50% (2603.12326 [ABS]) belongs in the central value |
| Screened operator rows | rows with R̃_ac ≠ 0 screened per WP0-v3 (5.3): n, j_L always; j_T via LFE (WP1-D4); **spin rows: triplet W^{scr} ladder + f_xc^T, R̃_s ≡ 4R_{s^zs^z}** (WP1-v3 IF-13) | central value; residual M on contracted scalars; spin rows: M with central × 1.61, σ_ln 0.22 within ~1 eV of the edge (×1.3–2, WP1-v3) | 𝒩(0,1) | material | WP1 |
| q_max / high-q cutoff | Θ(q − q_max)S_IA(q,ω), S_IA = Σ_sh 2π𝓃_e^{(sh)}(m_e/q)J^{(sh)}(p_z) (f-sum exact, C9) | added to central value; residual M on the tail | residual width E_B^{(sh)}/(q²/2m_e) per shell | material-wide | all-electron Compton profiles: **closed analytically** |
| k-grid / basis / PAW | difference of successive grids or bases | M (scalars) | half-normal (rate falls monotonically with k-density, 2105.05253 [ABS]) | run-specific | convergence pair |
| BO order n_B | κ_BO⁴ = m_e/M weight shift (WP0-v3 §6.2; remainder O(κ_BO^{2(n+1)}), G10) | M | 2×10⁻⁵ (Si); negligible | — | analytic |
| e–ph order n_g | n_g = 0 → 2: PAER sideband S^{X+} (A in the window, PSD there; onset exponents §3.3 table, WP3-v3 IF-5), ZPR shift (E), FC reduction e^{−2W} of the ZPL, 2W_κ = q·B_κ·q (M) | A + E + M | A: **interim pair-screening factor [0.4, 1.8] (WP3-v3 IF-10, multiplicative composition): median 0.85, σ_ln 0.75** (v2's [0.5, 1.2] had median 0.77, not 1); E: σ_E = \|ZPR\| ≈ 60 meV (Si) if unrenormalised; M: η_ep | material and T | EPW/ZG (WP3) |
| Screening channel (pair channel, external LFE in X+) | X2 classes; static DFPT error O(ω_Q²/E_g²) ≈ 3×10⁻³ with TR (WP0-v3 F11; O(ω_Q/E_g) for magnetic references) | M | inside the [0.4, 1.8] factor above | material | X2-N1…N4 |
| Anharmonic n_A | computed Δ^τ_A at amplitude 1 (central) + **type T (5.1″)** with shape ψ = ln(1 + Δ′_A/S_c) (R9) and the δE^kin term; WP2-v3 (6.1) with n_κ = (2π/Ω)\|c_κ\|² exact for all θ | T | θ_A ~ 𝒩(0,1) scaled by η_anh = 0.01–0.03 (T = 0); θ_δ ~ 𝒩(0,1) on σ_δE (0 if PIMD) | NR only; negligible for ER | WP2 (6.1), PIMD |
| Phonon order / regime K (NR) | truncation at n_ph ≤ N loses P[Pois(2W) ≥ N] of the f-sum per site; with several sites the \|c_κ\|²/M_κ-weighted mean, WP2-v3 (3.4″) (R9, AUDIT-2 m11) | M (one-sided) | that fraction | material | WP2 recursion |
| Thermal order n_T | S^{n_T+1} − S^{n_T}: phonon-absorption sideband ∝ n_{Qν} (TA at 130 K: n ≈ 0.25); t_g terms ∝ e^{−E_g/T} negligible; thermal factor applied once (WP3-v3 IF-11, EPW (64)) | A (sideband, PSD in window) or M | log-normal | per T | WP3 sideband |
| Temperature T (metadata) | E_g(T) shift (Varshni ≈ −1.5×10⁻⁴ eV/K at 130 K) and ∂ln S/∂T | E + M | σ_T ≈ 1 K | per experiment | analytic |
| Gap convention E_g(T) | E-type | E | σ_E: 1 meV if scissored to measured E_g(T_op); 60 meV if clamped and unscissored; WP6-D5 offset removed by convention | material-wide | measured E_g(T) |
| Edge construction (new) | q-dependent onset (3.1′): continuum vs exciton-replica PAER edge; ω_ν(Q*) from ab initio dispersion vs [E] | Δ + E | E: σ_E ≈ 2 meV on ω_TA(Q*) until computed | material-wide | WP3 S^{PA}, WP1 [E13] |
| Yield / cascade (WP5-v3 §8) | {step(ε_eh), R&K, URF cascade} until the URF cascade is computed, then: θ_seed (**no prior bound; computed**, WP5-v3 IF-R8-6), θ_{R-k} (computed), θ_GW (±20%), **θ_Z (0.8–1, global, M; new)**, θ_exch (computed, beyond first order), θ_PES, θ_LZ, θ_esc, **θ_dense ([C], unestimated; new)** | Δ (discrete) + M | ε_eh: 𝒩(3.75, 0.05) eV (Si, 130 K) [E]; (W4) ties θ_GW, θ_Z, θ_{R-k} to measured ε_eh, F_eh; (W13) ties η_pb | material-wide | WP5 (G1); R&K's tuned A is "non-physical" (2004.10709) |
| Fano term 𝔉 (cascade first step, O4 d7) | θ_𝔉: interference correction to P_casc(N_eh\|Λ) | A on P_casc (sign-free, Σ_ν𝔉_ν = 0) | **rigorous \|ΔP\| ≤ 2π max\|c^F\|; [E] ≲ 0.3 Γ/δ worst case, 0.11 Γ/δ optimistic central; GaAs Γ/δ map unknown** (WP5-v3 IF-R8-5); **0 for Si, Ge** | material (GaAs) | O4, WP5-v3 (W15)–(W17); export gated in §7.4 |
| Cascade band edge θ_Eg | ZPR band-edge shift in the cascade (L12) | E | σ_E as the gap row | shared with the response's gap nuisance (O4 d3) | WP5-v3 |
| Fano factor F_eh | width of P_casc(N_eh\|Λ) | M on the variance | F_eh = 0.119 ± 0.002 at 5.9 keV (2004.11499); near-gap prior uniform on [0.1, 0.2] [E] | material-wide | WP5 L23 |
| Superconducting targets (Al, WSi) (new) | L^{BCS} first-order screening term −2(Δ_BCS/qv_F)𝔰_BCS(y)𝔤_IL^{nor} (WP4-v3 [4.2′], I12): in the central value; residual M | M | ≤ 16% at y = 5, 4% at y = 10 (Al edge); Δ_BCS/v_Fq a first-order control parameter | material | WP4-v3; **no WSi factor quoted** (I13 withdrawn) |
| Halo | fixed nominal (2105.00599) in headline; band from (v₀, v_esc, v_E(t)) | separate object | v_esc 528⁺²⁴₋₂₅, v₀ 233 ± 6 (2011.12896, UNRESOLVED in R7); \|v_E(t)\| 237.4–266.4 km/s, v_max ∈ [781, 810] (C6) | all experiments | §6.3 |

**(5.3) Sum-rule constraints [D]** (STANDS WITH CORRECTION, B-16). The f-sum ∫_{−∞}^{∞}dω ωS = π𝓃_eq²/m_e (densities with inversion; ω < 0 included at
T > 0; WP0-v3 (4.6)), times the relativistic factor for all-electron tables: **≈ −0.23% Si, −0.73% Ge** with the Breit orbit–orbit term (WP0-v3 (4.6″),
G4 [E]; v2: −0.18%/−0.58%, mass-velocity only). It informs only **non-conserving** truncations: q/band cutoffs (closed by S_IA), non-local
pseudopotentials, a sideband without its Fan/vertex compensation, **and non-local quasiparticle rungs: the scissor of the central τ* (PBE + scissor
violates the f-sum by +Δ_scisΣ|ρ|² ≈ +3.5% in Si, WP1-v3 [E]) and BSE on GW or scissored bands ([H_QP, n] ≠ q·j)**. So the f-sum is informative for
exactly the rungs adopted, not vacuous. Rungs with local potentials are conserving, ∫ωΔ^τ_𝒳 = 0 (WP6-W3). Positivity is automatic for M on scalars,
for the PSD geodesic, for A with PSD Δ, and for T; **not** for M elementwise on S_ab, for A with non-PSD Δ, or for L. L17 (WP0-v3 (9.6)) gives a hard
upper limit on ∫ω^nS(θ), used as a support restriction on θ (not a prior), **only where its static step 1 − ε_ch^{-1}(q,0) ≤ 1 holds: ch = c, or
clamped ch = e; for electron-only coupling with a relaxed lattice it fails (×2.30 GaAs-like) and the computed ε_e is used instead** (WP0-v3 G6).

---
## 6. Statistical treatment and combination (G4, part 2)

**(6.1) Likelihood [D as a definition]** (= WP0-v3 (8.3)). Experiments ex, bins i, signal strength σ̄_e, theory θ, detector nuisances θ^det_ex:

  ℒ(σ̄_e, θ, θ^det | m_χ) = Π_ex Π_i Pois(N^obs_{ex,i} | σ̄_e s_{ex,i}(m_χ; θ, θ^det_ex) + b_{ex,i}(θ^det_ex)) · Π_k π_k(θ_k) · Π_ex π(θ^det_ex).   (6.1)

s_{ex,i} = μ_i of (1.7) per unit σ̄_e, halo fixed. Test statistic: two-sided profile-likelihood ratio with toy MC rather than asymptotics, and a
power-constrained limit at −1σ. The attribution of this recipe to 2105.00599 §2 is **UNRESOLVED** (REF-A did not fetch it); the recipe is adopted
as a campaign convention independent of the attribution.

**(6.2) Profile, envelope and Bayesian treatments differ at different orders [D]** (STANDS WITH CORRECTION, A-19, B-17; C8). Zero-count bin, b = 0,
asymptotic −2ln ℒ = 2sμ(θ) + θ², limit at −2Δln ℒ = 2.71, one theory nuisance of fractional size **δ_θ** (renamed from δ, which is the window detuning):
- *Linear μ = 1 + θδ_θ:* θ̂ = −sδ_θ, ratio 2(1 − √(1 − 2.71δ_θ²))/(2.71δ_θ²) = 1 + (2.71/4)δ_θ² + O(δ_θ⁴); 1.276 at δ_θ = 0.5; **no limit for δ_θ > 2.71^{−1/2}
  = 0.607** (the profile drives μ to zero).
- *Log-normal μ = (1 + δ_θ)^θ (M):* with k_δ ≡ ln(1 + δ_θ), θ̂k_δ = −w_δ, **w_δ = √(1 + 2.71k_δ²) − 1, the positive root of w² + 2w − 2.71k_δ² = 0**
  (v2's "Lambert-W"/W_Lam was a misnomer), ratio 2w_δe^{w_δ}/(2.71k_δ²) = 1.006, 1.047, 1.112 at δ_θ = 0.1, 0.3, 0.5; series 1 + (2.71/4)δ_θ² + O(δ_θ³).
- *Envelope* (worst case |θ| ≤ 1), **of the same type**: linear 1/(1 − δ_θ) = 1.11, 1.43, 2.0; M type (1 + δ_θ) = 1.1, 1.3, 1.5.
**Profiling costs O(δ_θ²); the envelope costs O(δ_θ).** Like for like at δ_θ = 0.5 the envelope/profile ratio is **×1.35 (M type, 1.5/1.112)** and
**×1.57 (linear, 2.0/1.276)**. v2's "up to ×1.8 (2.0/1.112)" divided a linear envelope by a log-normal profile and is withdrawn here, in §8 and in
WP0-v3 (8.3) (already applied there, G7). A Bayesian marginal with π_k = 𝒩 behaves like the profile at small δ_θ [E]. The choice is a convention
and must be declared (WP6-W4).

**(6.3) Recommendation: report three objects [D as a protocol]** (STANDS, A-20, B-18; = WP0-v3 (8.3)).
- **WP6-R1** nominal limit: θ = 0, central τ*, halo fixed to 2105.00599 (v_E(t) averaged over the exposure).
- **WP6-R2** theory-profiled limit: θ profiled with the §5.2 priors (M on scalars, T, A with PSD Δ). Headline.
- **WP6-R3** bands: the theory envelope over |θ_k| ≤ 1 of the same types (one at a time and in quadrature) around R1; a separate halo band
  (v₀, v_esc, the annual |v_E(t)| range, v_max ∈ [781, 810] km/s, the 252.1 km/s variant); the halo-independent bound (4.2) with its CL.
By (3.1′), E_th(·) and v_max are varied together in R3.

**(6.4) Combining experiments that used different codes and conventions [D].**
- *Step 1, common response.* Recompute each s_{ex,i} from the library at one τ* and version. Code differences (SENSEI: QEdark; DAMIC-M: QCDark + MTF;
  CDEX: EXCEED-DM) become θ-values at matched τ; the residual is a numerical nuisance; WP6-D5-type convention offsets are removed, not profiled.
- *Step 2, shared θ.* Common to every experiment on the same material; across materials the r_mat option.
- *Step 3, conventions.* ρ_χ → 0.3 (linear); fixed halo; one E_th convention (measured E_g(T_op) at each T) with the (3.1′) edge.
- *Step 4, the likelihood product* (6.1) = 2311.04957 Eq. (15) with θ shared.
- *Recast if only limits are public* (qualified, A-G, B-18). σ̄_e^{up,lib}(m_χ) = min_i N_i^up/s_i^lib(m_χ) is exact **only for a limit defined as the
  minimum over per-bin limits**, whose coverage is below the per-bin CL unless a trials (e.g. Bonferroni) correction is applied (§4.2); it is not a
  recast of a combined-bin CL. Single bin: σ̄_e^{up,C}s^C/s^lib. Optimum-interval and PLR analyses cannot be recast exactly without the binned likelihood.

**(6.5) Minimum publication standard [D: minimal sufficient set for (6.1)].** Per bin: N^obs_i, b_i with covariance, 𝔈_i; P_det(i|N_eh) with its θ^det
dependence; per-bin N_i^up and the CL convention of any combined limit; library version, τ* string + metadata and θ̂; the halo convention; the full
likelihood in machine-readable form (pyhf/HEPData-style JSON).

---
## 7. The shared, versioned response library (G4, part 3)

**(7.1) Content and axes [D as a specification]** (STANDS, A-20; with B-19 and WP1-v3 IF-10). One container per (material, T, τ, version):

| Dataset | Axes (shape) | Units / normalisation | Notes |
|---|---|---|---|
| `S_iso/ee` | q (N_q), ω (N_ω) | ΩS̄_ee [eV⁻¹], spin included, T as labelled | L24/L1–L3 workhorse; → \|f_crys\|², \|f_res\|², L by (1.6) |
| `S_iso/ab` | a, b (16×16 per species, Hermitian, upper triangle), q, ω | same; **orientation average (1.3a)** | WP0-v3 basis (2.2), screened per WP0-v3 (5.3); minimal form **12 real functions (Si/Ge), 18 (general, fixed q̂) + R⁰_{GG′}** (WP1-v3 IF-10; v2: 7); Im/antisymmetric parts are PT-zero diagnostics in Si/Ge; A^{(0)}, A^{(2)} of (1.4) by contraction with 𝔇 (Σ𝔇_abS_ab = tr[𝔇ᵀS], G1); tr S_{j_Tj_T} = Σ_λ(2ω²/e²)Im ε_{T,λ} off the 3-/4-fold axes (WP1-v3 IF-15) |
| `S_aniso/ee` | invariant-harmonic index (7 for O_h up to ℓ = 12; C11), q, ω | coefficients of G_eff-invariant harmonics | L19, daily modulation; other groups by the Molien series; odd-ℓ blocks (lowest odd ℓ of G_eff, C28) mandatory for P,T-broken targets (density odd part O(q³), WP4-v3 [3.2′]) |
| `S_aniso/NN` | ℓ, m, q, ω | WP2 S_ℓm | NR anisotropy (WP2 G11) |
| `eps` | G, G′ (small), q, ω | ε_{GG′}(q,ω), ε_e; ε(q,0) | screening (WP0-v3 (5.2)–(5.5)), L17 diagnostics (G6 domain) |
| `S_Lambda/<class>` | Λ-marginals ((E_e, E_h) coarse grid, n_ph, ω_ph), q, ω | ΩA^{(0)}(q,ω;Λ), ΩA^{(2)}(q,ω;Λ) per 𝒪_i class, and ΩS_ee(q,ω;Λ) | WP0-v3 (7.1)–(7.3) hand-off to WP5; no plasmon label within RPA; retarded out-state LFE weight; conv ∈ {window, DC} declared |
| `P_casc/<model>` | N_eh (≤ 20), Λ-marginal | probability | per cascade model, with F_eh, ε_eh metadata and the WP5-v3 §8 θ's |
| `Delta/<k>` | as the S it modifies | same, plus type ∈ {M (scalar or geodesic), A, E, Δ, T}, prior (median, σ_ln), correlation group | the §5 templates |
| `checks` | q; bins | ratios, flags | f-sum fraction (relativistic factor (4.6″)); min eigenvalue of S_ab; KK residual; detailed balance; L17 saturation (G6 domain); convergence deltas; O4 d1–d11 status; **monotonicity gate min_j[𝒜_i(v_{j+1}) − 𝒜_i(v_j)] ≥ 0 per bin and cascade model, and K^{(n)}_i ≥ 0 diagnostics (§4.2)** |
| `derived/A` | bin set, m_χ, v_j | 𝒜_ij of (4.1), by prefix sums | halo-independent analyses without rerunning |
| `derived/edge` | — | E_th(q) along the minimising path, (3.1′) m_min per channel (continuum, exciton replica, ZPL classes), p̄_on, ZPR | edge parameters of (3.1′), (3.3) |

**(7.2) Grids [E].**
- q: 0.1–30 αm_e (0.37–112 keV), N_q ≈ 300, log-spaced below 2αm_e and linear above; covers q ≈ 0.9 keV (Si PAER edge) and 25 αm_e (2603.12326).
- ω: 0–100 eV; Δω = 10 meV within 5 eV of E_g, 50 meV above; N_ω ≈ 2.5×10³. **Within 60 meV of each edge a 1 meV sub-grid** is needed to resolve the
  power-law window of (3.3) (Δm/m ≲ 1–5%).
- T ∈ {0, 0.05, 4, 77, 130, 300} K as needed.
- *Sizes:* S_iso/ee ≈ 6 MB; full 16×16 ≈ 1.5 GB per species; anisotropic ×7; each Delta set the size of its parent.

**(7.3) Provenance and versioning [D as a specification].**
- *Content addressing:* SHA-256 of every array and a PROV-style parent list (CIF, pseudopotential/basis hashes, code and commit, run cards).
- *Mandatory metadata:* the τ string in CONVENTIONS §11 slot order, **n_T a thermal order, never a temperature** (C13; WP0-v3 F9), e.g.
  `nB=0|ng=0|nA=0|X=RPA+LFE|nT=0|K=-|Mg=-|nD=-` with `T=130K;ref=normal;scr=ext,LFE;conv=window`; functional and scissor shift; k-grid, cutoffs,
  q_max, band count; convention flags (q from DM to target; spin included; per cell; units; CODATA; S_ab ordering and the tr[𝔇ᵀS] contraction);
  O4 d2, d3, d8, d9 hashes for every S_Lambda/P_casc pair; the checks summary.
- *Semantic versioning:* MAJOR for any change of τ* or convention; MINOR for added tables; PATCH for numerical refinement. Old versions immutable,
  DOI-minted.

**(7.4) Library build.** Per material: the central run τ* and one run per active truncation (about 6–9 runs). Codes: QE/VASP + Yambo/BerkeleyGW
(WP1); QCDark2/EXCEED-DM-type all-electron reconstruction (G7); EPW/ZG for X+ and ZPR (WP3); WP2 recursion; WP5 cascade. Cost: WP1–WP3 runs dominate;
assembly, checks and derived 𝒜 (prefix sums) take under 1 CPU-hour per material [E]; profiling cost per (4.4). *Validation gates:* f-sum within 2%
below the band cutoff (after the scissor correction of (5.3)); min eigenvalue ≥ −10⁻⁶ of the trace; KK residual < 1%; NIXS/EELS agreement where data
exist; O4 d1–d11; d7 (𝔉 export) mandatory for non-PT targets; **the (4.2) monotonicity gate**.

**(7.5) G4 status.** The fix is (5.1)–(5.3), (6.1)–(6.5) and the library (7.1)–(7.4). Exact remaining gaps: (i) prior widths of uncomputed truncations
are conventions; (ii) r_mat is not derivable; (iii) discrete yield models need discrete profiling until the URF cascade is computed; (iv) the combination
needs experiments to publish (6.5); (v) (P) outside its sufficient conditions is an assumption at the O(ω_Q/ε_eh) level, policed by the gate.

---
## 8. Summary of new content (v3 status)
- (1.2) General halo functional; (1.3) ξ = 2∫_{|u|}u′η du′ under (I) with the orientation average (1.3a), any f_χ, either sign of v_min.
- (1.5) Invariant harmonics of G_eff: ℓ = 4 first if P or T holds (all odd ℓ vanish); otherwise the lowest odd ℓ of G_eff (never ℓ = 1 for cubic
  groups; density odd part O(q³)); the day average keeps every zonal projection.
- (3.1′)–(3.4) **The edge is min_q q²/[2(qv_max − E_th(q))], and near it the rate is a power law δ_v,0^{7/2+k_tail+p̄_on}** (corner: 4 + k + p;
  bound lines 7/2 + k in cubic S̄), valid within Δm/m ≲ 1–5%; Si PAER edge ≈ 0.333–0.337 MeV, Ge ≈ 0.213–0.214 MeV [E]; halo and gap must be varied
  jointly (degenerate in position to ~1%, not in amplitude).
- (4.1)–(4.2) Halo-independent bound proved by the monotone step column under (P); (P)'s sufficient conditions, leakage and library gate; CL stated.
- (5.1)–(5.1″) Positivity-preserving nuisance algebra: M on scalars or the PSD geodesic, A on PSD increments, E, Δ, and the exponentially tilted
  type T that keeps exact linear constraints; type L only as its linearisation.
- (6.2) Profile vs envelope: O(δ_θ²) vs O(δ_θ); like for like ×1.35 (M) / ×1.57 (linear).
- (7) Library schema with the monotonicity gate and per-channel edges.

---
## 9. WP0 defects reported in v1 (record; all applied in WP0-v2/v3)
WP6-W1 (f-sum π not 2π), W2 (additive Gaussian positivity), W3 (f-sum vacuous for conserving truncations; now qualified by (5.3): non-local rungs are
informative), W4 (envelope vs profile; number corrected to ×1.35/×1.57), W5 (hypothesis (I)), N1 (v_E, ρ_χ). → WP0-v3 (4.6), (8.1)–(8.3), (9.1);
CONVENTIONS §8, §13.

## 10. Literature (statuses after the R7 full-text checks)
- **CONFIRMED** (REF-WP6-A and/or B, full text): 1509.01598 Eqs. (15)–(17), (21) = (64), (65)–(68) (with the D4 typos), App. B values;
  2311.04957 Eqs. (3)–(4), (7), (9)–(13), (19)–(20), §2.1–§2.4 (including the quote "any minimum … is a global minimum"), §3 values, E_gap = 1.2 eV, ε = 3.8 eV.
- **REFUTED and dropped:** "the η̃ profile is unique (as 2311.04957 states)" (v2 (4.2a)).
- **UNRESOLVED** (not checked in R7): 2105.00599 §2 (two-sided PLR + PCL at −1σ) and §3.1 (fixed, not profiled), Eq. (11) values; 2011.12896 (v_esc,
  v₀ bands); WP6-D1's "absorbs the target size" sentence ([E]); 2101.08275 Eq. (16) (verified algebraically, C2, not re-read).
- [ABS] (unchanged, context only): hep-ph/0209110, 1111.0292, 1408.6865, 1010.4300, 2004.10709, 2004.11499, 2105.05253, 2306.14944, 2603.12326, 2411.03433.
  [FT via WP1] 2607.06005.
- Via owner returns: WP0-v3 (G1, G4, G6, G7, G10, G12); WP1-v3 [E4], [E8], [E10], [E13], [E14]; WP2-v3 (6.1); WP3-v3 §M3, IF-5, IF-8, IF-10, IF-11;
  WP4-v3 [3.2′], [4.2′]; WP5-v3 §8, (W15)–(W17); O4 d1–d11.

## 11. Open items handed on (OW6-n)
- OW6-1: G8′ (4.5), the moment-problem characterisation of Radon transforms (open).
- OW6-2: p̄_on: **supplied** (WP3-v3 §M3 final table; WP1-v3 [E10]); remaining: ab initio ω_ν(Q*) along the minimising path for the edge values (3.1′).
- OW6-3: continuous P_casc(N_eh|Λ; θ): specified by WP5-v3 §8; the URF cascade computation is open.
- OW6-4: r_mat and the profile-vs-envelope convention at synthesis (M4).
- OW6-6: (P) — **resolved as a hypothesis** with sufficient conditions and a library gate (§4.2); the size of the O(ω_Q/ε_eh) leakage is open.
- OW6-7 (new): ab initio E_min(q), E^{ZP}(q) and ω_ν(Q) for Si/Ge to replace the [E] edges and the M1 window of (3.1′).

---
## 12. Rebuttals and referee disagreements

**Rebuttals (go back to the named referee).**
- **R-A1 (to REF-WP6-A, §D3: "bound-exciton lines have p_on = −1 and edge exponent 5/2 + k_tail").** Applied with a correction. At fixed q a bound line is
  δ(ω − E_l(q)) (p_on = −1), but the edge exponent depends on the dimension of the contact set of G(q) = ω_kin(|q|) − E_l(q). Near its maximum
  G ≈ ε − Σ c_i x_i² over the directions in which G is curved. In a cubic crystal E_l(q) depends on q̂, so the maximum is isolated in 3-D and
  ℛ ∝ ∫d³x(ε − x²)^{2+k} ∝ ε^{7/2+k} (C19). In the S̄ language the angle average turns the line into a step, p̄ = 0 (WP1-v3 [E10]), and (3.3) gives the
  same 7/2 + k. Only for an isotropic dispersion E_l(|q|) is the maximum a sphere (one curved direction), giving ε^{5/2+k}, REF-A's value. For the Si G = 0
  1s line (vertex ∝ |δq̂|²), p̄ = 1 and ε^{9/2+k}. The Beta-function form (C5b) is not used for p_on = −1, as REF-A says.
- **R-B1 (to REF-WP6-B, F4: "supp Π_mom[X] = supp X ∪ supp S^τ").** Only ⊆ holds. Π_mom[X] = X − S^τp(y_R) with p quadratic; on supp X ∩ supp S^τ it
  vanishes wherever X = S^τp. That set is generically of measure zero but need not be empty, and on a binned grid it can contain whole bins (e.g.
  X = S^τ·y_R² on a bin set where the fitted p equals y_R²). REF-A's "⊆" is the correct statement; the condition "no new support iff supp Δ′_A ⊆ supp S^τ"
  is unaffected.

**Referee disagreements, settled.**
1. *PAER edge value and construction* (REF-A ≈ 0.339 MeV from (E_g + c_TA|𝐊|)/(v_max + c_TA)²; REF-B ≈ 0.337–0.338 MeV from E_g + ω_TA at |Q| ≈ 0.53 Å⁻¹).
   By (3.1′), m_min is monotone in E_th(·) pointwise, and acoustic branches are sublinear (ω_TA(Q) ≤ c_TAQ), so REF-A's linear construction is an
   **upper bound** (0.3389 MeV, C18). By tangency the local slope enters only at second order, so m_min ≈ 2[E_g + ω_TA(Q*_0)]/v_max² with Q*_0 ≈ 0.53 Å⁻¹
   (C18): ≈ 0.337 MeV. **REF-B's construction is right**; REF-A's number is an upper bound. Neither included the exciton replica (E_x^b = 14.7 meV),
   which lowers the edge to ≈ 0.333 MeV [E]. (WP3-v3's §M3(c) also says to use ω_ν(Q*), never c_νd_K.)
2. *Size of δ ln v_max for v_esc = 600:* REF-A 6.8%, REF-B 7.0%. Both are right: ln(850.5/794.5) = 0.068, 850.5/794.5 − 1 = 0.070 (C17). v3 quotes the log.
3. *Annual factors at 760 km/s:* REF-A ×2.13/×0.310 (v_E ± 15), REF-B ×2.22/×0.373 (actual extremes 266.4/237.4, i.e. +15.9/−13.1 km/s). Different inputs, both
   exact (C16); the annual band uses the extremes (REF-B), the symmetric ±15 is listed for reference.
4. *Lowest odd harmonic for P,T-broken targets:* REF-A "ℓ = 3 for cubic magnetic targets", REF-B "lowest odd ℓ allowed by the magnetic group (ℓ = 1 only
   for polar groups)", WP4-v3 I4 "ℓ = 1 still leading (with ℓ = 3)". Character counts (C28): ℓ = 1 never occurs for cubic G_eff; the lowest odd ℓ is 3 for T
   and T_d but **9 for O**. REF-B's formulation is right in general; REF-A's "ℓ = 3" holds for T, T_d only; WP4-v3's statement holds only for polar G_eff
   (flag IF6-12 to WP4).
5. *Support of Π_mom:* REF-A "⊆", REF-B "=": REF-A right (R-B1).
No other item is contested between the referees (SOTA: REF-WP6-B agrees with REF-WP6-A on every shared item); where only one referee raised an item it
is applied as stated (closing table).

---
## 13. Interface flags (changes that alter a quantity another package uses)
| # | Owner / user | Quantity | v2 form | v3 form / action |
|---|---|---|---|---|
| IF6-2 | NOTATION | symbols | W_Lam; δ (nuisance size); K (phonon wavevectors); d | **w_δ; δ_θ; 𝐊_pk (= WP3-v3 K_pk); d_K** (= WP3-v3); NOTATION §M rows to update |
| IF6-3 | NOTATION | experiment index | §E "s_ei, b_ei" | ex (s_{ex,i}, b_{ex,i}, θ^det_ex) — unchanged request |
| IF6-4 | WP0-v3 (8.1), (8.2); O4 | positivity of nuisance types | "M PSD for all θ"; "positivity automatic for M and A" | **M PSD only on scalars (S_ee, contracted A^{(n)}) or as the PSD geodesic; A PSD only for PSD Δ (in window).** WP0-v3 (8.1)–(8.2) still carry the v2 wording: owed correction (B-14 F1/F2) |
| IF6-7 | WP5 | seeding | WP0-v3 (7.3) = WP5 (W6) | unchanged; contraction tr[𝔇ᵀS] (G1) |
| IF6-8 | WP3, WP5 | Fano term 𝔉 (GaAs) | \|ΔP\| ≤ 0.11Γ/δ | rigorous 2π max\|c^F\|; [E] 0.3Γ/δ worst, 0.11 optimistic (WP5-v3 IF-R8-5) — adopted |
| IF6-9 (new) | WP0-v3 (8.3), CONVENTIONS §13 item 13, SOTA | envelope/profile spread | ×1.8 | ×1.35 (M) / ×1.57 (linear); already in WP0-v3 (G7). Linear profile undefined for δ_θ > 0.607 |
| IF6-10 (new) | SOTA L1, LIMITS, M1, WP3, all edge users | threshold masses | 0.333 (Si), 0.338 (PAER), 0.212 MeV (Ge) as edges | **0.333/0.212 = floors at E_g for the continuum only; floor of the total S̄ 0.329/0.211 (E_x); edge = (3.1′); Si PAER ≈ 0.337 (continuum), ≈ 0.3327 (exciton replica); Ge ≈ 0.214/0.213 MeV [E]** |
| IF6-11 (new) | WP3-v3 (IF-8), AUDIT-2, SOTA M1 | M1 window lower edge | SOTA 0.338 vs WP3-v3 §M9 0.336–0.338 (free pairs) / 0.333 (replicas) | **Reconciled (R9 wording, m3):** WP3-v3 §M9 and WP6 agree; the Q* → 0 infimum (WP3 C5, fixed q) needs \|q\| = \|𝐊_pk\| (m_χ ≥ 0.474 MeV) and is not the edge; the PAER edge is (3.1′) at \|Q*\| ≈ 0.53 Å⁻¹: 0.333–0.337 MeV [E] (exciton replica / continuum). Window: Si PAER-only ≈ 0.333–0.42, PAER-leading to 0.43, two-channel 0.43–0.54, allowed ZPL above 0.54; Ge ≈ 0.213–0.32 MeV |
| IF6-12 (new) | WP4-v3 (I4, [3.2′] text) | lowest odd harmonic | "ℓ = 1 still the leading odd harmonic (with ℓ = 3)" | ℓ = 1 only for polar G_eff; cubic: 3 (T, T_d), 9 (O) (C28). Structure unchanged |
| IF6-13 (new) | WP3, M1 | PAER edge exponent | Si TA 15/2 + k_tail at the edge | **13/2 + k_tail** (continuum; WP3-v3 p̄ = 3), **5 + k_tail** (exciton replica); corner contact 4 + k + p; validity Δm/m ≲ 1–5% |
| IF6-14 (new) | WP2-v3 (6.1′), WP0-v3 (8.1) | anharmonic nuisance | type "A" affine (5.1′) | type T (5.1″) (exact constraints, PSD); affine = type L, linearisation only; normalisation n_κ = (2π/Ω)\|c_κ\|² (WP2-v3 IF-4) adopted |
| IF6-15 (new) | WP3, WP0-v3 (8.1) | PAER A-type prior | [0.5, 1.2], "central 1" | [0.4, 1.8] (WP3-v3 IF-10) encoded as median 0.85, σ_ln 0.75; ladder M: central × 1.61, σ_ln 0.22 |
| IF6-16 (new) | WP5-v3 §8 | yield nuisances | θ_seed "WP5 widths" | θ_seed unbounded (computed); θ_Z, θ_dense added (IF-R8-6 applied) |
| IF6-17 (new) | LIMITS, recasts | halo-independent bound / recasts | "minimum because 𝒜 ≥ 0"; "exact recast" | monotone-column proof under (P); Bonferroni CL; recast exact only for min-over-bins limits |
| IF6-18 (R9) | CONTROLS C5, coordinator | scope of C5 | "no PAER below E_g + min ω_Q at T = 0" | holds for the e–h continuum only; exciton replicas start at E_x + ω_ν(Q*), which can lie below E_g (Si 1.1688 eV); floor of the total S̄ is 2E_x/v_max² (0.329 / 0.211 MeV) (VER-B NEW-1; AUDIT-2 m2) |

v2 flags IF6-1, IF6-5, IF6-6 stay closed; IF6-7, IF6-8 updated above.

## 14. Closing table
**(a) Referee items** (one row per verdict; "applied" = correction made; location in v3).
| Item | Verdict | Action | Where |
|---|---|---|---|
| A-1 | STANDS | kept | (1.1)–(1.2) |
| A-2 | w/ corr. | applied: orientation average (1.3a); component-wise average wrong | (1.3); C26 |
| A-3 | w/ corr. | applied: TR removes all odd ℓ; no cubic ℓ = 1; G_eff; n = 2 anisotropy (J = 4, ℓ = 2, 4, 6) | (1.5), (2.4a); C11, C28 |
| A-4 | STANDS | kept | (1.6) |
| A-5 | STANDS | kept | (1.7) |
| A-6 | w/ corr. | applied: (V2) as a model hypothesis; linearised sensitivities replaced | (2.3) V2, V4; C16 |
| A-7 | CONFIRMED (D1) | kept, CONFIRMED | §2.5 |
| A-8 | CONFIRMED as ambiguity (D2) | rewritten as ambiguity | §2.5 |
| A-9 | CONFIRMED, incomplete (D4) | applied: Θ(v_esc − v_χ) typo added | §2.5 |
| A-10 | CONFIRMED (D3, D5) | kept; 3.8 eV, Ge 0.67/3.0 added | §2.1, §2.5 |
| A-11 | FALLS (REFUTED attribution) | **dropped**; replaced by "local = global; μ̂ unique; η̃̂ mod ker 𝒜" | (4.2a); §10 |
| A-12 | w/ corr. | applied: q-independence stated; (3.1′); floors relabelled; PAER construction (settled vs B) | (3.1), (3.1′); C18; §12 item 1 |
| A-13 | w/ corr. | applied: exact asymmetric factors | (2.3) V4, (3.2); C16 |
| A-14 | STANDS | kept; tangency argument and single-bin degeneracy qualifier added | (3.3), (3.4) |
| A-15 | STANDS | kept; p̄_on values now WP3-v3 final | (3.3) table |
| A-16 | w/ corr. | applied: monotone column; P′ stated; integrated kernels; gate | (4.2), §7.1, §7.4; C21 |
| A-17 | STANDS | kept (scalars) | (5.1) |
| A-18 | w/ corr. | applied: positivity collapse shown; type L; support ⊆; exponential tilting (type T) | (5.1), (5.1′), (5.1″); C24 |
| A-19 | w/ corr. | applied: ×1.35 / ×1.57; δ_θ > 0.607; O(δ³) | (6.2), §8; C8c |
| A-20 | STANDS | kept; recast qualifier | (6.4) |
| A-21 | w/ corr. | applied: G8 closed under (I), (P) + monotone column + gate | §4, (7.5) |
| A-22 | w/ corr. | applied: 𝐊_pk, δ_θ, d_K; symbols table | §3, (6.2), §15; IF6-2 |
| A-23 | STANDS | kept (§12 of v2: no contested owed corrections; −0.4% remark correct) | §14(c) |
| A-B3 | (sub-item) | applied: 6.8%/13.6%; 2.5% vs 1.170 eV | (3.5); C17 |
| A-D3 | (sub-item) | applied with correction: bound lines; **R-A1** | (3.3); §12; C19 |
| A-G (6.1) | UNRESOLVED | marked UNRESOLVED | (6.1), §10 |
| A-G (D6) | not fetched | marked UNRESOLVED | §2.5 D6 |
| B-1 | STANDS | kept | (1.2) |
| B-2 | w/ corr. | applied: \|v_min\| | (1.1), (1.3), (4.1); C10a,b |
| B-3 | w/ corr. | applied: no cubic ℓ = 1; daily mean keeps zonal projections | (1.5), (V3); C27, C28 |
| B-4 | STANDS | kept | (1.6) |
| B-5 | STANDS | kept | (1.7) |
| B-6 | w/ corr. | applied: ×2.26/÷10; equation-number convention declared | (2.3), header |
| B-7 | D1–D5 CONFIRMED; D1 last sentence UNRESOLVED; uniqueness REFUTED | applied: D1 sentence → [E]; uniqueness dropped | §2.5, (4.2a) |
| B-8 | w/ corr. | applied: unattained floors; min_q formula | (3.1′); C18 |
| B-9 | w/ corr. | applied: finite shifts; ∂ln η/∂v_esc gap attribution; 2–7% | (3.2), (3.5); C16, C17 |
| B-10 | w/ corr. | applied: corner 4 + k + p; validity window; edge exponent 13/2 + k (TA not at m_min) | (3.3); C19, C20 |
| B-11 | STANDS | kept | (4.1) |
| B-12 | w/ corr. | applied: monotone column; (P) as hypothesis with sufficient conditions; leakage; CL | (4.2); C21 |
| B-13 | STANDS | "≥" written | (4.3) |
| B-14 | w/ corr. | applied: M on scalars / geodesic; A only for PSD Δ; priors as median/σ_ln | (5.1), (5.2), (5.3); C22, C23, C25 |
| B-15 | w/ corr. | applied (support sentence); equality form **rebutted (R-B1)** | (5.1′); §12 |
| B-16 | w/ corr. | applied: scissor, GW–BSE rungs non-conserving | (5.3) |
| B-17 | w/ corr. | applied: ×1.35/×1.57; W_Lam → w_δ | (6.2); C8c |
| B-18 | STANDS (qualifier) | recast and CL qualified | (6.4), (4.2) |
| B-19 | w/ corr. | applied: profiling cost; prefix sums | (4.4); C29 |
| B-20 | w/ corr. | applied (as A-21) | §4 |
| B-21 | STANDS | kept | §14(c) |
| B-22 | w/ corr. | applied: C10a,b symbolic for both signs; C11 tests TR removal of all odd ℓ; C5b exact (gammasimp) | checks.py |

**Counts (referee items):** 49 rows (A-1…A-23, 4 A sub-items, B-1…B-22): **applied 29** (A 14, B 15; including A-D3 and B-15 with their partial rebuttals), **kept as STANDS/CONFIRMED 17** (A 10, B 7), **dropped 1 claim** (the η̃-uniqueness claim, A-11 = B-7), **marked UNRESOLVED 2** (A-G items); **rebutted in part 2** (R-A1 to REF-A, R-B1 to REF-B). Disagreements settled: 5 (§12).

**(b) Interface-routed items (R8 returns).**
| Source flag | Where applied |
|---|---|
| WP0-v3 G1 (tr[𝔇ᵀS]) | (1.2), (1.4), (1.7), §7.1, §7.3 |
| WP0-v3 G4 (relativistic f-sum −0.23%/−0.73%) | (5.3), §7.1 |
| WP0-v3 G6 (L17 domain) | (5.3), §7.1 |
| WP0-v3 G7 (×1.35/×1.57) | (6.2); IF6-9 |
| WP0-v3 G10 (BO remainder), G12 (odd part O(q³)), F9 (τ string), F11 | §5.2 n_B row; (1.5); §7.3; §5.2 screening row |
| WP1-v3 [E13], IF-6, IF-6b (edges, window, two-channel band) | (3.1′) table, (3.3); IF6-10, IF6-11 |
| WP1-v3 IF-4 (onset locations) | (3.3) (exponent rules unchanged; threshold at q^{ZP}) |
| WP1-v3 IF-3 (÷3 second-class line amplitudes) | §5.2 ladder row |
| WP1-v3 IF-10 (12/18 functions), IF-15 | §7.1 |
| WP1-v3 IF-13 (triplet ladder) | §5.2 screened-rows row |
| WP2-v3 IF-4 ((2π/Ω)\|c_κ\|²) | (5.1′), (5.1″), §5.2; C24 |
| WP3-v3 IF-5 (final p̄_on), IF-8 (window), IF-10 ([0.4, 1.8]), IF-11 (thermal factor once) | (3.3) table; (3.1′); §5.2 e–ph and n_T rows; C25 |
| WP4-v3 I4, I11 (odd ℓ, O(q³)) | (1.5), §7.1; IF6-12 |
| WP4-v3 I12 (BCS first order), I13 (WSi withdrawn) | §5.2 superconducting row |
| WP5-v3 IF-R8-5 (θ_𝔉 bound), IF-R8-6 (θ_Z, θ_dense, θ_seed) | §5.2 yield and Fano rows; IF6-8, IF6-16 |
| SOTA "R7 referee reports" (REF-WP3-A/B: no "Si TA 4") | (3.3) |

**(c) Contested corrections from v2 §12:** none (both referees: STANDS). The −0.4% remark ((794.5/796.1)² = 0.996) stands.

**Checks** (`python3 -I code/WP6-v3/checks.py`): **42/42 PASS** (C1–C15 incl. repaired C5b, C8c, C10a,b, C11; new C16–C29; R9: C30, and the C7b, C8b, C18 labels corrected).

## 14′. R9 clean-up (VER-WP6-A/B new items; AUDIT-2 rows addressed to WP6)
| Item | Change | Where |
|---|---|---|
| VER-A N1 | type T shape ψ = ln(1 + Δ′_A/S_c) (needs Δ′_A > −S_c): θ_A = 1 reproduces S_c + Δ′_A up to re-tilting | (5.1″); C30 |
| VER-A N2 = VER-B NEW-2 | existence: interior of the moment cone incl. the endpoint (upper variance) bound (y_min + y_max)T_1 − y_miny_maxT_0 − T_2 > 0, θ_δ bounded above; λ₂ tail integrability (Gaussian yes, power law no) | (5.1″); C30 |
| VER-A N3 | Π^{c}_mom (moments of S_c) vs Π_mom (moments of S^τ), O(Δ^τ_A) apart; linearisation uses Π^{c}_mom | (5.1″) first-order bullet |
| VER-A N4 | single-u₀ condition 𝒜_i(u₀) ≤ 𝒜_i(v) ∀v ≥ u₀; "non-decreasing" iff the bound holds at every u₀ | (4.2) |
| VER-A N5 = VER-B NEW-4 (counts) | duplicated, truncated counts sentence deleted | §14(a) |
| VER-B NEW-1 = AUDIT-2 m2 | 0.333/0.212 MeV = floors at E_g for the continuum only; Si replica edge 0.3327 ± 0.0004 MeV, at or below 0.3332 within the ω_TA error; floor of the total S̄ 0.329/0.211 MeV; Ge labelled likewise; C5 scope flagged | (3.1′) table, consequence (i); IF6-10, IF6-18 |
| VER-B NEW-3 | μ̂ unique only on bins with N_i > 0 | (4.2a) |
| VER-B NEW-4 (labels) | C7b ("0.338 withdrawn as PAER edge"), C8b ("quadratic root w_δ"), C18 ("slope enters at second order") | checks.py |
| AUDIT-2 m3 | WP3-v3 §M9's 0.336–0.338 / 0.333 MeV acknowledged; the Q* → 0 infimum is WP3's fixed-q C5, not WP3's edge; no number changes | (3.1′) consequence (ii); IF6-11 |
| AUDIT-2 m11 | phonon-order truncation loss: \|c_κ\|²/M_κ-weighted mean, WP2-v3 (3.4″) | §5.2 phonon-order row |
| AUDIT-2 m17 | 𝐁^{NR}_{αβγ} (WP0) ≡ b^{NR}_{αβγ}/ω² stated as one object | (1.5) |
| AUDIT-2 m1, m16, m29, m31, B1 | owned by WP1, WP4, NOTATION, WP0 (WP6 flags IF6-2, IF6-4, IF6-10/11, IF6-12, IF6-14, IF6-15 stand); no WP6 text change | §13 |
Checks re-run after R9: **42/42 PASS**.

## 15. Symbols introduced/used
NOTATION v4 and CONVENTIONS throughout, with the v2 list of §15 (unchanged objects: q, ω, v_min, v_T, v_∥, δ_v, δ_v,0, m_min, E_th, N_esc, η, ξ, η̃,
𝒢, f̂^{(n)}, k_tail, p_on, A^{(0)}, A^{(2)}, tr_T, d₂, d₂′, Π_mom, c_b, 𝔪_n, y_R, Δ′_A, P_δ, θ_A, θ_δ, σ_δE, P(i|Λ), 𝒜_ij, 𝒜_i(u₀), v_j, η̃_j, N_v,
δ_v,×, a_lens, ϱ, c_TA, Q_w, N^obs_{ex,i}, s_{ex,i}, b_{ex,i}, ℒ, π_k, a^A_k, k_δ, σ̄_e^up, q_max, 𝓃_e^{(sh)}, J^{(sh)}, E_B^{(sh)}, p_z, WP5 θ's, N_q, N_ω, N_bins).
**Deviations from v2 / new in v3 (flag IF6-2):**
- **𝐊_pk** (pocket-pair vector, = WP3-v3 K_pk) replaces v2's K (which NOTATION reserves for the τ slot); **d_K** ≡ ||q| − |𝐊_pk|| replaces v2's d.
- **δ_θ**: fractional nuisance size in (6.2) (v2 δ, which NOTATION reserves for the off-shell/window detuning; δ in (4.2) keeps that meaning).
- **w_δ** = √(1 + 2.71k_δ²) − 1 replaces W_Lam (a quadratic root, not Lambert W).
- **G_eff**, **H**: effective group on q̂ and unitary subgroup (1.5); **K_{ℓμ}**: G_eff-invariant harmonics; **D(R)**: representation on operator indices (1.3a);
  **s_L, s_T**: longitudinal/transverse parts in C26; **β, n̂, ŵ(t)**: day-cone half-angle, Earth axis, wind direction (crystal frame) (1.5).
- **E_th(q)**, **G(q)**, **ω_kin(q)**, **q₀**, **Q*_0**, **c′**, **E^{ZP}(q)**, **E_x** (= E_g − E_x^b), **ε**: (3.1′)/(3.3) edge objects (E^{ZP} as WP1-v3 [E13]); **p̄_on**: angle-averaged
  onset exponent (WP3-v3 notation for S̄; p_on keeps the fixed-q meaning); **s_±**: corner slopes.
- **ν** (non-negative step measure), **K^{(n)}_i(u)** (integrated kernels) in (4.2); **(P)**, **P′** (hypotheses).
- **Types L, T**; **S_c**, **ψ**, **φ**, **λ_b(θ)**, **T_a(θ_δ)**, **n_κ** ≡ (2π/Ω)|c_κ|² (5.1′)–(5.1″); **σ_ln** (log-width); **S(θ) geodesic** notation S^{τ½}.
- **𝔰_BCS, 𝔤_I, Δ_BCS, y** (WP4-v3 [4.2′], quoted); **θ_Z, θ_dense** (WP5-v3 names).
Labels: WP6v3-Cn (checks), WP6-D1…D6, WP6-W1…W5, WP6-N1, WP6-R1…R3, (I), (P), P′, (V1)–(V8), IF6-n, OW6-n, G8′, R-A1, R-B1.
