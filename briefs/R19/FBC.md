# R19 brief FBC: full-band carrier cascade in silicon (stage 1)

## Why
Book Chapter 18 solves the carrier cascade in an energy-only, random-k model calibrated to measured Si data (A_AB = 5.674 eV³, E_g = 1.160 eV; sections 18.1–18.3). Near threshold (2–20 eV) its predictions depend on physics the model does not compute:
- the electron/hole energy split of the seed (the Ramanathan–Kurinsky α_RK ambiguity, > 0.1 in total-variation distance below ~13 eV);
- momentum and valley memory of the first carriers;
- the competition between impact ionization and phonon emission at mK, where only emission occurs.

The step model overcounts by ~6× above a two-pair threshold at 5 eV. Goal: a full-band cascade for Si, with every rate on one band structure, that removes these assumptions and quantifies how good the energy-only model, Ramanathan–Kurinsky and the step model are.

## Required
1. **Bands.** Full-band empirical-pseudopotential bands of Si, reusing the book's EPM (book/figscripts/ch08 WE 8.7 and book/figscripts/ch18/seeds18_3.py; check the ch10 si_fcrys.py/ch11 elf11_7.py implementations). Calibrate or scissor the gap to the book's 1.160 eV at low T, and state the residual band errors (X/L valley energies, effective masses) against measured values. Use enough bands to cover 20 eV above the VBM for both carriers.
2. **Impact-ionization rate** W_ii(n,k) for electrons and holes, from Fermi's golden rule with a screened Coulomb interaction: direct and exchange terms, energy and crystal-momentum conservation over the full BZ (Umklapp included). Screening: a model ε(q, ω) (Levine–Louie or Penn-type static, or the Lindhard/RPA form the book uses in Ch4/10); state the choice and test its sensitivity. Compare the energy-averaged rate with the Kane/Keldysh threshold forms and with published full-band Si rates (Kotani–van Schilfgaarde; Fischetti–Laux; Nielsen et al. 2023 PRB 108 155203) where readable.
3. **Phonon emission** W_ph(n,k) at T → 0 (emission only): deformation-potential acoustic and optical (intra- and intervalley) couplings with literature Si values (Jacoboni–Reggiani-type parameter sets, as quoted by open sources), on the same bands. State that DFPT couplings are stage 2.
4. **Seeds.**
   - DM seed: the final-state-resolved electron/hole distribution of a DM–electron transition at deposit ω (heavy and light mediator, q-averaged over the halo as in book Ch10). Reuse the book's seed machinery from seeds18_3.py where possible.
   - Photon seed: the q → 0 optical transition at the same ω.
5. **Cascade.** Full-band Monte Carlo (or the 18.1 master equation on the full band grid) to the end of the prompt cascade: all carriers below the ionization threshold, then thermalized by phonon emission. Outputs:
   - P(N | ω) for ω = 2–20 eV, both seeds;
   - the mean pair energy ε and the Fano factor F at high ω (≥ 50 eV, or extrapolated), compared with measured Si values (ε ≈ 3.6–3.8 eV, F ≈ 0.1; quote the book's values from 18.2/18.4);
   - the energy partition (pairs, phonon heat, residual kinetic energy).
6. **Comparison.** Total-variation distance and the two-pair probability against:
   - the book's energy-only cascade (casc18_3.py at A_AB = 5.674, E_g = 1.160);
   - Ramanathan–Kurinsky (α_RK = 1 and ∞);
   - the step model.

   Also: how much of the α_RK spread the computed split removes; the size of valley/momentum memory; the size of mK phonon competition near threshold; and the photon-vs-DM seed difference (book 18.3 quotes ≤ 0.062 in the energy-only model).
7. **Uncertainty.** Vary the screening model, the phonon couplings within literature ranges, the band calibration and MC statistics. Report a band for every headline number. Name what stage 2 must supply (excitonic final states, GW-level rates, DFPT couplings, Ge/GaAs with SOC).

## Compute and rules
- Light-to-moderate: pure Python/numpy (numba allowed), ≤ ~4 CPU-hours total on this 4-core machine. No QE is installed here. Cache the rate tables (.npz) so reruns are cheap.
- Code in /home/user/dmdd-solid/code/FBC/, with a checks.py that must pass (sum rules, detailed-balance or energy-conservation checks, convergence in k-grid and MC samples).
- Literature: /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-FBC/. Verify every arXiv ID; delete PDFs at the end. Attribute unread sources as "quoted by".
- Follow /home/user/dmdd-solid/CONVENTIONS.md and NOTATION.md; read state/CORRECTIONS.md and SOTA.md "Book-phase corrections" before using any value.
- Write /home/user/dmdd-solid/returns/R19/FBC.md (≤ 450 lines). End with "Symbols introduced/used", "Interface flags" (what Ch18 should change) and "Proposed LIMITS rows".
- Do not edit book files or any other file. Do not commit.
- Final message ≤ 15 lines.
