# Chapter 1 derivation check (isolated verifier)

Scope: tex/ch01/s1-1..s1-5, tex/appC/C-9, tex/appD/D-1, against NOTATION.md and the cited sources. Sources fetched with lit.py into
sources/review-ch01/d<arXiv id>/ (html + pdftotext .txt kept; PDFs deleted). "PDF p." = arXiv PDF page index (Essig 2016's printed page
numbers differ by 2). Scripts: sympy for the algebra, scipy quadrature/MC for the halo numbers, the fig1_9.py toy re-run without plotting.
Verdicts: CHECKED (redone, agrees) / WRONG (correction given) / GAP (true but incomplete, mis-cited or unverifiable as cited).

## A. Rulings on the known items

1. **v_min: absolute value (1.3-vmin) vs D.1 signed sentence.** The absolute value is CORRECT: the delta function has a root in cos θ ∈ [−1, 1]
   iff v ≥ |(ω+Δ_χ)/q + q/2m_χ|. It is needed exactly when ω+Δ_χ < 0 (exothermic, or ω < 0 at T > 0); the signed form of Kahn–Lin Eq. (10)
   (PDF p.8) and Essig 2012 Eq. (2) (PDF p.3) is the special case ω ≥ 0, Δ_χ = 0, as the text says. D-1.tex line 50 ("For v_min < 0 ... η = η(0)")
   is the signed-form remnant: harmless but dead. Replace with: "By (1.3-vmin), v_min ≥ 0, so η is never needed at negative argument."
   NOTATION v_min row should say "|…|, ≥ 0" (editor decision (ii) is otherwise satisfied).
2. **σ̄_e = 3.0×10⁻³⁹ cm² (§1.4 WE).** CHECKED. Lin Eq. (74) (PDF p.44): σ̄_e = 16π μ_χe² κ² α_χ α/((αm_e)² + m_V²)², identical to (1.4-darkphoton)
   with y_χ² = 4πα_χ. Benchmark (Sect. III D, PDF p.44: m_χ = 10 MeV, m_V = 30 MeV, g_χ = 0.3, κ = 10⁻⁴) gives 7.665×10⁻¹⁸ MeV⁻² = 2.985×10⁻³⁹ cm².
   Lin's sentence "the two benchmarks give comparable values σ̄_e ≈ 10⁻³⁷ cm²" holds only for freeze-in (6.05×10⁻³⁸, also CHECKED); it is off by ~30
   for the thermal benchmark. GAP (text): add one clause so a reader comparing with Lin is not confused, e.g. "(Ref. [Lin] quotes ≈10⁻³⁷ cm² for
   both benchmarks; Eq. (74) gives 3.0×10⁻³⁹ for this one)".
3. **Al gap (§1.5).** Attribution CHECKED: Hochberg 2016 Sect. 2.2.1 "of order 0.6 meV in aluminum" (PDF p.8), Mitridate Table II 2Δ = 0.6 meV
   (PDF p.23); "~60 % into quasiparticles" CHECKED (Hochberg 2016 PDF p.9). Physics GAP: bulk Al, T_c = 1.175 K, BCS 2Δ = 3.53 k_B T_c = 0.357 meV
   (tunnelling ≈ 0.34 meV); 0.6 meV needs T_c ≈ 2 K (thin/granular films). Recommend: "bulk 2Δ_BCS = 3.53 k_B T_c ≈ 0.36 meV; thin films are higher,
   and the dark-matter literature adopts 0.6 meV". The single-pair threshold mass is then 0.10 keV (bulk) / 0.17 keV (0.6 meV): both CHECKED
   (2E/v_max²). Table 1-quanta "below 1 meV" stays true.
   **Toy rate, WE 1.7 (we:1-limit).** Arithmetic CHECKED: 3 cm⁻³ × 1.0720×10²⁵ kg⁻¹ × 2.1877×10⁸ cm s⁻¹ × 1.0102 = 7.107×10³³; r = 2.243×10⁴¹;
   N_sig = 22.4; σ̄_e^lim = 1.027×10⁻⁴¹ (text 1.03) CHECKED. M_cell = 52.33 GeV and the "second line O(1)" statement CHECKED (Essig 2016 below
   Eq. (3.13), PDF p.15–16). GAP: (3.13) is dR/d ln E_e, so R_toy is a per-log-energy spectrum; integrating ln E_e from E_g to ~30 eV adds a factor ≈ 3.
   Say "toy spectrum per unit ln ω" or include the factor. (Source-side, not the book's: Essig's own "≈29 events/kg/day" is ~10× below their formula:
   4 cm⁻³ × N_cell × 3.6×10⁻³⁷ cm² × αc = 292 kg⁻¹ day⁻¹. Do not quote it.)
4. **Freeze-out (§1.1), 2.2 vs 3 ×10⁻²⁶.** Derivation of (1.1-sigmav) from (1.1-fo) + entropy conservation CHECKED (sympy): ⟨σv⟩ = (45·1.66/2π²)
   x_fo s₀/(g_*^{1/2} M_Pl ρ_c). Numbers: s₀ = 2.2205×10⁻³⁸ GeV³ (2891 cm⁻³ from T₀ = 2.7255 K, g_s = 3.909), ρ_DM = 9.71×10⁻⁴⁸ GeV⁴, ⟨σv⟩ =
   1.98×10⁻⁹ GeV⁻² = 2.31×10⁻²⁶ cm³ s⁻¹, 1 GeV⁻² = 1.1673×10⁻¹⁷ cm³ s⁻¹: CHECKED ("≈2×10⁻²⁶"). 3×10⁻²⁶ as "commonly quoted": CHECKED (Steigman
   abstract, PDF p.1). 2.2×10⁻²⁶ above 10 GeV and 5.2×10⁻²⁶ at ≈0.3 GeV: CHECKED (abstract p.1; p.8). WRONG cite: Steigman's numerical results are
   **Sect. II C** (PDF p.7), not III C (III is "Confronting experimental limits"). GAP: Steigman assumes a Majorana χ (PDF p.9; Dirac doubles it)
   and Ωh² = 0.11 (WMAP-7); with Planck's 0.120 the value scales to ≈2.0×10⁻²⁶. Add both in a clause. The closeness of the crude estimate to 2.2 is
   partly coincidental (it omits post-freeze-out annihilation); fine as "order of magnitude".
   x_fo iteration: 25.6 at 100 GeV (g_* = 80) CHECKED; at 1 GeV it gives 21.0 (g_* = 80) or 22.0 (g_* = 10.75), not 20 → WRONG(minor): write "≈ 22".
   The ⟨σv⟩ inserted in the iteration is unstated (I used 3×10⁻²⁶; 2×10⁻²⁶ lowers x_fo by 0.4): GAP.
5. **Si numbers.** E_g(0) = 1.1692 eV CHECKED: Ramanathan–Kurinsky Eq. (11), PDF p.4 (a = 4.9×10⁻⁴ eV K⁻¹, b = 655 K; gives 1.123 eV at 300 K).
   a = 5.431 Å: CODATA not fetched (offline); value is standard. Ch. 1 uses it only via a ≈ 10/(αm_e) and 2π/a ≈ 2.3 keV: with 5.431 Å, a = 10.26 a₀,
   2π/a = 2.283 keV = 0.612 q₀ CHECKED; "a ~ 10 a₀" CHECKED (Kahn–Lin Sect. V, PDF p.46). GAP: "E_g = 1.11 eV at room temperature [Essig Eq. (5.2)]"
   (§1.3 ×2): Eq. (5.2) (PDF p.19) gives 1.11 eV with no temperature; Ramanathan Table I (PDF p.5) has ≈1.12 eV at 300 K, 1.169 at 0 K. Write
   "1.11 eV, the value of Ref. [Essig Eq. (5.2)] (1.12 eV at 300 K, 1.169 eV at 0 K [Ramanathan Eq. (11)])". At 1.1692 eV, m_min = 0.333 MeV (+5.3 %).
   WRONG: §1.5 Photons ¶ "each photon above the 1.2 eV gap" contradicts 1.11/1.17 → "the 1.1 eV gap (1.17 eV when cold)".

## B. Section 1.1
- (1.1-vc), (1.1-iso): CHECKED (sympy d/dr(v²r/G)/(4πr²) = v²/(4πG r²)); dims eV⁴ CHECKED; flat-curve M ∝ r CHECKED.
- WE local density: v_c = 7.338×10⁻⁴, v_c² = 5.385×10⁻⁷, r = 1.2510×10³⁶ GeV⁻¹, 4πr² = 1.967×10⁷³, ρ = 4.076×10⁻⁴² GeV⁴, (ħc)³ = 7.684×10⁻⁴²,
  0.530 GeV cm⁻³: all CHECKED. Kahn–Lin Eq. (2) 0.3–0.5 GeV cm⁻³ (PDF p.4) CHECKED.
- (1.1-rhocrit) 1.054×10⁻⁵ h² GeV cm⁻³ CHECKED. (1.1-omegac) 0.1200(12): Planck Table 2 (PDF p.16) and Eq. (23) (PDF p.19) CHECKED; abstract
  0.120 ± 0.001 (p.1) CHECKED; Ω_b h² 0.02237(15) CHECKED; ratio 5.36 → "5.4" CHECKED; mean density 1.264×10⁻⁶ CHECKED; 0.3/1.26×10⁻⁶ = 2.4×10⁵
  ("about 2×10⁵") CHECKED.
- KE ½m v²: 0.5 keV / 0.5 eV / 0.5 meV CHECKED. Xe at 1 GeV: 0.113 keV ("about 0.1 keV") CHECKED (M = 122.30 GeV).
- H_Hub = (8π³g_*/90)^{1/2}T²/M_Pl, 1.6602 CHECKED; Lin Eq. (19) (PDF p.15) CHECKED. Eq. (31) freeze-out (PDF p.20) CHECKED.
- Lin Sects. I A, I B, I C exist with the stated topics (TOC, PDF p.2); prose content not audited line by line: GAP (unverified, not wrong).
- Lee–Weinberg "m_χ ≳ 2 GeV [lee1977][Lin Eq. (44)]": GAP/WRONG-cite. Lin (PDF p.23) after Eq. (44) says the relic cross-section is undershot
  "when m_χ < GeV"; the 2 GeV is from Lee–Weinberg alone (not fetched). Cite Lin for the scaling only.
- "[Kahn–Lin Table I]" for "band gaps ≈ eV, optical phonons 30–150 meV, acoustic phonons and superconducting gaps at meV": GAP. Table I (PDF p.5)
  lists only 50 MeV↔zero-point momentum, 20 MeV↔10 eV, 2 MeV↔1 eV gap, 100 keV↔50 meV optical phonon. Cite elsewhere or drop "Table I".

## C. Section 1.2
- (1.2-rho) 2.305×10⁻⁶ eV⁴ CHECKED; 3 cm⁻³ / 3000 cm⁻³ CHECKED; one H atom in 3.1 cm³ CHECKED. Baxter Sect. 3.1.1 "0.2 to 0.6" (PDF p.11), Table 1 (p.11) CHECKED.
- (1.2-fgal) = Baxter Eq. (10) (PDF p.9) CHECKED. Note: Baxter (10) is the galactic-frame form; citing it also for f_χ(v) = f_gal(v+v_E) (line 72) is GAP (boost is implicit there).
- Jeans step: Green Eq. (11) (PDF p.5) with β = 0, σ_r² = v₀²/2, ρ ∝ r⁻² ⇒ v₀ = v_c CHECKED.
- v₀ = 238, 30.24 km s⁻¹ kpc⁻¹ × 8.275 kpc = 250.24, minus 12.2 → 238.0: CHECKED (Baxter Sect. 3.1.5, PDF p.12). v_esc 544, medians 485–580: Table 2 / Sect. 3.1.2 (PDF p.12) CHECKED.
- (1.2-nesc): sympy CHECKED; = Griffin Eq. (15) (PDF p.14) CHECKED. Galactic axes (r inward, φ rotation): Baxter Eq. (11) text (PDF p.10), Green Sect. 5 CHECKED.
- (1.2-vsun) (11.1, 250.2, 7.3): CHECKED (Baxter Table 1, Eq. (14), PDF p.11). |v_⊙| = 250.5525 km s⁻¹: WRONG rounding — one decimal is **250.6**
  (v_max 794.6, NOTATION rows v_⊙, v_E^ref, v_max). Effect 2×10⁻⁴, below every quoted digit except these; either change to 250.6/794.6 or write
  "250.55" once and say the book uses 250.5. All derived numbers below were recomputed with both and are insensitive.
- Unit Jacobian, ⟨v⟩ = −v_E, Galilean: CHECKED. rms 291.5 (Gaussian) and 284.2 (cut) CHECKED. Direction fractions (MC, 4×10⁶): 93.5 % ("94 %"),
  59.0 %, mean cosine 0.657: CHECKED.
- (1.2-vmax) 794.5 = 2.650×10⁻³ CHECKED (see rounding). Annual range 781.4–810.4 CHECKED; annual mean |v_E| = 252.11 CHECKED.
- F_χ angular integral and both branches of (1.2-Fspeed): sympy CHECKED (both branches exactly); continuity at v_esc − v_E CHECKED; v_E/v_esc ≤ 0.49 CHECKED.
  Peak 334.7 → "335" CHECKED. Tail fractions 35.9 / 14.9 / 4.16 / 0.579 / 0.098 % ("36, 15, 4.2, 0.58, 0.10") CHECKED.
- WE N_esc: 2.2857, erf = 0.99877, e^{−5.2245} = 0.005383, 2.5792×0.005383 = 0.01388, bracket 0.98489, π^{3/2}v₀³ = 7.507×10⁷, N_esc = 7.393×10⁷: CHECKED.
- (1.2-inv): derivation CHECKED (sympy, η branch (i) at v_min = 0); 364.21 − 2.70 = 361.51, prefactor 9.608×10⁻⁶, 3.474×10⁻³ = 1/287.9, 1041 (natural): CHECKED;
  no-cut 1/290.1, +0.8 %: CHECKED; June/Dec 1/298.3, 1/279.8, 6.6 % ("6 %") CHECKED; quadrature agrees to 10⁻¹⁵ CHECKED.
- (1.2-vorb) = Baxter Eq. (11) (PDF p.10), ω = 0.0172 d⁻¹, Δt from 22 March CHECKED; 29.8 = Baxter Eq. (13) (p.11) CHECKED; norms 1.00004/1.00004, dot 6.5×10⁻⁵ CHECKED.
  McCabe Table I (PDF p.4): e = 0 shifts peak 1.17 d, amplitude 0.39 % → "1.2 days, 0.4 %" CHECKED.
- (1.2-annual): v̂_⊙ = (0.0443, 0.9986, 0.0291), projections 0.1528/0.4664, 0.4908, 14.63, 71.86°, 72.9 d = 2 June, 60.6°: CHECKED. Second-order term
  (formula as written) 1.35 at both extremes, 1.56 mean ("1.3", "1.6") CHECKED. Exact max 266.45 (2 June), min 237.35 (2 Dec), mean 252.11 CHECKED.
- Curve crossing 363.7 ("364") CHECKED. η phase reversal 210.9 ("211"), 0.886 v₀ vs Green Sect. 5.2 x_p = 0.89 (PDF p.11) CHECKED.
  η June/Dec ratios: 600: 1.214/0.844 ("+21 %, −16 %") CHECKED; 700: 1.424/0.719 CHECKED. Yearly-average of ⟨1/v⟩: −0.33 %, equal to annual-mean value to 7×10⁻⁵
  CHECKED; η yearly average +2.6 % (600), +5.6 % (700) CHECKED.
- dI/dv_E = 0.6495 ("0.6498"), ∂ln⟨1/v⟩/∂v_E = −2.1947×10⁻³ (numerical derivative agrees), amplitude −3.20 % CHECKED.
- Modulation-test ¶ in 1.5 uses these: see E.
- Daily: rotation 0.465 km s⁻¹, 3.2 % of 14.6 CHECKED. McCabe (B3) angles (α_GP, δ_GP) = (192.85948°, 27.12825°), l_CP = 122.932° (PDF p.6) CHECKED;
  rotation rebuilt (Galactic centre lands at RA 266.40°, Dec −28.94°). NCP = (−0.4838, 0.7470, 0.4560), dot 0.7378, θ_E = 42.46° ("42.5") CHECKED;
  Griffin Sect. II D, Fig. 4 "θ_e ≈ 42°" (PDF p.14) CHECKED. Equatorial (0.4657, −0.4887, 0.7378), RA 20.91 h, Dec 47.54° CHECKED; June/Dec Dec 42.8°/52.6° CHECKED.
- (1.2-angle), (1.2-local): rederived (dot products of the stated unit vectors) CHECKED. 45°N: 2.5°–87.5°; (0, 0.04, 1.00); (−0.675, 0.522, 0.522), 31.3°, NW CHECKED.
  Equatorial-plane axis 47.5°–132.5°, sin²θ_E = 0.456 CHECKED. Griffin Sect. III C sapphire/GaAs, sidereal argument (PDF p.20) CHECKED.
- (1.2-flux), (1.2-vmean): I₃ and edge algebra sympy CHECKED; I₁ − I₂ closed form CHECKED numerically to 15 digits (sympy could not close it symbolically;
  the 4v_E y / odd-term split is correct by inspection); v_E → 0 limit 2v₀/√π (sympy) CHECKED; no-cut form CHECKED.
  WE: terms 4.685×10⁶, 3.3170×10⁷ (3.3182 with v_E = 250.55), −1.0075×10⁶; ⟨v⟩ = 354.1; no cut 358.2–358.3; Φ = 1.06×10⁸; 3.35×10¹⁵ yr⁻¹; 429 cm³, 7.54 cm,
  1290 ("1300"): CHECKED. Focusing 2.50 and 0.177 km s⁻¹ CHECKED; Green Sect. 5 footnote b CHECKED.
- Halo sensitivity: v₀ ± 6 → ⟨1/v⟩ ∓0.95 %, η(600) × 1.109/0.893; v_esc ± 25 → ⟨1/v⟩ −0.27/+0.38 %, η(600) × 1.059/0.920, η(760) × 2.26/0.101: CHECKED.

## D. Section 1.3
- (1.3-elastic), (1.3-ERmax), (1.3-omegaq), (1.3-vmin), (1.3-omegamax), q* = (2m_χω)^{1/2}, v_min,min = (2ω/m_χ)^{1/2}, limit-box v_min = q/2μ_χN: all sympy
  CHECKED; dims CHECKED; free-particle bound ½μv² = Essig 2016 Eq. (3.4) (PDF p.12) CHECKED; Eq. (3.2) CHECKED; Lin Eqs. (75)–(78) (PDF p.45–46),
  (116)–(119) (PDF p.60–61), (103) (p.53) CHECKED; Kahn–Lin Eqs. (9), (10) (PDF p.7–8) CHECKED. αm_e v = 3.7 eV ("≈4 eV") CHECKED.
- Exothermic band |Δ_χ| ± qv − q²/2m_χ CHECKED. m ≪ M: (4m/M)·½mv² CHECKED.
- (1.3-mmin): v_max² = 7.024×10⁻⁶; 1 eV → 0.285 MeV, 1 meV → 0.285 keV CHECKED. v_esc ± 25: v_max 3.1 %, m_min +6.6/−6.0 % (mean 6.3) CHECKED.
  "Over the year m_min by ∓3.6 %": actual −3.9 % (June, 810.4) / +3.4 % (Dec, 781.4) → WRONG(minor): write "by −3.9 % and +3.4 %".
- WE m_min: 0.316 MeV, q = 0.838 keV ("0.84"), 30 meV → 8.54 keV, q = 22.6 eV, ratio 37 CHECKED.
- (1.3-region), parabola, q ≥ ω/v_max (Kahn–Lin Eq. (122), PDF p.47) CHECKED; ω/q < 3×10⁻³ CHECKED.
- Table 1-kinematics: all 15 entries CHECKED (0.530/5.30/53.0/530 keV, 5.30 MeV; 0.351/3.51/35.1/351 eV, 3.51 keV; 5.39 µeV, 0.539 meV, 53.9 meV, 5.35 eV, 0.500 keV).
- Gap band: 1 MeV 0.459–4.84 keV, 10 MeV 0.422–52.6 keV CHECKED; free Si reaches 1.11 eV at 45.5 MeV ("≳45") CHECKED.
- (1.3-q0) 3.7289 keV CHECKED (Kahn–Lin Eq. (121), PDF p.46). 2m_χ v_max = q₀ at 0.704 MeV CHECKED (Kahn–Lin below Eq. (123): "m_χ/0.7 MeV", PDF p.47).
  0.42 keV = 0.112 q₀ CHECKED (Eq. (123)). 2m_χ v_max = 2π/a at 0.43 MeV ("about 0.4") CHECKED.
- Sound speeds 3–10 km s⁻¹ = 1.0–3.3×10⁻⁵ (Kahn–Lin Eq. (50), PDF p.22) CHECKED; ω ≤ 2c_ν m_χ v (Eq. (93), PDF p.35) CHECKED; fraction 4c_ν/v CHECKED.
  60 meV "Sect. IV A" (PDF p.32) CHECKED; width ~(ω₀E_R)^{1/2} (Sect. IV A, PDF p.34) CHECKED. 4m/M = 1.53×10⁻² CHECKED.
- WE nuclear: μ = 0.9630, q = 5.104 MeV, E_R = 0.4999 keV, 3.51 keV, 0.1424, Xe 0.113 keV CHECKED. "M = 26.06 GeV ... nuclear mass of ²⁸Si" (also §1.4):
  26.0603 GeV is the *atomic* mass; nuclear 26.0531 → GAP(cosmetic): say "atomic mass" or use 26.05 (no number changes at the stated digits).
- η angular average (1/2qv)Θ CHECKED; measure ∫d³q/(2π)³ η/2q = ∫q dq/(4π²) η CHECKED; = Kahn–Lin Eq. (11) (PDF p.8) CHECKED; Kahn–Lin (12) CHECKED;
  Essig 2012 below Eq. (5) (PDF p.3) CHECKED; Lin Eq. (103) g(v_min) CHECKED.
- (1.3-eta-shm) and branch (ii) = (D.1-eta1/2): sympy CHECKED (both exactly); quadrature agrees to 10⁻¹⁵ CHECKED.
- WRONG cite (Essig 2016 numbering, mixed schemes): §1.3 "Eqs. (43)–(46)" and "Eq. (45)" are ar5iv sequential numbers; the paper's own numbers are
  **(A.12)–(A.15)** and **(A.14)** (PDF p.34). The SHM branches, cited as "(67) and (68)" in §1.3 and "(66) and (68)" in D.1 (the two disagree), are
  **Eqs. (B.4) and (B.5)** (PDF p.39; ar5iv puts both under (68), (66) is K, (67) the integral). Use the (x.y) scheme everywhere, as for (3.13), (5.1)–(5.4).
- Fig 1-eta / text numbers: η(0)/η(200) = 1.410 ("within a factor of 1.4") → GAP(minor): "1.41"; 300→700: 1.530×10⁻³ → 7.96×10⁻⁶, factor 192 CHECKED;
  293.5 CHECKED; η(0) = 1041, η(600) = 19.2, η(700) = 2.38 CHECKED. June/Dec ratios: 700 1.42/0.72 CHECKED; 760 2.22/**0.373** (text 0.38) → WRONG(minor): 0.37;
  780 4.56/0.0085 ("4.5, 0.009") CHECKED.
- (1.3-edge): series and integration sympy CHECKED; scale 172.7 ("173") CHECKED. δ = 34.5/14.5: quadratic 0.814/0.919 ("0.81, 0.92") CHECKED; with correction
  0.977/**0.996** (text "0.98 and 0.99") → WRONG(minor): "0.98 and 1.00". Caption: within 10 % above 720 (0.908) CHECKED; "within 5 % above 740": 0.947 at 740,
  5 % point at 742 → WRONG(minor): "above 745" or "within 6 % above 740".
- Mass edge expansion CHECKED; 1 % above m_min → 3.97 km s⁻¹ CHECKED. η recovery 2.82×10⁻⁴, 1.92×10⁻³, 1.06 %, 13.6 %, 84.7 % CHECKED; 4.2 % above 600 CHECKED.
- δln m_min = δln E_th − 2δln v_max CHECKED.

## E. Section 1.4 and App. C.9
- C.9 (C.9-KG), (C.9-Proca) incl. ∂L/∂(∂_μA'_ν) = −F'^{μν}, Lorenz condition, ∇·E = J⁰: CHECKED. (C.9-static), (C.9-Gq) CHECKED. Contour: angular factor
  4π sin(qr)/qr, 1/(2π²r) → 1/(4π²r) Im∫, residue e^{−mr}/2, (C.9-Gx) CHECKED; ∇²G = m²G, −∇²(1/4πr) = δ³ CHECKED; hydrogen −α/r CHECKED.
- Energies: H_s = −½ρGρ, H_v = +½JGJ, cross terms ±y_χy_e G, test-particle check (−L_int = +y_eA'⁰): CHECKED (scalar attractive, vector repulsive).
- Kinetic mixing: sympy expansion, cross terms cancel, −¼(1−ζ²)F'² CHECKED; sign of mixing term = Lin Eq. (70) (+κ/2, PDF p.39) CHECKED; Hochberg 2017
  Eq. (5) has −κ/2 (PDF p.4) — consistent with "other papers use the opposite sign" CHECKED. Lin (71) millicharge basis, (72) dark-photon basis CHECKED.
  y_e = −ζe for the electron CHECKED against NOTATION (e > 0, electron −e).
- Static limit: neglected term < v_max² = 7×10⁻⁶ CHECKED. Born amplitude −(μ/2π)Ṽ ⇒ σ = μ²|Ṽ|²/π CHECKED.
- (1.4-yukawa), (1.4-Vq): sign/convention consistent with Ṽ = ∫e^{+iq·x}V (NOTATION) CHECKED; dims eV⁻² CHECKED. Knapen Eq. (7) NR reduction (PDF p.2) CHECKED.
- (1.4-defs), (1.4-Vsq), (1.4-yukawa-sigma): CHECKED; = Knapen Eqs. (11), (12) (PDF p.3) CHECKED; Essig 2012 Eqs. (3), (4) (PDF p.3) CHECKED.
- Limit box: heavy/light forms and both leading corrections sympy CHECKED; Essig 2012 Eq. (15) (PDF p.6) CHECKED; 0.53 MeV at 100 MeV ("0.5") CHECKED.
- (1.4-darkphoton) CHECKED (= Lin Eq. (74), = Essig 2012 display above (15) with g_D² = 4πα_D). WE: μ = 0.4862, μ² = 0.2363, 4α = 0.02919, 6.209×10⁻¹²,
  8.10×10⁵, 7.665×10⁻¹⁸ MeV⁻², 2.985×10⁻³⁹ cm²; factor 566 ("570"); 1.545×10⁻⁸ CHECKED. Freeze-in μ = 0.3382, 6.05×10⁻³⁸ CHECKED. See A.2 for Lin's 10⁻³⁷.
- ζ_eff: Hochberg 2017 Eq. (6) (PDF p.4) CHECKED; screening 1/|ε|² inside S: Knapen Eqs. (6), (8) (PDF p.2) CHECKED.
- Nuclei: σ_p = μ²y²y²/(πm_V⁴) ↔ Lin Eq. (99) (PDF p.52) CHECKED; (1.4-sigmaN) and Z + (A−Z)y_n/y_p ↔ Lin Eq. (104) (PDF p.53, normalized to b_n there;
  equivalent) CHECKED. 1/R = 39.5 MeV CHECKED. μ_χp 90.37, μ_χN 99.62, 1.2152, 953 ("950"); 1 GeV: 3.958, 3103 ("3100") CHECKED.
  "q ≤ 2m_χv_max ≲ 5 MeV for m_χ ≤ 1 GeV": 2m_χv_max = 5.30 MeV (the true nuclear maximum 2μv = 5.10) → GAP(minor): "≲ 5 MeV" → "≈ 5 MeV".
- (1.4-absorption) CHECKED; m_φ ≥ E_g vs 2E_g/v_max² ≈ 0.3 MeV CHECKED.
- (1.4-dp-abs) = Hochberg 2017 Eq. (7) (PDF p.4) CHECKED; dims (eV⁻⁴·eV³·eV = 1) CHECKED.
- ALP/scalar NR Lagrangians (1.4-alp), (1.4-scalar) = Mitridate Eq. (18) (PDF p.8) term by term, incl. ↔∇² definition CHECKED; dims eV⁴ CHECKED.
  −¼gφFF̃ = gφE·B with Graham Eqs. (2), (3) (FF̃ = −4E·B, PDF p.3) CHECKED; GAP: Graham (2), (3) do not contain the g_aee φψ̄iγ⁵ψ term (cite elsewhere).
  Mitridate Table I claims (spin-current ↔ σ_cond; scalar not fixed by σ_cond): not audited, GAP (unverified).

## F. Section 1.5
- Ramanathan Eq. (1) (PDF p.2) CHECKED; ε_eh 3.62–3.66 (300 K), 3.70–3.75 (5–123 K): Table I (PDF p.5) CHECKED — the paper labels it "TABLE I", book cites
  "Table~1" (×2 + Fig. 1-chain caption): cosmetic GAP. "well above 20 eV" not located in Sect. I: GAP (unverified). Data 3–8 eV then ≥ 50 eV (Scholze, PDF p.5) CHECKED.
- Fano 0.1–0.15: Essig 2016 Eq. (5.4) (PDF p.20) CHECKED. 27.0 pairs, spread 1.80, Poisson 5.20 CHECKED.
- (1.5-step) = Essig (5.1); E_g 1.11, ε 3.6 = (5.2) (PDF p.19) CHECKED; 5 eV → 2, 10 eV → 3 CHECKED; thresholds 1.11/4.71/8.31 eV → 0.316/1.341/2.366 MeV, factor 4.2 CHECKED.
- Skipper < 0.1 e⁻ (Kahn–Lin Sect. VII A, PDF p.76) CHECKED; (1.5-luke) = Kahn–Lin Eq. (195) (PDF p.77), 150 V CHECKED.
- Phonons: 15 mK ≈ 1.29 µeV ("1 µeV") CHECKED; 10.6 g, 3.86 eV, 16.3 eV (Sect. VII B, PDF p.78) CHECKED. Snowmass Sect. 3.3.1 TES/KID CHECKED.
- Photons: NaI 5.9, CsI 6.4, GaAs 1.52 eV (Sect. VII C, PDF p.79) CHECKED. "1.2 eV gap": WRONG (A.5).
- Al quasiparticles: see A.3. m_min(0.6 meV) = 0.171 keV CHECKED.
- (1.5-Nsig), (1.5-bins) CHECKED. Essig Fig. 7 peak at Q = 2 (PDF p.23) CHECKED.
- (1.5-rate) = Kahn–Lin Eq. (11) CHECKED; normalization q dq/(2π)² requires S with the 2π/V of Knapen Eq. (4) (PDF p.2) — consistent with Knapen Eq. (10)
  (rederived: ∫d³q/(2π)³ η/2q = ∫q dq/4π²). Ensure §4.2 defines S(q,ω) with that 2π (convention note for the editor). Dimensional check in text CHECKED.
- (1.5-FDMavg), (1.5-scaling), (1.5-heuristic), (1.5-limscaling): CHECKED (definitions/rearrangement).
- Poisson limit (sympy (1−N/K)^K → e^{−N}) CHECKED; N₉₀ = 2.3026, ln 20 = 2.9957, 3.8897 (1 event), 5.3223 (2 events) CHECKED; Mitridate 3 events at 95 %
  (Sects. IV–V, PDF p.20, 22) CHECKED. (1.5-limit) CHECKED; background √exposure scaling CHECKED.
- Modulation test: 2A/π = 0.1178, 0.236 N ≥ 2(2N)^{1/2} ⇒ N ≥ 143.6 ("144") CHECKED.
- Fig 1-exclusion (fig1_9.py re-run): heavy minimum 9.69 MeV, factor 46.1 at 1 MeV; light minimum 1.98 MeV, 1.42 at 1 MeV ("within 1.5"); large-m slopes 0.98/0.99
  CHECKED. Caption "cut off at q ≈ 2q₀" is a Gaussian e^{−q²/2(2q₀)²} in the script: fine for "≈".

## G. Appendix D.1
- (D.1-gauss) CHECKED. N_esc by parts CHECKED (sympy). Cut geometry and angular integral CHECKED (sympy). Branches (i)–(iii) CHECKED (sympy); continuity, vanishing at
  v_esc + v_E, dη/dv_min = −F/v_min, no-cut limit CHECKED. ⟨1/v⟩ CHECKED. ⟨v⟩: I₁ − I₂ (numerical 15 digits), I₃ = 2v_E e(v_esc² + v_E²/3) (sympy), assembly into
  (1.2-vmean) CHECKED; no-cut check and both limits CHECKED; quadrature to 10⁻⁶ CHECKED (I get 10⁻¹⁵).
- Line 50 signed sentence: see A.1. Line 52 cite "(66) and (68)": WRONG → Essig 2016 Eqs. (B.4) and (B.5).

## H. Convention drift against NOTATION
- No factor-of-2, π or sign drift found: Ṽ(q) = ∫e^{+iq·x}V, e² = 4πα with electron −e (y_e = −ζe), q from χ to target, ω to target, ω_q, η = ⟨Θ(v−v_min)/v⟩,
  F_DM, σ̄_e = μ²|Ṽ(q₀)|²/π (vacuum), m_min = 2E_th/v_max², Heaviside–Lorentz σ₁ all match NOTATION and C.9.
- First-use drift (NOTATION rows to update): Δ_BCS (listed 7.2, used §1.5); ρ_T (listed 1.5, used §1.4 Eq. (1.4-dp-abs)); σ₁ (listed 4.4, used §1.4).
  Symbols used in Ch. 1 with no NOTATION row: F_χ(v), ζ_eff, g_φee, x_fo, g_*, s₀, N_90, M_det, t_exp, ω_yr, ω_sid, θ_E (editor's call).
- v_⊙/v_E^ref/v_max rows: 250.5/794.5 rounding (C).

## I. Not verified (do not read as CHECKED)
CODATA a(Si) (not fetched); prose of Lin Sects. I A/I C/III C and Kahn–Lin Sect. III C; Ramanathan "well above 20 eV"; Mitridate Table I physics claims; all
non-equation cites not fetched: rubin1980, bertone2018, clowe2006, tremaine1979, lee1977 (incl. its 2 GeV), kolb1990, boehm2004, hall2010, holdom1986, lewin1996,
tuckersmith2001, fitzpatrick2013.
