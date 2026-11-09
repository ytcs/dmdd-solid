# R14 referee brief REF-GAP-EF-B (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not be helpful beyond stating the corrections.

## Under review
/home/user/dmdd-solid/returns/R14/GAP-EF.md, with its checks in /home/user/dmdd-solid/code/GAP-EF/ (rerun them).

## Read only
- the files under review;
- the campaign packages the return cites (returns/R8/*-v3.md, returns/R12/*.md, returns/R13/WP5-v4.md as cited);
- /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/CONTROLS.md, /home/user/dmdd-solid/DONE.md, /home/user/dmdd-solid/LIMITS.md, /home/user/dmdd-solid/STATEMENT.md.
Do NOT read referees/, state/, briefs/, LAUNCHES/log, or any returns/R14 or R15 file other than GAP-EF.md. You may read returns/R13/WP5-v4.md, WP8-U.md, returns/R12/WP7-E-v3.md, returns/R8/WP6-v3.md.

## Rubric
DONE.md rung 4, plus:
- (a) every DERIVED step is actually derived, with its hypotheses;
- (b) every proposed LIMITS row: source quoted correctly from full text, chain valid, validity and leading correction right;
- (c) every claim that a published paper or database is wrong: verify against the full text, fetched with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o /home/user/dmdd-solid/literature/papers-r14-REF-GAP-EF-B/ and deleted afterwards. Rate CONFIRMED / REFUTED / UNRESOLVED;
- (d) consistency with WP0-v3, CONVENTIONS and NOTATION;
- (e) every material value: provenance tag present and correct;
- (f) the central derivation: re-derive F_eh = 𝒱_< + 𝒱_> + 2𝒞_<> with the energy constraint independently (sympy), the claim that WP5-v4 §6.4(ii)'s 0.31 is a fixed-pair-number artefact (0.039 with the constraint), the random-parking limit 0.05104, the Klein-identity claim, the R&K F_∞ = 0.115 reproduction; whether the one-parameter calibration (𝒜_ph to Si ε_eh) makes the Si F_eh = 0.114 a genuine prediction; the validation set residuals and the [UNVERIFIED] exclusions; the IF-E9 Bernoulli-thinning result; whether the closed form and the 'observed' F(ε/E_g) quadratic are correctly tagged.

## Output
Write /home/user/dmdd-solid/referees/R14/REF-GAP-EF-B.md (≤ 220 lines). Start with a verdict table, one row per main claim: STANDS / STANDS WITH CORRECTION / FALLS, with a reason. Run no numerical simulations; sympy/numpy checks of ≤ 2 min are fine. Write only that file (and the papers folder, PDFs deleted). Do not commit. Your final message is a summary of ≤ 12 lines.
