# Adversarial prose round (2026-11-12): summary

Base commit 8904b84. Brief: briefs/volumes/PROSE.md. Detector: tools/llmese.py (candidate tells; a hit is not a verdict).

| Volume | Detector hits before | after | per 1000 words after | Diff review: changes checked / kept / fixed / reverted |
|---|---|---|---|---|
| I | 192 | 68 | 0.3 | 482 lines / 473 / 6 / 3 |
| II | 251 | 108 | 0.3 | 312 + 357 / 290 + 342 / 14 + 12 / 8 + 3 |
| III | 83 | 33 | 0.3 | 267 / 257 / 10 / 0 |

Remaining hits are mostly one-clause contrasts that head off a misreading ("an estimate, not a bound") and literal uses ("far from the core"), kept on purpose and listed in the unit logs. Reviewers restored every sentence whose edit dropped a fact, a qualifier or a validity condition, or changed a claim's strength; the logs review-vol1.md, review-vol2a.md, review-vol2b.md, review-vol3.md give one row per case. Final build: Vol I 600 pp, Vol II 806 pp, Vol III 246 pp; 0 errors, 0 undefined references or citations, 0 overfull boxes above 5 pt.
