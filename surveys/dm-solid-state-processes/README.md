# Dark matter in solid-state targets: the complete process space, its weight in exclusion plots, and the theory gaps (Oct 2026)

This is a synthesis. The detail lives in two companion catalogs:
- `catalog-processes.md`: about 95 channels arranged as a coupling × excitation matrix, with the mass regime,
  threshold, formalism and codes, status and experiments for each, and about 230 verified arXiv IDs.
- `catalog-analysis-and-gaps.md`: the analysis chain with published effect sizes, the low-energy excess,
  a table of which theory each current experiment uses, and 13 ranked gaps (about 100 verified IDs; about
  27 papers read in full text).

Both catalogs were compiled with `skills/breakthrough-maths/scripts/lit.py`, about 180 arXiv queries in
total, plus INSPIRE citation walks. Every arXiv ID was checked against the arXiv API. Claims carry tags:
[FT] full text, [ABS] abstract only, [EST] estimate. "Not found" means not found by these searches; it is
not an exhaustive audit. The companion survey `../dm-solid-state-scattering.md` covers the ER/NR lineage.

---

## 1. How to organise the space

A DM–solid interaction is fixed by three choices. The catalog is arranged along all three.

1. **Coupling** (7 classes): electron density (SI); nucleon (SI); dark photon (total charge density);
   electron spin or g_aee; nuclear spin or g_aNN; g_aγγ (needs an applied field); scalar coupling to e or N.
2. **Kinematic mode**: scattering (energy deposit ≤ ½m_χv², with v ≲ 800 km/s, so 1 eV needs about 0.3 MeV
   and 1 meV about 0.3 keV); absorption (deposit ≈ m_DM, with q ≈ 10⁻³ω); inelastic or exothermic (the DM
   brings its own Δ).
3. **Final state, and the order at which the target produces it.** This axis is usually left implicit, and
   it is where most gaps sit:
   - **First order: one elementary quantum.** An electron–hole pair (valence or core), an exciton, a plasmon,
     a single phonon (acoustic, optical, polar LO), a magnon, a phonon polariton, broken Cooper pairs, a Dirac
     quasiparticle, or an ionized dopant.
   - **Second order: composite final states.**
     - DM–nucleus × electron–phonon or non-adiabatic coupling → electron–hole pair: the crystal Migdal effect,
       including its phonon-mediated version.
     - DM–electron × electron–phonon → electron–hole pair plus phonon: **phonon-assisted electron recoil, not
       computed**.
     - Absorption × electron–phonon: phonon-assisted absorption. It is modelled for metals and
       superconductors and data-driven only for Si/Ge.
     - DM–nucleus × photon emission: NR bremsstrahlung, computed for atoms only.
     - Plasmon-mediated or exciton-mediated electron recoil.
   - **All orders: multiphonon and cascades.** The multiphonon structure factor from a single phonon up to free
     NR; anharmonicity; the hot-carrier cascade that turns a deposit ω into Q electron–hole pairs (the
     ionization yield); defect creation and annealing; scintillation.
   - **Readout transduction.** Athermal phonons, quasiparticles in TES/KID/SNSPD sensors, qubits, colour
     centres. These convert the deposit into a signal and carry their own modelling.

**Coverage matrix** (catalog-processes §1). The column dominated by first-principles (FP) results is
electron-density coupling into electron–hole pairs and single phonons. The spin columns (e-spin, nuclear
spin) are first-principles only for magnons and single phonons. The **"second order" row is almost empty at
first-principles level**: the crystal Migdal effect is the only composite channel with a mature treatment.

## 2. Status by family (one line each; detail in catalog-processes)

| Family | Mature (FP, public code) | Modelled only | Not computed |
|---|---|---|---|
| Electron–hole pairs (E1–E3) | QEdark, QCDark/QCDark2 (all-electron, RPA+LFE), EXCEED-DM, DarkELF; NR-EFT operators | ionization yield (R&K phenomenology) | finite-T / zero-point response; phonon-assisted |
| Excitons (E4–E6) | BSE: one study (Si/Ge/GaAs/NaI) | Frenkel (organics, molecular QC) | dark/indirect excitons, exciton–phonon replicas |
| Plasmons (E7–E9) | in the ELF (screening pole) | exotic low-energy plasmons, heterostructures | — (bulk plasmons kinematically hard for halo DM) |
| Low-dimensional / Dirac / SOC (E10–E12) | SOC-gapped materials (DFT), graphene | most Dirac/Weyl targets | — |
| Superconductors (E13, A2) | — | Lindhard/BCS, deformation-potential absorption | ab initio film ELF; pair-breaking efficiency |
| Dopants, colour centres (E14–E15, D2) | — | hydrogenic dopants | first-principles dopant/NV final states |
| Single phonons, polaritons (L1–L2, A4–A5) | PhonoDark (EFT + DFPT); absorption EFT | — | — |
| Multiphonon → NR (L3–L8) | DarkELF (harmonic, incoherent) | anharmonic, coherence (1D model) | a unified multiphonon + Migdal + defect partition |
| Magnons / spin (S1–S9) | magnons (Holstein–Primakoff on DFT) | nuclear-spin channels, axion quasiparticles | two-magnon continua; chiral/CD observables |
| Defects, tracks (D1–D5) | — | MD, SRIM | DFT-level defect creation by ER |
| Migdal / bremsstrahlung (X1–X11) | atoms; crystal ELF + phonon-final-state EFT | phonon-mediated Migdal | crystal NR bremsstrahlung; no semiconductor measurement |
| Absorption (A1–A12) | single phonons, magnetized media | data-driven σ₁(ω); devices | EPW-level phonon-assisted absorption |
| Inelastic / exothermic (I1–I5) | — | atoms, Migdal | exothermic DM into phonons and magnons |

## 3. Why it matters for exclusion plots

The published curve is a chain: halo → crystal response × mediator × screening → energy partition → quanta →
detector response → statistics. The catalog-analysis-and-gaps §1.1 table collects the published size of each
theory input. The important structural point is that **theory dominates at the edges of the plot, not in the
middle**:

1. **ER at the lightest masses (m_χ ≲ 3 MeV in Si/Ge).**
   - Only ω within a few eV of the gap contributes, at q near its kinematic minimum, and only the 1–2 e⁻ bins.
   - QCDark/EXCEED-DM disagree by about 2× at 1 MeV (DAMIC-M 2503.14617 [FT]).
   - Screening is largest here, ×2 at the 2e⁻ threshold (2101.08275 [FT]).
   - Ionization models differ by about 50% (2004.10709 [FT]).
   - The **clamped-lattice T = 0 band edge sets the kinematic cutoff itself**. Every production code makes that
     approximation (2603.12326 [FT]).
2. **Heavy-mediator ER above ~10 MeV.** High-q and all-electron physics: core states give about 10× for Ge
   (2105.05253 [FT]); QEdark/DarkELF q-cutoffs make the curves turn over. CDEX's whole limit sits in this
   regime.
3. **NR calorimetry at 40–150 MeV** (TESSERACT 44 MeV, CRESST, CPD). Thresholds of 0.4–10 eV are at or below
   the displacement threshold, yet free NR with unit heat quenching is assumed (2007.14289, 2503.03683 [FT]).
   The low-energy excess dominates the counts here.
4. **Migdal curves at 30–100 MeV.** Atomic, ELF and EFT models differ by up to 10×, and experiments mix them:
   SuperCDMS and EDELWEISS use atomic Migdal, SENSEI and DAMIC-M the semiconductor EFT.
5. **Sub-MeV targets** (SNSPD, superconductors, Dirac). Model Drude/Lindhard dielectrics set the edge;
   branch-cut choices alone move Al rates by up to 10⁷ (2101.08263 [FT]).
6. **Conventions are not shared.**
   - SENSEI's main limits still use unscreened QEdark; DAMIC-M uses QCDark with MTF screening; CDEX uses
     EXCEED-DM.
   - v_esc is 544 or 600 km/s, and ρ_χ is 0.3 or 0.4 GeV/cm³.
   - **No published exclusion curve carries a theory band**, and SENSEI says explicitly that the code spread
     "should not be taken as an uncertainty".
   - The combined code × ionization × halo spread is about 2–3× at 1 MeV [EST].
7. **The low-energy excess** is now attributed to stress relaxation, defect annealing and radiative
   secondaries. No DM interpretation survives; the plasmon channel is dead as an explanation but alive as a
   signal. Because no excess model predicts a spectrum with an uncertainty, nothing is subtracted, and
   low-mass NR limits are set by the excess plus the signal shape at a few eV.

## 4. Gaps and deficiencies, ranked by impact on exclusion plots

Merged from the two catalogs and from the PAER campaign. The rank is effect size × the parameter space it
moves × the absence of existing work.

| # | Gap | Plots moved | Size | What would fix it |
|---|---|---|---|---|
| 1 | **Near-gap ionization yield** P(Q\|ω,q,T): R&K is phenomenological with a tuned non-physical parameter; Ge has only a step function | every Si/Ge ER limit below ~5 MeV | ~50%–×2 | an ab initio hot-carrier cascade (GW bands + EPW e–ph rates + impact-ionization matrix elements) seeded by the DM vertex's (ω,q), not a photon's; tabulated with errors |
| 2 | **Frozen lattice / T = 0 / phonon-assisted band edge** | ER at 0.3–3 MeV, the 1e⁻ bin, DAMIC-M modulation (0.53–2 MeV) | ×2 already at 1 MeV between codes; a Si window m_χ ≈ 0.34–0.47 MeV that is phonon-assisted only | phonon-assisted second-order response (the PAER campaign derives it) plus finite-T special-displacement averaging plugged into QCDark2 / EXCEED-DM; publish R(T)/R(0) per Q bin |
| 3 | **NR energy partition at eV thresholds** (heat / defects / electrons; free NR assumed below ~10 eV) | NR at 40–150 MeV, CEvNS fog | O(1) near E_d | joint MD + multiphonon response per (E_R, direction); stop setting heat quenching to 1 |
| 4 | **No theory error bands; mixed conventions** | every combined plot and relic-benchmark exclusion | ×2–3 at 1 MeV [EST] | a shared, versioned response library with nuisance parameters (functional, q_max, LFE, yield model, F, E_g(T)) propagated by profile likelihood |
| 5 | **Screening and many-body effects beyond analytic RPA**: LFE is now done (QCDark2), but there is no finite-q BSE for Si/Ge and production limits use unscreened or MTF screening | all ER | 20–50% (LFE); ×1.4–2.5 (screening at all) | RPA+LFE as the default; finite-q BSE near the gap; validation against NIXS/EELS |
| 6 | **Inconsistent Migdal**, Migdal versus multiphonon double counting, Migdal inside measured quenching | Migdal at 30–100 MeV | ×2–×10 | one non-adiabatic Born–Oppenheimer framework giving S(q, ω_ph, ω_e) jointly, with sum rules; a neutron-calibration measurement |
| 7 | **Core / all-electron / relativistic** effects (Ge 3d misplaced by 4.5 eV by the XC functional; Dirac core states absent in crystals) | heavy-mediator ER, CDEX | up to ×10 (Ge) | all-electron codes in all limits; GW/hybrid 3d; scalar-relativistic + SOC |
| 8 | **Halo dependence at the kinematic edge** (exponential in v_esc + v_E) | lowest masses | 50%–×10 | halo-independent bounds alongside SHM; standardise v_esc |
| 9 | **Superconductor / thin-film dielectrics** (Drude, Lindhard; branch cuts) | everything below 1 MeV | O(1) to orders of magnitude | measured or ab initio film ELF with BCS coherence; pair-breaking efficiency from α²F |
| 10 | **In-medium non-density operators**, intermediate mediators | model interpretations | unknown per operator | publish density / spin / current response tables; consistent screening of every operator |
| 11 | **Excitons beyond one BSE paper**: dark, indirect and phonon-replica excitons | near-gap ER, scintillator projections | <10% in Si/Ge except within ~0.1 eV of the gap [EST]; large in NaI | BSE + exciton–phonon (finite q) |
| 12 | **Unmodelled channels**: crystal NR bremsstrahlung; exothermic DM into phonons/magnons; two-magnon continua; DFT-level defect creation by ER; first-principles dopant/NV final states; EPW-level phonon-assisted absorption | projections and new channels | — | each is a self-contained calculation with existing tools (EPW, phonopy, BSE codes) |
| 13 | **Anisotropy and modulation** (rates angle-averaged); **anharmonicity** | modulation analyses; NR below 10 MeV at large σ | few % (averaged); ≤10² (narrow) | q-resolved anisotropic tables; anharmonic S(q,ω) |

### A pattern across the gaps (coordinator synthesis)
Gaps 1, 2, 3, 6 and 11 share one root cause. **Production theory treats electrons and lattice separately,
each at first order, at T = 0**, while the threshold region of every plot is where electron–phonon coupling is
not optional:
- the cascade (gap 1) is electron–phonon scattering;
- the band edge (gap 2) is zero-point and electron–phonon renormalised;
- NR at eV energies (gap 3) is multiphonon plus defects;
- Migdal (gap 6) is non-adiabatic electron–phonon coupling;
- exciton replicas (gap 11) are exciton–phonon coupling.

One linear-response framework for the coupled electron–ion system, the density response at O(g²) and beyond
evaluated with EPW-class tools, would address all five consistently and carry its own sum rules. The PAER
campaign (`campaign/paer` on branch `claude/breakthrough-maths-campaign-paer`) builds its first piece: the
O(g²) phonon-assisted density response, derived by two independent routes that agree term by term.

## 5. Notable facts surfaced by this survey
- **SPLENDOR** (2507.17782) assumes phonon-assisted transitions are suppressed at mK. Phonon *emission*
  (factor n+1) survives at T = 0, so that assumption needs revisiting (campaign/paer literature L1).
- **EXCEED-DM's energy-only bound** for Si is m_min = 0.28 MeV (its eq. 33). Data-driven ELFs (Hochberg et
  al.; DarkELF) carry zero weight between E_g and E_dir at small q, and no halo-DM Si reach is shown below
  0.5 MeV (L1).
- **Kahn & Lin's review** (2108.03239 §VI) names the "2→3 electron + phonon" response near the gap without a
  formula. It is the only literature mention of the phonon-assisted electron-recoil process found.
