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
    """ Return the reverse complement of a given DNA Sequence."""
    complement_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    rev_comp = ""
    for base in inseq:
        rev_comp = complement_dict[base] + rev_comp
    return rev_comp


