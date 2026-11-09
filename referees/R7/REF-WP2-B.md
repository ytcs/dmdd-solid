# R7 / REF-WP2-B: hostile referee of returns/R6/WP2-v2.md (isolated)

Read: WP2-v2.md, code/WP2-v2/checks.py (re-run: 21/21 PASS, numbers reproduced), CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS, WP0-v2.
Not read (per brief): referees/, state/, AUDIT, other returns (WP3 J8 is judged only through WP0-v2's record of it).
Full texts fetched with lit.py into literature/papers-r7-WP2-B/ (2607.24933, 1712.06598, 2309.10839, 2205.02250, 2009.13534,
2411.03433, 1910.08092, 1807.10291; arXiv HTML + PDF), read, then deleted. HTML equation numbers are sequential and match the package's.

## Verdict table

| # | Claim (WP2-v2 location) | Verdict | One-line reason |
|---|---|---|---|
| 1 | GS-sector reduction (1.1), charge vertex (1.2) | STANDS WITH CORRECTION | Sound; but putting e^{−W_κ} on the δρ_κ part of the vertex in (2.2) does not follow from the additive vertex (1.2) (differs at O(2W)); see §A |
| 2 | Exact coherent harmonic S, all n_ph, finite T (2.1)–(2.2) | STANDS | Re-derived: prefactor 2π/(2Ω ω), e* with n+1 on emission, e^{iq·r_κ} phase, consistent with CONVENTIONS §2, §5 |
| 3 | Shell expansion (2.3) and the "≈2%" shell size (§3.3) | STANDS WITH CORRECTION | In diamond the nearest shell (2.35 Å) is κ ≠ κ′, not a lattice ΔR; the 2% is a node of j₀ at q = 10 keV; ≈10% at q = 2 keV |
| 4 | BZ-average theorem (2.4) | STANDS WITH CORRECTION | Polyatomic cross terms come from **every** ΔR, weight j_BZ(ΔR + r_κ − r_κ′), not only ΔR = 0; gradient term is O(q_BZ/q), so the result is asymptotic in q ≫ q_BZ only; C9 tests neither |
| 5 | 2607.24933 Eq. (47) incomplete (§3.3) | STANDS WITH CORRECTION | CONFIRMED for the polarisation weights (n = 1: 1/3 on each of LA, TA, TA instead of 1 on LA). The intra-cell-phase charge falls outside the paper's stated "monoatomic, isotropic" assumption; Eq. (47) is not used in their numerics |
| 6 | Incoherent finite-T S (3.1)–(3.2) and Einstein/Poisson limit | STANDS | Re-derived from (2.3) |
| 7 | Truncation loss P[Pois(2W_κ) ≥ N] at any T, coherent S included (3.4′) | STANDS | Re-derived (§C); caveat: at T > 0 it is a fraction of the *signed* first moment, per species κ |
| 8 | Panjer equation (3.5), ρ^ph (3.6), cost claims | STANDS WITH CORRECTION | Identity correct. At T > 0, w_κ has ω′ < 0 support, so (3.5) is not a forward recursion: the O(N_ω²) march is T = 0 only; use the FFT of e^{Φ(t)}. ⟨n_ph⟩ counts absorptions too |
| 9 | L4: total-ε ELF ≡ Born-charge formula (Sherman–Morrison, (4.2)), one branch (4.3) | STANDS | Re-derived exactly (§D); matches 1910.08092 Eq. (106) and 1807.10291 Eqs. (29), (32) (quotes verified) |
| 10 | 1712.06598 Eq. (5) has a spurious 1/V_cell; Eq. (12) has a spurious LO term | STANDS | Both CONFIRMED from the full text (§D) |
| 11 | Exact cumulants (5.1); 𝔨₁ exact | STANDS | Agrees with the Placzek/Sears moments; C5 certifies them |
| 12 | GS/X split of 𝔨₃ (5.2) | STANDS (as [D] at leading BO order, still OPEN on WP3's side) | Second-derivative (Hellmann–Feynman) identity and drag-mass first moment re-derived |
| 13 | 𝔨₃ contact formula (5.2′) | STANDS | Exact at all q for point nuclei and cubic sites (the self phase cancels) |
| 14 | 𝓜³_κκ\|_{V_eN} = −(m_e/M_κ)𝓜³_eκ "exactly" (§0 item 6, (5.2′c), IF-1) | STANDS WITH CORRECTION | True only for q·a_core ≪ 1, as WP0-v2 (4.7) is qualified. Hydrogenic Si 1s: off by 9% at 51 keV and 29% at 102 keV, which is the impulse regime |
| 15 | Anharmonic constraints (6.1); M-type incompatibility (6.1′) | STANDS | Linear in Δ; concavity of (1 ± a)^θ |
| 16 | 2309.10839 Eq. (9): e^{−W_d} should be e^{−2W_d} (§6.3) | STANDS | CONFIRMED (v1 HTML): Eq. (10) W_d = (q²/4m_d)∫D/ω, Eq. (13) e^{−2W^toy}, W^toy = q²/4m_dω₀ |
| 17 | Toy-model 𝔨₃ 7% low (§6.3) | STANDS [E] | (q²/2M)(ω₀² + 3σ²) with their Eq. (17) σ² = ω₀ω̄ − ω₀²; ignores their Θ(ω_max) cutoff |
| 18 | Spin channel "exactly" incoherent (7.1); 2009.13534 omits it | STANDS WITH CORRECTION | 2009.13534 claim CONFIRMED. "Exact" also needs the isotope mass disorder dropped (²⁹Si vs ²⁸Si local DOS, O(ΔM/M) ≈ 3.5%) |
| 19 | Cubic isotropy theorem (8.2) | STANDS | Φ_κκ(0,t) is bilinear in q, so only rank-2 site tensors enter; T_d sites make them ∝ 𝟙 |
| 20 | 2205.02250's "true peak shifted" is a discrepancy (L6) | FALLS (as a discrepancy) | The source says "peak", meaning the mode, which is shifted by 𝔨₃. The source is correct; the package's physics (mean exact) stands |
| 21 | 2411.03433's isotropic IA width is an "omission" (§8.2 iv, L19) | STANDS WITH CORRECTION | It is a declared, quantified approximation (q̂ = ẑ; ω̄_d differs by 6–8% for Al₂O₃), not an omission |
| 22 | Si/Ge: Z* = 0, quadrupolar dark-photon vertex (4.5) | STANDS | Inversion relates the two sites, T_d makes Z* ∝ 𝟙, and the ASR forces it to 0 |
| 23 | Gap closures G3, G11, G13, L4 add-on (§10) | STANDS WITH CORRECTION | A real specification, not a restatement; but the G3 tables at q < q_BZ, n_ph ≥ 2 rely on (2.4) outside its validity, and the Panjer route must be the FFT at T > 0 |
| 24 | Contested corrections (§14) | n/a | None contested; the "clarification" on WP0-v2 Table 6.1 is correct |

---
## A. Reduction and vertex (rubric a, d)
(1.2) writes ρ̄_e(q;R) = ρ̄_e(q;R⁰) + iΣ_I e^{iq·x⁰_I}δρ_κ·u_I + O(u²). This is **additive** and anchored at x⁰. The nuclear part
Z_κe^{iq·(x⁰+u)} then carries e^{−W_κ}, but the δρ_κ·u term does not: its one-phonon matrix element is ⟨Qν|u|0⟩ with no Debye–Waller
factor. (2.2) "absorbs (1.2) into c_κ" and multiplies the whole vertex by e^{−W_κ}. The two agree only at O(2W). 1910.08092 attaches Δ_j
to the moving ion (multiplicative form), which gives both the e^{−W_j} and the extra contraction term in its Y_j (Eq. (91), third term).
At q ≪ q_BZ these are O(2W) ≈ 6×10⁻⁴ and O(q³) respectively, so L4 is unaffected. Owed: state which bookkeeping (2.2) uses for the
non-rigid part, and that the claim "(1.2) reproduces 1910.08092 Eqs. (98)–(104)" holds at O(u) and q → 0 only.
Notation (d): NOTATION row 136 defines δρ_κ as the *valence* response, but (1.2) uses δρ_κ = q f^at_κ (core included) in the rigid-ion
limit, and §10 then introduces δρ^val_κ as "the valence part of δρ_κ" (NOTATION row 403). One of the two rows must change.

## B. BZ-average theorem (2.4): the polyatomic term is wrong as written
In (2.3) the only p-dependence under q → q + p, apart from the smooth factors, is the explicit phase e^{−i(q+p)·(ΔR + r_κ − r_κ′)}.
Hence

  (Ω/(2π)³)∫_BZ d³p e^{−ip·(ΔR + r_κ − r_κ′)} = j_BZ(ΔR + r_κ − r_κ′)*.

- κ = κ′: the argument is a lattice vector, so j_BZ(ΔR) = δ_{ΔR,0}. This is the package's step.
- κ ≠ κ′: ΔR + r_κ − r_κ′ is **never** a lattice vector, so the weight is nonzero for **every** ΔR. Moreover Σ_ΔR j_BZ(ΔR + r) = 1
  (Poisson summation; only G = 0 lies inside the BZ).

1D check, BZ = [−π/a, π/a], r = a/2: (a/2π)∫e^{−ip(na + a/2)}dp = (−1)ⁿ/(π(n + ½)), which is nonzero for every n.

**Correct statement:**

  ⟨S^{(n_ph)}⟩_BZ = S^{(n_ph)}_inc + Σ_{ΔR} Σ_{κ≠κ′} j_BZ(ΔR + r_κ − r_κ′)* S^{(n_ph)}_{κκ′,ΔR} + gradient terms.

In Si every nearest-neighbour pair is κ ≠ κ′, so the dropped terms are the leading ones. C9 is a monatomic chain with q-independent
weights, so it tests only j_BZ(ΔR) = δ_{ΔR,0}; "verifies the identity exactly" overstates what it checks.

**Gradient term.** The held-fixed factors are (q·e)^{n_ph} and e^{−2W(q)}. Across the BZ their relative variation is
n_ph·q_BZ/q + 4W·q_BZ/q, which is O(1) for q ≲ q_BZ. (2.4) is therefore an asymptotic statement for q ≫ n_ph q_BZ, and that hypothesis is
missing. It cannot support "incoherent is accurate in ω-integrated rates **below q_BZ**" (WP2-D1, as quoted in WP0-v2 Table 6.1); that
statement remains [E]. Headline §0 item 2 ("incoherent = BZ-averaged coherent S") must carry both qualifiers.

**Shell size (§3.3).** The quoted |ΔR| = 2.35 Å, z = 4 is the κ ≠ κ′ neighbour shell, which the lattice label ΔR does not index; relabel it
by the pair (ΔR, κ, κ′). The estimate 4|j₀(qd)|c̄² is 1.8% at q = 10 keV, but 10 keV is near a zero of j₀ (qd = 11.9). At q = 2 keV
(qd = 2.38, j₀ = 0.29) the same formula gives ≈ 10%. Quote the envelope 4c̄²/(qd), or a range, rather than a single "≈ 2%".

## C. Truncation loss (3.4′) at any T: verified
From (3.1), ∫w_κ = Φ_κκ(0,0) = q·B_κ·q = 2W_κ (coth included) and ∫ω′w_κ = q²/2M_κ, using n_B(−x) + 1 = −n_B(x). Then
∫ω w^{*n}/n! = n(∫ωw)(∫w)^{n−1}/n!, so the order-n share of the f-sum is e^{−2W}(2W)^{n−1}/(n−1)! = P[Pois(2W) = n − 1]. Keeping
n ≤ N loses P[Pois(2W) ≥ N]. ✔

Coherent terms: ∂_tΦ_κκ′(ΔR,0) = −i(2N√(M_κM_κ′))^{-1}Σ_Q e^{iQ·ΔR}q·(Σ_ν e_κν e†_κ′ν)·q, after using e(−Q) = e(Q)*, n_{−Q} = n_Q.
Completeness turns this into −i(q²/2M_κ)δ_κκ′δ_{ΔR,0}. Every shell term at order n has first moment ∝ nΦ^{n−1}(0)Φ̇(0) = 0. ✔

Qualifiers owed:
- At T > 0 the fractions refer to the signed first moment over ℝ.
- With several species the lost fraction is the |c_κ|²/M_κ-weighted mean of P[Pois(2W_κ) ≥ N].
- The coherent statement holds for vertices that are exactly multiplicative (rigid ion, nucleon); for the full 𝒵_κ only at n_ph = 1 (§A).

## D. L4 and the claims against 1712.06598
**Sherman–Morrison.** Write G = (D_A − z)^{-1}, s = pᵀGp, c = e²/Ω. Then ε = ε_∞ + cs, and SM gives pᵀ(D_A + (c/ε_∞)ppᵀ − z)^{-1}p =
s/(1 + cs/ε_∞). Hence

  −1/ε = −1/ε_∞ + cs/(ε_∞(ε_∞ + cs)) = −1/ε_∞ + (c/ε_∞²)pᵀ(D_NA − z)^{-1}p.

Taking Im at z = ω² + i0: (c/ε_∞²)Σ_ν(p·e_ν)²(π/2ω_ν)δ(ω − ω_ν). Times 2q²/e², this is exactly (4.2). ✔ It needs real Γ-point eigenvectors
and q ≪ q_BZ, both stated. The LO–TO residue (4.3) follows with LST. ✔

**1712.06598 Eq. (5) [FT]: CONFIRMED.** The text gives C_F = e[(ω_LO/2V_cell)(1/ε_∞ − 1/ε₀)]^{1/2} ("V_cell is the primitive cell volume"),
Eq. (6) Γ(p_i) = 2π∫d³p_f/(2π)³ δ(…)|ℳ_q|², and Eq. (7) |ℳ_q|² = κ²g_X²C_F²/(e²q²). Then [|ℳ|²] = [C_F²/q²] = E·E³/E² = E²
(1/V_cell ~ E³), so [Γ] = E³·E²·E^{-1} = E⁴ instead of E. The Fröhlich coupling carries the normalisation volume V, which
cancels against Σ_q = V∫d³q/(2π)³. The final rate "per unit time and target mass" leaves no V_cell to absorb the error. This is a
formula-level error; whether it reached their numbers was not checked, and the package does not claim so.

**1712.06598 Eq. (12): CONFIRMED.** Exact long-wavelength eigenvectors are e^{LA}_d = √(A_d/A_tot)q̂ and e^{LO} ∝ (√A₂, −√A₁)/√A_tot. With
b̄_d = b̄_nA_d and m_d = A_dm_n, F_LO ∝ √A₁√A₂ − √A₂√A₁ = 0 at O(q). Their equal-mass form leaves (b̄_n²/2m_n)q²(√A_Ga − √A_As)².
The true leading term is ∝ q²A₁A₂(q·Δr)²/A_tot. For GaAs it exceeds the spurious term once q ≳ 0.05 keV (angle-averaged), consistent
with the package's "≳ 0.1 keV [E]".

## E. 2607.24933 Eq. (47) [FT]: CONFIRMED, with scope correction
Eq. (46) is 𝒟(ω,k) = Ω_c/(3(2π)³)Σ_α δ(ω − ω_{α,k}). Eq. (47) (PDF 4.23) inserts it, with momentum conservation, into the full
structure factor. At n = 1 this gives (2πf²/Ω_c)(q²/2m)(1/3)Σ_α δ(ω − ω_{α,q−G})/ω_{α,q−G}, i.e. weight 1/3 on each branch. Even in an
isotropic continuum a plane wave at fixed k is purely L or T, so the exact weight is |q̂·e_α(q − G)|²: 1 for LA, 0 for TA. The same paper's
Eq. (48) (1D, LA weight 1) is consistent with the package, not with (47). So the polarisation part of the claim is CONFIRMED.

However, the text immediately after (47) says "we have still assumed a monoatomic, isotropic lattice for simplicity". The intra-cell
phases are therefore outside the paper's stated scope and must not be listed as an error of Eq. (47). Section 5 uses only 1D results as
proxies, so (47) does not enter their rates. The wording "incomplete" should become "incorrect for the coherent term at fixed k
(polarisation weights), not used numerically".

## F. Moments: (5.1), (5.2), (5.2′) and agreement with WP0-v2 (4.7) / WP3 J8
**(5.2′) 𝔨₃ formula ✔.** For the self term the phases e^{∓iq·R_I} cancel in the double commutator, so 𝔨₃ = (q²/2M²)⟨∂_q̂²V_pot⟩ holds at
all q. The pieces:
- V_ee is independent of R.
- ∇²_I V_NN = 0 away from coincidences; on a cubic site the averaged tensor is ∝ 𝟙, so ⟨∂_q̂²V_NN⟩ = 0.
- ∇²_R(−U_κ) = +Z_κe²δ³ (HL units, ∇²(1/4πr) = −δ³).

So 𝔨₃ = (q²/2M²)Z_κe²𝓃_e(R_κ)/3 exactly, under point nuclei and T_d sites. Normalisation check: with inversion,
𝓜³_κκ = 2∫(dω/2π)ω³S_κκ, so its potential part is 2𝓃_κ𝔨₃ = 𝓃_κq²Z_κe²𝓃_e/(3M²), as the package states. ✔ V_eN has no I ≠ J
cross derivatives, so "|_{V_eN}" is a pure self quantity. ✔

**Contact face (5.2′c): not exact at finite q.** The eκ moment WP0-v2 (4.7) carries the phase e^{iq·(R_I − r_i)}. The δ-function (trace)
part sits at r = R, where the phase is 1. The traceless ℓ = 2 part of (q·∇)²U, which averages to zero in the κκ moment by cubic symmetry,
couples in the eκ moment to the ℓ = 2 component of the phase. WP0-v2 states exactly this, with the qualifier qa ≪ 1.

Quantitatively, define R(q) = T(q)/T(0), T(q) ∝ ∫d³k ñ(q + k)(q̂·k̂)², for hydrogenic 1s², ñ(p) = (1 + p²/4Z²)^{-2}. Numerically
(scipy quadrature, scratch check only), with q in units of 2Z/a₀:

| q/(2Z/a₀) | 0.3 | 0.5 | 1 | 2 |
|---|---|---|---|---|
| R(q) | 1.035 | 1.091 | 1.288 | 1.674 |

For Si 1s (Z_eff ≈ 13.7) the unit is 2Z/a₀ ≈ 102 keV. So 𝓜³_κκ|_{V_eN} = −(m_e/M_κ)𝓜³_eκ fails by about 9% at q ≈ 51 keV and 29% at
102 keV. The 2s/2p shells break it earlier. That is the IA regime where (5.2′) is meant to be used.

Owed:
- Replace "exactly" (§0 item 6) and "at contact" (5.2′c, IF-1) by "for q·a_{1s} ≪ 1 (Si: q ≪ 50 keV)". 𝔨₃ itself stays exact.
- With that qualifier, WP2-v2 is consistent with WP0-v2 (4.7) and, per WP0-v2's record, with WP3-v2 J8 (q → 0). Without it, WP2-v2 is
  inconsistent with both.
- C11d checks the 1D operator algebra at phase = 1 only.

**(5.2) [D] at leading BO order ✔.** The identity ⟨∂²V⟩ − ∂²E₀ = 2Σ_n|⟨n|∂V|0⟩|²/ΔE_n gives 𝔨₃^X = (q²/M²)Σ|…|²/ΔE, equal to the ω³
moment of |(q/M)⟨n|∂V|0⟩/ΔE²|². The first moment, (q²/M²)Σ|…|²/ΔE³ = q·δM·q/(2M²), is the Born–Huang drag mass. ✔

Remark: since 𝔨₃^X/𝔨₃^{GS} ≈ 8×10⁵ [E], the listed O(𝔨₁/ΔE₃) and O(κ_BO⁴) corrections, relative to 𝔨₃, exceed 𝔨₃^{GS} itself. For
example, 3E_R/ΔE₃ × 8×10⁵ ≈ 10³ at E_R = 1 eV. 𝔨₃^{GS} is therefore usable only if defined and computed directly as a GS-sector cumulant
(as L6 prescribes), never as 𝔨₃ − 𝔨₃^X. Say so explicitly.

## G. Cubic isotropy (8.2) ✔
Φ_κκ(0,t) = q_αq_β∫dω D^{αβ}_κ(ω)[(n + 1)e^{−iωt} + n e^{iωt}]/(2M_κω). Every n_ph term of S_inc is a functional of this rank-2 site tensor
(and of 2W_κ = q·B_κ·q). T_d sites (Si, Ge, GaAs, diamond) admit only δ_αβ, so S_inc depends on |q| alone, at every n_ph and T.
The selection rules are right too: TR gives even ℓ, and for even ℓ, T_d, O_h and O share the A₁ multiplicities 1,0,0,0,1,0,1,0,1 (C7).
The theorem covers exactly 2411.03433's framework (their Eq. (24) with D^{q̂}, IA with q̂ = ẑ), so "explains their negligible Si/GaAs
modulation" stands. The residual list (coherent n = 1, κ ≠ κ′ shells, rank-4 𝔨₄) is complete for the harmonic + IA model.

## H. Other literature claims [FT]
- **2309.10839 Eq. (9)** (v1): e^{−W_d} with Eq. (10) W_d = (q²/4m_d)∫D/ω. Eq. (13) has e^{−2W^toy} with W^toy = q²/4m_dω₀ = W_d for
  D = δ(ω − ω₀), and 2205.02250 Eq. (36) has e^{−2W_d}. **CONFIRMED** (internal inconsistency; numerics not checked; only v1 read).
- **2009.13534** (text after Eq. (31)): "in the absence of ordering, the corresponding terms should be dropped". Their 1/N² argument omits
  the sum over all N phonon momenta k, which restores a finite incoherent rate (Σ_k (1/N)|Σ_l V_l e^{i(q−k)·x_l}|² ∝ N). **CONFIRMED.**
- **2205.02250** (below Eq. (38)): "The true peak is shifted slightly from the result (38)". A peak is the mode, and the mode does shift
  (by ≈ −𝔨₃/2𝔨₂). The mean is not claimed to shift. The claimed error is **REFUTED**: delete the L6 "Discrepancy" and the §0 item 6 /
  (5.1) framing, and keep "𝔨₁ is exact" as a clarification.
- **2411.03433** §II.B: they state that they use the isotropic approximation for the IA width (q̂ = ẑ) and that ω̄_d differs by 6–8% along
  xy for Al₂O₃. The description is accurate, but the approximation is declared, not omitted. **Reword.**
- **Quotes verified** [FT], matching: 1910.08092 Eqs. (92), (105), (106); 1807.10291 Eqs. (29), (32); 1712.06598 Eqs. (5), (7);
  2205.02250 Eqs. (36), (39), (42); 2309.10839 Eqs. (9), (10), (13), (16), (17); 2411.03433 Eqs. (12), (18), (24); 2607.24933 Eqs.
  (44), (46)–(48).
- **Not re-verified:** hep-ph/0608035 Eqs. (5), (9); 2011.09477 Eq. (10); 2607.06005 Eq. (10); 2506.11191.
- Citation slip: the π/Ω one-phonon form sits on the line tagged (91) in the 1910.08092 HTML, together with the Y_j definition, not on
  (90), which is the definition of S.

## I. LIMITS entries owned (rubric b)
- **L4 ✔:** chain valid, validity numbers reproduced (q_BZ 2.28/2.19/2.19 keV; 2W = 6.4×10⁻⁴ at 1 keV; (36/1500)² = 5.8×10⁻⁴), leading
  corrections right. Add the O(2W) vertex-bookkeeping remark of §A.
- **L5 ✎:**
  - The chain step "(equivalently the BZ average (2.4) minus intra-cell terms)" must read "minus κ ≠ κ′ terms from all ΔR", with
    q ≫ n_ph q_BZ.
  - Validity "rates ω-integrated over ≳ ω_max" is [E] below q_BZ.
  - Numbers reproduced (45.75/55.79 keV; 1.89–18.9 MeV).
  - The truncation statement is correct (§C).
- **L6 ✎:**
  - Delete the 2205.02250 discrepancy (§H).
  - The "leading correction: skewness 𝔨₃^{GS}" is right, but 𝔨₃^{GS} must be computed directly (§F remark).
  - IA onset 91.5/111.6 keV and endpoint masses 17.3/21.1 MeV reproduced.
- **L18 ✔:** quote and discrepancy CONFIRMED.
- **L19 ✔** with the 2411.03433 rewording.

## J. Gap closures (rubric e)
G3, G11 and G13 give formula + code + mesh + cost + output format: a real specification. Defects:
1. (3.5) at T > 0 is a two-sided integral equation, degenerate at ω = 0 and with a δ(ω) seed. The stated O(N_ω²) "march" exists only at
   T = 0; specify the FFT of e^{Φ(t)} (with a regulator for the Bragg δ) as the T > 0 route.
2. The G3 tables start at q = 0.1 keV with n_ph ≥ 2 from (3.2). Below ~n_ph q_BZ this is the unproven regime (§B; §12 gap 1). Flag those
   cells, or route them to the coherent (2.2), which G13 already specifies.
3. G11 "shell corrections for |ΔR| ≤ 4 shells" must index the pairs (ΔR, κ, κ′) (§B).

## K. Required corrections (summary)
1. (2.4): add the cross terms Σ_{ΔR,κ≠κ′} j_BZ(ΔR + r_κ − r_κ′)* S_{κκ′,ΔR}, and the hypothesis q ≫ n_ph q_BZ; fix the C9 wording.
2. §3.3: index shells by (ΔR, κ, κ′); replace "≈ 2%" by the envelope or a range (≈ 2–10% for q = 2–10 keV).
3. (5.2′c), §0 item 6, IF-1: add the qualifier q·a_{1s} ≪ 1 to the κκ/eκ contact relation (fails by 9%/29% at 51/102 keV in Si).
4. L6 / (5.1): drop the 2205.02250 "discrepancy" (REFUTED).
5. §3.3 / L5: limit the 2607.24933 Eq. (47) charge to the polarisation weights; note the declared assumption and that (47) is not used
   numerically.
6. §8.2 (iv) / L19: 2411.03433's IA width is a declared approximation.
7. (7.1): "exact" up to isotope mass disorder O(ΔM/M).
8. (3.5) / G3: Panjer cost and route at T > 0.
9. (2.2) / (1.2): e^{−W} on the δρ part of the vertex (O(2W)); NOTATION δρ_κ row vs δρ^val_κ.
