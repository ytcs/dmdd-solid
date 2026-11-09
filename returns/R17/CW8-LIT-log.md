# R17 / CW8-LIT log: literature, novelty and data closures

Agent CW8-LIT, brief briefs/R17/CW8-LIT.md, 2026-11-01. Nothing committed.

**Files edited**
- New: state/NOVELTY.md, state/DATA-ADDENDA.csv, this log.
- Status cells of LE-10, 11, 135, 158, 161, 162, 163 in state/LOOSE-ENDS.md.
- Source and novelty tags of LIMITS.md rows.

All shared-file edits were small exact-string replacements, made after re-reading the region; CW8-B was editing the same files concurrently. A usage-limit pause
fell between the literature work and the edits. All edits were made after it.

**Method**
- Literature: lit.py (arXiv, fetch, unpaywall) into literature/papers-CW8-LIT/; text by pdftotext; page = PDF page.
- INSPIRE citation walks: `refersto:recid:<n>`. The `refersto:arxiv:` form is not parsed and returns the whole database, so it was not used.
- Data: COD REST and CIF.
- Every arXiv ID was checked against the arXiv API (§D).

## A. Edits (file → section → source)

| File | Section / row | Edit | Source |
|---|---|---|---|
| state/NOVELTY.md | whole (new) | priority register N1–N18 + settled items | §C searches; FT reads §B3 |
| state/DATA-ADDENDA.csv | whole (new), v4 columns | Al C_ij (0 K), Al a; Ir C_ij (0 K); YIG a, ρ_T | 2109.13551 Table 2 p.5; 2401.12894 Table 2 p.13; COD 2101364 (+1008628, 1521848) |
| state/LOOSE-ENDS.md | LE-10 status (col. 1, last col.) | CLOSED | DATA-ADDENDA |
| state/LOOSE-ENDS.md | LE-11 status | CLOSED (IF-U7) | COD 2101364 |
| state/LOOSE-ENDS.md | LE-135 status | CLOSED, NONE FOUND | NOVELTY N11 |
| state/LOOSE-ENDS.md | LE-158 status | CLOSED, PRIOR ART | 1911.03482 Eq. (10) p.8 (earliest), 2205.02250 Eq. (30); 1910.10716 Eq. (35); 1807.10291 Eqs. (21)–(22) |
| state/LOOSE-ENDS.md | LE-161 status | CLOSED (register) | NOVELTY |
| state/LOOSE-ENDS.md | LE-162 status | CLOSED | §B1 |
| state/LOOSE-ENDS.md | LE-163 status | CLOSED (closed-access residuals kept [UNVERIFIED]) | §B2 |
| LIMITS.md | WP7 "Numbers carried", TLS bullet ("DM–TLS priority/novelty UNRESOLVED") | ✎R17: NONE FOUND | NOVELTY N11 |
| LIMITS.md | WP7 "Numbers carried", isotope B−L bullet ("Novelty UNRESOLVED") | ✎R17: NONE FOUND | NOVELTY N8 |
| LIMITS.md | LB1-3 source of the demon | Pines 1956 bibliography + statement [FT via 2007.06670] | 2007.06670 p.2, Ref. [1] p.8 |
| LIMITS.md | L-H3 source cell | 2106.12586 [ABS] → [FT] Eq. (18), (19)–(22); ∇↔² identity stated; 𝒯_e normalisation flagged [E] (not re-checked against NOTATION) | 2106.12586 pp.8–9 |
| LIMITS.md | L-D11 source cell | Bethe [UNVERIFIED] → PDG Eq. (34.5) [FT] | PDG RPP 2024 ch. 34 PDF p.4 |
| LIMITS.md | L-D11′ source cell | "[FT, CW3's reading]" → verified, formula quoted, NR reduction stated | same |
| LIMITS.md | L31 (Braun–Kivshar) | textbook-standard with edition | 1806.11002 Ref. [3] p.7 |
| LIMITS.md | L33 (Hecht) | bibliography + equation chain [FT] via later papers; original closed | 1712.03369 Ref. [9] p.24; 1701.03459 §2 pp.1–2 |
| LIMITS.md | L-O2 source cell | 2009.13534 re-read [FT]; 1203.3542 𝒪₂ [FT] | 2009.13534 pp.10, 13; 1203.3542 pp.8, 14 |

Interpretation: the two "Numbers carried" edits change novelty status words, not source tags. They were made because LE-135 and LE-161 require the priority result to be recorded where the UNRESOLVED flag sits.

Not edited:
- LB1-10 (Allen): already "closed access; no equation numbers" (CW4 CANNOT-CLOSE). Unpaywall gives no OA copy.
- B2-L6 (Larmor): already [FT] via Oshikawa–Affleck (CW4).
- Haldane: no LIMITS row cites it by name. The v_J = v_F statement sits in WP7-B1-v2 §3(a), which is a return and is not edited.
- The WP0/WP2/WP3/WP6 sources of §B1 appear only in returns (LIMITS rows L3–L19 of the R1 table list them as context, without a tag). Their verification lives here only.

## B. Source verification (LE-162, LE-163, L-D11′)

### B1. LE-162 (quotes in WP0-v3 §14, WP2-v3 §13, WP3-v3 §15, WP6-v3 §10 / A-G)
| Source (version read) | Return claim | Located in FT | Verdict |
|---|---|---|---|
| 1203.3542 v3 | 𝒪₁, 𝒪₃…𝒪₁₅ at most linear in S_N, v^⊥; 𝒪₂ = (v^⊥)² quadratic (WP0 §2) | Eqs. (18)–(23) p.8 ("O1 = 1, O2 = (v⊥)²"); p.14: elimination of the v_N^⊥·v_N^⊥ term within O2 | CONFIRMED |
| 2009.13534 v2 | Eq. (13) v_χ, v_ψ; Table III operator list; Eq. (15); Eq. (27) composite L_ψ, L_ψ⊗S_ψ; Eq. (38) magnon rate | Eq. (12) q ≡ k′ − k = p − p′ and Eq. (13) p.10 (v^⊥ ≡ v_χ − v_ψ, v_χ = v − q/2m_χ); Table III p.13; Eq. (15) p.14; Eq. (27) p.16; Eq. (38) p.21 | CONFIRMED at (13), Table III, (15), (27), (38); (16)–(26) are the intermediate steps between the located endpoints (15) and (27) and were not checked one by one. The sign convention of q equals the campaign's |
| 2105.02233 v2 | L3: velocity overlap Eq. (11); rate Σ_l Re(R_l*W_l) Eqs. (36)–(42) | Eq. (11) p.4; Eqs. (36)–(42) p.6 (W_l, B₁…B₅) | CONFIRMED. The source is IP only: "screen" does not occur in the text. The screening layer of L3 is the campaign's (WP1) |
| 2106.12586 v1 | Table I; Eq. (18) LO/NLO operators; Eqs. (20)–(22) mixing and rate | Table I p.4; Eq. (18) p.8; Eqs. (19)–(22) pp.8–9 | CONFIRMED. Transcription note: the pseudoscalar NLO term is (ig/4m_e²)(∂_tφ)ψ†Σ·∇↔ψ (factor i; WP0 §2 omits it, harmless for \|·\|²). The source uses ρ_φ = 0.4 GeV/cm³ in (22) |
| 1910.08092 v3 | Eqs. (94), (98)–(104), f_e term | Eq. (94) p.27; Eqs. (98)–(104) p.31; f_e(Z_j1 − Z*_j) term in (104) | CONFIRMED |
| 1911.03482 v2 | Eqs. (2), (8), (12), (13), (16), (17), (44); real eigenvectors below (14) | (2) p.6 (1/N Σ A_J…); (8) p.8; (12)–(14) p.9; text p.10 "eigenvectors are real … do not interfere"; (16)–(17) p.10; (44) p.20 (q⁴a²A₁A₂/(32ω_LOm_p(A₁+A₂))) | CONFIRMED |
| 2506.11191 v1 | Eqs. (68)–(72); footnote 6 | Eqs. (68)–(72) p.12; fn. 6 p.12: "we defined the C_{ℓ,d} without the 1/V normalization" | CONFIRMED |
| 2011.09477 v1 | Eq. (10) Poisson law | Eq. (10) p.3 | CONFIRMED |
| hep-ph/0608035 v2 | Eqs. (5), (7)–(9) | (5) p.2 (dR/dE = ρσ\|F\|²/(2mμ²)∫_{v>q/2μ}f/v d³v); (7)–(8) F_mass = F_charge; (9) Helm, p.2 | CONFIRMED |
| 2607.06005 v1 | Eqs. (6), (10); soft-limit Migdal ℓ = 0, 2 | (6) p.3; (10) p.4; ℓ = 0, 2 only: p.9 | CONFIRMED |
| 2412.18330 v1 | anharmonic NR corrections (L18) | Morse matrix elements Eqs. (7)–(10) p.4, λ_M = 0.02; validity Eq. (22) p.12; follows 2309.10839 | [ABS] → [FT] |
| 2105.00599 v3 | §2 two-sided PLR + PCL at −1σ; §3.1 fixed SHM; Eq. (11) | two-sided PLR recommended p.5; PCL at −1σ p.7; "recommended not to profile … fixed" p.11 and summary p.16; Table 2 p.11 (0.3, 544, (11.1, 12.2, 7.3), (0, 238, 0), 29.8); v_⊕(t) Eq. (11) p.10 | CONFIRMED (closes WP6-v3 A-G (6.1)) |
| 2011.12896 v3 | v_esc = 528⁺²⁴₋₂₅, v₀ = 233 ± 6 (WP6-D6) | p.7, p.13 | CONFIRMED (closes A-G (D6)) |
| Klein–Martinez–Seiler–Wang | Hunziker distortions (WP0 A-V15c alternative) | Crossref: CMP 143, 607–639 (1992), doi:10.1007/BF02099269; Unpaywall: closed | bibliography verified; content [UNVERIFIED], closed access |
| Cohen–Bergstresser | GaAs form factors ≈ 0.3 (WP3 §M4) | PR 141, 789 (1966); Unpaywall: closed | [UNVERIFIED], closed access |
| Si/Ge elastic constants (WP3 §15) | standard values for [E] locations | Si: 2109.13551 Table 2 p.5, C11 167.5, C12 65.0, C44 80.1 GPa at 77 K (McSkimin 1953) [FT secondary]; Ge not found open | Si CONFIRMED (secondary); Ge stays [E]-use |

### B2. LE-163 (classic citations) and L-D11′
| Citation | Route | Located | Verdict |
|---|---|---|---|
| Bethe (L-D11, L-D11′) | PDG RPP 2024 (Navas et al., PRD 110, 030001), ch. 34 "Passage of particles through matter", rev. Aug. 2023 (pdg.lbl.gov PDF, document date 25 Mar 2025) | Eq. (34.5) PDF p.4; validity 0.1 ≲ βγ ≲ 1000; §34.2.4 mean excitation energy | [FT, verified]. PDG supplies the Bethe form and I only |
| Hecht 1932 (L33) | 1712.03369 Ref. [9] p.24 (full title, Z. Phys. 77(3), 235–245); 1701.03459 §2 Eqs. (1)–(4) pp.1–2 (Ref. 3 = "K. Hecht, Z. Physik, 77 (1932) 235", p.5) | Eq. (4) is an image in the PDF | bibliography [FT]; equation chain [FT]; original closed |
| Pines 1956 (LB1-3) | 2007.06670 v2 p.2 (demon: neutral, out-of-phase bands, ω ∝ q, vanishing at q → 0), Ref. [1] p.8 = Can. J. Phys. 34, 1379 (1956) | — | [FT via later paper] |
| Haldane 1981 (WP7-B1 §3(a)) | Voit cond-mat/9510014, Eq. (3.34) p.28: v_Nν = v_F + (g₄ν + g₂ν)/π, v_Jν = v_F + (g₄ν − g₂ν)/π, so v_J = v_F iff g₂ = g₄; Ref. [3] p.149 = J. Phys. C 14, 2585 (1981) | — | [FT via review] |
| Braun–Kivshar (L31) | 1806.11002 Ref. [3] p.7: *The Frenkel–Kontorova model* (Springer, 2004) | M_cr not printed in 1806.11002 | textbook-standard, edition given |
| Allen 1971 (LB1-10) | Unpaywall closed | — | CANNOT-CLOSE unchanged (CW4) |
| Larmor / Oshikawa–Affleck (B2-L6) | cond-mat/0108424 v2 = PRB 65, 134410 (2002) (API) | — | [FT] (CW4), unchanged |
| Kanamori–Tachiki 1962 | cond-mat/0108424 Ref. 47 p.53 = J. Phys. Soc. Jpn. 17, 1384 (1962). Cited p.51 for the first term −⟨[A, S⁻]⟩/(2⟨S^z⟩) of the ESR shift, not for the Larmor theorem itself | — | bibliography [FT]; WP7-B2-v2 §5 should cite it for the shift term only |
| Zhang–Niu | 1308.6036 v3 = PRL 112, 085503 (2014): J^ph = Σ u × u̇ Eq. (1) p.1. 1502.02573 = PRL 115, 115502 (2015): quantised phonon pseudo-angular momentum; its conservation gives selection rules (abstract, p.1) | — | [FT] |
| Taraskin et al. (C^{IR}) | cond-mat/0604205 v1 (DOI 10.1103/PhysRevLett.97.055504) Eq. (1) p.1: C(ω) ≃ A + Bω² | — | [ABS] → [FT] |
| Taraskin–Elliott (IR coupling) | cond-mat/0604205 Ref. [8] p.5 = PRB 61, 12017 (2000); also Refs. [18], [25] | — | bibliography [FT]; content not read |
| Galeener–Sen | not in cond-mat/0604205's references (that cites Galeener–Leadbetter–Stringfellow, PRB 27, 1052 (1983)) | — | [UNVERIFIED], closed access |
| Ambegaokar–Conway–Baym 1965 (one–two-phonon interference) | no open copy found (book chapter) | — | [UNVERIFIED], textbook-standard |
| Andreev–Lifshitz | flagged by CW5 | — | unchanged |

### B3. Full texts read for the novelty register (LE-158, NOVELTY)
| Source | Located |
|---|---|
| 2205.02250 v2 | Eq. (27) p.7 (acoustic eigenvector √A_d/√ΣA); Eq. (30) p.8 (S_{n=1,LA}), credited there to its Ref. [25] = 1911.03482 (with Erratum PRD 102, 019904(E)) |
| 1911.03482 v2 | Eq. (10) p.8: S^{(1−ph,LA)} ≈ (Σ_dA_d)q²/(2m_pω_LA,q)δ(ω − ω_LA,q), the earliest source of (2.3a′) found |
| 1910.10716 v3 | Eq. (35) p.9 (light-mediator scaling ∝ 1/ω_min) |
| 1807.10291 v1 | Eqs. (21)–(22) p.17, rate Eq. (24) p.18 |
| 2609.06423 v1 | p.1: Lindhard agreement for ω ≳ 5Δ; no analytic Δ/(qv_F) term |

## C. Searches (NOVELTY)
- Battery scripts and raw JSON: scratchpad battery.py, spec*.json, battery{,2,3,4}.json (session-local; the queries and counts are copied verbatim into state/NOVELTY.md).
- INSPIRE walks (recid resolved from the arXiv number), with citing-record counts:

| Anchor | Citing records |
|---|---|
| 2011.09496 | 119 |
| 2205.03395 | 30 |
| 1607.01789 | 191 |
| 2106.12586 | 59 |
| 1512.04533 | 233 |
| 2101.08263 | 121 |
| 1708.08929 | 246 |
| 1910.02091 | 121 |
| 1403.4606 | 78 |
| 1703.09168 | 32 |
| 1608.01994 | 220 |
| 2302.08085 | not indexed in INSPIRE (`arxiv:2302.08085` → 0); the earlier SSL errors were the recid lookup. Walks 1512.04533, 2101.08263, 1708.08929, 1910.02091 rescreened for `phonon\|assisted\|indirect` for N5: none relevant |

- Candidates read at abstract level (arXiv API): 2210.04128, 2408.04021, 2606.30123, 2508.17810, 2606.14845, 2011.13352, 2006.13909, 2109.04473, 2105.08101, 2209.10902, 1708.08929, 2210.09313, 2405.00112, 1707.07019, 2603.22390, 2409.05988.

## D. arXiv IDs verified against the API (title as returned; version read)
| ID | Title | Version |
|---|---|---|
| 1203.3542 | The Effective Field Theory of Dark Matter Direct Detection | v3 |
| 2009.13534 | Effective Field Theory of Dark Matter Direct Detection With Collective Excitations | v2 |
| 2105.02233 | Crystal responses to general dark matter-electron interactions | v2 |
| 2106.12586 | Dark Matter Absorption via Electronic Excitations | v1 |
| 1910.08092 | Multi-Channel Direct Detection of Light Dark Matter: Theoretical Framework | v3 |
| 1911.03482 | Multiphonon excitations from dark matter scattering in crystals | v2 |
| 2506.11191 | Spin-Dependent Scattering of Sub-GeV Dark Matter: Models and Constraints | v1 |
| 2011.09477 | Dark Matter Detection With Bound Nuclear Targets: The Poisson Phonon Tail | v1 |
| hep-ph/0608035 | Model Independent Form Factors for Spin Independent Neutralino-Nucleon Scattering from Elastic Electron Scattering Data | v2 |
| 2607.06005 | Anisotropic electron scattering and Migdal effect in semiconductor detectors | v1 |
| 2412.18330 | Halo-dependent Anharmonic Effects in Collective Excitation for Light Dark Matter Direct Detection | v1 |
| 2105.00599 | Recommended conventions for reporting results from direct dark matter searches | v3 |
| 2011.12896 | Halo uncertainties in electron recoil events at direct detection experiments | v3 |
| 2205.02250 | Dark matter direct detection from the single phonon to the nuclear recoil regime | v2 |
| 1807.10291 | Directional Detection of Light Dark Matter with Polar Materials | v1 |
| 1910.10716 | Multi-Channel Direct Detection of Light Dark Matter: Target Comparison | v3 |
| cond-mat/0108424 | Electron Spin Resonance in S=1/2 antiferromagnetic chains | v2 |
| 1308.6036 | Angular Momentum of Phonons and Einstein-de Haas Effect | v3 |
| 1502.02573 | Valley contrasting chiral phonons in monolayer hexagonal lattices | v1 |
| cond-mat/0604205 | Universal Features of Terahertz Absorption in Disordered Materials | v1 |
| cond-mat/9510014 | One-Dimensional Fermi liquids | v1 |
| 2401.12894 | Ab initio thermodynamic properties of Iridium: A high-pressure and high-temperature study | v1 |
| 2109.13551 | Quasi-harmonic temperature dependent elastic constants: applications to silicon, aluminum, and silver | v1 |
| 2007.06670 | Observation of Pines' Demon in Sr$_2$RuO$_4$ | v2 |
| 1806.11002 | Structure and dynamics of crowdion defects in bcc metals | v1 |
| 1701.03459 | Electron Lifetime Determination in Semiconductor Gamma Detector Arrayes | v1 |
| 1712.03369 | Properties of GaAs:Cr-based Timepix detectors | v1 |
| 2609.06423 | A Mean-Field Approach to the Dielectric Response of Bulk Superconductors for Light Dark Matter Direct Detection | v1 |
| 1608.08567 | Charge collection efficiency mapping of interdigitated 4H-SiC detectors | v1 (no Hecht citation; not used) |

One ID was guessed and rejected: 1309.3839 (the API returned a mathematics paper). The correct Zhang–Niu IDs, 1308.6036 and 1502.02573, were found by API title search.

## E. Data notes (LE-10, LE-11)
- Al:
  - The JARVIS C₄₄ = 16.2 GPa in table v4 is a factor 1.95 below the measured 31.6 GPa.
  - Every v4 Al quantity that uses G_V or C₄₄ (c_T_iso, c_TA, θ_D_E, Y_mod) inherits this. This is not a ±40% effect.
  - Owner WP8-U should switch Al to C_ij_exp_0K.
- Ir: the DB values are 3–9% low.
- YIG: the v4 a_exp (12.56 Å, tagged [FT] 1905.13744 p.4) is the paper's approximate value, not a measurement. The measured 12.375 Å gives 𝓃_spin × 1.045 and ρ_T 5.173 g/cm³.
- Table v4 was not edited.

## F. Cleanup
PDFs in literature/papers-CW8-LIT/ deleted at the end; the HTML and JSON side files of lit.py fetch were deleted with them.
