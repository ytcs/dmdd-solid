# R13 brief WP8-U: the pickable universe and its property table

## Target
Define and populate the pickable universe of substrate materials for DM-in-solids detectors, and compile their properties with provenance.

## Required
1. **Screening criteria**, applied with explicit pass/fail evidence per material:
   1. survives repeated thermal cycling 300 K ↔ mK: no structural phase transition in 0.01–300 K (or one known to be benign), no cracking or delamination; thermal-expansion anisotropy and hygroscopicity are relevant; cite cryogenic-detector use where it exists;
   2. synthesizable at ≥ 1 g with detector-grade purity; the crystal growth method; commercial availability;
   3. instrumentable: TES/QET, KID, SNSPD, MMC or charge readout demonstrated or plausible on its surface (adhesion, chemical compatibility, film processing temperature).
2. **The candidate pool.** Start broad:
   - the elemental semiconductors and insulators (Si, Ge, diamond);
   - SiC polytypes, GaAs, GaN, AlN, Al2O3, SiO2 (crystal and amorphous), CaWO4, LiF, NaI/CsI, ZnO, BN (h and c);
   - Dirac/narrow-gap materials (ZrTe5, Bi-based, InSb);
   - superconductors (Al, Nb);
   - magnetic insulators (YIG, NiPS3 etc.);
   - polar materials with a large Born charge (e.g. SrTiO3, KTaO3, PbTe);
   - Li/He/H-rich targets for light NR (LiF, Li2MoO4, polyethylene-like, superfluid He as a reference only);
   - anything the literature has proposed (walk proposal papers: 1909.xxxxx 'polar materials', 2002.xxxxx SiC, Dirac materials, magnons, ...).

   Record exclusions with reasons.
3. **The property table** for the survivors. Include at least:
   - ρ, composition, Z, A, isotopic abundances;
   - E_g (direct/indirect, with T), ε_∞, ε₀, Born charges Z*, ω_TO, ω_LO, the maximal phonon energy, sound speeds, Debye T;
   - n_e (valence), plasma frequency, electron effective masses;
   - spin density and magnon gap (magnetic only);
   - the pair-creation energy ε_eh and Fano factor where measured;
   - phonon lifetimes and isotope-scattering rates where known;
   - nuclear spin (for spin-dependent couplings);
   - radiopurity/cosmogenic notes.

   Coordinate with the FOM input list in /home/user/dmdd-solid/returns/R13/WP8-F.md if it exists when you reach this step; otherwise use the list above.
4. Tag each value's provenance as described in Rules. Mark missing values as GAP, not estimate, unless a defensible scaling estimate is given and tagged [E].

## Data sources
- OPTIMADE: https://optimade.materialsproject.org, https://alexandria.icams.rub.de/pbe/ and others listed at providers.optimade.org.
- JARVIS-DFT: the figshare/jarvis-tools downloads.
- NIST, Springer Materials abstracts if open, and cryogenic-detector papers (SuperCDMS, CRESST, EDELWEISS, SPICE/HeRALD, TESSERACT, QROCODILE, DAMIC, SENSEI).

Return files: /home/user/dmdd-solid/returns/R13/WP8-U.md (≤ 600 lines) plus a machine-readable /home/user/dmdd-solid/returns/R13/WP8-U-table.csv.

## Rules
- Theory and data compilation only. Run no new first-principles numerics such as DFT, DFPT or Monte Carlo. Closed-form estimates and sympy/numpy checks of ≤ 2 min are fine. Put the checks in /home/user/dmdd-solid/code/<ID>/checks.py, and they must pass.
- Every material property needs provenance: a database entry ID (OPTIMADE/JARVIS-DFT/COD/NIST) or a full-text quote with page/table. Tag each value [FT] (full text), [DB] (database), [E] (estimate) or [UNVERIFIED].
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-<ID>/. Verify every arXiv ID against the API. Delete the PDFs at the end. Use INSPIRE for citation walks (OpenAlex is rate-limited).
- Do not use the Materials Project REST API (no key). Public OPTIMADE endpoints, including MP's, and JARVIS downloads are fine.
- Follow /home/user/dmdd-solid/CONVENTIONS.md and /home/user/dmdd-solid/NOTATION.md. Introduce new symbols only in the closing 'Symbols' section.
- Write only your return file and your code/ folder. Do not commit.
- End with three sections: 'Symbols introduced/used', 'Interface flags' and 'Proposed LIMITS rows'.
- Your final message is a summary of ≤ 15 lines.
