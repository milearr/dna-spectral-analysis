from .dnasequence import *
from .spectralanalysis import *

class SNR_SE(DnaSequence):
    def __init__(self, seq):
        super().__init__(seq)
        self.method = "SNR-SE"
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