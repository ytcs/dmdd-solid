# Chapter 8 revision (2026-11-02)

Files: tex/ch08/ch08.tex, s8-1 … s8-8 (Summary at the end of s8-8), tex/appD/D-24 … D-28. Outside these, exact small edits only:
tex/appC/C-20.tex and tex/appE/E-22.tex (𝒥(ω) → J_s(ω), ruling 8), NOTATION.md (𝓜^k unit; J_s row), tex/bib/book.bib (one entry,
dent2015general, arXiv 1505.03117 checked against the API), figscripts/ch08 (we8_pairs.py, we8_4.py, we8_sectors.py, fig8_3.py) and
tex/figures/ch08/fig8_3.pdf (regenerated: E_e, E_h in the pair box). No QE.
Compute: we8_pairs.py rerun with a Gaussian pair kernel (σ = 0.10 eV and 0.05 eV; Lorentzian η = 0.10 eV kept for the i0⁺ of the
bubble), Si NK = 20 and 24, GaAs NK = 20; outputs cached as figscripts/ch08/we8_pairs_<MAT>_NK<n>_gauss<σ>_eta0.1.json (+ run_*.log).
we8_4.py (PySCF ROHF, contact density) rerun; outputs cached as we8_4_out.json, we8_4_density.npz (radial densities), we8_4.log.
we8_sectors.py rerun at S_HR = 2 and 0; logs we8_sectors_SHR2.log, we8_sectors_SHR0.log.
Build and lint: see the end of this file.
Format: item → fix → location. "Declined" gives the reason.

## Editor rulings (brief)
| # | Item | Fix | Location |
|---|---|---|---|
| 1 | we:8-pairs photon seed (E_e + E_h = 8.73 ≠ 9.18 eV) | Cause: Lorentzian pair kernel (0.10 eV) × optical 1/Δ² weight pulls in low-energy vertical pairs. Pair delta functions now Gaussian (σ = 0.10 eV), the bubble's i0⁺ stays a 0.10 eV Lorentzian; every seed now has ⟨E_e + E_h⟩ = 9.18 eV = ω − E_g to 0.01 eV. Converged in NK (20/24) and σ (0.10/0.05). New values (NK = 24, σ = 0.10; NK 20 and σ 0.05 within 3 %): S^IP 1.7e8, S 4.9e7 eV² (×0.29), |ε⁻¹₀₀|² 0.33, other elements ≤ 0.05, further 12 % (was 13 %; 8.8 WE 8.10 updated); DM kick 4.8 / 4.4 eV, electron > half 64 % (was 63), lopsided 45 % (44), lowest valence band 4 % (5), the others about a third; IP fractions within three points (checked: max 2.8); photon 5.7 / 3.5 eV (was 5.4 / 3.3), 85 % (83); transverse current 5.3 / 3.8 eV (5.4 / 3.9), lopsided ~50 %; GaAs in/out 15 % (0.156), mean energies differ ≤ 0.02 eV (was 0.01). | s8-7 WE 8.9 (setup, Screening, Which pairs, Other seeds, In/out), closing ¶ of §8.7-pairs, §8.7-handoff "momentum transfer stays inside", Summary ¶ 8.7; we8_pairs.py docstring (old Lorentzian record kept, marked superseded) |
| 1 | "a volt" comparison | The comparison survives at reduced size: hole difference DM − photon 0.93 eV (NK 24, σ 0.10), 0.95 (NK 20), 0.88 (σ 0.05) → "about 0.9 eV"; "a volt below" → "about 0.9 eV below"; closing ¶ "by about 0.9 eV in the mean energy of the hole. That is close to the gap, …"; hand-off "the hole carries about 0.9 eV more"; Summary "a photon … gives 5.7 eV and 3.5 eV, with about 0.9 eV less in the hole". | s8-7 (as above); s8-8 Summary |
| 1 | cache outputs | we8_pairs_*.json (a few kB each) and logs; we8_4_out.json + we8_4_density.npz (127 kB) + we8_4.log | figscripts/ch08 |
| 2 | 8.7 symmetry condition | PT paragraph: "needs a kernel that is real symmetric, f_GG′ = f_G′G = f*_GG′, as RPA and ALDA are; a merely Hermitian kernel does not suffice"; "with the origin at an inversion center n_e(q+G) is invariant"; symmetry of R depends on the origin, pair weights do not. Factorization keyresult keeps "Hermitian kernel" (correct there) | s8-7 §pairs, ¶ "The two labelings agree" |
| 3 | Fano coefficients | ν runs over every decay channel (phonon branches and others, e.g. impact ionization), Γ^tot = Σ_νΓ^(ν), Υ_m over all channels; "the deviations c̄^F − c^F_ν … average to zero with the weights Γ^(ν), because ν runs over all channels … the coefficients themselves need not" | s8-6 Fano ¶; D-28 §resonant amplitude (weights sum to one; all-channels clause; phonon-only normalization by Γ^tot would fail) |
| 3 | velocity ratio | "at equal kinetic energy" | s8-6 §three sectors ¶2 |
| 3 | remainder of eq:8.6-decomp | δS_ab with \|δS_ab\|/S^bin = O(κ^{2(n+1)} α²m_e/Δω_bin); 1 meV bins: factor 2.7×10⁴, useful from n = 2 (2×10⁻³) | s8-6 keyresult + ¶ after |
| 3 | Dirac width | "By dimensional analysis the quasiparticle width is ω times a function of α̃ …"; sentence split in three; α̃ glossed (\cref{sec:7.3}) | s8-6 superconductor/semimetal ¶ |
| 3 | 8 % toy mismatch (4.72 vs 4.35 µeV) | Explained and checked: same origin as the 12 % in P_Mig, the displaced excited surface; with g_d = 0 the exact values are 3.52×10⁻⁶ and 4.34 µeV, within 0.3 % of the leading formulas | s8-6 WE 8.7 "The kick"; we8_sectors.py docstring (S_HR env var) |
| 4 | GaAs ionic term | −0.9×10⁻³ | s8-4 §lines, third consequence |
| 4 | theorem ω ≠ 0; LA phonon | keyresult: "in a crystal, a target whose long-wavelength longitudinal acoustic phonon moves it locally as a whole"; "at every q and every ω ≠ 0"; table "clamped nuclei, ω ≠ 0"; D.27 statement likewise (Bragg terms at ω = 0) | s8-4 keyresult, tab:8-screening; D-27 §exactness |
| 4 | WE 8.6 "same weight" | "its f-sum weight ∫ω S_NN/2π is unchanged; the area of the peak … falls by ω_T/ω_L = 0.925"; ¶ Nucleon number "same f-sum weight"; Summary "f-sum weight unchanged" | s8-4 WE 8.6, §couplings; s8-8 Summary |
| 4 | Π_em, "improper" | Π_em defined at first use (l.54, → §8.4-mixing); "photon version of the improper response" → "comes from the photon-reducible part of the response"; later definition shortened | s8-4 §rows, §mixing |
| 4 | one pointer, not four | 8.1 l.109 → bare \cref; 8.2 l.57 cut; 8.2 l.116 cut; s8-3 l.205 kept | s8-1, s8-2 |
| 4 | ε_e | kept as the electron-channel dielectric function (8.4, A.7 unchanged); 8.7's carrier energies renamed E_e, E_h (6 uses + Fig. 8.3); NOTATION row 599 (6.5, ε_e, ε_h) is not used in any 6.5/D.18 tex: proposed for the merge to follow | s8-7, fig8_3.py/pdf; SEAMS 8.7 |
| 5 | interference sign | "The positive part sits in the phonon final states, on the acoustic branch (energies that vanish with q) and on the optical phonons wherever the electrons move with the nuclei (\cref{sec:8.6}). Every electronic final state carries −(m_e/M_κ)\|⟨f\|n_e\|0⟩\|² at small q (eq:8.3-boostward)." | s8-3 §third, spring ¶ |
| 5 | O(q/G) imaginary | 8.3: real part corrected at (q/G)² at every cubic site; the first-order term at T_d sites is purely imaginary (odd part of a real density), enters Im 𝓜³ alone. D.26: n_{−G} = n_G*, odd part i Im n_G | s8-3 three-regimes ¶; D-26 §mixed moment |
| 5 | Campbell-Deem wording | "in a crystal with a coupling proportional to mass: the single optical phonon, the two-phonon final states and the anharmonic channel … ∝ q⁴" | s8-3 soft-limit ¶ |
| 5 | D.26 COM order | q⁸ → q⁶, with ω = q²/2(m_e + M_κ) | D-26 §third moments |
| 6 | O₇ | "No standard model produces 𝒪₇ at leading order (\cref{sec:8.1}); we take it as the simplest spin coupling that survives the trace." | s8-2 WE 8.3 |
| 6 | n_B step size | One rule in 8.5: each power of 𝐝 enters as 𝐯_N·𝐝/ΔE; lattice at rest: step n_B → n_B+2 = 1 + O((ω_ph/ΔE)²), 3×10⁻³ in Si (κ³ is the same ratio in atomic counting); kicked nucleus: the sudden probability; κ⁴ = m_e/M is a sum-rule share, not a step. tab:8-params entry now gives (ω_opt/E_g)² = 3×10⁻³ per step | s8-5 n_B ¶, tab:8-params |
| 6 | rung of DFPT inputs | "Inputs from DFPT, the phonons, Born charges and ε∞, … carry the rung TDDFT at ω = 0"; base-point ¶ and WE 8.8 say so | s8-5 𝒳 ¶, base point ¶, WE 8.8 |
| 6 | 𝔗 forward uses | 8.2: label glossed in words at first use ("the list of orders that a calculation keeps …, \cref{sec:8.5}"), n_T as "an expansion in the phonon occupations"; 8.3: 𝔗 sentence removed, n_B glossed; 8.4: "n_g = 2" → "second order in the vertex g" | s8-2, s8-3, s8-4 |
| 7 | spin-½ completeness | "complete for dark matter of spin ½ …; for spin 1 … two more operators … [Eq. (18)]{dent2015general}; for spin 0 only the operators free of 𝐒_χ remain. The target side does not change" | s8-1 ¶2 |
| 7 | ²⁹Si abundance, J (J = ½ cited to the ²⁹Si level spectrum of Klos Fig. 5) | "J_nuc = ½ [Fig. 5]{klos2013large} and an abundance of 4.685 % in natural silicon [meija2016isotopic]"; "in natural silicon one nucleus in 21 carries the spin" | s8-1 §nuclei |
| 7 | Coulomb-energy row | removed (no user in tex/ or the plan; SPINE l.1180 lists it only as 8.1's own item); SEAMS 8.1 withdraws its rows | s8-1 §absorption |
| 8 | 𝓜^k unit | NOTATION l.681 eV^{k+1} → eV^{k+3} (text already eV^{k+3}) | NOTATION.md |
| 8 | \varGamma | all rates in ch08/appD use \varGamma (grep: no upright \Gamma rate); row proposed | SEAMS 8.3 |
| 8 | 𝒬_{n,m} | → 𝒫^qp_{n,m} (s8-6, s8-7); D.28's 𝒬_A → 𝒫_A | s8-6, s8-7, D-28 |
| 8 | S⁰ clash | eq:8.7-IP keeps S⁰ (a zero-phonon sector use); the IP total in WE 8.9 is now S^IP | s8-7 WE 8.9 |
| 8 | 𝒜 clash | 8.6/D.28 off-shell amplitude → 𝒜^off_f, 𝒜^off_ν (D.25's 𝒜_fi unchanged) | s8-6, D-28 |
| 8 | g clash | we:8-sectors levels g, e → \|lo⟩, \|up⟩ (σ_z defined) | s8-6 WE 8.7 |
| 8 | 𝖫 | kept in 8.8: C.14 already uses 𝖫 for the likelihood; the clash is with 4.9's pair propagator, proposed for renaming at the merge (SEAMS 8.8) | — |
| 8 | 𝒥 vs C.20 | C.20/E.22 bath spectral density 𝒥(ω) → J_s(ω) (and 𝒥₃ → J_{s,3}); NOTATION rows l.835, l.839 updated; spin current keeps 𝒥^{αβ}_s (𝒮 is taken by the transition sum) | C-20, E-22, NOTATION |
| 8 | SEAMS rows | appended "Revision after the Chapter 8 review" blocks to SEAMS 8.1–8.8 | ledgers/SEAMS |
| 9 | knapen2021dark | "[Eqs. (6) and (13)]" | s8-6 tab:8-sectors |
| 9 | kahn2022searches | "[Sect. IV A, Eqs. (90)–(92)]" | s8-5 lattice regimes |
| 9 | Ramanathan | "fitted to the ionization yields of photon absorption" | s8-7 §handoff |
| 9 | pinpoints | hochberg2021determining → "[p. 2, discussion of Eq. (1)]" (checked in sources/review-ch08/2101.08263). puff1965application: **declined** — the paper is not open access (lit.py: 404 for html and pdf; no copy in sources/), so no equation number can be read from the text; the citation attributes the single-species third-moment rule as a whole work, like fano1961effects | s8-4 §exact |
| 10 | chapter opening ¶2 | rewritten as argument: one structure (model → tensor, target → one matrix), what follows from it (settle exactness, screening, truncation once), one closing "we will" sentence ending at Chap. 18; "three regions" and "every slow coupling" gone | ch08.tex |
| 10 | repetitions | 8.4 pointers (above); dark-photon reduction in 8.1 cut to a pointer; fermionic-absorption sentence kept in 8.2 only; interference bound in 8.2 → pointer; sector recap in 8.7 opener cut; "final state decides the sector" kept once (cut from the tab:8-sectors caption); "holds at every point of 𝔗" cut in 8.2 and 8.3; 8.3 "They share a structure" ¶ cut to one sentence | s8-1, s8-2, s8-3, s8-6, s8-7 |
| 10 | 8.6 cuts | opener "This section turns the bookkeeping into a theorem" + sector list → one sentence; code-chain ¶ → one sentence (\crefrange{app:E.4}{app:E.8}); Fano ¶ and ambiguity ¶ split (the second Fano ¶ opens "In many crystals the Fano term vanishes."); "We call" removed | s8-6 |
| 10 | Fig. 8.3 caption | production note removed | s8-7 |
| 10 | Tab. 8.6 cited before it appears | cited in the partition ¶ ("\cref{tab:8-sectors} below lists what each sector holds") | s8-6 |
| 10 | percent style | \SI{…}{\percent} chapter-wide (s8-5, s8-6, s8-7, s8-8); "percentage points" and "a percent" kept as words | ch08 |
| 10 | "a volt" → eV | every "a volt" replaced by "about 0.9 eV" (the recomputed value); "a factor 0.29" → "a factor of 0.29" | s8-7, Summary |
| 10 | "We call" | s8-6 "The range of 𝒫_ad is the electron-following sector"; s8-7 "…, seeding, is made precise in \cref{sec:18.3}" | s8-6, s8-7 |
| 10 | wording slips | "v_F" → "the valence electrons of silicon, taken as a free gas at their density, move at v_F"; magnons "gapless" → gaps set by anisotropy, below most phonon energies; "k is not a good label" → "its bare momentum k is not conserved; only its crystal momentum is" | s8-1, s8-6 |
| 10 | register | "however" +4 (s8-1, s8-3, s8-6 ×1 each, s8-4 kept); "only" −13 (s8-1 ×6, s8-6 ×7); "of order" → "about", "O(q²)", "relative size" where it was not a scaling statement (s8-1, s8-3) | ch08 |

## Derivation report, part 1
| # | Item | Fix | Location |
|---|---|---|---|
| 1 | GaAs ionic term | −0.9×10⁻³ | s8-4 |
| 2 | COM order | q⁶ | D-26 |
| 3 | "same weight" | f-sum weight; zeroth moment × ω_T/ω_L | s8-4 |
| 4 | ω ≠ 0 | keyresult, table, D.27 | s8-4, D-27 |
| 5 | LA-phonon hypothesis | stated in keyresult and D.27 | s8-4, D-27 |
| 6 | O(q/G) imaginary | as ruling 5 | s8-3, D-26 |
| 7 | Campbell-Deem | as ruling 5 | s8-3 |
| known | 𝓜^k unit; 𝒥 clash; NOTATION rows | ruling 8; rows in SEAMS 8.1/8.3/8.4 | NOTATION, SEAMS |
| known | Coulomb row | removed | s8-1 |
| WE 8.4 | 0.427 at 100 keV | rerun gives 0.42645 → 0.426 | s8-3 WE 8.4 |
| note | relativistic +8 % unsourced | kept as an estimate here (the reviewer's point-Dirac estimate is 1.077); 8.3 now says it grows roughly as (Zα)²; the source belongs to 12.5 | s8-3 |
| 8.7 | "real symmetric kernel" | ruling 2 | s8-7 |

## Derivation report, part 2
| Item | Fix | Location |
|---|---|---|
| velocity ratio at equal momentum (WRONG) | "at equal kinetic energy" | s8-6 |
| eq:8.6-decomp dimensions (GAP) | ruling 3 | s8-6 |
| d₀ⱼ = −dⱼ₀ for real states only (optional) | Ψ′₀ = d*_{j0}·∇Ψ′_j/(MΔE_j), "using d_{0j} = −d*_{j0}, the anti-Hermiticity …; the conjugate of Ψ′₀ in the overlap carries d_{j0}" | D-28 §kick |
| Fano sum (WRONG) | ruling 3 | s8-6, D-28 |
| knapen2021dark Eq. (6) | Eqs. (6) and (13) | s8-6 |
| WE 8-pairs not cached; "within three points", "a third each" not in record | cached JSON; both claims now checked in the cached record (IP–RET fractions differ by ≤ 0.028; bands 2–4 0.30–0.35 each) | figscripts/ch08; s8-7 |
| WE 8-pairs photon seed (WRONG/GAP) | ruling 1 | s8-7, s8-8 |
| Ramanathan "computed" | "fitted" | s8-7 |
| PT kernel real, origin | ruling 2 | s8-7 |
| geodesic PSD for every real ϑ (GAP) | PSD for ϑ ≥ 0; negative ϑ needs supp S⁺ = supp S; new support → eq:8.8-open | s8-8 |
| "too large by 6.1 %" | "the correct one-phonon rate is lower by 6.1 % than one that sets e^{−2W} = 1" | s8-8 |
| O(k³) loose | O(k⁶) (sympy: 1 + k²t/4 + k⁶t³/192) | s8-8 eq:8.8-cost |
| δ_X < 0 at 4 eV | "≤ 0" | s8-8 WE 8.10 |
| kahn2022searches | Eqs. (90)–(92) | s8-5 |
| NOTATION drift | 𝒬 renamed; new-symbol rows and the δ_w location in SEAMS 8.6 | s8-6, s8-7, D-28; SEAMS |

## Prose report
| Location | Item | Fix |
|---|---|---|
| ch08 ¶2 | section list | ruling 10 |
| Summary l.137 | vague theorem clause | "an electron-density coupling does so only at a static lattice" |
| Summary l.139 | four of seven values | all seven given (0.047 at 10 keV, 7×10⁻⁶, 1.9 / 0.05) |
| Summary l.145 | tilt without number | "from −0.44 to +0.25 across momentum and energy" |
| redundancy (5 items) | | ruling 10 |
| seams 8.6→8.7 | recap | 8.7 opener: "The cascade needs more than the sector of \cref{sec:8.6} in which a final state lies." |
| forward 𝔗, n_T, n_B, n_g | | ruling 6 |
| "We call" ×2; "transfer" (D-24 l.7) | | removed; "The momentum transfer" |
| "exactly" tic | cut in s8-4 l.54 and s8-6 l.29 | |
| overlong sentences | s8-6 Dirac split; s8-3 l.78 rewritten in Lin's form; s8-2 l.83 shortened; s8-7 l.74 split; new sentences of this revision split (ch08 ×2, s8-3, s8-5, s8-7, s8-8) | |
| numbers | \SI percent; "a factor of 0.29"; "a volt" | ruling 10 |
| pinpoints | Puff declined, Hochberg added | ruling 9 |
| float | tab:8-sectors cited before | ruling 10 |
| Fig. 8.3 caption | | ruling 10 |
| 8.1 l.3 | "In this section we build…" | "We will build the list, reduce … and add …" (8.2 pointer cut) |
| 8.1 calibration (b) | category frame | "In a solid the electron moves too." + "The rows also overlap, in the longitudinal direction." |
| 8.1 l.15 | q/m in the table | "\cref{tab:8-operators}, which writes q/m_e in place of q, so that each operator is dimensionless" |
| 8.1 l.20 | "Also, …" | "Refs. … define q as the momentum the dark matter gains, the opposite of the q of this book, so …" |
| 8.1 l.109 | "A practical calculation" | "In practice a calculation …" |
| 8.1 l.124 | abundance; "moreover" | ruling 7; "moreover" dropped |
| 8.2 l.30 | "sits at every point" | "No truncation of the target changes the master formula; it changes only S_ab." |
| 8.2 l.55 | 280-word ¶ | split at "The average needs …" |
| 8.2 l.65 | Lin rewrite | "Exothermic dark matter does something different: it does not reweight the band, it moves it." |
| 8.3 l.3 | count-teaser | "… needs three more: an interference bound, higher moments and a Ward identity." |
| 8.3 l.85 | "by more in heavier atoms" | "grows roughly as (Zα)² in heavier atoms" |
| 8.3 l.180 | restatement | cut to one sentence |
| 8.4 l.69 | 400-word ¶ | split at "The signs are fixed …"; opener "The converse takes two limits in which electrons and nuclei come apart." |
| 8.4 l.159 | "One may" | "We can" |
| 8.4 l.163 | triad of label jargon | "what a calculation keeps of it is a truncation that \cref{sec:8.5} labels" |
| 8.5 titles | triad | "Small parameters", "Lattice regimes" |
| 8.5 l.81 | n_B vs n_B(ω) typography sentence | **declined**: no ruling renames either symbol; the sentence stays until the merge decides (SEAMS 8.5 of the writer already flags it) |
| 8.5 l.112 | Lin rewrite | "Each rung moves ε∞ by about as much as the last, and not always in the same direction, so there is nothing to expand in."; "a few percent" → "within the accuracy of the bands" (the 4.9 statement) |
| 8.6 l.5, l.24, l.183, l.197, l.174, budget | | ruling 3/10 |
| 8.7 l.9, l.12, l.92, l.133, l.139 | | ruling 4/10; "The first is the identification …" |
| 8.7 l.83 fragment | | "Every seed shares the same 9.2 eV, and yet the three hand the cascade three different starting distributions." |
| 8.8 l.127 overclaim | | "The uncertainty of a rate then rests on computed steps wherever they exist, and it names its omissions where they do not." |
| 8.8 l.20 | Lin rewrite | "A nuisance must not vary from bin to bin. A truncation is a property of the calculation, not of the bin, …" |
| D-24 l.3, l.7, l.12 | | "Four steps take it there: …"; "The momentum transfer"; "(used only in this section)" |
| D-28 | \subsection* | numbered \subsection, as D.24–D.27 |
| D-28 l.3 opener | five verbs | **declined**: the reviewer marks it acceptable for an appendix |

## Reader (a)
| Item | Fix | Location |
|---|---|---|
| L1 (80/20 by rows) | shares of velocities, not rows; longitudinal parts cancel only in the sum | s8-1 WE 8.2 |
| L2 (positive interference) | ruling 5 | s8-3 |
| L3 (n_B step) | ruling 6 | s8-5 |
| L4 (Fano) | ruling 3 | s8-6, D-28 |
| L5 (photon seed) | ruling 1 | s8-7 |
| L6 (real symmetric f) | ruling 2 | s8-7 |
| GaAs −0.92×10⁻³ | −0.9×10⁻³ | s8-4 |
| D.27 case 2 "second phonon line" | "This case does not describe a pair with a phonon in the final state: its phonon line is virtual and screens the dark-matter vertex …" | D-27 §lines |
| UBD κ_BO-suppressed Migdal, eq:8.6-fsum-e in 8.4 | glossed in words at use ("the Migdal amplitudes, by which a moving nucleus excites the electrons"; "a fraction Z_κm_e/M_κ of its f-sum") | s8-4 §exact |
| Schrieffer–Wolff unglossed | **declined**: the sentence already defines it in place ("a transformation that removes H_ep to a given order") | — |
| gapless-target subsection beyond persona | **declined**: content needed by 14, 15, 20.4; D.28 carries the proof | — |

## Reader (b) and (c)
| Item | Fix | Location |
|---|---|---|
| spin-½ completeness | ruling 7 | s8-1 |
| 4A⟨B⟩ split | as reader (a) L1 | s8-1 |
| O₇ bound loose | "the second for spin flips into the empty minority band, which an exchange splitting above E_F↑ + ω closes; the bound is generous" | s8-2 WE 8.3 |
| pair lines too fast | one sentence on what they do: they screen the final pair at q + Q, not at q | s8-4 §lines |
| 4.72 vs 4.35 µeV | ruling 3 | s8-6 |
| photon seeds | ruling 1 | s8-7 |
| 𝒳 for DFPT | ruling 6 | s8-5 |
| notation S⁰, 𝒜, g | ruling 8 | s8-6, s8-7 |
| forward refs 8.3–8.4 | ruling 6; 8.4 impulse regime glossed in words | s8-3, s8-4 |
| "final state decides" ×3; "every point of 𝔗" ×3 | ruling 10 | s8-2, s8-3, s8-6 |
| (c) k label, v_F, gapless magnons | ruling 10 | s8-1, s8-6 |
| eq:8.6-ambiguity unmotivated in main text | **declined**: the three conventions are named in the ¶ before the equation; D.28 derives each term |  |

## Editor notes
| Note | Status |
|---|---|
| 8.1 c_i normalization, sign flips | verified by both derivation reviewers; unchanged |
| 8.1 𝒥 clash | resolved (C.20 → J_s) |
| 8.1 ²⁹Si, J, Coulomb row | ruling 7 |
| 8.6 δM_κ deferred compute | already DC-24 in state/DEFERRED-COMPUTE.md (l.1242 note too) |
| 8.6 griffin2018 Eqs. (19)–(23) | verified by derivation-2 |
| 8.2 SPINE outcome (iii) | not a ch08 file; the text already says exothermic DM shifts the region to positive ω and only a warm target gives ω < 0 |
| 8.4 ρ_c | drop at merge (SEAMS 8.4) |
| 8.4 E.14 bold P | App E pass-2, not this revision |
| 8.4 appD counter lines | none left in D-26/D-27 (grep "setcounter" in D-24…D-28: none) |
| 8.7 PT claim | verified algebraically (derivation-1) and by toy (derivation-2); hypotheses completed (ruling 2) |
| 8.7 ε̃⁻¹ row, P_casc | ε̃⁻¹ row proposed in SEAMS 8.7; P_casc first use 8.7 |
| 8.3 \varGamma, 𝓜^k, new symbols | ruling 8; rows in SEAMS 8.3 |
| 8.8 𝖫 | ruling 8 |

## Not touched
- The q-sign convention, c_i normalization, the master formula and every derivation the reviewers marked CHECKED.
- Fig. 8.1 (no renamed symbol). Fig. 8.3 regenerated only for E_e, E_h.

## Build
/tmp/build-ch08rev, full main.tex with latexmk -f: 1 LaTeX error, not from these files: a missing figure of a chapter
being written by another agent (first build: figures/ch11/fig11_1.pdf; final build: figures/ch10/limit10_4a.pdf); 0 undefined citations in the whole book. Undefined references from ch08, D.24–D.28,
C.20 and E.22, all to unwritten targets: app:D.36, app:D.47, chap:12–16, chap:18–22, sec:9.4, sec:10.4–10.7, sec:10.9, sec:11.3–11.7,
sec:12.1–12.5, sec:13.4, sec:13.6, sec:13.7, sec:14.4, sec:14.6, sec:16.2, sec:16.7, sec:16.8, sec:17.4, sec:18.1–18.3, sec:19.1,
sec:19.5, sec:19.6, sec:20.4, sec:21.2, sec:21.4–21.6. Lint (lint.py --banned): 0 blocking in all sixteen edited tex files; the
remaining hits are EQ-PUNCT false positives inside gathered/aligned and LONG-SENT merges of keyresults, tables and displays.
