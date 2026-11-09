# Ch21 part 2: derivation check (21.4–21.7, summary, D.47)

Reviewer: derivation verifier (isolated). Date 2026-11-06. Files: tex/ch21/{ch21,s21-4,s21-5,s21-6,s21-7,s21-summary}.tex, tex/appD/D-47.tex.
Method: sympy for the algebra; numbers recomputed from the cached logs and npz (figscripts/ch21, ch17/rank17_6.log, ch10/si_elf_binned.npz, ch16/zrte5_16.npz) and from independent scratch code. Nothing heavy was run, and no QE.
Sources read (lit.py → sources/review-ch21/, PDFs deleted afterwards): 2101.08275, physics/9711021, physics/0203002, 1509.01598, 1708.08929, 1910.02091, 2401.11971, 1602.08005, 2004.11499, 2507.07119, 2310.05815, 2610.16949, 1607.04560, 1910.10716.
Scratch scripts: /tmp/claude-0/-home-user-breakthrough-maths/30a63adb-c597-5cb8-b46c-4c5645c8b7d4/scratchpad/chk1.py to chk4.py.

Verdict counts: 3 WRONG, 9 GAP, the rest CHECKED. The WRONG items, most serious first:
(W1) the gap of the published tables (1.11 eV) in 21.4 contradicts the source;
(W2) the ²¹⁰Bi share ("a sixth") and the Z_d attribution in 21.7 and the summary table;
(W3) the ZrTe₅ recast range "5200 to 6400 between 20 keV and 1 MeV" (5090 at 20 keV).

## A. PRIORITY items (editor notes and partII notes)

### A1. D.47 (whole derivation): CHECKED, with two small GAPs
- eq:D.47-tfix, the implicit-function step and eq:D.47-weights: CHECKED. Σa_j = 1. ℓ' = 2 in empty bins. ℓ' ≥ 0 for N_obs ≤ N_bkg at every μ ≥ 0. The sign of the weight in an excess bin is right.
- Power-form derivative ∂ln s_j/∂ϑ_k = ⟨ln(1+δ_k)⟩_j: CHECKED (exact for a normalization, first order for a tilt). nuis21.py uses the finite step ln(rate(ϑ=1)/rate(0)) = ln(1 + δ·f_X). At 10 MeV this is 0.2283, against 0.2261 for the bin average f_X·ln 1.28. The text's "a finite step is used in practice" covers it.
- Band and envelope e^{±|β_k|}: CHECKED. The coherent and independent per-bin variance argument: CHECKED.
- Profile: min_y[Q(x−y) + y²/σ²] gives y = σ²Q'/2 and t_p = Q − σ²Q'²/4. Hence x_p − x0 = σ²Q'/4, which is eq:21.4-profile. CHECKED in sympy.
  - GAP (minor). "t_ϑ(μ) = Q(x − Σβ_kϑ_k)" holds with constant β only if the weights a_j do not depend on μ. That is true for zero counts or one bin. Otherwise β_k(x) varies with x, and the change is O(σ⁴) in the result. Add "β evaluated at x; its x-dependence enters at O(σ_β⁴)".
- One bin, zero counts: Q = 2s e^x, so t' = t*. sympy series of eq:8.8-cost: 2we^w/(k²t*) = 1 + k²t*/4 + k⁶t*³/192. There is no k⁴ term, so the "O(k⁶)" of 8.8 is right.
  - Numbers: σ = 0.3 gives 1.1039 exact and 1.1092 at second order; σ = 0.5 gives 1.2930 and 1.3335 (prints as 1.334). All CHECKED.
  - Q' = 2N^up = 2.605 for N_bkg = 1: CHECKED.
- Known sign: both directions CHECKED. They need δ̄_{k,j} of one sign in every bin and a_j ≥ 0 at every μ. The text states the second condition but not the first. Add "template of one sign in every bin".
- Removing cells, and 1/(1−f) for one bin: CHECKED.
- GAP (notation). D.47 sets μ ≡ σ̄_e. NOTATION reserves μ (with mandatory subscripts) for reduced masses, and those appear in the same chapter. Use σ̄_e directly, or a symbol that is free.

### A2. 21.4 WE band and profiled limit (9.23e-42 → 1.30e-41; band 8.8e-42 to 1.93e-41; profiled 1.53e-41)
- Arithmetic: CHECKED against we21_4.log.
  - Limits: 2.3026e-37/2.495e4 = 9.229e-42 and 2.3026e-37/1.771e4 = 1.300e-41.
  - Ratios: 1.345 (local fields), 1.047 (gap), 1.409 in all.
  - σ_β = 0.3935 and share 0.933.
  - Band: 8.77e-42 to 1.927e-41 (e^{±0.3935}).
  - Envelope factors: 1.280, 1.335, 1.081, 1.067.
  - Ratio of the random-phase limit to the nominal one: 0.710, with the lower band edge at 0.675.
  - Exact profile (eq:8.8-cost): 1.1792 → 1.534e-41. Second order: 1.1946.
  - Detector: σ = 0.4049, band factor 1.499, profiled factor 1.1905.
  - One-sided: σ = 0.3063, profiled factor 1.1081 → 1.441e-41.
  - Without attraction and tabulation spread: σ = 0.1015, band factor 1.107.
- **W1 WRONG (premise: the gap of the tables).**
  - What the text says: 21.4 (opening, the WE "random-phase level" step, the fig21_4 caption, and "stronger by 1.30 at 1 MeV and 1.50 at 10 MeV") treats the Knapen–Kozaczuk–Lin tables as carrying a 1.11 eV gap. It then applies a +0.06 eV shift as a computed correction (×1.048).
  - What the source says: 2101.08275 Sect. III B, verbatim, "a scissor correction is applied to match the experimentally measured Si and Ge bandgaps at T = 0". 21.6's own WE says the same ("a scissor to the measured gap"). The 1.11 eV is the DarkELF step-model constant (E_gap with ε = 3.6 eV; Sect. V of the source, Q = 1 + b(ω−E_g)/ε).
  - Why the nodes cannot settle it: the table's ω nodes are 0.22 eV apart (the first nonzero node is at 1.043 eV), as 21.6 itself notes.
  - Consequence: the ×1.048 step double-counts the cold gap.
  - Recomputed from nuis21 (unshifted RPA+LF tables, one-pair threshold at 1.17 eV):
    - rate 1.8546e4, nominal 1.24e-41 (×1.345 from the random-phase level, not ×1.409);
    - band 8.38e-42 to 1.84e-41;
    - profiled (t* = 2N90) 1.46e-41; one-sided 1.38e-41.
  - The gap nuisance c_gap should also be recomputed from the unshifted base. The change is small.
  - Same root as the 21.6 editor note on 10.10. Fix 10.10 and 21.4 together, together with fig21_4 and its caption.
- Dominant-nuisance switches 1.15 / 3.59 / 6.98 MeV: crossing masses CHECKED. They are bracketed by the logged c_k at 1, 2, 3, 5 and 10 MeV.
  - GAP (wording). Only 3.59 MeV changes the dominant nuisance (tabulation spread → attraction). At 1.15 MeV the gap passes the attraction, but the tabulation spread dominates (91 % at 1 MeV). At 6.98 MeV the local fields pass the tabulation spread, but the attraction still dominates (41 % at 10 MeV).
  - Correct to: "The ranking of the nuisances changes with mass: … the tabulation spread dominates up to 3.59 MeV and the attraction above."
- Band ×3.42 / 1.48 / 1.43 at 1 / 3 / 10 MeV; 91 % at 1 MeV; light mediator dominated by the spread up to 10 MeV (51 %): CHECKED.
- tab:21-dominant, row "3.6–10 MeV heavy": "attraction ×1.28" is the factor at or below 5 MeV. At 10 MeV the template gives ×1.256 (share at ω ≤ 10.5 eV 0.916). Write "×1.28 (×1.26 at 10 MeV)". GAP, minor.
- Basis of the tabulation spread. GAP (internal consistency).
  - 21.4 profiles it as a standard-normal nuisance carrying 54 % of σ_β² at 3 MeV. 21.4's own rule says a row known only between bounds is set at its weaker end.
  - 10.10 labels it "(bound) … an upper bound for the screened rate", and 21.6 cites it as the example of a template "flagged as a bound".
  - State once which it is. If it is a bound, the 21.4 band is not the construction 21.4 prescribes.

### A3. The three statistical constructions (k² coefficients 2.30 / 1.15 / 0.65)
- Calibrated threshold (21.4/8.8): ln ratio = k²t*/4 = 1.151k². CHECKED.
- Constraint-averaged probability: second order u/N90 = 1 + k²(N90−1)/2, coefficient 0.651. CHECKED by expansion: E[e^{−u e^{kθ}}] ≈ e^{−u}[1 + k²u(u−1)/2].
  - Exact: 1.103 at σ = 0.393; the formula gives 1.101.
  - GAP (minor). 21.4 attaches "1.103" to the formula. Write "1.103 (second order 1.101)".
- 21.5 Neyman construction with the nuisance at θ̂̂(obs), constraint held fixed: for zero counts p = e^{−u} and θ̂̂ = −ku, so N_nom = N90·e^{k²N90}, coefficient 2.303. CHECKED: 1.1215 at δ = 0.25, as in we21_5.log (3.2391/2.8882).
  - For several nuisances (profile along β) this is exactly e^{σ_β²N90} at zero counts, with no higher orders.
- **Recommendation (chapter-wide): the 21.5 Neyman construction with the nuisance at its conditional best fit.**
  - Reasons:
    - It is a defined coverage statement for any counts, backgrounds and number of bins.
    - It is the only one of the three that carries the 21.5 combination (B has 3 events on 2.5 and two bins). There the calibrated threshold of 8.8 has no unique calibration, and D.47's no-excess assumption fails.
    - It reduces to the classical N90 without nuisances.
    - It is already coded (we21_5.py).
  - Consequences if adopted:
    - 21.4 WE profiled factor e^{σ_β²N90}: 1.427 at σ_β = 0.393. That gives 1.86e-41, or 1.77e-41 with W1 fixed.
    - One-sided: 1.241 at σ = 0.306, giving 1.61e-41 (1.54e-41 with W1).
    - Detector: 1.459 at σ = 0.405.
    - eq:21.4-profile then holds only for a fixed threshold. For the Neyman construction at zero counts the exact result is ln ratio = σ_β²N^up = σ_β²t'/2, so the coefficient doubles.
    - D.47 "cost of profiling" needs a paragraph saying so, or its result relabelled as the fixed-threshold construction.
    - The summary and tab:21-nuisances ("1.179 … 1.103") must quote the adopted construction. Keep the other two as one comparison line.
  - If the editor keeps 8.8's calibrated threshold instead, 21.5's combination WE must say that it uses a different construction, and why.

### A4. Yellin maximum gap: CHECKED
- eq:21.5-C0 = Yellin Eq. (2) (physics/0203002). The k = 1 rewrite at g = 1 gives C0 = 1 − e^{−N}, so N90.
- Independent root-finding: g = 0.9 → 2.8358; g = 0.5 → 7.7794; g = 1/3 → 13.838; break-even with 3.890 at g = 0.7610.
- Counting limits 2.303 / 3.890 / 5.322 / 6.681. Optimum-interval count (N+1)(N+2)/2 and Sect. III attribution: CHECKED.

### A5. Combination WE (×1.109 against ×1.051): CHECKED by an independent re-implementation (chk3.py)
- 2D Neyman sum to 60 events each, likelihood-ratio statistic set to zero for μ̂ > μ, nuisance at θ̂̂(obs), fixed constraint.
- Results: no nuisance 0.92787; shared 1.02876 (θ̂̂ = −0.4625); split 0.97529 (θ̂̂ = −0.167, −0.290). Ratios 1.1087 and 1.0511.
- A alone 2.888e-42; B alone 1.311e-42 (s_up = 4.181); 0.32 and 0.71; signal at the limit 0.74 and 2.96; "halves its cost" 0.47; "too strong by 5 %" 0.948: all CHECKED.
- Two-pair bin [4.71, 8.31) eV, from 1.11 + 3.6 eV: CHECKED arithmetically.
  - It uses the step-model 1.11 eV, while 21.4 counts from 1.17 eV. Already flagged in the editor notes. Either label 1.11/3.6 as the DarkELF convention in the WE, or use Ch18. No arithmetic error.

### A6. Recast rule, bracket, 0.9ⁿ: CHECKED
- Exact for a common 𝒦 and for a minimum with public N_j^up. Bracket [min 𝒦_j, 𝒦_{j*}] ⊂ [min, max]: proof CHECKED.
- 0.9ⁿ = 0.81 and 0.729. ln(10n) = 3.401 for three bins.
- Halo example (stats21_5.log):
  - At 10 MeV: 𝒦 = 0.971, 0.917, 0.863. With density: 1.294, 1.222, 1.150. Published 3.401/9.746e41 = 3.490e-42. Recast 4.266e-42.
  - At 2 MeV: 0.854/1.105 and 1.139/1.473.
  - v_max: 840 and 794.5.
  - Essig halo (230, 600, 240, 0.4): CHECKED against 1509.01598 App. B.
  - "From the curve alone 1.150 to 1.294" is right, because j* is unknown from the curve.

### A7. Dirac recast factors
- Isotropic ε_bg²: ×1600 (3.4e-46 → 5.4e-43, 5.5e-45 → 8.8e-42). ε_bg^{1/2} in ζ, from Γ_pub = ε_bg·Γ. Both CHECKED.
- Hochberg parameters v_F = 4e-4, κ = 40, g = 2, Λ = 0.2 keV, Δ = 2.5 meV (half-gap): CHECKED (1708.08929).
- GAP (minor). The minimum is "near 9.5 keV" here and "near 9 keV" in we:16-factor. Align.
- ZrTe₅ tensor 308.4/20.75/126.1: CHECKED (1910.02091 Table 2). Harmonic mean 50.53, square 2554. On-axis squares 431, 1.59e4, 9.51e4. 25.34² = 642.
- **W3 WRONG (minor).** "5200 to 6400 between 20 keV and 1 MeV": the factor at 20.0 keV is 5090 (interpolated). The grid point 21.17 keV gives 5200, and the maximum is 6428. Write "5100 to 6400".
  - fig21_5.log contradicts itself ("20 keV – 1 MeV: 5200" and "m = 20 keV: 5091"), because `sel` starts at the first grid point at or above 20 keV.
  - Also "low by a factor of two to two and a half": 5091/2554 = 1.99 and 6428/2554 = 2.52. CHECKED.
  - 2178 at 10 keV and 817 at 7.75 keV: CHECKED.
- Compared with REF-DC-49-54-36 §4 item 5: "×(4–6)×10³ (th.), ×(2–3.4)×10³ (exp.), ±10–15 %". The book's own integral, 5.1–6.4×10³, exceeds the REF th. upper end by about 7 %, inside the stated accuracy.
  - The text quotes only its own computation, which is allowed. It should name which REF row it corresponds to ("th."), so that a reader can compare.

### A8. Boosted flux R^{-1/2}: CHECKED
- The σ̄² scaling is stated in 2401.11971 ("rate scales with cross section squared"). 0.93^{-1/2} = 1.037 and 0.05^{-1/2} = 4.47.
- Wording follows REF-DC-49-54-36 §4 items 1–3. The added clause "a factor between 1.04 and 4.5" is a derived consequence (items 2 + 3), not REF wording. The DC-RESULTS restriction says "in its wording"; the editor should accept it or drop the clause.
- No withdrawn number is used (R = 0.14, ×2.7 absent).

### A9. Library WE (L 0.1442, S 4.38e7 eV², ×0.864): CHECKED
- Node 3732.0 eV = 1.0008 q0 and ω = 9.8585 eV. ε00 and ε_mac from we21_6.log. L_LF = 0.1442 and L_RPA = 0.1585.
- 2q²/e² = 3.0377e8 eV² (e² = 4πα). S = 4.380e7 eV². ΩS = 0.2283 eV⁻¹ with Ω = 40.05 Å³ (a³/4). S^IP = 1.796e8. δ_X = −0.090.
- Linear interpolation at 10 eV: L = 0.1390, S = 4.223e7. EPM 4.888e7 gives 0.864, and 0.896 at the node.
- Screening 0.242 against 0.29. f-sum 0.916. Node spread 3.0 %. 10 % per node. 0.22 eV node spacing near 1 eV.
- Source facts (TB09, 500 eV, 8×8×8, 70 bands per spin, T = 0 scissor; Fig. 1 caption on the 70-band cutoff near 70 eV): CHECKED.
- Dimensions: S per volume has units of eV², and ΩS of eV⁻¹. CHECKED.

### A10. 21.7 guide table against guide21_7.log, rank17_6.log and Ch17
- Survivor cells equal tab:17-rank and rank17_6 (TeO₂ 2.39 [2.19, 2.60], 0.968 (0.987); LiF 18.9, 0.987 (1.000); NaF Migdal 0.315), as the text states. CHECKED.
  - guide21_7's own survivor run differs in the third decimal (0.989, 0.988, 0.320). This is not an error, because the text says it uses Ch17's values.
- Full-pool cells: CHECKED against guide21_7.log.
  - Floor: PbSe 0.0484 [0.0479, 0.0489].
  - Quanta: PbTe 1.52 [1.24, 1.87], 0.482 (1.000); PbSe 0.414; PbS 0.102.
  - NR heavy: CsI 3.73 [3.65, 3.80], 0.962 (0.976).
  - NR edge: h-BN 2.95 [2.72, 3.21], 0.656 (0.728); C 0.181, PE 0.119, cBN 0.043.
  - Polar rate: LiF 19.0 [15.5, 23.3], 0.918 (0.931); quartz 0.066.
  - Polar reach: CsI 2.85 [2.71, 2.99], 0.996 (1.000).
  - Migdal: NaCl 0.498.
  - Pairwise and other quoted probabilities: P(Ge<GaSb) 0.974, P(CsI>Bi₂Se₃) 0.978, P(CsI>NaI) 0.985, P(GaSb<Ge) 0.826 ("0.83"), Si/Ge 1.113.
  - Tolerances 1.48/1.22, 3.63, 1.42.
- Arithmetic checks:
  - Diamond array: 1.79 and six crystals.
  - CsI: 8.956/2.404 = 3.7255, and 3.809 with ρ×1.045.
  - Edge with c_LA,max 2.458 km/s: 23.08 keV.
  - Polar reach 2ω_L/v_max² with 10.0 meV: 2.848 keV; GaAs 10.35 keV ⇔ ω_L = 36.34 meV; ratio 3.64.
  - GaAs ε = 4.2 + 0.17 = 4.37. CsI floor 1.77 and pair 11.3. Migdal 0.427. "Up to 4.4 times" (0.2119/0.0484 = 4.38).
- Pool bookkeeping: 23 + 3 + 16 = 42 = 11 + 31. KTaO₃ is not in the pool (it is not in Griffin Table I), which is consistent with "two candidates".
- Sources: Griffin 24 crystals; Wei et al. 3.37 ± 0.01 with a = 0.85 ± 0.005, resolution value 3.32; Rodrigues 3.749 at 123 K; Nielsen Fig. 1 = measured values; Melchiorre 4.3 g, about 10 mK, NTD; Angloher 2 × 0.175 g, 16.8 eV. All CHECKED.
- Accepted Ch17/18/20 values: TeO₂ 0.968 → 0.781 (rank17_6 l.274); 0.987 → 0.956 and 4.8 % (s17-6); ×10 two-pair overcount at 5 eV (sec:18.3-fullband); 2.32 eV = (1+θ_ii)E_g with E_g = 1.16 (18.3). All CHECKED.
  - Mixed figures: tab:21-dominant quotes 17 % of events (simplified cascade, a factor 5.9), while 21.7 and tab:21-nuisances quote "about tenfold" (full band). Both are right. Name the cascade in the table row.
- GAP (provenance; CORRECTIONS l.601 and SOTA l.656). The capability cell "h-BN: crystals below 0.1 g" is stated as fact, but research marks it "S2 FAIL rests on an [UNVERIFIED] row". Either source it or write "not documented".
  - Also per CORRECTIONS l.601: the diamond C_ij, LiF ε₀, GaSb low-T gap and CsI C_ij are "literature read", not measurements. DC-93 records Vallin as "abstract read, full text not".

### A11. Radioactivity budget (689 per kg day keV per Bq/kg; 1.45 mBq/kg)
- Shapes recomputed (chk2.py): f(³H, Q 18.591, Z_d 2) = 0.08916; ²¹⁰Pb gs (63.5, 83) 0.04380; ²¹⁰Bi (1161.2, 84) 9.66e-4; ⁴⁰K unique third-forbidden 4.133e-4; ¹¹⁵In allowed 3.71e-3 and unique fourth-forbidden 4.54e-4.
- Budget: 86400 × (0.16·0.0438 + 9.7e-4) = 689.1 (605.6 + 83.5). 1/689.1 = 1.451 mBq/kg. Per kg of Pb: PbSe 2.00, PbTe 2.34, PbS 1.68.
- Other numbers: KTaO₃ (w_K 0.1459) 4626 Bq/kg and 1.47e5. InSb 121 Bq/kg and 4.8e3–3.9e4. ⁴⁰K 31.7 Bq/g. ¹²³Te 3.358e22 per kg, giving < 693 per kg per day.
- Compton 2πr_e²m_e/E² = 1.1948e-28 cm²/keV. Cube mean escape path 0.4481 L (Monte Carlo, 2e6 draws). Fraction 5.35e-4.
- Decay data (84/16 %, 46.5/17.0 keV, 22.2 y): CHECKED.
- **W2 WRONG.**
  - (i) "the ²¹⁰Bi part, a sixth of the total": it is 83.5/689 = 12.1 %, an eighth. The same error is in tab:21-nuisances, "crude for a sixth of it".
  - (ii) "the nonrelativistic Fermi function is crude at Z_d = 83; both move the ²¹⁰Bi part": Z_d = 83 is the daughter of ²¹⁰Pb. ²¹⁰Bi decays to Po, Z_d = 84, which is what the script uses.
  - Size, from the relativistic Fermi function (point-like 2(1+γ)(2pR)^{2γ−2}e^{πy}|Γ(γ+iy)|²/Γ(2γ+1)², allowed shape):
    - ²¹⁰Pb gs f = 0.0445 (+1.5 %); ²¹⁰Bi f = 1.26e-3 (+31 %);
    - total 724 (+5 %), budget 1.38 mBq/kg.
  - Correct to: "the nonrelativistic Fermi function, crude at Z ≈ 83–84, and the first-forbidden shape of ²¹⁰Bi move mainly the ²¹⁰Bi part, an eighth of the total; a relativistic Fermi function alone raises the total by about 5 %."
- GAP (minor). In eq:21.7-pb210 the left side lacks the "per Bq/kg" (×1 Bq kg⁻¹) needed for the stated units.

### A12. Tritium (Ge 7.31 against research 6.7): CHECKED
- 82 × 0.0892 = 7.31 at saturation. 100 d at sea level (T½ = 12.32 y): Si 0.169, Ge 0.112.
- 82 ± 21 is in 1607.04560.
- The research value 6.7 (WP8-U-top row 7) is 75 × 0.0892: the calculated production rate (WP8-F l.77, 75 ± 26). The book uses the measured 82. No superseded value. The difference is the production-rate choice, not an error.

## B. Remaining items by location

21.4
- eq:21.4-classical: limits 2.303 − b, 1.303, 2.890, 3.322 and the empty interval for b > 2.303. CHECKED.
- FC ratio = Eq. (4.1), Sect. IV A. Table IV: 2.44, 1.61, 1.08, 3.36. CHECKED against physics/9711021.
- eq:21.4-Nsig: dimensionless (cm² · kg yr · kg⁻¹ yr⁻¹ cm⁻²). eq:21.4-beta/band/profile: dimensionless. CHECKED.
- Limits: one bin β = −ln(1+δ); t' = t* at zero counts; e^{1.15σ²} = 1.195; t' = 2.61 at N_bkg = 1. CHECKED.
- Excluded cells:
  - Al 0.20 and 0.37 → 1.250 and 1.587 (we:15-alrate). CHECKED.
  - Migdal 33 % and 7 % → 1.493 and 1.075 (tab:12-nuisances). CHECKED.
  - The 10 μm scope respects DC-41. CHECKED.
- tab:21-dominant entries against the channel chapters (16 and about 29; 0.07/0.69; 0.24 %/−6.8 %; 2 %/37 %; 7.8 %/7.3 %; ×1.23; ×2.8; ×9 at 0.36 MeV; ×1.2–1.4): CHECKED. The δ ln m_min = δ ln E_th edge statement and ×231 (21.3): CHECKED.

21.5
- Monotonicity of the Poisson CDF in μ (dP/dμ = −P(N = n)): CHECKED.
- One-exposure closed form (θ̂̂ = −ku, N_nom = N90·e^{k²N90}): CHECKED in sympy, and −0.514 for A alone.
- tab:21-recast signs: 𝒦 = (1+δ)^{−ϑ}; ε_bg² and ε_bg^{1/2}; R^{-1/2}. CHECKED.

21.6
- Storage figures: 7.5e6 nodes × 12 × 8 B = 720 MB; 2.24e5 pairs → 1.68e12 numbers = 13.4 TB; 20 share bins = 1.2 GB; lattice table 1.2e7 values; 50 meV / 1.3 meV = 38. All CHECKED.
- Further facts: ℓ = 4, 6, 8 (no cubic ℓ = 2, odd ℓ removed by time reversal); detailed balance; S = (2q²/e²)L with the Gaussian-units remark (factor 4π); retarded vs advanced in GaAs 15 % (8.7); the x³ range 1.3 meV and 49 meV (21.3). All CHECKED.
- GAP. "R⁰_GG′ … some 600 TB" and "about 10 GB" have no stated basis. 600 TB/(7.5e6 × 16 B) implies N_G ≈ 2240 per node, which is neither the 500 eV wavefunction basis (about 1000 plane waves) nor |G| ≤ 25 αm_e (about 7e4). State the N_G assumed, or drop the number.

21.7
- eq:21.7-beta: the T → 0 limit is flat (p cancels 1/p of the nonrelativistic F). The unique n-th forbidden shape factor is homogeneous of degree 2n and is the standard form. CHECKED.
- eq:21.7-compton: Klein–Nishina T → 0 limit; full form at 1 keV is 0.99976 of it. CHECKED.

Summary and tab:21-nuisances
- All numbers agree with 21.1–21.7, except:
  - (i) "a sixth" → "an eighth" (W2);
  - (ii) "Statistical construction" row: add or replace with the construction adopted under A3;
  - (iii) if W1 is fixed, the summary's band factors stay, but any 21.4 limit values quoted elsewhere change.
- 21.1–21.3 numbers quoted in the summary (430.3/735.6 km/s, 3.9 %, +7.6/−13 %, 2.22/3.52, 1.00–1.15, 0.095 %, 0.034, 13/2, 15/2, 8–10, −3.3 km/s, ×231/8.8/2.7, 62/8.5, 6.0e-5/3.7e-8, +0.8/+4.3 %) match the section texts. They were not re-derived here; that is part 1's scope.

## C. Convention and notation drift against NOTATION
- 𝒦_j (21.5 recast factor) clashes three ways:
  - with 𝒦 of 8.5, the lattice-regime component of 𝔗, which 21.6's WE prints in the same chapter;
  - with 𝒦_t (14.6);
  - with 𝓚_c (18.1).
  - Known editor item, still open. Proposal: ℛ_j^{rc} or 𝔨_j.
- β_k, σ_β (21.4/D.47) against β, the inverse temperature: NOTATION rules "never bare β", and 21.6 uses e^{−βω}. Rename (for example b_k, σ_b) or add a flagged row.
- Not in NOTATION: β_k, σ_β, a_j, t', N^up, 𝒦_j, f_β, n_β, y_S, Z_d, b_{²¹⁰Pb}, r_cl.
  - r_cl duplicates the classical electron radius; check for an existing r_e row.
  - Ledger merge pending: SEAMS 21.4–21.7 exist.
- 𝖱_FC (21.4) against 𝖱, the detector record (18.3/21.6): minor, since the subscript separates them.
- k is used as ln(1+δ) (8.8/21.5), as k_tail and as the wavevector, and a as Wei's conversion constant and the weights a_j. Both are local; flag only.
- Factor, π and sign checks: −2ln L constraint ϑ²; β sign (negative for signal-raising templates); e² = 4πα in S = 2q²L/e²; detailed balance sign; ζ ∝ ε_bg^{1/2}. No drift found.

## D. Campaign cross-checks (CORRECTIONS, SOTA, DC-RESULTS)
- No superseded value is used.
  - SOTA headline figures (TeO₂ 2.31, Ge floor 0.210, diamond 3.15) are older research numbers. The book recomputes them (2.39, 0.212, 3.11) with the Ch17 inputs, which is legitimate.
  - CsI ε_eh: the book's 11.3 eV (cascade median) is not the withdrawn v1 value 11.46. GAP-EF-v2 gives 11.21, a 0.8 % difference.
- DC-93 (CsI): the measured C_ij route is used; c_LA,max 2.46 lies within DC's 2.32–2.46. DC asked for "≈ until the rerun"; the rerun is done in guide21_7, so 3.73 may be quoted. Provenance caveat: abstract read only.
- DC-49/54/36: see A7 and A8. The quoted wording matches REF §4 items 1–4, with the extra derived 1.04–4.5 clause.
- DC-41: the 10 μm mean-free-path scope is stated in the same passage (see B, 21.4).
- DC-67: the Si ε 3.7468 eV of DC-67 agrees with the measured 3.749 used. No library table is used.
- DC-91: LiF ε∞ 2.04 and Z* 1.054 (PBE, not refereed) do not enter; the guide uses Griffin's inputs. No conflict.
