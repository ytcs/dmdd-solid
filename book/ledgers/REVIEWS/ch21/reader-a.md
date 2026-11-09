# Chapter 21 mock-reader review: persona (a)
Reader: first-year PhD student, dark-matter direct detection. Read only the Chapter 21 text (tex sources plus the built PDF for resolved references), with Chapters 1–8 and 10–20 already read. Every derived step was worked by hand or in Python/scipy. Numbers that need the tabulated responses (kernel values, step columns, band sensitivities) were taken on trust; everything that can be checked from the stated inputs was checked.

## Chapter opening and map
- Clear. The opening count (zero events, 2.3 events) sets up the chapter well. The map figure caption is useful.
- **PDF defect:** "What remains open is indexed in ??" — `\cref{chap:22}` is unresolved in the build. This happens here and again in the last paragraph of the Summary.

## 21.1 Rate assembly
**Lost points.** None that block.
- Minor: the text says "it is 6.29e4 per kilogram and year at 300 km/s", calling this "the kernel". Strictly, the quantity is ρΓ/(mρ_T), as the caption of Fig. 21.2 says, not Γ itself. Writing "the kernel, scaled to a rate per target mass," in the text would avoid this.
**Reproduced.**
Eq. (21.1-gammav): the angular average gives q dq/(4π² v). Checked. Integration by parts to (21.1-etaform): the boundary terms vanish as stated. Eq. (21.1-eta2): differentiating both sides gives −2uη. The (v²−u²)^n recursion also checks. Debris flow: F_flow = v/(2 v_flow v_E), η_flow piecewise, window 89.5–590.5 km/s, 1/v_flow = 882 in natural units, 55 % above 400 km/s. WE debris: R_flow = 7.313e7/340 = 2.151e5; ratio 1.345; mixed rate 1.720e5 (the text gives 1.721e5, a rounding difference); 471 per kg per day; endpoint energies 19.4 and 35 eV; at 1 MeV, 0.78 + 0.22·0.39 = 0.866, i.e. −13 %. Floors: 0.3332, 0.3290, 0.3202 (June, −3.9 %) and 0.6031 MeV; v_on = 146.9 and 46.4 km/s.
**Could not reproduce.** ⟨δv_E⟩ = 1.61 km/s and ⟨δv_E²⟩ = 108.3 (km/s)². These need Eq. (1.2-annual) in full. They are plausible, and I accept them.
**Used before defined.** None.
**Pace.** The annual-average digression and the paragraph "The numbers behind the box" are dense but skippable. The η₂ paragraph is fast but complete.
**Outcomes.** (i) Write any channel's rate as a halo functional of f_χ: yes. (ii) Move between the kernel form and the η form: yes, done above. (iii) Compute a rate in a shell-plus-SHM halo by linearity: yes; I recomputed the mixed rate. (iv) Explain why 2E_th/v_max² is a floor and not an edge: yes, all three reasons.

## 21.2 Halo-independent bounds
**Lost points.**
1. WE "One stream saturating a bound": "with Ξ-mass c = u₀N^up/A₂ = 4.67e-23 yr⁻¹ in units with c = 1". The symbol c means two things in one sentence (the stream weight and the speed of light), and I had to reread it. Rename the stream weight, for example to c_a as in Ξ* = Σ c_a δ_{w_a}, or to ξ.
2. Box lim:21.2a: the title is "Halo-independent bound for a directional response", but the box states the isotropic formula "for a response averaged over the directions". It took the figure caption to see that the box gives the formula and the plot gives the directional program's ratio to it. One sentence in the box would fix this, e.g. "The formula ignores the anisotropy; the figure shows how far the true bound departs from it."
3. Declination support: the condition v² + v_E² − 2v v_E cos(δ + δ_E) ≤ v_esc² holds only at the most favourable right ascension. That is legitimate, because the kernel does not depend on right ascension and the program can choose it freely, but the text does not say so. As written it looks wrong at first, since the true angle depends on right ascension too.
4. Final-state leakage: "provided the number of pairs grows stochastically with the seed energy". "Stochastically ordered" (stochastic dominance) is not in my background and is not defined. A clause such as "P(N_eh ≥ n | E) does not decrease with E for every n" would fix it.
**Reproduced.**
The stream normalisation: count = ∫k dΞ recovers ρ/(mρ_T)∫fΓ. The union bound: ln 30 = 3.401. Feasibility and certificate for (21.2-hib). The proof that the SHM curve lies below the bound, via ∫η̃ dA_j ≥ η̃(u₀)A_j(u₀). WE stream: The column prefactor αm_e²·(1 kg·yr)/(M_cell μ²) = 8.64e22 yr, checked from M_cell = 2 × 28.0855 u. The three ratios N/A_i, the stream weight 4.67e-23, the counts 1.26/3.40/0.76, and λ₂ = 8.23e-21. The factor 2.94 = 2.42 × 1.22. The defect bound (21.2-defect): Ξ(supp f) ≤ N_tot/κ_v. Checked. The leakage factors 2 × 0.0641/3.75 = 0.034 and 0.036 (for the 3.6 eV pair energy). The grid gap 1.8921/1.8903 = 1.00095.
**Could not reproduce.** The sidereal-mean range of Y₄^c, [−0.16, 0.07], needs the orientation algebra of Sect. 11.7. I accept it. The bound "misassigned weight ≤ 2ω_max × largest phonon-dressed response" is only cited to App. D.46. I guessed "one strip of width ω_ph at each of the two bin edges", which would make the factor 2 obvious. Saying this in one clause would help.
**Used before defined.** "stochastically" (above). "Lipschitz constant" and "covering radius". These are standard mathematics but not in my assumed list; a parenthesis each would do. "semi-infinite linear program" appears only in the Summary.
**Pace.** Too fast: the directional subsection (21.2-dir) and the final-state paragraph of 21.2-leak, which packs the Dyson split, the seeding fix and stochastic ordering into a few sentences. The one-line proof of the certificate (∫f dΞ ≤ ∫Σλ_i k_i dΞ ≤ Σλ_i N_i) is short enough to give inline instead of only citing App. C.12.
**Notation.** δ means four things in this section and the next: the declination; the dip of the dual (Eq. 21.2-defect); the distance from the end point (Sects. 21.1 and 21.3); the templates δ_k.
None is ambiguous in context, but a different symbol for the dip (ε, say) would help.
**Outcomes.** (i) Set up the program with stream kernels: yes. (ii) Apply (21.2-hib) and write its certificate: yes. For a 1-bin case with A(v) given I can do it in two lines. (iii) Say when the directional response forces the full program: yes, near the bin onsets and for sidereal binning. (iv) Bound grid leakage: yes in principle; the table-versus-Lipschitz caveat is clear.

## 21.3 The kinematic edge
**Lost points.**
1. Degeneracy subsection: "the rate at fixed m_χ − m_edge scales as A_η v_max^{2p_on+8} for a heavy mediator". I could not get the exponent. My tally:
   - F_esc ∝ A_η v_max contributes 1.
   - δ_on ∝ v_max at fixed Δm contributes p + 7/2.
   - Γ_on ∝ q*^{p+3/2} contributes p + 3/2.
   - That gives 2p + 6. The remaining 2 must come from the q-powers of Eq. (10.2-rate) and the measure, which the text only names.
   A one-line tally would let a reader check the near-cancellation, 1.76 % per km/s on each side, that the worked example relies on.
2. "The envelope theorem applied to (13.1-mZP)": the theorem is named, not stated. Its content ("only the explicit dependence counts at the minimum") appears earlier in 21.3-power. Point back to that sentence.
**Reproduced.**
The q-width integral √(2m)[q*(v − v_on)]^{p+3/2} B(½, p+2). The lens geometry: v and u to second order, a_⊥ = v_E/(2 v_esc v_max), the lens volume and F_esc. A_η = F_esc/(2v_max), matching the SHM form. y ≪ k v₀²/(2v_esc) = 52 km/s. The beta-function power p + k + 7/2. dm_edge/dv_max = −2m²/q*, and δ_on = (v_max/2)Δm/m for a q-independent onset. Halo fractions within 12 km/s of v_max, by numerical integration of the Lisanti family: 6.03e-5, 4.73e-6 and 3.65e-8. All match. The free nuclear recoil: kernel linear, n = 3 + k, m_edge = 137 MeV for a 10 eV threshold. Every row of Table 21-edge from the counting rule. x*_max = 3.5 and 5.3 meV per 0.001 MeV. The exposure factors 10^{−2/13} = 0.70 and 10^{−2/15} = 0.74. The edge shifts: ±25 km/s gives 6.6 %; the annual range gives −3.9 % and +3.4 %; 1 % in the gap equals 4.0 km/s. ∂ln A_η/∂v₀ ≈ +3.1–3.2 % per km/s (giving 1.21 and 0.83), and ∂ln A_η/∂v_esc ≈ −1.7 % per km/s against 14/v_max = 1.76 % per km/s. WE gap shift: δm = 2.85e-3 MeV. The factors (1 − δm_edge/δm)^{13/2} = 0.0044, 0.115 and 0.371, using the model's 2.83e-3. The mimicking shift 3.35 km/s. The zero-phonon sensitivities 0.54 and −1.62 (from 3.5245 eV − 1.355 eV), and the 0.00188, 0.00277, 0.00095 and 0.00006 MeV shifts. The spectral shape (ω − E_on)^p (ω_top − ω)^{k+5/2}, and the extra ½ in the power from the year average near 2 June.
**Used before defined.** "Envelope theorem" (above). Everything else comes from Ch. 13 and is defined there.
**Pace.** The zero-phonon exponent paragraph, before Table 21-edge, is fast. It packs D = 5, the second-class vertex, Coulomb lowering and the 1s line into one paragraph. With Ch. 13 fresh it works. Otherwise the pace is right; this is the best section of the chapter.
**Outcomes.** (i) Derive the edge power for any p_on and k_tail, including the corner case: yes. (ii) Find which parameter combinations an edge limit measures (E_on/v_max², the product F_esc Γ_on, the sum p + k): yes. (iii) Estimate how far an exposure reaches toward the edge: yes, (σ M t)^{−1/n}.

## 21.4 Theory nuisances in a limit
**Lost points.** None that block.
**Reproduced.**
The classical limits: 2.303 − b; 2.890 for one event on b = 1; 3.322 for two events on b = 2. β_k for one bin. σ_β = 0.393, the band 8.78e-42 to 1.93e-41, the 93 % share, and the one-at-a-time factors 1.28, 1.34, 1.08 and 1.07. The random-phase level sits at 0.71 of the nominal limit; the lower band edge is at 0.675. With the detector nuisance, σ_β = 0.405 and the band factor is 1.499. The one-sided case: σ_β = 0.306. The profiled limit for no events: from t = 2(u + k²u²/2) = 2N₉₀ I get ln ratio = k²N₉₀/2 = σ_β² t*/4, i.e. Eq. (21.4-profile) with t′ = t*. t′ = 2N^up = 2.61 for b = 1. The constraint-averaged coefficient (N₉₀ − 1)/2 = 0.65. Excluded cells: 1/(1 − f) = 1.25, 1.59, 1.49 and 1.08.
**Could not reproduce.** The multi-bin weights a_j (App. D.47 only). The one-bin case suffices for everything in the section.
**Used before defined.** None.
**Pace.** Good. Table 21-dominant is dense, but it is a lookup table. The worked example is exemplary: every number follows from the stated inputs.
**Outcomes.** (i) Set a limit with a known background and say what Feldman–Cousins changes: yes. (ii) Compute β_k, the band and the second-order profile cost from templates: yes, done. (iii) Treat a template of known sign and excluded cells: yes.

## 21.5 Statistics, combination and recasting
**Lost points.**
1. Eq. (21.5-C0) has a removable 0/0 whenever N_sig/x is an integer. The text handles g = 1, but the worked cases g = ½ and g = ⅓ hit the same singularity, and a naive evaluation of the printed form divides by zero, as mine did. Printing the regular form, [(kx − N)^k − k(kx − N)^{k−1}] e^{−kx}/k!, which the text already writes for g = 1, would remove the trap.
2. Possible inconsistency with Ch. 18 that I cannot resolve:
   - Table 21-dominant: two pairs at 5 eV in "17 % of events against all".
   - Sect. 21.7 and Table 21-nuisances: "about ten times fewer events in the two-pair bin than the step model".
   - If these are different cascade models (resolved seed against full band), say so where they meet.
**Reproduced.**
The counting limits 2.303, 3.890, 5.322 and 6.681, and the monotonicity argument d/dμ P(N ≤ n) = −P(n). Maximum gap (solved numerically): g = 0.9 gives 2.836, g = 0.5 gives 7.78, g = ⅓ gives 13.84, and break-even is at g = 0.761. The interval count (N + 1)(N + 2)/2. WE combine: I implemented the stated Neyman construction (constraint term held fixed, nuisance at its conditional best fit to the data). It gives: 0.928e-42 without the nuisance; 1.029e-42 with one shared nuisance; 0.976e-42 with one nuisance per exposure. All three match. The closed form for exposure A gives N₉₀ e^{k²N₉₀} = 1.12. The recast bracket. 0.9^n coverage and ln(10n). The halo recast factors 1.294, 1.222 and 1.150, and 3.49 × 1.222 = 4.27, consistent with Fig. 21.3. The Dirac recast: ×1600, giving 5.4e-43 and 8.8e-42; and ε_bg^{1/2} for ζ. The boosted flux: R^{−1/2} gives 1.04 to 4.5.
**Used before defined.** None (𝒬 comes from Sect. 10.9).
**Pace.** 21.5-corrected (Dirac re-plots and boosted fluxes) is fast and leans on Chs. 10 and 16. It reads as an application list rather than new material, which is acceptable. Minor: "combined as in Sect. 21.5-recast" is a forward reference for the per-bin combination.
**Outcomes.** (i) Set a background-agnostic limit by counting or by maximum gap: yes, done. (ii) Combine exposures with shared nuisances, and say why splitting them is wrong: yes, reproduced the 5 %. (iii) Decide whether a correction can be recast from a curve: yes, using Table 21-recast and the bracket.

## 21.6 Shared response libraries
**Lost points.** None. This section is a specification, not a derivation.
- Minor: in WE libentry, S^IP = 1.74e8 eV² at 10 eV is "interpolated", but only the node value 1.796e8 is given; the next node's ε₂ is missing. So the screening factor 0.242 can be checked only from 4.22/17.4.
**Reproduced.**
The storage sizes: 7.5e6 nodes × 12 × 8 B = 720 MB; 1.68e12 numbers (13 TB); 1.2 GB for the seeds; 1.2e7 lattice values. The ratio 0.05 eV / 1.3 meV = 38. WE libentry: 2q²/e² = 3.038e8 eV². L = 0.1442 (macroscopic) and 0.1585 (head). S = 4.38e7 eV², and ΩS = 0.2283 eV⁻¹ with Ω = 40.05 Å³. δ_X = −0.090. Linear interpolation to 10 eV gives L = 0.1390, S = 4.22e7 eV², and a ratio to the model of 0.864.
**Used before defined.** "TB09" (functional) and "Kohn–Sham states" are used as labels. Density-functional theory is not assumed for me. A parenthesis such as "(a meta-GGA functional chosen for gaps)" would suffice.
**Pace.** Slightly slow and list-like for my persona (the versioning rules, the checks paragraph). It is still useful, and the worked example makes the conventions concrete.
**Outcomes.** (i) List what a library must tabulate and why it has no velocity axis: yes. (ii) Write a table entry with its label, nuisance flag and checks: yes, following the worked example. (iii) Name the conventions that cause factor-of-order-one errors: yes (normalisation per volume or per cell, e² units, head versus macroscopic ε, the two gaps).

## 21.7 Next targets
**Lost points.** None that block.
- Minor: the threshold-in-quanta row reads cleanly only after the sentence "GaSb ... beats germanium's measured value with probability 0.83". The floor row gives 0.974 for germanium ahead of GaSb. Both are correct, but they are easy to confuse because they are two different figures of merit.
**Reproduced.**
The ratios 3.73, 1.56 and 4.4, and the surface ratio 1.79. The edges: 2.85 keV for CsI, 10.35 keV for GaAs, and 23.1 keV for the CsI nuclear edge from ω_th/(2c(v_max − c)). The background tolerances 1.48, 1.22 and 2.44, and the scaling argument. The β fractions (numerical, Eq. 21.7-beta): tritium 0.0892; ²¹⁰Pb ground state 0.0438; ²¹⁰Bi 9.67e-4; ⁴⁰K with the unique-third shape factor 4.13e-4. ¹¹⁵In bracketed at 4.7e3 to 3.9e4. 689 per kg·day·keV, 1.45 mBq/kg, and 2.00, 2.34 and 1.68 mBq per kg of Pb. Tritium 0.169 and 11.0, and germanium 0.112 and 7.31. KTaO₃: 4.6 kBq/kg and 1.5e5. ¹²³Te bound: 693 per kg per day. Compton: 1.20e-28 cm²/keV, and a fraction of 5.4e-4.
**Could not reproduce.** The mean escape path 0.448 L for a cube: stated, not derived. I accept it. All the P(first) values: these are Monte Carlo results.
**Used before defined.** None (P(first), tiers and r_mat come from Ch. 17).
**Pace.** Right for a guide. The landscape table is heavy but self-explanatory. WE csi is a good model of how to read the table.
**Outcomes.** (i) Read the guide and say what each leader still has to show: yes. (ii) Compute whether a background ratio reverses a lead: yes. (iii) Estimate a sub-keV β background per Bq/kg for a given endpoint: yes, reproduced four cases.

## Summary
- Accurate, except one sentence: "a final-state assignment that is not stochastically ordered leaks at most 0.034 of a bin". The body says something different: the leakage comes from the sector split near bin edges, and the 0.034 bound *requires* the cascade to be stochastically ordered. Reword, e.g. "the zero-phonon/phonon-dressed split misassigns at most 0.034 of a bin in silicon, if the pair number grows stochastically with the seed energy."
- The Summary also uses "semi-infinite linear program", which the body never uses.
- The chap:22 reference renders as "??" (see the chapter opening).

## Overall
I would keep reading. Every derivation I attempted closes:
- the lens, the edge power, the stream bound and its certificate;
- the profile cost, and the Neyman combination reproduced to three digits;
- maximum gap, the recast bracket, and the β and Compton backgrounds.
The worked examples are fully checkable from their stated inputs. The gaps are local: the c clash, the box lim:21.2a whose title says directional while its formula is isotropic, the unexplained right-ascension optimisation, the undefined "stochastically ordered", and the uncounted v_max^{2p+8} exponent. None of them blocks later material. The removable singularity in (21.5-C0) and the two "??" are easy fixes.

**Verdict: MINOR GAPS.**
