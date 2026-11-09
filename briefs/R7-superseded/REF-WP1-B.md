# Round R6, referee brief REF-WP1-B (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not polish, and do not be helpful beyond stating
the corrections.

## Under review
/home/user/dmdd-solid/returns/R5/WP1.md

## Read only
- the files under review and their scripts in /home/user/dmdd-solid/code/;
- /home/user/dmdd-solid/STATEMENT.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/CONTROLS.md, /home/user/dmdd-solid/DONE.md, /home/user/dmdd-solid/LIMITS.md;
- /home/user/dmdd-solid/returns/R4/WP0.md, for the architecture the return builds on.

Do NOT read referees/, state/, other returns, or other briefs.

## Rubric
DONE.md rung 4, plus:
- (a) every DERIVED step is actually derived, with its hypotheses;
- (b) every LIMITS entry: the source formula is quoted correctly, the truncation chain is valid, and the
  validity conditions and leading correction are right;
- (c) every "the published paper is wrong" claim: VERIFY against the full text yourself. Fetch it with
  /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o
  /home/user/dmdd-solid/literature/papers-ref-WP1-B/, and delete the PDFs after. Rate each claim CONFIRMED / REFUTED /
  UNRESOLVED;
- (d) consistency with WP0's conventions (q sign, S normalisation, EPW g, e² = 4πα, η/(2q) halo factor);
- (e) the gap-closure claims: is the formula plus computation specification sufficient, or is it a
  restatement?
- (f) the specific focus items: the static ε ≥ 1 proof at RPA+LFE; the on-shell cancellation of the longitudinal velocity and the claim that only 3 of 5 Catena responses are independent; the claimed ~40× O₈ underestimate in 2510.25835; the spin channel = ¼ unscreened; exciton selection rules and thresholds (0.473, 0.708, 0.420 MeV); the anisotropy symmetry argument against 2607.06005

## Output
Write /home/user/dmdd-solid/referees/R6/REF-WP1-B.md (≤ 250 lines). Start with a verdict table, one row per main claim:
STANDS / STANDS WITH CORRECTION / FALLS, with a one-line reason. Then give the arguments, with explicit
derivations. Run no numerical simulations; sympy checks of ≤ 2 min are fine. Your final message is a
summary of ≤ 15 lines.
