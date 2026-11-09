# Ch 7 mock-reader review, persona (a), isolated
Read: tex/ch07/{ch07,s7-1..s7-4}.tex plus appD/D-19..D-23.tex (the PDF of Nov 1 23:46 predates the sources, so I read the .tex). Checks run in sympy, scipy and exact diagonalization.

## 7.1 Magnetic order and spin waves (+ D.19)
**1. Lost points**
- D.19, "The spin operators": "Near k = 0 both coefficients diverge as (A_0/2ω^M)^{1/2}". With ω^M = |S|(A²−B²)^{1/2} (D.19-omega) I get u² ≈ |S|A_0/(2ω^M), so a factor |S| is missing. It does not matter for |S| = 1, but I lost time on it. Fix: write (|S|A_0/2ω^M)^{1/2}.
- D.19 cites its own Hamiltonian and result as eq:E.9-heis and eq:E.9-afm, which are in an appendix I have not read, not 7.1-heis and 7.1-afm. For a moment I thought the conventions might differ. Fix: cite 7.1 as well, or say "identical to".
- The two-magnon numerics ("Leaving out the one-magnon states with all spins rotated together") took a second reading. I reproduced them once I understood that this means "drop the descendants S_tot^- of lower multiplets", including the one from |F>. One clause saying that would help.

**2. Steps I could not reproduce:** none. Every step checked:
- the singlet and triplet energies of H_12;
- J = 4t²/U − 2K, and t/U = 0.048–0.064 from J_2 with U = 4.6–8.2 eV;
- the HP commutator, the one-bond expansions (ferromagnetic and antiferromagnetic), and ω^M(k) and E_cl for the ferromagnet;
- the ferromagnetic chain: the exact one-magnon state, and by exact diagonalization 0.3277|J| (S=½, N=10) and 1.0827|J| (S=1, N=8) against linear spin-wave values of 0.382 and 1.172;
- A_k, B_k, ω^M = |S|(A²−B²)^{1/2} and E_0 from C.7;
- the small-k law 2√3 J_2|S|ak, the [111] law 2√3(J_1+J_2)|S|ak and the D.19-linear bracket;
- the velocity 274.6 meV·Å = 1.39e-4 = 41.7 km/s;
- the ferromagnetic S_ab, including the iε_abc sign from S_ab = ⟨O_a†O_b⟩ and its eigenvalues 2 and 0;
- the weights (u ∓ v)², the ordering wavevector |Q| = 1.30 Å⁻¹ = 2.6 keV, and m_χ ≳ 0.49 MeV.

**3. Used before defined:** Wigner–Eckart theorem (not in my undergraduate QM; a footnote would do). "Néel temperature" appears in the first sentence and is defined only by context. The DFT+U and frozen-magnon references go to App E.9, which I have not read; they are asides and not blocking.

**4. Pace:** about right. The kinetic-exchange paragraph is dense but complete. The antiferromagnet subsection is well paced because D.19 does the bookkeeping.

**5. Learning outcomes (inferred), can I do them?**
- Derive the Heisenberg coupling from Coulomb exchange and kinetic exchange: yes.
- Find the linear spin-wave dispersions of a ferromagnet and a two-sublattice antiferromagnet: yes. I built J_AA and J_AB for type-II fcc with J_1 and J_2 myself. Small-k slopes over 2×10⁴ random directions range from 254.8 to 269.2 meV·Å (254.8 along [111]), and a random scan gives a zone maximum of 118.17 meV = |S|(6J_2 − 3J_1). Both match the text.
- Write the one-magnon spin response and say where the antiferromagnet's weight sits: yes.

**6. State:** confident, keep reading.

## 7.2 Superconductivity (+ D.20, D.21)
**1. Lost points**
- Threshold of the pair spectrum: "Near the threshold the integrand is ±Δ² times the product of the two edge divergences". Read literally this gives π/4 for case I, not π/2. The numerator is E(ω−E) ± Δ² → Δ² ± Δ², that is 2Δ² for case I and 0 for case II. Then 2Δ²/(2Δ√…) integrated gives πΔ, and dividing by ω = 2Δ gives π/2. Fix: "the numerator tends to Δ² ± Δ²".
- "the ratio [Δ/v_F q] is at most v_max/2v_F = 0.20 … and it falls as the mass grows", followed by the worked example's 0.10 at the threshold mass. This confused me. The bound 0.20 is approached only as m_χ → ∞, because the smallest q for a given deposit decreases toward ω/v_max as m_χ grows. So the *maximum* ratio rises with mass and only the *typical* ratio (q ~ m_χ v) falls. Fix: say "the typical ratio falls".
- One inconsistency: D.21's gap equation is written for the reduced shell sum, while the q = 0 cancellation also uses V^{-1}Σ'1/E = 2/V_BCS. That is fine, but 7.2 should say once that all bubbles carry the shell restriction (D.21-R0 drops the prime).

**2. Steps I could not reproduce**
- Eq. 7.2-NVren, (λ−μ*)/(1+λ): it relies on eq:E.9-Z, eq:E.9-lambda and eq:E.9-Delta, which are outside my reading. I accept the 1/(1+λ) from the residue argument and take μ* on trust.
- Taken on trust as stated numerics: Anderson–Bogoliubov c = 0.579 v_F, the f-sum violation staying within 0.2 % up to v_F q = 20Δ, and the 48×48 lattice checks. These are not derivations.
- Reproduced:
  - the static pair term −2|g|²/(Nω);
  - the Cooper binding and its value, 2·40 meV·e^{−2/0.164} = 0.40 μeV;
  - the eigenvectors (u, −v) of h_k, γ_k1 annihilating |BCS>, b_k = uv, and the gap equation;
  - the T_c Matsubara sum, including the H_n asymptotics and ∫r(t)/t = 0;
  - all four coherence amplitudes, by inverting γ and relabeling;
  - the cohE identities;
  - S_n = 2πN_Fω/v_Fq = m²ω/πq and the pair-spectrum reduction;
  - the ratios at 4Δ: quadrature gives 1.2111 and 0.6719 (text: 1.21 and 0.67);
  - [s_1, η] = −2i s_2;
  - the q = 0 bubbles from the Pauli-trace identities, including the sign of R0_{s2η};
  - the cancellation (7.2-cancel);
  - γ_2 = −2iΔ/ω and the Ward-identity check;
  - the spurious-moment ratio 12Δ²/(N_F V v_F²q²) with n = (4/3)N_F E_F, crossing 1 at 8.55Δ;
  - the aluminum numbers: Δ = 0.179 meV, m_min = 0.10 keV, q = 0.27 eV, 1/q = 0.73 μm, pair size 2.3 μm, N_F V = 0.164 and 0.180, T_c = 54, 20 and 5.85 K, the factor 4.9, and the exponent −208 at 10 mK.

**3. Used before defined:** μ*_C and the "Eliashberg equations" (App E.9). The Ward-identity paragraph uses "dressed vertex", "amputate the two outer propagators" and "three-point function", which Ch 4 has not given me in this form. I followed the algebra but not the meaning of "remove the two outer propagators".

**4. Pace:** coherence factors and the pair spectrum are well paced. The Nambu and conserving-response subsection is fast for a reader with no field theory: the claim that mean-field dynamics in a Wick state is conserving carries a lot in two sentences. The explicit q = 0 cancellation rescues it, and D.21 gives the argument in full.

**5. Learning outcomes**
- Relate N_F V_BCS to λ_ep: yes.
- Solve the BCS model for E_k, the DOS, Δ(0), T_c and 1.764: yes.
- Compute case I and case II pair spectra and explain the jump and the rise: yes; see the quadrature above.
- Explain why the bare bubble violates the f-sum rule and how the phase mode repairs it: yes at q = 0. At finite q I would need D.21 open.
- Al threshold mass: yes, 0.10 keV.

**6. State:** worked hard, kept up.

## 7.3 Dirac and narrow-gap materials (+ D.22)
**1. Lost points**
- Kinematics: "the slope of the continuum edge never falls below v_D". This is false: dω/dq = v_D²q/ω < v_D everywhere on the edge ω = (v_D²q² + 4Δ²)^{1/2}. The conclusion still holds because the edge lies above v_D q and the dark-matter curve lies below v_max q. The chapter Summary states it correctly ("never rises more slowly than v_D q"). Fix: "the edge never lies below v_D q".
- The expansion parameter is written two ways: ln(v_DΛ_D/max(Δ_D, v_D q)) in the text, and ln(v_DΛ_D/2Δ_D) in we:7-zrte5, which gives 0.66 there. The first form would give 0.93. Fix: pick one.
- The Kramers/M-matrix paragraph: "any rotation of four-dimensional space can be produced in this way" (SU(2)×SU(2) → SO(4)) is asserted. I believe it but could not have supplied it. A pointer or a one-line justification would help.

**2. Steps I could not reproduce:** none blocking. Reproduced:
- MM† ∝ 1 → N_i = z_i + i c_i·σ, and the N N† identity;
- the Kane mass m_e E_g/E_P = 0.066, v = 4.7e-3 = 1.78 v_max;
- the DOS and the edge mass 0.053 m_e;
- n_c ≈ 1.0e-5 cm⁻³ at 4 K (Δ/T = 45.3);
- the pair edge (convexity argument);
- threshold masses by direct scan: 10.49 keV (v = 7.6e-4), 9.39 (4.4e-4) and 12.67 (1.1e-3), plus 8.9 keV in the flat limit;
- in D.22:
  - the overlap 𝓕 = (v²q² − D²)/4EE';
  - the region boundary: the sympy identity 4k²k'² − (k²+k'²−q²)² = q²(S²−q²−4Δ²) − D²(S²−q²) holds exactly;
  - ∫dD = (4/3)v³q³ρ and the prefactor q²/24π²v;
  - the b-substitution giving ln(U/Δ²) − 5/3;
  - the Feynman-x representation, Im ε and the gapless limit with ∫x(1−x)ln[x(1−x)] = −5/18;
- the ZrTe5 numbers: v_D = 7.61e-4, ε_bg = 50.5, α̃ = 0.190, Λ_D = 236 eV, and Dirac fractions 0.0930, 0.0813 and 0.0527 at q = 0, 41 and 118 eV;
- the anisotropic additions 9.8, 1.57 and 6.7, couplings 0.065, 0.155 and 0.109, and the limit-box residuals 0.098 (7.5Δ), 0.094 (3.7Δ with correction) and 0.003 (10Δ).

**3. Used before defined:** "vacuum polarization of QED", "running of the fine-structure constant" and "Lorentz invariant" with v_D are used as analogies I cannot check without QFT, but nothing depends on them. "Weyl node" and "chirality" are defined in place (fine).

**4. Pace:** the M-matrix reduction is too fast; it compresses a page into a paragraph. The screening subsection is well paced because D.22 is complete and self-contained; it was the most satisfying appendix.

**5. Learning outcomes**
- Derive the Dirac Hamiltonian from two-doublet k·p theory: mostly; see the SO(4) step.
- Write its DOS and thermal carrier density: yes.
- Find the pair continuum and the threshold mass: yes, 10.5 keV.
- Write ε(q,ω) with ε_bg and α̃, and evaluate it for ZrTe5: yes; see the numbers above.

**6. State:** confident.

## 7.4 Defects and dopants (+ D.23)
**1. Lost points**
- D.23: "The orbit is a prolate spheroid, flattened along the heavy axis". With radii 24.3, 24.3 and 14.0 Å the spheroid is oblate. The text contradicts itself ("flattened"). Fix: "oblate".
- we:7-sip uses `a` for the Si lattice constant ("volume a³/8") and two paragraphs later for the envelope radius ("1/a = 81 eV", "qa ≈ 0.42"). I had to work out which one each time. Fix: rename the envelope radii (a_⊥, b_∥, say).
- we:7-sip: "the measured 1s triplet of phosphorus, A_1 …, T_2 …, E …" calls three levels a "triplet", in the same breath as the T_2 triplet. Fix: "the three measured 1s levels".
- Summary: "Effective-mass theory gives 29.7 meV for every donor", but the body argues that 11.4 is the right ε_0 and uses 31.3 meV for the central-cell correction. Fix: quote 31.3 there, or "29.7–31.3".
- D.23 writes U = −e²/(4πε_0 r) with ε_0 = 11.7. To me this looks exactly like SI vacuum permittivity. Fix: −α/(ε_0 r) alone, or use another symbol.

**2. Steps I could not reproduce**
- Taken on trust: the coupled-radial solution 1.566 Ry*_⊥ (l ≤ 14) and the 11.4-ε levels 11.51, 6.42 and 5.49 meV. The 1/ε² rescaling of 10.92 and 6.09 does give 11.50 and 6.415.
- Reproduced:
  - the scaled anisotropic Coulomb factor;
  - the D.23 variational energy: minimizing gives −1.5642 Ry* at a = 24.26, b = 13.95 Å, i.e. 29.69 meV;
  - ⟨1/r⟩ = arcsin e/(a e);
  - ε_0 = 11.41;
  - the valley-orbit eigenvalues and Δ_f, Δ_0, Δ_g = −2.17, −4.09 and −1.51 meV;
  - the spheroid volume 3.46e-20 cm³;
  - |F(0)|²a³/8 = 7.76e-4 with the unrounded radii (7.71e-4 with the rounded ones);
  - m_χ ≥ 13.0 keV and q = 34.4 eV;
  - the Poisson weights 0.23, 0.34, 0.25 and 0.12; e^{−3.85} = 0.0213; the strongest line at p = 3 (0.2025 vs 0.195 for p = 4);
  - the E³ photon average 0.677 → 0.031, and −ln 0.032 = 3.44;
  - the Stokes shift 0.49 eV;
  - the recoil masses 0.153 and 0.26 GeV;
  - the T-center and NV threshold masses and momenta;
  - e^{−27.6} = 1e-12 and e^{−1.16e5}.

**3. Used before defined:** the irrep labels A_1, E and T_2 (no group theory assumed). They are glossed as singlet, doublet and triplet, which suffices. "Debye–Waller factor" in its color-center sense is handled well.

**4. Pace:** the shallow-donor opening re-explains donors and acceptors at length; it is slow after 4.9 and 3.3. The displacement subsection is descriptive, which is fine because nothing there is derived.

**5. Learning outcomes**
- Solve the EMT donor, isotropic and variational: yes.
- Extract the valley-orbit elements from a measured 1s multiplet: yes.
- Turn S_HR into zero-phonon fractions, with the E³ correction: yes.
- Give displacement thresholds and the dark-matter masses that reach them: yes.

**6. State:** confident.

## Overall
I would keep reading. Every derivation in the chapter body and in D.19–D.23 reproduced, including all the numbers in the four worked examples. The appendices are complete enough to stand in for the steps the chapter compresses. Nothing I found blocks later material. The real defects are a handful of local slips:
- a false slope statement in 7.3 (the conclusion survives);
- a garbled threshold sentence in 7.2 that gives π/4 if taken literally;
- an ambiguous "falls as the mass grows" in 7.2;
- "prolate" for an oblate orbit in D.23;
- a missing |S| in D.19;
- an `a` clash in we:7-sip.

The hardest passages for this persona are the k·p reduction to the Dirac form and the Nambu/Ward-identity paragraph, which assume more comfort with group theory and diagrammatics than Chapters 1–6 gave me. The only step I had to take on faith is 7.2-NVren, which rests on App E.9.

**Verdict: MINOR GAPS**
