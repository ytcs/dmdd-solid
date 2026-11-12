# Binding round: independent review of block vol3b (ch23-ch25)

Reviewer: independent hostile review (BINDING-REVIEW.md). Files: tex/ch23/{ch23,D-4,D-5,E-1,E-3}.tex, tex/ch24/{ch24,s3-5,E-2}.tex, tex/ch25/{ch25,s5-4,E-4,E-8}.tex. None is marked generated: the hits on "generated" are physics prose. Base 60cc72c. I read every changed sentence against its base sentence (word diff) and read every file whole. I opened the editor log (ch23-ch25.md) only after forming my verdicts, and used it to check its stated readings.

## Verdict

The denominators are the editor's per-file "sentences changed" counts, which count a split as two sentences. Every one of these sentences was read.

| File | Changed sentences checked | Accepted | Fixed | Reverted |
|---|---|---|---|---|
| ch23.tex | 4 | 3 | 1 | 0 |
| D-4.tex | 30 | 28 | 2 | 0 |
| D-5.tex | 22 | 22 | 0 | 0 |
| E-1.tex | 54 | 51 | 2 | 1 |
| E-3.tex | 42 | 41 | 1 | 0 |
| ch24.tex | 5 | 5 | 0 | 0 |
| s3-5.tex | 58 | 58 | 0 | 0 |
| E-2.tex | 33 | 32 | 1 | 0 |
| ch25.tex | 6 | 6 | 0 | 0 |
| s5-4.tex | 40 | 39 | 1 | 0 |
| E-4.tex | 31 | 29 | 2 | 0 |
| E-8.tex | 24 | 24 | 0 | 0 |
| **Total** | **349** | **338** | **10** | **1** |

The edit is faithful. I found no lost qualifier, number, validity condition or citation, and no physics slip. The settled name for $\Sigma_{\mathrm x}$, "the Fock term", was applied in the sentences the editor touched. It was not applied in two untouched ones (D-4:68, E-3:82), and one untouched sentence used "bare exchange" for $v_{\mathrm C}$ (D-4:86). I fixed all three, so in ch23 "bare exchange" now survives only as the explicit gloss in E-3:30 ("the bare exchange $\Sigma_{\mathrm x}$, which is the Fock term of Sect. 3.4"). Every other remaining "exchange term" refers to the energy term of $E[\Phi_0]$, and "exchange energy" refers only to $E_{\mathrm x}$.

## Fixes and reverts of editor text

| file:line | editor text | my text | reason |
|---|---|---|---|
| D-4:7 | The Hamiltonian has a one-body part, $h = …$ summed over the electrons, with $U_1$ the attraction of the nuclei, and the Coulomb pair potential $U_2…$, summed over pairs. | The Hamiltonian is the one-body part $h = …$, summed over the electrons, plus the Coulomb pair potential $U_2…$, summed over pairs; $U_1$ is the attraction of the nuclei. | Coordination scope. "and the Coulomb pair potential" reads as a second complement of "with" (U_1 the attraction …, and the pair potential). The base's "plus" was lost. |
| D-4:19 | A Hartree--Fock determinant makes $E[\Phi_0]$ stationary, | A Hartree--Fock determinant is one that makes $E[\Phi_0]$ stationary, | Fidelity. The base stated a definition ("is the one that"); the edit turned it into a property. |
| ch23.tex:16 | … give the silicon gap to about 0.1 eV of one another. The spread of about 0.1 eV among the three computed gaps and the error in the screening … | … give silicon gaps that agree to about 0.1 eV. The spread among the three gaps and the error in the screening … | Over-repair. The editor repeated "about 0.1 eV" in two consecutive sentences. |
| E-1:12 | and the cycle is iterated | and the loop is iterated (base wording) | Revert. "cycle" created a second name for the loop that E-1:111 calls "the self-consistency loop". |
| E-1:83 | The electronic dielectric constant $\varepsilon_\infty$ (Sect. 4.4), computed with DFPT at the PBE lattice constant, is an example. It is 14.36 … | An example is the electronic dielectric constant … at the PBE lattice constant. The computed $\varepsilon_\infty$ is 14.36 … | Left-heavy subject with a reduced relative. After the reorder, *It* would have had the PBE lattice constant as its nearest candidate. |
| E-1:95 | … Gaussians multiplied by Hermite polynomials. Their low moments vanish, … | … The low moments of these smearing functions vanish, … | The editor's split made *Their* bind to the nearest plural, the polynomials. The moments belong to the smearing functions. |
| E-3:61 | The ladder diagrams of the Bethe--Salpeter equation (Sect. 4.9), added to the polarizability of quasiparticle self-consistent $GW$, remove most of the overestimate of the gaps and the underestimate of $\varepsilon_\infty$ by that method. | Adding the ladder diagrams of the Bethe--Salpeter equation (Sect. 4.9) to the polarizability removes most of the gap overestimate and the $\varepsilon_\infty$ underestimate of quasiparticle self-consistent $GW$. | Left-heavy subject with a reduced relative. "by that method" was a pointer back. The following sentence ("With the ladder diagrams, … 1.08 eV") is kept separate, so the LONG-SENT hit the editor removed does not return. |
| E-2:3 | In the density vertex a pseudopotential that is excellent for total energies, bands and phonons can fail without any sign in those quantities. | A pseudopotential can be excellent for total energies, bands and phonons and still fail in the density vertex without any sign in those quantities. | Left-heavy subject that contains a relative clause. |
| s5-4:3 | … the second derivatives of the energy surface …: the first from finite differences of forces, the second from the linear response … | …: the supercell from finite differences of forces, the primitive cell from the linear response … | Garden path. "the second" follows "the second derivatives" and reads first as "the second derivative". |
| E-4:13 | … between different eigenstates, and the matrix elements of $\vect r$ between different eigenstates are well defined … | … between different eigenstates, and for $\vect r$ these matrix elements are well defined … | Robotic repetition of a long phrase in one sentence. |
| E-4:133 | and the $\vect k$ sum of these terms converges slowly | and the sum of these matrix elements and denominators over $\vect k$ converges slowly | "these terms" had no noun-phrase antecedent. The antecedent is "the velocity matrix elements and energy denominators". |

Editor changes I examined and accepted although they were close calls: s5-4:66 "With eq:5.4-Dwave inserted in eq:5.4-hess" (this keeps the base's direction of substitution); E-2:54 "reconstructed the vertex" (it matches s3-5:79 and s3-5:136); s3-5:33 (a long sentence, but it parses in one pass); D-4:42 (the exchange-hole apposition).

## Recall (paragraphs the editors did not change)

Sample: ch23, 20 paragraphs and 1255 words (ch23.tex:5; D-4:13,50,73,86,93; D-5:9,13,44,78; E-1:3,47,93,115,126,136; E-3:19,38,42,78). ch24, 17 paragraphs and 1349 words (s3-5:15,37,62,82,90,92,97,106,127,132,136,148; E-2:7,37,48,63,69). ch25, 33 paragraphs and 2743 words (s5-4:11,23,32,38,55,96,113,123,150; E-4:3,28,34,36,41,55,63,75,77,87,93,116,129,137,144; E-8:24,29,31,50,70,72,77,79,81). Every file was sampled, and E-1, E-3 and s3-5 were also checked against the ranker flags (`binding.py --summary`).

Misses in the sampled untouched paragraphs, all fixed:

| file:line | text | fix | failure |
|---|---|---|---|
| D-4:86 | the long range of the bare exchange, $v_{\mathrm C} \propto 1/k^2$ | the long range of the bare Coulomb interaction, $v_{\mathrm C}…$ | One name, two referents: E-3 uses "bare exchange" for $\Sigma_{\mathrm x}$. |
| s3-5:37 | … but asks one potential to describe a large part of the atom, and it transfers less well | … and the potential transfers less well | *it*: two candidates (a large $r_c$, one potential). |
| E-4:63 | the acoustic frequencies at $\Gamma$ before it should be small | … before the correction … | *it*: the candidates are the size, the correction and a diagnostic. |

Rates: **ch23 0.8, ch24 0.7, ch25 0.4 misses per 1000 words**. All three chapters are below 2, so none needs a second pass.

Misses in unchanged sentences inside paragraphs the editors changed (not counted in the rates above), all fixed:

| file:line | text | fix | failure |
|---|---|---|---|
| D-4:68 | the exchange term multiplies it by a number | the Fock term … | The settled name for $\Sigma_{\mathrm x}$. "Exchange term" is used in D-4 for the energy term. |
| E-1:81 | For an insulator these decay exponentially | these Fourier components decay | *these*: two candidates (components, superlattice vectors). |
| E-3:3 | The $GW$ self-energy …, with …, and the electron--electron lifetime from Im Σ are defined in Sect. 4.8. | \Cref{sec:4.8} defines the $GW$ self-energy …, with …, and the electron--electron lifetime from Im Σ. | Left-heavy subject of 18 words. |
| E-3:82 | The bare exchange $\Sigma_{\mathrm x}$ is a separate case | The Fock term $\Sigma_{\mathrm x}$ … | The settled name. |
| E-4:104 | In eq:E.4-drho these terms do not cancel | … the terms with $m$ occupied do not cancel | Plural pointer to the singular "the part with $m$ occupied". |
| E-8:42 | The convergence parameters are the number of time steps, which Ref. tracks through the change in the fitted constants, the supercell size, and the range … | The convergence parameters are the supercell size, the range of the force constants kept in the fit, and the number of time steps, which Ref. tracks through the change in the fitted constants. | Coordination scope: the relative clause appears to swallow the rest of the list. |
| ch25.tex:11 | which need the commutator with its nonlocal term | which need the commutator of the Hamiltonian with the position operator, nonlocal term included | *its*: there is no antecedent, and the commutator is not given its arguments. |

## Open items

OPEN.md lists no items for ch23-ch25.

Decisions on the editor's seven judgment calls:
1. Name of $\Sigma_{\mathrm x}$: "the Fock term" is confirmed and has now been completed in D-4:68 and E-3:82 (above). The one "Hartree--Fock exchange" in s3-4 stays, by the lead's decision.
2. ch23.tex:16 and E-3:87, "the spread": E-3:87 is accepted. ch23.tex:16 is rewritten (above).
3. E-1:83, "each weighted by the factor $1/(\varepsilon_c - \varepsilon_v)$": accepted. "Energy denominator" stays $\varepsilon_c - \varepsilon_v$ throughout E-3 and E-4.
4. E-1:145, introducing the overscreening: accepted. It matches E-4:50.
5. E-2:52, "the s and p channels": accepted. The order matches E-2:31.
6. s3-5:101, the split of the semicore sentence: accepted. The definition is unchanged.
7. ch25.tex:11, "of the measured renormalization … which remains": accepted. It matches E-8:88.

## Proposed erratum (for the errata review; not edited)

- **Location:** tex/ch23/D-4.tex:86, last sentence.
- **Old text:** "The screened exchange is the GW self-energy of \cref{sec:4.8}."
- **Proposed text:** "Replacing $v_{\mathrm{C}}$ by the screened interaction leads to the GW self-energy of \cref{sec:4.8}, of which the screened exchange is one part."
- **Reasoning:** E-3:30 defines the GW self-energy as a screened-exchange part plus a Coulomb-hole part, so within ch23 "screened exchange" names both the whole of Σ and one of its parts. The sentence states what a quantity is, so the change is a content correction and not only a wording fix.

## Checks

- `tools/invariant.py 60cc72c` on all 12 files: 0 files with a STOP.
- Lint: a two-sided diff of each file's output before and after my edits shows no new hits.
- `tools/chapcheck.sh ch23|ch24|ch25 /tmp/binding-review-vol3b`: exit 0 for each chapter, 0 undefined references and 0 multiply defined labels. ch25 has 5 overfull hboxes, the same count the editor found in the unedited ch25 (they sit at unresolved citations).
