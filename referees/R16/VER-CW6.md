# R16 verification VER-CW6 (hostile, isolated): returns/R16/CW6.md and returns/R16/WP8-R-v2.md

**Read:** CW6.md, WP8-R-v2.md, code/CW6/checks.py (rerun: **44/44 PASS, 15.4 s**, output identical to the return), referees/R14/REF-WP8-R-A.md and -B.md, LIMITS L33–L42,
state/LOOSE-ENDS.md (rows LE-20, 118–126), returns/R14/WP5-AUD.md §2 (AUD-1), returns/R12/WP7-E-v3.md (grep, (E13)). **Full text** (lit.py → literature/papers-r16-VER-CW6/,
PDFs, HTML and text copies deleted afterwards): 2012.12430, 1805.02495, 2408.04732, 1901.07569, 2303.02196, 1109.1193, 1109.4343, 1401.1937. Independent checks are in a
scratchpad: an independent P–SV solver, reruns of the K7 toy with changed inputs, and the Luke-rate integral. None is committed.
**Not checked (outside the read list of this brief):** returns/R15/CMPMC-AUD.md, returns/R16/CW5.md, and /home/user/cmpmc. So (CW5-3)/(CW5-4), OC-7/OC-8, the CMPMC-AUD T3/T8/T11
numbers and every presets.hpp / kaplan.hpp / engine.hpp file:line citation are taken as given here. None of them is rated STANDS.

## Verdict table (scope 1–3)
| # | Item | Verdict | Reason |
|---|---|---|---|
| 1 | WP8-R-v2 isotropic P–SV AMM (§3.2 table; K5a–c, e) | **STANDS** | My own independent solver (different sign and normalisation conventions) reproduces every number: Si→Al 0.977/0.892/0.960/t̄ 0.934; Al→Si 0.603/0.266/0.315/0.323; Ge→Al 0.629/0.781/0.905/0.809; Al→Ge 0.874/0.715/0.819/0.778; L/T 1.055 and 0.745; flux error ≤ 4×10⁻¹⁵ |
| 2 | Reciprocity theorem Σ₁t̄₁₂ = Σ₂t̄₂₁ (K5d, g) | **STANDS** | The proof is one line: c⁻²·2sinθcosθdθ = 2p dp, so each side is Σ_{νμ}∫2p T_{νμ}(p)dp, and the energy coefficients are reciprocal at fixed p. Numerically Σt̄ = 7.5581×10⁻⁸ in both directions (Si/Al) |
| 3 | "Fitted effective Si→Al 0.3–0.55 ⇒ t̄_esc = 0.10–0.19" (K5f, K6c; CW6 §7; v2 §3.2; OC-CW6-7; "×3 in τ_l") | **FALLS** | 1805.02495 p.8 [FT]: "the code does not implement phonon propagation in Al … (1-TSi→Al) include the probability of a phonon to enter the Al and to be reflected back". The fitted T is therefore t̄_{Si→Al}·P_abs (per entry), not an interface transmission, and reciprocity does not apply to it (§A) |
| 4 | Film-escape law (CW6-4); τ_l = 4d/(v t̄_esc); "exactly thickness_frac = 4/t̄_esc" | STANDS WITH CORRECTION | The geometric series and ⟨2d/cosθ⟩ = 4d (K6a, b) are correct. The per-θ form assumes no P↔SV conversion on reflection. The angle-averaged forms assume an isotropised in-film population: 67.2% of the SV and SH flux in Al lies beyond the Si critical angle (t = 0), i.e. 60% of all film phonon flux, so without in-film mixing it never escapes. "Exactly" is wrong. The t = 1 reduction to 1 − e^{−4d/λ} holds only to O(a) (Jensen) (§A) |
| 5 | 2012.12430 device thickness ruling (A wrong, B right) | **STANDS** | Table I: QP.4 is 1 mm and NF-C is 4 mm. σ = 2.65(2) eV is the NF-C device (Table I; p.4 "1 cm × 1 cm × 0.4 cm Si chip") |
| 6 | Near-face shell 0.5%/3.9% (K4b) | STANDS WITH CORRECTION | 2012.12430 p.4 places both QET arrays on the top surface. "Within r_rms of an instrumented face" is r_rms/d = 0.24%/1.9%, not 2r_rms/d. The error is in the conservative direction |
| 7 | Mean-field kernel functionals (CW6-1), linear solve, hit rate v̄/2d | STANDS WITH CORRECTION | Linearity and the slab wall rate are correct. **Sign:** checks.py l.292 computes a_prim − a_NTL, while (CW6-1) and v2 §3.5 define ζ_O ≡ a_NTL − a_prim. Under the stated definition the toy gives ζ_O = −0.42/−0.28/−0.11. Fix the film-labelling convention or use \|ζ_O\| (it affects the θ_ζ prior and the sign of ζ_gap/ζ_O in K3d) |
| 8 | Toy r_coll = 0.87–0.98 (K7c) and its use for L36 / WP7-E (B-b) (OC-CW6-2, IF-CW6-2, v2 §6) | STANDS WITH CORRECTION | The numbers reproduce, but the deficit is almost entirely the **sub-2Δ_Al energy of the assumed flat NTL birth spectrum, counted as lost**. With births below 2Δ_Al removed, r_coll = 1.000 (all-Al films) and 0.990–0.996 (Nb+Al). ℓ_s ×10 moves r(0.75 meV) from 0.875 to 0.819. The geometry (Nb + Al two-film, 4-mm Si) is not the 1803.02903/1805.09942 device. "Bounds void" overstates the effect: see §B for the quantitative shift |
| 9 | δ_coll^{gap} (CW6-3), K8a, b | STANDS WITH CORRECTION | The sympy re-derivation is exact, and ρ_g = 1.236 gives 0.048. The gap fraction of an NR is set by the **created** pairs (𝔶𝒢_gap, as v2 uses in Δf_g), whereas (CW6-3) uses y_ion = 𝔶⟨𝔮⟩_NR/⟨𝔮⟩_ER. The formula needs the stated hypothesis (⟨𝔮⟩_NR = ⟨𝔮⟩_ER, or trapped pairs retain E_g with 𝒢_gap → 𝒢_gap⟨𝔮⟩_ER). The effect is numerically immaterial at 0.048 |
| 10 | Bias scan breaks the r_coll/(δ_coll + E_st) degeneracy (K8c, d) | STANDS WITH CORRECTION | The rank-2 Jacobian is trivially right for the two-parameter linear (AUD-1) model at r = 1. It needs y_ion and X to be bias-independent over 4 → 40 V (⟨𝔮⟩, trapping and 𝒲_bias(t_pr) are field-dependent), not only r_coll. At r ≠ 1, ∂/∂X = (1 + g)/(1 + rg) is itself bias-dependent |
| 11 | Transfer-kernel bound (CW6-2) | STANDS WITH CORRECTION | The low-f term is bounded by the L1 norm of Δũ below f_m, not by Δ_soft = \|∫_{f<f_m}Δũ\|. Equality holds only if NR − ER is single-signed below f_m, which is true for v1's inputs but not in general. Write it as \|ΔO\| ≤ ‖Δũ‖_{L1,f<f_m} + τ_h‖Δũ‖_{L1,f>f_m} (state the TV = ½L1 factor) (§C) |
| 12 | Gap-channel two-window algebra ΔO_b = 𝒢(r_g^{ER} − 𝔶r_g^{NR}); sign flip at 3.86 t₀; 𝒮_b = 8.2/4.63/1.46; ζ_gap,min = 0.42 (K3h, i, k, l) | **STANDS** | Re-derived. e^{−3.865} = 0.02096 = 0.102/4.865. 𝒮_b(100 eV) recomputed by hand: σ = 0.0342, giving 8.2. The flip uses one t₀ for both laws, which is illustrative only, as stated |
| 13 | Δφ_gap = 𝒢(1 − 𝔶)/[(1 + g)(1 + 𝔶g)]; 0.053 at g = 𝔶^{−1/2} (K3a); ζ_O,min tables (K3b–e) | **STANDS** | The algebra and the numbers are reproduced |
| 14 | (c) HV → CONDITIONAL NO-GO, "firm at ≲ 220 eV" (K3f, j) | STANDS WITH CORRECTION | Per-energy maxima: 1.26 (100 eV), 1.72 (220 eV), 1.9986 → 2.0136 (300 eV, ε 3.75 → 3.8). The "300-eV band" in checks.py l.122 (Y 0.098–0.145, F 0.4–2.4) is a constructed envelope of the 220 and 460 rows, not a measured row, so say so. CW5 OC-7 itself was not checked |
| 15 | Planar space-charge field (K10a, b) and the volume form | STANDS WITH CORRECTION | The sheet and volume formulas are re-derived (the fixed-V zero-mean condition). 6.5×10⁴ e/cm² is the **jump**; max\|ΔE\| = jump·max(z₀, d − z₀)/d ∈ [½, 1]·jump, so 1% needs 6.5–13×10⁴ e/cm². The accumulation estimate (5 h) ignores e/h dipole cancellation [E] |
| 16 | Athermal-emission locality (K10c) | STANDS WITH CORRECTION | Arithmetic is right (0.95 ns, 1.16 µm). At 10.9 THz the isotropic f⁵ law lies outside L39 (f ≪ f_D). Real Si has no TA modes above ≈ 4.5 THz, and optical phonons decay in ps, so the bound is conservative. Tag it [E], not [D] |
| 17 | 2303.02196 "measures 0.6% per carrier", "12.7%" | STANDS WITH CORRECTION | p.4: n_eh "is further smeared to account for charge trapping (12.7% probability) and impact ionization (0.6% probability) in the detector [28]". These are model inputs from ref. [28], not measurements in 2303.02196 |
| 18 | LE-124 A_iso: 2408.04732 Eq. (4), Table 4; 1.50/1.55–1.64×10⁻⁴⁵; K9a–c | STANDS WITH CORRECTION | Verbatim: Γ = Bν⁴ = (4π³Γ_mdΩ/⟨c³⟩)ν⁴; Si 2.02×10⁻⁴, 2.13, 2.33, 2.42, "2.42-2.56 [61]". A = B/(2π)⁴ and ΓΩ⟨c⁻³⟩/(4π) are both correct. **Pages:** Eq. (4) is on p.4 and Table 4 on p.7 (PDF = printed), not p.6. The caption says the B_m,l range "correspond[s] to measurements of different phonon polarizations": it is a polarisation spread, not an error band, so "0.4% above the measured band" should say that |
| 19 | 1901.07569 does not contain 1.65×10⁻⁴⁵ (WP8-U attribution) | **STANDS** | Confirmed from full text. Table I (p.2) gives mean free paths, lifetimes and f_W/f_Al; the p.6 text is qualitative ("Ref. [54] demonstrated … isotopic scattering"). Side note: Table I f_Al(Si) = 90.0% is consistent with AMM t̄ = 0.934 |
| 20 | WP8-R-v2 verdict set (rows 4–8 of §0; overall) | STANDS WITH CORRECTION | The verdicts follow from the derivations: (a) NO-GO via the σ_pos cap and band overlap; (b) UNRESOLVED; (d) CONDITIONAL with the yield-ceiling reason. Row 3's "fitted 0.10–0.19" (item 3) and row 8's r_coll reading (item 8) need the corrections above |
| 21 | Cost of the LE-118 1-D first pass, "≈ 1 h" | STANDS WITH CORRECTION | 40 × 64 × 10⁴ × 10⁴ = 2.6×10¹¹ steps, which is **4.4 h** at 16 M steps/s, also above the 3-h box. The full-run figure of 35 h is right |
| 22 | LE-119 site–spectrum functional ζ_gap = Σ_ℓπ̄_ℓ(a_ℓ − a_prim); surface share e^{−z/L_X}, ≈ 2L_X/d | STANDS WITH CORRECTION | Linear and correct. e^{−z/L_X} needs S_surf → ∞; for finite S the prefactor is S/(S + D_X/L_X) (§C). (iii) "all pairs are collected" ignores trapping (12.7% input, item 17) |
| 23 | Ledger effect (OC-CW6-1, OC-CW6-9) | STANDS WITH CORRECTION | OC-CW6-1 stands. LE-123 stays CLOSED, but the ledger row's "vs measured Si→Al 0.3–0.55" comparison is withdrawn (nuisance = AMM/DMM only, item 3). LE-119 stays CLOSED-AS-EXACT-GAP with "two missing inputs" (§E). LE-118 and LE-121 stay CLOSED with the item 7–10 corrections. LE-20, 120, 122, 124, 125 and 126 are unchanged apart from the V-items |

## A. Interface items (scope 0, 1, 3)
- **Correct use of 1805.02495.** With (CW6-4), P_abs = T_fit/t̄_{Si→Al} = 0.32–0.59 (AMM t̄ 0.934) or 0.40–0.74 (DMM 0.743). At t_esc = 0.323 this fixes a = 2d/(λ_pb cosθ) ≈ 0.14–0.38,
  i.e. λ_pb ≈ 2d/a (normal incidence) to 4d/a (flux average) ≈ 0.3–1.7 µm for the 60-nm film. It is a constraint on λ_pb/d, **not on t_esc**. The RG7 nuisance θ_esc^{film} is therefore the AMM/DMM spread 0.26–0.33 (×1.25 in τ_l),
  until a real film→substrate datum exists. 1109.1193 p.14 [FT] ("∼33%" aSi–Al, empirically matched) is an absorption-type coefficient of the same kind.
- **OC-CW6-7 replacement text:** "t_esc is the flux- and mode-averaged film→substrate transmission t̄_esc: AMM 0.32, DMM 0.26 (Al/Si; CW6 §7). It enters τ_l = 4d/(v_film t̄_esc)
  for an isotropised film population and the per-entry absorption (CW6-4). The fitted Si→Al 0.3–0.55 of 1805.02495 is t̄_{Si→Al}·P_abs and constrains λ_pb/d (a ≈ 0.14–0.38 at 60 nm),
  not t_esc. RG7 closed as a nuisance θ_esc^{film} over AMM/DMM."
- **v2 §3.2:** delete the last sentence ("By the reciprocity theorem the matching film→substrate value is 0.10–0.19 …"). L40 Source: "measured effective" → "fitted effective (includes in-film absorption)".
- **CW6-L3 Validity:** add "film population isotropised (diffuse top surface or grain scattering) faster than escape; no mode conversion in the per-θ form; trapped T modes (60% of film
  flux, Al/Si) escape only through that mixing". Leading correction: the 2×2 P/SV reflection matrix.
- The "AMM t̄ = 0.934 is an upper bound" is acceptable only as a bound on T_fit (P_abs ≤ 1) if the AMM is right. It is not a theorem on the interface. Tag it [E].

## B. r_coll and L36 / WP7-E (B-b) (scope 0)
- From (AUD-1) with δ_coll = X^{oth} = 0, the identity 1 − η − E_st/ω = g_Luke(r − 1)(1 − y_ion − E_st/ω)/(1 + rg_Luke) (WP5-AUD §2) shows what happens when r < 1: the E_st/ω bound
  **widens** by ≈ g_Luke(1 − r)(1 − y_ion)/(1 + rg_Luke). At g_Luke = 4/3.82 and y_ion = 0.3 that is **0.050 / 0.015 / 0.007** at r = 0.87 / 0.96 / 0.98. The bounds are loosened by a
  computable amount. They are not "void".
- **OC-CW6-2 replacement text:** "(B-b) r_coll ≥ 1 is not supported by WP8-R-v2 §6. A mean-field toy (two-film Nb + Al, 4-mm Si) gives r_coll = 0.87–0.98 [E], entirely from NTL
  energy assumed born below 2Δ_Al and lost (r_coll = 1.00 without it). On r_coll < 1 the E_st/ω bounds widen by g_Luke(1 − r_coll)(1 − y_ion)/(1 + r_collg_Luke) (0.050 at 0.87). The
  stated bounds hold on the r_coll ≥ 1 branch (CW5 OC-8)." The same edit applies to IF-CW6-2 and v2 §0 row 8 / §6.
- §2 (ii) of CW6 ("negative for NTL births below 2Δ_Al or exposed to surface loss") is correct in the toy. Add "sub-2Δ_Al energy absorbed by W TES or by other films is a model choice
  (here: lost)". That choice decides the sign.

## C. (CW6-2) and other derivations (scope 3)
- (CW6-2) derivation: ΔO = ∫_{low}(w − w^∞)Δũ + ∫_{high}(w − w^∞)Δũ, since ∫Δũ = 0. Then |ΔO| ≤ sup|w − w^∞|·‖Δũ‖_{1,low} + τ_h‖Δũ‖_{1,high}. This reduces to
  Δ_soft + 2τ_h only when Δũ is single-signed below f_m. CW6-L2 must carry this. The NR optical-share sentence is unaffected.
- (CW6-4) per θ: the geometric series is right. K6a and K6b are verified symbolically.
- LE-119 (ii): e^{−z/L_X} assumes an absorbing face (S_surf → ∞). For finite S the prefactor is S/(S + D_X/L_X). The spec's S_surf scan needs this factor.
- (CW6-1) mean field: hypothesis (i) (diffusion ≪ absorption) holds for the toy numbers (≈ 0.4 µs vs ≈ 27 µs at 2 THz, my estimate). Its σ_pos = 0 is correctly flagged as a lower bound.

## D. Published-paper claims (scope 2)
| Claim | Source | Rating |
|---|---|---|
| Luke rate: 1109.1193 Eq. (21) is not the form to quote; the correct form is (v_L/3ℓ₀)(𝔐 − 1)³/𝔐 (IF-AUD-3, carried in v2 §9) | 1109.1193 p.20 [FT, HTML alttext]: "1/τ = (1/3)(v_L/l₀)(k/k_L)[1 − k_L/k]³" | **CONFIRMED.** (21) gives (𝔐 − 1)³/𝔐². The same paper's Eq. (22) has (k/k_L)², and ∫(22)dθ = (v_L/3l₀)𝔐²(1 − 1/𝔐)³ = (v_L/3l₀)(𝔐 − 1)³/𝔐. My golden-rule integral with Eq. (20) and l₀ = πħ⁴ρ/(2m³C²) gives the same. (21) is a misprint, inconsistent with (22) |
| 1901.07569 does not contain A_iso = 1.65×10⁻⁴⁵ | full text | CONFIRMED (item 19) |
| REF-A's "1 mm" for the 2.65-eV device | 2012.12430 Table I, p.4 | CONFIRMED that A is wrong (item 5) |
| (referee observation, not a return claim) 1109.4343 p.3 "2∆Al = 200 µeV" | p.3 [FT] | Quoted correctly. It is ≈ ½ of the BCS 2Δ for Al (3.53k_BT_c ≈ 0.35 meV). v2 §3.3 should not present it as an equal "reading"; it is likely Δ, not 2Δ. Conclusions unchanged (4Δ ≤ 174 GHz either way) |

## E. CLOSED-AS-EXACT-GAP rows (scope 4)
- **LE-119.** The "missing step (single)" is not single. It names two owners (CW5/LE-141 rates; CW6 D_X, S_surf, s_ℓ) and four object classes. Split it, or call it "two missing inputs".
  The s_ℓ method ("hard line at ω_op relaxing by §2, the conservative choice") is an **assumption**, and it reinstates for surface and electrode release the "born hard" step that v2
  withdrew (A F2, B B1). It is conservative only toward ζ_gap = 0. Required: scan s_ℓ between hard and soft-ballistic (1109.1193 p.17: "low frequency, ballistic regime", 13%), or compute
  it (multiphonon emission at the surface state, with the method named). The rest of the spec (what, 1-D exciton FD solve, convergence, three pitfalls, cost) is adequate.
- **LE-122.** The missing object (σ_ph-ion,j, σ_ii,j) is single and correctly named. Pitfalls missing: (1) D⁻/A⁺ are two-electron states (H⁻-like), so a one-electron hydrogenic model
  does not give their wavefunctions or cross-sections; (2) the Born impact cross-section is invalid near threshold (E_kin ≈ E_b, which is the hot-tail regime the row targets); (3) a 216-atom
  cell (1.6 nm) cannot hold the donor envelope (a* ≈ 2–3 nm), so DFT gives the central-cell correction only; (4) valley–orbit splitting enters σ_ph-ion near threshold. Convergence for the
  cross-section part (basis, valley sum) is not stated. With these added the spec is sufficient.

## F. LIMITS rows (scope 5)
| Row | Verdict | Correction |
|---|---|---|
| L39 (v2) | ✔ | Sources confirmed (1109.1193 p.14 wording now verbatim) |
| L40 (v2) | ✎ | Source "measured effective" → "fitted effective, includes in-film absorption (1805.02495 p.8)". The reciprocity part is DERIVED (item 2) |
| L41 (v2) | ✔ | 1401.1937 p.2/p.5 quotes are verbatim |
| L42 (v2) | ✔ | Algebra reproduced (item 13) |
| CW6-L1 | ✎ | Add "sub-2Δ loss is a model choice that sets the sign of r_coll − 1" and the ζ_O sign convention |
| CW6-L2 | ✎ | Restate as in §C (L1 norms; single-sign condition for Δ_soft) |
| CW6-L3 | ✎ | Validity per §A (isotropised film; mode conversion). Leading correction: the trapped-mode fraction |
| CW6-L4 | ✎ | Pages p.4 (Eq. (4)) and p.7 (Table 4). The B_m,l range is a polarisation spread |
| CW6-L5 | ✎ | Validity: add ⟨𝔮⟩_NR = ⟨𝔮⟩_ER (or 𝔶 for created pairs) and bias-independent y_ion, X |
| CW6-L6 | ✎ | 6.5×10⁴ e/cm² is the jump (max\|ΔE\| ≥ ½ jump). Locality tagged [E] (f⁵ outside ICA at 10.9 THz) |

## G. WP8-R-v2 closing table against the R14 referees (scope 0)
- All REF-A rows (V1–V10, F1–F10, N1–N6, (e)) and REF-B rows (A1–A5, B1–B4, §C, §D, §E) are dispositioned, and the dispositions are present in the v2 text where it says they are.
  Exceptions: (i) "C5c: 0.7 THz hole NTL sits on the 0.73 THz cut (stated)". No such statement is in the v2 body (no "0.73" occurs outside the closing table), so it was **not applied**.
  (ii) "C4f replaced by the e^{−N_mix} argument with computed N_mix": the argument is in §3.2, but no K-check computes e^{−N_mix}, so the weak check is removed, not replaced.
  (iii) B §D asked that L40 not call 0.3–0.55 "measured", and v2 L40 still does (§F). (iv) A F8 ("void") is applied in a stronger form than the algebra supports (§B).
- The thickness, E_2σ (382 A / 368–369 B / 357 measured) and Δ_Al disagreements are ruled correctly on the evidence. I reproduced the E_2σ values in the rerun and confirmed the
  thickness from the full text.

## H. Owed corrections (this referee → targets; exact text)
| # | Target | Exact text |
|---|---|---|
| V-1 | CW6 §7, v2 §3.2, OC-CW6-7, K5f/K6c labels, IF-CW6-8 | replace the "fitted-effective 0.10–0.19" clause with the §A text; "×3" → "×1.25 (AMM/DMM)" |
| V-2 | OC-CW6-2, IF-CW6-2, v2 §0 row 8 and §6 | §B replacement text |
| V-3 | CW6-4 / CW6-L3 / v2 §3.3 τ_l sentence | append "for an isotropised in-film population (60% of Al film flux is totally reflected at Al/Si)" and delete "exactly" |
| V-4 | (CW6-1), K7b, OC-CW6-5 θ_ζ row | "ζ_O ≡ a_prim − a_NTL with film 1 the high-gap film" (or prior on \|ζ_O\|); ζ_gap sign relative to the same convention |
| V-5 | (CW6-2), CW6-L2 | §C bound |
| V-6 | (CW6-3), OC-CW6-3 | add "(⟨𝔮⟩_NR = ⟨𝔮⟩_ER; else y_ion → 𝔶 and 𝒢_gap → 𝒢_gap⟨𝔮⟩_ER as trapped pairs retain E_g)" and "degeneracy broken if y_ion and X are bias-independent over the scan" |
| V-7 | CW6 §6 "2303.02196 measures 0.6%" | "uses 0.6% (impact ionization) and 12.7% (trapping), from its ref. [28] (p.4)" |
| V-8 | CW6 §8, OC-CW6-4 | "2408.04732 Eq. (4) (p.4) and Table 4 (p.7)"; "0.4% above the upper end of the polarisation range of measured B" |
| V-9 | K4b, v2 §2.4 and §0 row 2 ("≥ 96%"), CW6 §10 preamble | "0.24% (10 ns) / 1.9% (100 ns): one instrumented face" |
| V-10 | CW6 §2 cost | "≈ 4.4 h" for the 1-D pass |
| V-11 | CW6 §3 (LE-119) spec, §6 (LE-122) spec | §E additions |
| V-12 | v2 §9 row "weak checks" | C5c "not applied"; C4f "removed" |
