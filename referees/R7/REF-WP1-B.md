# R7 / REF-WP1-B: hostile referee report on returns/R6/WP1-v2.md

Referee B, isolated. I read only the brief's list: WP1-v2, code/WP1-v2/checks.py (re-run: 28/28 PASS, about 3 s), CONVENTIONS,
NOTATION, CONTROLS, DONE, LIMITS and WP0-v2. Full texts were fetched with lit.py into literature/papers-r7-WP1-B/ and deleted afterwards:
2510.25835, 2607.06005, 2105.02233, 2002.06937, 2101.08275, 2210.14917, 2507.14345, 1509.01598. My own checks are one closed-form scan
(thresholds, below) and hand derivations; I ran no simulations.

## Verdict table
| # | Claim (location) | Verdict | Reason (one line) |
|---|---|---|---|
| 1 | [E1], ladder 𝒳 (§1.1–1.2) | STANDS | Exact at n_B = 0 from WP0-v2 (5.3)–(5.5)(i); the rung definitions agree with 2507.14345 |
| 2 | [E2] out-state weight (ε^{-1})_{G0}ρ(q+G); F1 accepted (§1.3, §12) | STANDS | Factorisation re-derived (§A); weight = (1+v_CR)_{G0}; the in-state form is its conjugate |
| 3 | [E3] 0 < (ε^{-1})_{00}(q,0) ≤ 1 at RPA+LFE (§1.4) | STANDS WITH CORRECTION | RPA proof correct; the beyond-RPA condition "1 − f_HxcR⁰ > 0" is the wrong operator (§B) |
| 4 | §1.5 increment sizes | STANDS WITH CORRECTION | Pointwise 1/\|ε\|² = 0.1–0.44 is not "the ×1.4–2.5" of a q-integrated rate (non sequitur; also L1 (a)) |
| 5 | [E4] on-shell longitudinal cancellation (§2.2) | STANDS WITH CORRECTION | Density/current rows: correct. Spin-current rows also need [H, s_e] = 0 (SOC = 0); Δ_χ ≠ 0 leaves Δ_χ·n |
| 6 | [E5] transverse response | STANDS | FDT algebra correct (C6b); a scalar ε_T assumes degenerate transverse polarisations (state it) |
| 7 | [E6] spin channel: ¼S^{IP}, unscreened, f_xc^T (§2.4) | STANDS WITH CORRECTION | ¼ and no Coulomb screening are correct; R̃_s normalisation unstated; the leading beyond-IP term is the triplet W-ladder, not ALDA f_xc^T (§D) |
| 8 | §2.5 ALP vertex at SOC = 0, triplet refinement | STANDS | tr σ^ασ^β = 2δ_{αβ}; σ·p is a spin-1 (triplet) operator, so it carries no Hartree LFE or exchange |
| 9 | §2.6 / G10 "seven real functions" | STANDS WITH CORRECTION | 7 screened singlet functions + 7 IP (triplet) functions = 14; 𝒲̄₅ ≡ 0 in PT targets (§E) |
| 10 | [E7] exciton term with A^{λ*} | STANDS | √2 from the singlet pair state is correct; the conjugate is correct (C5a) |
| 11 | §3.2 selection rules (Si Γ₂₅′→Δ₁ forbidden at G = 0; Ge allowed) | STANDS | Agrees with the compatibility relations Γ₂₅′→Δ₂′⊕Δ₅ and Γ₂₅′→Λ₁⊕Λ₃; the nonsymmorphic phases cancel (§F) |
| 12 | [E8] Elliott/Wannier; 8.0 E_x^b; 𝒮_F values | STANDS | Algebra exact (C8a). "+35% at 1.5 eV" lies outside the validity of parabolic bands with constant ε∞, but it is tagged [E] |
| 13 | §3.4 thresholds 0.472 / 0.708 / 0.420 MeV as "the boundary WP3 must use" | **FALLS** (as thresholds) | Arithmetic correct, but q is pinned to Q_x+G. Minimising over q gives Si ≈ 0.40–0.43 MeV [E]; Ge zero-phonon opens at 0.256 MeV via Γ (§G) |
| 14 | [E10] onset exponents | STANDS | The exponents are right; but [E10] itself uses E_min,0(\|q\|) at any \|q\|, which contradicts §3.4 |
| 15 | [E9], §4.2 no bulk plasmon from halo DM | STANDS WITH CORRECTION | Conclusion stands; q_c = 1.88 keV is computed with ω_p, not ω_pl(q); with [E9]'s dispersion q_c ≈ 2.2 keV (§H) |
| 16 | §5.1–5.3, [E11] relativistic f-sum | STANDS WITH CORRECTION | [E11] re-derived. The FW spin-curl coefficient is (1/m_e) q×s_e, not 1/(2m_e); Ge 3d "~10⁻³" vs "≤ 2%" inconsistent (§I) |
| 17 | §6.1 symmetry theorems (odd ℓ ≡ 0 by TR; cubic first ℓ = 4) | STANDS | TR derivation re-done; O_h and T_d character counts correct (C11) |
| 18 | §6.2 / L19 against 2607.06005 | STANDS | Quote verified in FT (§III, Fig. 4 discussion); the ℓ = 1 attribution is symmetry-forbidden. CONFIRMED |
| 19 | L1, [E12], SOTA #7 | STANDS | [E12] = 2101.08275 Eq. (16) = 2105.02233 Eq. (81); the rate prefactors agree term by term |
| 20 | L2 | STANDS | 2101.08275 Eq. (6) verified; the LFE reading of KKL App. A is correct |
| 21 | L3 (a) "3 of 5 Catena responses independent" | STANDS WITH CORRECTION | Identity correct for local H. But Im 𝒲̄₂ and 𝒲̄₅ vanish identically in Si/Ge (PT), so Im 𝒲̄₂ does not measure V_NL (§E) |
| 22 | L3 (c) 2510.25835 𝒪₈ omits tr S_{jTjT}, ≈ 40× | STANDS WITH CORRECTION | Omission CONFIRMED; it also affects 𝒪₂ and 𝒪₅; 40 is an IP estimate, and in medium the ratio is larger (§C) |
| 23 | L10 | STANDS | KK breakage by the θ step and the A_i renormalisation verified in FT |
| 24 | L11 | STANDS WITH CORRECTION | The 5 keV ≠ 2π/a_lat point is CONFIRMED; "×(5/1.9)²" is REFUTED: Eq. (14) is ∫dq/q, so the factor is ≈ 1.4 (§H) |
| 25 | L14 | STANDS | 6³ grid, 10 CBs and TDA verified in 2507.14345 FT |
| 26 | L17 (c) ε ≥ 1 "DERIVED at RPA+LFE" | STANDS WITH CORRECTION | As item 3 (beyond-RPA hypothesis) |
| 27 | Gap specs G5, G7, G10, G11 | STANDS WITH CORRECTION | G5: a dense fine-grid kernel is about 7 TB per q_r, so interpolation or on-the-fly products are mandatory; G7: inconsistency in item 16; G10: count in item 9 |
| 28 | §12 "Contested corrections: none" (F1 accepted) | STANDS | The acceptance argument is correct (§A) |

---
## A. [E2] and F1 (focus: out-state)
With R = R⁰(1 − vR⁰)^{-1}: 1 + vR = (1 − vR⁰)^{-1} and 1 + R†v = (1 − R⁰†v)^{-1}. Then
(1+R†v)(R⁰−R⁰†)(1+vR) = (1+R†v)R − R†(1+vR) = R − R†. In the (3.2) order at T = 0, ω > 0,
(R⁰−R⁰†)_{GG′} = −2πiV^{-1}Σρ_G*ρ_{G′}δ, because (R⁰†)_{GG′} = (R⁰_{G′G})* puts the −i0 on the same ρ_G*ρ_{G′} product. Since
(R†v)_{0G} = [(vR)_{G0}]* (v real diagonal), the 00 element is a sum of |Σ_G(1+vR)_{G0}ρ_G|², which is [E2]. For adiabatic TDDFT the same
step needs f_Hxc Hermitian as a G-matrix, which holds for a real symmetric kernel; state it, since f_xc is not diagonal in G. The
"physical" reading (time-dependent Hartree particles moving in V_tot = ε^{-1}φ_ext) is the correct argument for choosing the out-state form.
Verdict: STANDS; F1 acceptance correct.

## B. [E3] static stability (focus)
RPA: X = v^{1/2}R⁰(q,0)v^{1/2} ≤ 0. The static Kubo response is Hermitian NSD for any stationary state: both the A_f and B_f pole terms
are rank-one PSD matrices divided by −Δ_f, so neither TR nor an insulator is needed. v^{1/2}Rv^{1/2} = X(1−X)^{-1} has spectrum in
(−1, 0]. Its 00 element is a convex combination of eigenvalues, so 1 + v(q)R_{00} ∈ (0, 1]. Correct.
**Correction (beyond RPA).** The text says the result needs 1 − f_HxcR⁰ > 0. That condition (stability of the full R) gives only the upper
bound (ε^{-1})_{00} ≤ 1, which is exact anyway from thermodynamic stability (Dolgov–Kirzhnits–Maksimov: either ε ≥ 1 or ε < 0). The lower
bound needs the Coulomb-proper response to be NSD: R̃ = R⁰(1 − f_xcR⁰)^{-1} ≤ 0, i.e. 1 − f_xc^{1/2}R⁰f_xc^{1/2} > 0 in the symmetrised
sense, **with f_xc, not f_Hxc**. The quoted HEG r_s = 5.25 is exactly the compressibility zero of 1 − f_xc(0)R⁰(0), which confirms that
f_xc was meant. Replace "f_Hxc" by "f_xc" in §1.4 and L17 (c), and add: "ε(q,0) < 0 (allowed by DKM) is excluded only under this condition."

## C. 2510.25835 and 𝒪₈ (focus; rubric (c))
FT: Eq. (1) is H_int = V(q, v⊥)[F·S_e + F₀n_e]. "v⊥ is the component of v that is perpendicular to q" is a c-number, and no current
operator exists in their framework. Eq. (6): dΓ₈/d³q = (v⊥²/4)dΓ₁/d³q. Text: the rate from "O1, O2, O5, O8 and O11 — is completely
determined by the dielectric response Im(−χ00)"; abstract: "contrary to common lore — are determined entirely by the dielectric
function". Their 𝒪₈ thus drops the target part v_s of v^⊥. **CONFIRMED** that Eq. (6) is the v_s → 0 truncation of [E4].
**Extension the package missed.** 𝒪₅ = iS_χ·(q/m_χ × v^⊥) contains q × j_T, and 𝒪₂ = (v^⊥)² contains v_χ·j and a v_s² (kinetic-type)
operator. Their dielectric-only claim fails for 𝒪₂, 𝒪₅ and 𝒪₈; it holds only for 𝒪₁ and 𝒪₁₁. L3 (c) and G10 should say so.
**Magnitude [E].** "≈ 40" uses ⟨p_T²⟩/m_e²|v_T|², which is an IP quantity. For a HEG slice at p_∥ ≈ 0, ⟨p_T²⟩ = k_F²/2 gives
2.4×10⁻⁵/1×10⁻⁶ ≈ 25. In medium, [E5] together with S_nn = (2q²/e²)Im(−1/ε_L) gives the exact ratio
tr S_{jTjT}/(|v_T|²S_nn) = 2(ω/q)²|ε_L|²(Im ε_T/Im ε_L)/|v_T|². So the density channel is suppressed by 1/|ε_L|² (0.1–0.44 in Si, §1.5)
while j_T is only LFE-screened. For the WSi (QROCODILE, Lindhard metal, ω ~ 0.1 eV) target the suppression of S_nn is far larger.
"Conservative by O(10)" is therefore a lower estimate; the number itself is UNRESOLVED. The cross term −2Re v_T·S_{nj_T} vanishes for
isotropic responses and survives only through cubic anisotropy, so "conservative" holds.

## D. Spin channel (focus)
SOC = 0, unpolarised, IP: S_{s^zs^z} = ¼(S_↑↑ + S_↓↓) = ¼S^{IP}_nn, and off-diagonal terms vanish by spin-rotation invariance. Coulomb
lines couple only n_↑ + n_↓. **Correct.**
- Normalisation: from δn_σ = (R⁰/2)(δv_σ + Σf_{σσ′}δn_{σ′}) one gets R_mm = R⁰ + R⁰f^TR_mm for m = n_↑ − n_↓, with f^T = (f_↑↑ − f_↑↓)/2,
  and R_{s^zs^z} = R_mm/4. Hence "R̃_s = R⁰ + R⁰f_xc^TR̃_s" holds only if R̃_s ≡ R_{σ^zσ^z} = 4R_{s^zs^z}. State it, or write the kernel as
  4f^T for R_{ss}.
- The beyond-IP size is understated. §1.5 says correctly that ALDA has no e–h binding. The triplet channel keeps the direct (−W^{scr})
  ladder: §3.1 says the BSE "removes the exchange term" and keeps W. So the Sommerfeld ×1.3–2 within ~1 eV of E_min and the triplet bound
  lines of [E8] apply to s_e as well, with E_x^b(triplet) ≥ E_x^b(singlet). The "+10–20% Stoner" figure is the static adiabatic kernel
  only. The same correction applies to the L3/EXCEED-DM sentence, where the missing piece is the triplet ladder plus f_xc^T, not f_xc^T
  alone. EXCEED-DM's "there is no screening" for the VA model is **CONFIRMED** in FT; the URF agrees at Hartree level.

## E. 2105.02233: 3-of-5, Im 𝒲̄₂, 𝒲̄₅ (focus; rubric (c))
FT Eq. (11): f′ = ∫ψ′*e^{iq·x}(i∇/m_e)ψ, so f′ = −⟨e^{iq·x}p⟩/m_e = −[j − (q/2m_e)n]. For local H, q·f′ = −(ΔE − q²/2m_e)f. This gives
𝒲̄₂ and 𝒲̄₄ in terms of 𝒲̄₁, and leaves 𝒲̄₁, the transverse part 𝒲̄₃ − (m_e²/q²)𝒲̄₄, and 𝒲̄₅. **The identity stands.**
**New: PT symmetry.** Si and Ge are centrosymmetric and TR-invariant, and the spinless PT operation squares to +1, so a real gauge
ψ_k(r) = ψ_k(−r)* exists. Substituting r → −r gives f = f* and f′ = f′*, per transition and gauge-invariantly after summing over
degenerate bands. Therefore B₂ = (q/m)·f′f* is real and B₅ = i(q/m)·(f′×f′*) = 0. **Im 𝒲̄₂ ≡ 0 and 𝒲̄₅ ≡ 0 in Si and Ge**, for local or
nonlocal (PT-invariant) pseudopotentials alike. Consequences:
- (i) The package's "their small Im 𝒲̄₂ measures the nonlocal-PP violation [V_NL, n_e]" is wrong. The violation sits in
  Re 𝒲̄₂ + (ΔE − q²/2m_e)𝒲̄₁/m_e.
- (ii) 2105.02233 §III.B attributes their nonzero Im W̄₂ and W̄₅ in Si/Ge to approximate axial symmetry of crystals: **REFUTED**. These
  values are numerical (gauge or k-sampling) noise.
- (iii) For TR alone (GaAs), S^{anti}_{jj}(q) = −S^{anti}_{jj}(−q), so the angle-averaged 𝒲̄₅ ≡ 0. In §2.6 the "antisymmetric part = 𝒲̄₅"
  is needed only unaveraged in non-centrosymmetric targets, or in P,T-broken ones.
- Eq. (80) sign: δ(ΔE − E_ik + E_i′k′) with ΔE ≡ E_i′k′ − E_ik (their Eq. (18) text), against 1509.01598 Eq. (21) δ(E_e − E_i′k′ + E_ik).
  **CONFIRMED** (typographic; also Eqs. (37), (47)).
- Eq. (81) |f_crys|² = q³W̄₁/(8ΔEαm_e²). With σ̄_e = μ²c₁²/(16πm_χ²m_e²), their Eq. (45) reproduces 1509.01598 Eq. (17) exactly, so the
  "consistent" verdict is **CONFIRMED**.
- Numbering: these are arXiv-HTML numbers; the PDF has (D1)/(D2) for (80)/(81), and 1509.01598's PDF has (3.13)/(3.17) for (17)/(21).
  Say "HTML numbering" in L1 and L3.

## F. Selection rules (focus)
In diamond (origin at an atom) the little group of Δ contains {E, C₂ₓ, σ_{y↔z}, σ_{y↔−z}} pure, and {C₄ₓ^{±}, σ_y, σ_z} with
τ = (¼,¼,¼)a. The function e^{iq·r}u_Γ and a Δ Bloch state both pick up the same e^{iq·τ} under {R|τ}, so the selection rule reduces to the
subduction Γ₂₅′(T₂g)↓C₄ᵥ = Δ₂′⊕Δ₅. That contains no Δ₁, which is C10a. Off-axis, δq_⊥ transforms as Δ₅ and Δ₅⊗Δ₅ ∋ A₁, so the s-exciton
weight is ∝ |δq_⊥|². δq_∥ is A₁, so the vertex stays zero along the axis. This supports [E10]'s p_on = 1 for the Si 1s line. For Ge,
Γ₂₅′↓C₃ᵥ ∋ Λ₁ = L₁↓C₃ᵥ, so the transition is allowed. Umklapp G = (1̄11): only σ_{y↔z} fixes G, and that symmetry does not forbid it.
**Stands.**

## G. Thresholds (focus): §3.4 FALLS as stated
The 0.472/0.708/0.420 MeV values are m_χ at which q = Q_x + G exactly becomes reachable; they are not onsets. On shell,
m_χ ≥ q²/[2(qv_max − E(q))] with E(q) = E_min(q) − E_x^b, minimised over q. At q = Q_x, ∂E_min/∂q = 0 (minimum), while
∂_q[q²/2(qv−E)] = q(qv − 2E)/[2(qv−E)²] > 0 because Q_xv_max = 5.14 eV > 2E_x = 2.31 eV (Si) and 5.03 > 1.48 eV (Ge).
- **Hence a strictly smaller m_χ always exists at |q| < |Q_x+G| [D].** The absolute floor is 2E_x/v_max² (NOTATION m_min): Si 0.329, Ge
  0.211 MeV.
- With a parabolic exciton dispersion E_x + (q−Q_x)²/2M_x (M_x = m_c + m_v ≈ 0.8–2 m_e) the optimum is:
  - Si G = 0: **0.40–0.43 MeV** (Δq ≈ 0.4–0.6 keV, E_kin ≈ 0.19 eV);
  - Si Umklapp: 0.59–0.65 MeV;
  - Ge L: 0.33–0.37 MeV.
  This is [E] (Δq ≈ 20–30% of 2π/a_lat, beyond strict parabolicity; real E_min(q) is needed).
- **Ge:** the direct Γ valley (E_dir(0) ≈ 0.90 eV, dipole-allowed) opens zero-phonon e–h creation at 2E_dir/v_max² ≈ **0.256 MeV**
  (q ≈ 0.68 keV), far below 0.420.
- Si direct (3.4 eV): 0.968 MeV, irrelevant.
- **Consequence:** the Si zero-phonon line (second class, suppressed) opens inside the "PAER-only window 0.34–0.47 MeV", near 0.42 MeV,
  not at its top. IF-6 and the "boundary WP3 must use" must be replaced by min_q of the above with ab initio E_min(q) along Γ–X (Si) and
  Γ–L plus Γ (Ge). [E10] already contains the right object, E_min,0(|q|) for all |q|.

## H. Plasmon and L11
- With [E9]'s ω_pl(q)² = ω_p² + (3/5)q²v_F², the crossing with qv_F + q²/2m_e is at q ≈ 2.2–2.3 keV:
  - at 2.1 keV: 18.98 vs 20.11 eV;
  - at 2.3 keV: 21.23 vs 20.74 eV.
  It is not at 1.88 keV, which is the crossing with the constant ω_p (C7 code). The conclusion holds, since q ≥ 6.3 keV is needed.
- 2002.06937 FT Eq. (4): "q_c ∼ 2π/a ∼ 5 keV, where a is the lattice spacing". 2π/a_lat(Si) = 2.28 keV; 5 keV corresponds to the bond
  length. **CONFIRMED** as inconsistent.
- But Eq. (14) is ∝ ∫₀^{q_c}dq η/q (logarithmic). For the fast component they need (v ~ 0.1, q_min = E/v ≈ 0.17 keV),
  ln(5/0.17)/ln(1.9/0.17) ≈ 1.4, not (5/1.9)² ≈ 6.9. The package's "×(5/1.9)²" is **REFUTED**.
- ε(E,q) ≈ ε(E,0) up to q_c is **CONFIRMED** in their text.

## I. Relativistic section
- [E11] re-derived: the angle average of (p+q)⁴ + (p−q)⁴ − 2p⁴ is 2[(10/3)p²q² + q⁴], times −1/8m³, relative to q²/m gives
  −(5/3)⟨T⟩/m − q²/4m². Correct. Darwin and SOC give zero double commutators, and the Dirac α·p gives zero. Correct.
- §5.2 third bullet: Gordon gives ū′γu → (p+p′)/2m ∓ i(q×σ)/2m = ∓ i(q×s)/m with s = σ/2. Equivalently, the g = 2 magnetisation current is
  (1/m_e)∇×s. **The coefficient is (i/m_e)q×s_e** (sign by convention), not (i/2m_e)q×s_e, given the package's own s = σ/2 (§2.4, C5b).
- Ge 3d: the table gives ~10⁻³ (with SO/binding = 0.02 as a bound), while G7 "Remaining gap" and §10 item 2 give "≤ 2%". Pick one;
  ~10⁻³ with a ≤ 2% bound is acceptable if worded so.

## J. 2607.06005 (focus; rubric (c))
FT verified:
- abstract: "daily modulation of the Migdal rate arises solely due to the quadrupole component";
- §II after Eq. (41): "the only anisotropic contribution to the event rate is from the quadrupole term (ℓ = 2)";
- §III (Si/GaAs results): "The modulation of the electron rate at 5 eV appears roughly like a clean sine wave with a period of one
  sidereal day, suggesting that it originates primarily from the dipole component."

TR: Θn(q)Θ^{-1} = n(−q) with a stationary TR-invariant state gives S(q,ω) = S(−q,ω) at any T, with or without SOC and without inversion,
and with unreduced q (LFE). Their Eqs. (10)/(25) pair T_ℓm with f̂_ℓm of the same ℓ, so ℓ = 1 cannot contribute.
- **Dipole attribution: CONFIRMED wrong.** A one-sidereal-day fundamental is still possible from the m = ±1 entries of D^{(4)}(t).
- Migdal: their W_ℓm(ω) (Eq. (39)) is the Y_ℓm moment of the finite-k ELF. The projection of an O_h- (T_d-)invariant function onto ℓ = 2 is
  invariant, and no ℓ = 2 invariant exists, so W_2m ≡ 0 for Si and GaAs. Any Migdal modulation in their Fig. 4 is numerical.
  **CONFIRMED.**
- Note: their Migdal ELF is the finite-k ELF, not the q→0 tensor; the argument holds for all k, so the package's "dipole-vertex" framing
  is sufficient but narrower than needed.

## K. Rubric (b), (d), (e) remarks
- L1 validity (a): "1/|ε|² ≈ 0.1 at 2 keV, 0.44 at αm_e, so L1 overestimates by ×1.4–2.5" mixes pointwise and rate-integrated factors.
  I checked: Cappellini static gives 1/ε² = 0.117 and 0.451. The ×1.4–2.5 is 2101.08275's rate ratio. Write the two separately.
- L2, L10, L14, L17 (a,b,d,e): chains valid. KKL FT checks:
  - footnote "approximation that the dielectric function is a diagonal matrix in reciprocal lattice space": CONFIRMED;
  - HTML Eq. (15) ⟨p,ℓ′|e^{ik·r}|p,ℓ⟩ (typo for p′): CONFIRMED;
  - ε averaged over directions before inversion: CONFIRMED (PDF Eq. (24) = HTML (27));
  - θ(ω−ω_edge) times Mermin with f-sum renormalisation of A_i breaks KK: CONFIRMED.
- 2507.14345: 6×6×6 grid, 10 CBs (Fig. S2 against 80), TDA: CONFIRMED.
- 2210.14917 Eq. (23) f_scr = 1/(q̂·ε·q̂) and "f_scr = 1" for non-mixing models. The URF statement that density coupling is screened for
  any mediator is correct; KKL say the same ("apply for both vector and scalar mediators"). CONFIRMED.
- (d) Conventions: η/2q, v_max = 794.5, the S↔L map, the spin factors, (ε^{-1})_{00} indexing, M/A nuisance types and the π f-sum all agree
  with CONVENTIONS and WP0-v2. CONVENTIONS §13 item 16 is now reconciled: [E2] ≡ WP0-v2 (7.2) ≡ X2 (2.2).
- (e) G5: 24³·48 = 6.6×10⁵ pairs; a dense kernel holds 4.4×10¹¹ complex entries ≈ 7 TB per q_r. The spec must require
  coarse-to-fine interpolation with on-the-fly products. The flop count (≈ 10¹⁴) is right but is not the bottleneck.
- (e) G10: the f_xc^T dressing needs the full IP G-matrix R⁰_{GG′}, not only the seven heads, and the output list should say so. G11:
  sufficient. Exciton-gap spec: add min_q of the zero-phonon onset (§G).

## Literature-claim ratings (rubric (c))
| Claim | Rating |
|---|---|
| 2510.25835 Eq. (6) omits the current term of 𝒪₈ | CONFIRMED (also 𝒪₂, 𝒪₅) |
| 2510.25835 "conservative by O(10)", ratio ≈ 40 | UNRESOLVED (IP estimate; in-medium larger) |
| 2607.06005 "dipole component" attribution | CONFIRMED wrong |
| 2607.06005 Migdal modulation in Si/GaAs is nonzero | CONFIRMED that it must vanish (ℓ = 2 absent) |
| 2105.02233 Eq. (80) energy-δ sign | CONFIRMED (typo) |
| 2105.02233 Im W̄₂ and W̄₅ nonzero in Si/Ge "from approximate axial symmetry" (referee's addition) | REFUTED (PT ⇒ ≡ 0) |
| Package: Im 𝒲̄₂ measures [V_NL, n] | REFUTED |
| 2210.14917 "no screening" (axial): misses triplet effects | CONFIRMED (missing piece = triplet ladder + f_xc^T) |
| 2101.08275 Eq. (15) typo; diagonal-ε approximation; average before inversion | CONFIRMED |
| 2002.06937 q_c ≈ 5 keV ≠ 2π/a_lat | CONFIRMED |
| 2002.06937 phase space overstated ×(5/1.9)² | REFUTED (log measure, ≈ 1.4) |
| 2507.14345 k-grid/CB/TDA limitations | CONFIRMED |

## Required corrections (summary)
1. §3.4, IF-6, §8 exciton gaps: thresholds must be min over q (Si ≈ 0.40–0.43 MeV [E]; Ge 0.256 MeV via Γ); the WP3 boundary moves.
2. §1.4 and L17 (c): f_Hxc → f_xc; the beyond-RPA condition is R̃ ≤ 0.
3. L3 (a): Im 𝒲̄₂ ≡ 𝒲̄₅ ≡ 0 in PT targets, and their nonzero values in 2105.02233 are noise; L3 (c): add 𝒪₂ and 𝒪₅; magnitude in medium.
4. §2.4: normalisation of R̃_s; the leading beyond-IP spin correction is the triplet W-ladder (×1.3–2 near the edge, bound lines).
5. §5.2: spin-curl coefficient 1/m_e; Ge 3d size made consistent.
6. §4.2 / L11: q_c ≈ 2.2 keV with dispersion; the 2002.06937 overstatement is logarithmic (≈ 1.4), not ×6.9.
7. §2.6 / G10: 14 real functions (7 screened singlet + 7 IP), plus the full R⁰_{GG′} for the f_xc^T dressing.
8. L1 (a), §1.5: separate pointwise 1/|ε|² from the rate ratio. Cite equation numbers as arXiv-HTML numbering.
