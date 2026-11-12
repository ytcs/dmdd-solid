
## From block ch01-ch02 + D.1-D.3
- appA/A-8.tex:5-9 ("Two Earth speeds"): restates ch01/s1-2.tex:81-86 (reference speed v_E^ref for thresholds and edges, full v_E(t) inside halo integrals), which the reader meets first. Suggest: cut the A-8 prose to the defining display and a \cref{sec:1.2}. (dup list pair s1-2:81 / A-8:7)
- appA/A-9.tex:22-28: redisplays eq:2.2-dsdq as eq:A.9-dsdq with the same sentence frame as ch02/s2-2.tex:27-33. Suggest: replace the A-9 display by a \cref{eq:2.2-dsdq} unless eq:A.9-dsdq is cited (grep first). (dup pair s2-2:27 / A-9:24)
- appA/A-2.tex:19-23 (Gaussian/SI conversion) and ch02/s2-3.tex:191 say the same thing; s2-3 already points to eq:A.2-map. Either side is acceptable; if trimming, keep A-2 (conventions home) and reduce s2-3:191 to the pointer, or leave both. (dup pair s2-3:186 / A-2:21)
- ch09/s9-2.tex:96: repeats ch01/s1-3.tex:65 (escape speed +-25 km/s -> v_max 3.1 %, m_min 6.3 %; annual -3.9 %/+3.4 %) with \cref{sec:1.3}. Suggest: keep the channel-specific numbers (acoustic edge, Dirac edge) and replace the floor and annual figures by "as in \cref{sec:1.3}". (dup pair s1-3:65 / s9-2:96)

## From the block reader of appA, appC, appB (hand-written), appD.tex, front

- **appC, volume shape.** C.10 (cited only by ch11), C.11 (ch18, ch20, appE D-43/44), C.12 (ch21, D-46, ch32), C.13 (ch17 only), C.16 (ch12 only) and C.20 (ch16, ch19, D-42, ch31) serve only Volumes II/III but print in Volume I, so their readers do not have them in hand. Suggest moving them to the Volume II derivations appendix (app:D-II), or folding C.13 into ch17/s17-6.tex at the tiers subsection (`eq:C.13-order`, `eq:C.13-height` move with it) and C.16 into ch12/s12-6.tex. Every C section is still cited (grep).
- **ch13/s13-9.tex:42** repeats the glide-phase argument for the vertex of appC/C-17.tex:85-90 (conjugation of e^{iq·r}, phase normal to the plane, η_c = η_v). Suggest reducing it to a pointer to `eq:C.17-selection`.
- **ch14/s14-4.tex:3** restates the C.19 opening (neutron spin couples to the same s_e(q) as spin-coupled DM). Minor; the clause "(\cref{app:C.19})" already carries it.
- **appA/A-5.tex:5 (`\int_V`) and appA/A-7.tex:21 (`VS_{ab}`)**: italic V where the normalization volume `\Vol` (script V) is meant; macros.tex reserves italic V for a potential. Plain typos, not changed because Appendix A symbols are frozen for this pass; lead to decide.
- **ch05/s5-6.tex:61-65 vs appC/C-6.tex**: the product formula `eq:C.6-product` and its application to u_κ(t), u_κ(0) were given in both; the C-6 application paragraph is cut to a pointer (log). No action needed.
- **appB/B-1.tex:1502-1503** (generated) still points to `app:D.17`, listed in E2E-undefined-labels.txt; the symbol-list generator needs the retarget.

## From block ch03, ch04, appD D-6 to D-12
- **dup pair ch03/s3-2.tex:7 / appA/A-5.tex:3** (Bloch normalization): ch03 is first; A-5 is the conventions home and states the same normalization as a convention. Suggest leaving A-5 as the reference statement or cutting its prose to the displays with a \cref{eq:3.2-bloch}; nothing to change in ch03.
- **dup pair ch03/s3-1.tex:126 / appC/C-2.tex:30** (lattice sum): C-2 already cites eq:3.1-latticesum and adds the infinite-crystal form; s3-1:139 points to C.2. No action needed.
- **dup pair ch03/s3-3.tex:203 / ch23/s3-4.tex:148**: ch23 reruns the we:3-kc bound with the LDA gap and cites we:3-kc; the repeat is the point there. No action needed.
- **ch03/s3-3.tex:24 (removed)**: the sentence "the value 1.11 eV of \cref{we:1-mmin} is the one commonly used in projections" pointed at a worked example that no longer uses 1.11 eV. Volume II (ch10/s10-9.tex:18, ch17/s17-1.tex:15, ch33/s21-6.tex:53) explains 1.11 eV as the step-model gap of the tabulated loss functions, so no fact is lost; no action needed.
