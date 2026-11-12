# Binding round: independent review of block vol1a

Files: tex/front/conventions.tex, tex/front/plan.tex, tex/ch01/*.tex, tex/ch02/*.tex, tex/ch03/*.tex. Base: 60cc72c.
Method: I read the sentence-level diff of every file against the base (old and new sentence side by side), and I read each changed paragraph in the current file. I formed a verdict before I opened the editors' logs (front-ch01.md, ch02.md, ch03.md). I used the logs afterwards only to check their stated interpretations.

Sect. 2.4 (s2-4.tex): its diff against 60cc72c is empty, so it has no changes after the pilot review to check under Job 1. It was sampled for Job 2 (1,504 words, 0 misses).

## Verdict table (Job 1)

The count is of base sentences, split at `.` and `?` only, that do not survive verbatim. Six of these 692 are my own recall fixes, which leaves 686 that the editors changed.

| Chapter | Editor-changed sentences checked | Accepted | Fixed | Reverted |
|---|---|---|---|---|
| front (conventions, plan) | 14 | 14 | 0 | 0 |
| ch01 (ch01, s1-1 … s1-5) | 200 | 197 | 3 | 0 |
| ch02 (ch02, s2-1 … s2-5; s2-4 has no changes) | 212 | 206 | 5 | 1 |
| ch03 (ch03, s3-1 … s3-4) | 260 | 254 | 5 | 1 |
| **Total** | **686** | **671** | **13** | **2** |

On the whole the editors' work is faithful. I found no lost qualifier or changed number. The failures were these: one pointer that extends a physics error (s1-3), one sentence with a lost commitment (s3-2 "We use"), one name pair coined against an existing name (s1-3 "energy edge"/"edge in mass"), one changed object name inside a paragraph (s3-1 Hamiltonian), two over-repairs, and some new sentences that do not parse cleanly.

## Fixes and reverts

| file:line | editor text | my text | reason |
|---|---|---|---|
| ch03.tex:3 | "The effective potential is accurate enough to compute the bands and wavefunctions…" | "Density-functional theory is accurate enough to compute the bands and wavefunctions…" | Wrong subject: the description is what is accurate, not the potential. The base phrase modified "a problem of independent electrons" |
| s1-3:161 | "This derivative is the origin of the factor $1/v$" | "This factor is the origin of the factor $1/v$" | The editor bound the pointer to "derivative", and that extends the loose claim of the previous sentence. $1/v$ comes from the factor $1/qv$, not from the derivative $qv$ (see erratum E1) |
| s1-3:189 | "The energy edge and the mass edge are both reached" | "The edge in energy and the edge in mass are both reached" | New names coined. L204 calls the mass edge "The edge in mass", so the book now uses one form |
| s1-4:172 | "and the mediator couples $\chi_1$ only to $\chi_2$" | "and the mediator couples $\chi_1$ to $\chi_2$ but couples neither state to itself" | Fidelity: "couples χ1 only to χ2" leaves χ2→χ2 open. The base "couples only across them" meant purely off-diagonal |
| s2-1:3 | "The toy rate of … predicts 73 events for a kilogram of silicon exposed for a year to 100 MeV dark matter with σe = …, and twice as many for two years" | "In the toy rate of …, dark matter of 100 MeV with σe = … produces 73 events in a kilogram of silicon in one year, and twice as many in two years" | PP chain of four, with a reduced relative ("exposed for a year to…") inside it |
| s2-1:121 | "; in effect it moves to a frame that rotates with the perturbation." | "; the substitution is a change to a frame that rotates with the perturbation." | *it* had two candidates (substitution, absorption term), and "a substitution moves to a frame" does not parse |
| s2-2:7 | "and the relative motion is the motion of a single particle of mass $\mu_{\chi e}$" | "which is the motion of a single particle of mass $\mu_{\chi e}$" | Partial revert, for over-repair: *which* had one candidate, the noun right before it. "the motion of" keeps the editor's repair of the category error |
| s2-2:192 | "In $^{73}$Ge, 7.8 % of natural germanium, the first excited state is at 13.3 keV and the second at 66.7 keV." | "The isotope $^{73}$Ge, 7.8 % of natural germanium, has much lower levels: its first excited state is at 13.3 keV and its second at 66.7 keV." | The editor's cut of "The exception" also lost the contrast with the MeV levels of the previous sentence. Restated positively, with the comparison named |
| s2-5:62 | "…; \cref{sec:4.2} develops the dynamic structure factor." | "…; \cref{sec:4.2} develops $S$." | Over-repair: the full term is repeated within one sentence. $S$ has one referent here |
| s2-5:163 | "\cref{chap:3} finds the crystal states that separate silicon from the free electron gas." | "\cref{chap:3} finds the crystal states responsible for the difference between silicon and the free electron gas." | "States that separate silicon from the gas" does not parse. Kept the relational noun with both of its arguments |
| s3-1:76 | "…, and reversing the order of the cross product in the triple product that the identity then gives restores the sign." | "where reversing the first cross product brings $\vect{a}_1$ to the front of both factors at the cost of a sign, and reversing the cross product inside the resulting triple product restores the sign." | Depth: a PP chain with a relative clause inside it. The algebra was checked: $(a_3\times a_1)\times(a_1\times a_2) = a_1[a_1\cdot(a_2\times a_3)]$ |
| s3-1:107 | "…the Hamiltonian of the electrons is … The electronic Hamiltonian is unchanged…" | "…The Hamiltonian of the electrons is unchanged…" | Two names for one object in consecutive sentences, created by the split |
| s3-2:28 | "The \emph{periodic gauge} of … makes the states themselves periodic…" | "We use the \emph{periodic gauge} of …, which makes the states themselves periodic…" | Fidelity: the base said the book adopts this gauge, and L169 relies on that ("With the periodic gauge") |
| s3-3:44 | "Three numbers per element suffice: the lattice fixes much of the band structure, and the band structure needs little of the potential." | "That three numbers per element suffice shows how much of the band structure the lattice fixes and how little of the potential the band structure needs." | Fidelity: the base made an inference from the small parameter count ("which shows"). The editor turned it into two bare assertions |
| s3-4:20 | "and the gap between the Hartree--Fock bands is the fundamental gap of the Hartree--Fock state" | "and their gap is its fundamental gap" | Revert, for over-repair: "Hartree--Fock" appears three times in one clause. *their* (plural) and *its* (singular) each had one candidate |

Open-item fixes (in base text):

| file:line | old text | my text | reason |
|---|---|---|---|
| s3-3:188 | "A photon is the opposite extreme." … "Scattering dark matter lies in between. Above a few hundred keV in mass it reaches $k_{\mathrm{c}}$…" | "A photon is the limiting case of a negligible momentum." … "Whether scattering dark matter needs a phonon depends on its mass. Above a few hundred keV in mass, scattering dark matter reaches $k_{\mathrm{c}}$…" | The extremes were never named. The paragraph's real contrast is vertical absorption (photon, absorbed boson) against scattering, which needs a phonon only near threshold. The next sentence now opens on the noun, and the later *it* binds to the subject of the previous clause |
| s3-4:84 | "the dashed bands, shifted by one constant, pass close to all of them" | "…pass close to every $G_0W_0$ square at a conduction state" | Checked against figscripts/ch03/fig3_8.py. The dashed curves are conduction bands only, and they lie 0.08–0.10 eV from the $G_0W_0$ conduction squares (Γ 3.28 vs 3.204, X 1.30 vs 1.221, L 2.20 vs 2.095, CBM 1.17 vs 1.076). The measured circles at one point spread by up to 0.35 eV, and some of them are valence states, so "all of them" cannot include the circles |

Recall fixes (Job 2, untouched paragraphs):

| file:line | old text | my text | reason |
|---|---|---|---|
| s1-4:130 | "Per unit target mass, the normalization of the event rate $\mathcal{R}$ of \cref{sec:1.5}, it is" | "In the normalization of the event rate $\mathcal{R}$ of \cref{sec:1.5}, per unit target mass, the dark-photon absorption rate is" | Apposition attached to a PP, then an *it* that resolves only through the sentence before |
| s2-2:121 | "Far from the atom the ejected electron is a spherical wave; near it, the wave is distorted by the ion." | "…; near the atom, the wave is distorted by the ion." | *it* had three candidates. The nearest one ("a spherical wave") is the wrong one |
| s2-3:157 | "By \cref{eq:2.3-basis} it is" | "By \cref{eq:2.3-basis} the determinant is" | *it* had two singular candidates (determinant, bonding orbital), and the subject of the previous sentence is plural |
| s3-1:184 | "Its components, \cref{eq:A.3-periodic}, are" | "The Fourier components of $f$, \cref{eq:A.3-periodic}, are" | *Its* had three candidates (function, potential, superposition). The nearest one is wrong |
| s3-3:224 | "Computing them requires a potential…" | "Computing the full bands and wavefunctions requires a potential…" | *them* had two plural candidate sets (edges/masses/splittings; bands/wavefunctions) |
| s3-4:56 | "…yields the equilibrium structure, and its second derivatives yield the force constants" | "…, and the second derivatives of the ground-state energy yield the force constants" | *its* had two candidates. The nearest one ("the equilibrium structure") is wrong |

Interpretations in the editors' logs that I checked and accepted:
- s1-1 "electron--phonon coupling": accepted.
- s1-3 L202 "the prefactor and the quadratic power of δ": accepted, since the next clause ("a smoother truncation would raise the power") supports this pair.
- s1-4 L34 "relative to $q^2$": accepted. The addition is correct because $\omega^2/q^2 \le v^2 < 10^{-5}$.
- conventions "ratio between": accepted.
- s1-2 L21 "$v_0$ to be the speed of the LSR": accepted.
- ch02 s2-2 L82 "atoms whose response depends only on $q$": accepted.

## Recall (Job 2)

I sampled paragraphs that are unchanged since the base, as whole lines, in every file that has any. Half were chosen by ranker density and half spread through the file. The figure is about 30 % of the unchanged words, and 60 % in ch03. conventions.tex, ch01.tex and ch03.tex have no unchanged paragraphs.

| Chapter | Paragraphs sampled (file:line) | Words | Misses | per 1000 |
|---|---|---|---|---|
| front + ch01 | plan:5; s1-1:8; s1-2:3, 7, 12, 211, 219; s1-3:14, 49, 81, 91, 191, 204; s1-4:18, 25, 130, 137; s1-5:8, 28, 32, 44, 73, 80, 181 | 1,400 | 1 | 0.7 |
| ch02 | ch02:8; s2-1:21, 100, 139; s2-2:23, 33, 121, 123; s2-3:7, 17, 30, 32, 47, 157, 193; s2-4:3, 12, 14, 19, 28, 38, 52, 59, 61, 63, 69, 94, 96, 109, 138, 162, 180; s2-5:12, 26, 39, 83, 100, 146 | 2,630 | 2 | 0.8 (s2-4 alone: 0 in 1,504) |
| ch03 | s3-1:14, 21, 28, 65, 103, 131, 145, 156, 184; s3-2:12, 30, 39, 57, 106, 117, 139, 143, 159, 184, 192, 273; s3-3:12, 48, 77, 135, 144, 170, 174, 181, 209, 224; s3-4:7, 30, 56, 89 | 2,220 | 3 | 1.4 |
| **Block** | | **6,250** | **6** | **1.0** |

No chapter exceeds 2 misses per 1000 words, so no chapter needs a second pass on this evidence. Words are counted with inline math as one token. Most of the sentences that remain untouched in these files are short and declarative. The six misses were all pronouns whose nearest candidate is the wrong one.

## Open items (OPEN.md, this block)

| Item | Decision |
|---|---|
| s3-3:188 "opposite extreme … lies in between" | Fixed (see above) |
| s3-4:84 "close to all of them" | Fixed against the figure script (see above) |
| s3-2:155 `\cref{sec:3.6}` | Stays. The label is Sect. 27.1, "Wannier functions" (tex/ch27/s3-6.tex, resolved through tex/xref/vol1.tex), which is the right target. chapcheck ch03 reports 0 undefined references |
| ch01 interpretations (s1-1, s1-3 L202, s1-4 L34) | All three verified and accepted (see above) |
| s1-3 L161 "the derivative" | Physics wording, so filed as erratum E1. The adjacent pointer was rebound to "This factor" so that it does not extend the error |

## Proposed errata

**E1.** Location: tex/ch01/s1-3.tex, line 161 (the paragraph after the angular average of the delta function, before Eq. (1.3-eta)).
- Old: "The factor $1/qv$ is the derivative of the argument of the delta function with respect to $\cos\theta$."
- New: "The factor $1/qv$ is the inverse modulus of the derivative of the argument of the delta function with respect to $\cos\theta$."
- Reasoning: the argument is $g(\cos\theta) = \omega + \Delta_\chi + q^2/2\mchi - qv\cos\theta$, so $g' = -qv$. By $\delta(g) = \delta(\cos\theta - c_0)/|g'(c_0)|$ (\cref{app:C.1}) the factor is $1/|g'| = 1/qv$, which the $\tfrac12$ of the angular average turns into $1/(2qv)$. As written, the sentence calls $1/qv$ the derivative itself.

## Checks
- `python3 tools/invariant.py 60cc72c` on all 19 files: 0 STOP.
- Lint (`lint.py --banned BANNED-TERMS.txt`) on the 11 files I edited: no hits on any line I changed.
- `tools/chapcheck.sh ch01|ch02|ch03 /tmp/binding-review-vol1a-chNN`: exit 0 for all three, 0 undefined references, 0 multiply defined labels. The overfull hboxes are 2, 3 and 3, the same counts the editors reported.
