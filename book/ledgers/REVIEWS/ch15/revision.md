# Chapter 15 revision (2026-11-06): item → done/how

Files revised: tex/ch15/ch15.tex, s15-1 … s15-4, s15-summary; tex/appD/D-39.tex, D-40.tex; Ch15 rows of tex/appF/F-rows.tex;
narrow R1 edits in tex/ch07/s7-2.tex (v_F, ξ_coh) and tex/appE/E-20.tex (WSi k_F𝔩_e, N^El/P^El); NOTATION.md (rows + clash entry 86);
tex/bib/book.bib (+3 entries: malica2020quasi 2109.13551, sacepe2020quantum 2007.15870, allen2015electron cond-mat/0407777, all
checked against the arXiv API). tex/ch06/s6-4.tex needed no edit (it prints v_F = 2.0e6 m/s, k_F = 1.75 Å⁻¹, E_F = 11.7 eV, all
consistent with the new set). Scripts: new figscripts/ch15/al_constants.py (+ .log); bcs15, edge15 (unchanged), tab15_1, limit15_1a,
limit15_2a, we15_1, film15, abs15, fig15_3, we15_4, map15 edited and rerun with their logs; fig15_1, limit15_4a, a2ftr15 rerun;
map13.py rerun as the brief asks (no change to ch13; map15.py also rerun). Build: see the end of this file.

## Rulings

| Item | Done / how |
|---|---|
| R0 (i) clean limit ℓ ≫ ξ₀ ≈ 1.6 µm | 15.4.3 "Three conditions…" first condition; 15.3.1 states the single clean criterion (ξ_coh = 2.4 µm free-electron, 1.6 µm tabulated, Kittel Ch. 10 Table 5); key result eq:15.4-sJ, summary, F row, nuisance row carry it. |
| R0 (ii) 10⁴ gain only over phonon-only clean-Al; film 2.0e-12 vs 1.5e-12 | 15.4.3 second condition; summary par. 4; F row. Numbers in fig15_3.log ("50 nm film, ALP at 0.72 meV …"). |
| R0 (iii) line shape: F₁ᵃ, triplet p-wave vertex, strong coupling g×~1.2; integrated weight by sum rule | 15.4.3 third condition (factor 1.196 for 1/(1+λ_ep), λ_ep = 0.43 of 6.4; fig15_3.log). Sum-rule robustness (exact spin f-sum; zero spin stiffness, Knight-shift analogy) stated in 15.4.3 and derived in a new D.40 paragraph (spin dipole commutator, local spin conservation of H_MF, no s-wave ladder on the odd vertex). SOC caveat (fraction ~ spin-flip rate/Δ; controlling for heavy elements) added. Literature: published projections "take the spin-current response equal to the current response, as for independent electrons"; no novelty wording. |
| R1 one Al set | figscripts/ch15/al_constants.py: a = 4.05 Å, m* = m_e → k_F = 1.749 Å⁻¹, **v_F = 6.753e-3** (the ruling's "≈ 6.76e-3" is k_F rounded to 1.75; the lattice constant gives 6.753e-3, printed 6.75e-3), E_F = 11.65 eV, ω_p = 15.78 eV, k_TF = 4.05 keV. Imported by bcs15, limit15_2a, film15, abs15 (we15_4, fig15_3 via abs15). All Ch15 numbers regenerated; loss ratios moved ≤ 0.004, 𝔳 moved +10 to +40 % (0.40→0.44, 0.20→0.21, 0.049→0.052, 0.003→0.004, 0.16→0.22 at y = 2.05). 7.2: v_F → 6.75e-3 (two places), ξ_coh 2.3 → 2.4 µm (other 7.2 numbers unchanged at printed precision, al_constants.log last line). E.20: v_F = 2.0e6 m/s unchanged (2.02e6). 0 K elastic constants (DATA-ADDENDA; Kamm–Alers via Malica–Dal Corso Table 2): c_LA = 6.51, c_TA = 3.42 km/s in 15.1, 15.4, inputs table. |
| R2 y-cut | Criterion logged in limit15_2a.log: keep y where the edge value L_cons/𝔤_I L^nor varies ≤ 10 % (max/min ≤ 1.1) over 𝔩_e = 30 nm–100 µm. y = 3: 1.058 (kept); y = 2.5: 1.751 (excluded) → cut y < 3 (boundary between 2.5 and 3). Adopted in 15.2-nuisance, summary par. 2, nuisance table, F row. The old bare-first-order 3.8 criterion is gone. "Masked/cells" removed everywhere. |
| R3 two-sided remainder | Clean scan over halo momenta: L_cons/𝔤_I L^nor ∈ [0.980, 1.085] for y ≥ 3 (tab15_1.log), impurity edge max 1.091 → −2 % to +9 %, two-sided, standard-normal constraint; dirty off-edge stated as not computed; "can only raise the signal" and "fall with q" removed ("largest on the edge"). Clean edge values carry the 𝔩_e clause (15.2-cons "These are clean values; at y ≤ 2.5 they hold only for 𝔩_e ≳ 10 µm"; 15.1-first last sentence points to 15.3-sc). |
| R4 fine-grid thresholds | limit15_1a.py now root-finds with one definition ("within 10 %" = smaller/larger ≥ 0.9, stated in the lim:15.1a caption). With the R1 v_F: Lindhard 7.86 (Δ/qv_F ≤ 0.0499) → 7.9/0.050; 4× edge 6.26 → 6.3; 𝔤_I L^nor 2.250 → 2.25; **bare 9.11 → 9.1** (9.19 at the old v_F; the R1 change moves it, limit15_2a and limit15_1a agree). Fig. 15.2b: 0.642 and 9.82 → 0.64, 9.8 (film15.log root-finder). Lindhard limit: 6e-5 at 10³Δ and 8e-7 at 10⁴Δ (new mpmath quadrature in tab15_1.py). "Within 8 %" → 9 % (15.1-chain, summary). Gray band of fig:15-limit-chain now at the root (7.86). |
| R5 sheet | eq:15.3-sheet presented as the leading term in q_∥d of Lasenby–Prabhu Eq. (19) (lasenby2022dark); WE 15-film: 540 leading, 588 exact slab (film15.log, LP Eq. (19) evaluated with the WE ε); summary and nuisance row "leading order (588 exact slab)". QROCODILE paraphrase: "strong at q ~ 1 nm⁻¹ and already significant at q ~ 1 keV for energies above 4 eV", "electrostatic problem of a single 2 nm WSi layer in vacuum". |
| R6 15.2 opener kinematics | Rewritten: threshold-mass particle scatters at q = 2ω/v_max; q_min/(ω/v_max) = 2.00, 1.17, 1.03 at m_min, 2m_min, 1 keV (tab15_1.log); "a few times heavier than m_min". |
| R7 overlaps | Conserving edge values: home eq:15.2-cons + tab:15-edge; 15.1 keeps 𝔳's definition, its maximum, the non-monotonic q dependence and the 0.954/1.048/1.053 check; five-value lists cut. Algebra + single quadrature recipe: D.39 (new subsections "The pair function" with the hyperbolic substitution, eq:D.39-Fcont, partial fractions, cutoff cancellation; "Quadrature of the conserving response"); 15.1 points there; the Gauss–Legendre recipe sentence removed. Mean free path: old 15.2.3 moved into 15.3.3 (sec:15.3-sc) with one normalization (÷ 𝔤_I L^nor at the same rate, as tab:15-edge; the Mattis–Bardeen limit is quoted in it too: 0.157/0.985/1.094/1.023 against the 30 nm column 0.187/1.008/1.091/1.021); 15.2 points forward. The WE 15-film "1.26 vs 1.091" mismatch is gone. AB pole: statement in 15.1-closed (with the proof pointer to D.39 and the scope: pole term exceeds the whole shift at y = 2.2, 58 % at 2.5, 16 % at 3, none at 5; limit15_2a.log), 15.2 gives its positions and the corrected reason (y ≲ 2.3 pole, y ≥ 3 continuum); repeat in 15.3 deleted. 𝔣_L: defined (with its one-line derivation) in 15.2; 15.3 gives only the complex continuation (eq:15.3-fL kept as that display). "Kinematic edge" defined at first use in 15.1 and distinguished from the pair-breaking edge; 15.2 retitled "Screening at the kinematic edge", its key result and lim:15.2a retitled; map15 node updated. |
| R8 numbers/typos | WE 15-film ×10⁶ and Im 0.234×10⁵ (now (3.48 + 0.234i)×10⁵ with the R1 gas; Im ratio 440, |ε| ratio 30). WSi: Einstein relation per Zhang row (film15.log): 2.7–3.3e47, bound 3.4e47; x = 0.85 tabulated 4.1/3.8 not reproduced (stated); ratio to gas 2.4–2.9. Gan: gap 0.26 meV (15.3-wsi), locators Sect. V (estimate and 5Δ) and Eq. (8) (ε_BCS); Hochberg 2021 "Eqs. (1), (S.13)"; Hochberg 2023 "Eq. (2) and text". WE 15.1 share 20 % (exact split of the ω integral, we15_1.log 0.197). Ladder 4e-4 averaged over the integrand (2.6e-4 most energetic phonon; 1.5e-6 at 1 meV; we15_4.log). Summary/table: bare "0.53 for y ≥ 3 and 0.38 at y = 2.2"; ×1.13 heavy kept (printed in WE 15.1 and logged). 𝔰_BCS → π²/2y (tab15_1.log y𝔰 → 4.935). Re ε^cons < 0 at y = 2.2 (1 + δ = −0.18, limit15_2a.log) stated in 15.2-cons. "Wavelength" → "1/q" / "length 1/q" (WE 15-edge, 15.2-nuisance, 15.3.1). M_{s2} phase explained via O_{s2} = −i(B† − B); |M_η|² step written out. |
| R9 language/provenance | "masked cells" and the tab:15-edge data-generation sentence removed (with the R1 v_F the impurity data at x = 0.390 differ from the book's 0.392 by ≤ 0.004 and their 𝔩_e labels become 1.000 µm/29.9 nm; logged in limit15_2a). Strong coupling: normal-metal factor 1/(1+λ_tr)² known (Allen 2015 Eq. (3), read), superconducting case open (15.4.4, summary, nuisance row, F row). Allen 1971: "as quoted by Hochberg, Lin and Zurek" (15.1, 15.4, F row); no "Ref. [29]". Pair lists cut to anchors + table pointers (15.1, 15.2, summary). Register: "however", "since", "of course", "we will" added; "gives"/"so" thinned; "turns out", "The physical picture is simple.", "The numbers are large.", "does not care", "knows nothing", "not a corner case", "does not screen more weakly", "per cent", "forty percent" removed. 16.2 "??" → plain prose ("need the response of a layered medium, which we do not treat here"); the sec:20.4 pointer replaced by plain prose in the summary. |
| R10 | Dirty limit: ∫₂^∞(𝔤_I − 1)dy = 2 stated; 0.05 % attributed to the Drude shape (flat σ_n gives 1.000000, cutoff 50 vs 500 eV identical; fig15_3.log — the cutoff plays no role, so the text names the Drude shape only). Electron–electron absorption: named in the 15.4 opener and as an unsized nuisance row (and F row); no size printed. |
| R11 notation | ω_AB → Ω_AB (\varOmega); v_F upright throughout 15.1 and the F rows; D.39 h, h(ω), g, G, T → 𝔥, 𝔨, 𝔨̃, δ𝔤, Y_tail; "1 + δ_𝔰 = 1.336" corrected to "bare 1 + δ = 1.329 against 1 + δ_𝔰 = 1.318" (new v_F); 𝔣_L(ν) → 𝔣_L(𝔴), ν_γ → 𝔴_γ; NOTATION row "𝔤_IL^nor" deleted, L^BCS → L^bare/L^cons; ε_BCS → ε^bare; Eliashberg Δ(E) → Δ^El(E); rows added (clash entry 86). check_notation.py on ch15 + D.39 + D.40: 0 gaps; default set 0 gaps. |

## Earlier editor-note items addressed to the review

| Item | Done / how |
|---|---|
| 15.3: merge the two mean-free-path passages | Merged into 15.3.3 (R7). |
| Sheet factor priority check | Verified by derivation-2; now cited as the LP kd ≪ 1 limit (R5). |
| E.20 WSi k_F𝔩_e ≈ 1 | E.20: "of a few (1.8–5.5 from its measured transport)". |
| Al v_F 6.67/6.77 | R1. |
| Attributions (Anderson 1959 credit only; QROCODILE width inferred; WSi interaction-disorder uncited) | Anderson unchanged (credit); QROCODILE sentence conditional ("If that width is added as …"); Altshuler–Aronov enhancement and Finkel'stein T_c suppression named and credited to Sacépé–Feigel'man–Klapwijk Sect. III.2 (read). |
| 15.1 9.4 vs 9.2 | R4 (now 9.1 with R1). |
| ω_AB clash; upright v_F; 𝔣_L(ν); L^BCS row | R11. |
| Gan only numerical; closed form is D.39 | Unchanged wording ("in resummed form"; 15.2 opener now "write it in resummed form"). |
| 0.39 vs 0.397 caption | R9. |
| Strong-coupling gap correction unsized | Nuisance row kept ("size unknown"). |
| 15.4 TOP PRIORITY spin current | R0, R10 (spincurrent-check: CORRECT WITH CAVEATS). |
| Free-electron ω_p 15.78 vs 15.7 | R1 (15.78 everywhere). |
| E.20 N_s, P_s | → N^El, P^El. |
| α²F_tr empty-core failure, 1/(1+λ_tr) | Unchanged (deferred); strong-coupling wording R9. |
| Conserving response closed form; resummed bare bubble label | 15.2 calls the resummed form the bare bubble; no physical claim rests on the first-order term (R2). |
| Allen 1971 unread | R9. |
| NOTATION row 1068 misparse | Deleted. |
| Duplicate pair-function reduction D.39 vs 15.1 | There was none; the reduction now lives only in D.39 (R7). |
| WE 15.1 bulk vs film gap | Unchanged physics; numbers regenerated (3.26/2.65 kg⁻¹yr⁻¹, ×1.23). |

## Report items (beyond the rulings)

derivation-1: all WRONG items fixed (P9 → R3; P6 → R4; P2 → 8e-7; P8 → 20 %; Gan Sect. V; AB-pole reason → R7). GAPs: k_TF²/q² ≥ 5.8e5;
"four digits" → explicit 1.0531 vs 1.0529 at y = 5; π²/2y; DC-RESULTS 𝔩_e clause; "in resummed form"; y = 5 range 0.80–0.86 now
single-rounded (0.801–0.856); e^{−209}; "every correction to the absorptive part"; D.39 O(ln y′/y′⁴); D.39 δ_𝔰 label; D.39 symbol
clashes; 15.2-cons cites eq:D.39-resum instead of restating it; log law kept in D.39 with a short pointer in 15.2; "ratios depend on
y and qv_F/Δ alone" kept once (15.2-resum). Gan (Δ/v_FQ)² vs 𝔳 like-with-like: 15.2 compares the response coefficient (27) only.

derivation-2: 1 (sheet) R5; 2 (QROCODILE) R5; 3 (0.64/9.8) R4; 4 (0.53/×1.13) R8; 5 (4e-4) R8; 6 (WSi DOS, Gan 0.26) R8; 7 (mass
convention, superseded sound speeds, NOTATION rows, clean criterion) R1/R11/15.3.1; 8 (e–e) R10; 9 (Dq² = 0.042Δ, excess not
established) 15.3.3 last sentence (film15.log). QROCODILE "microwires" used. 0.52 mass: "transport-weighted mass enhancement",
λ_tr. Ω, N defined at eq:15.4-a2Ftr and eq:15.4-T.

prose.md: chapter opening split, question once, orienting tail cut to one sentence, "bound by Δ" fixed; C1 lists → anchors; C2
connectives; C3 edges/retitle; C4 one value per quantity (k_TF 4.05, ω_p 15.78, clean criterion in 15.3.1, upright v_F, ε^bare,
𝔴/Ω_AB, "percent", \SI); C5 process language removed ("takes milliseconds", "specified in", "named, open" → "size unknown",
"reports … so that their difference measures it" → "computes the rate with and without it"); C6 one E.20 pointer per section;
O1–O7 done (O7: 𝔤_I L^nor removed from lim:15.2a, which now plots the resummation only; 15.1a keeps the chain); seams done;
section items: ordinal references removed (15.1 l.33/35), 15.1 algebra moved to D.39, l.76 phrasing, l.101 restatement cut, l.112
caption restatement cut, l.134 heading restatement cut, l.140 "all three controlling parameters", l.153 "which has no gap"; 15.2
items l.3, l.33, l.63, l.78 (paragraph deleted, useful sentence into the box), l.82, l.95, l.100, l.102, l.104; 15.3 items l.39, l.43–49,
l.63, l.88, l.90, l.92, l.96, l.102, l.104, l.127 (count dropped, paragraph moved to the end), 15.3.5 folded into 15.3.2 as three
numbered warnings ("Of course, …"), l.145, l.147; 15.4 items l.3, l.20, l.34, l.71, l.86, l.102 (restatement cut), l.114, l.124,
l.126, 15.4.4 retitled "Strong coupling and the transport function" with the scalar paragraph as a run-in heading, l.130; summary
"density matrix" → "Nambu matrix η of the density", table labels; D.39 title, symbols, duplicate; D.40 "Landen transform" glossed.

reader-a: WE 15-film typos; Al set; mask rationale (R2); 9 %; kinematic edge; M_s2 phase and |M_η|² step; Re ε < 0; 1/q; "the bubble
gives −2N_F and the ladder vanishes"; measure reason (D.39: cosh b db = cosh a da); M^N superscript named; WE 15-alrate marked
numerical with its quadrature; cutoff cancellation reason (D.39); impurity-dressed response stated (Born self-energy ηGη, same
ladder on density and pair vertices; E.20 pointer); retarded-branch formula for complex 𝔴 given at eq:15.3-fL; Ω, N defined; J_e as
the scalar Σ_α J^{αα}; 1 − cos θ bookkeeping written out. Not done: the phonon-pole correction (c_LA q/ω)² stays asserted
(standard; unchanged).

reader-b: all fix-list items 1–7 done; 8 (optional): Ward identity, Goldstone and Anderson–Higgs named once in 15.1; GL/H_c2/Einstein
relation/sheet resistance glossed and the E.20 methods paragraph marked skippable with glosses; Born-impurity Nambu structure
given; strong-coupling "open" narrowed (Allen 2015). Eliashberg N^El, P^El given a one-line picture (retarded interaction, energy-
dependent gap). v_max reminder added to the 15.1 opener. Ch. 1 "(??)" near ζ is outside this chapter (not touched).

spincurrent-check.md: caveats 1–5 → R0 text and D.40 paragraph (conserving-approximation remark and Knight-shift analogy included).

## Changes the campaign ledgers need (not edited here)

state/CORRECTIONS.md
- Supersede CW4 (8.1)/SPINE edge table (0.33–0.40 … 0.94–0.96) as physical and the type-Δ "KK spread" nuisance (l.343, l.391): the
  book uses the conserving response (DC-41) and a two-sided edge remainder −2 % to +9 % for y ≥ 3.
- New global value: aluminum free-electron set m* = m_e (v_F = 6.753e-3, E_F = 11.65 eV, ω_p = 15.78 eV, k_TF = 4.05 keV) replaces
  v_F = 6.67e-3 / 6.8e-3 (SPINE, SOTA, DC-41 𝔩_e labels). Record that DC-41's Γ → 𝔩_e conversion used 6.8e-3 (labels change by 0.6 %).
- Exclusion region: energies y < 3 (criterion: ≤ 10 % variation of the conserving edge value over 𝔩_e = 30 nm–100 µm) replaces the
  y < 3.8 mask based on the bare first-order term.
- 15.1's 9.4/8.2/6.5/2.3/0.049 thresholds were grid artefacts; current values 9.1/7.9/6.3/2.25/0.050 (book v_F).
- Room-temperature Al elastic constants still used in tex/ch06/s6-4.tex (force-constant fit of fig:6-a2F, a2ftr15.py) and
  tex/appC/C-18.tex l.106 (acoustic impedance): superseded by DATA-ADDENDA (C11 114.3, C44 31.6 GPa, §19.13(g)); a refit is owed at
  the next Ch6/App. C pass (outside this brief's scope).
- Zhang et al. Table I N₀ for x = 0.85 is inconsistent with their R_s and D (Einstein relation gives 3.3e47/3.0e47 against 4.1/3.8).

SOTA.md
- l.354/375/393: "≤ 16 % at 5Δ", "8–16 %", "y ≲ 3.5" → first-order term 17 % at y = 5 (v_F 6.753e-3); conserving edge values
  0.867/0.999/1.069/1.067/1.023 (clean, y = 2.2…10), impurity range 1.008–1.091 for y ≥ 3; exclusion y < 3.
- l.674 spin-current entry: status "verified with caveats" (spincurrent-check.md); add the three R0 conditions: clean only for
  ℓ ≫ ξ₀ (bulk), the 10⁴ gain is over phonon-only clean-Al projections (film: 1.5e-12 vs 2.0e-12 from MB σ₁), line shape not fixed
  (F₁ᵃ, triplet vertex, strong coupling ×1.2 in g); integrated weight protected by the exact spin f-sum and zero spin stiffness.
- Strong coupling: the normal-metal factor 1/(1+λ_tr)² = 0.52 is a known result (Allen 2015 Eq. (3)); only the superconducting
  extension is open.
- Sheet screening: leading-order factor = kd ≪ 1 limit of Lasenby–Prabhu Eq. (19); exact slab 588 vs 540 at qd = 0.086.

LOOSE-ENDS
- Open: origin of the 20 % excess of the 30 nm conserving value over the local Mattis–Bardeen limit at y = 2.2 (Dq² = 0.042Δ).
- Open: dirty-film conserving response off the kinematic edge (edge remainder off-edge with impurities not computed).
- Open: electron–electron (umklapp) contribution to the intrinsic σ₁ of Al near 1 meV (named, unsized; the reviewer's
  A ≈ 3e-6 µΩ cm K⁻² estimate is unverified and not printed).
- Open (Ch16): stacks of sheets / full slab response; the sec:16.2 pointer was replaced by plain prose.
- Open: triplet p-wave vertex / possible sub-gap triplet mode in the spin-current channel; Landau F₁ᵃ of Al.
- SPINE open problems to add (editor note 15.4): coherence factor of phonon-assisted spin-current absorption near the edge; scalar
  absorption near the edge (amplitude channel).

NOVELTY
- Record: direct spin-current pair breaking of ALPs in clean singlet superconductors — CORRECT WITH CAVEATS (spincurrent-check);
  published Al projections (1604.06800, 2106.12586) omit it by the Π_ΣΣ = Π_11 assumption; no prior paper found; no novelty wording
  in the book (R0).
- Record: exact identity ∫₂^∞(𝔤_I − 1)dy = 2 (dirty spin-current weight conservation) and the exact collapse of the phonon-assisted
  amplitude (eq:D.40-T) as book-phase results; the sheet factor is not new (Lasenby–Prabhu kd ≪ 1).

DEFERRED-COMPUTE
- "Unsized leading corrections (App. F)": add electron–electron absorption (Holstein/MB F row) and keep the spin-current line shape
  (F₁ᵃ, triplet vertex) and the strong-coupling gap in scattering as unsized.
- Existing deferred items unchanged: first-principles α²F_tr below a few meV (umklapp failure of the empty-core model, ×1.25e4);
  Eliashberg superconducting renormalization (E.20); impurity-dressed conserving response on the full (q, ω) grid (E.20); dirty
  off-edge remainder (new); refit of the 6.4 Al force-constant model with 0 K elastic constants (new, light Python).

## Build

latexmk -pdf -outdir=/tmp/claude-0/build-ch15rev main.tex: 0 LaTeX errors, 0 undefined citations, no undefined reference from Ch15, D.39, D.40 or the Ch15 F rows (the 321 unresolved references book-wide point to unwritten Chaps. 16–22 and App. D.47/B.2). Remaining Ch15-area boxes: one 9 pt overfull text line in 15.4 (Debye paragraph) and a 46 pt float-page box in D.40 at output time. Lint: 0 blocking hits in all eight files. check_notation (ch15 + D.39 + D.40): 0 gaps.

## Post-check fixes (postrev-check.md: ACCEPT WITH FIXES)

| Fix | Done / how |
|---|---|
| 1. Spin sum rule (D.40, 15.4.3) | D.40: [[H, D_s], D_s] is a quarter of the charge-dipole constant, compensated by the normalization of eq:15.4-sJdef. For the full Hamiltonian the exact sum is the total weight (π/2)ω_p² (free-electron ω_p, interband included); (π/2)(ω_p^intra)² is exact for a one-band Hamiltonian with spin-independent interactions. 15.4.3 sentence states both. |
| 2. Summary par. 4 | Clause added: the sum rule fixes the weight; the line shape depends on F₁ᵃ, a triplet interaction and strong coupling. |
| 3. E.20 l.7, l.82 | Im ε^BCS, L^BCS → Im ε^cons, L^cons. |
| 4. lim:15.4a | "following Allen as quoted there". |
| 5. 7.2 l.230 | "a wavelength 1/q" → "so 1/q = 0.73 µm". |
| 6. Docstrings | fig15_3.py (v_F 6.753e-3, γ_rel 26.65 meV), we15_4.py (v_F, ρ for sound speeds), bcs15.py. |
| 7. Optional | al_constants.py now uses ρ(0 K) = 2.73 g cm⁻³ for the sound speeds (ρ_T = 2.70 stays for rates): c_LA = 6.47, c_TA = 3.40 km/s; (c_LA/v_max)² = 6.6e-5; phonons below 2Δ for m_χ < 3.2 keV (3.15); phonon momenta 29.7/56.4 eV, k_F 61 times larger; averaged ladder 4e-4 at 2.2Δ (unchanged), 1.4e-6 at 1 meV. Printed in 15.1, 15.4, the inputs table, F row and NOTATION entry 86. al_constants, tab15_1, we15_4, fig15_3, limit15_4a rerun. fig:15-film caption now states its 10 % definition (ratio to the limit ≤ 1.1). |

Ledger addendum: the 0 K sound-speed convention (0 K C_ij with ρ = 2.73 g cm⁻³) should go to state/CORRECTIONS §19.13(g) together with the
owed 6.4/C-18 refit.

Post-check rebuild (-outdir=/tmp/claude-0/build-ch15rev): 0 LaTeX errors, 0 undefined citations, no undefined reference from Ch15/D.39/D.40/E.20.
