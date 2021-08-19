# DNA Coding Sequence Classification Using Spectral Envelope
A program to spectral analysis of DNA sequences

## Usage
Clone this repo to a local directory on your desktop and use it from the command line as

`main.py [-h] [-v] [-e] [-k] [-f] [-s] [-a] file-mode [-p] file`

or 

`main.py [-h] [-v] [-e] [-k] [-f] [-s] [-a] database-mode [-n] dir`

or

`main.py [-h] [-v] [-e] [-k] [-f] [-s] [-a] statistics-mode [-M] [-t] [-sd] dir`

where

```
-h            show the help message and exit
-v            set voss method
-e            set eiip mapping
-k            set qpks mapping
-f            set alg1 mapping
-s            set alg2 mapping
-a            set all methods: -v, -e, -k, -f, -s
-p            plot the energy spectrum of file from the chosen methods
-n N          delete sequences whose length is less than N (default: 0)
-M M          set the number of sequences drawn to M (default: 500)
-t TIMES      set the number of draws as TIMES (default: 10)
-sd SD        initialize the random number generator as SD (default: 10)
```
## Example

### Case 1: file-mode
In this mode, the input is a file in .fasta format. Use one or mores options among `-v`, `-e`, `-k`, `-f`, `-s` and `-a` to set the methods to spectral analysis. If you want to see the energy spectrum graphs, enable the option `-p`. For example, if you want set all methods of spectral analysis and plot their energy spectrum graphs, you must run the script from a command prompt as

`python3 main.py -a file-mode -p './database-seq/F56F11_4a_coding.fasta'`

The output is a file 'F56F11_4a_coding.txt' saved in the directory './results/' created in the same folder as the input. In this file are recorded values of normalized energy, normalized frequency, snr, entropy and TBP verification (True or False) for all methods of spectral analysis.

### Case 2: database-mode
In this mode, the input is a directory with files in .fasta format and their respective '-coding-sequence.txt' of chromossomes (these files are available at nucleotide database from National Center for Biotechnology Information (NCBI)). The database then consists of DNA sequences from intergenic regions and CDS recorded in these files. Use one or mores options among `-v`, `-e`, `-k`, `-f`, `-s` and `-a` to set the methods to spectral analysis. If you want to delete sequences whose length is less than N, enable the option `-n` with a value N (the default value is 200). For example, if you want set all methods of spectral analysis and delete sequences whose length is less than 200, you must run the script from a command prompt as

`python3 main.py -a database-mode -n 200 './database-cerevisiae/'`

For each sequence in database a file in .txt format is saved in the directory './results/' created in the same folder as the input. In each file are recorded values of normalized energy, normalized frequency, snr, entropy and TBP verification (True or False). Furthermore, two files summarize the results about TBP verification for each gene and are saved in the directory './results-summarized/' created in the same folder as the input. One file contains information about the intergenic regions and the other about the CDS.



### Case 3: statistics-mode
The input is a file in .fasta format. Use the one or mores options among `-v`, `-e`, `-k`, `-f`, `-s` and `-a` to set the methods to spectral analysis. If you want to see the energy spectrum graphs, enable the option `-p`.

The output is a file in .txt format saved in the directory './results/' created in the same folder as the input.

`main.py -a statistics-mode -p './database-cerevisiae/'`

## References
## Contact
Created by  feel free to contact me!

