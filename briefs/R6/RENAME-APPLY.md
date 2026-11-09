# R6 brief RENAME-APPLY: apply the owed v4 renames inside the v2 packages

## Target
Apply every rename listed in /home/user/dmdd-solid/state/CORRECTIONS.md §17 (and any §0 global rename still unapplied) to
/home/user/dmdd-solid/returns/R6/WP0-v2.md and WP2-v2.md through WP6-v2.md, edited in place. WP1-v2 owes none, but check it.

## Constraints
- Purely notational. Change no formula content, numbers, tags or claims.
- If a rename would change meaning (an ambiguous occurrence), leave that occurrence and list it.
- In each v2 file, update its "Symbols introduced/used" table to NOTATION v4, and add one closing-table row
  "NOTATION v4 renames (CORRECTIONS §17)".
- Apply the same renames to the matching code/<WP>-v2/checks.py, but only in comments and labels. Re-run
  every checks.py; all must still pass.
- Do not edit any other file.

## Output
Your final message is a ≤8-line summary: renames applied per file, ambiguous occurrences left, and the
check results per package.
