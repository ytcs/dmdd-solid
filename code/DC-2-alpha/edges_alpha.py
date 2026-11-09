import re,sys
print('alpha      G      L      X   dSO(G)   order')
for f in sys.argv[1:]:
    t=open(f,errors='ignore').read(); i=t.rfind('End of self-consistent calculation')
    if i<0: print(f,'no result'); continue
    t=t[i:]
    B=re.findall(r'k =\s*(-?[\d.]+)\s*(-?[\d.]+)\s*(-?[\d.]+)\s*\(.*?\n\n(.*?)\n\n',t,flags=re.S)
    r=[(tuple(float(x) for x in k[:3]),[float(x) for x in re.findall(r'-?\d+\.\d+',k[3])]) for k in B]
    v=max(e[27] for _,e in r); o={}
    for k,e in r:
        n=sum(x*x for x in k)
        if n<1e-8: o['G']=e[28]-v; o['so']=e[27]-e[23]; 
        if abs(n-.75)<1e-6: o['L']=e[28]-v
        if abs(n-1)<1e-6: o['X']=e[28]-v
    a=re.search(r'\.a([\d.]+)\.out',f); a=a.group(1) if a else 'ref'
    print(f"{a:6s} {o['G']:6.3f} {o['L']:6.3f} {o['X']:6.3f} {o['so']:6.3f}  {'L<G' if o['L']<o['G'] else 'G<L'}")
