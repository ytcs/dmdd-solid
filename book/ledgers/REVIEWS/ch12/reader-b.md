# Chapter 12 mock-reader review: personas (b) and (c)
Sources read: tex/ch12/ch12.tex, s12-1 to s12-6, tex/appD/D-33.tex, D-34.tex, read in order. build/main.pdf (Nov 1 23:46) is older than every ch12 .tex file, so I did not use it. I did not read any brief, ledger, SPINE or source paper.
Method: I reworked by hand or in sympy every displayed derivation, and checked every headline number I could rebuild from the constants given (about 90 checks). Unless an item is listed below, it reproduced to the digits shown.
The chapter states no learning outcomes, so I inferred them per section and tried each one (item 5).

## Persona (b): particle physicist (knows QFT, no solid-state physics)

### 1. Lost points
- **L1, the main finding: §12.3 and §12.4 contradict each other on the soft limit.** In §12.3-validity, eq:12.3-bracket writes the free-recoil boost as 1/(ω_e−y) − 1/ω_e with y=(q−p)·p/M. It drops p²/2M "in the denominators" but keeps −p²/M in the numerator. From this it derives the correction 3p²/q² ("the soft limit proper … decides the low masses"). The same correction appears in four other places: the intro of §12.3 ("holds down to about 16 MeV, below which the electrons take a sizable part of the nuclear momentum"), the solid curve and gray band of lim:12.3b (falls short by ×1.2 at 12 MeV and ×2 at 5 MeV), the sentence "the soft limit fails before the lattice does", and the 16 MeV range in the closing line of §12.3-validity. §12.4 then says the opposite: "None of the three is a ratio p/q". It also warns that keeping the p²/M numerator without the matching p²/2M denominators produces an error "of relative order p/q". Its key result says dP/dω_e is eq:12.3-soft "at every q", and tab:12-nuisances has no soft-limit row. My algebra (item 2) supports §12.4. After §12.3 I believed the Migdal formula fails below 16 MeV in silicon; after §12.4 I believed it does not. Fix: rewrite the §12.3 paragraph and the bracket, and redraw lim:12.3b and its caption, so that only the 9/5 Doppler term and the 2p²/Mω_e recoil term remain. Changing the text alone is not enough.
- L2. we:12-oscillator, "Excited-surface final states": the text gives the mean lattice energy "3ω₀ = 0.192 eV", and the next sentence adds 1.0463 + **0.188** = 1.234. I could not tell which 0.19 eV figure is meant, or where the 65.5 meV quanta come from. Fix: say that 1.0463 eV and 65.5 meV are read off the exact diagonalization, which includes g_n, and that 0.188 eV = 1.234 − 1.0463.
- L3. §12.1-boost estimates P_Mig ≈ (E_R/⟨ω_e⟩)(δM/M) using the trace value 2.7×10⁻⁴ and gets 2×10⁻⁶, against 1.86×10⁻⁶. §12.5 later says the trace value "is not what a kick measures", since the on-site value is 5.6×10⁻⁴, and that the valence drag mass is 18.6 m_e. So the agreement in §12.1 is partly coincidence: the point-ion model happens to carry about the trace drag mass. §12.1 should point forward to §12.5 at that sentence.
- L4. Solid-state vocabulary is dense in §12.3 (head of the inverse matrix, local fields, scissor gap, symmetrized ε̃) and in §12.3-wannier. Every term is defined in Ch. 3–5 or Ch. 10, but I had to look each one up. A one-clause reminder at first use in this chapter would remove the stops.

### 2. Steps I could not reproduce
- eq:12.3-bracket and the averaged square below it. Attempt in sympy: the exact free amplitude from the two orderings, written as in eq:12.4-exact, is b/[(ω−b+a)(ω+a)] with b=q·p/M and a=p²/2M. Its angle-averaged square divided by the leading (b/ω²)² is 1 − 2p²/(Mω) + (9/5)q²p²/(M²ω²) + O(p⁴/M²ω²), with **no 3p²/q² term**. The §12.3 form 1/(ω−b+2a) − 1/ω gives 1 + 3p²/q² + …, which reproduces the book's bracket. That bracket is therefore an artifact of the inconsistent truncation that §12.4 itself warns against. I reproduced eq:12.4-corr and its 9/5 coefficient exactly.
- we:12-oscillator: I could not reproduce 1.0463 eV (Δ_tl − S_HR ω₀ = 1.042 eV), the 65.5 meV quanta, or the Condon zero-phonon fraction 0.056. Poisson(3) gives e⁻³ = 0.050. If the 0.056 comes from unequal frequencies on the two surfaces, the text should say so.
- D.33-virtual gives the correction as (64.1 meV/1.17 eV)² = 3×10⁻³ in amplitude, a factor 1.006 in probability. §12.4 and we:12-five-keV give 2.9×10⁻³ in probability, from ⟨ω²⟩^{1/2} = 44.7 meV. Both are estimates, but they differ by a factor of 2 and neither one says why.

### 3. Used before defined
- I checked scissor, PBE, Herzberg–Teller, Condon, Huang–Rhys, Sternheimer, drag mass, off-shell window, Umklapp, Wannier, q_BZ, impulse onset and Debye–Waller. All of them are defined in Ch. 3–11.
- **GPAW** (caption of tab:12-moments) is not defined anywhere in Ch. 1–11.
- **"tagged-recoil measurement"** (§12.6-open) is not defined.
- eq:12.2-rate gives no unit. It is a rate per nucleus, while eq:12.1-rate carries 1/ρ_T and is per unit mass.

### 4. Too slow / too fast
- Too slow for me: the center-of-mass separation of §12.2, the two-ordering expansions (eq:12.4-series and the bremsstrahlung amplitude), and the setup of photon emission in §12.6-photon. All are standard second-order perturbation theory. That suits persona (a), and none of it is condescending.
- Too fast: §12.3-wannier (projector ordering, the acoustic sum rule in its electronic form) and the derivation of the dynamical Born charge. Each step is short, and the physical picture comes after the formula rather than before it.

### 5. Learning outcomes (inferred) and my attempts
- 12.1: write the Migdal entry as boost × vertex × S^ee × lattice factor, and avoid double counting. Done. I used weight 1−P_Mig and mass M+δM. I re-derived 48.4 meV = E_R + ⟨p²⟩/2M with p = 5.6 keV.
- 12.2: atomic probability by shell from tables. Done. Ge at 1 keV: (87.9/511)² = 0.0296, 0.0296×8.75×10⁻² = 2.59×10⁻³. First moment (N_e m_e/M)E_R = 0.242 eV.
- 12.3: the coefficient 4α from the f-sum. Done: cπe²/2 = e⁴/2 gives c = e²/π = 4α in Heaviside–Lorentz units. Si at E_R = 200 eV: P = 6.07×10⁻⁵ × 200 = 1.2×10⁻². Rate check: at 1 GeV I get about 9×10² /kg/yr (book: 970), at 100 MeV about 29 (book: 30). **I cannot yet state the low-mass validity** because of L1.
- 12.4: phonon-emitting fraction at 5 keV. Done: 2W(q−p) = 1.57×(25+37.2)/2500 = 0.039, giving 3.8%. Also v_min = (ω_e+ω_l)/q + q/2m_χ for a bound lattice, against q/2μ for a free recoil. Both correct.
- 12.5: bounds at 500 eV. Done: 0.0174 ≤ 0.0303 ≤ 0.163. **Error:** "Third moments from nonrelativistic all-electron densities are therefore about 40% low for germanium" is wrong. 1/1.425 = 0.70, so they are about 30% low. The "42% higher" in the other direction is right. Also δM/M = 28.7×0.511/26155 = 5.61×10⁻⁴, not the 5.58×10⁻⁴ given in we:12-drag (a rounding slip).
- 12.6: soft bremsstrahlung. Done: dN/dω = (2α/3π)Z²v²/ω with the n_r medium factor. Signs of the double commutator checked, and the 2α/3π = 1.549×10⁻³ check passes.

### 6. Own-field remarks (particle physics)
- **"the ten nonrelativistic operators of the dark-matter–nucleon interaction"** (§12.4-rate). The standard NR-EFT basis has 14 operators at linear order (O1–O15 without O2), or 15. Say which ten, and why only ten.
- Correct, and not condescending: HL units with e² = 4πα, the Dirac 1s solution (E = mγ_D, λ = Zαm, f/g ratio), the R_rel derivation, σ_N = A²σ_n μ²_N/μ²_n, the halo moment 16μ⁴∫u³η = 4μ⁴⟨v³⟩, the equivalence-principle argument for the scalar coupled to mass, and the series of the medium factor n_r/|ε|².
- Sign wording: "the force that the electrons exert on nucleus I, minus the force of the other nuclei" (§12.6-absorption). ∇V is minus the total force, so the sentence has the sign backwards.

**Overall (b).** I would keep reading. The structure of a single joint response reduced into four published forms is clear and convincing, and nearly every number reproduces. L1, however, is a real contradiction between two sections, and it changes what I would conclude about the low-mass reach in §12.3. §12.4 resolves it before anything else depends on it, so it does not block the rest of the chapter.
**Verdict (b): MINOR GAPS.** It is not LOST because §12.4 corrects L1 before any later material uses it.

## Persona (c): condensed-matter theorist (knows DFT and many-body theory, no dark-matter physics)

### 1. Lost points
- **L1, the same §12.3/§12.4 contradiction as above.** As a CMT reader I also found it from the lattice side: "p/q" cannot matter for the electronic spectrum once the lattice factor has unit weight at every q−p, which §12.4 shows.
- L2. Dark-matter kinematics arrive fast and lean on Ch. 1: η(v_min), v_max ≈ 795 km/s (which I had to back out from "35 eV at 10 MeV"), ⟨v³⟩^{1/3} = 401 km/s, the conversions between σ_N and σ_n, and "heavy mediator". I could follow them only by rereading §1.2–1.3. Stating v_max explicitly once in §12.2 would help.
- L3. "The frame of the transition density" (§12.1-boost, §12.4 end) is called an open question, but it is never stated as a question. As I read it, the question is whether valence transition densities move with the crystal or with the struck ion, and the Herzberg–Teller term interpolates between the two. One sentence saying this would help.

### 2. Steps I could not reproduce
- The same as persona (b), items 2a–2c.
- we:12-gaas: Ω = a³/4 with a = 5.6533 Å gives **45.17 Å³**, not the 44.80 Å³ stated. That moves Ωm_e/e² to 0.03276 and the charge sum to −0.350, about 0.8%. The conclusions do not change, but this is a stated input.

### 3. Used before defined
- GPAW and "tagged-recoil", as for persona (b).
- "θ_ep", "n_B", "𝔐", "𝒦" and "𝒳" in the truncation-label boxes are defined in Ch. 8, but they are used here with no reminder.

### 4. Too slow / too fast
- Too slow for me: the loss-function and FDT reminders, the oscillator-spring picture of the atomic dynamical charge, and the dielectric screening narrative in §12.6. Too fast for me: halo integrals and v_min (as in L2). The mass scaling μ⁴/(m_χμ_n²) is stated but not derived.

### 5. Learning outcomes (inferred) and my attempts
- 12.3: identify which dielectric element enters. Done. The diagonal of the inverse at G containing p. ε̃ has the same inverse diagonal as ε (v^{−1/2}ε^{−1}v^{1/2}).
- 12.5: compute I₂, I₃ and I₄ from two static Sternheimer solves. Done: ψ₁ = (H−E₀)⁻¹Fψ₀ and ψ₂ = (H−E₀)⁻¹ψ₁ give I₂ = ⟨ψ₁|ψ₁⟩, I₃ = ⟨ψ₁|ψ₂⟩ and I₄ = ⟨ψ₂|ψ₂⟩, which is correct. Trace rule through TRK: 2m²ΣΔ|X|² = N_e m_e. Reproduced. R_rel for Z = 14, R = 3.47 fm: γ = 0.99477 and prefactor 1.0133 × power 1.0681 give **1.082**. Reproduced, and Ge gives 1.425.
- 12.5: third moment of Si. Done: Ze²n/(3M) with n = 1765 a₀⁻³ gives 1497 eV². Lattice curvature over contact term is 1.3×10⁻⁶. Both reproduced.
- 12.6: Z*(1 eV) of Si from ε = 12.37. Done: Ωm_e(ε−1)/2e² = 0.02905 × 11.37/2 = 0.165. The ratio of polarizability per atom of the solid to the free atom, 228/69.5 = 3.3, also reproduced. GaAs, using the book's Ω: 4.94×10³. Reproduced.
- 12.4: phonon-mediated propagator. Done: the two orderings at first order in p give (p·e)(q·e)/[NM(ω_e²−ω_ν²)]. Reproduced, and so is the expansion 2⟨ω²⟩/ω_e² = 2.9×10⁻³ at 1.17 eV.

### 6. Own-field remarks (condensed matter / DFT)
- **ε̃ "is Hermitian in a crystal with time reversal and inversion"** (§12.3-validity). Wrong as written. The retarded matrix at real ω with absorption is complex *symmetric* (from T and I), not Hermitian. Im[−ε̃⁻¹_{GG'}] for G ≠ G' has to be read as the anti-Hermitian part (ε̃⁻¹ − ε̃⁻¹†)/2i, which equals the elementwise Im only because the matrix is symmetric. Say "symmetric", and define Im as the anti-Hermitian part.
- "**F** = Σ∇_iV_eN minus the total force on the electrons" (§12.3-wannier) reads as a subtraction. Write "F = Σ∇_iV_eN, which is minus the total force on the electrons".
- Correct: FDT S^ee_GG = 2p²/e² L, the metal discussion (L ∝ ω, perfect screening of a slow ion, 2Δ ≪ ω_ph), the Born-charge sum rule eq:12.6-sum and its two limits, F_cr → Z − Z* (28.89 and 35.11 for GaAs), the Bragg treatment of the zero-phonon line, and the Debye scaling for Ge (2ω_D/3 × 0.82 = 17.6 meV). Material constants (Si/Ge ε∞, Ω_Si, 2p/3d binding, Si exciton binding 14.7 meV, plasmon at 17 eV, optical phonons 64.1 and 37.6 meV) all match what I know.
- No condescension. The FDT and loss-function reminders are short, and they suit persona (a).
- Interesting and, I think, right: the on-site drag mass is not fixed by any sum rule, and the chain model shows that the off-site sum can take either sign. The proposed Q-resolved calculation with the trace rule as an acceptance test is well posed.

**Overall (c).** I would keep reading. From the CM side the chapter is careful: every approximation has a parameter, and almost every parameter has a number. I needed to go back to Ch. 1 for the DM kinematics, and the §12.3 soft-limit claim (L1) conflicts with §12.4, which is correct. The rest of the problems are wording or numerical slips of under 1%.
**Verdict (c): MINOR GAPS.**

## Items for the author, by priority
1. §12.3: eq:12.3-bracket, the averaged bracket, the paragraph "The soft limit fails first", lim:12.3b and its figure, the "16 MeV" in the §12.3 intro and the end of §12.3-validity. All of these conflict with §12.4 and with the exact two-ordering amplitude.
2. §12.5-third: "about 40% low" should be about 30%.
3. §12.3-validity: "Hermitian" should be "symmetric", and Im should be defined as the anti-Hermitian part.
4. §12.4: "ten nonrelativistic operators" needs to say which ten.
5. we:12-oscillator: explain where 1.0463 eV, 65.5 meV, 0.188 eV and 0.056 come from.
6. we:12-gaas: Ω = 45.17 Å³.
7. Define GPAW and tagged-recoil. State the unit of eq:12.2-rate. Fix the force-sign wording in §12.3-wannier and §12.6.
8. Reconcile the two binding-correction estimates in D.33-virtual and §12.4. Add a forward pointer from the §12.1 drag-mass estimate to §12.5.
