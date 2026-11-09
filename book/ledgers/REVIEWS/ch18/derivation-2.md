# Ch18 derivation check, part 2 (ch18.tex opening, 18.4, 18.5, Summary), isolated verifier
Scope: tex/ch18/ch18.tex, s18-4.tex, s18-5.tex, s18-summary.tex against NOTATION, STYLE, the cached logs (figscripts/ch18:
table18_4, limit18_4a/b/c, end18_5) and 12 cited arXiv sources fetched with lit.py into sources/review-ch18/ (PDFs deleted
afterwards; .txt/.html kept). Algebra redone in sympy (scratch sym18.py). The cascade numbers were checked against an
**independent event-by-event Monte Carlo** (scratch mc18.py, Dirichlet(3/2,3/2,3/2) splits, rejection for the hole cutoff, no grid),
not against the solver itself. No QE or heavy runs. Verdicts: WRONG = must change; GAP = missing or unsupported step; CHECKED = verified.

## Summary of actions (WRONG / GAP first)
1. s18-5 l.110 WRONG: "half of the gap energy has returned to the lattice at 0.83 µs, 99 % at 4.4 µs" confuses r_gap (still
   held) with the phonon return. Also "misses 42 %" leaves out the 5.6 % already lost to traps and light. Corrections below.
2. s18-4 l.36 (lim:18.4b) WRONG: the plane misses the cascade by 6–7 % at A_AB = 1, not 4 %. It is 4 % only at A_AB = 12.
3. s18-4 l.178 WRONG: SiO₂ (quartz) lies inside the validated range (λ 0.0073, w 0.0162; limit18_4c.log "True") and is
   missing from the list of Chap. 17 crystals inside it.
4. s18-4 l.33 (fig:18-limit-b caption) WRONG attribution: R&K's "constant at 2 % level" (Sect. IV A) says how much F varies over
   their plane. It is not a Monte Carlo scatter.
5. NOTATION drift: A_AB is printed in eV³ (correct, see 18.4 below), but the NOTATION row (l.1409) says eV². Many 18.4/18.5
   symbols have no NOTATION row. Ē_res clashes with the C.11 E_res row. ε₀ = 11.4 needs a NOTATION/ruling entry.
6. s18-4 l.70, l.58–60, Summary l.9 GAP (convention): "6 % low" is meas/model − 1 = +5.9 %. The model is 5.5 % below the
   measurement (3.97 vs 4.2). The Ge "5 %" is 4.9 % or 5.2 %, depending on the definition. Pick one definition (the table's
   meas/model − 1) and say "the measurement lies 6 % above the model".
7. s18-4 l.174 GAP: the full-band "3.1 eV for silicon, 15 % below the measurement". The source compares with the room-temperature
   ≈3.6 eV (14.9 %). Against the book's 3.749 eV it is 17 %. Name the reference value.
8. s18-5 l.101 GAP: r_gap overstates the held energy by up to E_x^b plus the bound-exciton localization energy (≈4.7 meV for P),
   ≈1.7 %, not "at most 1.3 %".
9. s18-5 l.39 GAP (last digit and self-consistency): 0.56 % (0.33–0.78 % from the unrounded F = 0.11407). If A_AB is recalibrated
   to the loss-corrected pair energy, the loss needed becomes 0.60 %.
10. Summary GAP: it omits 18.4's linear law, the validated-range residuals and the full-band comparison. Its 18.1 numbers
   (2.997/2.712) and the "5.8 eV" nuisance row still use the 18.1 parameter set (A_AB = 5.2, E_g = 1.17). Nuisance table lacks the
   −6.6 to +24.5 % residual spread. Details below.
11. A_AB = 5.674 GAP (precision): it is a production-grid (E_g/73) value. The continuum value is ≈0.5 % higher. F and 2.5σ are unchanged.

## Priority items (editor-notes ch18 / partII), independent verdicts
- **A_AB = 5.674 calibration** — CHECKED with a precision caveat. table18_4.log gives 5.6737 eV³ at E_g = 1.160, ω_AB 63 meV,
  B_h 12 eV, which yields λ = 3.635 and w = 0.0543. The independent MC at 5.6737 gives ε_eh = 3.7476 ± 0.0023 eV (3.749 printed)
  and F = 0.1146 ± 0.001 (0.1141). Residual 0.719E_g (0.716) and r_K 14.60 (14.73) also agree. The log's grid check (N 73 → 146:
  ε −0.040 % on refinement, convergence order h^{3/2}) extrapolates to Δε ≈ −0.062 %, which needs ΔA ≈ +0.54 % (continuum
  ≈5.70 eV³, using dlnε/dlnA = 0.115). This matches REF-DC-67 §3, where production → continuum moved A from 5.588 to 5.616 at
  E_g 1.164. Suggest "A_AB ≈ 5.67 eV³ on the grid E_g/73 (≈0.5 % higher in the continuum)". Alternatively, drop the fourth digit.
  The 9 % above 5.2 (1.091) is CHECKED.
  The difference from the research value 5.62 (REF-DC-67 quotable item 6) comes from the gap (1.160 vs 1.164) plus the grid: the
  required λ rises by ≈2 % at the lower gap. This is consistent, and no superseded value is used.
- **Table 18.1** — CHECKED: every model entry against table18_4.log (Si 3.749/0.114; low 3.766/0.1138; Ge 2.814/0.1247,
  2.830/0.1243; GaAs 3.965/0.1039, 4.133/0.1021). Independent MC: Ge 77 K 2.818 ± 0.003 eV, F 0.124; GaAs 300 K 3.957 ± 0.003 eV,
  F 0.104 (0.2 % below the log, immaterial). Si F 2.5σ CHECKED: (0.119 − 0.11407)/0.002 = 2.47. REF-DC-67 also says 2.5σ, and
  CORRECTIONS l.605/612's "2.6σ" is the research production-grid figure, so the book's 2.5σ is the right one to print. Lowe–Sareen
  0.118 ± 0.004 is 0.98σ, CHECKED, and the source quote (2004.11499 Sect. 5) is CHECKED. Ge −5 % and GaAs −6 %: see action 6.
  Ge E_g(77 K) = 0.7346 is CHECKED (Wei Eq. (7)). The Bose occupation 0.0035 is CHECKED.
- **Klein relation** — CHECKED. Eq. 18.4-shockley holds by the energy identity, since each pair ends with one terminal e and one
  terminal h (t → t + t + t̄). Eq. 18.4-uniform: sympy gives ∫x^{3/2}/∫x^{1/2} = (3/5)θE_g, so K1 + K2 give 1 + 2·0.9 = 14/5.
  The source's form (2610.16949 Eq. (1), E_f = 0.6E_i, "2.2E_i + rE_R") has E_i in the pair term. The book's statement that E_i is
  replaced by E_g is what reproduces 14/5, so it is correct and needed. Klein 14/5 with Raman phonon is CHECKED (Wei Eq. (3)).
  The Klein constant "0.5 to 0.6 eV" is CHECKED: +0.5 in 2610.16949 Sect. II, +0.6 in 2308.03893 Eq. (9) Sect. IV.
- **36–39 % overstatement** — CHECKED. Phonon-free MC: 1.5860 ± 0.0006 E_g (θ = 1) and 2.0558 ± 0.0008 (θ = 3/2), against the
  printed 1.585/2.056. Ē_res 0.293/0.528 is CHECKED. 2.2/1.585 − 1 = 38.8 % and 2.8/2.056 − 1 = 36.2 %.
- **0.65–84 window** — CHECKED: limit18_4a.log gives 0.646 and 84.3. MC at θ = 3/2, w = 0.0543: Klein/cascade 1.219 at λ = 0.1
  (printed 22 %) and 0.898 at λ = 84.3. The Si point (λ 3.635) gives 3.238 ± 0.003 E_g, so Klein is within 0.2 %, CHECKED.
  Exactness at λ = 3.51 is CHECKED. Caveat: that point uses the θ = 3/2 cascade at the θ = 1 calibration, λ 3.64. The recalibrated
  θ = 3/2 model has A = 5.604 (λ 3.59), and the conclusion is unchanged. Diamond λ = 0.0347 and Klein 15.92 eV are CHECKED
  (2311.05011: "15.92 eV").
- **Linear-law fit** — CHECKED. 1 − (3 + 0.9666)·0.2404 = 0.0464, and the ω power is 0.232. Sympy reduces Eq. 18.4-fit to
  Eq. 18.4-linear exactly, and the dimensions close (A ω^γ)^β E_g^{0.046} → eV. Fit max 0.54 % and rms 0.20 % over 60 points,
  13/24 crystals in the box, k₂(Si) 1.875, k₂ ranges 1.20–2.52 and 1.51–2.52, and the 1.4 % outside the box (PbSe −1.41 %) are
  all CHECKED against limit18_4c.log. "Observed fit, not derivation" agrees with CORRECTIONS l.481 (v1 "derived" withdrawn). The
  empirical 1.54E_g + 1.89 is CHECKED (2610.16949 Sect. II).
- **Validated-range table (tab:18-valid)** — CHECKED every λ, w, model, residual and statistic (range −6.6/+24.5 %, mean 8.0 %
  printed as 8.1 from unrounded values, rms 12.2 %) against limit18_4c.log and by hand. MC diamond 11.344 ± 0.008 eV (11.37
  printed, 0.26 % apart, immaterial). Sources: diamond inverse-variance mean of 13.1 ± 0.2, 13.25 ± 0.5, 13.05 ± 0.2 and
  12.82 ± 0.13 is 12.948 eV, CHECKED, with full band 12.87, both in 2311.05011. 3C-SiC 6.90, SiO₂ 18.0, full band 6.6/7.3/16.7
  (2610.16949 Table II) CHECKED. 4H 7.83 ± 0.02 (2311.03902) and 6H 6.7 (2008.08560 Table I) CHECKED. GaN 9.59 EBIC and full
  band 8.9 (2308.03893 Sect. IV) CHECKED; that source also cites 8.9 eV (Sellin–Vaitkus review), which would give +15.6 %. Inputs
  CHECKED: diamond 5.47/161, GaN 3.43/88.9, SiO₂ 9.2/149 from 1910.10716 Table I; SiC gaps 2.39/3.02/3.26 from 2008.08560 Table I.
  For 6H, ω_LO is listed as 119.7/120.3; 120.0 is the mean, not the highest, and the effect is negligible. DC-91 PBE phonons
  (C 160.3, 3C-SiC ω_LO 117.0 meV) bear on these inputs, but DC-RESULTS says measured values stay preferred, so no change.
- **eq:18.5-Eg** — CHECKED. Shares (E_j − μ_F) + (E_c − E_j) + (μ_F − E_v) = E_g for any level, and N → N − 1 in
  Eq. 18.5-Enp gives +E_g. This is the content of GAP-EF-v2 IF-E9 (CORRECTIONS l.444).
- **Binomial thinning** — CHECKED (sympy): ⟨N′⟩ = (1 − f)μ, Var = f(1 − f)μ + (1 − f)²Fμ, so F′ = (1 − f)F + f and
  ε′ = ε/(1 − f). Eq. 18.5-thingen is the law of total variance, CHECKED. Small GAP at l.41: "not (1 − f̄)²Var N for any mean f̄".
  Some f̄ always solves the equation, so write "not, in general, (1 − f̄)²Var N_eh with f̄ the mean capture probability".
- **0.56 % explains 0.114 vs 0.119** — CHECKED in substance; see action 9. The +0.57 % on ε_eh (1/(1 − f) − 1) is CHECKED.
- **Heat-based Fano F(1 − E_x^b/E_g)²** — CHECKED (sympy). Si: 14.7/1170 gives (1 − x)² = 0.9750 (−2.50 %). Ge: 5/744 gives
  −1.34 % (Ge 5 meV per the R5 correction, CHECKED). Eq. 18.5-Fheat is the variance of E_np + E_x^b N_X, CHECKED. 0.39 % of ω
  (14.7/3749) CHECKED.
- **Unsplit excitons, r_𝓔** — CHECKED. Eq. 18.5-Fmeas uses the same algebra as thinning. r_𝓔 = (α/ε₀e𝓔)^{1/2} with
  α/ε₀ = 0.1263 eV nm gives 0.562 µm at 4 V/cm and 0.112 µm at 100 V/cm. The field-ionization scale
  E_x^b/(e a_x) = 3.5×10⁴ V/cm, with a_x 4.2 nm, is CHECKED and consistent with 4.9 after the App E alignment.
- **Rate-equation solution** — CHECKED except action 1. M is lower triangular, so the decay constants are the diagonal entries.
  ∫p dt = −M⁻¹p(0), b_trap = Γ_FT/(Γ_FX + Γ_FT), and b_light matches Eq. 18.5-split exactly in sympy. The fluxes sum to 1.
  Numbers: γ = 1.053×10⁹, 1.1×10⁶, 4×10⁶ s⁻¹; weights +0.0499/+1.2790/−0.3288; split 0.0500/0.0086/0.9414.
  r_gap(1 µs) = 0.4197. r_gap reaches 0.5 at 0.8327 µs and 0.01 at 4.410 µs. p_B peaks at 0.1455 at 0.446 µs (analytic
  t* = ln(4/1.1)/2.9×10⁶ s). Γ_FT/Γ_FX = 0.0526, printed "0.053", is CHECKED. The source quote (200–300 ns via Lo et al.,
  from Schmid 1977) is CHECKED (1411.1324 l.66, Auger l.76). Lo does not state the temperature; "liquid-helium" comes from Schmid.
- **Summary and nuisance table vs final sections** — see the Summary section below.

## 18.4 line by line
- l.3 CHECKED: 3.749 ± 0.001 and 0.119 ± 0.002 at 123 K, 5.9 keV (2004.11499 abstract and table).
- l.7 GAP (minor): "Germanium and GaAs need slopes fitted between 30 and 60E_g when λ > 5". GaAs has λ 1.98/1.62, so only
  germanium qualifies. Write "Germanium, with λ_AB > 5, needs …". The grid claims (0.04 %, 0.05 %) are CHECKED. s18-2 says grid
  E_g/74 and s18-4 says E_g/73. Both are commensurate choices of grid(), but state one.
- l.9 CHECKED: E_g(123 K) = 1.1692 − 4.9×10⁻⁴·123²/(123 + 655) = 1.1597 (R&K Eq. (11)). ω 63 meV is from R&K Sect. II B.
- l.14 CHECKED: A = 5.2 at 300 K (R&K Table I), and Alig's fit to 5.2 (2610.16949 Sect. II).
  **Units**: R&K print "eV²" (Eq. (9), Table I). Their Eq. (8), Γ_ph/Γ_eh = A(105/2π)(E − ω₀)^{1/2}/(E − E_g)^{7/2}, needs eV³
  to be dimensionless. The book's eV³ is right, and E.13 l.69 already says so. NOTATION row A_AB (l.1409) still reads "eV²"
  (WRONG): change it to eV³ with "quoted as eV² in the source".
- l.20/lim:18.4b CHECKED: planes Eq. (12)–(13), Sect. III A algorithm (plasmons, hole re-split), "∼100 eV" (Sect. IV). E_g =
  1.124 is R&K's Fig. 3 slice. Their Eq. (11) gives 1.1230 at 300 K, which does not matter here.
- l.33 WRONG attribution: see action 4. Write "Light band: ±2 %, the level at which the source finds F constant over its plane
  (Sect. IV A)", or drop the band's interpretation.
- l.36 WRONG: limit18_4b.log at A = 1 gives eps ratio 0.926 and F ratio 0.936, a miss of 7.4 % and 6.4 %. At A = 12 it gives
  0.9615 and 0.9575 (3.9 %, 4.3 %). Correct to "by 6 to 7 % at A_AB = 1 and 4 % at 12".
- l.39 CHECKED: deviations 1.15 %/2.42 %, slopes 0.0904/0.00161/1.702/−0.0296, max slope difference 7.6 %, F 0.1144 against
  F∞ 0.115 (Sect. IV A). Trivial: "1.3 to 2.4 % above" is plane/solver − 1 = 1.3–2.5 %.
- l.45 CHECKED: Ge 37.6 meV (tab:5-phonons), GaAs ω_L 36.35 meV (s5-5 l.95).
- l.48 caption CHECKED: Mei Sect. 4.3 gives 2.96 eV at liquid-N₂ temperature and F 0.06–0.13 from five experiments [69–73].
  Bertuccio–Maiocchi GaAs is a data point in 2610.16949 Fig. 1 (≈4.18 eV in the original, so "≈4.2" stands).
- l.66 CHECKED: ±10 % A gives ε +1.15/−1.25 %, F +0.65/−0.71 %. MC: A×1.1 gives ε +1.18 %; F is within noise. Variants:
  θ = 3/2 gives 0.1133 (MC 0.1130 ± 0.001), CHECKED; ρ ∝ x gives 0.1024 (log only). R&K 0.115 is CHECKED.
- l.68, l.70 CHECKED: λ 14.3 and 1.98, ε/E_g 3.83/3.23/2.79, w 0.026. Wording: see action 6.
- l.81 CHECKED: 1.160 + 1.661 + 0.928 = 3.749. Ē_res = 0.8305 eV = 0.716E_g. r_K = 0.928/0.063 = 14.73.
- l.83 CHECKED: θ_ii = (2m_e + m_h)/(m_e + m_h) = 3/2 at equal masses (eq:18.1-theta).
- l.93, l.95, l.108, lim:18.4a: CHECKED (priority items above).
- l.112–136, lim:18.4c, fig:18-limit-c: CHECKED (above). The caption's fit window "12.5 to 25E_g" differs from Table 18.1's
  20–40E_g. Values agree to 0.03 % (Si 3.767 vs 3.766), so this is acceptable, but say so once.
- we:18-gaas CHECKED: λ 1.6157, w 0.02391, w^γ 0.02709, product 0.04377, power 0.4713, 2.7146, 4.126 eV. k₂ 1.670 and
  36.35/63 = 0.577 are CHECKED, as are the 0.19 % fit cost, empirical 4.231, Klein 4.756 and the 300 K value 3.960. Trivial:
  "1.61E_g = 2.46 eV" is 2.447 with the printed 1.61; it is 2.456 only with the unrounded 1.6159. Write 2.45, or 2.46 with
  "1.616".
- l.174 CHECKED, except action 7: residual statistics, and full band better for C/3C/GaN and worse for 4H/SiO₂.
- l.176 CHECKED: Gsponer Table 2 (0.1 linewidth [17]; ≤ 0.04 upper limit [13]), Eq. (3) noise subtraction. Model 0.0932.
  The minimum F of the scan is 0.0826 > 0.04.
- l.178 WRONG (action 3). Otherwise CHECKED: sapphire w 0.0118, MgO 0.0105 (printed 0.011), GaSb λ 15.2.
- l.180 CHECKED: halide/fluoride w 0.0016–0.0059; lead salts/InSb λ 233–1155, gaps ≤ 0.29 eV. LiF 25.06, NaF 20.49, CsI 11.21
  (the superseded v1 11.46 is not used, CORRECTIONS l.481) and PbSe 1.563 are all CHECKED. "No measured ε for sapphire,
  CaWO₄, LiF, NaF" agrees with EF-LIT (SOTA l.562).

## 18.5 line by line
- l.12 CHECKED: at fixed ω, Var N = Var E_np/E_g².
- l.14 CHECKED (eq:18.5-Eg above).
- l.43 CHECKED: r_C(0.1 eV) = 1.263 nm, πr² = 5.01×10⁻¹⁴ cm², 20 cm at 10¹² cm⁻³. At 0.35 eV: 0.361 nm and 4.09×10⁻¹⁵.
  At 10¹⁸ cm⁻³ the length is 0.2 µm (0.1 eV) to 2.4 µm (0.35 eV), so "micrometers" is CHECKED. k_BT(50 mK) = 4.309 µeV.
  Coulomb radius 29.3 µm. CDMS II "flashing" with IR LEDs is CHECKED (1803.02903 Sect. 2). ε₀ = 11.4 is the editor-noted
  11.4/11.7 item. 11.4 is physically right at mK, but NOTATION's ε₀ row allows 11.4 "once in 7.4" only, so it needs an extension.
  With 11.7, the radii shrink by 2.6 % (r_C) or 1.3 % (r_𝓔), and no printed conclusion changes.
- we:18-capture CHECKED: 25.80 → 26.97 eV, 45.6 meV and 1.124 eV, 33.75 eV, 4.167 eV (+11.1 %), F′ 0.2071, σ 1.091 → 1.365,
  variance split 0.964 + 0.900 = 1.864 (end18_5.log, Monte Carlo 0.2071). Small GAP: the mean pair number at 37.5 eV is
  ω/ε + b_N ≈ 10.35, not ten. Harmless, since the example then fixes N = 10, but "on average ten" should read "about ten".
- l.53, l.55, l.60 CHECKED: 3412 k_BT, 0.39 %, −2.5 %/−1.3 %.
- l.72 CHECKED: field numbers. The dense-track statement is qualitative.
- l.74 CHECKED: 1.70 × 14.7 = 25.0 meV (0.67 %), Ge 8.5 meV (0.30 %). Wording GAP: 1.70 is the secant slope at R&K's
  parameters (A 5.2, E_g 1.124), not "of the calibrated cascade". The calibrated cascade gives ∂ε/∂E_g|_A = 1.616 +
  0.046k₂/E_g = 1.69 (Si) and 1.72 (Ge), so the numbers stand.
- l.87, l.94 CHECKED: Auger mechanism; Poole–Frenkel lowering 2(αe𝓔/ε₀)^{1/2} (sympy max of −α/ε₀r − e𝓔r) = 2.25 meV at
  100 V/cm. Exponents 1.058×10⁴ and 1.006×10⁴.
- l.101 GAP (action 8). The rest is CHECKED: weights may be negative, and the integrals.
- l.110 WRONG (action 1). With phonons(t) = 1 − r_gap − trapped(t) − light(t) (quadrature): 0.445 at 0.833 µs, 0.525 at 1 µs,
  0.932 at 4.41 µs. Correct to: "half of the gap energy is still held at 0.83 µs and 1 % at 4.4 µs; a heat readout that closes
  its window at 1 µs misses the 42 % still held, plus the 5.6 % already trapped or radiated." The weights and the 0.15 peak
  at 0.45 µs are CHECKED. Nuisance-table row "42 % at 1 µs, 1 % at 4.4 µs" (gap energy still held) is CHECKED as worded.
- fig:18-end caption CHECKED.
- l.125 CHECKED: a factor of 0.8 on Γ_ii is A × 1.25, which gives Δε ≈ 2.6 % (log sensitivity) to 3.5 % (linear slope
  0.090/eV³), so "about 3 %" holds. The "one half above 3 to 5 eV" comes from 18.1, outside this check.

## Opening (ch18.tex) and Summary
- ch18.tex l.2 CHECKED: 10/1.17 = 8.5 pairs (so "eight" is right), 3.749/1.160 = 3.2 ("three times"). "Two or three in nearly every
  event" is a model statement of 18.1's set (editor note: label as model; after the one-set ruling, recheck with A 5.674).
- Summary l.3 GAP: 2.997/2.712 at 10 eV come from 18.1's set (A 5.2, E_g 1.17). The ruling "one set, 18.1 rerun (shift < 0.03)"
  makes them provisional. Update them with the rerun. The same applies to nuisance row 2's "5.8 eV": the calibrated set gives
  5.88 eV (Γ_ph = Γ_ii solved from Eq. (8) with A 5.674, E_g 1.160), so print 5.9.
- Summary l.5 CHECKED against s18-2 l.49 (book values 0.092 + 0.291 − 0.269; the research 0.091/0.288/0.265 is not used). 6.7×
  Poisson (s18-2 l.49), 0.0510387 and b_N 0.35 (known 0.345/0.352 item) are as in 18.2.
- Summary l.7 CHECKED against s18-3 l.3 (17 %).
- Summary l.9 GAP (editor note confirmed): add the linear law ε ≈ 1.61E_g + k₂ (k₂ 1.2–2.5 eV, an observed fit), the validated
  range (λ 0.007–14, w 0.016–0.054, residuals −7 to +25 %, rms 12 %) with the outside groups as estimates for 21.7, the Klein
  window 0.65–84, and the full-band comparison. "GaAs 6 % low": action 6. The rest is CHECKED.
- Summary l.11 CHECKED against 18.5 (all numbers). "Exact split" is right for the linear equations.
- tab:18-nuisances CHECKED row by row against 18.4/18.5 (0.47/4.7 for a 10 nm sphere with a_x 4.2 nm; z_qp 3 %; 17 %, 2.997/2.712;
  0.114 vs 0.119 2.5σ, 0.113, 0.102; Klein 0.2/22/36 %; Ge 5 %, GaAs 6 %; capture; F_heat; 0.56 µm; 25/8.5 meV; 42 %/1 %).
  GAP: the row "One phonon constant for all crystals" should carry the validated-range spread (−6.6 to +24.5 %, rms 12.2 %;
  GaN +24.5 %, diamond +13.8 %), the largest model error of the chapter, not only Ge/GaAs. A row for the grid/fit-window
  dependence of A_AB (≈0.5 %) is optional.

## NOTATION / convention drift
- A_AB units eV² (NOTATION l.1409) vs eV³ (s18-2, s18-3, s18-4): fix NOTATION (action 5).
- No rows for λ_AB, w_AB, B_h, Ē_res, k₁, E_np, E_heat, E_<, E_> (18.2 owner), f_cap, ε′_eh/F′_eh, N′, r_C, p_ns, r_𝓔, F_heat, N_X,
  r_gap, w_k, γ_k, b_trap/b_light/b_heat, Γ_FX/Γ_FT/Γ_X/Γ_XB,j/Γ_B,j, η_X, η_B,j, σ_XB,j, v_X, 𝓃^tr_j, σ_cap,j, σ^rec_j, Γ^em_j, μ_F,
  E_j. Research used r_cap/σ_cap (CORRECTIONS l.279–280), and r_C(E) is a different (energy-dependent) object, so keep it local.
- Ē_res (18.4, mean residual per terminal carrier) vs NOTATION E_res (C.11, renewal undershoot): the objects are related but not
  identical. Add a row or rename it Ē_term.
- F_meas: NOTATION gives first use as 20.1, but it is defined in 18.5 (Eq. 18.5-Fmeas). Move the row's section to 18.5.
- No factor-of-2, π or sign drift found. 105/2π matches Φ = (2π/105)y^{7/2} = Γ(3/2)³/Γ(9/2)·y^{7/2}. Var/mean conventions
  for F are consistent across 18.2/18.4/18.5.

## Campaign returns and DC-RESULTS
- DC-67 (PARTLY VALIDATED; quote REF-DC-67 §8 only). Its Si statement (F ≈ 0.114, 2.5σ, A ≈ 5.62 eV³ at E_g 1.164, continuum)
  agrees with the book (0.1141, 2.47σ, 5.674 at E_g 1.160, grid E_g/73). The A difference is explained above. No library value
  (Ge 2.794, GaAs 3.944) is used in the book, which is correct since the library is not releasable.
- GAP-EF-v3 (CORRECTIONS l.612): research A 5.588, max residual +24.7 %, rms 12.3 %, (EF9) 2.329/0.965. The book's own
  recalibration at E_g 1.160 gives 5.674, +24.5 %, 12.2 % and 2.331/0.9666. These are internally consistent book values, not
  superseded ones. CsI uses 11.21 (v3), not the withdrawn 11.46.
- DC-91 (C, 3C-SiC PBE phonons): no change; measured inputs are preferred. DC-2/DC-93/DC-83/DC-41/DC-49-54-36: no bearing on 18.4–18.5.
