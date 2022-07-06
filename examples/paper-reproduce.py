import os

# Figure 6
# os.system("python3 main.py -a file-mode -p './database-seq/YOR215C.fasta'")

# Figure 7
# os.system("python3 main.py -a file-mode -p './database-seq/YNL122C.fasta'")

# Database mode example
# os.system("python3 main.py -v -e -k -f -s database-mode -n 200 './database-cerevisiae/'")

# Figure 9
os.system("python3 main.py -v -e -k -f -s file-mode -p -sw -wl 351 -st 5 './database-seq/F56F11_4a.fasta'")