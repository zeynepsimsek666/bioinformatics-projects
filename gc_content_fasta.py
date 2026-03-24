"""
GC Content Calculator for FASTA files

This script reads a FASTA file and calculates GC content for each sequence.
It handles multiple sequences and unknown nucleotides.

Usage:
    python gc_content_fasta.py sample.fasta
"""

import sys

fastaFile = open(sys.argv[1], 'r')

gc = 0
at = 0
unknown = 0
seq_id = ""

for line in fastaFile:
    if line.startswith('>'):
        if (gc + at) > 0:
            total = gc + at
            percentage = round((gc / total) * 100, 2)
            print(f"{seq_id} | GC Content: {percentage}%")

        seq_id = line.strip()

        gc = 0
        at = 0
        unknown = 0

    else:
        nuc_str = list(line.strip())

        for n in nuc_str:
            if n in ['G','g','C','c']:
                gc += 1
            elif n in ['A','a','T','t']:
                at += 1
            else:
                unknown += 1

# last sequence
total = gc + at
if total > 0:
    percentage = round((gc / total) * 100, 2)
    print(f"{seq_id} | GC Content: {percentage}%")

fastaFile.close()
