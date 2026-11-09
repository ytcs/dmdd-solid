# R14 referee REF-WP8-R-B (hostile, isolated): returns/R13/WP8-R.md

Read: the return; code/WP8-R/checks.py (rerun); returns/R8/WP5-v3.md, WP0-v3.md (grep); returns/R12/WP7-E-v3.md; CONVENTIONS, NOTATION,
CONTROLS, DONE, LIMITS, STATEMENT. Full text was fetched with lit.py into literature/papers-r14-REF-WP8-R-B/ for 1109.4343, 1109.1193, 1805.02495,
2302.05998, 2408.04732 and 2012.12430; the PDFs and text copies were deleted afterwards. Not re-fetched: 2301.08699, 1401.1937, 2004.11499 and the
[ABS] items. AFLOW entries were not re-queried. Rerun: **48/48 PASS in 3.6 s** (the return says ≈ 1 s), and every printed number in §§0–4 is reproduced.

## Verdict table
| # | Claim | Verdict | Reason (details below) |
|---|---|---|---|
| 1 | NR/ER differ at birth: branch mix, plus an ER soft fraction f_s ≈ ω_op/ε_eh | STANDS WITH CORRECTION | f_s is [E] with no created-phonon spectrum (IF-R1, which the return admits). The census leaves out the **born-soft gap/relaxation population** that the return's own [FT] sources describe (§B1) |
| 2 | Memory lost within ~10–100 ns and ≲ 0.1 mm (the central claim) | STANDS WITH CORRECTION | (i) It is [E], not "derived" (§A1). (ii) It holds only for Si/Ge: in Al₂O₃, which is used as a substrate in §3, the mixing condition fails (§A2). (iii) It is a bulk statement: events within ℓ_mem of an instrumented face keep their memory (1109.4343 p.2). (iv) It covers prompt populations only, not the late gap-energy release (§B1) |
| 3 | No frequency/mode selectivity at interfaces or sensors in the arriving band | STANDS WITH CORRECTION | The AMM/DMM numbers are reproduced. "η_pb flat above 4Δ_BCS" is **not** in WP5 (W13) (§A3). The return also misses the precedent's actual frequency selector, mean free path × sensor coverage (§B2) |
| 4 | (a) Primary-route NO-GO; 2σ first at 0.52 keV (ζ_O = 1, σ_pos = 0) | STANDS WITH CORRECTION | The noise convention contradicts §4.1 (an extra √2). On §4.1's own definition, E_2σ = **0.37 keV**, which is sub-keV. The NO-GO survives only through σ_pos ≥ 0.7%·ζ_O. Scope: Si/Ge |
| 5 | (b) Gap channel: ζ_O = 0 under mode selection, "outside this screen" | **FALLS** | "Born hard" is untagged and unsourced, and the cited [FT] text contradicts it for release at surfaces and electrodes. A fast/slow O, which is inside the return's own §3.4 class, could read it. With ζ_O ≠ 0, Δf_g = 0.26 gives 𝔖(100 eV) ≈ 7ζ_O. The correct status is UNRESOLVED, not NO-GO (§B1) |
| 6 | (c) HV (100 V) NO-GO for E_R ≤ 300 eV | STANDS | The algebra and the numbers are reproduced (0.53/0.91 at F_NR = 1; 1.00/1.72 at F_NR = 0.15; 3.15 at 1 keV). Caveat: the Gaussian treatment at 4–5 pairs ignores pair quantisation at 0.03-pair resolution (2012.12430), but that is yield information either way |
| 7 | (d) CONDITIONAL; CDMS-calibrated 𝔖(100 eV) ≈ 2.7 | STANDS WITH CORRECTION | The leakage is "better than 1:10³" at an unstated NR acceptance, so ζ_O/σ_pos ≥ 9.3 is a floor (12–13 at 80–90% acceptance). The mechanism does not transfer (§B2). σ_ph = 2.65 eV is misattributed to a "Si CPD" (§C) |
| 8 | IF-E7: δ_prim ≤ 0.007, so "δ cannot carry the 0.048 deficit" | **FALLS (as stated)** | The bound covers only the prompt soft fraction. The ER-excess gap/relaxation phonons, (1 − y_ion)E_g/ε_eh = 0.20–0.24 for y_ion = 0.22–0.35 (Si), sit in ϵ_prim. A 20–24% collection difference for them alone gives 0.048 (§B3). The r statements STAND |
| 9 | Overall NO-GO for the brief's target | STANDS WITH CORRECTION | Correct as: **NO-GO for (a) and (c) in bulk Si/Ge; (b) UNRESOLVED (G-R2 is decisive); (d) not GO** (§B4) |
| L39 | Scaling-spectrum chain | STANDS WITH CORRECTION | Status should be ESTIMATED, not DERIVED; validity must exclude Al₂O₃; the source wording on surface loss needs fixing (§D) |
| L40 | AMM/DMM chain | FALLS (as a LIMITS row) | Its source is Kaplan 1979 [UNVERIFIED, not accessed], so it fails rubric (b). It should be an exact remaining gap until it is sourced (§D) |
| L41 | η_pb flat above 4Δ_BCS, "DERIVED (limits)" | FALLS (as DERIVED) | WP5 (W13) gives only ω < 4Δ_BCS and ω ≫ ω_D; nothing in between is derived (§A3) |
| L42 | NTL-route 𝔖 algebra, optimum g = y^{−1/2} | STANDS WITH CORRECTION | sympy and a hand check confirm it. Symbols need renaming (§C), and the √2 convention needs harmonising (§A4) |

## A. Derivation and number checks (rubric a, f)
**A1. "Here it is derived" (§2.3) is an overclaim.** WP8R-C3 is a toy matrix exponential on a grid with a Beta(3,3) kernel and one scalar rate
x_L𝒜_anh f⁵ for every phonon. Polarisation, and the fact that T phonons do not decay, are absent by construction. A deterministic toy run is [E], and
the return's own tag for the step is [E]. A [D] statement would be convergence to a self-similar profile for homogeneous fragmentation with rate ∝ f⁵,
which is a known theorem class in fragmentation theory. It would need citing with its hypotheses (a homogeneous scalar kernel), and the real two-species
L/T kernel does not obviously satisfy them. The statement is also not new. 1109.1193 p.6 [FT]: "This process allows us to start a Monte Carlo
with any high frequency distribution and details of the distribution will rapidly be lost". The return quotes only 1805.02495 and calls it an
assumption. **Correction:** relabel row 2 "E (toy) + D (f_*(t) scaling, N_mix, r_rms)", and credit 1109.1193 p.6. The numbers themselves are
reproduced. Si hard-part TV is 6.4×10⁻⁴ at 10 ns. Ge hard-part TV is 0.022 at 10 ns, 2.5×10⁻³ at 30 ns and 4×10⁻⁴ at 100 ns, so the Ge window "30–100 ns" is right
and "< 10⁻³" applies only from somewhere between 30 and 100 ns.

**A2. Al₂O₃ is outside the hypothesis of §2.2, but §3.2 uses it.** From 2408.04732 Table 4 [FT], B(Al₂O₃) = 0.025×10⁻⁴² s³. Table 3 [FT] gives
A = 12.7×10⁻⁵⁵ s⁴ (calc), with literature value 1.88×10⁻⁵⁵. Then f_eq = B/A = **0.02–0.13 THz**, so isotope mixing is slower than L decay over the whole primary band.
The mixing count is B f⁴ × 1 µs = 0.025, 0.4 and 16 at f = 1, 2 and 5 THz, against 652 in Si. The e^{−N_mix} argument (WP8R-C4f, which hard-codes N_mix = 100) does not
apply. Transverse phonons born in sapphire neither mix nor decay through the isotropic L-only channel. The verdict "Mode- and angle-selective transmission
carries no NR/ER information" is therefore **not established for the Al₂O₃/Al row**, which is the row with the largest L/T contrast (1.10). **Correction:** restrict
§3.2 and IF-R4 to Si/Ge substrates, and add sapphire as an exact gap (it needs a T-decay channel and the NR/ER birth polarisation, IF-R1).

**A3. η_pb flatness is not from WP5.** WP5-v3 §5 (read): "For ω < 4Δ_BCS … η_pb = 2Δ_BCS/ω" and "**For ω ≫ ω_D in a bulk absorber**,
η_pb → 0.57–0.6". The return asserts "η_pb(Ω) is flat above 4Δ_BCS(Al) = 0.17 THz" and that "every arriving … phonon (≳ 0.3 THz) sits on the flat
branch". That covers 4Δ ≲ Ω ≲ a few THz ≪ ω_D(Al), where WP5 explicitly leaves η_pb(ω, d_film, T) as a computation specification. WP8R-C5b checks only that 4Δ < 0.2 THz,
not flatness. **Consequence:** the conclusion is weakened but not reversed. A residual Ω dependence of η_pb would be a further ζ_O lever (NTL vs primary,
gap vs primary), and NR and ER primaries still share one spectrum. L41 → ESTIMATED. Δ_BCS(Al) = 0.18 meV is tagged [UNVERIFIED], but a cited [FT] source
gives a value: 1109.4343 p.3 says "2∆Al = 200 µeV". That implies 4Δ = 97 GHz, which differs from 0.18 meV and should be noted. The conclusion 4Δ < 0.2 THz holds for either value.

**A4. Noise convention (§4.1 vs WP8R-C7d).** §4.1 defines the pooled σ as (σ_ph/E_tot)² + …. fom_prim instead uses (√2σ_ph/E_R)², while fom (the NTL
route) uses σ_ph/E_tot. The primary route is therefore penalised by √2 relative to both §4.1 and the NTL route. On §4.1's definition, 𝔖_prim =
0.54 at 100 eV and 1.63 at 300 eV, and **E_2σ = 368 eV** at ζ_O = 1, σ_pos = 0 (0.52 keV is the √2 version). The NO-GO for (a) then depends on
σ_pos ≥ ζ_O(1 − 𝔶)f_s/2 ≈ 0.7%·ζ_O. That is plausible given 1109.4343 Figs. 1–2, but it is now the deciding input, and the quoted "0.52 keV" should be
corrected or the √2 justified (two-channel ratio) and applied to both routes alike.

**A5. Verified as stated.** f_*(t), 1-cm thresholds and N_mix: by hand, N = 5𝒜_iso f_*⁴t. Integrating from t = 0 overcounts by ≈ 94 of 652 (Si),
because f_* > f_D for t < 0.19 ns, which is immaterial. r_rms was checked, as were the hot-carrier phonon cutoff (5.75 meV at 30 meV), the AMM values (Si/Al Z-ratio by hand), DMM detailed balance, and Lindhard
𝔶(100 eV) = 0.153/0.126 and 𝔶_Ge(10 keV) = 0.234. ΔO = ζ_O g(1 − 𝔶)/[(1 + g)(1 + 𝔶g)] and g_opt = 𝔶^{−1/2} were checked, giving V_b = 9.6 V. The HV ceilings were checked, and so were
ζ_O,min = 0.15/0.28/0.53. The Ge DOS L fraction is 0.103 and Si's is 0.098 (isotropic Debye), against the quoted 9.8% and 9.3%, which is consistent.
**Weak checks.** C4f is tautological (exp(−100) is hard-coded). C5c's label says the Nb cut lies "between" Ge NTL (0.3/0.7 THz) and the primaries (≥ 0.7 THz),
but the 0.7 THz hole NTL sits *on* the 0.73 THz cut and on the Si arrival peak (0.7–0.9 THz). C8a evaluates only |ϵ_soft/ϵ_hard − 1| = ½.

## B. The central claim against the CDMS pulse-shape precedent (rubric f)
**B1. The hole: the precedent uses born-soft gap-energy phonons, which the return sends to "hard, memory lost".**
- 1109.1193 p.17 [FT, CONFIRMED verbatim]: "phonons created during electron-hole recombination at the surfaces contribute 13% of the total phonon signal but
  in a low frequency, ballistic regime that is used to provide a surface-event discriminator."
- 1109.4343 p.3 [FT]: relaxation phonons, "converting their Ge gap energy (0.75 eV) into Al quasiparticles … and a population of initially high energy phonons. In
  the presence of superconducting Al, such phonons experience rapid downconversion (… ∼1 µs), meaning that relaxation phonons are ballistic". They are absorbed at
  "a slow ∼755 µs".
- In the precedent, therefore, the gap energy reaches the crystal **soft and ballistic**, and it is read through frequency, via mean free path and absorption time.
  The return's §1.2 asserts instead that at zero field the gap-energy phonons "are born hard (multiphonon/Auger), so they lose memory as in §2". That assertion has
  no tag or source, and §4.3 sets ζ_O = 0 on it.
- The return's own observable class includes "a fast/slow ratio O = E_fast/E_tot" (§3.4). A soft gap population is exactly what such an O separates. The step
  "only timing … falls outside this screen" is therefore a category error: frequency-selective collection *is* a timing observable in these devices (B2).
- **Size, with the return's own formula:** ΔO = ζ_O(1 − 𝔶)E_g/ε_eh = 0.264ζ_O (Si, 100 eV), 18× the soft-fraction channel.
  - With the √2 convention and σ_pos = 0: 𝔖(100 eV) = 7.05ζ_O, i.e. 2.1 at ζ_O = 0.3.
  - With σ_pos = 0.05: 4.2 (ζ_O = 1) and 1.27 (ζ_O = 0.3).
  - This channel could clear ≳ 2σ at sub-keV with **no bias and no charge readout**, provided that at zero field and mK the gap energy is released (i) within the
    readout window and (ii) at surfaces or films as soft phonons. Both are unknown (G-R2, θ_tr, E_X kinetics, WP7-E-v3).
- **Verdict:** row 5 FALLS; (b) is UNRESOLVED, not "ζ_O = 0". This is the one place where the precedent uses phonon frequency information that the return
  declares erased. It does not touch prompt primaries.

**B2. The bulk ER/NR result of 1109.4343 does not refute §2, but the return misdescribes how it works.**
- Verified [FT]: ±2 V, 7–20 keV (NR-scaled), a single 40–70% risetime "radius", "1:10³ (limited by the statistics of the data)", and the "Much of the essential
  information …" quote.
- The mechanism is explicitly frequency-selective collection. p.2: "These different phonon populations are produced with different initial energy
  distributions"; "A phonon's timescale of surface absorption … is therefor highly dependent on mean free path" (6.1% Al coverage); and the near-surface NTL
  phonons at 300/700 GHz have "short mean free paths (∼1.8 cm and ∼600 µm) and fast absorption rates".
- So the selector is bulk mean free path × fractional coverage, not interface transmission or η_pb. §3's conclusion "none of the listed sensors is
  frequency-selective in the arriving band" is true of the interfaces and false of the detector as a collector.
- It does not reopen (a), because NR and ER primaries at one position still share one spectrum. It does mean the ζ_O of (b) and (d) is set by geometry and
  coverage, which §3 does not model. The sentence "The precedent supports §2" should become "is consistent with §2": the paper does not test for a primary
  NR/ER signature.
- Position dependence is real in the precedent. p.2: "If the event occurs near a sensor surface … the comparatively short mean free path increases … the rate
  of absorption". It is position information, which §2.4 handles correctly as σ_pos.
- **Calibration.** A leakage of 10⁻³ is 3.09σ only at 50% NR acceptance; it is 3.93σ at 80% and 4.37σ at 90%. The acceptance is shown in Fig. 3 but not stated,
  so ζ_O/σ_pos ≥ 9.3 is a floor. The caveat that the precedent's contrast came from high-field near-surface NTL is correct and decisive. In a uniform low-field device,
  NTL phonons are "emitted with low energies and correspondingly ballistic free paths" (p.2), so the transfer is [C], not [E].

**B3. IF-E7 δ.** The return says "NR and ER prompt phonons reach the sensors with one spectrum … apart from the ER soft excess", so δ_prim ≤ 0.007. But ϵ_prim in
WP7-E-v3 (E13) multiplies all non-NTL phonon energy, which includes the released E_g. The ER excess of gap/relaxation phonons is (1 − y_ion)E_g/ε_eh = 0.24–0.20
over y_ion = 0.22–0.35 (Si, the 1803.02903 range). It is born soft at the electrodes (B1), so its collection efficiency can differ from that of the quasidiffusive primaries,
with a sign that depends on geometry. A relative difference of 20–24% gives δ_coll = 0.048 on its own. The claim "δ cannot carry the 0.048 deficit" is therefore not
derived. **Correction:** "the prompt-spectral part δ_prim ≤ 0.007–0.012 (0.012 if ϵ_soft = 0); the gap-release part δ_gap is unbounded here (G-R2)". IF-R3 and
IF-R6 should be edited to match. The r analysis STANDS (r_coll ≠ 1 expected, sign open).

**B4. GO/NO-GO mapping against the rule ("≳ 2σ at sub-keV where yield/timing fails").**
- (a) and (c): NO-GO, correctly mapped (subject to A4 and A2).
- (d): not GO. It is the right call, but for the wrong stated reason. The rule does not require "an interface effect"; the reason is that (d) is yield information.
  Its ceiling is the same pair-number statistics (𝔖_int), and its inputs are unmeasured. Keep CONDITIONAL.
- (b): has **not** been shown to fail, so it cannot be folded into NO-GO.
- The overall line should read: "NO-GO for mode/frequency/angle selection of prompt populations in bulk Si/Ge; the zero-field gap-release channel is UNRESOLVED
  pending τ_gap and the release site/spectrum."

## C. Consistency with CONVENTIONS, NOTATION and WP0-v3 (rubric d)
| Item | Problem | Fix |
|---|---|---|
| g, δ, r, y | NOTATION (WP7-E clashes table) and LIMITS L36–L38 renamed these to **g_Luke, δ_coll, r_coll, y_ion**. The return lists "δ, r, g" as "used unchanged" | rename throughout (§4.4, §6, C8, L42) |
| 𝔶 | duplicates y_ion: L38 uses y_ion = 0.22–0.35 as Lindhard values, the same object. The "≠ source y" claim is unsupported | use y_ion, or justify the distinction |
| 𝔖 | clashes with NOTATION "𝔖, s^W(Q): Ward-identity generator" | e.g. 𝒮_sep |
| Ω (phonon energy in η_pb(Ω), L_pb(Ω)) | NOTATION Ω = cell volume; WP5 (W13) writes ω | use ω_{Qν} |
| f_D "new" | duplicates ω_D (Debye energy, NOTATION) | f_D ≡ ω_D/2π |
| 𝒜_anh, 𝒜_iso | NOTATION reserves bare 𝒜 for bin/step indices (halo matrix) | acceptable with ⚠, or use a_anh, b_iso |
| [DB] tag | not in CONVENTIONS §12 (FT/ABS/UNVERIFIED), although the header says "Tags follow CONVENTIONS §12" | propose [DB] to the coordinator, or tag as [FT]-equivalent with the entry ID |
| 2012.12430 | called "the Si CPD" (§4.1); it is the 1-g HVeV-type Si detector (1×1×0.4 cm; "2.65(2) eV … without a voltage bias") | relabel. L = 1 cm (WP8R-C2) is not that device's 4 mm |
WP0-v3: no conflict found with the objects used (WP5 (W4) via A-1, ħ = 1 energies, f in Hz flagged as source form). WP5 (W4) and the A-1 forms are consistent.

## D. Proposed LIMITS rows (rubric b)
- **L39.** The sources are quoted correctly from full text: 1109.1193 Table I gives A, B, v and ρ for Si and Ge, including Ge A = 6.43×10⁻⁵⁵ ✔; 2302.05998 §2.2.2 gives Eq. (3) and the
  9.3/37.6/53.1% and 9.8/36.7/53.5% mixes ✔; 2408.04732 Tables 3–4 ✔. 2408.04732's 0.741 for Si is a *calculated* literature value (A_c,l); the return correctly tags its own
  1.15 as "calc". The chain is valid as a scaling argument. Corrections:
  - status DERIVED → ESTIMATED (A1);
  - add "f_eq = 𝒜_iso/𝒜_anh ≫ f (holds for Si/Ge; fails for Al₂O₃)" (A2);
  - "f ≪ f_D" conflicts with birth at 0.95 f_D; replace it with "t ≫ (x_L𝒜_anh f_D⁵)⁻¹ ≈ 0.2 ns (Si)";
  - the leading correction "surface down-conversion ∼0.1%/bounce" should be the source's words, "a loss of ∼0.1% for each phonon-surface interaction"
    (1109.1193 p.14), which the source puts in a down-conversion paragraph but does not itself call down-conversion.
- **L40.** The source is unread (Kaplan 1979 [UNVERIFIED]). 1805.02495's "[0.3–0.55]" is a fitted effective coefficient (data vs MC with specular reflection), not
  a measured AMM transmission; the row calls it "measured". 1109.1193 p.14 [FT] adds that AMM angular dependence "can be washed out" and that its "relevance …
  can be lost". The textbook formulas are correct (T + R = 1, reciprocity), but under rubric (b) the row needs an [FT] source. Until then it belongs as G-R5.
- **L41.** FALLS as DERIVED (A3). It becomes ESTIMATED once a source for η_pb(Ω) at 4Δ ≲ Ω ≲ few THz is in hand; the leading correction is the Ω dependence of
  η_pb itself.
- **L42.** STANDS. The algebra is exact, and the validity and corrections are right. Add "noise convention as §4.1" (A4) and apply the renames in §C.

## E. Provenance (rubric e)
- **Confirmed against the full text.** Every [FT] number I checked matches its source:
  - 1109.1193: Table I (all constants used); p.6; p.14 (∼33%, ∼0.1%); p.17 (56%, 13%, L₀ ∼ 720 nm).
  - 1109.4343: 36.7×10⁻⁴², 1.61×10⁻⁵⁵ (credited there to Msall & Wolfe, not Tamura), 300/700 GHz, 755 µs, 6.1% coverage.
  - 1805.02495: 0.3–0.55, AMM favoured, 0.7–0.9 THz, 62 meV, 15 THz, η_pb = 0.57.
  - 2302.05998: the G4CMP "negligible … not implemented" quote and L → L′T, TT.
  - 2408.04732: (µ, λ) for Si and Al₂O₃, A, B.
  - 2012.12430: 2.65 eV, 20 µs rise, fall 30–160 µs, ≳ 29%.
- **Gaps.**
  - Δ_BCS(Al), with the [FT] 200 µeV value ignored (A3).
  - The "born hard" gap-phonon statement, which carries no tag (B1).
  - The ×½ in |ϵ_soft/ϵ_hard − 1| ≤ ½, which needs an [E] tag.
  - The AFLOW IDs, which I did not re-query (UNVERIFIED by this referee).
  - Al and Ir moduli, correctly [UNVERIFIED]: the derived v_L/v_T (6379/3092 and 5225/3091 m/s) agree with standard values to a few %.
- **(c) "published paper is wrong" claims:** none are made; ε_eh 3.75 vs 3.81 and the ×10 spread in Ge A are reported, not adjudicated. There is nothing to rate.

## Required corrections (summary)
1. §1.2, §4.3, row 5: withdraw ζ_O = 0 for (b); mark it UNRESOLVED; cite 1109.1193 p.17 and 1109.4343 p.3; report 𝔖_b(100 eV) ≈ 7ζ_O as conditional on G-R2.
2. §6 / IF-R3 / IF-R6: limit the δ bound to the prompt-spectral part; add δ_gap.
3. §2.3 and row 2: [E], not derived; credit 1109.1193 p.6. Add scope (bulk, Si/Ge, prompt populations).
4. §3.2, C4f, IF-R4: exclude Al₂O₃ (f_eq ≈ 0.02–0.13 THz).
5. §3.3, L41: η_pb flatness is ESTIMATED; note Δ_Al = 100 µeV in 1109.4343.
6. §4.2 / C7d: harmonise the √2 (E_2σ = 0.37 keV on §4.1's definition).
7. §5: describe the precedent's selector (mean free path × coverage); state ζ_O/σ_pos ≥ 9.3 as a floor; mark the transfer [C].
8. Overall: "NO-GO for (a), (c); (b) UNRESOLVED; (d) CONDITIONAL, not GO".
9. Renames per §C; L40 → gap until an [FT] source is found.
