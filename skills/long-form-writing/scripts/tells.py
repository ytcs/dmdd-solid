#!/usr/bin/env python3
"""Word- and phrase-level tells of machine-written prose (prose-review patterns 0, 6, 8, 13, 17-19, 22, 24-26, 28).

Usage: tells.py FILE.tex [FILE.tex ...]     prints file:line, tell, context; then counts per 1000 words
Complements lint.py (banned vocabulary, long sentences, monotony) and binding.py (pattern 27, sentence
construction). A hit is a candidate, not a verdict: read the sentence and decide. Math, labels, references and
citations are stripped first, so hits are in prose. Technical uses of a flagged word stay.
"""
import re
import sys
from collections import Counter
from pathlib import Path

R = {
    # cleft and pseudo-cleft constructions ("What X needs is Y")
    "cleft": r"(?:^|[.;]\s+)What (?:\w+[ -]){1,7}(?:is|are|was|were)\b(?! (?:the |a )?(?:same|ratio|rate|energy|value|number|probability|fraction|scale)\b)",
    # negation framing and false contrast
    "not-X-but-Y": r"\bnot (?:just |merely |only |simply )?[^.,;:]{2,45},? but (?:rather )?\b",
    "X-not-Y": r", not (?:a|an|the|by|from|in|on|at|its|their|as|through|for|with|to|what|how|one)\b[^.;]{0,40}[.;]",
    "rather-than-merely": r"\brather than (?:merely|simply|just)\b",
    "no-more-than": r"\b(?:does|do) (?:little|nothing) more than\b|\bnothing (?:more|else) than\b",
    # metaphor verbs and figurative nouns standing in for technical statements
    "metaphor-verb": r"\b(?:earns? (?:its|their) (?:place|keep)|pays? (?:off|for itself)|turns? on (?:the|a|whether|how)|has no standing|carr(?:y|ies) the (?:weight|burden|argument|story|day)|lives? (?:in|on|inside) (?:the|a|one)|does the (?:job|work|heavy lifting)|buys?\b|at stake|the price (?:of|is)|hands? (?:it|them|over) (?:to|back)|takes over\b|steps in\b|kicks in\b|comes? into play|enters? the picture|sets? the stage|paves? the way|opens? the door|holds? the key|tells? the (?:story|whole)|the (?:whole|full) story|the story\b|the bottom line|the upshot|the catch\b|the trick\b|the punchline)",
    # reader-directed and process phrases
    "reader-phrase": r"\b(?:the|a|our) reader (?:needs|must|should|can|will|may|has)\b|\bwhat a reader\b|\bone fact (?:a|the) reader\b|\bthe one (?:fact|number|thing) (?:a|the|that)\b",
    "read-one-at-a-time": r"\bread (?:one|two) at a time\b|\btaken one at a time\b|\bread together\b",
    "self-narration": r"\b(?:we (?:now )?(?:turn to|state|note|recall|emphasi[sz]e|stress|highlight|summari[sz]e)|as (?:we )?(?:noted|mentioned|discussed|shown) (?:above|earlier|before)|here we|in what follows|below we)\b",
    "evaluation": r"\b(?:remarkabl[ye]|strikingly?|surprisingly|crucially|importantly|interestingly|notably|naturally,|of course|indeed,|in fact,|clearly|obviously|simply put|in short|in other words|put differently|that is to say|it turns out|as it happens|the key (?:point|fact|step|ingredient|insight)|key insight|no accident|not a coincidence|by no means|far from)\b",
    "sufficient-but": r"\b(?:sufficient|necessary|correct|exact|true|right|safe|clean|valid) but (?:loose|crude|weak|rough|slow|expensive|incomplete|limited)\b",
    "count-teaser": r"(?:^|[.]\s+)(?:Two|Three|Four|Five|Six|Several) (?:\w+ ){0,3}(?:matter|follow|stand out|remain|are needed|differ|deserve|are worth|deserve mention|come from|are left)\b",
    "colon-reveal": r"\b(?:The (?:answer|reason|point|catch|upshot|difference|result|lesson|moral|surprise))(?: is)?:",
    "sentence-final-alone": r"\b(?:at all|on its own|by itself|in itself|in its own right)\.",
    "honest-figurative": r"\b(?:honest(?:ly)?|clean(?:ly)? (?:split|separation|answer|number|result|picture)|sharp(?:ly)? (?:answer|statement|picture)|tidy|neat(?:ly)?|elegant(?:ly)?|beautiful(?:ly)?|powerful|robust(?:ly)?|subtle|delicate|nontrivial|non-trivial|rich (?:structure|physics))\b",
    "double-negative": r"\bnot (?:un\w+|in\w+able|without)\b|\bno (?:\w+ ){0,2}without\b",
    "hedge-stack": r"\b(?:may|might|could) (?:perhaps|possibly|potentially|conceivably)\b|\b(?:somewhat|rather|fairly|quite|relatively) (?:small|large|close|similar|different|important)\b",
    "intensifier": r"\b(?:very|extremely|highly|truly|really|precisely|exactly|entirely|completely|fully|vastly|hugely) (?:\w+)\b",
    "em-dash": r"---",
}
COMP = {k: re.compile(v, re.I if k not in ("cleft", "count-teaser") else 0) for k, v in R.items()}


def prose(text):
    t = re.sub(r"(?<!\\)%.*", "", text)
    t = re.sub(r"(?s)\\begin\{(equation|align|gather|multline|eqnarray|tabular|longtable)\*?\}.*?\\end\{\1\*?\}", " EQN ", t)
    t = re.sub(r"\\\[.*?\\\]", " EQN ", t, flags=re.S)
    t = re.sub(r"\$[^$]*\$", " M ", t)
    t = re.sub(r"\\(?:c|C)ref(?:range)?\*?\{[^}]*\}(?:\{[^}]*\})?|\\(?:eq)?ref\{[^}]*\}|\\label\{[^}]*\}|\\cites?(?:\[[^\]]*\])*\{[^}]*\}", " REF ", t)
    t = re.sub(r"\\SI\{[^}]*\}\{[^}]*\}|\\num\{[^}]*\}", " NUM ", t)
    t = re.sub(r"\\(?:emph|textit|textbf|mathrm|text)\{([^}]*)\}", r"\1", t)
    return t


def scan(path):
    hits = []
    for i, line in enumerate(path.read_text().splitlines(), 1):
        p = prose(line)
        if len(p.split()) < 4:
            continue
        for k, rx in COMP.items():
            for m in rx.finditer(p):
                if k == "em-dash" and (p.count("---") < 2 or "&" in p):
                    continue
                if k == "intensifier" and m.group(0).lower().split()[0] in ("exactly", "precisely", "entirely", "completely", "fully"):
                    continue  # technical ("exactly solvable", "fully screened") too common to flag
                s = max(0, m.start() - 50)
                hits.append((i, k, p[s:m.end() + 40].strip()))
                break
    return hits


def main(argv):
    files = [a for a in argv if not a.startswith("-")]
    if not files:
        print(__doc__)
        return 0
    cnt, words = Counter(), 0
    for f in files:
        words += len(prose(Path(f).read_text()).split())
        for i, k, ctx in scan(Path(f)):
            cnt[k] += 1
            print(f"{f}:{i}\t{k}\t{ctx}")
    tot = sum(cnt.values())
    print(f"TOTAL: {tot} hits in {words} words ({1000 * tot / max(words, 1):.1f} per 1000 words)  "
          + ", ".join(f"{k} {n}" for k, n in cnt.most_common()))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
