# Volume II, end-to-end review: structural reader

Read: tex/vol2.tex, all chapter drivers (openings, map captions), the first paragraph of every section, every Summary, every table caption, the duplicate list E2E-vol2-dups.txt, and the contents of build/vol2.pdf (build of 01:09, 850 pp.). Block readers are editing at the same time, so line numbers can drift by a few lines. Page estimates use about 500 source words per printed page for running text and about 900 per page for \scriptsize tables.

Findings are ranked by importance. Each gives file:line, what is wrong, the fix and the estimated saving.

**Total from the structural changes below: about 65 pp.** Items 1–4 account for about 42 pp of it, and item 14 (optional, by tool) adds about 10 pp. This brings the volume to about 775–785 pp. The rest of the way to 600 has to come from cuts inside sections, the Pareto rule applied by the block readers.

---

## 1. Uncertainty records: one item is kept in up to five places (about 14 pp)

A sized truncation or an open question is currently recorded (a) in its home section, often under a subsection "Open problems"; (b) in the chapter's uncertainty table ("nuisance table"); (c) for Chaps. 10 and 11, again in a prose section that restates the sizes; (d) in tab:21-dominant; and (e) in tab:22-gaps. The silicon phonon-assisted window "known to a factor of ten" shows the pattern. It appears in the opening of Chap. 13, in Sect. 13.9 with its table and open problems, in the opening of Chap. 21, in tab:21-dominant, in the opening of Chap. 22 and in tab:22-gaps.

There are also three different layouts. Chapters 10 and 11 give the budget a whole section (sec:10.10, ch10/s10-10.tex:1–95; sec:11.9, ch11/s11-9.tex:1–89). Chapters 12 and 13 give it a subsection (ch12/s12-6.tex:125; ch13/s13-9.tex:143). Chapters 14–21 put the table inside the unnumbered Summary (ch14/s14-summary.tex:17, ch15/s15-summary.tex:13, ch16/s16-summary.tex:22, ch17/s17-summary.tex:17, ch18/s18-summary.tex:15, ch19/s19-summary.tex:15, ch20/s20-summary.tex:17, ch21/s21-summary.tex:18). A Summary that holds a 600–1100-word longtable no longer condenses the chapter. Every one of the 12 captions repeats the legend ("Type in the classes of Sect. 8.8: normalization, tilt, threshold, new support … Basis …"), and the prose before the tables re-explains what a template, an estimate and a spread are (ch10/s10-10.tex:25; ch11/s11-9.tex:7–15).

Fix:
- **One uncertainty budget per chapter, in one place.** Make it the last subsection of the last numbered section, titled "Uncertainty budget of the … rate", as the Terminology note of E2E.md asks. Take the tables of Chaps. 14–21 out of the Summaries.
- **Define the legend once.** Put it in the caption of tab:10-nuisances, or in Sect. 8.8. The other 11 captions say "classes and basis as in tab:10-nuisances".
- **Short cells.** Each cell holds a number, a type and a home section, with no prose. A row whose only content is "unsized" goes, and its question stays as one sentence in the home section. The 12 tables come to about 8,000 words now and can drop to about half.
- **Cut the restating prose.** In sec:10.10, cut "Many-body spread" (s10-10.tex:5–16) and "Gap and threshold" (:17–22) to the facts that stand nowhere else: the spread between the two tabulations (×1.18) and the 0.1 eV band-energy shift. Move those into Sect. 10.2 next to the tables they qualify, and delete the section. Do the same for sec:11.9 (s11-9.tex:5–28): the incoherent, anharmonic and temperature templates restate Sects. 11.3, 11.5 and 8.5.
- Savings: 10.10 prose about 3.5 pp, 11.9 prose about 3 pp, 12.6/13.9 lead-in about 1.5 pp, table cells about 5 pp, legends about 1 pp.

## 2. Chapter 22 indexes what the chapters already state: dissolve it (about 9 pp)

- **The chapter says so itself.** The opening (ch22/ch22.tex:2) says "Each of these statements stands in the section where its quantity arises". The key result (ch22/s22-2.tex:7–9) says "Each gap is stated once, in the section where the quantity arises".
- **The gaps table is a copy.** tab:22-gaps (s22-2.tex:21 ff.) is a landscape longtable of about 2,700 words, about 6 pp. Its "strongest statement" and "missing step" columns re-copy those sections, and it carries rows for Chap. 8 of Volume I.
- **The opening describes a section the chapter no longer has.** "\cref{sec:22.1} orders the open calculations by the result each would change" (ch22/ch22.tex:4): sec:22.1 is now Sect. 33.2 in Volume III.
- **The genuine content of Sect. 22.2 has other homes.**
  - sec:22.3, the scope of the master formula (s22-3.tex:5–37), belongs in Sect. 9.1. Its "empty cells" and "allowed but computed in no section" (ch09/s9-1.tex:77–92) are the same question: which processes the atlas does not cover.
  - Charged-current absorption (s22-3.tex:38–84) is a channel with its own rate. It belongs after "Fermionic absorption on nuclei" (ch11/s11-4.tex:102 ff.; see item 10).
  - Radiative decay and ion tracks (:85) go in Sect. 9.1 as one sentence each.
  - The charge-density-wave modes (:91) go in Chap. 16, which collects targets that need a conserving response.
- Fix:
  - Delete sec:22.2 and tab:22-gaps. Where a gap is only a "proof" item (the three gaps of the decomposition theorem), it already stands in Sect. 8.6.
  - Move the sec:22.3 pieces as above.
  - Fix the pointers to Chap. 22 in the opening of Chap. 21 (ch21/ch21.tex:4, "what remains open is indexed in Chap. 22") and in the map caption (ch21/ch21.tex:9, "The last box is the index of open problems of Chap. 22"). Redraw fig:21-map without that box.
- Saving about 9–10 pp: the table 6, prose 1.5, summary and opening 1, plus a chapter start under openright.

## 3. Summaries are 2–5 pages and restate sentences of the text (about 13 pp)

Prose Summaries, not counting the tables in them: Chap. 9 761 words, Chap. 10 933, Chap. 11 1,053, Chap. 12 793, Chap. 13 1,055, and Chaps. 14–21 between 890 and 1,540 (Chap. 16: 1,538). In total about 13,000 words, about 26 pp.

Some of them repeat text almost verbatim:
- ch16/s16-summary.tex, second paragraph ("One gram of fused silica cooled from room temperature to 10 mK still releases 46 pW an hour later, and the power falls as 1/t") repeats the first sentence of Sect. 16.8 (s16-8.tex:3).
- The first paragraph of ch9/s9-summary.tex retells the first paragraph of Sect. 9.1 with the same counts (24 rows, 144 cells, 57/8/79).

Fix: hold each Summary to the results and numbers a reader takes away, at most about 450 words. Do not retell the sections in order. Saving about 13 pp.

Only the Chap. 9 Summary is in the contents (s9-summary.tex:1 has \addcontentsline). Make all of them consistent one way or the other.

## 4. Sect. 9.4 and tab:9-limitchecks duplicate Appendix F, and their counts are stale (about 6 pp)

- **Duplicate index.** tab:9-limitchecks (ch09/tab9-3.tex, longtable of about 1,570 words, generated by figscripts/ch09/fig9_3.py) lists every Limit Check of Chaps. 10–17. Appendix F lists the same boxes with source and leading correction. fig:9-axes (s9-4.tex:30) and "Placement on the truncation label" (s9-4.tex:19–49) sort the boxes by axis. That is a catalogue of the boxes, not physics of a model that stays (Addendum 2: "A Limit Check box has no standing of its own").
- **Stale counts.**
  - tab9-3.tex lists 75 boxes. Only 59 limitbox environments are left in Chaps. 10–17. Its rows for lim:10.1a, 10.3a, 10.9a–c, 11.1c, 11.2c–d, 11.4b, 12.2b, 12.3d, 12.6a, 13.5a, 13.7a, 14.5b and 15.2a now point at removed boxes.
  - s9-4.tex:3 and :52 and s9-summary.tex:9 still say "90 published formulas … 80 of them in 75 boxes … 25 … the other 50".
- Fix:
  - Keep the one paragraph on how to read a box (s9-4.tex:5–18, "The comparison plot"). Better, fold it into front/conventions.tex, which already introduces the boxes and points to Sect. 9.4.
  - Delete "Placement on the truncation label", fig:9-axes, tab:9-limitchecks and "The table of limits" (s9-4.tex:50 ff.). If the lead wants the "controlling parameter" and "leading correction" information, it becomes one column of Appendix F's tab:F-rows.
  - Delete the last paragraph of the Chap. 9 Summary.
  - Retarget \cref{sec:9.4} from front/conventions.tex and appF/appF.tex.
- Saving about 6 pp (Sect. 9.4 runs to 7 pp).

## 5. Chapters 9, 17 and 21 each redo the kinematic edges and the interference cells (about 6.5 pp)

- **Interference, twice.** "Overlap regions and interference" with tab:9-overlaps (ch09/s9-3.tex:26–52) gives the dark-photon cross terms with the same numbers (196 + 196 − 392 = 0; 5.47×10⁻⁴) that Sect. 17.4 derives (ch17/s17-4.tex:5–14). The caption of tab:9-overlaps already sends the reader to sec:17.4 for each row. Fix: cut s9-3.tex:26–52 to two sentences ("Overlap is not interference; amplitudes interfere only for a coupling to both species and at the boundary of the two electronic sectors, Sect. 17.4"), and delete tab:9-overlaps. Repoint the Chap. 9 Summary. Saves about 1.5 pp.
- **Lightest masses, four more times.** The lightest mass of each channel is derived in Sect. 9.2, which has the general formula eq:9.2-mch, tab:9-edges and we:9-acoustic (s9-2.tex:5–86). It is derived again in:
  - "Kinematic ceilings of the sectors" (ch17/s17-1.tex:5–12; the same ceilings E_R^max and ω_max, from eq:1.3);
  - "Endothermic thresholds" with tab:17-endo (ch17/s17-3.tex:94–130). Its Δχ = 0 column repeats tab:9-edges (0.333 MeV, 18.3, 10.35, 6.12 keV);
  - "Threshold masses as floors" (ch21/s21-1.tex:84–93; again 0.3332/0.3374/0.405 MeV);
  - and partly the reach part of "Acoustic edge and effective sound speed" (ch17/s17-5.tex:77–80).

  Fix: Sect. 9.2 is the one home. Add the endothermic formulas eq:17.3-endogap and eq:17.3-endolin, and the Δχ = 10 meV and 1 eV columns, to Sect. 9.2 / tab:9-edges, and delete s17-3.tex:94–130. Cut s17-1.tex:5–12 and s21-1.tex:84–93 to pointers; the June floor (0.3202 MeV) stays in Sect. 21.1 because it is about the halo. Saves about 3 pp.
- **The phonon figure of merit re-derives Sect. 11.1.** "Acoustic edge and effective sound speed" (s17-5.tex:77–167, about 4 pp) re-derives the plateau, the "44 times the edge" rule and the window corrections from Sect. 11.1 (ch11/s11-1.tex:97–147). Its tab:17-speeds (s17-5.tex:148) checks a published table of sound speeds against measured elastic constants, an audit of the kind Addendum 2 lists. Fix: put eq:17.5-cNR1 and the window derivation into "Heavy mediator" of Sect. 11.1 (s11-1.tex:137). Sect. 17.5 then keeps the figure of merit and its window as a pointer. Keep only the rows of tab:17-speeds that a ranking uses (CsI, TeO₂, the computed tensors). Saves about 2 pp.

## 6. Sects. 17.6 and 21.6 rank the same crystals with the same method (about 3 pp)

- **What repeats.**
  - The eleven-crystal pool is defined in Sect. 17.6 (ch17/s17-6.tex:31) and again as the "survivor pool" in Sect. 21.6 (ch21/s21-7.tex:9).
  - Sect. 21.6 says it uses "the method and widths of Sect. 17.6 unchanged" (s21-7.tex:11).
  - The CsI and lead-salt paragraph appears twice: s17-6.tex:124 ("Crystals outside the pool can lead. CsI …") and the opening of s21-7.tex:3 ("CsI has a heavy-mediator single-phonon rate … 3.73 times …").
  - "Reach bands from input uncertainties" (ch16/s16-9.tex:43) applies the same input-width idea to the novel targets.
  - The inputs tables in the Summaries of Chaps. 14 and 15 (s14-summary.tex:52, s15-summary.tex:40) and tab:16-inputs are three separate tables of provenance and inputs.
- Fix: keep the method (provenance widths, Monte Carlo ranks, tiers, correlated method errors) in Sect. 17.6. Make Sect. 21.6 add only what is new there: the full pool, readiness, backgrounds and tab:21-next. Delete s17-6.tex:124 ff. Merge the three inputs tables into tab:17-provenance, or into one table in Sect. 17.6.
- Saving about 3–4 pp.

## 7. Chapter 13: the silicon-window edges are split between Sects. 13.1 and 13.9, and the window table appears three times (about 3 pp)

- **The kinematic part is split.** Sect. 13.1 gives directional upper values for the zero-phonon edge and defers the real edge to Sect. 13.9 ("Onset precision and the zero-phonon edge", ch13/s13-1.tex:101–106, which ends with a paragraph about computational cost). Sect. 13.9 opens by saying "Here the zero-phonon side is evaluated with bands over the whole zone" (s13-9.tex:3), then gives "The zero-phonon edges" and "The glide-parity selection rule" (s13-9.tex:5–56). The directional values are superseded by the whole-zone search.
- **The same edge masses are tabulated three times:** in tab:13-window (s13-9.tex:110), in tab:9-edges and in tab:17-edges (ch17/s17-1.tex:72).
- Fix:
  - Move s13-9.tex:5–56 into Sect. 13.1 in place of s13-1.tex:101–106, and delete the directional upper values.
  - Sect. 13.9 keeps the rates at and across the window.
  - Keep one table of window masses, tab:13-window. The Si rows of tab:9-edges and tab:17-edges cite it.
  - The silicon-window sentence in the openings of Chaps. 9, 13, 21 and 22 should stay only in Chap. 13 and in one place in Chap. 21.
- Saving about 3 pp.

## 8. Inelastic and fermionic dark matter are spread over three chapters (about 2 pp, plus a cleaner Chap. 17)

- Inelastic and exothermic scattering appears in Sect. 10.9 (ch10/s10-9.tex:5) and again in Sect. 17.3 (ch17/s17-3.tex, "Inelastic scattering into collective modes"). Sect. 17.3 is a channel calculation (new rates for down-scattering into phonons, magnons and plasmons), not a comparison. The map caption of Chap. 17 calls it a "side branch".
- Fermionic absorption appears on electrons (s10-9.tex:125), on nuclei (ch11/s11-4.tex:102) and as charged-current absorption (ch22/s22-3.tex:38).
- Fix:
  - Move Sect. 17.3, without its endothermic part (item 5), to follow Sect. 11.8, as "Inelastic dark matter and collective modes". Alternatively, make Sects. 10.9 and 17.3 one section at the end of Chap. 11.
  - Put charged-current absorption under Sect. 11.4 (item 2).
  - Chapter 17 is then left with 17.1, 17.2, 17.5 and 17.6, which are comparisons.
- Saving about 2 pp in openings, captions and repeated set-up.

## 9. Sect. 17.4 is the last mixed-sector calculation and belongs at the end of Chap. 13 (order; about 0.5 pp)

The opening of Chap. 12 promises it this way (ch12/ch12.tex:2: "Chap. 13 treats the second [mixed sector] and Sect. 17.4 their interference"). Sect. 17.4 derives the Migdal–phonon-assisted cross term and its positivity bound (s17-4.tex:15–64). This is physics of the two sectors just computed, and a reader of Chap. 13 should not have to jump four chapters ahead for it.

Fix: make it the last section of Chap. 13, before the silicon window (Sect. 13.9), or right after it. Update the map captions of Chaps. 12, 13 and 17, tab:9-overlaps (if kept) and the cell column of the atlas.

## 10. Dependency order: formulas used before their home section

- **Lindhard's formula.** It is displayed and labelled in the colour-centre section, eq:16.6-lindhard (ch16/s16-6.tex:50–55), and that section says "Sect. 19.3 derives it". Sect. 19.3 is its home ("Lindhard's integral equation", ch19/s19-3.tex:34) and cites it by the Chap. 16 label (s19-3.tex:3, :66). The Kinchin–Pease count is given the same way in s16-6.tex:56 and is the subject of "Displacement count" (ch19/s19-4.tex:22). Fix: display both in Sect. 19.3 and Sect. 19.4. Sect. 16.6 keeps a one-line forward pointer; the equation label stays where the display goes, and the lead retargets it.
- **The coherent classical-field regime.** It is set out in general in Sect. 14.6 (ch14/s14-6.tex:5–42), but already used for acoustic modes of a finite body in Sect. 11.8 (ch11/s11-8.tex:112–176, for example :172 "for records shorter than the coherence time the mean power is not a rate"). Fix: Sect. 14.6.1 is the general statement. Move it ahead of its first use, as the first subsection of "Acoustic modes of a finite body" in Sect. 11.8. Sect. 14.6 then starts from the Bloch equations.
- **The coherent-field likelihood.** "The exponential-bin likelihood" (s14-6.tex:111 ff.) is limit statistics. Move it to Sect. 21.5, next to the other limit constructions.
- **A forward reference for a number.** Sect. 20.4 opens with a number taken from Sect. 20.5 (ch20/s20-4.tex:3, \cref{sec:20.5-meanfield}). Either give the 0.59 THz soft end where it is first derived, in Sect. 20.2 "The scaling spectrum", or keep the pointer and note that it is forward.

## 11. Sect. 16.8 is detector kinetics and belongs in Part "Detection" (about 1.5 pp)

The opening of Chap. 16 already says so (ch16/ch16.tex:2: "The tunneling defects of glasses also release heat at millikelvin temperatures, and their kinetics shape the delayed signals of Sect. 19.6"). Sect. 16.8 (relaxation by phonons and electrons, hopping and tunneling, heat release, interacting two-level systems; 10 pp, with App. E.12) is not a dark-matter target. Sect. 19.6 takes its tunneling exponent from sec:16.8-hop (ch19/s19-6.tex:3), and "Defect kinetics at millikelvin" (s19-6.tex:5) writes its own master equation.

Fix: move Sect. 16.8 into Chap. 19 as the section before 19.6, "Two-level and defect kinetics at millikelvin", and merge sec:16.8-hop with sec:19.6-kinetics. Sect. 16.7 keeps the target physics (absorption and scattering on two-level systems). Saving about 1.5 pp from the merged kinetics; the main gain is order.

## 12. Sect. 19.4 is a fragment of Sect. 19.5 (about 1 pp)

Sect. 19.4, "Defects and stored energy" (ch19/s19-4.tex, 1,700 words), opens with the same calibration deficits (6.08 %, 4.8 %) that Sect. 19.5 then inverts. Sect. 19.5 reaches back for "the silicon datum of sec:19.4-calib" (ch19/s19-5.tex:226), and its subsections "The measured defect fraction" and "Upper bounds on the stored energy" (:176, :188) treat the same data.

Fix: make Sect. 19.4 the first subsection of Sect. 19.5 ("Reservoirs of the deposit", s19-5.tex:5). Keep its displacement count and stored energy per Frenkel pair, and drop the repeated statement of the datum.

## 13. Appendix E: short sections that repeat their chapter (about 3 pp)

Per Addendum 2 (item 2), these sections, each under about 1,100 words and titled almost exactly like their chapter section, are candidates to fold into the chapter at the point of use:
- E.3 (appE/D-32.tex, 1,101 words), "Impulse limit and Doppler width", against Sect. 11.4;
- E.4 (D-33, 946 words), "The joint electron–lattice response", against Sect. 12.1, which has the same title;
- E.5 (D-34, 1,082 words), "Moments of the Migdal spectrum", against Sect. 12.5, which has the same title;
- E.17 (D-47, 937 words), "Theory nuisances in a profile likelihood", against Sect. 21.4.

The duplicate list also flags s13-4.tex:76 against D-36.tex:59 and s15-4.tex:40 against D-40.tex:45.

Fix: the owning block reader checks each of these sections for steps the chapter lacks. If none, cut the section; if a few, move them into the chapter and remove the section. Each removed section saves its header and the repeated notation paragraph, about 0.7 pp.

## 14. Appendix B: 26 pp of symbols (optional, by tool; about 10 pp)

B-1-vol2.tex (15,700 words) lists every symbol first used in the volume, including symbols used inside one subsection only. If the generator kept only symbols used in more than one section, together with all symbols of Appendix A, the list would roughly halve. This is the lead's decision, since the appendix is generated.

## 15. Threads opened and not closed, and removals not followed through

- **Crystal form-factor box.** lim:10.1a has been removed from Chap. 10, but these places still cite it or rest on it:
  - ch21/ch21.tex:2 (the opening sentence of Chap. 21: "screening changes the silicon electron-recoil rate at 5 eV by a factor of two (lim:10.1a)"), the only undefined reference in a chapter driver;
  - ch09/s9-4.tex:41;
  - ch11/s11-7.tex:55;
  - ch13/s13-3.tex:46, :48;
  - ch21/s21-1.tex:54;
  - ch21/s21-2.tex:33.

  Similarly, lim:11.1c (s17-5.tex:90) and lim:11.2d (s17-5.tex:173) point to removed boxes. Fix: the owners retarget each to the section (sec:10.1, sec:10.2) or to the figure that now carries the number. Regenerate tab9-3 or delete it (item 4).
- **Crystal form factor and loss-function rate.** With its box gone, Sect. 10.1 (crystal form factor, 4 pp) is the independent-particle stepping stone that Sect. 10.2 screens. Sect. 10.10 (s10-10.tex:13) shows that the two independent-particle tabulations disagree by 1.18. Fix: make Sect. 10.1 the first subsection of Sect. 10.2 ("the independent-particle limit"), keeping its normalization and convergence paragraphs. This saves about 1 pp and removes a section whose own model the chapter then supersedes.
- **Absorption at the silicon edge, three times.** "Optical data near the silicon edge" (ch10/s10-7.tex:42), "Temperature transfer of absorption data" (ch13/s13-5.tex:56) and "Phonon-assisted absorption of bosonic dark matter" (ch13/s13-8.tex:97) all treat dark-photon absorption between the indirect and the direct gap, and each points to the others. Fix: Sect. 13.5 is the home. Cut Sect. 10.7.2 to one pointer and keep in Sect. 13.8 only the exciton-replica part.
- **Open-problem subsections in 12 sections, then indexed again.** Sects. 10.5, 10.6, 10.8, 10.10, 12.6, 13.9, 16.7, 19.2, 19.6, 20.1, 20.4 and 21.6 have "Open problems" subsections, and these are indexed again by tab:22-gaps and by sec:21.7-open (ch21/s21-7.tex:95). After item 2, keep them where they are and delete sec:21.7-open, which lists the missing inputs of the ranking. Alternatively, keep it as the one cross-channel list and remove the duplicates of its items from Sects. 16.9 and 17.6.

## 16. Map captions and openings untrue of the chapters as they stand

- **Chap. 14 is out of order.** The map caption (ch14/ch14.tex:7) runs 14.1, 14.2, 14.4, 14.3, 14.6, 14.5, which is the logical order: scattering, then neutron data, which replace the scattering response of 14.1, then absorption, then coherent fields (which continue absorption to ultralight masses), then chiral targets. The sections run 14.3 (absorption) before 14.4 (neutron data). Fix: swap Sects. 14.3 and 14.4 so that neutron data follow scattering, and put Sect. 14.6 before Sect. 14.5. The order then matches the caption and the opening sentence of the chapter ("which magnetic targets … how far measured neutron data … which crystals respond differently to q and −q … when an ultralight field must be treated as a coherent classical wave"), with chiral targets last and the Summary reordered to match. This is a pure reorder.
- **Chap. 22 opening:** describes sec:22.1, which is now in Volume III (item 2).
- **Chap. 21 opening and map:** point to Chap. 22 as the index of open problems (item 2). The map's dashed box "the response library … specified in Sect. 33.1" draws a Volume III section inside a Volume II map. Keep one pointer in the text and drop the box (Addendum 3).
- **Chap. 9:**
  - The second paragraph of the opening (ch09/ch09.tex:4) promises "for each pairing … the section that computes it, the lightest dark-matter mass it reaches and where its final states lie". It does not promise the Limit Check catalogue of Sect. 9.4. After item 4 the opening is true without that section.
  - Its counts "two dozen kinds of excitation and six classes of coupling" agree with tab:9-atlas.
- **Chap. 17 opening** (ch17/ch17.tex:2): "most comparisons an experimentalist needs are spread over seven chapters". After items 6 and 8, add nothing; the sentence stays true.
- **Chap. 10 map caption** (ch10/ch10.tex:9): "the spread across these approximations is a nuisance of the rate (Sect. 10.10)". Retarget to the uncertainty budget once item 1 is applied, and change the wording ("nuisance" → "uncertainty"; E2E Terminology).
- **Chap. 11 map caption** (ch11/ch11.tex:9): "the truncations as nuisances (Sect. 11.9)". Same fix.

## 17. Smaller items

- The section and subsection titles still use "nuisance", as listed in E2E Terminology, and the block readers must rename them. Check also the section title "Theory nuisances in a limit" (sec:21.4), where "nuisance parameter" is legitimate but the bare noun is not. Suggested: "Theory uncertainty in a limit".
- Ch14 has "The 1/|S| corrections as nuisances" (s14-2.tex:116) and Ch15 has "Corrections and nuisances" (s15-2.tex:69). Rename both, or move their content into the chapter budget (item 1).
- The Summary of Chap. 9 is the only Summary in the contents (item 3).
