# Round R6, referee brief REF-WP6-A (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not polish, and do not be helpful beyond stating
the corrections.

## Under review
/home/user/dmdd-solid/returns/R5/WP6.md

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
  /home/user/dmdd-solid/literature/papers-ref-WP6-A/, and delete the PDFs after. Rate each claim CONFIRMED / REFUTED /
  UNRESOLVED;
- (d) consistency with WP0's conventions (q sign, S normalisation, EPW g, e² = 4πα, η/(2q) halo factor);
- (e) the gap-closure claims: is the formula plus computation specification sufficient, or is it a
  restatement?
- (f) the specific focus items: the halo reduction (Radon transform + 2 moments; ξ = 2∫u′η du′); the power-law edge Δ₀^{7/2+k+p} and its degeneracy; m_min(Si) values; the conservative halo-independent bound and its use of positivity; the nuisance types, positivity, and the analytic q_max tail; the profiling vs envelope cost claim; the WP0 defects W1–W5; the claims against 2311.04957

## Output
Write /home/user/dmdd-solid/referees/R6/REF-WP6-A.md (≤ 250 lines). Start with a verdict table, one row per main claim:
STANDS / STANDS WITH CORRECTION / FALLS, with a one-line reason. Then give the arguments, with explicit
derivations. Run no numerical simulations; sympy checks of ≤ 2 min are fine. Your final message is a
summary of ≤ 15 lines.
