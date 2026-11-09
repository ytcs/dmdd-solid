# VER-CW4: hostile verification of returns/R16/CW4.md (LE-97 … LE-117)

Referee VER-CW4, brief briefs/R16/VER-CW4.md, 2026-11-01. Read: the return, code/CW4/checks.py, returns/R8/WP4-v3.md, returns/R12/WP7-B1-v2.md
(§9, §10, §12, E10, gaps), LIMITS.md rows L15, L16, LB1-5/6/8/10/11/13, B2-L6/L7, state/LOOSE-ENDS.md (CW4 rows). Not read: referees/R16/*, other R16 returns, briefs, log.
Rerun: `python3 code/CW4/checks.py` gives **18/18 PASS** (≈ 3 s). Same printed tables as the return. Independent checks: hand derivations, a sympy script for the algebraic items (§1 note) and a numpy rerun of K4 (scratchpad, < 1 min).
Literature fetched to literature/papers-r16-VER-CW4/ (full text read; PDFs and the text dumps deleted afterwards): 2208.05967, 1509.01598, 1910.02091 (v2),
1603.05351, 2109.04473, cond-mat/0108424 (v2), 1604.06800, 1805.06359, 2305.06084, 0706.4150, 1708.08929, 2609.06423, 2401.11971, 2504.02927, 1912.13484.

## 0. Verdict table (scope 1–3)
| # | Item | Verdict | Reason (details in §1–§3) |
|---|---|---|---|
| V1 | OC-1/OC-2, LB1-10: (A2.2) [D, sketch] → [D] (§12, (12.1)) | **STANDS** | Re-derived. j(q=0) = Σv_kΨ†τ⁰Ψ + const commutes with H_BCS; only two orderings survive; amplitude and case-I factor ½[1−(ξξ′−Δ²)/EE′] are correct. The ξ-integral equals x·E(√(1−4Δ²/x²)), which is 1604.06800 Eq. (17) [FT]. "= Allen (1971)" is attribution through 1604.06800 only |
| V2 | OC-3, LB1-5: Eq. (6) prefactor verdict (§14, (14.1)–(14.2)) | **STANDS** | Eqs. (6), (10), (12) quoted correctly [FT]. Eq. (12) ≡ 1509.01598 Eq. (3.17) [FT]. (14.1) re-derived from 1509.01598 Eq. (3.9). Ratio μ_eχ/(4E_r) and the dimension mismatch confirmed |
| V3 | OC-3, LB1-5: depolarisation criterion; Ref. [139] | **STANDS** | 9\|ε\|²/\|ε+2ε_o\|² > 1 ⟺ \|ε\|² > (ε_o/2)(ε₁+ε_o) is exact algebra. [139] = Hechster & Sarusi, JAP 122, 024302, confirmed in the 2208.05967 reference list. "Modelled intrinsic" rests on the title only (metadata) |
| V4 | OC-4, LB1-11: UNRESOLVED → [E] impact numbers (§13, K5) | **STANDS** | K5 integrand checked: q³·B_GOS·η(v_min), correct kinematic limits, |ε| held fixed. Numbers reproduce. Remains [E] (their ε not used) |
| V5 | OC-5, LB1-6: OPW / FSI sizes (§17, K4) | **FALLS (numbers); STANDS WITH CORRECTION (rest)** | "−25 to −35 % at 50–100 eV" is false away from the two sampled q. Same K4 functions: ×1.5–4.2 at 50 eV, q = 25–40 keV; 0.40–0.92 at 100 eV, 40 keV; up to ~5×10² at 10 eV. The 1D-Dirac part stands |
| V6 | OC-6, LB1-8: [D, sketch] → [D] under (H_W) (§19) | **STANDS WITH CORRECTION** | (19.1), K7 and K7b are correct. Owed text says "with Hermitian ordering", which contradicts the rejection of the symmetrised ordering in the same sentence. The relative-error bound is not a bound on the sum |
| V7 | OC-7, LB1-13: UNRESOLVED → "impact … exactly" (§18) | **STANDS WITH CORRECTION** | (18.1) follows from B1 (I5.1) vs 2401.11971 Eq. (5) [FT]. The source is CRDM (v_χ → 1), where the bound is vacuous, so the impact on *its* limits stays UNRESOLVED. K11 is tautological |
| V8 | OC-8, B2-L6: citation [FT] + AFM weight (§20, (20.1)) | **STANDS** (one return-text fix) | Oshikawa–Affleck quote verbatim [FT]. (20.1) re-derived by Bogoliubov: weight S(u−v)² = S√((A−B)/(A+B)). Kanamori–Tachiki is cited for the resonance *shift* (App. A11), not for linewidth theory |
| V9 | OC-9, B2-L7: no-go theorem (§21) | **STANDS** | P_T(gq̂):(gSgᵀ) = P_T(q̂):S holds trivially. (H_iso) inversion re-derived: P_T:S = S_∥(1−c²) + S_⊥(1+c²) |
| V10 | OC-10, L16: re-plot = exact shifts (§9, (9.1)) | **STANDS** | Follows from refereed WP4 [5.3]/[5.5] for background-free Poisson limits. 1708.08929 Eq. (2.6) keeps the log [FT], so not ×0.55–0.62. Numbers check: 1600, 640, 6.3, 5.0 |
| V11 | OC-11, WP8-U ZrTe₅ (§10) | **STANDS WITH CORRECTION** (target file; one fact) | 1910.02091 p.12 quote, Table 1 and caption verified [FT]. 1603.05351 has no gap value [FT]. Its Table I v_F (1.94, 4.89, 4.03 ×10⁵ m/s) *are* the "Exp. [52]" velocities; only the 11.75 meV is unsupported. OC-11 targets R13 WP8-U-table.csv, but R14 WP8-U-table-v2.csv supersedes it (same row, l.1543): name the v2 file |
| V12 | OC-11, WP8-U Al / Nb (§11) | **STANDS WITH CORRECTION** | Nb quote verified (1805.06359 p.3). 2109.04473 p.2: "∆ is half of the superconducting gap … For aluminum (Al), with ∆ = 0.3 meV" [FT], so the 1.7× finding is CONFIRMED (1604.06800 also uses ∆ ≃ 0.3 meV). Tag inconsistent: [D from FT T_c] in §11 and IF-CW4-2 vs "tag E" in OC-11. Correct tag is E. Target the R14 v2 table: its Nb row is `Delta_BCS_E` = 1.63 meV (1.764k_BT_c with DFT T_c 10.72 K, l.2395); OC-11 must add a measured row next to it, not overwrite a non-existent "Delta_BCS" |
| V13 | OC-12, WP4 I12 / L15: resummed (8.1) (§8) | **STANDS** | Algebra re-derived. Reduces to [4.2′] at first order. Re 𝔣_Lin(0.39) = 0.839 and 𝔯 = 0.730 checked. Log-at-threshold sign correct (step up ⇒ δ_𝔰 → +∞) |
| V14 | (1.1) GRPA vertex fraction 𝔳_GRPA (§1) | STANDS | Coherence factors equal 2609.06423 Eq. (7) [FT]. Retarded vs time-ordered pitfall noted correctly |
| V15 | (2.1) WSi configurational average (§2) | STANDS WITH CORRECTION | The validity clause ("correlation length exceeds … only partially") is garbled and L^nor_loc is undefined. See §3 |
| V16 | (3.1) two-magnon ladder (§3) | STANDS | Order counting O(1/S²) relative to one-magnon is right. Add the identical-pair (k ↔ q−k, ν = ν′) counting pitfall |
| V17 | (5.1) embedded transition density (§5) | STANDS | Standard one-body transition density. Structure only |
| V18 | (6.1) massive-Dirac Rydberg (§6) | STANDS (formula); spec corrected (§2) | Ry = μ(α/ε)²/2 with μ = Δ/(2v²) gives Δ(α̃/g)²/4. 0.052 and 0.145 meV reproduced. ZrTe₅ value is an isotropic [E] |
| V19 | (7.1) multiplet form-factor structure (§7) | STANDS | Even K ≤ 2ℓ with odd-rank K′ = K ± 1 (T-odd) is the standard tensor structure. Citation stays [UNVERIFIED] |
| V20 | (12.1) strong-coupling N_sN_s′ + P_sP_s′ | STANDS as [D, sketch] | Case-I creation (1+Δ²/EE′)·N_sN_s′ = N_sN_s′ + P_sP_s′ (BCS limit). The 1/(1+λ_tr) clause is only asserted |
| V21 | (13.1) valley–orbit lines | STANDS WITH CORRECTION | Si: g-process at 2k₀ ≈ 3.9 keV (or ≈ 0.7 keV after umklapp), f-process ≈ 2.7 keV. "≈ 2–3 keV" is wrong for g |
| V22 | (15.1) Förster coupling and size | STANDS | 5.6×10⁻⁵ eV reproduced. d = 0.3 nm is an input [E] |
| V23 | (16.1) Frenkel–CT mixing | STANDS | Two-state algebra. Note f_C(0) = 0 for orthogonalised orbitals (charge), as the difference form implies |
| V24 | (17.1) 1D massive-Dirac bubble | STANDS | Coherence factor ½(1 − n̂·n̂′) and closed form verified (K3). Weight ∫ = 1 re-derived (t-substitution). Massless limit g v q²δ(𝓈) = Luttinger. I₀K₀ is the *shell* kernel ("uniform cylinder" → "cylindrical shell") |
| V25 | (19.1)–(19.2) | STANDS WITH CORRECTION | See V6 |
| V26 | (20.1) AFM k = 0 weight | STANDS | See V8 |
| V27 | §21 no-go | STANDS | See V9 |
| V28 | Closure counts (§0) | STANDS WITH CORRECTION | The table gives 16 CLOSED rows (LE-97, 98, 100, 101, 103–106, 108–114, 116), not 15. At least 4 carry exact-gap remainders (LE-97, 104, 109, 110), not 2 |

## 1. Scope 1: owed corrections and status upgrades
**V1 (LB1-10 → [D]).** Independent derivation. With Ψ_k = (c_{k↑}, c†_{−k↓}) and v_{−k} = −v_k, Σ_kσ v_k c†c = Σ_k v_kΨ†_kτ⁰Ψ_k + const. So [j, ξτ³ + Δτ¹] = 0 needs only ξ_{−k} = ξ_k and Δ_{−k} = Δ_k. (For a parabolic band this is total-momentum conservation; the τ⁰ argument is the proof in general.)
Only two second-order orderings survive, with denominators +ω and −ω, which gives (12.1). The coherence factor comes from c_{k↑} = uγ_{k↑} + vγ†_{−k↓} and c_{−k↓} = uγ_{−k↓} − vγ†_{k↑}: γ†_{k+Q↑}γ†_{−k↓} has coefficient u_{k+Q}v_k + v_{k+Q}u_k, using (h3) g_{−k,−k−Q} = g_{k+Q,k}. Squared, this is ½[1 − (ξξ′ − Δ²)/EE′], which is Tinkham case-I creation.
The ξ-average gives ½(1 + Δ²/EE′). It integrates to x·E(√(1−4Δ²/x²)) (K1d), which is the integrand of 1604.06800 Eq. (17) [FT]. "No off-shell requirement" is correct, so the upgrade to [D] under (h1)–(h5) is justified.
*Correction to OC-1 text:* write "result = Allen (1971) as cited by 1604.06800 Ref. [29] (Allen not read)", not a bare "result = Allen".
**V2 (LB1-5 prefactor).** From 1509.01598 Eq. (3.9) [FT], σv = (σ̄_e/μ²)∫d³q/(4π) δ(…)F²|f|². The angular δ gives 2π/(qv), so d⟨σv⟩/dE = (σ̄_e/2μ²)∫q dq ηF²⟨|f|²⟩ with Eq. (10)'s δ(E_r − ΔE). Multiplying by E_r·N_tρ/m gives (14.1) exactly.
Eq. (6)/(14.1) = μ_eχ/(4E_r) = 4.05×10⁴ at m_χ = 10 MeV, E_r = 3 eV. Eq. (12) is term-by-term 1509.01598 Eq. (3.17), which is dimensionless, so Eq. (6) with Eq. (12) has mass dimension 2. "Results are taken from more precise numerical codes" (p.5) is verbatim, so "numerics presumably (14.2)" is a fair [E].
Verdict on the published paper: **2208.05967 Eq. (6) (= App. Eq. (A1)) is wrong as printed: CONFIRMED.**
**V4 (LB1-11).** K5 uses the B1 (A6.2) GOS without the q̃² prefactor, weighted by q³, which is equivalent to q dq|F|². The printed 3q̃ form is larger for q̃ < 1, so the ratio is > 1 at threshold. Reproduced: 1.47/0.91/0.59/0.56 (heavy) and 1.46/1.24/1.07/1.06 (light). Keep the [E] tag and "|ε| fixed". The source's a* = 23 a.u. was not re-checked.
**V5 (LB1-6 OPW).** I reran the K4 functions on a wider grid (2×10⁴ final directions; q ∥ ẑ, x̂ and 45°). |M_OPW|²/|M_PW|²:
| E_kin | q = 5 | 7.5 | 15 | 25 | 40 keV |
|---|---|---|---|---|---|
| 10 eV | 0.70–1.20 | 0.76–2.98 | 2.1–67 | 7–274 | 7.6–508 |
| 50 eV | 0.66–0.96 | 0.73–1.00 | 0.65–0.91 | 0.97–1.49 | 1.18–4.25 |
| 100 eV | 0.67–0.97 | 0.90–1.11 | 0.91–0.98 | 0.73–0.93 | 0.40–0.92 |
Heavy-mediator kinematics reach q ≈ 2m_χv_max ≈ 50 keV at m_χ = 10 MeV, so these q are in range. The sign and size depend on q and direction at *every* energy. The (10 eV, 7.5/15 keV) points are not "on/far from the Bethe ridge" either: the ridge is q ≈ k_f = 3.2 keV.
*Replacement OC-5 text:* "OPW orthogonalisation (C 2p_z model, [E], CW4 §17 + VER-CW4): factor 0.4–4 at 50–100 eV and 0.7 to ~5×10² at 10 eV over q = 5–40 keV, q- and direction-dependent; sign not fixed without all occupied orbitals (spec CW4 §17); FSI between 1 and the unscreened Sommerfeld 2.6–7.3 (100–10 eV) [E]; semiconducting CNT: CW4 (17.1)". The FSI and (17.1) parts stand.
**V6 (LB1-8).** (19.1) is exact: [h,[h,r]]_cm = (ε_c − ε_m)²r_cm, and Σ∇V = m[h,[h,r]] for local h ([h,r] = −ip/m, [h,p] = i∇V). The phase is A^{Mig} = +q_e·⟨a|Σr|0⟩ = −i × (iq_e·⟨a|Σr|0⟩), which is correct. K7b is correct: (P_valF)_cv = 0 for c ∉ 𝒲.
Errors: (a) OC-6 begins "[D] under (H_W) with Hermitian ordering". It must read "with ket-side ordering", because the same sentence rejects the Hermitian (symmetrised) ordering. (b) "[1 + O(W_𝒲/ω_cv)]" and "relative error ≤ 2W/ω + (W/ω)²" bound each term v′, not the sum. If the r_cv′(p^W_0)_v′v cancel, the relative error is unbounded. The rigorous form is |A^{(H_W)} − (m_eq/M)⟨c|rp^W_0|v⟩| ≤ (m_eq/M)(2W/ω + W²/ω²)Σ_v′|r_cv′(p^W_0)_v′v|, so state that.
**V7 (LB1-13).** 2401.11971 [FT] is a cosmic-ray-boosted DM paper (Eq. (5), F_DM at q² = Q² − ω²). The bound [(1 − v²_max)², 1] is vacuous there, and the transverse row (up to ~8 %, B1 §12) is not in R_URF. So "impact … exactly" overclaims.
*Replacement OC-7 text:* "density-row ratio R_URF/R_src = ⟨(1 − ω²/Q²)²⟩_src ∈ [(1 − v²_χ,max)², 1] (CW4 (18.1)); ≤ 2 % for v_χ ≲ 0.1; for the source's CRDM flux (v_χ → 1) **impact on its limits UNRESOLVED**, recast specified (CW4 §18)".
K11 defines cor = (1 − ω²/Q²)²·src and then tests that identity, so it checks nothing. The ratio rests on B1 C12, which was refereed.
**V8 (B2-L6).** The Oshikawa–Affleck p.4 text (Eqs. (2.4)–(2.5), "completely sharp, and located exactly at the Zeeman energy", "absorption intensity is generally affected by the exchange") is verbatim. OC-8 stands.
(20.1): a + b† = uα − vβ† + uβ† − vα, so S^x_tot ∝ (u − v)(α + α† + β + β†). The weight is S(u − v)² = S(A − B)/√(A² − B²), as claimed.
Return-text fix (§20): Ref. 47 (Kanamori & Tachiki) is cited at App. Eq. (A11) for "the first term in the shift", which is the resonance shift and not the linewidth.
**V10 (L16).** σ_lim ∝ 1/N (Poisson, no background) and κ² ∝ 1/Γ give ε_bg² and √ε_bg. 1708.08929 Eq. (2.6) contains the x(1−x)ln term, so Re δε_D is in the source's ε_r, and the warning against also applying 0.55–0.62 is right. Note that the 1910.02091 Δ-row is still the "Exp." Δ = 11.75 in §6.
**V11 (ZrTe₅).** The 1910.02091 v2 p.12 sentence, Table 1 (11.8 NR, 15.6 ISIF7, 11.75 Exp. [52]) and the caption "band gaps" are verbatim, and Eq. (1.1) has "2∆ is the band gap". **"Exp. [52] Δ = 11.75 meV" not in [52]: CONFIRMED** (text search: no gap value; Table I has F, k_F, m_eff, v_F, τ, ℓ, μ).
Add to OC-11: the Exp.-row velocities are [52] Table I, assigned as 4.03, 1.94, 4.89 ×10⁵ m/s → 1.34, 0.65, 1.63 ×10⁻³ c. So only Δ lacks provenance.
**V12 (Al/Nb).** The WP8-U 0.3 meV is the half-gap used by 2109.04473 (p.2) and by 1604.06800 (p.4). Bulk Al Δ(0) ≈ 0.17–0.18 meV. 1.764k_BT_c is the weak-coupling BCS ratio, not a derived Al property. So OC-11's "tag E" is right, and §11 and IF-CW4-2 "[D from FT T_c]" must become [E]. The 0706.4150 30 nm film value 209 ± 11 μeV is verified (Table 1).
**V13 (I12 / L15).** Write ε^nor = R(1 + i𝔯), Im ε^BCS = 𝔤_I·Im ε^nor and Re ε^BCS = R(1 + δ_𝔰). Then L^BCS/L^nor = 𝔤_I(1 + 𝔯²)/[(1 + δ_𝔰)² + 𝔤_I²𝔯²] exactly, and at 𝔯 → 0 to first order it is 𝔤_I(1 − 2δ_𝔰) = [4.2′]. Table reproduced. IF-CW4-1 wording: k_TF²/q² is 19 % above 0.84k_TF²/q² (or the true value is 16 % below), so the "16 % high" phrasing is ambiguous.

*Sympy note (scratchpad alg.py, < 1 s):* exact checks pass for (8.1) ≡ direct L^BCS/L^nor and its first-order reduction to [4.2′];
Eq. (6)/(14.1) = μ/(4E_r); 9|ε|² − |ε+2ε_o|² = 8[|ε|² − (ε_o/2)(ε₁+ε_o)]; [h,[h,X]]_ij = (e_i−e_j)²X_ij (symbolic 3×3).
(20.1) S(u−v)² = S√((A−B)/(A+B)) was checked numerically, because sympy simplify did not close it.

## 2. Scope 2: claims that a published paper is wrong or misprinted
| Claim | Rating | Evidence |
|---|---|---|
| 2208.05967 Eq. (6) prefactor exceeds the correct rate by μ_eχ/(4E_r) with Eq. (10); dimensionally inconsistent with Eq. (12) | **CONFIRMED** | Full text pp.5–6 and App. (A1)–(A2). Derivation in V2 |
| 2208.05967 plotted numbers come from QEdark (so Eq. (6) is a typographical defect) | UNRESOLVED (plausible, [E]) | Only the "more precise numerical codes" sentence. Fig. 4 not recomputed |
| 2208.05967 Eq. (16) absorption lacks dot depolarisation | CONFIRMED (already, B1) | Eq. (16) and [139] text verified |
| 1910.02091 Table 1 "∆" is the half-gap; caption "band gaps" loose | **CONFIRMED** | p.12 sentence, Eq. (1.1) |
| 1910.02091 "Exp. [52]" Δ = 11.75 meV not in 1603.05351 | **CONFIRMED** | Search of 1603.05351 full text. The v_F entries are from [52] |
| 1910.02091 typo q_x²v_{F,z}² in Eqs. (3.13)–(3.14) | not new (WP4-v3, CONFIRMED R8) | v2 Eq. (3.5) (00 entry) prints the correct q_x²v_{F,x}². The typo is in (3.13)–(3.14) per R8, not re-checked here |
| 2109.04473 uses Δ_Al = 0.3 meV (≈ 1.7× bulk) | **CONFIRMED** | p.2, "∆ is half of the superconducting gap … ∆ = 0.3 meV" |
| 2401.11971 Eq. (5) lacks (1 − ω²/Q²)² | CONFIRMED (B1). Impact UNRESOLVED | V7 |
| 2212.04504 Eq. (12) 3q̃ misprint | CONFIRMED (B1). Impact [E] | V4 |
| Kanamori–Tachiki should not be cited for Larmor | CONFIRMED, with the V8 fix | cond-mat/0108424 App. A |

## 3. Scope 3: new derived results (beyond §1)
- **(2.1) / §2.** The local-gap average is the local-density (adiabatic) approximation. It holds when ξ_coh is *small* compared with the length over which Δ(r) varies, and fails in the opposite limit, where the gap is self-averaged and P_Δ → δ(Δ − Δ̄). "Exceeds … only partially" states neither limit. L^nor_loc (a local normal-state loss) is not defined anywhere. *Fix:* state both limits and define L^nor_loc as the loss of the cell region with gap Δ, or drop the second form.
- **(6.1).** Correct. The ZrTe₅ number uses v_F,x and an isotropised ε. With an anisotropic mass the Rydberg needs the (v_F,i, ε_ii) average, so keep it [E].
- **(13.1).** Si: k₀ = 0.85·2π/a = 1.94 keV. g-process at 2k₀ = 3.9 keV, or |2k₀ − 4π/a| ≈ 0.7 keV in the G-sum. f-process at √2k₀ = 2.7 keV.
- **(17.1).** Verified. Rename "uniform cylinder" to "cylindrical charge shell" (I₀K₀).
- (1.1), (3.1), (5.1), (7.1), (12.1), (14.1)–(14.2), (15.1), (16.1), (18.1), (19.1), (20.1), §21 and (9.1) are checked in the table and in §1. No further error.

## 4. Scope 4: CLOSED-AS-EXACT-GAP rows
| Row | Single missing step? | Spec (what / approx / method+convergence / pitfalls) | Verdict |
|---|---|---|---|
| LE-99 two-magnon | yes (Γ^{(4m)} for a target + ladder solve) | complete | STANDS. Add pitfall: identical-boson pair counting (k ↔ q−k, ν = ν′: factor ½ / symmetrised basis). Dyson–Maleev vertex non-Hermitian, so use HP in the linear solve |
| LE-102 Dirac α̃ ≳ 1 | yes | **insufficient on k-resolution** | STANDS WITH CORRECTION. For ZrTe₅, a_D = 2v_F²ε_bg/(αΔ_D) ≈ 2×10³ Å (1/a_D ≈ 5×10⁻⁴ Å⁻¹). "60³ inside Λ_D" (Δk ≈ 8×10⁻³ Å⁻¹) and "ab initio k ≥ 24³" cannot resolve the bound series that the stated convergence target (Ry_D to 5 %) requires. Spec must (a) treat |√𝓈 − 2Δ_D| ≲ 10 Ry_D analytically (Elliott/Sommerfeld, §6 (ii)) and use BSE only away from threshold, or (b) use a log-graded grid down to ≲ 0.1/a_D. Also "non-perturbative (self-consistent GW + BSE)" vs the method "G₀W₀ + BSE": choose one and state that neither is controlled at α̃ ~ 1 |
| LE-107 (Al) | yes (one primary citation) | not a compute row; fine | STANDS. Tag fix V12 |
| LE-115 non-rigid Wannier | yes (𝔯_W) | nearly complete | STANDS WITH CORRECTION. Missing pitfall: (W.5) uses the *bare* ∇_RV between many-body states. A static DFPT dvscf (ε⁻¹(ω = 0)-screened) is the wrong screening for transitions at ω_e = 20–100 eV. Specify bare ∇V with RPA+LFE screening at ω_e (as for the (p, ω_e) lines), or justify the static vertex. Otherwise 𝔯_W mixes screening and non-rigidity |
| LE-117 longitudinal | yes | complete (routes i–iii) | STANDS |
| Remainders: LE-97 magnitude, LE-104 O(Δ²/q²v_F²) and KK tail, LE-109 impurity band, LE-110 depolarisation size | yes in each | complete. LE-110 needs a closed-access ε_in (stated) | STAND |

## 5. Scope 5: proposed LIMITS rows
| Row | Source quote [FT] | Validity / leading correction | Verdict |
|---|---|---|---|
| CW4-a | 2609.06423 Eq. (9) is the full-ε_BCS rate. Eq. (7) coherence factor = M₃ ✔ | correct (O(Δ²/q²v_F²); KK spread) | STANDS |
| CW4-b | 1604.06800 Eqs. (16)–(17) ✔ (E-function form verified) | correct | STANDS. Write "Allen 1971 via 1604.06800 Ref. [29]" |
| CW4-c | none | excitons; inter-subband | STANDS |
| CW4-d | 1912.13484 Eqs. (2.7)–(2.8) (Wannier boost) ✔ | add "absolute (not relative) W_𝒲/ω_cv bound" (V6) | STANDS WITH CORRECTION |
| CW4-e | cond-mat/0108424 Eqs. (2.4)–(2.5) ✔ (FM/SU(2) limit only; the AFM weight is CW4's own) | correct | STANDS |
| CW4-f | 2504.02927 Eq. (26): S_n ∝ P_T^{ij}χ″_ij ✔ | correct | STANDS |
| CW4-g | 2208.05967 Eqs. (6), (10), (12); 1509.01598 Eqs. (3.13), (3.17) ✔ | Status should read "DERIVED; source Eq. (6) wrong by μ_eχ/(4E_r) (CONFIRMED)" | STANDS |

## 6. Required edits before acceptance (summary)
1. OC-5 (LB1-6): replace the OPW numbers by the q- and direction-dependent range of V5.
2. OC-6 (LB1-8): change "Hermitian ordering" to "ket-side ordering", and use the absolute error bound (V6). The same bound applies in §19 and CW4-d.
3. OC-7 (LB1-13): keep "impact on 2401.11971's limits UNRESOLVED" (CRDM, v_χ → 1). (18.1) is density-row only.
4. §11 and IF-CW4-2: Al tag [E], not [D].
5. §20: Kanamori–Tachiki is cited for the resonance shift.
6. OC-11: retarget to R14 WP8-U-table-v2.csv (ZrTe₅ l.1543, Al l.1619, Nb `Delta_BCS_E` l.2395); note that the [52] v_F values are genuine.
7. OC-1 and CW4-b: Allen attribution via 1604.06800.
8. §2 validity clause; §13 q values; §17 shell kernel; §0 counts (16 CLOSED; 4 with remainders).
9. LE-102 spec: k-resolution / analytic threshold; LE-115 spec: screening of the vertex; LE-99: pair-counting pitfall.
Everything else stands as written.
