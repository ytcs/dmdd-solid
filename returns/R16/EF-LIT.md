# EF-LIT — published ε_eh / F_eh for Al₂O₃, CaWO₄, LiF, NaF (targeted search, R16)

## Result table

| # | Material | Quantity | Value | T | Method | Source, location | Tag |
|---|---|---|---|---|---|---|---|
| 1 | Al₂O₃ (sapphire, single crystal) | ε_eh ("energy to create an eh pair") | **27 eV**, no uncertainty | not stated (room T implied) | **Assumed/tabulated.** Table cites vendor web pages only ([4] CRYSTAL GmbH, [5] Molecular Technology GmbH). No measurement. | Karacheban et al., JINST 10 (2015) P08008, arXiv:1504.04023, Table 1, p. 3 | [FT] |
| 2 | Al₂O₃ (sapphire) | ε_eh ("mean energy to create an eh pair") and MIP yield | **27 eV**; "MIP eh created 22 eh/µm" (derived from the 27 eV, not independent) | 20 °C for the resistivity/mobility rows | **Copied** from row 1 (text cites the same work as [3]) | LUXE TDR, arXiv:2308.00515, Table 9.1, printed p. 299 (PDF p. 315); used again on p. 309 | [FT] |
| 3 | CaWO₄ | Conversion efficiency B = N_eh/N_max with N_max = E/(2.35E_g); gives **ε_eh = 2.35E_g/B ≈ 29.8 eV** (inferred, not printed) | B = 0.41, E_g = 5.2 eV | B given once, for both the 295 K and 9 K rows | **Semi-empirical** Robbins–Lempicki model, Eqs. (5), (8), (9). B is computed from ħω_LO = 108 meV, ε∞ = 3.5, ε₀ = 10.4. Only S (transfer) is fitted to the measured light yield; B is not. | Mikhailik & Kraus, Phys. Status Solidi B 247, 1583 (2010), arXiv:1001.5461, Table 2, preprint pp. 28–29 (PDF p. 28); Eq. (5) p. 26 | [FT] (the 29.8 eV is our arithmetic) |
| 4 | CaWO₄ | E_g only, no ε_eh | "E_gap ≈ 5.0 eV" | — | Model of STE scintillation; no pair count stated | Roth et al. (CRESST), arXiv:1501.04617, p. 1 | [FT] |
| 5 | LiF | ε_eh | **none found** | — | — | — | — |
| 6 | NaF | ε_eh | **none found** | — | — | — | — |
| 7 | Al₂O₃, CaWO₄, LiF, NaF | F_eh (Fano factor) | **none found** in any source, measured or computed | — | — | — | — |
| 8 | LiF (near miss) | Threshold for a primary e–h pair plus a secondary exciton, not ε_eh | "28–33 eV photons"; E_g ≅ 14.5 eV | low T | VUV excitation spectroscopy (Tartu group) | Seen only in a search snippet (typeset.io, "low temperature excitonic electron hole and interstitial…"). Not opened. | [UNVERIFIED] |

**Bottom line.** For the four materials, no measured ε_eh, no first-principles or full-band Monte Carlo ε_eh, and no Fano factor of any kind
were found in the places searched. There are only two numbers:
- Sapphire, 27 eV. This is a vendor-datasheet value that HEP detector papers repeat. Its primary origin was not traced.
- CaWO₄, ≈ 29.8 eV. This is a semi-empirical Robbins/Lempicki estimate that can be recovered from B = 0.41 in Mikhailik–Kraus 2010.

Neither has an uncertainty. Neither uses the ab initio definition used here: the CaWO₄ figure counts thermalised pairs available to
luminescence, with phonon losses folded into B.

## Details and exact quotes

**[1] Karacheban et al. 2015 (arXiv:1504.04023) [FT].**
- Table 1 (p. 3), "Relevant material properties of single crystal artificial sapphire and diamond [4], [5]", has the row:
  "energy to create an eh pair, eV  27  13" (sapphire, diamond). The same table gives "bandgap, eV 9.9 5.47".
- Text: "The band gap of sapphire is larger than for diamond, resulting in a by a factor of two larger energy needed to create an
  electron-hole pair."
- Refs [4], [5] are company web pages (crystal-gmbh.com; mt-berlin.com/.../sapphire.htm). Nothing in the paper measures ε_eh.
  The measured CCE (≈10% at 950 V) is interpreted with the 27 eV value.
- Implied ratio: ε/E_g = 2.73.

**[2] LUXE TDR (arXiv:2308.00515) [FT].**
- Table 9.1, printed p. 299, has: "mean energy to create an eh pair [eV]  27  13  3.6" (sapphire, diamond, silicon) and
  "MIP eh created [eh/µm]  22  36  73".
- Text: "Signals collected from sapphire detectors are limited by a relatively small amount of 22 electron–hole (eh) pairs produced per
  micron of MIP track…" The text cites [3] = Karacheban et al.
- The DESY instrumentation-seminar slides "Sapphire Detectors" quote the same 22 eh/µm (search snippet only, [UNVERIFIED]).

**[3] Mikhailik & Kraus 2010 (arXiv:1001.5461) [FT].**
- Eq. (5), p. 26: "N_e−h = N_max B = Eγ/(2.35E_g) · B". The 2.35E_g factor is attributed to "Robins [84]" (Monte Carlo, phosphors).
- Eq. (8): B = 1/(1+0.65K).
- Eq. (9): K = 0.244×10⁴ (1/ε∞ − 1/ε₀)[ħω_LO]^{3/2}/(1.5E_g).
- Table 2 CaWO₄ row: "CaWO4 295 5.2 108 3.5 10.4 0.41 2.9 0.76 0.61 15.8 4.6"; second row "9 … 1 0.85 28.7* 8.3".
  - The trailing digits printed in pdftotext (5.2⁵⁷, 108⁹⁶, 10.4⁹⁶, 15.8⁹⁸) are reference superscripts.
  - The columns are T, E_g, ħω_LO, ε∞, ε₀, B, E_λ, Q, S, LY (ph/keV), η (%).
- Recheck of K from Eq. (9): K = 2.1, so B = 0.42, matching the printed 0.41.
- Implied ε_eh = 2.35 × 5.2 / 0.41 = **29.8 eV**, so ε/E_g ≈ 5.7.
- This sits far above the campaign's model prediction (10.7 eV) and above the 2.3–3 E_g rules. The reason is that B folds in
  optical-phonon losses for a polar, low-ε∞ lattice. Treat it as a model value, not data.
- The same table gives ε = 2.35E_g/B for CdWO₄ (4.2/0.43 → 23 eV) and CaMoO₄ (4.0/0.37 → 25 eV), same caveat.

## Searched but no value found (exact scope)

- **Sapphire detectors, LHC/ILC beam monitors** (INSPIRE "t sapphire and t detector", web).
  - Only rows 1–2. The 27 eV goes back to vendor data in every sapphire HEP paper seen.
  - arXiv:2203.15903 (low-threshold sapphire, phonon readout) and arXiv:2212.04342 (MINER sapphire, per search summary) give no e–h value.
  - A G4CMP-for-sapphire slide deck lists ε_eh, E_g and F as needed inputs without values ([UNVERIFIED], Google Slides snippet).
- **RIC/EBIC/XIC in Al₂O₃, LiF, NaF.** Candidates exist, but no open full text was available:
  - Klaffky, Rose, Goland & Dienes, PRB 21, 3610 (1980), "Radiation-induced conductivity of Al₂O₃: Experiment and theory".
    It may contain an assumed pair-generation energy. Not OA, no abstract in Crossref. [UNVERIFIED]
  - "Gamma photoconductivity of Al2O3", Can. J. Phys. (1968), doi:10.1139/p68-022. Publisher page returns 403. The search summary of the
    abstract mentions trap filling and no pair energy. [UNVERIFIED]
  - Klein, J. Appl. Phys. 39, 2029 (1968), doi:10.1063/1.1656484, not OA. Its table is reproduced in 2610.16949 Fig. 1. That fetched
    full text contains no Al₂O₃, LiF, NaF or CaWO₄ (grep [FT]).
  - OSTI search for Al₂O₃ RIC returned nothing relevant.
  - Devanathan et al. NIMB 141 (1998), "Cryogenic radiation response of sapphire", is about defects only (OSTI abstract) [ABS].
- **Alkali-halide secondary emission / photoemission yields.**
  - Henke, Liesegang & Smith, PRB 19, 3004 (1979) measured nine alkali halides. The abstract does not name LiF and no per-electron
    energy appears in it. The DTIC copy (ADA083962) returned an HTML block page. [ABS/UNVERIFIED]
  - Akkerman–Boutboul–Breskin group, all [ABS], none computes ε_eh or F for our materials:
    - J. Appl. Phys. 76, 4656 (1994): sub-10 eV transport in CsI, NaCl, KCl.
    - J. Appl. Phys. 79, 6714 (1996): IMFP and stopping power for LiF, NaCl, KCl, CsI.
    - pss(b) 198, 769 (1996): IMFP for KF…KI, BeO, MgO, SiO₂, Al₂O₃.
- **Scintillator-efficiency models (CaWO₄ and others).**
  - Row 3 found.
  - Not OA and not checked, [UNVERIFIED]; these may list β or B for CaWO₄ and possibly LiF/NaF:
    - Lempicki, Wojtowicz & Berman, NIM A 333, 304 (1993), doi:10.1016/0168-9002(93)91170-R.
    - Robbins, J. Electrochem. Soc. 127, 2694 (1980).
    - Bartram & Lempicki, J. Lumin. 68, 225 (1996), doi:10.1016/0022-2313(96)00026-9.
  - CRESST papers (0910.4414, 0912.3689, 2505.01183) give light fractions (≲7% of the energy goes into light) but no ε_eh.
- **Monte Carlo W/F in halides.**
  - PNNL-23817 (OSTI 1164970) [FT]: W and F only for NaI and CsI (e.g. F_CsI → 0.28).
  - TREKIS/XCASCADE (Medvedev, Rymzhanov, Volkov; Lipp et al.) model cascades in Al₂O₃ and LiF but report no mean pair energy in the
    abstracts and full text checked. arXiv:2607.01016 [FT]: no per-pair value.
- **Citation walk for the first-principles papers** (OpenAlex `cites:`):
  - 2610.16949 [FT] covers Si, SiC, AlN, SiO₂ and others; 2311.05011 [FT] covers diamond and β-Ga₂O₃; 2308.03893 [FT] covers GaN.
    None of the three mentions sapphire, Al₂O₃, CaWO₄, LiF or NaF (grep).
  - The 8 + 14 citing works are about GaN, HEMTs, hot carriers and reviews.
  - One open item: Yakimov, "Measurement of electron–hole pair creation energy in wide bandgap semiconductors", Radiat. Phys. Chem.
    (2026), doi:10.1016/j.radphyschem.2026.113594. No abstract was available. Its materials are unknown, probably GaN, Ga₂O₃ and
    diamond, as in the author's earlier EBIC work. [UNVERIFIED]

## Notes

- Process: lit.py's HTTP user agent and its Unpaywall call contain a hard-coded personal mailto address. It was used for the first
  `works`/`fetch` calls before this was noticed. After that, all requests used curl with a neutral UA and no email.
- All downloaded PDFs and text dumps in literature/papers-EF-LIT/ were deleted at the end.
