# Chapter 5 mock-reader review: persona (a), first-year PhD student

Source: the built PDF (Nov 1 23:46) predates every ch05/appendix .tex edit (Nov 2), so I read the .tex sources:
ch05/s5-1 … s5-7, appD/D-13, D-14, D-15, appC/C-18. I read linearly and redid every derivation and every
number (pen and paper, sympy/numpy where faster). "I" below is the persona.

## 5.1 Born–Oppenheimer approximation
- **Lost points.** None blocking. The coupled equations (5.1-coupled/N) came out exactly when I projected on Ψ_j.
- **Could not reproduce.** Nothing. I checked κ_BO = 0.0665, κ²α²m_e = 0.120 eV, κa₀ = 0.0352 Å, ω_opt = (2·13.6/M)^½ = 63.7 meV,
  ℓ_zp = (M_κω)^{-½} = 0.048 Å, cubic/harmonic = |Φ³|ℓ/3Φ = 0.049, 2π/E_g = 3.5 fs, the period 64.5 fs, and the ratios against
  a and the bond (0.0091, 0.021). Power counting: derivative coupling (1/M)(1/a₀)(1/κa₀) = α²m_e κ³. Correct.
- **Used before defined.** "phonon density of states" and "4³ grid of phonon wavevectors" (fig caption, WE) come before 5.2.
  Same for "Ewald sum", "frozen-phonon", "Born effective charge", "Migdal's theorem", but these are labeled as forward references.
- **Pace.** Good. The hierarchy key result and WE 5-kappa are the best part: they show where the coefficients of order one go.
- **Outcomes.** (i) Derive the coupled equations and the BO limit: yes. (ii) Count orders in κ_BO: yes, for example
  the second-order derivative coupling (κ³)²/1 → κ⁶. (iii) Hellmann–Feynman and the derivative coupling (5.1-dcoup): yes,
  re-derived from ∂(HΨ_i = E_iΨ_i) projected on Ψ_j. (iv) Explain why ω/E_g, not κ², controls an insulator: yes (0.0548 = 12.4κ²).
- Typo: in the fig 5-scales caption, panel (b) says "(gray dashed)" twice.

## 5.2 The harmonic crystal
- **Lost points.** (a) WE 5-debye says the isotropic model "of C.18", with c_LA² = C₁₁/ρ and c_TA² = C₄₄/ρ, gives c̄ = 6.35 km/s
  and Θ_D = 697 K. That is true with the cubic C₁₁, C₄₄. But C.18's "isotropic convention" uses C₁₂ = 52.4 and C₄₄ = 68 GPa
  (so c = 9.0 and 5.4 km/s), and those values give c̄ = 5.98 km/s and Θ_D ≈ 655 K. Following the cross-reference, I could
  not tell which model is meant. Fix: say "with the cubic C₁₁, C₄₄", or quote the C.18 numbers.
  (b) The sentence "ρ_TΛ is the Christoffel matrix of the relaxed elastic constants" is asserted, not shown. I accept it, but
  "relaxed" is defined only through the internal-relaxation remark that comes later in the paragraph.
- **Could not reproduce.** Nothing. I verified the diatomic chain end to end: the force constants, D(Q), the quartic in ω², c, the
  folded equal-mass chain, K = 6.90 eV/Å², ω_X = 45.3 meV, c_LA = aω/8 = 6.61 km/s, the GaAs gap of 3.7%. Also the T^{αβγ}
  antisymmetry/symmetry argument (including the τ-term via the transposed ASR), the low-ω DOS, g_D, Q_D = 1.435 Å⁻¹,
  ω_D = 55.6 meV, Θ_D = 645 K, the [110]/[111] Christoffel speeds, and the direction averages (9.00, 5.66, 5.04 km/s → c̄ = 5.89 km/s,
  LA share 9.3%; my own Monte Carlo agrees).
- **Used before defined.** "Goldstone modes" (fine to skip). "Grüneisen parameter" is defined inline, but before Sec. 5.7 explains
  why it exists. "Tetrahedron integration" (caption) is not defined.
- **Pace.** The second-order sound-speed formula (D₂ plus D₁ through the optical modes) goes too fast: I can follow it as
  degenerate perturbation theory, but one more line showing that the acoustic block of D₁ vanishes before going to second order would help.
  The diatomic chain is ideal.
- **Outcomes.** Build D(Q) from force constants: yes (chain). ASR → three zero modes: yes. Sound speed from elastic constants:
  yes, c_TA[110] = √(50.85 GPa/2330) = 4.67 km/s. Debye model from c̄: yes. DOS/Van Hove peaks qualitatively: yes.
- Minor: TA DOS peak "near 18 meV" (intro, Summary) vs "at 17 meV" (DOS text).

## 5.3 Phonons
- **Lost points.** Table 5-phonons: the header says DFPT "300 K" and the caption says it uses "the PBE DOS of fig 5-si" (48³). The text
  gives 0.0495/0.0799 Å for that DOS at 293 K, and 0.050/0.081 Å for the 4³ grid. The table shows 0.049/0.081, a mix of the two.
  I could not tell which grid or temperature a row holds.
- **Could not reproduce.** Nothing. I checked the normal coordinates and their inverse, [u_Q, p_Q'] = iδ, the Heisenberg equations,
  [b, b†] = 1, the inverse ladder relations, the expansion of the bracket to ω(b†b + ½), and the crystal momentum of b†_Q.
  Numbers: zero-point energy 123 meV/cell, ℓ_opt = 0.024 Å, ℓ_TA(X) = 0.045 Å, 7×10⁻¹⁵ Å per kg, n_B = 0.091/0.95,
  q = 26 keV, ⟨u²⟩ Debye bracket (1.259, 2.088), 6.02×10⁻³ Å², 0.0448/0.0647 Å, T = 0.44Θ_D = 284 K, equipartition
  3.73×10⁻³ (×1.129 → 0.5%), and Ge: Θ_D = 373 K, 0.037/0.067 Å, thermal/zero-point = 2.35 ≈ "2.4".
- **Used before defined.** "Isotropic displacement parameter 8π²⟨u_x²⟩" is used once and is harmless. Notation: the symbol "zero-point
  length" now has a third meaning, ℓ_Qν = (2M_cell ω)^{-½}, after κa₀ (5.1, estimate) and (M_κω)^{-½} (fig 5-scales). The text
  reconciles the factor of two for the optical mode, and that helped, but the overloaded ℓ_zp/ℓ₀/ℓ_Qν costs a moment each time.
- **Pace.** Slightly slow: the single-oscillator ladder algebra (which the persona knows) is redone in full for normal modes. Acceptable,
  since the ±Q pairing is the new part.
- **Outcomes.** Quantize the modes and write (5.3-u): yes, I re-derived p_R as well. Emission/absorption weights: yes. Single-phonon
  amplitude with crystal-momentum δ and √N: yes. ⟨u_x²⟩ from g_ph and from Debye: yes (numbers above).

## 5.4 Phonons from first principles
- **Lost points.** (a) The cost scaling: the opening gives a supercell calculation as ∝ (atoms)² (216² ≈ 5×10⁴), then "ninth power of
  the range" implies ∝ (atoms)³. Presumably the k-point saving runs out at Γ-only, but I had to guess. (b) "the 2.6% mean
  difference between this functional and experiment (Sec. 5.2)": Sec. 5.2 never quotes 2.6%. (c) f_Hxc appears as a symbol only
  in prose. I took it to mean v_C + f_xc.
- **Could not reproduce.** WE 5-frozen: "The quartic correction is 0.02 eV Å⁻² at 0.03 Å, 0.15%, and Φ⁽⁴⁾ ≈ 90 eV Å⁻⁴". From
  13.62 (0.03 Å) and 13.64 (0.06 Å), Φ⁽⁴⁾(0.06² − 0.03²)/12 = 0.02 gives Φ⁽⁴⁾ ≈ 89, but then the correction *at* 0.03 Å is
  Φ⁽⁴⁾u²/12 ≈ 0.007 (0.05%). The 0.02 is the difference between the two steps. The rest checks: 2E/u² = 13.21/14.04,
  Φ⁽³⁾ = −41.5, symmetric 13.62, ω = 63.68 meV, the one-sided errors 1.5%/3% in ω, the Sternheimer projection argument
  (the occupied–occupied cancellation), the factor 4 in δn, the aliasing identity, the ⟨110⟩ distances (√19a/4 = 5.92 Å),
  and the un-repaired TA at 0.02(2π/a): √(0.829² + 0.675²) = 1.07 meV.
- **Used before defined.** "Kohn anomalies" (defined inline), "ionic plasma frequency", and "conjugate gradients" (fine).
- **Pace.** Too fast: the 2n+1 proof dismisses the orthonormality constraint in one sentence. I believe it, but cannot check it from the
  text. Pick–Cohen–Martin is stated, not derived from (5.4-hess); one line inserting δn = R δV_ext would close the gap.
- **Outcomes.** Central-difference force constants and aliasing: yes. Sternheimer equation without empty states: yes, re-derived.
  Read the D(Q) interpolation as un-aliasing: yes. ASR repair and its effect at meV: yes (numbers above). 2n+1: I can state it, but only
  half-prove it.

## 5.5 Polar crystals
- **Lost points.** None blocking. The Berry-phase paragraph is opaque at my level (Wannier centers, the quantum of P), but the text
  says correctly that Z* is free of the ambiguity, so I could skip it.
- **Could not reproduce.** Nothing. From (5.5-U) I got F and P, Q̂·D = 0 → (5.5-na), the reduced-mass equation, and (5.5-LOTO).
  Estimate 1.7×10⁻⁴ eV². LST from (5.5-eps). Numbers: 1.186 vs 1.169, ω_L = 36.61 meV, Ω = 5.831×10⁻⁹ eV⁻³,
  μ = 33.64 GeV, Z* = 2.108 (and 2.21 by the static route), the computed splitting 2.12 meV and 2.65 meV with the measured ε∞,
  z_ν = Z*ê/√μ, and polariton Q ≈ 0.1 eV.
- **Used before defined.** "dark photon" (I know it only loosely), "reststrahlen" (defined inline), "Fröhlich" (forward), and ε₀
  meaning the static dielectric constant (no clash in HL units, but it caught my eye).
- **Pace.** Good. The pole/zero argument is the clearest physics in the chapter.
- **Outcomes.** Define Z* two ways and the Maxwell relation: yes. ASR on Z* and why Si has none: yes. Derive LO–TO and LST: yes.
  Extract Z* from a measured splitting: yes, 2.11. Coupling to a uniform field and why only optical modes: yes.

## 5.6 Displacement correlations
- **Lost points.** "Its normalization is 2W_κ itself" (about P₁) confused me for a moment: P₁ is normalized to one, and the *prefactor*
  is 2W. Reword.
- **Could not reproduce.** Nothing. The product formula from BCH plus Bloch, the C(t) sum, the T-independent Im C, the slope
  −i/2M → mean energy E_R, P_n Poisson, and the D(α) shift with S = MωΔx²/2. I checked the overlap integral and the S·e^{-S} of
  the first replica, the Bessel generating function and its detailed balance, and these numbers: 2W = 0.063/0.164/0.153 (10 keV),
  1.573/4.10/3.81 (50 keV), Poisson 0.21/0.33/0.26/0.13/0.05, crossovers 40/26 keV, 56 keV for a single 60 meV oscillator,
  Debye 1.29/2.64, (111) DW loss 2.4%, S = 2 weights, room-T w₋₁ = 0.0207, w₁ = 0.249, and T = 0.91ω₀ for n_B = ½.
- **Used before defined.** "Wick's theorem" (D.11), "color centers / NV center" (fine), "Allen–Heine term" (forward).
- **Pace.** The Bloch-identity sketch in the main text is too terse to follow alone, but D.15 completes it and the pointer is there.
  Otherwise well paced.
- **Outcomes.** Compute 2W and the elastic weight for Si at given q, T: yes (above). Explain the Poisson phonon count and the f-sum
  mean E_R: yes. Franck–Condon/Huang–Rhys progression and anti-Stokes weights: yes.

## 5.7 Anharmonicity
- **Lost points.** (a) In the key result (5.7-gamma), the second term is described as "merging with −Q₁ν₁ into −Q₂ν₂", with
  Q₂ = −Q − Q₁. That does not conserve crystal momentum (Q − Q₁ ≠ −Q₂). Redoing it, I find that the vertex V(Qν, Q₁, Q₂) with
  Q₂ = −Q−Q₁ annihilates Q₁ν₁ and creates −Q₂ν₂. The formula's value is right after relabeling only Q₂; the sentence is not.
  (b) "anharmonic order n_A = 2" in the counting of Sec. 8.5 comes before n_A is defined, and I could not use it.
- **Could not reproduce.** Nothing else. I checked the decay matrix element (3! cancels), the occupation differences (1+n₁+n₂)δn and
  (n₁−n₂)δn, the factor ½ vs 1, 0.180 meV, 3.66 ps, 57 periods, n_B(ω/2) = 0.008/0.407, 2.63 cm⁻¹ (×2.01 → 2.92), 744 K,
  η = 0.049, 0.98 Å, η² = 2.4×10⁻³, the quartic ratio 1.3×10⁻³, κ_BO(H) = 0.153, and the SCHA variation.
- **Used before defined.** "Raman line" and cm⁻¹ (the conversion is given, fine), "phonon self-energy Π/bubble" (D.17, forward),
  "molecular dynamics", and "Gibbs–Bogoliubov inequality" (stated, not proved; acceptable).
- **Pace.** The SCHA derivation is the fastest passage in the chapter. "A Gaussian obeys the diffusion equation in its covariance"
  carries ∂⟨f⟩/∂C_cd = ½⟨∂_c∂_d f⟩ in one clause, and I needed to work it out separately. TDEP's Stein-lemma step likewise.
- **Outcomes.** Write H₃ in phonon operators: yes. Derive the linewidth and the Klemens law: yes. Estimate η_anh ~ κ_BO and the orders of
  γ, Δω: yes. Distinguish QHA/SCHA/TDEP by what each fits: yes, qualitatively.

## Appendix D.13
- All steps reproduced. N₀₀ ≥ 0, (D.13-dcoup), and the mixing estimate via 1/(Mℓ) = ωℓ all work. The solvable model: sympy gives
  ω² = (K/M)[1 − ε + (1 − K/k)ε² + …], with residuals 5.07e-5, 5.01e-7, 5.00e-9.
- **Lost point:** "The zero-point amplitude is the fraction κ_BO of a bond length" contradicts 5.1, whose WE stresses that the unit is
  a₀ and that the amplitude is 0.021 of the bond (bond = 4.4a₀). Replace "a bond length" with "a₀".
- Too slow: κ_BO, κ², κ³ and the 0.035 Å / 0.12 eV numbers are repeated verbatim from 5.1.

## Appendix D.14
- All steps reproduced: (D.14-na), LO–TO, LST, and the pole/zero interlacing (dε/dω² > 0 between poles). I also checked the Fröhlich
  reduction: g² = (e²ω_L/2Ω)(1/ε∞ − 1/ε₀)/Q² ✓, and V^L = eQ̂·ℰ/(iQ) ✓.
- Typo: "less than 10⁻⁴ of the zone, Dark-matter scattering" (comma should be a period).

## Appendix D.15
- All steps reproduced. The Hadamard shifts d → d + θη₂, d† → d† − θη₁, the trace cycling, F′ = θ⟨A²⟩F, and the bracket at
  T = ω_D = 4.11 (∫₀¹ = 0.778). Clear and the right length. "Quadruples the zero-point exponent" slightly overstates it: the thermal part adds
  3.1×, and the total is 4.1×.

## Appendix C.18
- All steps reproduced: B = 97.8 GPa, isotropy ratio 1.56, the Rayleigh bound 6.48 km/s (23% below 8.43), the quartic form in s_Q,
  impedances 19.6/17.0 ×10⁶, t = 0.995, 6.29–6.49 km/s for Al, 48°, and ½Zω²A².
- The isotropic-convention mismatch with WE 5-debye is listed under 5.2.

## Minor consistency notes (one line each)
- GaAs LO–TO "2.7 meV" (5.3) vs table values 33.6/36.4 (Δ = 2.8). Fine, since the unrounded values are 36.35 − 33.62 = 2.73.
- The Summary repeats "near 18 meV" for the TA peak, while the DOS text says 17 meV.

## Overall
I would keep reading, eagerly. Every derivation I attempted reproduced, often with a worked number to check against, and the chapter
builds one object (E^ad) into everything a later rate needs: D(Q), ℓ_Qν, B_κ, C(t), Z*, γ. The items above are local: one wrong
number in a worked example (Φ⁽⁴⁾ correction), one mislabeled sentence in a key result (merging term), one cross-reference that points at
different inputs (isotropic c̄), a table whose grid/temperature I could not pin down, one forward-defined symbol (n_A), and the
overloaded zero-point-length notation. None of them stops me from following later material. The fastest passages (2n+1 proof, SCHA,
second-order sound speed) are ones I can take on trust without losing the thread.

**Verdict: MINOR GAPS**
