import os

def save_results_file_mode(file, method, results):
    with open(file, 'a') as f:
        f.write('\n'*2 + 'M: ' + method.lower())
        for key in results:
            if key in ('freq', 'S'):
                string = ''.join(map(lambda x: '{:>9}'.format(round(x,4)), results[key]))
            elif key in ('snr', 'H'):
                string = '{:>9}'.format(round(results[key],2))
            else:
                string = '{:>9}'.format(str(results[key]))
            f.write('\n' + '{:>5}'.format(key) + string )
    return None

def write_summarized_results_database(path):
    try:
        os.mkdir(path + 'results-summarized')
    except:
        pass
    open(path + 'results-summarized/intergenic.txt', 'w') 
    open(path + 'results-summarized/cds.txt', 'w') 
    dirr = os.listdir(path + 'results/')
    for file in dirr:
        check = {'voss':0, 'eiip':0, 'mem':0, 'qpsk':0, 'alg1':0, 'alg2':0}
        with open(path + 'results/' + file, 'r') as f:
            for line in f:
                if 'M: ' in line:
                    method = line[3:-1]
                if 'exon' in line:
                    if 'True' in line:
                        check[method] = True
                    else:
                        check[method] = False
        if '-intergenic-' in file:
            with open(path + 'results-summarized/intergenic.txt', 'a') as f:    
                f.write('>' + os.path.basename(file)[:-4] + '\t'*2 + str(check) + '\n')
        else:
            with open(path + 'results-summarized/cds.txt', 'a') as f:    
                f.write('>' + os.path.basename(file)[:-4] + '\t'*2 + str(check) + '\n')
    return None

def write_statistics(dict_res, path, methods):
    try:
        os.mkdir(path + 'results-statistics')
    except:
        pass
    with open(path + 'results-statistics/results.txt', 'w') as f:
        for mtd in methods:
            f.write('method: ' + mtd.lower() + '\n')
            for line in dict_res:
                f.write('{:>12}'.format(str(line)) + '\t' + str(dict_res[line][mtd]) + '\n')
            f.write('\n')        
    return None