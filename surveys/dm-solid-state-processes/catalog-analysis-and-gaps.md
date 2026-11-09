# CATALOG-B: How theory enters DM–solid-state exclusion plots, and where it is the limiting systematic

Round R1b, brief CAT-B. Compiled 2026-10-31. Every arXiv ID below was checked against the arXiv API (export.arxiv.org `id_list`); the verification
list is at the end. Tags: **[FT]** = statement checked in the full text (fetched with `lit.py fetch`); **[ABS]** = from the arXiv abstract only;
**[EST]** = my own estimate, flagged as such. Background on the theory lineage (codes, Migdal, phonons, phonon-assisted ER) is in
`surveys/dm-solid-state-scattering.md` and is not repeated here.

---

## 1. The analysis chain and the size of each theory input

Chain: halo f(v) → DM–target rate dR/dω dq (crystal response × mediator form factor × screening) → energy partition (electrons vs lattice vs
defects) → quanta (e⁻h⁺ pairs Q, athermal phonons, quasiparticles) → detector response (charge transfer, trapping, impact ionization, NTL gain,
phonon collection, dark counts) → statistics (Poisson per Q-bin, optimum interval, profile likelihood).

### 1.1 Summary table: published effect sizes on limits

| Theory input | Effect on limit / rate | Where on the plot | Source |
|---|---|---|---|
| Code choice for Si ER (QCDark vs EXCEED-DM), as used by DAMIC-M | ratio of limits ≈ 1.1 for m_χ > 3 MeV, falling to ≈ 0.5 at m_χ = 1 MeV | lightest masses | DAMIC-M 2503.14617 End Matter [FT] |
| QEdark (orig., no screening) vs QCDark/EXCEED-DM/DarkELF on SENSEI@SNOLAB data | QEdark over-predicts at low ω for light mediator; under-predicts for heavy mediator at Q ≥ 3 (no all-electron); SENSEI calls the most accurate limits QCDark and EXCEED-DM | whole curve; heavy-mediator high-mass end | SENSEI 2312.13342 SM Fig. 6 [FT] |
| QEdark plane-wave cutoff | sharp turnover of reach at ~10 MeV (loss function vanishes above q = 6 αm_e) | heavy mediator, m_χ ≳ 10 MeV | 2603.12326 §IV.4 [FT] |
| DarkELF q-cutoff (6 αm_e) vs QCDark2 (25 αm_e) | curves diverge above ~10 MeV for heavy mediator; agree for light mediator | heavy mediator | 2603.12326 [FT] |
| All-electron/core states, Ge heavy mediator | ≈ 1 order of magnitude at Q ≥ 1; larger at Q ≥ 10 (3d states dominate) | Ge, m_χ ≳ 30 MeV | 2105.05253 §4.1 [FT] |
| High-q modes, Si heavy mediator | ~75 % rate increase in 10e⁻ bin going q_max 8 → 25 αm_e | high-Q bins | 2306.14944 §III.3.5 [FT] |
| Ge 3d binding energy vs XC functional | PBE/TPSS/SCAN put 3d at ~25 eV vs exp. ~29.5 eV; "significant differences" in 8–11 e⁻ bins | Ge high-Q | 2306.14944 [FT] |
| In-medium screening (Si, Ge; vs unscreened) | total rate ↓ ×1.4 (heavy) / ×2.5 (light) for m_χ ≳ 10 MeV; larger near kinematic threshold; ×2–2.1 at 2e⁻ threshold | light mediator, lowest masses | 2101.08275 [FT] |
| Local-field effects (RPA+LFE vs RPA) | reach ↓ 20–50 % for m_χ > few MeV in Si, Ge, GaAs, SiC, diamond; DSF of Si reduced to 15 % at low ω | whole curve | 2603.12326 [FT] |
| Analytic (MTF) vs RPA screening | MTF slightly over-predicts, Lindhard slightly under-predicts; MTF invalid for boosted DM | — | 2603.12326 [FT] |
| Screening for boosted / solar-reflected DM | Q = 1–2 bins suppressed by ~10² | SRDM curves | 2603.12326 [FT] |
| Superconductor (Al) screening branch choice | acausal vs causal log branch: up to 10⁷ in rate at lowest masses; plasmon width another ≳10× | sub-MeV, Al | 2101.08263 SM [FT] |
| Excitons (BSE vs RPA) | large rate increase at low ω in NaI; minimal for GaAs | near gap | 2507.14345 [ABS] |
| Ionization model, Si (R&K vs step function ε = 3.8 eV) | "significant differences" in 1e⁻ and 2e⁻ bins, similar for Q ≥ 3 | lowest masses (1–2e⁻ dominated) | 2306.14944 Fig. 9 [FT] |
| Ionization model systematics, Si | "systematics on the order of 50 %" in low-count regime; ε_eh and F inadequate near gap; hole-band width matters 12–50 eV | 1–10e⁻ | 2004.10709 [FT] |
| Fano factor | model F ≈ 0.115 below all measurements; 2 % CCE loss inflates measured F to 0.13, 5 % to 0.16 | Q-bin migration | 2004.10709 App. A [FT]; skipper F = 0.119 ± 0.002, ε = 3.749 eV at 5.9 keV, 123 K (2004.11499) [ABS] |
| Ge ionization model | only step-function model exists (no R&K analogue) | Ge 1–3e⁻ | 2306.14944 [FT] |
| NR ionization (Lindhard) in Si | measured efficiency deviates from Lindhard below ~1 keV; modified Lindhard (binding, straggling) fits ~50 eV–3 MeV; plain Sarkis model valid for Si only above ~500 eV | NR in CCDs | 1608.00957, 2209.04503, 2001.06503 [ABS] |
| NR quenching in Ge | 254 eV_nr: QF = 25 ± 3 % vs Lindhard 14 % (2405.10405); other data compatible with Lindhard 0.4–6.3 keV (2202.03754), disputed (2203.00750, 2102.10089) | Ge NR, CEvNS | [ABS] |
| NR intrinsic Fano | F_NR ≈ 24 (Si), 26 ± 8 (Ge) at ~25 keV | NR signal shape | 2206.13639 [ABS] |
| Defect energy loss | 6.08 ± 0.18 % of 103 keV Pb recoil in Ge → E_d ≈ 19.7 eV | eV-scale calorimetry | 1805.09942 [ABS] |
| Heat quenching in phonon calorimeters | assumed = 1 by SuperCDMS-CPD | CPD NR curve | 2007.14289 [FT] |
| Migdal: impulse approx. extrapolated to small q | under-estimates rate by up to ×2 | m_χ ≲ 100 MeV | 2210.06490 [FT] |
| Migdal: semiconductor vs isolated atom | rate "much higher" in semiconductors (smaller gap) | all Migdal curves | 2011.09496 [ABS] |
| Migdal: plasmon/ELF estimates | "may be uncertain within an order of magnitude" | — | 2003.12077 Fig. 3 caption [FT] |
| Halo: SHM parameter uncertainty | up to ~50 % in ER exclusion bounds | all | 2011.12896 [FT] |
| Halo: hydrodynamic-simulation spread (IllustrisTNG MW analogues) | factor O(10–20) even at m_χ ≳ 100 MeV, more for multi-e⁻ thresholds | high-Q thresholds | 2001.09156 [FT] |
| Anharmonicity (NR multiphonon) | up to 10² at m_χ ~ MeV, but only at large σ; negligible > 10 MeV | NR, MeV | 2309.10839 [ABS] |
| Relativistic bound-electron kinematics (atoms) | 30–50 % reduction of phase space / dσ | core levels | 2509.14534 [ABS] |
| Detector response (HVeV CT/II) | trapping 0.713 ± 0.093 %, impact ionization 1.576 ± 0.110 % per carrier at ±140 V | fills inter-peak regions | 1910.02162 [ABS]; model 1912.11549, 2403.01259 |

### 1.2 Crystal response (form factor / ELF / structure factor)
- Four production tools: QEdark (1509.01598; plane waves, pseudopotential), QCDark (2306.14944; Gaussian all-electron basis) and QCDark2
  (2603.12326; + RPA ε with LFE), EXCEED-DM (2210.14917, 2105.05253; PAW + all-electron reconstruction + semi-analytic core), DarkELF (2104.12786;
  GPAW RPA ELF, q ≤ 6 αm_e, Ge 3d frozen in the pseudopotential).
- QCDark and EXCEED-DM "good agreement", showing PAW reconstruction is accurate (2306.14944 [FT]). Main residual systematics named by QCDark:
  basis set, XC functional (even after scissor), q_max [FT]. Scissor correction fixes the gap at the experimental value, so the gap is not a
  free systematic for Si/Ge, but it is for new materials (2306.14944 [FT]).
- k-grid convergence: rate decreases monotonically with denser grids (R_10³ < R_9³ < R_8³); QEdark's 6³+27 grid sits closer to unconverged
  values; Ge more affected (2105.05253 [FT]).
- Every production code: T = 0, clamped nuclei, Kohn–Sham (or scissor-shifted) states, isotropic angular average (2603.12326 [FT];
  survey §1.2).

### 1.3 In-medium screening
- Density-coupled rate ∝ ELF = Im ε/|ε|²; screening factor 1/|ε|² applies to scalar as well as vector mediators (2101.08275 [FT]).
- Experiments now use: SENSEI main limits QEdark *without* screening, "to conform with other experiments", with others in SM (2312.13342
  [FT]); DAMIC-M QCDark + analytic (MTF-type) screening (2503.14617 [FT]); CDEX EXCEED-DM with screening factor (2206.04128 [FT]).
- RPA+LFE is the current best; the analytic MTF used in production limits slightly over-predicts (2603.12326 [FT]).

### 1.4 Ionization model (ε_eh, Fano, R&K, impact ionization)
- Standard step model Q = 1 + ⌊(ω − E_g)/ε⌋, ε = 3.6–3.8 eV (Si), 2.9 eV (Ge) (2105.05253, 2603.12326 [FT]).
- R&K (2004.10709): phenomenological cascade (energy split α, impact ionization vs phonon emission with tuned ratio A, plasmon
  redistribution above ħω_pl, T-dependence only through E_g(T)). Parameter A is "non-physical" and tuned to ε_eh at high energy [FT]. Used by
  SENSEI, DAMIC-M, SuperCDMS-HVeV, QCDark/QCDark2 for Si (2312.13342, 2503.14617, 2509.03608 [FT]). EDELWEISS (Ge) used the ionization model of its Ref. [12]
  with F = 0.15, chosen to allow comparison with the Si phonon-mediated (HVeV) result (2003.01046 [FT]).
- "Si impact-ionization model" in the detector sense (HVeV): charge trapping and impact ionization during NTL drift fill inter-peak regions
  (1910.02162, 1912.11549, 2403.01259); included as nuisance parameters in the 2025 HVeV likelihood (2509.03608 [FT]).

### 1.5 Quenching / Lindhard for NR at low energy
- Lindhard fails below ~1 keV in Si (1608.00957) and its binding-energy extension has a cutoff at 2× binding energy (2001.06503); extended
  model to ~50 eV (2209.04503); molecular-dynamics yields down to single-pair level (2506.03810, 2603.16702) [ABS].
- Ge sub-keV QF disputed (2202.03754 vs 2203.00750, 2102.10089, 2405.10405); a Migdal contribution to measured QF can mimic new physics
  in CEvNS (2104.01811) [ABS].
- For phonon calorimeters (CRESST, CPD, TESSERACT) Lindhard is irrelevant but the *heat* quenching (energy stored in defects) is set to 1
  (2007.14289 [FT]); defect formation removes ~6 % at 103 keV in Ge (1805.09942) and the displacement threshold is strongly anisotropic
  (2210.01557, 2301.06592) [ABS].

### 1.6 Migdal probabilities
- Experiments mix three generations of theory: isolated-atom Ibe et al. (1707.07258) in SuperCDMS (2203.02594) and EDELWEISS (2203.03993);
  semiconductor ELF/EFT (2011.09496, 2210.06490 with DarkELF input) in SENSEI@SNOLAB (2312.13342 [FT]) and DAMIC-M (2503.14617 cites
  2210.06490 [FT]); NR-EFT generalisation 2603.13052 recasts EDELWEISS.
- No experimental confirmation of the Migdal effect with SM probes in semiconductors (2210.04917 [ABS]); gas measurement under way (MIGDAL,
  2207.08284).

### 1.7 Astrophysical inputs
- Conventions: SENSEI/DAMIC-M follow 2105.00599 (v₀ = 238, v_esc = 544 km/s, ρ = 0.3) (2312.13342, 2503.14617 [FT]); HVeV v₀ = 238, v_esc = 544
  (2407.08085 [FT]); CDEX v₀ = 220, v_esc = 544, v_E = 232 (2206.04128 [FT]); QROCODILE ρ = 0.4, v₀ = 230, v_esc = 600, v_E = 240 (2412.16279
  [FT]); CRESST ρ = 0.3 SHM; TESSERACT Lewin–Smith (2503.03683 [FT]). The near-threshold edge depends exponentially on v_esc + v_E, so the
  lowest-mass points of different experiments are not on a common footing [EST].
- Halo-independent methods for ER: few populated bins (light mediator) make the inversion ill-posed (2311.04957 [ABS]).
- Daily modulation from Earth scattering: DAMIC-M 2307.07251, 2511.13962 constrain 0.53–2.7 MeV; these rely on Earth-stopping MC with free
  cross sections, not in-medium responses [ABS]. Modulation amplitude f_mod also changes when all-electron high-q modes are included
  (2306.14944 [FT]).

### 1.8 Detector-response modelling
- Skipper CCDs: spurious charge and single-electron rate set the 1e⁻ bin (2410.18716: 1.39 × 10⁻⁵ e⁻/pix/day; Cherenkov and recombination
  photons explain much of the SENSEI-2020 1e⁻ rate, 2011.13939 [FT]); charge-trap studies 2510.23336, 2605.30281, 2610.22418.
- HVeV: PCB luminescence and Cherenkov (2011.13939 [FT], 2407.08085 [FT]); single-charge resolution, CT/II nuisance (2509.03608).
- Phonon calorimeters: salting / energy-dependent efficiency (2503.03683 [FT]); phonon collection (2409.19238, 2311.11930).

---

## 2. The low-energy excess (LEE)

**Phenomenology.** Rising spectra below a few hundred eV in CONNIE, CRESST, DAMIC, EDELWEISS, MINER, NEWS-G, NUCLEUS, RICOCHET, SENSEI, SuperCDMS
(EXCESS workshop, 2202.05097 [ABS]). DAMIC@SNOLAB bulk excess confirmed with skipper CCDs: ~7 events/kg-day at ~80 eV_ee, origin unknown
(2306.01717 [ABS]). CRESST: time, energy and temperature dependence exclude DM, radioactivity and crystal-bulk sources as major contribution
(2207.09375 [ABS]); "solid-state physics aspects" favoured (2212.12513 [FT]).

**Leading explanations (non-DM).**
- Stress relaxation: glued vs suspended Si crystal differ by >10² in low-energy phonon event rate, decaying with time since cooldown
  (2208.02790 [ABS]); dislocation motion in Al films (strain ~4 × 10⁻³, ~400 MPa), predicting a 1/t rather than exponential decay
  (2406.15425 [FT]); interfacial thermal-contraction mismatch with SiO₂ under TESs (2605.30194 [ABS]); slower cooldowns lower initial LEE
  rate in NUCLEUS sapphire (2603.07687 [ABS]).
- Defect annealing: atomistic simulations reproduce exponential energy-release spectrum from long-term annealing of recoil-induced defects
  (2408.07518 [ABS]); defect-threshold bump as an NR/ER discriminator in diamond (2112.14495 [ABS]).
- Radiative secondaries: Cherenkov, transition radiation, recombination luminescence (2011.13939 [FT]).

**Theory channels proposed as DM explanations and their status.**
- Kurinsky, Baxter, Kahn, Krnjaic 2002.06937: DM-excited plasmons (needs plasmon probability ~10⁻³–1 with multiphonons). Robinson & Michaud
  2002.08893: assumes "unphysical ionization yield" for plasmons; reply 2003.00101. Kozaczuk & Lin 2003.12077: plasmon bremsstrahlung from
  recoiling nuclei is 4–5 orders below elastic, "cannot explain the excesses" (multiphonon-associated plasmon not covered) [FT].
- Common-origin check, 2202.03436: CPD (Si, >40 eV) and EDELWEISS-Surf (Ge, >100 eV) excesses share power law α ≈ 3.43 and
  ~A² scaling, but DM-NR origin "strongly disfavored" even allowing exotic condensed-matter effects [ABS].
- Status: no viable DM interpretation survives; plasmon channel is dead as an explanation but survives as a *signal* channel (2003.12077,
  2403.00123).

**What limits mean in the presence of the LEE.** CRESST, CPD, TESSERACT, EDELWEISS-Surf use Yellin optimum interval treating every event as
potential signal (2212.12513, 2503.03683 [FT]); the lowest-mass NR points are therefore set by the unmodelled LEE plus the theory of the
signal shape at a few eV. TESSERACT used a two-channel cut to remove sensor-coupled LEE (2503.03683 [FT]). For CCDs and HVeV the 1e⁻–2e⁻ bins
are background-limited by spurious charge, Cherenkov and luminescence, so ER limits at the lightest masses are background-limited too.
Because no LEE model predicts a spectrum with an uncertainty, nobody subtracts it, and limits degrade rather than improve with exposure
[EST].

---

## 3. Exclusion plots in current use

| Experiment (latest ID) | Target / readout | ER theory | NR / Migdal theory | Ionization / response | Lowest-mass reach claimed |
|---|---|---|---|---|---|
| SENSEI@SNOLAB (2312.13342; 1e⁻ rate 2410.18716) | Si skipper CCD | QEdark (orig., unscreened) main; QCDark, EXCEED-DM, DarkELF in SM | Migdal: Berghaus et al. (2210.06490) w/ DarkELF | R&K; halo 2105.00599 | ~0.5 MeV (ER, light med.); Migdal best below ~40 MeV [FT] |
| DAMIC-M (2503.14617; modulation 2511.13962, 2307.07251) | Si skipper CCD | QCDark + analytic screening (QEdark shown for comparison) | Migdal (heavy med.) shown; Earth-shielding caveat near 1 MeV | R&K-type MC | 1–1000 MeV; freeze-in excluded 3.5–490 MeV [FT]; modulation 0.53–2 MeV |
| SuperCDMS HVeV (2407.08085, 2509.03608) | Si, NTL phonon, single-charge | rates via SENSEI-type crystal form factor | — | R&K (Ref. 2004.10709), E_g = 1.131 eV; CT/II model | 0.5 MeV (2024), 1 MeV (2025) [ABS] |
| SuperCDMS CPD (2007.14289) | Si athermal phonon, σ_E = 3.9 eV | — | free NR, heat quenching = 1 | — | most stringent 93–140 MeV [ABS/FT] |
| SuperCDMS Soudan Migdal/brems (2203.02594) | Ge, Si | — | isolated-atom Migdal | — | Migdal to 30 MeV, brems to 220 MeV [ABS] |
| EDELWEISS ER (2003.01046) | Ge 33 g, NTL, 0.53 e⁻ RMS | QEdark | — | literature ionization model, F = 0.15 | sub-MeV (~0.5 MeV) [FT] |
| EDELWEISS-Surf (1901.03588) / Migdal (2203.03993) | Ge | — | free NR; isolated-atom Migdal | 30 eV_ee threshold | NR >600 MeV best above ground; Migdal 32 MeV–2 GeV [ABS] |
| CRESST-III Si (2212.12513); CaWO₄ (1904.00498); diamond (2310.05815) | phonon + light | — | free NR, SHM | 10 eV_nr threshold | 115 MeV (Si), 122 MeV (diamond) [ABS] |
| TESSERACT surface (2503.03683) | Si athermal phonon, σ = 0.36 eV | — | Lewin–Smith free NR at 1.5 eV threshold | salting | 44 MeV, "lowest mass ever probed" by NR [FT] |
| QROCODILE (2412.16279) | WSi SNSPD (thin film) | Drude dielectric for WSi, anisotropic thin-film response | NR via phonon production (structure factor) | SHM with v_esc = 600 | 30 keV [ABS/FT] |
| CDEX-10 (2206.04128) | Ge PPC, 160 eV_ee threshold | EXCEED-DM (only >160 eV_ee kept: core/3d dominated) | Migdal (earlier works) to ~30 MeV | — | best solid-state for m_χ > 90 MeV (heavy med.) [ABS] |
| Qubits / quantum devices (2601.02474, 2210.09313) | transmons, QP devices, CPD power | Lindhard-type ELF | — | QP generation efficiency | keV-scale (qubits); ~10 MeV–10 GeV NR (power) [ABS] |

**Where theory dominates the edge of the plot.**
1. *ER, lightest masses (m_χ ≲ 3 MeV, Si/Ge):* rate comes from ω within a few eV of the gap and from q near the kinematic minimum. Here the
   code ratio reaches 2 (DAMIC-M QCDark/EXCEED-DM ≈ 0.5 at 1 MeV [FT]), screening is largest (2101.08275 [FT]), only the 1e⁻–2e⁻ bins contribute
   where R&K and step models differ (2306.14944 [FT]), and the clamped-lattice T = 0 band edge sets the kinematic cutoff (survey §4).
2. *ER, heavy mediator, m_χ ≳ 10 MeV:* the curve is set by high-q all-electron physics; QEdark/DarkELF under-predict (2312.13342, 2603.12326
   [FT]); Ge 3d differences ~10× (2105.05253 [FT]). CDEX's whole limit is in this regime.
3. *NR calorimetry, m_χ ≈ 40–150 MeV:* thresholds 0.4–10 eV are at or below the Si displacement threshold, so free-NR + unit heat quenching is
   assumed where the energy partition between phonons, defects and electrons is unknown; LEE dominates counts.
4. *Migdal curves, 30–100 MeV:* model choice (atomic vs ELF vs EFT) changes rates by up to an order of magnitude (2011.09496, 2003.12077 caption
   [FT]); factor 2 from the impulse approximation alone (2210.06490 [FT]).
5. *Sub-MeV (superconductors, SNSPD, Dirac/doped targets):* the edge is set by a model dielectric function (Drude/Lindhard) never validated
   in the superconducting state (2609.06423 [ABS]) and by quasiparticle-to-signal efficiency.

---

## 4. Gaps and deficiencies, ranked by impact on exclusion plots

Ranking criterion: (size of effect) × (how much of the current published parameter space it moves) × (absence of any existing treatment).

### G1. Near-gap energy partition: the ionization yield below ~50 eV (Si and especially Ge)
- *Missing:* a predictive, first-principles P(Q|ω, q, T) near the gap. R&K is phenomenological with a tuned non-physical parameter A and
  temperature only via E_g(T); it ignores the q-dependence of the initial e–h energy split and phonon-assisted relaxation channels
  (2004.10709 [FT]). For Ge only a step function exists (2306.14944 [FT]). Fano factor measured only at 5.9 keV (2004.11499).
- *Plots affected:* every Si/Ge ER limit at m_χ ≲ 5 MeV (SENSEI, DAMIC-M, HVeV, EDELWEISS, future Oscura 2202.10518 and SuperCDMS SNOLAB).
- *Size:* ~50 % systematic (2004.10709 [FT]); "significant" 1–2e⁻ bin differences (2306.14944 [FT]); for EDELWEISS-Ge unknown [EST: factor ~2].
- *Improvement:* ab-initio hot-carrier cascade (DFT/GW bands + EPW electron–phonon scattering rates + impact-ionization matrix elements) as a
  function of initial (ω, q) from the DM vertex, not from a photon; validate on quantum-yield and skipper-CCD calibration; deliver tabulated
  P(Q|ω) with error bands for Si, Ge, GaAs at 0.1–120 K.

### G2. The kinematic and spectral edge at the gap: frozen lattice, T = 0, phonon-assisted transitions
- *Missing:* every production ER calculation uses clamped nuclei at T = 0 (survey §1.2; 2603.12326 [FT]). Scissor-shifted gaps include
  zero-point renormalization but matrix elements and band-edge broadening do not. Second-order DM–e × e–ph ("phonon-assisted ER") not
  computed (survey §4).
- *Plots affected:* lowest-mass end of SENSEI/DAMIC-M/HVeV/EDELWEISS ER curves (0.3–3 MeV) and the 1e⁻ bin; DAMIC-M modulation range
  0.53–2 MeV.
- *Size:* code-to-code factor 2 at 1 MeV already (2503.14617 [FT]); for Si a window 0.34–0.47 MeV where first-order rate is kinematically
  closed and the phonon-assisted rate is leading (survey §4 [EST]); thermal band-tail effects at 100 K CCD temperature [EST: tens of % in 1e⁻
  bin at m_χ ≈ 1 MeV].
- *Improvement:* finite-T crystal response via special displacement / ZG-configuration averaging or EPW-based second-order rates, plugged into
  QCDark2/EXCEED-DM; publish ratio R(T)/R(0) per Q bin.

### G3. NR energy partition at eV thresholds (calorimeters) and free-NR at 1–10 eV
- *Missing:* TESSERACT (1.5 eV threshold), CRESST (10 eV_nr), CPD use free NR with Lewin–Smith/Helm and heat quenching = 1 (2503.03683,
  2007.14289 [FT]). At these energies a fraction of energy is stored in Frenkel defects (E_d ≈ 20 eV in Ge, anisotropic; 1805.09942,
  2210.01557), and the final state is multiphonon (survey §2). The multiphonon S(q,ω) codes (DarkELF, 2205.02250) are not used by
  experiments.
- *Plots affected:* NR curves at 40–150 MeV (TESSERACT, CRESST, CPD, EDELWEISS-Surf), CEvNS-fog estimates.
- *Size:* defect loss ~6 % at 100 keV (1805.09942) and rising toward E_d; below E_d the defect channel switches off, producing a step/bump in the
  observed spectrum (2112.14495 [ABS]); free-vs-multiphonon differences small for E_R ≫ ħω_ph but O(1) within a few × ħω_ph [EST].
- *Improvement:* a joint MD + multiphonon response giving the measurable heat/ionization partition per recoil (E_R, direction), with
  anisotropy; experiments should convolve signal with it instead of setting quenching = 1.

### G4. No theory uncertainty on exclusion curves; incompatible conventions at the edge
- *Missing:* all experiments publish single curves; SENSEI explicitly says the four-code spread "should not be taken as an uncertainty"
  (2312.13342 [FT]). Different halo parameters (v_esc 544 vs 600; ρ 0.3 vs 0.4) and codes are mixed in comparison plots.
- *Plots affected:* every combined "world limit" plot, freeze-in/freeze-out benchmark exclusions (DAMIC-M excludes freeze-in 3.5–490 MeV
  [FT]).
- *Size:* combined code × ionization × halo spread ≈ factor 2–3 at m_χ ≈ 1 MeV [EST from §1.1 entries].
- *Improvement:* a shared, versioned response library with nuisance parameters (XC functional, q_max, LFE, ionization model, F, E_g(T)),
  propagated by profile likelihood; benchmark exclusion bands.

### G5. Screening and many-body effects beyond RPA (LFE done; excitons, vertex corrections not for Si/Ge)
- *Missing:* production limits use unscreened (SENSEI main) or analytic MTF (DAMIC-M) screening, both shown to deviate from RPA+LFE
  (2603.12326 [FT]); BSE excitonic response done only for GaAs, NaI (2507.14345); no BSE/TDDFT-kernel ELF for Si, Ge at finite q.
- *Plots affected:* all Si/Ge ER curves; NaI/GaAs scintillator projections (2402.01395); boosted-DM limits.
- *Size:* 20–50 % (LFE), ×1.4–2.5 (screening at all), ×10² for boosted DM in low-Q bins (2101.08275, 2603.12326 [FT]); excitons "significant"
  in NaI, minimal in GaAs [ABS]; Si/Ge exciton binding is small (meV) [EST: <10 % except within ~0.1 eV of gap].
- *Improvement:* adopt QCDark2/RPA+LFE as default; BSE at finite q for Si/Ge near the gap; validate against NIXS/EELS data (2603.12326 compares
  with NIXS for q < 3 αm_e [FT]).

### G6. Inconsistent Migdal treatments, and Migdal vs multiphonon double counting
- *Missing:* SuperCDMS/EDELWEISS use isolated atoms, SENSEI/DAMIC-M use the semiconductor EFT; NR multiphonon (DarkELF) and Migdal (ELF)
  are computed with separate approximations (harmonic, incoherent) and never in one framework with consistent sum rules; the Migdal
  contribution to measured NR quenching (2104.01811) is not subtracted from Lindhard-calibrated yields. No semiconductor measurement exists
  (2210.04917).
- *Plots affected:* all Migdal limits 30–100 MeV; Migdal near 1 MeV with Earth-shielding caveat (DAMIC-M [FT]).
- *Size:* order of magnitude between models (2011.09496 [ABS]; 2003.12077 caption [FT]); ×2 from impulse approx (2210.06490 [FT]).
- *Improvement:* single non-adiabatic Born–Oppenheimer framework (2505.08864) yielding S(q,ω_ph,ω_e) jointly; neutron-calibration
  predictions for Si (2210.04917); experiments should adopt one convention.

### G7. Core levels, all-electron and relativistic bound-state effects at high Q
- *Missing:* QEdark/DarkELF lack high-q modes and Ge 3d (2603.12326 [FT]); XC functional misplaces Ge 3d by ~4.5 eV (2306.14944 [FT]);
  relativistic (Dirac) treatment of crystal core states absent — atoms only (2509.14534); factorized "free electron × form factor" ansatz
  questioned (2509.14534).
- *Plots affected:* heavy-mediator ER curves above ~10 MeV; CDEX (entirely 3d-dominated above 160 eV_ee); high-Q bins of SENSEI.
- *Size:* ~10× (Ge, heavy) (2105.05253 [FT]); 30–50 % (relativistic, atoms) [ABS]; for Ge 3d at Z = 32 relativistic shifts are few % of binding
  [EST].
- *Improvement:* use QCDark/EXCEED-DM in all published heavy-mediator limits; GW or hybrid-functional 3d energies; scalar-relativistic +
  spin–orbit all-electron crystal response.

### G8. Halo-model dependence at the kinematic edge
- *Missing:* lowest-mass points use SHM with hard v_esc cutoff; no experiment shows halo bands; ER near the edge depends exponentially on the
  high-velocity tail.
- *Size:* ≲50 % within SHM (2011.12896 [FT]); Gaia-era v_esc shifts limits near threshold (1904.04781, for NR) [ABS]; O(10–20) across simulated MW analogues for multi-e⁻ thresholds (2001.09156 [FT]); light-mediator
  inversion poorly constrained (2311.04957 [ABS]).
- *Improvement:* report halo-independent bounds alongside SHM; standardize v_esc (544 per 2105.00599) across comparison plots.

### G9. Superconducting, thin-film and sub-MeV targets: model dielectric functions
- *Missing:* QROCODILE uses a Drude dielectric for WSi (2412.16279 [FT]); superconductor analyses use free-electron Lindhard whose validity
  in the BCS state was untested until 2609.06423 [ABS]; Al branch-cut subtleties change rates by up to 10⁷ (2101.08263 [FT]); quasiparticle
  yield per deposited meV is modelled, not computed.
- *Plots affected:* everything below ~1 MeV (QROCODILE 30 keV, qubit limits 2601.02474, Al/Dirac-material projections 1708.08929, 1910.02091).
- *Size:* O(1)–orders of magnitude at the lowest masses [ABS/FT as cited].
- *Improvement:* measured or ab-initio ELF of the actual film (disorder, thickness, BCS coherence factors); pair-breaking efficiency
  calculation from e–ph Eliashberg functions.

### G10. In-medium consistency of non-density EFT operators, spin-dependent responses, intermediate mediators
- *Missing:* experiments report only F_DM = 1 and 1/q²; screening of spin/current couplings is not consistently implemented; 2510.25835
  shows a class of spin-dependent rates is fixed entirely by ε; NR-EFT crystal responses exist (2105.02233, 2402.06817, 2407.14598) but are
  not used in limits; light/heavy limits are separated by up to three orders of magnitude in mediator mass (2605.11063).
- *Plots affected:* model interpretations (benchmark relic lines), non-standard operators.
- *Size:* unknown per operator; for intermediate mediators the excluded region shifts by orders of magnitude in m_φ (2605.11063 [ABS]).
- *Improvement:* publish response-function tables (density, spin, current) so recasts are possible; a consistent linear-response screening of
  all operators.

### G11. Anisotropy and daily modulation
- *Missing:* production rates are angle-averaged; anisotropic ELF changes modulation (Migdal modulation only from quadrupole, 2607.06005);
  DAMIC-M modulation analyses use Earth-attenuation modulation, not crystal anisotropy (2511.13962); NR anisotropic thresholds
  (2210.01557, 2301.06592); multiphonon modulation 1–10 % in Al₂O₃ (2411.03433).
- *Plots affected:* modulation limits; time-averaged limits barely [EST: few %].
- *Improvement:* q-resolved anisotropic tables in public codes; joint crystal-orientation + Earth-scattering signal model.

### G12. Defect, dopant and colour-centre channels
- *Missing:* sensitivity projections only (color centers 1705.03016; crystal defects 2002.03525; doped semiconductors 2212.04504); dopant
  levels and shallow-trap release are background (charge traps 2510.23336) but no signal-side theory with error bands.
- *Plots affected:* projections only; indirectly the LEE (G3, §2).
- *Improvement:* defect formation/annealing cross sections from MD + DFT with uncertainties.

### G13. Anharmonicity (low impact on current plots)
- Up to 10² at O(MeV) but only for very large σ; negligible above ~10 MeV (2309.10839); halo-dependent (2412.18330). Current NR thresholds
  (≥ 0.4 eV) do not reach this regime → lowest rank.

### Ranked summary
| Rank | Gap | Plots | Size | Existing work |
|---|---|---|---|---|
| 1 | Near-gap ionization yield (Si, Ge) | ER, m_χ ≲ 5 MeV | ~50 %–×2 | R&K (phenom.), none for Ge |
| 2 | Frozen lattice / T = 0 / phonon-assisted edge | ER, 0.3–3 MeV; modulation | ×2 at 1 MeV; window 0.34–0.47 MeV (Si) | none for (c) |
| 3 | NR energy partition at eV thresholds | NR 40–150 MeV | O(1) near E_d | MD yields, not used |
| 4 | No theory error bands; mixed conventions | all combined plots | ×2–3 at 1 MeV [EST] | none |
| 5 | Screening beyond analytic; excitons Si/Ge | all ER | 20–50 %; ×1.4–2.5 | QCDark2 (2026) |
| 6 | Migdal inconsistency | Migdal 30–100 MeV | ×2–×10 | EFT, BO (partial) |
| 7 | Core / all-electron / relativistic | heavy-med. ER, CDEX | up to ×10 (Ge) | QCDark, EXCEED-DM |
| 8 | Halo edge | lowest masses | 50 %–×10 | halo-indep. (2311.04957) |
| 9 | Superconductor / film ELF | < 1 MeV | O(1)–orders | 2609.06423 |
| 10 | EFT operators in medium | model plots | ? | 2510.25835 |
| 11 | Anisotropy | modulation | few % (avg) | 2607.06005, 2411.03433 |
| 12 | Defect / dopant channels | projections | — | proposals |
| 13 | Anharmonicity | NR ≲ 10 MeV, large σ | ≤10², narrow | 2309.10839 |

---

## 5. Search log
- `lit.py arxiv` (2–4 term queries, ~90): SENSEI skipper CCD; DAMIC-M dark matter electron; SuperCDMS HVeV; SuperCDMS CPD; EDELWEISS electron
  recoil germanium; CRESST low-mass; TESSERACT; QROCODILE; CDEX dark matter electron; low energy excess (+ cryogenic detectors, stress
  relaxation, NUCLEUS, CRESST-III, EXCESS workshop); Kurinsky plasmon; plasmon production nuclear recoil; Lindhard silicon quenching;
  silicon ionization efficiency nuclear recoil; germanium quenching factor; Fano factor silicon; impact ionization silicon; Migdal (measurement,
  semiconductor, crystal, multiphonon, SENSEI, observation); astrophysical / halo / escape-velocity uncertainties; QCDark; EXCEED-DM;
  QEdark; DarkELF; local field effects; in-medium screening; exciton; spin-dependent; superconductor; magnon; Dirac materials; doped
  semiconductor; color center; defect creation; anharmonic; sum rule; NR-EFT electron; Ge ionization yield; daily modulation; GaAs; SiC;
  diamond; graphene; SNSPD; qubit; relativistic bound electron; uncertainty bands (no hits).
- Full text fetched and read (grep + targeted sections): 2004.10709, 2312.13342, 2503.14617, 2407.08085, 2509.03608, 2007.14289,
  2003.01046, 2212.12513, 2503.03683, 2412.16279, 2206.04128, 2011.13939, 2202.05097, 2003.12077, 2406.15425, 2001.09156, 2011.12896,
  2202.03436, 2509.14534; plus already-present files 2306.14944, 2101.08275, 2101.08263, 2105.05253, 2210.14917, 2603.12326, 2011.09496,
  2210.06490.
- Not found: any exclusion curve published with a theory band; any first-principles ionization yield for Ge below 50 eV; any finite-T DM–e
  crystal response used in a limit.

## 6. Verified arXiv IDs (arXiv API, 2026-10-31)
1509.01598 1608.00957 1705.03016 1707.07258 1708.08929 1805.09942 1901.03588 1904.00498 1904.04781 1908.10881 1910.02091
1910.02162 1912.11549 2001.06503 2001.09156 2002.03525 2002.06937 2002.08893 2003.00101 2003.12077 2004.10709 2004.11499 2007.14289
2011.09496 2011.12896 2011.13939 2101.08263 2101.08275 2102.10089 2104.01811 2104.12786 2105.00599 2105.02233 2105.05253 2112.14495
2202.03436 2202.03754 2202.05097 2202.10518 2203.00750 2203.02594 2203.03993 2205.02250 2206.04128 2206.13639 2207.08284 2207.09375
2208.02790 2209.04503 2210.01557 2210.04917 2210.06490 2210.09313 2210.14917 2212.04504 2212.12513 2301.06592 2306.01717 2306.14944
2307.07251 2309.10839 2310.05815 2311.04957 2311.11930 2312.13342 2402.01395 2402.06817 2403.00123 2403.01259 2405.10405 2406.15425
2407.08085 2407.14598 2408.07518 2409.19238 2410.18716 2411.03433 2412.16279 2412.18330 2503.03683 2503.14617 2505.08864 2506.03810
2507.14345 2509.03608 2509.14534 2510.23336 2510.25835 2511.13962 2601.02474 2603.07687 2603.12326 2603.13052 2603.16702 2605.11063
2605.30194 2605.30281 2607.06005 2609.06423 2610.22418
