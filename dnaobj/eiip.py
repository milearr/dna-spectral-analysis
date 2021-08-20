from .dnasequence import *

class Eiip(DnaSequence):
    def __init__(self, seq):
        super().__init__(seq)
        self.method = "EIIP"
        self.dimension = 1
        self.label = {"A": 0.1260, "C": 0.1340, "G": 0.0806, "T": 0.1335}
        self.signal = self.mapping(self.label)