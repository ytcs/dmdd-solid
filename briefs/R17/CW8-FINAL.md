# R17 coordinator brief CW8-FINAL: final merge of the remaining verified results

You act for the coordinator. **You may edit exactly these files:** LIMITS.md, NOTATION.md, CONVENTIONS.md, state/CORRECTIONS.md, state/SOTA.md, state/LOOSE-ENDS.md, FRAMEWORK.md and registry.md, and returns/R17/CW8-FINAL-log.md (new). Edit no return and no referee report. Do not commit.

## Inputs (later overrides earlier)
1. **CW1.** returns/R16/CW1.md, read through referees/R16/VER-CW1.md and returns/R16/CW1-errata.md (the errata's re-issued text wins).
2. **WP8.** returns/R17/WP8-errata.md, read through referees/R17/VER-ERR-WP8.md (0 FALLS). The verifier's corrections are applied as owed text by this merge. In particular:
   - the heavy-mediator window becomes the verifier's per-material, pairwise statement: onset 4.7–5.7 × m_min, with the first-order η shift;
   - the 1910.10716 CaWO₄ defect is CONFIRMED;
   - the 2508.08858 citation becomes ref. [73];
   - CsI elastic constants are owed data (DEFERRED-COMPUTE);
   - B₀ is isothermal;
   - G-F6 wording;
   - L(k,ω) k-cut;
   - ⁴⁴Ti/⁴⁴Sc;
   - the §16.4 Pb-salt S1/S3 rows;
   - literature reads not labelled as measurements.

   WP8 (U-v3, F-v3, table v4 with errata, S-v2 with ranking_v3) is now VERIFIED; record its status.
3. **GAP-EF.** returns/R17/GAP-EF-v3-errata.md: the grid-commensurate numbers supersede GAP-EF-v2's last digits.
4. **Compute.** returns/R15/COMP-PH.md ([CALC]; Si controls pass except ε_∞ (+11%) and L_LO (−5.4%); Ge fails its band-order and TA controls → formulated as DC-2 and DC-4). Also returns/R15/COMP-PAER.md.
5. **Deferred work.** state/DEFERRED-COMPUTE.md: link it from LOOSE-ENDS and SOTA as the Phase-2 work list.
6. **Decisions.** CONVENTIONS §13 rows 32–38 (coordinator decisions already taken).

## Required
- **LIMITS.** Apply CW1 rows L8, L3 (CW1-errata: L3 unchanged), L9b; add the accepted CW1-L rows; apply the WP8 and GAP-EF row changes; use unique labels.
- **NOTATION and CORRECTIONS.** New symbols and renames go in NOTATION. Owed corrections to returns go in CORRECTIONS §20 (exact text, S/N/W).
- **SOTA:** an "R17 final state" block. It must give the Si PAER window as finally established:
  - PAER onset 0.3332 MeV (exciton replica) / 0.3374 MeV (continuum);
  - first zero-phonon edge 0.405–0.408 MeV (1s 0.402–0.405);
  - PAER leads to ≈ 0.43 MeV (≥ 0.42);
  - two-channel region 0.43–0.51 MeV;
  - zero-phonon leads above ≈ 0.51 MeV.

  Give each its status and its tier-H deferral (DC-1). Include the WP8 next-target guide headline (diamond leads the NR edge under the array rule, TeO₂ the survivors' heavy-mediator channel, and so on).
- **LOOSE-ENDS.** Mark every remaining OPEN or OPEN-pending row CLOSED / CLOSED-AS-EXACT-GAP / CANNOT-CLOSE with a pointer, and update the §4 counts. **The target is no OPEN row.** List any row that cannot be closed by what exists.
- **FRAMEWORK and registry.** Final statuses.
- **Verify the merged packages.** Run each merged package's checks.py once and report the pass counts.

Final message ≤ 12 lines: the LOOSE-ENDS final counts, the remaining OPEN rows (should be none), and conflicts for the coordinator.
