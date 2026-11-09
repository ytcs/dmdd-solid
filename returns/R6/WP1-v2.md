# R6 / WP1-v2: electronic sector at clamped nuclei, corrected standalone version

Revision agent, brief R6/REV-WP1. Supersedes returns/R5/WP1.md (v1), which stays as the historical record. Applies every owed correction
in state/CORRECTIONS.md (§0, §7, the coordinator items and the WP0-v2 interface flags F1, F11), the open items other packages addressed
to WP1 (WP3 O-WP3-5, WP6 O6-2), and three self-found corrections; closing table §13. Conventions: CONVENTIONS.md; symbols: NOTATION v4.
WP0 equations are cited from returns/R6/WP0-v2.md as WP0-v2 (s.n). This return's equations are [E1]…[E12] (v1 numbers kept; [E10],
dangling in v1, now labels the onset exponents of §3.6). Checks: `code/WP1-v2/checks.py` (sympy only, exact arithmetic, 28 checks, all
PASS, 3 s), cited as WP1v2-Cn. Tags: **[D]** derived (hypotheses stated), **[D, sketch]**, **[E]** estimated, **[C]** conjectured;
literature **[FT]** full text, **[ABS]** abstract. Status of the content: CLAIMED (SOTA R5 WP1), pending R×2.
Si/Ge inputs: lattice constant a_lat = 5.431/5.658 Å, E_g(0) = 1.170/0.744 eV, indirect-exciton binding E_x^b = 14.7/4.15 meV.
Halo reference scalars (CONVENTIONS §8): v_max = v_esc + v_E^ref = 544 + 250.5 = 794.5 km/s.

---
## 0. What changed (v1 → v2)
| v1 | v2 | change |
|---|---|---|
| [E1], [E2] in reduced form (ε^{-1})_{G_qG_q}(q_r,ω) | [E1], [E2] | written with the unreduced index of CONVENTIONS §2: (ε^{-1})_{00}(q,ω) ≡ (ε^{-1})_{G_qG_q}(q_r,ω) |
| [E2] weight (1+Rv)_{0G}ρ | [E2] | **out-state form (ε^{-1})_{G0}ρ(q+G)** (= WP0-v2 (7.2), X2 (2.2)); v1's form is the in-state labelling and needs a complex conjugate; F1 accepted (§1.3, WP1v2-C4) |
| [E7] \|Σ A^λ ρ\|² | [E7] | \|Σ A^{λ*} ρ\|² (self-found conjugation error; WP1v2-C5a) |
| §1.5 increments "WP0 (8.1)" additive; "[E10]" (undefined) | §1.5 | WP0-v2 (8.1) types M/A; reference → [E8] |
| §3.4 thresholds with v_max = 794 | §3.4 | v_max = 794.5 km/s: 0.472/0.708/0.420 MeV |
| — | §3.6 [E10] | onset exponents p_on near E_min(q) (answers WP6 O6-2) |
| §6.2 2607.06005 "dipole" claim (abstract-level check owed) | §6.2 | re-read in full text 2026-10-31: quote confirmed, verdict stands |
| L1 validity (e) "lab-isotropic f_χ" | L1 | hypothesis (I): angle-averaged S (WP0-v2 (9.1), WP6-W5) |
| G5 "matched by the f-sum (WP0 (8.2))" | G5 | ∫_ℝ ωS = π𝓃_eq²/m_e; informative only for non-conserving rungs (WP0-v2 (8.2)) |
| §9 "WP0 defects" D1–D6 | §9 | all applied in WP0-v2; D6 resolved by WP0-v2 CC-1, accepted here |
| checks C1–C8 (numpy/scipy) | WP1v2-C1…C12 | sympy only; adds F1, [E7], [E5], [E12], T_d and threshold checks |
| v2/v1 symbols (κ, W̄_l, ε_M, E_b, S_F, T_ℓm, F(q), K_ℓ, Ξ, Δ_sc, X, Δ_X, O_i, M¹, n_e, Π_T, v_⊥, v_ψ, G(q), …) | NOTATION v3 | §13 rows 2–19 |

---
## 1. The sector and the kernel ladder

**1.1 Clamped nuclei [D].** The clamped-nucleus sector is n_B = 0 in τ (CONVENTIONS §11; WP0-v2 §6): R̃_{eκ} = R̃_{κκ} = 0, so the total ε
equals ε_e. WP0-v2 (5.3) then holds with c = e only, and WP0-v2 (5.4) with (5.5)(i) gives, exactly at this level,

  S_ee(q,ω) = (2q²/e²)(1 − e^{−βω})^{-1} Im[−(ε^{-1})_{00}(q,ω)],   ε_{GG′}(q,ω) = δ_{GG′} − v_C(q+G) R̃_{GG′}(q,ω),                    [E1]

with (ε^{-1})_{00}(q,ω) ≡ (ε^{-1})_{G_qG_q}(q_r,ω), q = q_r + G_q, q_r ∈ 1BZ (CONVENTIONS §2). This is the X0 sector of Theorem D
(WP0-v2 (6.1)) at zero e–ph order. ZPR, PAER, the X+ sideband and the Debye–Waller (Franck–Condon e^{−2W}) reduction belong to WP3.

**1.2 The ladder 𝒳: truncations of R̃ (WP0-v2 (5.1)) [D as definitions].** R̃ is irreducible with respect to one Coulomb line of the
external channel {q+G}. Each rung approximates R̃ alone; R⁰ is the KS (or QP) independent-pair bubble:

| 𝒳 | R̃ used in [E1] | what it adds | exact relations kept (local H) |
|---|---|---|---|
| IP | none: S = −2Im R⁰_{00}/(1 − e^{−βω}) (no Dyson) | — | f-sum, positivity; KK for R⁰ (not for L) |
| RPA | R⁰, G = G′ = 0 only | 1/\|ε_{00}\|² screening | f-sum, KK, positivity |
| RPA+LFE | R⁰, full GG′ matrix | microscopic inhomogeneity | the same + static ε_mac ≥ 1 ([E3]) |
| TDDFT | R̃ = R⁰ + R⁰ f_xc R̃ | xc vertex (ALDA, LRC −α_LRC/\|q+G\|², bootstrap) | the same, if f_xc is ω-independent |
| BSE | R̃ = −iL^{BSE} contracted, kernel Ξ^{BSE} = −W^{scr} only (exchange v_C restored by ε) | e–h attraction (excitons) | f-sum only beyond TDA and with local H_QP |

The BSE row agrees with 2507.14345 [FT]: there L^{BSE} = L⁰ + L⁰Ξ^{BSE}L^{BSE} carries Ξ^{BSE} = v_C − W^{scr}, then ε^{-1} = 1 + v_CR.
Moving the v_C part of Ξ^{BSE} into ε is the WP0-v2 (5.1) bookkeeping; removing W^{scr} returns their RPA **[D]**.

**1.3 Exact pair-resolved (final-state) form [D] (WP1v2-C4).** Hypotheses: RPA(+LFE) or adiabatic TDDFT (v_C → f_Hxc, ε → ε̃ in the
weights), any target (no inversion assumed). From R = R⁰ + R⁰v_CR = R⁰ + Rv_CR⁰ the two exact factorisations

  R − R† = (1 + R†v_C)(R⁰ − R⁰†)(1 + v_CR) = (1 + Rv_C)(R⁰ − R⁰†)(1 + v_CR†)

hold (WP1v2-C4a). In the (3.2) index order (T = 0, ω > 0), (R⁰ − R⁰†)_{GG′} = −2πi V^{-1}Σ_{pairs}ρ_cv(k,q+G)*ρ_cv(k,q+G′)δ(…) (spin 2 inside Σ). The
00 element of the first factorisation gives the **out-state** (prompt-final-state) form, which is WP0-v2 (7.2):

  S(q,ω;cvk) = (4π/V) |Σ_G (ε^{-1})_{G0}(q,ω) ρ_cv(k, q+G)|² δ(ω − ε_{c,k+q} + ε_{vk}),   (ε^{-1})_{G0} = δ_{G0} + v_C(q+G)R_{G0}(q,ω),      [E2]

with R retarded and in the (3.2) order (a = n_e(q+G), b = n_e(q)). Physically the causal induced potential screens the external one,
V_tot(q+G) = (ε^{-1})_{G0}φ_ext, and V_tot creates bare outgoing pairs. The second factorisation gives the in-state labelling, weight
[(1 + Rv_C)_{0G}]*; it sums to the same Im R_00 (WP1v2-C4b,c) but distributes it differently over open pairs. **v1 printed
(1 + Rv)_{0G} without the conjugate:** that form equals [E2] pair by pair when R_{GG′} = R_{G′G} with real symmetric R⁰, S⁰ (TR plus
inversion: Si, Ge; WP1v2-C4e), but in GaAs its pair sum misses Im R_00 (WP1v2-C4d). This is WP0-v2 flag F1, accepted (§12). Totals,
rates and the PAER window (where R(q,ω) is Hermitian and both labellings coincide, WP0v2-C10e) are unaffected; the pair-resolved seeding
of WP5 in GaAs uses [E2] as written here. CONVENTIONS §13 item 16 and the coordinator's OPEN item are thereby closed on the WP1 side.

**1.4 Static stability (closes WP0 O5 at RPA+LFE) [D] (WP1v2-C3).** Hypotheses: an insulator with a static KS response R⁰(q,0) that is
Hermitian and negative semidefinite; RPA kernel. With X = v_C^{1/2}R⁰v_C^{1/2} ≤ 0, v_C^{1/2}Rv_C^{1/2} = X(1 − X)^{-1} has eigenvalues
λ/(1 − λ) ∈ (−1, 0] (C3a), so its diagonal lies in (−1, 0] and

  0 < (ε^{-1})_{00}(q,0) ≤ 1   ⇔   ε_mac(q,0) ≥ 1   (all q, LFE included; C3b exact complex 3×3 examples).                          [E3]

Beyond RPA this needs 1 − f_HxcR⁰ > 0, which fails only near a compressibility instability (HEG r_s > 5.25). Si and Ge have r_s ≈ 2.0
(C7), so the conservative L17 step holds for them **[E beyond RPA]** (WP0-v2 §9.2 (iii) adopts this status).

**1.5 Rung increments as nuisances (WP0-v2 (8.1)) [E, Si/Ge].** Each increment Δ^τ_𝒳 = S^{τ+e_𝒳} − S^τ is the **computed** next-rung
difference, entered as type M (multiplicative log-normal, r^M_𝒳 = Δ^τ_𝒳/S^τ) where S^τ > 0, and as type A where the higher rung opens
new support (bound-exciton lines below E_min(q), [E8]). The ladder is not an expansion (η_xc ~ 0.2–0.5); interim sizes:

| Increment | Size in Si/Ge |
|---|---|
| Δ^τ_{RPA−IP} | factor 1/\|ε\|² ≈ 0.1 at q = 2 keV and ≈ 0.44 at q = αm_e (ω ≈ 5 eV; Cappellini model with EXCEED-DM parameters ε_∞ = 11.3 (their "ε₀"), k_TF = 4.13 keV, ω_p = 16.6 eV). This is the ×1.4–2.5 of 2101.08275 |
| Δ^τ_LFE | −20…−50% (2603.12326) |
| Δ^τ_ALDA | few % at eV ω (ALDA has no e–h binding) |
| Δ^τ_BSE | +30…+100% within ~1 eV of E_min(q) ([E8], Sommerfeld); type A for the bound lines |

---
## 2. Non-density operators in the medium (G10; L3 chain)

**2.1 Continuity [D] (WP1v2-C1a).** For j_e = Σ½{p/m_e, e^{iq·r}} (WP0-v2 §2 operator table), [T_e, n_e(q)] = q·j_e(q) exactly, with no
(q²/2m_e)n_e term (applied in WP0-v2 (4.6); CONVENTIONS §6). For local H, ⟨f|q·j_e|i⟩ = (E_f − E_i)⟨f|n_e|i⟩, hence
S_{n j_L} = (ω/q)S_nn and S_{j_L j_L} = (ω/q)²S_nn, screened or not.

**2.2 On-shell projection theorem [D] (WP1v2-C6a).** Hypotheses: the WP0-v2 (2.2) matching with v^⊥ = v_χ − v_s, v_χ = v − q/2m_χ; local
H; Born; elastic DM (Δ_χ = 0). Then q·v_χ = q·v − q²/2m_χ = ω_q (WP0-v2 (2.1)) and q·j_e acts as ω, so (q·v^⊥)n_e ≐ (ω_q − ω)n_e = 0 on
δ(ω − ω_q). **Only the transverse parts survive in any rate**: on the DM side (1 − q̂q̂)·v_χ = v_T (the halo velocity transverse to q̂,
since q/2m_χ ∥ q̂), on the target side j_T (and J_T). For 𝒪₈ = 𝐒_χ·v^⊥ → 𝐒_χ·v_χ n_e − 𝐒_χ^αj_e^α (WP0-v2 (2.2)), with
(2j_χ+1)^{-1}tr(𝐒_χ^α𝐒_χ^β) = δ_{αβ}/4 (j_χ = ½; C5b),

  tr[𝔇S]_{𝒪₈} ∝ ¼[ |v_T|² S_nn − 2Re v_T·S_{n j_T} + tr S_{j_T j_T} ].                                                            [E4]

The same holds for 𝒪₃, 𝒪₅, 𝒪₇, 𝒪₁₂–𝒪₁₅ through the spin-current rows (J_T). This is the in-medium form of Galilean invariance.

**2.3 Transverse response [D] (WP1v2-C6b).** Per transverse polarisation, with Π^γ_T = e²(R_{j_Tj_T} + 𝓃_e/m_e) (R proper with respect to
the transverse photon only; Coulomb lines, hence LFE, included) and ε_T = 1 − Π^γ_T/ω²,

  S_{j_Tj_T}(q,ω) = (2ω²/e²) Im ε_T(q,ω)/(1 − e^{−βω}),   tr S_{j_Tj_T} = (4ω²/e²) Im ε_T/(1 − e^{−βω}).                                  [E5]

The transverse-photon correction to [E5] is O(ω_p²/q²) ≈ 2×10⁻⁵ at q = 4 keV. Screening of j_T is therefore **through local fields**:
j_T(q) couples to n_e(q_r + G ≠ q), so R̃_{j_T, n(q_r+G)} ≠ 0 and j_T is screened at LFE strength (≈ 10–30% [E]). WP0 v1's "transverse
currents unscreened" held only without LFE (WP1-D4, applied in WP0-v2 (5.3); CONVENTIONS §13 item 19). For a dark photon (total charge),
WP0-v2 (3.6) with the transverse 𝒟^γ gives L + |v^⊥|² Im[−q²/(ω²ε_T − q²)], which is 2608.20715 Eq. (2) [FT] for a light mediator **[D]**.

**2.4 Spin and spin-current channels [D] (WP1v2-C5b).** Take SOC = 0 and a spin-unpolarised reference. Charge (singlet) and spin
(triplet) channels decouple and Coulomb lines enter only the singlet. So

  S_{s^αs^β}(q,ω) = (δ_{αβ}/4) S_nn^{IP}(q,ω) at IP, with NO 1/|ε|²;   beyond IP R̃_s = R⁰ + R⁰ f_xc^T R̃_s,  f_xc^T = (f_↑↑ − f_↑↓)/2.     [E6]

The *unscreened* crystal form factor (L1) is thus the correct IP response for 𝒪₄-type electron-spin couplings. f_xc^T < 0 gives an
exchange (Stoner-like) enhancement, ≈ +10–20% for r_s ≈ 2 **[E]**. In the BSE it removes the exchange term, so triplet excitons lie
below singlets (§3). With SOC, R̃_{s,n} ≠ 0 at O(Δ_SO/E) and the channels mix: Si (Δ_SO = 44 meV) ≲ 2%, Ge (0.29 eV) ≲ 10% in amplitude
near the edge **[E]**. EXCEED-DM 2210.14917 Eqs. (68)–(71) [FT] state "there is no screening" for the axial (electron-spin) coupling: the URF agrees
at Hartree level; the triplet f_xc^T and the SOC mixing are missing there. Consistent with WP0-v2 (4.6e): 𝓜¹_{s^zs^z} = 𝓃_eq²/(4m_e).

**2.5 ALP absorption vertex (answers WP3 O-WP3-5) [D].** The ALP–electron NLO vertex is 2tr J_e(k) = Σ½{σ·p/m_e, e^{ik·r}} (WP0-v2 §2,
2106.12586 Eq. (18) [FT via WP0]). At SOC = 0, unpolarised: Σ_{ss′}|⟨s′|σ^α|s⟩p^α|² = 2|p|² (tr σ^ασ^β = 2δ_{αβ}), so the spin sum of
any amplitude (zero-phonon or PA) equals the velocity form summed over the three Cartesian components; WP3 L9b(c) is **confirmed**.
Refinement: the vertex lives in the **triplet** channel, so (i) it carries no Hartree local fields and no e–h exchange, whereas measured σ₁
(singlet) does; the difference is the optical LFE/exchange correction, ≲ 10% in Si **[E]**; (ii) with SOC it fails at O(Δ_SO/E) as above.

**2.6 Minimal response set (SOC = 0, unpolarised) [D].** Every NR-EFT electron rate (all 𝒪_i, any mediator) needs only
- the singlet blocks: L (screened), S_{n j_T} (2-vector, LFE-screened), S_{j_Tj_T} (2×2: symmetric part from [E5], antisymmetric part
  = Catena's 𝒲̄₅);
- the triplet blocks: S_nn^{IP}, S_{n j_T}^{IP}, S_{j_Tj_T}^{IP} with the f_xc^T dressing.

Longitudinal currents are not independent (§2.1). Seven real functions per (q,ω) on the IBZ ⊗ G grid. This is the G10 table.

---
## 3. Excitons, including dark and indirect ones, at finite q (exciton gaps; L14)

**3.1 Finite-q BSE contribution [D] (WP1v2-C5a).** Hypotheses: QP bands, static W^{scr}, pair basis at total momentum q_r, Hamiltonian
H^{exc}(q_r)A^λ = E_λA^λ including coupling (beyond TDA). With |λ⟩ = Σ_{cvk}A^λ_{cvk}|cvk; singlet⟩, ⟨λ|n_e(q)|0⟩ = √2 Σ A^{λ*}ρ_cv and

  S^{BSE}(q,ω) = (4π/V) Σ_λ |Σ_{cvk} A^{λ*}_{cvk}(q_r) ρ_cv(k, q)|² δ(ω − E_λ(q_r))   (TDA form; beyond TDA use the pseudo-norm).       [E7]

v1 omitted the conjugate (immaterial for real A or real ρ, not in general; C5a). Exchange (v_C(q+G)) is in H^{exc}, which makes [E7]
the screened (L) quantity. Triplet excitons give zero to S_nn.

**3.2 Selection rules at finite q [D].** (Band-structure labels Γ₂₅′, Δ₁, Λ₁, L₁ are BSW irrep labels; X here is the BZ point.)
- (a) **Spin.** Density excites only singlets. Spin operators (𝒪₄, 𝒪₆, 𝒪₉, 𝒪₁₀ …) excite triplets, which lie lower by the exchange
  splitting: dark to n_e, bright to s_e (a new channel; [E6]).
- (b) **Momentum.** An indirect exciton with Q_x = k_c − k_v is optically dark but DM-bright at q = Q_x + G as a zero-phonon process.
- (c) **Point group at the extrema (WP1v2-C10).** The little group of q acting on the VBM (Γ₂₅′) and CBM states sets the rule:
  - **Si**, CBM Δ₁ at 0.85 X, G = 0 so q ∥ [100]: Γ₂₅′ → Δ₂′ ⊕ Δ₅ contains no Δ₁, so ρ_cv(Γ→Δ₁, q∥Δ) = 0. The transition is second
    class: at fixed q the continuum rises as (ω − E_min)^{3/2} and only p-excitons are bright. Umklapp G = (1̄11) gives q off-axis
    (|q| = 3.25 keV) and is allowed. SOC (Δ₆/Δ₇ double group) lifts the zero at O(Δ_SO/E_g) ≈ 4% in amplitude.
  - **Ge**, Γ₂₅′ → Λ₁ ⊕ Λ₃ under C₃ᵥ contains L₁, so the G = 0 transition (q ∥ [111], |q| = 1.90 keV) is allowed.
  - The rules apply also to the zero-phonon line competing with PAER: the Si ZPL near threshold is suppressed quadratically in the
    k-offset from the extremum (pointer to WP3/M1).

**3.3 Wannier limit of [E7] [D for parabolic bands and constant ε_∞; E for Si/Ge] (WP1v2-C8).** Allowed class, exciton radius a_x,
binding E_x^b, reduced mass μ_x, hydrogenic principal number n_H:

  S_x(q,ω) = 4π|ρ_cv(k_v,q)|² [ Σ_{n_H} δ(ω − E_min(q) + E_x^b/n_H²)/(πa_x³n_H³) + (2μ_x)^{3/2}√(ω − E_min)/(4π²) · 𝒮_F(ω) ],
  𝒮_F = 2πζ_S/(1 − e^{−2πζ_S}),  ζ_S = √(E_x^b/(ω − E_min)).                                                                     [E8]

E_min(q) = min_k[ε_{c,k+q} − ε_{vk}]. Second class: |ρ|²/(πa_x³n_H³) → |∇_kρ|²(n_H² − 1)/(πa_x⁵n_H⁵) and 𝒮_F → 𝒮_F(1 + ζ_S²) (ℓ = 1 form).
Two consequences: the total bound weight equals the free-continuum weight within (6πζ(3))^{2/3}E_x^b = 8.0 E_x^b of the edge (C8a);
𝒮_F = 6.3, 2.3, 1.7, 1.35 at ω − E_min = 1, 10, 30, 100 E_x^b, so Si (E_x^b = 14.7 meV) still has +35% at 1.5 eV.
**Prediction [E]:** the survey estimate "< 10% except within 0.1 eV" (catalog-analysis G5/G11) is too small for Si/Ge. Near-edge singlet
S is enhanced by 1.3–2 over RPA for ω ≲ E_min + 1 eV, partly offset by LFE (opposite sign); consistent in sign with 2507.14345 (BSE > RPA
at low ω for GaAs and NaI).

**3.4 Kinematic thresholds for direct indirect-exciton creation [D given v_max = 794.5 km/s] (WP1v2-C9).** From ω_q ≥ E_x
(WP0-v2 (2.1), Δ_χ = 0): m_χ ≥ |q|²/[2(|q|v_max − E_x)], E_x = E_g − E_x^b.

| Case | \|q\| | m_χ,min | class |
|---|---|---|---|
| Si, G = 0 | 1.94 keV | 0.472 MeV | forbidden |
| Si, G = 1̄11 | 3.25 keV | 0.708 MeV | allowed |
| Ge, G = 0 | 1.90 keV | 0.420 MeV | allowed |

So in Si the zero-phonon exciton line opens at the upper end of the PAER-only window (0.34–0.47 MeV, SOTA R2), and opens suppressed.
This is the boundary WP3 must use. (v1 quoted 0.473 MeV with 794 km/s; the change is within rounding of the annual band.)

**3.5 Core excitons [E].** Ge 3d → CB at ≈ 29.5 eV + E_g carries a core-hole BSE (2507.14345 SM Fig. S3: the Ga 3d BSE onset lies below
RPA and is more peaked). It needs SOC (3d₅/₂–3d₃/₂ split 0.58 eV) and is handed to WP5 as Λ = core hole (WP0-v2 (7.1)).

**3.6 Onset exponents near the electronic edge (answers WP6 O6-2) [D for an M0 critical point with parabolic bands; E for Si/Ge].**
WP6 (3.3) needs p_on in S̄(q,ω) ∝ (ω − E_th)^{p_on}. At fixed q the pair energy near E_min(q) is quadratic in the k-offset (reduced mass
μ_x), so from [E2] and [E8]:

  fixed q:  p_on = ½ (IP, allowed) · 3/2 (IP, second class) · 0 (with e–h attraction: 𝒮_F√(ω − E_min) → 2π√E_x^b, both classes);
  S̄ (angle average at fixed |q|, isolated quadratic minimum over q̂, E_min(q) = E_min,0(|q|) + O(|δq̂|²),
  δq̂ the angular offset):  p_on → p_on + 1, and + 1 more if the vertex
  vanishes on the minimum direction (|ρ_cv|² ∝ |δq̂|², the Si G = 0 case);
  bound lines: δ at fixed q; in S̄ a step (p_on = 0) at E_min,0 − E_x^b (allowed) or E_min,0 − E_x^b/4 (second class, n_H ≥ 2).                [E10]

Hence for Ge (allowed, G = 0) the electronic onset of S̄ is a step at the 1s exciton line. For Si (G = 0, forbidden on the [100] axis)
the 1s line enters S̄ with p_on = 1 (weight ∝ |δq̂|² off axis), the 2p line as a step 3E_x^b/4 higher, and the allowed Umklapp class only at
|q| ≥ 3.25 keV. If E_th lies above the onset, p_on = 0. The X+ (PAER) onset exponent is WP3's (WP6 O6-2).

---
## 4. Homogeneous electron gas and plasmons (L10, L11)

**4.1 HEG limit [D].** Jellium (electron–nucleus potential → uniform background), plane-wave KS states, 𝒳 = RPA: [E1] becomes the
Lindhard L. Its e–h continuum is ω ∈ [max(0, q²/2m_e − qv_F), qv_F + q²/2m_e]. [E6] gives S_ss = ¼S^{Lin, unscreened}; [E5] gives Π^γ_T,
matching 2608.20715 Eq. (13) in structure. Si valence numbers (WP1v2-C7): r_s = 2.01, k_F = 3.57 keV, v_F = 6.98×10⁻³, ω_p = 16.6 eV.

**4.2 Plasmon [D, small-q RPA] (WP1v2-C7a).** At the zero of ε₁ with ε₂ → 0, Im[−1/ε] = πδ(ω − ω_pl)/∂_ωε₁. With
ε₁ = 1 − ω_p²/ω² − (3/5)ω_p²q²v_F²/ω⁴ (2003.12077 Eq. (5)):

  L_pl(q,ω) = (πω_p²/2ω_pl) w_pl(q) δ(ω − ω_pl(q)),   ω_pl² = ω_p² + (3/5)q²v_F²,   w_pl = 1 + O(q⁴),                               [E9]

so the pole carries the full f-sum ∫₀^∞dω ωL = (π/2)ω_p² (WP0-v2 (9.5)) to O(q²). The Landau onset (ω_pl = qv_F + q²/2m_e) is at
**q_c = 1.88 keV for Si**. Reaching ω_p needs q ≥ ω_p/v_max = 6.3 keV > q_c (C7b), so **no bulk plasmon is produced by halo DM** in the
electronic sector **[D]**. In real Si the 16.6 eV plasmon sits inside the interband continuum (width 3–4 eV); by [E2] its final states
are e–h pairs with branching 1 at clamped nuclei, so within RPA there is no separate plasmon label (WP0-v2 (7.1); CONVENTIONS §13 item 21).
Any plasmon → phonon branching is X+ (WP3), suppressed by η_ep **[E]**.

---
## 5. Core and relativistic states (G7; the factorisation question of 2509.14534)

**5.1 Factorisation theorem [D].** Hypotheses: Born in H_int; 4-component (no-pair) target Hamiltonian; DM–electron contact or mediator
interactions written as Dirac bilinears. Then WP0-v2 (3.3) holds unchanged with the target operator set extended to

  O_{(e,Γ)}(q) = ∫d³r ψ̂†(r)γ⁰Γ e^{iq·r}ψ̂(r),   Γ ∈ {1, γ⁵, γ^μ, γ^μγ⁵, ½[γ^μ,γ^ν]}  (16 bilinears; ψ̂ the electron field operator),

and 𝔇 is built from the DM bilinears. The rate is tr(𝔇S) exactly at Born level. It factorises into a single scalar K-factor only if one
target operator survives: scalar and pseudoscalar couplings, the 2509.14534 finding. Vector and axial couplings give a matrix S (density
+ current; spin + spin-current): the WP0-v2 multi-operator structure. The "off-shell bound electron with free kinematics" problem of
2509.14534 is an artefact of matching NR-EFT with *free on-shell spinors*; operator-level matching keeps p an operator (WP0-v2 §2).
**The URF answer: factorisation of DM physics from target physics is exact; factorisation into "free amplitude × scalar form factor" is
valid only for the n_e row (and s_e) at O(v_e⁰).** (WP0-v2 (1.2) adopts this.)

**5.2 Foldy–Wouthuysen reduction [D to O(1/m_e²)].**
- ψ̂†ψ̂ → n_e(q)(1 − q²/8m_e²) + (i/4m_e²)Σσ·(q × p)e^{iq·r} (picture change);
- ψ̂̄ψ̂ → n_e − (1/2m_e²)Σ½{p², e^{iq·r}} + …;
- ψ̂†γ⁰𝛄ψ̂ → j_e + spin curl (i/2m_e)q × s_e.

The 16-row NR basis of WP0-v2 §2 is the O(v_e¹) truncation; corrections are O(⟨p²⟩/m_e²) ≈ (Z_κα)² **[E]** (WP1v2-C2):

| Shell | O(⟨p²⟩/m_e²) |
|---|---|
| Si 1s | (Z_κα)² = 0.010 |
| Ge 1s | (Z_κα)² = 0.055 |
| Ge 3d | ~10⁻³ (SO split/binding = 0.58/29.5 = 0.02) |
| valence | α² ~ 5×10⁻⁵ |

**5.3 Relativistic f-sum [D] (WP1v2-C2a–c).** Hypotheses: Breit–Pauli one-body terms, closed shells. Darwin is multiplicative and SOC is
linear in p at fixed r, so both give an identically zero double commutator (C2b). Only mass-velocity contributes:

  𝓜¹_ee = (𝓃_eq²/m_e)[1 − (5/3)⟨T⟩/m_e − q²/4m_e² + O(m_e^{-4})],   ⟨T⟩ = mean kinetic energy per electron,                           [E11]

i.e. δ_rel = −(5/3)⟨T⟩/m_e − q²/4m_e² (= WP0-v2 (4.6′)). With all electrons: Si −0.18%, Ge −0.58% (Ge 1s alone −4.5%). In 4-component
theory without no-pair projection the double commutator vanishes (the Dirac Hamiltonian is linear in p); the NR f-sum is restored only
by the negative-energy (Z-graph) states, so codes using Dirac core states must project.

**5.4 What dominates G7 for halo DM [E].** ω ≤ ½m_χv_max² = 3.5 keV × (m_χ/GeV). Ge 1s (11.1 keV) is unreachable; Ge 2p (1.2 keV) only
for m_χ ≳ 0.35 GeV. **The Ge 3d band is the G7 shell.** Ranked: XC placement of the 3d band, 4.5 eV (2306.14944); the core-hole/core-
exciton final state (§3.5); the SOC split, 0.58 eV; scalar-relativistic and operator corrections, ≲ 10⁻³–2×10⁻². The relativistic 30–50%
of 2509.14534 (Coulomb wavefunctions with an effective charge; read in FT) does not carry over to Ge 3d at halo kinematics. Its large-q
statement survives as the Dirac cusp r^{√(1−(Z_κα)²)−1}: the 1s momentum density gains (q/Z_καm_e)^{(Z_κα)²}, ≈ +13% for Ge 1s at q = 10Z_καm_e.

---
## 6. Anisotropy and modulation (L19 electronic; G11)

**6.1 Symmetry theorems [D] (WP1v2-C11).** Hypotheses: nonmagnetic, TR-invariant reference, any T.
- (i) WP0-v2 (4.3) with TR gives S(q,ω) = S(−q,ω): **every odd-ℓ multipole of S, and of L, vanishes identically** (this holds without
  inversion, so also in GaAs; P- and T-broken targets are the converse case, WP0-v2 (4.3), WP4).
- (ii) O_h (Si, Ge, diamond) has invariant harmonics only at ℓ = 0, 4, 6, 8, … (C11a). T_d (GaAs) adds ℓ = 3, 7 (the xyz invariant),
  (ℓ = 3: xyz), which (i) removes (C11b). In both, ℓ = 2 has no invariant: **the first anisotropic multipole is ℓ = 4**; the ELF of a cubic crystal is
  isotropic through quadrupole order.
- (iii) With the pairing of 2607.06005 Eq. (10), the ER rate is Σ_{ℓ even}S_ℓm𝓡^{(ℓ)}_{mm′}(t)f̂_ℓm′. The dipole-vertex Migdal response
  contains only ℓ = 0, 2 (their text: "the only anisotropic contribution to the event rate is from the quadrupole term (ℓ = 2)"). So **in
  cubic crystals the ELF anisotropy produces no daily modulation of the dipole Migdal rate**. A residual can come only from beyond-dipole
  vertex terms (q·r)⁴ or from anisotropy of the nuclear S (WP2/WP3). WP2's statements (cubic harmonic incoherent multiphonon S exactly
  isotropic; soft-limit Migdal modulation zero) are consistent with this (§11 IF-7).

**6.2 Consequence for the literature [FT re-check 2026-10-31].** 2607.06005, §III discussion of Fig. 4, reads: "The modulation of the
electron rate at 5 eV appears roughly like a clean sine wave with a period of one sidereal day, suggesting that it originates primarily
from the dipole component." By (i) that component is zero; any ℓ = 1 in a computed ELF is a numerical artefact (IBZ reconstruction,
broadening, finite q_cut). A one-sidereal-day harmonic is still allowed from ℓ = 4 along a tilted v_lab cone (𝓡^{(4)}_{mm′}(t) contains
the sidereal fundamental). Their "Migdal modulation" in Si/GaAs must vanish by (ii)–(iii) up to numerical noise. Both are sharp diagnostics for any
code. Verdict unchanged; the referee FT check owed by CORRECTIONS §7 has been done here (quote above).

---
## 7. LIMITS entries
Chains cite WP0-v2 equation numbers; the τ point of each entry is WP0-v2 (9.7).

### L1: Essig et al. crystal form factor (1509.01598)
- **Source [FT]:** Eq. (17) dR/dlnE_e = (ρ_χ/m_χ)N_cell σ̄_e α (m_e²/μ²) ∫dlnq (E_e/q) η F_DM² |f_crystal|². Eq. (21):
  |f_crystal|² = (2π²(αm_e²V_cell)^{-1}/E_e) Σ_{ii′}∫_BZ (V_cell d³k/(2π)³)(V_cell d³k′/(2π)³) E_e δ(E_e−E_{i′k′}+E_{ik})
  Σ_{G′} q δ(q−|k′−k+G′|)|f_{[ik,i′k′,G′]}|². The spin 2 is inside 2π² (Eq. (60)). (Source units/notation: E_e = ω, V_cell = Ω.)
- **Chain [D]:** WP0-v2 (3.3) → (9.1) single n_e row → hypothesis (I) and (9.2) with 𝒢 = η/(2q) → [E1] at 𝒳 = IP (WP0-v2 (7.2) without ε)
  → angular average. Dictionary (WP1v2-C12a,b):

  |f_crystal(q,ω)|² = (Ω q³/4παm_e²) S̄^{IP}_ee(q,ω) = (Ω q⁵/8π²α²m_e²) ε̄₂^{noLFE}(q,ω).                                                [E12]

  The second equality is 2101.08275 Eq. (16) [FT], an independent check. Inserting [E12] in Eq. (17) (per target → per unit mass,
  N_cell/M_T = 1/(ρ_TΩ)) reproduces WP0-v2 (9.2) term by term, including spin 2 and η/2q (C12b). **SOTA #7 (Essig prefactor):
  CROSS-CHECKED.** D1's 2πα owes the factor 2 (CORRECTIONS §1).
- **Validity:** (a) |ε|² ≈ 1, needing q ≫ k_TF·(…); in Si 1/|ε|² ≈ 0.1 at 2 keV and 0.44 at αm_e (§1.5), so L1 overestimates by
  ×1.4–2.5. (b) T ≪ E_g. (c) pseudo-wavefunctions, accurate only to q ≲ 6–8 αm_e (2603.12326). (d) a scissor Δ_scis shifts energies but not
  ρ_cv, so the f-sum is violated by +Δ_scisΣ|ρ|², ≈ +3.5% in Si [E]. (e) hypothesis (I), angle-averaged S (not isotropy of f_χ; WP6-W5);
  the cubic anisotropy enters at ℓ = 4 (§6; L19 ~1%).
- **Leading correction [D]:** within RPA without LFE the correction is exactly multiplicative, S = S^{IP}/|ε_{00}|² (Im R = Im R⁰/|ε|²);
  then Δ^τ_LFE and Δ^τ_BSE ([E8]).
- **Discrepancies:** 2105.02233 Eq. (80) re-quotes Eq. (21) with δ(ΔE − E_{ik} + E_{i′k′}), the energy argument's sign flipped (also their
  Eqs. (37), (47)); typographic. QEdark f_crystal is spin-summed; Catena's 𝒲̄₁ = 8ΔEαm_e²|f_crys|²/q³ (their Eq. (81)) is per spin with the
  2 carried in their Eq. (6) (CONVENTIONS §6): consistent.

### L2: dielectric/ELF rate (2101.08275, 2101.08263)
- **Source [FT]:** 2101.08275 Eq. (6): S(ω,k) = (k²/2πα)(1−e^{−βω})^{-1} Im[−1/ε_L(ω,k)]; Eq. (13) the rate, with S defined with n_{−k}
  (Eq. (4)). 2101.08263 Eq. (1): Γ(v_χ) = ∫d³q/(2π)³|V(q)|²[2(q²/e²)Im(−1/ε(q,ω_q))], at T = 0.
- **Chain [D]:** WP0-v2 (3.3) → n_e row → (5.5)(i) clamped nuclei (or (ii) ω ≫ ω_max = 64 meV in Si, error O(κ_BO⁴)) → (5.4) → FDT (4.1).
  2q²/e² = k²/2πα with e² = 4πα (C12c). 𝒳 = exact or any rung. With LFE the exact object is (ε^{-1})_{00}(q,ω) [E1]; 2603.12326 Eq. (16) and
  2507.14345 (ε_M = 1/ε^{-1}_{GG}, their ε_mac) use exactly this.
- **Validity:** DM couples to the electron density only. A dark photon needs the total ε (WP0-v2 (5.4)); its ionic part is 0 in Si, and
  ε₀ − ε_∞ = 1.9 in GaAs only at ω ≪ ω_T. Electron-only coupling needs ε_e (WP0-v2 (5.5), §9.2 (ii)).
- **Leading corrections:** (i) KKL App. A works "in the approximation that ε is diagonal in G"; their "LFE" replacement ε_GG → 1/(ε^{-1})_{GG}
  is in fact the exact clamped result. (ii) KKL Eq. (27) averages ε over directions *before* inverting; since L = ε₂/|ε|² is nonlinear,
  Im(−1/ε̄) ≠ the average of Im(−1/ε); the bias is second order in the anisotropy, ℓ = 4 in cubic crystals [D]. (iii) |v^⊥|²-weighted
  transverse terms for vector mediators: [E4]/[E5], ≲ 10⁻⁹ relative for halo DM. (iv) X+ (PAER) and ZPR: WP3.
- **Discrepancies:** Hochberg et al. write ε(q,ω) with no LFE/G specification. KKL write ⟨p,ℓ′|e^{ik·r}|p,ℓ⟩ in Eq. (15), a typo for p′.
  The sign of k in n_{−k} is immaterial for TR-symmetric targets (§6.1(i)); binding for P,T-broken ones (CONVENTIONS §3).

### L3: NR-EFT crystal responses (2105.02233, 2009.13534, 2210.14917, 2510.25835)
- **Source [FT]:** 2105.02233 Eq. (36): 𝓡 = (n_χN_cell/128πm_χ²m_e²)∫dlnΔE∫d³q (1/q) η̂ Σ_l Re(R_l^*W_l), with W_l (Eq. (37)) built from
  B₁ = |f′|², B₂ = (q/m)·f′f′*, B₃ = |f′|², B₄ = |(q/m)·f′|², B₅ = i(q/m)·(f′×f′*) (Eqs. (38)–(42)); vector overlap f = ∫ψ*e^{iq·x}(i∇/m)ψ
  (Eq. (11)). 2210.14917 Eq. (18) R ∝ Σ_IF∫ f_scr² F_med² g 𝓕_IF, f_scr = 1/(q̂·ε·q̂) (Eq. (23)); axial: "Contrary to the kinetically mixed
  dark photon model, there is no screening" (with Eqs. (70)–(71)). 2510.25835 Eq. (5): the rate in terms of χ₀₀, χ_ij, χ_0i; Eq. (6):
  dΓ₈ = (v_⊥²/4)dΓ₁, "v_⊥ is the component of v that is perpendicular to q" (their v_⊥ = campaign v_T; their χ = campaign R).
- **Chain [D]:** WP0-v2 (3.3) → IP R̃ → WP0-v2 (5.3) screening of every row with R̃_ac ≠ 0 → §2.1–2.6.
- **Results [D]:** (a) **Only 3 of Catena's 5 responses are independent** (WP1v2-C1b). For local H, q·f = −(ΔE − q²/2m_e)f, so
  𝒲̄₂ = −(ΔE − q²/2m_e)𝒲̄₁/m_e (real) and 𝒲̄₄ = (ΔE − q²/2m_e)²𝒲̄₁/m_e²; 𝒲̄₁, 𝒲̄₃ − (m_e²/q²)𝒲̄₄ (transverse current) and 𝒲̄₅
  (antisymmetric transverse) are independent; their small Im 𝒲̄₂ measures the nonlocal-PP violation [V_NL, n_e]. (b) In medium: 𝒲̄₁, 𝒲̄₂,
  𝒲̄₄ are screened by |ε|^{-2}; the transverse 𝒲̄₃, 𝒲̄₅ by LFE only; spin rows follow [E6]. EXCEED-DM's global f_scr is right for the n_e row
  of a dark photon; it is wrong for scalar couplings to n_e (screened too, per L2) and for current and spin rows, which do not screen with
  1/(q̂·ε·q̂). (c) **2510.25835 Eq. (6) for 𝒪₈ is the v_s → 0 truncation of [E4]**: it omits tr S_{j_Tj_T} = (4ω²/e²)Im ε_T. The ratio
  tr S_{j_Tj_T}/(|v_T|²S_nn) ≈ ⟨p_T²⟩/(m_e²|v_T|²) ≈ 3×10⁻⁵/7×10⁻⁷ ≈ 40 in Si valence **[E]** (p_T the electron momentum transverse to q̂),
  so their 𝒪₈ limits are conservative by O(10); "determined entirely by the dielectric function" holds only at |v_T| ≫ |p_T|/m_e, which
  does not hold.
- **Validity:** SOC = 0 for the singlet/triplet split (Ge near-edge ≲ 10% mixing). For local H, all-electron or PAW-reconstructed states
  are needed; otherwise the longitudinal reductions acquire [V_NL, ·] terms.
- **Leading correction:** f_xc^T (spin), LFE on j_T, BSE in both channels.

### L10: Lindhard/Mermin ELF (2101.08275 Eqs. (17)–(24); 2104.12786)
- **Source [FT]:** 2101.08275 Eq. (17): ε_Lin = 1 + (3ω_p²/k²v_F²)[f₁ + i f₂] with Eqs. (18)–(21). Mermin Eq. (22):
  ε_Mer = 1 + (1+iΓ/ω)(ε_Lin(k,ω+iΓ)−1)/[1 + (iΓ/ω)(ε_Lin(k,ω+iΓ)−1)/(ε_Lin(k,0)−1)]. Eq. (23): ELF = Σ_i A_i(k) Im[−1/ε_Mer(ω_{p,i},Γ_i)]
  θ(ω−ω_edge,i); Eq. (24): A_i(k) renormalised by the f-sum. (Their Γ = campaign γ_rel.)
- **Chain [D]:** [E1] → jellium → 𝒳 = RPA → Lindhard. Mermin = relaxation-time closure (rate γ_rel) that conserves local particle number
  (continuity, §2.1); a damping closure, not a URF rung.
- **Validity:** ω inside the Lindhard continuum and ω ≫ E_g. Low ω fails: the HEG has intraband weight ∝ ω below E_g, whereas an
  insulator at clamped nuclei has S(ω < E_min) = 0 exactly. The static limit fails: ε_HEG(q→0,0) = k_TF²/q² → ∞, whereas ε_mac(0,0) = ε_∞
  = 11.7 in Si. Si r_s = 2.01.
- **Leading correction [D]:** the HEG xc local-field factor, ε = 1 − v_CR⁰/(1 + v_CG_LF(q)R⁰) (TDDFT rung), then band structure (gap).
- **Discrepancies:** their step θ(ω−ω_edge) breaks KK and the built-in Mermin f-sum, hence Eq. (24). The f-sum is restored per oscillator but KK is
  not; Re ε^{-1} must be regenerated, as KKL do.

### L11: plasmon production (2002.06937, 2003.12077)
- **Source [FT]:** 2003.12077 Eq. (5): ε̂_L ≈ 1 − (ω_p²/ω²)(1 + (3/5)k²v_F²/ω_p²); Eq. (7): Z_L ≈ 1 − (3/5)k²v_F²/ω_p²; cutoff k ≲ ω_p/v_F
  "(roughly 2.4 keV)"; Eq. (8): plasmon bremsstrahlung from NR. 2002.06937 Eq. (4): q_c ~ 2π/a ~ 5 keV; Eq. (13):
  P(E) = (α/π²)∫d³q q^{-2}Im{−1/ε(E,q)}δ(E − q·v + q²/2m_χ); Eq. (14): dR/dE ∝ S(E)∫₀^{q_c}dq/q η.
- **Chain [D]:** [E1] → pole of ε^{-1} [E9]. For a light mediator coupling to total charge, WP0-v2 (3.3) with |Ṽ|² = e_χ²e²/q⁴ and (5.4)
  gives Γ_χ = (α_χ/π²)∫d³q L/q², α_χ ≡ e_χ²/4π, which is 2002.06937 Eq. (13) (WP1v2-C12d).
- **Validity:** direct plasmon creation needs v ≳ ω_p/q_c ≈ 9×10⁻³ (Si), out of reach for halo DM ([E9]), as both papers find. Plasmon
  production from NR (2003.12077) is X+/mixed (WP3), quoted here only for Z_L. Within RPA the plasmon is not a separate final state
  (WP0-v2 (7.1)).
- **Leading correction:** [E9] with interband damping; Si's 16.6 eV resonance lies in the e–h continuum, so there is no separable pole
  beyond q ≈ 1–2 keV.
- **Discrepancies:** three cutoffs: 2π/a_lat ≈ 2.28 keV (2002.06937 quote 5 keV), ω_p/v_F = 2.38 keV, RPA Landau onset 1.88 keV (C7).
  2002.06937's 5 keV overstates the plasmon phase space ×(5/1.9)² in the log range of their Eq. (14), which also uses ε(E,0) up to q_c
  (no dispersion, no loss of pole weight). Z_L (2003.12077) is the Coulomb-gauge field residue, not the f-sum share w_pl(q) of [E9];
  different normalisations, no conflict.

### L14: BSE exciton rate (2507.14345)
- **Source [FT]:** Eq. (1): R = (1/ρ_T)(ρ_χ/m_χ)(π/α)(σ̄_e/μ²)∫d³v f∫d³k/(2π)³ k²|F_φ|²∫dω/2π (1−e^{−βω})^{-1}Im[−1/ε(ω,k)]δ(…).
  Eq. (2): L = L⁰ + L⁰ΞL, Ξ = −iδδv + iδδW(ω=0), in TDA, with ε_M(k=q+G) = 1/ε^{-1}_{GG}(q,ω). (Their L, Ξ, W = campaign L^{BSE},
  Ξ^{BSE}, W^{scr}; F_φ = F_DM.)
- **Chain [D]:** [E1] with 𝒳 = BSE (§1.2) → [E7]; Eq. (1) is L2 with the BSE ELF.
- **Validity:** static W^{scr} (dynamical corrections O(E_x^b/ω_p)). TDA, which breaks the f-sum (WP0-v2 (4.6)) and KK; the error grows
  toward the plasmon (the authors find a NaI change beyond TDA). Scissor QP: f-sum broken by Δ_scis (L1 (d)). 10 CBs (their Fig. S2: the
  ELF decreases with more CBs, ε₁ unconverged). 6³ k-grid, which cannot resolve Wannier excitons with a_x ≫ a_lat (Si 4.9 nm, GaAs
  11.6 nm): only the Sommerfeld continuum part of [E8] is captured, not the bound lines. Isotropic average.
- **Leading correction:** beyond-TDA coupling (restores the f-sum); the bound lines [E8] (type A nuisance, §1.5); selection rules §3.2;
  exciton–phonon replicas (WP3: replace the e–h final state of D2 eq. 2.1 by A^λ).
- **Discrepancy:** their F_φ = α²m_e²/k² is (αm_e)²/k², consistent; none of substance.

### L17 (electronic part, with WP0-v2 §9.2)
WP0-v2 derives the bound; WP1 adds which rungs preserve its ingredients (§1.2):
- (a) the f-sum (9.5) holds for IP, RPA(±LFE) and adiabatic TDDFT with local H (conserving: WP0-v2 (8.2) is vacuous for them);
- (b) it is broken by a scissor (+Δ_scisΣ|ρ|²), nonlocal PPs, TDA-BSE and relativistic cores without no-pair projection ([E11]); a
  truncated S can exceed (9.6) by these amounts;
- (c) the hypothesis ε(q,0) ≥ 1 is **DERIVED at RPA+LFE for any insulator** ([E3]; WP0-v2 §9.2 (iii));
- (d) the relativistic factor on ω_{p,e}² is −0.18% (Si), −0.58% (Ge) ([E11] = WP0-v2 (4.6′));
- (e) source formulas [FT]: 2110.01587 Eq. (1) ∫₀^∞(dω/ω)Im[−1/ε] = (π/2)[1 − 1/ε(q,0)] (the KK sum rule, WP0-v2 (9.4)); 2608.05282 Eq. (8)
  the Hölder interpolation K_n ≤ (π/2)ω_p^{n+1}[1 − ε^{-1}(q,0)]^{(1−n)/2} (WP0-v2 (9.6)), as read in full text by WP0.

### L19 (electronic part): daily modulation from the anisotropic ELF (2607.06005; lattice 2411.03433 → WP2)
- **Source [FT, re-read 2026-10-31]:** 2607.06005 Eq. (6): dR/dω ∼ ∫d³q F(q²)/q ∫dω_q T(q,ω_q,ω) f̂(s + v_lab·q̂, q̂). Eq. (10):
  dR/dω ∼ ∫dq qF(q²)∫dω_q Σ_{ℓmm′} T_ℓm(q,ω_q,ω)𝓡^{(ℓ)}_{mm′}(t)f̂_ℓm′(s,v_lab), with T = L for ER (their T_ℓm = campaign S_ℓm up to
  the S ↔ L factor). Text: "the only anisotropic contribution to the event rate is from the quadrupole term (ℓ = 2)" (Migdal), and the
  §III Fig. 4 sentence quoted in §6.2.
- **Chain [D]:** WP0-v2 (3.4) without angular average, crystal axes fixed in the lab; [E1] for S.
- **Validity:** the response is static on the sidereal time scale (trivially true).
- **Leading correction / content [D]:** §6.1: odd ℓ ≡ 0 (TR); no ℓ = 2 in cubic crystals, first term ℓ = 4; zero dipole-Migdal ELF
  modulation in Si, Ge, GaAs. P,T-broken targets: nonreciprocal S, v-odd rate (WP0-v2 (4.3), WP4).
- **Discrepancy:** the "dipole component" attribution (§6.2); their ≈ 1% ER modulation is consistent with an ℓ = 4-only response.

---
## 8. Gaps: formula and computation specification

**G5 (screening and many-body beyond RPA).**
- **Formula:** [E1] with 𝒳 = BSE beyond TDA, [E7], assembled as S = S^{BSE} (q ≤ 10 keV, ω ≤ E_g + 10 eV) ⊕ S^{RPA+LFE} (elsewhere), matched
  on a strip. The f-sum ∫_ℝ dω ω S = π𝓃_eq²/m_e (WP0-v2 (4.6), (8.2)) is a constraint only for the non-conserving parts (TDA, scissor,
  band cutoff); for the conserving rungs it is automatic, so the matching is checked on ω-moments of S^{BSE} − S^{RPA+LFE}.
- **Spec:** Codes: QE/PBE (or exciting all-electron) → G₀W₀ (BerkeleyGW or Yambo) for QP and W^{scr} → finite-Q BSE (BerkeleyGW finite-Q,
  Yambo q ≠ 0, or exciting). Pair basis: 4 VB (Ge: + 3d separately, G7) × 12 CB. Grids: coarse 8³ kernel, interpolated to fine 24³
  (resolves 50 meV continuum structure). Bound lines: added analytically by [E8] with ab initio μ_x, ε_∞, ρ_cv(k_v,q) at the extrema.
  Momentum points: q_r on the 24³ commensurate set and G-shells with |q| ≤ 10 keV (≈ 10³ (q_r,G) points after O_h reduction). Solver:
  Haydock/Lanczos (≈ 200 iterations); coupling (non-TDA) checked against the f-sum to < 1%. Cost per q_r: ≈ 24³·48 ≈ 6.6×10⁵ pairs, about
  200×(pairs)² ≈ 10¹⁴ flop → node-hours; total ≈ 10³ node-h. Validation: Si NIXS/EELS at q < 3αm_e (as 2603.12326). Outputs: L(q,ω) on
  (q̂, |q|, ω) bins; Δ^τ_BSE = S^{BSE} − S^{RPA+LFE} (type M, with the bound lines type A); p_on per [E10].

**G7 (core, all-electron, relativistic).**
- **Formula:** [E1] + [E7] with 4-component or ZORA states, FW-corrected operators §5.2, [E11] as the check; factorisation §5.1.
- **Spec:** all-electron FLAPW (exciting or WIEN2k) with SOC in second variation, or PAW plus core reconstruction (EXCEED-DM), for Ge 3d,
  Ga 3d, Si 2p (m_χ ≳ GeV). 3d binding: PBE vs HSE06 vs G₀W₀ vs ΔSCF core hole, spread taken as the nuisance (target: the 29.5 eV measured
  value). Core-level BSE at finite q (exciting XANES-type), 3d₅/₂/3d₃/₂ resolved. Grid: q ≤ 30 keV, ω ≤ 200 eV, 12³ k. Outputs: S^{core}(q,ω),
  core-hole fraction for WP5 (Λ = core hole), relativistic f-sum check.
- **Remaining gap:** no ab initio crystal 4-component response code with no-pair projection at finite q exists; ZORA + SOC is the
  practical limit, error O(⟨p²⟩/m_e²) ≲ 2% for Ge 3d **[E]**.

**G10 (non-density operators).**
- **Formula:** §2.6, [E4]–[E6]: L, S_{nj_T}, S^{sym/anti}_{j_Tj_T}, plus the triplet IP blocks with f_xc^T (seven functions).
- **Spec:** QE/EXCEED-DM-type IP module. Vertices: ρ_cv(k,q+G) and ⟨c|½{p, e^{iq·r}}|v⟩/m_e with the nonlocal-PP commutator correction (or
  PAW). Screening: RPA+LFE Dyson with the mixed blocks R̃_{j_T,n(q+G)}; spin: ALDA f_xc^T. Grids as QCDark2 (10³ k, q ≤ 25αm_e,
  LFE cutoff ≈ 8αm_e). Cost ≈ 3× an RPA+LFE ELF run. Outputs: versioned library tables (WP6), enabling recasts of every 𝒪_i, including 𝒪₈
  (fixing 2510.25835) and intermediate mediators (2605.11063 [ABS], entering only through F_DM in 𝔇).

**G11 (anisotropy, electronic).**
- **Formula:** §6.1 and the 2607.06005 Eq. (10) pairing, with S_ℓm restricted to even ℓ and cubic harmonics K^cub_ℓ (ℓ = 0, 4, 6, 8).
- **Spec:** full-q (IBZ + symmetry) RPA+LFE ELF (GPAW, QCDark2 or BerkeleyGW epsilon), projected on K^cub_ℓ up to ℓ = 8 per (|q|, ω).
  Diagnostics: |S_{1m}|, |S_{2m}|, |S_{3m}| / S₀₀ < 10⁻³ (pure noise; ℓ = 3 allowed by T_d but killed by TR). Outputs: S₄, S₆, S₈(|q|, ω)
  for Si/Ge/GaAs and the modulation amplitude for a given site latitude.

**Exciton gaps (catalog-processes §12 item 3).**
- **Formulas:** [E7], [E8] (bound lines plus Sommerfeld, allowed and second class), §3.2 rules, §3.4 thresholds, [E10] onsets, [E6] plus
  BSE without exchange (triplet, spin-coupled DM).
- **Spec:** as G5, plus Si exciton at q = 0.85 X + G and Ge at L + G; effective-mass hydrogenic series with ab initio anisotropic masses
  (Si longitudinal/transverse 0.92/0.19 m_e, Lipari–Baldereschi); ρ_cv and ∇_kρ_cv at the extrema from DFT.
- **Remaining gaps:** exciton–phonon replicas (WP3, X+ with an exciton final state); Frenkel/self-trapped excitons in NaI (lattice
  relaxation, WP3/WP5); beyond-TDA finite-q BSE has never been run for DM.

---
## 9. WP0 defects reported by WP1 v1: status in WP0-v2
| v1 label | Defect | Status |
|---|---|---|
| WP1-D1 | (4.6), (5.3) extra (q²/2m)n in [H, n] | applied, WP0-v2 (4.6), (5.3) (its #4) |
| WP1-D2 | δ_rel from SOC | applied: mass-velocity only, WP0-v2 (1.2), (4.6′) (#2) |
| WP1-D3 | Ge sizes 0.27/0.05 | applied: 0.055/~10⁻³ (#3) |
| WP1-D4 | j_T "unscreened" | applied: LFE-screened, WP0-v2 (5.3) (#6) |
| WP1-D5 | spins "unscreened" | applied: f_xc^T-renormalised (#7) |
| WP1-D6 | (7.2) weight vs (1+Rv)_{0G} | resolved by WP0-v2 CC-1 (out-state (ε̃^{-1})_{G0} general); **accepted here**: v1's form was the unconjugated in-state weight (§1.3) |
| O3, O5 | relativistic matching; ε(q,0) ≥ 1 | closed (WP0-v2 §12): §5 and [E3] |

---
## 10. Exact remaining gaps
1. Finite-q BSE beyond TDA for Si/Ge with bound lines: specified (G5), not computed. Interim nuisance Δ^τ_BSE ∈ [+0.3, +1.0]×S near the
   edge (type M) plus the bound lines (type A) [E].
2. A 4-component crystal response with no-pair projection (G7); interim error O(⟨p²⟩/m_e²) ≤ 2% for Ge 3d.
3. The spin-channel f_xc^T in insulators: ALDA only; uncertainty = ALDA-vs-RPA difference in the triplet channel.
4. The size of LFE screening of j_T (§2.3, 10–30% [E]) awaits the G10 run; the same number bounds the triplet-vs-σ₁ ALP difference (§2.5).
5. SOC mixing of singlet and triplet near the Ge edge (≲ 10% [E]).
6. Plasmon → phonon branching (X+, WP3).
7. The pair-resolved weight in GaAs: [E2] (out-state) is adopted with WP0-v2; the referee check of the in/out labelling (WP0-v2 OW0-7) is
   shared with REV-WP3 and R7.

---
## 11. Interface flags
| # | Owner | Quantity | Recorded form | Mismatch / action |
|---|---|---|---|---|
| IF-1 | WP3 (W.5), X2 (2.2) | external LFE weight, pair-resolved (F1) | WP0-v2 (7.2), X2 (2.2): (ε̃^{-1})_{G0}ρ(q+G) | **now identical to [E2]**; v1 mismatch removed. WP3 (W.5) must use this form in GaAs (CORRECTIONS §9 caveat); REV-WP3 to confirm |
| IF-2 | WP5 (generation-1 seeds) | S(q,ω;cvk) from WP1 (RPA+LFE) | WP5 §2 (G1): "S(q,ω;cvk), using WP1 outputs (RPA+LFE)" | use [E2]-v2; in GaAs v1's form mislabels open pairs (totals unaffected); with WP0-v2 (7.3) the seed weight is tr[𝔇S(Λ)] |
| IF-3 | WP6 (ladder nuisance) | Δ^τ_𝒳 fallback | WP6 §5 table: "if not computed, η_xc·S, η_xc = E_x^b/E_g near the gap" (≈ 1%) | **mismatch**: [E8] gives ×1.3–2 within ~1 eV of E_min (Sommerfeld) and new support below E_min (bound lines). Fallback should be §10 item 1 (type M + type A), not η_xc·S. WP0-v2 Table 6.1 agrees (η_xc not small; computed difference) |
| IF-4 | WP6 (3.3), O6-2 | onset exponent p_on | WP6: "WP1 to supply p(q)" | supplied: [E10] (Ge: step at the 1s line; Si G = 0: 1s line with p_on = 1, 2p step, Umklapp at ≥ 3.25 keV; S̄ adds +1 (+2 if the vertex vanishes on the minimum direction) to each fixed-q continuum exponent) |
| IF-5 | WP3 L9b(c), O-WP3-5 | ALP vertex tr J_e at SOC = 0 | WP3: spin sum = velocity form | confirmed (§2.5), with the triplet-channel refinement (no Hartree LFE/exchange; ≲ 10% vs measured σ₁ [E]) |
| IF-6 | WP3/M1 | Si zero-phonon edge | SOTA R5 WP1 | G = 0 symmetry-forbidden; exciton line at 0.472 MeV (v_max = 794.5 km/s) is the WP3 boundary; allowed Umklapp at 0.708 MeV |
| IF-7 | WP2 (L19 lattice) | cubic anisotropy | WP2: harmonic incoherent multiphonon S exactly isotropic; soft-limit Migdal modulation zero | consistent with §6.1 (different objects: ELF anisotropy starts at ℓ = 4; lattice incoherent S has none). No contradiction (AUDIT item 5) |
| IF-8 | WP0-v2 F11 | static DFPT error order | O(ω_Q²/E_g²) | WP1 quotes no DFPT error; nothing to update |
| IF-9 | NOTATION | new symbols | — | proposed rows: a_lat (lattice constant), n_H (hydrogenic principal number), α_χ ≡ e_χ²/4π, k_v (VBM crystal momentum), ψ̂(r) (electron field operator), α_LRC (LRC kernel strength), p_T (electron momentum transverse to q̂), E_min,0(|q|) (minimum of E_min over q̂), δq̂ (angular offset) |

---
## 12. Contested corrections
None. The one correction that changes a WP1 formula against its v1 statement, F1 (WP0-v2 CC-1, CORRECTIONS "WP0-v2 interface flags"),
is **accepted** after independent derivation (§1.3): with (R⁰ − R⁰†)_{GG′} ∝ ρ_G*ρ_{G′} in the (3.2) order, the v1 identity
Im R = (1+Rv)Im R⁰(1+Rv)† yields pair weights [(1+Rv_C)_{0G}]* (the conjugate was lost in v1), and the other factorisation yields the
retarded out-state weight (ε^{-1})_{G0}, which is the physical prompt-state labelling (WP1v2-C4a–e). v1's C3b/C3c tested only a
complex-symmetric R⁰ (TR + inversion), where the two coincide, which is why the slip was not caught.

---
## 13. Corrections applied (closing table)
| # | Correction (ID / source) | Where applied | How |
|---|---|---|---|
| 1 | CORRECTIONS §7 row 1: (ε^{-1})_{G_qG_q}(q_r,ω) ≡ (ε^{-1})_{00}(q,ω) (CONVENTIONS §2) | [E1], [E2], L2 | unreduced index written, identity stated |
| 2 | §7 row 2: κ (Sommerfeld) → ζ_S | [E8] | renamed |
| 3 | §7 row 2: W̄_l → 𝒲̄_l (per spin); B_l → B^{Cat}_l (NOTATION K) | §2.6, L1, L3 | renamed in campaign text; source quotes keep W_l, B_l |
| 4 | §7 row 2: ε_M → ε_mac | §1.2, [E3], L10 | renamed (2507.14345's ε_M noted as source notation) |
| 5 | §7 row 2: E_b → E_x^b | §3, header | renamed |
| 6 | §7 row 2: S_F → 𝒮_F | [E8], [E10] | renamed |
| 7 | §7 row 2: T_ℓm → S_ℓm | §6, L19, G11 | renamed; 2607.06005's T_ℓm kept in quotes |
| 8 | §7 row 2: F(q) → w_pl(q) | [E9], L11 | renamed |
| 9 | §7 row 2: K_ℓ → K^cub_ℓ | G11 | renamed |
| 10 | §7 row 2: Ξ (BSE kernel) → Ξ^{BSE} (and L → L^{BSE}, W → W^{scr}, CORRECTIONS §0) | §1.2, §3.1, L14 | renamed |
| 11 | §7 row 2: Δ_sc → Δ_scis | L1 (d), L14, L17 (b) | renamed |
| 12 | §7 row 2 / CONVENTIONS §14: C1–C8 → prefixed labels | checks, text | WP1v2-C1…C12; other returns' labels prefixed |
| 13 | §7 row 3: v_max = 794 valid as v_max^ref (CONVENTIONS §8) | header, §3.4, §4.2, C7, C9 | 794.5 km/s used; thresholds 0.472/0.708/0.420 MeV |
| 14 | §7 row 4 and SOTA R5 WP1: 2607.06005 "dipole" claim FT double check | §6.2, L19 | full text re-read, sentence quoted with section; verdict stands |
| 15 | §0 global: X (ladder) → 𝒳, Δ_X → Δ^τ_𝒳 | §1.2, §1.5, L chains | renamed |
| 16 | §0 global: O_i → 𝒪_i | §2.2, §3.2, L3, G10 | renamed |
| 17 | §0 global: M¹ → 𝓜¹; n_e (number density) → 𝓃_e | [E11], §2.3, §2.4, G5 | renamed |
| 18 | §0 global: v_q (Coulomb) → v_C | [E1], §1.3, §1.4, L10 | renamed |
| 19 | NOTATION v3 W1 local names: Π_T → Π^γ_T; G(q) → G_LF(q); q_TF → k_TF; v_⊥ (2510.25835) → v_T; v_ψ → v_s; a,b (Cartesian) → α,β; O_Γ → O_{(e,Γ)} | §2.3, L10, §1.5, L3, §2.2, [E6], §5.1 | renamed; source quotes keep source notation with the map stated |
| 20 | F1 (WP0-v2 CC-1; CORRECTIONS §5 X2 row, §9 (W.5), coordinator OPEN item; CONVENTIONS §13 item 16; NOTATION-APPLY D4) | [E2], §1.3, §9, §12, IF-1 | out-state weight (ε^{-1})_{G0} adopted; in-state = conjugated (1+Rv)_{0G}; derivation and WP1v2-C4a–e; accepted, not contested |
| 21 | F11 (static DFPT error O(ω_Q²/E_g²)) | IF-8 | no occurrence in WP1; recorded |
| 22 | WP0-v2 (8.1) / WP6-W2: nuisance types M/A/E/Δ, not additive Gaussian | §1.5, G5, §10 | increments typed (M; A for bound lines) |
| 23 | WP0-v2 (8.2) / WP6-W1, W3 (CONVENTIONS §13 item 12): f-sum π normalisation, vacuous for conserving rungs | G5, L17 (a) | ∫_ℝωS = π𝓃_eq²/m_e; matching role restated |
| 24 | WP0-v2 (9.1) / WP6-W5: hypothesis (I) angle-averaged S | L1 chain and validity (e) | "lab-isotropic f_χ" replaced |
| 25 | Citations to WP0 v1 numbers → WP0-v2 (CONVENTIONS precedence; brief) | throughout | (2.3) matching → (2.2); Table 2.2 → §2 table; §6.1 → §6/Table 6.1; (4.6′), (7.2), (8.1)–(8.2), (9.7) |
| 26 | WP3 O-WP3-5: confirm ALP/SOC statement of L9b(c) | §2.5, IF-5 | confirmed with triplet refinement |
| 27 | WP6 O6-2: onset exponent p near E_th | §3.6 [E10], IF-4 | derived per class, fixed q and S̄ |
| 28 | Self-found: [E7] missing complex conjugate on A^λ | [E7] | \|Σ A^{λ*}ρ\|²; WP1v2-C5a |
| 29 | Self-found: dangling "[E10]" reference in v1 §1.5 | §1.5 | → [E8]; [E10] now the onset statement |
| 30 | Self-found: [E5] properness stated loosely | §2.3 | R proper w.r.t. transverse photon only; correction O(ω_p²/q²) |
| 31 | RULES/brief: checks sympy only (v1 C3, C8 used numpy/scipy) | code/WP1-v2/checks.py | exact NSD examples; group characters for O_h, T_d (adds the T_d ℓ = 3 case) |
| 32 | Symbol hygiene vs NOTATION v3 (n band label vs principal number; α Dirac vs fine structure; Σ, σ^{μν} Dirac vs self-energy/smearing; a lattice vs operator index; ⟨v_e²⟩ vs DM v) | [E8], §5, header, L3 | n_H; ψ̂†γ⁰𝛄ψ̂; bilinear list {1, γ⁵, γ^μ, γ^μγ⁵, ½[γ^μ,γ^ν]}; a_lat; ⟨p²⟩/m_e², p_T |
| 33 | NOTATION v4 renames (CORRECTIONS §17) | §15 | none owed (checked: no v4 collision symbol occurs); §15 updated to v4, IF-9 symbols now NOTATION v4 §M rows. Notational only |

**Count:** 32 corrections applied: rows 1–19 owed by CORRECTIONS §7/§0 and NOTATION v3; rows 20–21 the WP0-v2 flags F1, F11; rows
22–25 routed from WP0-v2/WP6 defects and the precedence rule; rows 26–27 open items addressed to WP1 by WP3 and WP6; rows 28–32 self-found
(three formula/wording slips, script and symbol hygiene). Contested: 0. Row 33 (NOTATION v4 renames) is notational and outside this count.

---
## 14. Literature
Read in full text in v1 (equation numbers quoted; IDs verified against the arXiv API, 2026-10-31): 1509.01598, 2101.08275, 2101.08263,
2105.02233, 2210.14917, 2510.25835, 2104.12786, 2002.06937, 2003.12077, 2507.14345, 2509.14534, 2607.06005, 2608.20715, 2603.12326.
Re-read in full text for v2 (arXiv HTML, 2026-10-31): 2607.06005 (Eqs. (6), (10); §III Fig. 4 discussion; Migdal ℓ = 2 statement).
Abstract or text checks: 2411.03433, 2605.11063, 2501.18261, 2306.14944, 2105.05253, 2110.01587, 2608.05282. From WP0's reading:
2009.13534, 2106.12586. Local copies kept only in the session scratchpad.

---
## 15. Symbols introduced/used
All symbols follow NOTATION v4 and CONVENTIONS; **no deviations** (CORRECTIONS §17 owes WP1-v2 no rename; the IF-9 rows below are now NOTATION v4 §M rows). Used as defined there: q, q_r, G_q, ω, ω_q, Δ_χ, v, v_χ, v^⊥, v_s, v_T,
v_max, v_E^ref, v_esc, m_χ, μ_χe, σ̄_e, F_DM, Ṽ, 𝒪_i, 𝔇, 𝒱_a, 𝐒_χ, j_χ, e_χ, ρ_χ, ρ_T, f_χ, η, 𝒢, Γ_χ; Ω, N, V, e² = 4πα, α, v_C, k_c, E_g,
E_dir, E_min(q), ε_{nk}, ψ_{nk}, ρ_cv, n, m, v, c (band subscripts), p, p_nn, j_e^α, j_L, j_T, J_T, s_e^α, O_a, Γ, T_e, ⟨T⟩, δ_rel, H, 𝒵;
S, S_ab, S̄, S^{prop}, S_ℓm, S(q,ω;Λ), R, R̃, R⁰, Π^γ_T, ε, ε_{GG′}, ε̃, ε₁, ε₂, ε_e, ε_mac, ε_Lin, ε_Mer, ε_L, ε_T, ε_∞, ε₀, L, L_ch, K_n^{(ch)},
𝓜¹, ω_p, ω_{p,e}, f_xc, f_xc^T, f_Hxc, G_LF, W^{scr}, A^λ_{cvk}, E_λ, H^{exc}, λ, E_x, E_x^b, a_x, μ_x, Q_x, 𝒮_F, ζ_S, L^{BSE}, Ξ^{BSE},
ω_pl, w_pl, q_c, Y_ℓm, K^cub_ℓ, ℓ, v_F, k_F, k_TF, γ_rel, Δ_SO, Δ_scis, Z_κ, κ_BO, η_xc, η_ep, ω_T, ω_max (CONVENTIONS §10),
𝓃_e, τ, n_B, 𝒳, Δ^τ_k, r^M_k, θ_k, GS, X0, X+, Λ, p_on, E_th, 𝐛_NR (by reference), m_A (by reference).
Introduced here (new objects, no collision; NOTATION v4 §M rows, requested as IF-9): **a_lat** (lattice constant), **n_H** (hydrogenic principal
quantum number in [E8]), **α_χ ≡ e_χ²/4π** (L11), **k_v** (VBM crystal momentum, companion of k_c), **ψ̂(r)** (electron field operator,
§5.1), **α_LRC** (strength of the LRC xc kernel, §1.2), **p_T** (electron momentum transverse to q̂, L3 (c)); **E_min,0(|q|)** (minimum of E_min(q) over q̂ at fixed |q|) and **δq̂** (angular
offset of q̂ from that minimum), §3.6.
Labels (not symbols): BSW irreps Γ₂₅′, Δ₁, Δ₂′, Δ₅, Λ₁, Λ₃, L₁, Δ₆, Δ₇ and BZ points X, L; point groups O_h, T_d, C₄ᵥ, C₃ᵥ.
Source-only notation appears only inside quotes with its campaign map stated (χ → R, v_⊥ → v_T, W_l/B_l → 𝒲̄_l/B^{Cat}_l, T_ℓm → S_ℓm,
ε_M → ε_mac, L/Ξ/W → L^{BSE}/Ξ^{BSE}/W^{scr}, F_φ → F_DM, Γ (Mermin) → γ_rel, E_e → ω, V_cell → Ω, n_{−k} → n_q with q = −k).
Labels from this return: [E1]–[E12], WP1v2-C1…C12, IF-1…IF-9.
