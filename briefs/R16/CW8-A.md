# R16 coordinator brief CW8-A: merge the verified R14–R16 results into the campaign files

You act for the coordinator. **You are authorised to edit exactly these files:** LIMITS.md, NOTATION.md, CONVENTIONS.md, state/CORRECTIONS.md, state/SOTA.md, state/LOOSE-ENDS.md, FRAMEWORK.md, registry.md. Edit no return and no referee report; those are the record. Do not commit.

## Inputs, merged in this order of authority (later overrides earlier)
1. returns/R14/WP5-AUD.md with referees/R14/REF-WP5-AUD-{A,B}.md, as settled in returns/R16/CW5.md §LE-22 and CW5-errata.md.
2. returns/R16/GAP-EF-v2.md + GAP-EF-v2-errata.md, which supersede R14 GAP-EF. EF-LIT.md.
3. For each of CW2, CW3, CW4, CW5, CW6, CW7: returns/R16/CWn.md, read through referees/R16/VER-CWn.md and returns/R16/CWn-errata.md. **Only the errata's re-issued text is applied where the errata re-issues an item; items marked "unchanged" are applied from CWn.md.** Where a verifier item has an accepted rebuttal in the errata, the errata wins.
4. returns/R16/WP8-R-v2.md (with CW6-errata §B4), WP8-U-v3.md, WP8-U-table-v4.csv, WP8-F-v3.md. These are the current WP8 versions; WP8-S is NOT yet final, so do not merge any ranking.
5. returns/R15/CMPMC-AUD.md, returns/R16/CMPMC-DEV.md (CMPMC main 3d43a02), returns/R15/COMP-PAER.md (Si window [CALC]; rate/reach [E]).

## Required
- **LIMITS.md:** apply every owed correction aimed at LIMITS rows, and add the accepted proposed rows. Use unique labels: rename any clash; there are two rows labelled L17, so disambiguate them; v1 L39–L42 clash with WP8-R's rows. Statuses follow CONVENTIONS §12: claims verified R×1 after a return are REFEREED only if their package also had R×2; otherwise CLAIMED + VERIFIED. Every withdrawn or refuted item goes into a Withdrawn list.
- **NOTATION.md:** add a section "Rows added R14–R16" with every new symbol from these returns, and resolve clashes as in the earlier WP7 tables (rename table). Also apply the pending items: IF-R13-1 (stale §G rows 𝐍, N_trap, Y_H), and θ_X → θ_exc.
- **state/CORRECTIONS.md:** a §19 with every owed correction targeting a return (WP0–WP6 v3, WP5-v4, WP7-*, WP8 v1/v2), with exact text and type S/N/W. Mark §18's last row (IF-R13-7) done.
- **CONVENTIONS.md:** the owed rows (e.g. the r_mat convention, the [DB] tag, CW7's §13 row 29), each with its reason.
- **state/SOTA.md:** append an "R14–R16 consolidated state" block: one line per result, with status. Include the cross-cutting findings: the JARVIS C₄₄/C₆₆ shear-order swap affecting all non-cubic tensors used R14–R16 (fixed in table v4), the CMPMC Kaplan-buffer bug, and the published-paper errors confirmed.
- **state/LOOSE-ENDS.md:** mark each LE row CLOSED / CLOSED-AS-EXACT-GAP / CANNOT-CLOSE per the verified errata, with a pointer to where it is closed. Leave CW1 rows (LE-24…47, 178, 179) and LE-159 (WP8-S) OPEN-pending. List any row that is not closed by anything.
- **FRAMEWORK.md, registry.md:** status updates only.
- Write /home/user/dmdd-solid/returns/R16/CW8-A-merge-log.md: every edit, as file → section → source item. Report any conflict you could not settle. Do not guess; list it for the coordinator.

## Rules
Keep edits surgical; do not rewrite unrelated text. Follow CONVENTIONS §14 label prefixing. Run the existing code/*/checks.py of the merged packages once at the end and report their pass counts. Final message ≤ 15 lines.
