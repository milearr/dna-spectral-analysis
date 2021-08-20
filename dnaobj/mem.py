from .dnasequence import *
from .spectralanalysis import *

class Mem(DnaSequence):
    def __init__(self, seq):
        super().__init__(seq)
        self.method = "MEM"
        self.dimension = 1
        self.signal = self.binary_indicator
        self.Xsignal = SpectralAnalysis(self).dna_fourier()
        self.label = self.optimization()
        self.signal = self.mapping(self.label) 
    
    def optimization(self):
        map_opt = None
        H_old = np.inf
        hM = 1 / 2
        N0 = 201
        delta_h = 2*hM / (N0 - 1)
        XA, XC, XG, XT = self.Xsignal
        mid = self.N // 2
        
        for na in range(N0):
            for nc in range(N0):
                if na != nc:
                    a = na * delta_h - hM
                    c = nc * delta_h - hM
                    g = - (a*(XA[mid]-XA[0]*XT[mid]/XT[0]) +  c*(XC[mid]-XC[0]*XT[mid]/XT[0])) / (XG[mid]-XG[0]*XT[mid]/XT[0])
                    t = - (a*XA[0]+c*XC[0]+g*XG[0]) / XT[0]

                    X = a*XA + c*XC + g*XG + t*XT
                    S = abs(X)**2
                    ePX = sum(S)
                    pX = S/ePX
                    H_new = -sum([k*np.log(k) for k in pX if k > 0])

                    if H_new < H_old:
                        H_old = H_new
                        map_opt = (a, c, g, t)
        
        if map_opt != None:
            a,c,g,t = map_opt
            energy = a**2* sum(XA) + c**2* sum(XC) + g**2* sum(XG) + t**2* sum(XT)
            a = a/np.sqrt(energy)
            c = c/np.sqrt(energy)
            g = g/np.sqrt(energy)
            t = t/np.sqrt(energy)
            return {"A": a, "C": c, "G": g, "T": t}
        else:
            return {"A": 0, "C": 0, "G": 0, "T": 0}