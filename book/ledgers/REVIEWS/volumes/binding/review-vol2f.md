# Binding round: independent review of block vol2f (ch20)

Reviewer: independent hostile review (BINDING-REVIEW.md). Files: tex/ch20/ch20.tex, s20-1 to s20-5, s20-summary (none marked generated). Base 60cc72c. Every changed sentence was read against its base sentence (sentence-aligned diff), and every file was read whole, with the editor log consulted only afterwards for its stated readings.

## Verdict

| File | Changed sentences checked | Accepted | Fixed | Reverted |
|---|---|---|---|---|
| ch20.tex | 7 | 7 | 0 | 0 |
| s20-1.tex | 66 | 64 | 2 | 0 |
| s20-2.tex | 46 | 45 | 1 | 0 |
| s20-3.tex | 28 | 28 | 0 | 0 |
| s20-4.tex | 50 | 49 | 1 | 0 |
| s20-5.tex | 54 | 50 | 4 | 0 |
| s20-summary.tex | 4 | 3 | 1 | 0 |
| **Total** | **255** | **246** | **9** | **0** |

Overall the edit is faithful: no qualifier, number or validity condition was lost, and the new names (read charge, crystal thickness, quasiparticle yield, memory time, the named loss effects) are used consistently. One editor sentence introduced a physics slip (s20-5:63, "above the gap" for "above the threshold"); it is fixed below.

## Fixes to editor text

| file:line | editor text | my text | reason |
|---|---|---|---|
| s20-1:14 | Let the electrode at $z=d$ collect electrons (the anode), so that | Let the electrode at $z=d$, the anode, collect electrons, so that | the parenthesis attached "the anode" to *electrons* |
| s20-1:150 | The average over the angular distribution, in which $u$ … is weighted by $u^2$ … and so has the mean …, gives | In the angular distribution, $u$ … is weighted by $u^2$ … and so has the mean … . Averaging the phonon energy over the angular distribution gives | editor replaced a dangling modifier with a left-heavy subject containing a relative clause |
| s20-2:116 | since $E_*\propto t^{-1/5}$ the memory time grows as | … the time until a birth is forgotten, the memory time, grows as | definite before introduction (editor's own intended introduction point) |
| s20-4:111 | the ratio $\rho_g$ of \cref{sec:19.5}, which divides the collection efficiency of … by … | the ratio $\rho_g$ of \cref{sec:19.5}, the collection efficiency of the recombination phonons divided by the collection efficiency of the hard primaries | *which* had two candidates ($\rho_g$, sec. 19.5); "divides" reads as a process |
| s20-5:44 | After its first pair break, a film emits relaxation phonons and hot phonons that escape; | After the first pair break in a film, the film emits relaxation phonons and lets hot phonons escape; | cataphoric *its* before its antecedent; scope of "that escape" |
| s20-5:63 | The sub-gap loss and the conversion between two and four gaps act alone | The sub-gap loss and the energy dependence of the yield act alone | too narrow: the single-film formula \cref{eq:20.5-sign} carries $s_{\mathrm{ng}}$, which integrates the yield over all energies above threshold (the text itself cites the cascade yield between 5 and $8\Delta$); "energy dependence of the yield" is the s20-4:103 term |
| s20-5:63 | absorbed at the same rate as phonons above the gap | … as phonons above the threshold | physics slip introduced by the edit: "the gap" is $\Delta_{\mathrm{BCS}}$, sub-gap phonons lie between $\Delta$ and $2\Delta$ too; the comparison set is phonons above $2\Delta$ (base "the others") |
| s20-5:75 | … that would realize the lumped-film assumption. | … that would act like the lumped film. | robotic repetition of "the lumped-film assumption" in one sentence |
| summary:24 | ; in bulk silicon this memory loss takes 6.8 ns for births near the band top | , and in bulk silicon the memory time of births near the band top is 6.8 ns | *this memory loss* points at a predicate and is a second name for the memory time |

## Recall (untouched text)

Sample: every paragraph the editors did not change (67 paragraphs, about 4,990 words: s20-1 518, s20-2 1219, s20-3 1005, s20-4 845, s20-5 1268, summary 135), plus the unchanged sentences inside changed paragraphs, all files.

Misses found and fixed:

| file:line | text | fix | failure |
|---|---|---|---|
| s20-1:88 | if its dense track traps more often | if the carriers of its dense track are trapped more often than the carriers of an electron recoil | comparand missing; the track does not trap. The comparand is fixed by the definition $f_{\mathrm{ion}} = N^{\mathrm{NR}}_{\mathrm{ind}}/N^{\mathrm{ER}}_{\mathrm{ind}}$ and matches s19-5:101, so no claim is added (open item) |
| s20-2:136 | Hernandez et al.\ trace that spread to | … trace the spread of the decay constant to | *that spread* points at a predicate ("lies between … and …") |
| s20-4:111 | which sets the scale of its prompt phonons | … of the prompt phonons in germanium | *its*: "germanium" occurs only as an adjective |
| s20-5:3 | The rest of each deposit becomes phonons, and the phonon sensors see three populations: … the phonons that return the gap energy | The part of each deposit that the pairs do not hold as gap energy becomes phonons. The phonon sensors see three populations: … | *the rest* without its argument, read against the third population (open item); reading follows ch20:2 (69 eV of phonons plus 31 eV of gap energy) |
| summary:28 | The exclusion limits of the next chapter start from the measured charge and phonon signals, with these conditions. | … start from the measured charge and phonon signals, with these verdicts and the same assumption about transport. (budget-table sentence moved after it) | *these conditions* had no noun antecedent; the table sentence stood between it and the verdicts (open item) |
| s20-3:37 | The one critical angle that limits transmission | The only critical angle that limits transmission | *the one* read as a quantifier pointer (open item; see below) |

Rate: 6 misses in about 23,000 words read, of which 1 in the 4,990 words of wholly unchanged paragraphs (summary) and 5 in unchanged sentences of changed paragraphs (3 of them already listed by the editor as open). About 0.3 misses per 1000 words overall, at most about 1 per 1000 in any file. Below 2 per 1000 in every file: **no second pass needed for ch20.**

## Open items

- s20-4 ρ_g sentence: editor's reading confirmed (s19-5:169 defines $\rho_g$ as the collection efficiency of the gap-energy phonons over that of the hard primaries; "This" pointed at "need not equal"). Kept, with the *which* clause fixed (above).
- s20-5 "the first two effects" / "the third effect": the third is correctly the longer bounce. The first two are the sub-gap loss and the yield above threshold, not only 2–4 gaps; fixed (above).
- Summary "exclude collection as the whole explanation": confirmed; it is verbatim the base wording of s20-5:79, as is "decides between collection and stored energy" (s19-5 shows the two-bias measurement separates $\mathfrak{r}'$ from the heat quenching). Kept.
- s20-5:3 "The rest of each deposit": fixed (recall table).
- s20-1:88 "traps more often": fixed; the comparand is the electron recoil, which the definition of $f_{\mathrm{ion}}$ already implies (s19-5:101 uses the same comparison).
- Summary "with these conditions": fixed (recall table). Reading chosen: the conditions are the verdicts of the paragraph and their stated assumption of unvalidated transport. The lead may prefer to drop "and the same assumption about transport" if ch21 does not inherit that assumption.
- s20-3:37 "the one critical angle" against two angles in the fig:20-amm caption: **not a physics error.** With the Voigt speeds (Si 9.00/5.40, Al 6.63/3.30 km/s), from silicon only an incident SV wave meets faster waves: $\arcsin(5.40/9.00) = 36.9°$, where the *reflected* longitudinal wave in silicon becomes evanescent, and $\arcsin(5.40/6.63) = 54.5°$ (54.6° in the text, presumably from unrounded speeds), where the transmitted longitudinal wave in aluminum is lost. Only the second limits transmission, so the sentence is right. Wording changed to "The only critical angle". The panel-(b) angles also check: 21.5°, 29.9°, 37.7°, 47.5°.

## Proposed erratum (clarification, optional)

- Location: s20-3:37 or the fig:20-amm caption.
- Old: "Gray lines: critical angles, \SI{36.9}{\degree} and \SI{54.6}{\degree} in (a);"
- Proposed: "Gray lines: critical angles, \SI{36.9}{\degree} (reflected longitudinal wave of an incident SV wave) and \SI{54.6}{\degree} (transmitted longitudinal wave) in (a);"
- Reasoning: the caption lists two angles for (a) while the text says only one limits transmission. Both statements are right, but the reader cannot tell why without the speeds. This adds a claim, so it goes to the lead rather than being made here. Also check whether 54.6° should read 54.5° with the rounded speeds quoted in the chapter.

## Checks

- `tools/invariant.py 60cc72c tex/ch20/*.tex`: 0 files with a STOP.
- Lint on all ch20 files: no hits from my edits. One sentence I lengthened past 45 words (s20-5:3) was split again. The remaining LONG-SENT hits were there before.
- `tools/chapcheck.sh ch20 /tmp/binding-review-vol2f`: exit 0, 46 pages, 0 undefined references, 0 multiply defined labels; one overfull hbox (the s20-4 one the editor reported as pre-existing).
