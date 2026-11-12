# Binding round: unit front-ch01

Files: tex/front/conventions.tex, tex/front/plan.tex, tex/ch01/ch01.tex, s1-1 to s1-5. Base for invariant.py: 60cc72c.
Every paragraph was read whole, including captions, key-result and Limit Check boxes, worked examples, table prose and the Summary.

## Per file

| File | Ranker flags before | after | Sentences changed |
|---|---|---|---|
| front/conventions.tex | 9 | 9 | 10 |
| front/plan.tex | 4 | 3 | 2 |
| ch01/ch01.tex | 4 | 4 | 2 |
| ch01/s1-1.tex | 34 | 35 | 31 |
| ch01/s1-2.tex | 74 | 71 | 46 |
| ch01/s1-3.tex | 92 | 81 | 52 |
| ch01/s1-4.tex | 65 | 62 | 30 |
| ch01/s1-5.tex | 87 | 80 | 28 |
| **Total** | **369** | **345** | **201** |

The ranker count changes little: many of the fixes added a named noun phrase, which lengthens the sentence, and many of its flags (long equations, captions) are not failures.

Checks: invariant.py 60cc72c on all eight files reports 0 STOP (notes only: repeated items, and added `\cref` to eq:1.2-galilean and eq:1.3-edge). Lint: no new hits from these edits (the three long sentences the edits created were split). chapcheck ch01: exit 0, 0 undefined references, 0 multiply defined labels. The 2 overfull hboxes are in untouched text (the s1-2 L7 density range and tab:1-shm).

## Interpretations a reviewer should check
- s1-1 L14: "the coupling between the two" → "the electron--phonon coupling". "The two" had three candidates (crystal, electrons, lattice). The rewrite reads it as electrons and lattice vibrations and uses the field's term.
- s1-3 L202: "Both factors are fixed by the most uncertain parts of the halo model" → "The prefactor and the quadratic power of $\delta$ are both fixed by…". "Both factors" had no clear pair. The rewrite reads the pair from the next clause ("a smoother truncation would raise the power of $\delta$").
- conventions L5: "the ratio of the two" → "the ratio between the formula and the fuller result". No direction is stated, as in the original.
- s1-4 L34: "…in scattering $\omega \le qv$ with $v \lesssim 3\times10^{-3}$, which keeps the correction below $10^{-5}$" → "Since $\omega \le qv$ in scattering and $v \lesssim 3\times10^{-3}$, the $-\omega^2$ correction stays below $10^{-5}$ relative to $q^2$". The qualifier "relative to $q^2$" is added; it is correct because $\omega^2/q^2 \le v^2$.
- s1-2 L21: "We take the speed of the local standard of rest, the circular orbit at the Sun's radius, $v_0=…$" → "We take $v_0$ to be the speed of the local standard of rest, which moves on the circular orbit at the Sun's radius: …".

## Fifteen instructive changes

| file:line | Before | After | Failure fixed |
|---|---|---|---|
| s1-1:14 | "a reference cross-section $\sigmae$ that sets the strength, a form factor $\FDM(q)$ that carries the momentum dependence and the reduced mass $\mu_{\chi e}$…" | "with the reduced mass $\mu_{\chi e}$ of the dark matter and the electron, a reference cross-section $\sigmae$ that sets the strength, and a form factor $\FDM(q)$ that carries the momentum dependence" | Coordination garden path ("carries the momentum dependence and the reduced mass") |
| s1-1:16 | "shakes off an electron, which takes the joint response of electrons and lattice" | "shakes off an electron, and the Migdal rate needs the joint response…" | *which* bound to the nearest noun (electron), not to the process |
| s1-1:16 | "An electron excited across an indirect gap, where the highest filled … differ in crystal momentum, needs a phonon to supply the missing momentum, a second-order process" | "At an indirect gap the highest filled and the lowest empty electron states differ in crystal momentum. An electron excited across an indirect gap needs a phonon to supply this difference in crystal momentum, and the excitation is then a second-order process" | Left-heavy subject; *missing* without arguments; apposition to a clause |
| s1-1:12 | "a limit can be recast … by weighting it with the new coupling, without computing the solid again" | "…by weighting $S$ with the new coupling, without computing the response of the solid again" | *it* with two candidates (limit, $S$) |
| s1-1:20 | "where the visible mass alone would make it fall as $r^{-1/2}$" | "…would make $v_{\mathrm{c}}$ fall…" | *it* with two candidates (speed, disk) |
| conventions:5 | "The horizontal axis carries the controlling parameter, the variable along which the relative difference of the two runs … The leading correction, the first term of that difference…" | "The horizontal axis carries the controlling parameter: along this axis the relative difference between the formula and the fuller result runs … The leading correction is the first term of this relative difference…" | Defining appositions; *the two*; relational noun without arguments |
| s1-2:14 | "a self-gravitating gas with density … at galactocentric radius $r$, which encloses a mass… Its particles have…" | "…at galactocentric radius $r$. This density profile encloses a mass that grows linearly with $r$… The halo particles have…" | *which* with four candidates; *Its* with several candidates |
| s1-2:119 | "Substituting $y = v - v_{\mathrm{E}}$ in the first exponential …, the two cancel on…" | "After the substitutions … in the second, the two Gaussians cancel on…" | Dangling modifier; bare *the two* |
| s1-2:110 | "sees a rate suppressed by more than two orders of magnitude, and one that depends on $v_{\mathrm{esc}}$…, the most uncertain parts of the model" | "…, and this rate depends on $v_{\mathrm{esc}}$ and on the exact shape of the cut, which are the most uncertain parts of the model" | Elliptical *one*, which reads as a second object of "sees" |
| s1-2:170 | "Its meridian is the half-plane bounded by the rotation axis that contains the local vertical" | "The meridian of the laboratory is the half-plane that is bounded by the rotation axis and contains the local vertical" | Relative-clause attachment (axis or half-plane) |
| s1-3:39 | "Some papers take $\vect{q}$ as the momentum gained by the dark matter instead, a difference that matters for a crystal…" | "…instead. The choice of sign matters for a crystal…" | Apposition pointing to a proposition |
| s1-3:208 | "the rate is the product of $\eta$, quadratic in this window, and of the phase space of pairs … that fit inside it, which shrinks as a further power of the window. How fast that phase space shrinks…" | "the rate is the product of two factors: $\eta$, which is quadratic in the speed window $v_{\mathrm{max}} - \vmin$, and the phase space of the pairs … that fit inside this window. The phase space shrinks as a further power of the window, and how fast it shrinks…" | *this window* with no antecedent; *which* with three candidates |
| s1-4:36 | "constrained by accelerator, stellar and cosmological data, which bound the products … that enter rates and the couplings to ordinary matter separately" | "Accelerator, stellar and cosmological data constrain each mediator: they bound the products … that enter rates, and they bound the couplings to ordinary matter separately" | Coordination-scope ambiguity |
| s1-4:61 | "the first Born approximation yields the free elastic cross-section … It is that cross-section with $\tilde V$ frozen at $q_0$" | "The reference cross-section $\sigmae$ is this free cross-section with $\tilde V$ frozen at $q_0$" | *It* meant to be $\sigmae$, two sentences back, with three nearer candidates |
| s1-5:119 | "It is not the probability that $\sigmae$ lies below the limit, which would require a prior…" | "The confidence level is not the probability that $\sigmae$ lies below the limit; that probability would require a prior…" | *which* bound to the nearest noun (limit) |

Other recurring fixes: *such X* named (such a vector → a reciprocal-lattice vector; such particles → dark-matter particles of 100 MeV; such a target → a target whose response depends only on $q$). Bare *this* or *that* for a proposition replaced by a noun (this requirement, this derivative, this screening). Ellipses in "but $\eta$ … by factors" filled in. *Both* given its pair. Dangling gerunds ("Combining with", "interpolating", "Expanding the square") rewritten with an agent. Left-heavy subjects in s1-3 L114, s1-4 L110 and s1-5 L42/L66 moved after the verb.

## Not resolved
- s1-3 L161: "The factor $1/qv$ is the derivative of the argument of the delta function": the binding is now fixed, but the statement itself is loose (the factor is the inverse modulus of that derivative). This is a content point, outside this round, and was left unchanged.
