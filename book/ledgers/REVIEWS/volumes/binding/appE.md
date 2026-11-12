# Binding round: appE (Long derivations, D-30 to D-47)

Base commit: 60cc72c. Status: done. No file in tex/appE is marked as generated. All 17 section files (D-30 to D-47) were read paragraph by paragraph, including every subsection opening and every \emph{}/\paragraph lead-in. appE has no captions, footnotes, boxes or table prose. appE.tex holds only \input lines and was not changed.

- invariant.py: 0 STOP on all 17 files. Notes only: repeat counts of existing items, and \cref added to existing labels (eq:D.30-continuity, D.31-W2, 12.5-Rrel, D.35-T, 13.4-Lscr, D.37-ward, D.37-recoil, 14.1-Safm, D.40-T, D.40-g, D.42-alpha, D.43-firststep, D.43-cov, D.44-tagged, 19.5-identity, D.46-circle, D.46-defect). During the work, two STOPs were caught and reverted: a new token $S_{j_{\mathrm{T}i}j_{\mathrm{T}k}}$ in D-30, and a commutator rewrite in D-37 that dropped two existing math items. There is no deliberate symbol unification.
- chapcheck appE: exit 0, 42 pages, 0 undefined references, 0 multiply defined labels, 0 overfull hboxes > 5pt.
- Lint: no new blocking hits. The remaining LONG-SENT differences are of two kinds. Some are sentences that were already over 45 words and whose wording changed (D-33 "After multiplication…", D-34 "For a real ground state…", D-37 "Take … symmetrized…", D-37 "Away from an extremum…"). The others are reports that join a sentence ending in "gives"/"is" to the text after its display (D-35 twice, D-40). Six new long sentences that my edits created were split.

| File | Ranker before | Ranker after | Sentences changed |
|---|---|---|---|
| D-30.tex | 25 | 21 | 20 |
| D-31.tex | 38 | 30 | 25 |
| D-32.tex | 13 | 7 | 17 |
| D-33.tex | 17 | 16 | 14 |
| D-34.tex | 19 | 19 | 13 |
| D-35.tex | 20 | 17 | 14 |
| D-36.tex | 31 | 27 | 22 |
| D-37.tex | 23 | 23 | 20 |
| D-38.tex | 16 | 13 | 14 |
| D-39.tex | 14 | 12 | 9 |
| D-40.tex | 30 | 28 | 20 |
| D-42.tex | 17 | 16 | 9 |
| D-43.tex | 30 | 26 | 12 |
| D-44.tex | 32 | 27 | 16 |
| D-45.tex | 30 | 29 | 19 |
| D-46.tex | 27 | 24 | 10 |
| D-47.tex | 14 | 12 | 11 |

Totals: ranker 396 before, 347 after; about 265 sentences changed in about 18,000 words of prose (about 15 per 1000 words).

Names fixed across appE (checked against ch10/s10-4 and ch31/E-16): "singlet block", "triplet block", "cross block" (S_{n j_T}) and "current block" (S_{j_T j_T}). The D-30 phrase "the transverse block" became "the current block". The D-30 phrase "the two blocks" now follows an explicit introduction of the singlet and triplet blocks.

## Most instructive changes

| file:line | before | after | failure fixed |
|---|---|---|---|
| D-30:19 | Inserting both into \cref{eq:D.30-O8}, the longitudinal terms collect into … | Inserting \cref{eq:D.30-continuity} and this value of $\bar v_L$ into \cref{eq:D.30-O8} collects the longitudinal terms into … and gives | *both* reaching back three sentences; dangling modifier |
| D-30:47 | For independent particles the two blocks are related. | The scalar rows form the singlet block of the response matrix and the vector rows the triplet block. For independent particles the two blocks are related. | definite before introduction (the names were used later without introduction) |
| D-30:57 | The same holds for the triplet block: its rows change sign …, and the products of two of them stay real. | Every element of the triplet block is real as well: the triplet rows change sign …, and a product of two triplet rows stays real. | *the same* pointing to a proposition; *them* with two candidates |
| D-31:37 | The vertex held at $q$ is the approximation. Letting it vary adds … a correction linear in $p$ … and one $\sim(nq_{BZ}/q)^2$. | Holding the vertex at $q$ is the approximation. Letting the vertex vary adds two corrections to the self terms: a correction linear in $p$ … and a second-order correction $\sim(nq_{BZ}/q)^2$. | *it* with several candidates; *one* standing for a noun not repeated |
| D-31:39 | … and the farther pairs make up the difference to one with the opposite sign. | … and the farther pairs, with the opposite sign, bring the sum from 1.78 back to one. | relational noun *difference* without its arguments |
| D-32:25 | The first is … The second is half the double commutator …, and with … this is … | The term $\langle D^3\rangle$ is … The term $\langle D(H-E_0)D\rangle$ is half the double commutator …, and with … the double commutator gives … | *the first/the second* picking from the previous sentence; bare *this* |
| D-32:30 | …; that third moment includes the electronic excitations … and is the subject of \cref{sec:12.5}. | The third moment then includes the electronic excitations …, and \cref{sec:12.5} treats it. | demonstrative with no single antecedent |
| D-33:13 | …, which places it on the line $\omega_l = 0$. … This is \cref{eq:12.1-sectors}. | …, which places the final states of $\mathcal P_0$ on the line $\omega_l = 0$. … The placement of the three kinds of final state in the plane is \cref{eq:12.1-sectors}. | *it* with three candidates; bare *this* for a list of propositions |
| D-35:44 | The two minus signs cancel, | The factor $-1$ of the hole paths and the minus sign of the hole denominators cancel, | *the two X* naming objects from two different places |
| D-36:59 | That the sum over bare pairs is the whole absorptive part …, with nothing counted twice, is the optical theorem … | The optical theorem of the mean-field evolution states that the sum over bare pairs is the whole absorptive part … | left-heavy clausal subject |
| D-37:12 | … is the same number. Their ratio is exactly 1. … Both statements hold band by band, | … is the same number. The ratio of the vertex to the denominator is exactly 1. … The ratios $1$ and $-1$ hold band by band, | relational noun *ratio* without arguments; *both* picking from two sentences |
| D-37:73 | Divided into \cref{eq:D.37-gcmnn}, the factor $|Q|$ cancels and each term stays of order $\ell$. | Dividing the vertices \cref{eq:D.37-gcmnn} by these denominators cancels the factor $|Q|$, and each intraband term stays of order $\ell$. | dangling modifier with the operation inverted; vague *each term* |
| D-38:29 | Inserted in \cref{eq:4.2-Sab} …, their off-diagonal elements cancel, … Replacing $\hat z$ by the local ordering axis, the result holds … | When these matrix elements are inserted in \cref{eq:4.2-Sab} …, the off-diagonal elements of the two branches cancel, … With $\hat z$ replaced by the local ordering axis, \cref{eq:14.1-Safm} holds … | two dangling modifiers; *their* with two candidates |
| D-42:21 | a contact potential that differs between its configurations by $2V_d$, $\pm V_d$ over a volume $\Omega$ … | a contact potential $\pm V_d$ over a volume $\Omega$ around the defect, so that the potential differs between the two configurations by $2V_d$. | defining apposition |
| D-45:25 | … and the difference has to be found elsewhere. It is zero only while $N_h = N_e$ … | … and the difference between the two amounts has to be found elsewhere. Summed over the collected carriers, this difference is zero only while $N_h = N_e$ … | relational noun without arguments; *It* resolving to a proposition |

## Not resolved
- D-30:57. "inversion maps $\vect{q}$ back to $-\vect{q}$" looks like a slip: after time reversal the argument is $-\vect{q}$, and inversion maps it back to $\vect{q}$. Left unchanged, because fixing it changes a stated mapping. The lead should decide.
