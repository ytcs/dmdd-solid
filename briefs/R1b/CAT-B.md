# Round R1b, catalog brief CAT-B: what the theory of each DM–solid-state channel does to experimental analysis, and where the theory is deficient

## Target
For DM direct detection in solid-state targets (semiconductors Si/Ge/GaAs/SiC/diamond; sapphire;
superconductors; polar crystals; magnets; Dirac materials; doped semiconductors; quantum sensors),
determine how theoretical modelling choices enter published exclusion and projection plots, and where the
theory is the limiting systematic.

## Required content
1. **The analysis chain.** DM rate → energy deposition → measured signal: ionization yield / e⁻ count,
   phonon calorimetry, quasiparticle readout. Cover the pieces that carry theory:
   - the crystal response (form factor / ELF / structure factor);
   - in-medium screening;
   - the ionization model (pair-creation energy ε_eh, Fano factor, the Ramanathan–Kurinsky yield model, the
     Si impact-ionization model);
   - quenching / Lindhard for nuclear recoils at low energy;
   - Migdal probabilities;
   - astrophysical inputs (SHM parameters, v_esc, daily modulation);
   - detector-response modelling.
   For each, give the published size of its effect on limits (factor at given m_χ) with sources, e.g.
   QEdark vs QCDark vs EXCEED-DM differences, screening factors, and ionization-model spreads.
2. **The low-energy excess.** How unmodelled backgrounds and stress relaxation affect what limits mean, and
   which theory channels have been proposed as explanations (e.g. plasmons, Kurinsky et al. 2002.06937) and
   their status.
3. **Exclusion plots in current use.** SENSEI, DAMIC-M, SuperCDMS (HVeV, CPD), EDELWEISS, CRESST, TESSERACT,
   QROCODILE, CDEX, … For each: which theory/code they use for ER and NR, and the lowest-mass reach claimed.
   Where do theory assumptions dominate the edge of the plot (threshold region, lightest masses)?
4. **Gaps and deficiencies.** Rank by impact on exclusion plots. Each gap must be concrete: what is
   missing, which plots it affects, an estimated size if possible, and a proposed improvement (theory or
   model). Candidates to examine, not to assume:
   - the frozen-lattice / T = 0 approximation;
   - phonon-assisted transitions near threshold;
   - excitonic effects;
   - ionization yield below ~50 eV;
   - an inconsistent treatment of DM–nucleus multiphonon versus Migdal;
   - anharmonicity;
   - anisotropy / daily modulation;
   - spin-dependent responses;
   - many-body effects beyond RPA;
   - core-level / all-electron effects;
   - relativistic bound-state effects (2509.14534);
   - the ER threshold for sub-MeV DM;
   - defect / dopant channels;
   - consistency of the EFT operators in-medium;
   - uncertainty quantification (no theory error bands on exclusion curves).

## Rules
- Use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py for literature: arxiv (2–4 term queries); fetch <id> -o /home/user/dmdd-solid/literature/papers for full text; works.
  The INSPIRE-HEP API is allowed.
- Every arXiv ID must be verified against the arXiv API. No invented IDs.
- Do not read campaign/paer/returns/, other briefs, or literature/CATALOG-A.md. You may read
  /home/user/dmdd-solid/surveys/dm-solid-state-scattering.md.
- Write /home/user/dmdd-solid/literature/CATALOG-B.md (≤ 450 lines). Delete the PDFs at the end.
- Your final message is a summary of ≤ 15 lines.
