# R13 brief WP8-F: figures of merit per interaction channel

## Target
For every channel of the atlas (excitation × DM-interaction cell; see /home/user/dmdd-solid/literature/CATALOG-A.md, /home/user/dmdd-solid/LIMITS.md and /home/user/dmdd-solid/FRAMEWORK.md), derive the figures of merit (FOMs) that set the material choice for maximal sensitivity. Derive them from the refereed framework, the master formula Γ = tr[𝔇ᵀS], in the limits catalogued in LIMITS.md.

## Required
1. **Grouping.** Group the channels into FOM classes that share the same controlling material functional, e.g.:
   - ER scattering via the loss function Im[−1/ε];
   - absorption via Re σ, ε₂ and ε_bg screening;
   - single and multiphonon NR via the dynamic structure factor;
   - phonon polaritons and dark-photon mixing via Born charges and LO–TO;
   - magnons via spin density and anisotropy gap;
   - PAER and Migdal;
   - TLS and defects.
2. **For each class:**
   - the rate per target mass at fixed coupling, written as (material functional) × (kinematic factor);
   - the threshold/reach edge set by the material (gap, ω_max, sound speed, ...);
   - the screening suppression;
   - the background-relevant quantities (radiopurity-limited elements, cosmogenic activation, LEE proxies via WP7-E stored energy);
   - for each FOM, its scaling with elementary inputs (Z, A, ρ, E_g, ω_LO, Z*, v_s, n_e, ...) and the mass range where it dominates.
3. **Projected reach.** Distinguish the 'rate' FOMs from the 'reach' FOMs; which one governs depends on the exposure and background regime. Give a single scalar FOM per channel for a background-free and for a background-limited experiment.
4. **Uncertainty.** State which FOMs inherit theory uncertainty from the WP6 nuisance types and from UNRESOLVED LIMITS rows.
5. **Interface to WP8-U.** Output the list of material properties that WP8-U must tabulate, with units and the needed accuracy.

## Read
/home/user/dmdd-solid/STATEMENT.md, /home/user/dmdd-solid/FRAMEWORK.md, /home/user/dmdd-solid/LIMITS.md, /home/user/dmdd-solid/literature/CATALOG-A.md, /home/user/dmdd-solid/returns/R8/WP0-v3.md through WP6-v3.md as needed, /home/user/dmdd-solid/returns/R12/*.md (WP7), /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md.

Return file: /home/user/dmdd-solid/returns/R13/WP8-F.md (≤ 600 lines).

## Rules
- Theory and data compilation only. Run no new first-principles numerics such as DFT, DFPT or Monte Carlo. Closed-form estimates and sympy/numpy checks of ≤ 2 min are fine. Put the checks in /home/user/dmdd-solid/code/<ID>/checks.py, and they must pass.
- Every material property needs provenance: a database entry ID (OPTIMADE/JARVIS-DFT/COD/NIST) or a full-text quote with page/table. Tag each value [FT] (full text), [DB] (database), [E] (estimate) or [UNVERIFIED].
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-<ID>/. Verify every arXiv ID against the API. Delete the PDFs at the end. Use INSPIRE for citation walks (OpenAlex is rate-limited).
- Do not use the Materials Project REST API (no key). Public OPTIMADE endpoints, including MP's, and JARVIS downloads are fine.
- Follow /home/user/dmdd-solid/CONVENTIONS.md and /home/user/dmdd-solid/NOTATION.md. Introduce new symbols only in the closing 'Symbols' section.
- Write only your return file and your code/ folder. Do not commit.
- End with three sections: 'Symbols introduced/used', 'Interface flags' and 'Proposed LIMITS rows'.
- Your final message is a summary of ≤ 15 lines.
