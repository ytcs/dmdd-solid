import numpy as np, core as c, time
print("closed vs direct at complex z; Ward identity z*Rnn = Rjn; parity channels")
print(" y gamma Q | P33 dir, P33 closed | Ptilde dir, Ptilde closed | rel | P32*P23 sign | ward | |P31|,|P21|")
for (y,g,Q) in [(2.2,0.05,5.64),(2.2,0.01,5.64),(1.9,0.0,5.64),(1.5,0.0,3.0),(3,0.02,7.69),(5,0.02,12.82),(10,0.05,25.64),(2.2,0.02,9.7),(2.02,0.01,7.8),(0.3,0.0,1.0),(4,0.05,1.5),(2.5,0.02,30.0)]:
    z=complex(y,g); t=time.time()
    d=c.direct(z,Q)
    Pt=d['P33']+d['P32']*d['P23']/d['Dn']
    p,pt,F,UF=c.closed(z,Q,ns=30)
    Rj=d['Pj3']+d['Pj2']*d['P23']/d['Dn']
    print(y,g,Q,'| %.6f%+.6fj %.6f%+.6fj | %.6f%+.6fj %.6f%+.6fj | %.1e | %.3e | ward %.2e bare %.2e | %.1e %.1e | %.0fs'%(d['P33'].real,d['P33'].imag,p.real,p.imag,Pt.real,Pt.imag,pt.real,pt.imag,abs(Pt-pt)/abs(pt),abs(d['P32']+d['P23'])/abs(d['P32']),abs(z*Pt-Rj)/abs(z*Pt),abs(z*d['P33']-d['Pj3'])/abs(z*d['P33']),abs(d['P31']),abs(d['P21']),time.time()-t),flush=True)
