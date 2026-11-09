# STATEMENT v2: a complete response framework for dark matter in solid-state targets

Fixed 2026-10-31 by the user's directive: "Point the campaign towards a complete response framework that
covers and fixes all the gaps and deficiencies in the current literature. Connect widely cited formulas as
limit or approximation or special case within our completed framework." This supersedes v1, archived at
state/STATEMENT-v1-PAER.md. v1 becomes milestone M1, phonon-assisted electron recoil (PAER).

Numerics remain on hold (user, 2026-10-31). This phase delivers theory, plus specifications of every
computation the theory requires.

**Deliverable (user, 2026-11-01):** a textbook deriving all the theory and formulae. "Btw the main deliverable is the textbook that derive all the theory and formulae, concrete numerical results that relies on heavy computation is not required as long as the quantity to compute is explained and derived clearly in the theory. The compute work can happen later unless the numerical value is important for physical reasons and/or critical to the framing or presentation of the book's narrative".

## Headline (H): the Unified Response Framework (URF)
One first-principles framework, built on the coupled electron–ion(–spin) many-body system, that:
1. **Master formula.** Writes every DM–target rate (scattering, absorption, inelastic/exothermic) for every
   non-relativistic coupling class through one object: the matrix of finite-temperature dynamic response
   functions S_{OO′}(q,ω) of the full Hamiltonian H = T_e + T_N + V_ee + V_eN + V_NN (+ spin terms).
   - The operator set O covers the electron density, nuclear densities per species, spin densities,
     currents, and the other NR-EFT target operators.
   - Fluctuation–dissipation, causality, sum rules and in-medium screening must hold exactly at the
     master-formula level.
2. **Controlled expansions.** Organises approximations as explicit expansions with stated small parameters:
   - Born–Oppenheimer / non-adiabatic, in (m_e/M)^{1/4};
   - electron–phonon order;
   - harmonic versus anharmonic;
   - the exchange–correlation kernel ladder (independent particle → RPA → RPA+LFE → TDDFT/BSE);
   - temperature;
   - the kinematic regime (coherent → multiphonon → impulse);
   - the sudden versus adiabatic Migdal regimes.
3. **Measured signal.** Continues past the response to the measured signal, the energy partition: hot-carrier
   cascade and ionization yield, NR heat/defect/charge partition, quasiparticle yield. It is formulated as
   transport seeded by the response's final-state distribution, not by ω alone.
4. **Uncertainty quantification.** Carries theory uncertainty: every approximation level supplies a nuisance
   parameter or error estimate, and the framework specifies how to propagate it into exclusion curves.
5. **Closes the gaps** listed in surveys/dm-solid-state-processes/README.md §4 (G1–G13) and the
   not-computed channels of catalog-processes §12. Each gap is either closed by a derived formula plus a
   computation specification, or stated as an exact remaining gap.
6. **Recovers the literature.** Recovers every widely cited formula in LIMITS.md as a limit, approximation or
   special case. Each entry states the explicit chain of approximations and the conditions of validity, and
   what the framework predicts beyond it (the leading correction).

## Milestones
- **M1. PAER.** The O(g²) phonon-assisted electron response (the v1 target): R1–R3, in progress.
- **M2. Architecture.** The master formula and the expansion hierarchy (WP0).
- **M3. Sector work packages** WP1–WP6 (FRAMEWORK.md), each with its LIMITS.md entries derived.
- **M4. Synthesis.** A framework paper (PRD-length, revtex) plus the M1 letter-length paper.

## What does not count
- Relabelling known formulas without a derivation chain from the master formula.
- A "framework" that only lists codes.
- A limit asserted without its conditions and leading correction.
- Fixing a gap by naming a method without the formula and the computation specification.
- Claims of exactness without proof.
