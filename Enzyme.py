import DNA


def replace_in_sequence(dna_sequence: DNA.DNASequence, seq, replacement):
    current_sequence = dna_sequence.get_sequence()
    index = dna_sequence.find_alignment(seq)
    while index is not -1:
        current_sequence.remove(seq)
        current_sequence.insert(index, replacement)
        dna_sequence.replace_sequence(current_sequence)
        index = dna_sequence.find_alignment(seq)


def enzyme_from_name(name, params: list):
    if name == "Mutase":
        return Mutase(params.pop(0))
    elif name == "Crispr":
        return Crispr(params.pop(0))
    elif name == "Crispr/Cas9":
        return Crispr_Cas9(params.pop(0), params.pop(0))
    elif name == "Polymerase":
        return Polymerase()


class Enzyme:

    def process(self, dna_sequence: DNA.DNASequence):
        raise NotImplementedError()


class Mutase(Enzyme):

    def __init__(self, freq):
        self.freq = freq

    def process(self, dna_sequence: DNA.DNASequence):
        seq = dna_sequence.get_sequence()
        for i in range(0, len(seq), self.freq):
            seq = DNA.complement_of_nucleotide(seq[i])

        dna_sequence.replace_sequence(seq)


class Crispr(Enzyme):

    def __init__(self, seq):
        self.seq = seq

    def process(self, dna_sequence: DNA.DNASequence):
        replace_in_sequence(dna_sequence, self.seq, 'W')


class Crispr_Cas9(Crispr):

    def __init__(self, seq, new_seq):
        super().__init__(seq)
        self.new_seq = new_seq

    def process(self, dna_sequence: DNA.DNASequence):
        super().process(dna_sequence)
        replace_in_sequence(dna_sequence, 'W', self.new_seq)


class Polymerase(Enzyme):

    def __init__(self):
        super().__init__()

    def process(self, dna_sequence: DNA.DNASequence):
        dna_sequence.replace_sequence(dna_sequence.get_sequence())
