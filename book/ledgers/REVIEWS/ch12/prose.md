# Ch12 prose review (style and prose, isolated)

Scope: tex/ch12/ch12.tex, s12-1 … s12-6, appD/D-33.tex, D-34.tex. Checked against STYLE.md, style-guide.md, prose-review.md, REGISTER.md, and the prose items of ledgers/REVIEWS/ch12/editor-notes.md. No tex was edited.

## 1. Lint (lint.py --banned BANNED-TERMS.txt)

| File | Hits | Blocking | Notes |
|---|---|---|---|
| ch12.tex | 0 | 0 | — |
| s12-1 | 5 | 0 | EQ-PUNCT l.58; 4 LONG-SENT |
| s12-2 | 4 | 0 | 4 LONG-SENT |
| s12-3 | 12 | 0 | 12 LONG-SENT |
| s12-4 | 7 | 0 | EQ-PUNCT l.48, l.111; 5 LONG-SENT |
| s12-5 | 6 | 0 | EQ-PUNCT l.22, l.37, l.102; 3 LONG-SENT |
| s12-6 | 11 | 0 | EQ-PUNCT l.43; 10 LONG-SENT |
| D-33 | 5 | 0 | EQ-PUNCT l.41; 4 LONG-SENT |
| D-34 | 4 | 0 | 4 LONG-SENT |

- **All 8 EQ-PUNCT hits are false positives.** The punctuation (`,` or `.`) sits on the last line before `\end{split}` / `\end{gathered}`, and the linter does not see it there.
- **Most LONG-SENT hits are not real sentences.** They come from captions, keyresult openers, limit-box formula lines and table rows that the splitter merges with the next paragraph. The genuine ones:
  - s12-1 l.150, "The boost denominator $\omega_e^2$ must then be replaced by the full one, for a bound nucleus …" (about 60 words). Split after "full one".
  - s12-6 l.196, "The other open items of the chapter are stated where they arise: …" (a five-item list in one sentence). See the 12.6 entry below.
  - s12-6 l.192, "The headline silicon numbers … belongs to the point-ion model of \cref{sec:12.1}." Split at the semicolon.
  - s12-3 l.149 is one paragraph of about 300 words with four jobs: the mass dependence, local exponents, the per-nucleon reading, and conventions. Break it before "Two conventions travel with it".
- No banned terms are hit.

## 2. Verdicts

The density test is minor hits per 1,000 words, where PASS means ≤ 3. Where an editor ruling is still unimplemented, that overrides the test and the verdict is REVISE. No section is REWRITE. The voice is consistent across the six writers: the same "we", the same number-first openers, the same habit of naming the condition behind a number.

| Section | Words | Prose hits | Hits/1k | Verdict | Reason |
|---|---|---|---|---|---|
| Ch. opening (ch12.tex) | 300 | 1 | — | PASS | Minor: three orienting sentences at the end (STYLE allows one) |
| 12.1 | 3.4k | 10 | 2.9 | REVISE | R7 and R15 not implemented; R1 sentence missing or mis-scoped |
| 12.2 | 3.6k | 10 | 2.8 | REVISE | R2 (Fig 12.2 axis) and R5 (Ge exciton) not implemented; the "order of magnitude" seam contradicts 12.3 |
| 12.3 | 4.6k | 14 | 3.0 | REVISE | R9 numbers pending; "Computational connection" heading; G≠G′ wording (R1 conflict) |
| 12.4 | 3.6k | 10 | 2.8 | REVISE | Sentence fragment l.157; l.41 is reviewer-aimed and silently contradicts 12.3 |
| 12.5 | 3.2k | 8 | 2.5 | REVISE | R14 (`\cref{sec:12.6}` → `tab:12-nuisances`) not implemented; R1 attribution |
| 12.6 + Summary | 4.9k | 11 | 2.2 | REVISE | First row of tab:12-nuisances (R1 conflict); restating paragraph l.98; open-items list |
| D.33 / D.34 | 3.0k | 4 | 1.3 | PASS | Minor items listed in Sect. 5 |

## 3. Needs editor ruling (highest priority)

**E1. R1 conflicts with the tex. Do not apply R1 as worded.**
- R1 says lim:12.3a "measures the off-diagonal (G≠G′) elements directly". The tex says the opposite:
  - the lim:12.3a caption (s12-3 l.74): "The elements $\vect{G} \neq \vect{G}'$ are in neither curve";
  - its closing sentence (l.77): "the local fields lower the silicon probability by a factor 1.35; the elements G≠G′ are the next correction".
- So the 35 % is the scalar ε(|p|) against the *diagonal* of ε⁻¹ with local fields. The off-diagonal G≠G′ elements are still unsized.
- These places attribute the 35 % to G≠G′:
  - s12-5 l.67, "drops the off-diagonal elements that \cref{lim:12.3a} shows to be a 35 % effect";
  - the first row of tab:12-nuisances (s12-6 l.172), "Local fields of the electronic response (G≠G′) … about 35 %";
  - s12-6 l.192, "The local fields move the total by a third, and their off-diagonal part is unsized". This one is half right.
- s12-4 l.77 gets it right: "the plain dielectric form is 35 % high … and the elements G≠G′ remain to be sized".
- Related one-sense terminology problem: s12-1 l.129 and s12-3 l.12 say the G≠G′ elements "carry the local fields". Yet lim:12.3a shows the local fields acting through the diagonal of ε⁻¹.
- Proposed wording:
  - "Local fields enter twice: through the diagonal of ε⁻¹, where they lower the silicon probability by a factor 1.35 against a scalar ε (\cref{lim:12.3a}), and through the off-diagonal elements G≠G′, which no table in the book contains yet."
  - Split the nuisance row in two: (a) diagonal local fields, 1.35, computed; (b) G≠G′, named.

**E2. R9: every place that quotes the pending free-recoil numbers.** The prose fix follows the derivation review.
- s12-3 l.3: "it holds down to about \SI{16}{MeV}, below which the electrons take a sizable part".
- s12-3 l.92–101: eq:12.3-bracket, "up to the recoil energy $p^2/2M_\kappa$ in the denominators", the "$3p^2/q^2$" term, "It decides the low masses", and "within 10 % above 16.5 MeV … factor 1.2 at 12 MeV and 2 at 5 MeV".
- lim:12.3b: the caption (gray band "$\mchi \ge \SI{16.5}{MeV}$") and the closing sentence ("Below about \SI{16}{MeV} …").
- s12-3 l.115: "costs more than either in the range above \SI{16}{MeV}".
- s12-5 l.85: "the exact free-recoil bracket of \cref{sec:12.3-validity} adds a correction that reaches about 20 %". This is the 9/5 Doppler term, which survives, but the pointer goes to the bracket that will change.
- D-33 l.64: "together with the exact energy denominator for a free recoil that \cref{sec:12.3} derives".
- s12-4 l.41 is a separate problem (pattern 19): "keeping that difference without the matching $p^2/2M_\kappa$ in both denominators … would introduce an error of relative order $p/q$". It argues with 12.3 without naming it. Once R9 is settled, cut the sentence and let 12.3 state the correct bracket. 12.4 then needs only "None of the three is a ratio p/q."

**E3. The 12.2 → 12.3 seam contradicts itself.**
- s12-2 l.110 says "the atomic valence numbers above serve only as an order of magnitude". s12-2 l.145 says "For the valence electrons the atom gives only an order of magnitude, about 10⁻³ per keV".
- s12-3 l.121 says "The crystal is … 47 times its valence shells", which is more than an order of magnitude off.
- Fix: in 12.2, say "the atomic valence numbers do not carry over; the crystal valence probability is 47 times the atomic one (\cref{sec:12.3-atom})". Or drop the claim.

**E4. Which germanium number is the book's?** s12-2 l.83 and Fig 12.2 headline $1.63\times10^{-3}$ (Cox). The opener l.3 ("one in 580"), the worked example l.95 and the Summary (s12-6 l.202) use $1.73\times10^{-3}$ (Ibe). Pick one as the book's number and label the other as the second calculation.

## 4. Chapter as a whole

**Opening paragraph (ch12.tex l.2): PASS.**
- It is concrete ("A dark-matter particle of \SI{100}{MeV} gives a silicon nucleus at most \SI{5.3}{eV}") and motivational, and it places the chapter between Chap. 10/11 and Chap. 13.
- Minor: the last three sentences all orient ("In the language of the decomposition theorem …", "It is the first of the two mixed sectors; …", "We start from one response …"). STYLE allows one. Fold them into one: "In the decomposition of \cref{sec:8.6} it is the first mixed sector, the nuclear density reaching the electrons; \cref{chap:13} treats the second, and we derive every form of the effect from one response that resolves the two energies."

**Summary (s12-6 l.198–210): PASS with edits.**
- It is a précis per section, which is what a summary should be.
- Fix the Ge number (E4).
- l.204 "A scalar dielectric function overestimates it by about 35 %" is correct as written (see E1). Keep it.
- No R9 numbers appear in the summary. Good.

**Redundancy across sections**
- "Replacing the free recoil by the bound response changes the rate by less than 10⁻⁵" is stated four times: s12-3 l.90, the lim:12.3b caption, the lim:12.3b closing sentence, and s12-4 l.64. Keep it in l.90 and the box. 12.4 cites it with `\cref` and no number.
- "specifies" appears 11 times, mostly as "\cref{app:E.18} specifies …", and s12-1 l.129 and s12-3 l.88 have the same clause verbatim ("specifies the calculation that sizes them"). Keep one per section.
- A meta-frame recurs: "tables that the book computes elsewhere" (s12-1 l.89), "Both factors … are computed elsewhere in the book" (s12-4 l.96), "an input of the kind the book computes elsewhere" (s12-6 l.98). This is pattern 22. Open each with the quantity instead: "The dielectric matrix with local fields on a $(\vect{k},\omega_e)$ grid comes from \cref{app:E.6} …".
- The truncation-label paragraph after each limit check ("On the truncation label the box sits at …") appears 9 times (s12-2 l.81/141; s12-3 l.80/113/162/200; s12-4 l.77/137; s12-6 l.154).
  - Twice it ends in a sentence with no information: s12-3 l.162 "which the label does not count", and l.200 "which the label does not resolve".
  - Keep the label line, cut those two tails. Write "\cref{lim:…} sits at" instead of "the box".
- The worked-example closers repeat a count-teaser: "The model makes three points" (s12-1 l.102) and "The example makes three points" (s12-4 l.154). Name the first point instead.

**Seams (read across each join)**
- 12.1 → 12.2: clean. "starting with the isolated atom" leads straight into the germanium atom.
- 12.2 → 12.3: see E3.
- 12.3 → 12.4: 12.3 ends on the Wannier open problem, which is off the main line. 12.4's opener picks up the impulse onset well. The bracket contradiction (E2) sits across this join.
- 12.4 → 12.5: clean. But s12-4 l.124 calls the frame "the open question of \cref{sec:12.1-boost}", and 12.1 l.53 never poses it as open: it says only "a fraction of order p/q". 12.1 should name it as open and give its size, the factor 2.4 on the phonon-emitting fraction at 5 keV (\cref{sec:12.4}).
- 12.5 → 12.6: clean.

**Checks with no findings**
- None of the nine files has an exercise, a checkpoint, "you", "I" or "the reader".
- All nine limit checks follow the format: the formula with a one-line citation, the plot, and one sentence on what breaks. None has a Source/Chain/Validity list.
- Captions stand alone. Figs 12.1 and 12.4 are long but complete. The only caption problem is the Fig 12.2 axis (R2).
- No citation carries content (pattern 20): every cited formula is also stated in the book's notation.
- Symbols are defined at first use or inherited from Chap. 8 by `\cref` (κ_BO, n_B, 𝔐, 𝒦, 𝒳, θ_ep). No symbol is introduced silently.
- General background is confined to s12-6 l.7 (the radiation field, one paragraph pointing to App. C.16), and it is succinct.

**Templated openers (pattern 10, chapter level)**
- ch12, 12.3 and 12.4 all open "A dark-matter particle of X MeV …".
- 12.5 and 12.6 both open "A silicon nucleus kicked to a recoil energy of X eV …".
- Each opener is concrete, but the template becomes audible. Vary two, for example:
  - 12.4: "At $q = \SI{10}{keV}$ the lattice of silicon is left untouched in 94 % of kicks."
  - 12.6: "A nucleus that is suddenly set moving is a charge that radiates."

**Standalone scrub**
- s12-3 l.62 `\paragraph{Computational connection.}` uses the style sheet's internal term ("Computational connection … no dedicated subsection"). Delete the run-in heading and keep the paragraph.
- No campaign, ledger, F-row, writer or ruling labels appear. No bare "Limit N.M" or "limit box" appears.
- `\paragraph{Open problem.}` is a book-wide device (Chaps. 10–12), so it is fine.

**Citation and cross-reference style**
- s12-6 l.53: "is Eq.~(8) of Kouvaris and Pradler; … it is their Eq.~(3)". This hard-codes the source's numbers without `\cite`. Write `\cite[Eq.~(8)]{kouvaris2017probing}`.
- s12-3 l.92: `\cite[Eq.~(3)]{knapen2021migdal}\cite[Eq.~(1)]{liang2021describing}` has no separator. Put ", and" between them.
- R10 check, for the citation reviewer. The book cites `berghaus2023migdal` (2210.06490) at Eqs. (3.1), (3.6), (3.8), (4.1) and (4.5) in s12-1 tab, s12-4 l.15/32/57/67 and D-33 l.72. R10 places the misprinted Eqs. (3.8), (3.11), (4.1), (4.4) and (4.8) in 2603.13052. Confirm that the cited equation numbers belong to 2210.06490. The ch12 prose itself makes no misprint attribution.
- The s12-2 subsections have no `\label`s, while every other section labels its subsections. Add `sec:12.2-boost`, `-dipole`, `-cores` and `-excitation`.
- Numbers in prose: "three percent" (s12-5 l.67, l.94) and "−19 and +25 percent" (s12-6 l.95) should be `\SI{3}{\percent}` and so on. Also "$10^{-11}$ eV" (s12-6 l.102) should be `\SI{e-11}{eV}`.

## 5. Issues by section (location → problem → fix)

### 12.1 The joint electron–lattice response
- l.5, "We will define it, place the sectors …, and compute its Migdal entry" → a "we will" orienting sentence after a concrete opener, which REGISTER checklist item 1 allows. Acceptable; trim the three-verb list to one clause.
- l.45, "We call $\vect{p}$ the momentum given to the electrons." → "we call" tic (REGISTER Sect. 4) → "Here $\vect{p}$ is the momentum given to the electrons."
- l.53, "Two approximations are made in \cref{eq:12.1-amp}." → count-teaser (pattern 18) → "\Cref{eq:12.1-amp} takes the transition density at the equilibrium positions (the Condon approximation of \cref{sec:5.6}) and the vibrational final states of the ground surface."
- l.53, "changes the momentum of the lattice by a fraction of order $p/q$" → understates the effect the book measures elsewhere (seam with 12.4) → add "; at 5 keV it changes the phonon-emitting fraction by a factor 2.4 (\cref{sec:12.4})".
- l.78 → R7 is not implemented. The paragraph gives the valence-only model value $1.86\times10^{-6}$ and does not point to the full-silicon number → add: "The full silicon value, with $Z_{\mathrm{ion}}(p)$, is $6.07\times10^{-5}$ per eV of recoil energy (\cref{sec:12.3}); the point ion gives $3.9\times10^{-5}$."
- l.78, "$\langle p^2\rangle^{1/2} = \SI{5.6}{keV}$" → R11 asks for the model label → "(point ion of charge 4; \SI{6.1}{keV} with $Z_{\mathrm{ion}}(p)$, \cref{sec:12.4})".
- l.87, "The leading entry drops terms of three kinds, and each has a size." → count-teaser, and "each has a size" adds nothing (pattern 0) → "The leading entry neglects the nuclear motion in the energy denominators, the Herzberg–Teller term and the displacement of the excited surface."
- l.98 → the numbers do not reconcile for the reader. The mean lattice energy is "$3\omega_0 = \SI{0.192}{eV}$", yet the total uses "\SI{0.188}{eV}", and the quanta are "65.5 meV" against $\omega_0 = 64.1$ meV → one clause saying which surface's quanta enter each number (or let the derivation reviewer settle it).
- l.102, "The model makes three points." → count-teaser → open with the first point. Also "$S_{\mathrm{HR}}$ is essentially zero" uses the inflated "essentially" (pattern 2) → give the number or the scaling ("of order $1/N$ for a pair over $N$ cells").
- l.129, "Two choices recur across the table and deserve a remark." → filler (pattern 0) → "The three crystal formulas drop the off-diagonal elements $\vect{G}\neq\vect{G}'$, …".
- l.129, "These carry the local fields … \cref{app:E.18} specifies the calculation that sizes them." → the R1 sentence is missing and mis-scoped (E1) → use the E1 wording, with `\cref{lim:12.3a}`.
- l.138, "In silicon both corrections are below $10^{-3}$ at the momenta of \cref{chap:11}" → R15 asks for the range to be stated → "below $10^{-3}$ for $E_R \lesssim \SI{16}{eV}$; at \SI{500}{eV} the weight $1 - P_{\mathrm{Mig}}$ is a 3 % correction (\cref{sec:12.5-bounds})".

### 12.2 The atomic limit
- Title: OK. A noun phrase that predicts the content.
- l.3, sentences 5–8 ("The core shells of a crystal take … The atomic probability follows … Inside a crystal a core shell behaves … Transitions to bound excited states …") → an outline of findings in disguise; l.145 repeats it → keep the first four sentences and the sanctioned orienting close, "With these results we can give the probability, shell by shell, …". Cut the four thesis sentences between them.
- l.83, "and by \SI{6}{\percent} on the total" → the verb is missing after "within … within …" → "and differ by \SI{6}{\percent} on the total".
- l.83 / Fig 12.2 caption l.88, "per unit kinetic energy $E_{\mathrm{ej}}$ of the ejected electron" → R2 is not implemented → replot on $\omega_e$ and name the axis "$\omega_e$ (electronic energy transfer)", as Fig 12.3 does. The text at l.83 ("dominate below a few tens of eV") then follows the new axis.
- l.104, "Each has a number." → no content (pattern 0) → cut.
- l.110, "the atomic valence numbers above serve only as an order of magnitude" → see E3.
- l.112, "The leading corrections follow." → narration (pattern 22) → cut. The next sentence opens the paragraph.
- l.143, "and in germanium, where the binding is smaller still" → R5 is not implemented → "and in germanium, with \SI{4.15}{meV} \cite{…macfarlane…}". The reference is to be verified at revision, per R5.
- l.145, the closing paragraph → restates the section (pattern 5; REGISTER 3.7 says close on a consequence) → keep its last sentence only, corrected per E3.
- l.55, "Two sums over final states are fixed without solving for any of them." → a count-teaser, but the payload is in the same sentence. Minor; acceptable.

### 12.3 Crystals at large momentum
- Title → it gestures at the content (pattern 21). The central result is the loss-function form of $P_{\mathrm{Mig}}$ → "The loss-function form of the Migdal effect".
- l.3, "The formula has two limits in silicon: it holds down to about \SI{16}{MeV}" → depends on R9 (E2). Also, "limits" next to Limit Checks is ambiguous → "two conditions".
- l.7, "Three approximations take \cref{eq:12.1-Skk} to the loss function. The first …" → count-teaser plus ordinals (patterns 13, 18) → "Keeping the diagonal $\vect{G}=\vect{G}'$, a free recoil and the soft limit $p\ll q$ takes \cref{eq:12.1-Skk} to the loss function." Then name each in turn.
- l.12, "The dropped elements $\vect{G}\ne\vect{G}'$ carry the local fields in the vertex" → contradicts lim:12.3a (E1) → "carry the part of the local fields that couples different momenta".
- l.62 → see Sect. 4: drop the "Computational connection" heading.
- l.66, "Each of the three approximations has a parameter … We take them in the order of the derivation:" → self-narration (pattern 22) → cut. The next paragraph starts with the scalar-ε problem.
- l.88, "Knapen and collaborators checked that they change the rates … by at most a factor of order one" → E1, and a verbatim duplicate of s12-1 l.129 → one sentence pointing to the nuisance row.
- l.92–115 → E2.
- l.117, "Two further conditions are met everywhere in this section." → count-teaser plus narration → "The core shells stay frozen in $Z_{\mathrm{ion}}$: …".
- l.130, "Three differences produce the factor, and each can be read off the figure. … Here the second difference acts. … The third is the vertex." → ordinals for unlabelled parts (pattern 13) → name them: "The lower threshold … The plasmon and the interband peak … The vertex …".
- l.149, "Two conventions travel with it." → the second item (dominance near the gap) is not a convention → "$Z_{\mathrm{ion}}$ must count … And the weight $\omega_e^{-4}$ makes a small gap worth more than a large oscillator strength: …". Split the paragraph (Sect. 1).
- l.170, "and $\vect{F} = \sum_i\nabla_iV_{eN}$ minus the total force on the electrons" → misparses as F equals the sum minus the force → "and $\vect{F} = \sum_i\nabla_iV_{eN}$, the negative of the total force on the electrons".
- l.170, "We call this rigid Wannier following." → a coinage by fiat (REGISTER R2) → acceptable as a new term, but write "This is rigid Wannier following:" and keep the name in one sense.

### 12.4 Phonon final states at small momentum
- Title: OK.
- l.5, three questions and "We answer them in that order, for silicon, and then state where each form applies" → a questions-as-roadmap opener plus self-narration (patterns 8, 22) → keep the first question (the real one), cut the rest: "Does the leading entry hold for a bound nucleus, and with $p$ as large as the kick itself? It does, to a few parts in $10^3$, …".
- l.41 → E2 (pattern 19).
- l.79, title "Three regimes in silicon" → a count-title that gestures (pattern 21) → "Zero-phonon, few-phonon and impulse regimes".
- l.81, "Two momenta set the boundaries." → count-teaser → "The zero-phonon weight of the kick falls to one half at $q = \SI{33.2}{keV}$, and the impulse onset lies at \SI{92.5}{keV}; …".
- l.92, "The zero-phonon line needs one more remark." → filler (pattern 0) → "A zero-phonon Migdal event is a Bragg process: …".
- l.102, "and the proof takes a few lines" → narration → cut.
- l.142, "certifies … certifies" → bureaucratic register → "from which \cref{sec:11.3} shows the incoherent multiphonon terms to hold".
- l.154, "The example makes three points." → count-teaser (repeats 12.1) → "At small $q$ the Migdal signal is a pure charge signal: …".
- l.157, "The lattice factor below $|\vect{q}-\vect{p}| \approx \SI{6.6}{keV}$, where the incoherent approximation … is not certified (\cref{lim:11.3a}), while the zero-phonon line … agrees …" → a fragment with no main verb → "Below $|\vect{q}-\vect{p}| \approx \SI{6.6}{keV}$ the incoherent multiphonon terms are not certified (\cref{lim:11.3a}), while the zero-phonon line agrees with its Bragg sum within \SI{8}{\percent}."
- l.157, "the chapter's nuisance table carries all three (\cref{sec:12.6})" → point to the table → `\cref{tab:12-nuisances}`.

### 12.5 Migdal sum rules and bookkeeping
- Title → "bookkeeping" gestures at the content → "Moments of the Migdal spectrum". This also matches App. D.34.
- l.67, "the off-diagonal elements that \cref{lim:12.3a} shows to be a 35 % effect" → E1 → "the off-diagonal elements, which are not yet sized; the local fields on the diagonal already move the valence drag mass from 24.0 to $18.6\,m_e$".
- l.69, "carry the band as a nuisance of the chapter (\cref{sec:12.6})" → R14 is not implemented → "(\cref{tab:12-nuisances})".
- l.94, "The weight is a correction of three percent to the lattice rate; the mass shift is a sixteenth of the width." → restates the two sentences before it (pattern 5) → cut, or keep only "the mass shift is a sixteenth of the width" appended to the previous sentence.
- l.137, "Third moments from nonrelativistic all-electron densities are therefore about \SI{40}{\percent} low for germanium" → 1/1.425 = 0.70, so they are 30 % low → "about \SI{30}{\percent} low (the relativistic value is \SI{42}{\percent} higher)". Derivation reviewer to confirm.
- l.163, "Two pieces are missing for a crystal." → count-teaser → "For a crystal the valence anisotropy and the relativistic shape of the factor are missing."
- l.3 → good concrete opener. The closing four-verb list ("give …, test …, bound …, and fix …") is acceptable as one orienting sentence.

### 12.6 Bremsstrahlung and Migdal-type absorption
- l.7, "Two results carry over to this section." → count-teaser plus narration → "A charge $e_{\mathrm{c}}$ set moving … radiates \cref{eq:C.16-soft}, and inside a medium …".
- l.19, "which we write as $Z^*_{\mathrm{at}}$ for a reason that the next subsection makes clear" → forward narration (pattern 22) → "the free-atom limit of the dynamical Born charge of \cref{sec:12.6-brems}".
- l.55, "The conditions deserve a word each." → filler → cut. The paragraph starts "The photon must be soft: …".
- l.98, "The dynamical Born charges are an input of the kind the book computes elsewhere." → meta-frame, and the paragraph restates l.73 (patterns 5, 22) → delete the paragraph, and move the "shifted Sternheimer at ±ω, scissor, checks" clause into l.73.
- l.172, the first row of tab:12-nuisances → E1. Split it into "Local fields, diagonal (scalar ε against $\varepsilon^{-1}_{\vect{G}\vect{G}}$) | ×1.35 | computed" and "Off-diagonal $\vect{G}\neq\vect{G}'$ | — | named".
- l.192, "The local fields move the total by a third" → a factor 1.35 is 26 % down or 35 % up, not "a third" → "lower the total by a factor 1.35".
- l.196, "Two items belong to this section. … The other open items of the chapter are stated where they arise: …" → a count-teaser plus a catalog sentence of five items (pattern 11) → keep the two GaAs and absorption items. Replace the catalog with: "The open items of the earlier sections are rows of \cref{tab:12-nuisances}."
- l.196, "a tagged-recoil measurement in silicon … would test the whole chain at once (\cref{app:E.18})" → App. E is computational, so the pointer is odd → drop the `\cref` or point to the experimental chapter.
- l.53, "Note that their derivation kept only the elastic atomic channel" → fine (a real caveat). Keep.

## 6. App. D.33 and D.34
- D-33 l.3 and D-34 l.83 open with "We derive …" / "This appendix derives …" → acceptable for an appendix, but D-34 l.83's second sentence is a six-item catalog. Shorten to "the inverse force moments, the trace rule, the cross and third moments, and the Dirac contact density".
- D-33 l.50, "The derivation used three approximations, each stated in \cref{sec:12.1-boost}." → restates 12.1 (pattern 5) → keep only the new content, from "The last can be lifted …".
- D-33 l.64 → E2.
- D-33 l.80 gives "the factor 1.006 in the probability" at the silicon gap with 64.1 meV. s12-4 l.146 gives 1.0029 with $\langle\omega_{\mathrm{ph}}^2\rangle^{1/2} = 44.7$ meV for the same correction → use one convention (the band mean of 12.4). Derivation reviewer.
- D-34: no prose problems beyond the opener. The equation narration is concise.

## 7. Register (REGISTER.md)

**Connectives and tics, per 10k words (book chapter / L).**
- Missing connectives:
  - "however" is ≈ 2 / 8.0;
  - "we will" + "we can" is ≈ 1 / 26;
  - "we see" is 0 / 2.7;
  - "typical" is 0.3 / 15;
  - "note that" is ≈ 0.5 / 6.1.
- Overused words:
  - "gives" is 34 (12.2), 26 (12.3) and 46 (12.5), against L 7;
  - "only" is 26 (12.3), 34 (12.5) and 34 (12.6), against L 11;
  - "so" is 28 (12.6), against L 11.
- "Since" (10–20) is fine. There are no thereby, whereby, "in order to", "respectively", i.e. or e.g.
- The fix is to restore real contrasts with "however" or "but" (for example s12-3 l.90 does it well) and to swap "gives" for "is" or "leads to" in the derivation chains of 12.2 and 12.5.

**Terms of art.** The chapter uses heavy mediator, momentum transfer, Migdal effect, sudden, impulse approximation, loss function, Born effective charge, zero-phonon, multiphonon, f-sum rule and Debye–Waller correctly. The only verb use of "transfers" is s12-4 l.3 ("transfers at most $q$") → "can transfer a momentum of at most …". The other hits are the full noun "momentum transfers" (s12-3 l.156, s12-6 l.42 and l.55), which is fine.

**Calibration (2–3 passages per section; one Lin-style rewrite each).**
- 12.1. l.3 (the opener) and l.76 (estimate, then number, then verdict) read as Lin, with estimate-first. l.27 ("The electronic energy is a label, and it is defined where …") does not. Rewrite: "Of course, ω_e is only a label, and it makes sense only where \cref{sec:8.6} says labels do: inside the off-shell window it is unique up to corrections of order θ_ep."
- 12.2. l.37 ("The electrons that follow the nucleus add their mass to it.") and l.97 (sum-rule check) pass. l.145 does not. Rewrite: "The upshot for a crystal is simple: its core shells inherit the atomic probability, $q_e^2$ times their dipole sum, and its valence electrons do not."
- 12.3. l.92 ("The soft limit fails first.") and l.121 (crystal against atom) pass. l.66 does not. Rewrite: "Each approximation fails somewhere different, and it is worth seeing where before trusting the formula at low mass."
- 12.4. l.90 ("At small q the electrons' momentum controls the lattice.") and l.139 pass. l.5 does not. Rewrite: "We will see that the leading entry survives the binding of the nucleus to a few parts in a thousand, so the real question at small q is how the energy is shared."
- 12.5. l.56 ("exact, but not what a kick measures") and l.131 pass. l.94 does not. Rewrite: "Note that the mass shift, \SI{0.28}{eV}, is a sixteenth of the impulse width, so a phonon detector would never see it."
- 12.6. l.82 ("a check of the theory, not a search channel") and l.122 (equivalence principle) pass. l.98 does not. Rewrite: "In practice, for a polar crystal the site difference comes from frequency-dependent DFPT, and the sum rule \cref{eq:12.6-sum} checks it."

## 8. Editor-notes items that concern prose (status in the tex)

| Item | Status | Where |
|---|---|---|
| R1 G≠G′ wording | **Conflicts with the tex**; see E1 | s12-1 l.129, s12-3 l.12/88, s12-5 l.67, s12-6 l.172/192 |
| R2 Energy axis ω_e on Fig 12.2 | **Not done** (caption still uses $E_{\mathrm{ej}}$) | s12-2 l.88 |
| R3 Drag mass reconciliation | Done (the trace rule against the on-site element) | s12-5 l.56–69 |
| R5 Ge exciton 4.15 meV | **Not done** | s12-2 l.143 |
| R6 lim:12.3b bound-lattice curve | Done (<10⁻⁵ in the caption and closing sentence) | s12-3 l.107/110 |
| R7 Fig 12.1 label plus pointer to 12.3 | Label done; **pointer missing** | s12-1 l.78 |
| R8 P_Mig(1 keV) note value | Not used anywhere. OK | — |
| R9 12.3 bracket numbers | Pending derivation review; see E2 | s12-3, s12-4 l.41, s12-5 l.85, D-33 l.64 |
| R10 Misprint attribution | No prose mention in ch12; equation numbers need a check (Sect. 4) | s12-4, s12-1 tab, D-33 |
| R11 ⟨p²⟩^{1/2} which value | Done in 12.6 l.192; add the model label in 12.1 l.78 | — |
| R12 Nuisance rows | Rows present; the G≠G′ row is mis-scoped (E1) | s12-6 tab |
| R14 12.5 → tab:12-nuisances | **Not done** | s12-5 l.69 |
| R15 "below 10⁻³" range | **Not done** in 12.1 (the 8.6 l.120 half is out of scope here) | s12-1 l.138 |
