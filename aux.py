# from scripts import initialization
from dnaobj import *
# import dnaobj

dna = Voss('agcgcgtag')
spec = SpectralAnalysis(dna)
res = spec.results(graph=True)

print(dna.N)

# from scripts import *
# a = initialize()