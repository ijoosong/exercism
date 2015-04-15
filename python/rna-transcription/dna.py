def to_rna(nucleotide):
    rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna_string = ""
    buff = []
    if len(nucleotide) == 1:
        return rna[nucleotide]
    else:
        for char in nucleotide:
            buff.append(rna[char])
            rna_string = ''.join(buff)
        return rna_string
