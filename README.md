# DNA Coding Sequence Classification Using Spectral Envelope
A program to spectral analysis of DNA sequences

## Usage
Clone this repo to a local directory on your desktop and use it from the command line as

`main.py [-h] [-v] [-e] [-k] [-g] [-f] [-s] [-a] file-mode [-p] [-sw] [-wl] [-st] file`

or 

`main.py [-h] [-v] [-e] [-k] [-g] [-f] [-s] [-a] database-mode [-n] dir`

or

`main.py [-h] [-v] [-e] [-k] [-g] [-f] [-s] [-a] statistics-mode [-M] [-t] [-sd] dir`

where the optional arguments are

```
-h            show the help message and exit
-v            set voss method
-e            set eiip mapping
-k            set qpks mapping
-g            set mem mapping
-f            set alg1 mapping
-s            set alg2 mapping
-a            set all methods: -v, -e, -k, -f, -s
-p            plot the energy spectrum of file from the chosen methods
-sw           set the sliding window approach
-wl W         set window length to W  (default: 351)
-st S         set step size to S (default: 1)
-n N          delete sequences whose length is less than N (default: 0)
-M M          set the number of sequences drawn to M (default: 500)
-t TIMES      set the number of draws as TIMES (default: 10)
-sd SD        initialize the random number generator as SD (default: 10)
```
## Quick demo

### Example 1: file-mode
In this mode, the input is a file in .fasta format. Use one or mores options among `-v`, `-e`, `-k`, `-g`, `-f`, `-s` and `-a` to set the methods to spectral analysis. If you want to see the energy spectrum graphs, enable the option `-p`. For example, if you want set all methods of spectral analysis and plot their energy spectrum graphs to the file './database-seq/F56F11_4a_coding.fasta', you must run this script from a command prompt as

`python3 main.py -a file-mode -p './database-seq/F56F11_4a_coding.fasta'`

The output is a file 'F56F11_4a_coding.txt' saved in the directory './results/' created in the same folder as the input file. In this file are recorded values of normalized energy, normalized frequency, snr, entropy and TBP verification (True or False) for all methods of spectral analysis.

### Example 2: file-mode using sliding window
In this mode, the input is a file in .fasta format. Use one or mores options among `-v`, `-e`, `-k`, `-g`, `-f` and `-s` to set the methods to spectral analysis. If you want to see the energy spectrum graphs, enable the option `-p`. Use `-sw`to enable this method. Use `-wl` to set the window length as W. Use `-st` to set the step size as S. The MEM Spectrum constraints are true for sequences whose length is even, so `-a` cannot be used in this mode. For example, if you want set all other methods of spectral analysis and plot their energy spectrum graphs to the file './database-seq/F56F11_4a.fasta' considering a window length of 351 and step size of 5, you must run this script from a command prompt as

`python3 main.py -v -e -k -f -s file-mode -p -sw -wl 351 -st 5 './database-seq/F56F11_4a.fasta'`

The output is a file 'F56F11_4a-sliding-window.txt' saved in the directory './results/' created in the same folder as the input file. In this file are recorded values of energy, relative position and TBP verification (True or False) for all methods of spectral analysis.

### Example 3: database-mode
In this mode, the input is a directory with files in .fasta format and their respective '-coding-sequence.txt' of chromossomes (these files are available at nucleotide database from National Center for Biotechnology Information (NCBI)). The database then consists of DNA sequences from intergenic regions and CDS recorded in these files. Use one or mores options among `-v`, `-e`, `-k`, `-f`, `-s` and `-a` to set the methods to spectral analysis. If you want to delete sequences whose length is less than N, enable the option `-n` with a value N. For example, if you want set all methods of spectral analysis and delete sequences whose length is less than 200 to the files in the directory './database-cerevisiae/', you must run this script from a command prompt as

`python3 main.py -a database-mode -n 200 './database-cerevisiae/'`

As output, for each sequence in database, a file in .txt format is saved in the directory './results/' created in the same directory as the input. In each file are recorded values of normalized energy, normalized frequency, snr, entropy and TBP verification (True or False). Furthermore, two additional files summarize the results about TBP verification for each gene and are saved in the directory './results-summarized/' created in the same directory as the input. One file contains information about the intergenic regions and the other about the CDS.

### Example 4: statistics-mode
In this mode, the statistical analyses of the `database-mode` results are performed. The input is the same directory as `database-mode`. Use the one or mores options among `-v`, `-e`, `-k`, `-f`, `-s` and `-a` to set the methods to spectral analysis. Use `-M` to set the number of sequences drawn from database as M. Use `-t` to set the number of times `M` sequences are drawn. Use `-sd` to initialize the random number generator. For example, after perform the `database-mode`, you must run this script from a command prompt as

`python3 main.py -a statistics-mode './database-cerevisiae/'`

The output is a file 'results.txt' saved in the directory './results-statistics/' created in the same folder as the input. In this file are recorded for all methods of spectral analysis: the boxplot information for True Positive and False Positive classification, the coordinates of the point on the ROC space, and the accuracy, sensitivity and specificity rate.

## Feedback
Please do not hesitate to contact us if there is anything we may be able to help you with.
Please send error messages or comments to our contact address.

milena.arruda@ee.ufcg.edu.br
