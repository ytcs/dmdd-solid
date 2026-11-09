# Round R7, referee brief REF-WP1-B (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not polish, and do not be helpful beyond stating
the corrections.

## Under review
/home/user/dmdd-solid/returns/R6/WP1-v2.md, a standalone revised package, with its checks in /home/user/dmdd-solid/code/WP1-v2/.

## Read only
- the files under review;
- /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/CONTROLS.md, /home/user/dmdd-solid/DONE.md, /home/user/dmdd-solid/LIMITS.md;
- /home/user/dmdd-solid/returns/R6/WP0-v2.md (the architecture) when reviewing any other package.

Do NOT read referees/, state/, returns/R6/AUDIT.md, other returns, or other briefs.

## Rubric
DONE.md rung 4, plus:
- (a) every DERIVED step is actually derived, with its hypotheses;
- (b) every LIMITS entry the package owns: the source formula is quoted correctly, the truncation chain is
  valid, and the validity conditions and leading correction are right;
- (c) every claim that a published paper is wrong: VERIFY against the full text yourself. Fetch it with
  /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o
  /home/user/dmdd-solid/literature/papers-r7-WP1-B/ and delete it afterwards. Rate each claim CONFIRMED / REFUTED /
  UNRESOLVED;
- (d) consistency with CONVENTIONS and NOTATION, and with WP0-v2's interfaces;
- (e) gap-closure claims: is the formula plus computation specification sufficient, or a restatement?
- (f) the package's "Contested corrections" section, if any: is the argument right?
- (g) focus items: the static ε ≥ 1 proof at RPA+LFE; the on-shell longitudinal-velocity cancellation and the 3-of-5 claim against 2105.02233; the ~40× O₈ claim against 2510.25835; the spin channel (¼ unscreened plus XC); exciton selection rules and thresholds (0.472/0.708/0.420 MeV); the symmetry argument against 2607.06005; the out-state [E2]

## Output
Write /home/user/dmdd-solid/referees/R7/REF-WP1-B.md (≤ 250 lines). Start with a verdict table, one row per main claim:
STANDS / STANDS WITH CORRECTION / FALLS, with a one-line reason. Then give the arguments, with explicit
derivations. Run no numerical simulations; sympy checks of ≤ 2 min are fine. Your final message is a
summary of ≤ 15 lines.
