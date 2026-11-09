# R14 referee brief REF-WP8-R-A (hostile, isolated)

## Role
You are a hostile referee. Find errors and overclaims. Do not be helpful beyond stating the corrections.

## Under review
/home/user/dmdd-solid/returns/R13/WP8-R.md, with its checks in /home/user/dmdd-solid/code/WP8-R/ (rerun them).

## Read only
- the files under review;
- the campaign packages the return cites (returns/R8/*-v3.md, returns/R12/*.md, returns/R13/WP5-v4.md as cited);
- /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/CONTROLS.md, /home/user/dmdd-solid/DONE.md, /home/user/dmdd-solid/LIMITS.md, /home/user/dmdd-solid/STATEMENT.md.
Do NOT read referees/, state/, briefs/, returns/R14/, other R13 WP8 returns not cited, or LAUNCHES/log.

## Rubric
DONE.md rung 4, plus:
- (a) every DERIVED step is actually derived, with its hypotheses;
- (b) every proposed LIMITS row: source quoted correctly from full text, chain valid, validity and leading correction right;
- (c) every claim that a published paper or database is wrong: verify against the full text, fetched with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py fetch <id> -o /home/user/dmdd-solid/literature/papers-r14-REF-WP8-R-A/ and deleted afterwards. Rate CONFIRMED / REFUTED / UNRESOLVED;
- (d) consistency with WP0-v3, CONVENTIONS and NOTATION;
- (e) every material value: provenance tag present and correct;
- (f) test the central claim (NR/ER phonon populations lose frequency/polarisation memory within ~10–100 ns, ≲ 0.1 mm) against how the CDMS phonon pulse-shape (surface-event) discrimination actually works: if that precedent uses phonon information the return says is erased, the verdict has a hole. Check the down-conversion/isotope rates (Tamura, Maris), AMM transmissions and the 𝔖 algebra; check the GO/NO-GO mapping against the brief rule (≳ 2σ at sub-keV where yield/timing fails).

## Output
Write /home/user/dmdd-solid/referees/R14/REF-WP8-R-A.md (≤ 220 lines). Start with a verdict table, one row per main claim: STANDS / STANDS WITH CORRECTION / FALLS, with a reason. Run no numerical simulations; sympy/numpy checks of ≤ 2 min are fine. Write only that file (and the papers folder, PDFs deleted). Do not commit. Your final message is a summary of ≤ 12 lines.
