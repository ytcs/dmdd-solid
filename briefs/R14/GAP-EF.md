# R14 brief GAP-EF: theory of the pair-creation energy ε_eh and Fano factor F_eh; final-stage capture (WP7-E IF-E9)

## Target
WP5-v4 §6 states that ε_eh and F_eh are computable functionals of the cascade (W1)–(W3), but leaves the leading term of F_eh uncomputed: F_eh = [Var(Σ residuals, with the energy-constraint anti-correlation) + Var(phonon)]/(E_g²n̄) — "whose first term is not computed here". Close this at the theory level and give predictions with error bars for materials without data, validated against measured values.

## Required
1. Derive the residual-anticorrelation term: a controlled semi-analytic reduction of (W3) (e.g. a renewal/branching treatment with energy conservation, of the Klein/Alig–Bloom/van Roosbroeck/Shockley families) giving ε_eh and F_eh in terms of a small set of material inputs (E_g direct/indirect, E_th^{ii}, ω_op/phonon-emission-to-ionisation rate ratio, band-structure/DOS shape parameters). State hypotheses; quantify the truncation error. Recover Klein's ε ≈ 2.8E_g + rω₀ and the measured Si/Ge F as limits (LIMITS rows).
2. Validate against measured (ε_eh, F_eh) for every material where data exist (Si, Ge, diamond, SiC, GaAs, CdTe, GaN, ... from radiation-detector literature, [FT]). Report the residuals; calibrate no more than one parameter, and say which.
3. Predict ε_eh, F_eh with uncertainty for the WP8-U survivors lacking data (/home/user/dmdd-solid/returns/R13/WP8-U.md §0, §4.2); tag [E].
4. WP7-E-v3 IF-E9: shallow-level cascade capture and exciton parameters at the end of the cascade — how they shift ε_eh, F_eh, and N^meas; formulas plus the computation specification (BSE exciton parameters, capture cross-sections).
5. Computation specification for the full ab initio route (band structure + GW/DFT impact-ionisation rates + EPW phonon-emission rates + cascade MC) per material: inputs, grids, cost estimate, expected accuracy vs the semi-analytic model. Do not run it.

## Read
/home/user/dmdd-solid/returns/R13/WP5-v4.md (esp. §1–§3, §6), /home/user/dmdd-solid/returns/R12/WP7-E-v3.md (§1, §2, IF-E9), /home/user/dmdd-solid/returns/R8/WP6-v3.md (θ rows), /home/user/dmdd-solid/returns/R13/WP8-U.md, /home/user/dmdd-solid/LIMITS.md, /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md.

Return file: /home/user/dmdd-solid/returns/R14/GAP-EF.md (≤ 500 lines). ID for code: GAP-EF.

## Rules
- Theory and data compilation only. Run no new first-principles numerics such as DFT, DFPT, MD or Monte Carlo. Closed-form estimates and sympy/numpy checks of ≤ 2 min are fine. Put the checks in /home/user/dmdd-solid/code/<ID>/checks.py, and they must pass.
- Every material property needs provenance: a database entry ID (OPTIMADE/JARVIS-DFT/COD/NIST) or a full-text quote with page/table. Tag each value [FT] (full text), [DB] (database), [E] (estimate) or [UNVERIFIED].
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-<ID>/. Verify every arXiv ID against the API. Delete the PDFs at the end. Use INSPIRE for citation walks (OpenAlex is rate-limited).
- Do not use the Materials Project REST API (no key). Public OPTIMADE endpoints, including MP's, and JARVIS downloads are fine.
- Follow /home/user/dmdd-solid/CONVENTIONS.md (incl. "R13 amendments") and /home/user/dmdd-solid/NOTATION.md (incl. "Rows added WP7-E"). Introduce new symbols only in the closing 'Symbols' section.
- Write only your return file(s) and your code/<ID>/ folder. Do not commit. Do not edit any other file.
- End with three sections: 'Symbols introduced/used', 'Interface flags' and 'Proposed LIMITS rows'.
- Your final message is a summary of ≤ 15 lines.
