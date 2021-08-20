from .dnasequence import *

class Qpsk(DnaSequence):
    def __init__(self, seq):
        super().__init__(seq)
        self.method = "QPSK"
        self.dimension = 1
        self.label = {"A": 1+1j, "C": -1-1j, "G": -1+1j, "T": 1-1j}
        self.signal = self.mapping(self.label) 