# SEAM: Appendix D.16–D.23 (long derivations for 6.3, 6.4, 6.5, 7.1, 7.2, 7.3, 7.4)

Length (detex): D-16 ≈ 1,810 (planned 2,500); D-17 ≈ 1,550 (2,000); D-18 ≈ 1,470 (2,500); D-19 ≈ 1,330 (1,500);
D-20 ≈ 1,310 (2,000); D-21 ≈ 1,520 (2,000); D-22 ≈ 1,030 (1,500); D-23 ≈ 1,110 (1,500). Total ≈ 11,100 (planned 15,500);
every row of the spine is covered; nothing was padded.
Lint (BANNED-TERMS): 0 blocking in all eight files. Remaining hits are false positives: LONG-SENT merges across displays,
EQ-PUNCT on gathered/aligned displays whose punctuation is inside, two TITLE hits (D-19, D-21 titles kept close to the spine).
Build: full main.tex into /tmp/build-D-c: 0 LaTeX errors, 0 undefined citations; D.16–D.23 print with their planned numbers
(the other D writers have since added D-7 and D-12…D-15; the temporary `\setcounter{section}{15}` line that this writer
added after D-11 has been removed by them, and appD.tex now inputs D-1…D-23 in order). Undefined references only to unwritten
sections: chap:13, sec:4.5, 4.9, 5.4–5.7, 6.2–6.5, 7.1–7.4, 14.1, 16.5.
Checks: figscripts/appD/check_D_c.py, 69 assertions, all pass (rerun before submission). It asserts every number and closed form
quoted in the text: D.16 rigid-ion relation on a 1D crystal (FD Hessian vs PT 4e-6, RIA 1e-7, non-rigid failure 66 %), FM
Matsubara sum; D.17 λ from widths = 2∫α²F/ω, electron-gas full width = Allen form (1e-5), mass enhancement with finite band;
D.18 four-path amplitude vs exact Fock-space second-order T (machine precision; hole paths O(1)), HBB integral and prefactors;
D.19 type-II fcc LSWT vs linearized classical precession on 256 sites (1.7e-13 J₂), 6J₂|S|, 2√3J₂|S|a; D.20 Δ(0)/T_c = 1.76396
at 𝒩_F V_BCS = 0.2, Matsubara tanh expansion, coherence factors in a 4-mode Fock space; D.21 Nambu trace formula, q = 0
entries, Goldstone condition, conserving R_ηη(0,ω) = 0, f-sum on a 48×48 lattice (1e-9; bare ×28.5 and ×4.1), 8πΔ²/V_BCS,
Anderson–Bogoliubov c = 0.579 v_F; D.22 dispersion-integral form vs direct 3D quadrature with hard cutoff (1e-5), Feynman-
parameter identity, ∫ρ/u = ln(U/Δ²) − 5/3, −5/18, Im part vs 1708.08929 Eq. (2.6), static hard-cutoff constant −5/3 (1e-4);
D.23 isotropic limit, Ry*_⊥ = 18.98 meV, 91.0 meV, variational 29.7 meV at a = 24.3 Å, b = 14.0 Å, valley-orbit levels.
Shared files: appD.tex (inputs D-16…D-23 after D-11); book.bib (13 entries appended: allen1976theory, allen1981temperature,
allen1972neutron, calandra2010adiabatic, migdal1958interaction (no DOI exists), bardeen1957theory, anderson1958random,
nambu1960quasi, holstein1940field, hutchings1972measurement (not cited in the text; for 7.1), kohn1955theory,
hochberg2018detection (arXiv 1708.08929 checked), tinkham2004introduction (book, no chapter cited)); DOIs checked on Crossref
2026-11-02. Sources: sources/D-c/ holds the text extracts of 1708.08929 and 1910.02091 (PDFs deleted). APS papers are not
readable here; they are cited without equation numbers and everything attributed to them is derived.

## The reader now knows
- D.16: second-order coupling H⁽²⁾_ep and g^AH (eq:D.16-gAH, normalization of A.6, 1/N); Fan–Migdal self-energy from the
  D.11 boson rule with −|g|²𝖣₀/N (eq:D.16-FMmats), Matsubara sum done by residues, retarded form with n+1−f and n+f
  (eq:D.16-FM), Im Σ ≤ 0 and phonon-limited rate (eq:D.16-ImFM); Allen–Heine term as the thermal average of H⁽²⁾ with
  ⟨B_Q B_−Q⟩ = 2n+1 (eq:D.16-AH); not e^{−2W}; adiabatic RS limit, occupations cancel (eq:D.16-adiabatic); frozen-phonon
  route (eq:D.16-frozen); translational invariance: sum rules (eq:D.16-sr1 = acoustic sum rule, eq:D.16-sr2, exact); rigid-
  ion approximation and the on-site relation (eq:D.16-ria); Σ^AH in RIA with the displacement tensor B_κ (eq:D.16-AHria,
  Allen–Cardona form); exact cancellation for a uniform translation; off-site second derivatives dropped by the RIA.
- D.17: phonon bubble with sign count and spin factor 2; Π^b (eV) and Π_ν = 2ω_QνΠ^b (eV²); Dyson equation
  𝖣_ν = 2ω/(ω² − ω² − Π_ν) (eq:D.17-Pi); softening at ω = 0; double counting with DFPT phonons, nonadiabatic remainder
  (eq:D.17-nonad); Kohn anomaly (named, from D.8); linewidth γ^ep_Qν = −Im Π_ν/ω_Qν, a full width (eq:D.17-gamma); vanishes
  for ω_Qν < E_g in an undoped insulator at T = 0; Allen's metallic form (eq:D.17-allen) and its limits; α²F
  (eq:D.17-a2F) with 𝒩_FΩ per spin per cell; α²F and λ_ep from the widths (eq:D.17-lambda); λ_ep = −∂ReΣ/∂ω at the Fermi
  surface, z = 1/(1+λ_ep), mass enhancement (eq:D.17-mass); phonon-side Migdal theorem by power counting; electron-gas check
  m_e²ω/4π²Q.
- D.18: ε₂ from the golden rule and σ₁ = ωε₂ (eq:D.18-eps2); α_abs = ωε₂/n_r (eq:D.18-alpha); four paths with fermion signs
  and the on-shell combination into the one-electron sum over all bands (eq:D.18-M); ε₂^PA (eq:D.18-eps2PA); HBB edge with the
  joint-density integral πx²/8 (eq:D.18-HBB, eq:D.18-edge); kinks at E_g ∓ ω_ν, thermometer ratio e^{−ω/T}, forbidden edge
  x³, excitons named; the dark-matter generalization (pointer to chap:13).
- D.19: two-sublattice model with J^ex_AA(k), J^ex_AB(k) (eq:D.19-Jk), type-II fcc assignment; HP on both sublattices
  (eq:D.19-HP); quadratic Hamiltonian A_k, B_k (eq:D.19-Hk) with E_cl; Bogoliubov via C.7 (eq:D.19-bogo), u^M, v^M;
  ω^M_k = |S|(A² − B²)^{1/2} = eq:E.9-afm, ground-state energy (eq:D.19-omega); ΔS^z of the branches; stability A ≥ |B|;
  Goldstone and linear law (eq:D.19-linear); J₂-only type II: 6J₂|S|[1 − γ_k²]^{1/2}, max 6J₂|S|, c = 2√3J₂|S|a; spin
  operators through magnons (eq:D.19-inverse), u − v suppression at k → 0, u + v enhancement at the AF wavevector.
- D.20: reduced BCS Hamiltonian with V_BCS and shell ω_D (eq:D.20-H); gap definition (eq:D.20-Delta); mean field = C.7
  fermion problem; γ_k1, γ_k2 (eq:D.20-gamma); E_k, u^B, v^B (eq:D.20-E); BCS state; quasiparticle DOS (eq:D.20-dos);
  b_k = (Δ/2E)tanh(E/2T); gap equation (eq:D.20-gap); Δ(0) = ω_D/sinh(1/𝒩_FV_BCS) (eq:D.20-Delta0); T_c via the Matsubara
  expansion of tanh and harmonic numbers (eq:D.20-Tc); Δ(0)/T_c = πe^{−γ_E} = 1.764 (eq:D.20-ratio); coherence factors for
  n_e and s^z_e (eq:D.20-coh, eq:D.20-cohE), case I/II; jump vs continuous onset at 2Δ; the q = 0 pathology of the density.
- D.21: Nambu spinor and matrices η, 𝗌₁, 𝗌₂; O_A(q); density = η vertex; H_MF and 𝖦₀ (matrix); contact attraction with
  all pair momenta and its pairing-channel form; bare Nambu bubble at T = 0 (eq:D.21-R0); q = 0 traces and entries
  (eq:D.21-q0); bare violation ∫ωS⁰(0,ω) = 8πΔ²/V_BCS (eq:D.21-violation); [H_MF, n_e] = q·j + 2iΔO_𝗌₂; conserving
  response = linearized time-dependent mean field = RPA with K = diag(0, −V/2, −V/2) (eq:D.21-Rc); proof of continuity by
  Wick factorization; explicit cancellation at q = 0; Goldstone and Anderson–Bogoliubov mode (c = v_F/√3, numerical 0.579);
  Coulomb pushes it to ω_p; Ward identity in Nambu form (eq:D.21-ward), bare violation 2iΔ𝗌₂, ladder vertex γ₂ = −2iΔ/ω;
  spin density needs no vertex correction.
- D.22: 4×4 Dirac cone, projectors, overlap per state (eq:D.22-F), g_deg; reduction to one dispersion integral in the
  invariant s = ω² − v_D²q² (eq:D.22-R); cutoff u < 4v_D²Λ_D²; ε = ε_bg − v_C R⁰_D; Im part (eq:D.22-Im) = 1708.08929
  Eq. (2.6); closed form with Feynman parameter (eq:D.22-eps), hard-cutoff constant −5/3 ↔ Λ → e^{−5/6}Λ; static gapped
  (eq:D.22-static); gapless (eq:D.22-gapless) = Eq. (2.7); log screening, no Thomas–Fermi length; anisotropic rescaling.
- D.23: envelope equation (eq:D.23-EMT) from the Bloch expansion, band decoupling; hydrogenic E_b^D, a* (eq:D.23-hydrogenic);
  Si bracket 19.0/91.0 meV; KL variational energy (eq:D.23-variational) with ⟨1/r⟩ = arcsin e/(ae); Si 29.7 meV at
  a = 24.3 Å, b = 14.0 Å (eq:D.23-Si); species independence; six valleys, central-cell matrix elements, A₁/E/T₂ levels
  (eq:D.23-vo); ground state A₁ deepened; p-like states insensitive.

## Symbols introduced (with defining equation)
In NOTATION and used as listed: g_mnν, g^AH, Σ^FM, Σ^AH, ε^ren_nk, B_Qν, b_Qν, n_Qν, B_κ, Π_ν, γ^ep_Qν, α²F, λ_ep, 𝒩_F,
ε₂^PA, α_abs, m*_∥, m*_⊥, J^ex_ij, |𝐒|, a_kν, u^M_k, v^M_k, Δ_BCS, ξ_k, E_k, u^B_k, v^B_k, T_c, ω_D, v_D, Δ_D, ε_bg, α̃,
Λ_D, g_deg, a*, E_b^D, ε₀ (static constant), 𝖦, 𝖣₀, ω^F_j, ω^B_j, γ_rel not used. New, proposed below.

## Terms introduced
Fan–Migdal and Allen–Heine self-energies; rigid-ion approximation; translational-invariance sum rules; adiabatic Allen–Heine
formula; phonon Dyson equation; nonadiabatic phonon renormalization; Kohn anomaly (named); Allen's linewidth formula;
Eliashberg function; mass enhancement; phonon-side Migdal theorem; electron and hole paths (phonon-assisted absorption);
Hall–Bardeen–Blatt edge; forbidden indirect edge; Holstein–Primakoff bosons; Goldstone magnon; reduced BCS Hamiltonian;
pair amplitude; quasiparticle density of states; coherence factors case I/II; Nambu spinor; amplitude and phase channels;
conserving (generalized RPA) response; Anderson–Bogoliubov mode; Ward identity (Nambu form); Lorentz-invariant dispersion
integral; hard-cutoff constant; envelope function; valley-orbit splitting; central-cell correction.

## Threads: opened / advanced / closed
Advances the threads of 6.3–6.5 and 7.1–7.4 (electron–phonon coupling, composite processes, novel targets). Closes the
derivation debts D.16–D.23.

## Promises made to later sections ("we return to this in …")
- D.18 ends with the dark-matter version of the four paths (chap:13 / D.35).
- D.19 gives the magnon operators and ⟨d†d⟩ = (v^M)² per mode for the spin weights and ΔS (sec:14.1 / D.38).
- D.21 gives the conserving response; the resummed edge loss function is D.39 (sec:15.2).
- D.23 gives the valley-orbit structure used by 16.5.

## Open questions for the editor
1. Π_ν normalization: NOTATION lists Π_ν in eV², so D.17 defines 𝖣_ν = 2ω_Qν/(ω² − ω²_Qν − Π_ν) and Π_ν = 2ω_Qν × (Giustino's Π).
   γ^ep_Qν = −Im Π_ν(Q, ω_Qν)/ω_Qν is a full width, as γ_Qν (5.7). 6.4 must use these; the intermediate bubble is written Π^b (eV).
2. The α²F–linewidth relation, eq:D.17-lambda, is written for 𝒩_F per spin and the full width. Allen (1972) was not readable;
   the text states the normalization and does not quote Allen's prefactor.
3. Euler's constant is written γ_E (D.20) to avoid γ_Qν and γ_rel; a NOTATION row is proposed.
4. The Nambu matrices: η is reused from C.7 (diag(1, −1)); the two off-diagonal ones are 𝗌₁, 𝗌₂ (sans-serif), since τ is
   imaginary time and σ_i is reserved for s_e(q). 6.x/7.2 and 15.2 should use the same.
5. HP sublattice bosons are d_{Ai}, d_{Bj}, d_{Ak}, d_{Bk} (extension of the generic d_γ), magnons a_k1, a_k2 (ν = 1, 2).
6. The cell volume is written Ω in D.17/D.18 (as in NOTATION's clash list); the extinction coefficient is κ_ext and the
   refractive index n_r (D.18); valley mass ratio γ_m (D.23); Ry*_⊥, a*_⊥ (D.23). Please confirm or rename.
7. The NiO numbers (Hutchings–Samuelsen) are not quoted in D.19; WE 7.2 does that with E.9's J₂ = 19.0 meV.
8. D.21 assumes particle–hole symmetry over the shell to decouple the amplitude channel; the conservation proof does not
   need it, but the explicit q = 0 algebra does. The lattice check is away from half filling and conserves to 1e-9 with all
   three channels kept.

## Proposed ledger rows (the editor merges them)
NOTATION: Π^b_ν(Q, ω) phonon bubble in energy units, Π_ν = 2ω_QνΠ^b_ν | eV | D.17 · 𝖣_ν(Q, ω) phonon Green's function
2ω_Qν/(ω² − ω²_Qν − Π_ν) | eV⁻¹ | D.11/D.17 · ω^ren_Qν renormalized (nonadiabatic) phonon frequency (Ω is the cell volume) | meV | D.17 · Ω cell volume
(confirm) | Å³ | 3.1 · V_BCS BCS pairing strength (shell |ξ| < ω_D) | eV·Å³ | 7.2 · γ_E Euler's constant 0.5772 | 1 | D.20 ·
𝒩_s(E) BCS quasiparticle density of states per spin and volume | eV⁻¹Å⁻³ | 7.2 · γ_k1, γ_k2 Bogoliubov quasiparticle operators
(mandatory branch index; not γ_Qν) | — | 7.2 · Ψ_k Nambu spinor (c_k↑, c†_−k↓) | — | 7.2 · η, 𝗌₁, 𝗌₂ Nambu matrices (η from C.7)
| 1 | 7.2 · O_A(q) Nambu bilinear Σ_k Ψ†_{k+q}AΨ_k | — | D.21 · K channel kernel of the conserving response | eV·Å³ | D.21 ·
d_{Ai}, d_{Bj} Holstein–Primakoff sublattice bosons | — | 7.1 · J^ex_AA(k), J^ex_AB(k) intra- and inter-sublattice exchange
sums (E.9 uses them) | meV | 7.1 · A_k, B_k LSWT coefficients | meV | 7.1 · ω^M_k magnon energy | meV | 7.1 · N_s sites per
sublattice | 1 | 7.1 · 𝓕(k, k′) Dirac interband overlap per state | 1 | 7.3 · ρ(u) Dirac pair spectral function
(1 − 4Δ_D²/u)^{1/2}(1 + 2Δ_D²/u) | 1 | 7.3 · s invariant ω² − v_D²q² (local to D.22) | eV² | D.22 · F_j(r) donor envelope of
valley j | Å^{−3/2} | 7.4 · γ_m mass ratio m*_⊥/m*_∥ | 1 | 7.4 · Ry*_⊥, a*_⊥ transverse-mass effective Rydberg and radius | meV; Å
| 7.4 · Δ₀, Δ_g, Δ_f valley-orbit matrix elements | meV | 7.4 · n_r refractive index, κ_ext extinction coefficient | 1 | 6.5 ·
M^±_cvν(k, Q) phonon-assisted optical amplitude | eV·(velocity) | 6.5 · W_ab = ê·v_ab | 1 | 6.5.
GLOSSARY: Fan–Migdal self-energy; Allen–Heine self-energy; rigid-ion approximation; translational-invariance sum rule;
adiabatic Allen–Heine formula; phonon Dyson equation; nonadiabatic phonon renormalization; Allen's formula; Eliashberg
function; mass enhancement; Migdal's theorem (phonon side); Hall–Bardeen–Blatt edge; electron and hole paths; forbidden
indirect absorption; Holstein–Primakoff transformation; Goldstone mode; coherence factors (cases I and II); Nambu spinor;
conserving approximation; Anderson–Bogoliubov mode; Ward identity; hard momentum cutoff; envelope function; valley-orbit
splitting; central-cell correction.
CONCEPTS: Σ^AH = thermal average of the second-order potential (not e^{−2W}) → D.16; RIA ⇒ second derivatives from first
derivatives at Q = 0 → D.16; DFPT phonons include Π(Q,0) ⇒ add only Π(ω) − Π(0) → D.17; λ_ep = Σ γ/ω² and = mass
enhancement → D.17; hole paths fit the one-electron sum on shell → D.18; AF magnons linear because of pair mixing → D.19;
mean-field BCS response breaks charge conservation; the phase channel restores it → D.21; Dirac screening is logarithmic
and Lorentz invariant up to the cutoff → D.22; central-cell correction acts only on A₁ → D.23.
CLAIMS: Σ^FM retarded form (D.16, cited Giustino Eqs. (157)–(158)); RIA relation (D.16, cited Giustino Eqs. (193)–(198));
γ^ep vanishes below E_g in an undoped insulator at T = 0 (D.17, derived); λ_ep–γ relation (D.17, derived); four-path
amplitude (D.18, derived, Fock-space check); HBB edge (D.18, derived; cited Hall, Bardeen and Blatt 1954); ω^M_k (D.19,
derived; = eq:E.9-afm); Δ(0)/T_c = 1.764 (D.20, derived); conserving response vanishes at q = 0 and obeys the f-sum (D.21,
derived; lattice check); c_AB = v_F/√3 (D.21, cited Anderson 1958, numerical 0.579); Dirac ε with hard cutoff (D.22,
derived; = 1708.08929 Eqs. (2.6), (2.7) with Λ → e^{−5/6}Λ); Si EMT donor 29.7 meV variational (D.23, derived).
INDEX: Allen–Heine; Allen–Cardona; Fan–Migdal; rigid-ion approximation; acoustic sum rule; Debye–Waller (not); Kohn
anomaly; Allen's formula; Eliashberg function; mass enhancement; Migdal theorem; indirect absorption; Hall–Bardeen–Blatt;
Holstein–Primakoff; linear spin-wave theory; NiO type-II order; BCS gap equation; Euler's constant; coherence factors;
Nambu formalism; Ward identity; Anderson–Bogoliubov mode; Dirac material, polarization; effective-mass theory; donor,
shallow; valley-orbit splitting; central-cell correction.
