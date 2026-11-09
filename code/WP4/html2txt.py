"""Convert arXiv (LaTeXML) HTML to plain text, replacing <math> by its LaTeX alttext. Usage: python3 -I html2txt.py in.html out.txt"""
import sys, re, html
s = open(sys.argv[1], encoding='utf-8', errors='replace').read()
s = re.sub(r'(?s)<head>.*?</head>', '', s)
s = re.sub(r'(?s)<math[^>]*?alttext="([^"]*)"[^>]*>.*?</math>', lambda m: ' $' + m.group(1) + '$ ', s)
s = re.sub(r'(?s)<span class="ltx_tag ltx_tag_equation[^"]*">(.*?)</span>', r' [EQ \1] ', s)
s = re.sub(r'(?s)<(script|style).*?</\1>', '', s)
s = re.sub(r'<(br|p|div|tr|h\d|li)[^>]*>', '\n', s)
s = re.sub(r'<[^>]+>', '', s)
s = html.unescape(s)
s = re.sub(r'[ \t]+', ' ', s); s = re.sub(r'\n\s*\n+', '\n', s)
open(sys.argv[2], 'w').write(s)
