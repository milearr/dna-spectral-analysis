import numpy as np
import matplotlib.pyplot as plt

from .dnasequence import *

class SpectralAnalysis:
    def __init__(self, obj):
        self.N = obj.N
        self.signal = obj.signal
        self.dimension = obj.dimension
        self.description = obj.__str__()
        self.binary_indicator = obj.binary_indicator

    def dna_fourier(self):
        Xsignal = np.fft.fft(self.signal)     
        return Xsignal

    def envelope_spectral(self, Xsignal, k):
        Ui = np.array([[Xsignal[0][k], Xsignal[1][k], Xsignal[2][k], Xsignal[3][k]]])
        cov = np.matmul(Ui.conjugate().T,Ui)
        _, eigvec = np.linalg.eigh(cov)
        mapping = eigvec[:,-1]
        label = {"A": mapping[0], "C": mapping[1], "G": mapping[2], "T": mapping[3]}
        return label

    def spectral_energy(self, normalized=False):
        Xsignal = self.dna_fourier()
        freq = np.fft.fftfreq(self.N)
        if self.dimension == 1:
            S = abs(Xsignal)**2
        else: # Voss method
            S = abs(Xsignal[0])**2 + abs(Xsignal[1])**2 + abs(Xsignal[2])**2 + abs(Xsignal[3])**2
        if normalized == True:
            S = S/max(S)
        return freq, S
    
    def one_sided_energy(self, dc_value=False, normalized=False):
        freq, S = self.spectral_energy()
        mid = self.N//2
        Sdc = S[0]
        if self.N % 2 == 0:
            S = S[1:mid] + np.flip(S[mid+1:])
            freq = freq[:mid]
        else:
            S = S[1:mid+1] + np.flip(S[mid+1:])
            freq = freq[:mid+1]
        if dc_value == True:
            S = np.concatenate([np.array([Sdc]), S])
        else:
            S = np.concatenate([np.array([0]), S])
        if normalized == True:
            S = S/max(S)
        return freq, S

    def snr(self):
        _, S = self.one_sided_energy()
        Pfund = S[np.argmax(S)]
        totalNoise = sum(S) - Pfund
        r = 10*np.log10(Pfund / totalNoise)
        return r
    
    def entropy(self):
        _, S = self.one_sided_energy()
        ePX = sum(S)
        pX = S/ePX
        H = -sum([k*np.log(k) for k in pX if k > 0])
        return H

    def check_exon(self):
        freq, S = self.one_sided_energy()
        maxS = np.argmax(S)
        freqS = freq[maxS]
        if  freqS > 1/3-0.02 and freqS < 1/3+0.02:
            return True
        else:
            return False

    def results(self, graph=False):
        freq, S = self.one_sided_energy(normalized=True)
        snr = self.snr()
        H = self.entropy()
        check = self.check_exon()
        res = {'freq':freq, 'S':S, 'snr':snr,
                'H':H, 'exon':check}
        if graph == True:
            plt.title(f"H = {H:.2f}nats SNR = {snr:.2f}dB")
            plt.plot(freq,S)
            plt.show()
        return res