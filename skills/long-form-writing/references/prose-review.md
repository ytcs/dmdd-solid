# Prose review: anti-AI and clarity checklist

The prose reviewer reads the section as an editor at a science publisher would. It runs `scripts/lint.py`
first, then reads in full. Report every hit with a location and a concrete rewrite.

## Patterns to remove (the lint catches many; the reader must catch the rest)
1. **Empty signposting.** "In this section we will…", "Let us now turn to…", "It is worth noting that…",
   "It is important to note…", "As we will see…" with no payload. Say the thing.
2. **Inflated vocabulary.** delve, crucial, pivotal, intricate, realm, landscape, tapestry, robust (when
   not technical), seamless, leverage (as a verb), underscore, showcase, notably, essentially,
   fundamentally (as filler), "plays a key/vital role", "a wide range of", "cutting-edge".
3. **Reflexive triads.** Lists of three adjectives or clauses chosen for rhythm, not content.
4. **Stacked hedges.** "may potentially", "could possibly", "it might be argued that it is likely".
   State the claim with its actual condition.
5. **Restating paragraphs.** A paragraph that summarises the one before it. Summaries belong at chapter
   end.
6. **False contrast and negation framing.** "This is not just X, it is Y"; "Rather than merely…".
7. **Dash overuse.** More than about one em dash per paragraph, especially paired dashes used as
   parentheses. Use commas, parentheses or separate sentences.
8. **Colon-reveal and rhetorical questions** used for drama ("The answer? Screening.").
9. **Generic praise or motivation.** "This elegant result…", "This powerful framework…". Let the result
   speak.
10. **Uniform sentence rhythm.** Long runs of sentences of equal length and structure. Vary them. Short
    declarative sentences are good after a long derivation.
11. **Bullets instead of argument.** Reasoning must be in connected prose. Bullets only for enumerations.
12. **Vague quantifiers.** "significantly", "substantially", "a large number". Give the number or the
    scaling.
13. **Unanchored "this".** "This shows…" where the referent is unclear. Name the thing. The same goes for ordinal references to unlabelled parts ("the second form", "the latter") of an equation or a list: name the part ("the value in natural units").
14. **Over-qualification of established results** and under-qualification of new ones. Calibrate
    confidence to evidence.
15. **Anthropomorphic or marketing tone** ("the framework knows", "unlocks", "empowers").

16. **Titles with fluff.** Book, part, chapter and section titles are short noun phrases that name the
    content ("Lattice dynamics", "Screening"). No subtitles unless the publisher requires one, no
    colon-joined title pairs, no punchlines, no rhetorical or clever titles, no epigraphs or opening
    quotations.
17. **Wordy sentences.** Every sentence carries information. Cut throat-clearing openers, redundant
    modifiers, doubled synonyms ("each and every", "first and foremost") and nominalisations that hide
    the verb. Prefer the shorter of two equivalent phrasings.
18. **Abstract category frames.** A sentence that names a category instead of its members, so the reader
    immediately asks "like what?": "This chapter fixes what the rest of the book takes from outside the
    solid", "We collect the facts we need", "The key ingredients are discussed below". Name the members:
    the quantities, numbers, questions or results. Check every opening sentence of a chapter, section and
    paragraph against this, and every roadmap paragraph (say what the reader will be able to compute, do
    not list sections mechanically). Count-teasers are the same failure ("Two consequences need no knowledge of the target.", "Three bosons are standard."): name the consequences or the bosons in the sentence itself. So are recap openers ("The previous sections fixed …"): open with the new question.

19. **Process artifacts.** Sentences that exist only because the text went through drafting and review
    rounds, and that a human author would never write: assurances of internal consistency ("every
    threshold mass in this chapter uses that value, so that it can be compared with the literature";
    "we use the same value throughout for consistency"); justifications aimed at a reviewer rather than a
    reader ("a source with the opposite sign is converted before use"; "we do not quote the paper's number
    because it does not reproduce"); bookkeeping about which value was adopted and why, where the choice
    is unremarkable; defensive asides that answer a past review comment. Consistency is taken for granted
    in a book: state the value and use it. Keep a convention note only where a reader would otherwise be
    misled when comparing with the literature, and phrase it as a fact about the literature, in one clause.
    Revisers in particular must fix a reviewer's point in the text itself, never by adding a sentence that
    announces the fix.

20. **Citations as content.** Any place where the reader must consult a cited source to follow the text: a formula, definition, parameter value or procedure given only by reference ("Source: Ref. [12], Eq. (77)", "as defined in [12]", "the parameters of [12]"). State the content in the book; keep the citation for credit.
0. **The governing test: information content (user, 2026-11-02).** Claude-speak is any expression or sentence that carries little concrete information. Apply the deletion test to every sentence and title: delete it, then ask whether the reader lost a fact, a number, an equation, a definition, a named object or a step of argument. If not, cut it, or rewrite it so that it carries one. Patterns 16–23 are special cases of this test. Typical low-content forms:
   - **Gestures that point at content without stating it:** "plays a key role", "is central to", "has important consequences", "rich structure", "subtle interplay", "deep connection", "nontrivial".
   - **Evaluations without a referent:** "remarkably", "crucially", "it is worth noting that", "interestingly".
   - **Narration of the text's own moves:** "we now turn to", "we state", "as we will see".
   - **Restatements:** a sentence that only repeats the previous one at a higher level of abstraction.
   - **Generic framing sentences:** sentences true of any section in any book ("This is an important topic", "Several effects contribute").
   The fix is always to name the thing: which effect, how large, in which equation, under which condition.
21. **Gesturing titles.** A title must tell the reader what the section contains: its object, result or method, in the field's own terms. The failure is a title that gestures at the content without naming it: "The event rate and its factors", "What gravity fixes", "Where the electrons go", "Putting it together", "Beyond the simple picture", "X and its consequences", "Some subtleties". Test: from the title alone, could a reader guess the section's central equation or claim, and find it in an index? If not, rename. Prefer the established name ("The master equation of direct detection", "Inputs from cosmology", "The Lindhard function", "Multiphonon response").
22. **Self-narrating procedure.** Sentences that describe what the text is doing instead of doing it, especially deferral and provenance notes: "We state it here without derivation", "We give it in the form of Ref. [1, Eq. (8)]", "We now turn to…", "In this section we…". They add nothing, and a provenance note that points at a source's equation number sends the reader out of the book. When content is deferred, say where in the book it is derived ("We derive this in Chapter 2", "Chapters 2–4 derive each factor"); attribute with a bare citation.
23. **Unannotated master equations.** When a central equation is a product or sum of physically distinct pieces that the following text names and discusses one by one, label the pieces in the display itself (underbraces or overbraces with one- or two-word labels: "halo", "coupling", "target", "kinematics"). The reader should see the structure before reading the paragraph that explains it. Reserve this for the few organizing equations, not routine displays.

## Language and register checks
The text must read as if written by an experienced physicist explaining the subject to a colleague: plain,
idiomatic, and in the working parlance of the field. Each project names one or more **register models**:
human-written expositions in the same field whose voice the book should match (lectures, reviews and
textbooks known for clear writing). Their distilled usage is recorded in the project's REGISTER.md. The
reviewer checks against it:
- **Field parlance.** Use the terms of art practitioners use, in the sense they use them. Examples: "heavy
  mediator" and "light mediator", not "contact-limit regime"; "reach", "threshold", "the kinematic
  mismatch"; "order of magnitude" and "parametrically". Do not coin a phrase where an established one
  exists. When the book's NOTATION forces a non-standard symbol, say once what the literature usually
  writes.
- **Colloquial precision.** Prefer the plain verb and the concrete noun ("the rate drops", "the electron
  cannot follow", "this kills the signal below 1 MeV") over nominalised or bureaucratic constructions ("a
  reduction in the rate is obtained", "the consideration of"). Use the connectives and idioms the register
  model actually uses, at about its frequency (REGISTER.md counts them). Expository idioms such as "for
  concreteness" or "the upshot" are rare in good physics writing; use them sparingly, never as filler, and
  never to make prose sound casual. Watch for over-used crutches the model avoids (e.g. "so", "gives",
  "therefore", "only" at several times the model's rate).
- **Estimates and intuition, as physicists give them.** Parametric estimates come before exact results,
  where they help ("the rate scales as …, so …"). Back-of-the-envelope numbers ("about a meV"). Physical
  pictures ("the dark matter is too slow to resolve the atom"), stated, then checked by the formula.
- **Sentences a human would say aloud.** Vary the length. Use the active voice by default. Do not stack
  appositives or chain subordinate clauses. Write no sentence that needs a second reading to parse.
- **No translated-from-formalism prose.** Do not narrate an equation symbol by symbol ("where the first
  factor is …, the second factor is …") when one sentence about its meaning does the job.
- **No stilted connectives.** Avoid "thereby", "whereby", "thus" at every turn, "hence" chains,
  "respectively" constructions that make the reader pair lists, and "in order to" for "to".
- **Calibration against the register model.** For each section, the reviewer picks 2–3 passages and asks
  whether an author of the register model could have written them. When the answer is no, the reviewer
  rewrites one sentence as that author would, to show the target.

## Arrangement checks
- Each section opens with why the reader needs it: the problem it solves, or the question it answers,
  tied to what came before. Motivation is one or two sentences, not a preamble.
- Material is ordered so that each step follows from the last. No forward references for definitions,
  and a result is not stated before the tools to understand it.
- The simplest correct case comes first, then the generalisation.

## Clarity checks
- Every paragraph has one job. The first sentence says what it is.
- Every equation is introduced by what it will be used for, and followed by what it means.
- Every new symbol is defined where it first appears, and matches NOTATION.
- Technical terms are used in one sense only, and match GLOSSARY.
- Physical intuition accompanies formal results, but never replaces a derivation.

## Report format
A table with columns: location | pattern # | text | rewrite. Then a verdict: PASS (≤ 3 minor hits per
1,000 words), REVISE, or REWRITE (systemic voice problems).

### 24. Invented metaphor vocabulary in place of the field's terms
Symptom: a private metaphor becomes a technical noun and spreads through the text. Examples: the "rung" of an approximation "ladder", or a "tier" or "layer" where physicists say level of approximation, order, or approximation by name ("RPA", "RPA with local fields", "BSE"). Readers from the field don't recognise the word, and it carries less information than the name it replaces. Fix: use the field's own term or name the approximation ("the many-body approximation 𝒳", "at three levels of approximation: RPA, RPA with local fields, BSE"). Keep the word "ladder" only where the field uses it (the ladder diagrams of the Bethe–Salpeter equation). Check: would a referee in the field use this word in a paper?

### 25. Periphrasis and negation-stacked withholding
Symptom: a figurative or coy stand-in replaces the plain technical word, often wrapped in stacked negations that hold back the positive statement. Examples: "pull" for gravity; "silence" for a null result; "the data tell us"; "the lattice whispers"; "sits at the heart of"; "never … anything except"; "nothing … but"; "does little more than"; "has yet to".
Before: "Most of the matter in the universe has never been seen to do anything except pull. … That silence has shifted attention to lighter particles."
After: "Most of the matter in the universe has been detected only through its gravity. … Those null results have shifted attention to lighter particles."
Deletion test: rewrite the sentence with the technical noun and no negations. If nothing is lost, the original was periphrasis. Motivation comes from concrete stakes (a number, what fails, what becomes measurable), never from figurative cadence or aphorism. Technical uses stay: "window" (kinematic window), "Wannier picture".

### 26. Looped restatement ("looped response")
Symptom: the closing paragraphs of a subsection restate content already established, often several times in slightly different words. For example: a summary of the key-result box, then a "without knowledge of the target, X fixes Y" paragraph, then a corollary that repeats the box's claim. Each loop adds no new fact, number or consequence, and the reader has to work out that nothing has changed.
Example: Sect. 1.3.1, where the paragraphs after the keyresult re-derive and re-explain what eq:1.3-omegaq and eq:1.3-vmin already state.
Test: for each paragraph, write the one new fact it adds. If it adds none, or only one that an earlier paragraph already states, delete it, or merge its single new clause into the paragraph that first made the point. A subsection ends on its last new fact, not on a recap; the chapter Summary is the one sanctioned recap.
Writer rule: draft, then list the facts per paragraph and cut repeats before reporting. Reviewer rule: flag any paragraph whose fact list is a subset of earlier ones.
