# VER-FBC-v2: isolated verification of R19/FBC-v2 (full-band cascade, Si)

Verifier: Claude (LLM), isolated. Read FBC-v2.md, FBC.md, REF-FBC-A/B, code/FBC (checks.py, analyze_v2.py, run_mc.py,
summary_v2.json, all mc_*.npz configs) and the NF source text (book/sources/review-ch18/2610.16949). Nothing edited except
this file; no commit. Reproduction runs used a scratch copy of run_mc.py writing only to the scratchpad (1 BLAS thread per
process, 4 processes). CPU used about 8 CPU-min.

## 1. checks.py: 15/15 PASS (36 s)
C9 (production `mc.Model.run` with book kernels) TV 0.0041/0.0029/0.0025/0.0070 at 3×10⁴ events; C9ref ≤ 0.0023;
C11 disjoint random seed subsets, max TV 0.0204, max TV/noise 2.70 over 73 ω × 2 seeds; C12 Var(60 eV) −0.329 (X = 46)
vs 1.810 (fixed), F(50→100) 0.382 at NZ = 32 vs 0.1142, ε 3.7494 at NZ = 64, X = 90.
- C9 is now a real test of the production event loop (competition, phonon bookkeeping, energy identity, relabelling).
  It swaps out `sample_ii`/`sample_pair`, so the full-band final-state tables are still covered only by C5/C10. Adequate.
- C11 is now an absolute MC check (seed sampling + cascade). Its docstring still says "samples 0-9999 / 10000-19999";
  the code uses disjoint slices of a fixed random permutation (correct, but fix the docstring).
- C12 documents the casc18_3 failure and the fix; casc18_3.py itself is unchanged (book-side fix, flagged in IF-FBC-8).

## 2. The seed-ordering bug
- Confirmed. In seeds_refit_n12_m100_q4.npz at ω = 5 eV the first 10⁴ records have ⟨E_e⟩ = 1.891 eV against 2.068 eV for
  the last 10⁴ (P(E_e > 2 eV) 0.459 vs 0.555): the stored order is q-correlated.
- Effect on the first v2 pass (non-`_p` files vs `_p` reruns, P(≥2, 5 eV)): c_0_FP_050 0.076 → 0.089, c_lo 0.149 → 0.160,
  c_hi 0.029 → 0.033, v2h30 0.066 → 0.075, v2e052 0.131 → 0.126. Shifts up to 17 %, so the fix mattered.
- Fix: run_mc.py takes `perm = default_rng(12345).permutation(ntot)[off:off+nev]`. Correct; halfA/halfB use off = 0/10⁴
  (disjoint). analyze_v2.py overwrites `heavy_*` from the `_p` file for every 10⁴-event run and warns otherwise.
- v1 unaffected: every v1 P(N) run used nev = ntot (refit 20 000/20 000; scissor 10 000/10 000). The only partial run,
  mc_hefree (nev = 4000), ran on coarse ω and v1 used only its one-sided ε/F (its P(N) is not in summary.json's envelope).
- v2 unaffected: v2primary, v2rpaw, v2fp, v2thr050/100 used all 20 000; all 10⁴-event P(N) entering summary_v2 come from
  the `_p` reruns; ε/F/heat come from one-sided runs that use no seeds; photon/DM 20³ runs draw from share histograms.

## 3. Spot reproductions (fresh RNG seed 7; c_hi also on the disjoint seed half, off = 10⁴)
| quantity | v2 | verifier |
|---|---|---|
| primary ε_eh, F_eh | 4.149 ± 0.004, 0.114 ± 0.002 | 4.146 ± 0.004, 0.112 ± 0.002 |
| primary P(≥2, 5 eV) / overcount / ⟨N⟩10 | 0.097 / 10.3 / 2.381 | 0.097 / 10.3 / 2.383 |
| primary heat / pairs at 100 eV | 71.6 % (27.7 + 43.9) / 28.4 % | 71.6 % (27.7 + 43.9) / 28.4 % |
| c_hi ε, P(≥2, 5 eV), overcount | 4.729, 0.033, 30.7 | 4.735, 0.030 ± 0.002, 33.6 |
| W_ii × 3 below 4.5 eV: ε | 3.728 | 3.739 ± 0.003 |
| JR, no exchange (R_x ≡ 1): ε | (v1 rx0: −0.10) | 4.028 (−0.12 vs v2 primary) |
| FP phonons (e × 0.52, h × 3.0), R_x v2: ε | 4.234 | 4.242 |
| FP phonons, no exchange: ε | not run | **4.106** |
All tabulated v2 numbers I cross-checked against summary_v2.json (§2 R_x table, §3 phonon table, §5 bands, §6 as-is and
matched tables, §7 budget, photon_dm) agree to the quoted digits. Rates: rpaw/cap = 0.62–0.65 at 2–3 eV and 0.37–0.46 at
5–8 eV; rpaw × R_x = 5.2 × 10¹³ s⁻¹ at 4.9 eV (electrons), as stated.

## 4. Referee items
| item | verdict | evidence |
|---|---|---|
| A1 structural-gap inference | **RESOLVED** | Withdrawn in Result 1, A1 row, IF-FBC-6; F = 0.114 [0.101, 0.115]; "stage 1 cannot decide". No residual claim. |
| A2 ε band, NF | **PARTLY** | Joint corners run (14 + one-at-a-time); [3.95, 4.73] reproduced from summary_v2; ≥ ±0.4 eV stated beside it; NF 3.10/3.50 quoted (verified in source). But the NF reconciliation is wrong: NF use DFPT phonons for electrons *and* holes (source, lines 246, 341), so the mapped variant is FP + no exchange = **4.11 eV**, not "≈ 3.9" (which used e × 0.52 alone and the v1 −0.10). The residual to NF GW/BSE is ≈ 0.6 eV, not ≈ 0.4. |
| A3 Kotani, threshold R_x | **RESOLVED** | Kotani Eq. (5) agreement stated, v1 claim withdrawn. R_x = 0.75 [0.5, 1.0] below 3 eV propagated: P(≥2,5) 0.080/0.097/0.118, ε 4.207/4.149/4.096. The midpoint is a bounded choice, not a computed value; both ends in every corner. Hole R_x is 0.61 just above 3 eV, so 0.75 for holes sits high but inside the band. |
| A4 static vs dynamic screening | **PARTLY** | rpaw run (ε 4.369, P 0.068) and in every corner; Kotani match at 5 eV (by eye) reproduced. But "the static models give an upper bound on the rate and a lower bound on ε" (§2, A4 row) is false as written: static Resta gives Resta/cap = 0.44–0.48, i.e. ×0.68 of rpaw at 2–3.5 eV, and every Resta corner has higher ε than its rpaw twin (e.g. 4.45 vs 4.33). Only the Cappellini primary is the static upper bound. R_x reused for rpaw remains untested (stated). |
| A5 asymmetric phonons | **RESOLVED** | e × 0.52: ε 4.022, P 0.125; h × 3.0: 4.373, 0.075; joint FP 4.234, 0.109 (reproduced 4.242). JR values cited to arXiv:2104.08998 Table III; extrapolation stated. |
| A6 P(N) bands, overcount, matched TVs, α_RK | **RESOLVED with caveat** | 0.097 [0.030, 0.173], 10.3× [5.8, 33] reproduced (grid applied multiplicatively at the edges). Matched TVs at both ε edges (0.146/0.159/0.204) reproduced. "94 %" restated as precision. Caveat on the corners in §5 below. |
| A7 heat | **RESOLVED** | 71.6 % [70.2, 75.0] reproduced (71.60 %); stop convention and mK exciton step stated. |
| B1 grid term | **RESOLVED (label fix)** | ±7.8 % at 5 eV and ±17 % at 4.5 eV (2 × the 12³→14³ shift) are what analyze_v2 applies; the B1 row says "±8 % (4.5–5 eV)". The σ ∈ {0.05, 0.15} test was not run ("grid term covers it" is an assertion). |
| B2 photon vs DM | **RESOLVED** | Claim withdrawn. 20³: full-band max 0.150 at 7 eV; photon seed 20³ vs 12³/28³ 0.142/0.110; DM 0.009. "Not resolved" is the honest statement. |
| B3 checks | **RESOLVED** | C9, C11, C12 as in §1; C2 relabelled trivial. |
| B4 casc18_3 flag | **RESOLVED** | Mechanism (Gat extrapolation above X·E_g; NZ = 32 aliasing ~85 eV) confirmed by C12. |

## 5. Specific questions
- **"ε is decided below 4.5 eV".** Supported as a sensitivity statement: W_ii × 3 below 4.5 eV gives 3.73 (reproduced
  3.74), W_ii × 2 above 5 eV gives 4.150. The test is one-sided (no ×⅓ below, nothing for 4.5–5 eV) and the same region's
  phonon rates matter equally (e × 0.52 alone: −0.13 eV), so "decided by the II/phonon competition at 2.5–4.5 eV" is the
  accurate wording. Its use for NF is qualitative only and the arithmetic must be corrected (A2 above). Note also that
  hitting experiment needs ≈ ×3 the cap rate, i.e. ≈ ×4.6 the rpaw rate, below 4.5 eV.
- **Corners.** Both ends of every band are set by the two single-carrier phonon corners, which pair a first-principles
  coupling for one carrier with JR for the other (c_lo = cap / e × 0.52 / R_x 1.0; c_hi = Resta / h × 3.0 / R_x 0.5).
  REF-A asked for separate e/h ranges, so they are admissible, but c_hi stacks three low-rate extremes and REF-A notes the
  literature shift is anticorrelated. Resta is *not* implausible as such: near threshold it sits at ≈ 0.7 × rpaw, about
  where rpaw × z_qp (≈ 0.8) would be. The c_hi end is also MC-noisy (0.033 vs my 0.030 → overcount 30.7 vs 33.6).
  Without c_lo/c_hi (primary, one-at-a-time incl. e × 0.52 and h × 3.0, 12 JR/FP corners): ε [4.02, 4.59];
  P(≥2, 5 eV) with grid [0.036, 0.141]; overcount [7.1, 27.6]. The quoted band is conservative, not wrong; the
  "≥ 6×" floor is robust in either construction, while the "~30×" top rests on c_hi alone.
- **Photon vs DM.** Unresolved, correctly stated; the 20³ figure is not even a bound while the photon seed moves 0.11–0.14.
- **Heat 71.6 %.** Correct (pairs 28.4 % = 24.48 × 1.16/100; heat = E_ph + E_res).

## 6. Verdict: **ACCEPT WITH FIXES** (text only; no number in a headline band moves)
1. §2 NF paragraph and A2 row: replace "≈ 3.9 eV" by the joint mapping (FP phonons + no exchange = 4.11 eV, verifier
   run; no-exchange shift −0.12 eV in v2); say the residual to NF GW/BSE 3.50 is ≈ 0.6 eV, and keep "≥ ±0.4 eV".
2. §2 and A4 row: "static models give an upper bound" → "the static Cappellini primary is an upper bound; static Resta
   lies below rpaw (×0.68 at 2–3.5 eV) and acts as a proxy for rpaw plus z_qp".
3. §7 / Result 2 / IF-FBC-4: say that the envelope ends come from c_lo and c_hi and add the sub-band without them
   (ε [4.02, 4.59]; P(≥2, 5 eV) [0.036, 0.141]; overcount [7.1, 28]).
4. B1 row: grid term ±8 % at 5 eV, ±17 % at 4.5 eV.
5. checks.py C11 docstring: random disjoint permutation slices, not index halves.
Open but acceptable as stated: σ test not run; mK gap 1.17 eV not rerun [E]; screened DM seed not run [E];
R_x for rpaw untested.

## 7. What Chapter 18 may quote
- **ε_eh = 4.15 eV**, in-class envelope [3.95, 4.73] (most of it [4.0, 4.6]), plus a model-class systematic of at least
  ±0.4 eV; measured 3.75; NF obtain 3.10/3.50 and our run with NF-like phonon/exchange choices still gives 4.11. Caveat:
  stage 1, EPM / diagonal W / deformation-potential phonons, no plasmon branch, static Cappellini primary.
- **F_eh = 0.114 [0.101, 0.115]**, same as the book; below 0.119 ± 0.002, *without* any claim that the gap is structural.
- **P(N ≥ 2, 5 eV) = 0.097 [0.030, 0.173]** (DM heavy, grid ±8 % included); **step overcount ≈ 10×, at least 6×**; the
  upper end "~30×" only with the note that it comes from one extreme corner (Resta + holes × 3 + R_x 0.5).
- **Total heat at 100 eV 71.6 % [70.2, 75.0]**, pairs 28.4 %; the above-threshold/residual split is a convention.
- Exchange factor R_x = 0.66–0.84 (e), 0.51–0.65 (h) above 3 eV, in agreement with Kotani–van Schilfgaarde's 0.5–1.
- Qualitative only: memory ≤ 0.015 TV (model-internal); mK vs 123 K ≤ 0.016 TV; computed splits agree to 0.029 TV
  (precision within IP-EPM). Do **not** quote a photon-vs-DM number (unresolved), the "≈ 3.9 eV" NF reconciliation, or
  "static screening bounds the rate" in general.
