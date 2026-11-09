# Round R7, referee brief REF-WP3-B (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not polish, and do not be helpful beyond stating
the corrections.

## Under review
/home/user/dmdd-solid/returns/R6/WP3-v2.md, a standalone revised package, with its checks in /home/user/dmdd-solid/code/WP3-v2/. It contains Part I, the consolidated phonon-assisted electron recoil (PAER) theory, and Part II, the mixed sector.

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
  /home/user/dmdd-solid/literature/papers-r7-WP3-B/ and delete it afterwards. Rate each claim CONFIRMED / REFUTED /
  UNRESOLVED;
- (d) consistency with CONVENTIONS and NOTATION, and with WP0-v2's interfaces;
- (e) gap-closure claims: is the formula plus computation specification sufficient, or a restatement?
- (f) the package's "Contested corrections" section, if any: is the argument right?
- (g) focus items: PAER amplitude, Pauli theorem, rate and η/(2q); the screened amplitude M̃ with the pair channel and the [0.5, 1.2] systematic; the soft limit and C7a–e; the Dyson convention outside the window; the angle-averaged onset exponents p_on (3/4; Si TA 4) and the edge-shell criterion Q_w; unification of the four Migdal formulas and the 4α prefactor; the claim against 2603.13052 eq 4.7; the ZG energy-δ defect against 1604.02394 eq 24; crystal NR bremsstrahlung and the GaAs ~10³ estimate; J8

## Output
Write /home/user/dmdd-solid/referees/R7/REF-WP3-B.md (≤ 250 lines). Start with a verdict table, one row per main claim:
STANDS / STANDS WITH CORRECTION / FALLS, with a one-line reason. Then give the arguments, with explicit
derivations. Run no numerical simulations; sympy checks of ≤ 2 min are fine. Your final message is a
summary of ≤ 15 lines.
