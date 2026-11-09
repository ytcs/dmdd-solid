# Chapter 7 mock-reader review: personas (b) and (c)

Source read: the .tex files (ch07/s7-1..s7-4, appD/D-19..D-23). build/main.pdf (Nov 1 23:46) predates every one of them, so the PDF is stale.
Read linearly. Every derived step was worked by hand or in Python (scipy). Numerical claims checked are listed under "Outcomes".

---

## Persona (b): particle physicist (knows QFT, no solid-state physics)

### 7.1 Magnetic order and spin waves (+ D.19)
- **Lost:** none that blocks. Brief stumble at "type II", (111) stacking and rock-salt geometry. Fig. 7.1a and the plane-index rule resolve it.
- **Not reproduced:** none. Checked: Hubbard singlet shift −4t²/U, J^ex = 4t²/U − 2K_ex, HP commutators, FM bond expansion, ω = |S|[J(k) − J(0)], AFM A_k, B_k, Bogoliubov ω = |S|(A² − B²)^{1/2}, (u ∓ v)² = (A ∓ B)/(A² − B²)^{1/2}, the D.19 (u − v)(a₁ + a₂†) combination, and S_ab against the convention of eq:4.2-Sab (xy element = +i). All correct.
- **Before-defined:** none.
- **Pace:** good. The HP check is at exactly the right density for a QFT reader.
- **Missed connection (not an error):** FM and AFM break the same SO(3)→SO(2). The FM has one quadratic Goldstone mode and the AFM two linear ones. A QFT reader expects two modes and is not told why the FM has one (⟨[S_x, S_y]⟩ = i⟨S_z⟩ ≠ 0, type-B counting). One sentence would close this.
- **Outcomes:**
  - Chain exact diagonalization: two-deviation level 0.3277|J| vs LSWT pair 0.382 (S = ½, N = 10); 1.0827 vs 1.172 (S = 1, N = 8). Both match the text.
  - NiO: 2√3·19.01·4.17 = 274.6 meV·Å → 1.39×10⁻⁴ → 41.7 km/s; [111] slope 254.8 meV·Å.
  - Full J₁+J₂ model, numerically: slopes 254.8–269.2 meV·Å over random directions; zone maximum 118.17 meV = |S|(6J₂ − 3J₁).
  - Ordering wavevector 1.30 Å⁻¹ = 2.6 keV → m_χ ≳ 0.49 MeV.
  - **Can do:** derive LSWT for FM and AFM, the NiO velocity, the one-magnon weights.

### 7.2 Superconductivity (+ D.20, D.21)
- **Lost:** none blocking.
- **Not reproduced:**
  - Eq. 7.2-NVren, (λ − μ*)/(1 + λ), rests on the Eliashberg equations of App. E.9, which are outside the assigned text. Taken on trust.
  - Everything else reproduced: Cooper E_b = 2ω_D e^{−2/NV}; arsinh gap; T_c via the Matsubara sum; 1.764; coherence factors; normal-state S_n = m²ω/πq; violation 8πΔ²/V_BCS; the ratio 12(Δ/v_F q)²/NV crossing 1 at 8.55Δ; the q = 0 bubbles (η η, s₂ s₂, s₂ η) from the Pauli traces; R_ηη = 0; Ward identity at q = 0 with γ₂ = −2iΔ/ω; the commutator [s₁, η] = −2i s₂.
- **Before-defined:** μ*_C appears only with a gloss and a forward reference to App. E.9. ω_log is from 6.4 and fine.
- **Pace:**
  - Nambu, Ward identity and conserving RPA are well pitched for this persona. Not condescending.
  - The Eliashberg paragraph (7.2.1, last paragraph) is too fast for anyone who has not met it.
- **Missed connection:** "pushes the mode up to the plasma frequency" is the Anderson–Higgs mechanism, and saying so would anchor it for particle readers. The amplitude (Higgs) mode at 2Δ is also left unnamed when the s₁ channel decouples.
- **Error (prose), s7-2 "Near the threshold the integrand is ±Δ² times the product of the two edge divergences":**
  - At threshold E(ω − E) → Δ², so the numerator is Δ² ± Δ², which is 2Δ² for case I.
  - Read literally, the sentence gives a jump of π/4, not π/2.
  - Numerically the ratio is 1.5708 at ω = 2.0001Δ, so the stated result π/2 is right and only the sentence is wrong.
- **Outcomes:**
  - Pair spectra at ω = 4Δ: 1.211 and 0.672 (text: 1.21, 0.67).
  - Δ = 0.179 meV; m_min = 0.10 keV (0.17 keV for the film value); q = 0.27 eV; pair size 2.3 µm; v_F q = 10Δ.
  - NV = 0.164 (40 meV cutoff) and 0.180 (ω_log); T_c = 54, 20, 5.8 K; Cooper binding 0.40 µeV.
  - **Can do:** all of the section except deriving NVren.

### 7.3 Dirac and narrow-gap materials (+ D.22): my field
- **Lost:** none.
- **Not reproduced:** the Kramers → Dirac-form argument (7.3.1, "extends this across directions" and the SO(4) rotation step) is too terse to rebuild line by line. I accept the γ-matrix result I already know.
- **Before-defined:** none.
- **Pace:**
  - The Kramers derivation is too fast.
  - The QED analogies (α̃, running coupling, scheme constant −5/3 ↔ e^{−5/6}Λ) are correct and not condescending.
  - The q² prefactor is Π⁰⁰ = |q|²Π(s), so ε is Lorentz-invariant in s as claimed.
- **Error, s7-3 "Pairs and kinematics":**
  - The text says "the slope of the continuum edge never falls below v_D".
  - In fact dω_edge/dq = v_D²q/ω_edge < v_D always. What is true is ω_edge ≥ v_D q.
  - The conclusion (no scattering for v_D > v_max) survives. Rewrite as "the edge never lies below the line v_D q". The summary's "never rises more slowly than v_D q" is ambiguous in the same way.
- **Outcomes:**
  - DOS eq. 7.3-dos re-derived.
  - Threshold masses from my own root solve: 10.49 keV (isotropic), 9.39 (v_y), 12.67 (v_x); text 10.5 / 9.4 / 12.7. Flat-edge limit 8.9 keV.
  - Edge mass 0.053 m_e; n_c(4 K) = 1.0×10⁻⁵ cm⁻³.
  - Prefactor q²/(24π²v_D) and ρ(u) checked; ∫ρ/u = ln(U/Δ²) − 5/3; −5/18 integral; gapless limit and its −6Δ²/(v²q² − ω²) correction; Im ε.
  - Static ε: 0.0930 at q = 0, 0.0813 at 2Δ/v, 0.0527 at Λ/2 (text 0.093 / 0.081 / 0.053).
  - α̃ = 0.190 (and 0.199 for the older parameter set); axis additions 9.81 / 1.57 / 6.71; couplings 0.065 / 0.155 / 0.109.
  - **Can do:** everything.

### 7.4 Defects and dopants (+ D.23)
- **Lost (minor), "valley-orbit splitting":**
  - A₁, E, T₂ are used as labels with only "tetrahedral symmetry" for context.
  - The point group (T_d) and the meaning of the irreps are never stated in the main text.
  - D.23 gives the eigenvectors, which is enough to recover them.
- **Not reproduced:** none. Checked: Ry*_⊥ = 18.98 meV, a*_⊥ = 32.4 Å; ε₀ = 11.41 from 2p±; valley-orbit Δ_f = −2.17, Δ₀ = −4.09, Δ_g = −1.51 meV; 6×6 eigenvalues; ZPL weights; the E³ correction 0.677 → 0.031; m_χ for 12.5/36 eV recoils = 0.153/0.26 GeV; T-centre and NV threshold masses 0.266/0.554 MeV.
- **Before-defined / notation:**
  - In we:7-sip, a and b (variational radii) are used without definition in the chapter; they are defined only in D.23.
  - In the same worked example, "a³/8" uses a for the Si lattice constant (5.43 Å), while "1/a = 81 eV" uses a for the 24.3 Å radius. Two meanings within three lines.
  - D.23 writes U = −e²/(4πε₀r): to a particle reader ε₀ is the vacuum permittivity. Here it is the relative static constant, in Heaviside–Lorentz units. Write ε_s, or drop the 4πε₀ form.
- **Pace:** good. The F-centre etymology and the "telecommunications O band" aside are harmless.
- **Outcomes:**
  - Variational KL minimum −1.5642 Ry*_⊥ at 24.26 / 13.95 Å (text: −1.564, 24.3 / 14.0).
  - m_χ = 13.0 keV; q = 34.4 eV; qa = 0.42; N_D = 3×10¹⁹ cm⁻³; |F(0)|²a³/8 = 7.7×10⁻⁴.
  - **Can do:** all.

### Overall (b)
I would keep reading. 7.2 and 7.3 are the strongest sections for this persona. The problems are in prose, not results:
- the slope sentence (7.3);
- the "±Δ²" sentence (7.2);
- the notation clashes in 7.4/D.23 (a/b, ε₀).

Two QFT bridges are missing: Goldstone counting and Anderson–Higgs.

**Verdict (b): MINOR GAPS.**

---

## Persona (c): condensed-matter theorist (knows DFT and many-body theory, no dark-matter physics)

### 7.1 Magnetic order and spin waves (+ D.19)
- **Lost (DM side):**
  - The coupling "−Σ Ô_χa s_e,a" and "Table I of Ref. trickle2020detecting" are deferred to 8.1. That is acceptable, but I cannot yet say what Ô_χ is.
  - The kinematic statements (q ≤ 2m_χv_max, v_max = 2.65×10⁻³) are traceable to 1.3.
- **Not reproduced:** none (see b).
- **Before-defined:** none.
- **Pace:** Hund's rule, exchange integrals and HP are below my level, but correctly done and not condescending to a mixed audience.
- **Field errors and nits:**
  - (i) The hopping estimate. √(J₂/U_H) for U_H = 4.6–8.2 eV gives t/U = 0.048–0.064, i.e. "0.05 to 0.06", not "0.05 to 0.07".
  - (ii) NiO's charge type. NiO is the textbook charge-transfer insulator (ZSA), and superexchange through O involves Δ_CT as well as U_H (J ~ t_pd⁴/Δ_CT²·(1/U + 1/Δ_CT)). The text labels J ~ t²/U only "an estimate", but calling the regime a "Mott insulator" and inverting for t_eff glosses this. One clause would fix it.
  - (iii) The rest is correct: J₁/J₂ geometry (GKA), anisotropy gaps < 5 meV, the DFT spread as uncertainty, ⟨S_z⟩ zero-point reduction.
- **Outcomes:** as for (b). **Can do.**

### 7.2 Superconductivity (+ D.20, D.21)
- **Lost (DM side):** m_min = 2E_th/v_max² and "film convention 0.6 meV" need 1.3/1.5. Both were read; fine.
- **Not reproduced:** none. NVren is the standard simplified μ*-reduced coupling; McMillan has extra factors, but the text says "≃".
- **Before-defined:** none for this persona.
- **Pace:** good. The conserving-response subsection is a clean presentation that I would use in teaching.
- **Field errors and nits:**
  - (i) The "±Δ²" sentence (see b): the factor of 2 is missing from the prose.
  - (ii) Coherence-factor classes. "Every one-body probe falls into one of these two classes" is overstated: a generic operator splits into T-even and T-odd parts, each in one class. Write "every one-body probe is a sum of the two classes".
  - (iii) The rest is correct: Bardeen–Pines, μ*, the residue 1/(1+λ), sound attenuation 2n_F(Δ), Mattis–Bardeen, v_F/√3, the Coulomb push to ω_p, the f-sum violation and the q-range claim (8.55Δ).
- **Outcomes:** as for (b). **Can do.**

### 7.3 Dirac and narrow-gap materials (+ D.22)
- **Lost (DM side):** "daily modulation through the rotation of the Earth" is asserted without the mechanism (the direction of the dark-matter wind in the lab frame). Acceptable as a pointer.
- **Not reproduced:** none (checked as for b).
- **Before-defined:** none.
- **Pace:** good. The ε_bg double-counting discussion in we:7-zrte5 is exactly the caveat a DFT practitioner wants.
- **Field errors:**
  - (i) The slope sentence (see b).
  - (ii) Otherwise correct: Kramers degeneracy from PT; band inversion; Na₃Bi and Cd₃As₂ as Dirac semimetals; the Weyl condition; Kane mass 0.066 m_e; harmonic-mean ε_bg; the warning that semilocal functionals invert small gaps.
  - (iii) Na₃Bi and Cd₃As₂ have their nodes off the TRIM, on a rotation axis, unlike the k₀ = TRIM setting derived here. Worth one clause, so that the reader does not take them as examples of the derived case.
- **Outcomes:** as for (b). **Can do.**

### 7.4 Defects and dopants (+ D.23)
- **Lost:** none.
- **Not reproduced:** none.
- **Before-defined:** a and b in we:7-sip (see b).
- **Pace:** good.
- **Field errors and nits:**
  - (i) D.23, "Anisotropic valleys": the orbit with radii (24.3, 24.3, 14.0) Å is called a "prolate spheroid, flattened along the heavy axis". Two equal long axes and one short axis make an **oblate** spheroid. Error.
  - (ii) we:7-sip, "the measured 1s triplet of phosphorus, A₁…, T₂…, E": "triplet" here means the three 1s levels, one of which is itself the T₂ triplet. Write "the three 1s levels".
  - (iii) The Summary says "Effective-mass theory gives 29.7 meV … the central-cell correction brings phosphorus to its measured 45.6 meV". The worked example takes 31.3 meV (ε₀ = 11.4) as the reference and gets 14.3 meV. Either quote 31.3 in the summary or say which ε₀ is meant.
  - (iv) The rest is correct: KL/Faulkner values, measured P/As/Sb levels, the valley-orbit algebra, the T-centre exciton picture, E³ weighting, Holmström thresholds, Loferski–Rappaport 12.9 eV, the Frenkel-pair storage argument. The NV S_HR = 3.85 attribution to Alkauskas 2014 I could not confirm from memory, and the text's own photon check (0.031 vs 0.032) is consistent with it.
- **DM side:** E_R,max (eq. 1.3-ERmax) with M = 26.16 GeV is fine with Ch. 1 in hand.
- **Outcomes:** as for (b). **Can do.**

### Overall (c)
For a CM theorist the chapter is accurate and well pitched. Exchange, HP and the effective-mass donor are standard material, and the treatment is not condescending. 7.2's conserving response and 7.3's ε_bg bookkeeping are the parts I would value most.

Errors to fix, none blocking:
- the oblate/prolate slip (D.23);
- the edge-slope sentence (7.3);
- the "±Δ²" threshold sentence (7.2);
- t/U "0.07" (7.1);
- the "1s triplet" wording and the 29.7 vs 31.3 summary mismatch (7.4).

The DM-side gaps are forward references (8.1 couplings, daily modulation), which are acceptable at this point.

**Verdict (c): MINOR GAPS.**
