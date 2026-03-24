from structures import DNA_Codons

DNA_ReverseComplement = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

def reverse_complement(seq):
    return ''.join(DNA_ReverseComplement[nuc] for nuc in seq)[::-1]

def translate_seq(seq, init_pos=0):
    return [
        DNA_Codons.get(seq[pos:pos+3], "?")
        for pos in range(init_pos, len(seq) - 2, 3)
    ]
