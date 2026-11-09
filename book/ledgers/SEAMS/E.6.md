# SEAM: E.6 Dielectric response from first principles

Length (detex): appE/E-6.tex 2,932 words (budget 4,500; not padded; equations dropped by detex). Build/lint as E.4.
Sources: sources/E-b/ 2101.08275 (Knapen–Kozaczuk–Lin), cond-mat_9803194 (Albrecht 1998), cond-mat_0109434 (Reining 2002), 2006.09440 (Blase 2020).
Bib added: albrecht1998ab, reining2002excitonic, blase2020bethe (knapen2021dark, adler1962quantum, wiser1963dielectric existed).

## The reader now knows
- R⁰_GG′ (eq:E.6-R0, Adler–Wiser, book notation with ρ_mn); RPA/TDDFT Dyson (eq:E.6-dyson); L at q beyond the zone = −Im ε⁻¹_{G_qG_q}(q_r) (eq:E.6-L).
- 𝔗 placement: only 𝒳 differs (IP, RPA, RPA+LF, TDDFT, BSE); n_B = 0, n_T = 0; rung spread as uncertainty, same numerics for every rung.
- Convergence: k_cut = (2m_eE_cut)^{1/2} (500 eV ↔ 22.6 keV); N_G (N_G² build, N_G³ inversion); bands via f-sum, free-electron count
  (70 bands ↔ 84 eV above valence bottom in Si); k grid as bottleneck; η_b (broadening; renamed from bare η) vs grid; scissor: rigid shift, f-sum raised by Δ∫ε₂ (nonlocal-operator
  sum rule), spurious [(ω−Δ)/ω]² without velocity rescaling; semicore/core.
- LF effects: worsen Si optical spectrum (Albrecht), small in DM rate (KKL); ALDA ≈ RPA+LF for absorption, fine for EELS; long-range kernel
  −α_xc/q², α_xc = 0.2 (Reining).
- Optical conductivity σ₁ for 10.7; large-q loss function for 12.3 (G_q > 7 shortest G at 30 keV; all-electron, semicore).
- BSE Hamiltonian (eq:E.6-Hexc) with K^x, K^d; costs; Albrecht Si: 15 Ry, 2048 k, 4v+2c below 4.5 eV, diagonal ε⁻¹, dim 1.6e4, k-grid bottleneck,
  symmetry-phase sensitivity; bound excitons: Wannier–Mott with E_x^b ~ 10 meV, ε∞ = 11.7 → μ_x 0.10, a_x ≈ 6 nm → >100 points per direction.
- Molecular GW-BSE: Gaussian basis, N⁴ scaling, errors 0.1–0.3 eV, 0.2 eV on the ~200-excitation benchmark; reaction field (Blase 2020).
- WE (we:E-elf-si): KKL silicon ELF settings checked: k_cut, band reach, q resolution 0.49 keV on 8³, f-sum (π/2)ω_p² = 433 eV², ω_p = 16.6 eV.
## Symbols introduced
- K^x, K^d (BSE exchange and direct kernels; avoids W, reserved for W_κ and W^scr); H^exc; α_xc (long-range kernel strength; the source writes α);
  N_G, N_v, N_c, N_k, N_b (counts); k_cut (shared with E.2); E_cut.
## Terms introduced
- transition basis; Tamm–Dancoff (resonant) form; Lanczos–Haydock solver; long-range xc kernel; reaction field; resolution of the identity.
## Threads
- T2 (screening): advanced (how ε_GG′ and L are computed). T7 (theory uncertainty): advanced (rung spread needs common numerics).
## Promises
- 10.2 uses eq:E.6-L; 10.5 finite-q BSE; 12.3 large-q loss function; 16.4 molecular GW-BSE and the environment uncertainty.
## Proposed ledger rows
NOTATION: K^x, K^d | BSE exchange and direct kernels | eV | E.6 · H^exc | BSE Hamiltonian in the transition basis | eV | E.6 · α_xc | strength of
the long-range xc kernel −α_xc/|q+G|² | 1 | E.6 · E_cut | plane-wave energy cutoff | eV | E.6 · GLOSSARY: Tamm–Dancoff approximation; long-range kernel;
Haydock method · CLAIMS: KKL settings [cited]; Albrecht settings [cited]; α_xc = 0.2 [cited]; Blase accuracy [cited]; scissor f-sum shift [derived];
70-band reach [derived estimate] · INDEX: Adler–Wiser; local-field effects; TDDFT kernels; Bethe–Salpeter equation, practice; GW-BSE, molecular.
