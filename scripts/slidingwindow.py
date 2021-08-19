import os
from .dnasequence import *
from utils import *
import matplotlib.pyplot as plt


def sliding_window(args, seq):
    window_length = args.window
    step = args.step
    start = window_length//2
    position = np.arange(start, len(seq)-start, step)
    n = len(position)

    name = os.path.basename(os.path.splitext(args.file)[0])
    try:
        os.mkdir(args.dir + 'results')
    except:
        pass
    file = args.dir + 'results/' + name + '-sliding-window.txt'
    with open(file, 'w') as f:    
        f.write('>' + name + '\n')
        f.write('N: ' + str(len(seq)) + '\n')
        f.write('Methods: ' + ', '.join(args.methods))    
    
    for mtd in args.methods:
        S3 = np.zeros(n)
        check = np.zeros(n)
        for idx in range(n):
            center = start + idx*step
            window_seq = seq[center-start:center+start+1]

            if mtd == 'voss':
                dna = Voss(window_seq)
            elif mtd == 'eiip':
                dna = Eiip(window_seq)
            elif mtd == 'qpsk':
                dna = Qpsk(window_seq)
            elif mtd == 'alg1':
                dna = AlgI(window_seq)
            elif mtd == 'alg2':
                dna = AlgII(window_seq)
            
            spectral_seq = SpectralAnalysis(dna)
            _, S = spectral_seq.one_sided_energy()
            check[idx] = spectral_seq.check_exon()
            S3[idx] = S[window_length//3]
        S3 = S3/max(S3)
        chk = ''.join(map(lambda x: '{:>9}'.format(str(x)), check))
        pos = ''.join(map(lambda x: '{:>9}'.format(str(x)), position))
        res = {'pos': pos, 'S':S3, 'exon':chk}
        save_results_file_mode(file, mtd, res)
        
        if args.plot == True:
            plt.title(mtd.upper())
            plt.stem(position, check, markerfmt='r,', linefmt='r-')
            plt.plot(position, S3, 'k')
            plt.show()

    return None