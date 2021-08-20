from .dnasequence import *

class Voss(DnaSequence):
    def __init__(self, seq):
        super().__init__(seq)
        self.method = "Voss"
        self.dimension = 4
        self.label = None
        self.signal = self.mapping(self.label)