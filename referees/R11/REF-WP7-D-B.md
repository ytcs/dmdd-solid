# R11 referee report REF-WP7-D-B (hostile, isolated) on returns/R10/WP7-D.md

Brief: briefs/R11/REF-WP7-D-B.md. Read: the return, code/WP7-D/checks.py, WP0-v3, CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS.
Checks re-run: `python3 -I checks.py` gives **34/34 PASS** (about 5 s, reproduced). Full text fetched with lit.py into
literature/papers-r11-WP7-D-B/ and deleted afterwards: 1306.6089, 2011.01940, 2501.05504, 2507.14287, 1905.12635, 2109.08168, 1711.10489,
2101.01241, 1508.01798, 2006.13918, 1509.01598, 2102.10171 (PDF). Hand re-derivations: the (F.4) lepton-tensor contraction, the (F.6)
recoil factor, the (T.3) seagull rate, the (S.1) prefactor and the (D.3) monochromatic limit all agree with the return. No simulations were run.

## Verdict table

| # | Claim | Verdict | Reason (short) |
|---|---|---|---|
| V1 | (D.1) field spectrum; 1711.10489 Eq. (24) as a limit (L-D2) | STANDS WITH CORRECTION | the source is quoted correctly, but the k sign of (D.1) contradicts CONVENTIONS §2 and the second equality of (D.3) (§A1) |
| V2 | (D.2) coherent signal = off-diagonal retarded R; finite-body replacement | STANDS | Kubo at first order; finite body and depolarisation are correctly tagged sketch |
| V3 | (D.3) mean power and mean counts = f_χ-averaged (3.5); bunching | STANDS | re-derived; "any t_int" needs a stationary (always-on) coupling, which should be stated |
| V4 | (D.4), L-D1: Bloch limits; 1306.6089 Eq. (1) envelope wrong | STANDS WITH CORRECTION | envelope CONFIRMED; "resonant growth agrees" UNRESOLVED (factor 2, §A2); R_{I⁺I⁻} label inconsistent with the (3.2) order |
| V5 | (D.5)–(D.6), L-D3: SNR scalings, crossover (3/2)t_coh | STANDS WITH CORRECTION | the scalings stand; the constant 3/2 uses the weak-signal TS where one bin needs s/b = O(1) (§A3) |
| V6 | (D.7), L-D4: BAR, Q_s → Q_DM^eff = (π/2)mF_φ ≤ 1.3×10⁶ | STANDS WITH CORRECTION | Q_DM^eff CONFIRMED; "1/ε₀ = slab case" is not exclusive (bulk also gives 1/ε₀); the grid truncates the line (§A4) |
| V7 | "(D.8)", L-D5: h = −δα/α − δm_e/m_e; drive ∝ ω² | STANDS WITH CORRECTION | the scaling stands, source quoted correctly; no equation (D.8) exists; the (Zα)² number for Cu is unsupported (§A5) |
| V8 | "(D.9)", L-D6: multiferroic = R_{s^z,trJ_e} | STANDS WITH CORRECTION | the symmetry argument stands; the source's regime is Ginzburg–Landau near T_CM, which LSWT cannot compute (§A6) |
| V9 | (F.1)–(F.5): fermion-number-changing class; m_χ²/q² by continuity | STANDS | traces and contraction re-derived by hand; the hypothesis (L) is stated |
| V10 | (F.6), L-D7: 1905.12635 Eq. (4) + (1 − m_χ/M) + impulse width | STANDS | source quoted correctly; recoil factor re-derived; width [E] plausible |
| V11 | L-D8: 2011.01940 Eqs. (7), (10) exact; Eq. (9) off by 1 − ω²/m² + … at bound kinematics | STANDS WITH CORRECTION | algebra CONFIRMED; the size statement is wrong in both directions (§A7) |
| V12 | (T.1), L-D9: pair absorption = two-point S at (≈0, 2m_χ); ξ = 44.8 ↔ ρ/2m per species | STANDS WITH CORRECTION | the normalisation is CONFIRMED; the operator list and the wording are wrong (§A8) |
| V13 | (T.2)–(T.3), L-D10: dark Compton = 2109.08168 Eq. (2) through O(m_V/m_e) | STANDS WITH CORRECTION | re-derived; "first order in e" is wrong (O(e²) amplitude); "O(x²) is relativistic" is asserted, not shown |
| V14 | §3.1 classification and its two-point reductions | STANDS WITH CORRECTION | the reductions (closure → seagull + polarisability; Wick for (d)) are sketches tagged [D] |
| V15 | §3.5: §11.9 closed (independent processes, mediator never on shell) | STANDS | trivial and correct |
| V16 | (S.1)–(S.2), L-D11: Lindhard and Bethe as limits of (3.3) | STANDS WITH CORRECTION | the (S.1) prefactor is correct; the constant inside the Bethe log is not derived (k_min ≈ Ī/v is a heuristic) |
| V17 | §4.2, L-D12: I2 split; radiative part ∝ Re n_r | STANDS WITH CORRECTION | for a magnetic-dipole decay in a non-magnetic medium the factor is n_r³, not n_r (§A9) |
| V18 | Bookkeeping: equation labels, symbol table "no collision" | STANDS WITH CORRECTION | (D.8), (D.9), (F.7), (T.4)–(T.6), (S.3), (S.4) are cited but never defined; X and ε collide with NOTATION (§A10) |

## (c) Claims that a published paper is wrong or needs reinterpretation

| Claim in the return | Rating | Evidence (full text) |
|---|---|---|
| 1306.6089 Eq. (1) prints sin(δt)/δ, while the exact small-tilt envelope is sin(δt/2)/(δ/2), so the printed resonance is half as wide | **CONFIRMED** | Eq. (1): M ≈ npμE*ε_S d_n · sin[(2μB_ext − m_a)t/ħ]/(2μB_ext − m_a) · sin(2μB_ext t) ("≈"). Lab-frame linear response gives (cos ω_m t − cos ω_L t)/δ ∝ sin(δt/2)·sin(ω̄t); the first zeros are at π/t (source) and 2π/t (exact) |
| ... and "resonant growth agrees" with Ω_a = E*ε_S d_n | **UNRESOLVED** | the source says "d_n ε_S E* is the energy shift produced between spin-up and spin-down states", i.e. the splitting. Then the rotating-frame Rabi frequency is d_nε_SE*/2 and Eq. (1) is 2× the linear response on resonance. The return's identification assumes splitting = 2d_nε_SE*, against the source's own sentence (§A2) |
| 2011.01940 Eq. (9) (free-electron vertex at bound q) is not current-conserving; it differs from the continuity result by 1 − ω²/m_χ² + O(1/m_e) | **CONFIRMED** (algebra and mechanism) | Eqs. (7), (9), (10), (30) and σ_e = m_χ²/(4πΛ⁴) quoted correctly. At m_e → ∞ the ratio Eq. (9)/URF is q(2m_χ − q)/m_χ² = 1 − ω²/m_χ². At K-shell kinematics the continuity current J_L = (ω/q)n is ≈ 0.5n, while the free vertex has J_L ≈ (q/2m_e)n: a real omission. But the magnitude claims are wrong (§A7) |
| 2501.05504: "Q_s = min(Q_p, Q_DM) ∼ 10⁶" is replaced, for Q_p ≫ Q_DM, by Q_DM^eff = (π/2)mF_φ(ω_n), whose maximum is 1.3×10⁶ | **CONFIRMED** | the text below Eq. (7) and Eq. (8) are as quoted; ∫γ/(4Δ² + γ²)dΔ = π/2; the SHM peak value is reproduced. This reinterprets the paper consistently; it does not show the paper wrong |
| 2501.05504: "the 1/ε₀ in their Eq. (5) is the slab case" | **REFUTED as an exclusive attribution** | the source attributes 1/ε₀ to bulk dielectric screening ("Since the BAR is also dielectric"). For a non-relativistic dark photon (k ≪ ω) the bulk in-medium mixing is also κ/ε(ω → 0). Slab-normal and bulk coincide; sphere (3/(ε+2)) and slab-parallel (1) differ (§A4) |
| 2109.08168 Eq. (2) agrees through O(m_V/m_e); the O(x²) difference is relativistic | agreement **CONFIRMED**; "relativistic" **UNRESOLVED** | Eq. (2) quoted exactly; both sides expand to 1 − 3x/2. No computation supports the attribution of the O(x²) term |
| 2507.14287 Eq. (8) with ξ ≃ 44.8 gives ρ_DM/(2m) per species | **CONFIRMED** | f_DM = ξρ_DM/(2g m⁴β_c³)e^{−p²/m²β_c²}, β_c = 7.8×10⁻⁴, β_esc ≃ 5β_c/2. The g cancels; the cut Gaussian integral gives ξ = 44.8 |

## (b) Proposed LIMITS rows: quotation, chain, validity
- L-D1: 1306.6089 Eq. (1) and 2101.01241 Eq. (1) (M_a = uM₀Ω_aT₂cos ω_at) are quoted correctly. The chain is valid. The amplitude caveat of §A2
  must be added to the ✎.
- L-D2: 1711.10489 Eqs. (8), (10), (24) are quoted correctly. The chain is valid, with the k-sign correction (§A1).
- L-D3: 1306.6089 "Eqs. (8)–(9)" follow the arXiv HTML numbering; the PDF numbers them (A7)–(A8), and likewise (2) = (A1), (3) = (A2).
  State both numberings. 1711.10489 Eqs. (54), (63), (69) are quoted correctly. Validity: the crossover constant is not reliable (§A3).
- L-D4: 2501.05504 Eqs. (5), (7), (8) are quoted correctly. The prefactor 32 and M_n are open (declared). Fix the 1/ε₀ attribution (§A4).
- L-D5: 1508.01798 Eq. (7) is the effective Riemann tensor R_{i0j0} = δ_ij ḧ; h ≡ −δα/α − δm_e/m_e is defined in the sentence after it, and
  Eq. (8) is the force F_mod,n = −ḧM°RJ_n. Acceptable, but cite it as "Eq. (7) and text".
- L-D6: 2102.10171 Eqs. (5) and (10) are quoted correctly (Eq. (10): 1/√((ω_a² − ω_M²)² + η_M²ω_a²) × [χαM₀/2α_M − cP₀/2m_P²], with η_M a
  phenomenological damping). The chain needs the correction of §A6.
- L-D7: 1905.12635 Eqs. (1), (3), (4), σ_NC = m_χ²/(4πΛ⁴), and "ΔE_R/E_R ∼ 10⁻³" are all quoted correctly. The chain and the leading
  correction −m_χ/M are correct.
- L-D8: the dictionary S̄_at = π|f_ion|²/(2E_R) holds with 1509.01598 Eqs. (51)–(52), provided "occupied states" includes both spins
  (2k′³ prefactor). This is equivalent to the 4k′³ per (n,l) shell of 2011.01940 Eq. (8). State that equivalence explicitly, because the two
  printed prefactors differ by 2.
- L-D9, L-D10, L-D12: quoted correctly (2507.14287 Eqs. (3), (5)–(8); 2109.08168 Eqs. (2), (3); 2006.13918 Eq. (2)).
- L-D11: Bethe is [UNVERIFIED] (declared). The row should be tagged "D (Lindhard), sketch (Bethe log)".

## A. Corrections

**A1 (k sign in (D.1)).** With CONVENTIONS §2 (O(q) = ∫e^{+iq·r}, f(ω) = ∫dt e^{+iωt}), the stated inverse ⟨φφ⟩ = ∫𝒮e^{−ik·Δx−iωΔt}
applied to ⟨φφ⟩ ∝ cos[ω_vΔt − m_φv·Δx] puts the positive-frequency weight at **k = −m_φv**. Under the campaign convention, however, the
drive yφ couples to O(+k_φ), and that is what the second equality of (D.3) uses (R_OO(m_φv, ω_v)). Either write
𝒮_φ ∝ δ³(k + m_φv)δ(ω − ω_v) + δ³(k − m_φv)δ(ω + ω_v) and pair 𝒮(k,ω) with R(−k,ω) in (D.3), or redefine the transform. The error is
immaterial for P,T-invariant targets. CONVENTIONS §3 nevertheless makes the campaign sign binding, and §1.9 (multiferroic) is P,T-broken.

**A2 (spin precession).** (i) Under (3.2), R_ab carries O_a† first, so R_{I⁺I⁻} contains [I⁻, I⁻] = 0. The quoted pole
−(2⟨I^z⟩/V)/(ω − ω_L + i/T₂) is R_{I⁺I⁺} (O_a† = I⁻) for H = +ω_L I^z, ⟨I^z⟩ < 0. State the label and the sign of ⟨I^z⟩. Otherwise −Im R < 0
reads as emission. (ii) Remove "resonant growth agrees" from IF-D11/L-D1. Replace it with: "agrees if the source's d_nε_SE* is half the
up–down splitting; with the source's own definition (splitting), Eq. (1) is 2× the linear response at δω_L = 0." Rate the amplitude as
UNRESOLVED. (iii) The claimed form of u in 2101.01241 points to that paper's supplement (their ref. [53]), which was not read: tag it [D, sketch].

**A3 (crossover (3/2)t_coh).** (D.6) is the weak-signal Asimov statistic Σ(s/b)². For t_int ≪ t_coh the whole signal sits in one
Fejér-broadened bin, and TS ≈ 2.7 needs s/b = O(1) there. The exact exponential-bin Asimov statistic 2Σ[s/b − ln(1 + s/b)] then gives s/b ≈ 2.6 in a
single bin, where the weak-signal form gives √(2.71·3/2) ≈ 2.0. The scalings t^{−1/2} and (t t_coh)^{−1/4} stand. The constant 3/2 is an artefact: report "crossover at t_int = O(t_coh)",
or use the full statistic. Also, correction (a) of §1.6 (Rayleigh marginalisation) is already built into the exponential likelihood (complex
Gaussian signal plus noise), so applying it on top would double count. Say which is meant.

**A4 (BAR).** (i) The bulk in-medium mixing at k ≪ ω gives κ/ε₀ as well, so the source's 1/ε₀ is not specifically "the slab case". The
finite-body statement should read: relative to the bulk 1/ε₀, geometry multiplies the field by 1 (slab-normal), 3ε₀/(ε₀ + 2) (sphere)
or ε₀ (slab-parallel). That is up to ε₀² in power, a real IF-D9 item. (ii) Grid in §1.10: the SHM line is one-sided,
ω − m_φ = m_φv²/2 ∈ [0, 3.5×10⁻⁶m_φ] for v_max = 794.5 km/s (CONVENTIONS §8). "(1 ± 2×10⁻⁶)m_φ" wastes half the points and cuts the tail
above ≈ 600 km/s, so the 1% TS convergence target cannot be met. Use [m_φ, (1 + 3.6×10⁻⁶)m_φ].

**A5 (moduli).** No displayed (D.8) exists; number it. "dln a/dln α = −1 + O((Zα)²), e.g. 0.045 for Cu" takes the nuclear (Zα)² as the size of
the lattice-constant correction. With a = a_nr(1 + cα²) the correction is 2cα², i.e. twice the fractional scalar-relativistic lattice shift
(about 1% for Cu from standard DFT, sign negative). Keep it as [E] with the 2× fractional-shift formula and the sign; drop "0.045". The
"no force at k → 0, drive ∝ ω²" step is [D, sketch] and is tagged so in the text but not in the table: align them.

**A6 (multiferroic).** 2102.10171 obtains Eq. (10) from Ginzburg–Landau equations for longitudinal M dynamics ("a classical and minimal
description of the longitudinal magnon dynamics"; η_M is added by hand; the regime of interest is T ≈ T_CM with critical slowing down
τ ∼ |T − T_CM|^{−νz}, their Eq. (9)). LSWT on a T = 0 DFT+SOC structure does not produce a pole that softens at T_CM, and it cannot give the
critical-regime response the source targets. The computation spec must say "LSWT gives the T ≪ T_CM limit only. The near-T_CM regime needs a
finite-T method (e.g. stochastic LLG / spin dynamics on a DFT spin model) and is an exact remaining gap." Also note that ω_M in the source is
the zone-centre mode they call a magnon, while their dynamics is longitudinal: the "single-magnon-pole" identification is a sketch.

**A7 (2011.01940 size).** Using the coded ratio (code/WP7-D C10), checked here numerically:
- valence (ω = E_R^free + 12 eV): ratio 1.0067 at m_χ = 100 keV and 1.0196 at 200 keV. "< 10⁻³" holds only for m_χ ≲ 30 keV. This O(m_χ²/m_e²)
  part is of the same order as the J_T term the URF itself drops;
- Xe K shell: −5% is the value at threshold ω = 34.6 keV. At the typical ω = 34.6 + E_R ≈ 43 keV it is −11% (m_χ = 100 keV), and at the
  source's best-fit m_χ = 56.5 keV it is −34% to −41%.
So the effect is larger than reported where it matters, and smaller than the URF's own omitted terms for valence shells. Leading correction (i),
S_{J_TJ_T} relative ⟨p_e²⟩/m_e² ≈ (Zα)² ≈ 0.16 for the Xe K shell, has the same size as the claimed difference. IF-D10 should therefore
say: "the O(1) term −ω²/m_χ² is a real continuity defect of the free-vertex ansatz; a quantitative comparison needs the J_T and Dirac terms."

**A8 (pair absorption).** In 2507.14287 Eq. (3) the axial (and vector) electron currents come with the derivative DM current
i(S†∂↔^μS), not with S†S. The DM-side factor is then (E_p − E_p̄, p − p̄): the time component vanishes at leading order and the spatial part is
O(m v). "ψ̄γ^μγ₅ψ → spin rows" under H = G_pair(S†S)O is therefore a misattribution. It still yields a two-point S, but with a velocity-dependent
𝔇. Also (T.1) is a rate per unit volume (dimension 4), not "per DM pair density".

**A9 (I2 radiative factor).** The decay χ* → χγ in 2006.13918 Eq. (1) runs through σ^{μν}F_{μν}, a magnetic-dipole transition. In a transparent
non-magnetic medium the photon density of states scales as n_r³ and the per-photon |B|² as n_r²/n_r² = 1, so Γ_MD ∝ n_r³; Γ ∝ n_r holds for
electric dipoles. Replace "∝ Re n_r(δ)" by n_r³ (local-field factors aside), or derive it from −2 Im Σ with 𝒟^γ_T.

**A10 (bookkeeping).** (i) §0 and §5 cite (D.1)–(D.9), (F.1)–(F.7), (T.1)–(T.6), (S.1)–(S.4). Only (D.1)–(D.7), (F.1)–(F.6), (T.1)–(T.3) and
(S.1)–(S.2) exist. (ii) The §6 claim "no collision found" is false: X (readout total) collides with the sectors X, X0, X+ of NOTATION
(line 214), which §1.2 itself uses ("electronic X sector"). Bare ε (polarisation vectors in (T.2)) collides with ε ≡ ε_c (NOTATION line 181,
⚠). Rename them (e.g. X_rd; e_λ, e′_λ′). (iii) §3.4 "first order in e": the amplitude (T.2) is O(e²κ_mix). (iv) h_mod and d_α are listed
in §6 but never used.

## (a) DERIVED steps without derivation (downgrade to [D, sketch] or derive)
§3.1 reductions (closure, Wick factorisation); (S.2) constant inside the log; 2101.01241 u formula; §1.8 "no force in comoving coordinates";
§2.5 massive-ν̃ reduction (q²/2m_ν̃ versus q²/2m_χ of WP0 (2.1), a difference of O(Δ_χ/m_χ), unstated). Everything else tagged [D] was checked
and is derived.

## (d) Consistency with WP0-v3, CONVENTIONS, NOTATION
(3.5), (3.6), (4.1) and the tr[𝔇ᵀS] order are used correctly; the (D.5) noise −V coth(βω/2)Im R is the symmetrised (4.1) (checked). Departures:
A1 (k sign, CONVENTIONS §2–3), A2(i) ((3.2) index order), A10(ii) (NOTATION collisions). The ρ_χ = 0.3 and v₀ = 238 numbers match
CONVENTIONS §8. 2507.14287 uses ρ = 0.39; the return does not mix them.

## (e) Gap-closure sufficiency
Items 1–3: formula plus spec is sufficient, subject to A4(ii) (grid) and A6 (the multiferroic near-T_CM regime becomes an exact gap).
Item 4 (D3, D4, I2): the out-of-scope reasons are exact and the hand-off kernels are specified; with A9 for I2. §11.9: closed.
Charged-current fermionic absorption: stated as an exact remaining gap, correctly.

## (f) Novelty
The return claims no literature novelty; the new rows (𝔘_C, 𝔇^F) are framework additions. Q_DM^eff (a narrow resonator tracking the DM line
shape) is standard haloscope lore and should not be presented as a correction of 2501.05504 beyond what is stated. For IF-D10, later
relativistic or bound-electron treatments of fermionic absorption (e.g. 2201.11905, plus the IDs the return lists as "verified but not
read") were not checked. Priority for the continuity remark is UNRESOLVED; do not promote it to a literature correction without that search.

## Required before REFEREED
A1, A2, A3, A6, A7, A9 and A10(i)–(ii) are mandatory; A4, A5 and A8 are minor. No claim FALLS.
