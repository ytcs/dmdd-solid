# SEAM: Appendix D.4, D.5, D.8, D.9, D.11 (long derivations for 3.4, 4.5, 4.8)

Length (detex): D-4 ≈ 1,640 (planned 1,500); D-5 ≈ 1,560 (2,000); D-8 ≈ 1,180 (2,000); D-9 ≈ 1,180 (1,500); D-11 ≈ 2,480
(2,000). Total ≈ 8,040 (planned 9,000); D.8 is short because C.8 already holds the Lindhard logarithms and their branch.
Lint (BANNED-TERMS): 0 blocking. Remaining hits are false positives: EQ-PUNCT on gathered/aligned displays whose punctuation is
inside, one EQ-PUNCT on eq:D.5-gap (sentence continues "for the exact functional"), LONG-SENT merges across displays, one MONOTONY
in D-11 (T = 0 expansion paragraph).
Register self-check: 0 hits for respectively / in order to / i.e. / e.g. / one obtains / thereby / whereby in all five files;
per file so/gives/therefore/since: D-4 4/5/3/9, D-5 3/6/2/3, D-8 4/2/0/7, D-9 4/4/0/4, D-11 9/6/2/6; no count-teaser openers.
Build: full main.tex into /tmp/build-D-a: 0 LaTeX errors, 0 undefined citations, no overfull boxes in the five files except a
0.14 pt running head of D.5. Numbering checked in the aux: D.4, D.5, D.8, D.9, D.10, D.11 print with their planned numbers
(another writer has since added D-6 and changed the counter line to `{7}% D.7 not yet written`; numbering still correct).
Checks: figscripts/appD/check_D_a.py asserts the printed forms of eq:D.8-Rz and eq:D.9-eps against the tested forms, and every number and closed form quoted (exchange self-energy vs quadrature; ⟨F_L⟩ = 3/4;
E_x/N = −0.916/r_s Ry = −6.22 eV at r_s = 2.0; HF widening αk_F/π = 8.29 eV, width 20.8 eV; v_x^LDA = Σ_x(k_F) = −8.29 eV, Slater
−12.4 eV; antiderivative 𝓘(w) for complex w; R⁰ closed form vs 2D quadrature at complex z (1e−6); static = −2𝒩_F F_L; Im R⁰ = −S⁰/2
of eq:4.2-gas on a grid; high-frequency coefficient (3/5)q²v_F² + (q²/2m)²; f-sum to 1e−6 at q = 0.4, 1, 2.5 k_F; Mermin static
limit, Drude limit at q → 0, perfect screening vs naive substitution, f-sum of both to 1e−4 at γ_rel = 0.1E_F). Rerun: all pass.
Shared files: appD.tex (inputs D-4, D-5 after D-3; `\setcounter{section}{7}`; D-8, D-9; old `{9}` line deleted; D-11 after D-10);
book.bib (16 entries appended, DOIs checked on Crossref 2026-11-02). Sources: APS full texts blocked (403); no extracts kept,
no sources/ folder created.

## The reader now knows
- D.4: determinant energy (eq:D.4-energy, from 2.3's display); density matrix ϱ(x,x′), invariance under occupied rotations;
  variation with Lagrange multipliers → h_HF = −∇²/2m_e + U_1 + v_H + Σ_x (nonlocal Fock term); canonical HF eqs (eq:D.4-HF);
  self-interaction cancellation, exchange hole integrates to one electron; Σ_x = first-order self-energy (→ 4.7, D.11);
  E_γ, total energy with double counting (eq:D.4-Etot); Koopmans with the frozen-orbital hypothesis (eq:D.4-koopmans);
  relaxation vanishes as 1/N for Bloch states (stationarity argument); missing correlation/screening → HF gap too large (→ GW 4.8).
  Electron gas: Σ_x(k) = −(e²k_F/2π²)F_L(k/k_F) (eq:D.4-gas) with F_L of eq:C.8-FL; HF band widened by αk_F/π (8.29 eV at Si
  valence density, 20.8 eV width); log-divergent velocity at k_F; E_x/N = −3αk_F/4π = −0.916/r_s Ry = −6.22 eV (eq:D.4-Ex).
- D.5: HK1 by contradiction (nondegenerate GS; Ψ ≠ Ψ′ step shown); Levy constrained search 𝓕[𝓃] (eq:D.5-levy), HK2 by two-step
  minimization (no nondegeneracy / v-representability needed), Euler–Lagrange with μ_ch; K_s, E_H, E_xc split (eq:D.5-Exc);
  KS equations by orbital variation (eq:D.5-KS), local vs nonlocal; noninteracting v-representability assumed; crystal form →
  eq:E.1-density; total energy (eq:D.5-Etot); Janak (eq:D.5-janak, derived); HOMO = −I, affinity level = −A from piecewise
  linearity (cited PPLB); E_g = E_g^KS + Δ_xc (eq:D.5-gap, cited Perdew–Levy, Sham–Schlüter); Si: most of LDA gap error is Δ_xc
  (cited Godby–Schlüter–Sham); LDA (eq:D.5-LDA), v_x^LDA = (4/3)ε_x = Σ_x(k_F); Slater's average = (3/2)v_x; correlation from QMC
  (CA/PZ); self-interaction residue; GGA/hybrids → E.1.
- D.8: R⁰ at T = 0 for complex z (eq:D.8-Rz) via relabeling, angular logs, radial antiderivative 𝓘(w) (same as D.4); Re
  (eq:D.8-Re) and Im (eq:D.8-Im) by eq:C.8-branch; three regions; Im R⁰ = −S⁰/2 of WE 4.x (FDT at T = 0); static −2𝒩_F F_L
  (eq:D.8-static), Thomas–Fermi k_TF² = 2e²𝒩_F; small-q fixed-ν form −2𝒩_F[1 − (ν/2)ℓ(ν)] (eq:D.8-smallq); high-frequency
  expansion 𝓃_e q²/(m_e z²)[1 + ((3/5)q²v_F² + (q²/2m_e)²)/z²] (eq:D.8-highfreq); f-sum analytically for q > 2k_F.
- D.9: coherences δϱ_k = ⟨c_k†c_{k+q}⟩ and their equation of motion (one-electron Liouville eq.) → R⁰; relaxation-time term;
  naive (global equilibrium) vs Mermin (local equilibrium, φ_loc, eq:D.9-condition); R^Mer (eq:D.9-R) and ε_Mer in Mermin's
  form (eq:D.9-eps); valid at any T (isothermal static response, Matsubara j = 0 of 4.7); continuity equation from the summed
  equation of motion with j_e(q)† = Σ(k + q/2)/m_e c_k†c_{k+q} (eq:D.9-continuity); limits: static R^Mer → R⁰(q,0); q → 0 Drude
  ε = 1 − ω_p²/ω(ω + iγ_rel), σ_cond = ω_p²/(γ_rel − iω); perfect screening kept; naive substitution gives an insulator
  (ε → 1 + ω_p²/γ_rel²); f-sum obeyed by both.
- D.11: imaginary-time expansion U_I(τ,0) = T_τ exp(−∫H_int) and 𝖦 = −⟨T_τ U_I(β,0)c c†⟩₀/⟨U_I(β,0)⟩₀ (eq:D.11-Gexp), exact;
  equal-time convention (c† at τ + 0⁺); T = 0 real-time form via Gell-Mann–Low (eq:D.11-GT; hypotheses stated, theorem cited);
  Wick's theorem proved by Gaudin's trace argument (eq:D.11-wick), bosons, mixed strings, time ordering, T = 0 limit;
  contractions (eq:D.11-contract); linked-cluster cancellation (combinatorics shown); Coulomb rules in Matsubara space with the
  sign (−1)^n(−1)^F derived (open line vs loop), n!2^n cancellation, frequency/momentum counting, rules 1–5 (enumerated);
  Hartree and Fock at first order (eq:D.11-fock) checked against D.4; boson exchange: 𝖣₀(Q, iω^B) = 2ω_Q/((iω^B)² − ω_Q²)
  (eq:D.11-D0), rule v_C → |g|²𝖣₀ (eq:D.11-boson), static attraction −2|g|²/ω_Q, sign change at ω_Q, first boson self-energy
  written (→ 4.8 WE); T = 0 rules: i^n(−1)^F, line +i v_C/V, ∫dω/2π, Fock check, 𝖣₀(Q,ω) = 2ω_Q/(ω² − ω_Q² + i0⁺).

## Symbols introduced (with defining equation)
In NOTATION already and used as listed: 𝓃(r) (\nd), V_KS, v_xc, E_xc, r_s, R⁰, ε_Lin, ε_Mer, γ_rel, k_TF, 𝒩_F, 𝖦, 𝖦₀, ω^F_j,
ω^B_j, H₀, U_1, U_2, U_I, j_e(q), σ_cond, ω_p, ϱ̂ (here as the kernel ϱ(x,x′)), H_μ (proposed by 4.7). New, proposed below.

## Terms introduced
Hartree–Fock equations; Fock (exchange) operator; Hartree potential; Lagrange multipliers (orthonormality); canonical orbitals;
virtual orbitals; exchange hole; Koopmans' theorem; frozen orbitals; orbital relaxation; double counting; HF band widening;
exchange energy of the electron gas; Hohenberg–Kohn theorems; universal functional; constrained search (Levy);
N-representability (named); Kohn–Sham equations; noninteracting v-representability; independent-electron kinetic energy;
Hartree energy; Janak's theorem; fractional occupation; piecewise linearity; ionization energy, electron affinity;
fundamental gap; derivative discontinuity Δ_xc; local-density approximation; Slater exchange; self-interaction error;
Lindhard function (closed form); Thomas–Fermi limit; semiclassical (small-q) Lindhard form; coherences (one-electron density
matrix); relaxation-time approximation; local equilibrium; Mermin dielectric function; continuity equation; Drude dielectric
function; perfect screening; interaction picture in imaginary time; Gell-Mann–Low theorem; adiabatic switching; Wick's
theorem; contraction; pairing sign; linked-cluster theorem; vacuum diagrams; Feynman rules (Matsubara and T = 0); fermion loop
sign; topologically distinct diagrams; boson propagator; boson-mediated (retarded) interaction.

## Threads: opened / advanced / closed
- None (appendix).

## Promises made to later sections
- 3.4: uses eq:D.4-HF, eq:D.4-koopmans, eq:D.4-gas/Ex, eq:D.5-KS, eq:D.5-Etot, eq:D.5-gap, eq:D.5-LDA; 3.4 should cite D.4 for
  the qualitative "HF gap too large" (D.4 gives no number) and may quote the Si numbers −6.22 eV, 8.29 eV.
- 4.5: eq:D.8-Rz/Re/Im/static/smallq/highfreq (plasmon dispersion and q_c come from eq:D.8-highfreq and the edge ω_+ = qv_F +
  q²/2m_e named in D.8), eq:D.9-R/eps; 4.5's LO (iv) f-sum and perfect screening are checked in D.8/D.9.
- 4.8: eq:D.11-Gexp, -wick, -contract, -fock, -D0, -boson and the enumerated rules; the Einstein-boson self-energy displayed in
  D.11 (unlabeled) is the starting point of WE 4.14; GW (4.8) is pointed to from D.4 as "the screening that is missing".
- 6.2: g(Q) → g_mnν, d_Q → b_Qν stated in D.11. 7.2: boson-exchange attraction pointed to.

## Undefined references from these files (all to unwritten targets)
sec:3.4, sec:4.3, sec:4.4, sec:4.5, sec:4.8, sec:6.2, sec:7.2.

## Open questions / for the editor
1. No full texts could be fetched (APS returns 403 for the bronze-OA PDFs; others paywalled; none on arXiv). Hohenberg–Kohn, Kohn–Sham,
   Levy, Janak, PPLB, Perdew–Levy, Sham–Schlüter, Godby–Schlüter–Sham, Slater, Mermin, Gell-Mann–Low, Wick, Gaudin, Fock, Koopmans
   are cited for attribution without equation numbers; every result used is derived in the appendix except: piecewise linearity
   of E(N) (PPLB), the derivative discontinuity and eq:D.5-gap (Perdew–Levy, Sham–Schlüter), the Si statement that most of the LDA
   gap error is Δ_xc (Godby–Schlüter–Sham; from memory of the abstract, please verify), and the Gell-Mann–Low theorem itself.
2. Chapter numbers cited from memory: Giuliani–Vignale Chap. 2 (HF) and Chap. 4 (Lindhard); Martin Chaps. 6–7 (DFT foundations,
   KS); Fetter–Walecka Chaps. 3, 7; Bruus–Flensberg Chaps. 10–11 (please confirm against the Crossref chapter DOIs as 4.7 did).
3. Symbol K_s for the independent-electron kinetic energy (literature T_s; T is temperature) — editor to confirm; alternative
   E_kin,s. Likewise 𝓕[𝓃] (script F) for the universal functional.
4. "N" in D.4: N_e electrons, N cells (NOTATION entry 38); 2.3's Slater determinant uses bare N for particle number.
5. D.5's running head overflows by 0.14 pt; a short title `\section[Hohenberg--Kohn and Kohn--Sham]{…}` would fix it.
6. D.9 gives no numerical γ_rel for silicon or a metal (no source in hand); 4.5 must supply one if it quotes one.
7. The boson coupling g(Q) of D.11 is a new generic symbol; NOTATION entry 20 reserves bare g for the e–ph vertex. Alternative:
   write g_Q or reuse g with a "generic boson" note (as done).

## Proposed ledger rows (the editor merges them)
NOTATION:
| h, h_HF | one-body Hamiltonian −∇²/2m_e + U_1; Hartree–Fock (Fock) operator (D.4 only; bare h is the Hubble parameter, entry 45) ⚑ | eV | D.4 |
| v_H(r) | Hartree potential ∫e²𝓃(r′)/4π\|r − r′\| (upright H; cf. v_xc) | eV | D.4 |
| Σ_x(x, x′), Σ_x(k) | exchange (Fock) self-energy; its plane-wave value −(e²k_F/2π²)F_L(k/k_F) in the gas (Σ always decorated, entry 16) ⚑ | eV | D.4 |
| ϱ(x, x′) | one-body density matrix Σ_occ ψ_γ(x)ψ_γ*(x′) (kernel of ϱ̂; x = (r, s)) ⚑ | Å⁻³ | D.4 |
| λ_γγ′ | Lagrange multipliers of orthonormality (D.4, D.5 only; λ is also the exciton label) ⚑ | eV | D.4 |
| 𝓜 | unitary matrix of occupied-orbital rotations (D.4 only; script M; 𝓜¹ is the moment matrix) ⚑ | 1 | D.4 |
| E_γ (HF/KS) | Hartree–Fock or Kohn–Sham orbital eigenvalue (2.3's orbital energy; ε_nk in a crystal) | eV | D.4 |
| E^HF_k | Hartree–Fock band of the gas k²/2m_e + Σ_x(k) | eV | D.4 |
| E_x | exchange energy (E_x/N_e per electron) | eV | D.4 |
| Ry | Rydberg α²m_e/2 = 13.61 eV (unit) | eV | D.4 |
| 𝓕[𝓃] | Levy–Lieb universal functional min_{Ψ→𝓃}⟨H_kin + H_ee⟩ (script F) | eV | D.5 |
| H_kin | kinetic-energy operator Σp²/2m_e (decorated H) | eV | D.5 |
| K_s[𝓃] | independent-electron (Kohn–Sham) kinetic energy (literature T_s; T is temperature) ⚑ | eV | D.5 |
| E_H[𝓃] | Hartree energy | eV | D.5 |
| n_γ (fractional) | orbital occupations in Janak's theorem (2.5's n_γ; f_nk in a crystal) | 1 | D.5 |
| I, A | ionization energy, electron affinity (D.5 only; I is the nucleus index, A the mass number, entry 26) ⚑ | eV | D.5 |
| E_HOMO, E_LUMO | highest occupied and lowest unoccupied KS eigenvalues | eV | D.5 |
| E_g^KS, Δ_xc | Kohn–Sham gap; derivative discontinuity (subscript mandatory, entry 14) | eV | D.5 |
| ε_xc(𝓃), ε_x(𝓃) | exchange–correlation and exchange energy per electron of the uniform gas (ε decorated, like ε_eh; entry 2) ⚑ | eV | D.5 |
| v_x^LDA, v_xc^LDA | LDA exchange and exchange–correlation potentials | eV | D.5 |
| ν, y, κ, ν_± | Lindhard variables z/qv_F, q/2k_F, k/k_F, ν ± y (D.8 only; ν is also the phonon branch) ⚑ | 1 | D.8 |
| 𝓘(w), ℓ(w) | radial Lindhard integral w + ½(1 − w²)ℓ(w); ℓ(w) = ln[(w + 1)/(w − 1)] (D.8 only; ℓ is the cubic index, ℓ_Qν the phonon length) ⚑ | 1 | D.8 |
| δϱ_k(t) | coherence ⟨c_k†c_{k+q}⟩ (D.9 only) | 1 | D.9 |
| D_k | ξ_k − ξ_{k+q} (D.9 only; D^dyn, 𝒟_f distinct) ⚑ | eV | D.9 |
| φ_loc(t) | local-equilibrium potential (minus the local chemical-potential shift) in Mermin's construction (decorated φ, entry 21) | eV | D.9 |
| R^Mer | Mermin (relaxation-time, number-conserving) density response; ε_Mer = 1 − v_C R^Mer | eV² | D.9 |
| R⁰_γ, R⁰_st | shorthands R⁰(q, ω + iγ_rel), R⁰(q, 0) (D.9 only) | eV² | D.9 |
| U_I(τ, τ′) | imaginary-time interaction-picture evolution e^{τH₀}e^{−(τ−τ′)H_μ}e^{−τ′H₀} (argument decides real vs imaginary time, as 𝖦) | 1 | D.11 |
| O_I(τ) | interaction-picture operator e^{τH₀}Oe^{−τH₀} | — | D.11 |
| ⟨·⟩₀, 𝒵₀, \|Φ₀⟩ | free grand-canonical average and partition function; Fermi sea (2.3's reference determinant) | — | D.11 |
| H_int | interaction part of H_μ (4.7 uses it) | eV | 4.7 |
| d_Q, ω_Q, φ_Q = d_Q + d†_{−Q} | generic boson mode, energy, field (D.11, 4.8; phonons b_Qν, ω_Qν); φ_Q typeset \varphi, distinct from DM φ ⚑ | —; eV | D.11 |
| g(Q) | generic electron–boson coupling, g(−Q) = g(Q)* (→ g_mnν for phonons) ⚑ | eV | D.11 |
| 𝖣₀(Q, iω^B), 𝖣₀(Q, ω) | free boson propagator 2ω_Q/((iω^B)² − ω_Q²); time-ordered 2ω_Q/(ω² − ω_Q² + i0⁺) (sans-serif D, like 𝖦) ⚑ | eV⁻¹ | D.11 |
| F (loop count) | number of closed fermion loops in a diagram (D.11, 4.8; local) ⚑ | 1 | D.11 |
Clash notes: h vs Hubble h; ℓ(w) vs cubic ℓ; A (affinity) vs mass number A; ν (phonon branch) vs Lindhard ν (D.8 local); D_k vs D^dyn/𝒟_f; I (ionization) vs nucleus index I; 𝓜 vs 𝓜¹;
λ_γγ′ vs exciton λ; F loops vs form factors F_…; φ_Q (\varphi, boson field) vs DM field φ and φ_ext/φ_loc; K_s vs K̄.
GLOSSARY:
| Hartree–Fock equations | stationarity of the energy of one Slater determinant: h_HF ψ = Eψ with Hartree and nonlocal Fock terms | D.4 |
| Koopmans' theorem | with frozen orbitals, −E_a and E_r are the HF removal and addition energies | D.4 |
| exchange hole | deficit of same-spin electrons around an electron, −\|ϱ(x,x′)\|²/ϱ(x,x), integrating to one | D.4 |
| Hohenberg–Kohn theorems | the GS density fixes U_1 (hence H); E_0 = min_𝓃 [𝓕[𝓃] + ∫U_1𝓃] | D.5 |
| constrained search | 𝓕[𝓃] = min over states with density 𝓃 of ⟨H_kin + H_ee⟩ (Levy) | D.5 |
| Kohn–Sham equations | independent electrons in V_KS = U_1 + v_H + v_xc reproducing the interacting GS density | D.5 |
| Janak's theorem | ∂E/∂n_γ = E_γ for fractional occupations | D.5 |
| derivative discontinuity | jump Δ_xc of δE_xc/δ𝓃 at integer N; E_g = E_g^KS + Δ_xc | D.5 |
| local-density approximation | E_xc = ∫𝓃 ε_xc(𝓃) with the uniform-gas ε_xc | D.5 |
| Lindhard function | T = 0 independent-electron density response of the gas, eq:D.8-Rz | D.8 |
| Mermin dielectric function | relaxation-time RPA that relaxes to local equilibrium and conserves particle number | D.9 |
| Wick's theorem | free averages of operator strings = sum over pairings of products of contractions, with permutation sign | D.11 |
| linked-cluster theorem | vacuum diagrams cancel the denominator; 𝖦 = sum of connected diagrams | D.11 |
| Feynman rules | value of a diagram: (−1)^n(−1)^F Π𝖦₀ Π(v_C/V), TΣ per internal frequency (Matsubara) | D.11 |
CONCEPTS: "Hartree–Fock and Koopmans" | D.4 | `eq:D.4-HF`, `eq:D.4-koopmans`. "HK/KS" | D.5 | `eq:D.5-levy`, `eq:D.5-KS`,
`eq:D.5-gap`. "Lindhard function" | D.8 | `eq:D.8-Rz`. "Mermin function" | D.9 | `eq:D.9-R`. "Wick and Feynman rules" | D.11 |
`eq:D.11-wick`, `eq:D.11-boson`.
CLAIMS:
- HF equations from the variational principle; Koopmans with frozen orbitals; relaxation → 0 for Bloch states | D.4 | derived | Fock 1930; Koopmans 1934.
- Σ_x(k) = −(e²k_F/2π²)F_L(k/k_F); E_x/N = −0.916/r_s Ry; Si: −6.22 eV, widening 8.29 eV | D.4 | derived; computed (check_D_a.py).
- HK1, HK2 (constrained search) | D.5 | derived | Hohenberg–Kohn 1964; Levy 1979.
- KS equations and total energy; Janak | D.5 | derived | Kohn–Sham 1965; Janak 1978.
- HOMO = −I; E_g = E_g^KS + Δ_xc | D.5 | cited (piecewise linearity) | PPLB 1982; Perdew–Levy 1983; Sham–Schlüter 1983.
- Si LDA gap error mostly Δ_xc | D.5 | cited | Godby–Schlüter–Sham 1986 (to verify).
- v_x^LDA = Σ_x(k_F) = (2/3) Slater | D.5 | derived | Kohn–Sham 1965; Slater 1951.
- Lindhard closed form, Re/Im, limits, f-sum | D.8 | derived; checked numerically | Lindhard 1954; G&V Chap. 4.
- Mermin function; continuity; static, Drude, perfect-screening limits; f-sum for both | D.9 | derived; checked numerically | Mermin 1970.
- 𝖦 expansion in imaginary time (exact); T = 0 via Gell-Mann–Low | D.11 | derived / cited theorem | Gell-Mann–Low 1951.
- Wick's theorem (thermal and T = 0) | D.11 | derived | Wick 1950; Gaudin 1960.
- Linked cluster; Feynman rules incl. signs and factors; boson rule and 𝖣₀ | D.11 | derived | Fetter–Walecka Chaps. 3, 7; B&F.
INDEX: Hartree–Fock equations; Fock operator; Hartree potential; exchange hole; self-interaction; Koopmans' theorem; frozen orbitals;
orbital relaxation; exchange energy (electron gas); Hartree–Fock band width; Hohenberg–Kohn theorems; universal functional;
constrained search; Kohn–Sham equations; Kohn–Sham potential; v-representability; Janak's theorem; ionization energy; electron
affinity; derivative discontinuity; band-gap problem (DFT); local-density approximation; Slater exchange; Lindhard function;
Thomas–Fermi screening (from Lindhard); particle–hole continuum (Lindhard); Mermin dielectric function; relaxation-time
approximation; local equilibrium; continuity equation; Drude model; perfect screening; interaction picture (imaginary time);
Gell-Mann–Low theorem; Wick's theorem; contraction; linked-cluster theorem; vacuum diagram; Feynman rules; fermion loop;
boson propagator; phonon-mediated attraction.
