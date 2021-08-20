import os

# Figure 3
# os.system("python3 main.py -v file-mode -p './database-seq/YPL230W.fasta'")

# Figure 4
# os.system("python3 main.py -a file-mode -p './database-seq/YOR215C.fasta'")

# Figure 5
# os.system("python3 main.py -a file-mode -p './database-seq/YNL122C.fasta'")

# Statistics: Table I, Figure 8 and Figure 9
# os.system("python3 main.py -v -e -k -f -s database-mode -n 200 './database-cerevisiae/'")
# os.system("python3 main.py -v -e -k -f -s statistics-mode './database-cerevisiae/'")

# Figure 10
os.system("python3 main.py -a file-mode -p -sw -wl 351 -st 5 './database-seq/F56F11_4a.fasta'")