# Structural review of the spine: Chap. 8, Parts II–III (Chaps. 9–22) and Appendices E′, F (2026-11-01)
Severity: BLOCKER = must change before any Part II brief goes out; MAJOR = fix before the affected section is briefed; MINOR = edit
at briefing. Fixes that change the section list and renumber pointers (the Part I review's BLOCKER sense): S6, S16, S18. What I read: SPINE.md in full (Part I and Appendices A–E as the foundation), READER, STYLE, NOTATION, CONCEPTS, THREADS,
CLAIMS and skill §2. I re-derived every count and order below from SPINE.md, not from check_concepts.py.

| # | Issue | Section | Sev. | Proposed fix |
|---|---|---|---|---|
| S1 | Limitbox content is not specified. About 100 "Limit N.Mx" entries name a formula but not the parameter that controls the approximation, the fuller result to plot against, or the validity region. None of the 113 boxed rows has its comparison plot in a figure list or the budget. Several boxes hold two distinct formulas, not a row and its amendment (10.8d: dark Compton with the refuted ALP Eq. (3); 14.3a: the Larmor statement with the AFM weight; 16.8a). Several have no fuller result to compare with (11.5c, 11.6b, 14.6c, 16.8e–f, 19.4b) | all Part II–III | BLOCKER | Give each box a "Plot:" field: x = controlling parameter; curves = literature formula and the book's fuller result; validity region shaded; leading correction marked. Mark the boxes that use STYLE's fallback (parameter dependence with the validity boundary). One formula per plot, or one panel per row. Count the plots in each section's figures and budget |
| S2 | 9.4 outcome (i) and "Introduces" teach the retired box format ("source and equation, approximation chain, validity, leading correction"), which contradicts the user's limitbox directive and STYLE | 9.4, F.1 | MAJOR | Rewrite as: formula + one-line citation + comparison plot + one sentence on breakdown. The chain is in the text; the formal record is in App. F |
| S3 | The limitbox device is used in 8.1 and 8.2 (Limits 8.1a, 8.2a) before 9.4 defines it. CONCEPTS row "Limitbox" lists no uses because "Limit 8.xa" does not match its terms. Limit 8.2a boxes the Van Hove rate that 4.2 (ii) already derives from the same source | 8.1, 8.2, 9.4 | MAJOR | Introduce the device in the Chap. 8 opening or in 8.5; drop Limit 8.2a and cite 4.2 (F row L0 then stays at 8.2 as a no-box row); add `Limit ` to the match terms |
| S4 | The outline paragraphs of Chaps. 10–16 and 18–22 are section-by-section lists. STYLE says chapter openings are "introductory and motivational, not outlines … never a section-by-section list" | Chap. heads | MAJOR | Replace each with the chapter's physical question, why it matters and how it links back and forward, with at most one orienting sentence. Chap. 17's framing is the model |
| S5 | 13.7 "Computing the phonon-assisted rate" is a dedicated computation section, and the Chap. 13 head says "how to compute it (13.7)". This breaks directive (f) | 13.7 | MAJOR | Keep the physics: the adiabatic (Herzberg–Teller) limit, its error ω/δ_off, and what standard DFPT misses. Move the route, the controls and WE 13.7 (grids, cost) to App. E.5/E′.1. Retitle, e.g. "The adiabatic amplitude" |
| S6 | 17.5–17.7 rank "quanta" (ε_eh, F_eh; CLAIMS II-87 gives "quanta 3.37 eV") and screen on readout and backgrounds before Part III teaches them (18.2–18.4, 20, E′.14). 18.4 (iv) says ε_eh predictions for halides, fluorides and lead salts lie outside the validated range, which conditions 17.7's pool | 17.5–17.7 | MAJOR | Move 17.5–17.7 after Chap. 21: either a target-selection chapter that absorbs 22.4 (Outlook) to reach four sections, or the opening of Chap. 22 before the open-problems sections. Otherwise add forward markers and make 18.4 and 20.5 explicit inputs to Table 17.2 |
| S7 | 17.7 reads "the survivor list and its screens (thermal cycling, synthesis, readout, backgrounds)", while the framing says "current capability is a column of the guide, not a filter". The columns of Table 17.2 are not specified | 17.7 | MAJOR | Make the screens columns of Table 17.2 (leader with P(first) and rank interval; capability; missing demonstration; deciding measurement). "Survivor" then means eligible by data quality only |
| S8 | Open results are presented as established. 13.10 (i) lists "≈ 0.51 MeV leading" (an estimate) among the "established edges". Its key result is tagged "VER as estimates … stated as open". Outcome (iii) (masses where the phonon-assisted rate is the only channel) depends on the CL onset and an estimated rate | 13.10 | MAJOR | Split Table 13.1 into established rows (zero-phonon edges, glide rule, ordering) and open rows (onset, leads, two-channel band, rate and reach). Make (iii) conditional. Tag the estimates CL or open, never VER |
| S9 | Status tags disagree between sections and the F map: Limit 8.1a REF vs L-O2 VER; Limit 11.1a REF vs L-F1 VER (CLAIMS II-29 VERIFIED); Limits 11.8b, c VER vs L-D4, L-D5 REF; LT3 (17.7 backgrounds) REF while 17.7 says "estimated only [CL]"; L43 carries "OPEN", which is not a defined tag | 8.1, 11.1, 11.8, 17.7, F | MAJOR | Reconcile with CLAIMS; give L43 the tag GAP |
| S10 | Duplicate: 10.7 covers "the electronic and lattice responses" (purpose, Limit 10.7a, E′.4 pointer), and 11.7 covers lattice anisotropy again | 10.7, 11.7 | MAJOR | Limit 10.7 to electronic responses. 11.7 owns the lattice part and the combined amplitude, and the lattice half of Limit 10.7a moves there |
| S11 | Re-teaching Part I in Chap. 8: positivity (4.2 iv vs 8.3 i); the species-resolved f-sum (4.3 iv + D.6 vs 8.3 ii + D.26); the single-operator rate (4.2 ii vs 8.2 + D.25); WE 8.3 "recovering 2.2" vs WE 4.4 | 8.2, 8.3 | MAJOR | 8.3 cites 4.2 and 4.3 and derives only the mixed third moment and the Ward identities. D.26 drops its f-sum part. Replace WE 8.3 with a two-operator example |
| S12 | Duplicate: placing literature formulas on 𝔗 is done in 8.5 (Fig. 8.2, WE 8.7, "every LIMITS formula as a point of 𝔗"), again in 9.4 (Table 9.3, WE 9.4) and again in F.1 | 8.5, 9.4 | MAJOR | 8.5 defines the label and the small-parameter table; 9.4 alone does the placements. Alternatively, fold 9.4 into 9.1 + F.1, which saves about 3,000 words |
| S13 | Duplicate with a forward use: dark-photon absorption at the silicon indirect edge appears in 10.8 (the 77 K overestimate, which CLAIMS II-24 says is derived in 13.5), in 13.5 (temperature transfer) and in 13.9 (phonon-assisted absorption) | 10.8, 13.5, 13.9 | MAJOR | Home it in 13.5/13.9; 10.8 keeps a forward pointer only |
| S14 | Gap: a likelihood is used in 8.8 (iv) ("propagate into a likelihood") and 14.6 (iii) ("exponential-bin likelihood") with no defining section and no CONCEPTS row. Profiling appears only in 21.4, and READER assumes no statistics beyond what 1.5 recaps | 8.8, 14.6 | MAJOR | Add "likelihood and profile likelihood (recap)" to 8.8 Introduces, or a new App. C row; 14.6 points back to it |
| S15 | Gap: 10.6 calls Foldy–Wouthuysen a "recap", but the Dirac equation is taught nowhere (READER excludes QFT; 3.5 gives only the (Zα)² estimate). 10.9 (relativistic density row, "Dirac treatment") and 12.5 (contact density) also need it | 10.6, 10.9, 12.5 | MAJOR | Add an App. C row "Dirac equation and the Foldy–Wouthuysen reduction", or a recap in 3.5, and point to it from all three |
| S16 | Gap: 12.6 introduces "photon emission and minimal coupling (precise)" with no earlier operational row. READER assumes classical EM only, and 6.5 does not introduce the quantized field. The section also carries a new crystal bremsstrahlung formula and Migdal-type absorption in 4,000 words | 12.6 | MAJOR | Add a recap of the quantized radiation field (App. C, or extend 6.5) and raise 12.6 to about 5,500 words, or split it |
| S17 | Fluff by template: the (g) sections 10.10, 11.9, 14.7, 15.5 and 16.9 restate gaps already stated at home (14.7 repeats LE-72, 92, 99 and 117 from 14.2, 14.4 and 14.5). 22.1–22.2 restate them a third time, and each chapter's 700-word summary a fourth | (g) sections, 22 | MAJOR | State each gap once at home. (g) sections keep only the nuisance table and sizes. 22.2 is a table by reference. Merge 14.7 and 15.5 into the chapter summaries (saves about 6,000 words) |
| S18 | Overloaded sections: 10.8 (six processes, four boxes, seven F rows, 5,500); 16.8 (six boxes, seven rows, 5,000); 16.7 (four boxes plus two new results, 5,000); 10.9 (four kinds of dark-matter kinematics, 4,500); 14.5 (five target classes, 4,500); 20.1 (seven rows, 5,000). The plots of S1 add to each | as listed | MAJOR | Split 10.8 (bosonic absorption / two-insertion processes). Move defectons and crowdions from 16.8 to 19.6. Raise 10.9, 14.5 and 16.7 to about 6,000 words or split them |
| S19 | App. E/E′ pointers match by list but not by content. E′ rows promise quantities whose sections do not point to them: E′.3 (relaxed static step ↔ 10.2; orbit–orbit f-sum ↔ 10.6); E′.4 (finite-q density factors ↔ 12.5, which points to E′.5; nuclear momentum distributions ↔ 11.4; dynamical Born charges ↔ 12.6; elastic constants ↔ 17.7); E′.6 (glasses, random media ↔ 16.7; chiral three-phonon branching ↔ 14.5); E′.8 ↔ 16.2–16.6; E′.12 (exciton kinetics ↔ 18.5); E′.13 (coherent inputs ↔ 14.6; two-insertion ↔ 10.8; Fano map ↔ 13.6); E′.14 (spin-dependent nucleon inputs ↔ 11.6). E rows: E.8 ↔ 13.8; E.10 ↔ 16.6; E.6 ↔ 16.4; E.12 ↔ 20.1, 20.3–20.5 | E, E′ | MAJOR | Add the missing section pointers and the matching (→) entries; extend the check to E′ content lists |
| S20 | Titles: 12.4 has a colon; 13.1 is a clause ("Why indirect gaps open a window"); 19.1 is a long phrase; 16.1 repeats 7.3's title exactly; 9.4 repeats App. F's title; 18.4 nearly repeats 3.3; Chap. 16 is a four-item list | titles | MINOR | E.g. "Phonon final states at small momentum", "The indirect-gap window", "The recoil hand-over", "Dirac-material rates", "Limitboxes", "Pair energies in Si, Ge and GaAs", "Further targets" |
| S21 | Dependency: 16.4 lists "Frenkel → 7.4", but 7.4 defines the Frenkel pair, not the exciton (the shared match term `Frenkel` hides this). 10.10 names Frenkel excitons in NaI (LE-32) before 16.4 defines them | 16.4, 10.10 | MINOR | Change the prerequisite to excitons → 4.9, add a forward marker in 10.10, split the match term |
| S22 | Dependency: 13.1 uses "exciton replica" before 13.9. 19.5 uses the Luke gain g_L before Luke emission (20.1). 19.2 lists a forward item ("Lindhard-type models … precise in 19.3") as a prerequisite, and the term matches the 4.5 Lindhard function, a different concept. 8.5 omits its prerequisites sudden limit → 6.1 and Migdal effect → 6.1 | 13.1, 19.2, 19.5, 8.5 | MINOR | Add forward markers; move the Luke effect into 19.5 Introduces; give "Lindhard quenching" its own terms; complete 8.5's prerequisite list |
| S23 | Couplings and physics that are not taught: the B − L vector (11.6); scalars coupled to m_e or α (11.8 iv); fermionic absorption operators (missing from 8.1's "every interaction"); Landé g_J (14.3); the magnetic neutron cross-section (14.4); Bloch equations and NMR (14.6); the spin–boson ohmic bath (16.8) | 8.1, 11.6, 11.8, 14.3–14.6, 16.8 | MINOR | Add the operators to 8.1 and Table 8.1; list the rest as "(recap)" in each section's Introduces |
| S24 | Minor duplicates: the silicon f-sum split three times (WE 4.7, WE 8.4, Limit 17.5a; the 16.6 eV value of WE 4.10 again in 17.5a); stopping (4.4/WE 4.9 vs 19.3 iii); the Al gap (7.2, 9.2, 15.1, 15.5); the soft acoustic limit (8.3/D.26 vs 13.6/D.37); the Fano term and Dyson convention (8.6 vs 13.6 iv); the Cauchy–Schwarz band (8.3 vs 10.4 iii); LO–TO/LST (5.5 vs Limit 11.2d); recast exactness (21.1 iv vs 21.5 iv); the special-displacement quadrature (13.8 ii vs App. E.8); Limit 21.1a and Limit 10.1a both box 1509.01598's standard rate (Eq. (17) vs (3.17): check whether these are the same equation) | as listed | MINOR | Cite the earlier home, keep one derivation, and box a formula once |
| S25 | Outcomes: 9.1 (iv) is not testable; 11.7 (iii) (sapphire, SiC) has no key result behind it; 20.1 (v) "states" a Luke rate that is CL; 22.4 adds no new content (3,000) | 9.1, 11.7, 20.1, 22.4 | MINOR | Reword 9.1 (iv); add the 11.7 estimate to its key results; phrase 20.1 (v) as open; cut 22.4 to about 1,500 or merge it into 22.1 |
| S26 | NOTATION: clashes and missing symbols (detail in §8) | 9.2–20.5 | MINOR | Add the rows and rename the clashing symbols |
| S27 | App. D is numbered out of section order (D.41 → 16.8 before D.42 → 14.1). D.33 promises "four truncations", but 12.4 does not point to it | D | MINOR | Renumber; add 12.4 → D.33 or narrow D.33's description |
| S28 | Atlas: the cell "mobile defects × nuclei → 16.8" points to a section with no dark-matter rate (defect kinetics only). Random-media scattering (16.7 v), quantum crystals (11.5) and two-insertion processes (10.8) have no row or column | 9.1 | MINOR | Re-home or drop the cell; add the missing rows or a note under the table |
| S29 | Running example: silicon is carried well through 10–13 and 18–21, but Parts II–III add 17 contrast materials beyond STYLE's list (LiF, sapphire, SiC, diamond, TeO₂, CsI, YIG, MnF₂, Te, α-quartz, anthracene, PbS, WSi, NaI, a-SiO₂, ⁴He, Xe) | II–III | MINOR | Extend STYLE's contrast list, or mark these "cited where needed" |
| S30 | Front-matter reading paths stop at Chap. 8. The experimentalist path ("chapter openings and limitboxes of Part II") misses 17.5–17.7, which the user's framing writes for experimentalists | front matter | MINOR | Give section-level paths for Parts II–III |
| S31 | 15.1 (iv) and 15.5 use the Al bulk gap 0.18 meV as established (VER) while "the measured bulk gap" is listed as open. Unlabeled open items (15.5 ×3, 16.9, 18.2 ×2, 13.7, 17.7 ×3, 20.1 ×2, 10.9 ×2, 19.2) fall outside the 42 exact-gap rows | 15, 22.2 | MINOR | Call 0.18 meV the weak-coupling estimate; list every open item in Table 22.2 |
| S32 | 20.5's discrimination verdicts are tagged REF, but they rest on estimated memory-loss numbers and on an unrefereed transport validation (20.2, E′.12) | 20.5 | MINOR | Tag VER (estimate) and phrase the verdicts conditionally |

## 1. Dependency violations (re-derived)
Method: for every Chap. 8–22 entry I checked each prerequisite and each concept named in its purpose, outcomes and key results against
the defining section, using the CONCEPTS rows only as a list of defining sections. Violations not caught by the script:
- **The limitbox device** (S3): used in 8.1 and 8.2 and defined in 9.4. **Status tags** are "defined at the head of Part II" but used in
  Chap. 8. This is writer-side only and harmless if the head of Part II moves before 8.1.
- **Forward uses**: 10.8's 77 K claim needs 13.5 (S13); 17.5–17.7 need 18.2–18.4 and 20 (S6); 13.1 uses exciton replicas (13.9); 19.5 uses
  the Luke gain (20.1); 19.2 lists a forward prerequisite (S22).
- **Wrong pointer hidden by a shared match term**: 16.4 "Frenkel → 7.4" (S21); 19.2 "Lindhard-type" (S22).
- Otherwise every prerequisite points backward, and Part II–III order is consistent with the DAG (8 → 9 → 10 … 21 → 22). 18.4's "survivors
  of Chap. 17" is a backward use, but it shows the circularity of S6.

## 2. Gaps (Part II–III needs that Part I does not teach)
Not taught and not deferred: the likelihood (S14), the Dirac equation and Foldy–Wouthuysen (S15), and the quantized photon field for
emission (S16). Also the minor items of S23: the B − L and m_e/α-scalar couplings, fermionic absorption operators, Landé g_J, magnetic
neutron scattering, Bloch equations, the spin–boson bath; and continuum elasticity beyond WE 5.3 (11.1 introduces the Christoffel
problem; 20.3 needs acoustic impedance). Everything else Part II–III needs is in Part I: response, screening, BSE, phonons, Debye–Waller,
e–ph, BCS, Dirac, defects.

## 3. Duplicated coverage
MAJOR: S10 (anisotropy), S11 (Part I re-taught in 8.2–8.3), S12 (𝔗 placements), S13 (the indirect-edge absorption), S17 (gaps stated three
or four times). MINOR: S24. There is no case of the same cell explained twice in two voices: the atlas gives each cell one home.

## 4. Budget realism (3,000–6,000 per section; no hard cap, fluff cut)
All 101 sections lie inside 3,000–6,000 words (4 × 3,000; 7 × 3,500; 27 × 4,000; 33 × 4,500; 19 × 5,000; 11 × 5,500).
- Overloaded: S16, S18, and 12.3 (four boxes, 5,500, borderline).
- Fluff and template repetition: S17; 9.4 (S12); 22.4 (S25); the 17.1–17.3 overlays are mostly figures and could be about 3,500 each.
- The change log's own trims (merge 16.4 into 16.3, 14.4 into 14.1) are sound. Neither section is padding, but both are short.
- Unbudgeted: about 113 comparison plots (S1). Each needs the book's fuller result computed, so this is figure and compute load, not words.

## 5. Learning outcomes
Each outcome was checked for testability and for backing in the same section's key results. The failures are S2 (9.4 i, wrong format),
S8 (13.10 i, iii), S25, and S9's status conflicts, which decide whether an outcome is "taught as established". The rest are concrete
("derive …", "evaluate … for silicon") and are backed by a key result or worked example in the same entry.

## 6. Directive compliance
- No exercises, checkpoints or tasks: compliant. The only "by hand" phrases are worked examples 17.6 and 18.2, which are demonstrations.
- Computational connection: woven in at first appearance in 25 of 101 entries. Violation: 13.7 (S5). Missing pointers: S19. 21.6
  (libraries) is a data specification and is acceptable; keep its method content in E′.
- Silicon as running example: compliant (S29 minor).
- Titles: S20.
- Chapter openings: S4.

## 7. App. D/E/E′ pointers (both directions)
- **D.24–D.47**: every D.n named in Chaps. 8–22 exists and points back. D.33 is shared by 12.1–12.3. Issues: S27.
- **E.n**: every named E row lists the naming section, and every Part II–III "(→ …)" entry is named by its section (checked by hand for
  E.2, E.4–E.13). Missing: S19.
- **E′.n**: all 14 rows are named by at least one section, and every E′ citation in a section appears in the row's "(→ …)". The
  content-level mismatches are in S19.
- **A and C rows** with Parts II–III users (A.2, A.4, A.7–A.9, C.3, C.4, C.6, C.7, C.10–C.13) match both ways. C.8 says only "Part II"
  (name the sections).

## 8. NOTATION
The planned symbols cover nearly everything Chaps. 8–22 introduce, and clash entries 50–69 handle the research letters well.
- **Missing**: c_NR1 and "η(c + u)" (17.5); g_J and Landé g ("g/2", 14.4); ρ∞ (18.2); k₂, and r, ω₀ of the Klein relation (18.4); T_CM
  (14.5); q_BZ (11.9); c_L, c_LA (10.2, 11.1); bulk modulus B (11.1); ε_in, ε_out, ε_r (16.3, 16.7); a_mol, a_s, N_ch, v_a (16.2, 16.4);
  ℓ_mfp (15.3); Ī (19.3); P_abs, Σ₁, Σ₂ (20.3); T_hi, T_lo (16.8); m_a, x (10.8); E_r, q̃ (16.3, 16.5); σ_χN (16.7); 𝔤_IL^nor (15.1–15.2;
  NOTATION has 𝔤_I).
- **Clashes**:
  - Σ₁, Σ₂ (20.3) vs the self-energy Σ;
  - bare S as a spin length (14.1) vs "bare S only" for the structure factor;
  - bare v in t_l = 4d_f/(v t̄_esc) (20.3) vs the dark-matter speed;
  - bare c in m_min^ac vs the speed of light;
  - bare F(q) (12.5) vs entry 59;
  - δ₀ (13.6) vs tanδ₀ (16.7);
  - η(c + u) vs entry 52;
  - Landé g vs the vertex g;
  - ℓ_mfp vs ℓ_Qν and the cubic index ℓ;
  - m_a vs m_φ;
  - μ_eχ (16.3) vs the mandated μ_χe;
  - 𝓃_e(R_κ) (8.3) vs 𝓃(r);
  - n(ω) (12.6) vs the band index n.

## 9. Open problems stated as open?
- Mostly yes: 13.1 (onset CL), 10.9, 15.3, 18.2, 19.2, 20.1, 20.4 and 22 all state their CL and GAP items as open.
- Failures: S8 (13.10), S9 (LT3), S31 (Al gap), S32 (20.5), and 19.6 ("LEE bound and structure: VER; two steps missing, stated as open":
  split it into an established bound and an open model).

## 10. The Chap. 17 guide and the limitbox design
- **Guide**: the user's framing is recorded, and 17.7 has a leader with probability, the missing demonstration, deciding measurements
  and "no reading" verdicts (Migdal, light mediator). Problems: its position before Part III (S6), screens versus columns (S7), and the
  unspecified columns of Table 17.2. 17.7's open items (L(k, ω) for survivors, elastic constants, backgrounds) are correctly marked
  open, but LT3 contradicts them (S9).
- **Limitboxes**: the design principle and STYLE agree (a plot, not a procedure list). The spine does not yet implement them: S1 and S2,
  and F.1 should describe the record table, not the box.

## 11. Coverage claims, re-derived from SPINE.md
- **LIMITS**: 155 F-map rows; no duplicate Row label; each row names exactly one section (113 with a box, 42 without). Every one of the
  101 distinct "Limit N.Mx" names in the sections occurs in the F map, and every F-map box occurs in a section (10.3b only breaks across
  a line in 10.3). Exactly one home: holds. Status conflicts: S9.
- **Atlas**: 23 excitation rows × 6 columns = 138 cells; 48 filled, 90 "—"; each filled cell names one section. Holds, with the
  questionable cell of S28.
- **Exact gaps**: 44 distinct LE labels occur in Chaps. 8–22. LE-107 and LE-108 occur only in a Sources line, which leaves **42 in
  open-problems fields**, so the count holds. "Exactly one home" fails for 7 of them: LE-72, 92, 99 and 117 sit in 14.x and again in
  14.7; LE-73, 74 and 82 sit in 8.6 and again in 22.2 ("restated"). Also, at least 14 open items carry no LE label (S31), so the 42 is
  not the full open set.
- **Deferred computations**: DC-1…98 each occur in exactly one E′ row (98 distinct, none duplicated, none missing). The DC lists cited in
  sections (10.10, 11.9, 14.7, 15.5) agree with those rows. Holds.
