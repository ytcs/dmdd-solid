# Round R1b, catalog brief CAT-A: the complete space of DM–solid-state processes

## Target
A catalog, as complete as you can make it, of every channel by which a dark-matter particle (or a
bosonic DM field) deposits energy or momentum in a solid-state target and produces a detectable
excitation.

## Organisation
Organise by (i) the DM coupling (electron, nucleon/nucleus, photon via kinetic mixing / dark photon,
spin: electron or nuclear, axion couplings g_aee / g_aγγ / g_aNN, scalar couplings) × (ii) the final-state
excitation:
- single electron–hole pairs (band-to-band, core, valence);
- excitons (Wannier, Frenkel, dark/indirect excitons);
- plasmons;
- single phonons (acoustic, optical, polar LO);
- multiphonons;
- phonon polaritons;
- magnons and spin waves;
- superconducting quasiparticles (Cooper-pair breaking);
- quasiparticles in Dirac/Weyl semimetals and narrow-gap materials;
- dopant and defect ionization (shallow donors and acceptors, colour centres such as NV and SiV);
- defect creation and crystal damage (Frenkel pairs, displacement threshold, tracks);
- molecular / organic-crystal excitations (vibronic, scintillation);
- nuclear recoil in the free / impulse regime;
- the Migdal effect (in isolated atoms and in crystals);
- nuclear-recoil bremsstrahlung;
- photon emission / scintillation and Cherenkov-like processes;
- heat / thermal (calorimetric) channels;
- quantum-sensor channels (qubits, TES, SNSPD, phonon-polariton cavities);
- spin-dependent and chiral responses;
- absorption processes (bosonic DM absorbed on electrons, phonons or magnons, including phonon-assisted
  absorption);
- inelastic or exothermic DM;
- multi-step and composite processes (phonon-assisted electron recoil, Migdal plus phonons,
  plasmon-mediated, exciton-mediated);
- anything else you find.

## For each process (one row plus a short paragraph)
- DM mass range and kinematic regime;
- the relevant energy-deposition scale and threshold;
- the theory state of the art: formalism (e.g. ELF/dielectric, EFT of collective excitations, DFT, DFPT,
  many-body perturbation theory), the leading papers (arXiv IDs), and the public codes (QEdark, QCDark,
  EXCEED-DM, DarkELF, PhonoDark, …);
- status: computed from first principles / modelled / proposed only / not computed;
- experiments that use it.

## Rules
- Use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py for literature: arxiv (2–4 term queries), fetch <id> -o /home/user/dmdd-solid/literature/papers for full text when
  a claim needs it, works. INSPIRE-HEP API (https://inspirehep.net/api/literature?q=...) is allowed for
  citation walks and reviews.
- Start from reviews (Kahn & Lin 2108.03239; Mitridate–Trickle–Zhang–Zurek 2203.07492; Essig et al.
  Snowmass; Cooley et al. Snowmass) and walk forward to 2026.
- Every arXiv ID you cite must be verified (title and authors) against the arXiv API. No invented IDs.
- Do not read campaign/paer/returns/ or other briefs. You may read
  /home/user/dmdd-solid/surveys/dm-solid-state-scattering.md for orientation.
- Write /home/user/dmdd-solid/literature/CATALOG-A.md (≤ 500 lines). Delete the PDFs at the end.
- Your final message is a summary of ≤ 15 lines.
