def complement_of_nucleotide(nucleotide):
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    return 'G'


class DNASequence:
    nucleotides = []

    def __init__(self, nucleotides):
        self.nucleotides = nucleotides

    def get_sequence(self):
        return self.nucleotides

    def get_length(self):
        return len(self.nucleotides)

    def get_complement(self):
        return list(complement_of_nucleotide(nucleotide) for nucleotide in self.nucleotides)

    def get_nucleotide(self, index):
        return self.nucleotides[index]

    def replace_nucleotide(self, index, nucleotide):
        self.nucleotides[index] = nucleotide

    def find_alignment(self, seq):
        for i in range(len(self.nucleotides) - len(seq) + 1):
            if self.nucleotides[i:i+len(seq)] == seq:
                return i
        return -1

    def replace_sequence(self, seq):
        self.nucleotides = seq

