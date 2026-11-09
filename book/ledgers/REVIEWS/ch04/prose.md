# Ch. 4 prose review (style, register, standalone)

Scope: tex/ch04/ch04.tex, s4-1 … s4-9; App. D.6–D.12; App. C.5–C.7. Checked against STYLE.md, style-guide.md, prose-review.md and REGISTER.md. Lines are per file. Figs. 4.7 and 4.11 are judged for pedagogy only. No tex edited.

## 1. Lint record (`lint.py --banned BANNED-TERMS.txt`)

| file | hits (blocking) | notes |
|---|---|---|
| ch04.tex | 0 | — |
| s4-1 | 1 (0) | EQ-PUNCT l.37: false positive |
| s4-2 | 4 (0) | TITLE (editor-accepted, see §6); 3 EQ-PUNCT false positives |
| s4-3 | 1 (0) | EQ-PUNCT false positive |
| s4-4, s4-5, s4-6 | 0 | — |
| s4-7 | 12 (0) | 4 EQ-PUNCT FP; 7 LONG-SENT (equations counted as words; real long prose: none); 1 MONOTONY (contour paragraph, l.193) |
| s4-8 | 7 (0) | 1 EQ-PUNCT FP; 6 LONG-SENT, of which **one is real**: the l.3 roadmap sentence (~70 words) |
| s4-9 | 5 (0) | 3 EQ-PUNCT FP; 2 LONG-SENT (l.82 is equation-driven; l.146 ladder sentence is borderline) |
| D-6 … D-12 | 1/0/2/3/2/6/4 (0) | EQ-PUNCT all FP (D-6 l.80 continues the sentence); LONG-SENT equation-driven; D-11 MONOTONY in the T = 0 subsection (no action) |
| C-5/C-6/C-7 | 1/3/1 (0) | LONG-SENT equation-driven |

Every EQ-PUNCT hit is a false positive: the lint does not accept a space before the final period. A separate scan of all displays and `\label` lines found no unpunctuated equation. Banned/forbidden constructions (i.e., e.g., respectively, in order to, thereby, whereby, one obtains, it is easy, you, exercise, let's, ---): **0 hits**. One "essentially" (s4-3:172).

## 2. Verdicts

Approximate prose words (math stripped): 4.1 2.5k, 4.2 2.3k, 4.3 2.8k, 4.4 3.1k, 4.5 3.0k, 4.6 2.6k, 4.7 2.7k, 4.8 3.3k, 4.9 3.5k. The PASS threshold is ≤ 3 minor hits per 1000 words. Any logic error or typo forces REVISE.

| Section | Verdict | Reason in one line |
|---|---|---|
| Opening (ch04.tex) | PASS | Motivational, concrete, one orienting closing sentence |
| 4.1 Kubo formula | PASS | Minor: upright Γ sweep, one undefined weight, one comma splice |
| 4.2 Correlation functions | PASS | Five minor hits |
| 4.3 Causality and sum rules | REVISE | Garbled TRK attribution; outline opener; recap close; obscure Henke sentence |
| 4.4 Screening | PASS | Minor: "modelling", caption duplicate, "of a few", process aside |
| 4.5 Electron gas | REVISE | Self-contradiction on the f-sum rule; "In this section we"; three verification lines; repeated dark-matter verdict |
| 4.6 RPA, local fields, TDDFT | REVISE | "and and"; abbreviated list title; ε∞ triple repeated four times; ladder duplicated in 4.9 |
| 4.7 Green's functions | PASS | Minor: "therefore" chain, absurd 10⁻¹³⁶ in caption, 1.17 vs 1.11 eV |
| 4.8 Feynman diagrams | REVISE | Mechanical roadmap sentence; ordinal "first term"; verification line; "and … and" chain |
| 4.9 Excitons / Summary | REVISE | "labelled"; "In this section we"; count-teasers; claimed equality with D.12 kernels is false until the relabel; summary slips |
| D.6 f-sum rule | PASS | — |
| D.7 Dielectric matrix | PASS | One code-test aside (l.67) |
| D.8 Lindhard function | PASS | Ordinal "first term" (l.12); verification line (l.85) |
| D.9 Mermin | PASS | Repeats 4.5 text verbatim; verification line (l.86) |
| D.10 Imaginary time | REVISE | Three verification paragraphs (l.37, l.67, l.71) are process artifacts |
| D.11 Wick and rules | PASS | Wrong Bruus–Flensberg chapters (editor item) |
| D.12 Bethe–Salpeter | REVISE | Kˣ/K̄ˣ naming contradicts 4.9 (editor ruling unapplied); verification paragraph l.130 |
| C.5 Complex analysis | PASS | `v_C` without \mathrm (l.60); KK cites Kronig only (l.42) |
| C.6 Gaussian/oscillator | PASS | l.83 sentence with two semicolons and a redundant attribution |
| C.7 Matrix tools | PASS | `v_C` without \mathrm (l.54) |

## 3. Issues by section (location → problem → fix)

### 4.1 (PASS)
- l.114–181 (WE 4.1, Fig. 4.1 caption, causality text): 8× `\Gamma_{\mathrm{w}}` upright → STYLE Γ rule: rates are `\varGamma` (as in 4.3–4.5) → replace all 8.
- l.82–92: `p_i` first used in Lehmann sum without a definition here → add "with Gibbs weights $p_i = \ee^{-\beta E_i}/\mathcal{Z}$" at l.21 or l.82.
- l.143: "Two facts were used, causality, which …, and stability, which …" → comma splice. Use a colon: "Two facts went into this: causality, which …, and stability, which …".
- l.35: a long parenthesis redefines **G** ("a vector of the lattice of wavevectors on which …") → shorten to "(\cref{sec:3.1})"; G is defined in Ch. 3.
- l.114/126, l.167: editor renames still pending (M → oscillator mass symbol, λ → λ_osc, Δ → Δ_tl; see §6).
- l.3: "The treatment follows Refs. …" closes 6 of 9 section openings (4.1–4.4, 4.7, 4.8) and is absent from 4.5, 4.6 and 4.9. That is a writer tic, and the openings are inconsistent → move it to the end of the first subsection, or drop it where the citations already appear at the point of use.
- cal: l.3 yes · l.143 no · l.176 (two-level physics) yes. Rewrite: "Two facts went into this: causality, which cuts the integral off at t = 0, and stability, which keeps R(q,t) from growing."

### 4.2 (PASS)
- l.58: "In a uniform gas it cancels most of the one" → "the one" means the self term "1", and the reader stumbles → "cancels most of the self term".
- l.86: "the code computes $R_{ee}$" → no code has been introduced, so this reads like an internal label → "a first-principles calculation computes".
- l.158: "With fixed nuclei it deposits nothing" → "it" has no clear antecedent → "With fixed nuclei the elastic term deposits nothing".
- l.29/l.46: Van Hove is credited twice in 17 lines → keep one.
- l.25: "For the rest of this section the density element carries the physics, and the matrix returns when we prove positivity." → empty signpost (pattern 1) → cut.
- cal: l.29 yes · l.102 yes · l.58 no. Rewrite: "In a uniform gas, however, the pair term cancels most of the self term, because each electron digs a hole in the density of the others."

### 4.3 (REVISE)
- l.135: "Thomas, Reiche and Thomas, and Kuhn found it in 1925" → reads as a garbled list → "It was found independently in 1925 by Thomas, by Reiche and Thomas, and by Kuhn, before …".
- l.3: three outline sentences ("We will derive both … We will also see … then serves as a check on …") follow a good concrete opener → keep the first three sentences, then add one "we will" sentence naming what the reader will be able to test.
- l.3 vs ch04.tex l.3: "Nobody knows the exact excited states of silicon" echoes "nobody can write down the exact states" → vary it: "No calculation has the exact excited states of silicon, yet …".
- l.98: "in a representative silicon calculation it and the truncation of the band sum together leave …" → "it and" is awkward → "In a representative silicon calculation, this term and the truncated band sum together put the computed sum 12 to 19 percent below the local value at small q."
- l.170: "in tables now distributed from lower energies, which we use above 30 eV" → unclear, and process-flavored → "Their current distribution extends to 30 eV, and we integrate it from there."
- l.186: the close restates the three results as a list ("The Kramers–Kronig relations tie …, the f-sum rule fixes …, and the oscillator strengths …") (pattern 5 / REGISTER 3.7) → cut that sentence; keep the opening clause and the pointer to 4.4.
- l.158: "numerically the total is πn_eq²/m_e to 10⁻⁶ from q = 0.1 to 4 k_F" → verification log (see §5) → cut.
- l.142: η here is the Coulomb parameter, but in 4.1 l.63 η is the switching rate → one symbol, one meaning → rename this one (e.g. η_C). 4.2 l.22: ω_q is used undefined → add "(the energy deposited at q, \cref{sec:2.5})".
- l.150: "at energies of order E_B" → REGISTER tic → "at energies ∼ E_B".
- l.172: "essentially complete" → "complete to 2 percent" or "complete".
- cal: l.3 (first sentence) yes · l.98 no · l.148 yes. Rewrite: as for l.98 above.

### 4.4 (PASS)
- l.202: "modelling" → "modeling" (American).
- l.3: "screening effects of a few in the rate" → "screening changes the rate by a factor of a few".
- l.43: "the relations … used ahead of time in App. A.7" → reads like a process note → "the relations stated in App. A.7".
- l.143: "Gaussian sources write" → "Texts in Gaussian units write".
- l.178: "The three forms of Eq. (4.4.x) agree, as they must." → reassurance aimed at a reviewer (pattern 19) → cut.
- l.185: "Weighting each transfer in the rate" → bare "transfer" (REGISTER #6) → "each momentum transfer".
- l.101 (Fig. 4.5 caption): "Dashed: the single damped oscillator … (dashed)" → remove the second "(dashed)".
- l.134: "at energies of the order of ω_p" → "at energies ∼ ω_p".
- cal: l.3 yes · l.90 yes · l.178 no. Rewrite: cut the sentence and end with "…is reduced by $|\varepsilon_{\mathrm{TF}}|^2 = 4.9$, the factor of five quoted at the start."

### 4.5 (REVISE)
- l.148 vs l.153: "A static potential, the long-wavelength limit and the f-sum rule tell the two prescriptions apart" contradicts "Finally, the f-sum rule does not distinguish the two" → "A static potential and the long-wavelength limit tell the two prescriptions apart; the f-sum rule does not." (D.9 l.70 already has it right.)
- l.3: "In this section we evaluate …, screen it …, and follow … We then add collisions …" → pattern 1 and a mechanical roadmap → one sentence on what the reader will be able to compute (the plasmon, its cutoff, and where dark matter sits on the (q, ω) plane).
- l.74, l.117, l.153: "numerical integration … reproduces it to 10⁻⁵" ×3 → verification logs (§5) → keep l.117 (the plasmon's share of the f-sum is physics) and cut the other two.
- l.128: "It also shows the line ω = qv_max" → unanchored "It" → "The figure also shows".
- l.128 and WE 4.x l.174: "the plasmon is kinematically inaccessible" is stated twice, with the same numbers (6.27 keV) → keep it in the WE and shorten l.128 to a pointer.
- l.172: "the crystal supplying through its potential the momentum that the gas would need q > q_c to provide" → hard to parse → "the crystal potential supplies the momentum that, in the gas, only q > q_c could provide."
- l.3 vs l.168/l.170: "right to about one percent" vs "1.8 percent higher" vs "survives to two percent" → say once what is compared (the peak, 16.4 vs 16.6 eV, 1.2 percent) and keep the WE's zero-crossing figure.
- Limit box l.98: `\cite[Eq.~(171) and the text after it]` → `\cite[Eq.~(171)]` (the cutoff is stated in the box itself).
- l.80 uses u for the slab displacement, while l.36 in the same section uses u for an angle cosine → use a different symbol for the displacement (e.g. s).
- cal: l.3 (first four sentences) yes · l.80 yes · l.148 no. Rewrite: see the first item.

### 4.6 (REVISE)
- l.143: "$\varepsilon_\infty = 10.22$, and and with 113 vectors" → typo.
- Title l.1: "RPA, local fields and TDDFT kernels" → undefined abbreviations and a three-item list (STYLE: short noun phrase) → "Local fields and exchange–correlation kernels". TDDFT also appears unexpanded at l.121 → write it out.
- l.3: "In this section we build …, screen it …, and add …" → pattern 1 → cut, or reduce to one "we will" clause after the motivation.
- ε∞ = 11.45 / 10.22 / 10.81 appears at l.62, l.108, l.140 and in WE l.143, then again in 4.9 l.146 and the Summary → state it in the WE and point to it elsewhere.
- l.136–140 "The ladder of approximations" nearly duplicates 4.9 l.142–146 → keep the rung list in 4.9 only, and end 4.6 with the two-sentence uncertainty statement (l.140).
- l.138: "The order is not an expansion in a small number. … The rungs are therefore not a series whose next term bounds the error." → restatement → merge into one sentence (see cal).
- l.143: "with 113 vectors it is the same to three digits … All three numbers change by less than 0.1 percent between an 8³ and a 20³ grid" → convergence assurance (§5) → move to the Fig. 4.7 caption or App. E.6.
- l.11/l.14: "the spin sum gives a factor of two", "2/V" → editor ruling: g_deg throughout Ch. 4 (§6).
- l.3: "honestly quote" → "quote".
- Register: 0 "however" and 0 "we will/can/see" in the whole section, the lowest in the chapter.
- Fig. 4.7 (pedagogy): the caption stands alone, and panel (b) usefully overlays the unscreened ε₂. Its 0.10 eV broadening and 59-G cutoff details are fine. No change.
- cal: l.60 (capacitor picture) yes · l.99 yes · l.138 no. Rewrite: "The order is not an expansion in a small number: each rung adds a physical effect whose size depends on material, energy and momentum, so no rung bounds the error of the one below."

### 4.7 (PASS)
- l.63: "The addition poles therefore sit … The time-ordered function therefore equals …" → "therefore" chain → second one: "As a result, the time-ordered function equals …".
- l.114: "a triangle of area ξ²/2, and Γ ∝ ξ², and Γ/ξ → 0" → "and … and" chain → "…of area ξ²/2, so Γ ∝ ξ² and Γ/ξ → 0 as ξ → 0."
- l.121: 1.17 eV (measured) here, while 4.2–4.6 use 1.11 eV → add "(at low temperature; 1.11 eV at 300 K)".
- l.148 caption: "two bound states lie within 10⁻¹³⁶ eV of the band edges" → absurd precision distracts → "exponentially close to the band edges". "It agrees with a direct diagonalization … with 2000 band states" → cut (§5).
- l.142: "the sum rule ∫A_dd = 1 holds to within 10⁻⁶ in the band" → cut (§5).
- l.22: "and the result is the following." → weak lead-in → "and both enter with a plus sign:".
- `\mathsf{A}` throughout → editor: macro `\SpecA` (§6).
- \SI{}{\percent} here and in 4.8, but the word "percent" in 4.3–4.6 and 4.9 → pick one chapter-wide.
- cal: l.3 yes · l.114 yes · l.63 no. Rewrite: see the first item.

### 4.8 (REVISE)
- l.3: "Then we use them on the four diagrams …: the bubble and its random-phase chain, which give …; the self-energy …, which …; the screened interaction …, which …; and the ladder, which …" → a ~70-word mechanical roadmap (pattern 18) → "We then use them on the diagrams the rest of the book needs: the bubble chain behind screening, the boson self-energy behind phonon widths, the GW self-energy behind quasiparticle gaps and lifetimes, and the ladder behind excitons."
- l.94: "The first term is the emission of a boson, the second its absorption." → ordinal reference (pattern 13) → "The term with $-\omega_{\vect{Q}}$ in the denominator is emission, the one with $+\omega_{\vect{Q}}$ absorption."
- l.32: "…an even number, and the −1 of each contraction drops out, and the signs left over are …" → "and … and" chain → split into two sentences.
- l.103: "with the chemical potential near the middle of the gap, with the band bottom E_c at 0.5 eV above μ" → "with … with" → "with μ_ch near midgap, 0.5 eV below the band bottom E_c".
- l.112: "A direct numerical frequency sum …, with 2×10⁶ bosonic frequencies, reproduces … to 10⁻⁹" → cut (§5).
- l.106: ℓ(x) is redefined here, while ℓ(w) means the Lindhard log in 4.5 → one symbol, one meaning → rename (e.g. L_b(x)).
- l.88: "we arrive at the result." The same phrase appears in 4.1 l.35 and 4.7 l.72 → vary it.
- cal: l.155 ("An injected electron is thus a dark-matter particle with a Coulomb coupling") yes · l.143 yes · l.3 no. Rewrite: see the first item.

### 4.9 and Summary (REVISE)
- l.7: "labelled" → "labeled".
- l.3: "In this section we write …, solve it …, and put …" → pattern 1 → one "we will" clause.
- l.31: "Three approximations stand behind Eq. (4.9.x)", l.33: "Two limits tie …" → count-teasers (pattern 18) → name them in the sentence: "Behind Eq. (…) stand three approximations, each explicit in App. D.12: the change of W in the kernel is neglected, the rung is static, and pair creation and annihilation are decoupled (Tamm–Dancoff)."
- l.27: "\Cref{eq:4.9-bse} is \cref{eq:D.12-eig} with the kernels of \cref{eq:D.12-crystal}" → false as it stands: D.12-crystal's Kˣ sums over all G, while 4.9's Kˣ omits G = 0. This becomes true only after the D.12 relabel (§6).
- l.66: "a_x ≫ a" → a is not defined here → "≫ a, the lattice constant".
- l.134: "the electronic analog of the LO–TO splitting" → forward term, no pointer → add "(\cref{sec:5.5})" or point to App. D.14 as D.12 does.
- l.142–146: this duplicates the 4.6 ladder (see 4.6). Subsection title "The ladder of approximations, completed" (comma title) → "The completed ladder".
- Summary l.152: "van Hove" → "Van Hove" (as in 4.2).
- Summary l.166: "the coupling α/ε" → "α/ε∞".
- Summary l.156: "insulating below about 1.26 keV" → "about" with three digits → "below about 1 keV" (as in WE 4.x).
- Summary l.160 repeats the ε∞ triple a fifth time → "lowers ε∞ by a tenth, of which the kernel restores half".
- Fig. 4.11 (pedagogy): the caption stands alone and discloses the double counting of the excitonic shift. "(20,736 transitions)" and the solver details belong in App. E.6 → optional trim.
- cal: l.3 ("They do see each other.") yes · l.66 yes · l.31 no. Rewrite: see the count-teaser item above.

### Appendices (merged)
- D.8 l.12: "The first term is an electron leaving …; the second is the antiresonant partner" → ordinal → "The resonant term … the antiresonant term …".
- D.9 l.3, l.23, l.66: repeat 4.5 l.136 word for word ("Collisions with impurities and phonons conserve …", "Electrons are destroyed at the crests and created in the troughs") → keep the text in one place and point to it from the other. l.23: "+ c.c." is outside math mode → move it inside. l.61: `j_e(\vect{q})` → `\vect{j}_e(\vect{q})`, as in 4.3.
- D.11 l.3: `\cite[Chaps.~10 and 11]{bruus2004many}` → 12–14 and 17, as in 4.8 l.3 (editor).
- D.12 l.83/l.114/l.128: K̄ˣ = local-field kernel, Kˣ = full → editor ruling: Kˣ (no G = 0) and Kˣ_full (§6). l.123 cites `eq:A.5-optical`, while 4.6 and 4.9 cite `eq:3.2-optical` for the same vertex → use one label.
- C.5 l.42: cites Kronig only; 4.3 cites both Kronig and Kramers → add `kramers1927diffusion`. l.60: `v_C` → `v_{\mathrm{C}}` (also C.7 l.54).
- C.6 l.83: "which is Bloch's identity; App. D.15 gives a proof; the identity is due to Bloch, and Mermin gave …" → "which is Bloch's identity. App. D.15 proves it; Mermin gave a short alternative derivation [mermin1966short]."
- D.7 l.67: "A random complex proper response … is a convenient test of a code's conventions" → acceptable as a computational remark, but it is phrased as test advice; it belongs in App. E.6.

## 4. Chapter as a whole

**Opening (ch04.tex l.3).** PASS. It is concrete (2.00×10²³ cm⁻³, 16.6 eV), motivational, and asks two questions. It ties back to 2.5 and 1.4, and only the last sentence orients. Not an outline.

**Summary (s4-9 l.148–168).** Good: one paragraph per section, and it closes on the transition to Ch. 5. It restates numbers heavily; see the four fixes under 4.9.

**Redundancy across sections.**
- ε∞ 11.45/10.22/10.81: six occurrences (4.6 ×4, 4.9, Summary).
- The ladder of rungs: 4.6 l.136–140 and 4.9 l.142–146.
- The plasmon being out of reach: 4.5 l.128 and l.174, plus the Summary.
- "nobody knows/can write down the exact states": ch04.tex and 4.3 l.3.
- Mermin's motivation: 4.5 l.136 and D.9 l.3/l.23, verbatim.
- Isothermal vs isolated static response: 4.1 l.112 and 4.7 l.223. These are cross-referenced; acceptable.

**Seams (adjacent pairs).**
- Opening→4.1: smooth ("start from the response to a weak field" → "Apply … a weak potential").
- 4.1→4.2: smooth, but 4.2 l.3 repeats 4.1 l.3's "same operator" point → shorten 4.2's first sentence to the new claim (either one fixes the other).
- 4.2→4.3: smooth (exact constraints).
- 4.3→4.4: smooth (sum rules carried to the loss function).
- 4.4→4.5: smooth.
- 4.5→4.6: smooth.
- **4.6→4.7: weak.** 4.6 ends on the BSE rung "built from the screened interaction of 4.8", and 4.7 starts on quasiparticles with no tie back. Add to the 4.7 opener: "The last rung needs quasiparticle energies and a screened interaction, and both are properties of one added electron."
- 4.7→4.8: smooth (the width needs Σ).
- 4.8→4.9: smooth (ladder → excitons).

**Voice across the nine writers.** The voice is consistent: "we", plain declaratives, worked examples as demonstrations, and nothing is left to the reader (0 exercises, 0 "you"). The differences between writers are mechanical:
- "The treatment follows Refs." appears in 6 openings out of 9.
- "In this section we" appears in 4.5, 4.6 and 4.9.
- Upright Γ appears in 4.1 only.
- \SI{}{\percent} appears in 4.7 and 4.8, the word "percent" elsewhere.
- British spellings are confined to 4.4 and 4.9.

**Standalone scrub and the user rules.** There are no internal labels in the prose, but `sec:4.8-removal` breaks the label scheme (STYLE: sec:N.M); it is invisible in print. "the code" (4.2 l.86) is the only internal-sounding noun. Citations attribute; nothing requires opening a source.
- One borderline case: 4.6 l.134 says the real G_LF "departs from [q²] beyond q ∼ k_F [GV Chap. 5]" without saying how. Add one clause on its actual behavior, for example that it bends over and stays of order one.
- Limit boxes (4.5, two): each has the formula with a one-line citation, a self-contained comparison plot with the validity region shaded, and a closing sentence on breakdown. Compliant.
- Titles: all are short noun phrases except 4.6 (see above). 4.2 is editor-accepted.
- Cross-references: all use \cref. The only hard-coded "Sect. 3.4" strings are citation locators (`\cite[Sect.~3.4]`), which is correct.
- Captions stand alone, with one duplicate word in Fig. 4.5 and the 10⁻¹³⁶ eV in Fig. 4.8b.

## 5. Process artifacts (pattern 19), chapter-wide

These sentences certify that the writer's arithmetic checks out, aimed at a reviewer, not a reader. The rule for this list:
- **Keep** a check when it demonstrates physics or backs a figure: 4.8 WE "cut of the bubble" Monte Carlo (Fig. 4.10b); 4.5 l.117 (the plasmon's share of the f-sum); 4.7 l.142's residue argument (keep the physics, drop "to within 10⁻⁶").
- **Cut, or move to App. E**:
  - 4.3 l.158 ("to 10⁻⁶ from q = 0.1 to 4 k_F");
  - 4.4 l.178 ("agree, as they must");
  - 4.5 l.74 and l.153;
  - 4.6 l.143 (113 G, 8³ vs 20³ grid);
  - 4.7 Fig. 4.8b caption (2000-state diagonalization);
  - 4.8 l.112 (2×10⁶ frequencies, 10⁻⁹);
  - D.8 l.85;
  - D.9 l.86;
  - D.10 l.37, l.67, l.71 (six-level random Hamiltonian);
  - D.12 l.130 (the whole "numerical check pins down the sign" paragraph). D.12 states the sign argument in prose at l.36 already. If a check is wanted, put one sentence in App. E.

## 6. Editor-notes items that concern prose: status

| item | status (evidence) |
|---|---|
| A.7 "the first term" → "resonant term" | **open**: appA/A-7.tex l.17 still reads "only the first term" |
| WE 4.1 M → non-nuclear symbol; λ → λ_osc; Δ → Δ_tl (4.1) | **open**: s4-1 l.114, l.126, l.167–168 unchanged (grep for λ_osc/Δ_tl empty) |
| 4.2 title kept, lint false positive | done (accepted) |
| 4.4 ε₂ sum-rule pointer to 4.8 | done: s4-4 l.114 → sec:4.8-removal; 4.8 l.61–76 justifies it |
| 17.4 eV mean-energy example moved 4.3 → 4.4 | done: s4-4 l.129–134 |
| 4.7: bare G with real argument = time-ordered; tell 4.8 | done: s4-7 l.63, s4-8 l.141 |
| 4.7: macro \SpecA for 𝖠 | **open**: s4-7, s4-8, D.10 use `\mathsf{A}` |
| 4.7/4.8: Fetter–Walecka / Mahan chapter audit | not checked here (citation audit) |
| D.11: Bruus–Flensberg chapters 12–14 and 17 | **open**: D-11 l.3 "Chaps. 10 and 11"; 4.8 l.3 already correct |
| D.12 relabel K̄ˣ → Kˣ, Kˣ → Kˣ_full | **open**: D-12 l.83, l.114, l.128; makes 4.9 l.27 false |
| 4.6/Ch4 spin factor g_deg = 2 throughout | **open** in 4.6 (l.11 "factor of two", l.14 "2/V"); done in 4.9 |
| 4.6 trend (LF lowers ε∞, ALDA restores part) stated with a source | partly: albrecht1998ab and louie1975local are cited for the LF trend (l.62), nothing for ALDA; the ruling's published first-principles values (13.9/12.7/13.3) are not cited |
| 4.9 Fig. 4.11 as labelled model with published BSE cited | done in prose (caption disclosure; albrecht1998ab l.125) |
| 4.5 Mermin causality argument | present: s4-5 l.144, D.9 l.57 |
| 6.3 must cite we:4-einstein | outside Ch. 4 |

## 7. Register (REGISTER.md §4, §6.8) by section

Counts per section, math stripped. Targets per 1000 words: ≥1 "however/but", ≥1 "we will/can/see", ≤3 "so".

| | 4.1 | 4.2 | 4.3 | 4.4 | 4.5 | 4.6 | 4.7 | 4.8 | 4.9 |
|---|---|---|---|---|---|---|---|---|---|
| however | 1 | 2 | 2 | 1 | 1 | **0** | 1 | 1 | 1 |
| we will/can/see | 2 | 1 | 2 | 1 | 1 | **0** | 2 | 2 | 1 |
| typical(ly) | **0** | **0** | **0** | 4 | 2 | 1 | 1 | 1 | 2 |
| so | 7 | 2 | 7 | 11 | 8 | 8 | 8 | 5 | 8 |
| only | 7 | 6 | 10 | 9 | 9 | 8 | 7 | 10 | **17** |
| since (causal) | 5 | 8 | 8 | 5 | 8 | 5 | 9 | 1 | 8 |

Assessment:
- "so" is within target everywhere.
- "however" and "we will/can/see" are at about a third of Lin's rate in every section and absent from 4.6. Add a real contrast or a "we can" where one is present: for example 4.6 l.58, "Note what the head alone does" → "We can now see what the head alone does and does not change".
- "typical" is absent from 4.1–4.3. 4.2 l.29 and 4.3 l.150 are natural places for it.
- "only" in 4.9 is at the book's own tic rate (~34 per 10k). Cut the ones that do not mark an exclusion (e.g. l.35 twice, l.39, l.71).
- Terms of art are used correctly throughout (heavy/light mediator not needed here; momentum transfer, loss function, screening, Landau damping, kinematically, f-sum rule, quasiparticle). The one deviation is bare "transfer" (4.4 l.185).
