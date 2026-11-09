# Chapter 21 editor notes

## 21.1 drafted (2026-11-06; ~2,700 words; Ch21 opening + map; Limit Check 21.1a; 1 F row)
- Key result: the rate of any channel is a linear functional of f(v) (eq:21.1-functional, kernel eq:21.1-kernel from eq:8.7-handoff); η₂ and every velocity-dependent coupling are fixed by η. Fig. 21.1 reproduces WE 10.1's 1.60e5 /kg-yr. Si floors 0.3332/0.3290 MeV; June lowers the floor 3.9 %, so the floor belongs to its halo (SPINE says "floor": accept the refined statement, fix SPINE). WE: Kuhlen–Lisanti–Spergel debris flow (22 % at 340 km/s): +7.6 % at 10 MeV, −13 % at 1 MeV. Limit Check 21.1a: η closed form vs the year average within 1 % to 430.3 km/s, 10 % to 735.6 km/s.
- Kernel symbols: E.27 𝔎_i(𝐰), C.12 𝗄_i, 21.1 Γ_{N_eh}(𝐯_gal). State one relation (ledger merge / App. pass).
- New symbols avoid "DF" (f_DF is the defect fraction in 19.4).

## 21.2 drafted (2026-11-06; ~3,740 words; D.46 ~1,740; Limit Check 21.2a; 1 F row)
- For a direction-averaged response the bound is exact even with several bins: one stream at u₀ attains it, with a single-bin certificate (D.46). Dropping the halo costs ×2.22 at 10 MeV, ×3.52 at 2 MeV. A failed certificate by δ still bounds (+δN_tot/κ_v). Negative kernel pieces (zero-phonon/dressed split) ≤ (2ω_max/Δᵢ)ϱᵢ = 0.034 for Si, a nuisance for 21.4. Limit Check 21.2a: directional LP vs the isotropic formula 1.00–1.15 (model: EPM anisotropy, labelled). PRIORITY derivation.
- E.27 vs C.12/21.2 symbols (𝔎_i, F, 𝔥, ξ_i vs 𝗄_i, Ξ, 𝖿, λ_i; 𝔥 clashes with 𝔥_off and D.39). E.27's "no longer an upper bound" with negative pieces is wrong (weak duality holds; the mass bound fails). Align E.27 at the App. E pass.
- Pair bins use the step model with Sect. 1.5 values (1.11 eV, 3.6 eV/pair). After Ch18 the book's model is the calibrated cascade: review whether 21.2's example search should use Ch18 (3.75 eV, cascade P(N)) or state that the step model is a simplification for the example.
- The C.12 Lipschitz bracket is 45 % wide for tabulated kernels; a refined-grid scaled-dual check is recommended (moves 0.095 % at 600 km/s).

## 21.3 drafted (2026-11-06; ~3,300 words; tab:21-edge; WE gap shift; no box)
- Key result: edge power law (m − m_edge)^(p_on + k_tail + 7/2) (corner: +4), from the kernel onset (p_on + 3/2) and the halo escape tail (lens construction, (v_max − v)^(k_tail+1)); k_tail from Lisanti et al. (0 SHM, 1 King, 1.5–3.5 sims). Reduces to eq:13.9-medge and the 1.3 quadratic edge. Exposure reach ∝ (exposure·σ̄_e)^(−1/n). Degeneracies: E_on/v_max² (±25 km/s ≡ 73 meV); the zero-phonon edge mixes gap and v_max differently (0.54/−1.62 vs 1/−2); the year-average edge sits at June 0.3243 MeV with power +½ (×62 at 0.010 MeV above the edge). WE: 10 meV gap shift moves the edge 0.00283 MeV (×231/8.8/2.7 weaker), equivalent to −3.3 km/s in escape speed. PRIORITY derivation (incl. the zero-phonon onset exponents 5/2, 2, 1 and the 1s off-axis minimum).
- Make 21.1's floor paragraph and 21.3's year-average statement one position (review).
- Comparison halos use the book v0 = 238 km/s (Lisanti refit v0 per k); the caption says so.

## 21.6 drafted (2026-11-06; ~3,330 words; Table 21.1 schema (10 rows); WE library entry)
- WE: Knapen–Kozaczuk–Lin Si loss at |q| = 3732 eV, ω = 9.86 eV: L = 0.1442 → S = 4.38e7 eV²; local fields −0.090. The Ch08 EPM model and the published tables share a truncation label but differ ×0.864 at 10 eV (screening 0.29 vs 0.24).
- 10.10 (accepted) says the published Si tables carry a 1.11 eV room-temperature scissor; the source (Sect. III B) and 10.6 say the scissor matches the 0 K measured gap. The 1.11 eV in the DarkELF constants file sits next to ε_eh = 3.6 eV (the step-model conversion). Check 10.10 and fix (light pass).
- Two release tolerances (S_ab min eigenvalue ≥ −1e-6 tr; KK residual < 1 %) come from the planning source, not App. E. Accept, or add them to E.
- The patch/major version rule is the writer's refinement (stated as the book's rule).

## 21.5 drafted (2026-11-06; ~3,650 words; tab:21-recast; Fig. 21.5; WE combine)
- Unknown background: counting all events as signal is valid for any background; Yellin max gap 2.836 vs counting 3.890 (separated events), 7.78 with one event mid-signal; optimum interval stated. Combination: one likelihood, theory nuisances shared. WE: 0.928e-42 cm²; shared δ = 0.25 costs ×1.109, split per exposure only ×1.051 (≈5 % too strong). Recast rule/bracket: bin-uniform corrections recast exactly; bin-dependent only with per-bin upper counts; profile-likelihood/optimum-interval not recastable from the curve; a min over n bins at 90 % covers 0.9ⁿ. Dirac: isotropic ε_bg² exact (Hochberg ×1600); ZrTe₅ anisotropic 5200–6400 above 20 keV, 820 near threshold (ε_yy² = 431), so recast from rates. Boosted flux: limit ∝ R^{-1/2} (quotable REF-DC-49-54-36 §4 items 1–3). PRIORITY derivation.
- One statistical construction chapter-wide? WE uses an exact Neyman construction (k² coefficient 2.30) vs 21.4's 1.15 and 0.65. Rule at review.
- 10.9 (accepted) is partly out of date: the compute results now settle the cosmic-ray-boosted heavy-mediator case and the light mediator above 10 keV. Light-pass 10.9.
- Pair bins: step model 1.11/3.6 eV (as 21.2). Same pending question about switching to the Ch18 calibration.
- 𝒦_j vs 14.6's 𝒦_t: consider another letter.
- The last one-sentence edit is not rebuilt.

## 21.4 drafted (2026-11-06; ~3,100 words; D.47 ~930; Fig. 21.4; WE; nuisance table per channel)
- WE (Si, 3 MeV, heavy, 1 kg·yr, 0 events): RPA limit 9.23e-42 → 1.30e-41 cm² with local fields + low-T gap; band 8.8e-42–1.93e-41 (σ_β 0.393); profiled 1.53e-41 (1.44e-41 with one-sided attraction). Band ×3.4 at 1 MeV, ×1.48 at 3 MeV, ×1.43 at 10 MeV; dominant-nuisance switches at 1.15/3.59/6.98 MeV. PRIORITY derivation (D.47).
- The profiled limit uses the threshold calibrated to return the classical limit (as 8.8). 21.5 uses an exact Neyman construction: chapter-wide ruling needed (with 21.5's k² coefficients 2.30/1.15/0.65).
- The attraction template is set to zero above 10.5 eV (caption); the 10 % efficiency is illustrative; the 1 MeV tabulation spread ×3.2 is new (10.10 quoted 3 and 10 MeV).

## 21.7 + summary drafted (2026-11-06; ~5,980 + 1,750 words; Table 21.2 guide (landscape, 14 rows); Fig. 21.6; WE CsI; tab:21-nuisances 22 rows)
- Leaders match SPINE 21.7; survivor values quoted from tab:17-rank. Full-pool rerun with book inputs differs from the research: CsI 3.73 (3.89), h-BN P(first) 0.656 (0.606), Si ε 3.749 (3.72). The CsI rerun owed by the compute results is done here. GaSb's estimated ε beats Ge's measured with P = 0.83 (stated). Ge pair energy 3.37 eV is a model-dependent fit (2.96 at 77 K). ²¹⁰Pb+²¹⁰Bi: 689 /kg/day/keV below 1 keV per Bq/kg, so ≤ 1.45 mBq/kg for a 1 /kg/day/keV budget (convention, stated). Ge tritium 7.31 at saturation (research 6.7); Si agrees with E.27.
- SPINE open problem on elastic constants: now TeO₂ + computed-tensor crystals + the CsI cold density (diamond, CsI measured). Update SPINE and the Ch22 index.
- Most capability statuses follow the research screening record without citation (GaAs, diamond cited from abstracts). Review: source what can be sourced.
- Recheck the summary after the 21.1–21.6 review (the statistical-construction ruling for 21.4/21.5).

## Ch21 review rulings (2026-11-06; five reports: derivation-1/2, prose, reader-a/b — MINOR GAPS / REVISE, no REWRITE)
- R1. One statistical construction chapter-wide: the Neyman construction of 21.5 (nuisance at its conditional best fit). Update 21.4: the profiled factor e^{σ_β²N90} = 1.427, the second-order coefficient of eq:21.4-profile doubled for zero counts, the WE numbers. Add a note in D.47. Update the summary table. Remove the three-coefficient comparison.
- R2. Pair bins: switch the 21.2 and 21.5 examples from the step model to the book's Ch18 cascade (figscripts/ch18/casc18_3.json / si_cascade18.py; NOT the DC-67 library, which DC-RESULTS forbids quoting). Expected (derivation-1): at 10 MeV the one-pair bin binds; σ_lim 3.72e-42; bound at 500 km/s 3.61e-20; costs ×2.13 (10 MeV), ×3.7 (2 MeV). Rewrite WE 21.2's story and the bin crossovers accordingly. Make the leakage factor consistent with ε = 3.75 eV. Reconcile the two tables on the two-pair claim with 21.7/R19 (step ~10× high).
- R3. One position on the June shift: the exposure-averaged rate (year average) is the correct basis for a limit, and the June floor is part of that average, not a halo uncertainty. Reword 21.1 l.92, 21.4 l.34 and the summary. "June escape speed" → "June Earth speed".
- R4. Published Si tables (Knapen–Kozaczuk–Lin, 2101.08275 Sect. III B): the scissor already matches the measured gap at T = 0, so the ×1.048 "cold gap" correction in 21.4 is a double count. Recompute WE 21.4 and Fig. 21.4 (nominal 1.24e-41; band 8.4e-42–1.84e-41; profiled per R1). Fix Section 10.10's "1.11 eV room-temperature scissor" sentence by a narrow edit, and check 10.10's numbers for the same double count.
- R5. ²¹⁰Pb budget (21.7, summary): the ²¹⁰Bi part is 12 % (an eighth), not a sixth. The Z_d = 83 Fermi function belongs to the ²¹⁰Pb decay (²¹⁰Bi has Z_d = 84). Use a relativistic Fermi function (~724 /kg/day/keV per Bq/kg) and recompute the mBq/kg limit.
- R6. Number and statement fixes:
  - ZrTe₅ recast ~5100 at 20 keV.
  - The dominant nuisance changes only at 3.59 MeV; 1.15/6.98 are subdominant swaps.
  - Tabulation spread: one treatment (a bound entered as an envelope, consistent with 10.10/21.6; not a Gaussian nuisance), or justify the Gaussian with a stated prior.
  - 600 TB: state the basis or drop it.
  - The 21.5 boosted-flux clause uses the quotable REF-DC-49-54-36 §4 wording.
  - 21.3: 6.6 % ↔ 78 meV (+25 km/s → −6.0 %); the 1 % phonon-error statement.
  - Limit Check 21.1a boundary 740.3 km/s (or state the convention).
  - Limit Check 21.2a: credit Fox–Liu–Weiner (A1) for the single-bin form; the box title must match its content; the "up to 15 %" sampling range stated.
  - The 21.2 keyresult box adds the condition 𝒜_i(u₀) > 0.
  - 21.4: 1.101 (second order) vs 1.103 (exact).
  - Leakage: 0.034 ϱ_i, with the stochastic-ordering condition stated correctly (summary).
  - 21.7: where KTaO₃ enters the pool.
  - eq:21.5-C0 in regular form (g = ½, ⅓).
  - v_max^{2p_on+8} "at fixed edge mass" (verify the exponent).
  - State the envelope theorem.
  - Define "stochastically ordered".
  - ω_max 63.7 meV (NOTATION).
  - Optional: the scaled-dual check made exact at the cell break speeds.
  - Gloss u_ν; explain the TA phonon at Q* (~15 meV); a brief note on CL_s and the hybrid construction.
- R7. Prose:
  - the opening's second paragraph → motivation, not an outline;
  - "no reading" → "no resolved leader"; "gap" → "coverage hole" where meant;
  - 21.7 l.83: point to Ch20 instead of restating it;
  - the union bound, the E.27 pointer and the tabulation spread each stated once;
  - register; house forms (cross-section, nonnegative, km s⁻¹ per STYLE);
  - punctuate eq:21.7-pb210; fix the D.47 typo; capability statuses sourced where possible.
- R8. Notation: c (stream weight vs speed of light; Ξ-mass), δ (four meanings), 𝒦_j vs 14.6's 𝒦_t, β_k/σ_β, μ in D.47, the six undefined symbols, the kernel symbols vs C.12/E.27 (state one relation).
