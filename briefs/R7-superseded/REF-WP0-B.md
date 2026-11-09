# Round R6, referee brief REF-WP0-B (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not polish, and do not be helpful beyond stating
the corrections.

## Under review
/home/user/dmdd-solid/returns/R4/WP0.md and /home/user/dmdd-solid/returns/R5/O4.md (O4 extends WP0 Theorem D)

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
  /home/user/dmdd-solid/literature/papers-ref-WP0-B/, and delete the PDFs after. Rate each claim CONFIRMED / REFUTED /
  UNRESOLVED;
- (d) consistency with WP0's conventions (q sign, S normalisation, EPW g, e² = 4πα, η/(2q) halo factor);
- (e) the gap-closure claims: is the formula plus computation specification sufficient, or is it a
  restatement?
- (f) the specific focus items: the master formula and operator basis; screening eq 5.3 and its ELF claims; Theorem D's hypotheses and proof (PST applicability with Coulomb singularities); the new third-moment mixed sum rule eq 4.7; L17; O4's convention-independence theorem and its bound

## Output
Write /home/user/dmdd-solid/referees/R6/REF-WP0-B.md (≤ 250 lines). Start with a verdict table, one row per main claim:
STANDS / STANDS WITH CORRECTION / FALLS, with a one-line reason. Then give the arguments, with explicit
derivations. Run no numerical simulations; sympy checks of ≤ 2 min are fine. Your final message is a
summary of ≤ 15 lines.
