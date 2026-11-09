# Ch15 mock-reader review: persona (a), isolated

Reader: first-year PhD student in direct detection. Read linearly from the .tex sources (ch15/*.tex, appD/D-39, D-40), with Sec. 7.2, 4.3–4.5 and 8.8 reread for the cited equations. Every derived step was worked, by hand or in sympy/mpmath/scipy. Scripts are in the session scratchpad.

**Verdict: MINOR GAPS.** Nothing blocks the following material. Every closed form and nearly every number I checked came out right. The problems: two numerical typos in WE 15-film, one small "within 8%" vs 8.7% mismatch, an Al free-electron parameter set that is not self-consistent, and a few compressed steps.

## What I reproduced (so the reader can trust it)
- Eq. (15.1-ident): the product identity, the (E+E')² − (ξ'−ξ)² identity, the hyperbolic substitution, the measure dξ(E+E')/EE' = 2dA (checked numerically), and ∫ = 1/Δ².
- Eq. (15.1-F): the closed form and all three continuations, including the sign of Im F for p>1 (direct quadrature at ω+iη).
- Eq. (15.1-bubbles) by partial fractions; the mixed and phase bubbles from the stated M^N products; eq. (15.1-Rcons) from (7.2-Rc), with V_BCS dropping out.
- The limits of R^cons: zero at q=0; R^cons/(2N_F v_F²q²/3ω²) = 1 + 2.8e-5 at v_Fq = 0.01Δ; R^cons = −2N_F at ω→0; Lindhard limit at Δ→0.
- Eq. (15.1-gI): the angular integral, the elliptic form and the pair-energy form (7.2-pairspec) agree to 1e-9. Values 1.500/1.322/1.211/1.151/1.051 check, as does the large-y form.
- The s_BCS values (4.01, 2.82, 2.03, 1.05, 0.50, 0.248), s_BCS(0) = 0, and the cut values 2.91 and 1.14.
- Vertex fractions on the edge: 0.397, 0.324, 0.202, 0.0486, 0.0032.
- L^cons/g_I L^nor on the edge: 0.868, 1.001, 1.072, 1.068, 1.023. L^bare/g_I L^nor: 0.323 … 0.934. |ε^cons|/|ε_Lin| = 1.27, 1.06, 0.99.
- Peak of L^cons/L^nor: 1.432 at y = 2.70. AB poles: 1.921, 1.963, 1.991.
- Tab. 15-edge: the g_I, s_BCS, first-order and both resummed columns, all rows. First-order term = 0.3 at y = 3.833 (uncut) and 3.004 (cut).
- WE 15-edge: every line. WE 15-alrate: kinematics only (19.5Δ, 11.7Δ, 196Δ, 1.3e-3).
- Sec. 15.3: ρ_el·l_e = 3.97e-16 Ω·m², 0.79 μΩ·cm, γ_rel = 26.3 meV, D = l_e v_F/3, and the diffusive, ballistic and ratio forms of (15.3-limits). L_Mer/L_Lin = 24.0 at the WE point. MB ratios 0.045/0.235/0.744/1.302/1.259/1.074. Condensate weight (π²/2)Δσ_n. Sheet factor 540. The WSi transport numbers.
- Sec. 15.4/D.40: the Nambu forms (D.40-O, D.40-bogo) by hand; the collapse (D.40-T); the pair integral 2x g_I; the σ_1^S prefactor; λ_tr normalization; both γ_H branches.
- Holstein ratio: 0.421 (ω'^4) and 0.733 (ω'^2) at 1 meV; 90% at 11.39Δ (ω'^4) and 7.38Δ (ω'^2); max 1.0466 at 31Δ; crossing at 16.2Δ; case-II 90% at 53.7Δ. Edge formula off by 0.2% and 2.1%; σ_1^S(2.2Δ) = 4.39e-8 eV.
- Spin current: σ_1^J(1 meV) = 3.30e4 eV, the 87% and 99.5% fractions, and the tanh sum rule. g_II(4) = 0.672; g_II reaches 0.9 at 8.13Δ.
- D.39: the resummation algebra; the PV subtraction formula and the step-J log; the moment expansion h = 3ω²/(qv_F)² − 9/5.

## Sec. 15.1 Pair breaking by dark matter
**Lost points**
1. 15.1-closed, "phase −i relative to it (App. D.21)". The sign of R^0_{s2η}, and hence the sign of the ladder, rests on a phase I am asked to accept. The consistency check against Sec. 7.2 at q=0 helps. One line would fix it: "O_{s2} has Nambu matrix s_2; its pair-creation element is −i(uu'+vv')".
2. Superscript "N" in M^N_A is never explained (Nambu? normal-ordered?). Fix: name it on first use.
3. 15.1-closed, the step from the product identity to |M_η|² in (15.1-ident) is skipped. One needs EE' − ξξ' + Δ² = (EE' − ξξ' − Δ²) + 2Δ², then the product identity. I got there, but only after the text pointed me to the wrong factor (EE' − ξξ' − Δ²). Fix: one displayed line.
4. "At ω→0 both terms give R^cons = −2N_F": the ladder term goes to zero and the bubble gives −2N_F. I first read "both terms" as each giving −2N_F. Fix: "the bubble gives −2N_F and the ladder vanishes".
5. The measure claim dξ(E+E')/EE' = 2dA "at fixed μ" is stated without the one-line reason: cosh b db = cosh a da at fixed ξ'−ξ. I verified it numerically before I trusted it.

**Steps I could not reproduce**
- WE 15-alrate: the rates 3.30 and 2.68 kg⁻¹yr⁻¹ and the ratios 1.23, 0.946, 1.010, 0.850, 1.024. They need a 2D quadrature of (10.2-rate) with the halo. The inputs are clear, but a reader cannot check these by hand. That is acceptable for a worked example, but it should say "numerical; see App. E.20".
- The claim that the cutoff dependence of R^0_{s2s2} cancels "up to terms of order v_Fq/ω_D": asserted, not shown.
- The phonon-pole correction of relative order (c_LA q/ω)²: asserted.

**Used before defined**
- "kinematic edge" (q = ω/v_max) is used throughout 15.1-bare/first/chain but defined (emph) only in the 15.2 intro. Fix: move the definition to its first use in 15.1.
- "generalized random-phase approximation" is named but not distinguished from the RPA of Sec. 4.5. The adjective is clear enough from context.

**Too slow / too fast**
- Too fast: 15.1-closed packs five identities, a substitution, analytic continuation and a cutoff cancellation into about 40 lines. It is reproducible, but only with sympy at hand.
- Too dense: the last two paragraphs of 15.1-first and 15.1-bare are strings of numbers in which the normalizer keeps changing (L^nor, g_I L^nor, the conserving value). I had to tabulate them myself. Fix: point to Tab. 15-edge (currently first met in 15.2) or move it forward.
- Minor inconsistency: 15.1-first says the conserving loss function lies within 0.980–1.087 of g_I L^nor for y≥3, and 15.2-cons says "at most 8.7% at y=3.6". Yet 15.1-chain and the summary say "within 8%". Should read "within 9%".

**Learning outcomes (inferred)**
- Build L^cons from (7.2-Rc) and reduce it to bare, g_I L^nor and Lindhard: yes, done in code.
- Derive g_I by angle and by pair energy: yes.
- Compute the first-order screening correction and say where it fails: yes. I get 4.0%/17%/54%/145% at y = 10/5/3/2.2.
- Say why 0.18 vs 0.30 meV matters: yes qualitatively. The rate factor is not reproducible by hand.

## Sec. 15.2 Closed forms at the pair-breaking edge
**Lost points**
1. 15.2-nuisance, the mask boundary y<3.8. It is set by the bare bubble's first-order term reaching 0.3. But the chapter has just shown that the bare bubble is the wrong response, and that the conserving value is controlled (within 6% across mean free paths) already at y = 3. Why should a bare-bubble criterion define the mask? "No expansion about g_I L^nor has a controlled central value" did not convince me, since the conserving calculation is not an expansion. Fix: state the actual criterion, e.g. "we mask where the conserving value depends on l_e by more than X%, and add a margin", or justify 3.8 directly from the conserving column.
2. With my own quadrature, 1+δ for the conserving response is **negative** (−0.215) at y = 2.2 on the edge: the real part of ε changes sign. The text gives |ε| ratios and the y=3 value 0.58, but never says this. It is physically interesting (the inductive response that 15.2-disorder mentions) and it surprised me. Fix: one sentence.
3. Notation: δ is the real-part shift (15.2-cons), then δE in the nuisance paragraph, then δ = ω − 2Δ in WE 15-holstein. No real clash, but δ and δ_𝔰 sit side by side.

**Steps I could not reproduce**
- The impurity columns of Tab. 15-edge (1 μm, 30 nm) and all of 15.2-disorder: "conserving response with Born scattering, impurity ladder in bubble and pair channel". No formula is given, so I can only take the results on trust. Fix: state the dressed bubble at least schematically, or say explicitly that it is in App. E.20.
- The sum-rule value 0.8000 for R^cons above 2Δ (D.39): I checked the normal-metal side analytically but did not run the conserving integral.

**Used before defined**
- f_L(ν) is defined in (15.2-Lin) and defined again as (15.3-fL). This is harmless, but the second definition could simply cite the first.

**Too slow / too fast**
- 15.2-resum is well paced. The ratio 𝔯_ε = 0.749 is the key new idea and it is explained clearly.
- WE 15-edge: "a wavelength of 0.97 μm" is 1/q, not 2π/q (6.1 μm). The same usage appears in 15.2-nuisance ("the wavelength 1/q"). Fix: "reduced wavelength" or "length 1/q".

**Learning outcomes**
- Apply (15.2-LBCS) and (D.39-resum) on the edge: yes. All WE 15-edge numbers reproduce.
- Put a conserving response into resummed form via 𝔤 and δ: yes. I computed 𝔳 and 1+δ myself.
- Name the three nuisances and their types: yes. Justify the mask at 3.8: no (lost point 1).

## Sec. 15.3 Films and disorder
**Lost points**
1. **WE 15-film, numerical typos.**
   - Stated: ε_Mer = (0.394 + 10.36i)×10⁷ and the diffusion pole (0.747 + 10.34i)×10⁷. Both should be ×10⁶. I get 3.95e5 + 1.038e7 i and 7.48e5 + 1.037e7 i. Only ×10⁶ is consistent with the stated L = 9.64e-8 = Im ε/|ε|².
   - Stated: the complex-frequency Lindhard value (3.53 + 0.024i)×10⁵. It should be (3.53 + 0.24i)×10⁵. Only that matches the stated "imaginary part 430 times too small" (1.04e7/2.41e4 = 431).
   - As printed, these three numbers contradict the text around them, and I lost time on them.
2. The aluminum free-electron parameters are not self-consistent:
   - k_F = 1.75 Å⁻¹ = 3.45 keV gives v_F = k_F/m_e = 6.76e-3, not 6.67e-3. The value 6.67e-3 corresponds to k_F = 1.73 Å⁻¹.
   - k_TF is 4.05 keV in 15.1 and the tables, but 4.08 keV in WE 15-film.
   - ω_p is 15.78 eV in 15.4 and the input table, but 15.7 eV in WE 15-film.
   - Each is within about 1%, but a careful reader wonders whether they are different materials. Fix: one consistent set, or a sentence saying which number is primary.
3. 15.3-mermin: in the ballistic limit "ℓ(ν) ≃ −iπ + 2ν on the retarded branch" is right. My first numerical attempt at complex ν_γ used the principal log of (1+ν)/(1−ν) and got nonsense; the correct branch is log((ν+1)/(ν−1)). The book warns about this in 15.3-analytic, two subsections later. Fix: give the retarded-branch formula for complex ν where (15.3-mermin) is first used, not only by reference to (C.8-branch).

**Steps I could not reproduce**
- The QROCODILE anisotropy onset (cited) and the 1.25e4 weight of the empty-core model (Sec. 15.4): both asserted.

**Used before defined (jargon for persona a)**
- "Ginzburg–Landau coherence length" and "slope of the upper critical field" (15.3-wsi).
- In the 15.3-wsi specification paragraph: "Bogoliubov–de Gennes", "Kubo–Greenwood", "Wannier model", "melt-quench molecular dynamics with a machine-learned potential". None of these is defined. Acceptable in a pointer to App. E.20, but a three-word gloss on each would help.
- "Mattis–Bardeen conductivity" is used in 15.3-sc before 15.4 derives it (the forward reference is acknowledged).

**Too slow / too fast**
- Well paced. The derivations of D_diff, ρ_el·l_e, the diffusion pole and the sheet factor are exactly the right size.
- The Anderson-theorem paragraph is qualitative but clear enough.

**Learning outcomes**
- Compute the Mermin loss function of a film and identify diffusive vs ballistic: yes (24× at the WE point).
- Get the dirty superconducting edge from σ_1, σ_2: yes. I built σ_2 by Kramers–Kronig and reproduced all six ratios.
- Sheet screening factor: yes.
- Explain why WSi is outside relaxation-time forms and BCS: yes. All the k_F l_e, q l_e and γ_rel numbers check.

## Sec. 15.4 Absorption in superconductors and metals
**Lost points**
1. Eq. (15.4-a2Ftr): Ω and N appear without definition in the section (D.40 later gives V = NΩ). Fix: "Ω the cell volume, N the number of cells" at the equation.
2. 15.4-spin: J_e is the scalar Σ_α J^{αα} (σ·v), the combination the ALP couples to. This is implicit, and I had to infer it to see why only the αα components appear and why S_JJ = 3S_zz. Fix: one clause.
3. 15.4-holstein, "the weight averages to 1 − cos θ". The factor bookkeeping is ⟨[ê·(v'−v)]²⟩/⟨(ê·v)²⟩ = 2(1 − cos θ), with the 1/2 in the definition giving 1 − cos θ. Worth half a line.

**Steps I could not reproduce**
- WE 15-holstein and 15.4-spin event numbers: 1.29e18 ζ², ζ = 1.5e-9, 0.11 events, g_aee = 5.1e-13 and 5.6e-9. These need (10.7-dp) and (10.7-alp), which I did not reopen. The conductivities and L that feed them do check.
- σ_1^MB = 7.65e3 eV at 1 meV: consistent with σ_dc = 9.46e3 eV times g_II(5.56), but I did not evaluate g_II at that point.

**Used before defined**
- "Landen transform" (D.40, the Debye paragraph): undefined. Harmless.
- "Eliashberg Green's functions": used in 15.4-strong, which is explicitly a sketch.

**Too slow / too fast**
- The current/spin-current Nambu argument is the clearest part of the chapter: short, exact and checkable.
- 15.4-strong is speculative by design and labeled as open. Fine.

**Learning outcomes**
- Say from the Nambu matrix whether a uniform probe breaks pairs (current: unit matrix, no; spin current: η, yes): yes.
- Derive the exact phonon-assisted amplitude and Allen's formula with the case-I factor: yes.
- Evaluate σ_1^S/σ_1^N for a Debye law and the edge power δ⁵: yes.
- Compute σ_1^J and its sum rule: yes.
- Turn σ_1 into dark-photon and ALP event rates: not checked (needs Ch. 10.7 formulas).

## Summary table and appendices
- Tab. 15-nuisances agrees with the text, apart from the "within 8%" vs 8.7% wording above.
- D.39 and D.40 are clean and complete for what Ch. 15 uses. D.40's closed-form derivation of g_I and g_II is the clearest version in the book.

## Overall
I would keep reading. The chapter does what it promises: it builds the conserving loss function from Sec. 7.2 and shows in closed form why the bare bubble fails at the edge. It also shows that g_I L^nor is a good central value for y ≥ 3. Every key result reproduced to the printed digits, which made the chapter feel trustworthy.

The burden is density: 15.1-closed and the number-heavy paragraphs of 15.1 demand code. And the mask rationale in 15.2 is the one argument I did not accept.

Fix list, in priority order:
1. The WE 15-film exponent and imaginary-part typos.
2. The Al v_F / k_TF / ω_p consistency.
3. The mask rationale.
4. "Within 8%" → 9%.
5. Define "kinematic edge" at its first use.
6. The phase of M_{s2} and the |M_η|² step.
7. Mention the sign change of the conserving real part at y ≈ 2.2.
8. "Wavelength" → 1/q.

Verdict: **MINOR GAPS**.
