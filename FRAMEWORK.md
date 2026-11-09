# FRAMEWORK: work-package plan for the Unified Response Framework (URF)

Sector boundaries follow the expansion hierarchy. Every WP returns:
- (i) derivations from the WP0 master formula;
- (ii) its LIMITS.md entries, each derived with its approximation chain, validity conditions and leading
  correction;
- (iii) the gaps it closes (G-numbers from surveys/dm-solid-state-processes/README.md §4), each with a formula
  and a computation specification;
- (iv) the exact remaining gaps.

| WP | Sector | Gaps addressed | LIMITS entries |
|---|---|---|---|
| WP0 | **Architecture.** Coupled e–N–spin Hamiltonian; DM operator basis (NR-EFT, all coupling classes, absorption, inelastic); master rate formula via S_{OO′}(q,ω) at finite T; FDT, Kramers–Kronig, sum rules; screening at master level (proper versus improper response, external-field type); the expansion hierarchy with small parameters; notation | foundation for all | L0 (master), L-SR |
| WP1 | **Electronic sector, clamped nuclei.** IP → RPA → RPA+LFE → TDDFT/BSE (excitons, including dark/indirect); core and relativistic states; non-density operators in-medium; transverse response; plasmons; anisotropy | G5, G7, G10, G11 (electronic), exciton gaps | L1–L3, L10, L11, L14, L17 |
| WP2 | **Lattice sector.** Harmonic → anharmonic; single phonon → multiphonon → impulse; coherent/incoherent; polar couplings; anisotropy/modulation; NR spin couplings | G11 (lattice), G13 | L4–L6, L18, L19 |
| WP3 | **Mixed electron–lattice sector.** Non-adiabatic BO expansion unifying all Migdal versions, PAER (M1), phonon-assisted absorption, finite-T / zero-point renormalisation of electronic responses, crystal NR bremsstrahlung, exciton–phonon replicas; a consistent Migdal + multiphonon with sum rules, without double counting | G2, G6, (G5 excitons-phonon) | L7a–d, L8, L9, L9b, L12 |
| WP4 | **Spin, superconducting and special targets.** Magnons (one and two), chiral/CD responses; superconductors and thin films (BCS coherence, film ELF, branch cuts); Dirac/narrow-gap; dopants and colour centres as final states; exothermic DM into collective modes | G9, G12, catalog gaps | L13, L15, L16 |
| WP5 | **Energy partition and measured quanta.** Hot-carrier cascade (Boltzmann with ab initio e–ph and impact-ionization rates) seeded by the response's final-state distribution; NR partition (multiphonon + defects + charge; MD/BO surface); quasiparticle yield; Fano factor | G1, G3, G12 (defects) | L20–L23 |
| WP6 | **Rate assembly and uncertainty.** Halo and kinematics (SHM and halo-independent); shared conventions; nuisance-parameter structure for every approximation level; profile-likelihood propagation into exclusion bands | G4, G8 | L24 |

Order: WP0 first. WP1–WP6 then run in parallel on WP0's architecture. M1 (PAER: D1, D2, X1, X2) feeds WP3.
**Status (R16, CW8-A merge):** WP0–WP6 REFEREED (R7, v3); WP5 at v4 REFEREED (R14 WP5-AUD + R16 CW5). R16 closure packages CW2–CW7 (LOOSE-ENDS §2) CLAIMED + VERIFIED;
CW1 pending COMP-PH; M1 tier B: Si window [CALC] and rate/reach [E] (R15 COMP-PAER, CLAIMED); tier H FORMULATED.
**Final status (R17, CW8-FINAL merge, 2026-11-01):** WP0–WP6 REFEREED (WP5 at v4); WP7 (B1, B2, D, T, E) REFEREED (R12); closure packages **CW1–CW7 CLAIMED + VERIFIED**
(CW1 via VER-CW1 + CW1-errata); WP5-AUD, GAP-EF-v2 REFEREED (numbers read through GAP-EF-v3-errata, solver CROSS-CHECKED); WP8-R-v2 REFEREED; **WP8-U-v3, WP8-F-v3,
table v4 + WP8-errata, WP8-S-v2 + ranking_v3 VERIFIED** (VER-ERR-CW7, VER-ERR-WP8). COMP-PH (Si [CALC]; Ge FORMULATED), COMP-PAER, CMPMC-AUD/DEV CLAIMED. M1: tier B met
(Si window established, state/SOTA.md "R17 final state"); tier H FORMULATED (DEFERRED-COMPUTE DC-1). LOOSE-ENDS: no OPEN row (CLOSED 134, CLOSED-AS-EXACT-GAP 42, CANNOT-CLOSE 2
book-side). Every unrun computation is in state/DEFERRED-COMPUTE.md (Phase 2).
Each WP gets two isolated hostile referees. Synthesis (M4) comes after the referee rounds.

## Queued after R7 and the follow-up package (user, 2026-10-31)
- **WP7 follow-up package:**
  - the master-formula-only (B) catalog items: **WP7-B1 COMPLETE, WP7-B2 COMPLETE** (R12, REFEREED; LIMITS LB1-1…13, B2-L1…10);
  - the reachable D extensions (fermionic absorption, the coherent classical-field regime): **WP7-D COMPLETE** (R12, REFEREED; LIMITS L-D1…12);
  - low-T defect quantum kinetics: crowdions, defectons, tunnelling two-level systems: **WP7-T COMPLETE** (R12, REFEREED; LIMITS L25–L32).
  - **WP7-E: energy-partition reconciliation** (user question, 2026-10-31): **COMPLETE** (R12, REFEREED; LIMITS L33–L38; amendment to WP5 → R13 WP5-ERR, then the joint WP5 + WP7 audit and R×2 below). One time-resolved balance
    law per event:
    - **Budget:** E_dep = E_pairs·(pair channel) + Q_prompt (athermal phonons) + E_stored(t) (defects and
      TLS) + E_esc (photons, escaping phonons) + E_sensor-loss, with E_stored(t) relaxed by the WP7
      kinetics into a delayed-release spectrum.
    - **Consistency conditions with WP5:**
      - E_d is not counted twice: the displacement energy enters WP5's partition once, and WP7 decides
        only its time profile;
      - the yield models are applied to the electronic share only;
      - charge trapping on defect levels is shared between the yield and the detector response.
    - **Mapping to observables:** charge Q (with trapping and release), prompt heat, delayed events, and
      the low-energy-excess model.
    - **Literature:** Lindhard, R&K and measured quenching data are shown as limits that implicitly fold
      in specific defect assumptions.
    - **Output:** a WP5 v3 amendment, plus a joint WP5 + WP7 audit and R×2 referee step before WP8 uses
      the yields.
    - **Status (R16, CW8-A merge):** amendment applied (R13 WP5-v4); joint audit R14 WP5-AUD, R×2 (REF-WP5-AUD-A/B) settled in R16 CW5 §1: **WP5-AUD and WP5-v4
      REFEREED** (WP5-v4 read through state/CORRECTIONS.md §19.5). Yield rows released to WP8. ε_eh/F_eh cascade theory: R16 GAP-EF-v2, REFEREED.
- **WP8 purpose (user, 2026-11-01):** "I think this is more valuable because we want to help experimentalists identify where the next future experiment target might lie". WP8-S is a forward-looking guide: per channel, the materials that would lead a next-generation experiment, and for each the specific demonstration still missing (crystal mass or array, readout, radiopurity, a measured property). Current-capability screening is a column, not a filter.
- **WP8 figures of merit and material selection.** **Status (R16, CW8-A merge):** WP8-U-v3 (+ table v4) and WP8-F-v3 supersede R13/R16-v2, REFEREED at their R14
  content (R14 R×2 + VER-CW7), ERR-CW7 additions CLAIMED (R×2 owed, IF-ERR7-6); WP8-R-v2 supersedes R13 WP8-R, REFEREED (R14 R×2 + VER-CW6). ~~**WP8-S ranking: not final**
  (CW7 §12 synthesis under revision; REF-WP8-S-A/B; R×2 owed).~~ **R17: WP8-S-v2 + WP8-errata (ranking_v3) and the ERR-CW7 additions VERIFIED** (VER-ERR-CW7, VER-ERR-WP8,
  0 FALLS); next-target guide headline in state/SOTA.md "R17 final state". LIMITS L39–L42, L-F1–L-F4, LU/LT rows merged; R17: L-S1–L-S3, L-EW1.
  - For each interaction channel (excitation × DM interaction cell of the atlas), derive figures of merit
    from the refereed framework: the material properties that control sensitivity (rate per target mass at
    fixed coupling, threshold and reach edge, screening suppression, background-relevant quantities), with
    their scaling.
  - Then rank materials within the pickable universe. A material qualifies if it:
    1. survives repeated thermal cycling to mK and back (no phase transitions, cracking or delamination
       within the operating cycle);
    2. can be synthesised at ≥ gram scale with the needed purity;
    3. can carry sensors: TES, KID, SNSPD or charge readout can be fabricated on its surface, or another
       demonstrated readout exists.
  - Material properties come from the literature and databases (with provenance). New first-principles
    numerics remain on hold unless the user authorises them.
  - Deliverables: an FOM table per channel, the screened candidate list per channel with its reasons, and
    sensitivity of each ranking to the theory uncertainties.
- WP8 data source: the user dropped Materials Project (2026-10-31); use open sources (Materials Project OPTIMADE, JARVIS-DFT, literature) with provenance. Superseded note follows:
  - From this container the web app (next-gen.materialsproject.org) returns 403.
  - The REST API (api.materialsproject.org) is reachable but needs an API key, read from the environment
    variable MP_API_KEY.
  - Until a key is available: other open sources (OPTIMADE endpoints, JARVIS, literature values) with
    provenance, and MP-dependent rows marked pending.
- **WP8-R: mode-selective phonon collection as an NR/ER discriminant** (user, 2026-10-31). The question is
  whether substrate–sensor interfaces with mode- and angle-dependent phonon transmission (acoustic and
  diffuse mismatch; film choice, e.g. Al/W/Ti-based TES/QET) give useful NR/ER discrimination. It rests on
  the different initial phonon mode and frequency mix of nuclear and electron recoils, propagated through
  anharmonic down-conversion, isotope scattering and focusing to the sensors.
  - Figure of merit: the discrimination power, e.g. the separation of a mode-ratio observable in units of
    its event-by-event spread, after the full chain, for candidate substrate–film pairs.
  - **Go/no-go:** run first as a cheap order-of-magnitude screen. If the discrimination after the chain is
    minor (e.g. separation ≲ 1σ, or below existing ionization/timing discrimination), DROP the thread and
    record why. Pursue it further only if the effect is large.
  - No directionality claim.
  - **Status (R16):** go/no-go screen done (WP8-R-v2, REFEREED): NO-GO for mode/frequency/angle selection of prompt populations in bulk Si/Ge; HV (c) CONDITIONAL NO-GO
    at E_R ≤ 300 eV; zero-field gap-energy channel (b) UNRESOLVED (release law and site, G-R2); low-bias NTL route (d) CONDITIONAL. Thread not pursued further beyond the
    exact gaps G-R1…G-R6 (state/SOTA.md R14–R16 block).
