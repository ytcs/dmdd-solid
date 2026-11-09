# CATALOG-A: channels by which dark matter deposits energy in a solid-state target (Round R1b)

Compiled 2026-10-31 by the CAT-A literature agent. Scope: every channel by which a DM particle, or a bosonic DM
field, deposits energy or momentum in a solid and leaves a detectable excitation. The catalog starts from the
reviews (Kahn & Lin 2108.03239; Mitridate, Trickle, Zhang & Zurek 2203.07492; Essig et al. Snowmass 2203.08297;
Cooley et al. Snowmass 2209.07426) and walks forward to Oct 2026 using `lit.py arxiv` (about 90 queries of 2–4
terms) and INSPIRE citation walks. The walks pulled the 2024–26 citers of 2203.07492, 2108.03239, 2009.13534,
2104.12786, 2210.14917 and 2203.08297, 192 unique records in all.

**Verification.** Every arXiv ID below was checked against the arXiv API (export.arxiv.org `id_list`, title and
authors) in this session. No ID failed. No full texts were fetched, so the claims rest on abstracts plus the
orientation survey `surveys/dm-solid-state-scattering.md`. Where I say a process is "not found", that means not
found in these searches. It is not an exhaustive audit.

**Status codes.** **FP** = computed from first principles for real materials (DFT, DFPT or many-body inputs).
**M** = modelled (analytic, phenomenological or data-driven response). **P** = proposed, with order-of-magnitude
reach only. **NC** = not computed / not found.

**Kinematics used throughout.** These are my estimates. They take v ≲ v_esc + v_E ≈ 800 km/s ≈ 2.7×10⁻³ c, so the
DM kinetic energy is at most ≈ 3.5×10⁻⁶ m_χ. Scattering with energy deposit ω therefore needs m_χ ≳ ω / 3.5×10⁻⁶,
which gives 1 eV ↔ 0.3 MeV, 30 meV ↔ 10 keV and 1 meV ↔ 0.3 keV. Momentum constraints usually push the threshold
higher. Absorption deposits ω ≈ m_DM, with momentum q ≈ m_DM v ≈ 10⁻³ ω.

---

## 0. Reviews, white papers and production codes

| Kind | Items |
|---|---|
| Reviews / white papers | Kahn & Lin [2108.03239]; Mitridate, Trickle, Zhang, Zurek [2203.07492]; Essig et al. [2203.08297]; Cooley et al. [2209.07426]; Battaglieri et al. Cosmic Visions [1707.04591]; Wave-DM Snowmass [2209.08125]; Esposito, Nicolis, Penco, *EFTs for material media* [2607.06666]; Baxter et al., low-energy backgrounds [2503.08859] |
| Electron-response codes | **QEdark** [1509.01598]; **QCDark** [2306.14944] (all-electron, with RPA local fields in [2603.12326]); **EXCEED-DM** [2210.14917] (screening and general operators; intermediate mediators [2605.11063]); **DarkELF** [2104.12786] (ELF, Migdal, multiphonon); deep-learning surrogate [2403.07053]; Blanco–Lillard–Shergold form-factor code for molecules [2512.18010] |
| Phonon / collective codes | **PhonoDark** (Trickle–Zhang–Zurek EFT [2009.13534], absorption [2308.06314]); DarkELF multiphonon module [2205.02250]; G4CMP for athermal-phonon transport [2408.04732]; wavelet methods [2608.06452] |
| General frameworks | NR-EFT for DM–electron interactions [2407.14598, 2105.02233]; linear response [2402.06817]; the "master formula" writing every DM–e rate in terms of measured response functions [2510.25835]; sum-rule bounds [2110.01587, 2501.18261, 2608.05282]; Kohn–Sham cutting rules [2507.11033]; transverse dielectric response [2608.20715] |

## 1. Coupling × excitation matrix (✔ = computed, FP or M; ◐ = proposed; ✗ = not found)

| Excitation ↓ / coupling → | e (SI, density) | nucleon (SI) | dark photon / kinetic mixing | e-spin / g_aee | nuclear spin / g_aNN | g_aγγ | scalar (e, N) |
|---|---|---|---|---|---|---|---|
| e–h pairs (valence, core) | ✔ FP | ✔ via Migdal | ✔ FP (abs. + scat.) | ✔ M/FP | ✗ | ◐ (B-field) | ✔ M (abs.) |
| Excitons | ✔ FP (BSE, Si/Ge only) | ✗ | ✔ implicit (optical data) | ✗ | ✗ | ✗ | ✗ |
| Plasmons | ✔ M (ELF) | ✔ M (loop) [2510.18338] | ✔ M | ✗ | ✗ | ✔ (plasma haloscope) | ✗ |
| Single phonons | ✔ M (polar, via Born charges) | ✔ FP | ✔ FP | ✔ FP (EFT) | ✔ M [2411.10542] | ✔ (B-field polaritons) | ✔ FP (abs.) |
| Multiphonons | ✗ | ✔ M | ✔ M | ✗ | ✔ M (SD-nucleon) [2506.11191] | ✗ | ✗ |
| Phonon polaritons | — | — | ✔ FP | ✗ | ✗ | ✔ FP (in B) | ✗ |
| Magnons | — | — | ✗ | ✔ FP / EFT | ◐ | ✔ (axion quasiparticle) | ✗ |
| SC quasiparticles | ✔ M | ✔ M | ✔ M | ✗ | ✗ | ✗ | ✔ M |
| Dirac / narrow gap | ✔ M/FP | ✗ | ✔ M | ✗ | ✗ | ◐ | ✗ |
| Dopants / defects | ✔ M | ✔ M (damage) | ✔ M | ✗ | ✗ | ✗ | ✗ |
| Molecular / organic | ✔ FP (molecular QC) | ✔ (bond breaking) | ✔ (molecular abs.) | ✗ | ✗ | ✗ | ✔ (vibrational abs.) |
| Migdal / bremsstrahlung | — | ✔ FP/M | ✔ (Migdal) | ✗ | ✗ | — | ✔ (abs.-Migdal, atoms) |

---

## 2. Electronic excitations

| # | Process | m_DM / regime | ω, threshold | Formalism / codes | Key papers | Status | Experiments |
|---|---|---|---|---|---|---|---|
| E1 | Valence band-to-band e–h (Si, Ge, GaAs, diamond, SiC) | ≳0.3–0.5 MeV, scattering | E_g ≈ 0.7–5.5 eV; 1 e⁻ thresholds | DFT Bloch states; ELF/RPA; NR-EFT | 1108.5383, 1203.2531, 1509.01598, 1508.07361, 2105.05253, 2306.14944, 2101.08275, 2101.08263, 2603.12326 | FP | SENSEI 2004.11378, 2312.13342; DAMIC-M 2302.02372, 2503.14617; SuperCDMS HVeV 2407.08085, 2509.03608; EDELWEISS 2003.01046 |
| E2 | Core / semicore ionization in crystals | ≳10s MeV, large q | 10–100s eV | all-electron PAW reconstruction | 2105.05253, 2210.14917, 2306.14944; bound-state kinematics 2509.14534 | FP | same |
| E3 | General (spin/velocity-dependent) DM–e operators | as E1 | as E1 | NR-EFT, ≥5 crystal responses | 2105.02233, 2407.14598, 2402.06817, 2106.16214, 2510.25835 | FP (Si/Ge) | reinterpretation |
| E4 | Excitons (Wannier, via BSE) | ~0.5–few MeV, ω ≈ E_g | just below the gap | GW + Bethe–Salpeter | 2507.14345 | FP (one paper) | — |
| E5 | Frenkel excitons in organic crystals / molecules | ≳ MeV | 3–5 eV (scintillation) | molecular orbitals; anisotropic form factors | 1912.02822, 2103.08601, 2512.18010, 2607.12036 | FP (QC) | proposed |
| E6 | Dark / indirect excitons, exciton–phonon bound states | sub-MeV edge | E_g − E_b | — | none found | NC | — |
| E7 | Plasmons (bulk) | needs q ≳ ω_p/v_F; mostly ✗ for halo DM | ω_p ≈ 15–17 eV (Si, Ge) | ELF, Lindhard / RPA | 2002.06937, 2003.12077, 2101.08263, 2101.08275; boosted DM 2401.11971, 2501.07591; relativistic 2403.00123 | M | — |
| E8 | Low-energy / exotic plasmons (CDW, demons, 1D Luttinger, 2D) | keV–MeV | meV–eV | ELF, model Hamiltonians | 2507.07164, 2607.15338, 2608.01305, 2510.18338 | M/P | — |
| E9 | Heterostructure / layered responses | sub-MeV | meV–eV | sum rules, effective dielectric | 2110.01587, 2603.15581 | M/P | — |
| E10 | Quantum-dot excitations | ≳ MeV | ~2 eV + scintillation | ab initio QD electronic structure | 2208.05967, 2608.18204 | FP (new) | proposed |
| E11 | Narrow-gap / Dirac / Weyl quasiparticles | keV–MeV | meV–0.1 eV | Dirac Hamiltonians + in-medium screening; DFT for spin-orbit gapped | 1708.08929, 1910.02091, 1909.09170, 2008.05062, 2202.11716, 2305.19967 | M → FP (2202.11716) | SPLENDOR 2507.17782 |
| E12 | Graphene / CNT / bilayer graphene | keV–MeV | sub-eV to eV | tight-binding, DFT | 1606.08849, 1706.02487, 2303.15497, 2312.00866, 2604.21969 | M/FP | GLIMPSE 2002.07821 (proposed) |
| E13 | Superconducting Cooper-pair breaking (scattering) | ≳ keV | 2Δ ≈ 0.3–1 meV | BCS + Lindhard, in-medium screening | 1504.07237, 1512.04533, 2101.08263, 2109.04473, 2609.06423 | M | SNSPD 1903.05101, 2110.01586, QROCODILE 2412.16279; KIDs 2403.19739; qubits 2601.02474 |
| E14 | Shallow-dopant ionization | ≳ few keV (scat.), ≳10 meV (abs.) | ~10–50 meV | hydrogenic donor model | 2212.04504 | M | proposed |
| E15 | Colour-centre / NV / SiV electronic transitions (DM–e) | MeV | ~eV | — | 1901.07569 (diamond as e target) | M | CRESST diamond 2310.05815 (NR) |

**E1–E3. Band-to-band and core e–h pairs.** These are the workhorse channels. The theory runs from the original
proposals [1108.5383, 1203.2531] through QEdark [1509.01598] and modulation work [1508.07361] to the
all-electron/extended codes [2105.05253, 2210.14917, 2306.14944]. In-medium screening enters through the ELF,
Im[−1/ε(q,ω)] [2101.08275, 2101.08263], and the current state of the art for Si/Ge is all-electron + RPA with
local fields [2603.12326]. General operators are handled by NR-EFT with several crystal response functions
[2105.02233, 2407.14598, 2402.06817]. The data-driven master formula [2510.25835] and the sum-rule ceilings
[2110.01587, 2501.18261, 2608.05282] bound the rate in a material-agnostic way. Material screening is now
high-throughput [2506.19905]. Further recent work covers anisotropy and daily modulation [2607.06005, 2510.20889],
intermediate-mass mediators [2605.11063] and the ε_T contribution [2608.20715]. Open systematics: every production
code uses a frozen lattice at T = 0 (survey §4). The conversion of energy to charge, the ionization yield, is
phenomenological [2004.10709]. Inelastic and solar-reflected DM in crystals are covered in [2203.06664, 2607.09352].

**E4–E6. Excitons.** The only first-principles DM exciton calculation is the BSE study by Taufertshöfer et al.
[2507.14345]: the rate rises near ω ≈ E_g in Si/Ge. Frenkel excitons in aromatic crystals (trans-stilbene and
others) are treated as molecular excitations with anisotropic form factors [1912.02822, 2103.08601] and computed
with efficient many-body numerics [2512.18010, 2607.12036]. **Dark/indirect excitons and phonon-assisted exciton
creation were not found** (E6, gap).

**E7–E9. Plasmons.** For halo DM, bulk plasmons in Si/Ge (ω_p ≈ 16 eV) are kinematically hard to reach: slow DM
cannot supply ω_p at q ≲ ω_p/v_F [2003.12077]. The ELF approach still captures the plasmon pole in the screening
[2101.08263, 2101.08275]. A plasmon interpretation of low-energy excesses [2002.06937] was later revisited and
disfavoured [2202.03436]. Plasmons become relevant for boosted/relativistic particles [2401.11971, 2501.07591,
2403.00123], for leptophobic DM through a loop-induced coupling [2510.18338], for self-interacting light DM
[2608.01305], and for low-energy plasmons in unconventional materials: TiSe₂ CDW plasmon, Sr₂RuO₄ demon mode
[2507.07164], and 1D Luttinger modes in CNTs [2607.15338]. Heterostructures [2110.01587] and vdW stacks [2603.15581]
let one engineer the response.

**E10–E12. Low-dimensional and Dirac targets.** For Dirac/Weyl materials, weak screening (small ε) offsets the
small phase space and gives sensitivity to keV DM [1708.08929, 1910.02091]. Anisotropy gives directionality
[1909.09170]. Spin-orbit gapped materials have been predicted from DFT [2008.05062] and computed with
first-principles SOC wavefunctions [2202.11716]. Flat bands help further [2305.19967]. Graphene and CNT targets are
directional [1606.08849, 1706.02487]; graphene also has an ab initio general-operator calculation [2303.15497],
and bilayer graphene has a tunable gap [2312.00866, 2604.21969]. Experimentally, the narrow-gap platform is
SPLENDOR [2507.17782].

**E13. Superconductors.** Here a DM scatter breaks Cooper pairs, creating quasiparticles; the deposit is 2Δ for Al.
The Pauli-blocking analysis appears in [1504.07237, 1512.04533]. In-medium screening suppresses the rate strongly,
so it must be included [2101.08263]; directionality is studied in [2109.04473] and a mean-field dielectric
treatment in [2609.06423]. Readout options are SNSPDs [1903.05101, 2110.01586, 2412.16279], KIDs
[2403.19739, 2607.19319], TES [2506.18982, 2506.10070] and qubits [2601.02474, 2405.00112].

**E14–E15. Dopants and colour centres (electronic).** Dopant ionization at ~10–50 meV opens sub-MeV scattering and
sub-eV absorption [2212.04504]; it is modelled, with no first-principles dopant wavefunctions. Diamond as an
electron-recoil target is treated in [1901.07569]. No DM–e calculation that ends on NV/SiV electronic transitions
was found. Colour centres enter mainly as NR damage sensors (§5).

---

## 3. Lattice (nuclear/ionic) excitations

| # | Process | m_DM / regime | ω, threshold | Formalism / codes | Key papers | Status | Experiments |
|---|---|---|---|---|---|---|---|
| L1 | Single acoustic phonon | ~10 keV–10 MeV | 1–100 meV | DFT/DFPT (phonopy) + EFT; PhonoDark | 1910.08092, 2009.13534, 1905.05575 | FP | TESSERACT 2503.03683 (phonon readout) |
| L2 | Single optical / polar LO phonon (dark-photon mediator) | ~10 keV–MeV | 20–100 meV | Born effective charges, Fröhlich-like coupling | 1712.06598, 1807.10291, 2008.08560, 2502.01732, 2409.02439 | FP | TESSERACT (GaAs, sapphire), SPICE |
| L3 | Multiphonon (incoherent approximation) | ~1–100 MeV | ~ω_D to ~eV | dynamic structure factor S(q,ω), incoherent approx.; DarkELF | 1911.03482, 2205.02250, 2011.09477 | M (DFT phonon DOS) | CRESST-III 1904.00498 etc. |
| L4 | Anharmonic corrections to multiphonon | ~1–10 MeV | — | anharmonic oscillator; impulse matching | 2309.10839, 2412.18330 | M | — |
| L5 | Coherent → incoherent transition | MeV–100 MeV | — | solvable 1D N-site model | 2607.24933 | M | — |
| L6 | Free / impulse nuclear recoil | ≳100 MeV (Si) | E_R ≫ ω_D; thresholds 10–100 eV | free-nucleus kinematics + quenching | 2205.02250; Si/Ge yield data 2303.02196, 2102.10089, 2405.10405; MD simulation 2506.03810 | M (yield data-driven) | CRESST, SuperCDMS, EDELWEISS, DAMIC-M |
| L7 | Spin-dependent nucleon scattering → phonons | ≲100 MeV phonons, ≳100 MeV NR | as L3/L6 | incoherent phonon production from nuclear spins | 2506.11191 | M | — |
| L8 | Daily modulation of phonon / NR rates | ≲30 MeV | — | anisotropic S(q,ω) | 2411.03433, 2606.04091 | M | — |
| L9 | Chiral phonons (magnetic-moment readout) | sub-MeV | meV | DFT phonons of MOFs | 2301.07617, 2511.20461 | FP/P | proposed |
| L10 | Phonons in amorphous / random media | absorption meV–eV; sub-keV coherent | broadband | disordered phonon DOS; density fluctuations | 2603.22390, 2512.16451 | M/P | MICROSCOPE recast (2512.16451) |
| L11 | Solid-helium phonons (pressure-tuned) | keV–MeV | meV | ab initio phonons under pressure | 2409.02439 | FP | — |

**L1–L2. Single phonons.** Sub-MeV DM that couples to nucleons excites acoustic phonons coherently, with rate ∝ A².
A dark-photon mediator couples to polar optical (LO) phonons through Born effective charges [1712.06598,
1807.10291]. The EFT of collective excitations [2009.13534] and the multi-channel target comparison [1910.08092]
are implemented in PhonoDark. Further targets studied: SiC [2008.08560], perovskites [2502.01732] and solid He
[2409.02439]. Astrophysical uncertainties are treated in [2606.04091]. The general DM–phonon coupling is derived in
[1905.05575].

**L3–L6. Multiphonon to impulse NR.** The dynamic structure factor interpolates between single-phonon production
and free NR [1911.03482, 2205.02250]; Kahn–Krnjaic–Mandava call the low-energy end the "Poisson phonon tail"
[2011.09477]. Anharmonicity changes rates by up to ~10² at MeV masses [2309.10839, 2412.18330]. A solvable 1D model
shows how coherence emerges from interference [2607.24933]. At higher masses, NR measurements in Si/Ge at ~100 eV
[2303.02196, 2405.10405, 2102.10089] and MD simulations [2506.03810] calibrate the energy-to-ionization map.

---

## 4. Spin, magnetic and chiral responses

| # | Process | m_DM / regime | ω, threshold | Formalism | Key papers | Status | Experiments |
|---|---|---|---|---|---|---|---|
| S1 | Magnon scattering (e-spin coupling) | ~keV–MeV | 1–100 meV | Holstein–Primakoff on DFT magnetic structure; EFT | 1905.13744, 2009.13534, 2210.13516, 2501.18120 | FP/EFT | — |
| S2 | Axion / boson absorption into magnons (g_aee) | meV range | Kittel / AFM modes | spin-wave theory; in-B dispersion | 2005.10256, 2001.10666, 2411.11971 | FP/EFT | QUAX 1606.02201, 2001.08940; MOSAIC 2504.16160 |
| S3 | Axion quasiparticle (topological AFM) | 1–10 meV | AQ mass | axion electrodynamics | 1807.08810, 2102.05366 | M/P | — |
| S4 | Nuclear-spin precession (g_aNN, EDM) | neV–μeV, wave regime | NMR frequency | Bloch equations | 1306.6088, 1306.6089, 2101.01241, 2609.07908 | M | CASPEr-electric/solid |
| S5 | Broadband phonons from axion–nuclear-spin coupling | 1–100 meV | phonon band | phonon EFT with random spins | 2411.10542 | M | — |
| S6 | Spin-dependent response from neutron data | keV–MeV | — | dynamical magnetic susceptibility | 2504.02927 | M (data-driven) | — |
| S7 | Spin-dependent DM–e in electronic transitions | ≳ MeV | E_g | NR-EFT spin responses | 2106.16214, 2105.02233, 2510.25835 | FP/M | reinterpretation |
| S8 | Chiral phonons (see L9), single-molecule magnets | sub-MeV; meV abs. | meV | — | 2301.07617, 2601.01043 | P | — |
| S9 | Multiferroic / magnetoelectric axion coupling | meV | — | Landau theory | 2102.10171 | M | — |

**Paragraph.** If DM couples to electron spin, magnons are the natural final state [1905.13744]. Antiferromagnets
such as NiO are the best known targets [2210.13516, 2411.11971]; quasi-2D magnets give directionality [2501.18120].
For absorption, g_aee drives magnons and g_aγγ in a B field drives phonon polaritons [2005.10256], with the
conversion analysed in [2001.10666]. Neutron-scattering data fix the spin-dependent rate without ab initio input
[2504.02927]. Nuclear spins (CASPEr) probe g_aNN and the EDM coupling of wave-like ALPs [1306.6088, 1306.6089,
2101.01241, 2609.07908]. **Gaps:** chiral-response observables (optical activity, circular dichroism) for DM
scattering are proposed only, through magnetic moments of chiral phonons [2301.07617, 2511.20461]. Magnon
*multi*-excitation (two-magnon) continua and nuclear-spin magnons in solids were not found as computed DM channels.

---

## 5. Defect, damage and track channels

| # | Process | m_DM / regime | Threshold | Formalism | Key papers | Status | Experiments |
|---|---|---|---|---|---|---|---|
| D1 | Frenkel-pair creation / displacement threshold (energy lost to defects) | ≳ few 100 MeV (Si) | E_d ≈ 10–50 eV | classical / ab initio MD | 1703.05371, 2112.14495, 2301.06592, 2512.23553 | M (MD) | CRESST, COSINUS (NaI) |
| D2 | Colour-centre creation (F-centres) read out by fluorescence | sub-GeV (ER/NR) | few eV | defect-formation energetics | 1705.03016, 2104.13926, 2503.20732 | M + calibration data | LiF R&D (2503.20732) |
| D3 | Damage-track spectroscopy with NV/strain (directional) | WIMP (≳GeV) | 10s keV NR | NV strain spectroscopy | 1705.09760, 2009.01028 | P/R&D | diamond directional R&D |
| D4 | Paleo-detector tracks in minerals | ≳ 0.5 GeV to ultraheavy | track length ≳ 1–10 nm | SRIM/TRIM ranges | 1806.05991, 1811.06844, 2106.06559, 2301.07118, 2604.09732, 2606.02579 | M | mica, olivine, halite R&D |
| D5 | Chemical-bond breaking in molecular solids | sub-GeV | ~eV bond energy | molecular dynamics / thresholds | 1608.02940 | M/P | — |

**Paragraph.** Nuclear recoils above the displacement threshold leave Frenkel pairs. The energy stored in those
defects is invisible to phonon sensors, and the threshold is anisotropic, so the rate modulates daily
[1703.05371, 2301.06592]. Stored defect energy has been proposed as the source of the low-energy excess
[2112.14495], and defect formation in NaI has now been studied [2512.23553]. Colour centres turn damage into an
optical signal [1705.03016, 2104.13926, 2503.20732]. Track and strain spectroscopy in diamond [1705.09760,
2009.01028] and ancient minerals [1806.05991, 2106.06559, 2301.07118, 2604.09732, 2606.02579] extend reach to heavy
DM. All of these use classical MD or SRIM-style stopping. **Gap:** no DFT-level electronic-structure calculation of
defect creation by *sub-threshold or electronic (ER)* DM interactions was found.

---

## 6. Mixed nuclear → electronic channels

| # | Process | m_DM / regime | ω | Formalism | Key papers | Status | Experiments |
|---|---|---|---|---|---|---|---|
| X1 | Migdal effect, isolated atoms | ≳ 10s MeV | 10s eV to keV | sudden approximation, atomic Dirac–Hartree–Fock | 1707.07258, 1711.09906, 2208.12222, 1908.10881 | FP (atoms) | LXe searches 2307.12952, 2606.03174 |
| X2 | Migdal in crystals, impulse regime (ELF) | ≳ 50 MeV | ≳ E_g | ELF at the ion "kick"; DarkELF | 2011.09496 | M/FP | SENSEI, DAMIC-M, SuperCDMS reinterpretations |
| X3 | Migdal in crystals with phonon final states (small q) | ~MeV–100 MeV | ≳ E_g | EFT with measured S(q,ω) and ELF; NR-EFT extension | 2210.06490, 2603.13052 | M | — |
| X4 | Non-adiabatic Born–Oppenheimer derivation | as X3 | — | BO expansion | 2505.08864, 2606.14845 | M (formal) | — |
| X5 | Phonon-mediated (virtual-phonon) Migdal | down to ~MeV | ≳ E_g | e–ph vertex, incoherent approximation | 2205.03395, 2310.05704 | M | — |
| X6 | Migdal with Wannier functions / bremsstrahlung picture | ≳ 10s MeV | ≳ E_g | localized Wannier functions; many-body | 1912.13484, 2011.13352 | FP (diamond) | — |
| X7 | Anisotropic Migdal in Si, GaAs | ≳ 10s MeV | — | anisotropic ELF | 2607.06005 | FP | — |
| X8 | Migdal electron *excitation* (not ionization) | few MeV | ~eV UV | atomic (He) | 2604.26773 | M | He (not solid) |
| X9 | Nuclear-recoil bremsstrahlung (photon emission) | ≳ 100 MeV | keV photons | dipole emission from recoiling atom | 1607.01789, 1905.00046 | M (atoms) | LXe/LAr; crystals NC |
| X10 | Migdal-type effect in *absorption* (scalar–nucleon) | — | ionization | atomic | 2312.10566 | M (atoms) | — |
| X11 | Migdal measurement in semiconductors | — | — | neutron calibration design | 2210.04917 | P/R&D | — |

**Paragraph.** The Migdal effect in crystals is the best-developed composite channel. The impulse-regime ELF
formula [2011.09496] is complemented at small q by an EFT with phonon final states [2210.06490, 2603.13052], which
Esposito & Rocchi justify as purely non-adiabatic [2505.08864]; the adiabatic regime is treated in [2606.14845].
Liang et al. give tight-binding and Wannier versions [1912.13484, 2011.13352] and a phonon-mediated version
[2205.03395]. There is no observation in solids yet; a semiconductor measurement is proposed [2210.04917]. In LXe
there is a search [2307.12952] and a measurement-strategy paper [2606.03174]. NR bremsstrahlung [1607.01789,
1905.00046] has been computed only for isolated atoms or liquids; **a crystal calculation of NR bremsstrahlung
(phonon-dressed) was not found**, apart from the bremsstrahlung *picture* of Migdal [2011.13352].

---

## 7. Absorption of bosonic (and fermionic) DM

| # | Process | m_DM | Formalism | Key papers | Status | Experiments |
|---|---|---|---|---|---|---|
| A1 | Dark photon / ALP / scalar absorption on electrons (photo-/axio-electric) | ~E_g to keV | measured σ₁(ω) or DFT ε(ω); in-medium mixing | 0807.3279, 1412.8378, 1608.02123, 1608.01994, 2106.12586, 2303.11344 | FP + data-driven | SENSEI, DAMIC-M, SuperCDMS 2005.14067, EDELWEISS, Majorana, CDEX, GERDA |
| A2 | Absorption in superconductors / metals (phonon-assisted, two-loop) | 10 meV–eV | deformation-potential e–ph model | 1604.06800, 2106.12586 (App. A.3) | M | SNSPD, KIDs |
| A3 | Phonon-assisted absorption near the indirect gap (Si/Ge) | ~E_g | data-driven optical conductivity | 1608.01994 | M; FP **NC** (survey §4) | — |
| A4 | Single-phonon absorption (dark photon, ALP, scalar, B−L) | 10–100 meV | EFT + DFPT | 2308.06314, 1712.06598, 2005.10256 | FP | — |
| A5 | Absorption into phonon polaritons / magnetized medium (g_aγγ in B) | meV–eV | dielectric tensor in B | 2005.10256, 2209.12909, 2305.05681 | FP/M | — |
| A6 | Dopant absorption | 10–50 meV | hydrogenic | 2212.04504 | M | — |
| A7 | Broadband amorphous phonon absorption | meV–100 meV | disordered DOS | 2603.22390 | M | proposed |
| A8 | Qubit / device absorption (dark photon E-field) | μeV–meV | circuit QED | 2212.03884, 2412.20850, 2311.07857 | M | transmon searches |
| A9 | Piezoelectric BAR / hBAR phonon absorption | μeV–meV | electromechanical coupling | 2501.05504, 2410.17308 | M/P | proposed |
| A10 | Fermionic absorption (DM + N/e → ν + …) | MeV–100 MeV | nuclear / electronic | 1905.12635, 2308.00309, 2405.05728 | M | reinterpretations |
| A11 | Pair absorption, dark Compton, scattering+absorption interplay | various | — | 2507.14287, 2109.08168, 2501.09642 | M | — |
| A12 | Axion → photon in materials (dielectric / plasma haloscopes, heterostructures, Weyl CME, shift current, ferroelectric) | μeV–meV | macroscopic electrodynamics | 1611.05865, 1612.07057, 1904.11872, 2509.14320, 2606.13595, 2505.17007, 2204.11919 | M | MADMAX, ALPHA |

**Paragraph.** Absorption converts the full rest mass, so the rate is fixed by the in-medium conductivity: absorption
rate ∝ σ₁(ω = m), with in-medium mixing corrections for dark photons [1412.8378, 1608.01994, 2106.12586]. Most
results use measured optical data, which already contain the phonon-assisted pieces. **No EPW-style
first-principles DM absorption calculation including electron–phonon coupling was found** (survey §4). At meV, the
single-phonon absorption EFT [2308.06314] and magnetized-medium polaritons [2305.05681] are first-principles.
Device-level absorbers include transmons, BARs and SNSPD optical haloscopes [2212.03884, 2501.05504, 2110.01582].
Superconducting levitation [2310.18398] is a classical-force analogue.

---

## 8. Photon, scintillation, heat and quantum-sensor readouts

| # | Channel | Role | Key papers | Status | Experiments |
|---|---|---|---|---|---|
| R1 | Scintillation in crystals (GaAs, CsI, NaI) | e–h → photons | 1607.01009, 1802.09171, 2404.15741, 2507.07119 | M (light yields measured) | COSINUS, CRESST, GaAs R&D |
| R2 | Organic / liquid scintillator dark rates | sub-GeV | 1912.02822, 2512.13779 | M | — |
| R3 | Cherenkov / transition radiation | **backgrounds** in low-threshold detectors | 2011.13939 | M | — |
| R4 | Calorimetric (athermal phonons) | total-energy readout | 2408.04732, 2503.03683, 1904.00498 | M | TESSERACT, CRESST, SuperCDMS |
| R5 | Ionization yield / pair-creation energy | ER → N_eh map | 2004.10709 | M (phenomenological) | all CCD/HVeV |
| R6 | TES / KID / SNSPD / QPD / qubit readouts | meV thresholds | 2506.18982, 2506.10070, 2403.19739, 2607.19319, 1903.05101, 2405.17192, 2512.20309, 2405.00112, 2601.02474 | M | QROCODILE, QUALIPHIDE, transmon recasts |
| R7 | Phononic-crystal Ge transducer; vdW heterostructure sensors; Josephson junctions | meV | 2511.08329, 2603.15581, 2510.25203 | P/R&D | — |
| R8 | Halo-independent quantum-sensor analysis | low-v tail | 2606.25129 | M | — |

**Paragraph.** Cherenkov-like emission by *DM itself* was not found as a computed channel. Single-phonon emission
for v > c_s is kinematically Cherenkov-like but is treated as ordinary phonon production (§3). Cherenkov and
transition radiation from SM charged particles appear as low-energy backgrounds [2011.13939]. Recent work on the
low-energy excess and backgrounds is reviewed in [2503.08859].

---

## 9. Inelastic, exothermic and boosted DM

| # | Process | Key papers | Status |
|---|---|---|---|
| I1 | Exothermic DM (energy release Δ in NR/ER) | 1004.0937 | M |
| I2 | Inelastic DM, electromagnetic de-excitation signals | 2006.13918 | M |
| I3 | Inelastic DM–e scattering in atoms / SENSEI / Migdal | 2006.11938, 2203.06664, 2210.15474, 2112.06930 | M |
| I4 | Inelastic/exothermic DM into **collective modes** (phonons, magnons) | none found | NC |
| I5 | Boosted / solar-reflected DM in crystals (plasmon reach) | 2401.11971, 2501.07591, 2607.09352 | M |

**Paragraph.** Exothermic DM can deposit Δ even when it is slow, so it reaches sub-eV channels (phonons, magnons,
dopants) for very small m_χ. **I found no paper that computes exo/inelastic transitions into phonon or magnon
final states with DFT inputs** (gap).

---

## 10. Scalar couplings and wave-like DM in solids

Scalar couplings appear in four ways. (i) Absorption on electrons/phonons, with in-medium mixing [2006.13909,
2106.12586, 2308.06314]. (ii) Oscillating fundamental constants that strain the solid; classical acoustic
resonators [1508.01798, 2410.17308] and clocks [1405.2925]. (iii) Quadratic couplings scattering coherently off
density fluctuations in random media [2512.16451]. (iv) Scalar-nucleon Migdal-type absorption in atoms [2312.10566].
**No DFT calculation of scalar absorption beyond single phonons was found.**

---

## 11. Multi-step and composite processes

| Composite | Status | Refs |
|---|---|---|
| Phonon-mediated Migdal (DM–N → virtual phonon → e–h) | M | 2205.03395, 2310.05704 |
| Migdal + phonon final states | M | 2210.06490, 2603.13052, 2505.08864 |
| Phonon-assisted absorption (e–ph line) | M (metals, SC); data-driven (Si/Ge) | 1604.06800, 2106.12586, 1608.01994 |
| **Phonon-assisted electron *scattering* (DM–e × e–ph, indirect gap)** | **NC**: no calculation found; Si window m_χ ≈ 0.34–0.47 MeV per the survey's estimate | survey §4 |
| Plasmon-mediated ER (screening pole) | M/FP within RPA | 2101.08263, 2603.12326 |
| Exciton-mediated (BSE) ER | FP (Si/Ge only) | 2507.14345 |
| Exciton → scintillation (organics, QDs, GaAs) | M | 1912.02822, 2208.05967, 1802.09171 |
| Defect → stored energy → phonon deficit | M (MD) | 2112.14495 |
| Scattering + mediator absorption | M | 2501.09642 |
| Finite-T / zero-point lattice effects on ER thresholds | **NC** | survey §4 |
| Phonon-assisted exciton creation / indirect excitons | **NC** | — |

---

## 12. Gaps flagged (no computation found)

1. Phonon-assisted DM–electron **scattering** in indirect-gap semiconductors. A first-principles e–ph (EPW-like)
   treatment is absent, and it is the leading channel in the Si sub-MeV edge (survey estimate).
2. First-principles phonon-assisted **absorption** near the indirect gap (only data-driven exists).
3. Excitons beyond one BSE study: dark/indirect/Frenkel excitons in inorganic crystals, and exciton–phonon replicas.
4. NR bremsstrahlung in crystals (phonon-dressed), and exo/inelastic DM into collective modes.
5. DFT-level defect creation by electronic interactions. Colour-centre (NV/SiV) electronic transitions as DM–e
   final states.
6. Two-magnon / multi-magnon continua. Chiral optical response (CD) as a DM observable.
7. Finite-temperature and zero-point renormalization of production ER rates (every code uses a frozen lattice).

---

## 13. Verified arXiv IDs (all checked against the arXiv API, 2026-10-31)

Reviews/frameworks: 2108.03239 2203.07492 2203.08297 2209.07426 1707.04591 2209.08125 2607.06666 2503.08859
2407.14598 2105.02233 2402.06817 2510.25835 2110.01587 2501.18261 2608.05282 2507.11033 2608.20715 2403.07053
2512.18010 2408.04732 2608.06452.
Electronic: 1108.5383 1203.2531 1509.01598 1508.07361 2105.05253 2210.14917 2306.14944 2603.12326 2605.11063
2101.08275 2104.12786 2101.08263 2002.06937 2003.12077 2202.03436 2401.11971 2501.07591 2403.00123 2510.18338
2608.01305 2507.07164 2607.15338 2603.15581 2507.14345 1912.02822 2103.08601 2607.12036 2208.05967 2608.18204
1708.08929 1910.02091 1909.09170 2008.05062 2202.11716 2305.19967 1606.08849 1706.02487 2303.15497 2312.00866
2604.21969 2002.07821 1504.07237 1512.04533 2109.04473 2609.06423 2212.04504 1901.07569 2506.19905 2607.06005
2509.14534 2106.16214 2004.10709 2203.06664 2607.09352 2510.20889.
Lattice: 1712.06598 1807.10291 1910.08092 2009.13534 1905.05575 2008.08560 2502.01732 2409.02439 1911.03482
2205.02250 2011.09477 2309.10839 2412.18330 2607.24933 2506.11191 2411.03433 2606.04091 2301.07617 2511.20461
2603.22390 2512.16451 2303.02196 2102.10089 2405.10405 2506.03810.
Spin: 1905.13744 2210.13516 2501.18120 2005.10256 2001.10666 2411.11971 1606.02201 2001.08940 2504.16160 1807.08810
2102.05366 1306.6088 1306.6089 2101.01241 2609.07908 2411.10542 2504.02927 2601.01043 2102.10171.
Defects: 1703.05371 2112.14495 2301.06592 2512.23553 1705.03016 2104.13926 2503.20732 1705.09760 2009.01028
1806.05991 1811.06844 2106.06559 2301.07118 2604.09732 2606.02579 1608.02940.
Migdal/brems: 1707.07258 1711.09906 2208.12222 1908.10881 2011.09496 2210.06490 2603.13052 2505.08864 2606.14845
2205.03395 2310.05704 1912.13484 2011.13352 2604.26773 1607.01789 1905.00046 2312.10566 2210.04917 2307.12952
2606.03174.
Absorption/devices: 0807.3279 1412.8378 1608.02123 1608.01994 2106.12586 2303.11344 1604.06800 2308.06314 2209.12909
2305.05681 2212.03884 2412.20850 2311.07857 2501.05504 2410.17308 1905.12635 2308.00309 2405.05728 2507.14287
2109.08168 2501.09642 1611.05865 1612.07057 1904.11872 2509.14320 2606.13595 2505.17007 2204.11919 2110.01582
2310.18398 2006.13909 1508.01798 1405.2925.
Readout/experiments: 1607.01009 1802.09171 2404.15741 2507.07119 2512.13779 2011.13939 2503.03683 1904.00498
2506.18982 2506.10070 2403.19739 2607.19319 1903.05101 2110.01586 2412.16279 2405.17192 2512.20309 2405.00112
2601.02474 2511.08329 2510.25203 2606.25129 2004.11378 2312.13342 2302.02372 2503.14617 2407.08085 2509.03608
2005.14067 2003.01046 2310.05815 2507.17782.
Inelastic: 1004.0937 2006.13918 2006.11938 2112.06930 2210.15474.
