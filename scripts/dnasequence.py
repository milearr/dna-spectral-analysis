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