# STATEMENT: phonon-assisted electron recoil (PAER)

Fixed 2026-10-31 by the coordinator, from the user's instruction "fill that gap: derive the theory and
computation formula". The process is gap (c) of surveys/dm-solid-state-scattering.md §4.

## The process
A non-relativistic DM particle χ (mass m_χ, velocity v) couples to **electrons only**, through
H_int = Σ_e V(r_χ − r_e). For a dark-photon mediator the coupling to ions is treated as an extension
(T2c). The DM scatters in a crystalline insulator or semiconductor at temperature T (T → 0 is the
default). It transfers momentum q and energy ω. **One electron is promoted across the gap and one phonon
is emitted, or absorbed at T > 0, in the same event**: the electronic transition is completed by the
phonon. The amplitude is first order in the DM coupling and first order in the electron–phonon coupling.
The rate is the leading term where the zero-phonon (first-order) transition is kinematically closed,
for example below the direct-transition threshold of an indirect-gap crystal.

## Headline deliverable (tier A, theory + formula)
- **T1. Derivation.** Start from the electron–ion Hamiltonian, in the Born–Oppenheimer / harmonic phonon
  basis with linear electron–phonon coupling. Derive:
  - the one-phonon-assisted transition amplitude M_{cvν}(k, q, Q);
  - the rate dR/dω, including the spin and occupation factors, T-dependence (emission and absorption),
    and both time orderings;
  - the treatment of Pauli blocking in intermediate states;
  - the conditions (resonances, double counting with first-order processes and with O(g²)
    renormalisation of the zero-phonon channel) under which the one-phonon sideband is a well-defined,
    separately computable quantity.
- **T2. Response-function form.**
  - (a) Express the result as a phonon-assisted contribution to the dynamic structure factor / Im ε(q, ω).
  - (b) State how in-medium screening enters (ELF = Im ε / |ε|²) and prove that the f-sum rule and the
    published ELF sum-rule upper bounds still hold.
  - (c) Extend to charge-density (dark-photon) coupling, where the DM also couples to ions.
- **T3. Computable formula.** A recipe that existing first-principles codes can evaluate:
  - (a) Wannier/EPW variables: g_{mnν}(k,Q), ω_{Qν}, band energies, density vertex ρ_{mn}(k,q);
  - (b) the adiabatic (DFPT, Herzberg–Teller) form, with its error stated;
  - (c) a special-displacement (supercell) route that reuses existing DM–electron codes, with the
    unfolding of q stated;
  - (d) convergence parameters and cost.
- **T4. Controls** (CONTROLS.md):
  - the optical limit q → 0 reproduces the established phonon-assisted optical absorption theory;
  - g → 0 gives zero;
  - the rate is subleading wherever first-order transitions are open;
  - sum rules hold.

## Tier B: numbers for Si (DEFERRED by user directive 2026-10-31: this phase delivers the specification of these computations, not the numbers)
- **T5.** The kinematic window in Si (and Ge) where PAER is the leading ER channel, with the inputs stated.
- **T5 (cont.).** An estimate of the PAER rate and projected cross-section reach in that window for heavy
  and light mediators: at least at model or data-calibrated level, with an uncertainty band. Include a
  first-principles check of at least one amplitude: a frozen-phonon finite difference compared with the
  sum-over-states, from the same electronic structure.

## Tier H: production
- **T6.** A converged first-principles PAER spectrum and reach for Si (and Ge), from the T3 recipe, with
  convergence tables. This needs remote compute (RULES.md); it is pre-registered, not attempted locally.

## What does not count
- Rescaling first-order rates by a phonon "probability".
- A formula without both time orderings, or with Pauli blocking unhandled.
- Ignoring screening at small q.
- Double counting the first-order channel.
- Reusing an optical spectrum at finite q without bounding the error.
- A reach plot without the threshold and ionization assumptions stated.
- Phonon-mediated Migdal (DM–nucleus coupling) and absorption of bosonic DM. Both are known
  (surveys §4(a), (b)) and serve only as controls or extensions.
