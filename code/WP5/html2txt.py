"""Extract text from arXiv HTML (LaTeXML) keeping math alttext. Usage: python -I html2txt.py in.html out.txt"""
import sys, re, html
s = open(sys.argv[1], encoding='utf-8', errors='ignore').read()
s = re.sub(r'<math[^>]*alttext="([^"]*)"[^>]*>.*?</math>', lambda m: ' $'+html.unescape(m.group(1))+'$ ', s, flags=re.S)
s = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', s, flags=re.S)
s = re.sub(r'<span class="ltx_tag ltx_tag_equation[^"]*">(.*?)</span>', r' [EQ \1] ', s, flags=re.S)
s = re.sub(r'</(p|div|tr|h\d|li|table)>', '\n', s)
s = re.sub(r'<[^>]+>', '', s)
s = html.unescape(s)
s = re.sub(r'[ \t]+', ' ', s); s = re.sub(r'\n\s*\n+', '\n', s)
open(sys.argv[2], 'w').write(s)
