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
-n N          delete sequences whose length is less than N (default: 200)
-M M          set the number of sequences drawn to M (default: 500)
-t TIMES      set the number of draws as TIMES (default: 10)
-sd SD        initialize the random number generator as SD (default: 10)
```
## Example

### Case 1: file-mode
The input is a file in .fasta format. Use the one or mores options among `-v`, `-e`, `-k`, `-f`, `-s` and `-a` to set the methods to spectral analysis. If you want to see the energy spectrum graphs, enable the option `-p`.

The output is a file in .txt format saved in the directory './results/' created in the same folder as the input.

`main.py -a file-mode -p './database-seq/F56F11_4a_coding.fasta'`

