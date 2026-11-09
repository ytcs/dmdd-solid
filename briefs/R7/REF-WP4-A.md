# Round R7, referee brief REF-WP4-A (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not polish, and do not be helpful beyond stating
the corrections.

## Under review
/home/user/dmdd-solid/returns/R6/WP4-v2.md, a standalone revised package, with its checks in /home/user/dmdd-solid/code/WP4-v2/.

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
  /home/user/dmdd-solid/literature/papers-r7-WP4-A/ and delete it afterwards. Rate each claim CONFIRMED / REFUTED /
  UNRESOLVED;
- (d) consistency with CONVENTIONS and NOTATION, and with WP0-v2's interfaces;
- (e) gap-closure claims: is the formula plus computation specification sufficient, or a restatement?
- (f) the package's "Contested corrections" section, if any: is the argument right?
- (g) focus items: TOP PRIORITY: the conditional claim that 1708.08929 and 1910.02091 omit the background screening factor for dark-photon coupling. Verify against both full texts, including their own κ conventions, and settle it (OW4-2). Also: the BCS conserving response and the closed form 𝔤_I(y); η_pb = Δ_BCS⟨N_qp⟩/ω; the factor-4 claims against 2101.08263 eq 3 and 1512.04533 eq 13; retarded vs time-ordered against 2609.06423; the Drude/Mermin πqℓ/6 claim; the chiral/CD selection rule and its −½ fix; Theorem D-g

## Output
Write /home/user/dmdd-solid/referees/R7/REF-WP4-A.md (≤ 250 lines). Start with a verdict table, one row per main claim:
STANDS / STANDS WITH CORRECTION / FALLS, with a one-line reason. Then give the arguments, with explicit
derivations. Run no numerical simulations; sympy checks of ≤ 2 min are fine. Your final message is a
summary of ≤ 15 lines.
