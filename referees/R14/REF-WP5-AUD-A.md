# R14 referee REF-WP5-AUD-A (hostile, isolated) on returns/R14/WP5-AUD.md

Read: returns/R14/WP5-AUD.md, code/WP5-AUD/checks.py (rerun: **27/27 PASS, ≈ 2 s**), returns/R12/WP7-E-v3.md, returns/R13/WP5-v4.md §3.4,
returns/R13/WP8-R.md, LIMITS.md (L36–L38), CONVENTIONS.md §12, DONE.md, CONTROLS.md. Nothing under referees/, state/, briefs/ (except my brief), LAUNCHES/log
or other R14/R15 returns was read. In particular state/CORRECTIONS.md §18, which the return cites, was **not** read, so the rename claims (D-8) are checked
only against WP7-E-v3/WP5-v4 usage. Full texts were fetched with lit.py into literature/papers-r14-REF-WP5-AUD-A/: **2303.02196** and **1803.02903**. The PDF,
HTML and text extractions are deleted; only the *.graph.json stubs remain. My own checks were sympy/numpy runs of < 5 s.
They imported the audit's FOM functions unchanged. The scripts are not retained; every number they gave is transcribed in §2, §4, §5 and §7.

## 0. Verdict table
| # | Main claim of WP5-AUD | Verdict | Reason (details in §n) |
|---|---|---|---|
| 1 | A-1…A-16 applied faithfully in WP5-v4; K1–K17 table correct | STANDS | spot checks of A-4, A-12, (W11′) against WP7-E-v3/WP5-v4 text agree (§1) |
| 2 | D-1: D′ of (E7)/A-4/(W11) lacks E_pairs(t_win) + E_X(t_win) | STANDS WITH CORRECTION | the omission is real ((E1) carries E_hot + E_pairs + E_X; D′ = E_stored + ΔZPE + E_esc does not). **The size "+0.28 on Y_H" is wrong**: that is the first-order term of a deficit that is not small. Exactly, at P_g = 0 the shift is **+0.41** (×1.407). The proposed fix ("bracket gains …") is first order where first order fails. Separate P_g^{NR}, P_g^{ER} are needed. "L36–L38 unaffected" is unsupported by the table it cites (§2) |
| 3 | D-2: pre-t_pr bias heat must be weighted once, by ϵ_NTL | STANDS WITH CORRECTION | true, but (E7) as written already satisfies it: ω − D′ does not contain 𝒲_bias(t_pr). AUD-C3e is a tautology (it checks ε·W = ε·W). Downgrade to a clarifying sentence (N/W); it is not a defect of (E7) (§3) |
| 4 | IF-R13-2 / (AUD-1): general-r_coll first order, κ_cal(r_coll) = (1 + r_collg_Luke y_ion)/(1 + r_collg_Luke); C2a exact identity; bounds unchanged | STANDS | independently re-derived with sympy from my own encoding of 1803.02903 Eq. (1) and its ER calibration (§4). Source quotes verified [FT] |
| 5 | Corrected L38 text (§2 of the return) | STANDS WITH CORRECTION | the algebra is right. Two wording issues: the Chain cell keeps "g_Luke = 4/3.82" next to (AUD-1)'s O-symbol list, and the Validity cell must state the r_coll ≥ 1 premise (B-b) explicitly, not only inside the "implied by" clause (§4) |
| 6 | IF-R13-3 quench protocol (138 eV/cell Wigner offset) | STANDS | ⟨V⟩ = ω/4 per mode re-checked. 3·0.045/4·4096 = 138.2 eV. Protocol text consistent with WP5-v4 [v4] reading |
| 7 | D-4: r_coll prior σ_ln 0.05 → 0.2, "sign open" | STANDS WITH CORRECTION | the 0.05 criticism is right (1.144 at 2.69σ). But 0.2 is not derived: WP8-R §6 gives "|r − 1| ≲ 0.2 [E]" as a **bound**, which reads as ≈ 2σ, i.e. σ_ln ≈ 0.1. "Sign open" also contradicts AUD-C8b, which imposes r ≥ 1 (B-b), and drops the conditional E_st bound for half the prior mass (§5) |
| 8 | D-5: θ_𝒦 one-path class, interior condition | STANDS | the moment matrix of (1, E) is singular for one ε^{hop}. An exponential tilt matching the mean needs the target strictly inside (ε_min, ε_max). Correct |
| 9 | B-1 (G-R3) created-phonon spectrum amendment | STANDS WITH CORRECTION | the sum rule is not closed as written. Parts (i) "above E_th^{ii}" and (ii) "below ω_op" leave carrier relaxation between ω_op and E_th^{ii} unassigned. For an NR, ℋ_nuc (MD heat) is in ℋ_pr but in none of (i)–(iv) (§6) |
| 10 | B-2 (G-R4) sub-threshold yield amendment | STANDS WITH CORRECTION | N_eh ≤ 30 truncates the stated range: at 0.89 keV the source has Y = 0.127, F = 3.7, so ⟨N_eh⟩ ≈ 30 and σ ≈ 10. "≈ 6% variance at 500 trajectories" is Gaussian-only. "takes the 0 V phonon energy as E_r" misreads 2303.02196, whose sub-keV E_r is kinematic (§6) |
| 11 | WP8-R (c) HV NO-GO survives, "ceiling ≤ 1.999, rests on F_NR ≳ 0.4" (R-f, D-7, AUD-C7c) | **FALLS** (the robustness claims "ceiling ≤ 1.999 at band edge" and "F_NR ≳ 0.4 sufficient"; the (c) verdict itself becomes CONDITIONAL on Y, F_NR, ⟨𝔮⟩ and the C.L.; it holds at central values, §7) | (i) the audit evaluates the source's Y (defined with ε = 3.8 eV) with ε_eh = 3.75. With the source's ε the same corner gives **2.014 > 2**. (ii) The Table II bands are **1σ** ("Each systematic uncertainty is evaluated at 1σ"), so a "ceiling" at a 1σ corner is not a NO-GO bound. At the measured 220 eV point the 2σ corner gives 2.02. (iii) The F_NR threshold is a joint (Y, F_NR, ⟨𝔮⟩) condition: F_NR* = 0.40 at ⟨𝔮⟩ = 0.873 but 0.28 at ⟨𝔮⟩ = 1 (§7) |
| 12 | "C7l robust at F_NR = 0.15 fails: 2.18" (AUD-C7c′) | STANDS WITH CORRECTION | 2.18 uses Y(100 eV) = 0.102 at 300 eV, the energy-mismatch the audit itself charges to WP8-R (R-c, R-f). With its own energy-matched central Y(300) = 0.12: 1.993 (ε 3.75) / 2.008 (ε 3.8). Marginal, not 2.18 (§7) |
| 13 | WP8-R (a) NO-GO, (d) CONDITIONAL, ζ_O,min 0.13/0.24/0.44 | STANDS | C7a reproduction of WP8-R confirmed. It also confirms WP8-R used Lindhard(100 eV) at 300 eV: Lindhard(300 eV) would give 0.82, not the published 0.91. (d) numbers inherit the ε = 3.75/3.8 issue (sub-1% shift) |
| 14a | Proposed LIMITS rows L36 ✎, L37 ✎, new 2303.02196 row | STANDS WITH CORRECTION (L36, L37); STANDS (new, OPEN) | L36 ✎ carries "p_surv ≲ 0.475" (X-10). L37 ✎ adds the D-1 term in the first-order bracket form rejected in X-1: use the exact-ratio wording. The new row's "Y is the L37 truncation" is right, but its reason is wrong (X-6) |
| 14 | Remaining rows R-a…R-i, F-a…F-i, D-8…D-17 | STANDS (spot-checked) | D-12/C5 and D-13/C11 arithmetic reproduced; D-13 is cosmetic (0.4748 → 0.47 at 2 d.p., not "0.475") |

## 1. Rung-4 and (d) consistency, (a) DERIVED steps
- AUD-C1–C11 rerun: all PASS. Inspection shows C3c, C3e and C9 are **structural tautologies**. C3c checks that a formula with an extra term differs
  unless the term vanishes. C3e checks ε·W = ε·W. Neither verifies the physics claim built on it (the D-1 size, the D-2 double count). C9 is substantive: it checks that S(θ) is invariant
  under the non-unique λ. C7c is a 2–3-point corner grid, not a bound: the maximum over the stated boxes was located only on that grid. I checked that S_int is
  monotone in Y, F_NR, F_ER and ⟨𝔮⟩ on the box (ref2.py), so the corner is the true box maximum. The DERIVED label stands for (AUD-1) and C2a only.
- (d) CONVENTIONS/NOTATION: tags follow §12. I grepped NOTATION. P_g has no collision. κ_cal (row 633) is defined as the r = 1 value, so κ_cal(r_coll) overloads it with an argument. That is acceptable only if the NOTATION row is amended (D-15 covers it). WP0-v3: no overlap with this return's content; not checked. Not verifiable by me: the CORRECTIONS §18 rename list
  (D-8), which is outside my read set.

## 2. D-1 (free-pair/exciton energy at t_win) and its "+0.28 Y_H" size
**Existence: CONFIRMED.** WP7-E-v3 (E1), line 71: ω + 𝒲_bias = E_hot + E_pairs + E_X + E_trap + E_es + E_st + ℋ_ph + E_esc + E_sig + E_sl. E_stored ≡ E_st + E_trap +
E_es^{trap} (line 68), D′ ≡ E_stored(t_win) + ΔZPE(t_win) + E_esc (line 142), and A-4's D′ (WP5-v4 §3.4) likewise omit E_pairs and E_X (also E_hot, which is
negligible at t_win). Y_H = (1 − δ_coll)(ω − D′_NR)/(ω − D′_ER) is therefore incomplete whenever pairs or excitons survive to t_win.
**Size: REFUTED as stated.** The return writes "+0.28 at 100 eV in Si" (§1.2) and labels C3d "shifts zero-field Y_H by +(1 − y)E_g/ε_eh(1 − P_g) = +0.28".
That is only the first-order term. With G ≡ E_g/ε_eh = 1.17/3.75 = 0.312 and δ_coll = D′ = 0, the full ratio is
  Y_H = [1 − 𝔶G(1 − P_g)]/[1 − G(1 − P_g)]  ⇒  at P_g = 0: Y_H = 1.407 (𝔶 = 0.102), i.e. **+0.41 (0.39–0.42 over 𝔶 = 0.136–0.072)**, not +0.28 (ref3.py).
The ER deficit d′_ER = G(1 − P_g) ≈ 0.31 is not small, so the controlled-first-order premise of (E8)/(W11) (d′ ≪ 1, E C9a) fails in exactly this regime. Corrections:
- D-1's fix must not be "the bracket of (W11) gains ⟨ΔE_pairs⟩ + ⟨ΔE_X⟩". Keep E_pairs + E_X inside D′ in the **exact ratio** form and state that the
  first-order bracket is invalid unless G(1 − P_g) ≪ 1.
- Replace the single P_g by P_g^{NR}(t_win) and P_g^{ER}(t_win). Dense NR tracks recombine geminately faster, and taking P_g equal is an extra assumption. For excitons the stored
  amount is E_g − E_x^b per bound pair (E §1.1 exciton convention), not E_g.
- "+0.28" survives only as WP8-R's Δf_g (a difference of fractions of ω), which is a different quantity from a Y_H shift. The return conflates the two ("That is WP8-R's channel (b)").
- "L36–L38 numbers unaffected, because … pairs are collected well inside the phonon window (E §3.4 table)": the E §3.4 table (lines 250–259) contains **no**
  collection times. The statement may be true (μs drift against ms windows) but is unsourced. Tag [E] and cite a drift-time estimate.

## 3. D-2 (bias work)
(E7) is E_sig = ϵ_prim(ω − D′) + ϵ_NTL·(NTL heat). Its primary argument ω − D′ does not contain 𝒲_bias(t_pr) at all, and "NTL heat" is the whole drift work.
So (E7) **already** weights the pre-t_pr bias heat once, by ϵ_NTL. The double count arises only if a user identifies the primary argument with the MD/cascade ℋ_pr,
which contains 𝒲_bias(t_pr) per A-12 (ℋ_eff = ℋ_pr − 𝒲_bias(t_pr)). The appended sentence is a useful guard. D-2 should be N/W "clarification", owner WP5-v4 A-12 only.
WP7-E (E7) has no defect here. AUD-C3e proves nothing beyond the definition.

## 4. IF-R13-2 and the L38 κ_cal(r_coll) form (sympy, independent)
Own encoding: the ER-calibrated phonon scale maps an ER of energy ω to E_φ = ω(1 + g). Hence E_φ^{NR} = (1 + g)ω S_NR/S_ER, with
S_ER = (1 − d′_ER) + rg and S_NR = (1 − δ)(1 − d′_NR) + rgy. With E_Q = yω, E_R^{rec} = E_φ − gE_Q and η = (1 + g)S_NR/S_ER − gy, which matches 1803.02903:
"E_R = E_ϕ − E_Q(eV_b/ε)", the phonon scale "calibrated using a sample of bulk electron recoils, which should have unity ionization yield" (PDF p. 8), and the
MC rescaled to E′_MC = E_MCη^φ_NR (p. 15) [FT, verified]. Results (ref1.py):
- series to first order in (δ, d′_NR, d′_ER) minus (AUD-1): **0** (exact symbolic). The r = 1 reduction is 1 − δ − d′_NR + κ_cald′_ER: **0**. η₀(r): **0**. C2a identity
  1 − η − e = g(r − 1)(1 − y − e)/(1 + rg) at δ = X = 0: **0, exact**. The δ coefficient at d′ = 0 is exactly (1 + g)/(1 + rg). The r solving η₀ = 0.952 at y = 0.3,
  g = 400/382 is 1.14393.
- (AUD-1) is algebraically identical to WP5-v4 (W11′): the d′_ER weight (1 + g)(1 + rgy)/(1 + rg)² = w·κ_cal(r). **CONFIRMED.**
- Numbers 0.931, 0.618, 0.576, 0.642 reproduced. dκ_cal/dr = g(y − 1)/(1 + rg)² < 0, so (B-c) with κ_cal(1) implies (B-c) with κ_cal(r) **for r ≥ 1 only**.
  The corrected L38 Validity cell must therefore list (B-b) r_coll ≥ 1 as a hypothesis in its own right. It is not a by-product of the "implied by" clause.
  Leading correction O(d′², δ_colld′, δ_coll²): correct.
- (b) Source quotes: η^φ_NR = 95.2^{+0.9}_{−0.7}% "at 95% C.L." (p. 17), ε = 3.82 eV "above 77 K" (p. 5 fn. 2), 4 V / 4 V/cm (p. 5), "need not be identical",
  "relative fractions of primary and NTL phonons" (p. 6): all **CONFIRMED** [FT].

## 5. The σ_ln = 0.2 r_coll prior (D-4)
- CONFIRMED: σ_ln = 0.05 puts r = 1.144 at 2.69σ and pre-decides the E_st reading. The C8b numbers reproduced: median 0.036/0.026, P(E_st/ω < 0.01) = 0.028/0.181.
- **Not derived:** the only source of the width is WP8-R §6 "Bound: |r − 1| ≲ 0.2 [E]". Read as a bound, it gives σ_ln ≈ 0.1 (2σ). A σ_ln = 0.2 Gaussian puts
  32% of its mass outside the very bound it cites. With σ_ln = 0.1 (r ≥ 1): median E_st/ω = 0.029, P(< 0.01) = 0.13 (ref3.py). The qualitative point (the prior,
  not the data, decides) survives at 0.1. The specific 0.2 needs a stated rationale, or the row should read "σ_ln 0.1 (WP8-R bound as 2σ) [E]".
- **Internal contradiction:** the row says "sign open", but the conditional bound (B-b) and C8b both assume r ≥ 1. With a two-sided prior the posterior for E_st/ω
  widens: σ_ln 0.2 gives median 0.065, 95% point 0.144, against 0.026/0.047 with r ≥ 1. Half the prior mass then lies where E_st/ω ≤ 1 − η does not hold. The row must say
  which: either r ≥ 1 imposed (then not "sign open"), or sign open with the conditional bound (ii) explicitly restricted to the r ≥ 1 branch.

## 6. G-R3 / G-R4 amendment text (B-1, B-2)
**B-1.** The sum rule "Σ_(i)–(iv)∫dℋ/dω_ph = ℋ_pr" does not close as partitioned:
- (i) "relaxation part above E_th^{ii}" and (ii) "residual-kinetic part below ω_op" leave carrier energies in [ω_op, E_th^{ii}] unassigned. That interval holds the
  bulk of intervalley/optical emission (WP8-R §1.2: f ≈ 11–15 THz).
- For an NR, ℋ_pr includes the nuclear-stopping heat ℋ_nuc (E §1.5, E_nuc = ℋ_nuc + E_st + …), which is in none of (i)–(iv).
- Fix: (i) "carrier relaxation from creation down to ω_op"; add (v) "lattice (nuclear) heat ℋ_nuc from the §3.4 MD projection". Otherwise the per-sample check fails by construction.
- The "≤ 10% anharmonic residual at t_pr" acceptance level is unsourced ([E]).

**B-2.**
- "N_eh ≤ 30 on E_R ∈ [20 eV, 1 keV]" is too small. 2303.02196 Table II [FT, p. 5] gives Y = 0.127, F = 3.7 at 0.89 keV, so ⟨N_eh⟩ = 0.127·890/3.8 ≈ 30 with
  σ ≈ 10.5. The truncation removes about half the distribution. Fix: N_eh ≤ 80, or ≥ ⟨N⟩ + 6σ.
- "≥ 500 trajectories so that a sample variance is good to ≈ 6%" is √(2/(n − 1)), valid for Gaussian kurtosis only. With F up to 3.7 (negative-binomial-like), the
  relative error is larger; state √(2/(n − 1) + κ_ex/n).
- Validation numbers: Y and F at 0.10/0.22/0.46 keV, ε = 3.8 eV and Eq. (1) on p. 2 are **CONFIRMED** [FT]. "takes the 0 V phonon energy as E_r" is **wrong**. Sub-keV E_r are
  set by neutron kinematics (ring detectors at known angles, p. 3). 0 V data enter only through the phonon-scale calibration (±1.3%) and the LW scale factors
  (Table I). The L37-truncation conclusion stands for a different reason: Eq. (1) books the non-NTL phonon energy as E_r (unit heat quenching).
- "≤ 5.5% E_st bias inside their errors": ΔY ≈ 0.055·ε/eV_b = 0.002 ≪ 0.03. **CONFIRMED**.
- "trapping 12.7%, impact ionization 0.6%": **CONFIRMED** [FT, p. 4], but note these are **detector-model probabilities** from their Ref. [28], not ⟨𝔮⟩.
  Using ⟨𝔮⟩ = 0.873 (C7c) treats every trapped carrier as delivering zero NTL work. That is a worst case, not a measured value; tag [E].

## 7. WP8-R high-voltage NO-GO with the 2303.02196 measured yield (R-f, D-7, AUD-C7c, C7c′)
(c) Rating: claim "with energy-matched measured Y, F_NR the 100 V ceiling at E_R ≤ 300 eV is ≤ 1.999": **REFUTED**. Claim "WP8-R C7l (robust at
F_NR = 0.15) fails": **UNRESOLVED** (marginal). Reproduced numbers (audit FOM code unchanged; ref2.py):
| Case (300 eV, 100 V, F_ER = 0.119) | S_int, audit (ε_eh = 3.75 for the NR pair count) | S_int, source definition ⟨n_eh⟩ = YE_r/3.8 |
|---|---|---|
| Y 0.098, F_NR 0.4, ⟨𝔮⟩ 0.873 (audit's corner) | 1.9986 | **2.014** |
| Y 0.102, F_NR 0.15, F_ER 0.15, ⟨𝔮⟩ 1 (AUD-C7c′) | 2.18 | 2.196 |
| Y 0.12 (audit's own energy-matched central), F_NR 0.15, F_ER 0.15, ⟨𝔮⟩ 1 | 1.993 | 2.008 |
| Y 0.12, F_NR 0.4, ⟨𝔮⟩ 0.873 | 1.777 | 1.791 |
| 220 eV (measured point), joint 2σ-low Y 0.088 and F_NR 0.3, ⟨𝔮⟩ 0.873 | — | 2.015 |
- **ε consistency.** 2303.02196 defines ⟨n_eh⟩ = Y·E_r/ε with ε = 3.8 eV (Eq. (1), p. 2). The audit's fom computes n_NR = Y·E_R/3.75 and yg with g = qV/3.75,
  overstating the NR pair number by 1.3%. At a ceiling decided in the third decimal, this flips the verdict at the audit's own corner.
- **Confidence level.** Table II uncertainties are 1σ. The systematics are stated as such ("Each systematic uncertainty is evaluated at 1σ significance"); the statistical part comes from the MCMC and its C.L. is not quoted, presumably 68%. The audit
  calls the 1σ corner "the edge of the measured bands" and treats it as a ceiling. A NO-GO "at any contrast" needs the ceiling < 2 over a stated C.L. At 1σ it is ≈ 2.0;
  at the joint corner where Y and F_NR are both 2σ low (well beyond 2σ overall) it exceeds 2 even at the measured 220 eV point.
- **"F_NR ≳ 0.4" is not a one-parameter condition.** At 300 eV, Y = 0.098, the F_NR giving S = 2 is 0.40 at ⟨𝔮⟩ = 0.873 but 0.28 at ⟨𝔮⟩ = 1 (and 0.25 / 0.16 at 220 eV).
  The 300 eV "band" (Y 0.098–0.145, F 0.4–2.4) is a union of the 220 and 460 eV 1σ boxes, an [E] interpolation (F_NR is non-monotone: 0.9, 0.5, 1.8).
- At central measured values the (c) NO-GO **does** hold: S_int(300 eV) ≈ 1.4–1.8, and ≤ 1.27 at 100 eV over the whole 100 eV box with ε = 3.8. The V_b scan
  confirms 100 V is the worst point of the HV range (S_int falls monotonically: 1.76 → 0.62 from 100 to 300 V).
- **Correct D-7/L42 text:** "HV (≥ 100 V) NO-GO at E_R ≤ 300 eV at the central measured Y(E_R), F_NR (2303.02196, 1σ bands). At the 1σ corner (Y 0.098, F_NR 0.4,
  ⟨𝔮⟩ 0.873 [E]) the ceiling is 2.01 at 300 eV; at the joint 2σ corner it exceeds 2 from 220 eV. The NO-GO is firm only at E_R ≲ 220 eV (1σ) and is otherwise CONDITIONAL on F_NR, Y and ⟨𝔮⟩."
- **C7c′ (2.18):** this applies Y(100 eV) at 300 eV, which R-c/R-f object to in WP8-R. The energy-matched statement is S_int ≈ 2.00 ± 0.01 (ε choice) at F_NR = 0.15.
  So WP8-R's "also holds at F_NR = 0.15" is borderline, not refuted.

## 8. (e) Provenance spot checks
| Value in return | Tag | Check |
|---|---|---|
| η^φ_NR 95.2^{+0.9}_{−0.7}% 95% C.L.; ε 3.82; 4 V; unity-yield ER calibration; E′_MC | [FT] 1803.02903 | CONFIRMED, page numbers correct |
| Y, F at 0.10/0.22/0.46 keV; ε 3.8; Eq. (1) p. 2; 12.7%/0.6% p. 4; Table II p. 5 | [FT] 2303.02196 | CONFIRMED. Missing: "1σ" and "Er kinematic" |
| ⟨𝔮⟩ ∈ {0.873, 1} in C7c | none given | needs [E] (from a trapping probability, not a measured ⟨𝔮⟩) |
| σ_ln(r_coll) = 0.2 | "[E]" via WP8-R §6 | the source says "≲ 0.2" as a bound; width = 2σ reading gives 0.1 |
| 300 eV band Y 0.098–0.145, F 0.4–2.4 | implied [FT] | is [E] interpolation; not a measured band |
| "pairs collected well inside the phonon window" | cites E §3.4 | E §3.4 has no times; [UNVERIFIED] |
| F_meas^{obs} ∈ [0.119, 0.3] | none | upper value 0.3 untagged |

## 9. Required corrections (exact)
| ID | Target | Sev | Fix |
|---|---|---|---|
| X-1 | §1.2, D-1, AUD-C3d label, R-e | S | "+0.28" → "+0.41 exactly at P_g = 0 (first-order term 0.28; first order not valid, d′_ER ≈ 0.31)"; keep E_pairs + E_X in D′ of the exact ratio; P_g^{NR} ≠ P_g^{ER}; exciton term E_g − E_x^b. Tag the "L36–L38 unaffected" sentence [E] with a drift-time source |
| X-2 | D-2, AUD-C3e | W | reclassify as clarification. (E7) already excludes 𝒲_bias(t_pr) from ω − D′; owner A-12 only |
| X-3 | L38 Validity text | W | state (B-b) r_coll ≥ 1 as a hypothesis. The κ_cal(1) ⇒ κ_cal(r) implication holds only there |
| X-4 | D-4, §3.2 θ_coll row | S | σ_ln 0.2 → 0.1 (WP8-R bound read as 2σ) or give a derivation. Resolve "sign open" against (B-b): two-sided prior ⇒ conditional bound applies only on r ≥ 1 branch |
| X-5 | B-1 | S | close the partition: (i) carrier relaxation down to ω_op; add (v) ℋ_nuc |
| X-6 | B-2 | W | N_eh range ≥ ⟨N⟩ + 6σ (≥ 80); kurtosis term in the variance error; E_r kinematic, not 0 V |
| X-7 | R-f, D-7, §0 row 5, IF-AUD-6, L42 ✎, AUD-C7c | S | use ⟨n_eh⟩ = YE_r/3.8 (source ε). Ceiling 2.014 > 2 at the 1σ corner. Replace "≤ 1.999 / rests on F_NR ≳ 0.4" with the §7 text; state the 1σ C.L.; tag ⟨𝔮⟩ [E] |
| X-8 | AUD-C7c′, D-7 quote | W | 2.18 → energy-matched 2.00 ± 0.01. "C7l fails" → "C7l is marginal" |
| X-9 | §1 header claim "DERIVED" for C3c/C3e | W | label them consistency identities, not derivations of D-1/D-2/D-5 |
| X-10 | D-13 | N | 1.01 × 0.47 = 0.4748 → "≲ 0.47 (unrounded)", not "0.475" |

## 10. Overall
The return's central algebra (AUD-1, C2a, the quench protocol, the θ_𝒦 condition) is correct and independently reproduced. Two load-bearing numerical rulings
are overstated. First, D-1's +0.28 is the linear term of a non-small deficit; the exact value is +0.41. Second, the WP8-R HV "ceiling ≤ 1.999" depends on an ε-convention slip and on
reading 1σ bands as limits. With the source's ε, the ceiling is 2.014 at the audit's own corner. The WP8-R (c) NO-GO holds at central measured values only.
Status of WP5-AUD after these corrections: CLAIMED, with X-1, X-4, X-5, X-7 substantive.
