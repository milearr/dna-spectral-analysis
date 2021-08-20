import numpy as np
from .spectralanalysis import SpectralAnalysis

class DnaSequence:
    def __init__(self, seq):
        self.seq = seq.upper()
        self.N = len(seq)
        self.method = None
        self.dimension = 1
        self.signal = None
        self.binary_indicator = None 

    def __str__(self):
        return f"The sequence has {self.N}bp and was mapped using {self.method}"

    @property
    def binary_indicator(self):
        return self.__binary_indicator
    @binary_indicator.setter
    def binary_indicator(self, value):
        value = np.zeros((4,self.N), dtype=float) 
        for i in range(self.N):
            if self.seq[i] == "A": value[0][i] = 1
            if self.seq[i] == "C": value[1][i] = 1
            if self.seq[i] == "G": value[2][i] = 1
            if self.seq[i] == "T": value[3][i] = 1 
        self.__binary_indicator = value
    
    def mapping(self, label=None):
        if label == None:
            return self.binary_indicator
        else:
            return label["A"]*self.binary_indicator[0] + label["C"]*self.binary_indicator[1] + label["G"]*self.binary_indicator[2] + label["T"]*self.binary_indicator[3]

class Voss(DnaSequence):
    def __init__(self, seq):
        super().__init__(seq)
        self.method = "Voss"
        self.dimension = 4
        self.label = None
        self.signal = self.mapping(self.label)
        
class Eiip(DnaSequence):
    def __init__(self, seq):
        super().__init__(seq)
        self.method = "EIIP"
        self.dimension = 1
        self.label = {"A": 0.1260, "C": 0.1340, "G": 0.0806, "T": 0.1335}
        self.signal = self.mapping(self.label)

class Qpsk(DnaSequence):
    def __init__(self, seq):
        super().__init__(seq)
        self.method = "QPSK"
        self.dimension = 1
        self.label = {"A": 1+1j, "C": -1-1j, "G": -1+1j, "T": 1-1j}
        self.signal = self.mapping(self.label)  

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

class AlgI(DnaSequence):
    def __init__(self, seq):
        super().__init__(seq)
        self.method = "Alg.I"
        self.dimension = 1
        self.signal = self.binary_indicator
        self.Xsignal = SpectralAnalysis(self).dna_fourier()
        self.label = SpectralAnalysis(self).envelope_spectral(self.Xsignal, k=self.N//3)
        self.signal = self.mapping(self.label)  
    
class AlgII(DnaSequence):
    def __init__(self, seq):
        super().__init__(seq)
        self.method = "Alg.II"
        self.dimension = 1
        self.signal = self.binary_indicator
        self.Xsignal = SpectralAnalysis(self).dna_fourier()
        self.label = self.optimization()
        self.signal = self.mapping(self.label)

    def optimization(self):
        snr_ref = -np.inf
        label_ref = np.zeros(4)
        for delta in range(self.N//2 + 1):
            mapping = SpectralAnalysis(self).envelope_spectral(self.Xsignal, k=delta)
            self.signal = self.mapping(mapping)
            SNR = SpectralAnalysis(self).snr()
            if SNR >= snr_ref:
                snr_ref = SNR
                label_ref = mapping
        return label_ref
