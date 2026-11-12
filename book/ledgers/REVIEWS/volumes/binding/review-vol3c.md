# Binding review, block vol3c (ch29, ch30)

Reviewer: independent, after BINDING-REVIEW.md. Base 60cc72c. Files: tex/ch29/{E-11,E-12,E-13,ch29}.tex, tex/ch30/{E-17,E-19,E-20,E-21,E-22,ch30}.tex (none marked generated). The diff was read sentence by sentence and every file was read whole before the editors' log was opened.

## Verdict

| file | changed sentences checked | accepted | fixed | reverted |
|---|---|---|---|---|
| E-11 | 26 | 22 | 4 | 0 |
| E-12 | 19 | 19 | 0 | 0 |
| E-13 | 23 | 22 | 1 | 0 |
| ch29 (intro, Summary) | 3 | 2 | 1 | 0 |
| ch30 (intro, Summary) | 4 | 3 | 1 | 0 |
| E-17 | 21 | 20 | 1 | 0 |
| E-19 | 18 | 17 | 1 | 0 |
| E-20 | 21 | 20 | 1 | 0 |
| E-21 | 11 | 11 | 0 | 0 |
| E-22 | 19 | 19 | 0 | 0 |
| **total** | **165** | **155** | **10** | **0** |

The editors' work is sound. The changes I checked against sources hold up: E-11:18 ("Zero-point motion does set the width of the threshold step") matches s19-1 (σ_ω sets the 0.7 eV width), and E-11:76 now uses the p_FP ≥ 1/2 threshold of \cref{eq:19.1-Ed}, which needed only its arguments (row below). The fixes below are one fidelity slip, two places (E-11:76 and the ch29 Summary) where E_d could be read as a direction-averaged median threshold, and register repairs (robotic repetition).

## Fixes to editor sentences

| file:line | editor text | my text | reason |
|---|---|---|---|
| E-11:18 | "Two approximations come with the adiabatic limit." | "Two approximations come with \cref{eq:E.11-newton}." | Fidelity. The base "it" was Eq. (E.11-newton), the subject of the previous sentence. Classical nuclei is an approximation of Newton's equations and not of the adiabatic limit, so the editor's name gave the wrong referent for the first of the two approximations. |
| E-11:76 | "…E_d(r̂_R) is quoted as the lowest recoil energy at which p_FP reaches one half (\cref{eq:19.1-Ed})." | "…at which p_FP(E_R, r̂_R) reaches one half (\cref{eq:19.1-Ed})." | Binding and fidelity. Two sentences earlier the paragraph defines a bare p_FP(E_R) as the fraction of directions with a surviving defect, so the bare symbol had two antecedents and could be read as a median threshold. The arguments make the per-direction definition of eq:19.1-Ed explicit, and the expression was already in the file. |
| E-11:68 | "Moving 0.05 Å per step means 0.19 fs at 100 eV…" | "A limit of 0.05 Å per step means steps of 0.19 fs at 100 eV…" | The gerund subject read as "moving 0.05 Å means 0.19 fs" (a distance equated with a time). |
| E-11:70 | "…without reflecting back from the thermostat as a coherent pulse; a border that is too thin or too stiff reflects the heat back as a coherent pulse." | "…without a coherent pulse reflecting back from the thermostat, and a border that is too thin or too stiff produces the reflected pulse." | Over-repair: the editor repeated the whole predicate. |
| E-13:77 | "…the calculation needs a relative error of 1.7 % on the sample variance. The calculation therefore needs N_casc ≈ …" | "… A relative error of 1.7 % therefore takes N_casc ≈ …" | Robotic repetition ("The calculation … needs" twice). |
| ch29 Summary:11 | "The displacement threshold is the lowest recoil energy at which the defect probability, scanned over more than 1000 directions, reaches one half, and the stored energy is read after a quench…" | "The displacement threshold is scanned over more than 1000 directions, and along each direction it is the lowest recoil energy at which the defect probability reaches one half. The stored energy is read after a quench…" | Fidelity. The editor's version reads as a threshold where the probability *averaged over directions* reaches 1/2, which would be a median threshold. Eq. (19.1-Ed) and E-11:76 define E_d(r̂) direction by direction. I also split the sentence, which was over 45 words. |
| ch30 Summary:13 | "For tunneling defects and two-level systems, the parameters have not been computed …; they range from the ohmic coupling … to …" | "The parameters of tunneling defects and two-level systems range from the ohmic coupling and the release paths to the density vertex and the distribution of two-level parameters, and they have not been computed for a real material at the level the rates need." | "the parameters" was used as a definite before it was introduced, and the list came only after the claim. |
| E-17:80 | "The thermal contraction from 300 K … stores elastic energy … The integrated contraction comes from …" | "… The thermal contraction comes from …" | Two names for one object. |
| E-19:11 | "…checks at 1/4 and 1; damping only the internal modes preserves the exact limits…; the centroid is not thermostatted…" | "…checks at 1/4 and 1. Damping only the internal modes preserves the exact limits…; the centroid is not thermostatted…" | Three semicolon clauses in a row. The split gives a sentence that opens on a named noun. |
| E-20:51 | "…no controlled method exists at α̃ of order one, so at α̃ of order one the BSE stage gives only an estimate…" | "…no controlled method exists at α̃ of order one, where the BSE stage gives only an estimate…" | The same qualifier repeated inside one sentence. The editor's reading of "that stage" as the BSE stage is kept. |

## Recall (untouched text)

I read every paragraph the editors did not change, in every file, including the table cells: about 7,400 words in ch29 and 12,700 words in ch30 (prose words minus changed sentences). Pattern-27 failures I found and fixed:

| file:line | base text | my text | failure |
|---|---|---|---|
| E-12:87 | "A 10 keV deposit in silicon that has down-converted to 1 THz phonons (4.1 meV) holds 2.4×10^6 phonons." | "A 10 keV deposit in silicon holds 2.4×10^6 phonons once it has down-converted to 1 THz phonons (4.1 meV)." | left-heavy subject with a relative clause |
| E-13:21 | "brings the gap to experiment and the other tabulated conduction-band energies … to within 0.2 eV" | "brings the gap to experiment and puts the other tabulated conduction-band energies … within 0.2 eV" | coordination scope (read "to experiment and the other energies") |
| E-13:23 | "The number of bands below an energy E above the band bottom is about…" | "Below an energy E above the band bottom, the number of bands is about…" | PP chain in a heavy subject |
| E-17:23 | "At long wavelength its ℓ = 4 component in silicon…" | "At long wavelength the ℓ = 4 component of the one-phonon term in silicon…" | *its* has two candidates (the anisotropy, the one-phonon term). s11-7.tex:75 assigns S_4/S_0 = 0.028 to the one-phonon weight. |
| E-17:29 | "The relativistic density averaged over the finite nucleus raises…" | "The relativistic density, averaged over the finite nucleus, raises…" | garden path through a reduced relative. The commas close the relative clause; a gerund rewrite would have made the averaging the cause of the rise. |
| E-17:39 | "The test comes first: the same calculation with room-temperature occupations, sum and difference processes, and quasi-harmonic frequencies reproduces…" | "The test comes first: with room-temperature occupations, sum and difference processes, and quasi-harmonic frequencies, the same calculation reproduces…" | left-heavy subject |
| E-20:7 | "We want its vertex fraction 𝔳" | "We want the vertex fraction 𝔳 of the conserving response" | *its* has three candidates (response, phase-mode term, bubble) |
| E-21:9 | "DFT on 1000- to 4000-atom silicon clusters with two to four phosphorus atoms, at the shared 60 Ry setting of \cref{app:E.17}, checks the central-cell part for about 10^4 more." | "The central-cell part is checked, for about 10^4 more, by DFT on 1000- to 4000-atom silicon clusters…" | left-heavy subject |
| E-21:40 | "tagged neutron scattering on LiF at 10 mK followed by single-center optical readout measures…" | "…at 10 mK, followed by single-center optical readout, measures…" | reduced relative inside a heavy subject |
| E-21:46 | "The photodissociation quantum yield of the same molecular crystal at millikelvin, with fragments detected by infrared absorption, measures p_esc." | "p_esc is measured by the photodissociation quantum yield of the same molecular crystal at millikelvin, with fragments detected by infrared absorption." | left-heavy subject |
| E-22:11 | "The many-electron ground states of the two configurations in a cell of size L overlap as…" | "In a cell of size L the many-electron ground states of the two configurations overlap as…" | PP chain in the subject |
| E-22:58 | "The two-level systems that matter, with asymmetries below a meV and tunneling exponents below about 20, are rare among pairs of neighboring minima." | "The two-level systems that matter are rare among pairs of neighboring minima: they have asymmetries below a meV and tunneling exponents below about 20." | heavy subject with an apposition |

Misses per 1000 words: **ch29 3 / 7.4k = 0.4**; **ch30 9 / 12.7k = 0.7**. These counts exclude the three open items below. Both chapters are below 2 per 1000 words, so neither needs a second pass.

## Open items

OPEN.md has no entries for ch29 or ch30. The editors' log lists three unresolved items:

- **E-17:43 "a Cauchy–Schwarz bound on the same spectral sums"**: fixed. The definite *the same* had no antecedent in the section. New text: "a Cauchy--Schwarz bound on the spectral sums behind this expansion", where *this expansion* is the small-ω expansion of $Z^*_\kappa(\omega)$ in the same sentence. The new wording says nothing new about what the sums are. `git log --follow -S` shows the phrase already in the first commit (7696d03), with no earlier antecedent.
- **E-21:9 "The Bloch functions at the conduction minima, on the same grid"**: stays, and goes to the lead. The paragraph mentions no grid. The only grid in reach is the shared silicon base of \cref{app:E.17} ($12^3$ $\vect{k}$ grid), which the previous sentence points to only through its "60 Ry setting". Writing that grid in would add a claim I cannot verify. `git log --follow -S` shows the same sentence in the first commit (7696d03), with no grid in the paragraph then either. Proposed wording, if the author confirms: "The Bloch functions at the conduction minima, from the shared silicon base of \cref{app:E.17}, also give…".
- **E-12:69 "The four or six mean free paths"**: stays as wording and goes to errata (below), because it is a factual inconsistency.

## Proposed errata

1. **E-12:69 (tex/ch29/E-12.tex, Carrier transport, third paragraph).**
   Old: "Impurities enter as two processes, each with a mean free path that is fitted to the device. … The four or six mean free paths are fitted to the shape of these regions~\cite[Fig.~6]{kelsey2023g4cmp}."
   Proposed: "Impurities enter as two processes, with mean free paths that are fitted to the device. … G4CMP uses six mean free paths, two for the trapping of electrons and holes and four for impact ionization by electrons or holes, and fits them to the shape of these regions~\cite[Sect.~2.3 and Fig.~6]{kelsey2023g4cmp}."
   Reason: "each with a mean free path" (two in total) contradicts "four or six". The source (sources/review-appE/2302.05998/text.txt, near the paragraph that introduces Fig. 6) says: "In total, G4CMP uses six parameters to model this behavior, corresponding to two mean free paths for electron or hole trapping … and four mean free paths for either electrons or holes to produce an additional electron or hole via impact ionization." The quoted passage is in Sect. 2.3 (Charge transport) of the source.

## Checks

- `tools/invariant.py 60cc72c` on all ten files: 0 STOP. The notes are repeat counts and the added \cref to eq:E.11-newton, eq:19.1-Ed, eq:E.12-iso and sec:4.2 (all existing labels).
- lint: 0 blocking hits. The LONG-SENT hits are table environments and sentences the editors left unchanged; the one in the ch29 Summary that my first fix created was split.
- `tools/chapcheck.sh ch29` and `ch30`: exit 0, 0 undefined references, 0 multiply defined labels. ch29 has one overfull hbox (18.7 pt) in the untouched table tab:E-cascade-si, which predates this round.
