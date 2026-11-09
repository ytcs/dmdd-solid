# Chapter 1 register and artifact pass

Scope: tex/ch01/ch01.tex, s1-1.tex to s1-5.tex, tex/appC/C-9.tex, tex/appD/D-1.tex. Checked against REGISTER.md
(Sects. 2, 4, 5, 6) and prose-review.md patterns 18 (concrete openers), 19 (process artifacts) and 20 (citations are
attribution only). All edits are exact-string replacements. Physics, numbers kept in the text, equations, labels,
citations and cross-references are unchanged. A concurrent session edited s1-2, s1-3 and s1-4 during this pass
(June/December wording, limit boxes). Those edits were kept, and the limit boxes were left to that session.

## 1. Counts by kind

| kind | count |
|---|---|
| R-rewrites from REGISTER Sect. 5 applied (R1, R2, R3, R4, R5, R6, R7, R8; R9 and R10 are in s2-1) | 8 |
| Openers rewritten (rule 18: abstract or outline openers, a count-teaser, a recap opener) | 7 |
| Terms of art: bare "transfer(s)" to "momentum transfer(s)" or "pair (q, ω)" | 33 |
| Terms of art: "least speed" / "minimum speed" to "minimum velocity" (incl. subsection and keyresult titles) | 7 |
| Terms of art: "largest transfer" to "maximum momentum transfer"; "mediator factor" to "dark-matter form factor"; "energy given" to "energy deposited"; "dark rate"; "weighted toward small momentum transfers" | 12 |
| "the least" (energy/certain/known) to "lowest" / "most uncertain" / "most poorly known" | 7 |
| "of order" to "∼", "typical", "comparable to", "around" | 13 |
| "we call" coinages removed | 6 |
| Crutch "so" (conjunctive) recast with "since", "because", "and", colon or split | 69 |
| Crutch "gives" recast ("is", "leads to", "we find", "yields", "leaves", "contributes") | 63 |
| Crutch "therefore" removed or recast | 21 |
| Emphatic "only" cut or changed to "alone"/"merely" (load-bearing ones kept) | 6 |
| Hedge "about" changed to "roughly", "some", "typical" (worked examples keep their digits) | 12 |
| Connectives added: "however" 7, "we will/can/see" 6, "note that" 2, "compared to" 1, "by contrast" 1 | 17 |
| Process artifacts removed: consistency assurances | 5 |
| Process artifacts removed: reviewer-directed justifications / bookkeeping | 5 |
| Process artifacts reduced to one clause about the literature | 5 |
| Fix announcements | 0 found |
| Pattern 20: by-reference content replaced with an in-text cross-reference (citation kept as credit) | 2 |

Crutch frequencies per 10k prose words (same counter, before → after; chapter + C.9 + D.1, about 17,600 words):
"so" 55 → 16 (this includes "so that", which was kept); "gives" 54 → 18; "therefore" 11.9 → 0.6; "only" 37.5 → 34
(what is left is mostly load-bearing: "only up to", "depends only on"); "of order" 7.4 → 0; "the least" 4.5 → 0; bare
"transfers" 21 → 2.3 (what is left is in the other session's limit boxes); "we call" 3.4 → 0; "about" 27.9 → 19.5;
"since" 5.7 → 16; "typical(ly)" 6.3 → 10; "however" 0 → 3.9; "we will/can/see" 0 → 3.3. Lengths, before → after
(words): s1-1 1678 → 1700 (+1.3%), s1-2 5002 → 4932 (−1.4%), s1-3 +0.2%, s1-4 +0.4%, s1-5 +0.8%, C-9 −0.1%,
D-1 −0.1%, ch01.tex unchanged. Every file is within ±5% (the measured change includes the concurrent session's edits).

## 2. Representative changes (before → after)

**R-rewrites and openers**
1. s1-1:3 (R1) "This section fixes the local density and the cosmological abundance of dark matter that the rest of the book uses, and explains why masses between a keV and a GeV are both open and suited to solid-state detectors." → "What gravity does give us is the two numbers the rest of the book uses, the local density and the cosmological abundance. It also points us between a keV and a GeV: that window is still open, and its kinetic energies match the excitations of a solid." (Split into two sentences to clear LONG-SENT.)
2. s1-1:61 (R2) "We call particles with $m_\chi$ between a keV and a GeV light dark matter." → "Particles in this window, between a keV and a GeV, are what the field calls light dark matter, or sub-GeV dark matter."
3. s1-3:3 (R3) "This section derives the energy a slow particle can give to a target …, the least speed it needs to do so, …" → "Kinematics alone already tells us a lot: how much energy a slow particle can deposit at a given momentum transfer, the minimum velocity $\vmin$ it needs to do so, and from that the lightest mass that can get over a detector threshold."
4. s1-3:7 (R4) "Four terms of \cref{sec:3.1} enter the description of $\vect{q}$ in a crystal, and we give working definitions here." → "In a crystal, $\vect{q}$ brings some lattice vocabulary with it; \cref{sec:3.1} develops it properly, and for now four working definitions are enough."
5. s1-3:21 (R5, R6) "A target in a solid is not a free particle at rest. Electrons are bound and move with momenta of order $\alpha m_e$ … We call $\omega$ the energy given to the target; …" → "The free particle at rest is an idealization, and in a solid a poor one: electrons are bound, with typical momenta $\sim \alpha m_e$ … We write $\omega$ for the energy deposited in the target. In this book it is defined as the energy given to the target, so it can be negative at $T > 0$."
6. s1-4:30 (R7) "\Cref{eq:1.4-Vq} has two regimes. If $m_V$ exceeds every relevant $q$ …" → "\Cref{eq:1.4-Vq} has two limits, which the field calls the heavy- and light-mediator limits. For a heavy mediator … a contact interaction. For a light mediator … the rate is weighted toward the smallest momentum transfers."
7. s1-4:128 (R8) "Their couplings to electrons are stated below as results of the cited references, with equation numbers; this chapter derives none of them." → "We quote their couplings to electrons from the literature, with equation numbers, and do not derive them here."
8. s1-2:19 (count-teaser) "Three numbers specify it." → "It is specified by the speed parameter $v_0$ and the escape speed $v_{\mathrm{esc}}$, which together fix the normalization $N_{\mathrm{esc}}$."
9. s1-4:7 (recap opener) "\Cref{sec:1.1} showed that thermal light dark matter needs a mediator …" → "Thermal light dark matter needs a mediator with a mass at or below the GeV scale (\cref{sec:1.1})."
10. s1-5:3 "This section follows the energy from the deposit …" → "We will follow the energy from the deposit …"

**Process artifacts (pattern 19)**
11. s1-2:38 (consistency assurance) "This book adopts 250.5 km/s as the reference value of this speed, and all numbers below are computed with it; the difference, 2e-4 in relative terms, changes no final result at its quoted precision." → "…= 250.55 km/s, which we round to the reference value 250.5 km/s."
12. s1-2:127 (consistency assurance) "A direct numerical integration of \cref{eq:1.2-flab} reproduces all three values to four digits." → deleted.
13. s1-3:168 (consistency assurance) "…, and a direct quadrature of \cref{eq:1.2-flab} reproduces them to $10^{-6}$ (\cref{app:D.1})." → clause deleted; the check stays in D.1's Check paragraph.
14. s1-2:248 (consistency assurance) "With the rotation speed of the daily modulation above, none of these changes a number in this section at the stated precision." → "We neglect these shifts, as we neglected the Earth's rotation."
15. s1-2:31 (consistency assurance) "\Cref{eq:1.2-nesc} agrees with Ref.~\cite[Eq.~(15)]{griffin2018directional}." → deleted; the citation moved to "The normalization $N_{\mathrm{esc}}$ follows in spherical coordinates~\cite[Eq.~(15)]{griffin2018directional}."
16. s1-2:250 (reviewer-directed, "so that it can be compared") "Results in this book are quoted for the parameters of \cref{tab:1-shm}, so that they can be rescaled to any other halo model." → "Results in this book use the parameters of \cref{tab:1-shm}."
17. s1-2:152 (reviewer-directed justification) "The reference convention of \cref{eq:1.2-vmax} costs little in the yearly average. Averaging $\langle 1/v\rangle$ over the year gives a value 0.3% below …" → "Averaged over the year, $\langle 1/v\rangle$ lies 0.3% below its value at $v_{\mathrm{E}}^{\mathrm{ref}}$ and agrees to $10^{-4}$ with its value at the annual-mean speed."
18. s1-2:21 (bookkeeping, now one literature clause) "The adopted value is … It replaces the older 220 km/s used in \cref{sec:1.1} and in much of the literature." → "We take the speed of the local standard of rest, … $v_0 = 238$ km/s …; much of the literature, like \cref{sec:1.1}, uses the older 220 km/s."
19. s1-3:39 (convention note, now one literature clause) "Papers differ in the sign of $\vect{q}$; … The choice is immaterial for … We keep $\vect{q}$ from the dark matter to the target, and $\omega$ given to the target, throughout the book (\cref{app:A.4})." → "Some papers take $\vect{q}$ as the momentum gained by the dark matter instead, a difference that matters for a crystal without inversion symmetry or with magnetic order, where $\vect{q}$ and $-\vect{q}$ are physically different (\cref{app:A.4})."
20. s1-4:88 (literature clause) "It is also the expression of Ref.~[essig2012], written with $y_\chi^2 = 4\pi\alpha_D$, where $\alpha_D$ is that paper's dark fine-structure constant." → "…; Ref.~[essig2012] writes it with $y_\chi^2 = 4\pi\alpha_D$, where $\alpha_D$ is a dark fine-structure constant."
21. s1-4:57 (bookkeeping) "The quantity $\sigmae$ is defined in vacuum. Screening and every other effect of the medium are assigned … and never to $\sigmae$, so … Other papers use other reference points and normalizations; \cref{app:A.9} converts them." → "Since $\sigmae$ is defined in vacuum, with screening and every other in-medium effect assigned to the target response (\cref{sec:4.4}), a quoted $\sigmae$ means the same thing for every target. Other papers use other reference points and normalizations (\cref{app:A.9})."
22. s1-4:99 (kept: a reader comparing with Lin would otherwise be misled by a factor of 30) "…; its own Eq.~(74) gives the value found here for this one." → "…, although its own Eq.~(74) leads to the value found here for this one."

**Crutches, terms of art, connectives**
23. s1-1:71 "The right side contains $\langle\sigma v\rangle$, so we solve it by iteration … This gives $x_{\mathrm{fo}} \approx 25$" → "Since the right side contains $\langle\sigma v\rangle$, we solve it by iteration … We find $x_{\mathrm{fo}} \approx 25$"
24. s1-1:77 "Our crude estimate omits annihilation after freeze-out, so its agreement is only in order of magnitude." → "Since our crude estimate omits annihilation after freeze-out, we trust it to an order of magnitude, and it delivers that with little work."
25. s1-3:14 "the transfer is bounded, $q \le 2\mu_{\chi N}v$, and the energy given to the nucleus" → "there is a maximum momentum transfer, $q \le 2\mu_{\chi N}v$, and the energy deposited in the nucleus"
26. s1-3:41 "moving with velocity of order $\alpha$ … Its momentum is of order $\alpha m_e$, and a transfer of that size is what changes its state, so the typical transfer is set by the electron" → "moving with a typical velocity $\sim \alpha$ … Its momentum is then $\sim \alpha m_e$, and a momentum transfer of that size is what changes its state. The typical momentum transfer is set by the electron"
27. s1-3:47 "The same expression without the absolute value appears for $\omega \ge 0$ … For $\omega + \Delta_\chi < 0$ the signed expression can be negative" → "Refs.~[…], which treat $\omega \ge 0$ and $\Delta_\chi = 0$, write the same expression without the absolute value. For $\omega + \Delta_\chi < 0$, however, the signed expression can be negative"
28. s1-3:123 "Folding $\vect{q}$ would assign the wrong $\vmin$ and the wrong mediator factor $\FDM(q)$" → "… the wrong dark-matter form factor $\FDM(q)$"
29. s1-3:196 "Both factors are fixed by the least certain parts of the halo model" → "… the most uncertain parts of the halo model"
30. s1-4:66 "A light mediator weights small momentum transfers by $(q_0/q)^4$. It therefore favors excitations …" → "A light mediator weights the rate toward small momentum transfers, by $(q_0/q)^4$, and favors excitations …"
31. s1-5:38 "the lowest bins are polluted by charge that leaks across the gap without any deposit, so single-pair events carry the largest background." → "the lowest bins are polluted by a dark rate, charge that leaks across the gap without any deposit, and single-pair events carry the largest background."
32. s1-5:187 "We call this the theory uncertainty of a limit." → "Together these errors make up the theory uncertainty of a limit."
33. C-9:104 "For $m_V \neq 0$ that shift would mix the mass term, so the photon shift is the one to use." → "For $m_V \neq 0$, however, that shift would mix the mass term, and the photon shift is the one to use."

**Pattern 20 (citations as attribution only)**
34. s1-2:72 "the galactic one of Ref.~\cite[Eq.~(10)]{baxter2021recommended}" → "the galactic one of \cref{eq:1.2-fgal}~\cite[Eq.~(10)]{baxter2021recommended}"; the same fix in the fig:1-speed caption ("Earth velocity of \cref{eq:1.2-vorb}~\cite[Eq.~(11)]…"). No other main-text formula, value or parameter set in Ch. 1, C.9 or D.1 is given by reference alone. Limit boxes were not checked (left to the other session).

## 3. Kept on purpose
- Convention notes a reader needs when comparing with the literature: ζ against ε/κ/χ (s1-4, C-9), $g(\vmin)$ against $\eta$ (s1-3), Steigman's Majorana and $\Omega h^2 = 0.11$ assumptions (s1-1), and the 0.120 ± 0.001 figure usually quoted from Planck (s1-1; one clause).
- D-1's "Checks" paragraphs (they are mathematical checks a reader can follow), including the quadrature sentence.
- "so that" purpose clauses, and load-bearing "only" ("only up to a reciprocal-lattice vector", "depends only on").
- Worked examples keep their digits and most of their "gives" before displayed results.

## 4. Build and lint
- The repository build currently stops on `\input{appF/appF}` in main.tex, because appF/ is an empty directory added by the concurrent session. That is not caused by this pass. A copy of tex/ with a one-line stub appF/appF.tex builds cleanly to /tmp/build-ch01reg/main.pdf: 0 errors and 169 unresolved references, none of them from Ch. 1, C.9 or D.1 labels except `sec:12.2`, a chapter that is not yet written.
- lint.py --banned BANNED-TERMS.txt: no banned terms. The only remaining hits are LONG-SENT false positives where detex merges a caption with its table cells or figure (s1-2 tab:1-shm and fig:1-speed, s1-3 tab:1-kinematics, s1-4 tab:1-interactions, s1-5 tab:1-quanta). The fig:1-speed hit comes from the concurrent session's caption edit. Two new hits (VAGUE "very" in s1-1, WORDY "in terms of" in s1-4) and two new LONG-SENT openers (s1-1, s1-4) were fixed.
