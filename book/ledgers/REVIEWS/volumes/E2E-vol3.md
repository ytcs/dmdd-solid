
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
