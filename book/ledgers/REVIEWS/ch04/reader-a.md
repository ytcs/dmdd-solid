# Ch. 4 mock-reader review: persona (a), isolated

Reader: first-year PhD student (undergrad QM, E&M, stat mech, SR; no graduate solid state, many-body or QFT).
Source: the .tex files (ch04/s4-1..s4-9, appD/D-6..D-12, appC/C-5..C-7). main.pdf (built Nov 1 23:46) is older than
the sources (edited up to Nov 2 07:12). Ch. 2 s2-5 was reread for the transition-sum and Gibbs definitions. Figs 4.7 and
4.11 were judged for pedagogy only, because they are being regenerated.
Method: I worked every derivation by hand and checked the numbers with python/scipy. Numbers that come from data
(Franta, Henke) or from the EPM code cannot be checked from the text; I list them separately and accept them.

## 4.1 Kubo formula
- Lost points: none. Trace-cyclic step, interaction picture with the full H, Lehmann form, absorbed power (4.1-power),
  static limit, oscillator, two-level system and the tail (4.1-tail) all reproduced.
- Reproduced: the reality relation (4.1-reality); Im R_aa (4.1-ImR); P = -(ω φ0²/2) V Im R; oscillator VR(ω), with n_B
  cancelling in the Lehmann check; damped poles (-0.382i ω0 at Γ=3ω0); 2λ²/Γ = 10 λ²/ω0; tanh 1 = 0.762,
  VR(0) = -1.523|O10|²/Δ; double commutator 2λ²ω0.
- Too fast: the isothermal-vs-adiabatic remark at the end of "Static limit" is one sentence; it only makes sense after 4.7.
- Outcomes: derive Kubo/Lehmann (yes); read Im R as absorption (yes); poles and analyticity (yes); tail coefficient as a
  double commutator (yes).

## 4.2 Correlation functions, S, FDT
- Lost points: none.
- Reproduced: Van Hove transform (4.2-vanhove), with the sign flip t→-t; free-electron recoil correlation e^{-iq²t/2m};
  the off-diagonal FDT (4.2-fdt) term by term, including the e^{-βω} from the i↔f relabel; spectral form (4.2-spectral);
  gas S^0 (4.2-gas), the linear/parabola junction 0.239 m k_F at 0.75 E_F, and first moment π n q²/m; Si numbers
  (k_F = 3.57 keV, E_F = 12.5 eV, v_F = 7.0e-3, S^0 on the v_max line = 2.2e8 eV² = 0.121 m k_F); e^{-βΔ} = 2e-19;
  hydrogen inelastic share 1 - F² = 0.59.
- Used before defined: none. The forward references to R^0 (4.5) are labelled.
- Too slow/fast: about right. The positivity subsection is pleasantly short.
- Outcomes: convert S↔R by FDT (yes); compute S^0 of the gas (yes, did it); bound interference by Cauchy-Schwarz (yes).

## 4.3 Causality and sum rules
- Lost points (minor): (i) "Thomas, Reiche and Thomas, and Kuhn" reads like a typo at first, until you realise "Reiche
  and Thomas" are one pair of authors; consider "Thomas; Reiche and Thomas; and Kuhn". (ii) In we:4-sifsum, "in tables now
  distributed from lower energies, which we use above 30 eV" is unclear: from which energy are the tables distributed,
  and why 30 eV? (iii) Mass-velocity paragraph: "each [1s electron] ... alone would give 8.7e-3" does not say relative
  to what. I worked out that it is the fractional reduction of that electron's own f-sum, (5/3)·2.67 keV/m_e.
- Reproduced: contour KK; folded KK; moments identity (4.3-moments), including the (-1)^k S_ba(-q) term; continuity
  (4.3-continuity); f-sum; ω_p = 16.6 / 31.1 eV; mass-velocity bracket 4p²q² + 8(p·q)² + 2q⁴ → (4.3-mv);
  K̄ = 561 eV, 1.8e-3, 0.026 e/atom; q² term 2.7e-3 at 53 keV; nuclear share 14 m_e/M = 2.73e-4; TRK hydrogen
  (python): bound 0.5650, first three 0.524, continuum 0.4350, 0.316 within E_B, 0.0042 above 10 E_B, total 1.000000;
  gas f-sum split (1 - q/2k_F)³ = 27/64; gap bound S^st ≤ q²/(2m E_g), crossover 0.24 keV, ratio 0.42 at 0.1 keV.
- Accepted, not checkable from the text: the Henke integrals 0.35 / 8.46 / 1.61 and the saturation percentages.
- Too fast: the valence-only gap bound in we:4-gasfsum quietly uses the valence share of the f-sum (n_val q²/m) before
  we:4-sifsum says how that share is collected. Acceptable, because it points forward.
- Outcomes: apply KK (yes); derive the f-sum from the double commutator (yes); check a table against TRK (yes, hydrogen
  done numerically); say when the f-sum changes (NL, relativistic) (yes).

## 4.4 Screening and the dielectric function
- Lost points: (i) Transverse tensor. "The Kubo formula with O_b = j^β then yields the induced particle current
  e[n δ/m + R̃_jj]A" is compressed: the sign of the A-coupling (charge -e, p + eA), the diamagnetic term, and why the
  response is the proper one all arrive in one sentence. I got the result (ε = 1 - e²/ω²[...]) only after redoing it.
  Two more displayed lines would fix this. (ii) Ward identity (4.4-ward): "integrate by parts twice" with stationarity
  in between. I reproduced it, including the boundary term [q·j†, n] = N q²/m (the conjugate of the 4.3 commutator),
  but it took a page. Persona (a) will likely accept it on faith.
- Reproduced: Dyson/inverse pair; S = (q²/2πα) L/(1 - e^{-βω}); ε = 1 + iσ/ω, σ1 = ωε2, Π = -iωσ; f-sum for L;
  inverse moments; Ē = 17.4 eV; TF k_TF² = 4αm k_F/π = 3ω_p²/v_F² = 1.69e7 eV², 1/k_TF = 0.48 Å, ε_TF(q0) = 2.22,
  factor 4.9, crossover 1.26 keV; stopping formula (4.4-dEdx) prefactor; oscillator model: f-sum, inverse moment,
  resonance 5.08 eV, peak 4.34; slow-particle friction (∫x²/(1+x⁴)² = π/8√2) 0.181 eV/Å vs the full integral 0.186
  (+3%) and +22% at v_max (python); L_model(3 eV) = 0.035.
- Used before defined: the f-sum for ε2 (4.4-fsumeps) leans on "removing one Fourier component" (sec 4.8-removal), four
  sections ahead. The C.5 KK route is offered as an alternative, so this is not blocking.
- Accepted: Franta values (ε2 = 2.4, L = 3.1e-3 at 3 eV, peak 4.5 at 16.4 eV, 96%/92%).
- Typo: Fig. 4.5 caption, "Dashed: the single damped oscillator ... at q = 0 (dashed)" says "dashed" twice.
- Outcomes: go from R to ε, ε_mac and L (yes); explain why ε_mac ≠ ε_00 (yes, the capacitor picture in 4.6 helps);
  estimate TF screening and its failure in Si (yes); state when S ∝ L holds (yes).

## 4.5 Homogeneous electron gas
- Lost points: none. The Lindhard derivation in D.8 is complete enough to redo.
- Reproduced (python, from 4.5-lindhard): q_c = 0.7297 k_F = 2.605 keV, ω_pl(q_c) = 24.84 eV; ω_pl(0.3 k_F) = 17.65 eV;
  at q0, v_max: ω = 9.88 eV, |ε|² = 3.963, L = 0.1833; ε_Lin(q0,0) = 2.10; plasmon share 0.99997 (0.1 k_F) and 0.957
  (0.5 k_F); perfect screening 0.9925; naive vs Mermin static at 0.3 k_F, 1 eV: 12.83 vs 15.67. By hand: the moments
  ⟨Δ³⟩, ⟨Δ⁵⟩ → 12/175; α_pl = 0.45; r_s = 2.0; k_TF²/k_F² = 0.663 r_s; F_L series and the 4k_F²/3q² tail; plasmon weight
  πω_p/2; S^st → q²/2mω_p; the corner L ≈ e²m²qω/(2πk_TF⁴); Drude limit; Mermin tail γω/ω_p² vs naive 2γω/ω_p²;
  peak ω_p/γ = 4.54; L_Mer(3 eV) = 0.042.
- Used before defined: "Matsubara bubble eq:4.7-bubble" (labelled forward); "Kohn anomaly" and "Friedel oscillation"
  are named only in passing. Harmless.
- Too slow/fast: we:4-siplasmon "Position" argues well but quickly; the 87% / rms 6.5 eV come from data (accepted).
- Outcomes: evaluate Lindhard limits (yes); derive the RPA plasmon dispersion (yes); explain Landau damping and q_c
  (yes); say why the plasmon is kinematically out of reach for DM (yes, 6.27 keV); Mermin vs naive (yes).

## 4.6 RPA, local fields, TDDFT
- Lost points: (i) "The head and wings are computed analytically" uses "wings" for the first time. "Head" was
  introduced in 4.4; "wings" is never defined before D.7. Add "(the elements with one index 0)". (ii) Typo in
  we:4-siepsinf: "ε∞ = 10.22, and and with 113 vectors".
- Reproduced: crystal bubble (4.6-R0), including the Pauli cancellation; head (4.6-head) → ε2^IP and ε1^IP(0) with the
  1/Δ³; scissor argument; TDDFT Dyson and R̃ = (1 - R0 f_xc)^{-1} R0 (checked R^{-1} = R0^{-1} - f_Hxc);
  G_LF ↔ f_xc; compressibility rule; f_x = -e²/4k_F²; 1/(1 - 0.267·1.33) = 1.55; ε(q0,0) = 2.62 with G = 0.29;
  ratios 11%, 6%, ~half, (11.45/10.22)² = 1.25.
- Accepted: EPM numbers (11.45/10.22/10.81, peak heights). Figure under regeneration.
- Fig 4.7 pedagogy: good. Panel (b) with "unscreened ε2" against L shows the 1/|ε|² suppression at once.
  Suggestion: mark the DM window (ω ≲ q v_max, a few eV) on panel (b), because the text says "panel (b) shows what dark
  matter sees".
- Outcomes: write the Adler-Wiser matrix (yes); explain local fields by the capacitor picture (yes); say what ALDA can
  and cannot do (yes); use the rung spread as an uncertainty (yes).

## 4.7 Green's functions
- Lost points: none blocking. This is the densest new material so far (H_μ, anticommutator, T-ordering, Matsubara), but
  each step is shown.
- Reproduced: Lehmann form of G^R; normalisation and A n_F for removal; time-ordered Lehmann form with -i0 removal
  poles; EOM → Dyson; Im G(z) < 0 in the UHP; Im Σ ≤ 0; Σ(∞) = ⟨{[c,H_int],c†}⟩; quasiparticle z, Γ; level model:
  Σ_d = (Γ/2π) ln(...), slope 2Γ/πE_w = 0.0064, peak 63.7 eV⁻¹, Lorentzian weight outside the band 0.0064;
  occupation 0.78749 (python, ∫A n_F; sum rule 1.000000) vs n_F = 0.818; Matsubara integral and (p_i + p_f) weight;
  bosonic R(iω) with the β term; contour residue of n_F = -T.
- Too fast: "The real-time time-ordered function ... has no such expansion at T > 0" is asserted. D.11 explains it; a
  pointer to D.11 there would help.
- Outcomes: compute G^R and A of a solvable model (yes, the level); read a quasiparticle from Σ (yes); do a fermionic
  Matsubara sum by contour (yes); continue R(iω_B) to R(ω) (yes).

## 4.8 Feynman diagrams
- Lost points: (i) On a first pass the rules box is a list to accept. "Each closed loop gives -1 ... comes from the last
  contraction" and the response-function sign paragraph ("2n+2 propagators ... the -1 of each contraction drops out")
  were not followable without D.11. With D.11 I reproduced both, and checked the bubble sign directly by Wick:
  R0(τ) = (1/V)Σ G0(k+q,τ)G0(k,-τ). Suggest one sentence: "read D.11 now if the signs are unfamiliar." (ii) Removing
  one Fourier component (sec 4.8-removal): I follow the bridge argument, but "relative amount of order 1/N" for loop
  momenta is asserted. Fine for (a), who will trust it.
- Reproduced: the first-order chain R0 v R0 (value and sign); the boson self-energy (4.8-sigmaboson), all three residues
  including n_B(iω_F - ξ) = -(1 - n_F); Einstein example -9.14 meV, slope -0.0500, z = 0.952, self-consistent
  -8.73 meV, n_B = 0.109, Γ_qp = 2.08 meV (0.32 ps), -11.09 meV (0.4% from (2n_B+1)×), 24.4 meV, n_F ≤ 4e-9; GW
  lifetime (4.8-lifetime) with B odd and (1 - e^{-βω})(n_B+1) = 1; cutting-rule factorisations and Γ_in = e^{-βω}Γ_out;
  ω_+ = 39.7 eV at q0.
- Used before defined: "Ward identity" (4.4) is named here, but 4.4 never called eq 4.4-ward that.
- Outcomes: evaluate a one-loop diagram with the rules (yes, bubble and boson Fock); identify RPA as the bubble chain
  (yes); read Im Σ as a rate (yes); write G0W0 in words (yes; a full GW calculation was not attempted).

## 4.9 Excitons and BSE
- Lost points: (i) Notation clash. Eq 4.9-kernels defines K^x as the sum over G ≠ 0, and the text then says 4.9-bse "is
  D.12-eig with the kernels of D.12-crystal", where K^x sums over all G (D.12's barred K̄^x is the G ≠ 0 one). I spent
  time reconciling 4.9-S (divided by |ε_mac|²) with D.12-S (not divided). Fix: write K̄^x in 4.9, or say "with K̄^x".
  (ii) "The Woodbury identity then turns the resolvent ... into the solution of R̄ = R0 + R0 v̄ R̄". Not shown. I did
  it myself: X†(ω - D - gXX†)^{-1}X = M(1 - gM)^{-1} with M = X†(ω - D)^{-1}X. That is two lines the text could include.
  (iii) "LO-TO splitting" (here and in D.12) is used before ch. 5 defines it. Add a half-sentence gloss.
- Reproduced: WM reduction to hydrogen; Si spherical bracket 13-19 meV (m_e 0.26, m_h 0.28-0.72); μ_x = 0.148,
  a_x = 4.2 nm ≈ 7.7 a, 1/a_x = 0.024 Å⁻¹ vs |G_111| = 2.00; GaAs 21.9 → 5.24 meV, 12.6 nm, 22 a; ε0: 3.73 meV,
  15.0 nm; COM separation (4.9-dispersion); ε_mac, ε2 and static (4.9-eps2) reduce to 4.6-eps2/4.6-static;
  Elliott Σ_k A = V^{1/2}F(0); S lines.
- Numbers to recheck after the Fig 4.11 regeneration: "rises by 17 percent ... applied to 10.22 ... about 11.9", but
  10.22 × 1.17 = 11.96 ≈ 12.0. Either the percentage or the result needs adjusting. Also the 36% (L at 3 eV), 34 at
  3.36 eV, and 81 meV.
- Fig 4.11 pedagogy: the caption explains why the whole spectrum shifts down (double counting by the fitted bands) and
  why the tails sit below 3 eV. Good; the caption is long, but each clause earns its place.
- Outcomes: write H^exc and explain each kernel's sign (yes); derive WM binding and radius (yes, Si and GaAs);
  explain oscillator-strength transfer (yes); set up a BSE numerically for a toy model (not attempted).
  The chapter summary is consistent with the body.

## Appendices D.6-D.12, C.5-C.7
- D.6: the second-difference formula (D.6-dc), current, species, NL expansion → -i[q·r, q·v], mass-velocity, and
  virial K̄ = -E/Z. All reproduced.
- D.7: push-through; R^{-1} = R̄^{-1} - v0 and the head closing on itself; small-q orders O(q²)/O(q)/O(1);
  the symmetrised ratio |q+G|/|q+G'|. Reproduced. This is where "wings" is first made clear.
- D.8: angular/radial integrals, I(w) = w + (1-w²)ℓ/2, Im steps, the small-y form (I' = 2 - wℓ), high-ν series
  (2/3w + 2/15w³), and the f-sum integral. Reproduced.
- D.9: the Mermin algebra (partial fractions → 4.5-mermin) and the continuity sum with -D_k = q·(k+q/2)/m. Reproduced.
- D.10: antiperiodicity by trace cycling; symmetric value n - 1/2; bubble by direct τ integral and by residues.
  Reproduced.
- D.11: Gaudin proof; linked-cluster factorisation; loop sign; n!2^n; T = 0 factor i^n(-1)^F; Fock check closing
  the contour in the UHP; boson D0 transform. Reproduced. Heavy but complete; for persona (a) this appendix is required
  reading for 4.8, not optional.
- D.12: the index placement of K^x and K^d checked against the crystal vertices (ρ_{c'c}(k+q,p+G)*, ρ_{v'v}(k,p+G'));
  singlet g_deg; the D.12-eps2 prefactor 8π²α/(Ωω²). Reproduced. The four-spin-orbital numerical check is a nice touch.
- C.5 (n q²/m moment, folded KK, (2n_B+1)/2ω0), C.6 (BCH, Bloch), C.7 (Woodbury; E_b = 0.8, sinh²θ = 0.125): reproduced.

## Steps I could not reproduce
- None of the derivations. Unverifiable from the text, and accepted: the Henke integrals; the Franta optical values; the
  EPM/BSE model numbers (figures under regeneration); the numerical-convergence claims (1e-5, 1e-6, 0.6% rms MC).

## Overall
I would keep reading. Sections 4.1-4.6 are the clearest treatment of linear response I have met: every key result is
derived, then checked on a solvable model, and the silicon numbers keep it anchored to dark matter. Sections 4.7-4.9
change gear. Green's functions, Matsubara sums, Wick and the ladder are all new to persona (a). They are derivable, but
only with D.10-D.12 open alongside, and three places (the 4.8 sign rules, the 4.9 Woodbury step, the 4.9 K^x notation)
cost real time. None blocks what follows: the physics conclusions (RPA = bubble chain, Im Σ = rate, BSE = attraction
on top of local fields) come through even if the reader skims the signs.

Verdict: **MINOR GAPS**. Fixes, all small:
1. 4.9: write K̄^x (or say "with K̄^x") so it matches D.12.
2. 4.9: show the two-line Woodbury reduction.
3. 4.8: point to D.11 before the rules box.
4. 4.4: add two lines to the transverse-tensor/Ward step.
5. Define "wings" at first use in 4.6. 6. Gloss "LO-TO" in 4.9.
7. Fix the typos: "and and" (4.6), duplicated "(dashed)" (Fig 4.5), TRK author list (4.3). 8. Recheck 17% → 11.9 (Fig 4.11).
