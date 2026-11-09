# R14 referee REF-WP5-AUD-B (hostile, isolated): returns/R14/WP5-AUD.md

Read: the return; code/WP5-AUD/checks.py (rerun: **27/27 PASS, 1.7 s**); returns/R12/WP7-E-v3.md ("E"), returns/R13/WP5-v4.md,
returns/R13/WP8-R.md, LIMITS.md L35–L38, CONVENTIONS.md §12, NOTATION.md (E rows). Full text fetched with lit.py into
literature/papers-r14-REF-WP5-AUD-B/: **2303.02196** and **1803.02903** (PDF, HTML and text extractions deleted; graph.json kept). Own checks:
sympy/numpy scripts in my scratchpad (ref.py, fom.py, f2.py; < 5 s, not part of the campaign tree). WP0-v3 is not cited by the return and is
not in my read list, so the WP0-v3 leg of rubric (d) is **UNRESOLVED by construction**.

## 0. Verdict table
| # | Main claim | Verdict | Reason |
|---|---|---|---|
| 1 | A-1…A-16 applied faithfully in WP5-v4; (W11′) correct | STANDS | spot-checked A-4, A-11, (W11′) against E (E7), (E8), (E13), §6: text matches; (W11′) weights = (AUD-1) (§2) |
| 2 | D-1: D′ lacks E_pairs(t_win) + E_X(t_win) | STANDS | E line 68: E_stored ≡ E_st + E_trap + E_es^{trap}; D′ (E7), A-4 contain no pair or exciton term |
| 2′ | D-1 size "+0.28 in Y_H at 100 eV, Si" | **STANDS WITH CORRECTION** | 0.28 is the first-order bracket term (= Δf_g). At P_g = 0, d′_ER = E_g/ε_eh = 0.31 breaks the small-d′ hypothesis of (E8)/(W11). Exact Y_H shift is **+0.41** (+0.40 at ε = 3.8 eV) (§1) |
| 2″ | D-1: "L36–L38 numbers unaffected" | STANDS WITH CORRECTION | true for the 4 V/cm two-channel datum, but E §3.4 table gives no timing; the claim needs a stated [E] drift-time vs window estimate (§1) |
| 3 | D-2: pre-t_pr bias heat double-counted unless weighted by ϵ_NTL | **STANDS WITH CORRECTION (S/W → N)** | (E7)'s primary argument is ω − D′; 𝒲_bias is not in ω. No double count exists in (E7) as written; AUD-C3e is a tautology. Choosing "ϵ_NTL" is an unsupported spectral assignment [E] (§1) |
| 4 | IF-R13-2: general-r_coll form (AUD-1), κ_cal(r_coll); bounds unchanged | STANDS | re-derived independently with sympy: all three coefficients, the zero-deficit term and the exact δ_coll = X = 0 identity (§2) |
| 4′ | L38 ✎ proposed text, status DERIVED | STANDS WITH CORRECTION | the "exact under (B-a)–(B-d)" bound rests on a 2×10⁴-point scan (C2b), which is "observed" under CONVENTIONS §12. My closed-form proof is in §2; cite it, then DERIVED holds |
| 5 | IF-R13-3 quench protocol | STANDS | AUD-C4 (⟨V⟩ = ω/4 per mode, 138 eV per 4096-atom cell) re-derived |
| 6 | IF-R13-5 (a) | STANDS | — |
| 6′ | D-4: σ_ln(r_coll) 0.05 too narrow → 0.2 | **STANDS WITH CORRECTION** | "0.05 too narrow" confirmed (2.69σ, 0.36%). The value 0.2 is not derived: its source is WP8-R §6 "\|r − 1\| ≲ 0.2 [E]", a bound, which σ_ln = 0.2 turns into a 1σ. AUD-C8b imposes r ≥ 1 although the row says "sign open", and its flat E_st/ω ∈ [0, 0.1] prior is not stated in the return (§3) |
| 6″ | D-5 θ_𝒦 one-path uniqueness condition | STANDS | the moment matrix of (1, E) is PD iff ≥ 2 distinct ε^{hop}; the interior condition is correct |
| 7 | G-R3/G-R4 amendment texts B-1, B-2 | **STANDS WITH CORRECTION** | three defects: the B-1 E_s^{(0)} subtraction; the B-1 sum rule label; the B-2 N_eh ≤ 30 cap (§4) |
| 8 | WP8-R verdict survives: (a) NO-GO, (c) NO-GO ≤ 300 eV, (d) CONDITIONAL | STANDS | reproduced (C7a, C7b, C7d) |
| 8′ | (c) "ceiling ≤ 1.999 with measured Y, F_NR; NO-GO rests on F_NR ≳ 0.4" | **STANDS WITH CORRECTION** | 1.999 is reached only at ⟨𝔮⟩ = 0.873, which the return does not state. At ⟨𝔮⟩ = 1 the same corner gives 1.76. The threshold is F_NR* = 0.28 / 0.40 / 0.50 at ⟨𝔮⟩ = 1 / 0.873 / 0.8. The 300 eV "band" is built from the 220 eV 1σ edges; a log-interpolated 300 eV point gives 1.44 (§5) |
| 8″ | C7c′: "WP8-R C7l (robust at F_NR = 0.15) fails: 2.18" | STANDS WITH CORRECTION | 2.18 uses Y(100 eV) = 0.102 at 300 eV, the same energy mismatch the return charges WP8-R with. With interpolated Y(300) ≈ 0.12 and WP8-R's own F_ER = 0.15, ⟨𝔮⟩ = 1 the value is 1.993 < 2. The conclusion survives only with the return's F_ER = 0.119 or ⟨𝔮⟩ = 0.873 (2.12–2.40) (§5) |
| 9 | WP8-F rulings F-a…F-i | STANDS | F-c formula re-derived (AUD-C10); F-g/D-12 arithmetic re-checked |
| 10 | D-13 "0.48 is a rounding artefact" | STANDS | 0.055/(0.4·0.65)/0.45 × 1.01 = 0.4748 → 0.47; 0.48 only from 0.056 |
| 11 | Literature (2303.02196, 1803.02903) as quoted | CONFIRMED (wording note) | §6 |
| 12 | Provenance tags | STANDS WITH CORRECTION | §7 |

## 1. Energy ledger rulings (D-1, D-2)
**D-1 exists.** E (E1) has the reservoirs E_hot, E_pairs, E_X, E_trap, E_es, E_st, ℋ_ph, E_esc. D′ in E (E7) is E_stored + ΔZPE + E_esc, with
E_stored ≡ E_st + E_trap + E_es^{trap} (E line 68). A-4 writes D′ ≡ E_st + E_trap + E_es^{trap} + ΔZPE + E_esc. E_pairs and E_X are absent from both, so
(E8)/(W11) hold only if P_g(t_win) = 1. E §3.4 (zero-field row: "recombination heat", "E_g − E_x^b returned as heat or light") assumes this and does not
state it. The omission is real.
**The size is wrong as a Y_H shift.** At zero field, with 𝔶 = 0.102, E_g = 1.17 eV and ε_eh = 3.75 eV, the extra deficits are D′_ER += (E_g/ε_eh)(1 − P_g)ω and
D′_NR += 𝔶(E_g/ε_eh)(1 − P_g)ω. Exactly (sympy, my ref.py):
  Y_H(P_g = 0) / Y_H(P_g = 1) = (1 − 𝔶E_g/ε_eh)/(1 − E_g/ε_eh) = 1.407 (1.399 at ε = 3.8 eV),
i.e. **+0.41**, not +0.28. The value 0.28 = (1 − 𝔶)E_g/ε_eh is the first-order bracket term, which is WP8-R's Δf_g. The first-order form needs
d′ ≪ 1, and here d′_ER = 0.31, so it is invalid. AUD-C3d computes only (1 − 𝔶)E_g/ε_eh and never evaluates Y_H; it does not test the stated claim.
**Owed:** in §1.2, R-e, D-1 and the L37 ✎ text, write "Y_H(t_win) = (1 − δ_coll)(ω − D′_NR)/(ω − D′_ER) with the full D′; zero-field first-order term
+(1 − 𝔶)(E_g/ε_eh)(1 − P_g); exact at P_g = 0: +0.41 (Si, 100 eV)". The first-order form (W11) needs (E_g/ε_eh)(1 − P_g) ≪ 1, so P_g(t_win) ≈ 1 becomes
an explicit validity condition of (W11) at zero field. The symbol "y" in D-1 and in the §1.2 fix text is ambiguous (𝔶 or y_ion). It must be 𝔶 (the
created-pair yield) (N). Exciton binding: E_X carries E_g − E_x^b per exciton, a < 2% correction (N).
**"L36–L38 unaffected."** This holds for 1803.02903 at 4 V/cm only if all pairs are collected within the phonon integration window. The cited E §3.4
table states no times. Owed: a one-line [E] estimate (drift time over 1 cm at 4 V/cm against the phonon window), or the statement as an assumption.
L36's Ge input (1805.09942) is quoted in the same sentence, and its field condition is not addressed. State it, or restrict the claim to L38.
**D-2 is not a defect of (E7).** (E7) writes E_sig = ϵ_prim(ω − D′) + ϵ_NTL·(NTL heat). Its primary argument is ω − D′, and ω excludes 𝒲_bias, which
sits on the LHS of (E1). The pre-t_pr bias work enters once, through NTL heat = 𝒲_bias − ΔE_es (E10–E11). The double count would arise only if someone
weighted ℋ_pr itself by ϵ_prim, and no package does. AUD-C3e checks ϵ_q(ω − D′ + W) − ϵ_q(ω − D′) = ϵ_qW, a tautology. The prescription "weighted by
ϵ_NTL" is also physically unsupported. Drift work absorbed before t_pr by hot carriers is emitted inside the primary relaxation cascade. Its phonon
spectrum is then that of the primaries, not that of the terminal-velocity NTL phonons that set ϵ_NTL (WP8-R §6). Correct text: "counted once, inside
NTL heat; its collection efficiency lies between ϵ_prim and ϵ_NTL [E]; ≤ 0.25 eV per carrier (E C15)". Downgrade D-2 to N/clarification.

## 2. IF-R13-2 and the L38 ✎ text (independent sympy)
Model, as in the return: S_ER = (1 − d′_ER) + r_collg_Luke and S_NR = (1 − δ_coll)(1 − d′_NR) + r_collg_Luke y_ion, with η = (1 + g_Luke)S_NR/S_ER − g_Luke y_ion.
The model follows the 1803.02903 procedure, verified in full text: Eq. (1); the ER calibration "unity ionization yield" (PDF p. 8); "simulated nuclear
recoil energies are rescaled to ηNR EMC" (p. 15). My own differentiation (ref.py) gives:
- 1 − η₀ = g(r − 1)(1 − y)/(1 + rg) ✓;
- ∂(1 − η)/∂δ_coll = ∂(1 − η)/∂d′_NR = (1 + g)/(1 + rg) ✓;
- ∂(1 − η)/∂d′_ER = −(1 + g)(1 + rgy)/(1 + rg)² ✓ (= WP5-v4 (W11′), = w·κ_cal(r) of (AUD-1));
- numbers: w = 0.9314, κ_cal(1.144) = 0.6185, κ_cal(1) = 0.6419 ✓; C1e errors 2×10⁻⁵ vs 1.07×10⁻³ ✓.
**Bound, proof replacing the C2b scan.** Set d′_NR = e + κ_cal(r)X + x and d′_ER = X, with e = E_st/ω, X = X^{oth}_ER and x ≥ 0 (B-c). Define
f ≡ (1 − e − η)(1 − X + rg). Then:
(i) ∂f/∂x = (1 + g)(1 − δ_coll) ≥ 0;
(ii) ∂f/∂δ_coll = (1 + g)(1 − d′_NR) ≥ 0;
(iii) at x = δ_coll = 0, f = g(r − 1)(1 − y)(1 − X/(1 + rg)) − e[g(r − 1) − X], linear in e. It equals g(r − 1)(1 − y)(1 − X/(1 + rg)) ≥ 0 at e = 0
and (1 − y)X(1 + g)/(1 + rg) ≥ 0 at e = 1 − y.
Hence E_st/ω ≤ 1 − η exactly, for r ≥ 1, X ≤ 1 and d′_NR ≤ 1, under (B-a), (B-b), (B-d) and X_NR ≥ κ_cal(r)X_ER. The return's claim is true, but the
return proves it only numerically: C2b samples r ∈ [1, 1.4] and e ≤ 0.15. Under CONVENTIONS §12 that is "observed". Owed: cite this proof (or add it
as a sympy check) and keep DERIVED. The L38 Chain/Validity text, the "implied by κ_cal(1) for r_coll ≥ 1" clause (dκ_cal/dr = g(y − 1)/(1 + rg)² ✓)
and the A-4/E §6 constraint sentence are correct as written.

## 3. r_coll prior (D-4)
Confirmed: ln 1.144/0.05 = 2.69σ (one-sided tail 0.36%); ln 1.2/0.05 = 3.65σ. The return omits that r = 0.8 lies at 4.46σ, which strengthens its
point. The replacement σ_ln = 0.2 is not argued, only adopted. Its source is WP8-R §6, "Bound: |r − 1| ≲ 0.2 [E]". Encoding a bound as 1σ puts
32% of the mass outside it. σ_ln ≈ 0.1 (bound at ≈ 2σ) is the literal reading, and 0.2 is a deliberate widening. Either choice must be tagged [E],
with the reason given. The C8b illustration (median 0.036 → 0.026; P(E_st/ω < 0.01) 3% → 18%) has three unstated conditions, all of which belong in
the §3.2(b) text:
(1) r ≥ 1 is imposed (B-b), while the proposed row says "sign open";
(2) E_st/ω has a flat prior on [0, 0.1];
(3) δ_coll = X^{oth} = 0.
The qualitative point, that the prior width pre-decides the E_st reading, stands.

## 4. G-R3 / G-R4 amendment text (B-1, B-2)
- **B-1, E_s^{(0)} (S).** "E_s^{(0)} is the same projection of the Wigner R_I(0) state at t = 0" is wrong. u_s is measured from the quenched end-state
  minimum, so the t = 0 configuration, which sits at the perfect-crystal geometry, projects onto the end-state modes with the static
  defect-displacement energy. That energy is configurational (it is E_st, booked separately) and is not zero-point. The subtraction would remove
  E_st-scale energy from the spectrum. It should be the end-state zero-point level: ⟨E_s^{(0)}⟩ = ω_s/2 per mode (the Wigner expectation of each
  end-state mode). This is consistent with §3.1 step (4), where ΔZPE comes from the end-basin Hessian and is booked in ℋ_ph.
- **B-1, sum rule (W).** "Σ_{(i)–(iv)}∫dℋ/dω_ph = ℋ_pr" lists only carrier-derived parts: relaxation, residual kinetic, capture and pre-t_pr NTL. For an
  NR, ℋ_pr is dominated by the nuclear-cascade lattice heat (the §3.4 MD part). Either label the §2 rule ℋ_pr^{el}, or add (v) "MD lattice heat
  (§3.4 projection) + anharmonic residual + thermostat". ΔZPE ⊂ ℋ_ph is not sensor-absorbable and must be excluded from the spectrum (state this).
- **B-2, N_eh cap (W).** "N_eh ≤ 30 on E_R ∈ [20 eV, 1 keV]" truncates the distribution near its mean at the top of the range. 2303.02196 Table II
  gives Y(0.89 keV) = 0.127 and F = 3.7 [FT], so ⟨N_eh⟩ = 0.127·890/3.8 ≈ 30 and σ ≈ 10.5. Use N_eh ≤ ⟨N_eh⟩ + 6σ (≈ 100 at 1 keV), or cut the range.
- **B-2 (N).** "≥ 500 trajectories → variance to ≈ 6%" is √(2/(n − 1)), the Gaussian value. For F_NR ≈ 2–4 with excess kurtosis the error is larger. State
  the assumption. E_R,th = 352/395 eV matches WP8-R Table 1.1 ✓. The F_NR special case F_eh + Var(E_el)/(ε_eh⟨E_el⟩) follows from total variance ✓.
- **B-2 validation sentence (W).** 2303.02196 does not "take the 0 V phonon energy as E_r". E_r comes from neutron kinematics (TOF, ring angle), and
  the fit model E_t = E_r + n_eh·eV (Eq. (1), PDF p. 2) assumes the primary phonon energy equals E_r. That is the L37 truncation, so the conclusion
  stands; replace the wording.

## 5. WP8-R HV reinterpretation (R-f, D-7, L42 ✎, IF-AUD-6)
I re-implemented the return's fom_int (same formulas as checks.py), reproduced WP8-R (1.723 at 300 eV, Y = 0.153, F_NR = 0.15), and varied the inputs.
All values are at 300 eV, V_b = 100 V:
| Y | F_NR | F_ER | ⟨𝔮⟩ | 𝔖_int |
|---|---|---|---|---|
| 0.098 | 0.4 | 0.119 | 0.873 | **1.999** (the return's maximum) |
| 0.098 | 0.4 | 0.119 | 1 | 1.763 |
| 0.098 | 0.4 | 0.119 | 0.8 | 2.165 |
| 0.102 | 0.15 | 0.15 | 1 | 2.18 (C7c′) |
| 0.12 (interp.) | 0.15 | 0.15 | 1 | **1.993** |
| 0.12 | 0.15 | 0.119 / 0.15 | 1 / 0.873 | 2.12 / 2.25 |
| 0.111, 0.78 (interp. 1σ-low edges) | — | 0.119 | 0.873 | 1.44 |
Threshold F_NR* for 𝔖_int = 2 at Y = 0.098, F_ER = 0.119: **0.275 / 0.399 / 0.498** at ⟨𝔮⟩ = 1 / 0.873 / 0.8.
Rulings:
(i) The 1.999 note omits ⟨𝔮⟩ = 0.873, which is essential: ⟨𝔮⟩ enters as an effective bias ⟨𝔮⟩V_b, and 𝔖_int falls steeply with V_b (3.30 at 50 V,
1.76 at 100 V). Since a Ramo-collected trapped carrier still induces partial charge, ⟨𝔮⟩ = 1 − 0.127 is a lower bound, so the corner is
conservative. It must still be stated.
(ii) "Rests on F_NR ≳ 0.4" is a ⟨𝔮⟩-dependent threshold, 0.28–0.50. The 300 eV corner uses the 220 eV 1σ lower edges (Y 0.098, F 0.4). The
2303.02196 uncertainties are 1σ ("Each systematic uncertainty is evaluated at 1σ", PDF p. 5), so a 2σ excursion (F_NR ≈ 0.3) crosses 2 at
⟨𝔮⟩ = 0.873. Log-interpolated 300 eV values give 1.44, a 28% margin. So the NO-GO is knife-edge only under the bracket, and comfortable under
interpolation. Both statements belong in R-f, D-7, L42 ✎ and the IF-AUD-6 SOTA sentence.
(iii) C7c′ repeats the energy mismatch it charges WP8-R with. Owed: "with interpolated Y(300 eV) ≈ 0.12, C7l's F_NR = 0.15 case gives 1.99 (WP8-R's
F_ER, ⟨𝔮⟩) to 2.40 (F_ER = 0.119, ⟨𝔮⟩ = 0.873)".
(iv) Minor (W). F_meas^{obs} is applied to the ER only, but NR trapping adds the same binomial term. Applying it to the NR would lower 𝔖, so the
NO-GO direction is unaffected; state the asymmetry. C7b uses Y = 0.072 at all energies. That is a valid lower bound on E_2σ, and the text should
say "lower bound".
WP8-R's verdict (NO-GO for the brief's target; (d) CONDITIONAL, ζ_O,min 0.13/0.24/0.44 reproduced) **stands**.

## 6. Literature (rubric c; no "paper is wrong" claim is made)
| Statement | Full-text check | Rating |
|---|---|---|
| 2303.02196 Table II, Si Y and F at 0.10/0.22/0.46 keV | PDF p. 5: 0.102^{+0.034}_{−0.030}, 0.9^{+0.7}_{−0.4}; 0.108^{+0.009}_{−0.010}, 0.5^{+0.2}_{−0.1}; 0.136^{+0.009}_{−0.008}, 1.8^{+0.6}_{−0.5} | CONFIRMED |
| Eq. (1) E_t = E_r + n_eh·eV, ε = 3.8 eV; HV data at 100 V | PDF p. 2 | CONFIRMED |
| trapping 12.7%, impact ionization 0.6% | PDF p. 4: probabilities applied as smearing of the sampled n_eh, so the paper's Y is a **created**-pair yield (supports R-c "use measured Y for 𝔶") | CONFIRMED |
| "takes the 0 V phonon energy as E_r" | E_r from kinematics; 0 V mode is a cross-check | REFUTED as worded; the L37-truncation conclusion stands (§4) |
| 1803.02903: η^φ_NR = 95.2^{+0.9}_{−0.7}% (p. 17), ε = 3.82 eV (p. 5 fn. 2), "unity ionization yield" (p. 8), rescaling E_MCη (p. 15), efficiency "consistent with 100%" (p. 3), "relative fractions of primary and NTL phonons" (p. 6) | located | CONFIRMED |

## 7. Provenance and notation (rubric d, e)
- "g_Luke = 4/3.82, y_ion = 0.3, κ_cal = 0.642, r_coll = 1.144 | [FT]/[E]": split the tags. g_Luke is [FT] (1803.02903). y_ion = 0.3 is [E]. κ_cal and
  r_coll are [D] on [E] inputs (E C7e, C7f).
- "[FT via WP8-R]", "[FT via WP5-v4]" and "[FT via E, WP5-v4]" are not CONVENTIONS §12 tags. Write [FT] (source, as read by <package>) or [E].
- The 300 eV Y/F "bands" in C7c are a bracket constructed in this audit, not data. Tag them [E] (constructed from [FT] 220/460 eV rows).
- "y" in D-1, §1.2 and C3d must be 𝔶; "1 − y" in AUD-C3d also uses 2303.02196's Y (ε = 3.8 eV) as 𝔶 (ε_eh = 3.75 eV): a 1.3% rescale (N).
- D-12 writes "270–540" while AUD-C5 and F-g write "272–543" (N).
- New symbols κ_cal(r_coll), P_g and E_s/E_s^{(0)} do not collide in NOTATION. E_s^{(0)} must be redefined (§4).
- The 𝔮 rename (NOTATION l. 636, E's 𝔵) is honoured.

## 8. Owed corrections (for CORRECTIONS)
| ID | Target | Type | Fix |
|---|---|---|---|
| B-1 | WP5-AUD §1.2, R-e, D-1, L37 ✎ | S | Y_H size +0.41 exact (0.28 is the first-order term, invalid at d′_ER = 0.31); P_g(t_win) ≈ 1 is a validity condition of (W11) at zero field; y → 𝔶 |
| B-2 | WP5-AUD §1.2 "L36–L38 unaffected" | W | add the [E] drift-time vs window estimate; Ge (L36) field condition |
| B-3 | WP5-AUD D-2, AUD-C3e | W→N | no double count in (E7); "ϵ_NTL" → "between ϵ_prim and ϵ_NTL [E]"; drop "S/W" weight |
| B-4 | WP5-AUD §2, L38 ✎ status | W | replace the C2b scan by the §2 proof (or a sympy check of it) |
| B-5 | WP5-AUD §3.2(b), D-4, WP6 row θ_coll | W | σ_ln = 0.2 tagged [E] with reason (bound-as-1σ); state the C8b conditions (r ≥ 1, flat e-prior, δ = X = 0) |
| B-6 | WP5-AUD B-1 (§4) | S | E_s^{(0)} = ω_s/2 per end-state mode; sum rule label ℋ_pr^{el} or add the MD lattice part; exclude ΔZPE |
| B-7 | WP5-AUD B-2 (§4) | W | N_eh cap ≥ ⟨N_eh⟩ + 6σ (≈ 100 at 1 keV); Gaussian assumption for 6%; "0 V phonon energy" wording |
| B-8 | WP5-AUD R-f, D-7, C7c/C7c′ notes, L42 ✎, IF-AUD-6 | S (claim) | state ⟨𝔮⟩ = 0.873 at the 1.999 corner; F_NR* = 0.28–0.50 for ⟨𝔮⟩ = 1–0.8; 1σ bracket vs interpolation (1.44); C7c′ with interpolated Y gives 1.99–2.40 |
| B-9 | WP5-AUD §7 | N | split [FT]/[E]; "[FT via X]" → §12 tags; constructed 300 eV bracket [E] |
| B-10 | WP5-AUD D-12 vs C5 | N | one rounding (272–543) |

Status recommendation: the return's rulings 2 (IF-R13-2), 3 and 3′(c) are REFEREED (this referee) with B-4. Rulings 1, 4 and 5 are REFEREED with B-1…B-3,
B-5…B-8 applied. The WP8-R verdict stands.
