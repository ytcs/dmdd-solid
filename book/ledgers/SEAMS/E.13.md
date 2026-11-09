# SEAM: E.13 Hot-carrier cascades from first principles

Length (wc): E-13.tex ≈ 3,000 words (budget 3,500). No App. D file. Lint 0 blocking. Build clean in the wrapper (one 11 pt overfull line,
likely from unresolved \cref placeholders). Sources: sources/E-d/{0812.2923, 2004.10709, 2004.11499}.txt.

## The reader now knows
- ε_eh, F_eh as moments of P_casc(N_eh|Λ) (eq:E.13-moments); the three ingredients; 𝔗: W^scr at 𝒳 = RPA on QP energies, phonon rate n_g = 2,
  n_B = 0, incoherent sequence (fails near threshold; ħΓ = 0.066 eV at 10¹⁴ s⁻¹).
- QP bands: QSGW Si gap 1.23 eV (no SOC), scaled to experiment within 0.2 eV; scissor caveat; band counts 8/32/90 below 20/50/100 eV (free-electron).
- ii kernel: Γ_ii = 2z_qp (≈0.8, Kotani 2010 Sect. II)|ImΣ|, ImΣ from ImW^scr (eq:E.13-imsigma); plasmon emission included (no separate channel); Kane form, factor 0.5–1, omitting exchange multiplies the rate by ≥ 0.75.
- e–ph kernel (eq:E.13-gph); Wannier window problem at high energy; ~60 meV optical/intervalley losses.
- Full-band MC with self-scattering; holes (12 eV band width); seeding (18.1, 18.3).
- Single-parameter (Alig–Bloom / Ramanathan–Kurinsky) model eq:E.13-ab: ionization probability 0.05/0.36/0.77/0.88 at 3/5/8/10 eV; fits give
  3.71 eV, 0.115 at 123 K vs measured 3.749 ± 0.001 eV, 0.119 ± 0.002.
- Convergence: k grid (1728 points, factor 2 below 10¹⁰ s⁻¹); N_casc ≈ 7×10³ for δF = 0.002 via √(2/N); cost: N_G ≈ 260, 6 GB W^scr, 3×10⁹ kernel terms.
- Pitfalls (gap and T, double counting, threshold noise, exchange/z_qp, holes, model agreement ≠ validation); tab:E-cascade-si.

## Symbols introduced
- E_0 seed energy; Γ_ii(nk), Γ_ph(nk), Γ_tot, Γ_max; Ω_BZ zone volume; A_AB (Alig–Bloom constant; 5.2 in the source units, quoted as eV²; tuned to ε_eh, validated by hot-electron injection to 5 eV); ω_0 single phonon energy of the model (clash: ω₀ of the
  Klein relation k₂; r, ω₀ row — same physical meaning, check); k_E, N_G, N_k, N_b, N_casc.
- Used: ε_eh, F_eh, P_casc(N_eh|Λ), θ_ii, W^scr, Σ, z_qp, GF (sans G), g_mnν, n_Qν, ω_Qν, ε_nk, ψ_nk, Ω.
## Terms introduced
- impact-ionization kernel; full-band cascade Monte Carlo; single-parameter (Alig–Bloom) cascade model.
## Threads: none.
## Promises
- 18.2 defines the moments, 18.3 the seed, 18.4 compares models (I did not quote 18.4's own 0.114; I quote the RK asymptote 0.115). E.24 not pointed to (label unsettled).
## Proposed ledger rows
NOTATION: Γ_ii, Γ_ph | impact-ionization and phonon rates of a carrier state | s⁻¹ | E.13 · A_AB | Alig–Bloom phonon/ionization constant | source units (quoted eV²) | E.13 · E_0 | seed energy of a cascade | eV | E.13 ·
N_casc | number of simulated cascades | 1 | E.13 · Ω_BZ | Brillouin-zone volume | Å⁻³ | E.13.
CLAIMS: Kotani Eqs. (1)–(2), (5), Table I, Fig. 2 [cited]; RK Eqs. (8), (10)–(13) [cited]; Rodrigues values [cited]; probabilities, moments at 123 K, band/memory/N_casc estimates [derived].
INDEX: impact ionization (GW); hot-carrier cascade; Fano factor (computation); pair creation energy (computation); self-scattering.
