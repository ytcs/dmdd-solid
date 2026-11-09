# Dark matter scattering in solid-state targets: where the theory stands (Oct 2026)

Scope: light (keV–GeV) dark matter (DM) that deposits energy in crystals, through electron recoils (ER), nuclear recoils (NR) and collective modes (phonons, plasmons, magnons). The last section answers a narrow question: **has phonon-assisted ER been calculated?**

The arXiv IDs below were checked against the arXiv API. Statements about what a paper does *not* contain come from abstracts, targeted searches and, where noted, full-text reads. They are not an exhaustive literature audit.

---

## 1. Electron recoil (ER)

### 1.1 Lineage
| Stage | Key works | What it added |
|---|---|---|
| Proposal | Essig, Mardon, Volansky [1108.5383]; Graham, Kaplan, Rajendran, Walters [1203.2531] | Semiconductor ER for sub-GeV DM; the crystal form factor \(f_{\rm crys}(q,\omega)\) |
| First DFT rates | Essig et al. (QEdark) [1509.01598]; Lee, Lisanti, Mishra-Sharma, Safdi [1508.07361] | Si/Ge Bloch states from Quantum ESPRESSO; daily modulation |
| Extended DFT / all-electron | Griffin, Inzani, Trickle, Zhang, Zurek [2105.05253]; Trickle, EXCEED-DM [2210.14917]; Dreyer, Essig, Fernandez-Serra, Singal, Zhen (QCDark) [2306.14944] | Core and semicore states, all-electron reconstruction, large-q convergence, systematic DFT uncertainties |
| General couplings (NR-EFT) | Catena, Emken, Matas, Spaldin, Urdshals [2105.02233]; Trickle, Zhang, Zurek [2009.13534]; Catena & Spaldin, linear response [2402.06817] | Beyond \(\bar\chi\chi\bar e e\): spin and velocity-dependent operators, several crystal response functions |
| In-medium screening / dielectric | Knapen, Kozaczuk, Lin [2101.08275] and DarkELF [2104.12786]; Hochberg, Kahn, Kurinsky, Lehmann, Yu, Berggren [2101.08263] | For density coupling, the rate is \(\propto {\rm Im}[-1/\epsilon(q,\omega)]\) (ELF); screening; plasmons. Kurinsky et al. [2002.06937], Kozaczuk & Lin [2003.12077] |
| Sum rules & bounds | Lasenby & Prabhu [2110.01587]; Catena & Iglicki [2501.18261]; Barker, Epstein, James, Kahn, Peterson, Prabhu [2608.05282] | Material-agnostic upper bounds on the ER rate from f-sum and related sum rules |
| Beyond DFT-RPA | Taufertshöfer, Zema, Catena, Olevano, Spaldin [2507.14345] | Excitons (Bethe–Salpeter equation, BSE): the rate rises at ω ~ E_g |
| All-electron + RPA local fields | Dreyer, Essig et al. [2603.12326] (2026) | Current state of the art for Si/Ge. Full text checked: T = 0 Kohn–Sham states, electronic response only. Phonons enter only through a phenomenological ionization-yield model |
| Spin-dependent & data-driven | Hochberg, Khalaf, Lenoci, Ovadia [2510.25835] | A "master formula" that writes every DM–e operator in terms of measurable response functions |
| Screening of materials | Griffin, Hochberg, Lehmann, Ovadia, Persson, Suter [2506.19905] | High-throughput ELF-based ranking of target materials |
| Anisotropy / modulation | Al-Adulrazzaq, Settembri, Sassi, Giannessi, Profeta, Heikinheimo, Tuominen [2607.06005] | Anisotropic ELF; daily modulation of ER and Migdal rates in Si, GaAs |
| Bound-state kinematics | Ge, Sheng, Xing [2509.14534] | Questions the factorized "free-electron × form factor" ansatz (atoms; relevant to core levels) |

### 1.2 State of the art in brief
- **Production tools:** QEdark/QCDark (Essig group), EXCEED-DM (Trickle et al.), DarkELF (Knapen–Kozaczuk–Lin). Their Si results agree to O(1) once screening and all-electron corrections are applied. Remaining differences come from the exchange-correlation functional, the scissor correction, the q-cutoff and local-field effects.
- **Open systematics:** excitons and local fields (BSE, beyond RPA); the frozen-lattice approximation, i.e. every production ER calculation uses clamped nuclei at T=0; anisotropy; and a consistent treatment of non-density operators in-medium.

## 2. Nuclear recoil (NR) and phonons

| Regime | Key works | Notes |
|---|---|---|
| Single optical/acoustic phonon | Knapen, Lin, Pyle, Zurek [1712.06598]; Griffin, Knapen, Lin, Zurek [1807.10291]; Trickle, Zhang, Zurek, Inzani, Griffin [1910.08092]; Cox, Melia, Rajendran [1905.05575]; SiC study [2008.08560] | DFT phonons (phonopy), Born effective charges for dark-photon mediators; directional signals. Code: PhonoDark |
| Multiphonon → free NR | Campbell-Deem, Cox, Knapen, Lin, Melia [1911.03482]; Campbell-Deem, Knapen, Lin, Villarama [2205.02250]; Kahn, Krnjaic, Mandava [2011.09477] | Incoherent approximation; the dynamic structure factor interpolates from one phonon to impulse NR |
| Anharmonicity | Lin, Shen, Sholapurkar, Villarama [2309.10839] | Up to ~10² rate change at m_χ ~ MeV; negligible above ~10 MeV |
| Daily modulation | Stratman & Lin [2411.03433] | 1–10 % modulation in Al₂O₃ for m_χ < 30 MeV (harmonic, isotropic approximation) |
| Magnons / absorption on phonons | Trickle, Zhang, Zurek [1905.13744]; Mitridate, Pardo, Trickle, Zurek [2308.06314] | Spin-coupled DM; single-phonon absorption EFT |

## 3. Mixed channel: Migdal effect in crystals (NR → electronic excitation)
- Isolated-atom Migdal: Ibe, Nakano, Shoji, Suzuki [1707.07258]. Its relation to ER in semiconductors: Essig, Pradler, Sholapurkar, Yu [1908.10881].
- **Semiconductors via the ELF:** Knapen, Kozaczuk, Lin [2011.09496]. The Migdal rate is the ELF evaluated at the momentum the recoiling ion "kicks" into the electron gas. This is valid for m_χ ≳ tens of MeV, i.e. the impulse regime.
- **Small-q Migdal, where the nuclear final state is phonons:** Berghaus, Esposito, Essig, Sholapurkar [2210.06490] (EFT; the rate is fixed by the measured dynamic structure factor and ELF), extended to NR-EFT operators by Berghaus, Essig, McDuffie [2603.13052]. Esposito & Rocchi [2505.08864] show from a systematic Born–Oppenheimer expansion that the crystal Migdal effect is *entirely non-adiabatic*, reproducing the EFT result. See also Nellen Mondragón, Pradler, Sholapurkar [2606.14845] (adiabatic-response regime) and the tight-binding / bremsstrahlung treatments by Liang et al. [1912.13484, 2011.13352].
- **Phonon-mediated Migdal:** Liang, Mo, Zheng, Zhang [2205.03395] (PRD 106, 043004). DM excites multiphonons, and a valence electron crosses the gap by exchanging a *virtual phonon* through electron–phonon coupling. This extends Migdal reach down to ~MeV masses. Li & Xia [2310.05704] apply the same framework to CEvNS.
- Reviews: Kahn & Lin [2108.03239]; Mitridate, Trickle, Zhang, Zurek (Snowmass) [2203.07492].

## 4. Has phonon-assisted ER been calculated?

The answer depends on which process "phonon-assisted ER" means.

| Process | Status |
|---|---|
| **(a) DM couples to nuclei/ions, electron excited via e–ph coupling or non-adiabatic coupling** (phonon-mediated / small-q Migdal) | **Done, several ways:** Liang et al. 2022 [2205.03395] (virtual phonon, incoherent approximation, phenomenological e–ph vertex; CEvNS version [2310.05704]); Berghaus et al. [2210.06490, 2603.13052] (EFT with phonon final states); Esposito & Rocchi [2505.08864] (Born–Oppenheimer: purely non-adiabatic). |
| **(b) Absorption of bosonic DM (dark photon, ALP, scalar) with phonon emission** | **Done, with caveats.** Metals and superconductors: two-loop self-energy with an explicit e–ph line [Hochberg, Lin, Zurek 1604.06800; Mitridate, Trickle, Zhang, Zurek 2106.12586, App. A.3], using a deformation-potential model fitted to resistivity. Si/Ge near the indirect gap: only *data-driven*, from the measured optical conductivity, which already contains the phonon-assisted absorption [Hochberg, Lin, Zurek 1608.01994]. No first-principles (EPW-style) DM absorption calculation was found. |
| **(c) DM couples to electrons in scattering; the interband transition is completed by phonon emission or absorption** (second order: DM–e vertex × e–ph vertex, i.e. the scattering analogue of indirect optical absorption) | **I found no calculation**, phenomenological or first-principles. The searches covered arXiv full-text queries ("phonon-assisted" + "dark matter", "electron-phonon" + "dark matter"), web searches, and the ER papers above. Every production ER code computes first-order transitions in a frozen lattice. Data-driven ELF methods include phonon-assisted pieces only implicitly, in the q→0 optical limit. |

### Why (c) has been neglected, and where it could still matter (my estimate)
In scattering, the DM supplies momentum q ~ keV, which is comparable to the Brillouin-zone size (2π/a ≈ 2.3 keV in Si). Indirect transitions are therefore already allowed at first order, and the phonon-assisted term is a higher-order correction. Optical data suggest a suppression of roughly 10⁻³–10⁻⁴: indirect versus direct absorption coefficients. The exception is the **kinematic edge**. Reaching the conduction-band minimum at k_c directly requires
\(q \ge k_c\) and \(q v - q^2/2m_\chi \ge E_g\). A phonon instead carries the ~2 keV of crystal momentum at an energy cost of ħΩ ≲ 60 meV:

| Target | k_c | m_χ,min (first-order, to CBM) | m_χ,min (phonon-assisted) | m_χ,min (vertical direct gap) |
|---|---|---|---|---|
| Si (X valley, E_g = 1.12 eV, E_dir ≈ 3.4 eV) | 1.94 keV | ≈ 0.47 MeV | ≈ 0.34 MeV | ≈ 0.97 MeV |
| Ge (L valley, E_g = 0.67 eV, E_Γ = 0.80 eV) | 1.90 keV | ≈ 0.41 MeV | ≈ 0.20 MeV | ≈ 0.23 MeV |

(Assumes v_max = v_esc + v_E ≈ 794 km/s and a T ≈ 0 detector, so only phonon emission is possible.)

**Implications**
1. **Silicon has an open window, m_χ ≈ 0.34–0.47 MeV**, where first-order ER is kinematically closed at threshold and phonon-assisted ER is the leading channel. In Ge the window nearly closes, because the direct Γ gap sits only 0.13 eV above the indirect gap.
2. **The light-mediator enhancement partly offsets the e–ph suppression.** For F_DM ∝ 1/q², the rate scales as 1/q⁴. Phonon-assisted transitions can use q ~ ω/v ~ 0.4 keV instead of q ≥ 2 keV, which buys a factor of up to ~10²–10³ against the e–ph cost.
3. A further consistency issue appears even above the window. Scissor-corrected DFT rates use the *experimental* gap, which includes zero-point renormalization (≈ −60 meV in Si). Matrix elements, broadening and lattice polarization stay in the clamped-nucleus limit. A first-principles e–ph treatment, for example Wannier interpolation as in EPW applied to the DM–e vertex, would fix the threshold region systematically.
4. The sum-rule bounds [2110.01587, 2501.18261, 2608.05282] still apply. Phonon-assisted spectral weight is part of the same f-sum, so it cannot exceed those bounds.

### Search log for (c), Oct 2026
All searches ran through the repo's `skills/breakthrough-maths/scripts/lit.py` unless marked otherwise.
- `lit.py arxiv` (title+abstract, 2–4 terms, 17 queries): "phonon-assisted dark matter" (5 hits, none DM-theory), "dark matter indirect gap", "electron-phonon dark matter" (hep-ph; cond-mat.mtrl-sci → 1 irrelevant hit), "Migdal semiconductor phonon", "dark matter electron scattering phonon" (hep-ph), "dark matter absorption semiconductor", "dark matter electron scattering temperature", "Migdal crystal dark matter", "dark matter polaron", "dark matter intervalley", "dark matter Wannier", "dark matter electronic excitation phonon", "dark matter vibronic", "sub-MeV dark matter electron semiconductor", and raw `abs:"dark matter" AND abs:"electron-phonon coupling"` / `AND abs:"second-order" AND abs:phonon`. No hit computes (c).
- `lit.py works` (Crossref; OpenAlex and Semantic Scholar were rate-limited, HTTP 429), 3 queries: nothing relevant. `lit.py theses` (HAL/TEL): 0 hits. `lit.py theorems`: the corpus is mathematics, so no relevant hits, as expected.
- Citation walk (INSPIRE-HEP API, outside lit.py, used because OpenAlex was rate-limited): all 791 unique papers citing 1608.01994, 2205.03395, 2210.06490, 2011.09496, 2101.08263, 2101.08275, 2105.05253, 2306.14944, 2106.12586 and 1509.01598. Abstracts were grepped for phonon-assisted / indirect transition / electron-phonon / virtual phonon / second order / gap renormalization / polaron / vibronic. The only DM–solid-state hit was 2205.03395 itself, which is process (a).
- Full text fetched with `lit.py fetch` and read for 2106.12586, 2505.08864, 2606.14845, 2604.26773, 2603.12326, 2607.24933. None treats (c).

**Bottom line:** phonon-assisted electronic excitation exists in the DM literature as (a) phonon-mediated / non-adiabatic Migdal and (b) absorption, the latter treated phenomenologically or from optical data. I could not find a calculation of (c), DM–electron *scattering* completed by phonon emission in an indirect-gap semiconductor, from first principles or otherwise. It appears to be an open, well-defined problem. Its natural niche is the sub-MeV kinematic edge of Si and the light-mediator, threshold-dominated region.

---
### Main references (arXiv)
1108.5383 · 1203.2531 · 1509.01598 · 1508.07361 · 2105.05253 · 2210.14917 · 2306.14944 · 2105.02233 · 2009.13534 · 2402.06817 · 2101.08275 · 2104.12786 · 2101.08263 · 2002.06937 · 2003.12077 · 2110.01587 · 2501.18261 · 2608.05282 · 2507.14345 · 2510.25835 · 2506.19905 · 2607.06005 · 2509.14534 · 1712.06598 · 1807.10291 · 1910.08092 · 1905.05575 · 2008.08560 · 1911.03482 · 2205.02250 · 2011.09477 · 2309.10839 · 2411.03433 · 1905.13744 · 2308.06314 · 1707.07258 · 1908.10881 · 2011.09496 · 2205.03395 · 2310.05704 · 2210.06490 · 2603.13052 · 2505.08864 · 2606.14845 · 1912.13484 · 2011.13352 · 2603.12326 · 1608.01994 · 1604.06800 · 1512.04533 · 2106.12586 · 2108.03239 · 2203.07492
