# SEAM: E.12 Phonon and charge transport Monte Carlo

Length (wc): E-12.tex ≈ 3,200 words (budget 3,500). No App. D file. Lint 0 blocking (LONG-SENT hits are equations/tables merged).
Build clean in the wrapper. Sources: sources/E-d/{1109.1193, 2302.05998, 2408.04732, 1805.02495}.txt.

## The reader now knows
- Linear Boltzmann equation sampled by MC (eq:E.12-boltzmann); 𝔗: lowest-order golden-rule rates (isotope 2nd-order Born; anharmonic
  lowest cubic order, squared in the rate; Luke and intervalley one-phonon emission n_g = 2, n_B = 0); incoherence check Γ/ω ~ 10⁻³ at 15 THz.
- Isotope rate Γ_iso = B_iso(E_ath/h)⁴, B_iso = 4π³g_mdΩ_at⟨c⁻³⟩, ⟨c⁻³⟩ = (1/3)Σ_s c_s⁻³ = 1/2.13×10¹¹ s³ m⁻³ (eq:E.12-iso), Si worked: 2.35×10⁻⁴² s³ (tab 2.33, code 2.43);
  anharmonic Γ_anh = A_anh(E_ath/h)⁵ (eq:E.12-anh), A_anh = 0.741–1.15 ×10⁻⁵⁵ s⁴; ratio (E_ath/h)/33 THz; rates table tab:E-phrates.
- Branch populations 55:35:10; Christoffel equation and focusing; surfaces; AMM/DMM; 0.3–0.55 is an absorption probability (→ 20.3).
- Lumped Kaplan film: escape exp(−4d_f/λ_f), 3Δ_BCS collection; Y_qp sampled.
- Luke emission rate (eq:E.12-luke), k_s, l_0; Herring–Vogt; intervalley rates parametrized; trapping and impurity impact ionization; Hecht check;
  dt = τ/2 energy conservation; 5×10⁴ Luke phonons per pair at 100 V (2 meV code assumption).
- Collection kernels and Ramo weighting potentials; binomial errors; common random numbers.
- Closure checks (energy, charge, rate slopes, time step) and external benchmarks; cost (CPU day per few-keV event; ~hour with down-sampling;
  10⁸–10⁹ steps derived); down-sampling breaks fluctuations (no F_meas from weighted runs). Pitfalls; tab:E-transport-si.

## Symbols introduced (with defining equation)
- B_iso, g_md, Ω_at, ⟨c⁻³⟩ (eq:E.12-iso); Γ_anh, A_anh (eq:E.12-anh); Γ_L, k_s, l_0 (eq:E.12-luke); λ_f film mean free path; m_c conductivity mass;
  φ_s weighting potential; N_l launched phonons; 𝓔 (vect{\mathcal{E}}) applied field — check against ℰ (5.5, macroscopic field); f down-sampling fraction (local).
- Used: Γ_iso (11.6), E_ath (phonon energy, NOTATION 20.2), c_LA, ρ_T, D^n, m*_∥, m*_⊥, Δ_BCS, d_f, t̄_12, P_abs, Y_qp, V_bias, F_meas, e_κν (written ê here for elastic-wave polarization).
## Terms introduced
- collection kernel (computational definition); closure checks; down-sampling; self-scattering (also E.13); Herring–Vogt transformation; weighting potential.
## Threads: none.
## Promises made to later sections
- 20.1 Hecht/Ramo, 20.3 reciprocity and absorption reading, 20.4 Kaplan cascade, 20.5 kernels/contrasts. No pointer yet to App. E.14–E.27.
## Proposed ledger rows
NOTATION: B_iso, A_anh | isotope and anharmonic rate constants | s³; s⁴ | E.12 · Γ_anh | anharmonic decay rate | s⁻¹ | E.12 · g_md | isotope mass-variance
coefficient ⟨(M − M̄)²⟩/M̄² | 1 | E.12 · Ω_at | volume per atom | Å³ | E.12 · Γ_L, k_s, l_0 | Luke emission rate, sound-speed momentum, scattering length | s⁻¹; eV; m | E.12 ·
m_c | conductivity mass 3/m_c = 1/m*_∥ + 2/m*_⊥ | m_e | E.12 · φ_s | Ramo weighting potential of electrode s | 1 | E.12 (20.1 may define first).
Convention question for the editor: the anharmonic order of three-phonon decay on 𝔗 (n_A = 1 vertex / 2 in the rate) — text names the physics only.
CLAIMS: rate constants [cited]; B_iso arithmetic, tab:E-phrates, Luke count, step count [derived]. INDEX: phonon transport Monte Carlo; isotope scattering; anharmonic decay; Luke phonons; collection kernel; G4CMP.
