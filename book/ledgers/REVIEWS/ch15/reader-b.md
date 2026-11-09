# Chapter 15: mock reader b (isolated), personas (b) and (c)

Source read: build/main.pdf (current, 2026-11-06 07:42; no ch15/D-39/D-40 source newer), checked against
tex/ch15/*.tex, tex/appD/D-39.tex, D-40.tex. I worked every derivation by hand or in Python (scipy). That
includes a full numerical implementation of Eq. (15.6) R^cons from the book's own closed forms
(Eqs. 15.3–15.6). Scripts are in the session scratchpad and are not part of the book.

## What I reproduced (both personas rely on this)
- Eq. (15.1-gI): the elliptic form equals the angular integral to 1e-13. Values 1.500, 1.322, 1.211,
  1.151, 1.051 and the π/2 jump are correct. g_II(4) = 0.672; g_II reaches 0.9 at y = 8.13 (text: 8.1).
- s_BCS: 6.01, 4.01, 2.82, 2.03, 1.05, 0.50 at y = 2.05 … 10; s(0) = 0; cut values 2.91 and 1.14; the
  first-order term reaches 0.3 at y = 3.83. All correct. The "first order" column of Tab. 15.x matches.
- On the edge, f_L(0.397) = 0.833 and r_ε = 0.748. WE 15-edge arithmetic is correct throughout.
- Eq. (15.6) evaluated directly: v = 0.40/0.20/0.049/0.003; L^cons/(g_I L^nor) = 0.681, 0.868, 1.001,
  1.072, 1.068, 1.023; bare 0.217, 0.323, 0.441, 0.565, 0.794, 0.934; 1+δ_cons(3) = 0.578;
  |ε^cons|/|ε_Lin| = 1.27, 1.06, 0.99; AB poles at 1.9217, 1.9636, 1.9914 Δ; coefficient 26.9 (text 27).
  ω→0 limit gives −2N_F; f-sum tail ratio 1 + 3e-5. All agree with the text.
- D.39 sum rule: Lindhard gives 0.800000. The conserving response at qv_F = 5Δ, integrated over
  2Δ < ω < 1000Δ, gives 0.79999. Confirmed.
- Mermin limits, the ballistic/diffusive ratio π q l/6, and L_Mer/L_Drude = 1.10 at ql = 0.64 (text 0.63),
  1.43 at ql = 1.5 and 1.098 at ql = 10. Correct.
- Mattis–Bardeen at T = 0, from Kramers–Kronig with the δ weight (π²/2)Δσ_n: σ_2(2.2) = 0.757, and
  L_s/L_n = 0.045, 0.235, 0.744, 1.302, 1.259, 1.074. Correct.
- Holstein: σS/σN = 0.4209 at 1 meV (ω'^4) and 0.733 (ω'^2); 90 % at 11.39Δ (ω'^2: 7.38Δ); crossing at
  16.2Δ; maximum +4.66 % at 31.0Δ; case II reaches 90 % at 53.7Δ; γ_H = 8.72e-11 eV; L = 2.43e-16.
  Edge approximation off by 0.2 % and 2.1 %. Correct.
- σ^J: the integral is (π/2)ω_p²; 87 % / 99.5 %; 3.30e4 eV at 1 meV; it crosses σ_1^N at 11.52 meV; the
  ratio of g_aee values 1.10e4 matches 5.6e-9/5.1e-13. The T-matrix collapse (D.40-T), the Nambu forms
  (D.40-O, D.40-bogo), the elliptic reduction (D.40-g) and the Debye branches of γ_H are all correct.
- WSi: k_F, v_F, 2N_F(gas), both ℓ_e ranges, γ_rel ranges, the ρ ratios 205–263, the 3.6–11 width ratio,
  and ε0ωρ = (1.2–1.5)e-5. Correct.

## Persona (b): particle physicist, knows QFT, no solid-state physics
### 15.1 Pair breaking by dark matter
- **Lost points.** None blocking. The Nambu channels (η, s1, s2), the bubbles R^0_AB and the gap-equation
  cancellation lean entirely on §7.2. I had to reread Eq. (7.2-Rc) to confirm the sign of the ladder
  term; the q = 0 cancellation then confirmed it. A one-line restatement of the ladder form
  R_ηη − ½V R_ηs R_sη/(1 + ½V R_ss) before Eq. (15.6) would remove that trip back.
- **Could not reproduce.** WE 15-alrate (3.30 and 2.68 kg⁻¹yr⁻¹, and the ratios 0.946/1.010/0.850/1.024).
  I did not attempt the full Eq. (10.2-rate) integral. The stated method is clear.
- **Used before defined.** The "kinematic edge" is used throughout 15.1 but only given that name (in
  italics) in 15.2. Mean free path ℓ_e appears in the limit box of 15.1 before §15.3 defines it.
- **Pace.** The hyperbolic substitution paragraph (A, B) is dense but every step checks. Fig. 15.1 and the
  first-order discussion are well paced.
- **QFT-side remarks (not errors).** The pair-field ladder *is* the vertex correction that restores the
  Ward identity, and the AB mode is the Goldstone mode that Coulomb lifts to ω_p (Anderson–Higgs). Naming
  these once would anchor a particle physicist instantly. The book uses "Ward" elsewhere (§4) and
  "Goldstone" in §6–7, so this is a missed connection, not missing material.
- **Outcomes.** Write L^cons and its three truncations: yes. Compute g_I(y): yes (done). Estimate the
  first-order screening at a given (y, q): yes, e.g. at y = 5 on the edge 2(0.397/5)(1.053) = 0.167.
### 15.2 Closed forms at the pair-breaking edge
- **Error in my field (kinematics).** The opening paragraph says a particle near the threshold mass
  m_min = 0.10 keV "must move at nearly v_max and give up nearly all of its kinetic energy, so its
  scatters lie close to the line q = ω/v_max". That is wrong. Full loss of kinetic energy at v_max means
  q = m v_max = 2ω/v_max, twice the edge. Check: v_min(q, ω) = ω/q + q/2m with m = 2ω/v_max², which at
  q = ω/v_max gives 1.25 v_max (forbidden); at q = 2ω/v_max it gives exactly v_max. In general
  q_min/(ω/v_max) = (2/x)(1 − √(1−x)) with x = 2ω/(m v_max²). This runs from 2 at threshold down to 1
  only for m ≫ m_min. Ch. 7's WE already uses q = 2(2Δ)/v_max = 0.27 eV for m_min. The edge *is*
  relevant: for 1 keV at ω = 2Δ, q_min is only 2.6 % above it. So the conclusion stands, but the
  stated reason must change to "particles a few times heavier than m_min".
- **Lost points.** None blocking. Worth one sentence: on the edge the ladder makes Re ε^cons
  *negative*. My evaluation gives (1+δ) = −0.21 at y = 2.2 and −0.92 at y = 2.05. The phrase "moves the
  real part … to 0.58" (y = 3) does not prepare the reader for the sign change nearer the edge.
- **Reasoning point (statistics).** The mask boundary y = 3.8 is set by the first-order term of the *bare*
  bubble reaching 0.3, an expansion the section has just shown does not describe the physical response.
  The conserving calculation alone would place the boundary near y ≈ 3. Say plainly that 3.8 is a
  conservative choice and not a derived threshold. The one-sided half-normal ϑ ≥ 0 treatment is sound.
- **Could not reproduce.** Nothing in this section. The 1.5 % bare-vs-resummed claim checks (0.323 vs 0.328).
- **Outcomes.** Evaluate Eq. (15.2-LBCS) at a point: yes (y = 2.2 gives 0.328). Explain why the bare and
  conserving forms differ: yes. State the three nuisances and the mask: yes.
### 15.3 Films and disorder
- **Lost points.** The WSi paragraphs are the hardest in the chapter for me. The diffusion constant from
  "the slope of the upper critical field", the "Ginzburg–Landau coherence length", "sheet resistance",
  the "Einstein relation" (stated without a line of justification) and "electrons that diffuse slowly
  also repel each other more strongly" are all new to me. The last paragraph's
  "Bogoliubov–de Gennes on a Wannier model", "Kubo–Greenwood" and "melt-quench molecular dynamics" are
  defined only in App. E (after this point). Each needs a clause, or a sentence saying the reader can
  skip it. "Ioffe–Regel" is defined in place; good.
- **Errors (WE 15-film, arithmetic).** Exponents are off by a factor of ten in two places:
  ε_Mer = (0.394 + 10.36i)×10^7 should read ×10^6. With 10^7, L would be 9.6e-9, not the stated 9.64e-8.
  The diffusion pole (0.747 + 10.34i)×10^7 should also be ×10^6; directly, k_TF²D/(Dq² − iω) =
  (0.748 + 10.37i)×10^6. The complex-frequency Lindhard value (3.53 + 0.024i)×10^5 should read
  (3.53 + 0.241i)×10^5. The ratios "430 times" and "29 times" are correct only with the corrected values
  (431, 29.3).
- **Inconsistent inputs.** k_F = 1.75 Å⁻¹ = 3.453 keV implies v_F = k_F/m = 6.76e-3, but the book uses
  6.67e-3. WE 15-film quotes k_TF = 4.08 keV and ω_p = 15.7 eV; §15.1 and §15.4 use 4.05 keV and
  15.78 eV. (4.05 follows from k_F; 4.08 follows from √3 ω_p/v_F with the mismatched v_F.) The effect is
  ~1 %, but a careful reader stops.
- **Could not reproduce.** "2N_F = (2.6–4.1)×10^47 m⁻³J⁻¹" from σ = e²(2N_F)D. With ρ ≥ 163 μΩcm and
  D ≥ 0.70 cm²/s as stated, the maximum is 3.4×10^47 (range 2.5–3.4). The "2.3–3.6 times the gas"
  inherits the 4.1.
- **Rendering.** "Stacks of sheets and the full slab are treated in ??" (\cref{sec:16.2} unresolved).
- **Minor.** WE 15-edge (15.2) calls 1/q = 0.97 μm "a wavelength". It is 1/q; 2π/q = 6.1 μm.
- **Outcomes.** ℓ_e, D, γ from ρ: yes (0.79 μΩcm → 26.3 meV). Choose a regime and evaluate Mermin: yes.
  Local MB edge: yes. Sheet factor: yes ((2/0.086)² = 541). Explain why WSi falls outside: yes, in words.
### 15.4 Absorption in superconductors and metals
- **Lost points.** None. The Nambu-matrix argument (unit matrix vs η) is the clearest thing in the
  chapter for a field theorist, and the exact collapse of the second-order amplitude is elegant and checks.
- **Pace.** The strong-coupling paragraph is too fast. N^El, P^El and the Eliashberg Δ(E) arrive without
  a picture of what they are, and App. E.9 is only a pointer.
- **Outcomes.** Show the clean SC does not absorb at q→0: yes. Derive σ^J and its sum rule: yes.
  Explain why phonon-assisted absorption carries case I and impurity-assisted case II: yes.

**Overall (b).** I would keep reading. All the physics is reproducible from the page, and my
independent evaluation of the conserving response matches every table entry. The chapter's kinematic
motivation in 15.2 contains a real error in my field, and WE 15-film has two misprinted exponents.
None blocks the material that follows. **Verdict: MINOR GAPS.**

## Persona (c): condensed-matter theorist (DFT, many-body), no dark-matter physics
### 15.1
- **DM terms used without anchor.** "Master formula of Ch. 8", "density row", 𝔇_ee, F_DM = (αm_e/q)², σ̄_e,
  "standard halo" and "light/heavy mediator" are all from earlier chapters. With 1–8 and 10 read, that is
  fine. v_max = 2.650e-3 (Eq. 1.9) does the most work in the chapter and deserves a reminder in the
  15.1 opener.
- **My field.** The derivation of Eq. (15.6) is correct and pleasantly self-contained (I reproduced it).
  The "generalized RPA" label is fine. Calling the clean criterion ℓ_e ≫ v_F/Δ = 7.3 μm (limit box 15.1,
  Tab. 15-inputs) while §15.3 uses ℓ_e vs ξ_coh = v_F/πΔ = 2.3 μm mixes two criteria a factor π apart.
  Pick one.
- **Could not reproduce (thresholds in the 15.1 limit box).** With "ratio ≥ 0.9" I get the Lindhard
  function within 10 % of conserving for y ≥ 7.9 (text 8.2), y ≥ 6.3 at 4× edge (text 6.5), and the
  bare bubble for y ≥ 9.19. That last value matches 15.2's 9.2 but **contradicts 15.1's "9.4"**. With
  "ratio ≥ 1/1.1" I get 8.4, 6.7 and 9.7. g_I L^nor is within 10 % for y ≥ 2.26 (15.2: 2.25; 15.1: 2.3).
  The two limit boxes use different conventions, or the 15.1 figure uses a different Lindhard
  (finite q/2k_F?). State the convention and make 9.4/9.2 and 2.3/2.25 agree.
- **Condescension.** None.
### 15.2
- **My field.** The resummation (D.39-resum) is exact algebra, and the analytic structure (AB pole as a
  zero of 1/ε, sum rule 4/5) is correct and nicely done. The Born-impurity conserving response is
  asserted, not shown: "impurity ladder in the bubble and in the pair channel together". I accept it,
  but a CM reader wants to know whether the Born self-energy is in the Nambu τ0 or τ3 channel and
  whether the impurity vertex dresses the pair channel. One sentence, or a pointer into App. E.20.
- **DM side.** The nuisance and mask paragraph is clear even without DM-statistics background, thanks to
  §8.8.
- **Outcomes.** All met (see b).
### 15.3
- **Too slow for me (not condescending; the primary persona needs it).** The exponential free-flight
  derivation of D = v_F ℓ/3, the Drude-to-ρℓ step, and the definitions of ballistic, diffusive, clean and
  dirty. Anderson's theorem is stated correctly, including its weak-disorder premise, which is exactly
  what the WSi argument needs.
- **My-field errors.** The WE 15-film exponents, v_F/k_F/k_TF and WSi 2N_F, as listed under (b).
  The plasmon-width vs transport-rate distinction is correct and important. The "sheet" formula
  (15.3-sheet) is the standard thin-film (Keldysh-type) result; correct.
- **QROCODILE.** As a non-DM reader I needed a clause saying what the detector is (an SNSPD-type
  superconducting nanowire DM search). "QROCODILE nanowires" first appears here with no gloss.
- **Outcomes.** All met.
### 15.4
- **My field.** The Nambu identification of current = τ0 and spin current = τ3 at q = 0, the
  Mattis–Bardeen case II, and Holstein with case I are correct. The exact collapse of the amplitude is a
  nice point that I have not seen stated so cleanly. The spin-current pair breaking follows directly from
  [Σ v_k(n_k↑ − n_k↓), c†_k↑c†_−k↓] = 2v_k c†c† ≠ 0. Correct within BCS, with the needed caveats
  (spin–orbit, F_1^a renormalization) named.
- **Probable overstatement.** "Which renormalization factors … survive … is open." For the *normal* metal
  at ω ≪ ω_D, the extended-Drude (Allen; Shulga–Dolgov–Maksimov) analysis gives σ_1 ≈
  ω_p²γ_H(ω)/[ω²(1+λ_tr)²] beyond one-phonon order. That is the 1/(1+λ_tr)² = 0.52 the text calls
  hypothetical. Only the superconducting extension seems genuinely open. Please check and narrow the claim.
- **Outcomes.** All met.

**Overall (c).** I would keep reading. The many-body content is correct and often sharper than the
standard treatments. My objections are numerical consistency (inputs, two exponents, one DOS range, two
limit-box thresholds) and one probable overstatement about strong-coupling renormalization. The DM
framing is understandable from earlier chapters. **Verdict: MINOR GAPS.**

## Fix list (both personas, by priority)
1. §15.2 opener: the threshold-mass kinematics. A threshold-mass particle scatters at q = 2ω/v_max;
   only m ≫ m_min reaches the edge.
2. WE 15-film: ε_Mer and the pole are ×10^6, not ×10^7; complex-frequency Lindhard Im = 0.241×10^5.
3. Limit box 15.1 thresholds vs limit box 15.2 (9.4 vs 9.2; 2.3 vs 2.25; 8.2/6.5 not reproducible as
   stated). State the "within 10 %" convention.
4. §15.3 WSi 2N_F upper end 4.1 → ≤ 3.4 (and the 3.6× ratio), or state which data give 4.1.
5. Unify v_F (6.67 vs k_F/m = 6.76 e-3), k_TF (4.05/4.08) and ω_p (15.7/15.78).
6. Unresolved \cref{sec:16.2} renders as "??". (Out of chapter: Ch. 1 near "ζ" also shows "(??)".)
7. Minor: 1/q is not "a wavelength" (WE 15-edge). s_BCS → π²/(2y) = 4.93/y, not 5/y. Clean criterion
   v_F/Δ vs ξ_coh. Notation: f_L is real in Eq. (15.2-Lin) but complex in Eq. (15.3-fL); h and g are
   reused for two different functions in D.39; δ is both the edge shift and ω − 2Δ (WE 15-holstein).
8. Optional: name the Ward identity / Goldstone / Anderson–Higgs links once; gloss the GL/H_c2/Einstein
   relation and the App. E methods in 15.3; give the Born-impurity Nambu structure; narrow the
   strong-coupling "open" claim.

**Combined verdict: MINOR GAPS.**
