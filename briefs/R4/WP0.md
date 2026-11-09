# Round R4, brief WP0: architecture of the Unified Response Framework

## Target
Write the foundation that every later work package (WP1–WP6, FRAMEWORK.md) will build on. Items:
1. **Hamiltonian and degrees of freedom.** The coupled electron–ion(–spin) Hamiltonian, including the
   options for spin–orbit, relativistic cores and magnetic order.
2. **DM interaction basis.** A complete NR operator basis for DM interactions with the target, mapped to
   target operators O_a(q):
   - electron density, nuclear density per species κ (with nuclear form factor), electron and nuclear spin
     densities, paramagnetic and diamagnetic currents, velocity-dependent operators;
   - absorption couplings: dark photon via the current, ALP via g_aee spin and g_aγγ with an external field,
     scalar couplings;
   - inelastic and exothermic DM (energy offset Δ).
3. **Master rate formula.**
   - The rate is written as a contraction of DM-side tensors with the finite-T response matrix
     S_{ab}(q,ω) = (2π/V) Σ_{if} p_i ⟨i|O_a(q)†|f⟩⟨f|O_b(q)|i⟩ δ(ω − E_f + E_i), for scattering.
   - Give the analogous absorption formula (q ≈ m_DM v, ω = m_DM) through the retarded response / self-energy.
   - Fix the conventions so that they agree with D1/D2 (NOTATION.md) for the density channel.
4. **Exact relations at the master level.**
   - Fluctuation–dissipation, detailed balance, Kramers–Kronig.
   - Positivity of S as a matrix.
   - Sum rules: f-sum for the electron density and per nuclear species, the mixed electron–nuclear sum
     rules, and the Ward identities for rigid translation and the acoustic sum rule.
5. **Screening, from first principles.**
   - Distinguish the proper and improper (Coulomb-reducible) response, and how this depends on whether the
     DM couples to the electron density only, the total charge (dark photon), or nucleon number.
   - Derive the general screened formula: the matrix of ε⁻¹ in the e/N/charge basis, including local fields.
   - Show how the ELF form emerges.
   - Consistency check: the corrected screening result of the M1 work must be a special case. X2 is now
     running; state what form your architecture predicts.
6. **The expansion hierarchy.** Identify the small parameters and define each expansion so that each
   LIMITS.md entry is a specific truncation:
   - the BO expansion in κ_BO = (m_e/M)^{1/4};
   - the electron–phonon order;
   - the harmonic expansion (anharmonic parameter);
   - the XC kernel ladder;
   - T/ω_ph and T/E_g;
   - the kinematic regime parameters q²/(2Mω_ph) and q·u_zp (Debye–Waller);
   - sudden versus adiabatic for Migdal: the collision time compared with the electronic time;
   - the dipole parameter q·r.

   Give a "decomposition theorem" that splits S_ee, S_NN and S_eN at each order into the pure electronic
   (clamped), the pure lattice, and the mixed (non-adiabatic / phonon-assisted / Migdal) parts, with no
   double counting. State it as a theorem with hypotheses, and prove it or mark it CONJECTURED.
7. **From response to signal.** The interface from the response to WP5 (energy partition): which final-state
   information (not only ω) the response must hand over to a cascade or transport calculation. Define the
   "final-state-resolved response" S_{ab}(q,ω; Λ), with Λ the label of the final-state class (e–h pair with
   energies ε_e and ε_h, phonon content, defect).
8. **Uncertainty structure.** The interface to WP6: how each truncation supplies an error estimate (the size
   of the next term) as a nuisance parameter.
9. **Derive L0 and L17 fully.** For every other LIMITS.md entry, give a one-line pointer to the truncation
   that should produce it. Confirm or correct the expected chains in LIMITS.md.
10. **NOTATION v2.** A proposed symbol table, extending NOTATION.md without collisions.

## Read
- /home/user/dmdd-solid/STATEMENT.md, /home/user/dmdd-solid/FRAMEWORK.md, /home/user/dmdd-solid/LIMITS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/CONTROLS.md, /home/user/dmdd-solid/state/SOTA.md
- /home/user/dmdd-solid/returns/R1/D1.md and D2.md (only for conventions and the PAER structure)
- /home/user/dmdd-solid/surveys/dm-solid-state-processes/README.md
- /home/user/dmdd-solid/surveys/dm-solid-state-scattering.md

## Literature
You may use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py:
- arxiv, and fetch <id> -o /home/user/dmdd-solid/literature/papers-wp0/ to check exact forms, e.g. of the NR-EFT operator basis
  (Fitzpatrick et al. 1203.3542; Catena et al. 2105.02233; Trickle et al. 2009.13534) and the sum-rule papers;
- verify every cited ID against the arXiv API;
- delete PDFs at the end.

## Rules
- Theory only. Run no numerical simulations; sympy checks of ≤ 2 min are fine.
- Mark each step DERIVED (with hypotheses), ESTIMATED or CONJECTURED.
- Be concrete: equations, not prose. The returns of WP1–WP6 will cite your equation numbers.
- Write the return to /home/user/dmdd-solid/returns/R4/WP0.md (≤ 600 lines) and scripts to /home/user/dmdd-solid/code/WP0/.
- Your final message is a summary of ≤ 15 lines.
