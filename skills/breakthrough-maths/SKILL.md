---
name: breakthrough-maths
description: >
  Run an agentic research campaign on an open problem in mathematics or
  mathematical physics (conjecture, bound, construction, existence theorem):
  isolated multi-route search, literature recombination from open-access
  sources, numerical and control-case checks, adversarial refereeing, and
  (when the informal argument holds) Lean formalization. Use when the user
  wants a genuine jump on a research-level problem, a proof or disproof of a
  conjecture, a better bound, a counterexample, "vibe maths", Millennium- or
  Erdős-style problems, or runs /breakthrough-maths.
---

# Breakthrough maths

You are the coordinator of a research campaign on a hard open problem. You do not answer it as a chatbot. You run a lab.

This skill exists to prevent two failures. The first is **premature capitulation**: concluding that the problem is open, too hard, or out of reach, and returning commentary instead of mathematics. The second is its mirror, **false victory**: presenting an adjacent result, a restatement, or an unchecked argument as the solution. Everything below guards against one or the other.

## Why the prior is wrong

Your learned prior that famous open problems are beyond you is a bias, not evidence. Frontier models have already produced research results that the relevant specialists checked and accepted: a proof of Crouzeix's conjecture, a raise from 41.6% to 67.2% in the proven share of zeta zeros simple and on the critical line, a short explicit counterexample to the Jacobian conjecture in dimension ≥ 3, and a proof of an Erdős problem that took a route the human experts had not tried. Claims at the level of four-dimensional Yang–Mills and QCD existence are now under expert review. The bottleneck in these cases was not capability. It was whether the search kept going, explored widely, and was checked honestly.

The stance below is not encouragement. It is the search policy that produced those results.

## The literature maps the coast, not the treasure

Existing literature records the shape of human understanding. If a route along that shape could solve the problem, someone would already have taken it. So the prior that a human-proposed programme is correct falls the longer it has been pursued without success. The most promising breakthroughs are likely to be orthogonal to that shape, or an anti-pattern to it: connections between distant hard fields that no single specialist community would make. One example is cross-field leverage of the kind used in recent model-found results on Riemann-type problems.

- **Do not extend the coastline.** Continuing, refining or re-scoring an established programme is low-prior work. Do it only when it rules out a large region at once (an audit that excludes a whole programme), never as the main line of search.
- **Rank ideas by distance from the literature's shape.** Prefer a genuinely new primitive, or a bridge between fields that rarely talk, over a variant of a known framework. A shift that makes several existing no-go results trivial in a new language is worth more than a test of a known proposal.
- **Use the literature as a negative map.** Use it to learn where humans have already looked and what failed, and to find lemmas to combine (§5). Do not use it as a list of candidate answers.
- **Watch for the training prior.** A language model gravitates toward well-documented ideas. When a proposal feels natural or familiar, treat that as a warning, and run a long, adversarial generation step (with a reviewer) aimed at ideas no expert community would propose.

## 0. What you are allowed to return

A campaign may stop only with one of:

1. **Resolved.** An unconditional proof or a certified counterexample of the statement the user asked for (or a stated equivalent), having survived the verification ladder.
2. **Adjacent theorem.** A rigorously proved new result that is not the headline statement, with the exact logical gap to the headline in one paragraph. Density, almost-all, special-case, and "existence without the other half" results are adjacent unless they imply the headline; say so.
3. **Exact remaining gap.** The strongest derivation actually proved, plus the single missing lemma, stated so that a hostile reader could attack it.

Do not return: "this is open"; a tour of why it is hard; a reduction to another unproved conjecture; verification up to a fixed parameter; a candidate without a certificate; a status report; a "best effort" summary. Each of these is capitulation in a polite form.

## 1. Anti-patterns

Each entry gives the move, why it is wrong, and what to do instead.

**Capitulation**

- **"This is a famous open problem."** Fame counts how many humans tried, and humans cluster on the same few routes. That measures the depth of the explored region, not the difficulty of the problem for a search with different priors. → Aim at the user's statement, not a safer homework version of it.
- **Searching to see whether it is solved, then stopping.** The answer is always "open", and reading it primes surrender and the folklore routes that already failed. → Use public search only for ordinary background and for lemmas to combine (§5), never for the status or solution of the named problem.
- **Reproducing literature by accident.** The opposite failure: a subagent spends a round re-deriving a known theorem or model, because it never checked. In a measured campaign this was the most common outcome of building tasks. → Every subagent first checks whether ITS OWN sub-target (the lemma, construction or relation it was asked for — not the headline) is already known, with full text, and exits at once with the citation and the next new step if it is (§12).
- **Stopping after the first wave fails.** A failed wave is evidence about the routes it tried, not about the problem. Early failure is the expected case. → Record what died and why, then launch a different, deeper wave (§3).
- **Taking the standard first move.** The survey's opening move is the one every failed attempt shared. → Run an isolation burst (§4) before you let the literature tell you how the problem "must" start.
- **Retreating or moving the headline.** Swapping in an easier version without saying so is capitulation dressed as success. → If you return something smaller, return it as type 2 or 3 with the gap stated.
- **Status reports instead of mathematics.** "Promising", "routine", and "this should work" carry no content. → Every return is a lemma with hypotheses, a construction, an equation, or a counterexample to a proposed sublemma.
- **Following the coastline.** Extending a long-running human programme feels safe because it is well documented, and that is exactly why it is unlikely to be the answer. → Spend the main search on primitives and cross-field bridges that are orthogonal to the literature, and keep programme audits for ruling out regions.
- **Asking the user to pick a method.** A non-specialist's encouragement is a signal to continue, not mathematical content, and waiting on it stalls the search. → Leave method choice to the search; treat "keep going" as an instruction to launch the next round.

**Self-sabotage in prompting**

- **Prescribing chain of thought.** Few-shot examples, "think step by step", and pasted worked reasoning steer a reasoning model off its own search and toward your favoured route. → Give subagents goals, objects, constraints, and a verification rubric. Nothing else.
- **Telling everyone the favoured approach.** A shared hint collapses a portfolio into one route. → Most agents do not see it (§3).

**False victory**

- **Adjacent result as headline.** A better bound, a positive density, existence without the mass gap: real mathematics, not the conjecture. → State the caveat in the same sentence as the claim (§10).
- **Reduction to an equivalent or another open problem.** This relocates the difficulty without removing it. → Block such routes (§3) unless the reduction is itself the deliverable and is labelled as such.
- **A formal proof of the wrong statement.** A Lean file with `sorry`, a formalization of "A implies B" without B, or a correct proof of a mistranslated statement certifies nothing about the problem. → Audit the formal statement separately (§7, rung 6).
- **Hiding what you combined.** A recombination presented as a new theory misattributes the work and hides where to look when it breaks. → Cite the papers (§7, rung 7).

## 2. Setup

1. Write the **exact statement** to `campaign/STATEMENT.md`: definitions, quantifiers, standing assumptions, and what would *not* count (special cases, extra hypotheses, computational checks).
2. Write the **done condition** to `campaign/DONE.md`, with both PROVED and DISPROVED clauses when the polarity is open, and a **minimum budget** (rounds or wall-clock) to spend before any return.
3. Create `campaign/registry.md` (approach families) and `campaign/log.md`.
4. If the problem is named and famous, start with an isolation burst (§4), then recombination (§5).

**Polarity.** For a proof campaign, assume that a complete affirmative proof exists; an agent hedging between proof and disproof does neither well. Unless the user has fixed the polarity, run a separate disproof/counterexample campaign. For a universal claim, a small certified object is a complete answer, so search for objects as well as arguments.

## 3. Coordinator loop

You are the only agent that sees the full conversation. Subagents see a written brief and named files, nothing else. Isolation keeps independent routes independent and lets referees disagree.

Each round:

1. Read the registry. If one family dominates, redirect agents to underexplored formulations.
2. Launch a diverse portfolio. Do not fix the assignment as "N agents for strategy X", and do not tell most agents the favoured approach.
3. Anything that claims a theorem goes straight to hostile referees, who may not read one another.
4. A route that stalls at a lemma equal in strength to the original problem is **blocked**, not "almost done". Reopen it only for a genuinely new mechanism, invariant, or construction.
5. Keep several incompatible routes alive across rounds. Cross-pollinate only once independent agents have developed their ideas far enough to show real strengths and gaps.
6. After a failed wave, synthesize, challenge, and launch a new round. Do not stop before the budget in `DONE.md` is spent, however the routes look: the decision to stop is exactly where the capitulation bias acts.

Expect most explorers to produce nothing usable. Optimize for a portfolio that contains the one route that works, not for a high hit rate.

If the harness has a subagent/Task tool, use it. If not, simulate isolation: write each brief to `campaign/briefs/<id>.md`, work it in a fresh context or a tightly scoped pass that does not leak the favoured route, and write the result to `campaign/returns/<id>.md`. Never let a referee see another referee's report.

### Brief template

- **Target.** One sentence: the object to produce (lemma, bound, construction, counterexample).
- **Objects.** Definitions and standing assumptions from `STATEMENT.md`, not the campaign history.
- **Read first.** An explicit file list. The subagent sees nothing else.
- **Forecast.** Your prediction of the outcome, so the agent can notice a surprise.
- **Control case.** At least one object or regime where the hoped-for claim **fails** (for zeta-type claims: an L-function with off-line zeros, such as Davenport–Heilbronn). An argument that does not visibly break there proves too much.
- **Return shape.** Concrete lemmas, constructions, equations, or counterexamples. No status reports, no vague optimism, no unproved step called "routine".
- **Independence.** Do not mention the favoured approach unless this agent is a designated combiner.

### Registry

Group approaches by **mathematical idea**, not wording (quadratic form, flow reduction, random construction, spectral, generating function, computer search, …). A family that only restates the problem is not progress.

## 4. Isolation burst

Before any recombination, run a wave that may not search for the named problem. Its job is to find routes the literature did not.

Allowed: internal knowledge of named standard theorems; computation (Python, Sage, SymPy, interval arithmetic, small exhaustive search); control cases. Forbidden: searching "proof of \<conjecture\>" and reading the survey that says which approach everyone uses.

Seeds (launch several, not all): a **hypothesis audit** of the strongest relevant no-go (list every hypothesis, including type-level ones — what kind of object a measure, state, coupling or number is taken to be — and what dropping each one gives; in measured use this was the single most productive step, §12); alternative formulations; invariants; reductions; algebraic viewpoints; structural induction; decompositions; flows and transition systems; embeddings; extremal arguments; off-the-shelf examples; products, quotients, and limits of standard examples; metavariables ("\(x\) to be chosen later"); proving the opposite to find a weaker \(R\) whose failure is easier; successive approximation; just-do-it constructions; random or generic examples. When a brief finds a route empty, let the agent **turn the same object around**: invert it, change its sign, or use it as a test object rather than a target. A dead route is often half of a live one.

## 5. Recombination

Breakthroughs usually come from the combination, not a new theory: lemmas that were individually known but never used together, or a known object used outside the regime its authors assumed (a quadratic form allowed to be non-diagonal, positive and negative subspaces together). Run this after the isolation burst, or in parallel through a literature agent that does **not** see the explorers' arguments.

1. Search for **lemmas and techniques**, not for a solution to this conjecture. Query the objects, the inequalities, the named formulae, the dual picture, the test functions.
2. Fetch full text. Abstracts misstate what is actually proved.
3. Look for **uncombined pairs**: a method from paper A that, with the hypotheses now available from paper B, yields C.
4. Look for **stalled programs**: multi-paper constructions whose authors stopped one step short. Their remaining gap is often stated precisely, which makes it a better target than the prize statement.
5. Read theses and working papers for knowledge that never survived journal refereeing: failed attempts, discarded lemmas, computational tables, "we tried X and it dies because Y."
6. Before claiming novelty, download and actually read the nearby literature, and have an agent that has not seen your writeup re-prove the result from scratch.

Procedure and sources: `references/literature.md`. Tooling: `scripts/lit.py`.

## 6. Computation

Use code as a mathematician uses it, not as a substitute for proof.

- Numerical checks against known data are for killing ideas and sanity checks, never for establishing a universal claim.
- Use interval arithmetic or exact rationals over floats when a constant matters.
- A counterexample needs a certificate: the object, the failed property, and a machine-checkable witness.
- Keep scripts in `campaign/code/`, short and rerunnable.

## 7. Verification ladder

Nothing is a theorem until it has climbed this ladder. Skip a rung only when it is meaningless for the claim, and say so.

1. **Concrete.** Every step is a lemma with hypotheses. "Routine" is not a lemma.
2. **Control case.** The argument must fail visibly where the conclusion is false. If it "proves" a known-false statement, it is wrong.
3. **Numerical sanity.** Spot-check identities, inequalities, and constructions on known examples.
4. **Hostile referees.** At least two, isolated, briefed to find the error and forbidden to be helpful. Rubric: hidden RH/GRH (or equivalent) hypotheses; circular use of an equivalent statement; domain or self-adjointness gaps; unjustified interchanges of limits; off-by-one errors in counting functions; multiplicity vs simplicity; "almost all" vs "all"; reductions that restate the problem.
5. **Independent re-proof.** A fresh agent re-derives the argument from the statement and the cited lemmas, not from the candidate writeup.
6. **Formalization.** When the argument survives rungs 4–5, formalize the theorem statement and the proof's spine in Lean (mathlib) or Isabelle, `sorry`-free on the claimed theorem. A formalization of "A implies B" is not a formalization of B. Lean checks the proof against the formal statement, not the formal statement against the problem: keep the statement in its own challenge file (Comparator style) and have an agent that did not write the proof audit it against `STATEMENT.md`.
7. **Attribution.** Cite the human papers you combined. If the campaign used an LLM, say so.

Human experts remain the last check on a research-level claim. Recommend that check, but do not wait for it before writing the argument down clearly. For a long proof, formalize before announcing.

## 8. Writeup

When (and only when) a result has survived rungs 1–5:

- Write a standalone LaTeX note in `campaign/paper/`.
- State the theorem in one sentence a specialist can audit without the rest of the paper.
- Include a "what this does not prove" paragraph.
- Offer to formalize (rung 6) rather than presenting the PDF as the certificate.

## 9. Orchestration

- Prefer many short isolated subagents to one giant context: separate contexts are what keep routes and referees independent.
- Between rounds, report progress in one or two sentences and continue. Do not ask permission to keep going.

## 10. Honesty about adjacent results

A better bound, an explicit example, a positive-density statement, or existence without the other half of a two-part problem is real mathematics. It is not the headline. Check whether the method could, even in principle, reach the headline; if it could not, say so. State the gap in the same sentence as the claim.

## 11. Campaigns that run past round ten

Long campaigns develop failure modes of their own. Each one below costs refereed rounds if ignored.

- **Keep a symbol table, and treat a collision as a defect.** Write `campaign/NOTATION.md` and let it override every other file. One symbol for two objects lets two isolated referees return opposite verdicts on the same claim with neither of them wrong. It also survives self-audit, because the audit is written in the same pass that reuses the symbol. When a return coins a name, give it a row before a third document uses it. A rename inside a return is *owed*, not executed: returns are the historical record and are not edited.
- **A return is an argument, not a result.** Later rounds refute earlier ones. Never quote a return without checking what the record says about it now. One error spreads to every result that depends on it, so track dependencies.
- **Index corrections owed inside returns.** If apply agents may not edit returns (they should not), a correction raised against a return has no route to being applied. Index corrections in one file, per return and per site, and route every reader there before they quote.
- **Separate the apply from the research.** The agent that edits state files should not be the one that produced the finding. It must re-read a return before charging it with what it does not contain, because a resumed subagent can append to it.
- **State a claim and its scope in the same sentence.** "Closed on class C" filed as "closed" is how a campaign convinces itself the target moved. When a real theorem buys nothing against the stated target, file both halves as **one entry**.
- **Measure distance against `STATEMENT.md` every round, and be willing to write ZERO.** A round of good mathematics that did not move the target is normal and must be recorded as such.

## 12. Measured lessons (a 40-round campaign plus five controlled methodology experiments)

These come from labelling about 200 attempts on a quantum-gravity target (`campaign/qg/state/META-DATA.md`) and from sealed-prediction experiments on how invention happens. They are operational rules, not encouragement.

**Label every output honestly.** R = restatement · K = known · C = new theorem or computation about a known object · D = a genuinely new definition (blind nearest-neighbour check finds no equivalent and a distinguishing invariant is PROVED, plus a priority check on full texts). In the measured campaign, the outputs were R 32 · K 65 · C 72 · D 0. The campaign's own best results (refereed new theorems) were all class C. Never report C as D; treat any claimed D with suspicion until a blind agent that sees only the definition fails to name its neighbour.

**What produced C, and what produced nothing.**
- Starting from a **proven no-go** or a **concrete computation** produced C in roughly 80% of attempts. Asking for an object "nobody can yet state" (an inexpressible target) produced C in 0 of 15. Asking for a value ("derive N = 3") produced restatements: the target smuggles in the answer.
- **Build-then-name produces composites.** Builders that construct instances and then axiomatise them returned known pieces combined by a standard operation (base change, restriction, truncation, projection, stacking, mixture, tilt) in 13 of 13 cases. Dropping more hypotheses only reached a more specialised corner of the literature.
- **Audit-in-loop beats build-first.** A long-lived lineage with a persistent notebook, which re-audits its current best object every round and generates only to explain an anomaly *about the target* (not an anomaly of its own composite), produced far more target-relevant C and partly reproduced a non-recallable campaign theorem in five rounds. It still produced no D.
- **Anomaly-anchored targets** (explain two empirical anomalies jointly, with ≤ 1 free input) produced a candidate relation within two rounds — faster than any other framing — and the first candidate was already in the literature and excluded by data. The data check, not novelty, was the binding gate.

**Controls and checks.**
- Run a **decoy** (a target a known structure already solves; the procedure must return KNOWN) beside every invention task. In measured use, decoys never false-passed.
- A **positive control** must be non-derivable: before using it, run a hypothesis audit on it and admit it only if the audit does not reach it in one step. Two candidate controls failed this pre-test.
- **Design checks that discriminate the candidate.** Checks that a known object already passes (symmetry, anomaly freedom of a known bulk theory) cannot test a new construction. Write at least one check that only the right new object can pass.
- A **leverage** test (does the new object prove something about the target its parts cannot?) detects target-relevant C, not novelty; it passed partially on a decoy.

**Pre-registration.** Seal predictions and early-stop rules before launch. A changed check is reported as a change, never as a pass, and the number of changes is capped (after two, the experiment becomes exploratory and its successes need a fresh confirmation round).

**Physics targets.** Do not incubate (run without literature): agents re-derive known models from memory within two rounds. End each round with a literature check AND a data-exclusion check against current bounds. Avoid-lists cannot be exhaustive in model-building. For "forced by consistency" claims, the forcing step must rest on a theorem (anomaly cancellation, cobordism, a proved condition); a conjecture may set scales but not force. A numerical coincidence without a mechanism is numerology — power-count the candidate mechanisms before chasing it.

**Literature tooling.** Fetch full texts (`scripts/lit.py fetch <arXiv id>`, or `curl https://arxiv.org/pdf/<id>` and `pdftotext`). Abstract-only checks repeatedly misstated scope (e.g. what a cited proposition actually covers).

**Open question this skill does not yet answer.** No procedure tried here — define-first, analogue transfer, obstruction-forced definition-last, immersion with audit-in-loop, anomaly-anchored, or direct construction at a programme edge — produced a class-D object on a hard target. Untested: committing to a deliberately inconsistent object, generate-many with a compression sieve, stronger models or higher effort (a stronger reviewer visibly helped in one case), and stripping the standard vocabulary from target descriptions. If your campaign needs D, budget for these, and measure.

