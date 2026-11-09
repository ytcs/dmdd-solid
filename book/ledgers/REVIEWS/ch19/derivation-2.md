# Ch19 part 2: derivation check (isolated). Files: ch19.tex, s19-4, s19-5, s19-6, s19-summary, appD/D-45

Reviewer: derivation verifier, 2026-11-06. Method: every non-definitional step was redone in my own scripts, not the figscripts:
sympy for all of D.45/19.5 algebra; an independent product-integration solver plus a Monte Carlo for eq:19.4-count;
my own finite-difference solution for the defecton backward equation; my own discrete Frenkel–Kontorova relaxation and Mathieu
band; and direct recomputation of every printed number. The figscripts/ch19 logs (def19_4, bal19_5, rel19_6, limit19_6a/b) were then
compared with these results, and all agree to the printed digits. Sources were read in full text (lit.py, sources/review-ch19/, PDFs deleted):
1803.02903, 1805.09942, 2303.02196, 2007.14289, 2208.02790, cond-mat/0310283, 2202.05097, 1806.11002, 2206.06772, 2301.06592,
and Nordlund 2018 (Nat. Commun., OA). Not readable here: Holmström 2008 (Table III) and Braun–Kivshar (book).
Verdicts: CHECKED / WRONG / GAP. A count follows the main findings.

## 0. Main findings (new, not in editor notes)

1. **WRONG — s19-5 l.108 ("does not depend on the value adopted for ε_eh") and the WE 19.5 / two-bias numbers.** CDMS II sets the phonon scale
   with ER so that E_φ − E_Q·eV/ε_adopted = E_Q (1803.02903 Sect. 2.1.2). It uses ε_adopted = 3.82 eV (footnote 2). The adopted ε therefore enters
   *both* the scale and the subtraction as g_a = eV/ε_adopted. Only the Luke phonons carry g_t = eV/ε_true. The exact identity is
   Y_ph = (1+g_a)[(1−δ)(1−d_NR) + 𝔯 g_t f_ion]/(1 − d_ER + 𝔯 g_t) − f_ion g_a. At 𝔯 = 1 with no deficits, Y_ph − 1 = (g_a − g_t)(1 − f_ion)/(1 + g_t).
   The book's ε_true = 3.75 eV (the DC-67 value of 3.7468 agrees) gives **−0.0062**, against the datum's band half-width of 0.008. The consequences, from sympy and brentq:
   stored-only reading e = 0.042 (not 0.048); the 95 % edge 0.049 (not 0.055); collection-only 𝔯_coll = 1.134 (not 1.154); and
   "stored energy alone gives 0.952 at both biases" fails, giving 0.9475 at 40 V if the reconstruction keeps 3.82 eV.
   Fix: (i) delete the clause, (ii) write the identity with g_a and g_t (D.45), (iii) either state as a fifth condition that the reconstruction uses
   the true ε_eh, or carry the term. The bound 0.055 stays valid, and conservative, whenever ε_true ≤ 3.82 eV. It loosens if ε_true > ε_adopted.
   The same applies to tab:19-bounds, lim:19.4b, lim:19.5b, the summary ("0.048 … 1.154 … 0.033") and the nuisance row "Collection ratio".
2. **WRONG (attribution) — s19-5 WE l.185, "75 % of the high-field value … f_ion = 0.75×0.507".** The source's 75 % is relative to the
   Chavarria parameterization y_C = [1/(aE) + 1/y_L]⁻¹, a = 0.247 keV⁻¹ (1803.02903 Eq. (4), Fig. 12), not relative to Lindhard. The same source
   says that Lindhard *over-estimates* the yield at ≲ 20 keV and that the CDMS data follow y_C there (Sect. 4).
   With y_C: f_ion = 0.324 (20 keV), 0.269 (10 keV), 0.497 (100 keV), and 0.75×0.497 = 0.373. Then 𝔯_coll(collection only) = 1.148 (band 1.119–1.171), and
   Y_ph = 0.948 / 0.964 / 0.955. The conclusion ("does not separate the readings") is unchanged. Fix the attribution, and add y_C as the source-preferred
   f_ion (it also sets the 10 keV damage fraction to 0.731, so the bound in tab:19-bounds becomes 0.188 instead of 0.197).
3. **WRONG — s19-5 l.29: "the 31 meV of zero-point energy per silicon atom of sec:19.1-md".** s19-1 l.103 defines 31 meV = 3⟨ω⟩/4 as *half* the
   zero-point energy (its potential part). The ZPE per atom is 3⟨ω⟩/2 = 61 meV (123 meV per two-atom cell). Fix: "61 meV of zero-point energy
   per atom". The "about a tenth of an eV" estimate fits 61 meV better (4 neighbors × 0.061 × 0.3 ≈ 0.07 eV).
4. **WRONG (overstatement) — s19-6 l.166: "Electron recoils cannot displace atoms at all".** s19-4 l.99 itself puts the onset at
   E_e = 0.14 MeV for 12.5 eV (my recomputation: 0.1406 MeV), and Compton electrons from gammas exceed it. Fix: "Electron recoils below
   0.14 MeV cannot displace atoms; a 10 eV electron gives …".
5. **GAP — the bounds 0.055/0.064 and ΔE_zp.** x_NR contains ΔE_zp, whose sign is not stated ("changes … by about a tenth of an eV").
   A negative ΔE_zp (softened modes) breaks condition (c) and widens the bound by |ΔE_zp|/ω. SOTA IF-E8 (refereed) quotes 0.056 Si / 0.065 Ge
   with ΔZPE in D′. Fix: state the sign assumption in (c), or quote "≤ 0.056/0.065 for either sign of ΔE_zp".
6. **GAP — s19-6 l.166 "store at most 5.5 % … 6.4 % at 95 % confidence".** This drops "under conditions (a)–(d)", and 19.5 says that (b) is not supported.
   Add "if 𝔯_coll ≥ 1" (or "under the conditions of sec:19.4").
7. **GAP — Ge damage fraction T_d/E_R ≈ 0.7 (s19-4 l.113, tab:19-bounds, Ge E_d paragraph).** The yield 0.3 is the *observed* yield of surface
   events (1805.09942 Sect. II), and surface events suffer incomplete charge collection (1803.02903 Sect. 2.1). So 0.3 is a lower edge of the
   electronic share, and T_d/E_R ≤ 0.7. The bound 0.23 on p_surv E_FP/E_d is therefore not conservative: T_d/E_R = 0.8, the returns' value, gives
   0.20 (SOTA). The primary is also ²⁰⁶Pb in Ge (unequal masses), outside the self-recoil NRT form. State both.

## 1. Editor-note priorities: independent verdicts

| item | verdict | evidence |
|---|---|---|
| Displacement count ξ_d = 0.70 vs NRT 0.8 | CHECKED | My solver for T^{−4/3} (E_d = 1, h = 0.01) gives N(10) = 3.599, N(100) = 35.109, slope 0.701. Hard spheres T/2E_d hold to 1e−12. My own MC (cutoff 0.005 E_d, continuous loss below it) gives 3.589 ± 0.014 and 35.07 ± 0.10. The TF numbers come from def19_4.log (slopes 0.6988–0.7015, i.e. ≤ 1.5e−3 from 0.70). "11–14 %" = 1.110–1.144 ✓; "0.72 at 10 E_d" = 0.721 ✓ |
| Counting equation, three cases, hard-sphere reduction, c = 1/2E_d | CHECKED | Redone by hand: n = 0 below 2E_d; (2/E)∫_{E_d}^E N dT; continuity at 2E_d |
| T/E = x_L²/ε_L², dσ ∝ T^{−4/3}, ε_L(36 eV) = 8.8e−4, ~80 eV | CHECKED | c_L = 11.5/14^{7/3} = 0.02434 keV⁻¹; 2e−3/c_L = 82 eV |
| MC agreement | CHECKED | see above |
| Bounds 0.055/0.064, four conditions | CHECKED (algebra, numbers) / GAP | eq:19.4-bound follows exactly from eq:19.4-fDF (sympy 0). 1 − 0.945; 0.0608 + 1.645×0.0018 = 0.0638; 2σ 0.0644 ✓. Add §0.1 (ε), §0.5 (ΔE_zp) and §1 below on condition forms |
| Condition wording 19.4 vs 19.5 | GAP | 19.4 has (c) x_NR ≥ C_cal x_ER (first order, general-𝔯 C_cal) and (d) Y_ph ≥ f_ion. 19.5 has exact (c) and (d) e ≤ 1 − f_ion. The 19.5 gloss "at least C_cal times" is true only at 𝔯 = 1: the coefficient is (1+g_L f_ion)/(1+g_L). Keep one list (19.5) as the editor ruled, point from 19.4, and fix the gloss |
| p_surv bounds vs returns | CHECKED | 0.197/0.279/0.228 (0.217 central). Close pairs: full survival 0.0527–0.0582, p_surv ≤ 0.945–1.043. Separated: 0.0628–0.0752, p_surv ≤ 0.731–0.876. 100 keV: 1.34–1.48 / 1.04–1.24. Returns' 0.21/0.20 and p_surv ≲ 0.47 (CORRECTIONS §19.5) used ξ = 0.8 with T_d/E_R = 0.65 / 0.8 and E_d = 20 eV; the book's values are a change of inputs, not a superseded number. The text never quotes 0.47 ✓. Update SOTA as the editor notes say |
| Ge E_d = 19.7 model-conditionality | CHECKED | 4.28 eV, 4.61 eV per eV, 27.6 eV; counting rules give 34.5/27.6/24.2 ✓. Source: TRIM run with E_d from 15 to 23 eV, energy lost over 80–110 keV, "simple potentials … tuned", "systematic error does not include modeling imperfections", polarity remark (Sect. V B, C) ✓; the stored energy per displacement is indeed not stated ✓. 2.06σ ✓ |
| Balance law eq:19.5-balance, D.45 proof | CHECKED | The reservoir list matches CORRECTIONS l.353 D′ (pairs, excitons, trapped, E_es, ΔZPE, esc). ∂E_pairs/∂μ = N_h − N_e ✓. Ramo: induced −qz/L, work eV·s, ΣN_ind ✓. Luke heat W − ΔE_es ✓ |
| Configurational E_st, ΔZPE in E_phon | CHECKED | Consistent across 19.5 law, 19.6 sum rule and eq:19.6-hop argument. See §0.3 for the 31 meV label |
| W_bias = eV N_ind | CHECKED | Fully collected pair → eV whatever the creation point ✓ |
| Heat ratio 1.407 | CHECKED | 0.96818/0.688 = 1.4072. First order 1.2802 ✓. Matches SOTA (refereed Y_H 1.407; "first-order 0.28 invalid") |
| 3.5 % release | CHECKED | 0.01/[0.312(1.01 − Y_q)] = 0.0353, 0.0363, 0.0414 ✓. b = 0.5245 → 1.1564; b = 0.941 → 1.0168 ✓. "Four to ten times": 1/0.236 = 4.2 to 1/0.102 = 9.8 ✓ |
| Calibration identity eq:19.5-calib, eq:D.45-linear | CHECKED (single-ε model) | sympy 0. But see §0.1: with ε_adopted ≠ ε_true the identity gains g_a ≠ g_t |
| First order eq:19.5-first, C_cal | CHECKED | sympy series 0. C_cal 0.6626 (4 V), 0.4024 (40 V). Max error at the corner (𝔯 = 0.8, δ = d_NR = 0.05, d_ER = 0) = 2.79e−3 ✓ |
| Exact bound eq:19.5-bound | CHECKED | sympy 0. D.45 intermediate lines re-expanded ✓. "(c) holds for every x_NR ≥ 0 when x_ER ≤ 0" ✓ (needs δ ≤ 1) |
| Widening eq:19.5-widen | CHECKED | sympy 0. 0.0156 (0.95), 0.0313 (0.9); lim:19.4b 0.0859 at Y = 0.945 ✓. Equal to eq:19.4-bound at δ = x = 0 ✓ |
| Two-bias inversion | CHECKED (single-ε) | Determinant and Cramer: sympy 0; equal-Y gives 𝔯′ = 1, Y(0) = Y ✓. 40 V: 0.91953 (collection), 0.93469 (𝔯 = 1.0768, e = 0.024) ✓. "0.033 ≈ 4× half-width" = 0.0325/0.008 ✓. ±0.005 at 40 V moves 𝔯′ by ±0.020 ✓. Limit f + (Y0 − f)/𝔯′ = 0.9130 ✓ |
| 𝔯_coll 1.154 vs 1.144; f_ion range | CHECKED / see §0.1–0.2 | 1.15355 (band 1.1229–1.1780). f = 0.3 with g = 4/3.82 gives 1.1439 ✓. Lindhard f_ion 0.3022/0.3463/0.5071 (k_L = 0.14578) ✓. Y_ph 0.9488/0.9638/0.9545 ✓ |
| δ_gap eq:19.5-dgap | CHECKED | Derived from the ε_hard[1 + (ρ_g − 1)x E_g/ε] model (sympy 0); 0.0480 at ρ_g − 1 = 0.254; 0.0035 per 0.02 ✓ |
| 19.6a closed form D = (6T²/⟨q²⟩)[1 − I₀(A/T)⁻²] | CHECKED | Re-derived (flux form, periodicity C = −1/[y a²D₁I₀], parts). My FD solve matches to 1e−5 at y = 0.1, 1, 3, 10. Expansion 1 − I₀⁻² = (y²/2)(1 − 5y²/16) ✓ → 5/576 ✓. Limits 3A²/⟨q²⟩ = Δ²/12⟨q²⟩ and 6T²/⟨q²⟩ (Einstein with D_p = D₁) ✓ |
| T ≥ 0.28 band widths; 0.93; exponent −7.9 | CHECKED | 0.28222, 0.92787, −7.908 |
| Low-T coefficient 2× Pushkarov | CHECKED | Model 6/(4α) = 1.179 against Eq. (64) 0.59 = (3/2)²/(3α), the result of putting ε = 3T/2 into Eq. (61), with τ from (59) "of the order" ✓. ε(p) = Δ/4 ↔ D₉ ✓ (θ_p = c̄/2a) |
| 19.6b FK correction −a²/72d² | CHECKED | 4 sin²(ka/2) expansion → −(Ka³/24)∫u″²; ∫u″² = 2a²/(3π²d³); ratio to E_kink = 2Ka³/(π²d) gives a²/72d² ✓. My discrete relaxation: E ratio 0.98332 (d = a), 0.99361 (1.5a; the law within 2.2e−4, not "2e−4" exactly at 1.5a, trivial); mass 1.0303; barrier 0.7763 (d = a), 0.9249 (2a), 0.8996 at 1.74a ✓ |
| Summary and nuisance table vs sections | CHECKED except as listed | Every number matches its section (I checked each row). Carry §0.1/0.4/0.6 into them. Row "Stored share" should name the ΔE_zp sign (§0.5) |

## 2. s19-4 line by line

- l.23 6.08 %, 4.8 %, ~7 eV: CHECKED (1805.09942 abstract; 1803.02903 abstract 4.8 +0.7/−0.9 %).
- l.34 Frenkel pair 6.8–7.5, separated pair 8.1–9.7, bond defect 2.6–3.0 [Holmström Tab. III]: NOT VERIFIED (paywalled); consistent with 7.4. "More than half": 6.8/12.5 = 0.54 ✓.
- l.36 Dinmohammadi Eq. (8), 17.5–77.5 eV, ionization threshold = E_d: CHECKED (2301.06592 l.216–225, l.53).
- l.40 Sassi: 20 ps without a quench (potential-energy difference), minimum thresholds 18 eV Si / 13 eV Ge (Table II): CHECKED. The range "up to 200 eV [Fig. 1]" is the stated maximum for some materials, while the Fig. 1 axis runs to 500 eV. Check which range applies to Si.
- l.61 NRT ×0.8 "for realistic potentials" [Nordlund Eq. (1)]: CHECKED. lim:19.4a piecewise 1 on [E_d, 2E_d/0.8): CHECKED.
- l.74 "a third to a quarter" in metals: CHECKED (Nordlund: "factor of 3 to 4"). Si/Ge recombine much less [Sassi II B]: CHECKED.
- eq:19.4-loss and its dimensions: CHECKED. Damage fraction 0.698/0.493 ✓.
- WE 19.4: m_χ ≥ 0.7695 GeV ✓. Y_q is a log–log interpolation, 0.1190 (log-linear gives 0.120); "logarithmically" is ambiguous, so say "log–log". T_d 264.3 ✓. 7.342 ✓.
  Counts 3.671/2.937/2.686 ✓ (my power-law solver gives 2.682 at 7.34). Stored energy 18.3–20.1 eV (6.1–6.7 %), 21.8–26.1 eV (7.3–8.7 %); at E_d = 24: 3.953 and 10.3–11.9 eV ✓.
  Source table values 0.108 (0.22 keV) and 0.136 (0.46 keV) ✓ (2303.02196 Table II).
- l.99 T_max = 2E(E + 2m_e)/M → 0.1406 MeV ✓. The "Three kinds of terms" text and the C_cal range 0.640–0.746 ✓.
- l.107 4 V/cm, 4 V bias, ²⁵²Cf, resonance near 20 keV, 0.952 +0.009/−0.007 at 95 %, IR flashing: CHECKED. "g_L = 1.067 with the pair energy 3.75 eV": GAP, because the source reconstructs with 3.82 eV (§0.1).
- l.109–113 Ge: ±2 V, ~50 mK, Eq. (4) values 6.223/5.870 recomputed from f and f_sur ✓; weighted mean 6.074 ± 0.084 ✓; 2.06σ ✓; ×2.06 → 0.17, ⊕ syst → 0.18 ✓. Yield ~0.3 ✓ (but see §0.7).
- lim:19.4b: 0.086 ✓; 1.154 ✓ (single-ε, §0.1).
- l.157–159 numbers ✓ (§1). 6.9 % = 0.4 × 0.881 × 0.197 = 0.0694 ✓.
- l.163–165 Ge four choices ✓ (§1).

## 3. s19-5 and D.45 line by line

- l.3 34 pairs (33.87), 40 eV (39.6) ✓. Using Y_q at 0.89 keV for "1 keV" is fine; the figure caption says 0.89.
- l.25 "recombination phonons" named in 1803.02903 Sect. 2 ✓.
- l.29 31 meV: WRONG (§0.3).
- l.40 g_L 1.07 (4 V), 26.7 (100 V) ✓.
- fig:19-shares: 943/2.0/55/0.34 eV, phonons 905 eV ✓. Source fall time: 2007.14289 gives τ_f = 58 µs directly, with 2.7 kHz as the corresponding frequency. The book's 59 µs = 1/(2π·2.7 kHz) is off by 1 µs; quote 58 µs (no effect on the shares after 1 ms). 10.6 g ✓; unit heat quenching assumed [p. 4] ✓.
- eq:19.5-heatq, eq:19.5-release: CHECKED (d_NR = Y_q(E_g/ε)(1 − b) + (E_st + ΔE_zp)/ω).
- eq:19.5-bimol: CHECKED (sympy dsolve: 1/(1 + t), (1 + t)^{−1/2}). The late-time forms ✓.
- eq:19.5-signal, eq:19.5-identity: CHECKED within a single ε (§0.1).
- l.133 "C_cal < 1" argument ✓; values ✓.
- lim:19.5b: 0.031 ✓. "First-order form coincides" ✓ (the exact form is linear in d_NR at δ = d_ER = 0).
- l.152 condition (c) gloss: GAP (§1, "C_cal at 𝔯 = 1").
- l.154 2Δ_Al = 0.36 meV: the value comes from 1.5, not checked here. The transport sign is consistent with CORRECTIONS l.442 (WP8-R-v2 toy 𝔯 = 0.87–0.98 [E]). Per the editor note, 20.5 still owes the number.
- WE 19.5: all numbers ✓ under a single ε (§0.1). The 75 % attribution is WRONG (§0.2). "Collected in full" at 20 keV ✓ (source: consistent with 100 % below 20 keV).
- l.193 two-bias numbers ✓ (§1).
- l.195–197 hypotheses: add "the reconstruction ε equals ε_true, or both biases use the same adopted ε and the identity carries g_a" (§0.1).
- D.45 subsections: every displayed line was re-derived in sympy (identity, linear form, derivatives ∂Y/∂A and ∂Y/∂B, A − 1 expansion, bound expansion, widening, Δ₂, Cramer): CHECKED.

## 4. s19-6 line by line

- l.3 / l.29 / open problems: λ = 27.49, quartic ×4/3 = 36.66 (my derivation: ∫(1 − 4x²/d²) = 2d/3 against d/2), ln(Γ₀·1 yr) = 47.20 → 23.60, 14.2 %; Al λ = 25.15, 6.2 % ✓. SOTA states the Phillips/Jäckle λ and that "frozen" was withdrawn; the book says "conditional" ✓.
- eq:19.6-hop: (Δ₀²/4)·2πA = (π/2)ω_w²e^{−2λ}A ✓. The reduction to eq:16.8-golden was not checked (outside these files).
- Energy-gap law: 1/Γ(p + 1) at p = 16.67 → 2.68e−15, +16.8 in λ, λ ≤ 6.82; 7 eV → 443 ✓.
- eq:19.6-sumrule proof: CHECKED (label exchange). The five conditions are consistent with SOTA T-1 (i)–(v), including Σp_i = 1.
- WE sum rule: rates 2.863e−7 / 1.425e−8 / 1.929e−9 ✓, 38.5 d ✓, 0.9526 ✓. 1 yr: p_C = 7.6e−5 (printed "10⁻⁴"; its 5.3e−4 eV is dropped from E_st(t) = 2.526, which is below the printed digits), p_B = 0.9020, hops 0.9525/0.0474/0.0505, 4.4738 eV, 1.0504 hops, 4.259 eV/hop ✓. 10 yr 5.539 eV/1.431 hops; 100 yr 6.994 eV/1.950 hops ✓. f_ph·ε: 1.05/1.75/0.70 ✓.
- eq:19.6-tls, mean quantum π²T/(12 ln 2) = 1.1866 T → 0.491 meV ✓. 46 pW is from we:16-heat, not checked.
- fig:19-release: 0.389 within 1 yr ✓; 6.5 h – 3.6e5 yr ✓; 1.70–1.88 eV ✓; a TLS quantum is 7e−5 of that ("a ten-thousandth") ✓; 120 atoms → 3 eV ✓.
- Defectons: band, Δ = zA, m = 1/Aa², v_max = Aa ✓ (source Eqs. (1)–(3), (7)). Eq. (17), Eq. (20) R₀ = a(V₀/Δ)^{1/n} ✓ as printed by the source. Note that the source's R₀ uses φ(R₀) = Δ, not the gradient criterion it states, which would give a(3V₀/Δ)^{1/4}. The book follows the source, so this is acceptable. ⟨q²⟩ Eq. (58), α = 1.2724, c̄ as in the source (l.~520), Eq. (49) Rayleigh, Eq. (54) ✓. θ_p ≈ Θ/8 ✓. The "linear coupling second-order cancellation" step is qualitative and was not verified.
- Crowdions: d_k = 1.5915/2.2508 a, E = 6.37/9.00 eV, M = 0.1273/0.0900 M_κ (kink mass re-derived: (M/a)∫u′² = 2Ma/π²d) ✓.
  E_PN with C.20's 16π²V(d/a)²cosech: 1.206e−4 / 3.60e−7 eV ✓. My Poisson-sum derivation confirms that 16π² is the peak-to-peak barrier and that Fitzgerald Eq. (6) (8π²) is the amplitude, a factor 2 low. This confirms the partII editor note, and the book correctly cites C.20, not Eq. (6).
  Fitzgerald Eqs. (2)–(3), V₀ ~ 1 eV, βa² = 50–100 eV, meV atomistic barrier ✓. a_ch = 2.741 Å ✓. E_rec 0.1173/0.1659 meV ✓.
  My Mathieu bands: 90.1/165.9 µeV (1.05/1.92 K); with 1 meV, 12.7/33.6 µeV (0.148/0.389 K) ✓. R₀ = 42.5/18.2 ✓. SOTA's W band 0.024 meV lies inside the 13–34 µeV range ✓.
- l.152 "below about one row spacing … barrier falls to half": the barrier ratio is 0.69 at 0.75a and 0.58 at 0.55a, and reaches one half near 0.4a. Write "well below one spacing".
- LEE: 2208.02790: 1×1×0.1 cm³, GE varnish against Al wire bonds, 3–38/38–85 eV, 6–10 d, χ² = 4192/68 (Sect. II B), >100×, O(25 %) collection ✓. Adari Sect. 2.1.2 (shape fixed, jumps after >10 K, stress/holder null, epoxy hypothesis) ✓.
  0.781 meV ✓ (but see §0.4). 12/152 eV, 22 pairs, ~1500 atoms ✓. Borel mean and Stirling form, cutoff 2/(1 − b)² ✓. eq:19.6-lee dimensions ✓. Max-entropy exponential, 4.26 eV ✓.
- l.166 "(§0.6)" GAP.

## 5. ch19.tex and summary

- ch19 l.2: 200 MeV → 21.15 eV, 12.06 km/s, 2.35 Å / 12 km/s = 19.6 fs ✓.
- Summary "lighter than about 150 MeV": 12.5 eV needs m_χ ≥ 153.5 MeV ✓. All other summary numbers match the sections. Carry §0.1, §0.4 and §0.6.

## 6. Convention drift against NOTATION

- **M_κ for Si**: ch19 (with 7.4, 11, 12) uses 26.16 GeV (natural Si), while ch1, ch8 and C.6 use 26.06 GeV (²⁸Si). ch19 is internally consistent and the effect on 0.770 GeV is +0.4 %. No change needed in ch19; a book-wide note is owed.
- g_L clash: resolved by the upright L in NOTATION l.1262 ✓. The 19.4 parenthetical repeats it, so it can be removed once the macro is visible.
- Missing NOTATION rows (grep finds 0 hits): ξ_d, E_FP, P_b, E_st,b, f_sur, E_R^rec (19.4); A_dfn, Δ_dfn, ⟨q²⟩, α_P, σ_P, θ_p, c̄, R₀, D₉, ε^hop_ij, E^conf_i, ℛ_hop, ℛ_LEE, p_LEE, U_rel, E_slope, f_ph, E_reorg, Γ₀, t_obs (19.6). a_ch, K_ch, V_s, E_PN appear once each (C.20). The Y_ph row says 19.5 but its first use is now 19.4.
- No factor-2, π or sign drift was found beyond §0.1 and the Fitzgerald Eq. (6) issue, which the book already handles.

## 7. Campaign state and parallel compute

- Superseded values: none used. The book avoids p_surv ≲ 0.47 and the first-order 0.28 (which SOTA marks invalid). 1.144 appears only as a labeled variant; the editor adopted 1.154.
  0.055/0.064 matches SOTA IF-E8, but SOTA's ΔZPE variant 0.056/0.065 is not carried (§0.5).
- DC-RESULTS / returns/R18: DC-67 (PARTLY VALIDATED; quote only REF-DC-67) gives Si ε = 3.7468 eV. It supports the book's 3.75 eV (g_L changes by 1e−3, 𝔯 by < 1e−3). It is not quoted in these files, so no restriction is breached. Its main effect is to strengthen §0.1: ε_true < 3.82 eV implies the −0.6 % term. No other DC item bears on these sections.

Count: WRONG 4 (§0.1–0.4). GAP 7 (§0.5–0.7, condition wording, Ge yield, ε hypothesis in the two-bias paragraph, Sassi range). Minor wording items 4.
Everything else listed above is CHECKED.
