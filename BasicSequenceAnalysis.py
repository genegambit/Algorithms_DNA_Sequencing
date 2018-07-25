import random
import matplotlib.pyplot as plt
import numpy as np


def random_seq(seq_len):
    """ Generate a sequence of specified length. """
    req_seq = ''
    for _ in range(seq_len):
        req_seq += random.choice("ATGC")
    return req_seq


def generate_random_seq(seq_len):
    """ One liner to generate random sequence of specified length"""
    seq = ''.join([random.choice('ATGC') for i in range(seq_len)])
    return seq


def longest_common_prefix(s_1, s_2):
    """ Return the longest common prefix from the provided
    strings. """
    i = 0
    while i < len(s_1) and i < len(s_2) and s_1[i] == s_2[i]:
        i += 1
    return s_1[:i]


def check_match(s_1, s_2):
    """ Check if the given sequences are a perfect match. 
    Python's builtin functionality can also be used.
    "ATGC" == "ATGC" will return True and likewise. """
    if not len(s_1) == len(s_2):
        return False
    for index, _ in enumerate(s_1):
        if not s_1[index] == s_2[index]:
            return False
    return True


def reverse_complement(inseq):
    """ Return the reverse complement of a given DNA Sequence.
    The input is the sequence string, and the output is a string. """
    complement_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    rev_comp = ""
    for base in inseq:
        rev_comp = complement_dict[base] + rev_comp
    return rev_comp


def read_genome(fileloc):
    """ This function reads a genome file.
    The input is the location of the file. """
    with open(fileloc) as infile:
        genome = ""
        for line in infile:
            # Skip the first line with genome information.
            if not line[0] == ">":
                genome += line.rstrip()
    return genome


def count_bases(in_genome):
    """ Count the number of occurrences of each base.
    Can use the python built in collections.counter to 
    get the individual count of bases in the genome.
    The output in this case is a Counter Object."""
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in in_genome:
        counts[base] += 1
    print(counts)


def read_fastq(in_file):
    """ Read the Fastq file provided as an input 
    and return lists of the sequences and qualities."""
    seqs = []
    qual = []
    with open(in_file) as infile:
        while True:
            # Skip the header line containing the name.
            infile.readline()
            # Read the Sequence to the variable a_sq
            a_sq = infile.readline().rstrip() 
            # Skip the placeholder line.
            infile.readline() 
            # Read the Base Quality line.
            a_ql = infile.readline().rstrip()            
            if not a_sq:
                break
            seqs.append(a_sq)
            qual.append(a_ql)
    return seqs, qual


def phred33_quality(qual):
    """ Convert Phred+33 ASCII-encoded character to Quality Score."""
    return ord(qual) - 33


def quality_phred33(quality):
    """ Convert the Quality Score to Phred+33 ASCII encoded character. """
    return chr(quality + 33)


def get_base_qual_hist(quality_strings):
    """ Get the histogram of quality Scores. """
    # The number 50 is approximated based on the
    # highest quality score in the genome.
    # Can be changed depending on the input file. 
    hist = [0] * 50
    qualities = []
    for read in quality_strings:
        for phred in read:
            qual = phred33_quality(phred)
            qualities.append(qual)
            hist[qual] += 1
    return hist, qualities



