# R14 brief WP8-U-TOP: top-up of the WP8-U property table

## Target
WP8-U (/home/user/dmdd-solid/returns/R13/WP8-U.md, /home/user/dmdd-solid/returns/R13/WP8-U-table.csv) ran before WP8-F existed. Bring the table up to the property list of /home/user/dmdd-solid/returns/R13/WP8-F.md §5 and close the data gaps. Do NOT edit the R13 files; write a supplement.

## Required
1. Diff WP8-F §5 (properties, units, needed accuracy) against the CSV columns/properties; fill every missing property for the 10 SURVIVOR and 30 SURVIVOR-COND materials, or mark GAP with the reason.
2. **ε_eh and F_eh (pair-creation energy, Fano factor):** WP8-U has them as GAP outside Si, Ge, diamond, SiC. Search the radiation-detector and X-ray/γ spectroscopy literature (not only DM papers): GaAs, CdTe/CZT, SiC, GaN, AlN, diamond, Al₂O₃, LiF, TlBr, HgI₂, etc. Give measured ε_eh(T), F_eh, the method and temperature; note scintillators (CaWO₄, Li₂MoO₄, NaI, CsI) where ε_eh is not directly measured.
3. Resolve the two source disagreements WP8-U found: 2008.08560 Table I n_e (factor 2 for C, Si, SiC) and 1910.10716 Table I c_LA (GaN, AlN, ZnO, quartz, NaCl); state which values WP8-F should use and why.
4. WP8-R G-R5: Al and Ir elastic moduli with provenance; Kaplan 1979 (phonon transmission) if accessible.
5. Thin entries: magnets (YIG etc.: spin density, magnon gap, ω_max^mag) and many-atom oxides (Li₂MoO₄, CaWO₄: ε_∞, ε₀, ω_LO/TO, Z*).

Return files: /home/user/dmdd-solid/returns/R14/WP8-U-top.md (≤ 400 lines) and /home/user/dmdd-solid/returns/R14/WP8-U-table-v2.csv (the full R13 table plus your rows, same columns, with a 'supersedes' note where a value changes).

## Rules
- Theory and data compilation only. Run no new first-principles numerics such as DFT, DFPT, MD or Monte Carlo. Closed-form estimates and sympy/numpy checks of ≤ 2 min are fine. Put the checks in /home/user/dmdd-solid/code/<ID>/checks.py, and they must pass.
- Every material property needs provenance: a database entry ID (OPTIMADE/JARVIS-DFT/COD/NIST) or a full-text quote with page/table. Tag each value [FT] (full text), [DB] (database), [E] (estimate) or [UNVERIFIED].
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-<ID>/. Verify every arXiv ID against the API. Delete the PDFs at the end. Use INSPIRE for citation walks (OpenAlex is rate-limited).
- Do not use the Materials Project REST API (no key). Public OPTIMADE endpoints, including MP's, and JARVIS downloads are fine.
- Follow /home/user/dmdd-solid/CONVENTIONS.md (incl. "R13 amendments") and /home/user/dmdd-solid/NOTATION.md (incl. "Rows added WP7-E"). Introduce new symbols only in the closing 'Symbols' section.
- Write only your return file(s) and your code/<ID>/ folder. Do not commit. Do not edit any other file.
- End with three sections: 'Symbols introduced/used', 'Interface flags' and 'Proposed LIMITS rows'.
- Your final message is a summary of ≤ 15 lines.
