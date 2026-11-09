# R14 brief WP5-AUD: joint audit of WP5-v4 and WP7-E-v3 (and the yield sites of WP8-R, WP8-F)

## Target
FRAMEWORK requires a joint WP5 + WP7-E audit before WP8 uses the yields. Audit the interface between /home/user/dmdd-solid/returns/R13/WP5-v4.md and /home/user/dmdd-solid/returns/R12/WP7-E-v3.md (with /home/user/dmdd-solid/returns/R12/WP7-T-v2.md Theorem T-1), and every place /home/user/dmdd-solid/returns/R13/WP8-R.md and /home/user/dmdd-solid/returns/R13/WP8-F.md use yields, quenching, F_eh/F_NR, stored energy or LEE proxies.

## Required
1. Cross-package consistency: each A-item as applied in WP5-v4 (its §R13.1–§R13.2) against WP7-E-v3 §5; energy ledger closure (configurational E_st, ΔZPE inside ℋ_ph, CONVENTIONS §13 row 23); no double counting of E_d, E_g, bias work.
2. Rule explicitly on WP5-v4 IF-R13-2: are the LIMITS L38 / WP7-E (E13) calibration weights exact only at r_coll = 1, and what is the correct general-r_coll form? Give the corrected LIMITS L38 text if needed (verify with sympy).
3. Rule on IF-R13-3 (E_st quench protocol) and IF-R13-5 (WP6 nuisance rows); give the exact WP6-v3 row text owed.
4. Spec additions to WP5 owed by WP8-R G-R3 (record created-phonon spectra dℋ/dω_ph in the §3.4 MD and §2 e–ph kernel outputs) and G-R4 (𝔶 and F_NR at E_R ≲ 350 eV, §3.3 non-adiabatic channel): write them as amendment text.
5. For each yield-dependent statement in WP8-R and WP8-F: CONSISTENT / NEEDS CORRECTION (with the correction). State whether the WP8-R verdict survives.
6. Output a defect list (ID, owner, severity S/N/W, exact fix).

## Read
The four returns above, /home/user/dmdd-solid/returns/R8/WP6-v3.md, /home/user/dmdd-solid/LIMITS.md (WP7-E section), /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/state/CORRECTIONS.md §18.

Return file: /home/user/dmdd-solid/returns/R14/WP5-AUD.md (≤ 400 lines). ID for code: WP5-AUD.

## Rules
- Theory and data compilation only. Run no new first-principles numerics such as DFT, DFPT, MD or Monte Carlo. Closed-form estimates and sympy/numpy checks of ≤ 2 min are fine. Put the checks in /home/user/dmdd-solid/code/<ID>/checks.py, and they must pass.
- Every material property needs provenance: a database entry ID (OPTIMADE/JARVIS-DFT/COD/NIST) or a full-text quote with page/table. Tag each value [FT] (full text), [DB] (database), [E] (estimate) or [UNVERIFIED].
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-<ID>/. Verify every arXiv ID against the API. Delete the PDFs at the end. Use INSPIRE for citation walks (OpenAlex is rate-limited).
- Do not use the Materials Project REST API (no key). Public OPTIMADE endpoints, including MP's, and JARVIS downloads are fine.
- Follow /home/user/dmdd-solid/CONVENTIONS.md (incl. "R13 amendments") and /home/user/dmdd-solid/NOTATION.md (incl. "Rows added WP7-E"). Introduce new symbols only in the closing 'Symbols' section.
- Write only your return file(s) and your code/<ID>/ folder. Do not commit. Do not edit any other file.
- End with three sections: 'Symbols introduced/used', 'Interface flags' and 'Proposed LIMITS rows'.
- Your final message is a summary of ≤ 15 lines.
