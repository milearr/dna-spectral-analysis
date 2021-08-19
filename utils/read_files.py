import os
import ast 

def read_fasta(file): 
    with open(file) as f:
        seq = ''
        for line in f:
            if line!= '\n' and line[0]!= '>':
                seq += line[:-1]
    return seq

def read_intergenic(file, min_length_seq): 
    seq = read_fasta(file + '.fasta')
    data = dict()
    pos_min = 0
    tag = 0
    with open(file + '-coding_sequence.txt', 'r') as f:
        for line in f:
            if line[0] == '>':
                locus_tag = file.split('/')[-1] + '-intergenic-' + str(tag)
                tag += 1
                location = line.split('location=')[1].split(']')[0]
                index = location.split(')')[0].split('(')[-1].split('..')
                index = [idy for idx in index for idy in idx.split(',')]
                seq_aux = seq[pos_min:int(index[0])-1]
                pos_min = int(index[-1])
                if len(seq_aux) > min_length_seq:
                    data[locus_tag] = seq_aux
    return data

def read_cds(file, min_length_seq): 
    data = dict()
    with open(file + '-coding_sequence.txt', 'r') as f:
        for line in f:
            if line[0] == '>':
                try:
                    if len(data[locus_tag]) <= min_length_seq:
                        del data[locus_tag]
                except:
                    pass
                locus_tag = line.split('locus_tag=')[1].split(']')[0]
                data[locus_tag] = ''
            if line!= '\n' and line[0]!= '>':
                data[locus_tag] += line[:-1]
    return data

def read_dir_database(path, min_length_seq):
    dirr = os.listdir(path)
    data_cds = dict()
    data_intergenic = dict()

    for file in dirr:
        filename, format_file = os.path.splitext(file)
        if format_file == '.fasta' and filename + '-coding_sequence.txt' not in dirr:
            raise FileNotFoundError('file ' + filename + '-coding_sequence.txt can not be found!')
        elif format_file == '.fasta':
            data_cds.update(read_cds(path+filename, min_length_seq))
            data_intergenic.update(read_intergenic(path+filename, min_length_seq))

    return data_cds, data_intergenic

def read_summarized_results(file):
    data = dict()
    with open(file, 'r') as f:
        for line in f:
            aux = line[:-1].split('\t\t')
            gene = aux[0][1:]
            data[gene] = ast.literal_eval(aux[1])
    return data