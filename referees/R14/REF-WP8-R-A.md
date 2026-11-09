# R14 referee REF-WP8-R-A (hostile, isolated): returns/R13/WP8-R.md

Read: returns/R13/WP8-R.md, code/WP8-R/checks.py (rerun: **48/48 PASS, 1.4 s**, output identical to the return's tables), returns/R8/WP0-v3.md,
WP5-v3.md (grep), returns/R12/WP7-E-v3.md (grep), CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS, STATEMENT. Full texts were fetched with lit.py into
literature/papers-r14-REF-WP8-R-A/: 1109.4343, 1109.1193, 1805.02495, 2302.05998, 2012.12430, 1401.1937 and 2408.04732. All were read where cited, and the PDFs (and
the HTML/text copies) have been deleted. Re-checks are sympy/numpy only, ≤ 1 s each (scratchpad ref.py; not committed). No simulations were run.

## Verdict table
| # | Main claim | Verdict | Reason |
|---|---|---|---|
| V1 | NR/ER prompt populations differ at birth in branch mix and in the ER soft fraction f_s ≈ ω_op/ε_eh = 1.7% / 1.2% | STANDS WITH CORRECTION | The arithmetic is right. f_s rests on two assumptions: a uniform residual on [0, ω_op], and the 1805.02495 "Debye energy" used as ω_op. The NR branch mix is an assumed thermal spike. All of this is [E], as tagged, but "8–15 THz" is Si only (f_D(Ge) = 8.64 THz) |
| V2 | Frequency/polarisation memory is lost in t_mem ≈ 10 ns (Si) / 30–100 ns (Ge), ℓ_mem ≲ 0.1 mm | STANDS WITH CORRECTION | The rates, f_*, N_mix and r_rms reproduce. "Here it is derived" (§2.3) is an overclaim: the result is a toy linear cascade with an assumed Beta(3,3) kernel → [E], not [D]. The scope must be **bulk events farther than ℓ_mem from an instrumented face** (§F1) |
| V3 | AMM is frequency-independent in the primary band, L/T contrast is 0.95–1.10, and η_pb is "flat above 4Δ_BCS" | STANDS WITH CORRECTION | The AMM/DMM numbers reproduce. "η_pb flat above 4Δ" is **REFUTED** by 1401.1937 (§F4). The L/T contrast is for normal incidence only (§F5) |
| V4 | (a) Mode-selective collection of primaries is NO-GO; 2σ first reached at 0.52 keV (ζ_O = 1, σ_pos = 0) | STANDS WITH CORRECTION | The verdict holds through the σ_pos cap. The noise convention is inconsistent with §4.1 (an extra √2); with the stated 𝔖 the threshold is **0.38 keV** (ζ_O = 1) and **1.33 keV** (ζ_O = 0.3) (§F6) |
| V5 | (b) Zero-field gap-energy channel: ζ_O = 0 under mode selection, so only timing can read it | FALLS (the "ζ_O = 0" sub-claim); the flag stands | The precedent contradicts it. Surface-released gap energy arrives "in a low frequency, ballistic regime that is used to provide a surface-event discriminator" (1109.1193 p.17 [FT]) (§F2) |
| V6 | (c) HV/NTL mode is NO-GO at any contrast for E_R ≤ 300 eV | STANDS | It is a pair-number ceiling. With energy-dependent 𝔶 the ceilings are 0.53 / 0.82 (F_NR = 1) and 1.57 at 300 eV (F_NR = 0.15). The 1-keV range becomes 1.33–2.55, not 1.67–3.15 (§F6) |
| V7 | (d) Low-bias phonon-read NTL route: CONDITIONAL, with ζ_O,min = 0.15 / 0.28 / 0.53 at 100 eV | STANDS WITH CORRECTION | ζ_O,min at 100 eV reproduces. Off 100 eV the code freezes 𝔶 = 𝔶(100 eV), σ_Nph is defined but omitted, a third (gap/relaxation) population is missing from O, and the CDMS calibration transfer is unsupported (§F6–F7) |
| V8 | IF-E7: δ cannot carry the 0.048 deficit; r ≠ 1 is expected, its sign open | STANDS WITH CORRECTION | Only **δ_prim** is bounded. The return itself admits non-spectral δ. The "sign open" result undercuts WP7-E-v3 conditions (B-a) Δϵ ≥ 0 and (B-b) r ≥ 1 (L36, E_st bounds), and no flag is raised (§F8) |
| V9 | Overall: NO-GO for the brief's target; (d) is a measurement proposal | STANDS WITH CORRECTION | The verdict is right but the reasoning is wrong in part: (d) does use a frequency-selective interface (the Nb-like film supplies ζ_O, §3.3, §5). The valid reason is that (d) is a yield discriminant bounded by the yield's own pair-number ceiling, with 𝔶 underived below 352 eV (§F9) |
| V10 | LIMITS L39–L42 | L39 ✎, L40 ✎, L41 ✎ (falls as written), L42 ✔ with correction | §F10 |

## Rubric (f): the CDMS precedent against the central claim
**F0. What the precedent uses (1109.4343, full text, p.2–3).**
- *Bulk ER vs NR.* The separation is charge-mediated. The paper says: "Much of the essential information content of the charge measurement is duplicated
  in the phonon measurement, through the production of secondary phonon populations as charges propagate". The fast component is near-surface,
  high-field NTL (∼300/700 GHz). The return's reading is **CONFIRMED**, and so is its statement that relaxation phonons are ignored ("since they are initially ballistic").
- *Primary phonons.* The precedent **does** use frequency information at arrival, as a clock and position meter. "If the event occurs near a sensor surface,
  there is little delay in arrival, and the comparatively short mean free path increases the rate of absorption". The absorption rate is set by the
  frequency-dependent mean free path: "A phonon's timescale of surface absorption … is therefor highly dependent on mean free path" (6.1% Al coverage).
  1805.02495 p.8 [FT] agrees: when the source is near the absorber, the absorbed spectrum has "a longer tail to higher frequencies".
- *Surface events.* Leman 1109.1193 p.17 [FT]: recombination phonons at the surfaces, 13% of the signal, are "in a low frequency, ballistic regime that is
  used to provide a surface-event discriminator". This is a frequency-distinguishable, charge-borne gap-energy population.

**Verdict on the hole.** For **bulk** NR/ER, the precedent does not use initial-state primary information. It assumes the same loss of memory (1109.1193 p.13:
"details of the distribution will rapidly be lost … the detector's phonon response is insensitive to variations in the distributions"). So the central claim
has no hole there. It does have three holes in scope and in its sub-claims:

**F1. Near-sensor events (scope).** ℓ_mem is measured against L = 1 cm. The return's own numbers give r_rms ≈ 10 µm at 10 ns (scaling t^0.9 from 77 µm at 100 ns).
Within ≈ 10–80 µm of an instrumented face, hard primaries reach the film **before** t_mem, which is exactly the near-sensor regime 1109.4343 describes. The
reference device behind σ_ph = 2.65 eV is the 2012.12430 CPD, and that device is **1 mm thick** (Table I [FT]), not 1 cm. There ℓ_mem(100 ns) ≈ 8% of the thickness.
*Correction:* the NO-GO holds for the bulk population (events farther than ℓ_mem from a sensor face, which is a volume fraction ≳ 0.9 in a 1-mm CPD). The
near-face shell is a position class with residual primary memory. It is not a usable NR/ER discriminant at that volume fraction, but the statement "the
populations lose … memory" in §0 and IF-R6 must carry this scope. The comparison "≪ τ_ph" is unaffected.

**F2. Gap-energy channel (V5 FALLS as stated).** §1.2 and §4.3 assert that gap phonons "are born hard (multiphonon/Auger), so they lose memory" and that ζ_O = 0. The
first part is [UNVERIFIED], and the second is contradicted for surface release (Leman p.17). Carriers or excitons that recombine at a surface, or enter Al
(1109.4343 p.3: gap energy goes "into Al quasiparticles … and a population of initially high energy phonons", which become ballistic), produce a population with
its own channel fraction. With Δf_g = 0.26 (Si), that population is the largest NR/ER-differing phonon population at zero field. *Correction:* ζ_O(gap) is
**unknown and release-location-dependent** (bulk hard vs surface ballistic, or direct QP injection). It is zero only for bulk multiphonon release. Row 5 and IF-R2 should
read "ζ_O(gap) open (G-R2)", not 0. The channel remains charge-mediated (∝ 1 − 𝔶), so it does not rescue a non-yield discriminant.

**F3. Sensor-side frequency selectivity (V3 scope).** §3.3 says no listed sensor "is frequency-selective in the arriving band". The dominant frequency selectivity
in CDMS-type detectors is **geometric**: the per-bounce absorption with partial coverage turns the mean free path ∝ f⁻⁴ into an f-dependent absorption time.
That is the mechanism that gives (d) its ζ_O. It does not change any NR/ER conclusion for primaries (common spectrum), but the §3 summary "transmission …
carries no NR/ER information" should not read as "collection is frequency-blind".

## Rubric (b)/(c): sources, from full text
| Return's citation | Check | Rating |
|---|---|---|
| 1109.4343 p.2 "36.7×10⁻⁴²", τa⁻¹ = 1.61×10⁻⁵⁵ν⁵, "755 µs", 6.1% coverage | verbatim | CONFIRMED |
| 1109.1193 Table I: B = 2.43e-42/3.67e-41 s³, A = 7.41e-56/6.43e-55 s⁴, v_L, v_T, ρ, ν_D, E_g, ε = 3.81/2.96 | verbatim | CONFIRMED |
| 1109.1193 p.14 "∼0.1%" per surface interaction, "∼33%" aSi–Al; p.17 L₀ ∼ 720 nm, 56% / 13% | verbatim | CONFIRMED |
| 2302.05998 p.4: L-only down-conversion ("negligible … not implemented"), L → L′T, L → TT; 53.1/37.6/9.3% (Si), 53.5/36.7/9.8% (Ge) | verbatim | CONFIRMED |
| 1805.02495 abstract: Si–Al 0.3–0.55, AMM favoured; p.6 "wiped out after the quasidiffusion stage", "∼62 meV"; p.7 peak 0.7–0.9 THz | verbatim | CONFIRMED, but the 0.7–0.9 THz peak is a **Monte Carlo output that starts from the Debye energy**. Citing it as agreement with §2 is circular (it assumes the result). The 0.3–0.55 is for a **380 µm** Si / 60 nm Al device |
| 2012.12430: σ = 2.65(2) eV, 20 µs rise, fall 30–160 µs, efficiency ≳ 29% | verbatim (Table I) | CONFIRMED; thickness 1 mm (see F1) |
| 2408.04732 Table 3: Si μ = 68.58, λ = 53.68; Al₂O₃ 166.24 / 139.8; A: Si 1.15 (calc), 0.741 lit; Ge 6.8 (calc), 16.5 lit (×10⁻⁵⁵); Table 4 B(Si) 2.33 calc, 2.42–2.56 meas | verbatim | CONFIRMED |
| 1401.1937 "η_s ∼ 0.57–0.6" | verbatim, but only "for infinite superconducting volumes" | CONFIRMED as a quote; **misapplied** (F4) |
| §2.3 "The source assumes this; here it is derived" (on 1805.02495) | the source's assumption is quoted correctly; the "derived" is a toy model | the claim of improvement over the source is UNSUPPORTED |
The return makes no claim that a published paper or database is wrong. Nothing in this category is REFUTED except the return's own reading of 1401.1937 (F4).

**F4. η_pb is not flat above 4Δ (REFUTED from full text).** 1401.1937 §II (Fig. 4): "For 2∆ ≤ hνs ≤ 4∆, ηs reduces monotonically … At … 4∆ ≤ hνs ≤ 6∆ the
efficiency tends to increase again … The overall effect is a reduction in ηs as hνs increases for finite τl/τ0φ". The flat 0.57–0.6 holds for infinite volumes.
In thin films (finite phonon-loss time, which is the d_film/L_pb case the return itself raises) η_pb **decreases with Ω**. Check C5 tests only [2Δ, 4Δ), and the
code returns `None` above it, so the flatness is asserted, not checked. *Correction:* V3/row 3, §3.3 and L41 should read "η_pb(Ω) → 0.57–0.6 for Ω ≫ 4Δ in
thick films; in thin films it falls with Ω at a rate set by τ_l/τ_0φ (1401.1937 Fig. 4)". This is one more ζ_O lever. It does not create an NR/ER primary contrast.
Side note (e): 1109.4343 p.3 gives 2Δ_Al = 200 µeV, against 0.36 meV implied by the return's Δ_BCS = 0.18 meV [UNVERIFIED]. Either value leaves C5b true.

**F5. L/T contrast (V3).** The 0.95–1.10 values are normal-incidence ratios, plus an SH flux average. For Ge/Al, v_L(Al) = 6379 > v_L(Ge) = 5310 m/s, so L has a
critical angle at 56°, and the flux-averaged L transmission (P–SV with mode conversion) is not computed. "Best L/T contrast is 10%" is therefore unproven. It is
irrelevant to the verdict, because it multiplies e^{−N_mix}, but the sentence should say "at normal incidence".

## Rubric (a)/(e): derivations, numerics, tags (recomputed)
- **Rates and scales.** f_eq = 33 / 228 THz; f_*(1 µs) = 2.71 / 2.29 THz; N_mix = 5B(x_L𝒜_anh)^{−0.8}t^{0.2} = 652 / 5072; r_rms(100 ns) = 77 / 16 µm;
  f_b = 0.72 / 0.32 THz. **All reproduce.** Ge uses A = 1.61e-55 (the smallest of the four values), which is conservative for the claim (slowest decay). Γ_iso/Γ_anh,L is only
  3.3 at 10 THz in Si, so "mixing outruns decay" holds only marginally at the start. The return states this, and it is acceptable.
- **§2.3 tag (a).** The memory-loss "derivation" needs: a self-similar (f-independent) energy-fraction kernel, a pure f⁵ law up to f_D (optical phonons
  violate it: their real lifetimes are ps, i.e. faster), and no surfaces. That makes it a scaling **argument** plus toy numerics. Tag [E] (or [D, sketch] for the
  self-similarity), not DERIVED. The TV "<10⁻³ at 10 ns (Si)" is 0.001 at print precision, which is borderline.
- **F6. 𝔖 code and convention errors (e).**
  1. `fom_prim` uses noise √2·σ_ph/E_R, while §4.1 and `fom` use σ_ph/E_tot. With §4.1's definition: 𝔖(ζ = 1) = 0.28 / 0.54 / 1.58 / 5.07 / 14.5 at
     50 / 100 / 300 / 1000 / 3000 eV, and E_2σ = **382 eV** (ζ = 1), **1330 eV** (ζ = 0.3). One convention must be fixed. The primary-route verdict survives only through the
     σ_pos cap (σ_pos ≥ 0.7%·ζ_O). The NO-GO must be stated as **conditional on σ_pos ≳ 1%**, not as "S < 2 at E_R ≤ 300 eV, so NO-GO at sub-keV". With ζ_O = 1 and
     σ_pos = 0, 300–1000 eV **is** sub-keV and ≥ 2σ under §4.1. A soft-vs-hard ζ_O ≈ 1 is unphysical, though, because the soft band 0.3–1.4 THz overlaps the arrival
     band 0.7–2.7 THz. State that, and the NO-GO is clean.
  2. `fom` and `fom_prim` freeze 𝔶 = 𝔶(100 eV) = 0.153 at all E_R (code line 214: `yy = y100[mat]`). With 𝔶(E) = 0.139 / 0.177 / 0.209 at 50 / 300 / 1000 eV:
     the NTL row at 10 V, ζ_O = 0.3, σ_pos = 0.05 becomes 1.70 / 2.04 / 2.23 / 2.15 (not 2.41 / 2.56 at 300 / 1000 eV); the 100-V ceiling becomes 0.40 / 0.53 / 0.82 / 1.33; the
     CDMS-calibrated extrapolation becomes 2.02 / 2.73 / 3.27 / 3.30. **The 100-eV entries and C7j are unaffected.** Every entry off 100 eV in §4.2, §4.4 and §5 is wrong at the 5–25% level.
  3. σ_Nph (≈ 0.9%) is in the §4.1 definition but not in the code. Including it moves ζ_O,min to 0.16 / 0.29 / 0.54. That is small, but the text and the code disagree.
- **F7. Missing population in O (a).** At V_b > 0 (route d), each ER pair also delivers E_g at the electrodes, as Al relaxation phonons or direct QP injection
  (1109.4343 p.3). With Leman's 13% this is not negligible. At g = 𝔶^{−1/2} (9.6 V, 100 eV) the gap share is 0.088 (ER) against 0.034 (NR) of E_tot, a difference of 0.054, with
  its own contrast ζ_gap ≠ ζ_O. ΔO = ζ_O·Δφ_L is therefore incomplete. The term needs ΔO = ζ_OΔφ_L + ζ_gapΔφ_gap, and the sign of ζ_gap is unknown, so it can add or cancel.
  The HV ceiling is unaffected (both terms scale with N_eh). ζ_O,min at low bias is uncertain by O(ζ_gap·0.054/0.44 ≈ 0.1ζ_gap) relative.
- **(e) Provenance.** The Si ω_op proxy is the source's "Debye energy" (62 meV); it is close to the Si Γ optical energy, but it is a different quantity, so tag it [E] and say so.
  f_s(Ge) is 0.012 in the text and 0.0125 in the code. The Al/Ir moduli are [UNVERIFIED], as declared. The CDMS "3.1σ" is [E], as declared; note that "1:10³ (limited by the statistics)" is a
  **lower** bound on separation, so the calibration is not conservative in a known direction once the near-surface-field caveat is added. All 100-eV yields sit below
  WP5's E_R,th = 352 eV, where WP5 §3.3 says 𝔶 is **not derived**. Every (c)/(d) number at 50–300 eV is therefore [E] on an underived input. This belongs in §0 rows 6–7, not only in the caveats.
- The **ζ_O/σ_pos ≈ 9 transfer** (§5) moves a ratio from a 2.5-cm Ge iZIP with 6.1% coverage and a near-surface-field NTL population to a 1-mm Si CPD at uniform
  low field. The return's own caveat says the CPD lacks the contrast source. The extrapolated "𝔖(100 eV) ≈ 2.7" should be removed from §0 row 7 or marked as having no physical support.

## Rubric (d): consistency with WP0-v3, CONVENTIONS, NOTATION
- **N1 (renames owed, NOTATION rows 631–652).** NOTATION has renamed WP7-E's g → **g_Luke** (collision with the e–ph vertex g_{mnν}), r → **r_coll**, δ → **δ_coll**, and
  y → **y_ion**. The return uses g, r and δ throughout and lists them as "used unchanged … NOTATION/WP7-E-v3". That is wrong. Rename them: g_Luke, r_coll, δ_coll, and δ_prim → δ_coll^{prim}.
- **N2.** 𝔖 is already NOTATION's Ward-identity generator (row 338: "𝔖, s^W(Q)"). The return declares it **new**, which is a collision. Rename it (e.g. 𝔖_sep → S_sep).
- **N3.** 𝔶 duplicates **y_ion** (NOTATION 633, "ionization yield"). Either use y_ion with the L20-truncation qualifier, or justify a separate symbol in NOTATION §13.
- **N4.** The bare "O" observable clashes with STATEMENT's operator set O in S_{OO′} and with 𝒪_i. Use O_obs or 𝒪^{obs}.
- **N5.** "WP5-v4 does not exist yet". returns/R13/WP5-v4.md now exists and records dℋ/dω_ph as a mark (l.145), which bears on IF-R1/G-R3. Re-point IF-R1 there.
- **N6 (WP0-v3).** The return never writes O as a functional of the cascade map P_casc(𝐍|Λ) of WP0-v3 (7.3). The chain "response → measured signal" (STATEMENT H3) is
  therefore not closed for the new observable. Add one line: O = E[a·φ(𝐍, sensor marks)] under (7.3).
- CONVENTIONS §12 tags are used correctly apart from the [D] on §2.3 (above) and the [D] on L41.

## F8. IF-E7 (V8)
- §6 and row 8 say "δ cannot carry the 0.048 Si deficit". The bound covers only the spectral part δ_prim ≤ 0.007, and §6 itself says any larger δ comes from non-spectral
  differences (ΔE_esc, position, losses). *Correct to:* "δ_prim cannot; non-spectral δ_coll is not bounded here". IF-R3 already says this, and §0 and §6 must match it.
- The return finds the **sign** of r_coll − 1 open, and the sign of δ_prim depends on ϵ_soft/ϵ_hard − 1 (also open). WP7-E-v3's E_st bounds (⟨E_st⟩/E_R ≤ 0.055 / 0.064,
  p_surv ≲ 0.47 / 0.66) and LIMITS L36 are stated **only under (B-a) Δϵ ≥ 0 and (B-b) r ≥ 1** (WP7-E-v3 §0 row 10, l.214, L36). The return gives no support
  for (B-b) and no sign for (B-a). That is material for the campaign and missing from IF-R3. Add it: "WP8-R does not support (B-b). If r_coll < 1 the WP7-E-v3 bounds are void until G-R1 closes."
- "|r − 1| ≲ 0.2 [E]" has no derivation or source. Drop it or give the estimate.

## F9. GO/NO-GO mapping (V9)
The GO rule is "≳ 2σ at sub-keV where yield/timing fails".
- (a) passes 2σ at 0.38–1 keV only for ζ_O = 1 and σ_pos = 0 (F6.1), so it is NO-GO on physical ζ_O and σ_pos.
- (d) does reach ≥ 2σ at 100 eV under assumed inputs. The return excludes it as "not an interface effect", but its own §3.3/§5 make the frequency-cut (Nb-like) film the
  source of ζ_O, which is a frequency-selective interface element. The defensible exclusion is different: (d) is the **ionization-yield discriminant read
  out with phonons**. Its intrinsic limit is the same pair-number ceiling 𝔖_int as the yield's, and its 𝔶 is underived below 352 eV. It is therefore not a
  discriminant "where yield fails". It removes only the charge-amplifier noise. State the verdict as **NO-GO for primary mode/frequency/angle selection; (d) is
  a phonon-readout variant of yield discrimination, CONDITIONAL on ζ_O, σ_pos, ζ_gap (F7) and 𝔶(< 352 eV)**. With that reason the overall NO-GO stands.

## F10. Proposed LIMITS rows
| Row | Verdict | Correction |
|---|---|---|
| L39 | ✎ | Sources CONFIRMED. Status "DERIVED (scaling)" → **ESTIMATED** (scaling argument + toy, F-§2.3). Validity: add "bulk events farther than ℓ_mem from a sensor face" (F1) and "self-similar decay kernel". The chain should recover Leman p.13 and 1805.02495 p.6 ("details … rapidly lost", "wiped out") as its literature formula, and say so |
| L40 | ✎ | Its primary source is "Kaplan 1979 [UNVERIFIED, not accessed]", which fails (b). The AMM/DMM formulas used need an [FT] source (AMM: Little 1959 / Kaplan 1979; DMM: Swartz & Pohl, RMP 61, 605 (1989)) or must be derived in-return. The measured 0.3–0.55 is for 380 µm Si / 60 nm Al. Add the normal-incidence restriction (F5) |
| L41 | ✎ (falls as written) | "η_pb flat above 4Δ → no frequency selectivity" is REFUTED for thin films (1401.1937 Fig. 4, F4). Status DERIVED (limits) holds only for the [2Δ, 4Δ) branch. Validity: "Ω ≫ 4Δ and thick film (τ_l/τ_0φ → ∞)"; leading correction: the τ_l/τ_0φ-dependent decrease of η_pb with Ω |
| L42 | ✔ with correction | The algebra (ΔF, g_opt = 𝔶^{−1/2}, 𝔖_int) re-derived by sympy is correct. Add the gap/relaxation population (F7) as a leading correction; fix the frozen-𝔶 numbers (F6.2); and note that 𝔶 < 352 eV is not derived. "1109.4343 (precedent)" is not a source of the formula. Cite it as calibration only |

## Required corrections (summary)
1. §2.3/L39: [D] → [E]. Scope the memory-loss statement to bulk events beyond ℓ_mem of an instrumented face; use the 1-mm CPD thickness where σ_ph is taken from it (F1).
2. Row 5/§4.3/IF-R2: ζ_O(gap) is open and release-location-dependent, not 0 (F2; 1109.1193 p.17).
3. §3.3/row 3/L41: η_pb is not flat above 4Δ in thin films (F4). L/T contrast is at normal incidence only (F5). L40 needs an [FT] source.
4. Unify the 𝔖 noise convention (F6.1); restate (a)'s NO-GO as conditional on σ_pos ≳ 1% plus ζ_O ≪ 1 (band overlap); E_2σ = 0.38 / 1.33 keV.
5. Fix the frozen 𝔶 in `fom`/`fom_prim` and include σ_Nph. Re-issue every off-100-eV entry in §4.2, §4.4 and §5 and the 1-keV ceiling range (F6.2–3).
6. Add the gap/relaxation population to O at V_b > 0 (F7). Remove or mark the CDMS-calibrated "𝔖 ≈ 2.7" as having no physical support.
7. §6/row 8: "δ_prim cannot"; flag that WP7-E-v3 (B-a), (B-b) and L36 lack support from WP8-R (F8).
8. Renames: g_Luke, r_coll, δ_coll, y_ion (or justify 𝔶); 𝔖 collision; O → O_obs; re-point IF-R1 to WP5-v4; link O to WP0-v3 (7.3) (N1–N6).
9. Overall verdict: keep NO-GO, with the reason given in F9.
