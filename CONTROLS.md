# Controls (every derivation and computation must pass these)

- C1 **Optical limit.** For q → 0 at fixed ω, with screening removed, ε₂^{PA}(q,ω) must reduce to the
  standard second-order phonon-assisted optical absorption formula: Hall–Bardeen–Blatt / Elliott theory;
  in first-principles form, Noffsinger et al. PRL 108, 167402 (2012), arXiv 1202.3454; Zacharias &
  Giustino. Check every factor, not only the structure.
- C2 **g → 0.** The PAER amplitude vanishes identically.
- C3 **First-order open.** Where the zero-phonon channel is open, the one-phonon sideband is O(g²) relative
  to it (an order-of-magnitude statement, with the size of g stated).
- C4 **Sum rules.** The total f-sum rule ∫ω ε₂(q,ω)dω = (π/2)ω_p² is unchanged at O(g²): the sideband's
  first-moment excess is compensated by the Fan + vertex non-phonon cuts (as a sum); "Debye–Waller" means only the Franck–Condon e^{−2W} factor. State whether the
  formula alone satisfies it. ELF upper bounds (2110.01587, 2501.18261, 2608.05282) are not exceeded.
- C5 **Kinematics.** At T = 0 the free-pair PAER threshold at fixed q is ≈ E_g + ω_{Q*ν}(q) − ½(m_c+m_h)\|∇ω\|²
  (infimum over q: E_g, outside the window); exciton replicas start at E_x + ω_ν(Q*), which can lie below E_g (WP3-v3 §M3, C5; WP6-v3 (3.1′)); the "no response below E_g" statement holds for the continuum only, and the total floor is 0.329 MeV (Si) / 0.211 MeV (Ge) (WP6-v3 IF6-18). At T > 0 the absorption branch
  starts at E_g − ω_{Qν}, weighted by n_{Qν}.
- C6 **Adiabatic equivalence.** The sum-over-states amplitude equals the finite-difference derivative of
  the frozen-phonon transition density, up to O(ω_{Qν}/ΔE) terms. Check numerically on one system.
- C7 **Soft-acoustic limit** [WP0-v3 (4.9) = WP3-v3 (M.15); REFEREED R7, STANDS]. The legacy statement follows. Off shell at fixed (k,q), along Q = ηQ̂, η → 0: M → iℓ ρ_cv ê·[q + (D^cQ̂ ∓ cP_c)/(Q̂·v_c ± c) − (D^vQ̂ ∓ cP_v)/(Q̂·v_v ± c)], with intraband slope Ξ^n = D^n + v_n⊗P_n. C7a: acoustic sum rule + completeness at Q = 0. C7b: intraband slope against frozen strain. C7c: full limit. C7d: → 0 as q → 0. C7e: a synthetic g = [A,H] branch must reproduce iℓê·(q − ΔP)ρ_cv. Reproducing the R1 forms with the physical g is a BUG.
- C8 **Decoy** [book 13.9 update 2026-11-06: GaAs PAER-leading band 0.43 → 0.52–0.56 MeV (E_L(0) = 1.815 eV; L floor 0.517, edge ≤ 0.560), no calculation of the control yet; earlier: window per WP3-v3 §M9 C8: PAER-leading GaAs only at m_χ ≈ 0.4–0.9 MeV, full q integral]. A direct-gap crystal (e.g. GaAs at its Γ edge) must show PAER as a small correction, never
  the leading channel above E_dir.
