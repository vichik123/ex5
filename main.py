import json
import DNA
import Enzyme
import sys


def processData(dir_path):
    dna = open(dir_path + "/DNA.json", 'r')
    data = json.load(dna)
    dna_sequences = []
    protocol = open(dir_path + "/protocol.txt", 'r')
    protocol_data = protocol.read().split()
    name = protocol_data.pop(0)
    while name is not None:
        enzyme = protocol_data.pop(0)
        dna_sequence = DNA.DNASequence(data[name])
        Enzyme.enzyme_from_name(enzyme, protocol_data).process(dna_sequence)
        dna_sequences.append(dna_sequence)
        name = protocol_data.pop(0)

    dictionary = {}
    for i in range(len(dna_sequences)):
        dictionary[data.keys()[i]] = dna_sequences[i]
    json_object = json.dumps(dictionary, indent=4)
    # Writing to sample.json
    with open("ModifiedDNA.json", "w") as outfile:
        outfile.write(json_object)


if __name__ == '__main__':
    processData(sys.argv[0])
