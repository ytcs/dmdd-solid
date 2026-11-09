# SEAM: Appendix D.12, D.13, D.14, D.15 (long derivations for 4.9, 5.1, 5.5, 5.6, 6.1, 6.2)

Length (detex, math excluded): D-12 ≈ 2,310 (planned 2,000); D-13 ≈ 1,860 (2,500); D-14 ≈ 1,690 (2,500); D-15 ≈ 1,200 (1,500).
Total ≈ 7,060 prose words (planned 8,500); with displayed math the files are near budget. D.14 is short because E.4 already holds the
Berry-phase and DFPT side; D.13 is short because the counting is done once, by substitution, not term by term.
Lint (BANNED-TERMS): 0 blocking. Remaining hits are false positives: EQ-PUNCT on three aligned displays whose punctuation is inside
(D-12 l. 39, 53, 91); LONG-SENT in D-12, D-13 and D-15 where the linter merges a sentence with the display after it; TITLE on the section title of D.15
("The Bloch identity and the Debye–Waller factor"), kept as the planned title (same pattern as D.11's title).
Register self-check: 0 hits for respectively / in order to / i.e. / e.g. / one obtains / thereby / whereby / thus in all four files;
per file so/gives/therefore/since after revision: D-12 4/5/2/6, D-13 3/2/2/5, D-14 3/4/1/1, D-15 3/1/2/6; no count-teaser or recap
openers; ordinal references replaced by names (exchange / direct / self-energy contractions; "the bracket with one gradient").
Build: full main.tex into /tmp/build-D-b: 0 LaTeX errors; numbering checked in the toc: D.12–D.15 print as D.12, D.13, D.14, D.15 and
D.16 follows. No overfull boxes in the four files (one 21 pt overfull display in D-12 fixed by splitting it). Undefined references from
these files are all to unwritten targets: sec:4.6, 4.8, 4.9, 5.1, 5.2, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, chap:11. Final build: 0 undefined
citations. Overfull boxes of 7 pt and 94 pt in D-16 and one of 18 pt in D-21/22 (other writers).
Checks: figscripts/appD/check_D_b.py (rerun: all pass). D.12: exact diagonalization of four spin-orbitals (complex orbitals, degenerate
occupied and empty pairs) vs the resonant BSE with HF energies and K^x − K^d: error ratio 4.00 on halving the coupling (quadratic);
K^d sign reversed or hole indices n ↔ n′ exchanged: ratio 2.00 (linear); algebra of eq:D.12-Lsol, rank-one head separation
R00 = R̄00/(1 − vR̄00), optical prefactor 8π²α/(Ωω²). D.13: M/m_e = 5.10e4, κ_BO = 0.0665, κ² = 4.43e−3, κ³ = 2.95e−4,
α²m_e = 27.21 eV, κa₀ = 0.035 Å, κ²α²m_e = 0.12 eV; sympy series of the two-oscillator model ω²M/K = 1 − r + (1 − K/k)r²; deviations
5.0e−5, 5.0e−7, 5.0e−9 at m/M = 1e−2, 1e−3, 1e−4 (K = k/2); diagonal correction m_eω_e/(4M). D.14: eliminating ℰ = adding C^na for a
random anisotropic three-atom model (bordered-matrix singular values); generalized LST to 1e−12 with three polar modes; zeros of ε(ω)
at the LO frequencies; Fröhlich limit of eq:D.14-gL; Hermiticity eq:A.6-herm of g^L with complex polarization vectors; polariton scale
√13·30 meV = 0.11 eV vs 2π/a = 2.2 keV (ratio 5e−5). D.15: Bloch identity in a truncated Fock space for complex, non-Hermitian A; Debye
bracket closed form vs direct coth integral; value 4.11 at T = ω_D; high-T expansion 3q²T/(Mω_D²)[1 + ω_D²/36T²].
Shared files: appD.tex (inputs D-12…D-15 after D-11; the line `\setcounter{section}{15}% D.12–D.15 not yet written` that another writer
had put there was removed, since the four sections now exist); book.bib (10 entries appended, DOIs checked on Crossref 2026-11-02:
hanke1980many, strinati1988application, rohlfing2000electron, born1927quantentheorie, born1954dynamical (book, no DOI),
lyddane1941polar, frohlich1954electrons, cochran1962dielectric, gonze1997dynamical, pick1970microscopic; onida2002electronic was
already present and is cited). Sources: equation numbers read from existing extracts (arXiv numbering): Blase et al. 2006.09440
Eqs. (18), (20); Baroni et al. cond-mat/0012092 Eqs. (89)–(91), (98), Sect. II.D.2; Verdi–Giustino 1510.06373 Eqs. (1), (4). No new
sources folder.

## The reader now knows
- D.12: pair propagator 𝖫_{mn,m′n′}(τ) = −⟨T c†_n c_m(τ) c†_{m′}c_{n′}(0)⟩ (eq:D.12-L) and R_GG′ = V⁻¹ρ*𝖫ρ (eq:D.12-R);
  𝖫⁰ = TΣ𝖦𝖦 = (n_F(ξ_n) − n_F(ξ_m))/(iω^B − ξ_m + ξ_n) (eq:D.12-L0, from eq:D.10-sum); first-order contractions classified (exchange:
  two loops, sign +; direct: one loop, sign − by the loop rule of D.11; self-energy → quasiparticle energies); K^x and K^d in real
  space (eq:D.12-kernels); attraction from −K^d with K^d_diag > 0; screened rung W^scr = ε⁻¹v_C, exchange line unscreened; consistency
  with Σ = Hartree + GW (δW/δG neglected, cited Hanke–Sham, Strinati); static approximation = instantaneous rung → frequency sums
  factorize → algebraic BSE 𝖫 = 𝖫⁰ + 𝖫⁰(K^x − K^d)𝖫 (eq:D.12-BSE); validity vs ω_p = 16.6 eV; spin: singlet g_degK^x − K^d, triplet
  −K^d, density creates singlets only; T = 0 insulator: 𝖫 = (iω − D − FK)⁻¹F (eq:D.12-Lsol), block form with H^exc and coupling
  block (eq:D.12-blocks), Hermiticity conditions (real symmetric static W^scr); Tamm–Dancoff eigenproblem (eq:D.12-eig); crystal
  kernels with ρ_cv and W^scr_GG′ (eq:D.12-crystal), 1/V count; R00 in exciton eigenstates (eq:D.12-Rexc); exciton S(q, ω)
  (eq:D.12-S, with g_deg); G = 0 separation → ε_mac = 1 − v_C R̄00 (eq:D.12-epsmac); ε₂ in the optical limit (eq:D.12-eps2) with IP
  check 8π²α/(Ωω²); long-range exchange splits longitudinal/transverse excitons.
- D.13: H = T_N + H_el(u) (eq:D.13-H); adiabatic states (eq:D.13-adiabatic), real, no level crossing; exact expansion and coupled
  equations (eq:D.13-coupled) with non-adiabatic operators 𝒩_ji (eq:D.13-N: first- and second-derivative couplings); BO approximation
  (eq:D.13-BO); Born–Huang adiabatic approximation (diagonal term, positive); Hellmann–Feynman force (eq:D.13-HF); off-diagonal
  derivative coupling = force matrix element / excitation energy (eq:D.13-dcoup); power counting in a₀ and α²m_e: ℓ/a₀ ~ κ_BO,
  ω_ph ~ κ_BO²α²m_e (eq:D.13-scales); cubic κ³ (η_anh ~ κ_BO), anharmonic shifts κ⁴, first-derivative coupling κ³, second-derivative
  and diagonal κ⁴, all non-adiabatic shifts of vibrational levels κ⁶ (relative m_e/M); silicon κ numbers; small ΔE: mixing amplitude
  (ω_ph/ΔE)(ℓF/ΔE) (eq:D.13-mixing), → ω_ph/E_g in insulators, breakdown near the Fermi surface in metals (→ Migdal, 6.3);
  clamped-nuclei expansion (eq:D.13-expand) → H_ep of eq:A.6-Hep with the bare vertex, screened in 6.2; quadratic term → Allen–Heine;
  equivalence of the two expansions at first order; solvable electron + nucleus model (eq:D.13-model): M → M + m_e at first order.
- D.14: long-wavelength energy E^ad(u, ℰ) (eq:D.14-U) with C^an, Z*, ε∞; F and P (eq:D.14-FP); Z* index convention (force index
  first) and Maxwell relation; transposed convention of Baroni noted; coupling −e u·Z*·ℰ (→ dark photon, Chap. 11); ΣZ* = 0
  (eq:D.14-neutral) from translation invariance of the dipole of a neutral cell; electrostatic elimination of ℰ (∇×ℰ = 0, Q·D = 0) →
  nonanalytic C^na (eq:D.14-na) = eq:E.4-na; direction dependence at Q → 0; Pick–Cohen–Martin; polariton scale ~10⁻⁴ of the zone;
  cubic diatomic LO–TO (eq:D.14-LOTO) with μ_red; ε(ω) (eq:D.14-eps); LST (eq:D.14-LST); longitudinal modes at zeros of ε, transverse at
  poles; multi-mode mode charges 𝐳_ν and generalized LST (eq:D.14-LSTgen, Cochran–Cowley) with the interlacing argument; long-range
  vertex g^L (eq:D.14-gL, = Verdi–Giustino Eq. (4) G = 0 term in A.6 normalization), Hermiticity verified; Fröhlich form
  (eq:D.14-frohlich) with (1/ε∞ − 1/ε0).
- D.15: proof of Bloch's identity (eq:D.15-bloch) for complex, non-Hermitian A by trace cyclicity (Wick in generating-function form);
  hypotheses; anharmonic cumulant corrections (qualitative); B_κ mode sum (eq:D.15-B), real symmetric positive, limits T = 0 and
  high T, infrared finiteness; e^{−W} (eq:D.15-W); 𝒞_κκ′(R, t) mode sum (eq:D.15-C); generating formula (eq:D.15-gen) via
  eq:C.6-product, one-nucleus form of 5.6, multiphonon sorting; Debye model at any T (eq:D.15-debye), T = 0: (3/2)E_R/ω_D, high T
  with zero-point correction, bracket 4.11 at T = ω_D.

## Symbols introduced (with defining equation)
In NOTATION already and used: W^scr, A^λ_cvk, E_λ, g_deg, ρ_mn, R_GG′, 𝖦, ω^F_j, ω^B_j, n_F, ξ (as ξ_m, quasiparticle energy from
μ_ch), E^ad, κ_BO, F_κ (here F_Rκ), M_κ, u_Rκ, Φ^(n), ℰ, 𝐏 (\vect{P}), 𝐃 (\vect{D}, as in E.4), Z*_κ (Z^{*,αβ}_κ), ε∞, ε₀, ω_L, ω_T,
μ_red, g^L, ε_mac, ε₂, B_κ, W_κ(q), 𝒞_κκ′, g_ph(ω), ω_D, n_B, a₀, ω_ph (estimates only), E_F, E_g.
New (proposed below): 𝖫_{mn,m′n′}, 𝖫⁰, K^x, K^d, H^exc, 𝐅 and 𝐃 (bold upright, local matrices of D.12), \bar R_00, \bar K^x, \bar A^λ,
\bar E_λ, H_el, Ψ_i(r; u), E_i(u), Ψ^nuc_i, 𝒩_ji, v_κ, ΔE, F_j0, ℓ_zp, C^an_κκ′, C^na_κκ′(Q̂), ω_Tν, ω_Lν, 𝐳_ν, V^L, E^ad_ℰ, K_rr̄. E_R (q²/2M) uses the existing NOTATION row (1.3).
Local to one passage (no ledger row needed): Â_γ (D.15, one-mode pieces of Â), v_ab,cd (D.12 orbital matrix element), η₁, η₂, θ, F(θ) (D.15 proof), x, p, X, P, k_e, K_N,
ω_e, ω_BO (D.13 model), w (D.14 relative displacement), C₀ (D.14), a_ν (D.14 normal coordinates), ℰ_∥ (D.14).

## Terms introduced
Pair propagator (two-particle correlation function at pairwise equal times); transition (resonant, antiresonant); exchange
contraction, direct contraction, self-energy contraction; exchange kernel, direct kernel; ladder; static (screening) approximation;
singlet and triplet excitons; Tamm–Dancoff approximation; coupling block; transition-basis Hamiltonian; oscillator strength of an
exciton (coherent sum); long-range exchange; longitudinal–transverse exciton splitting (named). Adiabatic states; non-adiabatic
coupling operators; first-derivative (derivative) coupling; second-derivative (scalar) coupling; Born–Oppenheimer approximation vs
Born–Huang adiabatic approximation; diagonal (adiabatic) correction; Hellmann–Feynman theorem; power counting in κ_BO; clamped-nuclei
(crude adiabatic) expansion; mass dragging. Long-wavelength energy at fixed field (electric enthalpy, not named); Maxwell relation for
Z*; charge neutrality (acoustic sum rule) of Born charges; analytic and nonanalytic parts of the dynamical matrix; electrostatic
limit; phonon polariton (named); LO–TO splitting; Lyddane–Sachs–Teller relation and its generalization; mode charge vector;
long-range (Fröhlich) vertex. Bloch's identity (proof); cumulant expansion (named); displacement tensor; displacement correlation;
generating formula; Debye model of 2W at finite T; free recoil energy E_R.

## Threads: opened / advanced / closed
- None (appendix).

## Promises made to later sections
- 4.9: may quote eq:D.12-BSE, eq:D.12-eig (H^exc = eq:E.6-Hexc), eq:D.12-S (with g_deg and ρ*), eq:D.12-epsmac, eq:D.12-eps2; D.12
  points to 4.8 for W^scr = ε⁻¹v_C and the GW self-energy, and to 4.6 for local fields. 4.9 should state the static approximation's
  validity with the same scale (ω_p = 16.6 eV for Si).
- 5.1: eq:D.13-coupled/N/BO/HF/scales; D.13 says 5.1 compares κ_BO a₀ = 0.035 Å and κ²α²m_e = 0.12 eV with measured amplitudes and
  phonon energies (WE 5.1). E^ad's argument is "the set of nuclear positions".
- 5.2: D.14 uses the acoustic sum rule Σ_κ′ C^an_κκ′ = 0 and g_ph normalized to three modes per cell for one atom per cell (D.15);
  5.2 should state its normalization of g_ph.
- 5.5: eq:D.14-U/FP/neutral/na/LOTO/eps/LST/LSTgen; D.14 defines Z* force-index-first.
- 5.6: eq:D.15-B/W/C/gen/debye; D.15 says 5.6 computes 2W for silicon from the full mode sum; 𝒞_κκ′(t) is the shorthand for
  𝒞_κκ′(R, t) "where cell and time are clear".
- 5.7: D.13 gives η_anh ~ κ_BO and anharmonic shifts at κ⁴; D.15 says anharmonicity adds a fourth cumulant.
- 6.1: eq:D.13-N (both coupling operators), eq:D.13-dcoup, eq:D.13-expand, eq:D.13-mixing; κ⁶ counting.
- 6.2: eq:D.14-gL and eq:D.14-frohlich in A.6 normalization; D.14 says 6.2 writes the vertex through Fröhlich's coupling constant and
  evaluates it for GaAs. D.13 says the bare vertex is screened in 6.2.
- 6.3: D.13 points to Migdal's theorem for metals (ω_ph/E_F) and to the Allen–Heine term as the quadratic part of eq:D.13-expand.
- Chap. 11: D.14 says the coupling −e u·Z*·ℰ is how a dark photon drives optical phonons.

## Open questions for the editor
1. App. E.4, eq:E.4-epsZ writes eZ^{*,αβ} = Ω∂P^α/∂u^β = ∂F^α/∂ℰ^β. With NOTATION's Z* = ∂F/∂ℰ (force index first) the Maxwell relation
   gives Ω∂P^β/∂u^α = ∂F^α/∂ℰ^β, the transpose; eq:E.4-na writes (Q·Z*_κ)_α where the force-first convention needs (Z*_κ·Q)^α. The two
   agree for cubic sites only. D.14 states the force-first convention and the Maxwell relation explicitly.
2. App. C.6 says D.15 proves Bloch's identity "following Mermin". D.15's proof uses trace cyclicity (it is Wick's theorem in
   generating-function form) and credits Mermin for a short evaluation by a different route, since Mermin 1966 could not be read
   (paywalled). Suggest C.6 reads "App. D.15 gives a proof".
3. App. E.6 writes the exciton oscillator strength as |Σ A^λ ρ_cv|²; D.12 derives |Σ A^λ ρ_cv*|² (equal for real envelopes only).
4. C_F: D.14 does not fix it. If 6.2 writes g^L = i C_F ρ_mn/Q, then C_F² = (e²ω_L/2Ω)(1/ε∞ − 1/ε0) in the A.6 normalization.
5. NOTATION says italic K is not used in Part I; D.12 uses K^x, K^d as E.6 already does. Rows proposed below.
6. 𝒞_κκ′ now carries a cell argument, 𝒞_κκ′(R, t); NOTATION row should be updated.
7. K^x convention: D.12 writes K^x for the full exchange kernel (all G, needed for the complete R and S(q, ω)) and K̄^x for its
   local-field part (G ≠ 0, needed for ε_mac). App. E.6 (eq:E.6-Hexc) and the 4.9 spine row call the local-field part K^x. D.12 says
   once that E.6's H^exc is its H^exc with K̄^x; 4.9 should either adopt D.12's bar or state the same identification.
8. D.14's energy at fixed field is written E^ad_ℰ(u, ℰ) (reduces to E^ad at ℰ = 0), to keep E^ad for the surface alone.

## Proposed ledger rows (the editor merges them)
NOTATION:
| 𝖫_{mn,m′n′}(τ), 𝖫⁰ | pair propagator −⟨T c†_n c_m(τ) c†_{m′}c_{n′}(0)⟩ (sans-serif, like 𝖦); its independent-quasiparticle value | eV⁻¹ | D.12 (4.9) |
| K^x, K^d | exchange and direct kernels of the Bethe–Salpeter equation (superscripts mandatory; italic K only with them) | eV | D.12 (4.9) |
| H^exc | resonant (Tamm–Dancoff) transition-basis Hamiltonian | eV | D.12 (4.9) |
| R̄, K̄^x, Ā^λ, Ē_λ | quantities built with the exchange kernel without its G = 0 term (bar mandatory) | as unbarred | D.12 |
| H_el(u) | electronic Hamiltonian at fixed nuclei (T_e + V_ee + V_eN + V_NN) | eV | D.13 (5.1) |
| Ψ_i(r; u), E_i(u), Ψ^nuc_i(u) | adiabatic electronic states and energies (E_0 = E^ad); nuclear wavefunctions (superscript mandatory) | —; eV | D.13 (5.1) |
| 𝒩_ji | non-adiabatic coupling operator (script N with two state labels; 𝒩_F is the DOS) | eV | D.13 (6.1) |
| V_eN, V_NN, V_ee, T_e | electron–nucleus, nucleus–nucleus, electron–electron energies; electron kinetic energy | eV | D.13 (2.3) |
| ℓ_zp | zero-point amplitude in estimates (ℓ_Qν is the mode length) | Å | D.13 |
| C^an_κκ′, C^na_κκ′(Q̂) | zone-center force constants at zero macroscopic field; nonanalytic (dipole) force constants | eV Å⁻² | D.14 (5.5) |
| ω_Tν, ω_Lν | transverse and longitudinal zone-center frequencies of polar mode ν (generalized LST) | meV | D.14 (5.5) |
| 𝐳_ν | mode charge vector Σ_κ e_κν·Z*_κ/√M_κ | eV^{−1/2} | D.14 (5.5) |
| E^ad_ℰ(u, ℰ) | energy per cell at fixed macroscopic field (electric enthalpy); E^ad at ℰ = 0 | eV | D.14 (5.5) |
| K_rr̄ | coupling (resonant–antiresonant) block of the BSE kernel | eV | D.12 (4.9) |
| V^L(r) | potential energy of an electron in the macroscopic field of a longitudinal phonon | eV | D.14 (6.2) |
| 𝒞_κκ′(R, t) | displacement correlation ⟨u_Rκ(t)u_0κ′(0)⟩; 𝒞_κκ′(t) when R is clear (update of the existing row) | Å² | D.15 (5.6) |
GLOSSARY: pair propagator; exchange kernel; direct kernel; static (screening) approximation; Tamm–Dancoff approximation; singlet and
triplet excitons; adiabatic states; non-adiabatic coupling (first- and second-derivative); Born–Huang adiabatic approximation;
Hellmann–Feynman theorem; analytic / nonanalytic part of the dynamical matrix; Lyddane–Sachs–Teller relation (generalized); mode
charge; long-range (Fröhlich) vertex; Bloch's identity; displacement correlation; generating formula.
CONCEPTS: BSE from the static ladder (D.12 → 4.9); κ_BO power counting with κ⁶ non-adiabatic shifts (D.13 → 5.1, 6.1); derivative
coupling = force / gap (D.13 → 6.1, 6.3); nonanalytic term from the G = 0 Coulomb term (D.14 → 5.5, 6.2, E.4); LST from the zeros and
poles of ε(ω) (D.14 → 5.5); g^L → Fröhlich (D.14 → 6.2); Bloch identity ⇔ Wick for linear operators (D.15 → 5.6, C.6).
CLAIMS: (D.12) static ladder kernel = δ(v_H + Σ^GW)/δG with δW/δG neglected [cited Hanke–Sham 1980, Strinati 1988]; TDA error second
order in K/2E_g [estimate]; resonant block = Blase et al. Eq. (20) [checked, arXiv 2006.09440]. (D.13) BO orders κ⁰, κ², κ⁴, κ⁶ [cited
Born–Oppenheimer 1927; derived]. (D.14) C^na = Baroni Eq. (98) with 4πe_G² → e² [checked]; g^L = Verdi–Giustino Eq. (4), G = 0 term
[checked]; Fröhlich form = Verdi–Giustino Eq. (1) [checked]; generalized LST [cited Cochran–Cowley 1962; derived]. (D.15) Bloch
identity [derived; Mermin 1966 credited].
INDEX: Bethe–Salpeter equation (derivation); ladder diagrams; Tamm–Dancoff approximation; singlet exciton; triplet exciton;
static screening approximation; Born–Oppenheimer approximation (expansion); non-adiabatic coupling; Hellmann–Feynman theorem;
Born–Huang adiabatic approximation; nonanalytic term; LO–TO splitting; Lyddane–Sachs–Teller relation; Cochran–Cowley relation;
Born effective charge (sum rule); Fröhlich vertex; phonon polariton; Bloch's identity; Debye–Waller factor (finite temperature);
displacement correlation; Debye model (Debye–Waller exponent).
