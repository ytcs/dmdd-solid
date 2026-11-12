
## Block ch23–ch26 (block reader)

Read first: openings and Summaries of Chaps. 1–22, E2E-vol3-dups.txt, E2E-undefined-labels.txt (no label of that list occurs in ch23–ch26).

Words before/after: ch23 14530 → 14429; ch24 7632 → 7625; ch25 8007 → 7954; ch26 10679 → 10625; block 40848 → 40633 (−0.5 %; the unit passes had already trimmed these chapters, and this pass cut only cross-chapter repeats and stale framing).

Terminology: no "nuisance" in ch23–ch26; nothing to change.

Changes:
- ch23/ch23.tex (opening): removed the sentence "Every method is placed on the truncation label T of Sect. 8.5, whose components include ... sits at its base point T_0" (no longer true since the place-on-the-hierarchy subsections were removed); the next paragraph now opens "The calculation at clamped nuclei, with independent particles and no phonons, the base point of \cref{sec:8.5}, is density-functional theory." (built from the removed sentence and the old opener).
- ch23/s3-4.tex:20: the four-sentence argument that orbital relaxation vanishes in a crystal, given in full in app:D.4 (ch23/D-4.tex, "In a crystal the relaxation drops out"), cut to one clause with a pointer to app:D.4.
- ch23/E-3.tex:15: removed "A measured gap at temperature T contains the renormalization ..." (said in s3-4:134); the double-counting sentence with the 60 meV number stays.
- ch24/E-2.tex:48: removed "The germanium 3d shell is the case the book needs." (process wording); the next sentence names the shell.
- ch25/E-5.tex:41: removed the restatement of the one-gauge rule (stated in sec:3.6, s3-6.tex:155); the quasiparticle sentence now carries the pointer to sec:3.6.
- ch25/E-5.tex:45: removed "The momentum transfer is a parameter of the vertex, not a lattice wavevector, and for each q of interest the real-space matrix must be built anew" (said in s3-6.tex:155); kept as a clause with a pointer.
- ch25/ch25.tex (Summary): its last sentence repeated two sentences of E-5 verbatim ("the energy window, not the interpolation, is what makes fine grids affordable"; "each convergence statement belongs to the quantity, the energy range and the resolution"); replaced by a condensed statement with the numbers of we:E-counts.
- ch26/E-4.tex:55: removed "used throughout this book" after the measured ε∞ (process wording).
- ch26/E-4.tex:129: the Voigt-order paragraph repeated ch11/s11-1.tex:152 (dups list pair 18); cut to the check itself, with a pointer to sec:11.1 (s11-1 points to this check).
- ch26/E-4.tex:140: G_111 = 3.95 keV now points to sec:3.1, where the value is given, instead of sec:1.3.
- ch26/E-4.tex:36–41 (LO–TO display, dups list pair 26 with s5-5:58): cut, then restored, because ch11/s11-8.tex:97 cites eq:E.4-LOTO; listed in the notes for the lead.
- ch26/E-8.tex:88 (we:E-zpr): the GW-bands sentence and the overscreening explanation repeated ch06/s6-3.tex:139 (dups list pair 25); replaced by a pointer to sec:6.3. The double-counting sentence ("A calculation that scissors Kohn–Sham bands to it ... counts it twice"), the third copy after s3-4:134 and E-3:15, cut; the clamped-gap rule stays with a pointer to sec:3.4.

Sentences written not built from existing text: ch25 Summary, "Near an absorption edge an energy window around the band extrema cuts the number of pairs (k, Q) on 40^3 grids by four orders of magnitude."; E-5:41 "... and with the same U(k) as every other quantity of the amplitude (\cref{sec:3.6})."; E-4:129 "A cheap check against the Voigt-order error of \cref{sec:11.1} is to compute ..."; E-8:88 "... a shortfall that \cref{sec:6.3} traces to the overscreening of the vertex by the small Kohn–Sham gap."

Checked and left: dups pair 22 (ch03/s3-3:203 vs ch23/s3-4:148): the worked example recomputes the k_c bound with the LDA gap, which is new; kept. Dups pair 27 (ch23 Summary vs ch33 opening): later side is ch33, in the notes.

chapcheck (private outdirs /tmp/e2e-ch23 … /tmp/e2e-ch26): ch23, ch24, ch25, ch26 exit 0, no undefined references, no multiply defined labels, no float too large. Lint on changed files: no blocking hits; the one long-sentence warning in a sentence I touched (E-5:41) fixed by splitting.

Left for others (details in E2E-vol3-notes.md): ch27 opening repeats ch23 opening and ch23/ch24 Summaries; ch33 opening repeats the ch23 Summary and the stale truncation-label claim; s11-8:97 → eq:5.5-LOTO so that the E-4 LO–TO display can go; ch26 (and ch27, ch28) have no Summary; number mismatches SG15 r_c 1.89/1.88 Å and LDA a 5.401/5.403 Å listed, not fixed.

## Block ch27–ch30 (block reader)

Read first: openings and Summaries of Chaps. 1–26, E2E-vol3-dups.txt, E2E-undefined-labels.txt (no label of that list occurs in ch27–ch30; a scan of every \cref target of the block found none missing), E2E-vol3-structure.md (findings on this block applied where they lie inside it).

Words before/after: ch27 6590 → 6319; ch28 4216 → 4161; ch29 9622 → 9509; ch30 13472 → 13382; block 33900 → 33371 (−1.6 %; the unit passes had trimmed these chapters already, and the cuts here are cross-chapter repeats).

Changes:
- ch27/ch27.tex (opening): cut sentence 1 (repeated the ch23 opening) and the last sentence (ε∞ 13.0 vs 11.7 and the vertex beyond 1/r_c: the ch23 and ch24 Summaries). The kept sentence on the independent-particle form factor is preceded by one connective sentence. r_c is now defined at its first use, E-7.tex:52.
- ch27/E-6.tex:68 (bound excitons): the Wannier–Mott derivation of μ_x, a_x and the k spacing repeated ch04/s4-9.tex:72; cut to the radius and the zone fraction with \cref{sec:4.9}; the grid conclusion stays.
- ch27/E-6.tex:77: removed "We check each setting against the estimates of this section." (narration).
- ch27/E-7.tex:58: the description of the pseudo-wavefunction inside r_c (sec:3.5, E-2) cut to "The pseudo vertex is reliable only for q r_c ≪ 1 (sec:3.5)".
- ch27/E-7.tex:69 (core shells): the shell binding energies (99.4, 99.8, 150, 1839 eV) and the kinematic derivation of the openings repeated ch24/s3-5.tex:103–107; cut to the openings of Si 2p and Ge 3d with \cref{sec:3.5}.
- ch27/E-7.tex:76: the Griffin test of atomic against reconstructed orbitals (stated in ch24/E-2.tex:54) cut to one clause with \cref{app:E.2}; the net 1s shifts 0.26 % and 1.46 % (we:3-Zalpha) cut, the (Zα)² sizes kept with the pointer.
- ch27/E-7.tex:112: removed "the number quoted at the start of this section".
- ch28/ch28.tex (opening): cut the sentence on exchange-constant and Eliashberg uncertainties, which E-9.tex:3 states with its numbers.
- ch28/E-9.tex:3: cut "These two cases mark the range of what first-principles methods deliver ..." (no content).
- ch28/E-10.tex:3, 40: the 17.5–63.5 eV range is now said to be that of the Stillinger–Weber potential at its first mention; the second mention is replaced by the overshoot of 4–6 eV along ⟨111⟩ from sec:19.1-md.
- ch29/ch29.tex (opening): cut "and placed on the truncation label ... so that a number in the text can be traced to what it neglects and to the check that would expose it" (repeated the ch23 opening; structure finding on the truncation label).
- ch29/E-11.tex:3: cut "The atoms leave the region where the force constants of sec:5.2 apply" (said in the ch29 opening).
- ch29/E-11.tex:103 (pitfalls): the sentence on potentials that agree on elastic constants and disagree on thresholds repeated ch19/s19-1.tex:99; replaced by \cref{sec:19.1-md}.
- ch29/E-12.tex:61: the G4CMP lumped-film escape factor exp(−4d_f/l_f) and its explanation, removed from Chap. 20, replaced by the absorption probability P_abs of \cref{eq:20.3-pabs}.
- ch29/E-13.tex:64–71 (single-parameter model): the Ramanathan–Kurinsky Monte Carlo planes ε_eh = 1.7E_g + 0.084A + 1.3, F = −0.028E_g + 0.0015A + 0.14 and their values 3.71 eV and 0.115 removed (dominated, as in Chap. 18). The text now says which calibration it quotes: the original A_AB = 5.2 (source units) for the ionization probabilities, and the calibration A_AB = 5.703 eV³ of sec:18.4 (eq:18.4-AAB) for the comparison with the measured Fano factor, F_eh = 0.114, 2.4σ low. The model is pointed to as the free-particle limit of the random-k cascade of sec:18.1. tab:E-cascade-si: caption and model row follow (model 3.749 eV fitted, 0.114). No number changed.
- ch29/E-13.tex:85 (pitfalls): "the agreement of the cascade of sec:18.4 with the single-parameter model" read as a self-comparison, since sec:18.4 is that model; retargeted to the full-band cascade of sec:18.3-fullband, which gives the same F_eh = 0.114. Author to confirm.
- ch30/ch30.tex (opening): "This chapter and the two after it specify, quantity by quantity," → "\Crefrange{chap:30}{chap:32} specify ..., with the methods of \crefrange{chap:23}{chap:29}" (structure findings on the openings).
- ch30/E-14.tex:3: cut the restatement of the ch30 opening (the 0.333–0.405 MeV window, "known only to a factor of ten"); the paragraph now starts from the estimate.
- ch30/E-16.tex:17: the off-axis minima of the zero-phonon edge (dups pair 22 with ch13/s13-9.tex:13) cut to the angle range with \cref{sec:13.9}.
- ch30/E-18.tex:3: cut the clause on the coherent zero-phonon Migdal part (in the ch30 opening and in the subsection "Coherent zero-phonon Migdal response").
- ch30/E-18.tex:23: the ω² expansion of the on-site force constant at imaginary frequency (dups pair 16 with ch12/s12-5.tex:46) cut to a pointer to sec:12.5; the five-point fit stays.
- Terminology: "many-body nuisance" → "many-body theory uncertainty" (E-15.tex:7, E-18.tex:23); "reported as the nuisance" → "as the theory uncertainty" (E-15.tex:45, 49); "local-field nuisance" → "local-field uncertainty" (E-18.tex:33). No other use in the block; the label tab:12-nuisances is unchanged.

Sentences written not built from existing text: ch27.tex:3 "The bands and wavefunctions of \cref{chap:23,chap:24} reach an electron-recoil rate through the density vertices."; ch29/E-12.tex:61 "An incident phonon is absorbed with the probability $P_{\mathrm{abs}}$ of \cref{eq:20.3-pabs} and otherwise escapes back into the substrate."; ch30.tex:3 the clause "with the methods of \crefrange{chap:23}{chap:29}". All other new wording is assembled from sentences of s4-9, s3-5, E-2, s12-5, s18-1, s18-4, s19-1 and the ch18 Summary.

Checked and left: tab:E-md-si (E-11) recaps the section but is cited from ch19/s19-1.tex:99, so it stays; tab:E-transport-si and tab:E-cascade-si stay with it (structure finding 17, uniformity is the lead's call). E-9.tex:39 (J_2 from 11 to 27 meV) repeats the ch7 Summary but is the methods home of the number; kept.

chapcheck (private outdirs /tmp/e2e-ch27 … /tmp/e2e-ch30): ch27, ch28, ch29, ch30 exit 0, no undefined references, no multiply defined labels, no float too large. Overfull hboxes (ch28 1, ch29 1, ch30 2) are in lines not touched here (E-9:21, tab:E-cascade-si plasmon row, E-15:11, E-18:31). Lint on changed files: no blocking hit; long-sentence warnings in edited sentences split.

Left for others (details in E2E-vol3-notes.md): plasmon 16.6 vs 16.4 eV (E-13 vs E-24); E-6:44 "local fields small in the rate" against sec:10.2, ch21, sec:8.8; δ_LF against ε_mac in eq:E.16-dLF vs head-only in s13-4; SW threshold 17.5 vs 18 eV; ch23 opening gap "0.5 eV"; dups to cut in ch32.tex:3 and ch33/s22-1.tex:15, 79; no Summaries in Chaps. 27–30; order of ch30/ch31.

## Block ch31–ch33 (block reader)

Read first: openings and Summaries of Chaps. 1–30, E2E-vol3-dups.txt, E2E-undefined-labels.txt (no label of that list occurs in ch31–ch33; every \cref target of the block exists in tex/), E2E-vol3-structure.md.

Words before/after: ch31 15489 → 15370; ch32 11443 → 11312; ch33 8352 → 8220; block 35284 → 34902 (−1.1 %). The unit passes had already cut the removed-model specifications (ch30-33.md, second pass); this pass found no specification left whose Volume II model is gone (grepped: Klein, Ramanathan–Kurinsky, modified Lindhard, bare bubble, Landau multiferroic, Wigner correction, effective-mass envelope, form-factor and electron-gas rates; the remaining mentions are checks or data that Chaps. 15, 16, 18, 19 keep).

Terminology ("nuisance"): E-17 (3: "reported as the uncertainty", "is the uncertainty until it exists", "spread as the uncertainty"), E-19 ("method uncertainty", "uncertainty of the correction"), E-20 ("so that stage gives only an estimate of the theory uncertainty"), E-25 ("uncertainty of the contrasts"), E-27 ("theory uncertainty"), s21-6 ("uncertainty tables" ×2, "uncertainty template", "uncertainty of the approximations", schema row "Nuisances" → "Theory uncertainties", worked-example run-in "Uncertainty.", "The theory uncertainty that remains"; "its nuisance parameter ϑ_k" → "its parameter ϑ_k in the likelihood of \cref{sec:21.4}"), s22-1 ("uncertainty budgets"). No "nuisance" left in the block.

Changes:
- ch32/ch32.tex (opening): cut the acceptance rule and "quantity by quantity ..." (dups pair ch30:3/ch32:3, kept in ch30); joined the methods pointer to the cost sentence.
- ch33/ch33.tex (Summary): replaced. The old one restated Chaps. 23–25 (8^3 grid / nine percent, the three bookkeeping rules) and the ch32 cost range (dups pair ch23:17/ch33:9, structure finding 1). The new one condenses Sects. 33.1–33.2: what a library stores and why, the 22 channels by class, the calculation-limited group and tab:22-calc, the data- and theory-limited groups.
- ch33/s22-1.tex: opening sentence on MeV masses and v_max (Vol I kinematics) cut; germanium check in tab:22-calc reduced to the band check of app:E.14 (numbers stood in E-14:56); germanium paragraph: the hybrid/4s-shift numbers (E-14:58, E-1:143) cut to a pointer; Sect. 33.2.3: the three class definitions (repeat of sec:16.9-limits, dups pair s16-9:37) cut to a pointer, fig:22-limits caption "as defined in the text" → "as defined in \cref{sec:16.9-limits}"; we:22-fsum: the δ_NL definition replaced by a pointer to app:E.14.
- ch31/E-17.tex: the redisplay of eq:11.3-weight (label eq:E.17-Wn, one user, in E-17) cut to a sentence citing eq:11.3-weight; first paragraph: "for Si, Ge and GaAs these come from one DFPT calculation each" cut (said in the ch31 opening).
- ch31/E-19.tex:3: ", and only exact static moments bound the answer" cut (ch31 opening and E-19:15).
- ch31/E-20.tex: exclusion of the edge cells retargeted sec:15.1 → sec:15.2 (where the exclusion is made, s15-2:75); "(\cref{app:E.9})" added after DFT+U (structure finding 11).
- ch31/E-22.tex:25: the arithmetic of ln(Γ0 t)=47.2 and the two-parabola 27.5 (given in s19-6:27–29) cut to the two numbers with a pointer to sec:19.6.
- ch32/E-23.tex: "Dense tracks" and "Track recombination" retargeted sec:19.1 → sec:18.5,sec:19.5 (earlier note); first sentence rephrased so that it no longer repeats the ch32 opening (structure finding 10).
- ch32/E-24.tex:59: the binomial thinning formulas (eq:18.5-thin) cut to a pointer.
- ch32/E-25.tex: the space-charge numbers (s20-1:142, dups pair) cut; ", which fixes the size law" cut (s19-6:181, dups pair).
- Labels removed: eq:E.17-Wn (no reference outside E-17; tex/xref/all.tex keeps it until the next build).

Sentences written, not built from existing text: ch33 Summary (all of it condensed from s21-6:3, 7, 19 and s22-1:116–120; new wording: "Since a limit can be reproduced and recast only from the response tables it was computed with, ...", "Their calculations are specified, and \cref{tab:22-calc} orders them ...", "In the data-limited channels no calculation substitutes for a measurement of the sample or the detector.", "... the next step is a new method."); ch32.tex "These calculations use the methods of \cref{chap:29}, and their costs run from ..."; s22-1 "\Cref{fig:22-limits} sorts every channel of the book by theory, calculation and data, the three classes by which \cref{sec:16.9-limits} sorts the novel targets."; s22-1 "... which neither a hybrid functional nor a shift of the 4s-like orbitals gets right together (\cref{app:E.14})"; E-17 "... the n-phonon weight is the lattice sum \cref{eq:11.3-weight}, per cell, and its ratio δ^coh_n(q) to the incoherent weight is the exact coherence correction ..."; E-22 "For a silicon close pair in one year this is λ_tun ≤ 23.6 in the strong-coupling regime, against a two-parabola estimate of 27.5 (\cref{sec:19.6}), ..."; E-23 "In silicon a binary collision with a valence electron creates an electron–hole pair only above the recoil energy ..."; E-24 "A capture probability shared by every carrier changes ε_eh and F_eh by \cref{eq:18.5-thin}."; E-20 "so that stage gives only an estimate of the theory uncertainty".

Checked and left: dups pairs E-14:86/s22-1:79 (worked example kept, move proposed in the notes) and s19-6:181/E-25:29 (specification intro kept, one clause cut). Numbers checked consistent across the volume: Z*/ε∞ = 0.194 (2.11/10.88), (1+θ_ii)Eg = 2.32 eV with θ_ii = 1, λ_tun 23.6/27.5/14 %, attraction ×1.28 = 1 + δ_X(0.28), 27 pairs at 3.75 eV, 8.43 km/s.

chapcheck (/tmp/e2e-ch31, -ch32, -ch33): all exit 0, 0 undefined, 0 multiply defined, 0 floats too large; ch32 keeps its one pre-existing overfull hbox. Lint on changed files: only LONG-SENT warnings, none in a sentence I wrote (two split).

Left for others: see "Notes from block reader ch31–ch33" in E2E-vol3-notes.md (we:22-fsum placement, shared-base order, missing Summaries of Chaps. 31–32, c_κ^* in eq:11.3-weight, ch31 methods pointer).

## Structural fixes

Scope: tex/vol3.tex and tex/ch24 … ch33 (ch23 not edited: the Volume I fixer is moving s3-4). Inputs: E2E-vol3-structure.md (17 findings), E2E-vol3-notes.md, the block logs above. Words before/after: ch24 7625 → 7550; ch25 7954 → 7954; ch26 10625 → 10842; ch27 6319 → 6484; ch28 4161 → 4391; ch29 9509 → 9719; ch30 13382 → 14237 (+ we:22-fsum moved in, ~600 words); ch31 15370 → 15668; ch32 11312 → 11550; ch33 8220 → 7517 (− we:22-fsum). The growth is the seven Summaries (193–244 words each) and the moved worked example.

### Chapter order (findings 5 and 6): done
- Dependency check (grep of \cref targets between the chapters, after the block edits): ch25 (Wannier) cites ch26/ch27 inputs 7 times (app:E.4, eq:E.4-berry, eq:E.4-dpsiperp, we:E-dfpt-si, eq:E.7-fsum); ch26/27/28/29 cite ch25 only as "interpolated in app:E.5" pointers. ch30 builds on the base of app:E.17 (E-14:9, 19, 27, 64; E-16:9; E-18:23 and "the shared base" in E-14, E-16, E-18); ch31 cites ch30 only for the window grid and the germanium band test (E-17:7, 11). Both arguments still hold.
- vol3.tex: Methods now ch23, ch24, ch26, ch27, ch25, ch28, ch29; Specifications ch31, ch30, ch32, ch33. Printed: chap:26 → 25, chap:27 → 26, chap:25 → 27, chap:31 → 30, chap:30 → 31.
- \crefrange endpoints that no longer bracket the intended chapters: \crefrange{chap:30}{chap:32} → \crefrange{chap:31}{chap:32} in ch33.tex:3, s22-1.tex:3, E-17.tex:7, E-26.tex:7 (and the new ch31 opening); s21-6.tex:53 \crefrange{chap:23}{chap:26} (functional, pseudopotentials, scissor, grids: DFT, PP, Wannier, phonons) → \cref{chap:23,chap:24,chap:25,chap:26}. No "previous/next chapter" wording exists in ch24–ch33 (grep).
- Openings: ch31.tex (now the first specification chapter) takes the Part II acceptance rule from ch30.tex and names its method chapter (DFPT of chap:26) and its link to chap:30. ch30.tex loses the Part sentences, the "Each is placed on the truncation label" sentence (finding 3) and "The electronic channels come first" (position); it now names its methods (\crefrange{chap:23}{chap:25}, printed "Chaps. 23 to 27") and the lattice base of app:E.17. The "shared base" used before its definition (notes, ch31–33 block) is resolved by the order.
- ch24/E-2.tex: the closing paragraph that handed over to the Wannier chapter as the next one ("The density vertex ... can now be computed ... The localized orbitals of \cref{chap:25} turn a calculation on a coarse grid into one on any grid.") deleted; ch25's opening motivates the fine grids itself.
- The seven back-pointers to app:E.5 in ch26–ch29 now point forward; each says where a step is done (Addendum 3 test), kept.

### Summaries (finding 2): done
\section*{Summary} added at the end of the drivers of ch26, ch27, ch28, ch29, ch30, ch31, ch32, condensed from the section openings, key results, worked examples and summary tables (sources: ch26 s5-4, E-4 incl. we:E-dfpt-si, E-8 incl. we:E-zpr; ch27 E-6, E-7 incl. we:E-siff; ch28 E-9, E-10; ch29 E-11–E-13 and tab:E-md-si, tab:E-cascade-si; ch30 E-14, E-15, E-16, E-18, E-26, s22-1:3; ch31 E-17, E-19–E-22; ch32 E-23–E-25, E-27). They avoid the sentences of the openings and of the Summaries of ch23–ch25 (no ε∞ 13.0/11.7, no zero-point double count, no nonlocal-sum-rule rule, no cost range, no acceptance rule). No new number: every number is in the chapter.

### Repetition across openings and summaries (finding 3, 4 and item 3): done where in scope
- Acceptance rule: once, ch31.tex:3. "quantity by quantity …": once, ch23.tex:3. Cost range: once, ch32.tex:3. Truncation-label claim: gone from ch30.tex.
- ch26/E-8.tex (we:E-zpr): "So the window and threshold calculations of \cref{chap:13} take the measured gap and do not add the renormalization again." deleted (third copy of the double-count rule, finding 8); the clamped-gap rule stays.
- ch27/E-7.tex:99: "With a nonlocal pseudopotential, a test that compares the truncated sum with q²/2m_e alone confuses the two effects, and the nonlocal term must be included before the shortfall is read as band truncation." deleted (stated in ch24/E-2, to which the paragraph already points as "the band-summed form of eq:E.2-dc").

### Other findings
- 1 (ch33 Summary): done by block reader; checked.
- 7 (core region 24 ↔ 27): block reader cut the E-7 copies; remaining forward uses of eq:E.7-fsum and eq:E.7-vNL in ch24/E-2 are pointers to the per-state forms derived in E-7; accepted (E-2 derives the band-summed form, E-7 the per-state one). Order 24 before 27 (printed 26) unchanged.
- 8 (nonlocal f-sum, zero point): see above; ch23/E-3:11 and :15 listed for ch23.
- 9 (ch27 opening): the plasma-frequency/loss-peak sentences moved from E-6:3 to the opening (the opening now motivates by the 16.6 eV peak and the light-mass weight near the gap); E-6:3 keeps the hierarchy, rewritten as one sentence without the recap opener.
- 10 (openings vs first sections): done by block readers; ch31/ch30 rechecked after the opening rewrite, no repeat.
- 11 (method pointers): ch31.tex and ch30.tex openings (above); E-20 pointer done by block reader.
- 12 (split ch28): not done. E-10 holds formation energies, charged-defect corrections, color centers and tunneling defects in metals as well as the bridge to recoils; moving it to ch29 would put color centers into the recoil chapter. "Displacement thresholds" (E-10:38–40) now has unique content (SW best of three potentials, 4–6 eV above DFT along ⟨111⟩) and a pointer; kept.
- 13 (plane waves twice): ch24/s3-5.tex: the unlabeled-in-use display eq:3.5-pw removed (grep: no reference anywhere), its content kept as a clause pointing to app:E.1 for E_cut and k_cut; the first paragraph moved above the subsection to become the section's opening (Sect. 24.1 no longer starts with a subsection); subsection retitled "The cutoff and the vertex". Label removed: eq:3.5-pw (xref/all.tex keeps it until the next build).
- 14 (ch23 order): ch23, not edited; listed below.
- 15: done by block reader.
- 16 (E-16:9 "20 functions in all (sec:21.6)"): the count is defined in E-16 itself (12 + 4 per version); no change.
- 17: no "nuisance" left in ch24–ch33 except the label tab:12-nuisances; conventions.tex is front matter, for the lead.
- Notes, we:22-fsum: moved from ch33/s22-1.tex to the end of ch30/E-14.tex "The f-sum check with its parts separated" (after "… in minutes, and \cref{we:22-fsum} works it through at one momentum."); s22-1.tex:77 keeps its one-sentence pointer. Inside the example: the re-statement of eq:E.7-fsum and of the 0.81/0.89 band sums cut (stated two paragraphs earlier); "δ_NL of \cref{app:E.14}" → "δ_NL" (same section now). In E-14 the clause "an all-electron (PAW) calculation, which has no nonlocal term (\cref{app:E.2}), checks it" deleted; the example's accurate statement ("An all-electron calculation, or a PAW calculation whose density vertices are reconstructed inside the augmentation spheres, … checks the split") stands once.

### Sentences written (not copied verbatim)
- ch24/s3-5.tex:3 "A plane-wave code stores each periodic part as the Fourier series \cref{eq:3.2-pw}, truncated at the kinetic-energy cutoff of \cref{app:E.1}, $|\vect{k}+\vect{G}| \le k_{\mathrm{cut}} = (2m_eE_{\mathrm{cut}})^{1/2}$." (rebuilt from the old first sentence and display).
- ch27/E-6.tex:3 "The hierarchy of many-body approximations of \cref{sec:4.6,sec:4.9} runs from the independent-particle bubble through the random-phase approximation with and without local fields and time-dependent density-functional kernels to the Bethe--Salpeter equation." (rebuilt from the old sentence).
- ch30.tex:3 "The electronic channels, with those that mix electrons with phonons or with the motion of a nucleus, are specified here with the methods of \crefrange{chap:23}{chap:25}, on the lattice base of \cref{app:E.17}."
- ch31.tex:3 "One harmonic calculation per crystal by the DFPT of \cref{chap:26}, …" (clause added); "The electronic specifications of \cref{chap:30} start from the same ground state and phonons."; "The specifications of \crefrange{chap:31}{chap:32} share one rule: …" (rule sentence moved from ch30).
- ch30/E-14.tex: "… in minutes, and \cref{we:22-fsum} works it through at one momentum."; in we:22-fsum "The test momentum sits at the upper end of the range in which the norm-conserving sum at Γ reaches 0.89 of q²/2m_e with 100 bands."
- All sentences of the seven new Summaries (ch26.tex, ch27.tex, ch28.tex, ch29.tex, ch30.tex, ch31.tex, ch32.tex, last paragraph before \printbibliography): condensed rewordings of the cited sources, each checked against the prose patterns and the lint.

### Checks
chapcheck (/tmp/sf3-<unit>): ch24, ch26, ch27, ch28, ch29, ch30, ch31, ch32, ch33 exit 0, 0 undefined references, 0 multiply defined labels, 0 floats too large (ch25 not edited). Overfull hboxes > 5 pt: ch26 5, ch28 1, ch29 1, ch30 2, ch32 1, all in lines not touched here. Lint on changed files: 0 blocking; LONG-SENT warnings only in untouched sentences (and the ch33 Summary of the block reader); the long sentences I wrote were split. vol3.tex itself is not compiled (no full build run).

### For the lead (outside Volume III or ch23)
- ch23/ch23.tex:3 \Crefrange{chap:30}{chap:33} now prints "Chaps. 31 to 33"; change to \Crefrange{chap:31}{chap:33}. \Crefrange{chap:23}{chap:29} is still correct.
- ch08/s8-8.tex:24 \crefrange{chap:23}{chap:26} now prints "Chaps. 23 to 25" (DFT, PP, phonons); if the Wannier grids are meant, use \cref{chap:23,chap:24,chap:25,chap:26}.
- appB/B-1-vol3.tex (generated) lists notation blocks by chapter label in the old order (chap:25 before chap:26, chap:30 before chap:31); regenerate. xref/*.tex need a full build.
- ch23 items: finding 14 (scissor in 23.1 and 23.5), E-3:15 zero-point pointer (finding 8), E-3:11 eq:E.2-fsumNL forward pointer, ch23.tex:3 "about 0.5 eV" should name the functional (LDA).
- ch11/s11-8.tex:97 → eq:5.5-LOTO so that eq:E.4-LOTO (ch26/E-4:36–41) can go (block note, still open).
- front/conventions.tex Limit Check paragraph in Vol. III (finding 17).

### Value disagreements for the corrections stage (not changed)
- Norm-conserving f-sum at Γ with 100 bands: 0.88 (ch24/E-2, at 0.1 Å⁻¹ along [100]) against 0.89 (ch30/E-14 and the moved we:22-fsum, 0.1–0.5 Å⁻¹; sec:13.9). New.
- SG15 Si p core radius 1.89 Å (ch24/s3-5:43, fig:3-psae) vs 3.56 bohr = 1.88 Å (E-2:31). LDA a of Si 5.401 (ch23/s3-4:56) vs 5.403 Å (tab:E-functionals). Plasmon 16.6 eV (E-13, tab:E-cascade-si) vs 16.4 eV (E-24). SW threshold 17.5 (E-10) vs 18 eV (E-11). KS gap "about 0.5 eV" (ch23) vs 0.6 eV PBE (E-7). E-6:44 "local fields small in the rate" vs sec:10.2, ch21, sec:8.8. δ_LF reference ε_mac (eq:E.16-dLF) vs head-only (s13-4:122). c_κ^* in the old eq:E.17-Wn vs eq:11.3-weight.
