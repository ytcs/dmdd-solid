# Prose round, Stage 2: adversarial review of Volume I (Foundations)

Base commit 8904b84; edited state HEAD (e73026b, "prose round, Volume I complete"). Scope: tex/ch01-ch08, appA, appB/appB.tex, appB/B-2.tex, appC, appD, front. Editors' logs read: ch01-02, ch03, ch04, ch05-06, ch07, ch08, appA-appC, appD-front.

## Method
- Read the whole word diff 8904b84..HEAD (482 changed lines; every changed line is one paragraph or display line of the source, often with several edits). Each changed sentence was compared with the old one for meaning drift, and the surrounding paragraph was read in the file wherever a sentence was deleted, a referent changed or a count frame was removed.
- Mechanical drift check: for every changed file, the multiset of `$...$` spans, `\cref`/`\Cref`, `\cite`, `\SI`/`\num`, `\label` and bare numbers was compared between 8904b84 and the working tree. Every difference is accounted for: `\cref`/`\Cref` case changes at sentence starts (C-10:3, s3-4:152, s3-4:167, s7-2:210); symbols dropped with a deleted clause (C-2:55 $\omega$, D-13:14 $\mathcal{N}_{00}$ topic sentence, s1-3:7 $\vect{q}$, s6-3:125 $\omega_{\mathrm{Ein}}$, s8-3:128 $q$, s8-5:110 $\eta_{\mathrm{anh}}^2$); symbols added to name a referent (D-23:42 $r_\perp$, $r_\parallel$; D-24:63 $\mathcal{O}_3,\mathcal{O}_{12},\mathcal{O}_{15}$; s8-5:104 $\mathfrak{T}_0$; s3-1:215 "(200)"; C-20:73 $\alpha_{\mathrm{ohm}}<\frac12$, the book's own definition of weak coupling at C-20:3); D-20:44 $\Delta(0)$ and $T_c$ merged into $\Delta(0)/T_c$. No equation content, number, label, citation key or cross-reference target changed (one display-final comma became a period, D-23:30).
- Then 20+ untouched paragraphs read for misses (list below), plus the detector `tools/llmese.py` over all Volume I files as a net.

## Counts
| | |
|---|---|
| changed lines reviewed | 482 |
| kept | 473 |
| fixed (language) | 6 |
| reverted (old wording restored, in whole or for the drifting clause) | 3 |
| untouched paragraphs sampled | 37 |
| misses fixed in untouched paragraphs | 2 |
| files touched by this review | ch04/s4-2, s4-3, s4-5, s4-9; ch05/s5-5; ch07/s7-3; ch08/s8-6, s8-7; appD/D-26 |

## The two cases the editors flagged
- **ch03/s3-4.tex:95**, "about 0.1 eV in silicon among calculations that treat the gap seriously": kept as the editors left it. The deleted aphorism before it ("A computed rate is therefore only as good as the gap behind it") carried no fact. Naming the set would be a content claim: figscripts/ch03/fig3_8.py plots G0W0 1.24, 1.25, 1.29 eV, converged G0W0 1.10 eV and HSE 1.22 eV in panel (b), a range of 0.19 eV, so "about 0.1 eV" reads as a half-range and "seriously" stands for "beyond LDA/PBE". **Open for the author**: replace by "among the $G_0W_0$ and hybrid-functional calculations of panel (b)" and state the spread as ±0.1 eV, if that is the intended number.
- **ch06/s6-3.tex:125**, deleted "The choice of $\omega_{\mathrm{Ein}}$ carries physics.": kept. $\omega_{\mathrm{Ein}}$ is introduced at s6-3:107 ("Suppose every phonon has the same energy $\omega_{\mathrm{Ein}}$, an Einstein model") and used at 112, 115 and 117 before this paragraph; the paragraph itself works with $\langle u^2\rangle$.

## Fixes and reverts of the edits
| file:line | old (8904b84) | edited (HEAD) | now | verdict | why |
|---|---|---|---|---|---|
| ch04/s4-5:55 | "At $r_s = 2$ it is not exact, but it gets the long-wavelength physics right, since ..." | "At $r_s = 2$ it still holds at long wavelength, since ..." | old sentence | reverted | dropped "not exact" and strengthened the claim |
| ch04/s4-5:157 | "whether a real material has it is a question about the material, not about the gas" | "whether a real material has it depends on the material" | old clause | reverted | tautology; the old one-clause contrast is the content |
| ch07/s7-3:14 | "The block $M(\delta\vect{k})$ is not arbitrary, and the Kramers degeneracy is what pins it down." | "The Kramers degeneracy constrains the block $M(\delta\vect{k})$." | "The Kramers degeneracy pins down the block $M(\delta\vect{k})$." | reverted (verb) | "constrains" weakened the claim; the paragraph derives the form of $M$ |
| ch04/s4-3:148 | "fails the check by 43 percent: the continuum, which is the ionization channel of ..., is not a correction." | "misses the 43 percent that the continuum, the ionization channel of ..., carries." | "misses the 43 percent carried by the continuum, the ionization channel of ..." | fixed | edited sentence needed a second reading |
| ch04/s4-9:31 | "What is lost is the retarded response ..." | "This loses the retarded response ..." | "The static interaction misses the retarded response ..." | fixed | unanchored "This" (pattern 13) |
| ch05/s5-5:36 | "What is measurable is a change of polarization, the charge per unit area ..." | "Only a change of polarization is measurable, the charge per unit area ..." | "Only a change of polarization, the charge per unit area ..., is measurable." | fixed | appositive detached from its noun |
| appD/D-26:38 | "What remains is $m^{-2}(\vect{q}\cdot\nabla_i)^2U$." | "The term is therefore $m^{-2}...$" | "The same-particle potential term is therefore $m^{-2}...$" | fixed | "the term" read as the last term, the one shown to vanish |
| ch08/s8-6:29 | "harmonic reference lattice in which the electronic excitation sits" | "... that carries the electronic excitation" | "harmonic reference lattice of the excited electronic state" | fixed | new figurative verb |
| ch08/s8-6:185 | "What a bound has to control is the connected part" | "A bound therefore has to control the connected part" | "A bound has to control the connected part" | fixed | the edit made two "therefore" three sentences apart |

## Untouched paragraphs sampled (37)
Summaries: s2-5:155, 157, 159, 161; s5-7:156, 158, 162, 164, 166; s6-5:176, 178, 180, 182, 184. Chapter opening: ch02.tex:3 and its map caption. Section openers: s1-4:7, s2-3:3, s2-5:3, s3-4:3, s4-2:3, s4-8:3, s5-2:3, s8-2:3, s8-5:3, s8-7:3. Worked examples: s1-2:115, s4-4:179, s5-6:122, s6-3:115, s8-4:98. Captions: s1-1:33, s2-2:115, s6-4:12, s7-3:64; front/plan.tex:3-5. Plus the detector over all Volume I files (35 X-not-Y and 7 not-X-but-Y hits read; all are contrasts a reader needs, or false positives such as "far from").

Misses fixed:
| file:line | before | after | pattern |
|---|---|---|---|
| ch04/s4-2:3 | "the same Gibbs weights, and we will see that at each $\vect{q}$ and $\omega$ either one fixes the other." | "the same Gibbs weights, and at each $\vect{q}$ and $\omega$ either one fixes the other." | self-narration (22) |
| ch08/s8-7:116 | "Two questions remain open. First, the identification ... Second, the assumption ..." | "The identification ... The assumption ..." (each sentence ends on "is not established" / "is not known") | count-teaser (18) |

Noted, left as is (structural count frames that carry a condition): s5-7:122 "Three such theories are in common use, and they differ in what the harmonic force constants are fitted to."; s8-2:3 "Three things are missing before it can serve every model of Sect. 8.1."

## Checks
- chapcheck (`tools/chapcheck.sh <unit> /tmp/rev1-<unit>`): ch03, ch04, ch05, ch07, ch08, appD each exit 0, 0 undefined references, 0 multiply defined labels. (ch03 is unchanged by this review in the end; run because the s3-4:95 rewrite was tried and withdrawn.)
- lint (BANNED-TERMS) on the nine touched files: 0 blocking.

## Every changed line of the round (file:line in HEAD | old | edited | verdict | why)
Old and edited columns list the removed and added word spans of the line, joined by " … ", truncated at 150 characters.

| file:line | old | edited | verdict | why |
|---|---|---|---|---|
| appA/A-3.tex:15 | sits with | is in | kept | language only; meaning, conditions and references unchanged |
| appA/A-3.tex:51 | The reason for this bookkeeping is that every | Every | kept | language only; meaning, conditions and references unchanged |
| appA/A-8.tex:13 | belongs to the uncertainty … halo, not to the definition … edge. … absorbed | is part … uncertainty … halo. … treated | kept | dropped contrast 'not to the definition of the edge' is covered by the preceding sentence ('The fixed value keeps every threshold time-independent') |
| appA/A-9.tex:5 | first is the reference point. The | (deleted) | kept | count frame 'The first is ...' removed; A-9:3 already lists 'the reference point, the medium and the amplitude normalization' |
| appA/A-9.tex:7 | The second is the medium. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| appA/A-9.tex:9 | The third is the amplitude normalization. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| appB/B-2.tex:3 | renamings that a reader moving between the book and the papers will meet. | renamed symbols. | kept | language only; meaning, conditions and references unchanged |
| appC/C-1.tex:3 | takes for granted, | uses, | kept | language only; meaning, conditions and references unchanged |
| appC/C-1.tex:24 | rests on | needs | kept | language only; meaning, conditions and references unchanged |
| appC/C-10.tex:3 | \Cref{sec:11.5} asks what five … about … deposits. The answer is … the … distribution, | Five … deposits only up to … its … distribution (\cref{sec:11.5}), | kept | language only; meaning, conditions and references unchanged |
| appC/C-10.tex:24 | rests on | uses | kept | language only; meaning, conditions and references unchanged |
| appC/C-10.tex:41 | To see this, note that … 0$ for every linear $s$, | For every linear $s$, … 0$, | kept | language only; meaning, conditions and references unchanged |
| appC/C-10.tex:43 | We now show that the | The … that is | kept | language only; meaning, conditions and references unchanged |
| appC/C-10.tex:70 | beyond, which is what we need. | beyond. | kept | language only; meaning, conditions and references unchanged |
| appC/C-10.tex:81 | \tfrac56$. Five … say almost nothing about … median. | \tfrac56$, so five … leave … median almost undetermined. | kept | language only; meaning, conditions and references unchanged |
| appC/C-10.tex:90 | indeed | (deleted) | kept | language only; meaning, conditions and references unchanged |
| appC/C-10.tex:92 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| appC/C-11.tex:29 | pulls | moves | kept | language only; meaning, conditions and references unchanged |
| appC/C-11.tex:44 | not to … other | smaller | kept | 'not to the other root' -> 'the smaller root': roots are 1 and 2/3, so 2/3 is the smaller; same fact |
| appC/C-12.tex:3 | Three of its properties are needed: any | Any | kept | language only; meaning, conditions and references unchanged |
| appC/C-12.tex:18 | — | which … is … set of | kept | language only; meaning, conditions and references unchanged |
| appC/C-12.tex:43 | Where … sit follows … sit | The positions of … follow … lie | kept | language only; meaning, conditions and references unchanged |
| appC/C-12.tex:59 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| appC/C-13.tex:3 | resolve, no more. | resolve. | kept | language only; meaning, conditions and references unchanged |
| appC/C-13.tex:35 | sits … sits | is … is | kept | language only; meaning, conditions and references unchanged |
| appC/C-14.tex:19 | events, not a few. | events. | kept | language only; meaning, conditions and references unchanged |
| appC/C-14.tex:41 | that are not … but … not … exactly: | no direct … that … only approximately: | kept | language only; meaning, conditions and references unchanged |
| appC/C-14.tex:68 | widths faithfully, | widths, | kept | language only; meaning, conditions and references unchanged |
| appC/C-16.tex:11 | What remains is | The remaining terms sum to | kept | language only; meaning, conditions and references unchanged |
| appC/C-17.tex:26 | invariants, and it can be proved in two lines. | invariants. | kept | language only; meaning, conditions and references unchanged |
| appC/C-19.tex:14 | and … neutron passing through sees nothing. | so such … magnetization does not scatter neutrons. | kept | language only; meaning, conditions and references unchanged |
| appC/C-19.tex:26 | sits | is localized | kept | language only; meaning, conditions and references unchanged |
| appC/C-19.tex:30 | sit in | occupy | kept | language only; meaning, conditions and references unchanged |
| appC/C-2.tex:3 | also | (deleted) | kept | language only; meaning, conditions and references unchanged |
| appC/C-2.tex:19 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| appC/C-2.tex:55 | spikes, not a function of $\omega$. … carries | spikes. … has | kept | language only; meaning, conditions and references unchanged |
| appC/C-20.tex:54 | the content: | that | kept | language only; meaning, conditions and references unchanged |
| appC/C-20.tex:73 | At weak coupling … longer … wins. | For $\alpha_{\mathrm{ohm}} < \tfrac12$ … grows faster than the squared amplitude falls. | kept | 'At weak coupling' -> 'For alpha_ohm < 1/2': C-20:3 defines weak coupling as alpha_ohm < 1/2, so the condition is unchanged |
| appC/C-20.tex:119 | sits. | is. | kept | language only; meaning, conditions and references unchanged |
| appC/C-20.tex:130 | minimum sits … the maximum … rest on … a_{\mathrm{ch}}$ as well, | energy is lowest … highest … also assume … a_{\mathrm{ch}}$, | kept | language only; meaning, conditions and references unchanged |
| appC/C-3.tex:79 | sits | the momentum transfers of … lie | kept | language only; meaning, conditions and references unchanged |
| appC/C-3.tex:83 | crystal is not spherical, but a … close. | close to spherical symmetry. | kept | language only; meaning, conditions and references unchanged |
| appC/C-4.tex:36 | draws the consequences, | derives from it | kept | language only; meaning, conditions and references unchanged |
| appC/C-4.tex:74 | is the price of | comes from | kept | language only; meaning, conditions and references unchanged |
| appC/C-5.tex:26 | A … that … plane is all that the following derivations need. | The derivations below assume only that the … plane. | kept | language only; meaning, conditions and references unchanged |
| appC/C-6.tex:74 | probability, as it must be. | probability. | kept | language only; meaning, conditions and references unchanged |
| appC/C-7.tex:3 | Positive semidefiniteness, block inversion, Dyson-type equations and Bogoliubov transformations recur in \cref{chap:4,chap:7}. Positive … couplings. B… | In \cref{chap:4,chap:7}, positive … couplings, block … function, … interactions, and | kept | language only; meaning, conditions and references unchanged |
| appC/C-9.tex:67 | limit at all. … field, not a static potential. | limit. … field. | kept | language only; meaning, conditions and references unchanged |
| appD/D-1.tex:33 | There are three branches. | (deleted) | kept | 'There are three branches.' deleted; the branches follow as labelled cases (i)-(iii) |
| appD/D-10.tex:29 | What remains is | The two lines give | kept | language only; meaning, conditions and references unchanged |
| appD/D-12.tex:36 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| appD/D-12.tex:59 | \cref{eq:D.10-sum} on its own. … anyway | separately … \cref{eq:D.10-sum}. | kept | language only; meaning, conditions and references unchanged |
| appD/D-13.tex:14 | The diagonal term $\mathcal{N}_{00}$ takes a simple form. | (deleted) | kept | topic sentence on N_00 deleted; N_00 is still defined in the same paragraph |
| appD/D-13.tex:22 | what is left is | the remaining terms give | kept | language only; meaning, conditions and references unchanged |
| appD/D-14.tex:28 | out. What is left is … \cref{eq:6.2-frohlich}, | out, leaving … \cref{eq:6.2-frohlich} | kept | language only; meaning, conditions and references unchanged |
| appD/D-16.tex:44 | trades … for | expresses … through | kept | language only; meaning, conditions and references unchanged |
| appD/D-16.tex:57 | closes the gap. It writes | supplies it by writing | kept | language only; meaning, conditions and references unchanged |
| appD/D-2.tex:57 | The subtraction of … is what | Subtracting | kept | language only; meaning, conditions and references unchanged |
| appD/D-20.tex:5 | What remains | The mean-field Hamiltonian | kept | language only; meaning, conditions and references unchanged |
| appD/D-20.tex:44 | Dividing $\Delta_{\mathrm{BCS}}(0)$ by $T_c$, | In $\Delta_{\mathrm{BCS}}(0)/T_c$ | kept | language only; meaning, conditions and references unchanged |
| appD/D-22.tex:21 | only escape | remaining case | kept | language only; meaning, conditions and references unchanged |
| appD/D-22.tex:61 | response, its … alone, | response (its … alone) | kept | language only; meaning, conditions and references unchanged |
| appD/D-23.tex:9 | being | is … and | kept | language only; meaning, conditions and references unchanged |
| appD/D-23.tex:30 | , | . | kept | display-final comma -> period: the next line starts a new sentence ('Measuring lengths ...'); punctuation only |
| appD/D-23.tex:42 | radii are … and … half lattice constants. | radius $r_\perp$ is … lattice constants, $r_\parallel$ … half. | kept | radii now attached to r_perp (4.5) and r_par (2.5) in the order of the old sentence; transverse radius is the larger, consistent |
| appD/D-24.tex:63 | Three | The … $\mathcal{O}_3$, $\mathcal{O}_{12}$ and $\mathcal{O}_{15}$ | kept | count-teaser replaced by the names O_3, O_12, O_15, which D-24:63-69 then treat in that order |
| appD/D-25.tex:86 | What remains | The rate … then | kept | language only; meaning, conditions and references unchanged |
| appD/D-25.tex:126 | Neither the target's symmetries nor the form of the coupling entered; only … did. | Only … entered, not the target's symmetries or the form of the coupling. | kept | language only; meaning, conditions and references unchanged |
| appD/D-26.tex:38 | What remains | The term … therefore | fixed | 'The term is therefore' read as 'the last term' (the one just shown to vanish); now 'The same-particle potential term is therefore' |
| appD/D-26.tex:88 | Two hypotheses enter. | (deleted) | kept | 'Two hypotheses enter.' deleted; the two 'must' sentences follow |
| appD/D-27.tex:3 | sits | is | kept | language only; meaning, conditions and references unchanged |
| appD/D-27.tex:7 | stays inside | is included in | kept | language only; meaning, conditions and references unchanged |
| appD/D-27.tex:41 | drag; … are what separates | drag, and … make … differ | kept | language only; meaning, conditions and references unchanged |
| appD/D-27.tex:73 | Two cases arise. | (deleted) | kept | 'Two cases arise.' deleted; the two cases follow as emphasized paragraph heads |
| appD/D-27.tex:79 | not a Coulomb line but | (deleted) | kept | language only; meaning, conditions and references unchanged |
| appD/D-28.tex:60 | is what … kick: | kick; | kept | language only; meaning, conditions and references unchanged |
| appD/D-28.tex:87 | What remains, … so the response calculation does not need $\varGamma^{\mathrm{tot}}_m$, … does. | The rest, … and … needs $\varGamma^{\mathrm{tot}}_m$. | kept | language only; meaning, conditions and references unchanged |
| appD/D-28.tex:89 | Its use for the … is | The … estimate needs | kept | language only; meaning, conditions and references unchanged |
| appD/D-28.tex:97 | sits … itself, is what the estimate describes. | is created … top of … estimate describes the … itself. | kept | language only; meaning, conditions and references unchanged |
| appD/D-3.tex:38 | decay does not remember its own past: the … is the content of | defines | kept | language only; meaning, conditions and references unchanged |
| appD/D-3.tex:51 | plays … role in any | affects | kept | language only; meaning, conditions and references unchanged |
| appD/D-8.tex:12 | has moved into | now enters as | kept | language only; meaning, conditions and references unchanged |
| appD/D-9.tex:19 | pull | relax | kept | language only; meaning, conditions and references unchanged |
| ch01/ch01.tex:3 | What such a detector can see is set by a single quantity, the … it … events, | The … a detector … events sets what it can see, | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-1.tex:3 | What theory … is | Theory | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-1.tex:10 | Under … integrals sit … tied together | The integrand is … product of … joined | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-1.tex:12 | The value … is that each factor | Each factor | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-1.tex:14 | all that remains of … is | enters only through | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-1.tex:37 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-2.tex:79 | drift: the wind is broad. | drift. | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-2.tex:168 | What changes, however, is | The rotation does change | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-2.tex:231 | are what makes … cross-section, not the flux, keeps the … small. | make … small … comes from the cross-section. | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-3.tex:3 | Whether it can excite a target, and which excitation it can excite, is decided by energy … computed. | Energy … decide, … computed, whether it can excite the target and which excitations it can reach. | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-3.tex:7 | crystal, $\vect{q}$ brings some … vocabulary with it; … develops it properly, and for now four working definitions are enough. | crystal we need four terms of … theory, which … develops. | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-3.tex:21 | and it pays to separate … parties. … sits | so we treat … sides separately. … is | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-3.tex:63 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-3.tex:172 | Small … transfers carry | Each … transfer enters with | kept | 'Small momentum transfers carry the weight q dq' -> 'Each momentum transfer enters with the weight q dq': true and the measure is displayed just above; the old emphasis on small q is lost but the sentence goes on to the small-q cutoff by eta |
| ch01/s1-3.tex:176 | Three features matter for light dark matter: a plateau, a Gaussian fall and a second branch. | (deleted) | kept | deleted count-teaser named 'plateau, Gaussian fall, second branch'; the three are described in the next sentences and 'second branch' is defined at s1-3:174 (App. D.1 branches) |
| ch01/s1-4.tex:5 | Why … \cref{sec:1.1} should have the observed abundance is a separate question, … the simplest answer, thermal freeze-out, | Thermal freeze-out is the simplest explanation of the observed abundance of … \cref{sec:1.1}, … it | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-4.tex:61 | it is the cross-section of no process: … does, and $\sigmae$ merely normalizes $\|\tilde V(q_0)\|^2$. | $\sigmae$ only normalizes $\|\tilde V(q_0)\|^2$: … does. | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-5.tex:3 | quanta: | the | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-5.tex:42 | Present sensors are far from this: their … not by the | The … of present sensors … far above this | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-5.tex:73 | does not measure $\omega$ but $N_{\mathrm{eh}}$. | measures $N_{\mathrm{eh}}$ instead of $\omega$. | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-5.tex:87 | This step is where most … originates. | Most … originates in this step. | kept | language only; meaning, conditions and references unchanged |
| ch01/s1-5.tex:187 | are not statistical: they | (deleted) | kept | 'are not statistical' dropped; 'come from approximations' and 'A longer exposure does not reduce them' state the same |
| ch02/s2-1.tex:31 | sits | is | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-1.tex:70 | catch is that … has to sit | time … must lie | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-1.tex:126 | has no meaning on its own. | is undefined. | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-1.tex:155 | For readers comparing with particle-physics papers, we also translate to … is used | Particle-physics papers use … we use | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-2.tex:42 | An … does … conserve momentum by itself. | The momentum of an … is … conserved. | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-2.tex:64 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-2.tex:103 | dies | falls | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-2.tex:119 | hides … charge. | screens the charge of … nucleus. | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-2.tex:121 | packaged | written | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-2.tex:135 | sits. | enters. | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-2.tex:186 | sit | are contained | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-2.tex:219 | model, not a measurement. … wherever … matter is concerned. | model. … at the momentum transfers of … matter. | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-2.tex:231 | beats … costs almost nothing. | outweighs … is close to one. | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-3.tex:67 | exchanging … costs nothing. | are symmetric under exchange. | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-3.tex:88 | rest alone, and … does | others unchanged; … makes | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-3.tex:155 | collapses | reduces | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-3.tex:177 | is what | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-3.tex:182 | sit … around | stand … about | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-3.tex:224 | tamed … all of them | treated … both | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-3.tex:233 | What is left | The remainder | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-3.tex:239 | is part of the answer: with | matters. With | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-4.tex:3 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-4.tex:12 | sits | is now | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-4.tex:24 | It reads … left as a story: … it | Read … left, it says that … that the system … that | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-4.tex:94 | here. The trouble is that | here; | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-4.tex:114 | sits … sits; | stays … lies; | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-4.tex:152 | what remains of … This … the reason for care | Care … needed | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-4.tex:160 | sit … takes over~\cite[Sect.~VI]{kahn2022searches}. | lie … dominates~\cite[Sect.~VI]{kahn2022searches}. | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-4.tex:180 | sits | 1795}{eV^{-2}}, now positive, the principal-value cross term between the two orderings \SI{197}{eV^{-2}}, and the off-resonant ordering \SI{6}{eV^{-2}… | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-5.tex:19 | which is what makes | so … is | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-5.tex:43 | sits | is contained | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-5.tex:144 | of course | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch02/s2-5.tex:163 | sits … cannot … excited by less than \SI{1.17}{eV}; | is … contained … need at least \SI{1.17}{eV} to … excited; | kept | language only; meaning, conditions and references unchanged |
| ch03/ch03.tex:3 | sees | resolves | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-1.tex:3 | The repetition has two consequences that every later rate uses: … zone. | Because of the repetition, … zone; every later rate uses both facts. | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-1.tex:5 | What the … are | The | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-1.tex:170 | sit. | are. | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-1.tex:215 | it … it is what | the (200) component | kept | 'it' -> 'the (200) component': the referent of the old pronoun, made explicit |
| ch03/s3-2.tex:3 | what … rate needs, | the electronic input to … rate, | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-2.tex:37 | it is this tail that … probes. | \ii\vect{G}\cdot\vect{r}}$, so it is the lattice Fourier component of \cref{eq:A.3-periodic} at $-\vect{G}$, times $\Omega^{1/2}$. The electron in sta… | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-2.tex:79 | are what remains, … both carry no | remain, … neither carries a | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-2.tex:97 | is a different matter. It | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-2.tex:100 | What survives is the mechanism. Gaps … they are set by … potential. | The mechanism carries over to silicon: gaps … potential set their size. | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-2.tex:122 | atom; the payoff is that | atom, but then | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-2.tex:143 | atom, and the reason is chemical. | atom. | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-2.tex:151 | pay it back~\cite[Chap.~3]{harrison1980electronic}. | energy gained in the … compensates it~\cite[Chap.~3]{harrison1980electronic}. | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-2.tex:153 | sits: | lies: | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-2.tex:249 | The … vertex is now one line. Expand | To obtain the … vertex, expand | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:3 | sits … sits … Which … energies is … \cref{sec:1.3}, and the answer lies in the bands just below and just above the gap. | is … The bands just below and just above the gap decide which … energies, … \cref{sec:1.3}. | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:40 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:44 | That the fit works at all … needs; the price is that the … not computed but adjusted, … it says nothing about … is what … exactly | Three numbers per element suffice, which … needs. The … fitted rather than computed, … the fit does not constrain the | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:73 | carriers at all, | carriers, | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:104 | sits, | lies, | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:133 | cleanest measurement | splitting … measured most directly | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:140 | gap; … sit mostly | difference; … have most of their weight | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:172 | sits | is | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:181 | (\cref{eq:1.3-region}), and the comparison with the target is now direct. | (\cref{eq:1.3-region}). | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:188 | A … pair on its own. | Without a phonon, a … pair. | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:209 | at all | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-3.tex:221 | nothing confines … to vertical … sit | also makes nonvertical … lie | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-4.tex:18 | Each term has a plain meaning. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-4.tex:20 | costs nothing: | is exact: | kept | 'costs nothing' -> 'is exact': the same sentence gives the reason (relaxation energy vanishes as N -> infinity) |
| ch03/s3-4.tex:22 | The trouble is that a | A | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-4.tex:56 | — | given by | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-4.tex:77 | sit | be | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-4.tex:82 | discontinuity at all. | discontinuity. | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-4.tex:84 | \SI{1.52}{eV}, and germanium, … loses it: … its gap closes … sits … sit … The correction is not the same for every state, but … \SI{0.1}{eV} … are rig… | \SI{1.52}{eV}. Germanium, … has no gap … lies … lie … To … \SI{0.1}{eV}, the error of … is a rigid shift. | kept | 'The correction is not the same for every state, but within about 0.1 eV ... right in shape and wrong in position' -> 'To within about 0.1 eV, the error ... is a rigid shift': same claim and tolerance |
| ch03/s3-4.tex:93 | Why are quasiparticle … gaps, … ones? A physical picture follows from … close | Quasiparticle … are … gaps … ones because of … narrow | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-4.tex:95 | A computed rate is therefore only as good as the gap behind it. | (deleted) | kept (flagged case) | deleted aphorism 'A computed rate is therefore only as good as the gap behind it' carries no fact. 'among calculations that treat the gap seriously' left as is: naming the set (G0W0 + HSE of panel b) would make a factual claim; figscripts/ch03/fig3_8.py gives G0W0 1.24, 1.25, 1.29, converged 1.10 and HSE 1.22 eV, a range of 0.19 eV, so 'about 0.1 eV' reads as a half-range. Content question for the author, not a language fix |
| ch03/s3-4.tex:107 | What does … do to the ingredients of a rate? Energies and the density vertex are easy. Every … are less obvious. | Under … every … do change. | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-4.tex:134 | signature of | excess that … produces | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-4.tex:152 | Where … lies … bounds is a question for \cref{sec:13.1}. | \Cref{sec:13.1} locates … bounds. | kept | language only; meaning, conditions and references unchanged |
| ch03/s3-4.tex:167 | What the chapter has not included is … screening that \cref{chap:4} adds. | \Cref{chap:4} adds … screening. | kept | language only; meaning, conditions and references unchanged |
| ch04/ch04.tex:3 | Two questions follow: … Linear response answers both. | Linear response tells us | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-1.tex:18 | matter, for its part, | matter | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-1.tex:46 | carries | imposes | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-1.tex:122 | does not depend on temperature at all. | is independent of temperature. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-1.tex:141 | Two facts went into this: | This used | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-1.tex:174 | physics is in | temperature dependence comes from | kept | 'The physics is in the weight' -> 'The temperature dependence comes from the weight': the preceding paragraph ends on 'now the temperature matters'; same referent |
| ch04/s4-2.tex:48 | The classical reading of $\mathcal{G}_{\mathrm{VH}}$ is simple. | classical, … $\mathcal{G}_{\mathrm{VH}}$ of | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-2.tex:84 | sit | appear | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-2.tex:86 | is the bridge between … rate and … response. … which carries screening into … rate. | converts … response into … rate. … so that … rate includes screening. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-2.tex:111 | point, not the answer. | point. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-2.tex:154 | The … is where | In the | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-2.tex:156 | The … \cref{we:2-hydrogen} distribute the weight. At | With the … \cref{we:2-hydrogen}, at | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-3.tex:37 | Two limits of it carry physics. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-3.tex:51 | The … 1$ is the one with content. | For densities the first nonvanishing … is … 1$. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-3.tex:60 | A … over, and this is why the identity is useful. | The identity is useful because a … over. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-3.tex:80 | which closes … loop with | and the rule fixes … coefficient of | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-3.tex:98 | is not violated, … a device that reproduces … their every commutator. | still holds, … built to reproduce … and its commutators need … agree with those of the full Hamiltonian. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-3.tex:142 | takes over | starts | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-3.tex:148 | fails … check by … percent: … which is … is not a correction. | misses … percent that … carries. | fixed | edited sentence needed a second reading (relative clause split by an appositive); now 'misses the 43 percent carried by the continuum, the ionization channel of ...' |
| ch04/s4-3.tex:154 | sits. | lies. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-3.tex:160 | A gap changes the balance. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-3.tex:164 | is what | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:17 | In contrast, | The full response … called | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:28 | has a direct reading. The | in … the | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:43 | The classical reading is the familiar one. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:51 | cell, not uniformly. | cell. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:90 | which is … live. … the business of | the … lie. … treated in | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:92 | the factor $1/\|\varepsilon\|^2$ is what … out~\cite{knapen2021dark}. | out the factor $1/\|\varepsilon\|^2$~\cite{knapen2021dark}. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:94 | consequence is that the | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:112 | changes … by nothing … while … interaction at all. | does not change … and … interaction. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:127 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:132 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:136 | field, not … what … is | field rather than | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-4.tex:166 | sits | is | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-5.tex:3 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-5.tex:55 | The physical content is that … What is dropped is … is not exact, but it gets the long-wavelength physics right, | In this approximation … It drops … still holds at long wavelength, | reverted (one sentence) | 'At r_s=2 it still holds at long wavelength' dropped 'it is not exact' and strengthened 'gets the long-wavelength physics right' to 'holds'; old sentence restored. The other edits of the paragraph kept |
| ch04/s4-5.tex:76 | has to go somewhere, and … line is where it goes. | goes into … line. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-5.tex:80 | this is what … adds. | adds it. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-5.tex:105 | plasmon at all. | plasmon. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-5.tex:136 | what … is … point, not … there. | point while leaving … there unchanged. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-5.tex:157 | is a question about the material, not about … gas~\cite{hochberg2021determining,kahn2022searches}. | depends on … material~\cite{hochberg2021determining,kahn2022searches}. | reverted | 'depends on the material' was a tautology; the old one-clause contrast (material, not gas) restored |
| ch04/s4-5.tex:168 | sat | were | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-5.tex:172 | What the … sees is … and there | The … samples … where | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-6.tex:3 | shape hardly at all. | barely … shape. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-6.tex:58 | is a change of … no change of … spectrum. | changes … leaves … spectrum unchanged. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-6.tex:60 | What they do has … picture. … sits | The local fields have … analog. … lies | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-6.tex:71 | what dark matter sees. | the loss function that sets the dark-matter rate. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-6.tex:99 | unknown, and it has to do a lot. … sit | unknown. … lie | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-6.tex:116 | Its meaning is that an | An | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-6.tex:134 | At short wavelengths the … fails, and this is | The … fails at short wavelengths, | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-6.tex:138 | What the … give is a … of | The | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-6.tex:143 | Two comparisons place these numbers. … What is missing is | The adiabatic kernel lacks | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-6.tex:145 | takes back … exciton … rest and more. | undoes … electron--hole attraction more than makes up … rest. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-7.tex:3 | sits … What propagates is an … object, | lies … The … propagates … dressed electron, | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-7.tex:12 | commutator, and for good reason. | commutator. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-7.tex:63 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-7.tex:92 | sits | is | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-7.tex:142 | above … is no paradox. The … Indeed, in | exceeds … because the … In | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-8.tex:43 | sign of the … passes its first test: | gives the right sign: | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-8.tex:57 | The general statement is just as direct. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-8.tex:80 | carries | shows | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-8.tex:124 | What it … is | It | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-8.tex:155 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-9.tex:3 | In fact the … matter they matter | The … matter, excitons change the response | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-9.tex:29 | Each piece of $H^{\mathrm{exc}}$ has a plain meaning. … is what … coupling at all. | of $H^{\mathrm{exc}}$ … coupling. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-9.tex:31 | What is lost is | This loses | fixed | 'This loses' had no clear referent; now 'The static interaction misses the retarded response' |
| ch04/s4-9.tex:51 | sit | are | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-9.tex:70 | $1/r$ at all. | $1/r$. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-9.tex:91 | sits … on its own. | lies … without a phonon. | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-9.tex:120 | One property of these states decides how the figure is read. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-9.tex:138 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-9.tex:148 | What the … are | The | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-9.tex:160 | once and for all | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch04/s4-9.tex:168 | function can quote. | of … function. | kept | language only; meaning, conditions and references unchanged |
| ch05/ch05.tex:3 | rest on one fact, | follow from | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-1.tex:48 | turns out to be | is | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-1.tex:50 | The surface is computed, not modeled. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-1.tex:54 | silicon symmetry does most of the work. Each | silicon, each | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-1.tex:56 | motion at all. | motion. | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-1.tex:77 | fourth root is the point: the | because of the fourth root | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-1.tex:97 | what survives is … statement, | only … statement holds, | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-1.tex:101 | What is left is | The remaining term gives | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-1.tex:127 | and this is what | which | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-1.tex:129 | puts … to the test | tests | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-1.tex:153 | upshot is that the | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-2.tex:28 | What is left is … problem in the $3n_{\mathrm{at}}$ amplitudes, | The $3n_{\mathrm{at}}$ amplitudes then obey … problem, | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-2.tex:47 | The force constants are computed, not fitted. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-2.tex:107 | stiffness, is what the second term describes~\cite[Chap.~V]{born1954dynamical}. … other, but not … waves. | the second term describes … stiffness~\cite[Chap.~V]{born1954dynamical}. … other; … waves it is nonzero. | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-2.tex:128 | what matters is how many … there are | we need the number of | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-2.tex:134 | The … branches is what makes silicon's … phonons so numerous: | Because of the … branches, silicon has many … phonons: | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-3.tex:3 | what matters most for detection: | that | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-3.tex:37 | \nu$. What remains is | \nu$, leaving | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-3.tex:42 | Nothing … has happened yet. It | So far the calculation is classical; … mechanics | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-3.tex:89 | used throughout, and that | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-3.tex:100 | What is finite is the … that sum | The … is finite, … it | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-3.tex:117 | carries | has | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-3.tex:184 | verdict is that the | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-3.tex:187 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-5.tex:3 | sit … is what | lie | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-5.tex:7 | what … is | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-5.tex:34 | Silicon has no dipole to offer. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-5.tex:36 | What is measurable is … polarization, | Only … polarization is measurable, | fixed | appositive detached from its noun ('... is measurable, the charge per unit area ...'); reordered so the appositive follows 'a change of polarization' |
| ch05/s5-5.tex:40 | The Born charge, as we saw, comes through almost untouched. | (deleted) | kept | deleted 'The Born charge, as we saw, comes through almost untouched.'; s5-5:38 states Z* within 1 percent and s5-5:76 'right to a percent' |
| ch05/s5-5.tex:56 | not one matrix but | of matrices | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-5.tex:76 | names the culprit. … lands on | shows why. … agrees with | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-5.tex:78 | The … term is also why | Because of the … term, | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-6.tex:53 | This is the scale that controls everything below: the | The | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-6.tex:110 | lives … positive … lands | vanishes … negative … contributes | kept | 'P_1 lives at positive omega' -> 'P_1 vanishes at negative omega': same support statement at T=0 |
| ch05/s5-6.tex:112 | mean energy deposited takes no calculation at all. The … it | the mean energy deposited | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-6.tex:128 | sits … Indeed, a | lies … A | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-6.tex:135 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-6.tex:160 | well. Summing … weights is a job for the generating function. | well, and the generating function sums … weights. | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:3 | What limits their … detection this matters in two ways. An … And every | The … limited by … detection, an … Every | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:40 | is the price of | comes from | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:44 | sit | are | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:61 | survives, | remains, | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:68 | energy at all. … sit | energy. … lie | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:91 | actually | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:93 | silicon, where two transverse phonons cannot share the energy at all. | silicon. | kept | reason 'where two transverse phonons cannot share the energy at all' cut; s5-7:68 in the same subsection states it with the numbers |
| ch05/s5-7.tex:114 | sits at | is of | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:118 | pace | rate | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:129 | What the … is … widths at all. | The … widths. | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:146 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:160 | carries | has | kept | language only; meaning, conditions and references unchanged |
| ch05/s5-7.tex:168 | chapter has produced the phonons of a crystal, their quanta, … lifetimes, … on | phonons, … lifetimes are … properties of | kept | language only; meaning, conditions and references unchanged |
| ch06/ch06.tex:3 | part of it is already lost to | already lowers it | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-1.tex:3 | The same couplings, at … are what … drops. | At … drops the same couplings. | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-1.tex:38 | What survives is | The counting then becomes | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-1.tex:42 | pays with … sits | acquires … appears | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-1.tex:64 | Three things are left out of \cref{eq:6.1-Hep}. … $u$ | $u$, left out of \cref{eq:6.1-Hep}, | kept | count frame 'Three things are left out' removed; the three omissions (second order, V_NN, screening) remain, the first marked 'left out of eq:6.1-Hep' |
| ch06/s6-1.tex:66 | phonon, … insulator on its own. | phonon alone, … insulator. | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-1.tex:80 | is what … Two limits follow at once. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-1.tex:85 | The nucleus has been given a velocity, but its electrons have not. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-1.tex:130 | does … work that … did | replaces … assumed | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-2.tex:3 | is the electron's view of | comes from | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-2.tex:7 | what … is | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-2.tex:26 | What is left … how much … changes | The other factor … the change of | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-2.tex:40 | What survives is the … $Q$, | The … $Q$ remains, | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-2.tex:136 | grid, are what a calculation can afford. | calculation can afford a … grid. | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-2.tex:138 | What is left is | The matrix element becomes | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-3.tex:3 | hands | loses | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-3.tex:21 | propagator at all. | propagator. | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-3.tex:38 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-3.tex:66 | denominator. What is left is | denominator, which leaves | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-3.tex:79 | What survives at … is … term, | At … term remains, | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-3.tex:86 | What it … is | It | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-3.tex:112 | lands on … sits | gives … lies | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-3.tex:125 | The choice of $\omega_{\mathrm{Ein}}$ carries physics. | (deleted) | kept (flagged case) | deleted 'The choice of omega_Ein carries physics.' omega_Ein is defined at s6-3:107 (Einstein model, 'Suppose every phonon has the same energy omega_Ein') and used at 112, 115, 117 before this paragraph; the paragraph itself does not need it |
| ch06/s6-3.tex:127 | Two further numbers follow. … And replacing … nothing of … survives. | Replacing … vanishes. | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-3.tex:139 | coupling at all: | coupling: | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-3.tex:173 | sit | be | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-4.tex:3 | all at … is at work … crystals. What differs … detection these effects matter in two places. The … And every | acts … crystals; the difference … detection, the … Every | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-4.tex:46 | is what | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-4.tex:76 | sit … lives. | lie … is appreciable. | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-4.tex:110 | model behind it is the simplest that still has the right ingredients. The | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-4.tex:117 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-4.tex:126 | The shape carries more information than the number. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:3 | The process matters for dark matter twice. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:27 | is all there is. | only … remains. | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:54 | sits | is | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:58 | is what | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:65 | leads | dominates | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:78 | all there is. | the whole absorption. | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:88 | What remains is … space. | Then only … space remains. | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:113 | the photon pays for | is | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:115 | has two caveats. It … And it | It also | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:119 | sits | is | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:126 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:128 | occupations above are what the | the occupations | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:168 | sit | are evaluated | kept | language only; meaning, conditions and references unchanged |
| ch06/s6-5.tex:172 | Two kinds of dark matter … is all there is: | Absorbed bosons and scattering particles … only … contributes: | kept | language only; meaning, conditions and references unchanged |
| ch07/ch07.tex:4 | What is new … and | The rest | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-1.tex:3 | the Néel temperature of … value as tabulated by Fischer et al.~\cite[Table~IV]{fischer2009exchange}, the ordering temperature of an antiferromagnet, …… | Néel temperature~\cite[Table~IV]{fischer2009exchange}, | kept | 'the ordering temperature of an antiferromagnet' dropped; the sentence itself says the spins order below the Neel temperature |
| ch07/s7-1.tex:95 | $1/\|\vect{S}\|$ that linear spin-wave theory misses. | $1/\|\vect{S}\|$. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-1.tex:196 | sits | is localized | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-1.tex:202 | plays for … the role that … \cref{sec:2.2} plays for the charge. | is … analog of … \cref{sec:2.2}. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-1.tex:216 | $\vect{q}$: every momentum transfer finds its magnon with the same strength. | $\vect{q}$. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-1.tex:229 | paying | working against | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:3 | The gap is not … gap. It … answer them in turn, starting | Unlike … gap, it … start | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:12 | picture … one of timing. | attraction … retarded. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:31 | are also not bare electrons. They are | are, in addition, | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:36 | The model interaction keeps only what the gap needs: a constant attraction in a thin shell. | (deleted) | kept | deleted 'The model interaction keeps only ... a constant attraction in a thin shell.'; the shell and the constant V_BCS are defined at s7-2:18 |
| ch07/s7-2.tex:38 | are special. | have the most final states. | kept | 'are special' -> 'have the most final states': the next two sentences give exactly this reason |
| ch07/s7-2.tex:76 | do not matter … energies, … they | are negligible … energies | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:104 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:133 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:148 | quasiparticles. It is | quasiparticles, and | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:152 | culprit is | error comes from … so | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:157 | it. The violation is … confined to | it, and … only at | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:168 | The violation has a simple origin in this language. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:175 | What the … is | The | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:210 | The … operator are the subject of \cref{sec:8.3}. | the … \Cref{sec:8.3} derives the … operator. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:212 | is what the rate of pair breaking uses, | rate of pair breaking uses the | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-2.tex:227 | worse on its own. | alone … worse. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-3.tex:14 | block $M(\delta\vect{k})$ is not arbitrary, and the … is what pins it down. | constrains the block $M(\delta\vect{k})$. | reverted (verb) | 'constrains' weakened 'pins it down' (the paragraph derives the form of M); now 'The Kramers degeneracy pins down the block' |
| ch07/s7-3.tex:30 | is … physics in a familiar setting. | has … form. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-3.tex:32 | sit … sit … sits | lie … lie … lies | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-3.tex:50 | the right size: … matter, | matter and | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-3.tex:72 | do not disappear from | still contribute to | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-3.tex:84 | plays … role that … plays in | is … analog of … of | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-3.tex:101 | a signature | characteristic | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-3.tex:103 | carries | gives | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-3.tex:108 | And the … is not unique. States | The … depends on the cutoff: states | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-3.tex:125 | estimate, and what replaces it is an open question that … up. | estimate; … up the open question of what replaces it. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-3.tex:134 | delicate one: | hardest to compute: | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:3 | in two roles: | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:37 | do not depend on … says they should. … It … value of the … that calculations of donor levels use~\cite{faulkner1969higher,smith2017ab}, … 11.7. … neve… | are independent of … predicts. … This … 11.7, and calculations of donor levels use it~\cite{faulkner1969higher,smith2017ab}. … are insensitive to | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:39 | are another matter. | depend on the donor. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:48 | This \emph{valley-orbit splitting} is what the … show: | The … show this \emph{valley-orbit splitting}: | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:50 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:54 | What a … supplies well is … core. … splitting, which is the division of labor that … up. | A … describes … core accurately. … splitting; … up this scheme. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:63 | leans … can bear that weight, | depends … are accurate enough for this, | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:65 | sit … takes | lie … is lowered by | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:74 | sit … color centers are where … measured. | lie … measured on color centers. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:130 | sit at | occupy | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:137 | not … creates, and it is always larger. | always larger than … creates. | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:141 | The threshold is not … that … For dark matter, only … can … thresholds at all. … a handle | Only part of … threshold … Only … dark-matter … thresholds. … which can be used | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:145 | target in its own right, | itself … target, | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:147 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:155 | defect | violation | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:157 | opens the target to … particles: | is reached by particles as … as | kept | language only; meaning, conditions and references unchanged |
| ch07/s7-4.tex:159 | which opens silicon to … \SI{13}{keV}. | so that … \SI{13}{keV} can ionize the donor. | kept | language only; meaning, conditions and references unchanged |
| ch08/ch08.tex:2 | reader who meets a … have to start | mean starting | kept | language only; meaning, conditions and references unchanged |
| ch08/ch08.tex:4 | They share one structure. … collapses into … into … What a calculation leaves out then becomes a named step with a size, not a guess. | reduces to … to | kept | deleted 'What a calculation leaves out then becomes a named step with a size, not a guess.'; the previous sentence says truncation is settled once, and Sect. 8.5 gives sizes |
| ch08/s8-1.tex:3 | None does. … particle … What remains of the … is | particle, however, … The … enters only through | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-1.tex:15 | What remains | The result | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-1.tex:26 | What survives is the … \cref{eq:8.1-eft}. | The … \cref{eq:8.1-eft} survives. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-1.tex:43 | electrons they are old acquaintances. The | electrons, the | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-1.tex:113 | sits … sit | is … are | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-1.tex:133 | rows and nothing else. | only … rows. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-1.tex:146 | what remains of … is | reduces to | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-1.tex:159 | it is the target term $\mathcal{T}_e$ that | the target term $\mathcal{T}_e$ | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-1.tex:163 | scattering. What differs is … needed, | scattering; only … needed differs, | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-1.tex:184 | What is new is the … side, which … the kinematics, which … fixes. | The … side is new; … it … fixes the kinematics. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-1.tex:198 | A light … fermion changes the picture. | The … particle can also be a light fermion. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-2.tex:33 | expanded at all: | expanded: | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-2.tex:64 | field … quantum sits inside $g^\phi_a$. | field, $g^\phi_a$ contains … quantum. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-2.tex:81 | gives way to | is replaced by | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-2.tex:89 | sits | is | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-2.tex:91 | does something different: it does not reweight the band, it | the band instead of reweighting | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-2.tex:98 | contraction; what remains is | contraction, leaving | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-2.tex:109 | need two things at once. The … must couple … $\mathfrak{D}_{ab}$, … must correlate | are nonzero only when the … couples … $\mathfrak{D}_{ab}$ … correlates | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-3.tex:3 | turns out to be | is | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-3.tex:29 | sits … estimate. For … Its use is to put | is … estimate of the cross term: for … It puts | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-3.tex:33 | they are where … up. | up in them. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-3.tex:48 | lives on | is confined to | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-3.tex:54 | where … excitations live? | in the range of … of … excitations? | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-3.tex:56 | What is left | The result | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-3.tex:76 | sits … sits | is concentrated … is | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-3.tex:85 | quantity in its own right, and it is | quantity, | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-3.tex:128 | not merely small at small $q$ but | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-3.tex:145 | shakes … inside | excites … internal motion | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:3 | sits … alone | is … unchanged | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:25 | R_{aZ}$, and through nothing else. | only … R_{aZ}$. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:38 | charge at all, | charge, | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:40 | collapses | reduces | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:50 | not screened at all. | unscreened. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:69 | on its own. | independently. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:71 | at all … sits. | lies. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:122 | in an instructive way. … sits | twice. … lies | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:129 | sits … sits | is … is | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:141 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:143 | Three consequences follow. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-4.tex:164 | at all | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-5.tex:7 | What the … are | The | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-5.tex:70 | The … parameter, read together, | Together, the … parameter | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-5.tex:87 | self-energy sits there; … approximations and on nothing else~\cite[Sect.~III\,A, | so is … self-energy; … only … approximations~\cite[Sect.~III\,A, | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-5.tex:104 | sits there. | is at $\mathfrak{T}_0$. | kept | 'sits there' -> 'is at T_0': 'there' referred to the base point T_0 defined in the same paragraph |
| ch08/s8-5.tex:106 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-5.tex:110 | Nothing like $\eta_{\mathrm{anh}}^2$ predicts the size of the next step. | (deleted) | kept | deleted 'Nothing like eta_anh^2 predicts the size of the next step.'; the paragraph already ends the argument with 'so there is nothing to expand in' |
| ch08/s8-5.tex:117 | sit | are | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-5.tex:130 | equation, not by a power counting. | equation. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:3 | freely at all: … pair at all, … the danger: | freely: … pair, … a double count: | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:29 | in which … excitation sits. … nested, not competing. | that carries … excitation. … nested. | fixed | 'reference lattice that carries the electronic excitation' is a figurative verb; now 'harmonic reference lattice of the excited electronic state' |
| ch08/s8-6.tex:46 | sector, not the coupling. | alone … sector. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:50 | sit | are | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:67 | at all | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:72 | sits | is | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:106 | interference of electrons and nuclei is the sharpest case. Its | of the electron--nucleus interference | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:114 | turn into four | give | kept | 'four prescriptions' -> 'prescriptions': the four are enumerated in the next sentences |
| ch08/s8-6.tex:146 | genuine | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:148 | sum is what the … protects. | preserves the sum. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:160 | sharp | well defined | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:171 | has nothing … do with | is unrelated | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:177 | sit | lie | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-6.tex:185 | is … sufficient but loose: it … a clean split … What a … is | small cross terms only … A … therefore | fixed (one word) | the edit put two 'therefore' three sentences apart; second dropped ('A bound has to control the connected part'). 'guarantees small cross terms only on bins wide ...' kept: equivalent to 'sufficient but loose ... clean split' |
| ch08/s8-6.tex:187 | convention, not a consequence. | convention. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-7.tex:45 | Screening changes the picture. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-7.tex:68 | sits | is | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-7.tex:81 | changes how many … are … three, … which pairs hardly at all. | lowers the number of … three … leaves their distribution nearly unchanged. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-7.tex:90 | on … own. | under … own Hamiltonian. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-7.tex:98 | sits | is | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-7.tex:106 | Three conditions are easy to break. | (deleted) | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-8.tex:3 | What remains is to turn each … into | Each … still has to become | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-8.tex:7 | sits | lies | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-8.tex:20 | bin. A … not of the bin, … is what | bin: a | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-8.tex:22 | the one fact a reader needs. | that its size is unknown. | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-8.tex:37 | alone, | unchanged, | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-8.tex:53 | positive on their own, | separately positive, | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-8.tex:73 | The … is the one in which | In the | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-8.tex:81 | on its own; | alone; | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-8.tex:100 | sits | is | kept | language only; meaning, conditions and references unchanged |
| ch08/s8-8.tex:111 | spins, and nothing else | only … spins | kept | language only; meaning, conditions and references unchanged |
| front/conventions.tex:5 | quantity, computed … from a … calculation … from … drops, or measured. … band, and the steps from the book's general result to the formula are derived… | quantity: a measurement, or a calculation … for the … for … drops. … band. The … box derives the formula from the book's general result. | kept | language only; meaning, conditions and references unchanged |
