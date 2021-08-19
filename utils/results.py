import os
from project.dnasequence import *
from .write_files import*

def seq_analysis(args, seq):
    methods = args.methods
    name = os.path.basename(os.path.splitext(args.file)[0])
    try:
        os.mkdir(args.dir + 'results')
    except:
        pass
    file = args.dir + 'results/' + name + '.txt'
    with open(file, 'w') as f:    
        f.write('>' + name + '\n')
        f.write('N: ' + str(len(seq)) + '\n')
        f.write('Methods: ' + ', '.join(methods))
    
    for mtd in methods:
        if mtd == 'voss':
            dna = Voss(seq)
        elif mtd == 'eiip':
            dna = Eiip(seq)
        elif mtd == 'qpsk':
            dna = Qpsk(seq)
        elif mtd == 'alg1':
            dna = AlgI(seq)
        elif mtd == 'alg2':
            dna = AlgII(seq)
        spectral_seq = SpectralAnalysis(dna)
        res = spectral_seq.results(graph=args.plot)
        save_results_file_mode(file, mtd, res)
    return res

def database_analysis(args, database):
    for tag in database:
        args.file = tag + '.fasta'
        _ = seq_analysis(args, database[tag])
    return None