# R16 verification VER-CW7 (hostile, isolated): returns/R16/CW7.md (excl. §12), WP8-U-v2.md + table v3, WP8-F-v2.md

Read: the three returns, code/CW7/* (all), referees/R14/REF-WP8-U-A/-B, REF-WP8-F-A/-B, returns/R8/WP6-v3, WP4-v3, WP0-v3 (greps at cited items),
returns/R14/GAP-EF (§1, §3 table), WP5-AUD (§5.2), CONVENTIONS, LIMITS (L4, L16), state/LOOSE-ENDS. Not read: referees/R16, other R16 returns, briefs
(except this one), log/. Full texts fetched (lit.py → literature/papers-r16-VER-CW7/, PDFs/HTML deleted, pdftotext `.txt` kept): 2008.08560, 1910.10716,
1910.02091, 2507.07119, 0903.1445, 1607.08146, 1003.5140, 2205.02250, 1607.04560, 2007.10584, 1411.0106, 1411.5947, 1908.06755, 1901.07569.
**checks.py rerun: 32/32 PASS, 15.4 s** (reproduced). Own checks (numpy/sympy, < 1 min each) are quoted inline. Pages = PDF pages.

## Verdict table (scope 1–3; one row per item)
| # | Item | Verdict | Reason (§ below) |
|---|---|---|---|
| V1 | LE-19 WP8-U-v2 + table v3, closing table (25 rows) | STANDS WITH CORRECTION | 23/25 rows resolve their R14 item; A-G8/B-(e)(ii) and B-(e)(v) are only partly applied (55 [E]-evidence screen_S rows, 13 duplicated keys) (§A) |
| V2 | LE-21 WP8-F-v2, closing table (43 rows), "(prov.)" lifted | STANDS WITH CORRECTION | 41/43 resolve; A-§E(c) not done as requested; C20 does not test what L-F3 certifies; MAG nuisance width inconsistent with CW7 §7 (§A) |
| V3 | LE-152 Theorem G8′ (i)–(iv) | STANDS WITH CORRECTION | Proof sound (bipolar, finite-constraint Slater duality, Winkler atoms). (iv) needs the lab-frame ball; C3 is tautological (finite-LP duality); (c) signed φ needs (H4) on {φ > 0} (§B1) |
| V4 | LE-153 (CW7-153a,b), P_casc | STANDS WITH CORRECTION | Recursion and properties correct; **the deliverable solver is wrong for θ_ii > 1** (ΣP = 0.953 at θ_ii = 3/2); "exact for N < N_z" is false as worded (§B2) |
| V5 | LE-154 (CW7-154) and λ_i ≤ (2ω_max/Δ_i)ϱ_− | **FALLS (as stated)**; corrected form STANDS | Counterexample: leak 4.9×10⁻⁴ with [A_X+]_− ≡ 0 (bound 0). Correct ϱ_− uses max([A_X+]_−, [A_X0]_−) (§B3) |
| V6 | LE-155 scalar FOM (CW7-155a,b), sum rule | STANDS WITH CORRECTION | Operator, charge-conservation and ℓ = 1 argument correct. Sum rule is one-body only and **diverges** for Coulomb V (⟨r⁻⁴⟩_1s = ∞); polar mixing term omits the transverse propagator of WP0-v3 (3.6) (§B4) |
| V7 | LE-156 r_2m, magnon WP6 row | STANDS WITH CORRECTION | r_2m = ΔS(1+ΔS)/(S(1+2ΔS)) re-derived; ΔS = 0.078 reproduced. r^M is underived and contradicts WP8-F-v2 §4; owed WP4 text is self-contradictory (§B5) |
| V8 | LE-157 SC one-sided row, y ≲ 3.5 mask | STANDS WITH CORRECTION | Sign, widths 0.09/0.03 and masking logic correct (WP4-v3 K34 table). "WP6 does not carry I12" is false as worded; mask column unspecified (§B6) |
| V9 | LE-160 r_mat rule, CONVENTIONS row 29 | STANDS WITH CORRECTION | Both extremal statements need same-sign elasticities (and r_mat ∈ [0,1]); with opposite signs the conservative r flips (§B7) |
| V10 | LE-176 soft-mode ε₀ data + insensitivity | STANDS WITH CORRECTION | All three quotes CONFIRMED. PbTe shift is 2.8–5.6% (">1000" is a bound), PbS 10.3% not "≤ 10%"; 0903.1445 χ⁻¹ is a fit parameter (§B8) |
| V11 | LE-177 cosmogenics data + activity formula + spec | STANDS WITH CORRECTION | All rates CONFIRMED verbatim. CaWO₄ ³H is inferred, not "identified/observed"; Ge L-lines (1.1–1.3 keV) lie above the sub-keV ROI (§B9) |
| V12 | WP8-F-v2 derived changes (2.3a′), (2.3c), 2W, (2.7′), POL sensitivities, FM edge, floor, Migdal factors | STANDS | (2.3a′) and (2.3c) re-derived by hand = 2205.02250 Eqs. (30), (31) [FT p.8]; ∂ln𝓘/∂lnZ* = 1 + ε_∞/ε₀ = 1.844 re-derived; 0.93/0.72, 17.3 MeV, 137 MeV, 9.7–10.3 keV recomputed |
| V13 | Owed corrections list (CW7 end; 11 targets) | STANDS WITH CORRECTION | Targets exist (WP6-v3 l.321, l.363, l.450, l.584–588; WP4-v3 l.99, l.117; CONVENTIONS row 29 free). Items 3 (WP6 §4.2), 4 (magnon r^M), 5 (WP4 text), 7 (row 29) must be amended per V5, V7, V9 |
| V14 | Status upgrades ("(prov.)" lifted; IF-U5 closed; GaAs S2 PASS; NiPS₃/h-BN/c-BN/PE → COND; c_s FALLS for SiC) | STANDS | WP5-AUD l.186 releases the rows; 2507.07119 p.1 "a 4.3 g GaAs (GaAs-1) crystal, operated at approximately 10 mK"; 1910.02091 l.67/702 |
| V15 | New exact gap G-F6 (WP8-F-v2 §7) | STANDS WITH CORRECTION | Spec is wrong in kind: unpolarized nuclear spins make the SD one-phonon term incoherent (§C) |
| V16 | Proposed LIMITS rows (CW7 L-H1–H4; WP8-U L4 ✔, LU2′, LU4′; WP8-F L-F1–F3) | STANDS WITH CORRECTION | L-H1, L-H3 cite [ABS] only; L-H1/L-H2/L-H3 leading corrections need V5/V4/V6 fixes; L-F3 "CROSS-CHECKED (C20)" leans on a tautology (§D) |

## A. Closing tables (scope 0)
**WP8-U-v2 §9 vs REF-WP8-U-A §G and REF-WP8-U-B "Required changes".** Each row checked against the referee text and against the v3 CSV / build_v3.py.
- Resolved as claimed (23): A-G1–G7, A-G9, A-G10, A-C3 (extract: JVASP-1174 `dfpt_piezo_max_dielectric_electronic` = 3097.93, `dfpt_piezo_max_dielectric` = na,
  max_ir_mode 1.77 — CONFIRMED), B-1–B-10, B-C7, B-C8/C9, B-V2, B-V7/V15. V2 implementation: build_v3 derives the 14 GAP rows from the cached extract (gap < 0.05 eV or
  IR < 20 cm⁻¹), so CW7-C30 is a real check (not self-referential). SiC LST (C28) re-derived from 2008.08560 Table I [FT p.5]: 4H ∥ (119.5/97.0)² = 1.5177 vs
  10.32/6.8 = 1.5176; first member of each TO/LO pair = A₁ (∥). A-D7 (3C ε_eh): the measured 6.9 eV row (2610.16949, R14) makes §0 row 4 defensible.
- **A-G8 / B-(e)(ii) "replace [E] screening evidence by [UNVERIFIED]": PARTLY APPLIED.** Of the 154 new `screen_S*` rows, **55 still carry "[E]" as evidence**
  (e.g. CSV l.3076 CaF₂ S3 "COND: plausible [E]", l.3103 Bi₂Se₃, l.3131 PE S1), and **13 (material, screen_S*) keys have two rows with contradictory values**
  (SiC-3C/4H/6H, GaN, AlN, GaSb, α-SiO₂, ZnO, MgO, CaF₂, MgF₂ S1: rename "PASS … [E]" + supersession "COND"; GaAs S1/S2). Only the "supersedes" note
  disambiguates. Correction: drop or retag the renamed [E] rows (the §2 rule says such entries "read [UNVERIFIED]"), or state the "last superseding row wins" rule
  in the CSV header text of §0.
- **B-(e)(v) "TeO₂ ρ is a DFT proxy": PARTLY APPLIED.** §4.1 still prints TeO₂ 5.92ᵈ in the ρ_T column; the referee asked for a `*_DFT`-proxy flag.
- Minor: §0 row 8 says "V1–V5", §1.3 defines V1–V6.
- **Trace (≥ 20 rows).** Frame: the 314 new rows (CSV l.2999–3312); Python `random.seed(16071)`, `random.sample` of 24. Lines: 3006, 3008, 3061, 3076, 3103,
  3104, 3110, 3113, 3117, 3131, 3161, 3172, 3183, 3195, 3206, 3208, 3228, 3249, 3252, 3266, 3276, 3285, 3290, 3295. Traced: 10 renames → the v2 `screen_C*` row
  (verbatim); 3161 PbS "< 0.00553" → v2 activity; 3172 C ε_∞ 5.7 → 1901.07569 Table I p.2 "Relative permittivity 5.7 11.7 16.0" [FT]; 3183 KTaO₃ → extract IR 2.19;
  3195 → 1910.02091 l.67, l.702–703; 3206 → REF-WP8-U-A C5 quote; 3208 Si ⁷Be → 2007.10584 p.1 "(8.1 ± 1.9) … (9.4 ± 2.0)"; 3266/3276/3285/3290/3295 →
  GAP-EF §3 table rows Al₂O₃, C, MgO, NaCl, CaF₂ (all five values and bands identical); 3 GAP rows → rule. **0 value mismatches**; defects: 3008 (PASS [E],
  superseded by a conflicting row), 3076, 3103, 3131 ([E] evidence). Independent verbatim check: 2997 v2 rows = first 2997 v3 rows, 0 differences.
- Outside the sample, wrong note: CaWO₄ `cosmo_identified` says "179Ta, 181W and the associated 3H **observed** in CRESST data"; 1908.06755 p.4: ³H "is hard to be
  observed experimentally for CaWO4 in CRESST … the observed ¹⁸¹W should be accompanied by a ³H component". Write "³H inferred".

**WP8-F-v2 §9 vs REF-WP8-F-A (F1–F19, §B, §E) and REF-WP8-F-B (1–13).** Resolved as claimed: all F-rows, B-1–B-13, AUD F-a…F-i (checked against WP5-AUD §5.2).
- **A-§E(c) not done as requested**: the referee asked for per-branch K(ω_Lν; m_χ) "for sapphire at 2–3× the edge"; CW7-C23 evaluates ln(2m_χv_max²/ω) at
  1 MeV, ≈ 30× the 112 meV-branch edge (2ω/v_max² = 32 keV). A-§E(a) is done only for the angle average (C21), not for S_LO itself (my hand derivation below covers it).
- **CW7-C20 does not test the claim it is cited for**: it puts Z_κ² outside the k-integral (the R13 form A-F14(i) rejected) and is a sympy identity of a
  hand-written expression. The physics stands (re-derived: per mass Σ_κZ_κ²A_κ²/(A_κ³m_u³)·A_κ/M_cell ∝ Σ_κZ_κ²/A_cell), but C20 is not an independent route.
- **MAG nuisance inconsistency**: WP8-F-v2 §4 "residual M with r = r_2m/(2S)"; CW7 §7 owed WP6 row "(b) r^M = max(ΔS/S, r_2m/(2S))". One must go; neither is derived.
- Minor: "𝓡 vs ℛ confusable" (REF-B §9) not addressed.

## B. New derived results (scope 1, 3)
**B1. LE-152 Theorem G8′.** (i) Correct: R is the adjoint of g ↦ R*g; the image of the weak-* compact probability base excludes 0 (R[δ_w] ≠ 0), so the generated
cone is closed; bipolar gives the dual-cone test. (ii) The dual follows from the Lagrangian with **finitely many** (N_b) constraints; Slater at F = 0 gives zero gap —
the "semi-infinite LP" difficulty is on the dual side only, as stated. (iii) Bauer + Winkler (≤ N_b atoms) correct after restriction to supp φ.
(iv) Correct only for the **lab-frame** ball: in the galactic frame 𝔎_i depends on |w − v_E|, not |w|; write "(I) in the lab frame, F the lab-frame measure".
(c) signed φ: (H4) must hold on {φ > 0}, else Φ is unbounded. Checks: C1/C2 are fine; **C3 is tautological** (primal = dual holds for every finite LP; it does
not probe the semi-infinite statement or grid refinement); C4 is linearity of an average. Spec: sufficient (what, level, method, cost, convergence by
column generation with the dual certificate, pitfalls). Novelty rated UNRESOLVED on [ABS] reads — agreed.

**B2. LE-153.** (CW7-153a) is the correct first-step equation for the stated branching process; differentiating at z = 1 reproduces (EF3)–(EF4) (C5 to 10⁻⁹).
(b) threshold (1 + θ_ii)E_g correct. **Code defect (blocking for the spec):** `CascadeGF.solve_gf` computes the two-fold convolution C2[q] only inside the
loop n ≥ nth, i.e. for q ≥ nth − nG; for θ_ii > 1 the entries q < (θ_ii − 1)/h stay 0 although G = 1 there. Rerun at θ_ii = 3/2 (λ = 3.55, w = 0.054, X = 8,
h = 0.02): **ΣP = 0.9529, mean 1.970 vs the moment recursion 2.096** (moments_fast is unaffected because m = 0 below threshold; its θ_ii = 3/2 slope reproduces
GAP-EF's 2.056). θ_ii = 3/2 is GAP-EF's (K1) variant and its Si re-calibrated row, so the spec's "5 θ values × 27 survivors" would use a wrong solver.
Fix: precompute C2, C3 for all q < nth − nG with G = 1; add a θ_ii = 3/2 normalisation check. Also (CW7-153b) "exact for N < N_z" → "exact if P(N) = 0 for
N ≥ N_z" (aliasing adds P(N + kN_z) otherwise); the code docstring has it right. The solver is the symmetric-DOS case only (docstring); the return's t/t̄
notation implies the general one.

**B3. LE-154 — FALLS as stated.** The first inequality of (CW7-154) drops the ΔP < 0 region. With P_{X0} = P_{X+} + |ΔP| there,
P_{X0}A_tot + ΔP·A_{X+} = P_{X+}A_tot + |ΔP|A_{X0}, whose negative part is |ΔP|[A_{X0}]_−, not |ΔP|[A_{X+}]_−; for an interior bin ΔP takes both signs (P(i|E) rises
then falls), so this region always exists. Counterexample (step bin [2ε_eh, 3ε_eh), Si ε_eh, ω_Q; A_tot ≥ 0; A_{X+} ≥ 0 everywhere with a narrow peak above A_tot at the
lower edge, so A_{X0} = A_tot − A_{X+} reaches −0.053): **negative part 4.9×10⁻⁴, (CW7-154) bound 0**. CW7-C11 places its negative piece only in the ΔP > 0 window
and cannot see this. **Correction:** ϱ_− ≡ sup max([A_{X+}]_−, [A_{X0}]_−)/⟨A_tot⟩_i; then λ_i ≤ (2ω_max/Δ_i)ϱ_− holds (lemma and TV ≤ 2 under (M) unchanged; both
re-derived). The owed WP6-v3 §4.2 replacement text must not be applied as written. The remedy row (r ≤ (2ω_max/Δ_i)ϱ with |A_{X+}|) is correct.

**B4. LE-155.** ψ̄ψ → 1 − p²/2m_e² re-derived (|φ|² − |χ|² with FW normalisation); 𝒯_e(k) symmetrisation, n = k·j/ω, the longitudinal mixing algebra and
the point-group argument (R̃_{𝒯j}(0,ω) is an invariant polar vector; T_d, D_3d non-polar; C₆ᵥ, C₃ᵥ polar) are correct; (CW7-155b) spin factor (2π/V) correct.
Corrections: (1) **Sum rule.** Σ_f(E_f − E_i)|A_fi|² = ½⟨[[A,H],A]⟩ with p² = 2m(H − V) gives 2m⟨(∇V)²⟩ — re-derived — but only for a **one-body** V (e–e terms
give cross commutators for 𝒯 = Σ_i), and for the bare Coulomb nucleus ⟨(∇V)²⟩ ∝ ⟨r⁻⁴⟩ **diverges** for any state with s density at the nucleus (sympy:
4Z⁵/ε as the cutoff ε → 0, hydrogenic 1s). "Core-dominated" understates this; pitfall (3) (valence-restricted sum rule as a check) is unusable all-electron
(Si valence has 3s character) and pseudopotential-dependent otherwise. C12/C13 test smooth potentials only. A usable check is the exact identity
⟨c|p²|v⟩ = −2m_e⟨c|V|v⟩ (c ≠ v, same H, V possibly nonlocal). (2) **Polar mixing term.** WP0-v3 (3.6) uses the full photon propagator 𝒟^γ_{μν}; CW7 keeps only
the Coulomb (longitudinal) piece. For polar groups add R̃_{𝒯j}𝒟^γ_TR̃_{j𝒯} (non-polar result unaffected, since R̃_{𝒯j}(0) = 0 for all components).
(3) The n_e row is suppressed by v_DM/v_e (≈ 0.1–0.2 in amplitude before 1/|ε|), not by v_DM alone; label it so. Literature: 2106.12586 [ABS] — prefactors uncompared.

**B5. LE-156.** W_⊥ = S(1 + 2ΔS), W_∥ = ΔS(1 + ΔS) (Wick, same-sublattice ⟨aa⟩ = 0) re-derived; C14 ΔS = 0.0782 ✓; r_2m(½) = 0.1458 ✓. Corrections: r^M (owed row)
is an unmotivated [E] choice and conflicts with WP8-F-v2 §4; "(a) σ_ln = r_2m-weighted 0.5" is undefined. r_2m is an equal-time, q-integrated local ratio, not the
quantity 1/(2S) of WP4-v3 (an expansion parameter), so "far below the heuristic" compares different objects. Owed WP4 text "1/(2|𝐒_j|) ≪ 1: … **1** for |𝐒| = ½"
is self-contradictory: write "1/(2|𝐒_j|): 0.2 for YIG; = 1 at |𝐒| = ½, where LSWT is qualitative only".

**B6. LE-157.** WP4-v3 K34 table (l.251–254): |δL/L| KK-∞ 0.53/0.16/0.04 and cut 0.30/0.07/0.01 at y = 3/5/10, so σ_BCS = 0.09, 0.03 ✓; sign (lowers L) ✓;
masking a non-negative signal is conservative ✓; profiled ≥ θ = 0 limit is automatic for s(θ) ≤ s_c (C15 trivially). Corrections: WP6-v3 l.450 **does cite I12**;
what it lacks is I12's directives ("one-sided (downward) and must exclude … y ≲ 3.5", WP4-v3 l.621). Say "carries I12 by reference but not its one-sided/exclusion
rule". The mask threshold 0.3 lands at y ≈ 3 on the cut column (the central) and y ≈ 3.5–4 on the KK-∞ column; state which column defines the mask (the KK-∞ one
gives the stated y ≲ 3.5). σ_BCS is the edge value (q = ω/v_max) used for all q — conservative, say so. C15 mixes 2.303 (Poisson) and 2.71 (Wilks) thresholds.

**B7. LE-160.** (a), (b) correct for s_A(1+δ)^θ_A, s_B(1+δ)^θ_B with **equal-sign** elasticities and r_mat ∈ [0,1]. A method nuisance (XC, 𝒳 rung) can move two
materials' FOMs in opposite directions: then Var(s_A + s_B) = δ_A²s_A² + δ_B²s_B² + 2rδ_Aδ_Bs_As_B is maximal at r = 0 (over [0,1]) and the ratio variance at
r = 1. Row 29 text must add "for nuisances whose elasticities have equal sign; otherwise use the sign-dependent extreme". C16 tests equal positive widths only.

**B8. LE-176.** [FT] CONFIRMED: 0903.1445 Table 1 p.6 "a = χ⁻¹ … SrTiO₃ 5×10⁻⁵, KTaO₃ 2×10⁻⁴", obtained "by measuring the polarization in an electric field at
0.3 K and fitting" (a fit parameter of the equation of state, so ε₀ ≈ 2×10⁴ is model-inferred — keep [FT], say so); 1607.08146 p.1 "εr = 23, 000 at 4K",
p.2 "27,400"; 1003.5140 p.11 "huge dielectric constant of PbTe at low temperatures ( > 1000)". ∂ln(1/ε_∞ − 1/ε₀)/∂lnε₀ = ε_∞/(ε₀ − ε_∞) re-derived.
Corrections: PbTe "2.8%" → **2.8–5.6%** (DFPT 499 → 1000 … ∞; ε_∞/ε₀^{DFPT} = 0.053); PbS "≤ 10%" → **10.3%** (C17 prints 0.103). PbS/PbSe are not quantum
paraelectrics and pass V2 (IR 66.8/46.1 cm⁻¹); "unusable" is asserted, not shown (harmless given the insensitivity). C18 substitutes the conclusion (tautological).

**B9. LE-177.** CONFIRMED verbatim: 2007.10584 p.1 (112 ± 24, 8.1 ± 1.9, 43.0 ± 7.2; 124 ± 25, 9.4 ± 2.0, 49.6 ± 7.4); 1607.04560 p.2 (82 ± 21, 2.8 ± 0.6,
4.6 ± 0.7, 106 ± 13, "lower limit … of 74"), p.21 (90% C.L.), p.28 Table 5 (82 ± 12, 106 ± 10, 202 ± 16, 84 ± 3 (sat)), p.19 (27.7–210); 1411.0106 Table 6 p.15
(all eight); 1411.5947 Table 4 p.10 (182.0, 2.39, 0.81, 1.01 µBq/kg, ACTIVIA). Activity formula and ³H sub-keV fraction re-derived: Fermi-corrected ³H spectrum
gives f_{<1 keV} = 0.0892, so 0.169 and 11.06 /(kg·d·keV) ✓. Corrections: (1) 1607.04560 p.3 "L- and M-shell captures will produce weaker lines at approximately
1 and 0.1 keV" ✓, but its p.10 puts the Ge L-lines at **1.1–1.3 keV** (⁶⁵Zn, ⁶⁸Ge), above the < 1 keV ROI: only M-lines (and resolution tails of L) enter.
(2) CaWO₄ ³H inferred, not identified (§A). Spec: sufficient, except no convergence criterion for the Geant4 route (state the statistical target).

## C. Exact-gap rows (scope 4)
Only new one in scope: **G-F6** (WP8-F-v2 §7; LE-159 excluded). The spec "reuse WP2-v3 (2.2) with c_κ → spin weights" is wrong in kind: for unpolarized nuclear
spins ⟨𝐒_κ⟩ = 0, so the coherent one-phonon amplitude Σ_κ c_κ e^{iq·r_κ}(q·e_κ) vanishes for the spin-dependent operator; only the incoherent (spin-variance)
structure factor ∝ Σ_κ x_κ(J_κ+1)/J_κ ⟨S_{p,n}⟩² survives (incoherent form as WP8-F-v2 §2.4(a), with e^{−2W}). The missing step is therefore two steps (per-isotope
⟨S_{p,n}⟩ from shell-model full texts, and the incoherent SD phonon/impulse response), and the spec lacks approximation level, convergence and this pitfall.
Status: GAP stands; spec insufficient.

## D. Proposed LIMITS rows (scope 5)
| Row | Source quoted from FT? | Validity / leading correction | Verdict |
|---|---|---|---|
| L-H1 | No: 1403.4606, 1703.09168 [ABS] (NR stream method only) | add "lab frame for (I)"; leading correction must cite the corrected (CW7-154) | STANDS WITH CORRECTION |
| L-H2 | GAP-EF internal; 2004.10709 not re-read here | add "solver valid for θ_ii = 1 until the C2/C3 fix" | STANDS WITH CORRECTION |
| L-H3 | No: 2106.12586 [ABS] | add "one-body V; sum rule finite only for regular V"; polar mixing incomplete (B4) | STANDS WITH CORRECTION |
| L-H4 | internal (WP4-v3 [2.4]) | correct; leading correction O(1/S²) plausible | STANDS |
| L4 ✔ (ex-LU1) | 2008.08560 Table I p.5 [FT] — verified; LST 1941 [UNVERIFIED] | ≤ 1.2% verified (C28 re-derived) | STANDS |
| LU2′, LU4′ | 2004.10709 (via R14 referees); 2008.08560 / 1901.07569 T_D — 2008.08560 values verified (1430/1200 K) | correct as ESTIMATED / data cross-check | STANDS |
| L-F1, L-F2 | 2205.02250 Eqs. (27), (30), (31) p.8 [FT] — verbatim; 1807.10291 via R14 | correct, incl. Θ(ω_LO − ω) cut | STANDS |
| L-F3 | 2011.09496 Eq. (6) via REF-WP8-F-A [FT] | correct; "CROSS-CHECKED (C8, CW7-C20)": C20 is not an independent route (§A) — cite the R14 referees' recomputation | STANDS WITH CORRECTION |

## E. Claims that a published paper/database is wrong (scope 2)
| Claim | Full text checked | Rating |
|---|---|---|
| 2008.08560 Table I n_e = 2 e/atom × N (C, Si, SiC) | p.5: N 1.76/0.5/0.96, n_e 3.54/1/1.95; ħω_p 22/16.6/22.1. 3.713×10⁻¹¹√n: 1.0e23 → 11.7 eV ≠ 16.6; 2.0e23 → 16.6 | **CONFIRMED** |
| 2008.08560 diamond ħω_p = 22 eV suspect | 3.54e23 → 22.1 eV (2 e/atom); 4 e/atom → 31.2 eV | **CONFIRMED** (internally); physical value not read |
| 2008.08560 "cs" undefined; SiC values not an average phonon speed | no definition anywhere in the text (grep); p.5 only "cs (m/s)" | **CONFIRMED** (undefined); "> c_L" rests on DB moduli |
| 1910.10716 Table I c_LA (GaN, AlN, ZnO, α-SiO₂, NaCl) suspect | p.2 table, App. A3 definition (DFT ω_LA/q) | **UNRESOLVED** (no measured C_ij read; "suspect" is the right word) |
| 1910.02091 Table 1 caption "band gaps" loose (Δ = half-gap) | l.67 "2∆ is the band gap"; l.417; l.694 caption; l.702–703 "23.6 meV … ∆ = 11.8 meV" | **CONFIRMED** |
| 1901.07569 Ge E_g = 0.54 eV "matches no tabulated gap" | 1901.07569 not contradicted internally; no second source read | **UNRESOLVED** (return keeps it [UNVERIFIED] — correct) |
| JARVIS GaAs "ε₀ = 3098" is the electronic field | cached extract JVASP-1174 (above) | **CONFIRMED** |
| 1708.08929 Dirac rates ×ε_bg too large | carried from R14 (REF-WP8-F-A §C), not re-read here | not rated |

## F. Checks
32/32 reproduced. Tautological or weak: C3 (finite-LP duality), C15 (s(θ) ≤ s_c), C16, C18, C20, C27 (solve-for-the-symbol), C11 (constructed to avoid the B3
region), C5–C8 (θ_ii = 1 only), C32 (agent-written JSON; my 14 lit.py fetches of cited IDs all succeeded and matched the cited content).

## Required corrections (summary)
1. LE-154: ϱ_− with max([A_{X+}]_−, [A_{X0}]_−); amend the owed WP6-v3 §4.2 text and L-H1's leading correction; add a ΔP < 0 test to C11.
2. LE-153: fix `solve_gf` for θ_ii > 1 (C2/C3 below threshold), add a θ_ii = 3/2 ΣP = 1 check; reword "exact for N < N_z".
3. LE-155: one-body hypothesis; sum rule divergent for Coulomb V (drop pitfall (3) or restrict to regular pseudopotentials); full 𝒟^γ in the polar mixing term.
4. LE-156: one r^M (WP6 row ↔ WP8-F-v2 §4), derived or tagged [E]; rewrite the owed WP4 sentence.
5. LE-157: "cites I12 but not its directives"; name the K34 column that defines the mask.
6. LE-160 / CONVENTIONS row 29: same-sign elasticity hypothesis.
7. LE-176: PbTe 2.8–5.6%, PbS 10.3%; χ⁻¹ is a fit parameter.
8. LE-177 / CSV: CaWO₄ ³H "inferred"; Ge L-lines above 1 keV.
9. Table v3: retag/drop the 55 [E] screen_S rows and resolve the 13 duplicated keys; TeO₂ ρ DFT-proxy flag; V1–V5 → V1–V6.
10. G-F6: incoherent SD structure factor; complete the spec. 11. L-H1/L-H3: full-text sources or [ABS]-level status. 12. L-F3: drop C20 as the cross-check.
