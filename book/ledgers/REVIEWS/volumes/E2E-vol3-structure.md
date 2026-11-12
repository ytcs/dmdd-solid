# Volume III end-to-end review: structural reader

Scope: tex/vol3.tex, the eleven chapter drivers, the first paragraph of every section, every Summary, the table captions, the TOC of build/vol3.pdf, and E2E-vol3-dups.txt. Items 2 (order and threads), 4 (openings and summaries) and 6 (volume shape) of E2E.md. Findings only; no tex file was edited. Ranked by importance. Line numbers are those of the files on 2026-11-12. Block readers are editing at the same time, so check the text before applying a fix.

Background for findings 1 to 4: the old Appendix E opened with one paragraph and closed with one Summary (`git show 7696d03:book/tex/appE/appE.tex`). When the appendix was split into Chaps. 23 to 33, sentences of that paragraph and that Summary were copied into five chapter openings and two Summaries. Most of the repetition across chapter openings comes from this one source.

---

## 1. Chap. 33 Summary is the old Appendix E Summary. It does not summarize Chap. 33 and repeats three earlier Summaries

- **Where:** tex/ch33/ch33.tex:9.
- **What:** The first four sentences restate the methods of Chaps. 23 to 29: "one base calculation ... one entry of the truncation label at a time", "the $8^3$ grid that converges the energy to 2 meV per atom leaves $\varepsilon_\infty$ nine percent too high" (verbatim from ch23/ch23.tex:17, dup-list pair 1, 21 shared 7-grams), the three bookkeeping rules (ch23.tex:15 zero-point, ch25.tex:10 one gauge, ch24.tex:10 "a sum rule tested with a nonlocal Hamiltonian carries its nonlocal term", verbatim), and the cost range (verbatim from ch32/ch32.tex:3). Only the last sentence concerns Chap. 33. The results of Sects. 33.1 and 33.2 are missing: a limit can be reproduced only from the table it was computed with (s21-6.tex:3), of the 22 channels 12 are limited first by calculation, 9 by data and 2 by theory (s22-1.tex:116), and four calculations each replace a factor of order ten or an unsized rate in a leading result (s22-1.tex:120).
- **Fix:** Replace the Summary with sentences condensed from s21-6.tex:3 and s22-1.tex:107, 116, 120, and keep the final sentence (library with labels, conventions and checks; tab:22-calc ordering). Delete the 8^3/nine-percent sentence and the three-rules sentence: each already stands in the Summary of Chap. 23, 24 or 25. Keep the cost range in one place only, ch32.tex:3 or here, not both (see finding 4). If a volume-closing sentence on the methods is wanted, one clause is enough ("every method of \crefrange{chap:23}{chap:29} starts from the base point $\mathfrak{T}_0$ and moves one entry of the label at a time"). That clause is the existing first sentence, shortened.

## 2. Seven of eleven chapters have no Summary (STYLE.md line 8)

- **Where:** ch26, ch27, ch28, ch29, ch30, ch31, ch32 (drivers end with `\printbibliography` directly; no section file holds a `\section*{Summary}` either). Chaps. 23, 24, 25 and 33 have one. Every chapter of Volume II has one.
- **Why it matters:** The reader of Part II gets no condensed result from any specification chapter. The closing Summary of the volume (finding 1) cannot stand in for them.
- **Fix:** Assign one Summary per chapter to the block readers, assembled from existing sentences (the first paragraph of each section and the costs and acceptance tests in its summary table: tab:E20-params, tab:E21-params, tab:E22-summary, tab:E23-summary, tab:E24-summary, tab:E25-runs, the E-11/E-12/E-13 "Silicon" tables). Ch29's three "Place on the hierarchy" subsections, condensed to one sentence, give its Summary the place of each simulation on $\mathfrak{T}$. Do not reuse the sentences that the openings already carry (findings 3 and 4).

## 3. The volume introduction sits in Chap. 23, and its promise "every method is placed on the truncation label" fails for Chaps. 23 to 28

- **Where:** ch23/ch23.tex:3 (the old Appendix E opening, nearly verbatim); ch29/ch29.tex:3; ch30/ch30.tex:3.
- **What:** (a) ch23.tex:3 says "Every method is placed on the truncation label $\mathfrak{T}$ of \cref{sec:8.5}" and lists its components. No section of Chaps. 23 to 28 mentions $\mathfrak{T}$, $n_B$, $n_g$ or the base point (grep: zero hits in ch23/*.tex sections through ch28/*.tex). The label is first used in the three "Place on the hierarchy" subsections of Chap. 29 (E-11.tex:16, E-12.tex:14, E-13.tex:15) and then in every specification. (b) The clause "so that a number in the text can be traced to what it neglects and to the check that would expose it" appears in ch23.tex:3 and again in ch29.tex:3 (21 shared 7-grams). (c) "placed on the truncation label $\mathfrak{T}$ of \cref{sec:8.5}" appears in the openings of ch23, ch29 and ch30 and then once more in nearly every specification section.
- **Fix:** In ch23.tex:3, change the sentence to say where the label is used: "The simulations of \cref{chap:29} and every specification are placed on the truncation label ..." (connective wording; the list of components stays). Delete from ch29.tex:3 the clause "and placed on the truncation label $\mathfrak{T}$ of \cref{sec:8.5}, so that a number in the text can be traced to what it neglects and to the check that would expose it". Close the sentence after "Each simulation is followed here through silicon." Delete from ch30.tex:3 "Each is placed on the truncation label $\mathfrak{T}$ of \cref{sec:8.5}." (each section states its place, and ch23 has given the label). The Part pages carry no text, so ch23.tex:3 stays as the volume opening. It should then be the only opening that describes the whole volume.

## 4. Part II openings share sentences: the acceptance rule and "quantity by quantity"

- **Where:** ch30/ch30.tex:3, ch32/ch32.tex:3, ch23/ch23.tex:3 (dup-list pair 3, 21 shared 7-grams between ch30:3 and ch32:3).
- **What:** "Each calculation is accepted against an exact limit or sum rule and, wherever one exists, a measurement made at the same kinematics, never against the estimate it replaces" appears in both ch30:3 and ch32:3. Both come from the old Appendix E Summary. "specify, quantity by quantity, the calculation behind each number ... with its inputs, its method and its convergence targets" appears in ch23:3, ch30:3 and ch32:3. The cost range "from seconds for the pair-number library to about $10^6$ core-hours for the close-collision kernel" appears in ch32:3 and ch33:9.
- **Fix:** Keep the acceptance rule once, in ch30.tex:3, as the opening of Part II. Delete it from ch32.tex:3. In ch30.tex:3, cut "specify, quantity by quantity, the calculation behind each number that \crefrange{chap:9}{chap:22} use" to "\Crefrange{chap:30}{chap:32} specify the calculation behind each number that \crefrange{chap:9}{chap:22} use", because ch23:3 already gave "quantity by quantity ... convergence targets". Note also that "This chapter and the two after it" should be \crefrange{chap:30}{chap:32}. In ch32.tex:3, reduce "The sections of this chapter specify these calculations quantity by quantity, with the inputs, the grids and the convergence targets of each, using the methods of \cref{chap:29}" to "The calculations below use the methods of \cref{chap:29}". The rule of exact relations and controls is spelled out in sec:22.1-checks (s22-1.tex:7). The ch30 opening could point there once.

## 5. Specifications run electronic before lattice, but the electronic specifications are built on the lattice base of Sect. 31.1

- **Where:** tex/vol3.tex:21-22; ch31/E-17.tex:5-14 ("The shared harmonic base"); used by ch30/E-14.tex:9, 19, 27, 64; ch30/E-16.tex:9; ch30/E-18.tex:23.
- **What:** E-17.tex:7 defines "the setting ... shared by every specification of \crefrange{chap:30}{chap:32}" (PBE, SG15 at 60 Ry, lattice constants, grids). Chap. 30 cites it six times, starting with its first section ("The ground state and the phonons are the shared harmonic base of \cref{app:E.17}"). So the first specification chapter depends on the second. The order also mirrors Methods the wrong way: Methods give phonons (Chap. 26) before dielectric response (Chap. 27), and Specifications give electronic (Chap. 30, the pair of 27) before lattice (Chap. 31, the pair of 26 and 28). Cross-references: ch30 to ch31, 6 forward; ch31 to ch30, 4 (E-17.tex:7, 11, pointers to the window grid).
- **Fix (preferred):** Swap the two \input lines at vol3.tex:21-22 so that "Lattice and special targets" precedes "Electronic and mixed channels". The labels are unchanged and the printed numbers follow. Then fix the two openings: the new first specification chapter (ch31.tex:3) takes the Part II sentences of finding 4, and ch30.tex:3 loses them. **Fix (minimal):** Leave the order and move the subsection "The shared harmonic base" (E-17.tex:5-14) to the start of ch30/E-14.tex, or to a short first paragraph of ch30.tex. Keep its label references unchanged.

## 6. Chap. 25 (Wannier) uses DFPT and nonlocal-sum-rule results of Chaps. 26 and 27 before they are given

- **Where:** tex/vol3.tex:15-17; ch25/s3-6.tex:61 (eq:E.4-berry); ch25/E-5.tex:14, 18, 22, 37, 79 (app:E.4, eq:E.4-berry, eq:E.4-dpsiperp), :81 (eq:E.7-fsum), :83 (we:E-dfpt-si).
- **What:** Sect. 25.2 interpolates electron–phonon vertices, Born charges and $\varepsilon_\infty$, and adds the remainder by the projected Sternheimer equation, all from Sect. 26.2. Its worked phonon-assisted calculation (E-5.tex:77-83) chains DFPT (Chap. 26), the nonlocal $f$-sum of Sect. 27.2 and the phonon-assisted dielectric function. That is 9 forward references to inputs. The references from Chaps. 26 and 27 back to Chap. 25 are pointers of the type "interpolated in \cref{app:E.5}" (E-4.tex:34, 91, 111; E-8.tex:61, 81; E-6.tex:88; E-7.tex:31).
- **Fix:** Reorder Methods to 23, 24, 26, 27, 25, 28, 29 (move vol3.tex:15 after vol3.tex:17). Wannier interpolation then follows the quantities it interpolates. The seven back-pointers become light forward pointers. Check after the move: ch25.tex:3 cites \cref{sec:6.5,sec:13.3} and needs no change. ch26.tex:3 and ch27.tex:3 do not mention Chap. 25. The chapter openings of 26 and 28 refer to "\cref{app:E.5}" by label and stay correct. If the lead prefers not to move a chapter, the alternative is to move only Sect. 25.2 (E-5) to the end of Chap. 27. That leaves Chap. 25 with one section.

## 7. Core states, all-electron reconstruction and the large-$q$ vertex are treated twice: Chap. 24 and Sect. 27.2

- **Where:** ch24/s3-5.tex:54-117 (PAW, "Core and semicore states", relativistic); ch24/E-2.tex:46-55 ("Semicore states", "The density vertex at large momentum"); ch27/E-7.tex:56-77 ("All-electron reconstruction", "Core and semicore states").
- **What:** The silicon shell energies (99.4, 99.8, 150, 1839 eV, same source) are given in s3-5.tex:103 and again in E-7.tex:69. The test of Griffin et al., which compares atomic orbitals with reconstructed crystal states up to the reconstruction cutoff, is given in E-2.tex:54 and again in E-7.tex:73. The statement "pseudo vertex reliable only for $qr_c \ll 1$" appears in s3-5, E-2.tex:52 and E-7.tex:58. The dup script missed these pairs (different wording). In the other direction, Chap. 24 uses equations defined only in Sect. 27.2 (s3-5.tex:85 app:E.7, :107 eq:E.7-core; E-2.tex:69 eq:E.7-fsum, :73 eq:E.7-vNL). So the thread runs 24 → 27 → 24.
- **Fix:** Chap. 24 is the first place and the home for the physics of the core region. In E-7.tex:56-77 keep only what is computation: the two routes of the reconstruction with eq:E.7-radial, the Bloch sums eq:E.7-core and the core–conduction vertex. Cut the shell-energy list, the kinematic opening masses already in s3-5.tex:112, and the Griffin test sentence, each with a \cref{sec:3.5} or \cref{app:E.2}. Report to the block owner of ch24/ch27 (and to the lead, since the edit spans two chapters). If finding 6 is applied, Chap. 27 still follows Chap. 24, so the forward uses of eq:E.7-* in Chap. 24 remain. Either move the short definitions eq:E.7-vNL and eq:E.7-fsum into ch24/E-2 "Nonlocal sum rules" (E-2.tex:56) where they are first used, or accept the pointers.

## 8. The nonlocal $f$-sum and the zero-point double count are each stated in four places

- **Where:** Nonlocal sum rule: ch23/E-3.tex:11 (eq:E.2-fsumNL, forward), ch24/E-2.tex:56-75, ch25/E-5.tex:81, ch27/E-7.tex:33-55, plus the Summaries ch24.tex:10 and ch33.tex:9. Zero-point renormalization counted twice: ch23/E-3.tex:15, ch26/E-8.tex:88, ch23.tex:15, ch33.tex:9.
- **Fix:** The derivation stays in one section (E-2 or E-7 per finding 7). Each other text place keeps one clause with \cref. For the zero-point rule, E-8.tex:88 (the section on the renormalization) is the home and E-3.tex:15 points to it, or the reverse. The Summary of Chap. 23 keeps it, and Chap. 33 drops it (finding 1).

## 9. Chap. 27 opening is assembled from other chapters' sentences and does not motivate the dielectric response

- **Where:** ch27/ch27.tex:3.
- **What:** Its first sentence is the first sentence of ch23.tex:3 ("loss function out to 100 eV and density vertices at momentum transfers of tens of keV, and neither is measured everywhere it is needed"). Its last sentence combines ch23.tex:17 ("$\varepsilon_\infty$ of 13.0 computed against 11.7 measured") and ch24.tex:10 ("the vertex beyond $q\sim1/r_c$ ... dominant theory uncertainties"). The number 13.04 against 11.7 now appears in s3-4.tex:66, E-1.tex:83, E-3.tex:13, E-4.tex:144, ch23.tex:17 and ch27.tex:3. The opening says nothing of the hierarchy IP → RPA → local fields → TDDFT → BSE that Sect. 27.1 computes, and nothing of the connection to Chaps. 23 and 24.
- **Fix:** Rebuild the opening from E-6.tex:3 (plasma frequency 16.6 eV and the main loss peak; "where the dark-matter rate is largest for light masses, depend on how the response is computed"; the hierarchy of \cref{sec:4.6,sec:4.9}) and E-7.tex:3 (the $5\times10^{11}$-term sum; bands from Sect. 23.4, screening from Sect. 27.1). Keep the sentence "The independent-particle form factor is where every electronic rate of \cref{chap:10} starts, and screening and local fields use the same vertices as input". Delete the two copied sentences, then cut the corresponding sentences from E-6.tex:3 so the reader does not meet them twice on one page.

## 10. Chapter openings repeat the first sentences of their own first section

- **Where and what:**
  - ch29.tex:3 "A struck atom leaves the region where the force constants of \cref{sec:5.2} apply and may end as a vacancy and an interstitial that store several eV" against E-11.tex:3 (10 shared 7-grams).
  - ch30.tex:3 "known to a factor of ten (\cref{sec:13.9}) ... below $2q_{\mathrm{BZ}}$ the coherent zero-phonon part of its Migdal rate is not computed at all (\cref{sec:12.4})" against E-14.tex:3 "That rate is known only to a factor of ten" and E-18.tex:3 (8 shared 7-grams).
  - ch31.tex:3 "One harmonic DFPT calculation per crystal ... (\cref{app:E.17})" against E-17.tex:3. Also "At millikelvin the response of a quantum crystal is bounded only by the band of its exact moments (\cref{app:E.19})" against s22-1.tex:116 and E-19.tex:3-5.
  - ch32.tex:3 (charge at 100 eV below the binary threshold; no first-principles cascade reaches the measured pair energy) against E-23.tex:3 and E-24.tex:3.
  - ch28.tex:3 against E-9.tex:3 (NiO, aluminum).
- **Fix:** The opening keeps the motivating fact. The later side (the section's first paragraph) is cut to its specific numbers. For example, delete "That rate is known only to a factor of ten." from E-14.tex:3, the clause "below $2q_{\mathrm{BZ}}$ the coherent zero-phonon part ... (\cref{sec:12.4})" from E-18.tex:3, and "The atoms leave the region where the force constants of \cref{sec:5.2} apply" from E-11.tex:3. These are edits for the block readers. List them in E2E-vol3-notes.md if they are not taken.

## 11. Chaps. 30 and 31 do not name the methods they use; Sect. 31.3 does not point to Sect. 28.1

- **Where:** ch30/ch30.tex:3, ch31/ch31.tex:3, ch31/E-20.tex:29.
- **What:** Only ch32.tex:3 names its methods chapter ("using the methods of \cref{chap:29}"). The pairs 27↔30 and 26/28↔31 are visible only inside sections. E-20 "Magnet inputs from DFT $+\,U$" (app:E.20-magnet) computes $U$ by linear response and exchange constants by four-state mapping, which is the method of Sect. 28.1 (E-9.tex:5-61), and never cites app:E.9 (grep: 0 hits).
- **Fix:** Add one clause to each opening: ch30.tex:3 "... using the methods of \crefrange{chap:23}{chap:27}"; ch31.tex:3 "... using the methods of \cref{chap:26,chap:28}". In E-20.tex:29, after "otherwise from DFT $+\,U$", add "(\cref{app:E.9})". These are pointers only.

## 12. Chap. 28 joins two unrelated sections; Defects belongs with Chap. 29

- **Where:** tex/ch28/ch28.tex:3-6; ch28/E-10.tex:38-40; ch31/E-22.tex:3.
- **What:** Sect. 28.2 (Defects) has a subsection "Displacement thresholds" that only points forward to Sect. 29.1 (E-10.tex:40 → app:E.11), and gives the 17.5 to 63.5 eV range a second time (E-10.tex:3 and :40). The specification that uses it, Sect. 31.5, says it is "built from the methods of \cref{app:E.10,app:E.11}". The two sections form one thread (supercell defects → recoil molecular dynamics). Sect. 28.1 (magnets, superconductors) shares nothing with Sect. 28.2 except the chapter. The ch28 opening holds them together with a last sentence about defects.
- **Fix (optional, lead decision):** Move ch28/E-10 to be the first section of Chap. 29. Retitle Chap. 28 "Magnets and superconductors" (title change only, label unchanged). Rewrite the last sentence of ch28.tex:3 as one clause of ch29.tex:3. Cut the subsection "Displacement thresholds" (E-10.tex:38-40) to its pointer, since Sect. 29.1 gives the protocol. If the chapter is not split, still cut that subsection: it repeats E-10.tex:3 and points forward.

## 13. Duplicate "Plane waves and the cutoff" subsections in Sects. 23.4 and 24.1; Sect. 24.1 has no opening paragraph

- **Where:** ch23/E-1.tex:41-78 and ch24/s3-5.tex:3-22, same title. The expansion of $u_{n\vect{k}}$ is written twice (unlabeled in E-1, eq:3.5-pw in s3-5). E-1.tex:77 uses eq:3.5-Ecut forward. ch24/s3-5.tex:1-3: the section starts directly with a subsection (the only section in the volume that does).
- **Fix:** E-1 comes first in reading order and keeps the expansion and $N_{\mathrm{PW}}$. In s3-5.tex:3-10 replace the second display by a reference to it, keep eq:3.5-pw only if another file uses the label (grep first), and retitle the subsection "The cutoff and the vertex" or similar. Its new content is the $2k_{\mathrm{cut}}$ bound and eq:3.5-Ecut. Give Sect. 24.1 a two-sentence first paragraph built from ch24.tex:3 material or from the existing first sentence of its first subsection.

## 14. Chap. 23 interleaves theory, derivation and practice of the band gap

- **Where:** ch23/ch23.tex:7-11. Sect. 23.1 ends with "The band-gap problem" and "The scissor shift" (s3-4.tex:68-160). Sects. 23.2 and 23.3 are the HF and HK–KS derivations. Sect. 23.4 is KS practice. Sect. 23.5 opens with "The scissor shift in practice" (E-3.tex:9).
- **What:** The scissor is introduced in 23.1 and taken up again in 23.5, with two derivation sections and the practice section between them. This is a mild order problem. The derivations prove equations of 23.1 and sit well after it.
- **Fix (low priority):** Move the subsections "The band-gap problem" and "The scissor shift" of s3-4 to the head of E-3 (Sect. 23.5), before "The scissor shift in practice". Alternatively, leave the order and make sure E-3.tex:9-15 only points back (eq:3.4-scissor) and does not restate. That is the block reader's call.

## 15. Chap. 25 Summary ends with a sentence copied from the text

- **Where:** ch25/ch25.tex:10, last sentence "each convergence statement belongs to the quantity, the energy range and the resolution for which it was made", verbatim from E-5.tex:73 (15 shared 7-grams).
- **Fix:** Condense it to a clause, or drop it and keep the preceding sentence on the energy window.

## 16. Forward references from specifications into Chap. 33

- **Where:** ch30/E-16.tex:7, 9, 11, 67 (sec:21.6, we:22-fsum); ch32/E-24.tex:42, 51 (sec:21.6).
- **What:** The library schema of Sect. 33.1 is cited by the specifications before it is reached. This is acceptable: the schema indexes the specifications (tab:21-schema, last column). Chap. 33 then closes the volume as the opening of ch33.tex:3 promises: tables → schema → open calculations → limits by theory, calculation and data. No move is proposed. Check only that E-16.tex:9 ("20 functions in all (\cref{sec:21.6})") does not count on a definition given only in Sect. 33.1. If it does, point to \cref{sec:10.4}, which E-16 already cites for the 12 functions.

## 17. Small items

- front/conventions.tex:5 (shared front matter, printed in Vol. III): the Limit Check paragraph cites Sect. 9.4 and Appendix F, and Volume III contains no `limitbox`. For the lead: either accept it as volume-independent front matter, or print the paragraph only in Volumes I and II (`\ifnum\volid<3`).
- Terminology (E2E.md "nuisance"): remaining uses in Part II, for the block readers: ch30/E-15.tex:7, 45, 49; ch30/E-18.tex:23, 33; ch31/E-17.tex:81, 83, 85; ch33/s22-1.tex:107 ("open problems and nuisance tables" → "open problems and uncertainty budgets"). The references to tab:12-nuisances (E-18.tex:39, 41) keep the label and change only the words around it.
- Summary tables: Chaps. 29, 31, 32 and Sects. 30.1, 30.4 end each section with a table of grids, tests and costs. Sects. 30.2, 30.3, 30.5, 31.2 and 32.4 have none. No fix proposed (no new content). Note it if the lead wants uniformity by trimming rather than adding.
- No chapter of Volume III has a chapter map, and none of the openings refers to one, so there are no stale map captions. Chap. 27 (IP → RPA → LF → TDDFT → BSE) is the only chapter whose content is a ladder in the sense of STYLE.md §Chapter maps. The ladder is already mapped in Sects. 4.6 and 4.9 of Volume I, so a pointer is enough.
- Length: 260 pages. Nothing here argues for adding material. Findings 1, 4, 7, 8, 9, 10 and 13 each shorten the volume.
