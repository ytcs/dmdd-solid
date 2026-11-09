# Standalone public document: the scrub

The book must read as if written by an author with no knowledge of how it was produced.

## Never in the book
- Names of agents, tools, models, workflows, rounds, briefs, returns, ledgers, file paths, repository or
  branch names.
- Internal labels of the research effort: work-package numbers, milestone names, gap IDs, correction IDs,
  referee labels, claim IDs, truncation codes that were only used internally.
- Phrases such as "our campaign", "the pipeline", "in round 3", "the referee found", "as established in
  the audit".
- References to unpublished internal documents.

## Translate instead
- An internal label for a result becomes a descriptive name, defined in the book: "the decomposition
  theorem (Theorem 8.2)", not "Theorem D".
- An internal acronym may survive only if it is useful to readers, defined at first use, listed in the
  acronym table, and not tied to the production process.
- Internal conventions (sign of q, normalisations, nuisance types) are stated in the book's own
  conventions chapter or appendix.
- Results that came from internal review are presented with their derivations, and attributed to public
  literature where they exist there.

## Enforcement
1. Maintain `BANNED-TERMS.txt` from the start: seed it with every internal label in the source material,
   and add new ones as they appear.
2. Run `scripts/lint.py --banned BANNED-TERMS.txt` on every section, and on the whole book before
   release.
3. Run a final human-style read by an agent that has never seen the source material. It flags anything
   that sounds like an internal reference.

## Process artifacts
The scrub also removes sentences that reveal the production process indirectly: consistency assurances, reviewer-directed justifications and fix announcements (prose-review.md pattern 19). A sentence that would make sense only to someone who saw an earlier draft or a review report does not belong in the book.
