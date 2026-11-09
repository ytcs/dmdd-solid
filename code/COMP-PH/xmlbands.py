import sys, numpy as np, xml.etree.ElementTree as ET
def read(f):
    r=ET.parse(f).getroot(); HA=27.211386
    alat=float(r.find('.//atomic_structure').get('alat'))
    K=[];E=[]
    for ks in r.iter('ks_energies'):
        K.append([float(x) for x in ks.find('k_point').text.split()]); E.append([float(x)*HA for x in ks.find('eigenvalues').text.split()])
    return alat,np.array(K),np.array(E)
if __name__=='__main__':
    alat,K,E=read(sys.argv[1]); nv=int(sys.argv[2])
    vbm=E[:,nv-1].max(); ic=E[:,nv].argmin()
    print('nk',len(K),'VBM',round(vbm,4),'at',K[E[:,nv-1].argmax()],'CBM at',K[ic],'Eg',round(E[ic,nv]-vbm,4))
    for lab,k in [('G',[0,0,0]),('X',[1,0,0]),('L',[.5,.5,.5])]:
        i=np.where(np.all(abs(K-k)<1e-4,1))[0]
        if len(i): i=i[0]; print(lab,'c-VBM',np.round(E[i,nv:nv+3]-vbm,4),'v-VBM',np.round(E[i,max(0,nv-3):nv]-vbm,4))
    np.savetxt(sys.argv[3],np.column_stack([K,E]),fmt='%.6f') if len(sys.argv)>3 else None
