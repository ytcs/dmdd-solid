# App. E.14–E.27: mock-reader review (isolated)

Reviewer stance: computational condensed-matter postdoc asked to run these specs on a cluster. Read: E-14…E-27 in full; E.1–E.13 and ch01–ch07 only where pointed to (grep-checked). No briefs, ledgers, SPINE or state files read.

## Overall verdict: MINOR GAPS (bordering NOT EXECUTABLE for E.16 library, E.18 Migdal rate, E.21 color centres)

About half the sub-calculations can start tomorrow: E.14 ground state and phonons, E.17 base, E.18 drag mass, E.19 PIMD, E.20 aluminium, E.22 pilot, E.25 kernels, E.26 Fano map, E.27 tritium. The arithmetic is unusually good: I re-derived about 60 numbers and nearly all check out (Lebedev degrees, supercell momenta, plane-wave and memory counts, Massey parameter, Auger integral, GaAs `d`, Sommerfeld factors, tritium activity, collection-kernel step count). The problems sit elsewhere, in five systemic issues and a short list of hard errors.

### Systemic issues (apply across sections)
1. **Undrafted chapters carry the conventions.** Every section refers to ch.8–21 (`sec:8.5` truncation label, `sec:8.2` master rate, `sec:13.x`, `sec:21.7` target list, …), and none of these labels resolve in the current tree. The specs then point to them for normalisations, halo conventions, `F_DM`, window definitions (`E_min(q)`, `δ_w`, `δ_off`, `x_R`, `θ_ii`, `W`) and target lists. The appE intro defines `n_B, n_g, n_A, n_T, X`, but not the lattice regime `K` or the Migdal regime `M` used in E.17, E.18 and E.21. Halo parameters (`v0 = 238`, `v_esc = 544`, `ρ = 0.3`) live in ch01/A-8, but no E-spec points there.
2. **Candidate lists never appear.** E.16 ("every candidate"), E.17 ("forty-odd candidate targets of §17.5"), E.24 ("ranked materials") and E.27 ("survivors of §21.7") all depend on a list that is nowhere in the drafted text. E.17 tab:E17-batch names only 8 materials.
3. **The shared lattice is not shared.** E.17 says "one harmonic lattice per material serves every lattice channel … a mismatch … is an error". It then computes the base at the *measured* lattice constant with 80 Ry. E.14 runs Si phonons at the *PBE* lattice constant with 60 Ry, and chose PBE on purpose because the TA branch is better there. E.17 also says the E.14 runs "replace the base once converged at the same cutoff". Which lattice constant wins is undefined.
4. **The same DFPT run gets three different costs.** E.14 gives ≈100 core-h for Si (60 Ry, 12³ k, 8³ q) and also "about one core-hour" per wavevector. E.17 gives 25 core-h for Si at a *higher* cutoff (80 Ry, 12³, 8³). E.18 assumes ≈25 core-h per DFPT run (75 core-h for three). E.14 Ge gives 17 core-h (80 Ry, 8³k, 6³q), while E.17 Ge gives 60 core-h. The Ge SOC estimate in E.14 ("×4–8 → 400–800") scales from 100, not from 17. A reader cannot budget from these figures.
5. **`S` is normalised two ways.** E.17 tabulates `S(q,ω)` "in eV⁻¹ per cell". E.18 uses "eV² per cell", and E.19–E.21 use "eV², the units of §4.2" (sec 4.2 is per volume, eV²). No conversion is stated.

### Broken pointers (hard)
- E.27: `\cref{app:D.46}` does not exist. Appendix D ends at D.23.
- E.18: the drag-mass inputs are attributed to "the shared harmonic calculation of app:E.4 (SG15, 80 Ry, 12³)". E.4 uses 35 Ry examples; the shared base with those settings is **E.17**.
- E.24 (twice): "the Bethe–Salpeter equation of app:E.3". E.3 is quasiparticles and itself defers the BSE to E.6.
- All `sec:8.x`–`sec:21.x` and `chap:17/20/21` refs (see 1). Everything else (`app:`, `eq:`, `tab:`, `we:`) resolves, and all cite keys are in book.bib.

---

## E.14 Phonon-assisted electron recoil (start tomorrow: partly)
- **Ready:** QE/DFPT/Wannier90/EPW stages and the f-sum check (eq. E.14-remainder is clean and correct).
- **Missing:** the two non-standard codes (the density vertex rotated into the Wannier gauge, and the second-order amplitude with Sternheimer remainder) have no interface or algorithm spec beyond prose, and no development time is costed. The source of the dynamical quadrupoles is "a long-wave DFPT code or the literature", but no code or values are named. "30 directions in the irreducible wedge … about the valley axis" is ambiguous. Rate conventions (halo, `F_DM`, `δ_w`) are deferred to undrafted §13.
- **Inconsistencies:**
  - The Bethe-ridge remark gives `|q| ≲ 0.5 α m_e` (1.86 keV), but the bins run to 2.47 keV.
  - Targets: 630 / "about 1800 unfolded" vs "several hundred targets" in Cost.
  - Neutron-scaled onsets: a 0.48 meV shift gives +0.00014 MeV. The replica value (0.3332 → 0.3334) is within rounding of that, but the free-pair value (0.3374 → 0.3378) is not.
  - The Ge Wannier count jumps from 16 to 36 functions without saying the second count includes 3d.
- **Cost:** "about 10⁵ diagonalizations" for the density vertices is too few. 630 targets × 12³ k-points without symmetry is ≈10⁶ (≈3×10⁶ unfolded). Either the count or the 50–70 core-h is off by about 10×.
- **GaAs:** "Z* and ε∞ from app:E.17", but E.17 says PBE ε∞ for GaAs is tens of percent off and should be replaced by measured values. Which one to use is not stated.

## E.15 Excitons and core states (partly)
- The TDA estimate checks out (ε₁ᵀᴰᴬ ≈ 3.9, L ratio ≈ 2). The BSE sizes check out (24 576 pairs ≈ 10 GB; 6.6×10⁵ pairs → 7 TB).
- **Unclear:** the section says the f-sum rule is broken by the resonant form. The Migdal-lines calculation then uses the hybrid route: resonant proper lines with RPA external screening. It still demands the f-sum "for lines plus continuum to 1%". Whether that test applies to the hybrid route, and to which function, is not defined.
- **Acceptance by estimate:** the core-level test is "reproduce −0.58% Ge relativistic f-sum shift of §10.6 to 0.1%". That reproduces an estimate the calculation is meant to replace. It also clashes with E.16's "−0.73% total for Ge". (The numbers are consistent if −0.58% is mass–velocity only, since 0.58×1.27 ≈ 0.73, but E.15 does not say so.) The same quantity is computed in two sections.
- `(Z_eff α)⁴ ≈ 10⁻⁶` for Ge 3d implies `Z_eff ≈ 4`. This is questionable for a semicore 3d shell; with `Z_eff` of 10–15 the term is closer to 10⁻⁴.
- **Model chain:** hoppings, `E_g` and bandwidths in model units, the phonon frequency and the Fock-space truncation are not given. "W/E_g = 0.05–0.3" alone does not define the model.
- **Self-trapped exciton (NaI):** no lattice constant, pseudopotentials, cutoff or k-sampling is given, and no measured luminescence energy or tolerance. **Cost implausible:** 64–216-atom hybrid relaxations with I spin–orbit, plus TDDFT excited-state relaxation, at "≈10³ core-h" is about 10–100× low.
- "8³ grid of p in the irreducible zone … about 60 irreducible points": 8³ fcc has 29 irreducible points (E.14 says so), so the shell count behind 60 is unclear.
- The intro announces "five excitonic + one core-level" calculations, but there are seven subsections (spin–orbit mixing is unannounced).
- **Overlap:** the Si exciton binding is computed here by a variational effective-mass method and again in E.24 by GW-BSE with 10⁴–10⁵ k-points, with no cross-reference.

## E.16 Electronic response libraries (no, for the library itself)
- **Cost implausible:** `|q+G| ≤ 8 α m_e` (≈15 Å⁻¹) is ≈2300 G-vectors. Storing the full `R⁰_GG'` on 250 |q| × 30 directions × 1000 ω is ≈85 MB per (q,ω), about 6×10¹⁴ B (≈600 TB). The Dyson inversions alone are ≈10¹⁷ flop. "50–100 core-hours" is off by orders of magnitude, and so is the storage plan. The spec needs a reduced G-set or a reduced (q,ω) grid for the stored matrix.
- **Kinetic row:** eq. E.16-TT divides `|⟨c|p²|v⟩|²` by `4m_e⁴`. For `T = p²/2m` the square gives `1/(4m_e²)`. Either a coupling normalisation is hidden or this is a typo; the reader cannot tell.
- **1D local-field model:** "gap 1, width 2" (whose width?), and `u₀`, `ω_Q`, `Q`, `q`, `ω` are not given. "Three couplings have exact answers", yet two are stated only "of order".
- **Cutoff count:** "4 Ry (about 60 G)" is ≈37 G-vectors in Si (≈100 if 4 Ha).
- Anisotropy: "Two diagnostics … ℓ = 1, 2 and 3" lists three.
- Static step: `W` (Debye–Waller) is undefined here. "1×1×N cells" does not say primitive or conventional.
- Candidate loss functions: the target list is missing (see systemic 2).
- **Good:** Lebedev degrees 17/25/35, supercell momenta (0.76/1.08/…, 0.57/0.81/…), `Ω_P,e = 0.51 eV` → 18 keV, and the boosted-DM 2% bound all check.

## E.17 Lattice libraries (yes, with caveats)
- **Self-contradictory acceptance:** the base is at the measured lattice constant and must match neutron data at Γ, X and L to 5%. E.14 states that at the measured lattice constant the Si TA branch is **8% low** at X and L. The base fails its own test by construction. For Ge, E.14 reports 13.5% low. A remedy is needed: exempt TA, or use a different lattice constant.
- **Charge vertex count:** "|Q+G| ≤ 20 keV, about 4000 reciprocal-lattice vectors" is ≈700 in Si (6.19 Å⁻³ per G). It is off by ≈6× (4000 would correspond to ≈36 keV).
- Coherent two-phonon: valid only at T = 0, as stated. The library also lists 1 K and 77 K, with no prescription for the coherent correction there.
- **Checks out:** GaAs `d = −1.33×10⁻³`, the 41% sensitivity, the 2.4% requirement, `D/c ≈ 300 keV`, PIMD `P ≈ 250` at 10 K, and the 4096-atom Hessian timing.
- LST eq. E.17-lst omits 4π, which is fine only in Heaviside–Lorentz `e²` (consistent with E.16). The convention should be stated next to it.

## E.18 Migdal and non-adiabatic (drag mass: yes; crystal rate: no)
- **Checks out:** drag mass 14 `m_e` → 2.7×10⁻⁴, the `E_R` bounds 4.3 / 3.1 eV, the Sternheimer moment formulas, the G-counts (≈300 → 1000; ≈230), and the 16 MB / 32 GB memory figures.
- **Cost implausible (crystal Migdal rate):** a `50³` p-grid per shell × 2000 ω × ~10³ G with a 12³ k-mesh is ≫10³ core-h. Even the irreducible p count (≈2600) gives ≈10¹⁹ flop. The p-grid definition (Cartesian? reduced? up to 30 keV?) is also ambiguous.
- **Acceptance not executable:** "must agree with a measured Migdal signal in neutron scattering … which the proposal of Adams et al. makes possible". No such data exist.
- Wannier ratio: "bare perturbation from ph.x (ionic part without induced Hartree and xc)" needs a code modification (`dvqpsi` output). This should be stated as new code.
- Pointer E.4 → should be E.17 (see above).

## E.19 Anharmonic, disordered, quantum solids (partly)
- **Checks out:** the cell sizes (320/1080/2560; 512/1728), `P ≈ 80`, 80 ps, the timestep, the He `βω_D ≈ 25`, the cubic-tensor size 0.45 GB, the Hessian 1.9 GB / 4×10¹² flop, and the wall pressure 5×10⁻¹¹ Pa.
- **Garbled:** "The self-consistent harmonic ladder costs about 10² for the self-consistent harmonic ladder, 10³ for helium …"
- **Operating temperatures:** "at the temperatures where a target operates" is never listed. The pitfalls then rule out RPMD/CMD at mK, so the actual run temperatures are undefined.
- **Glass `C^IR`:** at L ≈ 4.3 nm, `k ≤ 0.3 Å⁻¹` holds only about two k-shells (2π/L = 0.147). Extracting a k→0⁺ limit *and* a curvature from them is ill-conditioned. The 1728- and 648-atom models violate the "box ≥ 4 nm" rule while being part of the convergence test.
- **Chiral phonons:** no framework (MOF) is named, and no lanthanide ion or host. The calculation cannot start.
- MICROSCOPE geometry (cylinder dimensions, Pt-alloy composition) is not given.

## E.20 Magnetic, superconducting, Dirac (mostly yes)
- Al: executable, but `N_F` and `v_F` values are not given in the spec. The `qξ ≥ 1.6` derivation checks.
- **ZrTe₅:** two dielectric tensors are used side by side. `ε_bg = 25.3` is Hochberg et al.'s clamped-ion harmonic mean. The axis factors 9.5×10⁴, 431 and 1.6×10⁴ (ε_ii ≈ 308, 21, 126) come from Geilhufe et al.'s tables. The spec never says which tensor feeds the threshold/BSE stage. It also says "static `ε_bg` includes the ionic part" while quoting a clamped-ion value. `Ry_D`, `a_D` and the 37× ratio check.
- Optical activity: "one magnetoelectric crystal" is unnamed.
- a-WSi: an RPA matrix at 1000 atoms with G to q + 3 keV (≈1.7×10⁴ G) over the ω range is likely more than the 10⁴–10⁵ core-h quoted. The text gives 1.6×10⁴–1.6×10⁵ but the table gives 10⁴–10⁵.
- **Checks out:** two-magnon ratios (0.146/0.049/0.029), YIG 80 atoms and 20 Fe, and the re-plot factors (1600/6.3, 640/5.0).

## E.21 Dopants, colour centres, small targets (partly)
- **Checks out:** NV parameters, donor intervalley momenta (3.88/0.685/2.74/2.33 keV), Sommerfeld 7.3/3.4/2.6, and the `q_max` for 10 MeV.
- **Molecular crystals:** "G₀W₀ + BSE … 50–100 atoms … 200 bands". That is ≥66 occupied bands (anthracene, Z = 2) and up to ≈136 (stilbene, Z = 4). It leaves only ~60–130 empty bands, far too few for G₀W₀.
- **Colour centres, cost implausible:** ≥10³ decoherence-corrected surface-hopping trajectories on constrained hybrid-DFT surfaces in 64–216-atom cells is ~10⁶–10⁷ core-h, not 10⁵. Unless an ML surface or a model is used, this needs to be said.
- Bond breaking: no molecular solid is named. The low-dimensional tables name no tube chiralities, dot materials or substrates.

## E.22 Defects and TLS (partly)
- **Checks out:** W plane-wave count 2.1×10⁵ / 7 GB, ln(Γ₀t) = 47.2, λ = 27.5, the 14% margin, `S_pol` integrals, SiO₂ 2.8×10⁵ PW / 2.5 GB, 576 bands, and 0.83 keV.
- **α_ohm supercell route is flawed as specified:** cells of 54, 128 and 250 atoms with k-grids shrinking 4³ → 2³ give Born–von-Kármán lengths of 12a, 12a (or 16a) and 10a. The effective L does *not* grow, so the ln L slope is undefined. The route needs Γ-only or fixed BvK scaling. With an `L` span of only 1.67×, slope extraction is fragile anyway.
- "the four targets cost 4×10³", but five are listed (W, Nb–H, Al, AlOx, a-WSi; the table agrees with five).
- **f_TLS:** the TLS are found in 10³–10⁴-atom glasses (ensemble subsection), but the vertex runs in 216-atom cells. How a TLS is carved or transplanted into a 216-atom cell is not specified.
- "Swap Monte Carlo or a comparable method" for network SiO₂ with an MLP is not an established route. The stable-glass protocol is effectively unspecified, and the text itself says it is the dominant systematic.

## E.23 Nuclear-recoil partition (partly)
- **Checks out:** Massey 15 / 2, the 216-atom TDDFT grid 5.4×10⁵ / 3.7 GB, ZPE 126 eV in 4096 atoms, n ≥ 1112, and the Auger integral (eq. E.23-fA).
- **TDDFT kernel:** the (E_coll, b) grid density is not given, so the 10⁶ core-h cannot be checked. A rough estimate (≈30 fs at 2 as for 216 atoms, ×20–50 trajectories × a 10×10 grid) gives ≳10⁶–10⁷. The 10% HSE-Ehrenfest subset is uncosted and very expensive.
- **Contradiction:** "cells hold 64 to 216 atoms" but "the cell must be at least 15 Å across". The 64-atom Si cell is 10.9 Å.
- **`C_Aug` is circular:** it "comes from … app:E.24". E.24 lists Auger recombination among the needed rates but gives no method for it.
- MLIP timing: 3×10⁴ threshold runs of 4–8×10³ atoms × 3–5 ps at 0.1 fs in "10³ GPU-h" is optimistic for MACE/NequIP (≈10⁴), though plausible for ACE. The code choice should be fixed.

## E.24 Electron cascades (partly)
- **Grid gap:** P_n(q,ω,T) gives |q| "from 0 to 25 α m_e along three directions" with no step. Each bin seeds a k-resolved first generation of up to 8×10⁴ samples, so the cost cannot be checked without the q count.
- **Opaque arithmetic:** a 25% rise in `A_AB` raises ε_eh by "0.084×1.3 = 0.11 eV". This works only if `A_AB ≈ 5.2` (ΔA = 1.3), and the value is not given. "1.3" also appears as the fit constant, which confuses the reader.
- **Wide-gap cost sum:** 3 oxides × 10⁵ + 2 halides × (10⁴–10⁵) + 5 crystals × 2×(Si cost 3×10⁴–2×10⁵) ≈ 6×10⁵–2.5×10⁶, not 4×10⁵–1.5×10⁶.
- **Exciton k-mesh contradiction:** Si/Ge "need 10⁴–10⁵ points", but the convergence test is "8³ → 12³ to 1 meV".
- "accepted 3.6 eV" (intro) vs the validation value 3.749 eV at 123 K (and E.23/E.25 use 3.75/3.8). Say which is meant where.
- BSE pointer E.3 → E.6.

## E.25 Event-level transport (yes)
- **Checks out:** 26.7 pairs, the field-sheet `n_s = 6.5–12.9×10⁴ cm⁻²`, 5–10 h, 10.9 THz, 2×10⁴ trajectories, and the kernel cost (2×10¹² steps / 36 h / 140 core-h, 4.4 h, 0.44 h, 3%).
- **Notation:** `ε₀` is used for Si's relative constant (11.7) and `ε₀^SI` for the vacuum permittivity, which collides with the standard usage. The table writes `U_el`; the text writes `U_rel`.
- The epoxy MLP "does not exist" (acknowledged), and its DFT training is not costed.

## E.26 Coherent fields, fermionic absorption, two insertions (mostly yes)
- **Checks out:** t_coh 6.6 ms / 1.6 km (with v₀ = 238), line width 3.6×10⁻⁶, the propagator factor, `(Zα)² ≈ 0.16`, and Thomson in HL units.
- **GaAs cutoff conflict:** this section uses 90 Ry (fully relativistic NC). E.14 and tab:E17-batch use 140 Ry "with Ga 3d in valence". Is the 3d in the valence here?
- "13 824 k points of the shell" (= 24³) is ambiguous: is it the shell or the full grid?
- The multiferroic near-T_N case is explicitly unsupplied (honest, but it leaves a hole).

## E.27 Halo, backgrounds, FOM inputs (yes, except pointer)
- `app:D.46` is dangling.
- Stream grid: 100 speeds to 1000 km/s in the galactic frame, while the support is `|w| ≤ v_esc = 544`. About 45% of the columns are outside the ball. Either the grid or the frame is mislabelled.
- Tritium arithmetic checks (0.17 / 11).
- "Geant4 with 10⁸ primaries 1–3 CPU-hours" is optimistic for hadronic spallation (≈10–30 h).
- The survivor list is undrafted, and the number of bins in the LP is unspecified.

---

## Repetition / overwriting
- Gauge-consistency warnings (one `U(k)` for `g`, ρ and the BSE vectors) appear in E.14, E.15 (twice), E.18 and E.26. One canonical statement in E.5 plus pointers would do.
- The off-axis zero-phonon optimum and the "hole not at Γ" point are re-explained in E.14, E.15 (twice) and E.16.
- The f-sum completeness rule "60 bands ≥95% with nonlocal term" is stated in both E.14 and E.16.
- The Si TA lattice-constant story appears in E.14 and E.17.
- The relativistic f-sum shift for Ge is a test in E.15 and a computed quantity in E.16, with different numbers (−0.58% vs −0.73%).
- The Si exciton binding is computed in both E.15 and E.24.
- Nuclear PIMD appears in E.17 and E.19 (consistent, but two specs).
- "One configurational-energy table" is repeated in E.22 and E.23 (twice), which is acceptable as a cross-link.
- No section overwrites another's numbers outright. The conflicts are the lattice constant (E.14/E.17), the DFPT costs (E.14/E.17/E.18), the GaAs cutoff (E.14/E.17/E.26) and the units of `S` (E.17 vs E.18–E.21).

## Fixes in priority order
1. Repair `app:D.46` (E.27) and the E.18 → E.17 and E.24 → E.6 pointers.
2. Decide one lattice constant and cutoff per material for the shared base. Reconcile the E.17 neutron test with the known 8% TA deficit.
3. Re-cost E.16 `R⁰_GG'` storage, the E.18 crystal Migdal rate, E.21 surface hopping and the E.15 STE, or shrink their grids.
4. Fix the counts: E.17 "4000 G" → ≈700; E.16 "60 G" → ≈37; E.14 "10⁵ diagonalisations"; E.22 "four targets"; E.24 wide-gap sum; E.14 neutron-scaled onsets.
5. Resolve which ZrTe₅ ε_bg tensor is used where, the E.16 `m_e⁴`, the E.22 BvK-length scaling and the scope of the E.15 f-sum test under TDA.
6. Name the missing targets (MOF, magnetoelectric, molecular solid) and list the candidate/survivor materials, or point to one table.
7. Unify the normalisation of `S` (per cell vs per volume; eV⁻¹ vs eV²) and the `ε₀` notation (E.25).
