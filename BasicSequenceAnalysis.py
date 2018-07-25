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

