# R12 verification VER-WP7-E-B of returns/R12/WP7-E-v2.md (+ code/WP7-E-v2/checks.py) against referees/R11/REF-WP7-E-B.md

Same isolation as R11. Read: WP7-E-v2, its checks (run: 36/36 PASS, ≈ 2 s), my R11 report, and WP5-v3 for the amendment sites.
Re-fetched in full text with lit.py (deleted after use): 1803.02903, 1805.09942, 2202.05097, 2007.14289. One hand derivation of the
calibration algebra (E13). No simulations.

## 1. R11 items
| R11 item | Verdict | Note |
|---|---|---|
| A: checks tautological | RESOLVED | identities replaced by two-route checks (Green's function vs Gauss law, order statistics vs Ramo, mixture variance, 3D PDE) |
| A/B8: C10 ħc ×100 | RESOLVED | 1.19×10⁴ V/cm; Poole–Frenkel 2.2 meV added (C10c, re-derived) |
| B1 ΔZPE | RESOLVED | E_st redefined (§1.1, A-3) |
| B2 excitons | RESOLVED, but NEW ERROR N3 | E_x added; its definition is inconsistent with E_pairs and the t_pr formula (N3) |
| B3 electrostatic reservoir | RESOLVED | E_es = ½Σq_iq_jG incl. self-image; battery work = ΔE_es + NTL heat (C2a–e; image energy σ²z′(d−z′)/2d re-derived) |
| B4 μ reference; t_pr split; singly trapped | RESOLVED | μ_F; E_pairs^{unp} + E_trap^{pr} μ-independent; μ_F − E_v − E^tr_h (C1c,d) correct |
| B5 (E3) sufficiency | RESOLVED | (H-E6), marks 𝔪, G-E9 |
| B6 Theorem E-2 "exactly" | RESOLVED | creation-only claim; knock-on threshold E ≈ 0.2 MeV re-derived; reactions moved post-prompt, G-E7 ([UNVERIFIED] refs acceptable as tagged) |
| B7 position term in F_meas | RESOLVED | (E12) re-derived: [F⟨m²⟩ + ⟨Var𝔵⟩]/⟨m⟩ + N̄Var_r m/⟨m⟩ |
| B9 delayed events | RESOLVED | single threshold 2.7 eV; pockets (N_a ≈ 270 at 16 eV re-derived); minor: the CPD threshold "4.2σ, 16.3 eV" is stated in 2007.14289 [FT], not "the referee's reading" |
| B10 3D correlated recombination | RESOLVED | (r_c/d)erfc((d − r_c)/√4Dt) (Smoluchowski) correct |
| B11 E_hot(0⁺), WP5 (B3) | RESOLVED | §1.1; A-12 |
| C1 2004.10709 App. A | RESOLVED (stands) | L35 |
| C2 1803.02903 "Y_H = 1" reading | RESOLVED (withdrawn) | η^φ_NR quote verified verbatim; but the replacement algebra has NEW ERROR N1 |
| C4 2405.10405 misapplied | RESOLVED | dropped as θ_tr prior; 77 K stated |
| C5 selective LEE quotes | RESOLVED | the stress-null, epoxy-cracking and χ²/dof = 4192/68 quotes are now present, all verified verbatim |
| C6 1805.09942 vs 1803.02903 | RESOLVED | "differ by 2.06 standard deviations", "biased with opposite polarities" verified verbatim |
| C8 "secondary" U | RESOLVED | A-8, §4 |
| D2 nuisance types | RESOLVED | type T on a two-point measure gives the logistic, a WP6 (5.1″) object |
| D3 θ_tr prior | PARTLY RESOLVED, NEW ERROR N4 | 77 K bound dropped; the replacement datum is misidentified (N4) |
| D4 symbols | RESOLVED | μ_F, ℰ_b, D_diff, 𝔠 |
| E LIMITS validity / leading correction / Hecht | RESOLVED | columns added; Hecht citation (Z. Phys. 77, 235 (1932)) is correct, honestly tagged [UNVERIFIED]; L37, L38 inherit N1 |
| F computation spec | RESOLVED | cascade capture for shallow levels, G4CMP credited, IF-E9 |
| f novelty | RESOLVED | header disclaims; 2208.02790 credited |
| G A-1 non-existent (W3) state | RESOLVED, NEW ERROR N3 | types and kernels added; exciton deposit inconsistent (N3) |
| G A-4 Δ/ratio/NTL normalisation | RESOLVED in form, NEW ERROR N1 | ratio form and NTL ratio (1+yg)/(1+g) correct; linearisation invalid as written (N1) |
| G A-8 | RESOLVED | |
| G A-10 | RESOLVED in structure, NEW ERROR N5 | sentence fixed; substitution has a sign and omission error (N5) |
| G four unamended sites | RESOLVED | A-12…A-15 apply to the right WP5 sentences (checked against WP5-v3 §1.2 (B3), §6.4, §9 R6, §14) |

## 2. New E_st data constraints (§3.2) and (E13)
- **(E13) algebra verified by hand.** Raw phonon signal ω − D + g·y·ω, with ER calibration of both channels:
  η = (1+g)(1 − d_NR + gy)/(1 − d_ER + g) − gy = 1 − d_NR + κd_ER + O(d²), κ = (1 + yg)/(1 + g). With g = 4/3.82 = 1.047 and y = 0.3 [E], κ = 0.642. Correct as algebra.
- **N1 (NEW ERROR, substantive).** D ≡ E_stored + E_esc + E_sl contains the **absolute** sensor loss. For phonon sensors E_sl/ω = 1 − ϵ_coll
  is O(1) (typically 0.7–0.9), so d_ER is not small. The "+O(d²)" remainder in (E13), and the "O(D_ER ΔD/ω²)" remainder in (E8) and A-4, are then
  O(1) relative corrections, not second order (C9a's −ΔD·D_ER/ω² is itself ~ΔD/ω × 0.7). Worse, ΔE_sl is not an independent term: a stored E_st
  removes phonons before the sensor, so ΔE_sl ⊃ −(1 − ϵ_coll)E_st < 0. That breaks §3.2's premise that "the non-E_st terms are ≥ 0". The identification
  "d_NR − κd_ER = ⟨E_st + ΔE_trap + … + ΔE_sl⟩/ω" is also wrong for κ ≠ 1: it omits +(1 − κ)d_ER = 0.36 d_ER. **Fix:** treat collection multiplicatively.
  Write E_sig = ϵ_prim(ω − D′) + ϵ_NTL·(NTL heat), with D′ = E_stored + E_esc the pre-sensor deficit (small) and ϵ_prim, ϵ_NTL per recoil type.
  Redo (E8), (E13) and A-4 to first order in d′ and Δϵ/ϵ. The ER-calibrated η is then ≈ 1 − d′_NR + κ′d′_ER + (Δϵ terms), with an analogous κ′. The 4.8%
  maps onto E_st/ω + ΔE_trap/ω + … + Δϵ/ϵ, and the E_st upper bound survives to that order, provided Δϵ ≥ 0 is assumed and stated.
- **N2 (NEW ERROR, minor).** The labelled "upper bounds" p_surv E_st,1/E_d ≤ 0.18 (Si) and ≤ 0.19 (Ge) use the **central** deficits (0.048, 0.0608; checks.py l. 156).
  With the quoted bounds (0.055 at 95% CL, 0.065) they are 0.21 and 0.20, and the implied p_surv ≲ 0.47 (Si) and ≲ 0.66 (Ge). Either relabel them "central"
  or use the bound values. §0 row 10, C8b,c and θ_st must agree.
- 1803.02903 quotes verified: η^φ_NR = 95.2^{+0.9}_{−0.7}% (95% CL), "relative to electron recoils of the same deposited energy", 10–100 keV. The phrase
  "²⁵²Cf-resonance energies" is not in the source: write "10–100 keV (²⁵²Cf neutron calibration)".
- 1805.09942 verified: f_DF = 6.08 ± 0.18% (uncertainty already inflated by the 2.06 factor); "systematic error does not include modeling imperfections".
  The opposite-polarity sentence supports the ΔE_trap reading. The Ge row is otherwise correct, subject to N1 and N2.
- **N4 (NEW ERROR).** §2.3(a) and θ_tr read 1803.02903's "ionization collection efficiency … consistent with 100% … below 20 keV … ∼75% at 100 keV"
  (verified verbatim) as ⟨𝔵⟩_NR/⟨𝔵⟩_ER. The source defines it relative to a yield parameterisation y_C from measurements by other groups "at higher electric
  fields" (Ref. [30]). It is therefore ⟨𝔵⟩_NR(4 V/cm)/⟨𝔵⟩_NR(high field), and it depends on that model. It is not an NR/ER ratio, nor a "direct constraint".
  Restate it as a field-dependence datum with model dependence, and widen σ_ln accordingly.

## 3. Amendment A-1…A-16
- A-2, A-3, A-5, A-6, A-7, A-8, A-9, A-11, A-12, A-13, A-14, A-15: correct as text.
- **N3 (NEW ERROR).** The exciton bookkeeping is inconsistent across §1.1, §1.2, §1.3 and A-1. The reservoir table defines E_pairs over
  "unbound free carriers" and E_x = −ΣE_x^b, and the t_pr formula counts N_eh = "fully free pairs". A bound pair's band energy E_g then sits in no reservoir.
  The process ledger ("E_pairs → E_x + ℋ_ph (E_x^b)") and A-1's deposit "E_x −= E_x^b" both assume that bound carriers stay in E_pairs. Fix: either E_pairs
  runs over all band carriers, bound or not (and then N_eh in the t_pr formula counts bound pairs too), or E_x ≡ Σ(E_g − E_x^b).
- **N5 (NEW ERROR, A-10).** From the amended (W4), N_eh E_g = ω − ℋ − E_st − E_esc − E_pairs^{unp} − E_x − E_trap^{pr} − E_es. So the replacement in (W14) is
  ℋ → ℋ + E_trap^{pr} + E_pairs^{unp} + E_x + E_es, with E_x ≤ 0, i.e. "+E_x", not "−E_x". E_pairs^{unp} must not be omitted. The sign depends on resolving N3.
- **A-4** is correct in its ratio form. Its linear form and remainder inherit N1.
- **A-16 (minor NEW ERROR).** It replaces P_casc(𝐍|Λ) in (W6) by P(𝐌,t|Λ) but leaves the left-hand side as dℛ/d𝐍. Change it to dℛ/d𝐌, or keep (W6)
  as the cascade-level rate and add (E4) beside it.

## 4. Summary of new errors
N1 additive treatment of the O(1) sensor loss invalidates the first-order (E8)/(E13)/A-4 forms and the sign premise of the §3.2 bounds (substantive;
the bound survives after a multiplicative restatement). N2 central values labelled as bounds. N3 exciton energy unbooked/inconsistent. N4 1803.02903
collection efficiency misread as NR/ER. N5 A-10 sign and omission. Minor: A-16 left-hand side; "resonance"; CPD threshold is [FT].
Every other R11 item is RESOLVED.
