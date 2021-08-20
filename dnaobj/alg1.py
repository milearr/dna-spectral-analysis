from .dnasequence import *
from .spectralanalysis import *

class AlgI(DnaSequence):
    def __init__(self, seq):
        super().__init__(seq)
        self.method = "Alg.I"
        self.dimension = 1
        self.signal = self.binary_indicator
        self.Xsignal = SpectralAnalysis(self).dna_fourier()
        self.label = SpectralAnalysis(self).envelope_spectral(self.Xsignal, k=self.N//3)
        self.signal = self.mapping(self.label) 