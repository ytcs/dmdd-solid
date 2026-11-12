# Binding round: appA-appB (Conventions and units; Notation)

Base commit: 60cc72c. Status: done. Files edited: tex/appA/A-1 to A-9, tex/appB/appB.tex, tex/appB/B-2.tex. B-3.tex was read; its one prose sentence is fine, so it is unchanged (it is also generated, by gen_B3.py). B-1*.tex not edited (generated); proposals below.

| File | Ranker before | Ranker after | Sentences changed |
|---|---|---|---|
| appA.tex | 0 | 0 | 0 |
| A-1.tex | 12 | 10 | 4 |
| A-2.tex | 11 | 11 | 5 |
| A-3.tex | 14 | 12 | 12 |
| A-4.tex | 14 | 13 | 9 |
| A-5.tex | 13 | 10 | 8 |
| A-6.tex | 18 | 13 | 11 |
| A-7.tex | 15 | 13 | 8 |
| A-8.tex | 15 | 14 | 10 |
| A-9.tex | 16 | 11 | 9 |
| appB.tex | 2 | 1 | 1 |
| B-2.tex | 2 | 2 | 3 |
| B-3.tex | 0 | 0 | 0 |
| **Total** | 132 | 110 | 80 |

Checks: `invariant.py 60cc72c` on all edited files: 0 STOP (notes only: repeat counts, and added `\cref` to existing labels eq:A.7-SL, eq:A.6-u, eq:A.7-eps, eq:A.8-eta). Lint: no new hits from the edits (one new WORDY and two LONG-SENT hits were fixed). chapcheck appA: exit 0, 0 undefined references, 0 multiply defined labels; 2 overfull hboxes > 5pt (A-6 l. 22, A-7 l. 64), both also present at the base commit (checked by compiling a copy with the base A-6 and A-7). appB cannot be compiled alone.

## 15 most instructive changes

| file:line | before | after | failure fixed |
|---|---|---|---|
| A-1:3 | "A dark-matter speed of 250.5 km/s is 8.356e-4, and the energy and momentum it carries at mass $m_\chi$ are …" | "… and a particle of mass $m_\chi$ at this speed carries the energy ½mv² and the momentum mv, both in eV" | *it* bound to "a speed", which carries nothing; "the same unit" had no argument |
| A-1:45 | "…= m²; it is the signature of most particle-physics texts, and App. C.9 uses it." | "Most particle-physics texts use the same signature, and so does App. C.9." | two *it*s, nearest candidate the mass-shell relation |
| A-2:8 | "the charge density operator is e times the sum of the nuclear densities weighted by Z minus the electron density" | "… e times the difference between the Z-weighted sum of the nuclear densities and the electron density" | coordination scope (e×sum − n_e vs e×(sum − n_e)) |
| A-3:24 | "The sign is fixed by the direction of q, which is the momentum the dark matter gives" | "The momentum transfer q is the momentum the dark matter gives to the target, and the direction of q fixes the sign of the spatial transform." | *which* attaching to "direction"; "the sign" of what |
| A-3:24 | "Shifting the integration variable to x = …, [equation]" | "The matrix element of the potential follows by shifting the integration variable to x = …:" | dangling modifier before a display |
| A-3:65 | "and the distinction only conjugates; for a Bloch function it does not." | "and the sign flip only conjugates the component; for a Bloch function this relation does not hold." | *it does not* pointing to a predicate |
| A-3:74 | "Both forms appear …; Ref. writes the second with …" | "The unreduced and the reduced form both appear …; Ref. writes the reduced form with …" | *both*, *the second* picking from an equation, not a coordinated NP |
| A-4:8 | "The component of the dark-matter velocity along q̂ that the delta function selects is …, and the speed integral depends … only through it" | "The energy-conserving delta function of a rate selects the component … of the dark-matter velocity along q̂, and … only through this component" | left-heavy subject with a relative clause; *the delta function* before introduction; *it* |
| A-4:12 | "…for phonons, magnons … at a few kelvin, it is not." | "… the ω < 0 part is kept." | *it is not* = predicate ellipsis |
| A-4:18 | "The two agree … Inversion symmetry gives this directly, since it maps … Time-reversal symmetry gives it too" | "The conventions agree … Inversion symmetry gives the same response at q and −q directly, since inversion maps … Time-reversal symmetry gives the same result" | *the two* with no pair; *this/it* standing for a proposition |
| A-4:18 | "with |ĩ⟩ and |f̃⟩ the time-reversed states, which have the same energies, and the sum over the mapped states is the same sum" | "where |ĩ⟩ and |f̃⟩ are the time-reversed states. They have the same energies as the original states, and the sum over them runs over the same states as the original sum" | *same* without argument; second name ("mapped states"); two-parse sentence |
| A-5:48 | "Every quantity that enters one amplitude, the vertex ρ, the e–ph vertex g … and any tensor …, is therefore computed in one gauge" | "Every quantity that enters one amplitude is therefore computed in one gauge, with one set of gauge matrices U(k): the vertex ρ, …" | subject of ~30 words with an apposition list |
| A-6:65 | "the reduction of the zero-phonon weight of a momentum transfer q to nucleus κ by the factor e^{-2W}" | "the factor e^{-2W} that reduces the zero-phonon weight when nucleus κ takes up a momentum transfer q" | chain of four prepositional phrases |
| A-6:70 | "The two objects share B and appear next to the same double commutator, that of the first-moment sum rule … the elastic share of the scattering weight, whose mean energy the sum rule fixes" | "The Allen–Heine vertex and the Debye–Waller factor share B, and both appear, in different roles, next to the double commutator of the first-moment sum rule … and the sum rule fixes the mean energy of the scattering weight at the free recoil energy" | *the two objects* from two sentences back; *that of*; *whose* with two candidates (share vs weight) |
| A-9:32 | "…the nuclear cross-section at small q follows from it. It is σ_N = …" | "…follows from σ_p as σ_N = … For unequal proton and neutron couplings, A² → …" | *It* with two candidates (σ_p, σ_N) |

Other changes, briefly: A-2 "the two agree" → "the two prefactors agree"; "the factor 1/e²" given its source (\cref{eq:A.7-SL}); A-5 "its plane-wave coefficients" → "the plane-wave coefficients u_n(k+G)"; "does not have this protection" → "the squared modulus of a second-order amplitude is gauge independent only under a condition"; A-6 "by eq this maps Q to −Q" → "the exchange amounts to mapping Q to −Q"; "It must equal" → "The Hermitian conjugate must equal"; A-7 "Both carry 1/V" → "R_ab and S_ab both carry"; "The proper part gives the absorptive part" → "The Coulomb-proper response gives the absorptive part of the dielectric function"; "this factor" → "the spin factor"; "The inverse matrix, ε_mac and L are [two equations]" → "ε_mac and L follow from the inverse matrix" (the list named three objects for two equations); A-8 "Papers that quote v_E mean one or the other" → "mean either the annual mean of |v_E(t)| or |v_⊙|" (nearest coordinated pair; lead please confirm this is the intended pair); "the difference is treated in the same way" → "this difference is also counted in the uncertainty of the halo"; A-9 "A change of either sign" → "Reversing either the sign of the mixing term or the sign of the photon coupling"; "The spin average is part of this definition" (pointer two paragraphs back) → "… of the definition of σ̄_e in Ref. [Eq. (3.8)]"; A-8 "an interaction through the electron density with transform Ṽ" → "an interaction with potential transform Ṽ that couples to the electron density"; "which a fixed detector does not" → "and a fixed detector does not sample them equally"; "the correction is below 1e-5" → "the correction from ω² in the propagator"; "which is the meaning of the reference cross-section" → "so for a heavy mediator σ̄_e is the total cross-section of free elastic scattering"; B-2 "in one … in the other" across sentences → explicit "In dark-matter papers … in condensed-matter papers …"; the 25-word four-item subject of the closing sentence moved after the verb; appB.tex "the conventions in which they differ" → "… in which these papers and textbooks differ", with App. A made the subject.

## Proposed fixes for generated files (B-1*.tex; for gen_B1.py / split_B1.py)

| Location | Current | Proposed | Failure |
|---|---|---|---|
| B-1 intro (all volumes) | "Each symbol is listed once, under the chapter or appendix in which it first appears; the last column gives that section." | "Each symbol is listed once, under the chapter or appendix of its first use; the last column gives the section of its first use." | *that section*: no section introduced (chapter or appendix was) |
| B-1-volN intro | "a symbol first used in another volume is listed there" | "a symbol first used in another volume is listed in the list of symbols of that volume" | *there* with no place noun |
| B-1 cell ϑ_k, ϑ_X | "ϑ_X that of the many-body approximation" | "ϑ_X the nuisance parameter of the many-body approximation" | *that of* |
| B-1 cell ΔS_k, δ_X | "δ_X that of the many-body approximation" | "δ_X the fractional size for the many-body approximation" | *that of* |
| B-1 cell n_2D … | "Areal density; that of the heavy band" | "Areal density; areal density of the heavy band" | *that of* |
| B-1 cell z_qp | "z_qp(n,k) that of the one-electron state nk" | "z_qp(n,k) the residue of the one-electron state nk" | *that of* |

The symbol table (about 33,000 words of glossary cells) was screened with a pronoun grep, not read cell by cell; the cells are telegraphic noun phrases and the hits above are the clear cases.
