# Binding round, second pass: ch15 (Superconductors)

Brief: briefs/volumes/BINDING.md (with the calibration and the table-cell note). Inputs: the first-pass log ch09-ch15.md and the review review-vol2c.md. The review measured 3.0 misses per 1000 words in unchanged ch15 text. Base for invariant.py: 60cc72c. I reread every paragraph of tex/ch15/*.tex in full: body, captions, key-result and Limit Check boxes, worked examples, the prose cells of tab:15-disorder and tab:15-nuisances, and the Summary. The reviewer's fixes (s15-1:27, s15-1:100, s15-3:105, s15-3:138, s15-4:38, and the two nuisance-table cells) are kept unchanged.

## Main fix: the two edges

s15-1:3 defines two objects: the **kinematic edge** $q = \omega/v_{\mathrm{max}}$ and the **pair-breaking edge** $\omega = 2\Delta_{\mathrm{BCS}}$. Every bare "the edge" in the chapter now carries one of these two names, decided by the physics of its sentence:
- Kinematic edge: s15-1:93 (two uses), 108 (two), 115, 118, 121 (two); s15-2:3, 16 (two), 20, 55 (two), 57, 71, 73 (two), 75 (two); s15-3:95; the two s15-2 subsection titles.
- Pair-breaking edge: ch15.tex:4 (three uses); s15-1:104, 123, 137; s15-2:57 ("just below the gap", see below), 73 (two); s15-3:136; s15-4:32, 38, 83, 86 (two), 98, 124 (two), 128 (three), 132, 134 (two), 136 (two); the tab:15-nuisances cell "tilt near the edge"; summary:3 and summary:7.
- A third referent, found in s15-3 and not listed in the review: the caption of tab:15-disorder said "The pair-breaking edge is $q = 2\Delta_{\mathrm{BCS}}/v_{\mathrm{max}}$", and s15-3:134 said "At the pair-breaking edge … There $q = …$". Both made the name a momentum. Now: "The row for the pair-breaking edge uses $q = …$, the smallest momentum transfer at which …", and "The smallest momentum transfer on the pair-breaking edge is $q = …$". The math items are unchanged.

Names kept as fixed compounds:
- "edge momentum": always the momentum on the kinematic edge. The pair-breaking edge has no momentum of its own, so the compound cannot mean the other edge.
- "edge remainder": a named nuisance, used in the text, tab:15-nuisances and the Summary.
- "gap edge" (s15-4:20): the quasiparticle spectrum at $E = \Delta$, a different object.
- The label tab:15-edge.
- "the threshold": s15-1:3 ties it to the pair-breaking edge.

The tab:15-nuisances caption still defines "edge" as the kinematic edge. Its only remaining bare use, "impurities on the edge", is the kinematic edge.

## Per file

| File | Ranker before | Ranker after | Sentences changed |
|---|---|---|---|
| ch15.tex | 5 | 4 | 5 |
| s15-1.tex | 56 | 53 | 18 |
| s15-2.tex | 24 | 20 | 20 |
| s15-3.tex | 75 | 74 | 7 |
| s15-4.tex | 90 | 89 | 20 |
| s15-summary.tex | 7 | 7 | 2 |
| **Total** | **257** | **247** | **72** |

"Sentences changed" counts the sentences of the new text that do not occur in the old text, titles included. A split counts twice.

## 15 instructive changes

| file:line | before | after | failure fixed |
|---|---|---|---|
| s15-2:57 | "the Anderson–Bogoliubov pole … lies just below the gap, at 1.927, 1.966 and 1.992 Δ" | "… lies just below the pair-breaking edge, at …" | one name, two referents: the values are below 2Δ, not below Δ (wording, not physics) |
| s15-2:73 | "δE = 2δΔ moves the edge, and at fixed ω it moves y. … a tilt that acts only near the edge … The third is the edge remainder" | "moves the pair-breaking edge, and at fixed ω a change of the gap moves y. … only near the pair-breaking edge … edge remainder" | one paragraph used "edge" for both edges; *it* had two candidates |
| tab:15-disorder caption | "The pair-breaking edge is $q = 2\Delta/v_{max}$, the smallest momentum transfer …" | "The row for the pair-breaking edge uses $q = …$, the smallest momentum transfer …" | name defined as a third object (a momentum) |
| s15-3:134 | "At the pair-breaking edge the situation is the opposite. There $q = …$ and" | "… The smallest momentum transfer on the pair-breaking edge is $q = …$, and" | same; bare *There* |
| s15-1:108 | "and each truncation is worst on that edge. … gives the values on the edge" | "worst on the kinematic edge … values on the kinematic edge" | demonstrative and bare name |
| s15-1:137 | "The difference between the two factors comes from the edge." | "… comes from the energies near the pair-breaking edge." | bare name; here it means the coherence-factor window above 2Δ |
| s15-3:136 | "Anderson's theorem would keep the clean gap and \cref{eq:15.3-MB} would give the edge." | "… would give the loss function at the pair-breaking edge." | bare name and a missing object (what the equation gives) |
| summary:3 | "the ladder raises that absorption by up to 44 % near the edge" | "… by up to 44 % on the kinematic edge near the threshold" | bare name; 0.44 is the kinematic-edge value at y = 2.2 (s15-1:93), so naming only the pair-breaking edge would claim a maximum over all q |
| summary:7 | "At the edge of a dirty film the condensate short-circuits" | "At the pair-breaking edge the condensate of a dirty film short-circuits" | bare name; preposition kept |
| s15-3:136 | "BCS theory contains neither effect" | "BCS theory contains neither the Altshuler–Aronov effect nor the Finkel'stein mechanism" | *neither* picked from two earlier sentences |
| s15-4:13 | "comes from the sign of the velocity under k → −k, which the density, an even function of k, does not have" | "comes from the velocity, which changes sign under k → −k; the density is an even function of k and does not change sign" | *which* with two candidates; apposition inside the relative clause |
| s15-4:38 | "…, that is a momentum of at most 29.7 or 56.4 eV" | "…, this phonon has a momentum of at most …" | *that* standing for a proposition |
| s15-4:128 | "…is open, but the part competes with the direct term only above about 10 meV, where it tends to its normal-metal value" | "…is open. Above about 10 meV, however, the phonon-assisted part tends to its normal-metal value, and only above that energy does it compete with the direct term." | *it*: the nearest candidate was "the direct term" |
| s15-1:91 | "…agree with the elliptic form to 10⁻¹². It jumps to π/2" | "… The function g_I jumps to π/2" | *It*: the nearest candidate was "the elliptic form" |
| ch15.tex:4 | "the correction that restores it is largest" | "the correction that restores charge conservation is largest" | *it*: candidates were "response" and "charge conservation" |

Other changes:
- s15-1:27: "It therefore creates" became "The phase operator therefore creates" (nearest candidate: the pair creation operator).
- s15-1:41: "The remaining integral" became "The integral over ξ that remains" (definite before introduction).
- s15-1:18: "the bare electron mass" was a dangling list item. It is now attached to v_F.
- s15-1:127: "approach twice it" became "approach twice the bulk value".
- s15-1:130: "Every point" became "Every point (q, ω) that the particle reaches".
- s15-1:139: "lost below it" became "lost below 2Δ".
- s15-2:3: "the edge value" became "the momentum on the kinematic edge" or "the edge momentum".
- s15-2:66: "this excess" became "the excess over the normal metal".
- s15-2:23 and s15-3:95: "the normal state" (in a normalization) became "the normal-state loss function" or "that Mermin loss function".
- s15-3:19: "either" became "either value of the coherence length".
- s15-3:78: "It is within" became "The ratio is within".
- s15-4:3: "the phonon-assisted part reproduces" became "the phonon-assisted absorption reproduces" (a part without its whole).
- s15-4:136: "that channel … that response" became "the amplitude channel … the scalar response".

Considered and left unchanged:
- s15-3:91 "The other branch": there are exactly two branches, and the retarded one is named in the previous sentence.
- s15-4:132 "it is known": the antecedent "the renormalization" is the subject of the previous sentence.
- s15-4:140 "both": picks from the coordinated pair in the same sentence.

## Checks
- `python3 tools/invariant.py 60cc72c tex/ch15/*.tex`: 0 files with a stop. The only notes are repeat counts and cref notes for existing labels (eq:15.1-gI, eq:15.3-sheet, eq:15.4-MB, also noted in pass 1). No intended symbol unification.
- Lint against a baseline taken before editing: no new hits. Two hits that my edits introduced were fixed. A 46-word sentence in s15-1:93 was split at "however.". The title "The conserving response on the kinematic edge" became "Conserving response on the kinematic edge". The s15-3 caption LONG-SENT hit was in the baseline.
- `tools/chapcheck.sh ch15 <scratchpad>/chapcheck`: exit 0, 0 undefined references, 0 multiply defined labels, 3 overfull hboxes > 5pt (the same count as pass 1 and the review).
