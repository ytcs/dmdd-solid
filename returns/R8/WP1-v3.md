# R8 / WP1-v3: electronic sector at clamped nuclei, corrected after the R7 hostile review

Revision agent, brief R8/REV3-WP1. Supersedes returns/R6/WP1-v2.md (v2), which stays as the historical record. Applies every verdict of
referees/R7/REF-WP1-A.md (items A-1…A-23) and REF-WP1-B.md (items B-1…B-28), and the coordinator's cross-package item in state/SOTA.md
("R7 referee reports"): the zero-phonon exciton threshold as a minimum over q, the corrected IF-6 boundary for WP3/WP6, and the size of the
forbidden-class zero-phonon rate against PAER. Referee disagreements are settled in §R2, rebuttals are in §R1, literature ratings in §R3,
and the closing table is §13. Conventions: CONVENTIONS.md; symbols: NOTATION v4 (new symbols flagged in §15). WP0 equations are cited
from returns/R6/WP0-v2.md as WP0-v2 (s.n). Equations [E1]…[E12] keep their v2 numbers; [E13] (threshold) and [E14] (ZPL/PAER ratio) are
new. Checks: `code/WP1-v3/checks.py` (sympy only, exact arithmetic or polynomial roots of closed forms, **49 checks, 49/49 PASS, ≈ 5 s; re-run after the R9 clean-up**),
cited as WP1v3-Cn. Tags (CONVENTIONS §12): **[D]**, **[D, sketch]**, **[E]**, **[C]**; literature **[FT]**, **[ABS]**, **[UNVERIFIED]**.
Status: CLAIMED (SOTA R5 WP1), REFEREED R7 with corrections; this version is pending the coordinator's acceptance.
Si/Ge inputs: a_lat = 5.431/5.658 Å, E_g(0) = 1.170/0.744 eV, E_x^b = 14.7/4.15 meV, E_x = E_g − E_x^b = 1.1553/0.7399 eV.
New band inputs for §3.4 **[UNVERIFIED, from memory; to be replaced by ab initio E_min(q)]**: Si CB longitudinal mass m_l = 0.916 m_e;
Ge L-valley m_l = 1.59 m_e; Ge Γ-CB mass 0.038 m_e; Ge E_dir = 0.889 eV (direct exciton binding 1.4 meV); heavy-hole masses from the
Luttinger parameters, m_hh[100](Si) = 0.277 m_e, m_hh[111](Ge) = 0.50 m_e (the heaviest direction, the one most favourable to a low threshold).
Halo reference scalars (CONVENTIONS §8): v_max = v_esc + v_E^ref = 544 + 250.5 = 794.5 km/s.

---
## 0. What changed (v2 → v3)
| v2 | v3 | change (referee item) |
|---|---|---|
| §3.4 thresholds 0.472/0.708/0.420 MeV "the boundary WP3 must use" | §3.4 [E13] | **FALLS → replaced**: threshold = min over q of the zero-phonon edge; Si second class ≈ 0.42, Si allowed ≈ 0.54, Ge ≈ 0.32–0.36 MeV [E]; floors 0.329/0.211 MeV [D] (A-12, B-13) |
| §3.2 (c) Si: allowed Umklapp only G = (1̄11), 3.25 keV | §3.2 (c) | **Si G = (2̄00) on-axis Umklapp is allowed** (\|q\| = 2.63 keV), from the nonsymmorphic phase e^{−iG·t_d} (A-11; settles D1) |
| — | §3.7 [E14] | forbidden-class zero-phonon rate vs PAER where both are open (coordinator item) |
| §1.4 beyond RPA "1 − f_HxcR⁰ > 0" | §1.4 | condition is (−R⁰)^{-1} + f_xc > 0 (proper R̃ NSD), counterexample to the v2 condition (A-3, B-3, B-26) |
| L3 (a) "3 of 5 independent; Im 𝒲̄₂ measures [V_NL, n_e]" | L3 (a) | PT (TR+I) ⇒ Im 𝒲̄₂ ≡ 𝒲̄₅ ≡ 0 for any H; 2 independent in Si/Ge; V_NL statement withdrawn (A-7, B-21) |
| L3 (c) ratio ≈ 40, "conservative by O(10)", "not determined by the dielectric function" | L3 (c) | IP ratio 20–30 (⟨p_T²⟩), larger in medium by \|ε_L\|²; conservative robust by Cauchy–Schwarz; "not fixed by Im(−1/ε_L) alone"; extends to 𝒪₅, 𝒪₂ (A-8, B-22) |
| §2.6 "seven real functions" | §2.6 | 12 in Si/Ge (6 screened singlet + 6 IP), 18 at fixed q̂ in general; plus R⁰_{GG′} for the triplet dressing (A-9, B-9) |
| [E8] second class (n_H² − 1)/(πa_x⁵n_H⁵) | [E8] | factor 1/3; matching continuum replacement \|ρ\|² → \|∇_kρ\|²k_rel²/3 (A-13) |
| [E5] tr S = (4ω²/e²) Im ε_T | [E5] | Σ_λ(2ω²/e²) Im ε_{T,λ} (A-5, B-6) |
| [E6] R̃_s undefined; "+10–20% Stoner" leading | [E6] | R̃_s ≡ R_mm = 4R_{s^zs^z}; leading beyond-IP term is the triplet W^{scr} ladder (B-7) |
| §5.2 spin curl (i/2m_e) q × s_e | §5.2 | (i/m_e) q × s_e up to sign convention (B-16, C2d) |
| §4.2 q_c = 1.88 keV | §4.2 | q_c ≈ 2.24 keV with the [E9] dispersion (B-15; settles D2) |
| L11 "×(5/1.9)²" | L11 | REFUTED; logarithmic measure, ≈ ×1.4 (B-24) |
| §1.5, L1 (a) "1/\|ε\|² 0.1/0.44 is the ×1.4–2.5" | §1.5, L1 | pointwise 0.117/0.451 (Cappellini) separated from the 2101.08275 rate ratio ×1.4–2.5 (B-4) |
| G5 "node-hours per q_r" | G5 | dense fine kernel ≈ 7 TB per q_r: matrix-free Haydock with interpolated coarse kernel (A-22, B-27) |
| checks 28 (v2) | 49 | C9, C10 replaced (v2's C9 solved the pinned formula only; v2's C10 used point operations only); 21 new checks |

---
## 1. The sector and the kernel ladder

**1.1 Clamped nuclei [D].** The clamped-nucleus sector is n_B = 0 in τ (CONVENTIONS §11; WP0-v2 §6): R̃_{eκ} = R̃_{κκ} = 0, so the total ε
equals ε_e. WP0-v2 (5.3) then holds with c = e only, and WP0-v2 (5.4) with (5.5)(i) gives, exactly at this level,

  S_ee(q,ω) = (2q²/e²)(1 − e^{−βω})^{-1} Im[−(ε^{-1})_{00}(q,ω)],   ε_{GG′}(q,ω) = δ_{GG′} − v_C(q+G) R̃_{GG′}(q,ω),                    [E1]

with (ε^{-1})_{00}(q,ω) ≡ (ε^{-1})_{G_qG_q}(q_r,ω), q = q_r + G_q, q_r ∈ 1BZ (CONVENTIONS §2). This is the X0 sector of Theorem D
(WP0-v2 (6.1)) at zero e–ph order. ZPR, PAER, the X+ sideband and the Debye–Waller (Franck–Condon e^{−2W}) reduction belong to WP3.
(A-1, B-1: STANDS.)

**1.2 The ladder 𝒳: truncations of R̃ (WP0-v2 (5.1)) [D as definitions].** R̃ is irreducible with respect to one Coulomb line of the
external channel {q+G}. Each rung approximates R̃ alone; R⁰ is the KS (or QP) independent-pair bubble:

| 𝒳 | R̃ used in [E1] | what it adds | exact relations kept (local H) |
|---|---|---|---|
| IP | none: S = −2Im R⁰_{00}/(1 − e^{−βω}) (no Dyson) | — | f-sum, positivity; KK for R⁰ (not for L) |
| RPA | R⁰, G = G′ = 0 only | 1/\|ε_{00}\|² screening | f-sum, KK, positivity |
| RPA+LFE | R⁰, full GG′ matrix | microscopic inhomogeneity | the same + static ε_mac ≥ 1 ([E3]) |
| TDDFT | R̃ = R⁰ + R⁰ f_xc R̃ | xc vertex (ALDA, LRC −α_LRC/\|q+G\|², bootstrap) | the same, if f_xc is ω-independent; ε_mac ≥ 1 under (1.4′) |
| BSE | R̃ = −iL^{BSE} contracted, kernel Ξ^{BSE} = −W^{scr} only (exchange v_C restored by ε) | e–h attraction (excitons) | f-sum only beyond TDA and with local H_QP |

The BSE row agrees with 2507.14345 [FT]: there L^{BSE} = L⁰ + L⁰Ξ^{BSE}L^{BSE} carries Ξ^{BSE} = v_C − W^{scr}, then ε^{-1} = 1 + v_CR.
Moving the v_C part of Ξ^{BSE} into ε is the WP0-v2 (5.1) bookkeeping; removing W^{scr} returns their RPA **[D]**.

**1.3 Exact pair-resolved (final-state) form [D] (WP1v3-C4).** Hypotheses: RPA(+LFE), or adiabatic TDDFT with a kernel f_Hxc that is a
**Hermitian G-matrix** (true for a real symmetric kernel; f_xc is not diagonal in G, so this must be stated, B §A) with v_C → f_Hxc and
ε → ε̃ in the weights; any target (no inversion assumed). From R = R⁰ + R⁰v_CR = R⁰ + Rv_CR⁰ the two exact factorisations

  R − R† = (1 + R†v_C)(R⁰ − R⁰†)(1 + v_CR) = (1 + Rv_C)(R⁰ − R⁰†)(1 + v_CR†)

hold (C4a). In the (3.2) index order (T = 0, ω > 0), (R⁰ − R⁰†)_{GG′} = −2πiV^{-1}Σ_{pairs}ρ_cv(k,q+G)*ρ_cv(k,q+G′)δ(…) (spin 2
inside Σ). The 00 element of the first factorisation gives the **out-state** (prompt-final-state) form, which is WP0-v2 (7.2):

  S(q,ω;cvk) = (4π/V) |Σ_G (ε^{-1})_{G0}(q,ω) ρ_cv(k, q+G)|² δ(ω − ε_{c,k+q} + ε_{vk}),   (ε^{-1})_{G0} = δ_{G0} + v_C(q+G)R_{G0}(q,ω),      [E2]

with R retarded and in the (3.2) order (a = n_e(q+G), b = n_e(q)). Physically the causal induced potential screens the external one,
V_tot(q+G) = (ε^{-1})_{G0}φ_ext, and V_tot creates bare outgoing pairs; equivalently, [E2] is the T-matrix element to the free final pair,
⟨f|(1 + V_int G⁺)V_ext|0⟩ (REF-A A2). The second factorisation gives the in-state labelling, weight [(1 + Rv_C)_{0G}]*; it sums to the same
Im R_00 (C4b,c) but distributes it differently over open pairs. The v1 form (1 + Rv)_{0G} without the conjugate equals [E2] pair by pair
when R_{GG′} = R_{G′G} (TR plus inversion: Si, Ge; C4e) but misses Im R_00 in GaAs (C4d). F1 stays accepted (A-2, B-2, A-23, B-28: STANDS).

**1.4 Static stability [D] (WP1v3-C3).** (i) *RPA+LFE.* Hypotheses: any stationary reference with a static Kubo response R⁰(q,0) (Hermitian
and negative semidefinite; both pole families are rank-one PSD matrices divided by −Δ_f, so neither TR nor inversion is needed); RPA
kernel. With X = v_C^{1/2}R⁰v_C^{1/2} ≤ 0, v_C^{1/2}Rv_C^{1/2} = X(1 − X)^{-1} has eigenvalues λ/(1 − λ) ∈ (−1, 0] (C3a); a diagonal element
is a convex combination of eigenvalues, so

  0 < (ε^{-1})_{00}(q,0) ≤ 1   ⇔   ε_mac(q,0) ≥ 1   (all q, LFE included; C3b exact complex 3×3 examples).                          [E3]

(ii) *Beyond RPA (corrected, A-3, B-3).* Stability of the full R (1 − f_HxcR⁰ > 0, the v2 condition) gives only the upper bound
(ε^{-1})_{00} ≤ 1, i.e. ε ≥ 1 **or ε < 0**, which thermodynamic stability already allows (Dolgov–Kirzhnits–Maksimov). C3c is an explicit
counterexample: R⁰ = −1, f_xc = −2, v_C = 3 gives 1 − f_HxcR⁰ = 2 > 0 and (ε^{-1}) = −1/2. The lower bound holds iff the Coulomb-proper
response R̃ = (1 − R⁰f_xc)^{-1}R⁰ is NSD, i.e. (for invertible R⁰)

  (−R⁰)^{-1} + f_xc > 0   (f_xc, not f_Hxc),                                                                                         (1.4′)

and then the proof of (i) goes through with R⁰ → R̃ (C3d: exact 3×3 examples with an attractive non-diagonal f_xc). **ε(q,0) < 0 is excluded
only under (1.4′).** It fails first at the proper (compressibility) instability, r_s ≈ 5.25 in the HEG; Si and Ge have r_s ≈ 2.0 (C7), so
the conservative L17 step holds for them **[E beyond RPA]** (WP0-v2 §9.2 (iii)).

**1.5 Rung increments as nuisances (WP0-v2 (8.1)) [E, Si/Ge].** Each increment Δ^τ_𝒳 = S^{τ+e_𝒳} − S^τ is the **computed** next-rung
difference, entered as type M (multiplicative log-normal, r^M_𝒳 = Δ^τ_𝒳/S^τ) where S^τ > 0, and as type A where the higher rung opens
new support (bound-exciton lines below E_min(q), [E8]). The ladder is not an expansion (η_xc ~ 0.2–0.5); interim sizes:

| Increment | Size in Si/Ge |
|---|---|
| Δ^τ_{RPA−IP} | pointwise factor 1/\|ε\|² = 0.117 at q = 2 keV and 0.451 at q = αm_e (static Cappellini model, EXCEED-DM parameters ε_∞ = 11.3 (their "ε₀"), k_TF = 4.13 keV, ω_p = 16.6 eV; C7d). The q-integrated rate ratio is a different number: ×1.4–2.5 (IP over screened) in 2101.08275 (B-4) |
| Δ^τ_LFE | −20…−50% (2603.12326) |
| Δ^τ_ALDA | few % at eV ω (ALDA has no e–h binding) |
| Δ^τ_BSE | +30…+100% within ~1 eV of E_min(q) ([E8], Sommerfeld); type A for the bound lines |

---
## 2. Non-density operators in the medium (G10; L3 chain)

**2.1 Continuity [D] (C1a).** For j_e = Σ½{p/m_e, e^{iq·r}}, [T_e, n_e(q)] = q·j_e(q) exactly, with no (q²/2m_e)n_e term (CONVENTIONS §6).
For local H, ⟨f|q·j_e|i⟩ = (E_f − E_i)⟨f|n_e|i⟩, hence S_{n j_L} = (ω/q)S_nn and S_{j_L j_L} = (ω/q)²S_nn, screened or not.

**2.2 On-shell projection theorem [D] (C6a).** Hypotheses: the WP0-v2 (2.2) matching with v^⊥ = v_χ − v_s, v_χ = v − q/2m_χ; local H;
Born; **for the spin-current rows also [H, s_e] = 0, i.e. SOC = 0, no hyperfine term H_hf and no external field B₀** (B-5; WP0-v3 G13, AUDIT-2 m33). Then q·v_χ = ω_q + Δ_χ and q·j_e acts as ω, so
(q̂·v^⊥)n_e ≐ ((ω_q + Δ_χ − ω)/q)n_e = (Δ_χ/q)n_e on δ(ω − ω_q). For elastic DM (Δ_χ = 0) **only the transverse parts survive in any rate**:
on the DM side (1 − q̂q̂)·v_χ = v_T, on the target side j_T (and J_T). For inelastic DM the longitudinal remainder is the extra density term
(Δ_χ/q)n_e (B-5). For 𝒪₈ = 𝐒_χ·v^⊥ → 𝐒_χ·v_χ n_e − 𝐒_χ^αj_e^α, with (2j_χ+1)^{-1}tr(𝐒_χ^α𝐒_χ^β) = δ_{αβ}/4 (j_χ = ½; C5b) and Δ_χ = 0,

  tr[𝔇S]_{𝒪₈} ∝ ¼[ |v_T|² S_nn − 2Re v_T·S_{n j_T} + tr S_{j_T j_T} ].                                                            [E4]

[E4] is unchanged by the index-order correction tr[𝔇S] → tr[𝔇ᵀS] of REF-WP0-A, since only Re v_T·S_{nj_T} enters. The same holds for 𝒪₃,
𝒪₅, 𝒪₇, 𝒪₁₂–𝒪₁₅ through the J_T rows. This is the in-medium form of Galilean invariance. (A-4 STANDS; B-5 applied.)

**2.3 Transverse response [D] (C6b).** Per transverse polarisation λ (eigenvector of the transverse block), with
Π^γ_{T,λ} = e²(R_{j_Tj_T,λ} + 𝓃_e/m_e) (R proper with respect to the transverse photon only; Coulomb lines, hence LFE, included) and
ε_{T,λ} = 1 − Π^γ_{T,λ}/ω²,

  S_{j_Tj_T,λ}(q,ω) = (2ω²/e²) Im ε_{T,λ}(q,ω)/(1 − e^{−βω}),   tr S_{j_Tj_T} = Σ_{λ=1,2}(2ω²/e²) Im ε_{T,λ}/(1 − e^{−βω}).                 [E5]

The two polarisations are degenerate only for q̂ on a 3- or 4-fold axis of a cubic crystal (E irrep of C₃ᵥ, C₄ᵥ) or in an isotropic
medium; then tr S = (4ω²/e²)Im ε_T (A-5, B-6). The transverse-photon correction is O(ω_p²/q²) ≈ 2×10⁻⁵ at q = 4 keV. Screening of j_T is
**through local fields**: j_T(q) couples to n_e(q_r + G ≠ q), so R̃_{j_T, n(q_r+G)} ≠ 0 and j_T is screened at LFE strength (≈ 10–30% [E]).
For a dark photon (total charge), WP0-v2 (3.6) with the transverse 𝒟^γ gives L + |v^⊥|² Im[−q²/(ω²ε_T − q²)], which is 2608.20715
Eq. (2) for a light mediator **[D]** (the FT quote is UNRESOLVED by R7; §R3).

**2.4 Spin and spin-current channels [D] (C5b).** Take SOC = 0 and a spin-unpolarised reference. Charge (singlet) and spin (triplet)
channels decouple and Coulomb (Hartree) lines enter only the singlet. With m = n_↑ − n_↓ and the spin-summed bubble R⁰ = χ⁰_↑ + χ⁰_↓,

  S_{s^αs^β}(q,ω) = (δ_{αβ}/4) S_nn^{IP}(q,ω) at IP, with NO 1/|ε|²;   beyond IP R̃_s = R⁰ + R⁰ f_xc^T R̃_s,  f_xc^T = (f_↑↑ − f_↑↓)/2,
  R̃_s ≡ R_mm = R_{σ^zσ^z} = 4R_{s^zs^z}   (equivalently the kernel is 4f_xc^T for R_{s^zs^z}).                                        [E6]

(Normalisation stated, B-7; consistent with A §A5.) The *unscreened* crystal form factor (L1) is the correct IP response for 𝒪₄-type
electron-spin couplings. **Beyond IP the leading correction is the triplet BSE ladder** (B-7): the triplet channel loses the exchange
(v_C) term but keeps the direct −W^{scr} ladder, so the Sommerfeld factor ×1.3–2 within ~1 eV of E_min(q) and the bound lines of [E8]
apply to s_e as well, with E_x^b(triplet) ≥ E_x^b(singlet). The adiabatic f_xc^T (< 0, Stoner-like) adds ≲ +10–20% at r_s ≈ 2; that figure
is a static q → 0 HEG number and an upper bound at keV q and eV ω **[E]** (A §A5). With SOC, R̃_{s,n} ≠ 0 at O(Δ_SO/E) and the channels mix:
Si (Δ_SO = 44 meV) ≲ 2%, Ge (0.29 eV) ≲ 10% in amplitude near the edge **[E]**. EXCEED-DM 2210.14917 (App. B, Eqs. (B15)–(B18) in the PDF;
(68)–(71) in the HTML) states "there is no screening" for its axial coupling, whose target operator is the spin-current trace K_e·σ_e/2m_e
(J row, like the ALP vertex), not s_e (A-21). The URF agrees at Hartree level; missing there are the triplet ladder and f_xc^T (and SOC
mixing). Consistent with WP0-v2 (4.6e): 𝓜¹_{s^zs^z} = 𝓃_eq²/(4m_e).

**2.5 ALP absorption vertex (WP3 O-WP3-5) [D].** The ALP–electron NLO vertex is 2tr J_e(k) = Σ½{σ·p/m_e, e^{ik·r}} (WP0-v2 §2,
2106.12586 Eq. (18) [FT via WP0]). At SOC = 0, unpolarised: Σ_{ss′}|⟨s′|σ^α|s⟩p^α|² = 2|p|², so the spin sum of any amplitude equals the
velocity form summed over the three Cartesian components; WP3 L9b(c) is **confirmed**. The vertex lives in the **triplet** channel, so it
carries no Hartree local fields and no e–h exchange, whereas measured σ₁ (singlet) does; the difference is ≲ 10% in Si **[E]**, now to be
read with the triplet-ladder caveat of §2.4. With SOC it fails at O(Δ_SO/E). (B-8 STANDS.)

**2.6 Minimal response set (SOC = 0, unpolarised) [D] (corrected count, A-9, B-9; settles D5).** Every NR-EFT electron rate built from the
operators n_e, j_e, s_e, J_e (all 𝒪_i except the kinetic-type piece of 𝒪₂, see L3 (c)) needs, per (q,ω):
- the singlet (screened) block on the rows {n, j_T1, j_T2} (j_L eliminated by §2.1): a Hermitian PSD 3×3 matrix: S_nn (1 real),
  S_{nj_T} (2 complex), S_{j_Tj_T} (2×2 Hermitian: real symmetric part from [E5], antisymmetric imaginary part 𝒲̄₅-type);
- the triplet block on {s^z, J^z_T1, J^z_T2} (spin-rotation invariance makes it δ_{αβ} times one 3×3 block): at IP equal to ¼ × the IP singlet
  block (so it costs the IP singlet block, not new data), dressed by the triplet ladder/f_xc^T, for which the full IP G-matrix R⁰_{GG′}
  (not only the heads) is needed (B §K).

Symmetry reductions (§L3 (a), C1c): under TR, S_ab(q) = η_aη_bS_ab(−q)* (η_n = +1, η_j = −1); under inversion S_ab(q) = η_aη_bS_ab(−q);
with both (PT, Si, Ge) every S_ab is **real**, so S_{nj_T} is a real 2-vector and the antisymmetric jj block vanishes. Counts of real
functions per (q,ω) to tabulate: **Si, Ge: 6 (screened singlet) + 6 (IP singlet, which also fixes the IP triplet) = 12**; no symmetry,
fixed q̂ (e.g. GaAs at generic q̂): 9 + 9 = 18. With TR alone nothing vanishes at fixed q̂; after angle averaging Im 𝒲̄₂ (odd in q)
vanishes, while the isotropic part of the antisymmetric jj block is a pseudoscalar (q·g with g the axial vector of S^A), which vanishes in
achiral crystals (GaAs, T_d) and survives only in chiral ones (natural optical activity) [D].
Longitudinal currents are not independent (§2.1). This is the G10 table.

---
## 3. Excitons at finite q, thresholds, and the zero-phonon line against PAER (exciton gaps; L14; IF-6)

**3.1 Finite-q BSE contribution [D] (C5a).** Hypotheses: QP bands, static W^{scr}, pair basis at total momentum q_r, H^{exc}(q_r)A^λ = E_λA^λ
including coupling (beyond TDA). With |λ⟩ = Σ_{cvk}A^λ_{cvk}|cvk; singlet⟩, ⟨λ|n_e(q)|0⟩ = √2 Σ A^{λ*}ρ_cv and

  S^{BSE}(q,ω) = (4π/V) Σ_λ |Σ_{cvk} A^{λ*}_{cvk}(q_r) ρ_cv(k, q)|² δ(ω − E_λ(q_r))   (TDA form; beyond TDA use the pseudo-norm).       [E7]

Exchange (v_C(q+G), G = 0 included) is in H^{exc}, which makes [E7] the screened (L) quantity. Triplet excitons give zero to S_nn.
(A-10, B-10: STANDS.)

**3.2 Selection rules at finite q [D] (C10).** (Band labels Γ₂₅′, Δ₁, Δ₂′, Δ₅, Λ₁, L₁, X₁ are BSW irrep labels; X is the BZ point.)
- (a) **Spin.** Density excites only singlets. Spin operators (𝒪₄, 𝒪₆, 𝒪₉, 𝒪₁₀ …) excite triplets: dark to n_e, bright to s_e ([E6]).
- (b) **Momentum.** An indirect exciton with Q_x = k_c − k_v is optically dark but DM-bright at q = Q_x + G as a zero-phonon process.
- (c) **Space group at the extrema (nonsymmorphic phases kept).** For g = {R|t} with Rq = q and Rk_c = k_c, the Bloch state at k_c carries
  e^{−ik_c·t}Γ_c(R) and P_g e^{iq·r}P_g^{-1} = e^{iq·r}e^{−iq·t}, so the transition is allowed iff the trivial representation occurs in
  e^{−iG·t}·Γ_c*(R)·Γ_v(R), G = q − k_c + k_v (REF-A A8). The residual phase e^{−iG·t} is origin-independent for RG = G and is absent only for
  G·t ∈ 2πℤ. Diamond structure, origin on an atom: t = 0 for R ∈ T_d, t = t_d ≡ (¼,¼,¼)a_lat for R ∈ O_h∖T_d (the "t_d elements").
  - **Si, G = 0**, CBM Δ₁ at 0.85 X, q ∥ [100]: phases cancel; Γ₂₅′ ↓ C₄ᵥ = Δ₂′ ⊕ Δ₅ has no Δ₁ (C10a): **forbidden on the axis**, second
    class off it (|ρ|² ∝ |δq_⊥|², δq_⊥ transforms as Δ₅ and Δ₅ ⊗ Δ₅ ∋ A₁; δq_∥ is A₁, so the zero persists along the whole axis, B §F).
  - **Si, G = (2̄00)·2π/a_lat (new, A-11):** q = (−1.15, 0, 0)·2π/a_lat, **|q| = 2.63 keV**, on the axis. G·t_d = −π, so e^{−iG·t} = −1 on the
    t_d elements C₄^±, σ_y, σ_z: the operator carries the B₂ (= Δ₂′) character and B₂ ⊗ (B₂ ⊕ E) ∋ A₁: **allowed on the axis**, multiplicity 1
    (C10c). This is the glide-forbidden (200) reflection of diamond seen from the other side: e^{iG·r} with G = (200) is odd under the t_d
    elements. Cross-check (C10e): relabelling a Bloch state k → k + (200) multiplies the t_d characters by −1, i.e. exchanges Δ₁ ↔ Δ₂′, which is
    the band sticking at X (X₁ = Δ₁ ⊕ Δ₂′). Along the axis the vertex therefore switches from forbidden (|q| < 2.28 keV, final state on the
    −k_c side) to allowed (|q| > 2.28 keV, final state on the +k_c side) at q = X. Amplitude unknown, possibly small (the (200) Fourier
    component of the crystal potential vanishes) **[E]**, but not symmetry-suppressed.
  - **Si, G = (1̄11):** q = (−0.15, 1, 1)·2π/a_lat off the axis, |q| = 3.25 keV; little group {E, σ_{y↔z}}: allowed (C10d).
  - **Ge, G = 0** (and G = (1̄1̄1̄), same |q| = 1.90 keV): C₃ᵥ ⊂ T_d has no t_d elements; Γ₂₅′ ↓ C₃ᵥ ∋ Λ₁ = L₁↓C₃ᵥ: **allowed** (C10b).
  - SOC (Δ₆/Δ₇ double group) lifts the Si on-axis zero at O(Δ_SO/E_g) ≈ 4% in amplitude **[E]**.
- (d) The rules apply to the zero-phonon line competing with PAER: §3.7.

**3.3 Wannier limit of [E7] [D for parabolic bands and constant ε_∞; E for Si/Ge] (C8).** Allowed class, exciton radius a_x, binding E_x^b,
reduced mass μ_x (2μ_xE_x^b = 1/a_x²), hydrogenic principal number n_H:

  S_x(q,ω) = 4π|ρ_cv(k_v,q)|² [ Σ_{n_H} δ(ω − E_min(q) + E_x^b/n_H²)/(πa_x³n_H³) + (2μ_x)^{3/2}√(ω − E_min)/(4π²) · 𝒮_F(ω) ],
  𝒮_F = 2πζ_S/(1 − e^{−2πζ_S}),  ζ_S = √(E_x^b/(ω − E_min)).                                                                     [E8]

E_min(q) = min_k[ε_{c,k+q} − ε_{vk}]. **Second class (corrected, A-13):** for ρ_cv ≈ ∇_kρ_cv·k_rel (k_rel the relative e–h momentum offset,
fixed gradient), the bound weight is |ρ|²/(πa_x³n_H³) → |∇_kρ_cv|²(n_H² − 1)/(3πa_x⁵n_H⁵) (only the n_H p state along ∇_kρ_cv contributes;
C8b with the hydrogenic R_{n1}, n_H = 2…5), the continuum replacement is |ρ|² → |∇_kρ_cv|²k_rel²/3 (k_rel² = 2μ_x(ω − E_min)), and 𝒮_F → 𝒮_F(1 + ζ_S²)
(ℓ = 1). v2's (n_H² − 1)/(πa_x⁵n_H⁵) is the m- and Cartesian-summed trace, 3× too large for a fixed gradient. Check of consistency (C8c):
with these forms the line density per unit energy as n_H → ∞ equals the continuum density at E_min⁺, for both classes (1/(2πa_x³E_x^b)
and |∇_kρ|²/(6πa_x⁵E_x^b)). Consequences: the total bound weight equals the free-continuum weight within (6πζ(3))^{2/3}E_x^b = 8.0 E_x^b of the
edge (C8a); 𝒮_F = 6.3, 2.3, 1.7, 1.35 at ω − E_min = 1, 10, 30, 100 E_x^b. **Prediction [E]:** near-edge singlet S is enhanced by 1.3–2 over
RPA for ω ≲ E_min + 1 eV, partly offset by LFE (opposite sign); consistent in sign with 2507.14345 (BSE > RPA at low ω for GaAs and NaI).
v2's "Si still +35% at 1.5 eV" applies the hydrogenic 𝒮_F at ≈ 100 E_x^b, where parabolic bands and static ε_∞ screening of the e–h attraction
do not hold: the sign is kept, the size is a model figure only (A-13; B-12 STANDS with the [E] tag).

**3.4 Zero-phonon kinematic thresholds: minimum over q [D for the formula; E for the numbers] (C9; replaces v2 §3.4, A-12, B-13).**
A zero-phonon final state of total momentum q (unreduced) has a lowest energy E^{ZP}(q) = min over the class of [E_min(q) − E_x^b(q)]
(bound exciton) or E_min(q) (continuum). From ω_q ≥ E^{ZP}(q) with Δ_χ = 0 (WP0-v2 (2.1)), a DM mass m_χ reaches it iff some q satisfies
|q|v_max − |q|²/2m_χ ≥ E^{ZP}(q), i.e.

  m_χ ≥ m_χ^{ZP} ≡ min_q |q|² / [2(|q|v_max − E^{ZP}(q))]   ⇔   min_q [E^{ZP}(q)/|q| + |q|/2m_χ] ≤ v_max,                               [E13]

the second form being REF-WP6-A's edge condition (C9c). The minimum runs over |q|, q̂ and all G (every Umklapp copy), class-resolved.
- **The extremum value is not the threshold [D] (C9a).** At q = Q_x + G, ∇_qE^{ZP} = 0, while d/dQ[Q²/2(Qv_max − E)] = Q(Qv_max − 2E)/[2(Qv_max − E)²]
  > 0 whenever Qv_max > 2E (Si 5.14 > 2.31 eV; Ge 5.03 > 1.48 eV). So a strictly smaller m_χ exists at |q| < |Q_x + G|; v2's values
  0.472/0.594/0.708/0.420 MeV (C9d) are upper bounds.
- **Floor [D].** E^{ZP} ≥ E_x gives m_χ^{ZP} ≥ 2E_x/v_max² = **0.329 MeV (Si), 0.211 MeV (Ge)** (reached only for a flat dispersion).
- **Parabolic estimate [E].** Along the valley axis, E^{ZP}(Q) = E_x + (Q_0 − Q)²/2M_x with M_x = m_l + m_hh (pair translational mass along
  the axis; the hole carries Δq·m_hh/M_x). The optimum condition is linear (C9b): Q^{ZP} = (2M_xE_x + Q_0²)/(M_xv_max + Q_0).

| Final state (class) | \|Q_0\| | extremum (v2) | m_χ^{ZP} [E] | at \|q\| | pair offset | validity |
|---|---|---|---|---|---|---|
| Si Δ, G = 0 (second class on the axis) | 1.94 keV | 0.472 | **0.42** (0.44 with M_x/2; 0.417 with WP3's M_x = 1.41 m_e) | 1.45 keV | +0.19 eV | Δq = 0.21 q_BZ |
| Si Δ, G = (2̄00) (allowed on the axis) | 2.63 keV | 0.594 | **0.54** (optimum Q^{ZP} = 1.96 keV lies beyond X; constrained to \|q\| ≥ 2.28 keV) | 2.28 keV | +0.10 eV | at X (band-sticking point; nonparabolic) [E] |
| Si Δ, G = (1̄11) (allowed) | 3.25 keV | 0.708 | 0.62 | 2.46 keV | +0.51 eV | outside |
| Ge L, G = 0 (allowed) | 1.90 keV | 0.420 | **0.32** (0.36 with M_x/2) | 1.10 keV | +0.30 eV | Δq = 0.37 q_BZ: outside |
| Ge Γ (direct, allowed) | 0 | — | **> 2 MeV** (3.1 MeV with M_x = 0.54 m_e) | 0.67 keV | — | see below |

  M_x = 1.19 m_e (Si), 2.09 m_e (Ge L), 0.54 m_e (Ge Γ, heaviest hole). WP3-v3 §M3 (c) uses M_x(Si) = m_l + m_hh ≈ 1.41 m_e; both mass sets are
  [UNVERIFIED] and the corresponding window momentum is quoted as Q_w ≈ 0.31–0.33 Å⁻¹ (AUDIT-2 m19). **Second-class onset (VER-A N2):** on the axis the
  1s line is dark; the lowest bright state is the 2p line (E_min − E_x^b/4) or the off-axis 1s with weight ∝ |δq_⊥|². Using E_x (1s) in [E13]
  therefore gives the onset with a vanishing weight; the 2p value is higher by ≈ m_χ^{ZP}·(3E_x^b/4)/(qv_max − E) ≈ 0.001 MeV, far below the
  parabolic uncertainty. For the Si (2̄00) class the unconstrained optimum would move the
  electron past X, where the allowed branch ends (§3.2 (c)): the allowed-class value is the one at q = X, ≈ 0.54 MeV. For the Ge Γ valley,
  max_q(qv_max − q²/2M_x) = M_xv_max²/2 = 0.965 eV barely exceeds E_dir − E_x^b(dir) = 0.888 eV, so the channel needs m_χ ≈ 3 MeV in parabolic
  bands; it undercuts the Ge L value only if the Γ-pair dispersion is as flat as an effective mass ≥ 2.3 m_e at q ≈ 0.67 keV (C9f), not
  supported by the Ge valence band **[E]** (§R1).
- **Summary for WP3/WP6 [E]:** Si zero-phonon line opens at **≈ 0.42 MeV (0.40–0.44)**, second class (on-axis forbidden, (k_rel)² or SOC-
  suppressed; lowest bright state 2p), and is allowed by symmetry from ≈ 0.54 MeV ((2̄00) branch at X); it leads only if |ρ_cv^{(2̄00)}| ≳ η_PA^{1/2}|ρ_cv^{ref}| [E, open: the (200) potential component vanishes], otherwise the reliably allowed class starts at ≈ 0.62 MeV ((1̄11)); Ge zero-phonon (allowed, L valley) opens at **≈ 0.32–0.36 MeV**. All numbers
  sit at Δq ≈ 0.15–0.37 q_BZ, beyond strict parabolicity: the boundary must be recomputed from [E13] with ab initio E_min(q) along Γ–X
  (Si, both sides of X) and Γ–L plus Γ (Ge), with the exciton dispersion; the formula is the deliverable, the numbers are interim.
- **Consequence (IF-6):** the Si "PAER-only window" (v2: 0.338–0.47 MeV) narrows to **≈ 0.333–0.42 MeV**, with the reconciled PAER edge ≈ 0.333 MeV (exciton replica) /
  0.337 MeV (continuum) [E] (WP6-v3 (3.1′), AUDIT-2 §5, m1; v2's 0.338 used ω_TA at the zone boundary); between ≈ 0.42 and ≈ 0.54 MeV the zero-phonon
  channel is open but only second class, and PAER does not automatically lead there (§3.7). The Ge PAER-only window is ≈ 0.213–0.32 MeV
  (lower edge: the reconciled Ge PAER edge ≈ 0.213 MeV [E], AUDIT-2 §5), not closed at 0.256 MeV.

**3.5 Core excitons [E].** Ge 3d → CB at ≈ 29.5 eV + E_g carries a core-hole BSE (2507.14345 SM Fig. S3: the Ga 3d BSE onset lies below
RPA and is more peaked). It needs SOC (3d₅/₂–3d₃/₂ split 0.58 eV) and is handed to WP5 as Λ = core hole (WP0-v2 (7.1)).

**3.6 Onset exponents near the electronic edge (WP6 O6-2) [D for an M0 critical point with parabolic bands; E for Si/Ge].**
WP6 (3.3) needs p_on in S̄(q,ω) ∝ (ω − E_th)^{p_on}. At fixed q the pair energy near E_min(q) is quadratic in k_rel (reduced mass μ_x), so
from [E2] and [E8]:

  fixed q:  p_on = ½ (IP, allowed) · 3/2 (IP, second class) · 0 (with e–h attraction: 𝒮_F√(ω − E_min) → 2π√E_x^b, both classes);
  S̄ (angle average at fixed |q|, isolated quadratic minimum over q̂, E_min(q) = E_min,0(|q|) + O(|δq̂|²)):  p_on → p_on + 1, and + 1 more
  if the vertex vanishes on the minimum direction (|ρ_cv|² ∝ |δq̂|², the Si G = 0 case);
  bound lines: δ at fixed q (p_on = −1 in WP6's convention); in S̄ a step (p_on = 0) at E_min,0 − E_x^b (allowed) or E_min,0 − E_x^b/4
  (second class, n_H ≥ 2).                                                                                                          [E10]

Ge (allowed, G = 0): the electronic onset of S̄ is a step at the 1s line. Si (G = 0, forbidden on the [100] axis): the 1s line enters S̄
with p_on = 1 (weight ∝ |δq̂|² off axis), the 2p line as a step 3E_x^b/4 higher; **the allowed on-axis class exists only for |q| ≥ 2.28 keV
(the (2̄00) branch, extremum at 2.63 keV; A-14)**, the off-axis (1̄11) class at 3.25 keV. [E10] uses E_min,0(|q|) at every |q| and is
therefore consistent with [E13]; at the m_χ threshold the relevant |q| is q^{ZP}, not |Q_x + G| (B-14). If E_th lies above the onset,
p_on = 0. The X+ (PAER) onset exponent is WP3's.

**3.7 Forbidden-class zero-phonon rate against PAER where both are open (coordinator item) [E].** At a point (q,ω) with
ε_ex ≡ ω − E_min(q) > 0 (ε_ex, not bare ε, which is the dielectric function; AUDIT-2 m26) near the Si G = 0 edge, compare the second-class zero-phonon S (continuum of [E8] with the corrected replacement) with
the PAER sideband S^{PA}(q,ω). Write the allowed free-pair density with a reference vertex |ρ_cv^{ref}| (an allowed Si transition of typical
size), and define η_PA ≡ S^{PA}(q,ω)/S^{I}_{free}(ω̄) with S^{I}_{free} the allowed zero-phonon spectral density evaluated at PAER's own
excess energy ε̄_PA = ω − E_g − ω_ph (≈ E_min(q) − E_g + ε_ex, i.e. ≈ 0.19 eV + ε_ex at q ≈ q^{ZP}); WP3-v2 §M9 C3 gives sideband/ZPL ≈ 10⁻³–10⁻²
where both are open (≈ η_ep). **Using that calibration, made against the allowed ZPL, in the Si G = 0 region is a transfer [E]** (VER-B N2). With ℓ_∇ ≡ |∇_kρ_cv|/|ρ_cv^{ref}| and k_rel²a_x² = ε_ex/E_x^b:

  ϖ_II(ε_ex) ≡ S^{X0}_{II}/S^{PA} ≈ (ℓ_∇/a_x)² · [(ε_ex + E_x^b)/(3E_x^b)] · 𝒮_F(ε_ex) · √(ε_ex/ε̄_PA) / η_PA.                                          [E14]

As ε_ex → 0, 𝒮_F√ε_ex → 2π√E_x^b, so ϖ_II stays finite. Inputs [E]: ℓ_∇ ≈ 1–3 Å (k·p: |∇_kρ| ~ p_{cn}/(m_eΔE) with E_P ≈ 20 eV, ΔE ≈ 3–4 eV),
a_x = 4.9 nm, η_PA = 10⁻³–10⁻². Numbers (C9g), low/central/high:

| ε_ex | 1 meV | E_x^b = 14.7 meV | 0.1 eV | 0.5 eV |
|---|---|---|---|---|
| ϖ_II | 0.03 / 0.3 / 2 | 0.05 / 0.6 / 4 | 0.2 / 2 / 15 | 0.7 / 8 / 60 |

So **PAER is not guaranteed to lead once the forbidden zero-phonon channel is open**: pointwise it leads only within ≈ E_x^b of E_min(q)
(and everywhere below E_min(q), where the zero-phonon channel is closed); at ε_ex ≳ 0.1 eV the two are comparable, with the zero-phonon
channel likely larger. SOC adds an on-axis allowed-type piece with |ρ|² ≈ 2×10⁻³|ρ^{ref}|² (4% amplitude), ϖ ≈ 0.3–3 near the edge, and
makes the 1s line bright on the axis. In m_χ: at m_χ just above m_χ^{ZP} the open zero-phonon region shrinks to a point, so the
integrated ratio rises from 0; ω_max(q) grows by ∂ω_max/∂m_χ = q²/2m_χ² ≈ 6 eV/MeV at q ≈ 1.45 keV, so ε_ex ≈ 0.06–0.1 eV becomes reachable
within Δm_χ ≈ 0.01–0.02 MeV. **Interim statement for WP3/M1 [E]: the Si window in which PAER is the leading electronic channel is
≈ 0.333 (replica) / 0.337 (continuum) – ≈ 0.43 MeV; between ≈ 0.43 and ≈ 0.54 MeV the second-class zero-phonon line is comparable to PAER (ratio 10^{−1}–10^{1.5}); an allowed zero-phonon channel is allowed by symmetry from ≈ 0.54 MeV ((2̄00) branch at X); it leads only if |ρ_cv^{(2̄00)}| ≳ η_PA^{1/2}|ρ_cv^{ref}| [E, open: the (200) potential component vanishes], otherwise the reliably allowed class starts at ≈ 0.62 MeV ((1̄11)); where the allowed ZPL has a reference-size vertex, PAER/ZPL ≈ 10⁻³–10⁻².** In Ge the zero-phonon channel is allowed, so PAER leads only below ≈ 0.32 MeV.
The ratio needs ab initio ∇_kρ_cv at the Si extremum and WP3's PAER spectrum at the same (q,ω) (specified in §8 "Exciton gaps").

---
## 4. Homogeneous electron gas and plasmons (L10, L11)

**4.1 HEG limit [D].** Jellium, plane-wave KS states, 𝒳 = RPA: [E1] becomes the Lindhard L. Its e–h continuum is
ω ∈ [max(0, q²/2m_e − qv_F), qv_F + q²/2m_e]. [E6] gives S_ss = ¼S^{Lin, unscreened}; [E5] gives Π^γ_T, matching 2608.20715 Eq. (13) in
structure. Si valence numbers (C7): r_s = 2.01, k_F = 3.57 keV, v_F = 6.98×10⁻³, ω_p = 16.6 eV.

**4.2 Plasmon [D, small-q RPA] (C7a–c).** At the zero of ε₁ with ε₂ → 0, Im[−1/ε] = πδ(ω − ω_pl)/∂_ωε₁. With
ε₁ = 1 − ω_p²/ω² − (3/5)ω_p²q²v_F²/ω⁴ (2003.12077 Eq. (5)):

  L_pl(q,ω) = (πω_p²/2ω_pl) w_pl(q) δ(ω − ω_pl(q)),   ω_pl² = ω_p² + (3/5)q²v_F²,   w_pl = 1 + O(q⁴),                               [E9]

so the pole carries the full f-sum ∫₀^∞dω ωL = (π/2)ω_p² to O(q²). **The Landau onset ω_pl(q) = qv_F + q²/2m_e is at q_c ≈ 2.24 keV for Si**
with the [E9] dispersion (C7b; B-15). v2's 1.88 keV used the constant ω_p; the difference is not small because (3/5)(q_cv_F)²/ω_p² ≈ 0.5
(settles D2). Reaching ω_p needs q ≥ ω_p/v_max = 6.26 keV > q_c (C7c), so **no bulk plasmon is produced by halo DM** in the electronic
sector **[D]** (A-15, B-15). In real Si the 16.6 eV plasmon sits inside the interband continuum (width 3–4 eV); by [E2] its final states are
e–h pairs with branching 1 at clamped nuclei (WP0-v2 (7.1); CONVENTIONS §13 item 21). Plasmon → phonon branching is X+ (WP3), ~η_ep **[E]**.

---
## 5. Core and relativistic states (G7; the factorisation question of 2509.14534)

**5.1 Factorisation theorem [D].** Hypotheses: Born in H_int; 4-component (no-pair) target Hamiltonian; DM–electron interactions written as
Dirac bilinears. WP0-v2 (3.3) holds unchanged with the target operators

  O_{(e,Γ)}(q) = ∫d³r ψ̂†(r)γ⁰Γ e^{iq·r}ψ̂(r),   Γ ∈ {1, γ⁵, γ^μ, γ^μγ⁵, ½[γ^μ,γ^ν]},

and 𝔇 built from the DM bilinears. It factorises into a single scalar K-factor only if one target operator survives (scalar and pseudoscalar
couplings, the 2509.14534 finding); vector and axial couplings give a matrix S. Whether 2509.14534's "off-shell bound electron with free
kinematics" problem is an artefact of matching NR-EFT with free on-shell spinors is **UNRESOLVED by R7** (not re-fetched). **URF statement
[D]:** factorisation of DM physics from target physics is exact; factorisation into "free amplitude × scalar form factor" is valid only for
the n_e row (and s_e) at O(v_e⁰). (A-16, B-16: STANDS for this part.)

**5.2 Foldy–Wouthuysen reduction [D to O(1/m_e²)].**
- ψ̂†ψ̂ → n_e(q)(1 − q²/8m_e²) + (i/4m_e²)Σσ·(q × p)e^{iq·r} (picture change);
- ψ̂̄ψ̂ → n_e − (1/2m_e²)Σ½{p², e^{iq·r}} + …;
- ψ̂†γ⁰𝛄ψ̂ → j_e − (i/m_e) q × s_e (the g = 2 magnetisation current (1/m_e)∇ × s_e; overall sign by the Fourier convention), **corrected from
  (i/2m_e)q × s_e** (B-16, B §I). Check C2d: in the Pauli limit χ′†(σ·p′σ^i + σ^iσ·p)χ/2m_e = (p + p′)^i/2m_e − (i/m_e)(q × s)^i, q = p′ − p,
  s = σ/2.

The 16-row NR basis of WP0-v2 §2 is the O(v_e¹) truncation; corrections are O(⟨p²⟩/m_e²) ≈ (Z_κα)² **[E]**:

| Shell | O(⟨p²⟩/m_e²) |
|---|---|
| Si 1s | (Z_κα)² = 0.010 |
| Ge 1s | (Z_κα)² = 0.055 |
| Ge 3d | ~10⁻³ estimate; bounded by ≤ 2% (SO split/binding = 0.58/29.5) (B §I: one statement used throughout) |
| valence | α² ~ 5×10⁻⁵ |

**5.3 Relativistic f-sum [D] (C2a–c).** Hypotheses: Breit–Pauli one-body terms, closed shells. Darwin is multiplicative and SOC is linear in
p at fixed r, so both give an identically zero double commutator (C2b). Only mass-velocity contributes:

  𝓜¹_ee = (𝓃_eq²/m_e)[1 − (5/3)⟨T⟩/m_e − q²/4m_e² + O(m_e^{-4})],   ⟨T⟩ = mean kinetic energy per electron,                           [E11]

i.e. δ_rel = −(5/3)⟨T⟩/m_e − q²/4m_e² (= WP0-v2 (4.6′)). All electrons: Si −0.18%, Ge −0.58% (Ge 1s alone −4.5%). The two-body Breit
orbit–orbit term (REF-WP0-A: ≈ 27% of the mass-velocity shift) is outside these one-body hypotheses and is WP0's item. In 4-component theory
without no-pair projection the double commutator vanishes (the Dirac Hamiltonian is linear in p); codes using Dirac core states must project.

**5.4 What dominates G7 for halo DM [E].** ω ≤ ½m_χv_max² = 3.5 keV × (m_χ/GeV). Ge 1s (11.1 keV) is unreachable; Ge 2p (1.2 keV) only for
m_χ ≳ 0.35 GeV. **The Ge 3d band is the G7 shell.** Ranked: XC placement of the 3d band, 4.5 eV (2306.14944); the core-hole/core-exciton
final state (§3.5); the SOC split, 0.58 eV; scalar-relativistic and operator corrections, ~10⁻³ (≤ 2%). The large-q statement survives as the
Dirac cusp r^{√(1−(Z_κα)²)−1}: the 1s momentum density gains (q/Z_καm_e)^{(Z_κα)²}, ≈ +13% for Ge 1s at q = 10Z_καm_e.

---
## 6. Anisotropy and modulation (L19 electronic; G11)

**6.1 Symmetry theorems [D] (C11).** Hypotheses: nonmagnetic, TR-invariant reference, any T.
- (i) Θn(q)Θ^{-1} = n(−q) with a TR-invariant state gives S(q,ω) = S(−q,ω), with or without SOC and inversion, unreduced q (LFE): **every
  odd-ℓ multipole of S, and of L, vanishes identically** (GaAs included; P,T-broken targets are the converse case, WP0-v2 (4.3), WP4).
- (ii) O_h (Si, Ge) has invariant harmonics only at ℓ = 0, 4, 6, 8, … (C11a). T_d (GaAs) adds ℓ = 3, 7 (xyz), which (i) removes (C11b).
  In both, ℓ = 2 has no invariant: **the first anisotropic multipole is ℓ = 4**.
- (iii) With the pairing of 2607.06005 Eq. (10), the ER rate is Σ_{ℓ even}S_ℓm𝓡^{(ℓ)}_{mm′}(t)f̂_ℓm′. Their Migdal response W_ℓm(ω) (their
  Eq. (39)) is the Y_ℓm moment of the **finite-k** ELF; the projection of an O_h- or T_d-invariant function on ℓ = 2 vanishes at every k, so
  W_2m ≡ 0 in Si and GaAs (the v2 "dipole-vertex" framing was sufficient but narrower than needed, B §J). A one-sidereal-day harmonic is still
  allowed from ℓ = 4 when the crystal axes are tilted with respect to the Earth axis (the m = ±1 entries of 𝓡^{(4)}(t)). WP2's statements
  (cubic harmonic incoherent multiphonon S isotropic; soft-limit Migdal modulation zero) are consistent (IF-7). (A-17, B-17: STANDS.)

**6.2 Consequence for the literature [FT, both referees].** 2607.06005 §III (Fig. 4 discussion): "The modulation of the electron rate at 5 eV
appears roughly like a clean sine wave with a period of one sidereal day, suggesting that it originates primarily from the dipole
component." By (i) that component is zero (CONFIRMED wrong, A and B); any ℓ = 1 in a computed ELF is a numerical artefact. Their Migdal
modulation in Si/GaAs must vanish up to numerical noise (CONFIRMED, A and B). Their ≈ 1% ER modulation is compatible with ℓ = 4 only.
(A-17, B-18: STANDS.)

---
## 7. LIMITS entries
Chains cite WP0-v2 equation numbers; the τ point of each entry is WP0-v2 (9.7). Equation numbers of arXiv sources are given in **PDF
numbering**, with the HTML sequential number where it differs (B §E, A-21, A §A13 (d,f)).

### L1: Essig et al. crystal form factor (1509.01598)
- **Source [FT]:** Eq. (17) (PDF (3.13) per REF-B) dR/dlnE_e = (ρ_χ/m_χ)N_cell σ̄_e α (m_e²/μ²) ∫dlnq (E_e/q) η F_DM² |f_crystal|²;
  Eq. (21) (PDF (3.17) per REF-B) |f_crystal|² = (2π²(αm_e²V_cell)^{-1}/E_e) Σ_{ii′}∫_BZ (V_cell d³k/(2π)³)(V_cell d³k′/(2π)³) E_e
  δ(E_e−E_{i′k′}+E_{ik}) Σ_{G′} q δ(q−|k′−k+G′|)|f_{[ik,i′k′,G′]}|². Spin 2 inside 2π². (E_e = ω, V_cell = Ω.) The Eq. (21) quote itself is
  UNRESOLVED by R7 (A re-derived from it as quoted; B checked the Eq. (17) consistency).
- **Chain [D]:** WP0-v2 (3.3) → (9.1) single n_e row → hypothesis (I) and (9.2) with 𝒢 = η/(2q) → [E1] at 𝒳 = IP → angular average
  (C12a,b; independent re-derivation A §A12):

  |f_crystal(q,ω)|² = (Ω q³/4παm_e²) S̄^{IP}_ee(q,ω) = (Ω q⁵/8π²α²m_e²) ε̄₂^{noLFE}(q,ω).                                                [E12]

  The second equality is 2101.08275 Eq. (16) [FT, CONFIRMED by A] = 2105.02233 Eq. (D2) (HTML (81)). **SOTA #7: CROSS-CHECKED.**
- **Validity:** (a) |ε|² ≈ 1: pointwise 1/|ε|² = 0.117 at 2 keV and 0.451 at αm_e (C7d); the q-integrated overestimate of the IP rate is
  ×1.4–2.5 (2101.08275) — two different numbers (B-4, B §K). (b) T ≪ E_g. (c) pseudo-wavefunctions, accurate to q ≲ 6–8 αm_e (2603.12326).
  (d) a scissor Δ_scis violates the f-sum by +Δ_scisΣ|ρ|², ≈ +3.5% in Si [E]. (e) hypothesis (I), angle-averaged S (WP6-W5); cubic
  anisotropy at ℓ = 4.
- **Leading correction [D]:** within RPA without LFE, S = S^{IP}/|ε_{00}|²; then Δ^τ_LFE and Δ^τ_BSE ([E8]).
- **Discrepancies:** 2105.02233 Eq. (D1) (HTML (80)) re-quotes Eq. (21) with δ(ΔE − E_{ik} + E_{i′k′}), the sign flipped (also Eqs. (37),
  (47)): typographic, **CONFIRMED** (A, B). Catena's 𝒲̄₁ = 8ΔEαm_e²|f_crys|²/q³ is per spin, with their Eq. (45) reproducing 1509.01598
  Eq. (17): consistent, **CONFIRMED** (B). (A-18, B-19: STANDS.)

### L2: dielectric/ELF rate (2101.08275, 2101.08263)
- **Source [FT]:** 2101.08275 Eq. (6): S(ω,k) = (k²/2πα)(1−e^{−βω})^{-1} Im[−1/ε_L(ω,k)] (verified by B); Eq. (13) the rate. 2101.08263
  Eq. (1): Γ(v_χ) = ∫d³q/(2π)³|V(q)|²[2(q²/e²)Im(−1/ε(q,ω_q))].
- **Chain [D]:** WP0-v2 (3.3) → n_e row → (5.5)(i) clamped nuclei (or ω ≫ ω_max) → (5.4) → FDT. 2q²/e² = k²/2πα (C12c). With LFE the exact
  object is (ε^{-1})_{00}(q,ω) [E1], as in 2603.12326 Eq. (16) and 2507.14345.
- **Validity:** DM couples to the electron density only; a dark photon needs the total ε (ionic part 0 in Si).
- **Leading corrections:** (i) KKL App. A work "in the approximation that the dielectric function is a diagonal matrix in reciprocal lattice
  space" (CONFIRMED, B); their "LFE" replacement ε_GG → 1/(ε^{-1})_{GG} is the exact clamped object (CONFIRMED, A). (ii) KKL **Eq. (24)** (PDF;
  HTML (27)) averages ε over directions before inverting (CONFIRMED, A, B); the bias is second order in the anisotropy, ℓ = 4 in cubic
  crystals [D]. (iii) transverse terms for vector mediators: [E4]/[E5], ≲ 10⁻⁹ relative for halo DM. (iv) X+ and ZPR: WP3.
- **Discrepancies:** KKL write ⟨p,ℓ′|e^{ik·r}|p,ℓ⟩ in Eq. (15), a typo for p′ (CONFIRMED, A, B). The sign of k in n_{−k} is immaterial for
  TR-symmetric targets (§6.1 (i)). (A-19 applied; B-20 STANDS.)

### L3: NR-EFT crystal responses (2105.02233, 2009.13534, 2210.14917, 2510.25835)
- **Source [FT]:** 2105.02233 Eq. (36): 𝓡 = (n_χN_cell/128πm_χ²m_e²)∫dlnΔE∫d³q (1/q) η̂ Σ_l Re(R_l^*W_l), with W_l (Eq. (37)) built from
  B₁ = |f′|², B₂ = (q/m_e)·f′𝐟′*, B₃ = |𝐟′|², B₄ = |(q/m_e)·𝐟′|², B₅ = i(q/m_e)·(𝐟′ × 𝐟′*) (Eqs. (38)–(42); scalar f, **vector 𝐟**
  in bold, A §A6); 𝐟 = ⟨ψ′|e^{iq·x}(i∇/m_e)|ψ⟩ (Eq. (11)). 2210.14917 Eq. (18) R ∝ Σ_IF∫ f_scr² F_med² g 𝓕_IF, f_scr = 1/(q̂·ε·q̂)
  (Eq. (23)); axial coupling: "there is no screening" (App. B). 2510.25835 Eq. (5): the rate in terms of χ₀₀, χ_ij, χ_0i; Eq. (6):
  dΓ₈ = (v_⊥²/4)dΓ₁, "v_⊥ is the component of v that is perpendicular to q", v the DM velocity (their v_⊥ = campaign v_T; χ = R).
- **Chain [D]:** WP0-v2 (3.3) → IP R̃ → WP0-v2 (5.3) → §2.1–2.6.
- **Results.**
  - (a) **Catena's responses [D] (C1b, C1c).** For local H, q·𝐟 = −(ΔE − q²/2m_e)f, so 𝒲̄₂ = −(ΔE − q²/2m_e)𝒲̄₁/m_e (real) and
    𝒲̄₄ = (ΔE − q²/2m_e)²𝒲̄₁/m_e² (CONFIRMED, A, B). **New (A-7, B-21):** in TR + inversion targets (Si, Ge) the antiunitary PT maps n → n,
    j → j at the same q, so every S_ab(q) is real: **Im 𝒲̄₂ ≡ 0 and 𝒲̄₅ ≡ 0 for any Hamiltonian, nonlocal pseudopotentials included** (C1c:
    exact lattice model with a nonlocal hop; the identity fails when inversion is broken). With TR alone, Im 𝒲̄₂ is odd in q and vanishes
    after angle averaging; the averaged 𝒲̄₅ is a pseudoscalar, zero in achiral crystals (GaAs) and nonzero only in chiral ones (§2.6, §R1). Hence in Si and Ge only **two** responses are independent for local H (𝒲̄₁ and 𝒲̄₃ − (m_e²/q²)𝒲̄₄); a
    nonlocal V_NL violates the **real** relation Re 𝒲̄₂ + (ΔE − q²/2m_e)𝒲̄₁/m_e = 0 (and the 𝒲̄₄ one). **Withdrawn:** v2's "their small Im 𝒲̄₂
    measures the nonlocal-PP violation [V_NL, n_e]" (REFUTED by A and B). Their own attribution (2105.02233 §III B) of nonzero Im W̄₂, W̄₅ in
    Si/Ge to approximate axial symmetry is likewise wrong: these values are numerical (k sampling, gauge or reconstruction) **[D]**.
  - (b) In medium: 𝒲̄₁, 𝒲̄₂, 𝒲̄₄ are screened by |ε|^{-2}; 𝒲̄₃ contains (m_e²/q²)𝒲̄₄ and is therefore partly |ε|^{-2}-screened; only the
    transverse combination 𝒲̄₃ − (m_e²/q²)𝒲̄₄ (and 𝒲̄₅ where nonzero) is LFE-screened only (A §A6); spin rows follow [E6]. EXCEED-DM's global
    f_scr is right for the n_e row of a dark photon; it is wrong for scalar couplings to n_e (screened too; their "f_scr = 1" for non-mixing
    models is CONFIRMED in FT by A and B) and for current and spin rows.
  - (c) **2510.25835 Eq. (6) for 𝒪₈ is the v_s → 0 truncation of [E4]** (CONFIRMED in FT, A and B: App. A matches with a static electron,
    v_⊥ a DM c-number): it omits tr S_{j_Tj_T} and the cross term. The same omission affects **𝒪₅** (contains q × j_T) and **𝒪₂** (contains
    v_χ·j and a kinetic-type v_s² operator) (B-22). Size: the IP zeroth-moment ratio tr S_{j_Tj_T}/(|v_T|²S_nn) ≈ ⟨p_T²⟩/(m_e²|v_T|²) with
    ⟨p_T²⟩ = (2/3)⟨p²⟩ = (2/5)k_F² gives **≈ 20–30** in Si valence for |v_T|² = (0.7–1.0)×10⁻⁶ (C6e; v2's "40" used ⟨p²⟩) **[E]**; it is a ratio
    of moments valid for q ≫ k_F, not a fixed-(q,ω) ratio. In medium the exact ratio is 2(ω/q)²|ε_L|²(Im ε_T/Im ε_L)/|v_T|² (C6d, B §C),
    larger than the IP value by ≈ |ε_L|²(1 − δ_LFE), i.e. by 2–9 at keV q. **Conservative [D]:** S PSD gives
    |v_T·S_{nj_T}| ≤ |v_T|(S_nn tr S_{j_Tj_T})^{1/2}, so the true 𝒪₈ rate ≥ ¼(|v_T|√S_nn − √tr S_{j_Tj_T})², which exceeds their ¼|v_T|²S_nn
    whenever r ≥ 4 (C6c); with r ≳ 20 the true rate is ≥ (√r − 1)² ≳ 12 times theirs. Their limits are therefore conservative by at least
    an order of magnitude **[E]** (the bound is [D]; "≥ 1 order" uses the IP estimate r ≳ 20); the factor itself is UNRESOLVED pending G10. **Corrected wording:** the 𝒪₈ (and 𝒪₅) rate is **not determined by
    Im(−χ₀₀) = the longitudinal ELF alone**; at SOC = 0 it is determined by the full finite-q dielectric tensor ε_ij(q,ω) (longitudinal,
    mixed, transverse components) (A §A7). For 𝒪₂ even ε_ij is insufficient: the kinetic-energy-density row 𝒯_e is needed [D, sketch].
- **Validity:** SOC = 0 for the singlet/triplet split (Ge near-edge ≲ 10% mixing). For local-H reductions, all-electron or PAW-reconstructed
  states; otherwise the longitudinal relations acquire [V_NL, ·] terms (in the real parts).
- **Leading correction:** the triplet ladder and f_xc^T (spin), LFE on j_T, BSE in both channels.

### L10: Lindhard/Mermin ELF (2101.08275 Eqs. (17)–(24); 2104.12786)
- **Source [FT]:** 2101.08275 Eq. (17): ε_Lin = 1 + (3ω_p²/k²v_F²)[f₁ + i f₂]; Mermin Eq. (22); Eq. (23): ELF = Σ_i A_i(k) Im[−1/ε_Mer(ω_{p,i},Γ_i)]
  θ(ω−ω_edge,i); Eq. (24): A_i(k) renormalised by the f-sum. (Their Γ = campaign γ_rel.) KK breakage by the θ step and the A_i
  renormalisation verified in FT (B-23).
- **Chain [D]:** [E1] → jellium → RPA → Lindhard. Mermin is a number-conserving relaxation-time closure, not a URF rung.
- **Validity:** ω inside the Lindhard continuum and ω ≫ E_g. The HEG has intraband weight below E_g, whereas a clamped insulator has
  S(ω < E_min) = 0; ε_HEG(q→0,0) → ∞, whereas ε_mac(0,0) = ε_∞ = 11.7 in Si.
- **Leading correction [D]:** the HEG xc local-field factor, ε = 1 − v_CR⁰/(1 + v_CG_LF(q)R⁰), then band structure.
- **Discrepancies:** their step θ(ω−ω_edge) breaks KK and the built-in Mermin f-sum, hence Eq. (24); Re ε^{-1} must be regenerated, as KKL do.
  (B-23 STANDS.)

### L11: plasmon production (2002.06937, 2003.12077)
- **Source [FT]:** 2003.12077 Eq. (5): ε̂_L ≈ 1 − (ω_p²/ω²)(1 + (3/5)k²v_F²/ω_p²); Eq. (7): Z_L ≈ 1 − (3/5)k²v_F²/ω_p². 2002.06937 Eq. (4):
  "q_c ∼ 2π/a ∼ 5 keV, where a is the lattice spacing" (FT quote, B); Eq. (13): P(E) = (α/π²)∫d³q q^{-2}Im{−1/ε(E,q)}δ(E − q·v + q²/2m_χ);
  Eq. (14): dR/dE ∝ S(E)∫₀^{q_c}dq η/q.
- **Chain [D]:** [E1] → pole [E9]. For a light mediator coupling to total charge, WP0-v2 (3.3) with |Ṽ|² = e_χ²e²/q⁴ gives
  Γ_χ = (α_χ/π²)∫d³q L/q², which is 2002.06937 Eq. (13) (C12d).
- **Validity:** direct plasmon creation needs v ≳ ω_p/q_c ≈ 7×10⁻³ (Si), out of reach for halo DM ([E9]), as both papers find.
- **Leading correction:** [E9] with interband damping; Si's 16.6 eV resonance lies in the e–h continuum.
- **Discrepancies:** three momentum scales: 2π/a_lat = 2.28 keV, ω_p/v_F = 2.38 keV, Landau onset ≈ 2.24 keV ([E9] dispersion; C7b). With a the
  lattice spacing (their definition), 2π/a = 2.28 keV, not 5 keV (5 keV corresponds to the bond length): **CONFIRMED** inconsistent (B, FT;
  settles D6). **Dropped:** v2's "overstates the plasmon phase space ×(5/1.9)²" (REFUTED, B). Their Eq. (14) is logarithmic in q, so for the
  fast component (v ≈ 0.1, q_min ≈ 0.17 keV) the effect is ln(5/0.17)/ln(1.9/0.17) ≈ 1.4 (C12e) **[E]**. Their use of ε(E,0) up to q_c (no
  dispersion, no loss of pole weight) is CONFIRMED in their text (B). Z_L vs w_pl: different normalisations (UNRESOLVED by R7, not re-fetched).

### L14: BSE exciton rate (2507.14345)
- **Source [FT]:** Eq. (1): R = (1/ρ_T)(ρ_χ/m_χ)(π/α)(σ̄_e/μ²)∫d³v f∫d³k/(2π)³ k²|F_φ|²∫dω/2π (1−e^{−βω})^{-1}Im[−1/ε(ω,k)]δ(…).
  Eq. (2): L = L⁰ + L⁰ΞL in TDA, ε_M(k=q+G) = 1/ε^{-1}_{GG}(q,ω). (Their L, Ξ, W = campaign L^{BSE}, Ξ^{BSE}, W^{scr}; F_φ = F_DM.)
- **Chain [D]:** [E1] with 𝒳 = BSE → [E7]; Eq. (1) is L2 with the BSE ELF.
- **Validity:** static W^{scr}; TDA (breaks f-sum and KK; the authors find a NaI change beyond TDA); scissor QP; 10 CBs (Fig. S2: ELF
  decreases with more CBs); 6³ k-grid, which cannot resolve Wannier excitons with a_x ≫ a_lat: only the Sommerfeld part of [E8] is captured.
  These limitations are **CONFIRMED** in FT (B-25).
- **Leading correction:** beyond-TDA coupling; the bound lines [E8] (type A); selection rules §3.2; exciton–phonon replicas (WP3).

### L17 (electronic part, with WP0-v2 §9.2)
- (a) the f-sum (9.5) holds for IP, RPA(±LFE) and adiabatic TDDFT with local H;
- (b) it is broken by a scissor (+Δ_scisΣ|ρ|²), nonlocal PPs, TDA-BSE and relativistic cores without no-pair projection ([E11]);
- (c) the hypothesis ε(q,0) ≥ 1 is **DERIVED at RPA+LFE for any insulator** ([E3]); beyond RPA it holds under (1.4′), (−R⁰)^{-1} + f_xc > 0,
  and ε(q,0) < 0 is excluded only under that condition (B-26). REF-WP0-A/B add that for electron-only coupling with a relaxed lattice the
  two-fluid ε_e^{-1} can be negative: WP0's item; [E3] is the clamped statement;
- (d) the relativistic factor on ω_{p,e}² is −0.23% (Si), −0.73% (Ge) in total, i.e. the one-body mass-velocity part −0.18%/−0.58% ([E11])
  plus the Breit orbit–orbit term (WP0-v3 G4; AUDIT-2 m14);
- (e) source formulas as read by WP0 (2110.01587 Eq. (1); 2608.05282 Eq. (8)). (A-20 STANDS.)

### L19 (electronic part): daily modulation from the anisotropic ELF (2607.06005; lattice 2411.03433 → WP2)
- **Source [FT, A and B]:** 2607.06005 Eq. (6), Eq. (10) (T_ℓm = campaign S_ℓm up to the S ↔ L factor); "the only anisotropic contribution
  to the event rate is from the quadrupole term (ℓ = 2)" (§II after Eq. (41), Migdal); §III Fig. 4 sentence quoted in §6.2.
- **Chain [D]:** WP0-v2 (3.4) without angular average; [E1] for S.
- **Content [D]:** §6.1: odd ℓ ≡ 0 (TR); no ℓ = 2 in cubic crystals, first term ℓ = 4; zero Migdal ELF modulation at every k in Si, Ge, GaAs.
- **Discrepancy:** the "dipole component" attribution (CONFIRMED wrong); their ≈ 1% ER modulation is consistent with ℓ = 4 only.

---
## 8. Gaps: formula and computation specification

**G5 (screening and many-body beyond RPA).**
- **Formula:** [E1] with 𝒳 = BSE beyond TDA, [E7], assembled as S^{BSE} (q ≤ 10 keV, ω ≤ E_g + 10 eV) ⊕ S^{RPA+LFE} (elsewhere), matched on a
  strip; the f-sum ∫_ℝ dω ω S = π𝓃_eq²/m_e constrains only the non-conserving parts (TDA, scissor, band cutoff).
- **Spec:** QE/PBE (or exciting) → G₀W₀ (BerkeleyGW or Yambo) → finite-Q BSE (BerkeleyGW finite-Q, Yambo q ≠ 0, or exciting). Pair basis
  4 VB (Ge: + 3d, G7) × 12 CB. Grids: coarse 8³ kernel (24576 pairs, ≈ 10 GB per q_r stored), **interpolated to the fine 24³ grid with
  on-the-fly matrix–vector products; the dense fine kernel (6.6×10⁵ pairs, 4.4×10¹¹ complex entries ≈ 7 TB per q_r) is never stored**
  (A-22, B-27). Solver: Haydock/Lanczos (≈ 200 iterations, matrix-free); coupling (non-TDA) checked against the f-sum to < 1%. Momentum points:
  q_r on the 24³ commensurate set and G-shells with |q| ≤ 10 keV (≈ 10³ (q_r,G) points after O_h). Cost: ≈ 200 × (fine pairs × interpolation
  stencil) per q_r ≈ 10¹³–10¹⁴ flop; total ≈ 10³ node-h **[E]**. Bound lines: added analytically by [E8] with ab initio μ_x, ε_∞,
  ρ_cv(k_v,q) and ∇_kρ_cv at the extrema. Validation: Si NIXS/EELS at q < 3αm_e. Outputs: L(q,ω) on (q̂, |q|, ω) bins; Δ^τ_BSE (type M; bound
  lines type A); p_on per [E10].

**G7 (core, all-electron, relativistic).**
- **Formula:** [E1] + [E7] with 4-component or ZORA states, FW-corrected operators §5.2 (spin curl (i/m_e)q × s_e), [E11] as the check.
- **Spec:** all-electron FLAPW (exciting or WIEN2k) with SOC, or PAW plus core reconstruction, for Ge 3d, Ga 3d, Si 2p. 3d binding: PBE vs
  HSE06 vs G₀W₀ vs ΔSCF, spread as the nuisance (target 29.5 eV). Core-level BSE at finite q, 3d₅/₂/3d₃/₂ resolved. q ≤ 30 keV, ω ≤ 200 eV, 12³ k.
- **Remaining gap:** no crystal 4-component response code with no-pair projection at finite q; ZORA + SOC is the practical limit, error
  ~10⁻³ (bounded by 2%) for Ge 3d **[E]**.

**G10 (non-density operators).**
- **Formula:** §2.6, [E4]–[E6]: the screened singlet block and the IP block (12 real functions per (q,ω) in Si/Ge, 18 at fixed q̂ in general).
- **Spec:** QE/EXCEED-DM-type IP module. Vertices ρ_cv(k,q+G) and ⟨c|½{p, e^{iq·r}}|v⟩/m_e with the nonlocal-PP commutator correction (or
  PAW). Screening: RPA+LFE Dyson with the mixed blocks R̃_{j_T,n(q+G)}; spin: triplet ladder or ALDA f_xc^T, **which needs the full IP matrix
  R⁰_{GG′}, to be output** (B §K). Grids as QCDark2 (10³ k, q ≤ 25αm_e, LFE cutoff ≈ 8αm_e). Diagnostics: Im S_{nj_T}, S^{anti}_{j_Tj_T} < 10⁻³
  of the real parts in Si/Ge (PT zero). Outputs: versioned library tables (WP6), enabling recasts of 𝒪₅, 𝒪₈ (fixing 2510.25835); 𝒪₂ needs the
  𝒯_e row in addition.

**G11 (anisotropy, electronic).**
- **Formula:** §6.1 and the 2607.06005 Eq. (10) pairing, S_ℓm restricted to even ℓ, cubic harmonics K^cub_ℓ (ℓ = 0, 4, 6, 8).
- **Spec:** full-q RPA+LFE ELF (GPAW, QCDark2 or BerkeleyGW), projected on K^cub_ℓ to ℓ = 8 per (|q|, ω). Diagnostics |S_{1m}|, |S_{2m}|,
  |S_{3m}| / S₀₀ < 10⁻³. Outputs: S₄, S₆, S₈(|q|, ω) for Si/Ge/GaAs and the modulation amplitude for a site latitude. (B-27: sufficient.)

**Exciton gaps (catalog-processes §12 item 3).**
- **Formulas:** [E7], [E8] (corrected second class), §3.2 rules (with the nonsymmorphic phase), **[E13] thresholds as min over q**, [E10]
  onsets, [E14] ZPL/PAER ratio, [E6] plus triplet BSE (spin-coupled DM).
- **Spec:** as G5, plus: (i) ab initio E_min(q) and the exciton dispersion along the full Γ–X line on both sides of X (Si) and along Γ–L and
  near Γ (Ge), then [E13] class-resolved (B §K); (ii) ρ_cv and ∇_kρ_cv at the Si extremum (for ℓ_∇ in [E14]) and the (2̄00) Umklapp vertex
  magnitude; (iii) WP3's S^{PA}(q,ω) on the same (q,ω) points for η_PA; (iv) effective-mass hydrogenic series with ab initio anisotropic masses
  (Lipari–Baldereschi).
- **Remaining gaps:** exciton–phonon replicas (WP3); Frenkel/self-trapped excitons in NaI (WP3/WP5); beyond-TDA finite-q BSE has never been
  run for DM.

---
## 9. WP0 defects reported by WP1 v1: status
| v1 label | Defect | Status |
|---|---|---|
| WP1-D1 | (4.6), (5.3) extra (q²/2m)n in [H, n] | applied in WP0-v2 |
| WP1-D2 | δ_rel from SOC | applied: mass-velocity only (Breit orbit–orbit now a WP0 item, REF-WP0-A) |
| WP1-D3 | Ge sizes | applied: 0.055 / ~10⁻³ (≤ 2%) |
| WP1-D4 | j_T "unscreened" | applied: LFE-screened |
| WP1-D5 | spins "unscreened" | applied, now to read "triplet ladder + f_xc^T", not f_xc^T alone (B-7) |
| WP1-D6 | (7.2) weight vs (1+Rv)_{0G} | resolved (out-state weight) |

---
## 10. Exact remaining gaps
1. Ab initio zero-phonon thresholds [E13] (Si: both sides of X; Ge: L and Γ) and the ratio [E14] (needs ∇_kρ_cv and WP3's S^{PA} on the same grid).
2. Finite-q BSE beyond TDA for Si/Ge with bound lines (G5). Interim Δ^τ_BSE ∈ [+0.3, +1.0]×S near the edge (type M) plus the bound lines (type A).
3. A 4-component crystal response with no-pair projection (G7); interim ~10⁻³ (≤ 2%) for Ge 3d.
4. The triplet channel beyond IP in insulators (ladder + f_xc^T); interim: the singlet Sommerfeld range ×1.3–2 near the edge.
5. LFE screening of j_T (10–30% [E]) and the in-medium 𝒪₈ ratio (G10).
6. SOC mixing near the Ge edge (≲ 10% [E]) and the SOC-lifted Si on-axis vertex (≈ 4% amplitude [E]).
7. Plasmon → phonon branching (X+, WP3).

---
## 11. Interface flags (changes that alter a quantity another package uses)
| # | Owner | Quantity | v2 | v3 | Action |
|---|---|---|---|---|---|
| IF-6 | **WP3 (§M9, IF-8), WP6, M1/SOTA** | Si/Ge zero-phonon boundary | 0.472 (Si, forbidden), 0.708 (Si, allowed), 0.420 MeV (Ge); "the boundary WP3 must use" | **[E13] min over q**: Si 0.42 (second class; bright state 2p), 0.54 MeV (allowed by symmetry, (2̄00) branch at X, vertex possibly small; (1̄11) at 0.62); Ge 0.32–0.36 MeV (allowed); floors 0.329/0.211 MeV; all [E] pending ab initio E_min(q) | WP3: Si PAER-only window **≈ 0.333 (replica) / 0.337 (continuum) – ≈0.42 MeV**; PAER-leading to ≈ 0.43 MeV; comparable 0.43–0.54 ([E14]); allowed ZPL by symmetry from ≈ 0.54 MeV, leading only if the (2̄00) vertex is not small, else from ≈ 0.62 MeV [E]; Ge PAER-only ≈ 0.213–0.32 MeV. WP6: edges and m_min tables use [E13] |
| IF-6b | WP3, WP6 | forbidden ZPL vs PAER | — | ϖ_II [E14] ≈ 0.03–2 at the edge, 0.2–15 at ε_ex = 0.1 eV (η_PA calibration transferred [E]) | WP3 to supply S^{PA} on the same (q,ω); WP6 to carry the 0.43–0.54 MeV Si band as a two-channel region |
| IF-4 | WP6 (3.3), O6-2 | onset exponents p_on | Si allowed Umklapp at \|q\| ≥ 3.25 keV | allowed on-axis branch for \|q\| ≥ 2.28 keV (extremum 2.63 keV); threshold at q^{ZP}, not \|Q_x + G\| | exponent rules unchanged; locations change |
| IF-3 | WP6 (ladder nuisance) | type-A amplitude of second-class bound lines | (n_H² − 1)/(πa_x⁵n_H⁵) | ÷3 | WP6 fallback amplitudes for Si second-class lines ÷3 |
| IF-10 | WP6 (library, G10), WP0-v2 | response-set size | 7 functions | 12 (Si/Ge), 18 (general, fixed q̂) + R⁰_{GG′} | library schema; Im/antisymmetric parts are PT-zero diagnostics in Si/Ge |
| IF-11 | WP0-v2 §2 table, G7, WP4 | Dirac vector current, spin curl | (i/2m_e) q × s_e | (i/m_e) q × s_e (sign by convention) | WP0 operator table / any magnetisation-current row |
| IF-12 | WP0-v2 §9.2 (iii), L17 (c) | beyond-RPA hypothesis for ε ≥ 1 | 1 − f_HxcR⁰ > 0 | (−R⁰)^{-1} + f_xc > 0 | WP0 to restate (iii) |
| IF-13 | WP0-v2 (5.3), CONVENTIONS §7 | spin-row screening statement | "xc-renormalised by f_xc^T" | triplet W^{scr} ladder + f_xc^T; R̃_s ≡ 4R_{s^zs^z} | CONVENTIONS §7 wording; WP4/WP6 spin-operator nuisances (×1.3–2 near edge) |
| IF-14 | LIMITS L3, SOTA | 2510.25835 𝒪₈ factor; Catena count | ≈ 40, "O(10)"; 3 of 5 | IP 20–30, ≥ 12× with medium enhancement, factor UNRESOLVED; 2 independent in Si/Ge; 𝒪₂, 𝒪₅ also affected | LIMITS L3 text |
| IF-15 | WP0-v2/WP6 users of tr S_{j_Tj_T} | transverse trace | (4ω²/e²) Im ε_T | Σ_λ(2ω²/e²) Im ε_{T,λ} | only for q̂ off the 3-/4-fold axes |
| IF-16 | LIMITS L1 (a), WP6 nuisance sizes | screening factor | "1/\|ε\|² 0.1/0.44 = ×1.4–2.5" | pointwise 0.117/0.451; rate ratio ×1.4–2.5 separately | wording |
| IF-17 | LIMITS L11, WP5 (plasmon) | Landau onset q_c | 1.88 keV | ≈ 2.24 keV | numeric only; no-plasmon conclusion unchanged |
| IF-1, IF-2, IF-5, IF-7, IF-8 | WP3, WP5, WP2, WP0 | as v2 | — | unchanged ([E2] out-state; ALP triplet vertex now with the ladder caveat; cubic anisotropy; F11) | none |
| IF-9 | NOTATION | new symbols | — | §15 | rows requested |

---
## 12. Contested corrections
None against CORRECTIONS.md. One referee statement is rebutted (§R1); disagreements are settled in §R2.

---
## R1. Rebuttals (go back to the named referee)

**To REF-B (§G, item B-13, Ge part): "Ge zero-phonon via the direct Γ valley opens at 2E_dir/v_max² ≈ 0.256 MeV".**
The number is the flat-band floor of [E13], not an onset. Derivation: for a Γ-valley pair, E^{ZP}(q) ≥ E_dir − E_x^b(dir) + q²/2M_x(q),
and for parabolic bands M_x = m_c(Γ) + m_hh ≤ 0.038 + 0.50 = 0.54 m_e (heaviest hole direction). The reachable energy at fixed q is
qv_max − q²/2m_χ ≤ qv_max, so the channel requires qv_max − q²/2M_x ≥ E_dir − E_x^b(dir) for some q, i.e. M_xv_max²/2 ≥ 0.888 eV: 0.965 eV, so
it is open, but [E13] then gives m_χ^{ZP} = 3.1 MeV (C9f). For the Γ channel to open below the Ge L-valley onset (≈ 0.32 MeV) the Γ-pair
dispersion must stay below q²/2(2.3 m_e) at q ≈ 0.67 keV (C9f), i.e. a pair kinetic energy ≤ 0.19 eV at 31% of q_BZ, whereas the Ge heavy-hole
band (L₃′ at −1.43 eV at the zone edge) lies roughly 0.5 eV down there **[E]**. Hence the Ge zero-phonon onset is the L-valley value
≈ 0.32–0.36 MeV [E] (consistent with REF-A's 0.32 and REF-B's own L-valley 0.33–0.37 MeV), and the Ge PAER-only window is ≈ 0.213–0.32 MeV,
not "effectively closed at 0.256 MeV". The ab initio Γ–L dispersion remains the decisive input (§8).

**To REF-B (§E, item B-9): "14 real functions (7 screened singlet + 7 IP)".** The triplet must be counted (B is right on that), but the
singlet "7" assumed a real S_{nj_T} (2 numbers) together with a nonzero antisymmetric jj block (1 number). Reality of S_{nj_T} requires PT,
which also kills the antisymmetric block (B's own §E), so no symmetry class has 7. The counts are 6 + 6 = 12 (Si, Ge) and 9 + 9 = 18 at fixed q̂
without symmetry (§2.6). The IP triplet block is ¼ of the IP singlet block and costs no extra functions; its dressing needs R⁰_{GG′}.

**To REF-B (§E (iii)): "for TR alone, S^{anti}_{jj}(q) = −S^{anti}_{jj}(−q), so the angle-averaged 𝒲̄₅ ≡ 0".** The premise is right, the
conclusion does not follow: 𝒲̄₅ ∝ i(q/m_e)·(𝐟′ × 𝐟′*) contracts the axial vector g(q) of S^{anti} with q, and q·g(q) is **even** in q when g is
odd. The isotropic (ℓ = 0) part of q·g is a pseudoscalar, which is nonzero in chiral TR-invariant crystals (natural optical activity) and
zero in achiral ones. For GaAs (T_d, improper operations present) the averaged 𝒲̄₅ does vanish, by achirality, and at fixed q̂ the first
allowed pseudoscalar is of degree 6, (q_x² − q_y²)(q_y² − q_z²)(q_z² − q_x²), consistent with REF-A's "allowed only beyond linear order in q".
The v3 text (§2.6, L3 (a)) uses this reason.

---
## R2. Referee disagreements and how they are settled
| # | Item | REF-A | REF-B | Settlement (derivation) | Right |
|---|---|---|---|---|---|
| D1 | Si selection rules, nonsymmorphic phases (A-11, B-11) | (2̄00) Umklapp allowed on axis (phase e^{−iG·t_d} survives) | "the nonsymmorphic phases cancel" (item STANDS) | The operator acquires e^{−iq·t} and the Bloch state e^{−ik_c·t}: the residue is e^{−iG·t}, which cancels only for G·t_d ∈ 2πℤ. B's statement is exact for G = 0 (C10a) and fails for G = (2̄00), G·t_d = −π (C10c). Cross-check: Δ₁ ↔ Δ₂′ relabelling across X (C10e) | **A** (B correct at G = 0 only) |
| D2 | Landau onset q_c (A-15/A13(c), B-15) | change O(q²v_F²/ω_p²), negligible | 2.2–2.3 keV | At q_c, (3/5)(qv_F)²/ω_p² ≈ 0.5, so the "small" term is not small; exact root of the quartic gives 2.24 keV (C7b). Conclusion (no plasmon) unchanged for both | **B** (number); both on the conclusion |
| D3 | 𝒪₈ factor (A-8, B-22) | 20–30, CONFIRMED (⟨p_T²⟩) | ≈ 25 at IP; larger in medium; UNRESOLVED | A's number is the IP zeroth-moment ratio (C6e); B's exact in-medium ratio (C6d) multiplies it by ≈ \|ε_L\|²(1 − δ_LFE) = 2–9. "Conservative" is robust for r ≥ 4 (C6c) | both: A for the IP value and the direction, **B** that the factor is UNRESOLVED |
| D4 | "determined by the dielectric function" (A-8, B-22) | REFUTED as worded: holds for the full ε_ij | fails for 𝒪₂, 𝒪₅, 𝒪₈ (holds for 𝒪₁, 𝒪₁₁) | Their claim is about Im(−χ₀₀) (B's FT quote). 𝒪₅, 𝒪₈ need S_{nj_T}, S_{j_Tj_T} ⊂ ε_ij(q,ω) (A right that ε_ij suffices); 𝒪₂ contains v_s², a 𝒯_e row outside ε_ij (B's extension, strengthened) | both, on different objects; wording in L3 (c) |
| D5 | response count (A-9, B-9) | redo with symmetry reductions | 14 | §2.6 and §R1: 12 (Si/Ge), 18 (general) | **A** on the method; B's triplet inclusion kept |
| D6 | 2002.06937 q_c ≈ 5 keV (L11) | UNRESOLVED (may be the bond length) | CONFIRMED (FT: "a is the lattice spacing") | The paper defines a as the lattice spacing (B's FT quote); 2π/a_lat = 2.28 keV; 5 keV ↔ 2π/2.35 Å (bond). A did not re-fetch | **B** |
| D7 | KKL equation number (A-19, B §K) | Eq. (24); no Eq. (27) | PDF (24) = HTML (27) | Same equation; PDF numbering adopted with the HTML number noted | both |
| D8 | Ge threshold (A-12, B-13) | ≈ 0.32 MeV (L) | L 0.33–0.37; Γ 0.256 MeV | L: 0.32 (M_x = 2.09 m_e) to 0.36 (M_x/2) (C9e); Γ rebutted (§R1, C9f) | **A** on the Ge onset; B's L range consistent |
| D9 | [E6] normalisation (A-6, B-7) | consistent | unstated | Both: the v2 algebra is right once R̃_s ≡ R_mm = 4R_{s^zs^z} is stated | both |

---
## R3. Literature claims after R7 (CONFIRMED kept, REFUTED dropped, UNRESOLVED marked)
| Claim | Rating (referee) | In v3 |
|---|---|---|
| 2510.25835 Eq. (6) omits the electron-velocity (current) part of 𝒪₈ | CONFIRMED (A, B) | kept, L3 (c) |
| … also 𝒪₂, 𝒪₅ | CONFIRMED (B) | kept |
| 2510.25835 𝒪₈ limits conservative | CONFIRMED in direction (A; robust, C6c) | kept |
| … size "O(10)" / "≈ 40" | UNRESOLVED (B); A: 20–30 at IP | marked UNRESOLVED; IP 20–30 [E] |
| 2510.25835 "determined entirely by the dielectric function" fails | fails for Im(−χ₀₀) (B CONFIRMED; A agrees on ε_L alone); package wording REFUTED (A) | reworded |
| 2105.02233 𝒲̄₂, 𝒲̄₄ fixed by 𝒲̄₁ (local H) | CONFIRMED (A, B) | kept |
| package: Im 𝒲̄₂ measures [V_NL, n_e] | REFUTED (A, B) | **dropped** |
| 2105.02233 §III B: nonzero Im W̄₂, W̄₅ in Si/Ge from approximate axial symmetry | wrong (A, B: PT ⇒ ≡ 0) | kept as [D] statement |
| 2105.02233 Eq. (D1) (HTML (80)), (37), (47) δ sign | CONFIRMED typo (A, B) | kept |
| 2105.02233 Eq. (45) ≡ 1509.01598 Eq. (17) | CONFIRMED (B) | kept |
| 2210.14917 f_scr = 1 for non-mixing models (no screening for scalar n_e couplings) | CONFIRMED (A, B) | kept |
| 2210.14917 axial "no screening" misses triplet effects | CONFIRMED (B); vertex is K_e·σ_e (A) | kept |
| 2607.06005 "dipole component" attribution | CONFIRMED wrong (A, B) | kept |
| 2607.06005 Migdal modulation in Si/GaAs | CONFIRMED must vanish (A, B) | kept |
| 2101.08275 Eq. (15) typo; diagonal-ε approximation; LFE replacement exact; average before inversion (Eq. (24)) | CONFIRMED (A, B) | kept |
| 2101.08275 Eq. (16) = [E12] | CONFIRMED (A) | kept |
| 2002.06937 q_c ≈ 5 keV ≠ 2π/a_lat | CONFIRMED (B, FT); A UNRESOLVED | kept (D6) |
| 2002.06937 phase space overstated ×(5/1.9)² | REFUTED (B) | **dropped**; log factor ≈ 1.4 [E] |
| 2507.14345 6³ grid, 10 CBs, TDA | CONFIRMED (B) | kept |
| 2101.08275 Mermin/θ step breaks KK; A_i renormalisation | CONFIRMED (B) | kept |
| 2509.14534 off-shell artefact; 2003.12077 Z_L normalisation; 1509.01598 Eq. (21) quote; 2608.20715 Eq. (2) | UNRESOLVED (A, not re-fetched; B not rated) | marked UNRESOLVED |

---
## 13. Closing table (one row per referee item)
Status: **applied** (correction made, or STANDS and kept as is), **dropped** (claim removed or replaced), **rebutted** (§R1).
| Item | Verdict | Status | Where |
|---|---|---|---|
| A-1 | STANDS | applied (kept) | §1.1 |
| A-2 | STANDS | applied (kept; T-matrix reading added) | §1.3 |
| A-3 | w/ corr. | applied: (1.4′), DKM, C3c–d | §1.4, L17 (c) |
| A-4 | STANDS | applied (kept) | §2.2 |
| A-5 | w/ corr. | applied: polarisation sum | [E5], IF-15 |
| A-6 | STANDS | applied (kept; normalisation stated, D9) | [E6] |
| A-7 | w/ corr. | applied; V_NL statement **dropped**; PT result, C1c | L3 (a), §2.6 |
| A-8 | w/ corr. | applied: 20–30 (IP), [E], ε_ij wording; old wording dropped | L3 (c), D3, D4 |
| A-9 | w/ corr. | applied: count redone (12/18) | §2.6, D5 |
| A-10 | STANDS | applied (kept) | §3.1 |
| A-11 | w/ corr. | applied: (2̄00) allowed, C10c,e | §3.2 (c), D1 |
| A-12 | FALLS | **dropped** (pinned boundary) and replaced by [E13] | §3.4, IF-6 |
| A-13 | w/ corr. | applied: factor 1/3, continuum replacement, C8b–c; +35% downgraded | [E8], IF-3 |
| A-14 | w/ corr. | applied; "Umklapp only ≥ 3.25 keV" **dropped** | [E10], IF-4 |
| A-15 | STANDS | applied (conclusion kept; q_c number per D2) | §4.2 |
| A-16 | STANDS | applied (kept; FW coefficient fixed per B-16) | §5 |
| A-17 | STANDS | applied (kept) | §6 |
| A-18 | STANDS | applied (kept) | L1 |
| A-19 | w/ corr. | applied: KKL Eq. (24) | L2, D7 |
| A-20 | STANDS | applied (kept) | L14, L17 |
| A-21 | w/ corr. | applied: K_e·σ_e vertex, (B15)–(B18) | §2.4, L3 |
| A-22 | w/ corr. | applied: matrix-free spec | G5 |
| A-23 | STANDS | applied (kept) | §12 |
| B-1 | STANDS | applied (kept) | §1.1–1.2 |
| B-2 | STANDS | applied (kept; Hermitian f_Hxc stated) | §1.3 |
| B-3 | w/ corr. | applied (as A-3) | §1.4 |
| B-4 | w/ corr. | applied: pointwise vs rate ratio, C7d | §1.5, L1 (a), IF-16 |
| B-5 | w/ corr. | applied: [H, s_e] = 0; (Δ_χ/q)n_e remainder | §2.2 |
| B-6 | STANDS | applied (degeneracy stated) | [E5] |
| B-7 | w/ corr. | applied: R̃_s normalisation, triplet ladder | [E6], IF-13 |
| B-8 | STANDS | applied (kept) | §2.5 |
| B-9 | w/ corr. | applied in part (triplet counted); "14" and the §E (iii) reason **rebutted** | §2.6, §R1, D5 |
| B-10 | STANDS | applied (kept) | §3.1 |
| B-11 | STANDS | applied (G = 0 rule kept; phase argument restricted to G = 0, D1) | §3.2 |
| B-12 | STANDS | applied (kept; size downgraded per A-13) | [E8] |
| B-13 | FALLS | Si part applied (pinned values **dropped**, [E13]); Ge Γ 0.256 MeV **rebutted** | §3.4, §R1, D8 |
| B-14 | STANDS | applied (consistency with [E13] stated) | [E10] |
| B-15 | w/ corr. | applied: q_c ≈ 2.24 keV, C7b | §4.2, IF-17 |
| B-16 | w/ corr. | applied: spin curl 1/m_e (C2d); Ge 3d one statement | §5.2, IF-11 |
| B-17 | STANDS | applied (kept) | §6.1 |
| B-18 | STANDS | applied (kept; finite-k framing) | §6.1–6.2 |
| B-19 | STANDS | applied (kept; HTML/PDF numbering) | L1 |
| B-20 | STANDS | applied (kept) | L2 |
| B-21 | w/ corr. | applied (as A-7); V_NL reading **dropped** | L3 (a) |
| B-22 | w/ corr. | applied: 𝒪₂, 𝒪₅; medium factor; number UNRESOLVED | L3 (c), D3 |
| B-23 | STANDS | applied (kept) | L10 |
| B-24 | w/ corr. | applied; ×(5/1.9)² **dropped**, ≈ 1.4 (C12e) | L11 |
| B-25 | STANDS | applied (kept) | L14 |
| B-26 | w/ corr. | applied (as A-3) | L17 (c) |
| B-27 | w/ corr. | applied: G5 matrix-free; G7 consistency; G10 count and R⁰_{GG′}; exciton-gap min_q | §8 |
| B-28 | STANDS | applied (kept) | §12 |

**Count:** 51 referee items. Applied 51 (each row's correction or confirmation is in the text), of which 7 involve **dropped** claims
(A-7/B-21 V_NL reading, A-8 dielectric-function wording, A-12/B-13 pinned thresholds, A-14 Umklapp sentence, B-24 ×(5/1.9)²), and **2
rebutted** in part (B-13 Ge Γ onset; B-9 "14" and B's §E (iii) reason). Not applied silently: 0. Referee disagreements settled: 9 (D1–D9).

---
## 14. Literature
Read in full text in v1/v2 (equation numbers quoted): 1509.01598, 2101.08275, 2101.08263, 2105.02233, 2210.14917, 2510.25835, 2104.12786,
2002.06937, 2003.12077, 2507.14345, 2509.14534, 2607.06005, 2608.20715, 2603.12326. Re-checked in full text by the R7 referees (their
reports): A: 2510.25835, 2105.02233, 2607.06005, 2210.14917, 2101.08275; B: 2510.25835, 2607.06005, 2105.02233, 2002.06937, 2101.08275,
2210.14917, 2507.14345, 1509.01598. No new paper is cited in v3. Band-mass and E_dir inputs of §3.4 are [UNVERIFIED] (from memory) and
enter only [E] numbers.

---
## 15. Symbols introduced/used
All symbols follow NOTATION v4 and CONVENTIONS; no deviation. Used as defined there (unchanged from v2): q, q_r, G_q, ω, ω_q, Δ_χ, v, v_χ,
v^⊥, v_s, v_T, v_max, v_E^ref, v_esc, m_χ, m_min, μ_χe, σ̄_e, F_DM, Ṽ, 𝒪_i, 𝔇, 𝐒_χ, j_χ, e_χ, ρ_χ, ρ_T, f_χ, η, 𝒢, Γ_χ; Ω, N, V, e² = 4πα, α, v_C,
k_c, k_v, E_g, E_dir, E_min(q), E_min,0(|q|), δq̂, ε_{nk}, ψ_{nk}, ψ̂, ρ_cv, n, m, v, c (band subscripts), p, p_T, j_e^α, j_L, j_T, J_T, s_e^α, 𝒯_e,
O_a, Γ, T_e, ⟨T⟩, δ_rel, H; S, S_ab, S̄, S_ℓm, R, R̃, R⁰, Π^γ_T, ε, ε_{GG′}, ε̃, ε₁, ε₂, ε_e, ε_mac, ε_Lin, ε_Mer, ε_L, ε_T, ε_∞, L, 𝓜¹, ω_p, f_xc,
f_xc^T, f_Hxc, G_LF, W^{scr}, A^λ_{cvk}, E_λ, H^{exc}, λ, E_x, E_x^b, a_x, μ_x, Q_x, 𝒮_F, ζ_S, L^{BSE}, Ξ^{BSE}, ω_pl, w_pl, q_c, Y_ℓm, K^cub_ℓ, ℓ, v_F,
k_F, k_TF, γ_rel, Δ_SO, Δ_scis, Z_κ, η_xc, η_ep, 𝓃_e, τ, n_B, 𝒳, Δ^τ_k, r^M_k, X0, X+, Λ, p_on, E_th, a_lat, q_BZ, n_H, α_χ, α_LRC.
**Introduced in v3 (rows requested, IF-9; no collision found in NOTATION v4):**
- **m_χ^{ZP}** — zero-phonon kinematic threshold mass [E13] (distinct from m_min = 2E_th/v_max², the flat-band floor);
- **E^{ZP}(q)** — lowest zero-phonon final-state energy at total momentum q, class-resolved;
- **q^{ZP}** — the |q| at which [E13] is attained (not q_*, which is NOTATION's kinematic-minimum momentum; not WP3's Q*);
- **M_x** — exciton/pair translational mass along the optimisation direction (M_x = m_l + m_hh);
- **m_l, m_hh** — conduction-band longitudinal mass, heavy-hole mass (band inputs; the Luttinger parameters stay source-only notation);
- **k_rel** — relative e–h momentum offset from the minimum-energy pair (κ stays the nuclear species index);
- **ℓ_∇** — vertex-gradient length |∇_kρ_cv|/|ρ_cv^{ref}|; **ρ_cv^{ref}** — reference allowed vertex;
- **η_PA, ε̄_PA** — PAER-to-allowed-ZPL spectral ratio and PAER's own excess energy in [E14];
- **ϖ_II** — forbidden-class ZPL / PAER ratio [E14];
- **ε_ex ≡ ω − E_min(q)** — excess energy above the zero-phonon edge in [E14] (R9: renamed from bare ε, AUDIT-2 m26);
- **t_d ≡ (¼,¼,¼)a_lat** — diamond nonprimitive translation (§3.2; τ stays the truncation multi-index).
Labels (not symbols): BSW irreps Γ₂₅′, Δ₁, Δ₂′, Δ₅, Λ₁, Λ₃, L₁, L₃′, X₁, Δ₆, Δ₇; point groups O_h, T_d, C₄ᵥ, C₃ᵥ; **t_d ≡ (¼,¼,¼)a_lat** is the
diamond nonprimitive translation (new symbol, §3.2; τ stays the truncation multi-index). Labels of this return:
[E1]–[E14], (1.4′), WP1v3-C1…C12 (sub-letters), IF-1…IF-17, D1–D9.

---
## R9 clean-up (coordinator consolidation; edits in place)
Sources: referees/R8/VER-WP1-A.md (N1, N2), VER-WP1-B.md (N1–N4), returns/R8/AUDIT-2.md rows addressed to WP1. Checks re-run: 49/49 PASS
(only the C9g label text changed, ε → ε_ex; no number changed).
| Item | Source | Change | Where |
|---|---|---|---|
| N1 | VER-A N1, VER-B N1 | "allowed ZPL leads above ≈ 0.54 MeV" hedged: allowed by symmetry from ≈ 0.54 MeV ((2̄00) at X); leads only if \|ρ_cv^{(2̄00)}\| ≳ η_PA^{1/2}\|ρ^{ref}\| [E, open]; otherwise the reliably allowed class starts at ≈ 0.62 MeV ((1̄11)); integrated ratio starts at 0 at the onset | §3.4 summary, §3.7 interim statement, IF-6 |
| N2 (A) | VER-A N2 | Si second-class bright state is 2p (or off-axis 1s ∝ \|δq_⊥\|²); [E13] with E_x(1s) is the onset with vanishing weight; 2p shift ≈ 0.001 MeV | §3.4 (after table), summary, IF-6 |
| N2 (B) | VER-B N2 | η_PA calibration (against the allowed ZPL) transferred to the Si G = 0 region tagged [E] | §3.7, IF-6b |
| N3 | VER-B N3 | "conservative by at least an order of magnitude" tagged [E] (bound [D], factor from IP r ≳ 20) | L3 (c) |
| N4 | VER-B N4 | (2̄00) row validity: "at X (band-sticking point; nonparabolic) [E]" | §3.4 table |
| m1 | AUDIT-2 | Si PAER edge 0.338 → ≈ 0.333 (exciton replica) / 0.337 (continuum) MeV [E]; Ge edge quoted 0.213 MeV | §3.4 consequence, §3.7, IF-6, §R1 |
| m14 | AUDIT-2 | L17 (d) quotes the total −0.23%/−0.73% (mass-velocity −0.18%/−0.58% + Breit orbit–orbit, WP0-v3 G4) | L17 (d) |
| m19 | AUDIT-2 | both Si mass sets stated (1.19 m_e here, 1.41 m_e WP3; both [UNVERIFIED]; 0.417 MeV with 1.41); Q_w ≈ 0.31–0.33 Å⁻¹ | §3.4 table and note |
| m26 | AUDIT-2 | bare ε in §3.7/[E14] renamed ε_ex (symbol row added) | §3.7, [E14], IF-6b, §15 |
| m33 | AUDIT-2 | §2.2 spin-current condition: SOC = 0, no H_hf, no B₀ | §2.2 |
| B2, m12, m13, L1, L3, L11 | AUDIT-2 | owned by WP0/WP4/LIMITS; WP1 text already carries the corrected content ((1.4′), IF-13, IF-16, IF-14, IF-17); nothing further in WP1 | — |
