# Chapter 1 mock-reader review: persona (a), isolated
Reader: first-year PhD student, undergraduate QM/EM/stat mech/SR, no grad solid state, no QFT, no astrophysics beyond textbook.
Read: tex/ch01/s1-1..s1-5, appC/C-9, appD/D-1, plus built main.pdf (rendering, cross-refs). Nothing else.
Method: linear read; every derivation redone by hand, numbers re-run in numpy/scipy (I needed scipy for erf values, the halo
integrals, the Monte Carlo wind fractions and the rotation matrix; I did the algebra of the derivations myself).
Format: `location | issue | fix`. Equation numbers are those of the built PDF.

## Global
- PDF | 63 unresolved `??` in Chapter 1 and 7 in the appendices. The ones I missed as a reader: halo conventions (A.8, three times),
  natural units/hbar c (A.1), Fourier convention (A.3, needed for Eq. 1.37), sign convention for q (A.4), erf (C.8), rate
  derivation (§2.2), reciprocal lattice (§3.1), thermal weights (§2.5). | Expected while later chapters are missing; the A.1/A.3/A.4/A.8/C.8 ones matter now because Ch.1 depends on them.
- PDF | The appendix cited as C.9 in the brief prints as "C.1" in the build and the text says "Appendix C.1"; it is consistent within the PDF. | Note only.
- Numerics | Every number I re-ran matches to the quoted precision, with rounding-level slips: dI/dv_E 0.6498 (I get 0.6495);
  η(760) December ratio 0.38 (0.372); η(780) December 0.009 (0.0084); "94 %" wind fraction (my MC 93.5 %). None matters.

## §1.1 Evidence for dark matter
Lost points
- Freeze-out paragraph | The x_fo equation contains ⟨σv⟩, which is what the paragraph then solves for, and g_* is not given at 1 GeV.
  With ⟨σv⟩ = 2e-9 GeV^-2 I get x_fo = 25.4 (100 GeV, g_*=80) and 20.7–21.7 at 1 GeV (g_* = 80…10.75), not "20". | Say "iterate
  together with Eq. 1.6" or "insert the result" and state g_* at each mass.
- Freeze-out | "n_χ/s constant" (comoving entropy conservation) is used without a sentence on why. | One clause: adiabatic expansion conserves S = s a^3.
- Lee–Weinberg | "⟨σv⟩ ∝ m_χ²/m_med⁴" is asserted. | Half a line: G_F-like coupling squared times m_χ² by dimensions.
Steps reproduced: Eq. 1.1, 1.2 (0.530 GeV/cm³ ✓), ρ_crit 1.052e-5 h² ✓, mean density 1.26e-6 ✓, 9.68e-48 GeV⁴ ✓, s_0 = 2890 cm^-3 ✓,
1.66 = (8π³/90)^{1/2} ✓, the x_fo log equation ✓, Eq. 1.6 prefactor (my derivation gives the same 45·1.66/2π²) → 1.99e-9 GeV^-2 =
2.3e-26 cm³/s ✓ ("≈2e-26" is fine), GeV^-2 → cm³/s 1.167e-17 ✓.
Used before defined: "Pauli limit" for phase-space density (Tremaine–Gunn), only cited; g_deg (defined implicitly by use).
Too slow/fast: The freeze-out paragraph is the densest in the chapter (H, n_eq, s, x_fo, s_0 all in one paragraph). Rotation curves are the right pace.
Outcomes (inferred): (i) estimate ρ_local from a flat curve: for v_c = 238 km/s I get 0.62 GeV/cm³ ✓ can do. (ii) explain why
keV–GeV fits solids: yes. (iii) reproduce the thermal ⟨σv⟩: yes, once I fixed x_fo by hand.

## §1.2 The local halo
Lost points
- Daily modulation | RA, declination, local sidereal time, hour angle and "meridian plane" are never defined. The equatorial components
  (0.4657, −0.4887, 0.7378) need the full eq→gal rotation, but the text gives only its third column and three angles. I built the
  matrix myself (checked: Galactic centre comes out at RA 266.4°, dec −28.9°) and reproduced 20.9 h / 47.5°; a typical reader could not. | Print the 3×3
  matrix (or the two missing columns), and define RA/dec/hour angle in one sentence each.
- Daily modulation | "uniaxial crystal, optic axis" are used without explanation (a reader from a particle background will not know them). | Gloss: a crystal with one axis different from the other two.
- Jeans equilibrium | A one-line import of hydrostatic equilibrium for a collisionless gas; I accepted it but could not justify it. | One sentence: the velocity variance acts as a pressure (from the Jeans equation, the first moment of the collisionless Boltzmann equation).
Steps reproduced: Jeans step v_0 = v_c ✓; N_esc bracket 0.98489, 7.393e7 ✓; normalisation of F_χ = 1 ✓ (numerical);
Eq. 1.15 ✓ (cos-integral and completing squares); ⟨1/v⟩ = 1/287.9 km/s, 1041 natural, no-cut 1/290.2 ✓; June/Dec 1/298.3, 1/279.8 ✓;
v_rms 291/284 ✓; tail fractions 36/15/4.2/0.58/0.10 % ✓; peak 334.7 ✓; crossing 363.7 ✓; ⟨v⟩ 354.1 (formula = quadrature) ✓, no-cut
358.3 ✓; flux 1.06e8 cm^-2 s^-1, 3.4e15/yr, 1290 per kg Si ✓; orbit unit vectors, projections 0.1528/0.4664, amplitude 14.6, t_peak
72.9 d ✓; extremes 266.4/237.4, mean 252.1 ✓; 2nd-order 1.35/1.56 km/s ✓; −3.2 % modulation of ⟨1/v⟩ ✓; phase flip 210.9 km/s ✓;
η(600/700) June/Dec ratios 1.214/0.844, 1.422/0.718 ✓; yearly-average +2.6/+5.6 % ✓; θ_E 42.46° ✓; June/Dec dec 42.8/52.6 ✓;
(east,north,up) at 45°N ✓; sin²θ_E 0.456 ✓; halo sensitivity factors 1.11/0.89, 1.06/0.92, 2.26/0.10 ✓; rotation 0.465 km/s ✓.
Could not reproduce without help: equatorial vector (above); the "94 %, 59 %, 0.66" wind statistics (needs MC; I got 93.5/59.0/0.657).
Used before defined: η(v_min) in §1.2 text (forward-pointed to §1.3, acceptable); "local standard of rest" (glossed adequately).
Too slow/fast: Annual-modulation paragraph on the reference convention vs yearly mean is long and repeats itself (it appears in §1.2 twice and
again in §1.3). Daily modulation is too fast on coordinates and slow on the uniaxial argument.
Outcomes: (i) compute N_esc, ⟨1/v⟩, ⟨v⟩: yes (did it). (ii) find the annual phase and amplitude: yes. (iii) predict θ_lab(t) for a
given lab axis: only after building the rotation matrix myself → partial.

## §1.3 Kinematics of slow dark matter
Lost points
- Free-particle bound below Eq. 1.28 | "A free particle of mass M cannot… the bound becomes ½μv²". If "energy" means recoil, the
  maximum is 2μ²v²/M (Eq. 1.25), which for M = m_χ equals ½m_χv², not ½μv² = ¼m_χv². ½μv² is the maximum *internal* excitation
  of a free target that also recoils. I stopped here. | Say "the most energy that can go into an internal excitation of a free target".
- Bound-electron paragraph | q ≈ μ_χe α and ω ≈ α m_e v are asserted (cited to Lin), and "ω_q would be negative" for m_χ < m_e needs
  α/2 > v, which is unstated. | Two lines: the electron momentum p ~ α m_e sets q; ω ~ q·v_DM; show the sign check.
- §1.3-edge, mass edge | "the whole of that range is set by particles faster than 600 km/s". At 2 m_min = 0.64 MeV,
  v_min = (2E_g/m_χ)^{1/2} = 558 km/s; 600 km/s corresponds to 0.55 MeV (factor 1.75). | "faster than about 560 km/s" or "the first 75 %".
- Table 1.2 caption | "The third column is also the threshold for which m_min = m_χ": counting as the caption lists them, the third is
  the Si recoil; the intended column is ½m_χ v_max². | Name the column.
- Text after Table 1.2 | "Table 1.2 gives 2m_χv_max = q_0 at m_χ = 0.70 MeV", but 0.70 MeV is not a row. | "From Table 1.2, interpolating…".
- Fig. 1.4 caption | The acoustic line is drawn only up to 2π/a = 2.3 keV, so for m_χ ≥ 1 MeV it cannot "leave each parabola near its right end"
  (right ends 5.3–530 keV). | Qualify: "for the lightest mass".
Steps reproduced: Eq. 1.24 (elastic) ✓; Eq. 1.25 ✓; Eqs. 1.26–1.27 (ω_q, v_min) ✓ incl. the absolute value argument; ω_max and the
v_min minimum at q = (2m_χω)^{1/2} ✓; v_max² = 7.023e-6, m_min 0.28 MeV/0.28 keV/0.316 MeV/8.54 keV, q = 0.84 keV/23 eV ✓; Table 1.2
all rows ✓; 1 MeV band 0.459–4.84 keV, 10 MeV 0.422–52.6 keV ✓; 45 MeV for Si recoil = 1.11 eV ✓; Xe 0.113 keV, fraction 0.142 ✓;
angular delta average = Θ/(2qv) ✓; q dq/4π² measure ✓; limit box v_min = q/2μ ✓; η branches (via D.1) ✓; η(0/600/700) natural
1041/19.2/2.39 ✓; fall ×192 ✓; edge expansion Eq. 1.34 (Taylor coefficient and δ³/3) ✓, 0.81/0.92 and 0.98/0.99 ✓, scale 172.7 ✓;
mass-edge linearisation and "4 km/s" ✓; η at favourable speed 2.8e-4, 1.9e-3, 1.1 %, 14 %, 85 % ✓; escape-shift 3.1 %/6.3 % ✓.
Used before defined: Brillouin zone, "folding", crystal momentum, reciprocal-lattice vector, first zone (first paragraph and §1.3
threshold mass; defined only in §3.1); acoustic branch ν (§5.2); band gap is used in §1.1/Fig. 1.1 and defined here; "matrix element" (fine).
Too slow: "the elastic collision… which every reader has met" (fine but long). Too fast: the "never fold q" convention arrives before I know what folding is.
Outcomes: (i) m_min for a 2 eV threshold: 2·2/7.023e-6 = 0.570 MeV ✓. (ii) open q-band for a 1.5 eV gap at 5 MeV: roots of Eq. 1.30,
0.579–25.9 keV ✓. (iii) η(650 km/s) at v_E^ref: second branch, 7.72 in natural units ✓. (iv) explain edge ∝ δ²: yes. All can do.

## §1.4 Light dark-matter models
Lost points
- Opening and Eq. 1.35 | `ψ̄γ^μψ`, `ψ̄ψ`, "reduce to the number density" are QFT language I do not have. I took the claim on trust; C.9
  then rescued me (classical fields only). | Say in words: "for slow particles both reduce to the number density (no proof needed here)".
- Dark photon | U(1) gauge boson, kinetic mixing, "loops of heavy particles" are QFT; C.9's shift algebra I could follow.
- Absorption | Eqs. 1.45–1.46 (ALP and scalar NR reductions) are quoted, not derived; "formally higher order in 1/m_e but dominates"
  is unargued; γ⁵, F F̃, field operator ψ̂ (§2.3), optical conductivity σ_1, plasma frequency, self-energy Π, ζ_eff formula all arrive
  without definition. I could not check any of it. | Acceptable as a preview if labelled so; one sentence on why ∂_tφ beats ∇φ
  (m_φ vs m_φ v) is given, but the 1/m_e ordering is not.
- Inelastic | "Dirac fermion split into two Majorana states" is opaque at my level; the kinematic consequence is clear.
Steps reproduced: static Proca → (−∇²+m²)A'^0 = yδ ✓; Eq. 1.36 (sign via C.9) ✓; Eq. 1.37 (via C.9 contour) ✓; Born σ = μ²|Ṽ|²/π
(4π(μ/2π)²) ✓; Eq. 1.38–1.40 ✓; limit-box leading corrections (both) ✓; Eq. 1.41 from y_e² = 4πα ζ² ✓; worked example μ 0.486,
7.67e-18 MeV^-2 = 2.98e-39 cm² ✓, factor 566 ✓, 1.5e-8 ✓; freeze-in 6.05e-38 cm² ✓; σ_N factors 1.22/952 and 3.96/3103 ✓; 1/R 39 MeV ✓;
absorption-rate dimensions ✓.
Used before defined: S(q,ω) (forward), Helm form factor (forward), longitudinal dielectric function ε, TDDFT/RPA (forward, fine).
Too fast: the whole absorption subsection; the in-medium mixing paragraph. Pace of the Yukawa and σ̄_e parts is right.
Outcomes: (i) σ̄_e for a heavy dark photon with m_χ = 50 MeV, m_V = 100 MeV, ζ = 1e-3, y_χ = 0.5: μ_χe = 0.506 MeV, σ̄_e = 7.3e-39 cm² ✓.
(ii) decide heavy vs light for given m_V: yes. (iii) write F_DM for a Yukawa: yes. (iv) absorption couplings: can state, cannot derive.

## §1.5 Detector signals
Lost points
- Eq. 1.52 dimension check | "S(q,ω) has eV²" must be taken on trust, as S is defined only in §4.2. | Say "with the normalisation of §4.2".
- Toy rate | "α = q_0/m_e is the typical speed" makes the factor α a speed (αc in cgs); I briefly divided by 137 again. | Write αc explicitly in the
  formula when converting.
- Readout | Kinetic-inductance detector, Fermi level, impact ionization are used without a gloss (Cooper pair is glossed). Minor.
Steps reproduced: step model (2 and 3 pairs) ✓; thresholds 1.11/4.71/8.31 eV → 0.316/1.341/2.366 MeV ✓, factor ≈4 ✓; 27 pairs, σ 1.8 vs
5.2 ✓; Al 0.17 keV ✓; binomial→Poisson ✓; N_90 = 2.303, ln 20 = 3.00, 3.89 and 5.32 ✓; background √exposure scaling ✓; modulation
2A/π = 0.118, N ≥ 144 ✓; toy r = 7.11e33 cm^-2 s^-1 kg^-1 = 2.243e41 /yr, N_sig 22.4, limit 1.03e-41 cm² ✓.
Not checkable: Fig. 1.8 numbers (factor 46 at 1 MeV, 1.5 at 2 MeV) need the toy response, which is not specified precisely enough to recompute.
Too slow: the binomial-to-Poisson derivation (I have stat mech). Right pace: the exclusion-plot shapes.
Outcomes: (i) zero-background limit with one observed event and the toy r: 3.89/2.243e41 = 1.73e-41 cm² ✓. (ii) threshold mass for an
n-pair threshold: ✓. (iii) read the slopes and edge of an exclusion plot: yes. (iv) list theory vs measured inputs: yes.

## Appendix C.9 (prints as C.1)
- Euler–Lagrange for fields and the Proca Lagrangian are assumed. This is not in my background, but the step ∂(F F)/∂(∂A) = 4F is shown and I followed it.
- Contour integral for G(x): reproduced (residue e^{-mr}/2, result e^{-mr}/4πr) ✓; direct check ✓; H_s, H_v signs ✓; kinetic-mixing
  shift, coefficient −¼(1−ζ²) ✓; Born amplitude ✓. Clear.
- "Energy = −∫L for a static configuration" is correct for φ but for A^0 (no conjugate momentum) it works only because of the E²/2
  check. The text does flag this. Fine.

## Appendix D.1
- All of it reproduced: N_esc by parts ✓, angular integral ✓, η branches (i)/(ii) ✓, continuity ✓, dη/dv_min = −F/v_min ✓, I_1−I_2
  collection ✓, I_3 ✓, no-cut limits ✓.
- "The Gaussian pieces combine by Eq. (D.2)": the label sits on the y·e^{-y²} integral, but the combination in branch (i) uses the
  erf integral (D.1). | Cite both, or label the gather as a pair.
- Citation inconsistency: §1.3 says Essig et al. Eqs. (67) and (68); D.1 says Eqs. (66) and (68). | Reconcile.

## Overall
I would keep reading. The halo and kinematics sections are the best part: every number regenerates, the closed forms are derived
end to end in D.1, and the worked examples teach the arithmetic. What slowed me was vocabulary from outside my background,
crystal-momentum language in §1.3 and astronomical coordinates in §1.2, and the QFT-flavoured preview of absorption in §1.4,
which I had to take on trust. None of these blocks Eq. 1.52, which I could assemble from η, |Ṽ|² and S. One physics sentence (the
½μv² free-target bound) is ambiguous enough to stop a careful reader. The unresolved `??` references to the conventions appendices are the
other practical obstacle.

Verdict: **MINOR GAPS**
