# Binding round: appC (Mathematical tools)

Base commit: 60cc72c. Status: done. Every paragraph of C-1 to C-20 read whole, including the key-result boxes and the worked example in C-17 (appC has no captions, footnotes or prose table cells; appC.tex holds only \input lines). Line numbers below refer to the edited files.

Checks: `tools/invariant.py 60cc72c tex/appC/*.tex` gives 0 STOP lines (notes only: repeat counts, and added `\cref` to existing labels). Lint: no hit introduced by these edits; three pre-existing LONG-SENT hits went away (C-5, C-6, C-7). `chapcheck.sh appC` exits 0, with 0 undefined references and 0 multiply defined labels.

| File | Ranker before | Ranker after | Sentences changed |
|---|---|---|---|
| C-1.tex | 32 | 25 | 21 |
| C-2.tex | 24 | 23 | 12 |
| C-3.tex | 28 | 27 | 9 |
| C-4.tex | 28 | 26 | 15 |
| C-5.tex | 25 | 23 | 13 |
| C-6.tex | 25 | 25 | 9 |
| C-7.tex | 31 | 28 | 11 |
| C-8.tex | 21 | 19 | 11 |
| C-9.tex | 23 | 18 | 8 |
| C-10.tex | 24 | 22 | 11 |
| C-11.tex | 30 | 29 | 11 |
| C-12.tex | 26 | 23 | 10 |
| C-13.tex | 17 | 15 | 5 |
| C-14.tex | 25 | 24 | 5 |
| C-15.tex | 31 | 30 | 8 |
| C-16.tex | 22 | 19 | 10 |
| C-17.tex | 42 | 41 | 9 |
| C-18.tex | 35 | 29 | 9 |
| C-19.tex | 19 | 17 | 8 |
| C-20.tex | 35 | 34 | 10 |
| **Total** | **543** | **497** | **205** |

The ranker count changes little because most of its hits in appC are appositions that name an equation ("the Sokhotski–Plemelj formula", "the Rayleigh quotient") and pronouns with one candidate. I read these and kept them. The changes were mostly misses that the ranker does not flag: propositional *which* and *this*, *it* with several candidates across an equation, and dangling participles before a display.

## Fifteen instructive changes

| file:line | before | after | failure fixed |
|---|---|---|---|
| C-1:33 | "…where the last integral is the Dirichlet integral with u → 2u. This is the integral quoted in Sect. 2.1. The central lobe … holds 90.3 % of it." | "\Cref{eq:C.1-sinsq} is the integral quoted in Sect. 2.1. The central lobe of the integrand, \|u\| < π, holds 90.3 % of the integral." | *This* binds first to the nearest noun phrase, the Dirichlet integral, which is the wrong integral |
| C-1:20 | "Expanding w(u/t) in powers of u/t, an even f with a finite second moment gives w(0) + …, a correction of relative order 1/t²." | "For an even f with a finite second moment, expanding w(u/t) in powers of u/t gives w(0) + …, and the correction to w(0) is of relative order 1/t²." | dangling participle; an apposition attached to the whole expression |
| C-1:52 | "This is why Sect. 2.1 reads the rate off the probability, whose kernel is positive, as well as off its derivative." | "Because of this weaker convergence, Sect. 2.1 reads the rate off the probability, whose kernel is positive, as well as off the time derivative of the probability." | *this* stands for a proposition; *its* has three candidates (rate, probability, kernel) |
| C-2:51 | "The error of a grid is the set of Fourier components of the integrand at distances equal to the size of the fictitious block. It is the crystal version…" | "The error of the grid average consists of the Fourier components F_R at the nonzero lattice vectors of the fictitious block. This error is the crystal version…" | four-phrase prepositional chain; "the integrand" used without introduction |
| C-2:55 | "A Gaussian broadening is preferred to a Lorentzian of the same width, because its error is of order σ²…" | "…of the same width. A Gaussian gives an error of order σ² …, while the slow tails of a Lorentzian give an error of order σ…" | *its* has two candidates (Gaussian, Lorentzian) |
| C-3:83 | "A response that is even in q … is invariant under q̂ → −q̂ all the same" | "…is invariant under q̂ → −q̂ even though T_d lacks inversion" | *all the same* points to the preceding proposition |
| C-4:65 | "…the product of a denominator and its conjugate, whose poles lie on opposite sides of the axis and pinch it as Γ → 0. Its limit does not exist" | "…and its complex conjugate. The two factors have poles on opposite sides of the axis, and the poles pinch the axis as Γ → 0. The limit of the modulus squared does not exist" | *whose*, *it* and *Its* each have several candidates |
| C-5:12 | "Inserted with z = ω + i0⁺, every pole lies below the axis of real ω" | "With z = ω + i0⁺, every pole of the Lehmann form lies below the axis of real ω" | dangling participle; "every pole" without its owner |
| C-7:25 | "Multiplying the first two factors gives (M/D B; 0 D) with M/D the middle upper block … The middle factor contains the Schur complement of D, M/D ≡ A − BD⁻¹C." | The two sentences reordered: the Schur-complement definition comes first, and "which returns M" becomes "so that the product is M again" | symbol used one sentence before its definition; propositional *which* |
| C-7:43 | "To second order in the coupling, …, it is the level shift Σ\|H'\|²/(E_i − E_f)" | "…, the term H_PQ(E − H_QQ)⁻¹H_QP is the level shift…" | *it* has three candidates (the bracket, the equation, the effective Hamiltonian) |
| C-10:101 | "It is tighter only at intermediate ξ, where a node … lies below zero: for silicon at q = 100 keV it lies below ϱ_MK by at most 6.8 %" | "…: for silicon at q = 100 keV the second entry lies below ϱ_MK by at most 6.8 %" | the second *it* rebinds to "a node", the nearest singular noun |
| C-11:24 | "Inserting both into eq.(var) and dividing by f⟨N⟩, the Fano factor of the kept items is" | "Inserting ⟨N_k⟩ and G''_{N_k}(1) into eq.(var) and dividing by f⟨N⟩ gives the Fano factor of the kept items," | *both* picks from the previous sentence; dangling participle |
| C-12:3 | "A limit that should hold for every velocity distribution, the problem of Sect. 21.2, is then the largest value … That is a linear program…" | "Sect. 21.2 needs a limit that should hold for every velocity distribution, and that limit is then the largest value … The maximization is a linear program…" | left-heavy subject with an apposition; *That* stands for a proposition |
| C-16:11 | "A harmonic oscillator of frequency ω_k whose classical amplitude a is normalized so that its energy is ω_k\|a\|² matches this with c = a/(2Vω_k)^{1/2}." | "The sum matches the energy of a set of harmonic oscillators of frequencies ω_k if c = a/(2Vω_k)^{1/2}, where the classical amplitude a of each oscillator is normalized so that its energy is ω_k\|a\|²." | 17-word subject containing a relative clause; *this* without an antecedent noun |
| C-20:119 | "The continuum kink has the same energy wherever its center is. The discrete chain does not, and the difference is the Peierls–Nabarro barrier…" | "…In the discrete chain the energy of a kink depends on where its center is, and a kink must cross the resulting Peierls–Nabarro barrier to move by one spacing." | ellipsis stated only negatively; relational noun *difference* without its arguments |

## Notes for the reviewer
- Unresolved, C-4:76: "A width that depends on energy, Γ(x), keeps the delta limit of eq.(SP) at its value at x₀". I fixed the two later pronouns (now "provided Γ_w(x) varies little …; the slope of Γ_w(x) enters …"). I left "its value at x₀" as it was. It can mean the width at x₀ or the delta term ∓iπw(x₀), and choosing one would change the claim. The author should decide.
- C-12:61. "that leakage" is now "the resulting leakage", which uses the term of Sect. 21.2 (subsection "Grids, certificates and leakage"). The cross-reference target is unchanged.
- No symbol unification, and no new name for a technical object. Where I gave an object a name, I reused the one the file already uses ("golden-rule function", "image terms", "the Dirichlet integral", "the rule for a delta function of a function").
