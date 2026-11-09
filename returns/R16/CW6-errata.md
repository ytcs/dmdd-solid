# R16 / CW6-errata: verification corrections to returns/R16/CW6.md and returns/R16/WP8-R-v2.md (VER-CW6)

Errata agent ERR-CW6, brief briefs/R16/ERR-CW6.md, 2026-11-01. **Read together with returns/R16/CW6.md and returns/R16/WP8-R-v2.md ("v2")**. Neither is edited, because
returns are the record. Where this file gives replacement text, that text supersedes the CW6.md or v2 text at that site. **The merger uses only §B of this file** for the
owed corrections, the interface flags, the proposed LIMITS rows and the v2 replacement passages. Everything not named here stands as written (VER-CW6 rows 1, 2, 5, 12,
13, 19 are STANDS).
**Read:** CW6.md, v2, referees/R16/VER-CW6.md, code/CW6/checks.py (original), returns/R14/WP5-AUD.md §2 ((AUD-1), the exact δ_coll = X^{oth} = 0 identity), returns/R13/WP8-R.md
(C4f, C5c sites), referees/R14/REF-WP8-R-B.md (weak checks), state/LOOSE-ENDS.md (LE-119, LE-123), returns/R8/WP4-v3.md (RG7, l.329, l.551), LIMITS L36, CONVENTIONS §§10–14 and
R13 amendments, NOTATION (WP7-E rows: κ_cal, g_Luke, y_ion, 𝔮). **Not re-checked here (as in VER-CW6):** returns/R15/CMPMC-AUD.md, returns/R16/CW5.md, /home/user/cmpmc file:line
citations. They are carried unchanged from CW6.md.
**Literature [FT]** (lit.py → literature/papers-ERR-CW6/; full text read; PDFs, HTML and graph files deleted afterwards; `.txt` extracts kept for the locators): 1805.02495,
2408.04732, 2303.02196, 2012.12430, 1109.1193, 1109.4343. Page numbers are PDF pages (in 1805.02495 and 2408.04732 they equal the printed page numbers).
**Checks.** `python3 code/CW6/checks.py` gives **62/62 PASS in < 15 s** (numpy, scipy, sympy; deterministic; the one random test, K11a, uses a fixed seed). This supersedes the
"44/44 PASS in ≈ 17 s" line of CW6.md and of v2. The labels stay CW6-Kn. Changes are listed in §D. No heavy numerics, no CMPMC run, no QE run.
Tags as CONVENTIONS §12. Status of everything new: CLAIMED. Equation labels new in this file: (CW6-2′), (CW6-3′), (CW6-5).

---
## A. Corrections, by verifier row

### A1. VER-CW6 row 3 (FALLS): "fitted effective Si→Al 0.3–0.55 ⇒ t̄_esc = 0.10–0.19" (CW6 §7, K5f, K6c, OC-CW6-7, IF-CW6-8; v2 §3.2, L40)
**Withdrawn and re-derived.** 1805.02495 p.7 [FT] (VER-CW6 cites p.8; see §C4): "the code does not implement phonon propagation in Al, so a phonon absorbed in the KIDs
generates a signal with probability ηpb or is killed. Hence, (1-TSi→Al) include the probability of a phonon to enter the Al and to be reflected back to the Si substrate".
The same page says "in the current implementation no mode conversion occurs", with specular reflection for the AMM fit. The fitted coefficient is therefore a per-hit
**absorption** probability, T_fit = t̄_{Si→Al}·P_abs, not an interface transmission. The reciprocity theorem (which is correct, VER-CW6 row 2) does not apply to it.
**Correct use [E] (CW6-K5f, K6e, K6f).** With the AMM pair (t̄_{Si→Al} = 0.934, t̄_esc = 0.323): P_abs = 0.321–0.589. Inverting (CW6-4) exactly,
e^{−a} = (1 − P_abs)/(1 − (1 − t̄_esc)P_abs), gives a = 0.142–0.380. With the DMM pair (0.743, 0.257): P_abs = 0.404–0.740, a = 0.161–0.550. For d = 60 nm,
λ_pb = 2d/a (normal incidence) to 4d/a (flux average) = 0.22–1.7 µm. This is a constraint on λ_pb/d, **not on t_esc**. Hypotheses: the substrate phonons hitting the KIDs
average like the isotropic flux average (the 1805.02495 MC is specular and ballistic, so this is an approximation, [E]), and the film population is isotropised (A2).
**Remaining nuisance.** θ_esc^{film} spans the AMM/DMM spread 0.257–0.323, a factor **1.26 in τ_l** (CW6-K6c), until a film→substrate datum exists. 1109.1193 p.14 [FT]
("phonon-aSi-aluminum interaction … probability of ∼33%", "empirically matched") is a fitted absorption-type coefficient of the same kind. It is not a t_esc either.
"The AMM t̄ = 0.934 is an upper bound" holds only as a bound on T_fit (P_abs ≤ 1) *if the AMM is right*. It is not a theorem about the interface, so it is tagged [E].
Replacement texts: §B1 (CW6 §7), §B2 OC-CW6-7 and IF-CW6-8, §B4 (v2 §3.2, §9 row, L40).

### A2. VER-CW6 row 4 (STANDS WITH CORRECTION): film-escape law (CW6-4), τ_l, "exactly thickness_frac = 4/t̄_esc"
The geometric series (K6a) and ⟨2d/cosθ⟩ = 4d (K6b) stand. Three hypotheses were missing. The verifier's numbers are confirmed by the AMM solver (CW6-K5h):
- **Trapped modes.** In Al, SV and SH beyond θ_c = arcsin(c_T^{Al}/c_T^{Si}) = 34.9° have t = 0 (Si P and T both evanescent; the solver gives t = 0 to machine precision).
  At the free top face, SV→P conversion is cut off above arcsin(c_T/c_L)^{Al} = 29.0°, so these modes stay SV/SH under specular reflection. The trapped share is
  1 − (c_T^{Al}/c_T^{Si})² = **67.2% of the T flux = 60.2% of all film flux** (weight 2c_T⁻²/Σ_Al = 0.895). Without in-film mixing (diffuse top face, grain or
  dislocation scattering) these phonons never escape. They are pair-broken in the film, which raises P_abs above (CW6-4).
- **Mode conversion.** The per-θ form assumes no P↔SV conversion on reflection. The leading correction is the 2×2 P/SV reflection matrix at both faces.
- **Angle average at t = 1.** ⟨1 − e^{−2d/(λ_pb cosθ)}⟩_flux = **1 − 2E₃(2d/λ_pb)** exactly (E₃ the exponential integral; CW6-K6d). This is below CMPMC's 1 − e^{−4d/λ_pb}
  (Jensen). The two agree only to O(a): they differ by 2.9%/8.3%/11.8% at d/λ_pb = 0.01/0.06/0.2, which is the range A1 gives for the 60-nm film.
"Exactly" is deleted. τ_l = 4d/(v_film t̄_esc) is the escape time of an **isotropised** film population. Replacement: §B1, §B3 (CW6-L3), §B4 (v2 §3.3).

### A3. VER-CW6 row 6: near-face shell
2012.12430 p.4 [FT]: "The detector top surface is instrumented with two QET arrays". One face is instrumented, so the shell of events within r_rms(t) of it is
r_rms/d = **0.24% (10 ns) / 1.9% (100 ns)** (CW6-K4b), not 2r_rms/d = 0.5%/3.9%. The bulk scope becomes ≥ 98% of the 4-mm device at 100 ns. The old numbers were
conservative. Replacement: §B4 (v2 §0 row 2, §2.4, §9 V2/F1 row) and §B1 (CW6 §10 preamble).

### A4. VER-CW6 row 7: ζ_O sign convention ((CW6-1), K7b, OC-CW6-5)
checks.py computed a_prim − a_NTL with a ≡ the film-1 (Nb-like, high-gap) share, while (CW6-1) and v2 §3.5 define ζ_O ≡ a_NTL − a_prim. **Fix:** the definition
ζ_O ≡ a_NTL − a_prim (and ζ_gap ≡ a_gap − a_prim) is kept everywhere, and the channel fraction is **oriented**:
- two-film observable: a_pop ≡ E_2,pop/(E_1,pop + E_2,pop), with **film 2 the lower-gap film** (Al in the toy);
- fast/slow observable: a_pop ≡ the energy fraction in the channel (fast or slow) that the NTL population enriches in the stated geometry, so that ζ_O ≥ 0 by construction.
  ζ_gap is signed relative to the same channel.
This is the same as VER-CW6 V-4's "ζ_O ≡ a_prim − a_NTL with film 1 the high-gap film" (the film-1 and film-2 shares sum to 1), but it keeps one definition of ζ_O
across CW6, v2 and WP6. Toy values under it: **ζ_O = +0.420/+0.282/+0.107** at ⟨E_Luke⟩ = 0.75/2/4.7 meV (CW6-K7b; the magnitudes are unchanged). The θ_ζ prior
uniform [0, 0.5] stands. K3d's ζ_gap/ζ_O scan (−1 … +1) is symmetric, so its result 0.27/0.25/0.24/0.22/0.21 is unchanged (now checked to 0.01, CW6-K3d). Replacement: §B1 (CW6
§2), §B2 OC-CW6-5, §B4 (v2 §3.5).

### A5. VER-CW6 row 8 and §B: toy r_coll = 0.87–0.98 and its use for L36 / WP7-E (B-b)
**What the toy number is (CW6-K7d, K7e) [E].** The deficit is the NTL energy born below 2Δ_Al, which the toy counts as lost. The toy NTL spectrum is flat in f up to
2⟨E_Luke⟩ but **truncated at the 0.05 THz grid edge**. Its sub-2Δ_Al share is 0.118/0.040/0.016 at ⟨E_Luke⟩ = 0.75/2/4.7 meV (not the 0.24 a flat spectrum from 0
would give at 0.75 meV). It accounts for 0.118 of the 0.136 loss at 0.75 meV. With those births removed, r_coll = 0.992/0.995/0.998 (Nb + Al) and 1.000 (all-Al films).
With ℓ_s × 10, r_coll = 0.819/0.914/0.965. Whether sub-2Δ_Al energy is lost, absorbed by a W TES or absorbed by another film is a **model choice**, and it decides the
sign of r_coll − 1. The geometry (Nb + Al two-film, 4-mm Si) is not the 1803.02903 or 1805.09942 device.
**Effect on the L36 bounds [D] (CW6-K7f; rebuttal §C1).** With δ_coll = X^{oth} = 0 the WP5-AUD §2 identity 1 − η − E_st/ω = g_Luke(r − 1)(1 − y_ion − E_st/ω)/(1 + rg_Luke)
is exact. Solving it for E_st/ω at the measured η gives
  E_st/ω = (1 − η) + g_Luke(1 − r_coll)(η − y_ion)/(1 + g_Luke).                                                                          (CW6-5)
At g_Luke = 4/3.82, y_ion = 0.3, η = 0.952 the bound widens by **0.042/0.015/0.006** at the toy r_coll (0.8745/0.9552/0.9815), or 0.043/0.013/0.007 at the rounded
r = 0.87/0.96/0.98. The bounds are loosened by a computable amount, not "void". They are void only if r_coll has no lower bound. Replacement: §B2 OC-CW6-2, IF-CW6-2; §B4
(v2 §0 row 8, §6, IF-R3); §B3 (CW6-L1).

### A6. VER-CW6 row 9: δ_coll^{gap} (CW6-3) hypothesis
**General form [D] (CW6-K8e).** Let x_ER, x_NR be the gap energy released as phonons within the window, per unit gap energy of the ER's created pairs. Then
  δ_coll^{gap} = 𝒢_gap(ρ_g − 1)(x_ER − x_NR)/[1 + 𝒢_gap x_ER(ρ_g − 1)],   ρ_g ≡ ϵ_gap/ϵ_hard,                                              (CW6-3′)
exactly at fixed populations (CW6-3′). Three cases follow. (CW6-3) is x = (1, y_ion). If every created pair releases E_g as phonons, x = (1, 𝔶). If trapped pairs retain E_g,
x = (⟨𝔮⟩_ER, 𝔶⟨𝔮⟩_NR), which is (CW6-3) with 𝒢_gap → 𝒢_gap⟨𝔮⟩_ER. (CW6-3) as printed therefore holds if ⟨𝔮⟩_NR = ⟨𝔮⟩_ER (then y_ion = 𝔶), or in the
trapped-retain case with 𝒢_gap → 𝒢_gap⟨𝔮⟩_ER. Numerically this is immaterial: at ⟨𝔮⟩_ER = 0.873 the 0.048 needs ρ_g − 1 = 0.27 instead of 0.24 (CW6-K8f).
Replacement: §B1 (CW6 §5), §B2 OC-CW6-3, §B3 CW6-L5.

### A7. VER-CW6 row 10: the bias scan
**Completed [D] (CW6-K8g).** Multiplied by (1 + r g_Luke), (AUD-1) is linear in (r_coll, X): m_i(1 + r g_i) = g_i(r − 1)(1 − y_ion) + (1 + g_i)X, with m_i ≡ 1 − η^φ_NR(V_i).
Two biases therefore invert it **exactly within the first-order (AUD-1) model, for any r_coll** (round trip r = 0.9, X = 0.02 in K8g). It does not need the r = 1
Jacobian. At r ≠ 1, ∂(1 − η)/∂X = (1 + g)/(1 + rg) varies with bias, and the inversion carries that. **All missing inputs, stated separately:** (1) r_coll
bias-independent over 4 → 40 V (the NTL birth spectrum is field-dependent, IF-AUD-5; LE-118 computes dr_coll/dV_b); (2) y_ion bias-independent, i.e. ⟨𝔮⟩_NR/⟨𝔮⟩_ER
measured at both biases from the charge channel (trapping is field-dependent); (3) X bias-independent: δ_coll (through the field-dependent gap-release site) and D′
(through 𝒲_bias(t_pr) and E_trap) at both biases. With three biases, the system is overdetermined and tests (1)–(3).
Replacement: §B1 (CW6 §5), §B2 OC-CW6-3, §B3 CW6-L5.

### A8. VER-CW6 row 11 and §C: transfer-kernel bound (CW6-2)
**Re-derived [D] (CW6-K11a; refinement §C2).** Hypotheses: (h1) linear transport; (h2) the observable is linear in the delivered energies with weights in [0, 1]
(energy fractions E_s/E, fast fraction E(t < t_f)/E). A ratio observable (a = E_1/(E_1 + E_2)) is linearised, and its weight range W replaces 1 below. (h3) No sensor
absorption before t_mem (bulk scope, A3). (h4) τ_h(t_mem) ≡ sup over hard birth spectra (f > f_m) of the TV distance of their evolved spectra at t_mem. v1 §2.3 and
CW6-K4a evaluate it for one pair only, so its value is [E]. From (h3)–(h4), the response w(f) to a birth at f > f_m has oscillation ≤ τ_h on f > f_m. Since ∫Δũ = 0,
ΔO = ∫(w − w^∞)Δũ for any constant w^∞. Taking w^∞ as the midpoint of w on f > f_m gives
  |ΔO_obs| ≤ ‖Δũ‖_{1, f<f_m} + ½τ_h‖Δũ‖_{1, f>f_m} ≤ ‖Δũ‖_{1, f<f_m} + τ_h,    ‖·‖_1 = 2‖·‖_TV,   Δũ ≡ ũ_NR,0 − ũ_ER,0.                    (CW6-2′)
It equals Δ_soft + τ_h (Δ_soft ≡ |∫_{f<f_m}Δũ|) **only when Δũ is single-signed below f_m**. That holds for v1's inputs (ER-only soft band) but not in general. K11a gives a
counterexample with |ΔO| = 0.1 and Δ_soft = 0. The middle expression of (CW6-2) used TV norms where L1 norms are needed; that factor 2 is **conceded**. The final
"Δ_soft + τ_h" is right under the single-sign condition. The NR optical-share sentence is unaffected. Replacement: §B1 (CW6 §4), §B3 CW6-L2.

### A9. VER-CW6 row 14: HV ceiling
Per-energy maxima (CW6-K3m, ε = 3.75/3.8 eV): **1.26/1.27 (100 eV), 1.71/1.72 (220 eV)** on the measured rows. On the 300-eV row they are 1.9986/2.0136. The "300-eV band"
(Y 0.098–0.145, central 0.12; F_NR 0.4–2.4) is a **constructed envelope** of the 220-eV and 460-eV rows of 2303.02196 Table II [E], not a measured row. So "firm at ≲ 220 eV"
rests on measured rows, and "CONDITIONAL" above it rests on an envelope. CW5 OC-7 itself was not checked by VER-CW6 or here. Replacement: §B4 (v2 §0 row 6, §4.4 HV bullet).

### A10. VER-CW6 row 15: space charge
6.5×10⁴ e/cm² is the **jump** en_s/(ε_rε₀) at 1% of 1 V/cm. The field change is max_z|ΔE| = jump·max(z₀, d − z₀)/d ∈ [½, 1]·jump (CW6-K10d). So ξ_SC = 1% needs
n_s = **6.5–12.9×10⁴ e/cm²** (12.9 for a mid-plane sheet). The accumulation time becomes ≈ 5–10 h [E] at 1 Hz of 100-eV events on 1 cm². It ignores e/h dipole cancellation
(electrons and holes trapped at different depths partly cancel), so it is a lower bound on the time only if a single sign dominates. Replacement: §B1 (CW6 §6), §B3 CW6-L6.

### A11. VER-CW6 row 16: athermal-emission locality
The arithmetic stands (0.95 ns, 1.16 µm, CW6-K10c). At 10.9 THz the isotropic f⁵ law lies outside L39 (f ≪ f_D, ICA). Real Si has no TA modes above ≈ 4.5 THz and
optical phonons decay in ps (both per VER-CW6 row 16, not re-read here). The f⁵ estimate overstates the survival time, so the bound is conservative. Tag **[E]** (was [D]). Replacement: §B1, §B2 OC-CW6-8, §B3 CW6-L6.

### A12. VER-CW6 row 17: 2303.02196 trapping and impact ionisation
2303.02196 p.4 [FT]: "n_eh is further smeared to account for charge trapping (12.7% probability) and impact ionization (0.6% probability) in the detector [28]". These are
**model inputs taken from its ref. [28]**, not measurements of 2303.02196. Replacement: §B1 (CW6 §6), §B4 (v2 §4.4 caveat).

### A13. VER-CW6 row 18: 2408.04732 locators and the B_m,l range
Verified [FT]: Eq. (4) "Γisotopic = Bν⁴ = (4π³Γ_mdΩ/⟨c³⟩)ν⁴" is on **p.4**; Table 4 is on **p.7**; Table 3 is on p.6. The Table 4 caption reads "Ranges in the Bm,l column
correspond to measurements of different phonon polarizations". So 2.42–2.56 is a polarisation spread, not an error band. WP8-U's 1.65×10⁻⁴⁵ s³ lies 0.4% above the
**upper end of the polarisation range** of the measured B. Replacement: §B1 (CW6 §8), §B2 OC-CW6-4, §B3 CW6-L4, §B4 (v2 §2.1 locator).

### A14. VER-CW6 row 20: v2 verdict set
The verdicts stand. Row 8's r_coll reading is corrected by A5. The fitted-coefficient clause is not in row 3 (row 3 has no fitted number, §C5); it sits in §3.2 and is
corrected by A1. Replacement: §B4.

### A15. VER-CW6 row 21: cost of the LE-118 first pass
40 × 64 × 10⁴ × 10⁴ = 2.56×10¹¹ steps = **4.44 h** at 16 M steps/s (CW6-K10f), above the 3-h box. The full run is 35.6 h. A box-runnable first pass is the same 1-D grid at
10³ phonons per (f, z) cell: 0.44 h, with statistical error ≈ 3%/√(ϵ) per cell, to be followed by the 10⁴ pass outside the box. Replacement: §B1 (CW6 §2).

### A16. VER-CW6 row 22 and §E: LE-119 (site–spectrum functional, spec)
- (ii) **Robin face [D] (CW6-K10e).** For half-line diffusion with D_X n″ = γ_X n and D_X n′(0) = S_surf n(0), the fraction of excitons born at depth z₀ that recombine at the
  face is **[S_surf/(S_surf + D_X/L_X)]e^{−z₀/L_X}**. It reduces to e^{−z₀/L_X} only for S_surf → ∞. The surface share is ≈ (2L_X/d)·S_surf/(S_surf + D_X/L_X) for L_X ≪ d
  and two recombining faces. The S_surf scan of the spec carries this factor.
- (iii) "All pairs are collected" ignores trapping. Replacement: in NTL mode a fraction ⟨𝔮⟩ is collected and releases E_g at the electrodes at the drift time (≈ 1 µs,
  CW5 §1.2 [E]). The trapped fraction retains E_g until release by flashing or emission (2303.02196 uses 12.7% per carrier as a model input from its ref. [28]).
- **"Missing step (single)" → "two missing inputs"**: (1) the kinetic rates of (CW5-4) (owner CW5/LE-141); (2) the transport inputs D_X, S_surf and s_ℓ (owner this row).
  These are four object classes.
- **s_ℓ was an assumption.** "Hard line at ω_op relaxing by §2, the conservative choice" reinstates for surface and electrode release the "born hard" step that v2 withdrew
  (A F2, B B1). It is conservative only towards ζ_gap = 0. It is replaced by a scan and a named computation. Replacement spec: §B1 (CW6 §3).

### A17. VER-CW6 §E: LE-122 spec pitfalls and convergence
Added: two-electron D⁻/A⁺ states, the Born failure near threshold, the 216-atom cell vs the donor envelope, valley–orbit splitting, and the convergence of the
cross-section part. Replacement spec: §B1 (CW6 §6).

### A18. VER-CW6 row 23: ledger effect
OC-CW6-1 stands. LE-123 stays CLOSED, but its "vs measured Si→Al 0.3–0.55" comparison is withdrawn: the nuisance is AMM/DMM only (A1), and the fit constrains λ_pb/d.
LE-119 stays CLOSED-AS-EXACT-GAP with "two missing inputs" (A16). LE-118 and LE-121 stay CLOSED with A4–A8 and A15. LE-20, 120, 122, 124, 125 and 126 are unchanged apart
from the errata texts. Replacement: §B2 OC-CW6-9.

### A19. VER-CW6 §D: Δ_Al reading of 1109.4343 p.3
1109.4343 p.3 [FT]: "Al quasiparticles (of energy 2∆Al = 200 µeV)". BCS gives 2Δ ≈ 3.53k_BT_c ≈ 0.36 meV for Al, so the 200 µeV is likely Δ (thin-film Δ ≈ 0.18–0.20 meV [UNVERIFIED]),
not 2Δ. v2 §3.3 no longer presents it as an equal reading. The 4Δ range becomes **97–193 GHz** (CW6-K11c), not "≤ 174 GHz either way" (§C3). The conclusion is
unchanged: every arriving primary or NTL phonon (≳ 0.3 THz) lies above 4Δ. Replacement: §B4 (v2 §3.3), §B1 (CW6 §1).

### A20. VER-CW6 §G and V-12: v2 closing table, weak checks C4f and C5c
Both are **applied here** rather than marked "not applied/removed":
- C5c (REF-B): the Nb-like cut 2Δ = 3 meV is 0.725 THz (CW6-K11d). The 0.7 THz Ge hole NTL band lies on it, 3.5% below, and the cut sits inside the Si arrival peak 0.7–0.9 THz
  (1805.02495 p.7). A Nb-like film therefore does not separate Ge hole NTL phonons from primaries. Text: §B4 (v2 §3.3).
- C4f: the e^{−N_mix} argument is now computed from N_mix(1 µs) = 652/5072: log₁₀e^{−N_mix} = −283 (Si), −2203 (Ge) (CW6-K11b). This replaces v1's hard-coded e^{−100}.
- B §D (L40 "measured"): applied (§B4 L40). A F8 ("void"): applied in the A5 form.

### A21. VER-CW6 §F: LIMITS rows
L39, L41 and L42 are ✔. L40 is ✎ (A1). CW6-L1…L6 are ✎ (A2, A4, A5, A6, A7, A8, A10, A11, A13). The full replacement rows are in §B3.

---
## B. Re-issued texts (merger: use this section only)

### B1. Replacement passages in CW6.md
| Site | Replacement text |
|---|---|
| header, "Deliverables" line | "… both checked by `code/CW6/checks.py`: **62/62 PASS in < 15 s** (ERR-CW6 revision; numpy, scipy, sympy; deterministic) …" |
| §1 Result, Δ_Al clause | "Δ_Al is stated in three readings (0.18 meV v1; 1109.4343 p.3 writes "2∆Al = 200 µeV", which against BCS (2Δ ≈ 0.36 meV) is likely Δ; Δ = 173.715 µeV CMPMC presets.hpp:298). 4Δ = 97–193 GHz across them, so no conclusion changes." |
| §2, "Estimate [E] (CW6-K7)" through "geometric quantity." | "**Estimate [E] (CW6-K7).** Si, d = 4 mm, c₁ = c₂ = 5%, t = 0.9, film 1 Nb-like (2Δ = 3 meV, cut 0.725 THz), film 2 Al (2Δ = 0.36 meV), ℓ_s = 10⁻³. Channel fraction a ≡ E_2/(E_1 + E_2) (film 2 = the lower-gap film; errata A4). Primaries (Debye birth): film 1/film 2/loss = 0.415/0.574/0.012. NTL births flat in f up to 2⟨E_Luke⟩ (truncated at the 0.05 THz grid edge), ⟨E_Luke⟩ = 0.75/2/4.7 meV (the paer-sota range of IF-AUD-5 [CALC pending]), give ζ_O = +0.42/+0.28/+0.11 and r_coll = 0.87/0.96/0.98. The r_coll deficit is the sub-2Δ_Al NTL birth share (0.118/0.040/0.016), which the toy counts as lost: without it r_coll = 0.992/0.995/0.998 (1.000 with two Al films); with ℓ_s × 10 it is 0.82/0.91/0.97 (K7d, K7e). The loss assignment of sub-gap energy (lost, W TES, other film) is a model choice and sets the sign of r_coll − 1. σ_pos = 0 in this limit by construction; it is a purely geometric quantity." |
| §2 (ii) | "… which is **negative** for NTL births below 2Δ_Al or exposed to surface loss (K7c, K7d), **when sub-2Δ_Al energy absorbed by a W TES or by other films is counted as lost (the toy's model choice; that choice decides the sign)**." |
| §2 Cost, last clause | "… above the 3-h box limit, so FORMULATED. A 1-D (depth-only) reduction with 64 depth points at 10⁴ phonons per cell costs 40 × 64 × 10⁴ × 10⁴ = 2.6×10¹¹ steps ≈ **4.4 h** (CW6-K10f), also above the box; the box-runnable first pass is the same grid at 10³ phonons per cell (≈ 0.44 h, ≈ 3%/√ϵ statistical error per cell), followed by the 10⁴ pass." |
| §3 (ii) | "(ii) Surface and electrode channels have π_ℓ set by the diffusion of excitons/carriers to faces: for diffusion constant D_X, lifetime 1/γ_X and surface recombination velocity S_surf, the fraction reaching a face from depth z and recombining there is [S_surf/(S_surf + D_X/L_X)]e^{−z/L_X}, L_X = (D_X/γ_X)^{1/2} (half-line, 1-D, Robin face) [D, CW6-K10e]; so the surface share is ≈ (2L_X/d)·S_surf/(S_surf + D_X/L_X) for L_X ≪ d and two recombining faces." |
| §3 (iii) | "(iii) In NTL mode a fraction ⟨𝔮⟩ of the pairs is collected and releases E_g at the electrodes at the drift time, ≈ 1 µs (CW5 §1.2 estimate [E]); the trapped fraction (2303.02196 uses a 12.7% per-carrier trapping probability, a model input from its ref. [28]) retains E_g until flashing or emission. The collected part merges the timing channel with (d) through ζ_gapΔφ_gap (v2 §4.4)." |
| §3 "Missing step (single)" through the end of the Specification | "**Missing inputs (two):** (1) the rates of (CW5-4) at 10–50 mK (k_FX, k_FT, k_XB,j, k_B↓, η_X, C_X; owned by CW5/LE-141); (2) the transport inputs D_X, S_surf and the per-channel spectra s_ℓ (owned here). **Specification.** *Kinetics part:* CW5 §2.5 spec (EPW cascade capture, BSE/DFT for bound excitons; book appendix: kinetic equations, BSE). *Transport part (this row).* *What:* π_ℓ(r, t), s_ℓ(f) for Si and Ge, then ζ_gap and its timing distribution. *Approximation:* drift–diffusion of excitons (neutral, so field-free) with Robin faces of velocity S_surf; s_ℓ is **not** assumed: for surface and electrode recombination it is either scanned or computed. *Scan:* s_ℓ^{(κ)} = (1 − κ)s_hard + κs_soft, κ ∈ {0, 0.25, 0.5, 0.75, 1}, with s_hard the line at ω_op relaxing by v2 §2 and s_soft a Debye (∝ f²) spectrum cut at f_c ∈ {0.5, 1, 2} THz, i.e. ballistic over the window (f_*(t) > f_c until ≳ 10 µs; 1109.1193 p.17 [FT]: surface recombination phonons are "13% of the total phonon signal but in a low frequency, ballistic regime"); report ζ_gap(κ, f_c). *Computation (replaces the scan when done):* nonradiative multiphonon emission at the surface/interface recombination centre (P_b-type dangling bond at Si/SiO₂, metal-contact states) by the configuration-coordinate (Huang–Rhys/Henry–Lang) line-shape method, with S_HR and the local-mode frequencies from DFT supercells of the centre (rtsc layout, `@PSEUDO@`, SG15 ONCV v1.2) and the emitted spectrum handed to the transport kernels; τ: n_g multi-phonon, frozen surface reconstruction. *Method:* CMPMC does not model excitons (CMPMC-AUD §1.4: NOT USED; §6 items 3 and 5 are prerequisites). Until item 3 lands, run the exciton diffusion as a separate 1-D finite-difference solve (dz ≤ L_X/20, implicit time step, Robin faces with velocity S_surf), feed π_ℓ(z, t) as time-tagged sources into CMPMC `transport` with s_ℓ as birth spectra, and read ζ_gap with the LE-118 kernels. *Convergence:* grid and time step (r_g to 10⁻³); S_surf ∈ [10, 10⁴] cm/s scan; κ and f_c scan as above; for the computed s_ℓ, supercell size and S_HR to 10%. *Pitfalls:* (1) at mK, D_X and k_XB depend on the impurity census of the actual crystal; (2) droplet formation (Ge, Si at high density) is outside (CW5-4); (3) luminescence (η_X) leaves the detector and is in E_esc, not in ζ_gap; (4) s_hard alone pre-decides ζ_gap = 0 for the surface channels (the withdrawn "born hard" step); (5) the Robin prefactor, not e^{−z/L_X}, at finite S_surf. *Cost:* the diffusion solve is seconds; the transport part is LE-118's kernel cost (no new run once 𝒦_s exists); the DFT line-shape part ≈ 10³ CPU-h per centre." |
| §4, (CW6-2) block | "Then, under (h1) linear transport, (h2) weights in [0, 1] (energy-fraction observables; ratio observables linearised, with their weight range replacing 1), (h3) no sensor absorption before t_mem and (h4) τ_h(t_mem) the supremum over hard births of the evolved-spectrum TV distance ([E]: v1 sampled one pair), \|ΔO_obs\| ≤ ‖Δũ‖_{1,f<f_m} + ½τ_h‖Δũ‖_{1,f>f_m} ≤ ‖Δũ‖_{1,f<f_m} + τ_h (CW6-2′), ‖·‖_1 = 2‖·‖_TV, Δũ ≡ ũ_NR,0 − ũ_ER,0. It equals Δ_soft + τ_h, Δ_soft ≡ \|∫_{f<f_m}Δũ\|, when Δũ is single-signed below f_m (true for v1's ER-only soft band, not in general; CW6-K11a). With the v1 inputs Δ_soft ≈ (1 − 𝔶)f_s and τ_h ≤ 10⁻³, which is the v1 result; with computed spectra the L1 norm below f_m is evaluated directly and is the number the WP5 tables must supply." The rest of §4 stands. |
| §5, after (CW6-3) | "(CW6-3) assumes ⟨𝔮⟩_NR = ⟨𝔮⟩_ER (so y_ion = 𝔶). In general δ_coll^{gap} = 𝒢_gap(ρ_g − 1)(x_ER − x_NR)/[1 + 𝒢_gapx_ER(ρ_g − 1)] with x the released gap fractions: x = (1, 𝔶) if every created pair releases E_g as phonons; x = (⟨𝔮⟩_ER, 𝔶⟨𝔮⟩_NR), i.e. (CW6-3) with 𝒢_gap → 𝒢_gap⟨𝔮⟩_ER, if trapped pairs retain E_g (CW6-K8e). ρ_g − 1 = 0.24 (0.27 with 𝒢_gap⟨𝔮⟩_ER, ⟨𝔮⟩_ER = 0.873) gives 0.048 for Si (K8b, K8f)." |
| §5, "Degeneracy broken [D]" paragraph | "**Degeneracy broken [D, within (AUD-1)].** Multiplied by 1 + r_collg_Luke, (AUD-1) is linear in (r_coll, X), X ≡ δ_coll + (D′_NR − κ_cal(r_coll)D′_ER)/ω: m_i(1 + r_collg_i) = g_i(r_coll − 1)(1 − y_ion) + (1 + g_i)X, m_i ≡ 1 − η^φ_NR(V_i). Two biases invert it exactly for any r_coll (CW6-K8g; at r_coll = 1 the Jacobian has rank 2, K8c, d; at r_coll ≠ 1 the X weight (1 + g)/(1 + r_collg) is itself bias-dependent and is carried by the inversion). **Measurement proposal:** η^φ_NR at V_b = 4 V and 40 V (g_Luke = 1.05, 10.5) on one detector and source, with ⟨𝔮⟩ measured at both biases. **Hypotheses (each a missing input):** r_coll, y_ion (through ⟨𝔮⟩_NR/⟨𝔮⟩_ER: trapping is field-dependent) and X (δ_coll through the gap-release site; D′ through 𝒲_bias(t_pr) and E_trap) are bias-independent over 4 → 40 V. A third bias overdetermines the system and tests them; the residual from r_coll(V_b) is of order dr_coll/dV_b·ΔV_b, which the LE-118 run computes. Separating δ_coll from E_st needs one more handle: the two-window Y_H (CW5 §2.5) or an ER/NR source pair with matched depth profiles (δ_coll^{pos} = 0)." |
| §6, space-charge sentences from "The nonlinearity parameter" to "[E]" | "The **nonlinearity parameter** ξ_SC ≡ max_z\|ΔE\|/ℰ_b. A sheet produces the jump en_s/(ε_rε₀) and max_z\|ΔE\| = jump·max(z₀, d − z₀)/d ∈ [½, 1]·jump (CW6-K10d), so 1% of 1 V/cm in Si needs n_s = 6.5–12.9×10⁴ e/cm² (6.5×10⁴ is the jump; K10a). Accumulation: with event rate R per area, pairs per event N_eh, trapped fraction p_tr (12.7% is the per-carrier trapping probability 2303.02196 p.4 uses as a model input from its ref. [28]) and neutralisation (IR flashing) every t_flash, n_s(t) ≈ RN_ehp_trt up to t_flash. For a 1-cm² Si face at R = 1 Hz of 100-eV events (27 pairs), ξ_SC = 1% at 1 V/cm after t ≈ 5–10 h [E], ignoring e/h dipole cancellation; dense calibration runs reach it in minutes." |
| §6, "Athermal emission: a locality bound [D]" | "**Athermal emission: a locality bound [E].** … (K10c). The f⁵ law at 10.9 THz lies outside L39 (f ≪ f_D, ICA); real Si has no TA modes above ≈ 4.5 THz and optical phonons decay in ps, so the true survival is shorter and the bound is conservative." The rest of the paragraph stands, except the last parenthesis, which becomes "(2303.02196 p.4 uses 0.6% per carrier for impact ionisation, a model input from its ref. [28])". |
| §6, Specification (replaces *Approximation* through *Cost*) | "*Approximation:* σ_ph-ion for D⁰/A⁰ from the effective-mass hydrogenic envelope with central-cell correction and deformation-potential coupling (Fermi golden rule, one-phonon absorption; Ξ of Kaplan/Leman); for **D⁻/A⁺ a two-electron (H⁻-like) variational wavefunction** (Chandrasekhar-type correlated two-electron envelope; E_b ≈ 0.055 E_b(D⁰) [UNVERIFIED]), never a one-electron hydrogenic state; σ_ii away from threshold from the Born impact cross-section on the same wavefunctions, and **near threshold (E_kin ≈ E_b, the hot-tail regime this row targets) from a distorted-wave or close-coupling calculation, the Born form being invalid there**; **valley–orbit splitting** (Si 1s(A₁)/1s(T₂)/1s(E), 6 valleys; Ge 4 L valleys) included in the initial and final states, since it sets the threshold of σ_ph-ion; trapped-charge field from 1-D Poisson (above) or the FEM fields of CMPMC (mesh_field.hpp: NOT USED, not audited). *Method:* (1) effective-mass cross-sections on a converged envelope basis (no DFT for the envelope); **DFT supercells give only the central-cell correction**, since a 216-atom Si cell (1.6 nm) cannot hold the donor envelope (a* ≈ 2–3 nm): pw.x 216-atom Si:P, ecut 60 Ry, Γ-only, ≈ 10³ CPU-h, inputs with `@PSEUDO@`, SG15 ONCV v1.2 via `rtsc/pseudo.sh`, stages as `rtsc/bench/run-fork.sh`; (2) CMPMC trapping/impact ionisation (charge_physics.hpp:104–127; USE with caveat) extended by CMPMC-AUD §6 item 5 (E9 kinetics with history n_j(t), speed-dependent σ and space charge), **prerequisite**; (3) a run-sequence driver that carries n_j(t) across events. *Convergence:* cross-section part: envelope basis until E_b and σ change < 1% (≥ 1s–3p manifold or an equivalent Gaussian/Lagrange-mesh basis), all valleys summed with valley–orbit mixing, phonon-q grid and threshold energy grid ≤ E_b/50; Poisson grid dz ≤ d/200; event-sequence length until ξ_SC saturates. *Pitfalls:* (1) constant mean-free-path trapping cannot produce history dependence; (2) Ramo is exact with space charge (WP7-E-v3 C2c), but the dissipated heat differs by −ΔE_es; (3) flashing resets n_j but creates D⁻/A⁺ populations; (4) one-electron models for D⁻/A⁺; (5) Born cross-sections at threshold; (6) supercell envelopes; (7) valley–orbit splitting omitted near threshold. *Cost:* minutes for (1) on the envelope basis and for (3); ≈ 10³ CPU-h for the central-cell DFT; (2) is item 5 (≈ 1 week implementation)." |
| §7, "Film-escape law [D]" paragraph, from "which reduces to" | "… which reduces at t_esc ≡ 1 to 1 − e^{−a} per θ; its flux average is 1 − 2E₃(2d/λ_pb) exactly (CW6-K6d), which CMPMC's 1 − e^{−4d/λ} (kaplan.hpp:51–58, path 4d = ⟨2d/cosθ⟩, K6b) matches only to O(a) (2.9%/8.3%/11.8% below at d/λ = 0.01/0.06/0.2); P_abs ≈ a/t_esc for a ≪ 1. Hence, **for a film population isotropised (diffuse top face or grain scattering) faster than escape**, the film phonon loss time is τ_l = 4d/(v_film t̄_esc), the τ_l of 1401.1937 that controls the thin-film fall of η_pb. The per-θ form assumes no P↔SV conversion on reflection. Without in-film mixing, SV and SH beyond 34.9° (60% of the Al film flux) are totally reflected at Al/Si and never escape (CW6-K5h). CMPMC's film model is the t̄_esc = 1 limit; at small a and with an isotropised population the physical value enters as `thickness_frac` ≈ 4/t̄_esc, and as (CW6-4) per θ in general." |
| §7, "t_esc from the interface" paragraph, from "Reciprocity theorem" | "**Reciprocity theorem [D]:** Σ_Al t̄_{Al→Si} = Σ_Si t̄_{Si→Al}, Σ = c_L⁻² + 2c_T⁻² (K5d). It does not apply to the fitted Si → Al 0.3–0.55 of 1805.02495 (p.1, p.9 [FT]; 380 µm Si / 60 nm Al, specular MC fit): that MC does not propagate phonons in Al, so its coefficient is t̄_{Si→Al}·P_abs (p.7 [FT]), and it fixes the in-film optical depth a = 0.14–0.38 (AMM pair) or 0.16–0.55 (DMM pair), i.e. λ_pb ≈ 0.2–1.7 µm for 60 nm [E] (K5f, K6e), not t_esc. The AMM and DMM differ by ×1.26 in τ_l (K6c). This is the RG7 closure: t_esc is no longer phenomenological; its model spread (AMM/DMM) is the nuisance θ_esc^{film}, until a film→substrate datum exists." |
| §7 Pitfalls (2) | "(2) fitted 'transmission' coefficients from MCs without in-film propagation (1805.02495 0.3–0.55; 1109.1193 p.14 ∼33%) are absorption probabilities t̄·P_abs, not t_esc;" |
| §8 Finding, locator and band | "… The [FT] source of the formula and value is **2408.04732 Eq. (4) (p.4) and Table 4 (p.7)** …"; and "WP8-U's 1.65 lies 0.4% above the upper end of the polarisation range of the measured B (Table 4 caption: the B_m,l ranges 'correspond to measurements of different phonon polarizations') and is acceptable as [E]." |
| §10 preamble | "The statement must carry the bulk scope (near-face shell 0.24–1.9% of a 4-mm device with one instrumented face, 10–100 ns) …" |

### B2. Owed corrections of CW6.md (re-issued; type as CONVENTIONS §12)
| # | Target | Type | Exact text | Status |
|---|---|---|---|---|
| OC-CW6-1 | returns/R13/WP8-R.md | S | as CW6.md | **unchanged** |
| OC-CW6-2 | LIMITS L36 Validity cell | S | append: "(B-b) r_coll ≥ 1 is not supported by WP8-R-v2 §6. A mean-field toy (two-film Nb + Al, 4-mm Si) gives r_coll = 0.87–0.98 [E], entirely from NTL energy assumed born below 2Δ_Al and lost (r_coll = 0.99–1.00 without it; CW6-K7d). With δ_coll = X^{oth} = 0, on r_coll < 1 the E_st/ω bound widens by g_Luke(1 − r_coll)(η^φ_NR − y_ion)/(1 + g_Luke) (exact; 0.042 at the toy r_coll = 0.8745, CW6-errata (CW6-5)). The stated bounds hold on the r_coll ≥ 1 branch (CW5 OC-8)." | **re-issued** (V-2; rebuttal §C1 on the width) |
| OC-CW6-3 | WP7-E-v3 §8 G-E4 and IF-E7 | W | G-E4 → "δ_coll = δ_coll^{prim} + δ_coll^{gap} + δ_coll^{pos} + δ_coll^{esc}; δ_coll^{prim} ≤ 0.012; δ_coll^{gap} = 𝒢_gap(ρ_g − 1)(x_ER − x_NR)/[1 + 𝒢_gapx_ER(ρ_g − 1)] with released gap fractions x (= (1, y_ion) if ⟨𝔮⟩_NR = ⟨𝔮⟩_ER; (⟨𝔮⟩_ER, 𝔶⟨𝔮⟩_NR) if trapped pairs retain E_g) can carry 0.048 (ρ_g − 1 = 0.24–0.27). (AUD-1) times (1 + r_collg_Luke) is linear in (r_coll, X), so η^φ_NR at two biases determines r_coll and δ_coll + E_st-term exactly, provided r_coll, y_ion (⟨𝔮⟩ measured at both biases) and X are bias-independent over the scan (CW6 §5, CW6-errata A7)" | **re-issued** (V-6) |
| OC-CW6-4 | WP8-U U7, IF-U10, LU3 | W | U7: "A_iso is ordered Ge > Si > C as 1901.07569 p.6 states qualitatively; the Si value 1.65×10⁻⁴⁵ s³ is this return's closed form [E], consistent with 2408.04732 Eq. (4) (p.4) and Table 4 (p.7) [FT]: 1.50 (calc), 1.55–1.64 (measured; the range is the spread over phonon polarisations) ×10⁻⁴⁵ s³; 1.65 lies 0.4% above the upper end of that polarisation range". LU3 source: "2408.04732 Eqs. (3)–(9), Table 4 p.7 [FT]; Tamura PRB 27, 858 (1983) (bibliography verified, not accessed)"; status ESTIMATED → DERIVED (formula, [FT]) / E (value) | **re-issued** (V-8) |
| OC-CW6-5 | WP6-v3 §5.2 | S | append the rows: θ_ζ "contrast ζ_O ≡ a_NTL − a_prim of the two-film (a = lower-gap film share) or fast/slow (a = share of the channel the NTL population enriches) observable \| M \| uniform [0, 0.5] [E] (central from 𝒦_s when computed) \| geometry, V_b \| WP8-R-v2 §4.4; CW6 LE-118; CW6-errata A4"; θ_ζg "gap-population contrast ζ_gap ≡ a_gap − a_prim, same orientation as θ_ζ \| M \| uniform [−0.5, 0.5] [E] (sign open) \| geometry, release site \| WP8-R-v2 §4.3; CW6 LE-119"; θ_pos, F_NR rows as CW6 §9; θ_Ssurf "surface recombination velocity S_surf (enters through S/(S + D_X/L_X)) \| M \| σ_ln 2.3 [E] \| crystal surface \| CW6 LE-119; CW6-errata A16" | **re-issued** (V-4) |
| OC-CW6-6 | state/SOTA.md, IF-R6 | W | as CW6.md §10 text | **unchanged** (the shell numbers are in the §10 preamble, B1, not in the statement) |
| OC-CW6-7 | WP4-v3 §6 RG7 and l.329, l.551 | W | "t_esc is the flux- and mode-averaged film→substrate transmission t̄_esc: AMM 0.32, DMM 0.26 (Al/Si; CW6 §7). It enters τ_l = 4d/(v_film t̄_esc) for an isotropised film population and the per-entry absorption (CW6-4). The fitted Si→Al 0.3–0.55 of 1805.02495 is t̄_{Si→Al}·P_abs and constrains λ_pb/d (a ≈ 0.14–0.38 at 60 nm), not t_esc. RG7 closed as a nuisance θ_esc^{film} over AMM/DMM (×1.26 in τ_l)." | **re-issued** (V-1) |
| OC-CW6-8 | LIMITS L33, L34 leading-correction cells | W | add: "space-charge field ΔE(z) = (1/ε_rε₀)[∫_0^zρ_tr − (1/d)∫_0^d(d − z′)ρ_tr dz′]; a sheet gives max\|ΔE\| ∈ [½, 1]·en_s/(ε_rε₀) (CW6 §6, CW6-errata A10); phonon-driven emission from neutral shallow centres confined to ≲ 1 µm of a track [E] (f⁵ law outside its validity at 10.9 THz; conservative)" | **re-issued** (rows 15–16) |
| OC-CW6-9 | LOOSE-ENDS (coordinator) | N | "LE-20, 118, 120, 121, 123, 124, 125, 126 CLOSED; 119, 122 CLOSED-AS-EXACT-GAP (pointers to CW6.md and CW6-errata.md). LE-119: 'two missing inputs' (CW5/LE-141 rates; D_X, S_surf, s_ℓ). LE-123: the 'vs measured Si→Al 0.3–0.55' comparison is withdrawn; nuisance = AMM/DMM (the fit constrains λ_pb/d)." | **re-issued** (row 23) |

**Interface flags re-issued** (the others, IF-CW6-1, -3 … -7, unchanged):
| # | Owner | Item | Action |
|---|---|---|---|
| IF-CW6-2 | WP7-E (IF-E7, G-E4), LIMITS L36 | (B-b) | WP8-R-v2 does not support r_coll ≥ 1: toy r_coll = 0.87–0.98 [E], entirely from sub-2Δ_Al NTL energy counted as lost (0.99–1.00 without it); on r_coll < 1 the E_st/ω bound widens by g_Luke(1 − r_coll)(η − y_ion)/(1 + g_Luke); δ_coll^{gap} can carry 0.048; exact two-bias inversion (CW6-errata A5–A7) |
| IF-CW6-8 | WP4 | RG7 | t_esc replaced by t̄_esc^{AMM/DMM} (0.32/0.26) with (CW6-4) for an isotropised film; τ_l = 4d/(v t̄_esc); the 1805.02495 fit is an absorption datum on λ_pb/d |

### B3. Proposed LIMITS rows of CW6.md (re-issued in full; numbering by the coordinator)
| # | Chain | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| CW6-L1 | transport Green's function → collection kernels 𝒦_s → ζ_O, ζ_gap, σ_pos, r_coll (CW6-1), a oriented (two-film: lower-gap film share; fast/slow: the NTL-enriched channel), so ζ_O ≥ 0; mean-field linear solve | derived here; 1109.1193 p.14 (surface loss) [FT] | linear transport; mean-field: diffusion ≪ absorption time; **sub-2Δ loss assignment is a model choice that sets the sign of r_coll − 1** | position dependence (σ_pos); dispersion above 1 THz; AMM vs DMM surfaces; sub-gap absorption in TES/other films | DERIVED (functionals) / E (toy) |
| CW6-L2 | transfer-kernel bound (CW6-2′): \|ΔO_obs\| ≤ ‖Δũ‖_{1,f<f_m} + τ_h (= Δ_soft + τ_h iff Δũ single-signed below f_m) | derived here | linearity; weights in [0, 1] (ratio observables: linearised, scaled by their weight range); no absorption before t_mem; L39 scaling; τ_h a supremum over hard births [E] | non-ICA decay; surfaces before t_mem | DERIVED |
| CW6-L3 | film escape (CW6-4); τ_l = 4d/(v t̄_esc); reciprocity Σ₁t̄₁₂ = Σ₂t̄₂₁ | derived here; CMPMC kaplan.hpp:51–58 (t̄ = 1 limit; its 1 − e^{−4d/λ} is the O(a) form of 1 − 2E₃(2d/λ)) | specular film faces; lumped λ_pb; **film population isotropised (diffuse top surface or grain scattering) faster than escape; no mode conversion in the per-θ form; trapped T modes (60% of film flux, Al/Si) escape only through that mixing** | the 2×2 P/SV reflection matrix and the trapped-mode fraction; interference for λ ≳ d; anisotropy; interlayers | DERIVED |
| CW6-L4 | Tamura/Klemens isotope rate A_iso = Γ_mdΩ⟨c⁻³⟩/(4π) | 2408.04732 Eq. (4) (p.4), Table 4 (p.7) [FT] (B_m,l range = polarisation spread) | ICA, f ≪ f_D | dispersion (Tamura 1983/1985) | DERIVED (formula) / FT (value) |
| CW6-L5 | δ_coll^{gap} (CW6-3, general form with released fractions x); exact two-bias inversion of (AUD-1) | derived here; (AUD-1) | first order; fixed populations; **⟨𝔮⟩_NR = ⟨𝔮⟩_ER for (CW6-3) as printed (else x as stated); r_coll, y_ion, X bias-independent over the scan** | δ_coll^{pos}; field dependence of r_coll, ⟨𝔮⟩, trapping, 𝒲_bias(t_pr) | DERIVED |
| CW6-L6 | planar space-charge field; locality of phonon-driven emission | derived here | 1-D, fixed V_b; f⁵ decay law (outside ICA at 10.9 THz; conservative) | 3-D trapped distributions; e/h dipole cancellation; D⁻/A⁺ cross-sections | DERIVED (field; 6.5×10⁴ e/cm² is the jump, max\|ΔE\| ≥ ½ jump) / E (locality) |
| L40 (v2) | isotropic welded AMM (P–SV + SH) and DMM; reciprocity Σ₁t̄₁₂ = Σ₂t̄₂₁ | derived here (CW6-K5); **fitted effective Si→Al 0.3–0.55 for 380 µm/60 nm, including in-film absorption (1805.02495 p.1, p.7 [FT]); it constrains λ_pb/d, not t_esc** | λ ≪ d_film; isotropic media; clean interface | anisotropy (Christoffel AMM); oxide/aSi layers; partial specularity | DERIVED (formulas) / E (numbers) |
L39, L41, L42: unchanged (VER-CW6 §F ✔).

### B4. Replacement passages in returns/R16/WP8-R-v2.md (Required 0)
| Site | Replacement text |
|---|---|
| header, "Checks" line | "**Checks:** `code/CW6/checks.py`, **62/62 PASS in < 15 s** (ERR-CW6 revision; numpy, scipy, sympy; deterministic, no Monte Carlo), cited **CW6-Kn**." (the rest of the line stands) |
| §0 row 2, scope clause | "… events farther than r_rms(t) from the instrumented face (≥ 98% of a 4-mm device with one instrumented face at 100 ns, CW6-K4b)" |
| §0 row 6 | "… firm at the central measured Y, F_NR (2303.02196) and at E_R ≲ 220 eV (1σ; per-energy maxima 1.26 at 100 eV, 1.72 at 220 eV); at the 1σ corner of the 300-eV band, a constructed envelope of the 220/460-eV rows [E], the ceiling is 2.014 with the source's ε = 3.8 eV (1.999 with 3.75) (CW6-K3f, K3j, K3m; CW5 OC-7)" |
| §0 row 8 | "**δ_coll^{prim} ≤ 0.007–0.012** only. The gap-release part δ_coll^{gap} (exact, CW6-K8a, K8e; (CW6-3) needs ⟨𝔮⟩_NR = ⟨𝔮⟩_ER) gives the whole 0.048 for ρ_g − 1 = 0.24–0.27 (K8b, K8f): **δ_coll can carry the deficit.** r_coll ≠ 1 expected, sign open; a mean-field toy gives r_coll = 0.87–0.98 (K7c), entirely from sub-2Δ_Al NTL energy counted as lost (0.99–1.00 without it, K7d), so WP8-R **does not support (B-b) r_coll ≥ 1**; on r_coll < 1 the E_st/ω bound widens by g_Luke(1 − r_coll)(η − y_ion)/(1 + g_Luke) (K7f). Two biases of η^φ_NR invert (AUD-1) exactly for any r_coll if r_coll, y_ion and X are bias-independent (K8g)" |
| §2.1, locator | "(1109.1193 Table I p.16; 2408.04732 Table 4 p.7: 2.33 calc, 2.42–2.56 meas (polarisation spread); Table 3 p.6: 1.15×10⁻⁵⁵ calc)" |
| §2.4, near-face sentence | "… that shell (events within r_rms(t) of the top face, which carries both QET arrays, 2012.12430 p.4 [FT]) is 0.24% of the volume at 10 ns and 1.9% at 100 ns (CW6-K4b)." |
| §3.2, "Measured." paragraph (replaces it) | "**Fitted.** 1805.02495 p.1 [FT]: "transmission coefficients Si-Al in the range [0.3 - 0.55]" for "an aluminum film of 60 nm and a silicon substrate of 380 µm", fitted data-vs-MC with specular reflection. That MC "does not implement phonon propagation in Al", so "(1-TSi→Al) include the probability of a phonon to enter the Al and to be reflected back" (p.7 [FT]): the coefficient is t̄_{Si→Al}·P_abs, an absorption probability that includes the in-film absorption, not a transmission. Under the AMM it is bounded by t̄_{Si→Al} = 0.934 (P_abs ≤ 1) [E]. With (CW6-4) it fixes the in-film optical depth a = 0.14–0.38 (AMM pair) or 0.16–0.55 (DMM pair), i.e. λ_pb ≈ 0.2–1.7 µm for 60 nm [E] (CW6-K5f, K6e). The film→substrate t̄_esc stays the AMM/DMM 0.32/0.26." (The reciprocity sentence "By the reciprocity theorem the matching film→substrate value is 0.10–0.19 …" is deleted.) |
| §3.3, τ_l sentence | "The film loss time is τ_l = 4d_film/(v_film t̄_esc) for an isotropised in-film population (60% of the Al film flux is totally reflected at Al/Si and escapes only through in-film mixing; CW6-K5h); its t = 1 flux average is 1 − 2E₃(2d/λ_pb) (CW6.md LE-123, CW6-errata A2)." |
| §3.3, Δ_BCS(Al) sentences | "**Δ_BCS(Al):** v1 used 0.18 meV [UNVERIFIED]; 1109.4343 p.3 [FT] writes "Al quasiparticles (of energy 2∆Al = 200 µeV)", which against BCS (2Δ ≈ 3.53k_BT_c ≈ 0.36 meV) is likely Δ; the CMPMC preset has Δ = 173.715 µeV (presets.hpp:298). 4Δ = 97–193 GHz across these readings, so every arriving primary or NTL phonon (≳ 0.3 THz) lies above 4Δ; it does **not** lie on a flat branch." The rest of §3.3 stands, and this is appended: "**Nb-like cut (REF-B C5c).** 2Δ = 3 meV is 0.725 THz: the 0.7 THz Ge hole NTL band sits on it (3.5% below) and it lies inside the Si arrival peak 0.7–0.9 THz (1805.02495 p.7), so such a film does not separate Ge hole NTL phonons from primaries (CW6-K11d)." |
| §3.2, "Mode and angle." first sentence | "The L/T contrast multiplies an NR/ER L-fraction difference ∝ e^{−N_mix}, with log₁₀e^{−N_mix(1 µs)} = −283 (Si), −2203 (Ge) from the computed N_mix (CW6-K11b), so no NR/ER information follows in Si/Ge." |
| §3.5, last sentence | "Contrasts ζ_O ≡ a_NTL − a_prim, ζ_gap ≡ a_gap − a_prim, with a oriented: two-film a = E_2/(E_1 + E_2), film 2 the lower-gap film; fast/slow a = the fraction in the channel the NTL population enriches, so ζ_O ≥ 0 and ζ_gap is signed relative to it (CW6-errata A4)." |
| §4.4, HV bullet, first sentence | "**HV (100 V), conditional NO-GO (CW5 OC-7).** Per-energy maxima of the pair-number ceiling on the measured rows are 1.26 (100 eV) and 1.71/1.72 (220 eV, ε 3.75/3.8); on the 300-eV band, a constructed envelope of the 220/460-eV rows (Y 0.098–0.145, F_NR 0.4–2.4) [E], it is 1.9986 (ε 3.75, ⟨𝔮⟩ 0.873) and **2.014** with the source definition ⟨n_eh⟩ = YE_r/3.8 (2303.02196 Eq. (1)) (CW6-K3f, K3j, K3m)." The rest of the bullet stands. |
| §4.4, low-bias bullet, toy sentence | "A mean-field two-film toy (4-mm Si, 5% Nb-like + 5% Al coverage; a = Al-film share) gives ζ_O = +0.11 … +0.42 for ⟨E_Luke⟩ = 4.7–0.75 meV (K7b; CW6.md LE-118) …" |
| §4.4, caveats bullet | "… low-field trapping at mK (θ_tr; 2303.02196 p.4 uses trapping 12.7% and impact ionization 0.6% per carrier as model inputs from its ref. [28]) …" |
| §6, r_coll bullet (replaces the second and third sentences) | "Mean-field toy: r_coll = 0.87 (⟨E_Luke⟩ 0.75 meV), 0.96 (2 meV), 0.98 (4.7 meV) (K7c). The deficit is the NTL energy born below 2Δ_Al, which the toy counts as lost (r_coll = 0.99–1.00 without it, K7d; 0.82 at 0.75 meV with ℓ_s × 10, K7e); that loss assignment is a model choice and sets the sign. **WP8-R does not support (B-b) r_coll ≥ 1. If r_coll < 1, the WP7-E-v3 (L36) bound on E_st/ω widens by g_Luke(1 − r_coll)(η − y_ion)/(1 + g_Luke) (exact at δ_coll = X^{oth} = 0; 0.042/0.015/0.006 at the toy values, K7f); it is void only if r_coll is unbounded below** (A F8, in the CW6-errata A5 form)." |
| §6, degeneracy bullet | "**Breaking the degeneracy [D, within (AUD-1)].** (AUD-1) times (1 + r_collg_Luke) is linear in (r_coll, X); η^φ_NR at two biases (g_Luke = 1.05 and 10.5) inverts it exactly for any r_coll (CW6-K8g; rank 2 at r_coll = 1, K8c, d), provided r_coll, y_ion (⟨𝔮⟩ measured at both biases) and X are bias-independent; a third bias tests that. Two windows separate E_st^{rel}P_rel and r_g (CW5 §2.5)." |
| §8, checks table | add rows: "K3m \| HV per-energy maxima; 300-eV envelope"; "K5f, K5h, K6c–f \| fitted coefficient as t̄·P_abs; trapped film modes; 1 − 2E₃; inversion for a, λ_pb; AMM/DMM ×1.26"; "K7d–f \| sub-2Δ_Al origin of r_coll < 1; ℓ_s scan; exact E_st/ω widening"; "K8e–g \| general δ_coll^{gap}; exact two-bias inversion"; "K10d–f \| max\|ΔE\|; Robin face; run cost"; "K11a–d \| (CW6-2′) test; computed e^{−N_mix}; 4Δ readings; C5c"; and K5 row: "… DMM (value only; reciprocity by construction)" |
| §9 row "V2 / F1" | "applied; device thickness corrected to 4 mm (A's 1 mm wrong, B right; 2012.12430 p.4); shell 0.24%/1.9% (one instrumented face, CW6-errata A3)" |
| §9 row "V8 / F8 / B3" | "applied: δ_coll^{prim} vs δ_coll^{gap} (exact; general form CW6-errata A6); (B-b) unsupported flag; F8 applied as a computable widening of the E_st/ω bound, not 'void' (CW6-errata A5); '\|r−1\| ≲ 0.2' replaced by OC-8 prior \| §6, K7c–f, K8a,b,e–g" |
| §9 row "1805.02495 0.7–0.9 THz circular; 0.3–0.55 device and fitted" | "applied: 0.3–0.55 is t̄_{Si→Al}·P_abs (no propagation in Al in that MC, p.7), used for λ_pb/d only; no reciprocity map (CW6-errata A1) \| §2.3, §3.2, K5f, K6e" |
| §9 row "weak checks C4f, C5c, C8a" | "applied in CW6-errata A20: C4f replaced by K11b (e^{−N_mix} from computed N_mix); C5c stated in §3.3 with K11d; C8a range stated \| §3.2–3.3, §6" |
| §9 row "Δ_Al 200 µeV (1109.4343 p.3)" | "the 200 µeV is likely Δ (BCS); 4Δ = 97–193 GHz; conclusion unchanged (CW6-errata A19) \| §3.3, K11c" |
| §9, new row | "B §D (L40 'measured') \| B \| applied: 'fitted effective, includes in-film absorption' \| L40" |
| Interface flag IF-R3 | "δ_coll^{gap} can carry 0.048 (general form, CW6-errata A6); (B-b) not supported by WP8-R (toy r_coll < 1 from sub-2Δ_Al loss; bound widening g_Luke(1 − r_coll)(η − y_ion)/(1 + g_Luke)); exact two-bias inversion under bias-independent r_coll, y_ion, X" |
| L40 row | as §B3 |

---
## C. Rebuttals and refinements of VER-CW6
**C1. §B and V-2: the size of the bound widening (rebuttal of the formula).** VER-CW6 gives the widening as ≈ g_Luke(1 − r)(1 − y_ion)/(1 + rg_Luke) = 0.050/0.015/0.007
at r = 0.87/0.96/0.98. That expression is the change of 1 − η at fixed E_st/ω. It is not the change of the inferred E_st/ω at the measured η, which is what bounds E_st.
sympy (CW6-K7f): `solve(1 − η − s − g(r − 1)(1 − y − s)/(1 + rg), s)` gives s = (1 − η) + g(1 − r)(η − y)/(1 + g), exactly. The widening is
**g_Luke(1 − r_coll)(η − y_ion)/(1 + g_Luke) = 0.043/0.013/0.007** at r = 0.87/0.96/0.98 (0.042/0.015/0.006 at the unrounded toy values). The verifier's conclusion stands:
the bounds are loosened by a computable amount, not voided. Its 0.050 overstates the 0.87 case by 15%. OC-CW6-2 uses the exact form.
**C2. Row 11 / §C: constant of the corrected bound (refinement).** VER-CW6 writes |ΔO| ≤ ‖Δũ‖_{1,low} + τ_h‖Δũ‖_{1,high}, "reducing to Δ_soft + 2τ_h". Because ∫Δũ = 0,
w^∞ can be taken as the midpoint of w on the hard band, where its oscillation is ≤ τ_h. That halves the high-band weight: |ΔO| ≤ ‖Δũ‖_{1,low} + ½τ_h‖Δũ‖_{1,high} ≤
‖Δũ‖_{1,low} + τ_h. So CW6's Δ_soft + τ_h is right under the single-sign condition, with hypotheses (h1)–(h4) of A8. The verifier's main point (L1 norm, single-sign
condition) is accepted, and so is the TV/L1 factor in CW6's middle expression. K11a tests the bound on 4000 seeded random instances (max ratio 0.47) and gives the
counterexample to Δ_soft + τ_h.
**C3. §D: "4Δ ≤ 174 GHz either way" (rebuttal).** If 200 µeV is Δ, as the verifier argues, then 4Δ = 0.8 meV = **193 GHz** (CW6-K11c: 97/168/174/193 GHz for 2Δ = 200 µeV,
CMPMC, v1, Δ = 200 µeV). The verifier's conclusion stands for a different reason: all four values are below the ≳ 0.3 THz arrival band.
**C4. Row 3: locator.** The quoted 1805.02495 passage ("the code does not implement phonon propagation in Al … reflected back to the Si substrate") is on **PDF p.7**, which
carries the printed page number 7, not p.8 (literature/papers-ERR-CW6/1805.02495.txt, page break 7). The content of row 3 is confirmed and applied (A1).
**C5. Row 20: site of the fitted clause.** v2 §0 row 3 contains no fitted value. The "0.10–0.19" clause is only in v2 §3.2 (and CW6 §7, OC-CW6-7). The correction is applied at
those sites (B1, B2, B4). This is a pointer correction; the substance of row 20 stands.
**C6. Row 8: numbers (refinement).** With the sub-2Δ_Al births removed, my rerun of the original toy gives r_coll = 0.992/0.995/0.998 (Nb + Al), against the verifier's
0.990–0.996. All-Al 1.000 and ℓ_s × 10 → 0.819 agree. The errata use the CW6-K7d values. The verifier did not note that the toy NTL spectrum is truncated at the 0.05 THz grid
edge (sub-gap share 0.118, not 0.24); that is stated in A5.
**C7. Row 10: "at r ≠ 1, ∂/∂X = (1 + g)/(1 + rg) is itself bias-dependent" (refinement).** True, and it does not weaken the proposal. (AUD-1) multiplied by (1 + rg) is linear
in (r, X), so two biases determine both exactly for any r (CW6-K8g). The real conditions are the bias independence of r_coll, y_ion and X, which A7 lists.
**C8. Row 4: "holds only to O(a)" (refinement).** Correct. The exact t = 1 average is 1 − 2E₃(2d/λ), and the leading discrepancy is O(a² ln a), i.e. 8% at d/λ = 0.06
(CW6-K6d). It is quantified in CW6-L3.

---
## D. Changes to code/CW6/checks.py (62 checks, < 15 s)
| Label | Change | Reason |
|---|---|---|
| K2a | tolerance ±2 → ±1 eV (382; 368–369) | tighten |
| K2b | 300–420 / 1100–1450 eV → 357 ± 1, 442 ± 1 (σ_Nph), 1150–1250 eV | tighten to the printed numbers |
| K2d | hard-coded `max(0.3, 0.7) < min(1.4, 2.7)` → arrival band computed as f_*(1 ms)–f_*(1 µs) = 0.68–2.71 THz; overlap 0.72 THz | circular |
| K3d | range [0.15, 0.40] → the five values 0.27/0.25/0.24/0.22/0.21 | tighten (A4) |
| K3f | 1.99 < S < 2 → \|S − 1.9986\| < 10⁻⁴; label states the 300-eV envelope | tighten (A9) |
| K3j | 5×10⁻⁴ → 10⁻⁴ | tighten |
| K3m | **new**: per-energy maxima 1.26/1.27, 1.71/1.72, 1.9986/2.0136 | A9 |
| K4a | 1e-3 < TV(30 ns) < 5e-3, TV(100 ns) < 1e-3 → 0.022 ± 0.001, 2.5e-3 ± 3e-4, 4e-4 ± 1e-4 | tighten |
| K4b | 2r_rms/d → r_rms/d (0.241%, 1.918% ± 10⁻⁵) | A3 |
| K5b | 1e-9 → 1e-12 | tighten (printed 3×10⁻¹⁵) |
| K5d | 1e-3 → 1e-5 | tighten (printed 6×10⁻⁶) |
| K5f | reciprocity map 0.3–0.55 → 0.10–0.19 **removed**; now P_abs = T_fit/t̄ (AMM, DMM) and Σ_Si/Σ_Al ± 5×10⁻⁴ | A1 (FALLS) |
| K5g | DMM reciprocity identity (true by construction) **removed**; DMM values only | circular |
| K5h | **new**: solver t = 0 beyond 34.9°, SV→P cutoff 29.0°, trapped share 67.2%/60.2% | A2 |
| K6c | "AMM 0.29–0.33, ×3" → AMM 0.323, CMPMC-Al 0.328, DMM 0.257, ratio 1.257 | A1 |
| K6d–f | **new**: 1 − 2E₃(2b) (quadrature to 10⁻¹⁰) vs 1 − e^{−4b}; inversion for a and λ_pb; sympy inversion identity | A1, A2 |
| K7a | closure 0.02 → 10⁻⁹, for every population | tighten |
| K7b | range check → signed ζ_O = +0.420/+0.282/+0.107 with a = Al share (equal to the old a_prim − a_NTL of the film-1 share) | A4 |
| K7c | 0.85 < r < 1 → 0.8745/0.9552/0.9815 | tighten |
| K7d–f | **new**: sub-2Δ_Al share and r_coll without it; all-Al; ℓ_s × 10; exact E_st/ω widening (sympy) | A5, C1 |
| K8e–g | **new**: general δ_coll^{gap} (sympy, three cases); ρ_g − 1 = 0.27 at ⟨𝔮⟩_ER = 0.873; exact two-bias inversion round trip | A6, A7 |
| K10d–f | **new**: max\|ΔE\| ∈ [½, 1] jump and 6.5–12.9×10⁴; Robin face S/(S + D/L) (sympy Green's function); run cost 35.6/4.44/0.44 h | A10, A16, A15 |
| K11a–d | **new**: (CW6-2′) on 4000 seeded random instances plus counterexample; computed e^{−N_mix}; 4Δ readings; C5c | A8, A20, A19 |
Unchanged: K1a, K1b (reproduction of v1 by v1's own code, labelled as such), K2c, K3a–c, K3e, K3g–l, K4c, K5a, K5c, K5e, K6a, K6b, K8a–d, K9a–c, K10a–c.

---
## E. Closing table (verifier item → resolution → location)
| VER-CW6 item | Verdict | Resolution | Location |
|---|---|---|---|
| 1 isotropic P–SV AMM | STANDS | none; K5b, K5d tightened | §D |
| 2 reciprocity theorem | STANDS | none; applies to AMM/DMM only (A1) | A1 |
| 3 fitted 0.3–0.55 ⇒ t̄_esc 0.10–0.19 | FALLS | withdrawn; re-derived as t̄·P_abs → a, λ_pb [E]; nuisance AMM/DMM ×1.26 | A1; B1 §7; B2 OC-CW6-7, IF-CW6-8; B3 L40; B4 §3.2; K5f, K6c, K6e, K6f; C4 |
| 4 film-escape law, "exactly" | SWC | trapped-mode share, mode conversion, isotropisation hypotheses; exact 1 − 2E₃; "exactly" deleted | A2; B1 §7; B3 CW6-L3; B4 §3.3; K5h, K6d; C8 |
| 5 device thickness ruling | STANDS | none | — |
| 6 near-face shell | SWC | r_rms/d = 0.24%/1.9%; ≥ 98% | A3; B1 §10; B4 §0 r2, §2.4, §9; K4b |
| 7 ζ_O sign | SWC | oriented a (lower-gap film / NTL-enriched channel); ζ_O = +0.42/+0.28/+0.11 | A4; B1 §2; B2 OC-CW6-5; B3 CW6-L1; B4 §3.5, §4.4; K7b, K3d |
| 8 toy r_coll and (B-b) | SWC | sub-2Δ_Al origin (grid-truncated spectrum), model choice; exact widening (CW6-5) | A5; B1 §2; B2 OC-CW6-2, IF-CW6-2; B4 §0 r8, §6, IF-R3; K7c–f; C1, C6 |
| 9 δ_coll^{gap} hypothesis | SWC | general form with released fractions x; 0.24–0.27 | A6; B1 §5; B2 OC-CW6-3; B3 CW6-L5; K8e, K8f |
| 10 bias scan | SWC | exact two-bias inversion within (AUD-1); three bias-independence inputs | A7; B1 §5; B2 OC-CW6-3; B4 §6; K8g; C7 |
| 11 (CW6-2) | SWC | (CW6-2′) with hypotheses h1–h4; single-sign condition; TV/L1 factor conceded | A8; B1 §4; B3 CW6-L2; K11a; C2 |
| 12 gap two-window algebra | STANDS | none | — |
| 13 Δφ_gap, ζ_O,min tables | STANDS | none (K3d tightened) | §D |
| 14 HV "firm ≲ 220 eV" | SWC | per-energy maxima; 300-eV row is a constructed envelope | A9; B4 §0 r6, §4.4; K3f, K3m |
| 15 space charge | SWC | jump vs max\|ΔE\|; 6.5–12.9×10⁴; 5–10 h [E]; dipole caveat | A10; B1 §6; B2 OC-CW6-8; B3 CW6-L6; K10d |
| 16 athermal locality | SWC | tag [E]; conservative | A11; B1 §6; B2 OC-CW6-8; B3 CW6-L6 |
| 17 2303.02196 0.6%/12.7% | SWC | model inputs from its ref. [28] | A12; B1 §3, §6; B4 §4.4 |
| 18 2408.04732 pages, B_m,l | SWC | p.4 / p.7 (Table 3 p.6); polarisation spread | A13; B1 §8; B2 OC-CW6-4; B3 CW6-L4; B4 §2.1 |
| 19 1901.07569 attribution | STANDS | none | — |
| 20 v2 verdict set | SWC | rows 6, 8 and §3.2 replaced; row 3 pointer | A14; B4; C5 |
| 21 1-D pass cost | SWC | 4.44 h; box first pass 0.44 h at 10³ phonons/cell | A15; B1 §2; K10f |
| 22 LE-119 functional | SWC | Robin prefactor; trapping in (iii) | A16; B1 §3; B2 OC-CW6-5 (θ_Ssurf); K10e |
| 23 ledger effect | SWC | OC-CW6-9 re-issued | A18; B2 OC-CW6-9 |
| §A text items (OC-CW6-7, v2 §3.2, CW6-L3, "upper bound" [E]) | — | applied | A1, A2; B |
| §B (OC-CW6-2 text; §2 (ii) model choice) | — | applied with the exact widening | A5; B1, B2; C1 |
| §C (CW6-2), LE-119 (ii), mean field (i) | — | applied; (i) confirmed | A8, A16 |
| §D Luke rate, 1901.07569, REF-A 1 mm | CONFIRMED | none | — |
| §D 1109.4343 "2∆Al = 200 µeV" | observation | likely Δ; 4Δ = 97–193 GHz | A19; B1 §1; B4 §3.3; K11c; C3 |
| §E LE-119 "single" step, s_ℓ assumption | — | two missing inputs; s_ℓ scan + Huang–Rhys computation | A16; B1 §3; B2 OC-CW6-9 |
| §E LE-122 pitfalls, convergence | — | four pitfalls and cross-section convergence added | A17; B1 §6 |
| §F L39, L41, L42 | ✔ | unchanged | B3 |
| §F L40, CW6-L1…L6 | ✎ | re-issued in full | A21; B3 |
| §G C5c not applied | — | applied (§3.3 text, K11d) | A20; B4 §3.3, §9 |
| §G C4f removed, not replaced | — | replaced by computed e^{−N_mix} (K11b) | A20; B4 §3.2, §9 |
| §G B §D L40 "measured" | — | applied | B3 L40; B4 §9 |
| §G A F8 "void" too strong | — | applied in the computable-widening form | A5; B4 §6, §9 |
| V-1 … V-12 owed corrections | — | V-1 OC-CW6-7/B1 §7/B4 §3.2; V-2 OC-CW6-2/IF-CW6-2/B4; V-3 B1 §7/CW6-L3/B4 §3.3; V-4 OC-CW6-5/B1 §2; V-5 B1 §4/CW6-L2; V-6 OC-CW6-3; V-7 B1 §6; V-8 B1 §8/OC-CW6-4; V-9 B4 §0 r2, §2.4/B1 §10; V-10 B1 §2; V-11 B1 §3, §6; V-12 B4 §9 | B |
