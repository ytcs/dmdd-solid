# Chapter 5: mock-reader review, personas (b) and (c)

Source read: .tex (build/main.pdf, dated Nov 1 23:46, is older than every ch05 source), ch05/s5-1 to s5-7, appD/D-13, D-14, D-15, appC/C-18. Read linearly, Ch. 1–4 assumed.
Numerical checks were done in Python/sympy: Christoffel sphere averages, Debye integrals, Poisson and Bessel weights, Z* from the LO–TO splitting, the D.13 two-spring model, and about 120 other quoted numbers. Almost everything reproduces to the quoted digits. The exceptions are listed under "Steps I could not reproduce".

## Persona (b): particle physicist, knows QFT, no solid-state physics

### 5.1 Born–Oppenheimer
- **Lost points.** None blocking. "Ewald sum" and "SG15 norm-conserving pseudopotential, 50 Ry cutoff" (Fig. 5.1 caption) are used bare. That is fine in a caption, but a pointer to Sec. 3.5 or App. E would help.
- **Could not reproduce.** None. I checked κ_BO = 0.0665, the counting κ³/κ⁴/κ⁶, the mixing amplitude ωℓF/ΔE² (from (1/M)(F/ΔE)(1/ℓ)/ΔE with 1/M = ωℓ²), ω_opt = (2Φ/M)^{1/2} = 63.7 meV, ℓ_zp = (Mω)^{-1/2} = 0.048 Å, cubic/harmonic = 0.049, and 2π/E_g = 3.5 fs.
- **Used before defined.** None.
- **Pace.** Good. The power counting is the clearest version of it I have read.
- **Fig. 5.1 caption:** "Gray dashed: the estimate κ_BO a₀ (gray dashed)" repeats itself.
- **Outcomes.** Estimate the BO scales for a new crystal: yes. For Ge, κ = (7.55e-6)^{1/4} = 0.052, κ²·27.2 eV = 75 meV, against 37.6 meV measured (0.5κ², as for Si). State what clamped nuclei miss: yes.

### 5.2 Harmonic crystal
- **Lost points.** None. Rotational invariance is invoked for a crystal under Born–von Karman conditions, where rigid rotations are not symmetries. A footnote saying the argument assumes a finite free crystal would remove the doubt.
- **Could not reproduce.** None.
  - Chain determinant, small-Q limit, equal-mass folding, K = 6.90 eV/Å², ω_X = 45.3 meV, c_LA = aω/8 = 6.61 km/s, GaAs gap 3.7 %.
  - T^{αβγ} antisymmetric plus symmetric, hence zero.
  - All Christoffel speeds. Sphere averages 9.00/5.66/5.04, c̄ = 5.89 km/s, LA share 9.3 %, Q_D = 1.435 Å⁻¹, ω_D = 55.6 meV, Θ_D = 645 K / 512 K, isotropic c̄ = 6.35 km/s.
- **Minor inconsistency.** The optical mode is "15.40 THz, 0.8 % low" here, while 5.4 says the measurement is "0.7 % higher". 63.7 vs 64.1 meV is 0.6 %. Pick one number.
- **Pace.** The mass-weighting paragraph is slow for me but needed by persona (a). The Goldstone remark is welcome and correct.
- **Outcomes.** Build D(Q) for a chain and get the branches: yes. Get sound speeds from C_ij: yes. Compute Θ_D from elastic constants: yes (Ge from the table: 373 K reproduced).

### 5.3 Phonons
- **Lost points.** None.
- **Notation.** The convention is unusual for a field theorist. p_Q carries e^{+iQR}, so p_Q is conjugate to u_Q (in QFT language π_{-k}), and b uses p†. It is internally consistent. I checked [u,p], [b,b†] and u̇ = p†. One sentence flagging the difference from φ_k/π_{-k} would save QFT readers a few minutes.
- **Could not reproduce.** None.
  - ℓ = 0.024/0.045/0.086 Å, 7e-15 Å per mode in 1 kg, n_B = 0.091/0.95.
  - Debye bracket 2.088, √⟨u_x²⟩ = 0.0448/0.0647 Å, T = 0.44Θ_D = 284 K.
  - High-T series, Ge rms 0.037/0.067 Å, thermal/ZP = 2.35 for Ge.
- **Inconsistency.** Table 5.3, Si DFPT at 300 K, says 0.081 Å. The caption says this column is Eq. (5.3-u2) with the 48³ DOS, which the text gives as 0.0799 Å at 293 K (≈0.080 at 300 K). 0.081 is the 4³-grid number.
- **Three "zero-point lengths".** ℓ_zp of the bond coordinate (rms, (Mω)^{-1/2}), ℓ_Qν = (2M_cell ω)^{-1/2}, and ℓ_0 = (2μω)^{-1/2} in 5.6 are all called "zero-point length". The text does reconcile the factor 2 for the optical mode, which I appreciated, but a single sentence fixing the convention would help.
- **Outcomes.** Write u in phonon operators and get the emission/absorption matrix elements: yes. Compute ⟨u²⟩ in Debye: yes.

### 5.4 Phonons from first principles
- **Lost points (for me, as a non-DFT reader).**
  - The Pick–Cohen–Martin formula and the Sternheimer derivation are followable.
  - "Egg-box" style ASR violation is explained.
  - "Kohn anomalies" is defined inline. Good.
- **Could not reproduce.**
  1. WE 5-frozen: "The quartic correction is 0.02 eV Å⁻² at 0.03 Å, 0.15 %, and Φ⁽⁴⁾ ≈ 90 eV Å⁻⁴." The 0.02 is the *difference* between the u = 0.06 and u = 0.03 symmetric estimates (13.64 − 13.62). That difference gives Φ⁽⁴⁾·(0.0036 − 0.0009)/12 = 0.02, so Φ⁽⁴⁾ ≈ 89, which is consistent. But the correction *at* 0.03 Å is then Φ⁽⁴⁾u²/12 = 0.007 eV Å⁻² (0.05 %), not 0.02 (0.15 %). The 0.15 % figure belongs to neither step size; at 0.06 Å the correction is 0.027 (0.2 %).
  2. Cost scaling. The opening says a supercell costs N_cell² (N³ for the atoms, ÷N for the k-points). Later the cost of a complete set of force constants "grows as the ninth power of their range". With N ∝ L³ the first rule gives L⁶. L⁹ holds only once the k-point saving has saturated (Γ-only). Say which regime is meant.
  - Everything else reproduces: the energies 13.21/14.04/13.62, Φ⁽³⁾ = −41.5, ω = 63.68 meV, the ASR-shifted TA 1.07 vs 0.83 meV, and the ⟨110⟩ distances.
- **Prose.** "The 3³ grid … does not contain X, however, and puts … but the test points are within 1.2 meV": "however" and "but" in one sentence. Reword.
- **Outcomes.** Extract a force constant by symmetric finite differences: yes, and this check is what caught item 1. Explain aliasing and the grid ⇔ supercell equivalence: yes. Write the Sternheimer equation: yes.

### 5.5 Polar crystals
- **Lost points.** None. The Berry-phase paragraph is compressed, but it is marked as a pointer to App. E.
- **Could not reproduce.** None.
  - Z* = 2.108 from the splitting, 2.21 from ε₀, ratio 1.186 vs 1.169.
  - ω_L(LST) = 36.61 meV, splitting 2.65 meV with measured ε∞, estimate 1.7e-4 eV², polariton Q ≈ 0.11 eV.
  - D.14 LO–TO, ε(ω) second form, the interlacing argument, and the Fröhlich reduction to (e²ω_L/2Ω)(1/ε∞ − 1/ε₀).
- **Own field.** "Dark-photon absorption in GaAs peaks at the LO energy" is correct: in-medium mixing gives a rate ∝ Im(−1/ε) for m ≈ ω. Saying so in one clause would make the "which resonance" paragraph self-contained instead of deferring entirely to Ch. 11. The q ≳ 1 eV kinematic statement is right.
- **D.14 typo:** "less than 10⁻⁴ of the zone, Dark-matter scattering …": comma splice, capital D.
- **Outcomes.** Derive the nonanalytic term and the LST relation: yes. Get Z* from the measured splitting: yes.

### 5.6 Displacement correlations
- **Lost points.** None. Bloch identity, BCH product formula and Poisson counting are what I would write.
- **Confusing wording.** "P₁(ω) … normalized to one … Its normalization is 2W_κ itself." Two different normalizations sit in adjacent sentences. Say "the prefactor is 2W_κ because the value at t = 0 is q·B·q".
- **Could not reproduce.** None.
  - 2W = 0.063/0.164/1.57/4.10, the Poisson weights, crossover at 40/26 keV, 56 keV for the 60 meV oscillator, Debye 1.29/2.64.
  - DW for (111) 2.4 %, the first moment from the double commutator, the overlap integral, S = 2 weights.
  - Bessel weights at 300 K: w₋₁ = 0.0208, w₁ = 0.249, ratio 0.084.
- **D.15:** "At T = ω_D the bracket is 4.11: the thermal motion already quadruples the zero-point exponent." The total is 4.1×, so the thermal part is 3.1×. "Quadruples the exponent" is fine; "the thermal motion … quadruples" is not.
- **Pace.** BCH and Wick are slow for me. That is fine for persona (a).
- **Outcomes.** Compute elastic and n-phonon weights for given q and T: yes. Compute Franck–Condon weights and the Stokes shift: yes.

### 5.7 Anharmonicity
- **Lost points.** None.
- **Could not reproduce.** None. 1.45 cm⁻¹ = 0.180 meV = 3.66 ps, Klemens 1.016/1.814, η = 0.049, 3Φ₂/|Φ₃| = 0.98 Å, quartic ratio 1.3e-3, the occupation algebra of the linewidth (1 + n₁ + n₂, n₁ − n₂, the factor ½), and the SCHA stationarity.
- **Outcomes.** Write H₃ and the golden-rule width: yes. Estimate the anharmonic parameter: yes.

### App. C.18
- **Inconsistency, confusing.** "In the isotropic convention … ρc_LA² = C₁₁ and ρc_TA² = C₄₄, which for the silicon values above are 9.0 and 5.4 km/s."
  - With the values directly above (165.6, 79.5 GPa) these give 8.43 and 5.84 km/s.
  - 9.0/5.4 comes from the isotropic set C₁₂ = 52.4, C₄₄ = 68.0 (C₁₁ = 188.4) of the preceding paragraph.
  - Sec. 5.2 meanwhile cites "the isotropic model of App. C.18, which uses c_LA² = C₁₁/ρ and c_TA² = C₄₄/ρ", with measured C₁₁ and C₄₄, giving c̄ = 6.35 km/s, Θ_D = 697 K. The C.18 set would give c̄ = 5.98 km/s.
  - So there are two different "isotropic models" under one name. Name the constants explicitly in both places.
- Everything else reproduces: B = 97.8 GPa, the bound 6.48 km/s, Z_ac, t = 0.995, 48°.

### Persona (b) overall
I would keep reading, and with pleasure. The chapter is written for someone like me: every solid-state notion is built from mechanics I know, and the numbers check. None of the defects above blocks anything; two are real numerical slips (5.4 quartic, C.18 isotropic speeds). No condescension toward QFT; the field-theory asides (Goldstone, Wick, generating functions) are accurate.
**Verdict: MINOR GAPS.**

## Persona (c): condensed-matter theorist, knows DFT and many-body theory, no dark-matter physics

### 5.1
- **Own field.** The statements are accurate: LDA 5.401 / PBE 5.477 Å, Si ZPR of about 60 meV, Pulay forces, N₀₀ as the Born–Huang diagonal correction, and Migdal's small parameter ω/E_F.
- **D.13 wording.** "The zero-point amplitude is the fraction κ_BO of a bond length." It is a fraction of a₀; the bond is 4.4 a₀. WE 5-kappa makes exactly this point, so the appendix contradicts its own main text.
- **Dark-matter terms.** The 0.33 MeV / 18 keV bounds via 2ω/v_max² are understandable from Ch. 1. I can reproduce them with v_max ≈ 800 km/s, which is not restated here.
- **Lost points.** None.
- **Outcome.** The counting: yes.

### 5.2
- **Own field.** Correct. Mild condescension risk: the mass-weighting paragraph, the DOS definition, and the Debye model at textbook length. It is justified by persona (a) and does not read as patronising. The Debye-convention warning (one wavevector per atom vs per cell, 645 vs 512 K) is valuable even to me.
- **DM side.** "acoustic edge m^ac_min of Sec. 9.2" and "c/v_max ~ 10⁻²" are both clear forward references.
- **Outcome.** Yes.

### 5.3
- **Own field.** Correct. The "displacement field B_Qν" name collides with the "displacement field D" of electrostatics in 5.5. It is harmless but noticeable.
- **DM side.**
  - The single-phonon amplitude for e^{iq·X} is clear. Momentum conservation up to G and the N-scaling are well motivated.
  - The phrase "nuclear density n_κ(q) of Sec. 2.3" assumes I remember that DM couples through it.
  - "cryogenic detector … emission is the whole signal" is clear.
- **Outcome.** Yes.

### 5.4
- **Own field.**
  - DFPT, Sternheimer with projector and shift, 2n+1, the Gonze reference, aliasing ⇔ supercell, Wigner–Seitz assignment, long-range ⟨110⟩ IFCs in diamond, and ASR repair are all accurate.
  - ASR violation is attributed solely to the XC real-space grid. In practice incomplete convergence (cutoff, k-sampling) also contributes. I would write "chiefly".
  - The supercell cost statement: see (b), item 2.
- **Not condescending.** It is pitched at the right depth for me, slightly fast for persona (a) in the PCM paragraph.
- **DM side.** "An acoustic-phonon search with a meV threshold samples exactly the region the unrepaired constants get wrong" is a good motivation, understood.
- **Outcome.** Yes, including spotting the WE quartic inconsistency.

### 5.5
- **Own field.**
  - Born-charge convention (index order, transpose in Baroni) and the Maxwell relation are correct.
  - The GaAs PBE numbers are plausible: ε∞ = 13.7 from the 0.57 eV gap, Z* = 2.09, a_PBE = 5.746 Å.
  - Converging the Z* sum rule with k-mesh is a nice practical test.
- **DM side.**
  - "A dark photon, or a dark-matter particle that couples to charge through a light dark photon" is understandable from Ch. 1.
  - "in-medium mixing" is used without even a one-line gloss. I do not know what it does to the field the crystal sees, and the paragraph defers the answer to Ch. 11.
  - **This is my one genuine lost point.** The claim that absorption peaks at ω_L rather than ω_T follows from the preceding sentence only if I accept that the dark photon "fixes the source of D". One sentence would close it: the effective in-medium coupling of a non-relativistic dark photon is screened by 1/ε, so the rate ∝ Im(−1/ε), which peaks at ω_L.
  - "A boson of mass m from the halo moving at v ~ 10⁻³ deposits ω ≈ m" is clear.
- **Outcome.** Yes, except the dark-photon claim, which I must take on trust.

### 5.6
- **Own field.** Correct. The DW naming caveat (Allen–Heine vs Debye–Waller) is appreciated. Huang–Rhys, the Stokes shift as 2Sω, and the Bessel line shape are all standard and right.
- **DM side.** "free recoil of the standard nuclear-recoil rate (Sec. 11.4)" and the 10/50 keV examples are well chosen: I now see why the multiphonon crossover sits at ~40 keV for cold Si.
- **Outcome.** Yes.

### 5.7
- **Own field.**
  - Maradudin–Fein form, the Klemens law and its failure in Si (TA+TA closed, LA+TA dominant, 94.3/5.7 % from Debernardi) are all correct.
  - The SCHA derivation via Gibbs–Bogoliubov and Gaussian diffusion is correct and compact. TDEP = SCHA curvature for Gaussian sampling (Stein's lemma) is correct.
  - **Precision issue.** "in the language of the phonon self-energy of App. D.17 it is −Im Π/ω". This depends on Π's normalization (Π in ω² units vs ω units). Fine if D.17 matches, but the statement should name the convention.
- **DM side.** Down-conversion to the sensors (Sec. 20.2) is understood.
- **Outcome.** Yes.

### Persona (c) overall
In my own field I found no physics errors, only the numerical slips listed under (b) and the D.13 "bond length" wording. On the dark-matter side, everything except the dark-photon screening claim in 5.5 is followable from Ch. 1 and the inline glosses. I would keep reading; the chapter is a cleaner treatment of lattice dynamics than most CM texts, and its DM hooks are concrete.
**Verdict: MINOR GAPS.**

## Fix list (priority order)
1. s5-4 WE frozen: the quartic correction at 0.03 Å is ≈0.007 eV Å⁻² (0.05 %), not 0.02 (0.15 %). Or rephrase: "the two step sizes differ by 0.02".
2. C-18 l.62: "for the silicon values above are 9.0 and 5.4" is wrong for the values above. Reconcile with s5-2 WE debye ("isotropic model of App. C.18" → c̄ = 6.35).
3. s5-5: add one clause on why dark-photon absorption sees Im(−1/ε) (peak at ω_L).
4. s5-4 intro vs Sect. "Frozen phonons": N² vs "ninth power of range". State the regime.
5. Table 5.3: Si DFPT 300 K 0.081 vs text 0.0799 (48³ DOS).
6. s5-2 "0.8 % low" vs s5-4 "0.7 % higher" (actual 0.6–0.7 %).
7. D-13 "fraction κ_BO of a bond length" → "of a₀".
8. Small fixes:
   - D-14 comma splice "zone, Dark-matter".
   - Fig 5.1 caption duplicated "(gray dashed)".
   - D-15 "thermal motion already quadruples".
   - s5-6 P₁ "normalization" wording.
   - s5-4 "however … but".
9. Optional:
   - One line on the p_Q convention vs QFT's π_{−k}.
   - One line on rotational invariance under BvK.
   - "chiefly" for the cause of ASR violation.
   - Name the Π convention in s5-7.
