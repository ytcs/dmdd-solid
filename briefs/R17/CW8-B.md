# R17 brief CW8-B: framework bookkeeping closures

## Target
Close LOOSE-ENDS rows **LE-164** (the remaining part), **LE-167, 169, 170, 174, 175**. Read each row in /home/user/dmdd-solid/state/LOOSE-ENDS.md.

## Required
1. **LE-164 and LE-167.**
   - The WP5-v4 symbol-table rows not yet in NOTATION.
   - Check IF-R8-7 (3Δ → 4Δ) and IF-R8-8 (thresholds 352/395 eV) against SOTA and LIMITS L20/L23.
   - Merge the WP5-v4 proposed L20–L22 amendments and the (W11) pointer: returns/R13/WP5-v4.md, read with returns/R14/WP5-AUD.md and returns/R16/CW5-errata.md.
2. **LE-169.** Every LIMITS row still [D, sketch], "observed" or "prefactor open" gets an explicit exact-remaining-gap field.
3. **LE-170.** Re-audit the H1–H6 and G1–G13 + catalog §12 coverage table (LOOSE-ENDS §1b; returns/R6/AUDIT.md §8 for the catalog) against the current state. Write the updated verdict table into state/LOOSE-ENDS.md §1b.
4. **LE-174.** For each "owner to cite/adopt" interface flag addressed to a frozen v3 package, either:
   - write the owed adoption text into state/CORRECTIONS.md §19, or
   - state why it is not needed.
5. **LE-175.** Decide whether 𝔘_C, 𝔇^F and 𝔇^{pair} belong in the CONVENTIONS §7 operator / DM-tensor basis. Add the rows with a reason, or record why they stay outside the basis.

## Edit only
LIMITS.md, NOTATION.md, CONVENTIONS.md, state/CORRECTIONS.md, state/LOOSE-ENDS.md, state/SOTA.md, and returns/R17/CW8-B-log.md (new).

## Rules
- You act for the coordinator and may edit only the files named in your brief.
- Follow CONVENTIONS and NOTATION.
- Literature via /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/literature/papers-<ID>/. Verify every arXiv ID against the API. INSPIRE for citation walks. Delete the PDFs at the end.
- Do not commit. Write a log file: returns/R17/<ID>-log.md, recording every edit as file → section → source.
- Final message ≤ 12 lines.
