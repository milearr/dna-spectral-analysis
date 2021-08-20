import numpy as np

class DnaSequence:
    def __init__(self, seq):
        self.seq = seq.upper()
        self.N = len(seq)
        self.method = None
        self.dimension = 1
        self.signal = None
        self.binary_indicator = None 

    def __str__(self):
        return f'The sequence has {self.N}bp and was mapped using {self.method}'

    @property
    def binary_indicator(self):
        return self.__binary_indicator
    @binary_indicator.setter
    def binary_indicator(self, value):
        value = np.zeros((4,self.N), dtype=float) 
        for i in range(self.N):
            if self.seq[i] == 'A': value[0][i] = 1
            if self.seq[i] == 'C': value[1][i] = 1
            if self.seq[i] == 'G': value[2][i] = 1
            if self.seq[i] == 'T': value[3][i] = 1 
        self.__binary_indicator = value
    
    def mapping(self, label=None):
        if label == None:
            return self.binary_indicator
        else:
            return label['A']*self.binary_indicator[0] + label['C']*self.binary_indicator[1] + label['G']*self.binary_indicator[2] + label['T']*self.binary_indicator[3]