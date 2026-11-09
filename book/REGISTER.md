# REGISTER: the voice of *Dark Matter Detection in Solids*

This file distils how the register models write, so that writers can match the voice and prose reviewers can check against it. It puts into concrete form the "Language and register checks" of the long-form-writing prose review. Where it conflicts with STYLE.md or NOTATION.md, those two files win (Sect. 7).

**Models and sources.** The texts were fetched as arXiv PDFs and extracted to `sources/register/` with page markers (`===== PAGE n =====`). Page references are to the arXiv PDF page, which for all three equals the printed page number.

| Key | Text | Version | Role |
|---|---|---|---|
| **L** | T. Lin, "TASI lectures on dark matter models and direct detection", arXiv:1904.07915 | v1 | primary: voice, estimates, the DM side |
| **KL** | Y. Kahn and T. Lin, "Searches for light dark matter using condensed matter systems", arXiv:2108.03239 | v2 | the DM / condensed-matter interface: S(q, ω), phonons, ELF, Migdal |
| **G** | F. Giustino, "Electron-phonon interactions from first principles", Rev. Mod. Phys. 89, 015003, arXiv:1603.06965 | v2 | Part I solid state: lattice dynamics, e–ph coupling, DFPT, polar materials |

**Why Giustino.** The text is open, and the RMP is widely cited as a clear account of its subject. Its scope matches the Part I chapters line by line: harmonic lattice dynamics and the dynamical matrix, the e–ph Hamiltonian to first and second order, DFPT and the Sternheimer equation, the adiabatic approximation, Debye–Waller terms, the Fröhlich coupling in polar materials, and phonon-assisted absorption. Like the book, it is written for readers who will compute these quantities from first principles. Baroni et al. (cond-mat/0012092) covers DFPT in more depth but is narrower. **Use G for vocabulary and for its physical-picture sentences, not for its syntax.** G is the most formal of the three. It has the highest rates of "in order to" (12.7 per 10k words), "whereby" (3.0), "respectively" (3.0) and passive constructions, which are exactly what the skill's register checks forbid.

Quotes are short (at most about 20 words), are copied from the extracts, and use "…" for cuts. Counts are per 10,000 words. They are approximate, because they come from PDF extraction (with contents pages and figure text included, and line-break hyphens repaired).

---

## 1. The register in a paragraph

Lin writes as a lecturer at the board. She uses "we" for herself and the audience together ("we will", "we can" and "we have" each occur 11–14 times per 10k words), and she says where she is going ("We turn to phonon excitations next", L 67). The tone is relaxed and confident, and in places openly enjoys the subject: "Remarkably, we find…" (L 74), "Nuclei and electrons in such materials have enormous interactions with each other!" (L 59), "But wait – there is one more candidate" (L 23). Sentences are of ordinary length, with a median of 26 words, and are mostly declarative. Short punchy ones are mixed with longer explanatory ones, and parentheses carry the asides. She hedges with numbers rather than adverbs. A quantity is "typical" (15 per 10k) or "∼" a value, "a few" eV, "O(1)", "roughly", "≃ 50 − 100 events/kg/day". The hedge always comes with a reason ("this is just a typical energy deposition", L 61). The standard move from picture to formula is estimate, then calculation, then check. She states the physical situation, makes a crude estimate ("let us start by dropping the left-hand-side… and estimating the momentum transfer", L 60), works the formula in a toy model, and then closes the loop ("This makes explicit the arguments made at the beginning of this section", L 64). Approximations are named and often owned with a light touch ("brazenly take the limit of small uJ", L 72; "we will gloss over some of the details", L 72), and a statement of the limits of validity follows. Kahn and Lin keep the same voice in a review. Their sentences are a little longer (median 31 words), they use more "indeed", "thus" and "the upshot", and they lean harder on the condensed-matter terms (dynamic structure factor, loss function, kinematic match). Giustino is measured and authorial. He is good at the one-line physical gloss ("Physically this singularity corresponds to the 'Fröhlich electron-phonon coupling'", G 37), but his syntax is the formal review's.

**Calibration against the book.** Ch. 1 and Sect. 2.1 already match the models in sentence length (median 27 words) and use the right nouns. What they lack is the models' connective tissue. Per 10k words the book has 0 "however" (L 8.0, KL 8.7), 0 "we will", "we can" and "we see" (L 12.6, 13.6 and 2.7), 0 "note that" (L 6.1), 0 "of course" (L 3.6), 0 "indeed" (KL 5.0), 0 "for instance" and 0 "in addition". It also overuses a few words of its own: "so" 47 (L 11), "gives" 39 (L 7), "only" 34 (L 11), "therefore" 12 (L 3), "about" 26 (L 5), "of order" 7.7 (L 0) and "threshold" 28 (KL 9.5). The result is correct but airless, a run of flat assertions joined by "so" and "therefore". Restoring the models' connectives, and their habit of saying why before saying what, is most of the job.

---

## 2. Terms of art

"Use as" is how the models use the term. "Avoid" lists what the book should not write instead. Where NOTATION fixes a symbol, the term still follows the field.

| # | Term | Use as (quoted example, page) | Avoid |
|---|---|---|---|
| 1 | **heavy mediator** | the limit F_DM → 1; "the heavy mediator limit corresponds to a contact interaction" (KL 13) | "contact-limit regime", "short-range case", "the m_V ≫ q regime" as a name |
| 2 | **light mediator** | the limit F_DM → (q₀/q)²; "for both scattering through a heavy vector mediator and a light vector mediator" (L 65); "If the mediators are sufficiently light, this further modifies the recoil spectrum to favor lower energy recoils" (L 58) | "long-range regime", "Coulomb-like regime" as a name |
| 3 | **massless mediator limit** | the idealized light-mediator limit; "Taking the massless mediator limit, there is an additional momentum-transfer dependence" (L 74) | "zero-mass case" |
| 4 | **contact interaction** | what a heavy mediator gives; "sensitive to single phonons produced from a DM-nucleus contact interaction" (KL 31) | "pointlike coupling", "delta potential" in prose |
| 5 | **weighted toward small q** | the effect of a light mediator; "the rate integral is weighted toward the smallest kinematically-allowed momentum transfers" (KL 16) | "low-q dominance is obtained" |
| 6 | **momentum transfer** | always the full noun; "q is the momentum transfer" (L 46) | bare "transfers", "the transfer" for q (the book has 20) |
| 7 | **maximum momentum transfer** | "There is a maximum momentum transfer" (L 46) | "the largest transfer" |
| 8 | **energy deposited / energy deposition** | the field's word for ω > 0; "It is worth emphasizing that this is just a typical energy deposition" (L 61) | "energy given to the target" as a term (keep it only as the book's sign definition, Sect. 7) |
| 9 | **minimum velocity, v_min** | "the minimum velocity vmin required to generate a nuclear recoil" (KL 29) | "the least speed" (the book has 8) |
| 10 | **kinematic match** | the overlap of the DM parabola with a target's dispersion; "The best kinematic match is obtained when" (KL 28); "nuclear recoils are a poor kinematic match" (KL 5) | "kinematic compatibility", "phase-space overlap condition" |
| 11 | **kinematically allowed** | "a new process is then kinematically allowed" (L 21) | "permitted by conservation laws" |
| 12 | **reach** | the lowest cross section, or mass, an experiment can probe; "The reach at low masses is driven entirely by the detector thresholds" (KL 31) | "sensitivity floor", "testable region" |
| 13 | **threshold / low-threshold** | "could be probed with a kg-day exposure in a low-threshold experiment" (L 74) | "detection floor", "minimum detectable deposit" |
| 14 | **exposure** | target mass × time, in kg-day or kg-year; "an exposure of around a kg-day is sufficient to observe a DM signal" (L 65) | "integrated mass-time" |
| 15 | **zero background / background-free** | the idealization behind projections; "Of course, this assumes zero background" (L 74); "the background-free projected limits" (KL 49) | "in the absence of any background events being present" |
| 16 | **dark rate** | events with no deposit; "polluted by a dark rate consisting mostly of charge leakage across the band gap" (KL 76) | "spurious-event rate" |
| 17 | **projection / projected reach** | expected future sensitivity; "the background-free projected limits from a number of theory proposals" (KL 49) | "forecast exclusion" |
| 18 | **rare-event search** | "thermal relic DM experiments are truly rare-event searches" (KL 14) | "low-count-rate experiment" |
| 19 | **thermal target** | the cross section a thermal history predicts; "leading to concrete thermal targets in parameter space" (KL 12) | "relic-motivated value" |
| 20 | **benchmark** | a fixed model point; "A benchmark model of such a new force is a dark photon" (KL 12) | "reference scenario" |
| 21 | **sub-GeV / light dark matter** | "We then turn to sub-GeV dark matter (light dark matter)" (L 1) | "low-mass regime" as a coinage |
| 22 | **dark photon, kinetically mixed** | "A kinetically mixed dark photon is a nearly ubiquitous feature in models of dark sectors" (L 79) | "hidden photon" (older usage, say once) |
| 23 | **form factor (nuclear)** | "which implies that we need a form factor for the DM-nucleus interactions" (L 46) | "coherence factor" |
| 24 | **DM form factor** | the q-dependence of the potential; "a momentum-dependent DM form factor" (KL 13) | "mediator factor" |
| 25 | **reference cross section σ̄_e** | defined at a fixed momentum; "a cross section for DM scattering off a free electron at a reference momentum" (KL 13) | "normalized cross-section", "effective cross-section" |
| 26 | **crystal form factor** | "referred to as the crystal form factor" (KL 61) | "Bloch overlap factor" |
| 27 | **coherent enhancement, A²** | "a coherent enhancement in scattering rates by A2 in the long-wavelength limit" (L 49) | "constructive-sum factor" |
| 28 | **incoherent** | large q, scattering off a single constituent; "as if DM interacted incoherently with an individual electron or nucleus" (KL 16) | "independent-particle regime" |
| 29 | **spin-independent** | "known as spin-independent scattering because it does not depend on the spin of the target nucleus" (L 49) | "scalar-type coupling" |
| 30 | **reduced mass** | "is the reduced mass for the DM-nucleus system" (L 46) | — |
| 31 | **recoil energy / nuclear recoil** | "The deposited energy (recoil energy of the nucleus)" (L 46) | "kick energy" |
| 32 | **many-body effects / physics** | "the necessity of incorporating many-body physics" (L 59); "the scale at which many-body effects become crucial" (KL 16) | "collective corrections" as a coinage |
| 33 | **in-medium effects** | the medium's modification of the mediator; "accounts for in-medium screening effects" (KL 63) | "medium corrections are obtained" |
| 34 | **screening** | "The screening leads to a rough suppression in DM-electron scattering rates" (L 67) | "attenuation by the medium" |
| 35 | **dynamic structure factor S(q, ω)** | "This target response piece is called the dynamic structure factor" (KL 7) | "response kernel" |
| 36 | **loss function, ELF** | "the experimentally-measured loss function or energy loss function (ELF)" (KL 24) | "inverse-dielectric spectrum" |
| 37 | **RPA / Lindhard** | "essentially computing the polarization in a noninteracting gas" (KL 62) | "mean-field dielectric approximation" as a coinage |
| 38 | **plasmon** | "all of the valence electrons in the material are oscillating in phase at the classical plasma frequency" (KL 66) | "collective charge mode" in place of the name |
| 39 | **Landau damping** | "beyond which Landau damping occurs and the plasmon can efficiently decay into electron-hole pairs" (KL 66) | "plasmon decay regime" |
| 40 | **f-sum rule** | "Since the integrated weight of the ELF is constrained by the f -sum rule" (KL 66) | "spectral normalization constraint" |
| 41 | **quasiparticle** | "we should really think of these as quasiparticle excitations" (L 65) | "dressed carrier" |
| 42 | **band gap** | "Semiconductors have typical electron band gaps of around an eV" (L 65) | "excitation offset" |
| 43 | **crystal momentum** | "crystal momentum is conserved only up to a reciprocal lattice vector" (KL 61) | "quasi-momentum" without saying once that the two are the same |
| 44 | **Migdal effect** | "producing a charge excitation from a nuclear interaction … is known as the Migdal effect" (KL 68) | "recoil-induced ionization" as a name |
| 45 | **sudden (approximation)** | "fast compared to response of electronic orbitals" (KL 70) | "instantaneous-kick limit" |
| 46 | **impulse approximation** | "relies on an impulse approximation to treat the recoiling ion wavefunction as a plane wave" (KL 74) | "free-recoil assumption" without the name |
| 47 | **phonon-assisted** | a transition that needs a phonon for crystal momentum; "it is responsible for phonon-assisted optical transitions" (G 48) | "phonon-mediated indirect step" |
| 48 | **single-phonon / multiphonon** | "which allows for single-phonon creation" (KL 27); "we enter the multiphonon regime" (KL 30) | "one-quantum lattice excitation" |
| 49 | **acoustic / optical phonon** | "The gapped optical phonon mode typically has energies of 10–100 meV in crystals" (L 76) | "zone-center gapped mode" as a name |
| 50 | **Goldstone mode** | "the acoustic phonon is a Goldstone boson associated with spontaneous breaking of translational symmetry" (L 69) | — |
| 51 | **long-wavelength limit** | "which is the dynamical ion charge in the long-wavelength limit" (KL 38) | "small-q asymptotic regime" |
| 52 | **Born effective charge, polar material** | "The Born effective charges are nonzero for polar materials" (KL 39) | "ionic charge" for Z* |
| 53 | **Fröhlich coupling** | "Physically this singularity corresponds to the 'Fröhlich electron-phonon coupling'" (G 37) | "polar long-range term" as a name |
| 54 | **Debye–Waller factor** | "which roughly speaking accounts for the effect of the zero-point motion of the ions in the lattice" (KL 26) | "thermal smearing factor" |
| 55 | **zero-point motion** | "a typical 'zero-point' motion of the ions in the lattice" (L 73) | "ground-state jitter" |
| 56 | **displacement energy** | "well in excess of any displacement energy" (KL 28) | "binding threshold of the lattice" |
| 57 | **harmonic approximation** | "one begins by making the harmonic approximation" (G 8) | "quadratic truncation" as a name |
| 58 | **adiabatic (Born–Oppenheimer) approximation** | "In the adiabatic approximation the nuclei are considered immobile during characteristic electronic timescales" (G 22) | "clamped-ion picture" without the name |
| 59 | **dynamical matrix, force constants** | "The Fourier transform of the interatomic force constants yields the 'dynamical matrix'" (G 8) | "stiffness matrix" |
| 60 | **frozen-phonon vs DFPT** | "One disadvantage of the frozen-phonon method is that the supercell may become impractically large" (G 11) | "finite-displacement supercell technique" without the name |
| 61 | **toy model** | "the discussion here will center on toy models to provide intuition for the relevant many-body physics" (L 59) | "simplified illustrative system" |
| 62 | **absorption** | "similar to the photoelectric effect, where bosonic DM is absorbed to create electron and phonon excitations" (L 77) | "full-energy capture" |
| 63 | **daily modulation** | "daily modulation is mainly a threshold effect" (KL 60) | "diurnal variation" (the field rarely says this) |
| 64 | **neutrino floor** | "along with the neutrino floor and the thermal target parameter space" (KL 35) | "irreducible coherent background" alone |

---

## 3. Characteristic moves

**3.1 A parametric estimate before the exact result.** The estimate comes first and is labeled as an estimate. The exact result follows and is checked against it.
- "let us start by dropping the left-hand-side of the equation above, and estimating the momentum transfer as" (L 60)
- "we can do a quick and dirty calculation to obtain the 'miraculous' thermal relic WIMP annihilation cross section" (L 20); then "we will feel good about getting at the same answer (to an order of magnitude) with not much work" (L 20)
- "This makes explicit the arguments made at the beginning of this section, where we used free electron kinematics" (L 64): this is the check that closes the loop.

**3.2 A physical picture.** A concrete image comes in plain verbs, often with a contrast against the naive picture.
- "Our idealized picture of a free, nearly-at-rest particle just waiting for an incident DM particle to provide some excitement is hardly reflective of reality." (L 59)
- "As q → 0, all atoms are displaced by the same amount" (L 69); "the out-of-phase oscillations in an optical phonon can be viewed as oscillating dipoles" (L 77)
- "This can intuitively be understood by recalling that the dielectric function of the homogeneous electron gas diverges" (G 23)

**3.3 Motivating a calculation.** Say what we want to learn, or which figure we want to understand, before starting.
- "The relevant physics can be identified if we examine the kinematics of DM-nucleus scattering more closely." (L 45)
- "One of the goals of this lecture will be to understand this figure" (L 59)
- "There are a number of compelling reasons to go beyond nuclear recoils" (L 58); "There are a number of motivations for considering DM couplings" (L 67)

**3.4 Signaling an approximation and its validity.** Name the approximation, say in a clause why it holds, and say what is lost. The tone stays light.
- "The effects are modest for DM with mass above ∼ 10 GeV, so we will not pursue this further." (L 47)
- "This is a good leading approximation, but there are regimes of phase space" (KL 68); "this will easily be valid for nuclear recoils with energy 10 meV or above" (KL 70)
- "The above result captures the qualitative form of the scattering rate, but is only approximate." (L 73); "Obviously this is not always the case, and important exceptions will be discussed" (G 22)

**3.5 Comparing channels.** Give a "compared to X" frame and state the one feature that decides the comparison. The reason comes in its own sentence ("The reason is…").
- "Compared to nuclear recoils, the most important features of electron scattering are that the electron is much lighter than the proton" (L 59)
- "it can be even more advantageous to search for excitations into optical phonons. The reason is that the optical phonon has an approximately constant energy" (L 76–77)
- "Indeed, collective modes like phonons can provide a much better kinematic match to the DM." (KL 28–29); "In polar materials, the DM scattering does not create electron excitations (which have a large gap) but instead creates phonon excitations" (L 67)

**3.6 Handling numbers.** A number comes with "typical", "a few", "∼" or a range, and usually with a verdict on what it means.
- "≃ 50 − 100 events/kg/day" (L 65), followed at once by "Thus, an exposure of around a kg-day is sufficient to observe a DM signal!" (L 65)
- "the momentum spread is about 50 keV" (KL 28); "1/λTF ≃ few keV for a typical materials" (L 67)
- "which is very optimistically ω ≃ meV" (L 74); "an expected rate of O(1) events/min/kg, a sizable rate compared to WIMP experiments!" (KL 61)

**3.7 Closing a section.** End on a consequence, an open problem or a pointer, not on a summary list.
- "This makes the simplest WIMP story more and more difficult to achieve." (L 58)
- "A focused effort in this direction could potentially do much better." (L 65)
- "To summarize, the maximum nuclear recoil energy drops as" (KL 30); "The upshot is that thermal freeze-out scenarios with sharp benchmark values … are excluded" (KL 14)

---

## 4. Idioms and connectives

**Frequencies per 10k words** (approximate; "—" means zero).

| Idiom | L | KL | G | Book now | Guidance |
|---|---|---|---|---|---|
| typical / typically | 15.3 | 11.0 | 1.4 | 5.6 | raise; this is the models' main hedge |
| we will | 12.6 | 12.2 | 1.2 | — | use, without overdoing it |
| we can | 13.6 | 8.9 | 3.7 | — | use |
| we have (found, used, neglected) | 11.2 | 6.6 | 2.1 | 0.5 | use when taking stock |
| we see / we obtain or find | 2.7 / 4.9 | 2.1 / 2.3 | 2.1 / 3.7 | — | use after a result |
| let us | 2.9 | 0.6 | 0.5 | — | occasional; never "let's" (Sect. 7) |
| however | 8.0 | 8.7 | 4.9 | — | use for real contrasts |
| note that | 6.1 | 5.6 | 1.4 | — | use, at most about once a page |
| of course | 3.6 | 1.4 | — | — | use for a caveat the reader expects |
| for instance / for example | 2.2 / 7.3 | 1.4 / 3.3 | — / 7.4 | — / 1.5 | raise |
| indeed | 1.5 | 5.0 | 0.9 | — | occasional |
| in addition / furthermore | 2.7 / 1.7 | 3.1 / 1.7 | 1.6 / 1.2 | — | occasional; prefer "also" |
| as a result | 2.2 | 0.4 | 2.1 | — | use in place of some "so" |
| meanwhile (for contrast) | 2.2 | 0.2 | — | — | occasional |
| as before / again | 1.7 / 2.7 | 1.0 / 2.1 | — | — / 0.5 | use to tie a step to an earlier one |
| since (causal) | 13.9 | 14.1 | 9.5 | 4.1 | raise; the models give reasons in subordinate clauses |
| roughly / roughly speaking | 1.5 / 0.2 | 0.6 / 0.2 | 0.2 / — | 0.5 / — | use |
| order of magnitude | 1.2 | 0.6 | — | 0.5 | use |
| a few | 5.4 | 1.4 | 2.3 | 12.8 | the book is already high; do not add more |
| parametrically | — | 1.0 | — | — | use for scalings |
| the upshot | — | 0.6 | — | — | occasional, at a section's turn |
| in practice | — | 0.8 | 1.2 | — | use for computational remarks |
| it turns out | — | — | 0.2 | — | rare; avoid as filler |
| to see this / for concreteness | — | — | — | 0.5 / — | the skill's examples are absent from the models; at most once a chapter |
| sufficiently (light, low) | 4.1 | 1.4 | — | — | use for validity statements |
| suppressed / suppression | 5.6 | 2.3 | 0.2 | 1.5 | use: the field speaks of suppression and enhancement |
| remarkably, interesting, exciting | 0.5, 2.9 | 0, 1.4 | 0, 1.9 | — | rare; a book can afford one per chapter |
| exclamation marks | 23 in total | 33 in total | 1 in total | 2 | at most one per chapter, in a worked example |

**The book's own tics, to reduce.** "so" 47 (L 11), "gives" 39 (L 7), "only" 34 (L 11), "therefore" 12.3 (L 2.9), "about" 26 (L 5), "of order" 7.7 (L 0), "the least" 4.1 (L 0.2), bare "transfers" 10.2 (KL 2.5), "we call" 2.6 (L 0). Lin writes "∼" or "typical" where the book writes "of order". She writes "since" and "because" where the book writes "so". She writes "is" or "leads to" where the book writes "gives".

**Constructions the models avoid, or that the book should avoid even where a model uses them.**
- "thereby" (L 0, KL 0), "whereby" (L 0.5, KL 0; G 3.0), and "respectively" pairings (L 0.7; KL 2.3; G 3.0). Do not write them.
- "in order to" (L 3.4; G 12.7). The skill forbids it; write "to".
- "it is easy to see" and "it is straightforward to show" are absent from L and KL. Banned in the book.
- "one obtains" and "one finds" (G 2.1; L 0.2). Write "we find".
- Chains of "hence" and "thus". The models use "thus" 6–9 times per 10k words, but not in chains. The book follows the skill and keeps "thus" and "hence" below the models' rate.
- "i.e." and "e.g." occur in the models rarely, mostly inside parentheses (L 5 and 3 times; KL 1 and 2). The book writes "that is" and "for example" (Sect. 7).
- Narrating an equation symbol by symbol. The models give one sentence on what the expression means ("The integral is proportional to a Fourier transform of the density field. Thus a DM scattering creates a density excitation", L 71).

---

## 5. Ten before → after rewrites

Each "before" is quoted from the current text. Each "after" keeps the physics, the numbers, the macros and the cross-references.

**R1. Abstract opener → concrete content** (s1-1.tex, l. 13)
- *Before:* This section fixes the local density and the cosmological abundance of dark matter that the rest of the book uses, and explains why masses between a keV and a GeV are both open and suited to solid-state detectors.
- *After:* What gravity does give us is the two numbers the rest of the book uses, the local density and the cosmological abundance, and a reason to look between a keV and a GeV: that window is still open, and its kinetic energies match the excitations of a solid.

**R2. "We call …" → the field's name, given in passing** (s1-1.tex, l. 71)
- *Before:* We call particles with $m_\chi$ between a keV and a GeV \emph{light dark matter}.
- *After:* Particles in this window, between a keV and a GeV, are what the field calls \emph{light dark matter}, or sub-GeV dark matter.

**R3. Outline opener → motivation, with the field's term** (s1-3.tex, l. 3)
- *Before:* This section derives the energy a slow particle can give to a target at a given momentum transfer, the least speed it needs to do so, and the lightest mass that can cross a detector threshold.
- *After:* Kinematics alone already tells us a lot: how much energy a slow particle can deposit at a given momentum transfer, the minimum velocity $\vmin$ it needs to do so, and from that the lightest mass that can get over a detector threshold.

**R4. Bookkeeping sentence → plain motivation** (s1-3.tex, l. 7)
- *Before:* Four terms of \cref{sec:3.1} enter the description of $\vect{q}$ in a crystal, and we give working definitions here.
- *After:* In a crystal, $\vect{q}$ brings some lattice vocabulary with it; \cref{sec:3.1} develops it properly, and for now four working definitions are enough.

**R5. Coined term → the field's term, with the book's sign rule said once** (s1-3.tex, l. 21)
- *Before:* We call $\omega$ the \emph{energy given to the target}; all of the target's physics is in which pairs $(\vect{q}, \omega)$ it can absorb, and with what probability.
- *After:* We write $\omega$ for the energy deposited in the target. In this book it is defined as the energy given to the target, so it can be negative at $T > 0$. All of the target's physics then sits in which pairs $(\vect{q}, \omega)$ it can absorb, and how often.

**R6. "Of order" and a flat list → the model's picture and hedge** (s1-3.tex, l. 21)
- *Before:* A target in a solid is not a free particle at rest. Electrons are bound and move with momenta of order $\alpha m_e$, and nuclei are tied to a lattice.
- *After:* The free particle at rest is an idealization, and in a solid a poor one: electrons are bound, with typical momenta $\sim \alpha m_e$, and nuclei are tied to a lattice.

**R7. Generic "regimes" → heavy and light mediator** (s1-4.tex, l. 30)
- *Before:* \Cref{eq:1.4-Vq} has two regimes. If $m_V$ exceeds every relevant $q$, $\tilde V$ is a constant and the interaction acts as a contact interaction. If $m_V$ is below every relevant $q$, $\tilde V \propto 1/q^2$, as for Coulomb scattering, and small momentum transfers dominate.
- *After:* \Cref{eq:1.4-Vq} has two limits, which the field calls the heavy- and light-mediator limits. For a heavy mediator, with $m_V$ above every relevant $q$, $\tilde V$ is a constant: a contact interaction. For a light mediator, with $m_V$ below every relevant $q$, $\tilde V \propto 1/q^2$, as in Coulomb scattering, and the rate is weighted toward the smallest momentum transfers.

**R8. Bureaucratic disclaimer → plain statement** (s1-4.tex, l. 128)
- *Before:* Their couplings to electrons are stated below as results of the cited references, with equation numbers; this chapter derives none of them.
- *After:* We quote their couplings to electrons from the literature, with equation numbers, and do not derive them here.

**R9. Outline opener → the question the section answers** (s2-1.tex, l. 3)
- *Before:* This section derives that rate, Fermi's golden rule, states the window, and fixes the normalization of states in which every later rate is written.
- *After:* To see how a rate emerges, and when the idea stops making sense, we derive Fermi's golden rule; along the way we fix the normalization of states that every later rate uses.

**R10. A stacked validity condition → the catch, then the reasons** (s2-1.tex, l. 68)
- *Before:* The step is valid when $t$ is long compared with the inverse energy scale of the continuum, short compared with the inverse level spacing, and short enough for first order to hold.
- *After:* The catch is that $t$ has to sit in a window. It must be long compared with the inverse energy scale of the continuum, so that energy is resolved; short compared with the inverse level spacing, so that the levels still look continuous; and short enough that the initial state is barely depleted, so that first order holds.

---

## 6. Checklist for writers and prose reviewers

1. **Opening.** The first sentence of a section states a physical question, a number or a result, not a plan. Where an outline seems needed, put a "we will…" sentence after the motivation (R1, R3, R9).
2. **Field terms.** Use heavy and light mediator, momentum transfer (never bare "transfer"), energy deposited, minimum velocity, reach, threshold, exposure, kinematic match, screening, in-medium, dynamic structure factor, loss function, Migdal effect, phonon-assisted, and the other entries of Sect. 2. Coin nothing that table already names.
3. **Estimate first.** Before an exact result, give the parametric estimate in a sentence ("the rate scales as …", "∼ a few eV"). After it, give the check ("this makes explicit…").
4. **Picture.** Each new mechanism gets one plain-verb image ("all atoms move together", "the electron cannot follow"), then the formula.
5. **Approximations.** Name each one, give in a clause why it holds, and say what is lost. Phrase validity with "sufficiently", "as long as" or "for …", not as a stacked list (R10).
6. **Comparisons.** Write "Compared to X, …", give the deciding feature, and then the reason in its own sentence.
7. **Numbers.** Hedge with "typical", "∼", "a few" or a range, and add a verdict ("which is sizable", "an enormous challenge"). Keep the book's exact digits in worked examples (Sect. 7).
8. **Connectives.** Use "however", "note that", "of course", "for instance", "since" and "as a result" where a real contrast, caveat or reason is present. Cut "so", "therefore", "gives" and "only" wherever they chain. As a rough target, in 1,000 words: at least one "however" or "but", at least one "we will", "we can" or "we see", and no more than three "so".
9. **Forbidden constructions.** No "thereby", "whereby", "respectively" pairings, "in order to", "it is easy to see", "one obtains", "i.e." or "e.g.", and no chains of "hence" or "thus".
10. **Equations.** One sentence on what an equation means. Do not narrate it symbol by symbol.
11. **"We call".** Introduce a term the way the field uses it ("what the field calls …"), not by fiat (R2, R5).
12. **Closing.** End a section on a consequence or a pointer to the next question, never on a list of contents.
13. **Calibration.** For each section, take two or three passages and ask whether Lin, or Kahn and Lin, could have written them. If not, rewrite one sentence as in Sect. 5.

---

## 7. Where the book deliberately differs from the models

- **Notation: NOTATION.md wins.** The book writes ζ for kinetic mixing (the models write κ or ε). It writes q from the dark matter to the target, and ω as the energy given to the target, which can be negative at T > 0. It writes σ̄_e, F_DM and η(v_min), where nuclear-recoil papers write g(v_min). Where the book's symbol differs from the models', say once what the literature writes (as s1-4 does for ζ), then use the book's symbol. In prose "energy deposited" is fine wherever ω > 0.
- **Spelling and abbreviations.** The book writes "dark matter" in full (0 occurrences of "DM", against hundreds in L and KL). It writes "cross-section" with a hyphen, in American spelling with Springer conventions. It names the defined term "light dark matter" and may gloss it once as "sub-GeV".
- **No exercises, and nothing left to the reader.** Lin delegates steps ("Exercise: …", "As an exercise, you can check…", "The exercise is left to the reader", L 50, 64, 69). The book writes every step out, in the text or in Appendix D. The book never addresses the reader as "you". It uses no contractions ("Let us", never "Let's", which L 20 and 74 use), and no "I" (Lin's acknowledgments do).
- **Derivation density.** The book is more complete than lecture notes. Where Lin writes "we will gloss over some of the details and instead refer the interested reader" (L 72), the book derives the result, or puts it in a `limitbox` with its source equation, the chain of approximations, its validity and the leading correction. The voice stays the same: the estimate and the picture come first, then the full derivation.
- **Numbers.** Worked examples carry the digits the calculation produces. In a computation the book keeps its digits (2.650×10⁻³, 0.333 MeV) where Lin would write "≃". In running prose, and in estimates before a derivation, the book uses the models' hedges.
- **Connectives below the models' rate.** The skill forbids "in order to", "whereby" and chains of "thus" and "hence", all of which L and G use. The book follows the skill and keeps "thus" and "hence" below Lin's rate (5.8 and 0.7 per 10k words).
- **"i.e." and "e.g."** The models use them, rarely; the book writes "that is" and "for example".
- **Citations.** The book cites the specific equation (`\cite[Eq.~(9)]{…}`). The models cite whole references.
- **Enthusiasm.** Lin's exclamation marks and "But wait" suit a lecture. The book allows one per chapter at most, in a worked example or a closing sentence.

## Moves Lin never makes (calibration, 2026-11-03)
Figurative stand-ins for technical words ("pull", "silence", "fingerprint", "the data tell us"), and stacked negations that delay the positive statement ("never … anything except"). See prose-review pattern 25.
