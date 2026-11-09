# R8 consistency audit brief AUDIT-2 (v3 packages)

## Target
Read all v2 packages, /home/user/dmdd-solid/returns/R8/WP0-v3.md through WP6-v3.md (plus every "Interface flags" section in them), together with /home/user/dmdd-solid/CONVENTIONS.md,
/home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/LIMITS.md, /home/user/dmdd-solid/state/CORRECTIONS.md and /home/user/dmdd-solid/state/SOTA.md.

Check the cross-package consistency of the following:
- (1) Every interface quantity, wherever it is used: the master formula; S/R/L/ε definitions; the screening
  formula; Theorem D sectors; the final-state-resolved response feeding WP5; the multiphonon S_NN feeding
  WP5; the M̃ amplitude; the halo factor; the nuisance structure feeding WP6.
- (2) Every LIMITS entry: owner, status, and the chain citing current v2 equation numbers.
- (3) Symbols against NOTATION v3.
- (4) Every owed correction in CORRECTIONS.md: applied, contested (with argument), or missing.
- (5) Duplicated or contradictory claims across packages, such as the anisotropy/modulation results in
  WP1 and WP2, or the Migdal claims in WP0 and WP3.
- (6) Every gap G1–G13 and every catalog gap: assigned, closed with formula + specification, or recorded
  as an exact remaining gap.

## Output
Also check every item in state/SOTA.md marked "R7 ITEM" or "for the audit", e.g. the WP2/WP3 𝔨₃ normalisation mismatch and the stale WP5-v2 I1/I3 flag text. Resolve or route each one.

Write /home/user/dmdd-solid/returns/R8/AUDIT-2.md (≤ 250 lines):
- a defect table: ID | packages | location | defect | proposed resolution | severity (blocking /
  minor);
- the LIMITS status table;
- the gap-coverage table.

Do not edit any other file. Sympy checks are allowed. Your final message is a summary of ≤ 15 lines,
including the count of blocking defects.

## Additional R8 items
- Check that every interface flag raised in a v3 package has been applied by the package that owns the
  quantity. The flags are: WP0 G1–G15; WP1 IF-3..IF-17; WP2 IF-1..IF-14; WP3 IF-2..IF-16; WP4 I1–I17;
  WP5 IF-R8-1..10; WP6 IF6-2..IF6-17. List each one: applied / missing / not needed.
- M1 window consistency across WP1, WP3, WP6 and state/SOTA.md: the edges (Si ≈ 0.333–0.42 MeV, Ge ≈
  0.213–0.32 MeV [E]), the competing ZPL classes, and the p̄_on table.
- Coordinator-owned files that still state superseded values: CONVENTIONS, LIMITS, CONTROLS, NOTATION,
  SOTA. List exact lines and replacements.
- Use the catalog-coverage classification only if it changed.
Write /home/user/dmdd-solid/returns/R8/AUDIT-2.md (≤ 250 lines).
