# Ch20 post-revision check 2: R1 rework (isolated verifier, 2026-11-06)

Scope: postrev-check.md (REWORK item), revision.md "Post-check rework", tex/ch20/s20-5.tex, s20-summary.tex, Ch20 F rows,
E.25, figscripts/ch20/kern20_5.py, film20_5.py, kern20_5.log. Scratch test: the kern20_5 solver run without the figure
(r = inf, 0.72); nothing in figscripts written.

## 1. Phonon return and energy closure: CONFIRMED (closure wording in revision.md overstated)
- Both films return every phonon they emit after a first pair break (escaped above-gap and relaxation phonons, film20_5
  spectrum): `solve(..., ret=True)` applies the return matrix to each film; the Nb-like film's relaxation phonons
  between 0.36 and 3 meV return and are absorbed by Al. Only returns below 2Δ_Al = 0.36 meV are dropped (physical:
  no film absorbs them). The `Ret[j:, j] = 0` cut removes 0 energy at every tested W (0.5–62 meV, both gaps, r = inf/0.72).
- Returned energy per first-broken phonon = W(1 − Y) within 1e-4 relative (film20_5 closure max 9.7e-5 thick, 3.3e-5
  at 60 nm). Independent balance: absorbed + bare loss = birth + returned to 1e-6 in all 12 cases (1/2 films x
  thick/60 nm x primaries/Luke).
- Note: kern20_5's "closure 1.00000" is an identity (the dropped term is the residual, 1e-16). The physical closure
  (residual minus the sub-0.36 meV returns) is ≤ 1.6e-4 of the birth energy, not 1e-5 as revision.md says. Effect
  on 𝔯_coll ~1e-4; no book text claims a closure figure. No action in the book.

## 2. Final band: CONFIRMED (log + scratch rerun at sample points)
| Item | Text | Log / rerun |
|---|---|---|
| all conserved, 0.75–4.7 meV | 0.81–1.02 | 0.813–1.018 (max: one Al film, κ = 1, spread, 0.75 meV) |
| at 0.84 meV | 0.82–1.01 | 0.820–1.014; rerun two thick B 0.5604/0.6837 = 0.8197 |
| one Al film | 0.96–1.02 | 0.960–1.018 (r = inf … 0.72) |
| two films | 0.81–1.01 | grid 0.813–1.001; fine grid max 1.014 at 3.49 meV (rerun 1.0141) |
| ε_prim (two thick) | 0.684 | 0.6837 (rerun 0.683719); a_prim 0.610; deleted 0.610/0.563 |
| uniform sink, loss ≤ 0.3 | ≤ 1.023 ("below 1.03") | 1.0232 (one 60 nm Al film, shape A); two films fall to 0.55 |
| escape, one film | within 0.002 | max 0.0016 (r = 0.72); 0.995/0.969 at 0.84 meV |
| two 60 nm films | 0.85–1.01 | fine grid 0.849–1.008 |
1.128 (1.099–1.152) is reached by no conserved case (log: False).

## 3. Selective sink: CONFIRMED
1.05–1.10 (r = 4) and 1.30–1.53 (60 nm) match the lost variant (1.054–1.103, 1.299–1.525). 20.5 l.76 calls them "an
upper envelope of the lumped-film assumption; the estimate does not identify a physical sink"; Fig. 20.6 (purple,
"a selective sink that the model does not identify in a detector (upper envelope)"), the summary, the nuisance row
and the F row label them the same way. E.12/E.25 code lumped films return their phonons (E.12 l.61, E.25 closure
test), so the computed kernels will not inherit the selective sink.

## 4. Conclusion wording: CONSISTENT after two trivial fixes (applied)
20.5 l.80, Fig. 20.6, summary l.11 and nuisance row l.35 all carry "not reached; not excluded until computed kernels
test real detectors; the two-bias measurement decides" (the nuisance row in short form). E.25 says nothing contrary
(degeneracy, l.55; "conditional verdicts", l.92). Fixed in tex/appF/F-rows.tex:
- Ch20 F row (l.898) lacked the conclusion: appended "1.128 is not reached by the transport estimate, and not excluded
  until computed kernels test real detectors (E.25); the two-bias measurement of 19.5 decides."
- Ch20 F row corrections (l.899) "near-gap yield (up to +0.09)" was the deleted-phonon value: now "(up to +0.09 when
  film phonons are deleted; with them returned the ratio stays ≤ 1.02)".

## 5. Other rework items: CONFIRMED
Operating point "0.84 to 4.6 meV for Si electrons" with the 0.75–4.7 scan labelled as covering Ge; ϖ_O 0.39/0.12/
0.045/0.019; flat-yield 0.992 and 0.935–0.998; the 1.36 (f_det = 0.873)/1.52 qualifier; ρ 2.70/2.73 clause.

## Verdict: ACCEPT (with the two F-row wording fixes above, applied)
