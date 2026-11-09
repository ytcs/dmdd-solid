"""Independent SVG path reader for pdftocairo output (referee). No reuse of the DC-* parser."""
import re, numpy as np
num=r'-?\d+\.?\d*(?:e-?\d+)?'
def load(fn):
    s=open(fn).read(); out=[]
    # track <g ... transform> is not needed for matplotlib/MMA? pdftocairo puts transform on each path
    for m in re.finditer(r'<path\b([^>]*?)/?>',s):
        a=m.group(1)
        g=lambda k:(re.search(r'(?:^|\s)%s="([^"]*)"'%k,a) or [None,None])[1]
        d=g('d'); st=g('stroke'); tr=g('transform')
        if d is None: continue
        toks=re.findall(r'[MLCZHVmlczhv]|'+num,d); pts=[];subs=[];i=0;cmd=None
        while i<len(toks):
            t=toks[i]
            if t in 'MLCZ':
                cmd=t;i+=1
                if t=='Z': continue
            if cmd=='M':
                if pts: subs.append(pts)
                pts=[(float(toks[i]),float(toks[i+1]))];i+=2;cmd='L'
            elif cmd=='L': pts.append((float(toks[i]),float(toks[i+1])));i+=2
            elif cmd=='C': pts.append((float(toks[i+4]),float(toks[i+5])));i+=6
            else: i+=1
        if pts: subs.append(pts)
        M=None
        if tr:
            v=re.findall(num,tr)
            if tr.startswith('matrix'): M=[float(x) for x in v]
        for q in subs:
            q=np.array(q)
            if M: q=np.c_[M[0]*q[:,0]+M[2]*q[:,1]+M[4],M[1]*q[:,0]+M[3]*q[:,1]+M[5]]
            out.append(dict(stroke=st,dash=g('stroke-dasharray'),w=g('stroke-width'),pts=q))
    return out
