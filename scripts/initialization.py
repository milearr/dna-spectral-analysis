import argparse
import os

def argparse_check_file(file):
    _, file_extension = os.path.splitext(file)
    if not os.path.isfile(file):
        raise argparse.ArgumentTypeError(file + ' is not a valid file name')
    elif file_extension not in ('.fasta',):
        raise argparse.ArgumentTypeError(file_extension + ' is not a valid format')
    else:
        return file

def argparse_check_dir(path):
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(path + ' is not a directory')
    else:
        return path

def argparse_check_dir_summarized(path):
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(path + ' is not a directory')
    elif 'results-summarized' not in os.listdir(path):
        raise argparse.ArgumentTypeError(path + ' is not a valid path')
    else:
        return path

def argparse_check_interval(num):
    num = int(num)
    if num <= 0 or num > 500:
        raise argparse.ArgumentTypeError('must be positive and less than 500')
    else:
        return num

def argparse_check_window(num):
    num = int(num)
    if num % 3 != 0:
        raise argparse.ArgumentTypeError('must divide 3')
    else:
        return num

def initialize():

    parser = argparse.ArgumentParser(
        description='A program to spectral analysis of DNA sequences.',
        formatter_class= argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers(help='')

    parser_file = subparsers.add_parser('file-mode',
                        help='process only one file in FASTA format')
    parser_file.add_argument('file', type=argparse_check_file, 
                        help='file in FASTA format')
    parser_file.add_argument('-p', '--plot', action='store_true', 
                        help = 'plot the energy spectrum of file from the chosen methods')
    parser_file.add_argument('-sw', action='store_true', 
                        help = 'set the sliding window approach')
    parser_file.add_argument('-wl', '--window', metavar='', 
                        type=argparse_check_window, default=351,
                        help = 'window length of sliding window approach '
                        '(default: %(default)s)')
    parser_file.add_argument('-st', '--step', metavar='', type=int, default=1,
                        help = 'step size of sliding window approach '
                        '(default: %(default)s)')


    parser_database = subparsers.add_parser('database-mode',
                        help='process a database from a directory dir')
    parser_database.add_argument('dir', type=argparse_check_dir, 
                        help='directory of the database')
    parser_database.add_argument('-n', type=int, 
                        default=0, dest='min_length_seq', metavar='N',
                        help = 'delete sequences whose length is less than N '
                        '(default: %(default)s)')

    parser_statistic = subparsers.add_parser('statistics-mode',
                        help='process a database from a directory dir')
    parser_statistic.add_argument('dir_statistics', type=argparse_check_dir_summarized, metavar='dir',
                        help='directory of the summarized results')
    parser_statistic.add_argument('-M', type=argparse_check_interval, 
                        default=500,
                        help = 'set the number of sequences drawn to M '
                        '(default: %(default)s)')
    parser_statistic.add_argument('-t', '--times', type=int, 
                        default=10, metavar='',
                        help = 'set the number of draws '
                        '(default: %(default)s)')
    parser_statistic.add_argument('-sd', '--seed', type=int, 
                        default=10, metavar='',
                        help = 'initialize the random number generator '
                        '(default: %(default)s)')    

    parser.add_argument('-v', '--voss', action='store_true', 
                        help = 'set voss method')
    parser.add_argument('-e', '--eiip', action='store_true', 
                        help = 'set eiip mapping')
    parser.add_argument('-k', '--qpsk', action='store_true', 
                        help = 'set qpks mapping')
    parser.add_argument('-g', '--mem', action='store_true', 
                        help = 'set mem mapping')
    parser.add_argument('-f', '--alg1', action='store_true', 
                        help = 'set alg1 mapping')
    parser.add_argument('-s', '--alg2', action='store_true', 
                        help = 'set alg2 mapping')
    parser.add_argument('-a', '--all', action='store_true', 
                        help = 'set all methods: -v, -e, -k, -f, -s')    

    args = parser.parse_args()
    if args.all == True:
        args.voss = True
        args.eiip = True
        args.qpsk = True
        args.mem = True
        args.alg1 = True
        args.alg2 = True
    arguments = vars(args)
    args.methods = [i for i in arguments if arguments[i] == True and i not in ('all', 'plot', 'step', 'window', 'sw')]

    return args