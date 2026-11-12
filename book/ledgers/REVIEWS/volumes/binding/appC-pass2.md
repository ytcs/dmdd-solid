# Binding round, second pass: appC (Mathematical tools)

Base commit for the content guard: 60cc72c. Starting text: the reviewed state at 546ad31 (first pass plus the fixes of review-vol1c.md). None of the reviewer's fixes were undone. I read every paragraph of C-1 to C-20 again, whole, including the key-result boxes and the worked example of C-17. Each sentence's pointers were checked, and I looked hardest at the two constructions the review named: plural pronouns and quantifiers (*they, them, their, these, those, both, each, either, the other two*) whose antecedent lies two sentences back or is not a noun phrase, and *that of / those of / that through* without a coordinated antecedent. I also checked the rest of pattern 27 (propositional *this/which*, *such X*, ordinal ellipsis such as "the second gives", pointers to objects stated only negatively, and *the X* before X is introduced). I did not touch the open items from the first pass (C-4:76, C-12:61).

## Per file

| File | Ranker before | Ranker after | Sentences changed |
|---|---|---|---|
| C-1.tex | 25 | 23 | 6 |
| C-2.tex | 23 | 23 | 2 |
| C-3.tex | 27 | 26 | 2 |
| C-4.tex | 26 | 25 | 3 |
| C-5.tex | 23 | 23 | 0 |
| C-6.tex | 25 | 24 | 2 |
| C-7.tex | 28 | 28 | 4 |
| C-8.tex | 19 | 19 | 2 |
| C-9.tex | 18 | 17 | 2 |
| C-10.tex | 22 | 21 | 3 |
| C-11.tex | 29 | 27 | 5 |
| C-12.tex | 24 | 21 | 4 |
| C-13.tex | 14 | 14 | 1 |
| C-14.tex | 24 | 23 | 1 |
| C-15.tex | 30 | 29 | 2 |
| C-16.tex | 19 | 19 | 0 |
| C-17.tex | 39 | 38 | 4 |
| C-18.tex | 29 | 29 | 3 |
| C-19.tex | 17 | 16 | 3 |
| C-20.tex | 34 | 35 | 6 |
| **Total** | **495** | **480** | **55** |

The ranker barely moves, as in the first pass: most of what it flags are equation appositions and pronouns with one candidate, and I kept those. The C-20 count rises by one because "both references" (which picks from one coordinated noun phrase in the same sentence) replaces "theirs".

## Fifteen instructive changes

| file:line | before | after | failure fixed |
|---|---|---|---|
| C-1:20 | "…and their second moments diverge. The expansion then fails: their corrections are of order 1/t, and they are set by the values of w far from the origin, not by its curvature at the origin." | "…The expansion then fails. For the Lorentzian and the golden-rule function the correction is of order 1/t, and it is set by the values of w far from the origin, not by the curvature of w at the origin." | *their*: the nearest plural is "second moments"; the intended antecedent, the two functions, is the subject of the sentence before; *its*: w or the correction |
| C-1:40 | "The first term uses …. In the other two, w(ξ) − w(0) = …" | "In the second and third terms, …" | *the other two* picks from three terms of a display, not from a coordinated noun phrase |
| C-3:17 | "For instance, ∫… = … and ∫… = …. With eq:C.3-j1 they combine into" | "…the two integrals combine into" | *they*: the nearest plural noun is "Laplace transforms of powers", two sentences back |
| C-3:29 | "the direction average of (q·v)² is q²v²/3, and that of a quadratic form q·B·q is q² Tr B/3" | "…and the direction average of a quadratic form …" | *that of* without a coordinated antecedent |
| C-8:44 | "The complete elliptic integrals of the first and second kind are … [display]. The DLMF writes k …. Both integrals equal π/2 at s = 0." | "K(s) and E(s) both equal π/2 at s = 0." | *both* picks from a noun phrase two sentences and a display back |
| C-8:81 | "…counts the on-shell transitions, and its real part is their principal-value transform" | "…and the real part of the logarithm is the principal-value transform of the density of these transitions" | *their* binds to "transitions", but a transform is taken of a density, not of transitions; *its* had two candidates |
| C-10:70 | "…whose canonical representation through −ξ is the mirror image of that through ξ" | "…the mirror image of the canonical representation through ξ" | *that through*, the same failure as *that of* |
| C-11:3 | "The branching recursion builds the statistics of a whole tree from those of one step." | "…from the statistics of one step." | *those of* without a coordinated antecedent |
| C-11:101 | "A numerical solution … reproduces the offset to 10⁻⁶, and a simulation … the other two values to 1 %." | "…and a simulation … reproduces ⟨E_res⟩ and the Fano factor to 1 %." | *the other two values* picks from a list of three in the previous sentence; the gapped verb made a second parse |
| C-12:43 | "These are the complementary-slackness conditions, and they make the optimum checkable" | "The two equality conditions are the complementary-slackness conditions…" | *These* points to two propositions in two earlier sentences |
| C-13:35 | "…although its midpoint, 5.25, is below that of C, 6.5" | "…below the midpoint of C, 6.5" | *that of* |
| C-15:100 | "The relative size (Zα)² is that of each relativistic term." | "Each relativistic term has the relative size (Zα)²." | *that of*; the sentence also opened on a pointer back |
| C-17:76 | "The components (020) and (002) vanish, and by the glides … so does (200). They vanish for every function with the symmetry of the crystal" | "The components (020), (002) and (200) vanish for every function…" | *They*: the nearest plural is "the glides"; the intended set is split over two clauses |
| C-18:50 | "The group velocity … is not parallel to Q̂ either, and this deviation is the origin of the phonon focusing" | "…and the angle between the group velocity and Q̂ is the origin of the phonon focusing" | pointer to an object stated only negatively ("not parallel") |
| C-20:45 | "The real part grows without bound, …, so the overlap decays and the bath forgets which configuration it was prepared in. At T = 0 it decays only as a power" | "At T = 0 the overlap decays only as a power" | *it*: real part (subject of the previous main clause), overlap or bath; the intended one is none of the preferred candidates |

Other changes of the same kinds: C-1:47 "The second gives" → "The second part gives"; C-1:82 propositional *which proves* → "so the two transforms are indeed inverse to each other"; C-1:82 apposition "the step that solves" → "and this replacement solves"; C-1:94 "the convolution of the two densities" → "of the density of the uniform sphere with the Gaussian"; C-2:17 "The other terms" → "The terms with nonzero m"; C-2:55 "Either way" → "With broadening or with tetrahedra"; C-4:18 "the second is integrable" → "the second factor"; C-4:23 propositional "this is the complex conjugate statement" → "eq:C.4-SP is the complex conjugate of the statement with the upper sign"; C-4:74 "states how it approaches" → "how δ_Γ approaches" (*it*: δ_Γ or Eq. 2.4-split); C-6:36 "this statement is Wick's theorem" → "this sum over pairings"; C-6:59 "This is the operator through which…" → "Dark matter acts on a bound nucleus through e^{iqx}"; C-7:31 "this statement reads" → "the relation between the inverse and the Schur complement reads"; C-7:36 "Applied to the dielectric matrix it gives" → "…, eq:C.7-head gives"; C-7:61 "to one of size r" → "to an inversion of size r"; "apart from the rest" → "apart from the other elements"; C-9:40 "Both are solved" → "Both equations are solved"; C-9:50 "the integrand of the first" → "of the first form"; C-10:24 "these distributions" (two sentences and a heading back) → "two distributions with the same five moments"; C-10:41 "The other two are the roots" → "The other two roots are…"; C-11:46 "the spurious roots" (never introduced) → "the solutions other than the physical one"; C-11:62 "These hold" → "eq:C.11-mean,eq:C.11-second hold"; C-11:66 "This gives the renewal equation" → "The two cases give…"; C-12:12 "This is weak duality" → "eq:C.12-weak is weak duality"; C-12:25 "Such programs are called semi-infinite" → "The primal and the dual are therefore called semi-infinite programs"; C-12:43 "this is the statement proved above" → "the bound on the number of streams is…"; C-14:57 "is that of a Gaussian" → "is the interval of a Gaussian"; C-15:107 "bounds both" → "bounds the scalar correction and the spin-dependent term"; C-17:3 "Both start" → "Both sections start"; C-17:42 "the product of theirs" → "the product of the characters of its indices"; C-17:57 "all three counts" → "the two gyration counts and the count of rank-three invariants"; C-18:50 "the other two are quasi-transverse" → "the other two branches"; C-18:85 "never meets the others" → "never meets the two smaller eigenvalues"; C-19:9 "The second makes … the first then fixes" → "The second condition … the first condition"; C-19:14 "so such a magnetization" → "so a magnetization parallel to q"; C-19:56 "the other two separate" → "the second and third channels separate"; C-20:7 "The environment is" → "The environment, the bath, is" (the next paragraph and the subsection title use "bath", which was never introduced); C-20:22 "the normalization of eq:C.20-ohmic is theirs" → "…, and both references use the normalization of eq:C.20-ohmic" (*theirs* had no noun phrase as antecedent); C-20:54 "calls the approximation" → "calls this second-order approximation"; C-20:73 "the two satisfy" → "the two rates satisfy"; C-20:130 "the continuum profile and its mass" → "and the kink mass".

Kept on purpose: C-3:93 "Each is a multiple of the unit tensor" (its antecedent is the list "Examples are A, B or C" directly before); C-19:26 "Their normalization…" (antecedent "Berlin et al.", the subject of the previous sentence); C-13:3 "one of them but not from the other" (picks from "two materials" in the same sentence); C-5 and C-16 had no failure I could find.

## Checks

- `python3 tools/invariant.py 60cc72c tex/appC/C-*.tex`: 0 STOP, notes only (repeat counts; added `\cref` to existing labels eq:C.4-SP, eq:C.7-head, eq:C.11-mean, eq:C.11-second, eq:C.12-weak, eq:C.20-ohmic). Three STOPs from my first drafts were removed by rewording: a new `m\neq0` in C-2, a new `r\times r` in C-7 and a dropped `\Imag` in C-8.
- Lint with BANNED-TERMS.txt: the same hits as at 546ad31 in every file (pre-existing LONG-SENT); none from these edits.
- `tools/chapcheck.sh appC <scratch>`: exit 0, 0 undefined references, 0 multiply defined labels, 0 overfull hboxes > 5 pt. The first run showed one at C-9 l. 40 after "Both static equations"; the shorter "Both equations" removed it.
- No symbol unification, no new technical name except "bath" made explicit in C-20 (already the section's term).
