# Chapter 20 editor notes

## 20.5 + summary drafted (2026-11-06; ~4,460 + 1,430 words; tab:20-nuisances 15 rows; fig:20-rcoll, fig:20-ceiling)
- Sign number promised by 19.5: 𝔯_coll − 1 = s_ng − (1 − κ_sub)s_sub. s_sub 0.017–0.058 at mean Luke 0.75 meV; two-film 𝔯_coll 0.935–0.998 (sub-gap lost), 0.992 (Al absorbs). BUT the film yield near threshold (2Δ…4Δ) can raise 𝔯_coll to 1.04–1.09: the sign is not fixed. The yield ramp 4Δ–6Δ is the writer's model choice; check it against 20.4. Forwarded to the Ch19 reviser (a clause in 19.5).
- The campaign toy's 𝔯_coll 0.87–0.98 came from cutting its spectrum at the grid edge (sub-gap share 0.118 vs 0.017–0.058): superseded. Log in CORRECTIONS.
- HV readout ceiling: 1.22 at central inputs at 220 eV/100 V; max 1.72 over 1σ; > 2 below 224 eV at 2σ. The no-go at E_R ≤ 300 eV is conditional on Y_q, F_NR, collection and C.L. Differs from the campaign's 1.9986/2.014 (measured yield rows only; book F).
- E.25: ℭ_s = fraction ending as quasiparticles ("absorbs" → precise); the ϖ_O range extends to 0.03 at 4.7 meV.
- 20.1's "15 % better" → about 13 % (revised 19.5 gives 1.128).
- F_eh 0.119 (measured, used for ER) vs 20.1's 0.114 (cascade): make the convention explicit.
- Summary paragraphs for 20.2/20.4 and two nuisance rows rest on SPINE + 1401.1937: recheck.

## 20.1 drafted (2026-11-06; ~4,200 words; Ch20 opening + map; Limit Checks 20.1a–c; 3 F rows)
- Measured-charge Fano: WE at 95 % collection in Si gives 0.158 (binomial), 0.170 (published formula), 0.125 (midplane partial charges), 0.136/0.165/0.324 for uniform depth at 0.1/1/5.9 keV. PRIORITY derivation (general formula with cascade, partial-charge and position terms).
- PRIORITY: E.12 eq:E.12-luke (from G4CMP Eq. (8)/Leman Eq. (21)) is smaller by k_s/k than the golden-rule Luke rate derived in 20.1, and smaller than the integral of E.12's own angular law. Settle at review; align E.12.
- ε_s 11.4 (mK) vs 11.7 (E.25) for space charge: one book-wide value (light pass; also 18.5 note).
- Limit Check 20.1a uses an illustrative saturating drift (no tabulated mK data). The drift heating (mean Luke energy 1.1–2.1 meV at 1–4 V/cm) is an upper estimate.
- Hecht/Shockley/Ramo cited "as quoted by" Lachish.
- Luke-rate transverse-phonon correction unsized: DEFERRED.

## 20.4 drafted (2026-11-06; ~3,430 words; Limit Check 20.4a; 1 F row)
- Key result: the yield is exactly 2Δ/E below 4Δ (kinematic proof). WE: 3Δ phonon in Al, Y = 2/3, t_pb 0.206 ns. Cascade (0.01Δ grid, MC within 1.2σ): no-escape peak 0.600 at 5.46Δ → 0.590 (published 0.57–0.6); at 10Δ 0.349–0.554 for t_l/t₀ = 0.5–8; Guruswamy Fig. 4 lies above by 0.001–0.011 (t_l/t₀ ≤ 4), 0.036–0.041 at 8 (digitized at 200 dpi, ±0.005). Arrival-band yield drop 20.5/6.5/1.7 %. Electrode recombination phonons 85/92 % ≤ 2Δ_Al (87 GHz): ballistic (isotope mfp 39 m Si, 1.5 m Ge).
- RULING FOR THE CH20 REVIEW: 20.5's near-gap yield model (2Δ/E then a linear rise to 0.59 at 6Δ) must be replaced by 20.4's logged cascade (0.594 at 5Δ, max 0.600 at 5.46Δ, 0.595 at 6Δ, and the escape-dependent values). Recompute the 20.5 𝔯_coll band (0.935–0.998; 1.04–1.09) from it, and update 19.5's pointer text if the band moves.
- Kaplan 1976 "as quoted by" Leman.

## 20.3 drafted (2026-11-06; ~3,350 words; Limit Check 20.3a; 2 F rows)
- Oblique AMM solved (Voigt isotropic): Si→Al 0.934, Al→Si 0.327 (DMM 0.741/0.259); reciprocity from S-matrix unitarity (6e-16); 59.8 % of the Al film flux trapped beyond 35.2°. Escape time t_l = 4d_f/(v_s t̄_esc): 60 nm Al 0.223–0.281 ns (t_l/t₀ 0.86–1.08). The lumped film form (E.12) understates thin-film absorption by 1/t̄_esc = 3.06. The fitted 0.3–0.55 = t̄ × P_abs constrains 𝔩_f/d_f ≈ 6–26, not the escape probability. Impedance law within 10 % only for speed ratios 1.175–1.273 (overstates Al escape ×3.03). PRIORITY derivation.
- RULING FOR THE CH20 REVIEW: Al elastic constants. Ch15 R1 adopted the 0 K set (Malica–Dal Corso; sound speeds c_LA 6.47, c_TA 3.40 km/s with ρ(0 K) = 2.73), and the room-temperature C.18/Kittel values are superseded (refit owed in 6.4/C.18; CORRECTIONS §19.13(g)). 20.3 must use the 0 K set as primary (t̄_esc +12 %, t_l −16 %) and drop the room-temperature numbers to a sensitivity. Propagate to 20.4/20.5 (t_l/t₀) and E.25 (critical angle).
- E.25: transverse critical angle 34.9° → recompute with the 0 K set; clarify the "3–12 %" reference.
- Swartz–Pohl cited without a locator (content derived); t₀ = 0.26 ns near 2Δ "as quoted by" Guruswamy.

## 20.2 drafted (2026-11-06; ~4,380 words; Limit Checks 20.2a/b; 3 F rows)
- Memory-loss times: SPINE "≈10 ns (Si), 30–100 ns (Ge)" holds only for prompt phonons born near the band top (6.8 ns Si, 47 ns Ge). For births in the upper factor-two of the band: 0.15 µs Si, 1.0 µs Ge. For 22 meV TA phonons from optical decay (ER): ~1 µs Si, and the memory region near the sensor face is 13.5 % of a 4 mm crystal. Rule: a birth is forgotten at E_* ≈ 0.52 of its energy, so the time ∝ (birth energy)⁻⁵. These are continuum estimates at 5–15 THz, where Rayleigh is off in Si. Fix SPINE/SOTA wording; 20.5's discrimination verdicts depend on it (review must check the 20.5 consistency).
- Transfer-kernel bound: loose for the model spectra (0.15 vs actual 0.012 at 1 µs); reduces to f_s = 1.7 % only when every hard birth lies above the memory energy.
- Rayleigh within 10 % in Si only below 5.6 meV (1.36 THz).
- Ge isotope constant: Leman 6.43e-55 vs Hernandez 1.65e-54 s⁴, both "quoted by" Tamura (unread). Resolve at review if possible.
- The daughter distribution uses a Beta(3,3) stand-in: the shape constants are model numbers.
- E.25 τ_h → Δ_h (τ is imaginary time).
- WE: natural Si B_iso 2.44e-42 s³ at 1 THz (measured 2.42–2.56).

## Ch20 review rulings (2026-11-06; reports derivation-1/2, prose, reader-a/b — MINOR GAPS / REVISE, no REWRITE)
- R1. 𝔯_coll rebuilt with film escape (substantive). In kern20_5.py use 20.4's logged cascade yield (not the linear ramp) together with film escape at the t_l/t₀ of 20.3 (0 K Al constants, R3). Recompute the 𝔯_coll band over ⟨E_L⟩ and over film thickness/geometry (one Al film, two-film; derivation-2 finds 1.05–1.13 at ⟨E_L⟩ ≤ 1 meV for one Al film with escape). Use the validated DC-83 mean Luke energy 0.84 meV at 1 V/cm (20.1's 1.09 is an overestimate) where the operating point enters. State the band honestly. If it contains 1.128, say collection alone is not excluded by transport and that the two-bias measurement (19.5) is what separates collection from stored energy. Remove "outside every value of this estimate". State that the near-gap model lowers 𝔯_coll at 0.75 meV without escape (0.91–0.93). The coordinator amends Ch19 to match after this pass (do not edit Ch19).
- R2. Memory-loss times: 20.5, the summary and the nuisance table use 20.2's values (6.8/47 ns near the top; 0.15/1.0 µs broad; ~1 µs for 22 meV TA; 13.5 % of a 4 mm crystal near the face at 1 µs). The primary-phonon discrimination limit is an estimate, not a bound. Remove "a few percent".
- R3. Al elastic constants: 0 K set, isotropic (Voigt) speeds 6.63/3.30 km/s at ρ = 2.70 (Ch15's 6.47/3.40 are [100] speeds; flag for a Ch15 light pass). Rerun 20.3: t̄_esc 0.368, t_l 0.187 ns, t_l/t₀ 0.72–0.94, lumped factor 2.72 (thin limit; ~1.9 at 60 nm, state both), critical angle 37.7°, 𝔩_f/d_f 5–23. Propagate to 20.4/20.5 and E.25. Room-temperature numbers become a sensitivity.
- R4. Luke rate: 20.1 is right. Fix E.12 eq:E.12-luke by a narrow edit (factor k_s/k; "grows as k²"). State in 20.1, in one neutral clause, that Leman Eq. 21 / G4CMP Eq. 8 are low by k_s/k while their angular law (Leman Eq. 22, G4CMP Eq. 9) integrates to the golden-rule rate.
- R5. Number fixes:
  - HV 220 eV: 1.72 is the mean-charge limit; the binomial limit gives 1.36. State both wherever 1.72 appears.
  - Low-bias ceiling 10.8 (extend the bias grid past 0.3 V).
  - Film loss 49–60 % over 16–60Δ (not "up to 40 %", which is Guruswamy's 10Δ figure), in 20.4 and 20.5.
  - ch20.tex opening 15 % → about 13 %.
  - 62 meV is the band top, not the Debye energy (55.6 meV).
  - 45 meV phonon spread 1.0 µm; hole Luke mean 1.14 meV at 1 V/cm; recheck "4.4 meV" and "a quarter below 3 meV".
  - The face-sheet bound: the 6.3e4 cm⁻² face value applies only in a vanishing slab; restate.
  - WE 20.2 δ^M sign.
  - The fig 20.2 caption gains the LA:TA energy shares.
  - The summary's electrode-phonon origin.
  - State that t₁ = 3.87 t₀ depends on Y_q.
- R6. Citations: Leman Sect. III G (not IV G); Leman does not give the pair-breaking rate (fix the attribution). Source the 0.7–2.7 THz band or drop it. 20.2's ω_opt 64.1/37.6 meV is not in Leman Table I: re-source it. Ge isotope constant: give both quoted values with "quoted by" and say they disagree.
- R7. Structure and prose:
  - cut the 20.5 verdicts subsection (a second summary) and keep the facts in the Summary;
  - 20.5 does not re-derive 20.2's soft-phonon share: point to it;
  - "transport codes are not validated" stated once;
  - E.25 pointers reduced;
  - "as quoted by" notes kept only where needed;
  - register;
  - US spelling.
- R8. Notation:
  - t₀ (pair-breaking time) vs 19.5's track time: rename one;
  - b(t) → f_ret; f_soft/ω_op → f_s/ω_opt; ε_0 vs ε₀;
  - one x_L (0.093 or 0.0975 from the log);
  - F_eh convention stated (0.119 measured for ER signals; 0.114 cascade);
  - one Al sound-speed set;
  - add the missing rows.
- R8 addendum: x_L (Ch20 longitudinal phonon share) clashes with Ch19's x_L (Lindhard reduced transfer variable): rename the Ch20 symbol (e.g. f_LA).
