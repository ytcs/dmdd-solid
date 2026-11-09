# Chapter 2 mock-reader review: personas (b) and (c)

Read: build/main.pdf (pdftotext -layout), Chapter 2 pp. 45–88, Appendix A.1–A.9, D.2, D.3, and Chapter 1 for
cross-references. I worked every derived step by hand and checked the numbers with mpmath and sympy.
**Applies to both personas.** About 35 cross-references in Ch. 2 print as "??" (74 "?" pairs, counting "????"), and
so do about 18 in App. A/D. Most point to Chaps. 3–7 and App. C, which are empty in this build. Some of them were
meant to carry a proof. These are listed once here and not repeated per section.
- p. 47 "du sin²u/u² = π (??)" and "Eq. (2.4) ... which ?? proves";
- p. 52 the δ(g(x)) rule (??); p. 54 Σ_m|Y_lm|² (??); p. 55 the angular integrals 4π sin(qr)/(qr) and 4πi j₁ (??);
- p. 77 Sokhotski–Plemelj "which ?? proves for the general case"; p. 78 "?? collects these definitions";
- p. 49 "?? evaluates the target operators for each boson"; p. 54–55 "?? defines S(q, ω) for any target".
Persona (a) would need these. For (b) and (c) the results are standard, so none of them blocks.

## Persona (b): particle physicist (QFT, no solid state)

### 2.1 Fermi's golden rule
- Lost points: none. Eqs. (2.1)–(2.9) reproduce, including the integration by parts with Si(z) and the long-time
  bracket π/2 − 2/(E_w t). The 90.3 % central-peak fraction checks (0.9028), and so do Γ = 10.0 meV, 0.66/0.84/66 fs,
  8.3 ps and 1.52×10¹³ s⁻¹.
- The box ↔ relativistic bridge (p. 50–51) is the best paragraph in the chapter for me. ⟨f|H′|i⟩_rel = −M(2π)³δ³ is
  consistent with S = 1 + iT; ⟨f|H′|i⟩_box = −M δ/[V Π(2E)^{1/2}] reproduces the 2→2 phase-space formula; and
  |M|² = 16m_χ²m_e²|Ṽ|² checks.
- Used before defined: "Dyson series of the interaction picture" (p. 46) appears before Sect. 2.4.1. That is fine for me.
- Too slow: 2.1.1–2.1.2 is textbook for me, but it is right for persona (a). Too fast: nothing.
- Small physics gap: p. 48 says the diagonal element Ṽ(0)/V "for a massive mediator vanishes as the volume grows".
  The massless case (Ṽ(0) → ∞, cured by neutrality) is not mentioned, though 2.3.8 later handles exactly this.
  One clause pointing forward would close it.
- Outcomes: derive the golden rule and state the window (2.7): yes. Track V through a rate and convert it to σ: yes.
  Map the box element to M: yes.

### 2.2 Born approximation and form factors
- Reproduced: (2.14)–(2.16), Rutherford, (2.17)–(2.20), with the angular average Θ/(2qv) giving (1/2π)∫q dq.
  The gas S(q,ω) = 2πn_T Σ… matches (1.52). F₁s (2.21), ⟨r²⟩ = 3a₀², the half points 1.29 / 0.87 / 2 and 0.64/0.41/0.59
  all check. |f₁s→2p|² = 72x²/(9/4+x²)⁶ checks numerically against the direct overlap. Its small-q slope 2¹⁵/3¹⁰, its
  peak 0.084 at 0.67 and its value 0.061 at q₀ also check. Plane-wave (2.24) reproduces, including the 2(2l+1) spin
  count.
- **Error (kinematics).** p. 59: "A bound electron moves with a typical speed ∼ α, a hundred times the dark-matter
  speed". In fact α/v ≈ 7.3 at v = 10⁻³, 8.7 at 250 km/s and 2.8 at v_max. The book itself gives v_F = 7.0×10⁻³ =
  2.6 v_max (p. 85). The same "hundred times" is in Ch. 1 (pp. 18, 22). It should read "about ten times".
- **Numerical slip.** p. 59 WE 2.3: at m_V = 30 MeV "the difference is 3 × 10⁻⁸". From the book's own formula I get
  2.3×10⁻⁸ (≈ (2q₀² − q_max²)/m_V²). The other values (1.015, 2.63, 192, q_max = 2.69 keV = 0.72 q₀) check.
- Too fast: p. 56, "The sum over final states at fixed ω is |f_ion|²/4 per unit ln E_ej". The step from d/dω in (2.20)
  to d/d ln E_ej in (2.23) uses dω = E_ej d ln E_ej. That step is left implicit, and I had to redo it to see that the
  1/E_ej cancels. One sentence would fix this.
- Too fast: Fig. 2.3 ("exact Coulomb continuum states"). The partial-wave sum is not given, so I cannot reproduce
  0.46 or 0.036. I accept it as a quoted result.
- Used before defined: "Hartree–Fock orbitals" (p. 58; defined in 2.3.7) and "Roothaan–Hartree–Fock" (never defined).
  "Dynamic structure factor" (p. 54) is sent to "??", although Sect. 2.5 (Eq. 2.67) and App. A.7 define it. Point there.
- Helm (2.28), R_nuc = 3.47 / 4.77 fm, first zeros 256 / 186 MeV, F² = 0.998 / 0.89 / 0.36 (Si) and 0.0019 (Ge at
  100 GeV), and σ_N/σ_p = 953 / 3100 all check. The dR/dE_R derivation reproduces.
- Outcomes: derive σ̄_e as a free cross-section: yes. Write (2.18) for a bound target: yes. Compute hydrogen form
  factors: yes. Explain A² and when F_N matters: yes. Derive (2.23): yes, after supplying the Jacobian.

### 2.3 Second quantization
- Reproduced: (2.31)–(2.33), the Heisenberg phase e^{iEt}c†, the two-orbital bond expansion, (2.41) via normal
  ordering, (2.44)–(2.46), the HF energy, the jellium k = 0 cancellation (N²/2 − N² + N²/2 = 0, leaving −N v_C(0)/2V),
  the cross-term doubling in (2.48), and ⟨p−k|U₁|p⟩.
- Too slow for me: 2.3.1–2.3.3 (Slater determinants, ladder operators). This is fine for persona (a). The plane-wave
  Coulomb section 2.3.7 is pitched well.
- Used before defined: "Bloch states of ??" and "crystal momentum (??)" are both dead links. I can manage.
- Outcomes: write any one- or two-body operator in Fock space: yes. Derive H_ee in momentum space with the
  self-energy removed: yes. Read off momentum conservation: yes.

### 2.4 Second-order processes
- **Sign error.** p. 72, the inner integral of 2.4.2. The text prints
  ∫_{−∞}^{t₁} dt₂ e^{[i(E_m−E_i)+1/τ_s]t₂} = −i e^{…}/(E_i − E_m + i/τ_s). The correct value is **+i**e^{…}/(E_i − E_m +
  i/τ_s): 1/(iΔ + 1/τ) = i/(−Δ + i/τ), and I checked this numerically. With −i the second-order amplitude would come
  out as −A₂ and T = H′ − ΣHH/(…). The final A₂ and (2.52) are correct, and D.3 (D.12) gets the sign right, so the
  slip is in the displayed intermediate only.
- Reproduced: the three switching-rate Lorentzians, including the cross-term contour 2πi(3/τ)/(3i/τ) = 2π;
  S = δ − 2πiδT; the optical theorem Γ = −2 Im T_ii; the polarizability combination 2Δ|O|²/(ω² − Δ²); the finite-part
  expansion (2.60), including −πΓ_w w″(0)/4. WE 2.6 checks throughout: −0.833 eV⁻¹, 6.9×10⁻¹³ eV = 1.1×10³ s⁻¹,
  factor 16, |A|² = 4.0×10⁶, 4.7 ppm, 0.04. The broadband checks also work: exact 2.410×10⁵, δ term 2.507×10⁵, −1/σ²,
  the remainder +313 closing the gap, and 4753 / 41 % at 30 meV.
- Used before defined: Γ_w appears on p. 73 ("t ≫ 1/Γ_w") before 2.4.4 defines it.
- Mild mismatch: WE 2.6 absorbs two photons, while Eq. (2.54) and Fig. 2.5 are written for absorb + emit. The text
  says "we use the language of Eq. (2.54)", but the denominators differ (ω₂ enters with + sign). Say so explicitly.
- Outcomes: derive (2.52) and the Lippmann–Schwinger form: yes. Enumerate time orderings: yes. Regularize a resonance
  and split the rate into cascade + finite part: yes.

### 2.5 Thermal states and detailed balance
- Reproduced: (2.66), (2.67) with S = (2π/V)S_ne, the reduction to (1.52), (2.68), (2.70) and the F-D identity, WE 2.7
  (0.109, 10.2, 2.5×10⁻⁷⁶, 9.1×10⁻⁶, 1.27/1.79, 1.22, the first moment |λ|²ω₀), (2.71) with k_F = 3.57 keV,
  E_F = 12.5 eV, v_F = 7.0×10⁻³, N_F = 9.2×10⁷ eV², and the lens fraction (2.72), including 7.8 % at 0.1 q₀.
- Used before defined: "f-sum rule of ??" in WE 2.7. App. A.7.4 states it, so point there.
- Outcomes: average the golden rule over a Gibbs state: yes. Prove detailed balance: yes. Use n_B, n_F and
  Pauli blocking in a rate: yes.

### Appendices A, D.2, D.3 (as pointed to)
- A.3.1 retarded transform, A.7 (A.33), (A.37), (A.40), A.8 (A.43)–(A.45) and A.9 (A.47)–(A.48): all reproduce. The
  ω_p = 16.6 eV and the unit table entries (7.6835×10⁻¹⁵ eV³, 3.718×10⁻⁵⁹ …) check.
- A.8.3 says "Eq. (A.31) absorbs the remaining 2π/V (Sect. 2.2)". The thermal golden rule is in Sect. 2.5 (Eq. 2.67).
- D.3: K(τ) for the flat band, Laplace inversion, R(z) = (Γ/2π) ln[(z+E_w/2)/(z−E_w/2)], R′(0) = 2Γ/(πE_w) = 0.0064,
  and the 0.0023 excess at t = 1/Γ all reproduce. Very clear.

### Condescension / errors in my field
- No condescension. The Peskin cross-reference, the T-matrix and the optical theorem are stated correctly and briefly.
- Errors in my field: the 2.4.2 inner-integral sign, and the α ≈ 100 v claim (pp. 18, 22, 59).

**Verdict (b): MINOR GAPS.** Nothing blocks. I would keep reading: every rate formula could be checked to the last
digit. Fix the sign, the factor "hundred" and the ln E_ej Jacobian.

## Persona (c): condensed-matter theorist (DFT, many-body; no dark matter)

### 2.1 Fermi's golden rule
- Lost points: none on the QM. The dark-matter side is new to me, and it is just enough. "the delta function ...
  becomes δ(ω − ω_q) of Sect. 1.3" needed a reread of Eq. (1.27), which the text cites.
- The flux and cross-section paragraph (p. 50–51) and the absorption-depends-on-ρ_χ argument (p. 49) are clear.
  ϕ₀² = 2ρ_χ/m_ϕ² checks.
- Outcomes: yes, as for (b).

### 2.2 Born approximation and form factors
- Lost point (mild): the Born-validity parameters y_χy_eμ/(4πm_V) and y_χy_e/(4πv) (p. 52) are quoted "up to O(1)
  factors" from Sakurai. I could not derive them, but I accept them. "Heavy dark photon of Worked example 1.6" needed
  a lookup in Ch. 1.
- Too fast for me: the step that turns Θ(v − v_min)/v into η(v_min). It is defined in Ch. 1 (Eq. 1.33), but a
  one-line reminder of what η is would help a reader coming from solid state.
- Good: the coherent/incoherent split and the "Bragg-like elastic response deposits no energy" (p. 54) are correct
  and well put, and so is the closure argument (2.19).
- Same α vs v factor-of-ten error as (b) noted (p. 59).
- Outcomes: compute a transition form factor and see how a crystal form factor generalizes it: yes.

### 2.3 Second quantization
- **Error/inconsistency in my field.** p. 69, the Coulomb vs kinetic estimate for silicon's valence density. The text
  gets "kinetic energy about 1.3 eV, Coulomb 8.4 eV, ratio about 6" by using 1/(2m_e d²) with d = n^{−1/3}. Sect. 2.5.5
  then gives E_F = 12.5 eV for the same density, so the mean kinetic energy is (3/5)E_F = 7.5 eV and the ratio is ≈ 1.1.
  The standard measure is r_s = (3/4πn)^{1/3}/a₀ = 2.0. The conclusion "not a small perturbation" stands, but "ratio
  about 6" contradicts the book's own numbers. Quote r_s ≈ 2 and E_F instead, or call the estimate an order of
  magnitude.
- Too slow: 2.3.1–2.3.6 is first-chapter Bruus–Flensberg for me. It is appropriate for (a) and not condescending.
  Table 2.1 is useful, but its layout is very hard to parse in the extracted text; check that it is legible in the PDF.
- Correct and well chosen: the order of limits in the jellium k = 0 term, the V-counting check in 2.3.8, and the
  statement that the electron–nucleus term gives crystal momentum modulo G.
- Outcomes: yes.

### 2.4 Second-order processes
- Phonon-assisted absorption in Si: the HBB bracket, the indirect gap, and the photon momentum 6×10⁻⁴ Å⁻¹ against
  2π/a = 1.16 Å⁻¹ are correct. q₀ = 1.89 Å⁻¹ > 2π/a, so scattering reaches indirect transitions at first order. That
  is a nice point.
- The remark on not double-counting band-structure renormalization as a second-order rate (p. 79) is correct and important.
- Sign error in 2.4.2: as reported by (b).
- Outcomes: yes. I could set up the photon–phonon amplitude for Si with this.

### 2.5 Thermal states and detailed balance
- Correct: the grand-canonical/canonical remark, μ = 0 for phonons, (2.70) with Pauli blocking, and smearing in
  metallic BZ sums.
- Mild: "Silicon is of course not a metal" (p. 85). The "of course" is unnecessary. The free-gas scales for Si
  (k_F ≈ q₀, v_F ≈ 2.6 v_max) are a genuinely useful bridge to the dark-matter kinematics.
- Outcomes: yes.

### Appendices (my field)
- A.5: (A.15)–(A.18) are correct, including ⟨m|r|n⟩ = −i v_mn/(ε_m − ε_n) and the nonlocal-pseudopotential caveat. Typo
  at p. 105: the sentence "a vertex defined with an extra factor √N ..." starts in lower case after a full stop.
- A.6: the conventions match Giustino (Eqs. 16–18, 37–38). The Hermiticity relation (A.27) checks, and the
  Debye–Waller naming rule is sensible.
- A.7: the Lehmann form, Im R < 0, the F-D theorem, S ↔ loss (A.37) and the spin factor (A.38) are all correct. The
  warning about the spin factor 2 is valuable.
- D.2: the lemma (D.6) and the two-body proof reproduce, including the boson variant.

### Condescension / errors in my field
- No condescension apart from the "of course" above.
- Errors in my field: the Coulomb/kinetic ratio of 6 in 2.3.8, and the lower-case typo in A.5.

**Verdict (c): MINOR GAPS.** I would keep reading. The dark-matter side was reachable from Ch. 1 citations alone, and
the many-body content is correct apart from the r_s-style estimate. Dead "??" links are the main annoyance.

## Combined priority list
1. p. 72: inner integral of 2.4.2, −i → +i.
2. pp. 18, 22, 59: "a hundred times the dark-matter speed" → "about ten times" (α/v ≈ 3–9).
3. p. 69: the Coulomb/kinetic "ratio about 6" conflicts with E_F = 12.5 eV (p. 85). Use r_s ≈ 2.
4. p. 56: state dω = E_ej d ln E_ej between (2.20) and (2.23).
5. p. 59: 3×10⁻⁸ → 2×10⁻⁸ at m_V = 30 MeV.
6. Repoint the dead refs that the existing text can serve: S(q,ω) → Sect. 2.5 / App. A.7, f-sum → App. A.7.4.
   A.8.3: "Sect. 2.2" → "Sect. 2.5".
7. p. 73: Γ_w used before 2.4.4. WE 2.6: note that both photons are absorbed (not the absorb + emit case of Eq. 2.54).

Verdict: MINOR GAPS (both personas).
