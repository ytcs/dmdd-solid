# Ch 6 mock-reader review, reader b (personas b and c)

**Read:** the .tex sources `tex/ch06/ch06.tex`, `s6-1.tex` … `s6-5.tex` and `tex/appD/D-16.tex` … `D-18.tex`. I did not use `build/main.pdf` because it is stale: it was built Nov 1 23:46, and s6-2…s6-5 and D-16…D-18 were edited after that. I read nothing else.
**Method:** I read linearly and redid every derivation by hand. A script checked the Cherenkov rates (6.3-cherenkov) and their Si numbers. I recomputed by hand every number in the worked examples (WE). Tags: `[lost]` lost point, `[repro]` step not reproduced, `[ubd]` used before defined, `[pace]` too slow or too fast, `[LO]` learning outcome.

**Numbers reproduced** (to quoted precision unless noted):
- 6.1: v_N = 1.96e-4 (59 km/s); m_e v_N = 100 eV; (v_N/α)² = 7.2e-4; κ_BO³ = 2.94e-4; v_N/(ακ³) = 91; the sinh brackets 0.47 and 0.074 and the adiabatic asymptote; the hydrogen WE (μ = 484.2 MeV, q = 2.566 MeV, recoil 3.51 keV, v_N/α = 0.375, P0 = 0.871, "9 % high", v_N/α = 0.87 at P0 = ½, q = 5.96 MeV, recoil 18.9 keV, 1/ΔE = 0.065 fs, ΔEτ = 1.6e-5); the harmonic-well factor 1.006.
- 6.2: ω_LA = 0.55 meV, ℓ = 0.26 Å and |g| = 26 / 2.6 meV; ℓ_opt = 0.024 Å and |g| = 0.25 eV; C_F² = 4.11e3 eV⁴, |g^L| = 3.25 eV, α_F = 0.072 (0.067 via LST), 2.6 meV, 39.6 Å, 0.025 Å⁻¹, 1.29 eV.
- 6.3: coth(0.588) = 1.891; −50.1 / −46.2 / −57.3 meV; slopes 0.318, 0.26 and 0.33 meV/K; ZPR −51.8 and −59 meV; isotope shift 1.8 meV; 600 K check (model 140.4 vs fit 140.6 meV); Γ = 7.1 + 5.2 = 12.3 µeV, i.e. 53 ps, 0.91 ns and 16 ps; thresholds 0.065 and 0.031 meV.
- 6.4: γ_el/γ_free = 0.951 → 1.36 mJ/K²mol, giving λ = 0.43; two-peak λ = 0.396 and ω_log = 26.7 meV = 310 K; k_F = 1.75 Å⁻¹, E_F = 11.7 eV, v_F = 2.0e6 m/s, Q ≲ 2e-3 Å⁻¹; Migdal ratio 0.0034 / 0.0015; e^{−Eg/2T} = 4e-10.
- 6.5: the four free thresholds and the four excitonic ones; n_TA = 0.973, n_TO = 0.120; slopes 0.987/1.405 and 0.346/1.058; ratios 0.702/0.327; values at 77 K and 20 K; e^{−21200}; the A_ν prefactor matches D.18-HBB × ω/n_r.

---

## Persona (b): particle physicist (QFT, no solid state)

### 6.1 Non-adiabatic coupling
- [LO] *Show that both BO couplings form a square with a matrix "vector potential" d.* Done: (∇+d)² = ∇² + (∇·d) + 2d·∇ + d², which gives 6.1-Pd. The velocity form 6.1-tdep also follows from projecting iΣ(ċΨ + c u̇·∇Ψ). Yes.
- [LO] *Adiabatic vs sudden from 6.1-accel.* Done: the integration by parts and the sech² Fourier integral reproduce 6.1-model. For the kicked-then-trapped nucleus I took Ẍ = vδ(t) − vω_ph sin(ω_ph t)Θ(t), which gives ∫Ẍe^{iω_e t} = v/(1 − r²) and so the factor [1 − r²]⁻². Yes.
- [LO] *P0 for a kicked hydrogen atom, and d_j0 = m_eΔE r_j0.* Done via P = i m[H, r]. Yes.
- [pace] The derivative coupling is a non-abelian Berry connection; Ch. 3 already says "Berry connection" for k-space. One clause naming it would land at once with this persona. This is a missed connection, not an error.
- [lost, mild] The "kick duration" for a *contact* interaction is "time to cross the nuclear radius" (4e-21 s; 1.1e-21 s for the proton). A contact interaction has no spatial extent. The defensible statement is the one the text gives two paragraphs later: a first-order amplitude is a single act, and the c.m. separation does the rest. Suggest saying "classical heuristic only" at its first use, or relying on the impulse argument alone.
- [ubd] "vertex corrections" and g^AH are named here and defined only in 6.3. The forward references are given, so this is acceptable.

### 6.2 Electron–phonon matrix elements
- [lost] Para. "How much is left at long wavelength": local fields ε⁻¹_{0G} "replace the ionic charge by Z*" (Pick–Cohen–Martin) is asserted, not shown. With no solid-state background I cannot see why off-diagonal dielectric elements turn Z into Z*, and in particular to 0 in Si. One sentence would fix it, e.g. "the bond charge that moves with the ion is the monopole that cancels Z − Z*".
- [repro] 6.2-screen: reproduced, (1 − fR⁰)⁻¹ = 1 + fR. 6.2-asr: reproduced, −∂V = −i[p,V]. 6.2-D: reproduced, including the strain factor i. The piezo vertex: reproduced, the iQ cancels and e^pz is symmetric. 6.2-alphaF: reproduced, including the ∫dQ/(ω + Q²/2m) = (π/2)(2m/ω)^{1/2} step.
- [ubd] "dynamical quadrupoles" (piezo paragraph and the Wannier section) is never defined.
- [pace] The derivation of the Wannier formula 6.2-gW ("translate every term by the cell of the bra") is fast but followable with 3.6 at hand.
- [LO] *Three long-wavelength scalings, Q^{1/2}, Q⁰ and Q⁻¹, and why.* Yes. *α_F for GaAs.* Yes, 0.072. *Why the Fröhlich part is subtracted before interpolation.* Yes, because no finite Fourier sum gives a 1/Q singularity.
- [own-field] "The squared vertex falls as 1/Q², the same Coulomb form that weights a light-mediator rate". A light-mediator rate goes as |F_med|² ∝ 1/q⁴. The Fröhlich |g|² ∝ 1/Q² is a Coulomb propagator 1/Q² times a dipole source ∝ Q. The analogy is loose; suggest "the same Coulomb propagator, here acting on a dipole source".

### 6.3 Electron self-energy
- [LO] *Write the FM and AH self-energies and their adiabatic limit.* Yes: (n+1−f)+(n+f) = 2n+1. *Translational cancellation.* Yes: ⟨[p,[p,H]]⟩ = 2Σ(ε_n−ε_m)|p_mn|², which cancels the Fan term. *Einstein-model ZPR from data.* Yes. *Lifetime of a hot carrier.* Yes: I re-derived 6.3-cherenkov, including cosθ = −(Q/2 + m*c)/k and the Jacobian m*/(kQ).
- [pace] For a QFT reader, the FM+AH pair is exactly the rainbow plus seagull of scalar QED. Their cancellation for a rigid translation is the analogue of the gauge cancellation in low-energy Compton (Thomson) scattering. One remark would anchor the whole subsection for persona (b).
- [ubd] λ_ep is used in the Migdal subsection with only an inline gloss; it is defined in 6.4. ω_D is from 5.2, fine.
- [repro] I did not check the 2.661 ratio ⟨u²⟩(300 K)/⟨u²⟩(0): it needs the computed phonon DOS, so it is a numerics item, not a gap.

### 6.4 Phonon self-energy and Eliashberg function
- [LO] *Π as a bubble, pole expansion, linewidth.* Yes: D ≈ 1/(ω − ω₀ − Π/2ω₀) gives γ = −ImΠ/ω₀. *Allen's formula and α²F → λ.* Yes: the term-by-term comparison gives λ = Σγ/(2πN_FΩNω²). *λ_Al from the specific heat and from two Einstein peaks.* Yes.
- [repro] Double delta ∫δ(ξ_k)δ(ξ_{k+q}) = m²/(4π²q): reproduced. 6.4-a2Fgas from 6.4-a2F: reproduced. The full-model λ = 0.436 and ω_log = 250 K need the force-constant model, so they are numerics only.
- [own-field] Units: the book fixes e² = 4πα (Heaviside–Lorentz; Ch. 2 table, 6.1 writes −Ze²/(4πr), and 6.2 writes −Ze²/k²). 6.4 writes the Al ion as "−3e²/r" and w(q) = −4π·3e²cos(qr_c)/[Ωq²ε]. That is Gaussian. In the book's convention it should be −3e²/(4πr) and w(q) = −3e²cos(qr_c)/[Ωq²ε]. This is a notational slip only: the quoted λ = 0.436 matches the literature, so the computation was consistent. A QFT reader stops on it.
- [pace] The Dyson/propagator material is at a good pace for this persona. D0 = 2ω₀/(ω² − ω₀²) is the familiar scalar form.
- [ubd] ω_log first appears in the Fig. 6-a2F caption, before its definition in the text.

### 6.5 Phonon-assisted absorption
- [LO] *Second-order amplitude with both orderings and hole paths.* Yes: in D.18 I checked that on the energy shell the path-3 and path-4 denominators become those of paths 2 and 1, with the fermion sign. *ε₂^PA and α_abs prefactors.* Yes: power balance gives πe²g/(ω²Ω)⟨⟨…⟩⟩, and the HBB constant A_ν agrees between 6.5 and D.18. *Read phonon energies and temperature off the edge.* Yes.
- [pace] The hole orderings are old-fashioned-perturbation-theory Z-graphs. This reader would welcome that one word.
- [own-field] Dark photon: "even less momentum for its energy than a photon (m_φv ≈ 1e-3 m_φ)" is correct. "screened by the medium" is correct (in-medium mixing, deferred to Ch. 8).

### Persona (b): condescension, own-field errors, overall
- Condescension: none. Explaining the Galilean boost and the golden-rule reading of thermal factors is brief.
- Own-field errors:
  - the Gaussian-unit w(q) in 6.4;
  - the "same Coulomb form" 1/Q² vs 1/q⁴ analogy in 6.2;
  - the contact-interaction "crossing time" heuristic in 6.1 (mild; the text self-corrects).
- Overall: I would keep reading. The QFT scaffolding (Matsubara sums in D.16 and D.17, Dyson series, cutting rules) is correct and economical. The solid-state content is reachable, with one real gap (local fields → Z*) that does not block later material. **Verdict (b): MINOR GAPS.**

---

## Persona (c): condensed-matter theorist (DFT, many-body; no DM)

### 6.1 Non-adiabatic coupling
- [lost] DM kinematics are taken from Ch. 1: "maximum momentum transfer 5.10 MeV", v_max = 2.650e-3, "dark matter as heavy as the target bounces it at about its own speed". With 1.3 reread I could follow, and q = 2μv_max checks. A one-line reminder "q_max = 2μv_max" at first use would spare a CM reader the flip.
- [lost, mild] Why a DM–nucleus coupling acts as e^{iq·X} on the proton coordinate only (keyresult 6.1-P0) rests on 2.2. This is acceptable, but this persona's natural question is "what about the DM–electron coupling in the same event?" Say in a clause that it is a separate, independent channel.
- [LO] *Migdal 1941 vs Migdal 1958.* Yes, and the closing paragraph separating them is excellent for this persona.

### 6.2 Electron–phonon matrix elements
- [own-field] **Quadrupole tail in nonpolar crystals.** The text says g^W in Si "falls off at least as fast as a quadrupole, as R_p⁻³", and then that "a coarse grid whose supercell contains the range of g^W reproduces the vertex". An R⁻³ tail has no finite range in 3D, and its Fourier transform carries a nonanalytic, direction-dependent Q⁰ term (Q_αQ_β/Q²). That is exactly why the same section subtracts quadrupoles for GaAs. Recent work (Brunin et al. 2020; Jhalani et al. 2020; Park et al. 2020) finds quadrupole corrections matter for interpolated acoustic vertices and mobilities in Si too. Suggest "short-ranged up to a quadrupolar tail, which is small in Si for the optical-phonon-assisted processes of this book and can be subtracted like the dipole".
- [own-field] "the piezoelectric coupling … comes from the dynamical quadrupoles" is incomplete. The piezoelectric tensor has a clamped-ion part (quadrupolar) and an internal-strain part (Z* × relative displacement). Suggest "from the dynamical quadrupoles together with the Born charges of the internal-strain relaxation".
- [own-field, consistency] Static screening is said to be correct "with corrections of relative order ω_ph/E_g" (6.2), while 6.4 says Π(ω) − Π(0) is of relative order (ω/E_g)² because Π is even in ω. The second statement is right for the screened phonon frequency. The 6.2 sentence should say (ω_ph/E_g)², or specify which quantity is first order.
- [pace] "A phonon-assisted rate in silicon converged to 14 meV" is unclear (an energy resolution of 14 meV?). 6.5 says "energy resolution", so use that phrase here.
- [pace] There are two "zero-point lengths" for the Si optical mode: 0.048 Å in 5.1 (coordinate u, mass M_κ) and ℓ_0ν = 0.024 Å here (mass-weighted to M_cell, factor 2). Both are right, but a sentence reconciling them would help.
- Deformation potentials, Herring–Vogt, Fröhlich and EPW are accurate. Ξ_d, Ξ_u and α_F agree with standard values.

### 6.3 Electron self-energy
- [own-field] **Sign claim.** After 6.3-cancel the text says "the interband vertex translates the electronic state … and like any second-order mixing it lowers the energy. The Allen–Heine term … raises the energy by exactly as much." The Fan contribution is ℓ²Σ_m(ε_n − ε_m)|p_mn|². That is negative only from bands above n. For a conduction state with valence bands below it, or for the VBM, it has either sign. The second-order shift is sign-definite only for the ground state. Suggest "it shifts the energy, and the Allen–Heine term shifts it back by exactly as much".
- [repro] 6.3-ria from D.16-sr2/ria: reproduced (N from the cell sum, symmetrize (κα) ↔ (κ'β)). The smearing 6.3-smear: reproduced.
- [LO] *Rigid-ion AH from first-order vertices.* Yes. *Why acoustic modes barely shift the gap, so ⟨u²⟩ scaling overestimates by 2×.* Yes. *ZPR extraction routes.* Yes. The 9 meV zero-point-expansion correction and the 20 % underestimate are correctly attributed.
- Migdal for insulators: the statement (static vertex good to ω_ph/E_g; it says nothing about intraband carriers near edges; polaron vertex corrections O(α_F)) is correct and well put.

### 6.4 Phonon self-energy
- No errors found. The screened-screened vs bare-screened bubble and the Calandra subtraction are handled correctly, which is rare in a text at this level. The aluminum model is a nice touch: the TA suppression explained by umklapp, and λ stationary in r_c.
- [lost, mild] The motivation "the superconducting sensors of Ch. 7" is enough. A CM reader does not need more DM context here.

### 6.5 Phonon-assisted absorption
- [lost] Last subsection: "just above [the threshold mass] the energy needed to cross the gap is available at momentum transfers well below k_c". As a non-DM reader I want the kinematics in one line: ω ≤ qv − q²/2m_χ, so for ω ≈ E_g the minimum q ≈ E_g/v_max ≈ 0.45 keV, against k_c ≈ 1.9 keV. Without it the "window of masses" is asserted. This is not blocking, since Ch. 13 is promised.
- [own-field] Special displacements cannot separate the E_g ± ω thresholds. Correct. The 0.15–0.23 eV rigid shift (Noffsinger) is correctly described.
- [pace] The refractive-index and extinction derivation of α_abs is slow for this persona but right for persona (a). It is not condescending.

### Persona (c): condescension, own-field errors, overall
- Condescension: none. The explanations of α²F notation, "the symbol is read as one", and the deformation-potential argument are brisk and useful.
- Own-field errors, in priority order:
  - (1) the "second-order mixing lowers the energy" sign claim (6.3);
  - (2) Si treated as having a finite-range g^W despite an R⁻³ quadrupole tail (6.2);
  - (3) the piezoelectric origin given as quadrupoles only (6.2);
  - (4) the ω/E_g vs (ω/E_g)² inconsistency (6.2 vs 6.4).
  None changes a number in the chapter.
- Overall: I would keep reading. The many-body content is accurate and current (Giustino review conventions, Calandra subtraction, rigid-ion caveats). The DM framing is light enough that the missing kinematics never blocked me. **Verdict (c): MINOR GAPS.**

---

**Overall verdict: MINOR GAPS.** No lost point or unreproduced step blocks later material. The steps I could not reproduce (Al full-model λ and ω_log, ⟨u²⟩ ratio 2.661, local fields → Z*) need numerics or derivations the text deliberately cites rather than supplies.
