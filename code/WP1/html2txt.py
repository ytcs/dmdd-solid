"""Convert arXiv LaTeXML HTML to plain text, keeping LaTeX alttext for math and equation tags.
Usage: python3 -I html2txt.py in.html out.txt   (stdlib only)"""
import sys, re
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.out = []; self.skip = 0; self.inmath = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'math':
            self.out.append(' $' + (a.get('alttext') or '') + '$ '); self.inmath += 1; return
        if self.inmath: return
        if tag in ('script', 'style'): self.skip += 1
        if tag in ('p', 'div', 'tr', 'h1', 'h2', 'h3', 'h4', 'li', 'table'): self.out.append('\n')
        cls = a.get('class') or ''
        if 'ltx_tag_equation' in cls: self.out.append(' [EQTAG] ')
    def handle_endtag(self, tag):
        if tag == 'math': self.inmath -= 1; return
        if self.inmath: return
        if tag in ('script', 'style'): self.skip -= 1
    def handle_data(self, d):
        if self.skip or self.inmath: return
        self.out.append(d)

p = P(); p.feed(open(sys.argv[1], encoding='utf-8', errors='ignore').read())
t = ''.join(p.out); t = re.sub(r'[ \t]+', ' ', t); t = re.sub(r'\n\s*\n+', '\n', t)
open(sys.argv[2], 'w').write(t)
