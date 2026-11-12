# Binding and parse-depth review, second pass: ch08 (The response framework)

Brief: briefs/volumes/BINDING.md (with its calibration notes). Inputs: first-pass log ch08.md and the independent review review-vol2a.md, which measured 3.0 pattern-27 misses per 1000 words in text the first pass left unchanged. That review found mostly heavy or clausal subjects before the main verb, gerund subjects included, and binding failures at about 0.5 per 1000. Base commit for invariant.py: 60cc72c. Files: tex/ch08/ch08.tex and s8-1.tex to s8-8.tex.

Method. I reread every paragraph of the nine files whole, changed or not: body text, key-result and limit boxes, worked examples, figure and table captions, prose cells of tables, and the Summary. Subject weight came first: subjects over about eight words, subjects that contain a relative, appositive or participial clause, clausal subjects ("Which operators a model produces follows…", "How much…", "Whether…", "That λ₀ and λ₁ exist…"), and long gerund subjects. Pronoun and pointer binding came second. As a cross-check I ran a scripted scan for determiner-led and gerund subjects with a clause before the first finite verb, then read each hit; most were false positives. I applied the edits as exact old/new pairs, with each old string asserted to occur exactly once (scripts are in the scratch directory binding-ch08-pass2/). I kept every fix the reviewer had made, and kept the pronouns that have one candidate which is also the subject of the previous clause (calibration item 3).

## Per file

"Sentences changed" counts the sentences of the pre-pass file that no longer occur verbatim.

| file | ranker before (flagged / per 1000 w) | ranker after | sentences changed |
|---|---|---|---|
| ch08.tex | 6 (16.7) | 6 (16.5) | 1 |
| s8-1.tex | 83 (20.7) | 79 (19.6) | 17 |
| s8-2.tex | 70 (19.4) | 65 (18.0) | 15 |
| s8-3.tex | 83 (20.2) | 80 (19.4) | 19 |
| s8-4.tex | 98 (23.2) | 89 (20.9) | 22 |
| s8-5.tex | 94 (25.7) | 92 (25.1) | 15 |
| s8-6.tex | 133 (21.1) | 125 (19.7) | 31 |
| s8-7.tex | 86 (23.2) | 82 (22.1) | 12 |
| s8-8.tex | 81 (23.4) | 77 (22.1) | 15 |
| total | 734 | 695 | 147 |

Most of the ranker's remaining flags are definite noun phrases with a named antecedent, and long sentences that carry math. I read them and left them as they are, as the first pass did.

## Fifteen instructive changes

| file:line | before | after | failure fixed |
|---|---|---|---|
| s8-1:22 | Which operators a model produces follows from the non-relativistic limit of its couplings. | The non-relativistic limit of the couplings of a model fixes which operators the model produces. | clausal subject |
| s8-1:22 | Multiplying a dark-matter bilinear by an electron bilinear and by the mediator propagator gives the coefficients. | The coefficients are the product of a dark-matter bilinear, an electron bilinear and the mediator propagator. | 13-word gerund subject |
| s8-1:7 | Galilean invariance, the freedom to add a common velocity to both particles, then allows … | Galilean invariance is the freedom to add a common velocity to both particles, and it allows … | defining apposition inside the subject |
| s8-2:89 | a dark-matter particle that moves against q, or that recoils with more kinetic energy than it brings, gains energy, ω_q < 0. | a dark-matter particle gains energy, ω_q < 0, when it moves against q or recoils with more kinetic energy than it brings. | subject with two relative clauses before the verb |
| s8-2:33 | No truncation of the target changes the master formula; it changes only S_ab. | A truncation of the target changes only S_ab, never the master formula. | *it* bound to a negated quantifier |
| s8-3:56 | … and of the terms of U only the electron–nucleus Coulomb energy Σw(r−X), w(y) = −Zα/y, depends on both … | Of the terms of U, only the electron–nucleus Coulomb energy depends on both …; this energy is Σw(r−X), with w(y) = −Zα/y. | subject carrying two math appositions |
| s8-3:145 | only the part of a coupling that is not proportional to mass excites the internal motion of the crystal. | the internal motion of the crystal is excited only by the part of a coupling that is not proportional to mass. | 11-word subject with a relative clause |
| s8-4:7 | The Coulomb lines that carry a momentum of the channel are the ones that screen the dark-matter vertex. | Only the Coulomb lines with a momentum of the channel screen the dark-matter vertex. | relative clause in the subject; *the ones* |
| s8-4:149 | App. D.25 summed the chain and found that it turns ζ² into | … found that the summed chain turns ζ² into | *it*: the appendix (subject) or the chain |
| s8-5:7 | How much a given process feels them depends on how fast the nuclei move. | The effect of the non-adiabatic couplings on a given process depends on how fast the nuclei move. | clausal subject; *them* named |
| s8-5:106 | The exchange–correlation functional, the frozen core of a pseudopotential, the GW quasiparticle energies, and the numerical parameters of a calculation (…) are of this kind; | Of this kind are the exchange–correlation functional, …, and the numerical parameters of a calculation (…); | 20-word coordinated subject |
| s8-6:171 | An incoherent cascade cannot generate the term, since it is a coherence between production and decay | … since the term is a coherence between production and decay | *it*: the nearest candidate (cascade) is not the intended one |
| s8-6:179 | Suppose a dressing unitary U_qp, of the kind that Landau's theory and the Migdal–Eliashberg equations construct order by order, maps … | Suppose that a dressing unitary U_qp maps …; Landau's theory and the Migdal–Eliashberg equations construct a unitary of this kind order by order. | relative clause between subject and verb |
| s8-7:3 | How the two carriers share the 9 eV decides how many further pairs they make on their way down. | The split of the 9 eV between the two carriers decides how many further pairs they make on their way down. | clausal subject; *split* is then the noun that "a lopsided split" picks up |
| s8-8:97 | That λ₀ and λ₁ exist and are unique follows from one convex function. | One convex function shows that λ₀ and λ₁ exist and are unique. | clausal subject |

Other recurring repairs:
- *If …* or *When …* clauses for subjects that carried a relative clause: s8-4:42, s8-5:93, s8-6:114, s8-6:162 (two gerund subjects "Adding a Lorentzian …"), s8-7:3, s8-7:110, s8-8:3, s8-8:48, s8-8:81, s8-8:100.
- Fronted participles for participial subjects: s8-1:87, s8-6:16, s8-6:187, s8-6:200, s8-8:113.
- Appositive subjects split into a predicate: s8-2:75, s8-3:11, s8-3:173, s8-4:9, s8-4:124, s8-5:16, s8-5:85, s8-6:65, s8-6:194, s8-7:79, s8-8:73.
- Pointers named:
  - *its* spins (ch08:2)
  - *it* after a list (s8-3:76, "the curvature of the Coulomb potential")
  - *it* among several candidates (s8-6:173, "the level-shift matrix"; s8-4:71, "the electronic rate")
  - *its uncertainty* (s8-8:100, "the local-field uncertainty")
  - *those of* (s8-7:114)
- Attachment and scope:
  - "of strength …, with …, and range 1/m_V" became "of range 1/m_V and strength …" (s8-2:47)
  - the relative "that varies" was moved onto *density* (s8-3:74)
  - "with an even number of electrons" was moved onto *target* (s8-7:72)
  - "a tensor on the dark-matter side that weights" became "a dark-matter tensor that weights" (s8-1:3)
- Garden paths through reduced relatives: "A dark photon absorbed there couples" became "When a dark photon is absorbed at 3 eV, it couples" (s8-4:149). "A pair m created at energy ω lies" became "A pair m at energy ω lies" (s8-6:127).

## Judgment calls

- s8-1:22. Rewriting "Dark matter with an electric dipole moment that couples through a photon-like mediator" kept the original scope: "when it couples through a photon-like mediator" stays on the electric-dipole clause and does not spread to the magnetic-dipole and anapole clauses.
- s8-6:118. "Whether the split … means anything depends on where ω lies" became "The split … may or may not mean anything, depending on where ω lies". This keeps the possibility that the split has no meaning, which "the meaning of the split depends …" would have dropped.
- s8-7:116. "The identification of the prompt pair with the out-state … is derived only within …" became "The prompt pair is identified with the out-state … only within …". The restriction to time-dependent mean-field linear response is kept.
- s8-4:149. "there" became "at \SI{3}{eV}", repeating the energy that the previous sentence states. invariant.py reports this only as a repeat count, not as a STOP.
- Left as they are:
  - short restrictive relatives in subjects of at most about seven words, e.g. "Papers that normalize their states relativistically quote …" (s8-1:20) and "A phonon line that itself cuts the diagram in two is not a Coulomb line" (s8-4:139);
  - the reviewer's accepted "the phonon energies that are read off its thresholds" (s8-5:3);
  - the reverted base sentence at s8-8:106.

## Checks

- invariant.py 60cc72c on all nine files, after the last edit: 0 STOP. The `note` lines are repeat counts of existing items and the `\cref`s that the first pass added. This pass adds no `\cref`, symbol, number or label that was not already in the file.
- Lint (BANNED-TERMS): each file was compared with its own pre-pass copy, and I added no new hit. Two LONG-SENT hits that my edits created were removed:
  - s8-3 "We collect …": the pronoun was restored, since it binds to the subject of the previous clause;
  - s8-4 spin-current clause: the sentence was split at the semicolon.
  The one changed LONG-SENT in s8-6 ("On a Gaussian bin …") is the sentence before a display that was already over the limit; it is now shorter.
- chapcheck ch08, with the build directory binding-ch08-pass2/build in the session scratchpad: exit 0, 0 undefined references, 0 multiply defined labels, 0 oversized floats, 0 overfull hboxes.
- No git command was used except diff, show and log. Only tex/ch08/*.tex and this log were written.
