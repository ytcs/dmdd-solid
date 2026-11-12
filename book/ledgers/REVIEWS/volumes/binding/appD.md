# Binding round: appD (Long derivations)

Base commit: 60cc72c. Status: done. invariant.py: 0 STOP on all 22 files (notes only: repeat counts of existing items, added \cref to existing labels). chapcheck appD: exit 0, 0 undefined references, 0 multiply defined labels (2 overfull hboxes: one at the inline formula $c_i(t) = \dots$ that opens a D-3 paragraph, where later sentences of the paragraph were edited but the first line was not; one at an unresolved citation in an unedited D-11 paragraph. Both are probably pre-existing, but the base was not compiled for comparison.). Lint: no new hits except LONG-SENT reports in D-6, D-8, D-11, D-24 that join a sentence ending in "gives" to the text after its display (the prose sentences are short); one real new long sentence in D-9 was split.

| File | Ranker before | Ranker after | Sentences changed |
|---|---|---|---|
| D-1.tex | 5 | 6 | 6 |
| D-2.tex | 27 | 22 | 22 |
| D-3.tex | 21 | 15 | 16 |
| D-6.tex | 12 | 14 | 16 |
| D-7.tex | 20 | 14 | 16 |
| D-8.tex | 12 | 11 | 6 |
| D-9.tex | 26 | 21 | 16 |
| D-10.tex | 23 | 15 | 15 |
| D-11.tex | 52 | 42 | 35 |
| D-12.tex | 48 | 41 | 28 |
| D-13.tex | 26 | 23 | 13 |
| D-14.tex | 5 | 4 | 3 |
| D-16.tex | 21 | 16 | 12 |
| D-20.tex | 14 | 10 | 12 |
| D-21.tex | 16 | 14 | 9 |
| D-22.tex | 21 | 19 | 12 |
| D-23.tex | 15 | 14 | 8 |
| D-24.tex | 29 | 26 | 18 |
| D-25.tex | 21 | 18 | 16 |
| D-26.tex | 26 | 18 | 22 |
| D-27.tex | 54 | 48 | 16 |
| D-28.tex | 60 | 57 | 30 |

Totals: ranker 554 before, 468 after; 347 sentences changed in about 27,000 words of prose (about 13 per 1000 words).

## Most instructive changes

| file:line | before | after | failure fixed |
|---|---|---|---|
| D-11:19 | "For $0<\tau<\beta$, inserting both into \cref{eq:4.7-Gtau} and using ...," [display] | "... inserting the Boltzmann factor and $c_{\vect{k}}(\tau)$ into \cref{eq:4.7-Gtau} and using ... gives" | *both* picking from the previous sentence; dangling modifier before a display |
| D-11:34 | "tends to an eigenstate of $H_\mu$. It is the ground state when that state is nondegenerate and is reached ... which we assume." | "We assume that the ground state is nondegenerate and is reached ...; the eigenstate is then the ground state." | *it*, *that state* and *which* for three referents |
| D-11:70 | "joins the two external operators to some set of $m$ of the $n$ factors $H_{\mathrm{int}}$, the connected part, and joins the remaining $n-m$ factors only among themselves, the vacuum part" | "splits the $n$ factors into two parts. The connected part consists of the $m$ factors that the pairing joins to the two external operators; the vacuum part consists of the remaining $n-m$ factors, which the pairing joins only among themselves." | genitive chain; appositions naming sets |
| D-11:90 | "Relabeling the $n$ ... factors ..., and exchanging the two ends of any interaction line, which is a relabeling ... under which $v_{\mathrm{C}}$ is unchanged, maps one pairing onto another" | "Two operations map one pairing onto another with the same value: relabeling ..., and exchanging the two ends of any interaction line. The exchange is a relabeling ..., under which $v_{\mathrm{C}}$ is unchanged." | left-heavy gerund subject with a nested relative |
| D-11:123 | "the polarization lags behind it, and a second electron ... is attracted to it. For phonons this is the attraction behind superconductivity" | "the polarization lags behind the electron, and a second electron ... is attracted to the polarization. For phonons the same attraction is behind superconductivity" | two *it* with different antecedents; *this* for a proposition |
| D-12:36 | "One of them is on the electron line, which enters at $c^\dagger_{m'}$ and leaves at $c_m$, and requires $a = m$" | "One bilinear is on the electron line, which enters ... and leaves ...; this bilinear requires $a = m$" | coordination scope: *requires* attached to the line or to the bilinear |
| D-12:52 | "on one side of the line ... and the line is $W^{\mathrm{scr}}$ at the bosonic difference ..." | "on one side of the interaction line ... and the interaction line is $W^{\mathrm{scr}}$ at the bosonic frequency ..." | one word, two referents (electron line, interaction line); relational *difference* |
| D-3:51 | "exceeds $\ee^{-1}$ by $0.0023$, 0.4% of the depletion: this is the deviation from $1-\ee^{-\varGamma_it}$ that the exact solution of that model shows" | "... or 0.4% of the depletion. The exact solution for the flat continuum of \cref{we:2-continuum} deviates from the depletion $1-\ee^{-\varGamma_it}$ by this amount" | *this* for a proposition; *that model*; relational *deviation* |
| D-3:79 | "It also evaluates ... Strictly, the resolvent gives them at the energy $E_i$ ... The two agree when ..., which always holds near resonance" | "The derivation also evaluates ... at the energy $E_m$ of $m$, whereas strictly the resolvent gives them at $E_i$ ... The values at $E_m$ and at $E_i$ agree when ..., a condition that always holds near resonance" | chain of pointer-led sentences; *the two* |
| D-9:63 | "so a nonzero density, and with it the nonzero coherences $\delta\varrho_{\vect{k}} = \dots$, exist exactly where the denominator vanishes" | "so a nonzero density exists exactly where the denominator vanishes. The nonzero density comes with the nonzero coherences $\delta\varrho_{\vect{k}} = \dots$." | subject interrupted by a formula-length insertion |
| D-9:63 | "a solution of the equation of motion without a field that grows as" | "a field-free solution of the equation of motion that grows as" | attachment ambiguity (field that grows) |
| D-23:46 | "the part $\delta U$ of the donor potential that the envelope equation leaves out, which differs from $-\alpha/\varepsilon_0r$ only within about a lattice constant" | "... leaves out. The donor potential differs from $-\alpha/\varepsilon_0r$ only within about a lattice constant" | *which* with two candidates (and the intended one is the donor potential, not $\delta U$) |
| D-24:43 | "A massive vector mediator exchanged between two currents adds the spatial components to the potential" | "The exchange of a massive vector mediator between two currents adds the spatial components of the currents to the potential" | reduced relative read as a main verb |
| D-28:75 | "Any two definitions of the label that agree at $g=0$ and are continuous in $g$, the phonon number ..., a Schrieffer--Wolff number, the number of phonons ..., assign $|\tilde f\rangle$ to $\mathcal{P}_+$" | "Consider any two definitions of the label that agree at $g=0$ and are continuous in $g$, such as .... Both assign $|\tilde f\rangle$ to $\mathcal{P}_+$, and they differ by at most this weight." | left-heavy subject with relative clause and appositive list |
| D-7:39 | "Since $\bar R$ is a response of the electrons to a potential, causal and with a local Hamiltonian," | "Since $\bar R$ is a causal response to a potential, and the electrons it describes have a local Hamiltonian," | coordination scope of an appended modifier pair |

## Notes
- A second pass over my own new sentences fixed splits that opened on a pointer (D-16, D-21, D-27, D-28), a new reduced relative in D-7, a robotic repetition in D-8, a weakened identity in D-26 ("as in the middle regime" restored to "in the middle regime") and a third name for $K^{\mathrm{x}}$ in D-12.
- D-1 and D-6 went up in the ranker (5 to 6, 12 to 14). The newly flagged sentences are rewrites that now name the object ("the speed distribution", "the commutator ..."). I read them and kept them, since each pointer has one candidate.
- D-24:19: "this is $\vect{q}\cdot\vect{v} = q^2/2\mu_{\chi T}$" became "the elastic condition is ...". Writing "\cref{eq:D.24-free} is" there would have been wrong for $\Delta_\chi \ne 0$.
- D-13:3 "force constants of the same electronic order" became "of the same order as the electronic force constants", which is the reading the next sentence's ratio $(M/m_e)^{1/2}$ assumes.
- Not resolved: D-24:97 "This is the order-$v^2$ term of the scalar bilinear" was left as written. The precise antecedent is the expression $(1/8m_e^2)(-K^2)$, and repeating it as a standalone formula would be a new math item for invariant.py.
