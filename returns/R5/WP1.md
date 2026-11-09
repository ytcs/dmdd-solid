# R5 / WP1: electronic sector at clamped nuclei

Isolated theory agent. Read scope as briefed. Theory only. Identity and number checks are in `code/WP1/checks.py`
(C1–C8, all PASS, < 30 s). `code/WP1/html2txt.py` converts arXiv HTML to text for quoting. Every arXiv ID cited was
verified against the arXiv API on 2026-10-31 (§11). Source formulas are quoted from FULL TEXT (fetched to
`literature/papers-WP1/`; PDFs deleted at the end). Tags: **[D]** DERIVED (hypotheses stated), **[E]** ESTIMATED,
**[C]** CONJECTURED. WP0 equations are cited as WP0 (s.n). This return's equations are numbered [E1], [E2], …
Notation follows NOTATION v2 = WP0 §10: R is the retarded response, ε_{GG′} is WP0 (5.2), and the DM vertex sits at the
unreduced q (q = q_r + G_q with q_r ∈ 1BZ). Si/Ge numbers: a = 5.431/5.658 Å, E_g(0) = 1.170/0.744 eV.

---
## 1. The sector and the kernel ladder

**1.1 Clamped nuclei [D].** The clamped-nucleus sector is n_B = 0 in τ (WP0 §6.1): R̃_{eκ} = R̃_{κκ} = 0, so ε = ε_e. Then
WP0 (5.3) holds with c = e only, and WP0 (5.4) and (5.5)(i) give, exactly at this level,

  S_ee(q,ω) = (2q²/e²)(1−e^{−βω})^{-1} Im[−(ε^{-1})_{G_qG_q}(q_r,ω)],   ε_{GG′} = δ_{GG′} − v_{q_r+G} R̃_{GG′}.          [E1]

This is the X0 sector of Theorem D at zero e–ph order. ZPR, PAER and the Debye–Waller (FC) reduction belong to WP3.

**1.2 The ladder: truncations of R̃ (WP0 (5.1)) [D as definitions].** R̃ is irreducible with respect to every Coulomb line of
the external channel {q_r+G}. Each rung below is an approximation to R̃ alone. Writing R⁰ for the KS (or QP) pair bubble:

| X | R̃ used in [E1] | what it adds | exact relations kept (local H) |
|---|---|---|---|
| IP | none: S = −2Im R⁰_{G_qG_q} (no Dyson) | — | f-sum, positivity; KK for R⁰ (not for the ELF) |
| RPA | R⁰, diagonal G only | 1/\|ε_{G_qG_q}\|² screening | f-sum, KK, positivity |
| RPA+LFE | R⁰, full GG′ matrix | microscopic inhomogeneity | the same + static ε_M ≥ 1 ([E3]) |
| TDDFT | R̃ = R⁰ + R⁰ f_xc R̃ | xc vertex (ALDA, LRC −α/\|q+G\|², bootstrap) | the same, if f_xc is ω-independent |
| BSE | R̃ = −iL contracted, kernel Ξ = −W only (exchange v restored by ε) | e–h attraction (excitons) | f-sum only beyond TDA and with local H_QP |

The BSE row is consistent with 2507.14345: there L = L⁰ + L⁰ΞL carries Ξ = v − W, and then ε^{-1} = 1 + vχ. Moving the v part
of Ξ into ε is the WP0 (5.1) bookkeeping. Removing W gives back their RPA. **[D]**

**1.3 Exact amplitude form (final-state resolved) [D].** By (C3b), Im R = (1+Rv) Im R⁰ (1+Rv)†. At RPA(+LFE) level the
pair-resolved response is

  S(q,ω;cvk) = (4π/V)|Σ_G (1+Rv)_{G_q G}(q_r,ω) ρ_cv(k, q_r+G)|² δ(ω − ε_{c,k+q} + ε_{vk}).                                  [E2]

When R_{GG′} = R_{G′G} (time reversal plus inversion, as in Si and Ge), (1+Rv)_{0G} = (ε^{-1})_{G0} (C3c), which is WP0 (7.2).
In GaAs (no inversion) the weight must be written as in [E2].

**1.4 Static stability (closes WP0 O5 at RPA+LFE) [D].** Hypotheses: an insulator with a static KS response R⁰(q,0) that is
Hermitian and negative semidefinite, and the RPA kernel. Write X = v^{1/2}R⁰v^{1/2} ≤ 0. Then v^{1/2}Rv^{1/2} = X(1−X)^{-1} has
eigenvalues λ/(1−λ) ∈ (−1,0], so

  0 < (ε^{-1})_{00}(q,0) ≤ 1   ⇔   ε_M(q,0) ≥ 1   (all q, LFE included; check C3).                                   [E3]

Beyond RPA this needs 1 − (v+f_xc)R⁰ > 0. That fails only near a compressibility instability (HEG r_s > 5.25). Si and Ge have
r_s ≈ 2.0 (C4), so the conservative L17 step holds for them **[E beyond RPA]**.

**1.5 Rung increments as nuisances (WP0 (8.1)) [E, Si/Ge].**

| Increment | Size in Si/Ge |
|---|---|
| Δ_RPA−IP | factor 1/\|ε\|² ≈ 0.1 at q = 2 keV and ≈ 0.44 at q = αm_e (ω ≈ 5 eV; Cappellini model with EXCEED-DM parameters ε₀ = 11.3, q_TF = 4.13 keV, ω_p = 16.6 eV). This is the ×1.4–2.5 of 2101.08275 |
| Δ_LFE | −20…−50% (2603.12326) |
| Δ_ALDA | few % at eV ω (ALDA has no e–h binding) |
| Δ_BSE | +30…+100% within ~1 eV of E_min(q) ([E10]) |

The ladder is not an expansion (η_xc ~ 0.2–0.5), so Δ_X must be computed (G5 spec), not estimated.

---
## 2. Non-density operators in the medium (G10; L3 chain)

**2.1 Continuity [D] (C1).** For j = ½{p/m, e^{iq·r}} (WP0 Table 2.2), [T, n(q)] = q·j(q) exactly, with no extra (q²/2m)n term
(WP0 defect D1, §9). For local H: ⟨f|q·j|i⟩ = (E_f−E_i)⟨f|n|i⟩, so S_{n j_L} = (ω/q)S_nn and S_{j_L j_L} = (ω/q)²S_nn, screened
or not.

**2.2 On-shell projection theorem [D].** Hypotheses: the WP0 (2.3) matching with v^⊥ = v_χ − v_ψ and v_χ = v − q/2m_χ, local H,
Born, and elastic DM (Δ_χ = 0). Then q·v_χ = q·v − q²/2m_χ = ω_q (WP0 (2.1)). By §2.1, q·j acts as ω on shell. So
(q·v^⊥) n ≐ (ω_q − ω) n = 0 on δ(ω − ω_q). Hence **only the transverse projection P_T = 1 − q̂q̂ of v^⊥ survives in any rate**: the
DM side keeps P_T v_χ, and the target side keeps j_T. For O₈ this gives

  Tr FF†(O₈) → ¼[ |P_Tv_χ|² S_nn − 2Re (P_Tv_χ)·S_{n j_T} + tr S_{j_T j_T} ].                [E4]

The same holds for O₃, O₅, O₇, O₁₂–O₁₅ through the spin-current rows (J_T). This is the in-medium form of Galilean invariance.

**2.3 Transverse response [D].** Per transverse polarisation, with Π_T = e²(R_{j_Tj_T} + n/m) proper with respect to the
transverse photon and ε_T = 1 − Π_T/ω²,

  S_{j_Tj_T}(q,ω) = (2ω²/e²) Im ε_T(q,ω)/(1−e^{−βω}),   tr S_{j_Tj_T} = (4ω²/e²) Im ε_T.                                   [E5]

Screening of j_T has two parts:
- through the transverse photon, a relative correction O(ω_p²/q²) ≈ 2×10⁻⁵ at q = 4 keV, so negligible;
- **through local fields**: j_T(q) couples to n(q+G) for G ≠ 0, so R̃_{j_T, n(q_r+G)} ≠ 0 and j_T is screened at LFE strength
  (≈10–30% [E]). WP0 (5.3) "transverse currents unscreened" holds only without LFE (defect D4).

For a dark photon (total charge), WP0 (3.6) with the transverse 𝒟 gives the sum L + |v^⊥|² Im[−q²/(ω²ε_T − q²)]. This is
2608.20715 Eq. (2) [FT] for a massless or light mediator. **[D]**

**2.4 Spin and spin-current channels [D].** Take SOC = 0 and a spin-unpolarised reference. The charge (singlet) and spin
(triplet) channels then decouple, and Coulomb lines enter only the singlet. So

  S_{s^as^b}(q,ω) = (δ_ab/4) S_nn^{IP}(q,ω)  at IP, with NO 1/|ε|² ;   beyond IP: R̃_s = R⁰ + R⁰ f_xc^{T} R̃_s,  f_xc^T = (f_↑↑ − f_↑↓)/2.  [E6]

So the *unscreened* crystal form factor (L1) is the correct IP response for O₄-type electron-spin couplings. f_xc^T < 0 gives an
exchange (Stoner-like) enhancement, about +10–20% for r_s ≈ 2 **[E]**. In the BSE it removes the exchange term, so triplet
excitons lie below singlets (§3). With SOC, R̃_{s,n} ≠ 0 at O(Δ_SO/E) and the channels mix: Si Δ_SO = 44 meV gives ≲ 2%
in amplitude, Ge Δ_SO = 0.29 eV gives ≲ 10%, near the edge **[E]**. EXCEED-DM 2210.14917 Eq. (68)–(71) [FT] states "there is no
screening" for the axial coupling σ_e. The URF agrees at Hartree level, but the triplet f_xc and the SOC mixing are missing there.

**2.5 Minimal response set (SOC = 0, unpolarised) [D].** Every NR-EFT electron rate (all O_i, any mediator) needs only
- the singlet blocks: L (ELF, screened), S_{n j_T} (2-vector, LFE-screened) and S_{j_Tj_T} (2×2: symmetric part from [E5],
  antisymmetric part = Catena W₅);
- the triplet blocks: S_nn^{IP}, S_{n j_T}^{IP} and S_{j_Tj_T}^{IP} with the f_xc^T dressing.

Longitudinal currents are not independent (§2.1). Seven real functions per (q,ω) on the IBZ ⊗ G grid. This is the G10 table.

---
## 3. Excitons, including dark and indirect ones, at finite q (exciton gaps; L14)

**3.1 Finite-q BSE contribution [D].** Hypotheses: QP bands, static W, a pair basis at total momentum q_r, and Hamiltonian
H^{exc}(q_r)A^λ = E_λA^λ including coupling (beyond TDA). The singlet poles of the full R give

  S^{BSE}(q,ω) = (4π/V) Σ_λ |Σ_{cvk} A^λ_{cvk}(q_r) ρ_cv(k, q)|² δ(ω − E_λ(q_r))   (TDA form; beyond TDA use the pseudo-norm).          [E7]

Exchange (v_{q+G}) is in H^{exc}, which makes [E7] the screened (ELF) quantity. Spin factor: |⟨S|n_q|0⟩|² = 2|Σ Aρ|², and triplet
excitons give zero to S_nn.

**3.2 Selection rules at finite q [D].**
- (a) **Spin.** Density excites only singlets. Spin operators (O₄, O₆, O₉, O₁₀ …) excite triplets, which lie lower by the exchange
  splitting. They are dark to n and bright to s (new channel; [E6]).
- (b) **Momentum.** An indirect exciton with Q_x = k_c − k_v is optically dark but DM-bright at q = Q_x + G, as a zero-phonon
  process.
- (c) **Point group at the extrema (C7).** The rule is set by the little group of q acting on the VBM (Γ₂₅′) and CBM states:
  - **Si**, CBM Δ₁ at 0.85X, G = 0 so q ∥ [100]: Γ₂₅′ → Δ₂′ ⊕ Δ₅ contains no Δ₁, so ρ_cv(Γ→Δ₁, q∥Δ) = 0. The transition is
    "second class": the continuum goes as (ω−E_min)^{3/2} at fixed q, and only p-excitons are bright. Umklapp G = (1̄11) gives
    q off-axis (|q| = 3.25 keV) and is allowed. SOC (Δ₆/Δ₇ double group) lifts the zero at O(Δ_SO/E_g) ≈ 4% in amplitude.
  - **Ge**, Γ₂₅′ → Λ₁ ⊕ Λ₃ under C₃ᵥ contains L₁, so the G = 0 transition (q ∥ [111], |q| = 1.90 keV) is allowed.
  - These rules apply also to the zero-phonon line that competes with PAER (pointer to WP3/M1: the Si ZPL near threshold is
    (δk)²-suppressed).

**3.3 Wannier limit of [E7] [D for parabolic bands with constant ε_∞; E for Si/Ge].** Take allowed class with exciton radius a_x
and binding E_b. Then

  S_x(q,ω) = 4π|ρ_cv(k_v,q)|² [ Σ_n δ(ω − E_min(q) + E_b/n²)/(πa_x³n³) + (2μ_x)^{3/2}√(ω−E_min)/(4π²) · S_F(ω) ],  S_F = (2πκ)/(1−e^{−2πκ}), κ = √(E_b/(ω−E_min)).   [E8]

Here E_min(q) = min_k[ε_{c,k+q} − ε_{vk}]. For second class, replace |ρ|²/(πa_x³n³) by |∇_kρ|²(n²−1)/(πa_x⁵n⁵) and S_F by its
l = 1 form.

Two consequences (C5):
- The total bound weight equals the free-continuum weight within 8.0 E_b of the edge.
- S_F = 6.3, 2.3, 1.7 and 1.35 at ω − E_min = 1, 10, 30 and 100 E_b. Si (E_b = 14.7 meV) therefore still has +35% at 1.5 eV.

**Prediction [E]:** the survey estimate "< 10% except within 0.1 eV" (catalog-analysis G5/G11) is too small for Si/Ge. Near-edge
singlet S is enhanced by 1.3–2 over RPA for ω ≲ E_min + 1 eV, partly offset by LFE (opposite sign). This is consistent in sign
with 2507.14345 (BSE > RPA at low ω for both GaAs and NaI).

**3.4 Kinematic thresholds for direct indirect-exciton creation (C6) [D given v_max = v_esc + v_E = 794 km/s].**
m_χ ≥ |q|²/[2(|q|v_max − E_x)]:

| Case | |q| | m_χ,min | class |
|---|---|---|---|
| Si, G = 0 | 1.94 keV | 0.473 MeV | forbidden |
| Si, G = 1̄11 | 3.25 keV | 0.708 MeV | allowed |
| Ge, G = 0 | 1.90 keV | 0.420 MeV | allowed |

So in Si the zero-phonon exciton line opens at the upper end of the PAER-only window (0.34–0.47 MeV, SOTA), and it opens there
suppressed. This is the boundary WP3 must use.

**3.5 Core excitons [E].** Ge 3d → CB at ≈ 29.5 eV + E_g carries a core-hole BSE (2507.14345 SM Fig. S3: the BSE onset of Ga 3d
lies below RPA and is more peaked). It needs SOC (3d₅/₂–3d₃/₂ split 0.58 eV) and is handed to WP5 as Λ = core-hole.

---
## 4. Homogeneous electron gas and plasmons (L10, L11)

**4.1 HEG limit [D].** Jellium (V_eN → uniform background), plane-wave KS states, X = RPA: [E1] becomes the Lindhard ELF. The
Lindhard e–h continuum is ω ∈ [max(0, q²/2m − qv_F), qv_F + q²/2m]. Spin [E6] gives S_ss = ¼S^{Lindhard,unscr}. [E5] gives
Π_T^{jj}, which matches 2608.20715 Eq. (13) in structure. Si valence numbers (C4): r_s = 2.01, k_F = 3.57 keV, v_F = 6.98×10⁻³,
ω_p = 16.6 eV.

**4.2 Plasmon [D, small-q RPA].** At the zero of ε₁ with ε₂ → 0, Im[−1/ε] = π δ(ω−ω_pl)/∂_ωε₁. With
ε₁ = 1 − ω_p²/ω² − (3/5)ω_p²q²v_F²/ω⁴ (2003.12077 Eq. (5)) this gives

  L_pl(q,ω) = (π ω_p²/2ω_pl) F(q) δ(ω − ω_pl(q)),  ω_pl² = ω_p² + (3/5)q²v_F²,  F = 1 + O(q⁴) (C4),                    [E9]

so the pole carries the full f-sum WP0 (9.5) to O(q²). The Landau onset (ω_pl = qv_F + q²/2m) is at **q_c = 1.88 keV for Si**.
Reaching ω_p needs q ≥ ω_p/v_max = 6.3 keV > q_c, so **no bulk plasmon is produced by halo DM** in the electronic sector **[D]**.
In real Si the 16.6 eV plasmon sits inside the interband continuum (width 3–4 eV). By [E2] its final states are e–h pairs with
branching 1 at clamped nuclei. Any plasmon → phonon branching is X+ (WP3) and is suppressed by η_ep **[E]**.

---
## 5. Core and relativistic states (G7; the factorisation question of 2509.14534)

**5.1 Factorisation theorem [D].** Hypotheses: Born in H_int; a 4-component (no-pair) target Hamiltonian; DM–electron contact
or mediator interactions written as Dirac bilinears ψ̄Γψ. Then WP0 (3.3) holds unchanged with the target operator set
extended to

  O_Γ(q) = ∫d³r ψ†(r)γ⁰Γ e^{iq·r}ψ(r),   Γ ∈ {1, γ⁰, γ^i, γ⁰γ^i, γ⁵, γ⁰γ⁵, Σ^i, …}  (16 bilinears),

and 𝔇 is built from the DM bilinears. The rate is tr(𝔇S) exactly, at Born level. It "factorises" into a single scalar K-factor
only if one target operator survives. That is the case for scalar and pseudoscalar couplings, which is the 2509.14534 finding.
Vector and axial couplings give a matrix S (density + current; spin + spin-current), which is already the WP0 multi-operator
structure.

The "off-shell bound electron with free kinematics" problem of 2509.14534 is an artefact of matching NR-EFT with *free on-shell
spinors*. Matching at the operator level (field theory) has no kinematic assumption on the electron: p_i stays an operator, as in
WP0 Table 2.2. **The URF answer: factorisation of DM physics from target physics is exact. Factorisation into "free amplitude ×
scalar form factor" is valid only for the n row (and s) at O(v_e⁰).**

**5.2 Foldy–Wouthuysen reduction [D to O(1/m²)].**
- ψ†ψ → n(q)(1 − q²/8m²) + (i/4m²) Σ σ·(q × p)e^{iq·r} (picture change).
- ψ̄ψ → n − (1/2m²)Σ{p², e^{iq·r}}/2 + ….
- ψ†αψ → j + spin-curl (i/2m)q × s.

So the 16-row NR basis of WP0 is the O(v_e¹) truncation. The corrections are O(⟨v_e²⟩), with these sizes **[E]**:

| Shell | ⟨v_e²⟩ |
|---|---|
| Si 1s | (Zα)² = 0.010 |
| Ge 1s | (Zα)² = 0.055 |
| Ge 3d | ~10⁻³ (SO split/binding = 0.58/29.5 = 0.02) |
| valence | α² ~ 5×10⁻⁵ |

**5.3 Relativistic f-sum [D] (C2).** Hypotheses: Breit–Pauli one-body terms and closed shells.
- Darwin is multiplicative, so it adds nothing.
- SOC is linear in p, so its double commutator vanishes identically.
- Only mass-velocity contributes:

  M¹_ee = (n_e q²/m)[1 − (5/3)⟨T⟩/m − q²/4m² + O(1/m⁴)],   ⟨T⟩ = mean kinetic energy per electron.                   [E11]

With all electrons: Si −0.18%, Ge −0.58% (1s alone −4.5%). This corrects WP0 (1.2)/(4.6) (defect D2). In 4-component theory without
no-pair projection the double commutator vanishes (H_D is linear in p). The NR f-sum is restored only by the negative-energy
(Z-graph) states, so codes using Dirac core states must project.

**5.4 What dominates G7 for halo DM [E].** ω ≤ ½m_χv_max² = 3.5 keV × (m_χ/GeV). Ge 1s (11.1 keV) is unreachable, and Ge 2p
(1.2 keV) is reachable only for m_χ ≳ 0.35 GeV. **The Ge 3d band is the G7 shell.** Ranked by size:
- XC placement of the 3d band: 4.5 eV (2306.14944);
- core-hole/core-exciton final state (§3.5);
- SOC split of 0.58 eV;
- scalar-relativistic and operator corrections, ≲ 10⁻³–2×10⁻².

The relativistic 30–50% of 2509.14534 [ABS-level claim, read in FT: Coulomb wavefunctions with an effective charge] does not
carry over to Ge 3d at halo kinematics. Its large-q statement survives as a Dirac r^{γ−1} cusp: |ψ̃(q)|² gains
(q/Zαm)^{(Zα)²}, which is ≈ +13% for Ge 1s at q = 10Zαm.

---
## 6. Anisotropy and modulation (L19 electronic; G11)

**6.1 Symmetry theorems [D].** Hypotheses: nonmagnetic, TR-invariant reference, any T.
- (i) WP0 (4.3) with TR gives S(q,ω) = S(−q,ω). **Every odd-ℓ multipole of S, and of L, vanishes identically.**
- (ii) For point group O_h or T_d (Si, Ge, GaAs, diamond), ℓ = 2 contains no A₁ (C8). The first anisotropic multipole is
  ℓ = 4 (then 6, 8, …). The ELF of a cubic crystal is isotropic through quadrupole order.
- (iii) With the multipole pairing of 2607.06005 (their Eq. (10)), the ER rate R(t) = Σ_{ℓ even} T_ℓm 𝓡^{(ℓ)}(t) f̂_ℓm. The
  dipole-vertex Migdal response contains only ℓ = 0, 2 (their Eq. for W_ℓm with (q̂·k̂)²). So **in cubic crystals the ELF
  anisotropy produces no daily modulation of the dipole Migdal rate at all**. A residual can come only from beyond-dipole vertex
  terms (q·r)⁴ or from anisotropy of the nuclear S (WP2/WP3).

**6.2 Consequence for the literature.** 2607.06005 states that the 5 eV ER modulation in Si/GaAs "originates primarily from the
dipole component". By (i) that component is zero; any ℓ = 1 in a computed ELF is a numerical artefact (IBZ reconstruction,
broadening, finite q_cut). A one-sidereal-day harmonic is still allowed, from ℓ = 4 along a tilted v_lab cone. Their reported
"Migdal modulation" in Si/GaAs must also vanish by (ii)–(iii) up to numerical noise. Both are sharp diagnostics for any code.

---
## 7. LIMITS entries

### L1: Essig et al. crystal form factor (1509.01598)
- **Source [FT]:** Eq. (17) dR/dlnE_e = (ρ_χ/m_χ)N_cell σ̄_e α (m_e²/μ²) ∫dlnq (E_e/q) η F_DM² |f_crystal|². Eq. (21):
  |f_crystal|² = (2π²(αm_e²V_cell)^{-1}/E_e) Σ_{ii′}∫_BZ (V_cell d³k/(2π)³)(V_cell d³k′/(2π)³) E_e δ(E_e−E_{i′k′}+E_{ik})
  Σ_{G′} q δ(q−|k′−k+G′|)|f_{[ik,i′k′,G′]}|². The spin 2 is inside 2π² (Eq. (60)).
- **Chain [D]:** WP0 (3.3) → (9.1) single n row → (9.2) isotropic η/2q → [E1] at X = IP (WP0 (7.2) without ε) → angular average.
  Derived dictionary:

  |f_crystal(q,E)|² = (Ω q³/4παm_e²) S̄^{IP}_ee(q,E) = (Ω q⁵/8π²α²m_e²) ε̄₂^{noLFE}(q,E).                                  [E12]

  The second equality is exactly 2101.08275 Eq. (16) [FT], an independent check. Inserting [E12] in Eq. (17) reproduces WP0 (9.2)
  term by term, including spin 2 and η/2q. **This closes SOTA #7 (Essig prefactor): CROSS-CHECKED.**
- **Validity:** (a) |ε|² ≈ 1, which needs q ≫ q_TF·(…). In Si 1/|ε|² ≈ 0.1 at 2 keV and 0.44 at αm_e (§1.5), so L1 overestimates by ×1.4–2.5. · (b) T ≪ E_g. · (c) pseudo-wavefunctions, accurate only to q ≲ 6–8 αm_e (2603.12326). · (d) scissor shifts energies but not ρ_cv, so the f-sum is violated by +Δ_sc Σ|ρ|², about +3.5% in Si [E]. · (e) lab-isotropic f_χ (L19 ~1%).
- **Leading correction [D]:** within RPA without LFE the correction is exactly multiplicative, S = S^{IP}/|ε_{G_qG_q}|²
  (Im R = Im R⁰/|ε|²), then Δ_LFE and Δ_BSE ([E8]).
- **Discrepancies:** 2105.02233 Eq. (80) re-quotes Eq. (21) with δ(ΔE − E_{ik} + E_{i′k′}), which has the sign of the energy argument flipped; the same holds in their Eqs. (37) and (47). Typographic. · QEdark f_crystal is spin-summed, while Catena's W̄₁ = 8ΔEαm_e²|f_crys|²/q³ (Eq. (81)) is per spin with the 2 carried in their Eq. (6). Both are consistent.

### L2: dielectric/ELF rate (2101.08275, 2101.08263)
- **Source [FT]:** 2101.08275 Eq. (6): S(ω,k) = (k²/2πα)(1−e^{−βω})^{-1} Im[−1/ε_L(ω,k)]. Eq. (13) is the rate, with S defined with n_{−k} (Eq. (4)). · 2101.08263 Eq. (1): Γ(v_χ) = ∫d³q/(2π)³|V(q)|²[2(q²/e²)Im(−1/ε(q,ω_q))], at T = 0.
- **Chain [D]:** WP0 (3.3) → n row → (5.5)(i) clamped nuclei (or (ii) ω ≫ ω_max = 64 meV in Si, error O(κ_BO⁴)) → (5.4) → FDT
  (4.1). 2q²/e² = k²/2πα with e² = 4πα. X = exact or any rung. With LFE, the exact object is (ε^{-1})_{G_qG_q}(q_r,ω) [E1].
  2603.12326 Eq. (16) and 2507.14345 (ε_M = 1/ε^{-1}_{GG}) use exactly this.
- **Validity:** DM couples to electron density only. A dark photon needs the total ε (WP0 (5.4)); its ionic part is 0 in Si, and ε₀ − ε_∞ = 1.9 in GaAs only at ω ≪ ω_TO. · Electron-only coupling needs ε_e (WP0 L17 (ii)).
- **Leading corrections:** (i) KKL Appendix A works "in the approximation that ε is diagonal in G". Their "LFE" replacement ε_GG → 1/(ε^{-1})_{GG} is in fact the exact clamped result, not an approximation. · (ii) KKL Eq. (27) averages ε over directions *before* inverting. Since L = ε₂/|ε|² is nonlinear, Im(−1/ε̄) ≠ the average of Im(−1/ε). The bias is second order in the anisotropy, ℓ = 4 in cubic crystals [D]. · (iii) |v^⊥|²-weighted transverse terms for vector mediators: [E4]/[E5], ≲ 10⁻⁹ relative for halo DM. · (iv) X+ (PAER) and ZPR: WP3.
- **Discrepancies:** Hochberg et al. write ε(q,ω) with no LFE/G specification. · KKL write ⟨p,ℓ′|e^{ik·r}|p,ℓ⟩ in Eq. (15), a typo for p′. · The sign of k in n_{−k} is immaterial for TR-symmetric targets ([§6.1(i)]).

### L3: NR-EFT crystal responses (2105.02233, 2009.13534, 2210.14917, 2510.25835)
- **Source [FT]:** 2105.02233 Eq. (36): 𝓡 = (n_χN_cell/128πm_χ²m_e²)∫dlnΔE∫d³q (1/q) η̂ Σ_l Re(R_l^*W_l), with W_l (Eq. (37)) built from B₁ = |f′|², B₂ = (q/m)·f′f′*, B₃ = |f′|², B₄ = |(q/m)·f′|² and B₅ = i(q/m)·(f′×f′*) (Eqs. (38)–(42)). The vector overlap is f = ∫ψ*e^{iq·x}(i∇/m)ψ (Eq. (11)). · 2210.14917 Eq. (18) R ∝ Σ_IF∫ f_scr² F_med² g 𝓕_IF, f_scr = 1/(q̂·ε·q̂) (Eq. (23)). Axial: "Contrary to the kinetically mixed dark photon model, there is no screening" (with Eqs. (70)–(71)). · 2510.25835 Eq. (5): the rate in terms of χ₀₀, χ_ij, χ_0i. Eq. (6): dΓ₈ = (v_⊥²/4)dΓ₁, with "v_⊥ is the component of v that is perpendicular to q" (DM velocity).
- **Chain [D]:** WP0 (3.3) → IP R̃ → WP0 (5.3) screening of the rows with R̃_{ac} ≠ 0 → §2.1–2.5.
- **Results [D]:** (a) **Only 3 of Catena's 5 responses are independent.** By C1b (local H), q·f = −(ΔE − q²/2m)f, so W̄₂ = −(ΔE−q²/2m_e)W̄₁/m_e (real) and W̄₄ = (ΔE−q²/2m_e)²W̄₁/m_e². W̄₁, W̄₃ − (m²/q²)W̄₄ (transverse current) and W̄₅ (antisymmetric transverse) are independent. Their numerically small Im W̄₂ measures the nonlocal-PP violation [V_NL, n]. · (b) In medium: W̄₁, W̄₂ and W̄₄ are screened by |ε|^{-2}. The transverse W̄₃ and W̄₅ are screened by LFE only, and spin rows follow [E6]. EXCEED-DM's global f_scr is right for the n row of a dark photon. It is wrong for scalar couplings to n (which are screened too, per L2), and for current and spin rows, which do not screen with 1/(q̂·ε·q̂). · (c) **2510.25835 Eq. (6) for O₈ is the v_ψ → 0 truncation of [E4].** It omits tr S_{j_Tj_T} = (4ω²/e²)Im ε_T. The ratio is tr S_{j_Tj_T}/(|v_⊥|²S_nn) ≈ ⟨v_{e,T}²⟩/|v_⊥|² ≈ 3×10⁻⁵/7×10⁻⁷ ≈ 40 in Si valence **[E]**. Their O₈ limits are conservative by O(10). Their statement that O₈ rates are "determined entirely by the dielectric function" holds only at |v_⊥| ≫ v_e, which does not hold.
- **Validity:** SOC = 0 for the singlet/triplet split (Ge near-edge ≲ 10% mixing). For local H, all-electron or PAW-reconstructed
  states are needed, otherwise the longitudinal reductions acquire [V_NL, ·] terms.
- **Leading correction:** f_xc^T (spin), LFE on j_T, and BSE in both channels.

### L10: Lindhard/Mermin ELF (2101.08275 Eqs. (17)–(24); 2104.12786)
- **Source [FT]:** 2101.08275 Eq. (17): ε_Lin = 1 + (3ω_p²/k²v_F²)[f₁ + i f₂] with Eqs. (18)–(21). · Mermin Eq. (22): ε_Mer = 1 + (1+iΓ/ω)(ε_Lin(k,ω+iΓ)−1)/[1 + (iΓ/ω)(ε_Lin(k,ω+iΓ)−1)/(ε_Lin(k,0)−1)]. · Eq. (23): ELF = Σ_i A_i(k) Im[−1/ε_Mer(ω_{p,i},Γ_i)] θ(ω−ω_edge,i). Eq. (24): A_i(k) is renormalised by the f-sum.
- **Chain [D]:** [E1] → jellium → X = RPA → Lindhard. Mermin = relaxation-time approximation that conserves local particle
  number (continuity, §2.1). This is not a URF rung but a damping closure.
- **Validity:** ω inside the Lindhard continuum, and ω ≫ E_g. · Low ω fails: the HEG has intraband weight ∝ ω below E_g, whereas an insulator at clamped nuclei has S(ω<E_g) = 0 exactly. · The static limit fails: ε_HEG(q→0,0) = q_TF²/q² → ∞, whereas ε_M(0,0) = ε_∞ = 11.7 in Si. · Si r_s = 2.01.
- **Leading correction [D]:** the HEG xc local-field factor, ε = 1 − vΠ⁰/(1 + vG(q)Π⁰) (TDDFT rung), then band structure (gap).
- **Discrepancies:** θ(ω−ω_edge) breaks KK and the Mermin built-in f-sum, hence the renormalisation in Eq. (24). · The f-sum is restored per oscillator but KK is not; Re ε^{-1} must be regenerated, as KKL do.

### L11: plasmon production (2002.06937, 2003.12077)
- **Source [FT]:** 2003.12077 Eq. (5): ε̂_L ≈ 1 − (ω_p²/ω²)(1 + (3/5)k²v_F²/ω_p²). Eq. (7): Z_L ≈ 1 − (3/5)k²v_F²/ω_p². Cutoff k ≲ ω_p/v_F "(roughly 2.4 keV)". Eq. (8): plasmon bremsstrahlung from NR. · 2002.06937 Eq. (4): q_c ~ 2π/a ~ 5 keV. Eq. (13): P(E) = (α/π²)∫d³q q^{-2}Im{−1/ε(E,q)}δ(E − q·v + q²/2m_χ). Eq. (14): dR/dE ∝ S(E)∫₀^{q_c}dq/q η.
- **Chain [D]:** [E1] → pole of (ε^{-1}) [E9]. For a light mediator coupling to total charge, WP0 (3.3) with
  |Ṽ|² = e_χ²e²/q⁴ and (5.4) gives exactly Γ = (α_χ/π²)∫d³q L/q², which is 2002.06937 Eq. (13).
- **Validity:** Direct plasmon creation needs v ≳ ω_p/q_c ≈ 9×10⁻³ (Si), so it is out of reach for halo DM ([E9]). This agrees with both papers. · Plasmon production from NR (2003.12077) is X+/mixed, which is WP3. It is quoted here only as the source of Z_L.
- **Leading correction:** [E9] with interband damping. Si's 16.6 eV resonance lies in the e–h continuum, so there is no
  separable pole beyond q ≈ 1–2 keV.
- **Discrepancies:** Three different cutoffs: 2π/a ≈ 2.28 keV (2002.06937 quote it as 5 keV), ω_p/v_F = 2.38 keV, and the RPA Landau onset 1.88 keV (C4). 2002.06937's 5 keV overstates the plasmon phase space ×(5/1.9)² in their Eq. (14) log range. · Their Eq. (14) uses ε(E,0) up to q_c, ignoring the dispersion and the loss of pole weight. · Z_L (2003.12077) is the Coulomb-gauge field residue, not the ELF share F(q) of [E9]. These are different normalisations, and no conflict is claimed.

### L14: BSE exciton rate (2507.14345)
- **Source [FT]:** Eq. (1): R = (1/ρ_T)(ρ_χ/m_χ)(π/α)(σ̄_e/μ²)∫d³v f∫d³k/(2π)³ k²|F_φ|²∫dω/2π (1−e^{−βω})^{-1}Im[−1/ε(ω,k)]δ(…). · Eq. (2): L = L⁰ + L⁰ΞL, Ξ = −iδδv + iδδW(ω=0), in TDA, with ε_M(k=q+G) = 1/ε^{-1}_{GG}(q,ω).
- **Chain [D]:** [E1] with X = BSE (§1.2) → [E7]. Eq. (1) is L2 with the BSE ELF.
- **Validity:** Static W (dynamical corrections O(E_b/ω_p)). · TDA, which breaks the f-sum (WP0 (4.6)) and KK; the error grows toward the plasmon (the authors find a NaI change beyond TDA). · Scissor QP, which breaks the f-sum by Δ_sc (L1 (d)). · 10 CBs (their Fig. S2: the ELF decreases with more CBs, so ε₁ is unconverged). · 6³ k-grid, which cannot resolve Wannier excitons with a_x ≫ a (Si 4.9 nm, GaAs 11.6 nm): only the Sommerfeld continuum part of [E8] is captured, not the bound lines. · Isotropic average.
- **Leading correction:** beyond-TDA coupling (restores the f-sum); · the bound-state lines [E8]; · the selection rules §3.2; · exciton–phonon replicas (WP3: replace the e–h final state in D2 eq. 2.1 by A^λ).
- **Discrepancy:** their F_φ is written α²m_e²/k², which is (αm_e)²/k², so it is consistent. None of substance.

### L17 (electronic part, with WP0 §9.2)
WP0 derived the bound. WP1 adds which rungs preserve its ingredients. Using the table of §1.2:
- (a) The f-sum (9.5) holds for IP, RPA(±LFE) and adiabatic TDDFT with local H.
- (b) It is broken by scissor (+Δ_scΣ|ρ|²), nonlocal PPs, TDA-BSE, and relativistic cores without no-pair projection ([E11]).
  A truncated S can therefore exceed (9.6) by these amounts.
- (c) The hypothesis ε(q,0) ≥ 1 is **DERIVED at RPA+LFE for any insulator** [E3].
- (d) The relativistic correction to ω_{p,e}² is −0.18% (Si) and −0.58% (Ge) [E11].

### L19 (electronic part): daily modulation from the anisotropic ELF (2607.06005; lattice 2411.03433 → WP2)
- **Source [FT]:** 2607.06005 Eq. (6): dR/dω ∼ ∫d³q F(q²)/q ∫dω_q T(q,ω_q,ω) f̂(s + v_lab·q̂, q̂). · Eq. (10): dR/dω ∼ ∫dq qF∫dω_q Σ T_ℓm(q,ω_q,ω)𝓡^{(ℓ)}_{mm′}(t)f̂_ℓm′, with T = L for ER. · Text: "the only anisotropic contribution [to Migdal] is from the quadrupole term (ℓ = 2)".
- **Chain [D]:** WP0 (3.4) without angular average, crystal axes fixed in the lab; [E1] for S.
- **Validity:** the response is static on the sidereal time scale (trivially true).
- **Leading correction / content [D]:** §6.1: odd ℓ ≡ 0 (TR); · no ℓ = 2 in cubic crystals, so the first term is ℓ = 4; · zero dipole-Migdal ELF modulation in Si, Ge and GaAs.
- **Discrepancy:** the "dipole component" attribution (§6.2). Their ≈ 1% ER modulation is consistent with an ℓ = 4-only response.

---
## 8. Gaps: formula and computation specification

**G5 (screening and many-body beyond RPA).**
- **Formula:** [E1] with X = BSE beyond TDA, [E7], assembled as a composite:

  S = S^{BSE}(q ≤ q_B, ω ≤ ω_B) ⊕ S^{RPA+LFE}(elsewhere),   matched on a strip by the f-sum (WP0 (8.2)).

  q_B ≈ 10 keV, ω_B ≈ E_g + 10 eV.
- **Spec:** Codes: QE/PBE (or exciting all-electron) → G₀W₀ (BerkeleyGW or Yambo) for QP and W → finite-Q BSE (BerkeleyGW finite-Q, Yambo q ≠ 0, or exciting). · Pair basis: 4 VB (Ge: + 3d separately, §G7) × 12 CB. · Grids: coarse 8³ kernel, interpolated to a fine 24³ k-grid (resolves 50 meV continuum structure). · Bound lines: added analytically by [E8], with ab initio μ_x, ε_∞ and ρ_cv(k_v,q) at the extrema. · Momentum points: q_r on the 24³ commensurate set, and G-shells with |q| ≤ q_B (≈ 10³ (q_r,G) points after O_h reduction). · Solver: Haydock/Lanczos (≈ 200 iterations). Coupling (non-TDA) is checked against the f-sum to < 1%. · Cost per q_r: N_pair ≈ 24³·48 ≈ 6.6×10⁵, about 200N² ≈ 10¹⁴ flop → node-hours. Total about 10³ node-h. · Validation: Si NIXS/EELS at q < 3αm_e (as 2603.12326). · Outputs: L(q,ω) on (q̂, |q|, ω) bins, and the nuisance Δ_BSE = S^{BSE} − S^{RPA+LFE}.

**G7 (core, all-electron, relativistic).**
- **Formula:** [E1] + [E7] with 4-component or ZORA states, FW-corrected operators §5.2, and [E11] as the check. The factorisation
  answer is §5.1.
- **Spec:** All-electron FLAPW (exciting or WIEN2k) with SOC in second variation, or PAW plus core reconstruction (EXCEED-DM). This is done for Ge (3d), Ga (3d), Si (2p for m_χ ≳ GeV). · 3d binding: PBE vs HSE06 vs G₀W₀ vs ΔSCF core hole, with the spread taken as the nuisance (target: the 29.5 eV measured value). · Core-level BSE at finite q (exciting XANES-type), 3d₅/₂/3d₃/₂ resolved. · Grid: q ≤ 30 keV, ω ≤ 200 eV, 12³ k. · Outputs: S^{core}(q,ω), the core-hole fraction for WP5, and the relativistic f-sum check.
- **Remaining gap:** no ab initio crystal 4-component response code with no-pair projection at finite q exists. ZORA + SOC is
  the practical limit; the error is O(⟨v²⟩) ≲ 2% for Ge 3d **[E]**.

**G10 (non-density operators).**
- **Formula:** §2.5, [E4]–[E6]. The 7-function table: L, S_{nj_T}, S^{sym/anti}_{j_Tj_T}, plus the triplet IP blocks with f_xc^T.
- **Spec:** Codes: QE/EXCEED-DM-type IP module. Vertices: ρ_cv(k,q+G) and the velocity vertex ⟨c|½{p,e^{iq·r}}|v⟩/m with the nonlocal-PP commutator correction (or PAW). · Screening: RPA+LFE Dyson with the mixed blocks R̃_{j_T,n(q+G)}. Spin: ALDA f_xc^T. · Grids: as QCDark2 (10³ k, q ≤ 25αm_e, q_LFE ≈ 8αm_e). · Cost: ≈ 3× an RPA+LFE ELF run. · Outputs: tables in a versioned library (WP6). These enable recasts of every O_i, including O₈ (fixing 2510.25835) and intermediate mediators (2605.11063 enter only through F_DM in 𝔇).

**G11 (anisotropy, electronic).**
- **Formula:** §6.1 and the 2607.06005 Eq. (10) pairing, with T_ℓm restricted to even ℓ and cubic harmonics (ℓ = 0, 4, 6, 8).
- **Spec:** Codes: full-q (IBZ + symmetry) RPA+LFE ELF (GPAW, QCDark2 or BerkeleyGW epsilon), projected on the K_ℓ cubic harmonics up to ℓ = 8, per (|q|, ω). · Diagnostics: |T_{1m}|, |T_{2m}| / T₀₀ < 10⁻³ (pure noise). · Outputs: T_{4},T_{6},T_{8}(|q|,ω) for Si/Ge/GaAs, and the modulation amplitude A(t) for a given site latitude.

**Exciton gaps (catalog-processes §12 item 3).**
- **Formulas:** [E7] (finite-q BSE), [E8] (bound lines plus Sommerfeld, allowed and forbidden classes), §3.2 (spin, momentum and
  point-group rules), §3.4 (thresholds), [E6] plus BSE without exchange (triplet, spin-coupled DM).
- **Spec:** as G5, plus: Si exciton at q = 0.85X + G and Ge at L + G; · the effective-mass hydrogenic series with ab initio anisotropic masses (Si m_l = 0.92, m_t = 0.19, Lipari–Baldereschi); · ρ_cv and ∇_kρ_cv at the extrema from DFT.
- **Remaining gaps:** exciton–phonon replicas (WP3, X+ with an exciton final state); · Frenkel/self-trapped excitons in NaI (lattice relaxation, which needs WP3/WP5); · beyond-TDA finite-q BSE has never been run for DM.

---
## 9. WP0 defects
- **D1.** In (4.6) and (5.3), "[H,n_s(q)] = q·j_s + (q²/2m_s)n_s" and "q·j_L = [H,n] − (q²/2m)n" are inconsistent with
  j = ½{p/m, e^{iq·r}} (Table 2.2). The correct identity is [T,n] = q·j (C1). WP0's own (9.1)(α) uses the correct form.
  Consequences: none for (4.6) or the f-sum. The "j_L screened like n" statement is exact as j_L = (ω/q)n.
- **D2.** (1.2) and (4.6) attribute δ_rel to H_SO, as "O(q²⟨∇V⟩/m³)". SOC is linear in p and Darwin is multiplicative, so both
  contribute exactly zero to the f-sum double commutator. Only mass-velocity contributes: [E11], δ_rel = −(5/3)⟨T⟩/m (C2).
- **D3.** (1.2) sizes "O((Zα)²) ≈ 0.27 for Ge 1s, ≈ 0.05 for 3d". The correct values are (Zα)² = 0.055 for Ge 1s and ~10⁻³ for
  Ge 3d [E], with 0.02 as the SO/binding ratio.
- **D4.** (5.3): "transverse currents … unscreened" holds only without local fields. In a crystal j_T(q) mixes with n(q+G≠0)
  (§2.3).
- **D5.** (5.3): spins with SOC = 0 are not Coulomb-screened but are xc-renormalised by f_xc^T ([E6]).
- **D6 (refinement).** (7.2) uses (ε^{-1})_{G0}. The general weight is (1+Rv)_{0G}. They coincide for R_{GG′} = R_{G′G} (TR plus
  inversion), so GaAs needs [E2].
- **Answer to O3.** Relativistic matching: §5. L3 screening of j_L and s: §2.
- **Answer to O5.** [E3].

## 10. Exact remaining gaps
1. Finite-q BSE beyond TDA for Si/Ge, with bound lines: specified (G5) but not computed. Until then Δ_BSE ∈ [+0.3, +1.0]×S near
   the edge, as an interim nuisance [E].
2. A 4-component crystal response with no-pair projection (G7). The interim error is O(⟨v²⟩) ≤ 2% for Ge 3d.
3. The spin-channel f_xc^T in insulators: ALDA only. Its uncertainty is the ALDA-vs-RPA difference in the triplet channel.
4. The size of LFE screening of j_T (§2.3, 10–30% [E]) awaits the G10 run.
5. The SOC mixing of singlet and triplet near the Ge edge (≲ 10% [E]).
6. Plasmon → phonon branching (X+, WP3).

## 11. Literature (all IDs verified against the arXiv API, 2026-10-31)
Read in full text (equation numbers quoted): 1509.01598, 2101.08275, 2101.08263, 2105.02233, 2210.14917, 2510.25835, 2104.12786,
2002.06937, 2003.12077, 2507.14345, 2509.14534, 2607.06005, 2608.20715, 2603.12326.
Abstract or text checks: 2411.03433, 2605.11063, 2501.18261, 2306.14944, 2105.05253, 2110.01587, 2608.05282.
From WP0's reading: 2009.13534.
PDFs and HTML in `literature/papers-WP1/` deleted at the end, per the brief.

## 12. Symbols introduced/used (per coordinator; WP0 §10 governs)
| Symbol | Meaning | Status vs WP0 §10 |
|---|---|---|
| q, ω, n_q = Σe^{+iq·r}, S_ab, R_ab, R̃_ab, ε_{GG′}, ε_e, L, 𝔇_ab, ρ_cv | as WP0 §10 / NOTATION | same |
| q_r, G_q | 1BZ part and reciprocal vector of the unreduced q (q = q_r + G_q) | new; no collision |
| R⁰ | KS/QP independent-pair response (= D2's Π at IP) | new label for an existing object |
| X ∈ {IP, RPA, RPA+LFE, TDDFT, BSE}, Δ_X | ladder rung, rung increment | same as WP0 τ, (8.1) |
| f_xc, f_xc^T | xc kernel (charge), triplet (spin) kernel | new |
| ε_M | macroscopic dielectric function 1/(ε^{-1})_{G_qG_q} | new label (standard) |
| ε_T, Π_T | transverse dielectric function and transverse polarisation [E5] | new |
| j_L, j_T, J_T, P_T | longitudinal/transverse paramagnetic current, transverse spin current, transverse projector | consistent with WP0 j_e, J_e |
| A^λ_{cvk}(q_r), E_λ, H^{exc} | BSE eigenvector, energy, pair Hamiltonian | new |
| E_b, a_x, μ_x, S_F, κ | exciton binding, Bohr radius, reduced mass, Sommerfeld factor and its argument | new; κ here ≠ species κ: **collision, rename to κ_S at reconciliation** |
| E_min(q), E_x, Q_x | minimal pair energy at fixed q, exciton energy, exciton momentum | new; Q_x ≠ phonon Q |
| ω_pl(q), F(q), q_c | plasmon dispersion, f-sum share of the pole, Landau-onset momentum | new |
| W̄_l, B_l | Catena et al. crystal responses (2105.02233) | quoted; WP0 renames Catena W_i → 𝒲_i: **use 𝒲̄_l at reconciliation** |
| O_Γ(q) | Dirac-bilinear target operators (§5.1) | new extension of WP0 (2.2) |
| ⟨T⟩, δ_rel | mean kinetic energy per electron, relativistic f-sum shift | δ_rel as WP0 (1.2) |
| T_ℓm, K_ℓ | multipoles of the target response, cubic harmonics | new |
| v_max | v_esc + v_E = 544 + 250 km/s | halo per 2105.00599 (v_esc = 544). ρ_χ is not used in any number here |
| Ω | unit-cell volume (= V_cell of the sources) | same |
