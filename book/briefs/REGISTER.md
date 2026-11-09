# Book brief REGISTER: distil the register model for *Dark Matter Detection in Solids*

The user wants the book to read like human expert exposition in the field, with the field's own parlance and colloquial precision. The primary register model is **Tongyan Lin, "Dark matter models and direct detection", TASI lectures, arXiv:1904.07915**. Secondary models:
- **Kahn & Lin, "Searches for light dark matter using condensed matter systems", arXiv:2108.03239**, for the condensed-matter and DM interface;
- **one classic condensed-matter exposition known for clear writing**, which you choose and justify from those with open text. Examples: Giustino's electron–phonon RMP, arXiv:1603.06965, or Baroni et al.'s DFPT RMP, arXiv:cond-mat/0012092. It serves for Part I solid-state chapters such as lattice dynamics, e–ph coupling and response.

Fetch the full texts with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/register/. Delete the PDFs and keep the text extracts.

Read them closely, especially the passages that explain physics rather than list results. Then write **/home/user/dmdd-solid/book/REGISTER.md** following /home/user/dmdd-solid/skills/long-form-writing/references/prose-review.md, "Language and register checks". It must contain:
1. **The register in a paragraph.** How these authors sound: person, tone, sentence length, how much they hedge, how they move from picture to formula.
2. **Terms of art.** A table of the field's working vocabulary: term → how the register model uses it → what to avoid instead. Examples: heavy and light mediator, reach, threshold, kinematic matching, in-medium effects, screening, Migdal effect, phonon-assisted, form factor, exposure, background-free. About 40–60 entries, each with a quoted example and page reference.
3. **Characteristic moves**, each with 2–3 quoted examples (page refs):
   - how they introduce a parametric estimate before an exact result;
   - how they give a physical picture;
   - how they motivate a calculation;
   - how they signal an approximation and its validity;
   - how they compare channels;
   - how they handle numbers ("roughly", "of order", "a few");
   - how they close a section.
4. **Idioms and connectives they actually use**, with frequencies where you can count them: "for concreteness", "to see this", "it turns out", "the upshot", "in practice", "roughly speaking", "parametrically", and so on. Also connectives and constructions they avoid.
5. **Ten before → after rewrites.** Pick sentences from the book's current Chapter 1 and Section 2.1 (/home/user/dmdd-solid/book/tex/ch01/*.tex, /home/user/dmdd-solid/book/tex/ch02/s2-1.tex) that miss the register, and rewrite each as the model author would. Physics unchanged. This calibrates the writers.
6. **A short checklist** for writers and prose reviewers. It is the concrete form of the skill's register checks for this book.
7. **Where the book deliberately differs** from the model: notation (NOTATION.md wins), the no-exercises rule, a more complete derivation density than lecture notes. The book is more complete than the lectures, but uses the same voice.

**Rules.** The output is distilled usage, not a copy: short quotes only, with page references. Write only REGISTER.md and the sources folder. Do not commit. Final message ≤ 8 lines.
