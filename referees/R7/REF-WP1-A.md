# R7 / REF-WP1-A: hostile referee of returns/R6/WP1-v2.md (isolated)

Scope: WP1-v2 with code/WP1-v2/checks.py (re-run: 28/28 PASS, ~3 s), against CONVENTIONS, NOTATION v4, CONTROLS, DONE, LIMITS and
WP0-v2. Full texts fetched and read for this report (then deleted): 2510.25835, 2105.02233, 2607.06005, 2210.14917, 2101.08275.
Referee checks (sympy/closed form, < 1 min, scratchpad): `thr.py` (threshold minimisation), `ell.py` (hydrogenic p-state derivatives),
`umk.py` (diamond space-group selection rule with the nonsymmorphic phases). Tags as in CONVENTIONS §12.

## Verdict table
| # | Claim | Verdict | One-line reason |
|---|---|---|---|
| 1 | [E1] clamped-nucleus ELF form | STANDS | WP0-v2 (5.3)–(5.5)(i) with c = e; unreduced index per CONVENTIONS §2 |
| 2 | [E2] out-state pair weight (ε^{-1})_{G0}ρ(q+G) (F1 accepted) | STANDS | factorisation re-derived; also = T-matrix to the free final pair, ⟨f|(1+V G⁺)V_ext|0⟩ (§A2) |
| 3 | [E3] 0 < (ε^{-1})_00(q,0) ≤ 1 at RPA+LFE, any insulator | STANDS WITH CORRECTION | proof right; the "beyond RPA" condition is misstated (f_Hxc → f_xc; §A3) |
| 4 | §2.1–2.2 continuity, on-shell longitudinal cancellation, [E4] | STANDS | q·v^⊥ ≐ ω_q − ω = 0 for local H, Born, Δ_χ = 0; [E4] trace and cross term re-derived |
| 5 | [E5] S_{j_Tj_T} ↔ Im ε_T | STANDS WITH CORRECTION | "tr = 4ω²Im ε_T/e²" assumes equal transverse polarisations; write Σ_λ (2ω²/e²)Im ε_{T,λ} |
| 6 | [E6] spin channel ¼S^{IP}_nn unscreened, f_xc^T dressing | STANDS | ¼ = tr(σ^ασ^α)/4 ÷ 2; f^T = (f↑↑−f↑↓)/2 consistent with the spin-summed R⁰ (§A5) |
| 7 | L3 (a) "only 3 of Catena's 5 responses independent" | STANDS WITH CORRECTION | true for local H; in TR+inversion targets (Si, Ge) 𝒲̄₅ ≡ 0 and Im 𝒲̄₂ ≡ 0 by symmetry, independent of locality: the "Im 𝒲̄₂ measures [V_NL, n]" statement is wrong for Si/Ge (§A6) |
| 8 | L3 (c) 2510.25835 Eq. (6) is the v_s → 0 truncation; O₈ ×~40; limits conservative | STANDS WITH CORRECTION | CONFIRMED in FT; the ratio uses ⟨p²⟩ not ⟨p_T²⟩ (≈ 20–30, not 40); "fails to be determined by the dielectric function" overstated: it is determined by the full finite-q ε_ij (§A7) |
| 9 | §2.6 "seven real functions" | STANDS WITH CORRECTION | the count does not follow from the listed blocks; with TR+I S_{nj_T} is real and the antisymmetric (𝒲̄₅) block vanishes (§A6) |
| 10 | [E7] exciton contribution with A^{λ*} | STANDS | ⟨λ|n|0⟩ = √2ΣA*ρ; full exchange incl. G = 0 ⇒ improper L |
| 11 | §3.2 (c) selection rules at the extrema | STANDS WITH CORRECTION | Si G = 0 forbidden and Ge G = 0 allowed confirmed; **missed: the Si G = (2̄00) Umklapp is allowed on axis**, |q| = 2.63 keV < 3.25 keV (§A8) |
| 12 | §3.4 thresholds 0.472/0.708/0.420 MeV as "the boundary WP3 must use" | FALLS (as a boundary) | arithmetic correct, but (i) the threshold is min_Q over the exciton/pair dispersion, which lies below the extremum value (Si ≈ 0.42, Ge ≈ 0.32 MeV [E]); (ii) the lowest allowed Si Umklapp gives 0.594 MeV, not 0.708 (§A9) |
| 13 | [E8] Wannier/Elliott limit, 8.0 E_x^b, Sommerfeld numbers | STANDS WITH CORRECTION | second-class bound weight is |∇_kρ|²(n_H²−1)/(3πa_x⁵n_H⁵) for a fixed gradient (factor 3 too large as printed); the +35% at 1.5 eV is a hydrogenic extrapolation to ~100 E_x^b (§A10) |
| 14 | [E10] onset exponents | STANDS WITH CORRECTION | exponent algebra right; the Si sentence "allowed Umklapp class only at |q| ≥ 3.25 keV" falls with #11 |
| 15 | [E9], no bulk plasmon for halo DM, L10, L11 | STANDS | C7 numbers reproduced; ω_p/v_max = 6.26 keV > q_c = 1.88 keV |
| 16 | §5 factorisation, [E11] relativistic f-sum, G7 ranking | STANDS | double-commutator check C2 re-derived; FW signs (§5.2) not script-checked |
| 17 | §6.1 symmetry theorems; §6.2 / L19 verdict on 2607.06005 | STANDS | TR ⇒ S(q) = S(−q) without inversion; O_h/T_d invariants verified; FT quotes verbatim (§A11) |
| 18 | L1 [E12] and SOTA #7 | STANDS | dictionary re-derived independently (§A12); 2101.08275 Eq. (16) confirmed in FT |
| 19 | L2 (KKL statements) | STANDS WITH CORRECTION | substance right; KKL's angular average is their Eq. (24) (arXiv v1), there is no Eq. (27) |
| 20 | L14, L17 electronic part | STANDS | — |
| 21 | 2210.14917 (EXCEED-DM) statements, §2.4 and L3 | STANDS WITH CORRECTION | f_scr = 1 without photon mixing confirmed in FT; their axial vertex is K_e·σ_e (spin-current trace), not s_e; equation numbers are (B15)–(B18) in the arXiv PDF |
| 22 | Gap G5 computation specification | STANDS WITH CORRECTION | a dense BSE kernel at 6.6×10⁵ pairs is ≈ 7 TB per q_r: the spec must be matrix-free/interpolated or the pair window reduced |
| 23 | Contested corrections: none; F1 accepted | STANDS | argument in §12 correct |

## Literature verdicts (rubric (c))
| Claim that a paper is wrong | Rating |
|---|---|
| 2510.25835 Eq. (6) dΓ₈ = (v_⊥²/4)dΓ₁ omits the electron-velocity (current) terms | CONFIRMED (their App. A matches with a static electron, k = (m_e, 0); Table I treats v_⊥ = (1 − q̂q̂)·v as a DM c-number) |
| 2510.25835 O₈ limits conservative by O(10) | CONFIRMED (robust by Cauchy–Schwarz, §A7); size ≈ 20–30, not 40 |
| 2510.25835 "determined entirely by the dielectric function" fails | REFUTED as worded: fails for ε_L alone, holds for the full ε_ij(q,ω) at SOC = 0 |
| 2105.02233: 𝒲̄₂, 𝒲̄₄ fixed by 𝒲̄₁ (local H) | CONFIRMED (their B₂ = (q/m_e)·f(𝐟)*, B₄ = |(q/m_e)·𝐟|², 𝐟 with i∇/m_e) |
| 2105.02233: nonzero Im 𝒲̄₂ "measures the nonlocal-PP violation" | REFUTED for Si/Ge (TR+I force Im 𝒲̄₂ = 𝒲̄₅ = 0 for any H); their own "crystal anisotropy" explanation is also refuted; both are numerical |
| 2105.02233 Eq. (80) (= App. D Eq. (D1)) and Eqs. (37), (47): δ(ΔE − E_ik + E_i′k′) sign | CONFIRMED (typographic) |
| 2210.14917: no screening for scalar n_e couplings | CONFIRMED (f_scr "incorporates screening effects due to mixing … with the photon"; f_scr = 1 otherwise) |
| 2607.06005 §III "originates primarily from the dipole component" | CONFIRMED wrong (ℓ = 1 ≡ 0 by TR) |
| 2607.06005 Migdal daily modulation in Si/GaAs | CONFIRMED zero up to noise (their Eq. (41) keeps ℓ = 0, 2; W_2m = 0 in O_h and T_d) |
| 2101.08275 Eq. (15) ⟨p,ℓ′| for ⟨p′,ℓ′| | CONFIRMED (typo) |
| 2101.08275 "LFE" replacement ε_GG → 1/(ε^{-1})_GG is the exact clamped object | CONFIRMED |
| 2101.08275 average-then-invert bias, second order in anisotropy | CONFIRMED (math); equation number wrong (Eq. (24)) |
| 2002.06937 q_c ~ 5 keV overstates; 2509.14534 off-shell artefact; 2003.12077 Z_L; 2507.14345; 1509.01598 Eq. (21) quote; 2608.20715 Eq. (2) | UNRESOLVED by this referee (not re-fetched); 2002.06937's "2π/a" may use the bond length (2π/2.35 Å = 5.3 keV), so "overstates" needs their definition checked |

---
## Arguments

**A1. [E1].** At n_B = 0, R̃_{eκ} = R̃_{κκ} = 0 so ε = ε_e and WP0-v2 (5.4) with (5.5)(i) is exact; FDT per CONVENTIONS §6. No issue.

**A2. [E2].** R = R⁰(1 + vR) and R† = (1 + R†v)R⁰† give R − R† = (1 + R†v)(R⁰ − R⁰†)(1 + vR). With
(R⁰ − R⁰†)_{GG′} = −2πiV^{-1}Σρ_G*ρ_{G′}δ and (1 + R†v)_{0G} = [(1 + vR)_{G0}]*, the 00 element is −2πiV^{-1}Σ_pairs|Σ_G(ε^{-1})_{G0}ρ_G|²δ.
Index check: R_{G0} = R_{ab} with a = n(q+G) is the response of ⟨n(q+G)†⟩ (the e^{+i(q+G)·r} component of δn) to the field coupled to
n(q), so V_tot(q+G) = (ε^{-1})_{G0}φ_ext. Physical labelling: the amplitude to the bare pair |f⟩ is ⟨f|(1 + V_int G⁺)V_ext|0⟩, retarded,
which is the first factorisation. C4a–e reproduce the claims. Stands.

**A3. [E3].** Static KS R⁰_{GG′}(q,0) = −Σ_f Δ_f^{-1}[⟨0|n_{q+G}†|f⟩⟨f|n_{q+G′}|0⟩ + ⟨0|n_{q+G′}|f⟩⟨f|n_{q+G}†|0⟩] is Hermitian NSD for
any insulator (no TR/inversion needed). With X = v^{1/2}R⁰v^{1/2} ≤ 0, v^{1/2}Rv^{1/2} = X(1 − X)^{-1} has spectrum in (−1, 0], and
(ε^{-1})_00 = 1 + (v^{1/2}Rv^{1/2})_00 ∈ (0, 1] as a diagonal element (convex combination). Correct.
*Correction.* "Beyond RPA this needs 1 − f_HxcR⁰ > 0" is the wrong condition. Stability of the full R (the f_Hxc condition) gives only
(ε^{-1})_00 ≤ 1, i.e. ε ≥ 1 **or ε < 0** (Dolgov–Kirzhnits–Maksimov). The same proof goes through iff the Coulomb-proper R̃ = (1 − R⁰f_xc)^{-1}R⁰
is NSD, i.e. (−R⁰)^{-1} + f_xc > 0 (f_xc alone, not f_Hxc). The quoted HEG instability r_s ≈ 5.25 is the proper (compressibility) one, so
the intended statement is right; the formula is not.

**A4. On-shell projection.** v^⊥ = v_χ − v_s, v_χ = v − q/2m_χ, so q·v_χ = ω_q (Δ_χ = 0). For local H, ⟨f|q·j_e|i⟩ = (E_f − E_i)⟨f|n_e|i⟩
(C1a: [T_e, n_e(q)] = q·j_e exactly). The longitudinal amplitude is (ω_q − ω)⟨f|n_e|i⟩ = 0 on δ(ω − ω_q), so all cross terms with it
vanish too. O₈: amplitude S_χ^α(v_T^αn − j_T^α); (2j_χ+1)^{-1}tr S^αS^β = δ_{αβ}/4; S Hermitian PSD gives
¼[|v_T|²S_nn − 2Re v_T·S_{nj_T} + tr S_{j_Tj_T}] = [E4]. Hypotheses complete (local H excludes SOC and nonlocal PPs, as stated in L3 validity).

**A5. Spin channel.** At SOC = 0, unpolarised: Σ_{ss′}|⟨s′|σ^α/2|s⟩|² = tr(σ^ασ^β)/4 = δ_{αβ}/2 vs Σ_{ss′}|⟨s′|1|s⟩|² = 2 ⇒ ¼. Coulomb
(Hartree) lines couple to n only, so no 1/|ε|² and no LFE. Kernel: V_m = (V↑ − V↓)/2 = [(f↑↑ − f↑↓)/2]δm with m = n↑ − n↓, and
χ⁰_mm = χ⁰↑ + χ⁰↓ = R⁰ (spin-summed), so R̃_m = R⁰ + R⁰f^TR̃_m, S_{szsz} = S_mm/4: [E6] is consistent. 𝓜¹_{szsz} = 𝓃q²/4m_e checks.
The "+10–20%" Stoner figure is a static q → 0 HEG number; at keV q and eV ω it is an upper bound **[E]**.

**A6. Catena's responses (2105.02233 [FT]).** Their B₁ = |f′|², B₂ = (q/m_e)·f′(𝐟′)*, B₃ = |𝐟′|², B₄ = |(q/m_e)·𝐟′|²,
B₅ = i(q/m_e)·[𝐟′ × 𝐟′*] (Eqs. (38)–(42)); 𝐟 = ⟨ψ′|e^{iq·x}(i∇/m_e)|ψ⟩ (Eq. (11)). (WP1's quote drops the boldface, so its B₁ and B₃
read identically: fix the quote.) e^{iqx}p = q·j·m_e − (q²/2)e^{iqx} gives q·𝐟 = −(ΔE − q²/2m_e)f (C1b), hence 𝒲̄₂, 𝒲̄₄ ∝ 𝒲̄₁ bin by bin.
**Missed, and it changes a stated result:** for O_a → η_aO_a(−q) under TR (η_n = +1, η_j = −1) one has S_ab(q) = η_aη_bS_ab(−q)*, and
under inversion S_ab(q) = η_aη_bS_ab(−q). With TR + I both hold, so S_{nj}(q) and S_{j_αj_β}(q) are **real**; a real Hermitian S_{jj}
is symmetric. Therefore, in Si and Ge, Im 𝒲̄₂ ≡ 0 and 𝒲̄₅ ≡ 0 (𝒲̄₅ ∝ Im S_{j_1j_2}, the gyrotropic part), **whatever H is**, nonlocal
PPs included. Consequences: (i) only two responses are independent in Si/Ge (𝒲̄₁ and the transverse 𝒲̄₃ − (m_e²/q²)𝒲̄₄); (ii) L3 (a)'s
"their small Im 𝒲̄₂ measures the nonlocal-PP violation [V_NL, n_e]" is false there: V_NL violates the *real* relation for 𝒲̄₂ and 𝒲̄₄,
while their nonzero Im 𝒲̄₂ and 𝒲̄₅ (their §III B, "not exactly zero" due to approximate axial symmetry) are numerical (k-set or
reconstruction), and both explanations are refuted; (iii) §2.6: S_{nj_T} is a real 2-vector and the antisymmetric block vanishes in
TR+I targets; in GaAs the antisymmetric block is allowed only beyond linear order in q (T_d has no gyration tensor). The "seven real
functions" count should be redone with these symmetry reductions stated. Also L3 (b): 𝒲̄₃ itself contains (m_e²/q²)𝒲̄₄, which is
|ε|^{-2}-screened; only the combination 𝒲̄₃ − (m_e²/q²)𝒲̄₄ (and 𝒲̄₅) is "LFE-screened only".

**A7. O₈ against 2510.25835 [FT].** Their v_⊥ is "the component of v that is perpendicular to q", v the DM velocity (their Eq. (F3):
v_⊥ = (1 − q̂q̂)·v); Table I footnote: v_⊥ is a c-number; App. A matches with a static electron, k = (m_e, 0). So their 𝒪₈ (and every
v_⊥-operator, e.g. anapole → 2𝒪₈, Table II) lacks the electron-velocity part of the Galilean invariant v^⊥ = v_χ − v_s, although their
text says the operators are built "from the Galilean invariants". Eq. (6) is exactly the v_s → 0 limit of [E4]. CONFIRMED.
*Size.* The step tr S_{j_Tj_T}/(|v_T|²S_nn) ≈ ⟨p_T²⟩/(m_e²|v_T|²) is a ratio of zeroth moments (valid for q ≫ k_F, where the static
structure factor → 1), not a fixed-(q,ω) ratio; mark it [E]. Numerically ⟨p²⟩/m_e² = (3/5)(k_F/m_e)² = 2.9×10⁻⁵ (Si valence HEG,
k_F = 3.57 keV), so 3×10⁻⁵ is ⟨p²⟩; ⟨p_T²⟩ = (2/3)⟨p²⟩ = 2.0×10⁻⁵, giving ≈ 20–30 for |v_T|² = (0.7–1.0)×10⁻⁶. Write "O(20–30)".
*Conservative is robust:* S PSD gives |v_T·S_{nj_T}| ≤ |v_T|(S_nn tr S_{jj})^{1/2}, so the true rate ≥ ¼(|v_T|√S_nn − √tr S_jj)²,
which exceeds their ¼|v_T|²S_nn whenever the ratio r ≥ 4; with r ≈ 20–30 the true rate is ≥ (√r − 1)² ≈ 12–20 times theirs.
*Overstatement:* "determined entirely by the dielectric function holds only at |v_T| ≫ |p_T|/m_e". S_nn, S_{nj_T}, S_{j_Tj_T} are all
charge–current correlations, i.e. components of the finite-q dielectric tensor ε_ij(q,ω) (longitudinal, L–T mixed, transverse; [E5]
itself says S_{j_Tj_T} ∝ Im ε_T). At SOC = 0 the O₈ rate *is* determined by the dielectric tensor; what fails is "by Im(−1/ε_L) alone".

**A8. Selection rules, including Umklapp (umk.py).** For g = {R|t} with Rq = q and RG = G, P_g e^{i(q+G)·r}P_g^{-1} = e^{i(q+G)·r}e^{−i(q+G)·t}.
Against the Δ₁ Bloch factor e^{−iq·t}, the effective operator carries e^{−iG·t}, which is origin-independent because G·(1 − R)s = 0 for
RG = G. G = 0: Γ₂₅′ = T_2g ↓ C₄ᵥ[100] = B₂ ⊕ E (yz → B₂), no A₁: forbidden. Confirmed (C10a). **G = (2̄00)·2π/a_lat:** the τ-carrying
cogroup elements fixing [100] are C₄±, σ_y, σ_z (not in T_d), and G·τ = π, so the operator acquires the B₂ character; B₂ ⊗ (B₂ ⊕ E) =
A₁ ⊕ E ⇒ **allowed on the axis** (multiplicity 1, umk.py). This is the familiar statement that (200) is the diamond glide-forbidden
reflection: e^{iG·r} with G = (200) is odd under the τ operations. q = k_c + G = (−1.15, 0, 0)·2π/a_lat, |q| = 1.15 × 2.283 = 2.63 keV,
the smallest Umklapp of the Si valley (the (1̄11) choice gives 3.25 keV). Amplitude unknown, and possibly small since the (200)
crystal-potential component vanishes **[E]**, but it is not symmetry-suppressed. Ge G = 0 allowed (C10b): confirmed.

**A9. Thresholds (thr.py).** For a zero-phonon final state of momentum Q and energy E(Q), the condition is
m_χ ≥ min_Q g(Q), g = Q²/[2(Qv_max − E(Q))]. At the extremum dE/dQ = 0 and dg/dQ = Q(Qv_max − 2E_x)/[2(Qv_max − E_x)²] > 0 whenever
Qv_max > 2E_x (Si: 5.14 > 2.31 eV; Ge: 5.03 > 1.48 eV). The extremum value is therefore **not** the threshold; the minimum lies at |Q| < |k_c|.
Parabolic estimate (E(Q) = E_x + (|k_c| − Q)²/2M, M = m_l + m_hh along the axis): Si G = 0 ≈ 0.42 MeV (Q ≈ 1.45 keV, +0.19 eV);
Ge G = 0 ≈ 0.32 MeV (offset 0.30 eV, outside parabolic validity); Si (1̄11) Umklapp ≈ 0.62 MeV **[E]**. For Si G = 0 the channel
stays second class along the axis (pairs with k off the Δ line, ρ ∝ k_⊥) and opens as (ω − E_min(q))^{3/2}. With A8, the allowed Si Umklapp
opens at q²/[2(qv_max − E_x)] = 0.594 MeV at the extremum, lower after the Q minimisation. **Consequence:** the "PAER-only window
0.34–0.47 MeV" and IF-6 (0.472 / 0.708 MeV) must be recomputed as min_q q²/[2(qv_max − E_min(q))] with ab initio E_min(q) (and the
exciton dispersion), class-resolved. 0.472/0.708/0.420 are correct only as "value at the band extremum".

**A10. [E8].** C8a (8.0 E_x^b) and the 𝒮_F values reproduce. Second class: for ρ ≈ b·δk with fixed b = ∇_kρ,
Σ_m|b·∇ψ_{n1m}(0)|² = |b|²|∂_zψ_{n10}(0)|² = |b|²(n_H² − 1)/(3πa_x⁵n_H⁵) (ell.py: ratio 1/3 to the printed form for n_H = 2, 3, 4). The
printed (n_H² − 1)/(πa_x⁵n_H⁵) is the m- and Cartesian-summed trace; divide by 3, or define |∇_kρ|² as that trace and give the
matching continuum replacement (|ρ|² → |b|²k²/3). "Si still +35% at 1.5 eV" applies the hydrogenic 𝒮_F at ≈ 100E_x^b, where
parabolic bands and static ε_∞ screening of the e–h attraction do not hold; keep the sign, downgrade the size to a model figure.

**A11. Symmetry and 2607.06005 [FT].** Antiunitary Θ: Θn(q)Θ^{-1} = n(−q); a TR-invariant ensemble gives S(q,ω) = S(−q,ω), so every
odd-ℓ multipole vanishes without inversion. Quotes verified verbatim: Migdal "the only anisotropic contribution to the event rate is from
the quadrupole term (ℓ = 2)" (their §II, after Eq. (41)); §III, Fig. 4: "… suggesting that it originates primarily from the dipole
component." Their Eq. (41) contains W_ℓm for ℓ = 0, 2 only; W_2m = A₂∫d³kY_2m(k̂)Z²(k)W(k,ω) = 0 for any O_h- or T_d-invariant W with
isotropic Z(|k|) (no ℓ = 2 invariant, C11). A sidereal-day fundamental from ℓ = 4 is allowed when the crystal axes are not aligned with
the Earth axis. Their ≈ 1% ER modulation is compatible. Stands.

**A12. [E12] independent check.** Angle average S̄ = (4πq²)^{-1}∫d³q′δ(|q′| − q)S(q′); with Σ_{k′}∫d³q′ → Σ_{G′}∫_BZd³k′ and
S = (4π/V)Σ|ρ|²δ (spin 2 inside), S̄ = q^{-2}Σ_{ii′}∫d³k/(2π)³∫d³k′Σ_{G′}δ(q − |k′ − k + G′|)|ρ|²δ(ω − ΔE). Inserting in 1509.01598
Eq. (21) as quoted gives |f_crys|² = Ωq³S̄/(4παm_e²). Matches [E12] and 2105.02233 Eq. (D2) (𝒲̄₁ = 8ΔEαm_e²|f_crys|²/q³).

**A13. Smaller items.** (a) [E5]: tr S_{j_Tj_T} = Σ_λ(2ω²/e²)Im ε_{T,λ}/(1 − e^{−βω}); the two transverse polarisations differ at generic q̂
in a cubic crystal. (b) §2.4: EXCEED-DM's axial operator is K_e·σ_e/2m_e (2210.14917 Eq. (B16)–(B17)), a spin-current trace (J row,
like the ALP vertex), not "electron-spin"; the URF conclusion (no Hartree screening; f_xc^T and SOC missing) is unchanged. (c) §4.2 q_c
uses ω_p = qv_F + q²/2m_e rather than ω_pl(q); the change is O(q²v_F²/ω_p²) and does not affect the no-plasmon conclusion. (d) L2:
"KKL Eq. (27)" → Eq. (24) (arXiv v1 has no Eq. (25)–(27) in the main text). (e) G5: 4 VB × 12 CB × 24³ = 6.6×10⁵ pairs; a dense kernel
is ≈ 4.4×10¹¹ complex entries ≈ 7 TB per q_r, so "node-hours per q_r" requires a matrix-free kernel, interpolation, or a narrower
energy window; state which. (f) WP1 cites EXCEED-DM axial equations as (68)–(71) / (70)–(71): these are HTML sequential numbers;
the PDF numbers are (B15)–(B18).

## Owed corrections (for state/CORRECTIONS.md)
1. **S** §3.2 (c), §3.6 [E10], IF-6: add the Si G = (2̄00) on-axis Umklapp (allowed, |q| = 2.63 keV); delete "allowed Umklapp only at ≥ 3.25 keV".
2. **S** §3.4, IF-6, and the PAER-only window used by WP3: threshold = min_q q²/[2(qv_max − E_min(q))] (class-resolved, with exciton
   dispersion); extremum values are upper bounds (Si G = 0 ≈ 0.42, Ge ≈ 0.32, Si Umklapp ≤ 0.59 MeV [E]).
3. **S** L3 (a), §2.6: TR + I ⇒ Im 𝒲̄₂ ≡ 𝒲̄₅ ≡ 0 for any H; withdraw "Im 𝒲̄₂ measures [V_NL, n_e]"; redo the function count.
4. **S** [E8] second class: factor 1/3 (or define the trace and give the continuum replacement).
5. **W** L3 (c): ratio ≈ 20–30 (⟨p_T²⟩), [E] as zeroth-moment ratio; "dielectric function" → "dielectric tensor ε_ij(q,ω)".
6. **W** §1.4: beyond-RPA condition (−R⁰)^{-1} + f_xc > 0 (proper kernel), not 1 − f_HxcR⁰ > 0.
7. **W** [E5] polarisation sum; L3 (b) 𝒲̄₃ wording; B₁/B₃ quote boldface; KKL Eq. (24); EXCEED-DM (B15)–(B18) and "spin-current".
8. **W** G5 spec: kernel storage/matrix-free statement.
