# Round R6, referee brief REF-WP4-A (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not polish, and do not be helpful beyond stating
the corrections.

## Under review
/home/user/dmdd-solid/returns/R5/WP4.md

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
  /home/user/dmdd-solid/literature/papers-ref-WP4-A/, and delete the PDFs after. Rate each claim CONFIRMED / REFUTED /
  UNRESOLVED;
- (d) consistency with WP0's conventions (q sign, S normalisation, EPW g, e² = 4πα, η/(2q) halo factor);
- (e) the gap-closure claims: is the formula plus computation specification sufficient, or is it a
  restatement?
- (f) the specific focus items: TOP PRIORITY: the claim that 1708.08929 and 1910.02091 omit 1/κ² background screening (rates ~1600× too high). Verify against both full texts, and check whether their κ conventions already include it. Also: BCS conservation and the g_I(ω/Δ) closed form; the factor-4 claims against 2101.08263 eq 3 and 1512.04533 eq 13; the retarded vs time-ordered claim against 2609.06423; the Drude πqℓ/6 claim; the chiral/CD selection rule

## Output
Write /home/user/dmdd-solid/referees/R6/REF-WP4-A.md (≤ 250 lines). Start with a verdict table, one row per main claim:
STANDS / STANDS WITH CORRECTION / FALLS, with a one-line reason. Then give the arguments, with explicit
derivations. Run no numerical simulations; sympy checks of ≤ 2 min are fine. Your final message is a
summary of ≤ 15 lines.
