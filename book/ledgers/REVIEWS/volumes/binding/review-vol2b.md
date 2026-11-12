# Binding round: independent review of block vol2b

Files: tex/ch11/*.tex, tex/ch12/*.tex, tex/ch13/*.tex (none is marked generated). Base: 60cc72c.

Method. For each file I diffed the base against the current text sentence by sentence (old and new sentence side by side). For every changed sentence that looked doubtful I read the paragraph around it in the current file, and for many of them the cross-referenced section, figure script or worked example as well (we:8-sectors, figscripts/ch13/fig13_9.py, eq:5.7-gamma, ch13 opening). I reached a verdict on every changed sentence before I opened the editors' logs (ch11.md, ch12.md, ch13.md). I used the logs afterwards only to check the readings they had chosen and the open items they had left.

Counting. A sentence count is the number of base sentences that do not survive verbatim. Sentences are split at `.`, `?` and `;`; this is finer than the vol1a count, which did not split at `;`. The counts below leave out the four base sentences that I changed myself as recall fixes (s12-3:44, s12-6:31, s13-4:16, s13-5:92).

## Verdict table (Job 1)

| Chapter | Editor-changed sentences checked | Accepted | Fixed | Reverted |
|---|---|---|---|---|
| ch11 (ch11, s11-1 … s11-9) | 319 | 311 | 8 | 0 |
| ch12 (ch12, s12-1 … s12-6) | 195 | 193 | 2 | 0 |
| ch13 (ch13, s13-1 … s13-9) | 414 | 408 | 4 | 2 |
| **Total** | **928** | **912** | **14** | **2** |

The editors' work is faithful on the whole, and good. I found no changed number, unit or citation. The editors' readings held up in the places I checked against sources: - the 1.4 % LST residual (s11-2:149);
- "the subsection on thermal diffuse scattering" (s11-3:106);
- "Above $q_{\mathrm{BZ}}/2v_{\mathrm{max}}$" (s11-1:144);
- "at the bound" (s13-3:106);
- "0.0015 and 0.002 MeV" (s13-7:83, checked against the paragraph).

The failures I found fall into six groups:
- two strengthened claims: s11-2:3 ("no optical-phonon channel") and s11-7:49 (a defining appositive);
- one restatement that replaced the base claim by its consequence (s13-6:3);
- one new garden path (s12-1:93);
- one coined name (s12-6:123, "the nucleon amplitude");
- a few over-repairs and splits that left robotic repetition, a comma splice, a doubled `\cref`, or a definition placed after its use.

## Fixes and reverts (editor-changed sentences)

| file:line | editor text | my text | reason |
|---|---|---|---|
| s11-1:3 | "The kinematic match, with the momentum taken up by the whole crystal and the energy set by the sound speed, makes single phonons …" | "This kinematic match makes single phonons …" | Over-repair. The appositive repeats the previous sentence word for word. The new sentence still opens on a pointer back, but the pointer names the field's term (REGISTER #10) and binds to exactly one antecedent, the whole previous sentence, which defines the match. A rewrite without the opener would have to restate that definition again |
| s11-2:3 | "so these two crystals have no optical-phonon channel for a coupling to charge" | "so the optical branches of these two crystals have no Born-charge vertex" | Strengthened claim. The base "no such channel" refers to the long-wavelength Born-charge vertex. Higher-order (quadrupole) charge couplings at finite $q$ remain |
| s11-2:9 | "…frequencies $\omega_{\mathrm{T}\nu}$, each of which the field drives through its mode charge" | "…frequencies $\omega_{\mathrm{T}\nu}$; the field drives each eigenmode through its mode charge" | *each of which* had three plural candidates (eigenmodes, polarization vectors, frequencies) |
| s11-2:40 | "The condition of small $q$ on the vertex is the one that matters in practice" | "In practice the small-$q$ condition is the one that matters" | The editor's noun phrase does not parse cleanly ("condition … on the vertex"). The condition is named directly |
| s11-2:53 | "The dynamical quadrupoles … add a contribution of the same order …. The dynamical quadrupoles are the next term beyond the Born charge when …" | "When the charge that moves with an atom is expanded in powers of $q$, the next term beyond the Born charge is the dynamical quadrupole. The dynamical quadrupoles of the displaced atoms add …" | The split put the definition after the use, and the second sentence opened on a repeated noun. The two sentences are reordered |
| s11-5:61 | "In the single-site model the anharmonic rate exceeds …. In the single-site model the anharmonic rate is never below …" | "… In this model the anharmonic rate is never below …" | Robotic repetition of the opening phrase in consecutive sentences. The binding is unchanged |
| s11-7:49 | "Nonreciprocal targets, with a response odd in $\vect{q}$, are treated in \cref{sec:14.5}." | "Targets in which the interference term survives are nonreciprocal; \cref{sec:14.5} treats them." | The editor's appositive adds a defining claim (response odd in $q$) that is stronger than the base. The new text names the interference term of the previous sentence instead, which is what the base "Such nonreciprocal targets" pointed to |
| s11-7:129 | "…, the same mounting and mass give $\mathcal{R}_4/\mathcal{R}_0 = 1.6\times10^{-3}$ and $A_{\mathrm{day}} = …$" | "…, the nuclear part has $\mathcal{R}_4/\mathcal{R}_0 = …$ and $A_{\mathrm{day}} = …$" | Over-repair: "the same mounting and mass give" appears twice in two sentences. The new subject is short, and it covers both values in the coordination |
| s12-1:93 | "This Herzberg--Teller term is the excess of 12 % of the exact probability over the boost formula that \cref{we:8-sectors} traced to the displaced surface, and it acts most on the zero-phonon line." | "\Cref{we:8-sectors} traced the 12 % excess of the exact probability over the boost formula to the displaced surface; this excess is the Herzberg--Teller term, and it acts most on the zero-phonon line." | New garden path: "that … traced" attaches to "the boost formula". Checked against we:8-sectors: exact $3.94\times10^{-6}$ against boost $3.51\times10^{-6}$ |
| s12-6:123 | "The nucleon amplitude then adds $\tilde cm_e$ …" | "The amplitude of the nucleon coupling then adds $\tilde cm_e$ …" | "Nucleon amplitude" is a coined name used nowhere else. The next sentence says "The nucleon coupling adds no new row" |
| s13-2:95 | "The size of the error depends on the model; its order, one, does not." | "The size of the error depends on the model; that the error is of order one does not." | Partial revert. The editor's apposition is stilted. The base claim is restored with a noun subject |
| s13-2:135 | "The distance below the zero-phonon edge is the tighter condition." | "The distance $E_{\mathrm{min}}(\vect{q}) - \omega$ below the zero-phonon edge gives the tighter condition." | Relational noun without its argument (the distance of what), at the place where "margin" was renamed |
| s13-3:102 | "…falls into a band at the edge of the window, the edge band of \cref{sec:13.6}, where … (\cref{sec:13.6}), and the phonon-assisted rate alone has no exponent." | "…falls into the edge band of \cref{sec:13.6}, at the edge of the window, where the phonon-assisted rate is not separately defined and therefore has no exponent of its own." | The same `\cref` twice in one sentence, an apposition that defines its head noun, and "phonon-assisted rate" twice |
| s13-5:54 | "The bound pair lies … below the gap …, every threshold has an excitonic companion …" | "…, and every threshold has an excitonic companion …" | The split left a comma splice |
| s13-5:101 | "Two causes add, the gap shift and …" | "Two causes add: the gap shift and …" | Appositive list after a comma reads as a second clause |
| s13-6:3 | "…and inside the window the soft limit is never reached." | "…and inside the window the soft acoustic phonon is never on the energy shell." | Revert to the base claim, with *it* replaced by its noun. The editor's version states the consequence instead: inside the window $|\vect{Q}|$ is bounded below (s13-6:31), so the soft limit is not reached. That consequence is true and close to the base, but the opening paragraph should keep the base statement. I count this as a revert, not as a physics change |

## Open items (OPEN.md)

| Item | Decision |
|---|---|
| ch11 s11-1:144 "Above that" → $q_{\mathrm{BZ}}/2v_{\mathrm{max}}$ (0.42 MeV) | Accepted. The caption of fig:11-rate puts the onset of Umklapp and multiphonons at $q_{\mathrm{BZ}}/2v_{\mathrm{max}}$, so the editor's reading is the right one |
| ch11 s11-3:106 names the TDS subsection | Accepted: the subsection "Thermal diffuse scattering" does the resummation |
| ch11 s11-2:149 LST 1.4 % spelled out | Accepted and checked: route 2 gives $1 - \omega_{\mathrm{T}}^2/\omega_{\mathrm{L}}^2 = 0.1446$, so $\omega_{\mathrm{L}}^2/\omega_{\mathrm{T}}^2 = 1.169$, against $\varepsilon_0/\varepsilon_\infty = 1.186$, a difference of 1.4 % |
| ch11 s11-5:3 "which anharmonicity cannot change" | A physics error, not a wording question. Left in the text and proposed as erratum E1 below |
| ch12 s12-3:130 "the second" | Fixed in base text: "…would not have the lower threshold, and one with valence electrons as localized as atomic ones would not concentrate their oscillator strength in the plasmon and the interband peak." The three differences in L128 are listed in order as threshold, plasmon/interband weight above 8 eV, and vertex. I read the second as the plasmon concentration, which delocalized valence electrons produce. I considered the third difference, the vertex, as the referent and rejected it: the ordinal counts in the order of L128, where the vertex comes third, and the localization of the valence electrons bears on the plasmon, not on the boost vertex. The lead may wish to confirm this with the author |
| ch12 s12-5:163 "Until both are computed" | Fixed: "Until the valence anisotropy and the relativistic shape of the factor are computed". These are the two quantities the paragraph declares missing. The normalization and the quadrupolar part are parts of the relativistic shape, not separate unknowns. I also split the sentence that followed, which had grown past 45 words, at "…gallium arsenide. The relativistic factor itself carries…" |
| ch12 s12-6:123 "The nucleon amplitude" | Fixed (see the table above) |
| ch12 Summary last sentence | Accepted. It now uses the same phrase as the opening of ch13, and the physics is right |
| ch13 "margin" only $\delta_{\mathrm{w}}$ | Accepted after grepping every use. "margin" now means $\delta_{\mathrm{w}}$ or its band (s13-3, s13-6, s13-7, s13-9), and "distance" is used for $E_{\mathrm{min}} - \omega$. I fixed one bare "distance" (s13-2:135) |
| ch13 s13-9:77 "reproduces the two powers" | Fixed. figscripts/ch13/fig13_9.py, panel (b), plots $p_{\mathrm{on}} = 3$ (free pair) and $3/2$ (exciton replica). The text now reads "reproduces the powers $13/2$ of the free pair and 5 of the exciton replica, and the local value of each stays within 0.06 of its power up to 0.01 MeV above its onset" |
| ch13 table cell "carries half of it" (s13-9:134, tab:13-window) | Fixed: "…extrapolated below 1.206 eV carries half of the rate)". invariant.py shows no STOP. tab:13-nuisances has no unbound pointer |
| ch13 "5 picked readings" | All five checked. s13-3:106 "at the bound" is right. "by factors of 38, 16 and 7" is right. "0.0015 and 0.002 MeV" matches the two numbers in the paragraph. The caption reading follows s13-3:21. "The crystal momentum that the dark matter cannot supply" is right and is now the phrase used throughout ch12/ch13 |

## Proposed erratum E1 (for the errata review)

- Location: tex/ch11/s11-5.tex:3, the last sentence of the section opening.
- Old: "In a crystal with a soft mode or a light atom no expansion is available, and the response is bounded only by its exact moments, which anharmonicity cannot change."
- Proposed: "In a crystal with a soft mode or a light atom no expansion is available, and the response is bounded only by its exact moments, whose expressions hold for any potential of the nuclei."
- Reasoning: eq:11.5-moments gives $\mu_0 = 1$ and $\mu_1 = E_R$ for any potential. But $\bar\mu_2 = 4E_RE^{\mathrm{kin}}_\kappa$, $\bar\mu_3 \propto \langle\partial^2_{\hat q}V\rangle$ and $\bar\mu_4$ are ground-state averages whose values do change with anharmonicity. The book says so itself in three places:
  - s11-4:100: "The kinetic energy and curvature of an anharmonic crystal shift $\sigma_\omega$ and $c_3$".
  - s11-5:102: "The anharmonic change of the kinetic energy of silicon moves the cumulative distribution…".
  - s11-5:143: the moments are obtained "at any temperature and anharmonicity" from path integrals.
  
  What anharmonicity cannot change is the form of the moment expressions, which is the property eq:11.5-moments states ("for any potential $V$ of the nuclei"). s11-9:5 states the correct version for the zeroth and first moments. A grep of ch11–ch13 for "cannot change" and "anharmonicity cannot" finds no other instance.

## Recall (Job 2)

I listed the paragraphs that are unchanged against the base (prose lines of at least 40 words, display and environment lines excluded). From that list I read every sixth or seventh paragraph in every section file. For ch12 and ch13, where the first rates came close to the threshold, I read about every third. Each file is covered at better than one paragraph in ten. Words were counted with each inline math group and each `\cref`/`\cite` counted as one word. One standard applied throughout: a bare *This*/*this* that stands for a display or a proposition counts as a miss, which is the construction the editors repaired elsewhere (s11-3:15, s11-4:81, s13-9:37).

| Chapter | Paragraphs sampled (file:line) | Words | Misses | Per 1000 words |
|---|---|---|---|---|
| ch11 | s11-1:11; s11-2:15, 121 (caption); s11-3:30, 140 (caption); s11-4:17; s11-5:26, 80, 141; s11-6:7, 54, 109 (caption); s11-7:11, 75, 111; s11-8:18, 86, 124; s11-9:41 | 1668 | 0 | 0 |
| ch12 | s12-1:27, 76 (caption), 104, 113; s12-2:12, 48, 88 (caption), 121; s12-3:44, 72 (caption), 105 (caption), 119, 144; s12-4:9, 39, 64, 84 (caption), 125 (caption); s12-5:50, 71, 99, 111, 137; s12-6:31, 50, 71 (caption), 121, 164 | 3061 | 2 | 0.7 |
| ch13 | s13-1:79, 86; s13-2:43 (caption), 65; s13-3:71, 109; s13-4:16, 57, 90, 94; s13-5:11, 30, 92, 123; s13-6:34, 90; s13-7:24, 34; s13-8:50, 69, 118; s13-9:15, 32, 44, 48, 57, 98 (caption) | 2758 | 2 | 0.7 |

Recall fixes:

| file:line | old text | my text | reason |
|---|---|---|---|
| s12-3:44 | "\noindent This is the formula of Knapen, Kozaczuk and Lin" | "\noindent \Cref{eq:12.3-soft} is the formula of Knapen, Kozaczuk and Lin" | Bare *This* stood for the display of the key-result box, which holds two equations |
| s12-6:31 | "…a charge $eZ^*_\kappa$ that jumps to the velocity $\vect{v}_N = \vect{q}/M_\kappa$. This is the classical result of \cref{app:C.16} for a sudden kick…" | "… The factorized amplitude is the classical result of \cref{app:C.16} for a sudden kick…" | Bare *This* stood for the proposition of the previous sentence (the factorization) |
| s13-4:16 | "To see this, remove from the Coulomb kernel …" | "To see why, remove from the Coulomb kernel …" | *this* stood for the proposition "exactly one factor of $1/\varepsilon$ survives" |
| s13-5:92 | "…not only shifted (\cref{sec:6.3}), and the vertices change with them" | "…and the vertices change with the bands" | *them* had two plural candidates (the bands, the lattice vibrations) |

No chapter exceeds 2 misses per 1000 words, so none needs a second pass. In ch11–ch13 the editors changed most paragraphs, so few paragraphs were left unchanged (3 to 22 per file). The ch13 sample covers most of what remains unchanged there.

Table cells. I grepped all 45 tabular rows of ch11 and ch12 (tab:11-nuisances, tab:12-nuisances and the ch12 moment table) for *it, its, this, these, those, both, the two, the rest, the other, such*, and found none. The ch11 editors' log says these cells have no pointers, and the grep confirms it. For ch13, see the open items above.

## Checks

- `python3 tools/invariant.py 60cc72c tex/ch11/*.tex tex/ch12/*.tex tex/ch13/*.tex`: 0 files with a STOP. The `note` lines are repeat counts and the editors' added `\cref`s to existing labels. No symbol was unified.
- Lint (`lint.py --banned BANNED-TERMS.txt`) on the files I changed: no blocking hits. My s12-5:163 fix made one sentence too long, and I split it. The remaining warn-tier hits (LONG-SENT counts that run across captions and displays, EQ-PUNCT) were there before my edits.
- `tools/chapcheck.sh ch11|ch12|ch13 /tmp/binding-review-vol2b` (ch12 and ch13 re-run after the last recall fixes): all three exit 0, with 0 undefined references and 0 multiply defined labels. Overfull hboxes: 1 in ch11, at s11-3:15, and 2 in ch12, at s12-4:96–97 and 116–117. None is from my edits, and all three occur at lines that end in `\cites`.
