# R12 verification VER-WP7-E-A: returns/R12/WP7-E-v2.md against referees/R11/REF-WP7-E-A.md

Read: WP7-E-v2 (460 lines); code/WP7-E-v2/checks.py, run 36/36 PASS (≈2 s); WP7-T-v2 §4.3 and §5.3 (Theorem T-1); WP5-v3 target strings.
1803.02903 re-fetched to check the new quotes (literature/papers-r12-VER-WP7-E-A/, deleted afterwards).

## 1. R11 items
| R11 item | Verdict | Note |
|---|---|---|
| 1 (E1) μ reference, reservoirs, vacuous checks | RESOLVED, with NEW ERROR (§3.1) | μ_F, E_x, E_es and ΔZPE added. C2a–C2d are genuine two-route checks: field energy = G-sum + V²/2d, battery work = ΔE_es + heat, Ramo with space charge. C2e still only checks endpoint zeros (harmless). New error: E_x is double-booked, or else the exciton's E_g is lost |
| 2 (E3) sufficiency; marks | RESOLVED | (H-E6) is stated as a hypothesis, G-E9 records its residual, and 𝔪 is a marked law |
| 3 E_d once; E_st^{frz} vs ∫^∞; stimulated channels | RESOLVED, with NEW inconsistency (§2) | E6 is cut at t_obs and 𝒦^{rel}(…; Φ_ph, n_car) is added. ΔZPE in E_st does not match WP7-T-v2's E^conf |
| 4 Theorem E-2 "exactly" | RESOLVED | creation only. The 0.2 MeV knock-on threshold checks: 2E(E+2m_e)/M_Si = 20 eV at E ≈ 0.21 MeV |
| 5 singly trapped carrier | RESOLVED | C1c,d; Table 3.4; A-4 |
| 6 (E11) multi-electrode | RESOLVED | Σ_kV_kΔQ_k. NTL heat = 𝒲 − ΔE_es (C2d) is correct |
| 7 F_meas position term | RESOLVED | I re-derived (E12) by the law of total variance; it is exact, given N_eh independent of r |
| 8 ER calibration in two-channel and y^meas | RESOLVED, with NEW ERRORS (§3.2) | I re-derived η^φ_NR = 1 − d_NR + κd_ER, κ = (1+yg)/(1+g) = 0.641 (g = 4/3.82, y = 0.3). The §3.2 "measured combination" drops a (1−κ)D_ER term, and the bound numbers are not consistent with each other |
| 9 (E8) ΔE_trap, normalisation, monotonicity | RESOLVED | ratio form; C9a–c correct |
| 10 ħc ×100 | RESOLVED | constant 1.97327×10⁻⁵ eV·cm, F = 1.19×10⁴ V/cm. Poole–Frenkel √(e³ℰ/πε) = 2.2 meV at 100 V/cm (Si) checks |
| 11 TLS per λ; pockets; selective quotes | RESOLVED | C12a total = per-λ × ½ln(Γ_max/Γ_min). Pocket N_a ≳ 16/(0.3×0.2) = 267 checks. The stress null and the single-exponential rejection are now quoted. Threshold comparator is the Si CPD |
| 12 3D correlated recombination | RESOLVED | C3d,e solve the diffusion problem with an absorbing sphere |
| 13 literature limits | RESOLVED, with NEW ERROR (§3.3) | NRT label, f_DF content, 2007.14289 next sentence and QF-as-ratio all fixed. The new 1803.02903 "⟨𝔵⟩_NR/⟨𝔵⟩_ER" reading is wrong |
| 14 WP5 amendment | mostly RESOLVED; NEW ERRORS in A-1 and A-10 (§4) | — |
| 15 nuisances (prompt trapping) | RESOLVED, with NEW ERROR (§3.4) | θ_tr^{pr} with f₀ = 0 cannot move |
| 16 computation spec | PARTLY RESOLVED | cascade capture and G4CMP added. The closing table says excitons were added to §7, but §7 has no exciton or EHD formation kinetics (G4CMP does not model them). NOT RESOLVED (minor) |
| L33–L38 | RESOLVED | Hecht source now UNVERIFIED; validity and leading-correction columns supplied. Fix the L36/L38 numbers per §3.2 |
| rubric (c): 2004.10709 CONFIRMED; TRIM UNRESOLVED | RESOLVED | carried over correctly |
| §7 symbol clashes | RESOLVED | 𝔠, μ_F, ℰ_b, D_diff |

## 2. (E6) against WP7-T-v2 Theorem T-1
- **Consistent in form.** T-1 (5.3): ∫₀^{t_obs}∫E𝒦^{rel} = E^conf_c − Σ_iN_i(t_obs)E^conf_i = E_st − ⟨E_st^{frz}⟩. This is (E6) with the same t_obs cut and the
  same frozen-energy definition. Its conditions (i) uphill hops included, (ii) one E^conf table, (iii) photon branch kept in E are
  compatible with WP7-E-v2 §1.3/§1.5. (E6) is therefore an **identity**, not the "constraint on WP7-T's path tables" that §1.5, IF-E2 and
  G-E3 still call it (written before T-1 existed). **Update:** call (E6) "identity under T-1 (i)–(iii)", and close IF-E2 and G-E3 down to condition (ii).
- **Normalisation mismatch.** T-1: ∫∫𝒦^{rel} = ⟨N_hop⟩, not 1, and the single-path Σ𝒫Γe^{−Γt} form is only the one-hop case. WP7-E-v2 §1.5 ("∫Γe^{−Γt} = 1")
  and the θ_𝒦 constraint "∫𝒦 = Σ𝒫" (§6) use the one-hop normalisation. Replace the latter by ∫∫𝒦 = ⟨N_hop⟩.
- **Mean versus event.** T-1 holds for the mean populations N_i(t). (E5) therefore gives ⟨E_st(t)⟩, not the event-by-event E_st(t) that (E1) is stated
  for. Write (E5) as an expectation, or give the event-level process as a sampled hop sequence with the same mean.
- **Stimulated channels.** T-1 is proved for the master equation (W12) with rates Γ_ij(T). The telescoping proof also holds for time-dependent rates
  Γ_ij(t; Φ_ph, n_car), but WP7-T-v2 does not state this. Add one line to IF-E2 asking WP7-T-v2 to say so.
- **NEW inconsistency (ΔZPE).** WP7-E-v2 (A-3, §1.1) redefines E_st = ΔE^ad_0 + ΔZPE. T-1 and WP5 (W12) use E^conf_i ≡ E^ad_0(R_i), purely
  configurational, so (E6) = (E_st with ZPE) − (E_st^{frz} without ZPE) is off by ⟨ΔZPE⟩ of the frozen states (~0.1 eV per defect, [E]).
  **Fix:** either E^conf_i in WP7-T-v2 includes the basin ZPE (preferred: it is the T → 0 free energy that hops conserve), or A-3 drops ΔZPE.
  One choice must hold across WP5, WP7-T and WP7-E.

## 3. New errors
1. **Exciton bookkeeping (§1.1, §1.2, A-1).** E_pairs runs over "unbound free carriers" and N_eh counts "fully free pairs", while E_x = −ΣE_x^b.
   Under that definition a bound exciton contributes only −E_x^b to (E1), and its E_g appears in no reservoir. The ledger row "E_pairs → E_x + ℋ_ph (E_x^b)"
   instead assumes the bound carriers stay in E_pairs. **Fix:** E_pairs (and N_eh) count every band carrier, bound or not, and E_x is the binding
   correction. Alternatively, E_x := Σ(E_g − E_x^b) over excitons. Either way, state one convention.
2. **§3.2 measured combination and bounds.** Exact first-order algebra: d_NR − κd_ER = [E_st + ΔE_trap + ΔE_es^{trap} + ΔE_esc + ΔE_sl + (1−κ)D_ER]/ω. The table
   omits (1−κ)D_ER ≈ 0.36D_ER. The upper bound survives because the omitted term is ≥ 0, but the stated combination is wrong (same in L37, L38).
   The ±0.9/0.7% on η^φ_NR are **95% C.L.** (1803.02903 FT: "95.2^{+0.9}_{−0.7} % at 95% C.L."). So ⟨E_st⟩/E_R ≤ 0.055 is right, but "p_surv E_st,1/E_d ≤ 0.18"
   uses the central 0.048. At 95% it is 0.055/(0.4×0.65) = 0.21, and p_surv ≲ 0.47 (Si). Ge 0.19 is likewise the central f_DF. Relabel these as central
   values, or quote the bound.
3. **1803.02903 "ionization collection efficiency" misread (§2.3(a), §4(a), θ_tr prior).** The FT defines it against a yield parameterisation: "The
   ionization collection efficiency assumes the parameterization for y_C from Ref. [30]" (Fig. 12). It is measured yield ÷ a model yield taken
   from higher-field data, not ⟨𝔵⟩_NR/⟨𝔵⟩_ER. It mixes trapping with the QF model, so it cannot set θ_tr's central value and σ_ln = 0.1 as stated.
   **Fix:** use it as a one-sided constraint on the product (⟨𝔵⟩_NR/⟨𝔵⟩_ER)·(y_true/y_C), with the model dependence flagged.
4. **θ_tr^{pr} prior (§6, A-11).** Type T on the two-point measure gives f(θ) = f₀e^{θψ}/(f₀e^{θψ} + 1 − f₀). With the stated "central 0", f₀ = 0, so f ≡ 0 for every θ,
   and "ψ giving 1% at θ = 1" is impossible. A tilt cannot move mass onto a point that has none. **Fix:** f₀ > 0 (e.g. 10⁻³ [E]) with ψ = ln(10.1) for 1% at θ = 1,
   or type A (a positive increment).
5. **A-12 (minor).** "A drift field acts after t_pr" is not exact. Over t_pr ≈ 100 ps at saturated velocity (10⁶–10⁷ cm/s), a carrier gains eℰ_b v t_pr ≈
   0.01–0.1 eV at 100 V/cm. (E1) remains exact because 𝒲_bias is defined for all t. Reword: "bias work before t_pr is O(eℰ_b v_d t_pr) per carrier, booked in
   𝒲_bias and ℋ_pr; negligible for N_eh but not zero for HV detectors".

## 4. Amendment A-1…A-16
| # | Verdict | Note |
|---|---|---|
| A-1 | NEW ERROR | (a) Exciton convention, as §3.1. (b) "N_eh = fully free pairs" and E_pairs^{unp} are not additive per particle. Whether a pair is "fully free" depends on both siblings' fates, which (W3)/(B2) treats as independent. So δ𝐍 deposits cannot carry it, and the capture deposit as written does not update N_eh or E_pairs^{unp}. **Fix:** additive per-carrier deposits N_e^f, N_h^f, N_e^{tr}, N_h^{tr}, with energies (E_c − μ_F), (μ_F − E_v), (E_c − E^tr − μ_F), (μ_F − E_v − E^tr), and capture heat E^tr into ℋ. N_eh = N_e^f = N_h^f only when there is no capture. The t_pr balance then follows by summation |
| A-2 | RESOLVED | marks, given A-1's additive list fixed as above |
| A-3 | NEW inconsistency | ΔZPE vs T-1's E^conf (§2) |
| A-4 | RESOLVED | (W11) in ratio form, μ_F, ΔE_trap of either sign, NTL ratio |
| A-5, A-6, A-7, A-8, A-9 | RESOLVED | A-7's two cases are correct. A-9 marks TRIM UNRESOLVED |
| A-10 | NEW ERROR | from the amended (W4): ω − N_eh E_g − E_st − E_esc = ℋ + E_trap^{pr} + E_x + E_pairs^{unp} + E_es. With E_x ≡ −ΣE_x^b < 0, (W14) must use ℋ + E_trap^{pr} + **E_x** + E_pairs^{unp} + E_es, not "ℋ + E_trap^{pr} − E_x". The sign is wrong and two terms are missing (they follow from fixing A-1) |
| A-11 | NEW ERROR | θ_tr^{pr} f₀ = 0 (§3.4) |
| A-12 | minor | §3.5. Target string in WP5 (B3) verified verbatim |
| A-13, A-14 | RESOLVED | target strings exist verbatim (WP5 §6.4 "Leading URF corrections"; §9 R6) |
| A-15, A-16 | RESOLVED | NOTATION N_trap restriction; (W6) → (E3)/(E4) |

## 5. Summary
Every R11 item is RESOLVED except one: excitons are still missing from the §7 spec (minor). (E6) agrees with Theorem T-1 in form and is now an identity.
Required updates: drop the "constraint" wording, use ⟨N_hop⟩ normalisation, take the mean in (E5), and resolve the ΔZPE convention across WP5, WP7-T
and WP7-E. New errors to fix: the exciton bookkeeping and non-additive N_eh in A-1; the A-10 sign and missing terms; the §3.2 (1−κ)D_ER term and the
central-versus-95% bound labels; the 1803.02903 "collection efficiency" misread used as the θ_tr prior; the θ_tr^{pr} prior with f₀ = 0;
and the A-12 wording.
