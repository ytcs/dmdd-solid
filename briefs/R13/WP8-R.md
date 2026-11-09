# R13 brief WP8-R: mode-selective phonon collection as an NR/ER discriminant (go/no-go)

## Target
Decide with a cheap, order-of-magnitude screen whether substrate–sensor interfaces with mode-, frequency- and angle-dependent phonon transmission can give useful NR/ER discrimination. Examples are Al-fin/W-TES QETs vs Ti- or Ir-based TES, and the acoustic vs diffuse mismatch.

## Required
1. **The initial phonon populations** for NR vs ER of the same total phonon energy, from WP5-v4/v3 (cascade, NR partition) and WP2:
   - the polarization and frequency mix;
   - the relaxation-carrier (Luke/NTL) phonons for ER;
   - the athermal, high-frequency LO/optical share for NR.
2. **Propagation:**
   - anharmonic down-conversion (Tamura/Maris rates, ∝ ν⁵);
   - isotope scattering (∝ ν⁴);
   - focusing.

   Estimate the time and distance after which the NR and ER populations become indistinguishable, compared with the crystal size (cm) and the collection time for Si and Ge, using literature rates.
3. **Interface transmission:**
   - AMM/DMM transmission per mode and angle for Si/Al, Si/W, Si/Ti, Ge/Al, sapphire/Al, using literature values;
   - the quasiparticle-trapping efficiency vs phonon frequency (above 2Δ_Al).

   Build a mode-ratio observable, e.g. the fast/slow ratio or the two-film ratio.
4. **Discrimination figure of merit:** the separation of the observable between NR and ER in units of its event-by-event spread. The spread includes phonon-number fluctuations, position dependence and caustics.
5. **The verdict:**
   - GO if the separation is ≳ 2σ at an energy where existing ionization-yield or timing discrimination fails (sub-keV, in HV/NTL mode or without charge readout);
   - otherwise NO-GO, with the reason quantified.

   No directionality claims.

## Read
/home/user/dmdd-solid/returns/R8/WP5-v3.md (and /home/user/dmdd-solid/returns/R13/WP5-v4.md if present), /home/user/dmdd-solid/returns/R8/WP2-v3.md, /home/user/dmdd-solid/returns/R12/WP7-E-v3.md, /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md. Literature: Tamura isotope scattering, Maris down-conversion, Kaplan phonon transmission, SuperCDMS/CRESST QET phonon-collection papers, the CDMS phonon-pulse-shape (surface-event) discrimination literature (the closest precedent, which you must compare against), and recent phonon-physics papers (e.g. 2109.xxxx, 2307.xxxx on phonon transport in DM detectors).

Return file: /home/user/dmdd-solid/returns/R13/WP8-R.md (≤ 350 lines).

## Rules
- Theory and data compilation only. Run no new first-principles numerics such as DFT, DFPT or Monte Carlo. Closed-form estimates and sympy/numpy checks of ≤ 2 min are fine. Put the checks in /home/user/dmdd-solid/code/<ID>/checks.py, and they must pass.
- Every material property needs provenance: a database entry ID (OPTIMADE/JARVIS-DFT/COD/NIST) or a full-text quote with page/table. Tag each value [FT] (full text), [DB] (database), [E] (estimate) or [UNVERIFIED].
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-<ID>/. Verify every arXiv ID against the API. Delete the PDFs at the end. Use INSPIRE for citation walks (OpenAlex is rate-limited).
- Do not use the Materials Project REST API (no key). Public OPTIMADE endpoints, including MP's, and JARVIS downloads are fine.
- Follow /home/user/dmdd-solid/CONVENTIONS.md and /home/user/dmdd-solid/NOTATION.md. Introduce new symbols only in the closing 'Symbols' section.
- Write only your return file and your code/ folder. Do not commit.
- End with three sections: 'Symbols introduced/used', 'Interface flags' and 'Proposed LIMITS rows'.
- Your final message is a summary of ≤ 15 lines.
