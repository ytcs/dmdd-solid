# R14 / WP5-AUD: joint audit of WP5-v4 and WP7-E-v3 (with WP7-T-v2 T-1), and the yield sites of WP8-R and WP8-F

Audit agent, brief briefs/R14/WP5-AUD.md. Read: returns/R13/WP5-v4.md ("WP5-v4"), returns/R12/WP7-E-v3.md ("E"), returns/R12/WP7-T-v2.md §5 (T-1),
returns/R13/WP8-R.md, returns/R13/WP8-F.md, returns/R8/WP6-v3.md §5, LIMITS.md (WP7-E rows L33–L38), CONVENTIONS.md (incl. §13 rows 23–28 and "R13
amendments"), NOTATION.md (incl. "Rows added WP7-E"), state/CORRECTIONS.md §18. WP7-E-v3 symbols are written in their NOTATION names (§18 renames).
**Checks:** `code/WP5-AUD/checks.py` (sympy + numpy, **27/27 PASS, ≈ 2 s**), cited **AUD-Cn**. WP8-R's FOM functions are re-implemented there with
WP8-R's formulas and reproduce its published numbers (AUD-C7a) before the yield inputs are varied. **Literature:** 1803.02903 and 2303.02196 fetched
with lit.py into literature/papers-WP5-AUD/ and read in full text (PDFs and text extractions deleted). The arXiv IDs 1803.02903, 2303.02196, 1805.09942,
2007.14289, 2405.10405, 2004.11499, 2004.10709, 2001.06503, 2209.04503, 2206.13639, 1109.4343 and 2208.02790 were checked against the arXiv API
(arxiv-*.json there; all exist and the titles match). INSPIRE citation walk on 2303.02196 (recid 2638592, 40 citing records): no newer Si sub-keV yield
measurement by title. Tags per CONVENTIONS §12. No first-principles numerics. Status: CLAIMED (one audit), pending R×2.

## 0. Rulings at a glance
| # | Item | Ruling |
|---|---|---|
| 1 | A-1…A-16 in WP5-v4 | all 16 applied faithfully (§1.1). The one place WP5-v4 goes beyond the amendment, (W11′), is correct. Ledger closes at t_pr. **At t_win the pre-sensor deficit D′ of E (E7)/A-4/(W11) lacks E_pairs(t_win) + E_X(t_win)** (S, D-1). Pre-t_pr bias heat must be weighted once, by ϵ_NTL (W, D-2) |
| 2 | IF-R13-2 | **CONFIRMED.** The κ_cal weights are exact only at r_coll = 1. General form: 1 − η^φ_NR = g_Luke(r_coll − 1)(1 − y_ion)/(1 + r_collg_Luke) + [(1 + g_Luke)/(1 + r_collg_Luke)]·[δ_coll + d′_NR − κ_cal(r_coll)d′_ER] + O(2), κ_cal(r) ≡ (1 + rg_Luke y_ion)/(1 + rg_Luke). The E_st bounds are unchanged, exactly as well as at first order (AUD-C1, C2). Corrected L38 text in §2 |
| 3 | IF-R13-3 | **CONFIRMED.** Both ends must be quenched. The protocol text is in §3.1 |
| 3′ | IF-R13-5 | **CONFIRMED with two changes:** the r_coll prior (σ_ln 0.05) is too narrow (S, D-4); the θ_𝒦 one-path statement has the wrong uniqueness condition (W). The WP6-v3 row text is in §3.2 |
| 4 | G-R3, G-R4 | amendment text for WP5 §2, §3.3 and §3.4 in §4 |
| 5 | WP8-R, WP8-F | 9 + 9 statements ruled (§5). **The WP8-R verdict survives:** NO-GO for (a) and for (c) at E_R ≤ 300 eV, and (d) CONDITIONAL with lower ζ_O,min. But the (c) NO-GO now rests on the measured F_NR ≳ 0.4: the ceiling reaches 1.999 at the edge of the measured bands, and WP8R-C7l's "robust at F_NR = 0.15" fails |
| 6 | Defects | 17 rows, §6 |

---
## 1. Cross-package consistency (Required 1)
### 1.1 A-items as applied in WP5-v4 (its §R13.1–§R13.2) against E §5
| A | E §5 content | WP5-v4 site | Status |
|---|---|---|---|
| A-1 | type "trapped on j", 𝒦_cap, per-carrier deposit once at t_pr, excitons post-prompt; (W4) scope and general (E1-pr) | §1.2 Statement, Exact bookkeeping, (W4), (W4′) | CONSISTENT; (W4′) = (E1-W4) with E_x → ΔE_X^b (AUD-C3a,b re-derive it from (E1-pr) + neutrality) |
| A-2 | additive 𝐍; marks 𝔪 | §1.2 | CONSISTENT; NOTATION §G row stale (IF-R13-1, D-15) |
| A-3 | E_st configurational; ΔZPE in ℋ_ph; ⟨E_st(t)⟩, T-1; E_d via P_FP | §3.2 + [v4] quench reading | CONSISTENT; the [v4] reading is required (§3.1) |
| A-4 | multiplicative Y_H(t_win), NTL ratio, unit quenching, η^φ_NR sentence | §3.4 (W11) + (W11′) | text faithful; the last sentence inherits E's r = 1 weights (D-3). (W11′) correct (AUD-C1a). D′ incomplete (D-1) |
| A-5 | N^meas = Σ𝔮_i; QF via ⟨𝔮⟩; 1803.02903 efficiency reading | §3.3 last bullet | CONSISTENT; quote p. 3 verified [FT, 1803.02903 PDF p. 3] |
| A-6 | (W12) ⊗ 𝒯_𝔠, visibility, sub-threshold releases, WP7-T-v2 rates below T_× | §4 | CONSISTENT; ΔZPE_ij = ΔZPE_i − ΔZPE_j has the WP7-T-v2 §4.1 sign. The thresholds are ranges, not points: E_thr ≤ 2.1–2.7 eV, N_a ≳ 272–543 (D-12, AUD-C5) |
| A-7 | SC absorber / film bookkeeping | §5 | CONSISTENT |
| A-8 | (F) implicit Lindhard assumptions | §6.1 step 4 | CONSISTENT |
| A-9 | NRT 0.8; f_DF combination; bound 0.20 with (B-a)–(B-d); TRIM UNRESOLVED | §6.3 | CONSISTENT; numbers re-checked (AUD-C11) except "p_surv ≲ 0.48" (ΔZPE), which is a rounding artefact (0.475; D-13) |
| A-10 | (W14) validity, ℋ_eff, F_meas^{obs} | §6.4 | CONSISTENT |
| A-11 | θ_esc escape only; θ_tr^{pr}; E §6 rows | §8 | CONSISTENT as copied; E's θ_coll prior is defective (D-4) |
| A-12 | (B3) pre-t_pr bias work in 𝒲_bias and ℋ | §1.2 (B3) | CONSISTENT as a ledger entry; observable weighting missing (D-2) |
| A-13 | §6.4 leading corrections | §6.4 | CONSISTENT |
| A-14 | §9 R6 | §9 | CONSISTENT |
| A-15 | N_trap restriction | Symbols | CONSISTENT; NOTATION row owed (D-15) |
| A-16 | (W6) → dℛ/d𝐌 with P(𝐌, t\|Λ) | §1.3 | CONSISTENT; t_pr marginal kept |
WP5-v4's K1–K17 conflict table is correct: every conflict is resolved in favour of E. Its §R13.3(a) T-1 table agrees with WP7-T-v2 §5.3 (i)–(v),
including E^{conf}(𝔅₀) = 0 in the index set. T-1's E_st^{unrel} ≡ Σ_iN_iE^{conf}_i − E^{conf}_0 forces the 𝔅₀-minimum reference of §3.1.

### 1.2 Energy-ledger closure and double counting [D]
- **Configurational E_st, ΔZPE inside ℋ_ph (CONVENTIONS §13 row 23).** (W4) reads ω = N_ehE_g + (ℋ_ph^{avail} + ΔZPE) + E_st^{conf} + E_esc, so ΔZPE is
  counted once, inside ℋ. D′ carries ΔZPE(t_win) because ΔZPE cannot reach a sensor. The release argument ε^{hop} + ΔZPE_ij is used only in 𝒯_𝔠, and
  (W12)'s δ-argument stays configurational. This is consistent, and the ZPE sum rule telescopes separately (WP5v4-C38, E C16). A classical MD has no
  ΔZPE: its heat ℋ_MD equals ℋ_ph, and ℋ^{avail} = ℋ_MD − ΔZPE needs the end-basin Hessian (§3.1 step 4).
- **E_d** appears only in (W10), P_FP and N_FP^{NRT}, and is never booked as N_FP·E_d (E Theorem E-1). CONSISTENT.
- **E_g.** At t_pr, E_g is booked once per created pair, as N_ehE_g + E_pairs^{unp} + E_trap^{pr} + ΔE_X^b. This sum is μ_F-independent (AUD-C3a,b). The v3 term
  ⟨N_trap⟩E_g is gone from (W11). **But at t_win**, (E1) gives the sensor-available phonon energy as ω − [E_pairs + E_X + E_trap + E_es + E_st + ΔZPE +
  E_esc](t_win) + NTL heat. E (E7) and A-4/(W11) define D′ without E_pairs(t_win) + E_X(t_win). So Y_H = (1 − δ_coll)(ω − D′_NR)/(ω − D′_ER) holds only
  once every pair has recombined or been collected by t_win (AUD-C3c). In a zero-field calorimeter with unreleased gap energy the omitted term is
  +(1 − y)E_g/ε_eh·(1 − P_g(t_win)), i.e. **+0.28 at 100 eV in Si** (AUD-C3d). That is WP8-R's channel (b). **D-1 (S).** The L36–L38 numbers are
  unaffected, because in the two-channel data the pairs are collected well inside the phonon window (E §3.4 table).
- **Bias work.** 𝒲_bias = eV_bN^meas is on the left-hand side of (E1). The pre-t_pr part 𝒲_bias(t_pr) (≤ 0.25 eV per carrier, A-12) sits inside ℋ_pr and inside
  ℋ_eff as −𝒲_bias(t_pr), which is consistent. In (E7)/A-4, though, "NTL heat" is the whole drift work, so the pre-t_pr part must be collected with
  ϵ_NTL and kept out of the ϵ_prim argument ω − D′. Weighting ℋ_pr by ϵ_prim would count it twice (AUD-C3e). **D-2 (W).**

## 2. IF-R13-2: ruling and corrected LIMITS L38 (Required 2)
**Model.** This is 1803.02903's own procedure [FT]. E_φ = E_R + E_QeV_b/ε (Eq. (1), PDF p. 6). "The energy scale for the phonon channels is calibrated using a
sample of bulk electron recoils, which should have unity ionization yield" (p. 8). The MC recoil energies "are rescaled to E′_MC = E_MC η^φ_NR" and
compared with E_R = E_φ − E_Q(eV_b/ε) (pp. 6, 15). So η^φ_NR = E_R^{rec}/ω. With E (E7) signals, S_ER ∝ (1 − d′_ER) + r_collg_Luke and
S_NR ∝ (1 − δ_coll)(1 − d′_NR) + r_collg_Luke y_ion. Exact sympy (AUD-C1a) gives

  1 − η^φ_NR = g_Luke(r_coll − 1)(1 − y_ion)/(1 + r_collg_Luke) + [(1 + g_Luke)/(1 + r_collg_Luke)]·[δ_coll + d′_NR − κ_cal(r_coll) d′_ER] + O(d′², δ_colld′, δ_coll²),
  κ_cal(r_coll) ≡ (1 + r_collg_Luke y_ion)/(1 + r_collg_Luke),   κ_cal ≡ κ_cal(1) = (1 + y_iong_Luke)/(1 + g_Luke).                                         (AUD-1)

This is WP5-v4 (W11′) written in factorised form; the two are identical (AUD-C1a). **Ruling: IF-R13-2 is correct.** The weights of E (E13), L38 and A-4
are exact at first order only at r_coll = 1. At r_coll = 1.144 they are 0.931 and κ_cal(r) = 0.618 (w·κ = 0.576), against 1 and 0.642 (AUD-C1d). A-4's
mixed sentence, which combines the r_coll-term with r = 1 weights, is off by O((r_coll − 1)d′). The sample point in AUD-C1e gives 1.1×10⁻³ against
the general form's 2×10⁻⁵. **Bounds:** with δ_coll = X^{oth} = 0 the identity 1 − η − E_st/ω = g_Luke(r − 1)(1 − y_ion − E_st/ω)/(1 + rg_Luke) is **exact,
not only first order** (AUD-C2a). A 2×10⁴-point exact scan confirms E_st/ω ≤ 1 − η under (B-a), (B-b), (B-d) and (B-c) with κ_cal(r) (AUD-C2b). Since
dκ_cal/dr < 0, E's (B-c) with κ_cal(1) is sufficient for r ≥ 1 (AUD-C1c, C2c). The 0.055/0.064 bounds stand.

**Corrected LIMITS L38 (proposed text, replaces the Chain and Validity cells):** "η^φ_NR = 1 − g_Luke(r_coll − 1)(1 − y_ion)/(1 + r_collg_Luke) −
[(1 + g_Luke)/(1 + r_collg_Luke)]·[δ_coll + d′_NR − κ_cal(r_coll)d′_ER] + O(d′², δ_colld′, δ_coll²), κ_cal(r_coll) = (1 + r_collg_Luke y_ion)/(1 + r_collg_Luke)
(= κ_cal at r_coll = 1, giving 1 − δ_coll − d′_NR + κ_cald′_ER); η₀(r_coll) = 1 + g_Luke(1 − r_coll)(1 − y_ion)/(1 + r_collg_Luke); g_Luke = 4/3.82 [FT]
(WP5-v4 (W11′), AUD-C1) | ER calibration at the same field; multiplicative collection; first order in d′, δ_coll (the δ_coll = X^{oth} = 0 identity is
exact, AUD-C2a); bounds need (B-a), (B-b), (B-d) and X^{oth}_NR ≥ κ_cal(r_coll)X^{oth}_ER, implied by X^{oth}_NR ≥ κ_calX^{oth}_ER for r_coll ≥ 1". The same
change applies to A-4's last sentence, E §6 "Exact constraints", the L36 Validity cell (κ_cal → κ_cal(r_coll), or the "implied by" clause) and WP8-F §4.1
(D-3). The A-4/E §6 constraint sentence should read: "η^φ_NR = 0.952 constrains g_Luke(r_coll − 1)(1 − y_ion)/(1 + r_collg_Luke) + [(1 + g_Luke)/(1 +
r_collg_Luke)](δ_coll + (D′_NR − κ_cal(r_coll)D′_ER)/ω) = 0.048."

## 3. IF-R13-3 and IF-R13-5 (Required 3)
### 3.1 IF-R13-3: E_st quench protocol, CONFIRMED
T-1 (ii) and the definition E_st^{unrel} = Σ_iN_iE^{conf}_i − E^{conf}_0 need E^{conf} differences between basin minima. A Wigner-sampled R_I(0) has
⟨V⟩ = ω/4 per mode, i.e. 3⟨ω⟩/4 = 34 meV per atom, or **138 eV per 4096-atom cell** (AUD-C4 re-derives WP5v4-C39). WP5-v4's reading
E_st ≡ E^{conf}(R_final^{min}) − E^{conf}(𝔅₀^{min}) is therefore necessary. **Protocol text owed in WP5 §3.4 (Partition tables) and §4 (Barriers):** "(1)
E^{conf}(𝔅₀^{min}) is the relaxed perfect cell, computed once per MLIP, cell and boundary condition. It is never taken from the sampled R_I(0). (2) At
t_pr, R_final is quenched by steepest descent or FIRE at fixed cell, with no finite-T annealing and no barrier crossing. The basin assigned is the
one of R_final(t_pr), and the same label enters p_st (WP7-T-v2 (5.1)) and the NEB end states. (3) One MLIP, cell size, boundary condition and
reference energy serve E_st, p_st, the §4 NEB end states and 𝒦^{rel}. A cell-size elastic correction is stated once and applied to all three
alike. (4) ΔZPE of the end basin comes from the harmonic Hessian at both minima. It is recorded separately and booked in ℋ_ph, never in E_st.
ℋ^{avail} = ℋ_MD − ΔZPE, where ℋ_MD includes the energy absorbed by the boundary thermostat. (5) The MLIP-versus-DFT spread of E^{conf} differences
is θ_PES." The residual G-E3 (one shared E^{conf} table) is closed as a specification and stays open as a computation.

### 3.2 IF-R13-5: WP6-v3 nuisance rows, and the exact row text owed
**Rulings.** (a) θ_coll's median-1 prior does put half its mass outside (B-a)/(B-b). That is correct and harmless if WP6 reports two objects, as
WP5-v4 asks. (b) **New, S (D-4).** σ_ln = 0.05 on r_coll puts E's own degenerate point r_coll = 1.144 at 2.69σ (tail 0.36%). It also puts WP8-R's
|r_coll − 1| ≲ 0.2 (sign open, §6 there) at 3.6σ. The prior therefore pre-decides E's statement that the data "cannot distinguish" the two readings.
On the same datum with r_coll ≥ 1, the posterior median of E_st/ω is 0.036 for σ_ln = 0.05 and 0.026 for σ_ln = 0.2. P(E_st/ω < 0.01) is 3% and 18%
(AUD-C8). (c) θ_𝒦 for a one-path class: the moment matrix of φ = (1, E) is singular. λ is then not unique, but S(θ) is unique, and the tilt acts only
on the time shape, degenerate with θ_λ/θ_law (AUD-C9). WP5-v4's conclusion stands. Its reason, "≥ 3 support points", is the condition for
φ = (1, y_R, y_R²). For two constraints the condition is ≥ 2 distinct ε^{hop} with ε_min < E_st^{rel}/⟨N_hop⟩ < ε_max (W, D-5). (d) The η^φ_NR exact
constraint uses (AUD-1).
**WP6-v3 §5.2 rows owed** (replace the "Yield / cascade" and "Fano factor F_eh" rows; append the rest after "Cascade band edge θ_Eg"):
| Level (τ slot) | Template Δ^τ_k | Type | Prior | Correlation | Source of Δ^τ_k |
|---|---|---|---|---|---|
| Yield / cascade (WP5-v4 §8) | {step(ε_eh), R&K, URF cascade} until the URF cascade is computed, then θ_seed (no prior bound; computed), θ_{R-k} (computed), θ_GW (±20%), θ_Z (0.8–1, global, M; correlated with θ_GW), θ_exch (computed), θ_PES, θ_LZ, θ_dense ([C]) | Δ + M | ε_eh: 𝒩(3.75, 0.05) eV (Si, 130 K) [E]; (W4′)/(W14) with ℋ_eff ties θ_GW, θ_Z, θ_{R-k} to the measured ε_eh and F_meas^{obs} (not F_eh) | material-wide | WP5-v4 (G1); WP5-AUD |
| Fano factor | width of P_casc(N_eh\|Λ); reported F_meas^{obs} = [F_eh⟨m_ind²⟩ + ⟨Var𝔮⟩]/⟨𝔮⟩ + ⟨N_eh⟩Var_r m_ind/⟨𝔮⟩ | M on the variance | F_eh = 0.119 ± 0.002 at 5.9 keV (2004.11499) is F_meas^{obs} at ϵ_det ≈ 1; near-gap prior uniform [0.1, 0.2] [E]; F_NR (Si): 0.9^{+0.7}_{−0.4} (100 eV), 0.5^{+0.2}_{−0.1} (220 eV), 1.8^{+0.6}_{−0.5} (460 eV) [FT, 2303.02196 Table II] | material-wide | WP5-v4 L23 (A-10) |
| θ_esc | escape only | M | per detector | detector | WP5-v4 §8 (A-11) |
| θ_tr^{pr} | prompt capture fraction | T on {0, 1}, (5.1″) with φ = (1) | f₀ = 10⁻³, ψ = ln 10.09 (1% at θ = 1) | material, field | E §6 |
| θ_unrel | E_st^{rel}/E_st per class | T (two-point) | central from WP7-T-v2 Γ on t_obs; ψ per σ_λ = 2 [E] | class, T | E §6 |
| θ_λ, θ_γ | Γ_path | M | σ_ln = 2σ_λ (σ_λ = 2) [E]; 2σ_γ/γ (0.3) [E] | material | WP7-T-v2 §4.6 |
| θ_𝒦 | shape of 𝒦^{rel} at ∫∫𝒦^{rel} = ⟨N_hop⟩, ∫∫E𝒦^{rel} = E_st^{rel} | T, (5.1″) with φ = (1, E) | 𝒩(0,1); **only for classes with ≥ 2 distinct ε^{hop} and ε_min < E_st^{rel}/⟨N_hop⟩ < ε_max; for one-path classes omit (absorbed by θ_λ/θ_law)** | class | E §6; WP5-AUD |
| θ_law | {1/t, t^{−3/2} 1D/3D, exp} (bimolecular excluded by T-1 (iv)) | Δ | discrete profiling | class | WP7-T-v2 |
| θ_st | ⟨E_st⟩/E_R scale | M | central MD (quench protocol WP5-AUD §3.1); one-sided caps 0.055 (Si) / 0.064 (Ge), 95% C.L., under (B-a)–(B-d), valid at 10–100 keV (Si) and 103 keV ²⁰⁶Pb (Ge) only | material | E §3.2 |
| θ_tr | ℓ^tr_{e,h}, track trap density | M | per-detector calibration; σ_ln 0.5 [E]; 1803.02903 efficiency only as a one-sided model-flagged product ≥ 0.75 (100 keV) | detector, flash state | E §2.3 |
| θ_em | athermal Γ^{em}_j | M | σ_ln = 2.3 [E] | detector, history | E §2.1 |
| θ_SC | field map, E_es | Δ + M | per exposure state | detector | E §2.1 |
| θ_coll | δ_coll and r_coll | M on (1 − δ_coll) and on r_coll | (1 − δ_coll): median 1, σ_ln 0.05; **r_coll: median 1, σ_ln 0.2 (sign open; WP8-R §6 \|r_coll − 1\| ≲ 0.2)** [E]; profiled jointly with θ_st through η^φ_NR | material–sensor | E §3.1; WP8-R §6; WP5-AUD |
| θ_X | exciton formation and recombination fractions; **gap-energy release P_g(t_win)** | T (two-point) | central from E §7 kinetics; f₀ ≥ 10⁻³ | material, field, T | E §2.1, §7; WP8-R IF-R2 |
| θ_bg,𝔠 | background reservoir amplitudes | A | log-normal per run, σ_ln 1 | run | E §3.3 |
**Exact constraint (add to WP6-v3 §6):** "η^φ_NR (1803.02903) fixes (AUD-1), the general-r_coll form of WP5-v4 (W11′), and ties θ_coll, θ_st, θ_tr and θ_esc. Report
(i) the profiled E_st constraint under the full priors and (ii) the conditional bound E_st/ω ≤ 1 − η under (B-a)–(B-d) separately."

## 4. Spec additions to WP5 owed by WP8-R G-R3 and G-R4 (Required 4; amendment text)
**B-1 (G-R3). §2 "Grid of outputs", append:** "For each cascade sample (or by the moment equations), record the created-phonon spectrum
dℋ/dω_ph(ω_ph; ν) = Σ_emissions ω_{Qν}δ(ω_ph − ω_{Qν}) − Σ_absorptions ω_{Qν}δ(ω_ph − ω_{Qν}). It is branch-resolved (ν = LA, TA₁, TA₂, LO, TO), on a 0.5 meV grid to
ω_max, and split into (i) the relaxation part above E_th^{ii}, (ii) the residual-kinetic part below ω_op (intravalley acoustic emission; this gives
WP8-R's f_s), (iii) capture heat E^tr (𝒦_cap) and (iv) pre-t_pr NTL heat 𝒲_bias(t_pr) (collected with ϵ_NTL, D-2). Sum rule per sample:
Σ_{(i)–(iv)}∫dℋ/dω_ph dω_ph = ℋ_pr. Absorbed thermal phonons carry negative weight (§3.1(i) sign rule). The spectrum is the mark dℋ_pr/dω_ph(r) of A-2,
with the spatial centroid and rms of each part." **§3.4 "Partition tables", append:** "At t_pr, before the quench, project the excess lattice state
onto the harmonic modes s of the quenched end state: E_s = ½(p_s² + ω_s²u_s²), dℋ/dω_ph = Σ_s(E_s − E_s^{(0)})δ(ω_ph − ω_s), branch-labelled by
eigenvector overlap with the perfect-crystal modes. E_s^{(0)} is the same projection of the Wigner R_I(0) state at t = 0, so the zero-point spectrum is
subtracted. Record the anharmonic residual ℋ_MD − ΣE_s (check: ≤ 10% at t_pr) and, separately, the energy absorbed by the boundary thermostat, with its
spectrum from the frequency-resolved flux into the thermostat layer (or record spectra in the NVE core before the front reaches the thermostat).
Classical occupation is used for the excess only. Validation: for x_R ≲ 1 the created-minus-absorbed spectrum must reproduce WP2 (3.6) ρ^{ph}_κ. Cost:
negligible beyond the MD."
**B-2 (G-R4). §3.3, new bullet "Charge yield below E_R,th":** "Tabulate the full P(N_eh | E_R, r̂_R, T), N_eh ≤ 30, on E_R ∈ [20 eV, 1 keV] (≥ 25
log points, dense around E_R,th = 352/395 eV), from MLIP-MD trajectories carrying stochastic excitation events drawn from the TDDFT
dP/dω_e(b_imp, E_coll) table (§3.4). Flag three channels separately: binary (above E_R,th), Landau–Zener promotion, and the momentum-tail linear
response. Convert each excitation through P_n(ω_e) of §2, never ω_e/ε_eh^γ (§6.1(b)). Use ≥ 500 trajectories per E_R point, so that a sample
variance is good to ≈ 6%. Outputs: 𝔶(E_R) ≡ ⟨N_eh⟩ε_eh/E_R (WP8-R's created-charge yield; y_ion = 𝔶⟨𝔮⟩_NR/⟨𝔮⟩_ER, A-5), P(N_eh = 0 | E_R), and
F_NR(E_R) = Var N_eh/⟨N_eh⟩ by the law of total variance, E[Var(N|seeds)] + Var(E[N|seeds]). F_NR = F_eh + Var(E_el)/(ε_eh⟨E_el⟩) (§6.4) is the
special case of an ε-constant conversion. Also record Corr(N_eh, ℋ) and Corr(N_eh, E_st) at fixed E_R. Nuisances θ_LZ, θ_PES; gap R3 stands.
Validation (not fit): Si, 2303.02196 Table II [FT, PDF p. 5]: Y = 0.102^{+0.034}_{−0.030}, F = 0.9^{+0.7}_{−0.4} (0.10 keV); 0.108^{+0.009}_{−0.010},
0.5^{+0.2}_{−0.1} (0.22 keV); 0.136^{+0.009}_{−0.008}, 1.8^{+0.6}_{−0.5} (0.46 keV). Their Y uses ε = 3.8 eV and takes the 0 V phonon energy as E_r
(E_t = E_r + n_eheV, Eq. (1), PDF p. 2), i.e. the L37 truncation; the ≤ 5.5% E_st bias (L36) is inside their errors. Ge: 2405.10405 (64 ± 8 eV_ee at
254 eV_nr, via E §4(b))."

## 5. Yield-dependent statements of WP8-R and WP8-F (Required 5)
### 5.1 WP8-R
| # | Site | Statement | Ruling |
|---|---|---|---|
| R-a | §1.1 | "ω = N_e^f(E_c − μ_F) + … + E_esc" (A-1 ledger) | NEEDS CORRECTION (W): left-hand side ω + 𝒲_bias(t_pr) (A-1); zero at zero field |
| R-b | §1.1, §1.3 | prompt phonon part ℋ ≈ ω(1 − E_g/ε_eh) (ER); ≈ E_R(1 − 𝔶E_g/ε_eh) (NR) | CONSISTENT with (W4′) at [E]; the NR form omits −E_st − E_esc (≤ 5.5%, L36) |
| R-c | §1.1 table, Symbols | 𝔶(100 eV) = 0.153/0.126 (Lindhard), "≠ source y of 1803.02903" | numbers reproduced (AUD-C6). NEEDS CORRECTION (W): 𝔶 equated with E_el/E_R is L20's N_eh = E_el/ε_eh^γ truncation, which WP5 §6.1(b) rejects for near-gap NR seeds; y_ion = 𝔶⟨𝔮⟩_NR/⟨𝔮⟩_ER. Use the measured Si Y(100 eV) = 0.102^{+0.034}_{−0.030} [FT, 2303.02196] until B-2 |
| R-d | §4.2 (a) | ΔO ≤ ζ_O(1 − 𝔶)f_s; 𝔖 = 0.38/1.15 at 100/300 eV; 2σ at 0.52 keV | CONSISTENT; with 𝔶 ∈ [0, 0.25], 𝔖 < 2 at ≤ 300 eV; 2σ first at ≥ 0.47 keV (AUD-C7b). NO-GO survives |
| R-e | §4.3 (b) | Δf_g = (1 − 𝔶)E_g/ε_eh = 0.26 | CONSISTENT; 0.28 (0.27–0.29) with the measured yield (AUD-C7e). This is the D-1 term: it enters Y_H(t_win) as +Δf_g(1 − P_g(t_win)) |
| R-f | §4.4 (c), C7g, C7l | HV NO-GO at any ζ_O for E_R ≤ 300 eV; "also holds at F_NR = 0.15" | NEEDS CORRECTION (S-for-the-claim, D-7): WP8-R evaluates 𝔶 = Lindhard(100 eV) at all energies and F_ER = F_eh. With the measured Y, S_int(300 eV, F_NR = 0.15) = 2.18 (AUD-C7c′). With energy-matched measured Y and F_NR, F_ER → F_meas^{obs} ∈ [0.119, 0.3] and g_Luke⟨𝔮⟩, the ceiling is ≤ 1.999 (AUD-C7c). The NO-GO survives, marginally, on F_NR ≳ 0.4 |
| R-g | §4.4 (d) | ζ_O,min = 0.15/0.28/0.53 at σ_pos = 0.02/0.05/0.10 | CONSISTENT in kind; 0.13/0.24/0.44 with Y = 0.102, F_NR = 0.9 (AUD-C7d). CONDITIONAL stands |
| R-h | §4.1, §4.4 caveats | F_ER = 0.15, F_NR = 1 [E]; σ_φ from pair number | NEEDS CORRECTION (W): ER spread is F_meas^{obs} ≥ F_eh (A-10); NTL gain g_Luke⟨𝔮⟩; F_NR now [FT] (R-f) |
| R-i | §6 | δ_prim ≤ 0.007 cannot carry the 0.048; r_coll ≠ 1 expected, \|r − 1\| ≲ 0.2 | CONSISTENT with (AUD-1): the δ_coll weight is ≥ 0.93 for r ≤ 1.2. It conflicts with E's θ_coll prior (D-4) |
Also N (D-8): WP8-R writes E's unrenamed δ, r, g (CORRECTIONS §18: δ_coll, r_coll, g_Luke), contrary to its header. **WP8-R verdict: survives.**
(a) NO-GO; (c) NO-GO at E_R ≤ 300 eV, conditional on the measured F_NR ≳ 0.4; (d) CONDITIONAL with ζ_O,min ≈ 0.24 at σ_pos = 0.05; overall NO-GO for the
brief's target.

### 5.2 WP8-F
| # | Site | Statement | Ruling |
|---|---|---|---|
| F-a | §2.1(d) | threshold in quanta "N_eh via ε_eh" (3.749 eV, F_eh 0.119, 123 K) | NEEDS CORRECTION (W): near threshold use P(N_eh\|q,ω) (WP5 (W5)–(W6), §2 output P_n(q,ω,T); L21 step model exact only in the forced region). ε_eh, F_eh are asymptotic (≳ 50 eV) and T-dependent beyond E_g(T) (WP5 §2). Measured charge: N^meas = Σ𝔮_i, F_meas^{obs} |
| F-b | §2.1(d) | charge readout needs ω ≥ E_g; NTL readout needs g_Luke gain | CONSISTENT |
| F-c | §2.4(b) | "E_th in nuclear-recoil energy (E_th^{ee}/QF)" | NEEDS CORRECTION (W): mean only, with QF = y_ion = 𝔶⟨𝔮⟩_NR/⟨𝔮⟩_ER (A-5). Phonon readout: E_th^{nr} = E_th^{ee}(1 + r_collg_Luke)/(Y_H + r_collg_Luke y_ion) (AUD-C10; zero field E_th/Y_H, unit by L37 within the 0.048 combination). Below 350 eV, data (2303.02196) until B-2 |
| F-d | §2.4(d) | "plus the NR partition (WP5 L20–L22; prov.)" | CONSISTENT, read with WP5-v4 (A-8, A-9) |
| F-e | §2.7 Migdal (d) | "As ER + NR" | NEEDS CORRECTION (W): add WP5 §3.1's rule. Neutron-calibrated yields contain Migdal: Y_tot = Y_casc[S^{GS}] + ∫P_casc dP_Mig, never Y_casc + Migdal |
| F-f | §2.8(d) | caps 0.055/0.064; 0.21/0.20; 0.47/0.66 (≤ 1% wider with ΔZPE); 𝓟_st upper-bound proxy | CONSISTENT (AUD-C11), with additions (W): the caps hold only at the calibration energies (Si 10–100 keV; Ge 103 keV ²⁰⁶Pb, surface). The event-seeded release power is ≤ 𝓟_st by T-1 (E_st^{rel} = E_st − E_st^{unrel}, E^{conf} ≥ E^{conf}(𝔅₀)) |
| F-g | §2.8(d) | single FP visible for E_thr ≤ 2.7 eV; pockets N_a ≳ 270 at 16.3 eV | NEEDS CORRECTION (W): ≤ 2.1–2.7 eV (E_st,1 = 7–9 eV); N_a ≳ 272–543 (0.2–0.1 eV/atom) (AUD-C5) |
| F-h | §4.1 last row; §4.2 | θ_st, θ_coll joint via η^φ_NR; L38 degeneracy | NEEDS CORRECTION (W): the joint profile uses (AUD-1), and θ_coll takes the r_coll width of §3.2 |
| F-i | §5.2 rows "E_d, E_st,1, p_surv", "ε_eh, F_eh, y_ion, QF" | source WP5-v3/WP7-E-v3; needed 2% (ε_eh) | NEEDS CORRECTION (W): source WP5-v4 + this audit; E_st via the §3.1 protocol; y_ion/QF as ⟨𝔮⟩ ratios; sub-350 eV from 2303.02196 until B-2 |
With these corrections the WP8-F "(prov.)" rows may be used by WP8-U (IF-F3 answered).

## 6. Defect list (Required 6)
| ID | Owner | Sev | Exact fix |
|---|---|---|---|
| D-1 | WP7-E-v3 (E7), (E8); WP5-v4 A-4/(W11) | S | D′ ≡ E_st(t_win) + **E_pairs(t_win) + E_X(t_win)** + E_trap(t_win) + E_es^{trap} + ΔZPE(t_win) + E_esc. Add: "E_pairs, E_X vanish once all pairs have recombined or been collected by t_win; otherwise the bracket of (W11) gains ⟨ΔE_pairs⟩ + ⟨ΔE_X⟩ (zero field: −(1 − y)E_g/ε_eh·(1 − P_g(t_win))ω)". L36–L38 numbers unchanged |
| D-2 | WP5-v4 (B3)/A-12, (W11); E (E7) | W | append to A-12: "in (W11)/(E7) the pre-t_pr bias heat is NTL heat, weighted by ϵ_NTL, and is excluded from the ϵ_prim argument ω − D′" |
| D-3 | LIMITS L38 (Chain, Validity), L36 (Validity); E (E13) remark, §6 Exact constraints; WP5-v4 A-4 last sentence; WP8-F §4.1 | S (A-4/E §6 sentence), W (L38) | replace by (AUD-1) / the §2 texts |
| D-4 | E §6 θ_coll; WP5-v4 §8; WP6-v3 (new row) | S | r_coll prior σ_ln 0.05 → 0.2 (sign open), §3.2 row |
| D-5 | WP5-v4 §R13.3(b) θ_𝒦 note; IF-R13-5 | W | "≥ 3 support points" → "moment matrix of (1, E) singular for one ε^{hop}; interior condition ε_min < E_st^{rel}/⟨N_hop⟩ < ε_max with ≥ 2 distinct ε^{hop}" |
| D-6 | WP6-v3 §5.2 | S | add the §3.2 rows and exact constraint |
| D-7 | WP8-R §0 row 6, §4.4, C7l, IF-R4 | S (claim) | "NO-GO at any contrast for E_R ≤ 300 eV" → "… given the measured F_NR ≳ 0.4 (2303.02196); the ceiling is 1.999 at the band edge; at F_NR = 0.15 it reaches 2.18 at 300 eV"; use energy-dependent measured Y |
| D-8 | WP8-R throughout | N | δ, r, g → δ_coll, r_coll, g_Luke (CORRECTIONS §18) |
| D-9 | WP8-R §1.1 | W | 𝔶 vs y_ion relation and the E_el/ε_eh^γ caveat (R-c); A-1 left-hand side 𝒲_bias (R-a) |
| D-10 | WP8-R §4.1 | W | F_ER → F_meas^{obs}; g → g_Luke⟨𝔮⟩ (R-h) |
| D-11 | WP8-F §2.1(d), §2.4(b), §2.7(d), §5.2 | W | F-a, F-c, F-e, F-i texts |
| D-12 | E §0 row 13, §3.3(b′); WP5-v4 A-6/C41; WP8-F §2.8(d) | W | "N_a ≳ 270" → "N_a ≳ 270–540 (0.2–0.1 eV/atom)"; "E_thr ≤ 2.7 eV" → "≤ 2.1–2.7 eV" |
| D-13 | E §3.2; WP5-v4 §6.3, C35; LIMITS L36; WP8-F §2.8 | W | p_surv(Si, ΔZPE) "≲ 0.48" → "≲ 0.475" (0.48 only after rounding 0.0556 → 0.056) |
| D-14 | WP5 §3.4, §4 (spec) | S | quench protocol §3.1 (IF-R13-3) |
| D-15 | NOTATION §G | N | IF-R13-1 rows (𝐍 per A-2; N_trap per A-15; Y_H(t_win) as NR/ER signal ratio); add κ_cal(r_coll) |
| D-16 | WP5 §2, §3.3, §3.4 (spec) | S | B-1, B-2 (§4) |
| D-17 | WP8-F §2.8(d), θ_st | W | caps valid at calibration energies only; release power ≤ 𝓟_st (T-1) |

## 7. Provenance of values used
| Value | Tag | Source |
|---|---|---|
| E_φ = E_R + E_QeV_b/ε; ε = 3.82 eV above 77 K; 4 V, 4 V/cm; ER phonon calibration "unity ionization yield"; η^φ_NR = 95.2^{+0.9}_{−0.7}% (95% C.L.); E′_MC = E_MCη^φ_NR | [FT] | 1803.02903 PDF pp. 6, 5 (fn. 2), 5, 8, 17, 15 |
| Si Y, F at 0.10/0.22/0.46 keV; E_t = E_r + n_eheV, ε = 3.8 eV; trapping 12.7%, impact ionization 0.6% | [FT] | 2303.02196 Table II (PDF p. 5); Eq. (1) (p. 2); p. 4 text |
| g_Luke = 4/3.82, y_ion = 0.3, κ_cal = 0.642, r_coll = 1.144 | [FT]/[E] | as E §3.1 |
| f_DF = 6.08 ± 0.18% (Ge) | [FT via E, WP5-v4] | 1805.09942 |
| E_dam/E_R, E_st,1, E_d, ⟨ω⟩ = 45 meV, ϵ_coll = 0.3, pocket 0.1–0.2 eV/atom | [E]/[UNVERIFIED] | E §3.2–§3.3, WP5-v4 §R13.5 |
| E_g = 1.17 (Si), ε_eh = 3.75 eV, f_s = 0.017, σ_ph = 2.65 eV | [FT via WP8-R]/[E] | WP8-R Table 1.1, §4.1 |
| ε_eh = 3.749 eV, F_eh = 0.119 ± 0.002 (5.9 keV, 123 K) | [FT via WP5-v4] | 2004.11499 |
| Lindhard k, g(ε) | [FT via WP5-v4 §6.1] | 2001.06503 Eqs. (4), (7) |

---
## Symbols introduced/used
*Used as defined (NOTATION v4, "Rows added WP7", "Rows added WP7-E"):* ω, E_R, E_g, E_c, E_v, μ_F, ε_eh, F_eh, F_NR, F_meas^{obs}, N_eh, N_e^f, N_h^f,
N_e^{tr}, N_h^{tr}, N_X, ΔE_X^b, E_pairs, E_pairs^{unp}, E_X, E_trap, E_trap^{pr}, E_es, E_es^{trap}, E_st, E_st^{rel}, E_st^{unrel}, E_st,1, E^{conf}, E^ad_0, ℋ, ℋ_ph,
ℋ_ph^{avail}, ℋ_pr, ℋ_eff, ΔZPE, ΔZPE_ij, ε^{hop}_ij, E_esc, E_sig, 𝒲_bias, ℰ_b, D′, d′, X^{oth}, δ_coll, r_coll, ϵ_prim, ϵ_NTL, ϵ_coll, κ_cal, g_Luke, y_ion,
η^φ_NR, η₀(r_coll), 𝔮, m_ind, N^meas, t_win, t_obs, t_pr, P_rel, E_thr^det, 𝒦^{rel}, ⟨N_hop⟩, 𝔅₀, R_final^{min}, 𝔅₀^{min} (WP5-v4), p_st, P_FP, E_d, p_surv,
E_dam, N_a (E), P_casc, P_n, 𝔶 (WP8-R), 𝔖, 𝔖_int, ζ_O, σ_pos, f_s, Δf_g (WP8-R), 𝓟_st (WP8-F), θ_* (E §6, WP5-v4 §8), Y_H, V_b. Source-only: 1803.02903 ε, y,
E_φ, E_Q; 2303.02196 Y, F, E_t, n_eh.
*Introduced here (checked against NOTATION for collisions):*
| Symbol | Meaning | Where |
|---|---|---|
| κ_cal(r_coll) | (1 + r_collg_Luke y_ion)/(1 + r_collg_Luke); the existing κ_cal ≡ κ_cal(1) | (AUD-1), §2 |
| P_g(t_win) | fraction of the created-pair gap energy (free pairs and E_X) returned to phonons by t_win | §1.2, D-1 |
| E_s, E_s^{(0)} | harmonic-mode energy of the quenched end state at t_pr; its Wigner (t = 0) value | B-1 |
| (AUD-1), B-1, B-2, D-1…D-17, R-a…R-i, F-a…F-i, AUD-C1…C11 | labels (prefix WP5-AUD) | — |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-AUD-1 | WP7-E (next revision) / WP5 | D-1, D-2, D-3 | apply; WP5-v4 A-4/(W11)/(B3) take the same text |
| IF-AUD-2 | WP6 | D-4, D-6 | add the §3.2 rows and the exact constraint; report profiled and conditional E_st objects separately |
| IF-AUD-3 | WP5 | D-14, D-16 | adopt §3.1 protocol and B-1, B-2 in §3.4/§4/§2/§3.3 |
| IF-AUD-4 | WP8-R | D-7…D-10 | correct the (c) robustness claim; measured Y, F_NR; renames |
| IF-AUD-5 | WP8-F, WP8-U | D-11, D-17; IF-F3 | (prov.) rows released with the §5.2 corrections |
| IF-AUD-6 | coordinator: LIMITS, SOTA | D-3, D-12, D-13 | L38/L36 texts; SOTA: "the HV phonon-PSD NO-GO at ≤ 300 eV rests on the measured F_NR ≳ 0.4 (2303.02196)" |
| IF-AUD-7 | NOTATION | D-15 | IF-R13-1 rows; κ_cal(r_coll), P_g |
| IF-AUD-8 | coordinator: CORRECTIONS §18 | WP5-v4 | mark "WP5-v4 audited (R14 WP5-AUD)"; IF-R13-2, -3, -5 resolved here; IF-R13-4, -8 stand as noted |

## Proposed LIMITS rows
| # | Change | Status |
|---|---|---|
| L38 ✎ | Chain/Validity as §2 (general-r_coll first order, κ_cal(r_coll)) | DERIVED (AUD-C1, C2; WP5v4-C34), pending R×2 |
| L36 ✎ | Validity: X^{oth}_NR ≥ κ_cal(r_coll)X^{oth}_ER (implied by κ_cal for r_coll ≥ 1); p_surv(Si, ΔZPE) ≲ 0.475; caps valid at the calibration energies only | DERIVED (AUD-C2c, C11) |
| L37 ✎ | Validity: add "all created pairs recombined/collected by t_win (else the ΔE_pairs + ΔE_X term of D-1)" | DERIVED (truncation; AUD-C3c) |
| L42 (WP8-R, provisional) ✎ | Leading correction: "measured Y(E_R) and F_NR (2303.02196) replace Lindhard; HV ceiling < 2 at ≤ 300 eV needs F_NR ≳ 0.4" | E (AUD-C7c, C7c′) |
| new (coordinator assigns) | 2303.02196 Si NR ionization yield 0.1–3.9 keV: URF chain B-2 (P(N_eh\|E_R) via §3.3 channels) against Table II; its Y is the L37 truncation of the URF ratio | OPEN (B-2 not computed) |
