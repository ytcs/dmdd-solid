# Round R7, referee brief REF-WP0-B (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not polish, and do not be helpful beyond stating
the corrections.

## Under review
/home/user/dmdd-solid/returns/R6/WP0-v2.md, a standalone revised package, with its checks in /home/user/dmdd-solid/code/WP0-v2/.

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
  /home/user/dmdd-solid/literature/papers-r7-WP0-B/ and delete it afterwards. Rate each claim CONFIRMED / REFUTED /
  UNRESOLVED;
- (d) consistency with CONVENTIONS and NOTATION, and with WP0-v2's interfaces;
- (e) gap-closure claims: is the formula plus computation specification sufficient, or a restatement?
- (f) the package's "Contested corrections" section, if any: is the argument right?
- (g) focus items: the master formula and the 16-operator basis; screening (5.3), the four Coulomb-line classes and (5.6)–(5.7); CC-1 (out-state vs in-state local-field weight); Theorem D (PST applicability with Coulomb singularities) and (iv′)/(iv″) with the Γ/δ bound and the code-pair conditions d1–d11; the mixed third-moment sum rule (4.7) with its q → 0 qualifier; the C7 soft limit (4.9); L0, L17

## Output
Write /home/user/dmdd-solid/referees/R7/REF-WP0-B.md (≤ 250 lines). Start with a verdict table, one row per main claim:
STANDS / STANDS WITH CORRECTION / FALLS, with a one-line reason. Then give the arguments, with explicit
derivations. Run no numerical simulations; sympy checks of ≤ 2 min are fine. Your final message is a
summary of ≤ 15 lines.
