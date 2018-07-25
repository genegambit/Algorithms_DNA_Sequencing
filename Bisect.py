
# Text Preprocessing: Text Preprocessing involves building an index from the Text (T), 
# with substrings of specified lengths. These substrings are referred to as k-mers. 
# Indexing is used to determine the location (index) at which the pattern occurs within a text.
# If the location is found then the location os referred to as the index hit. The index hit may 
# or may not be a match, it is just a pointer to the locations in the text where the search should be thorough.


import bisect
from BoyerMoore import BoyerMoore, boyer_moore_implementation


class Index(object):
    """ Class to generate Indexes. """
    def __init__(self, txt, kmer_len):
        self.txt = txt
        self.kmer_len = kmer_len
        self.index = []
        for i in range(len(txt) - kmer_len + 1):
            # add (k-mer, offset) pair
            self.index.append((txt[i:i+kmer_len], i))
            # Sort by kmer
        self.index.sort() 


    def query(self, pattern):
        """ Return Indexes of first kmer of P."""
        kmer = pattern[:self.kmer_len]
        i = bisect.bisect_left(self.index, (kmer, -1))
        hits = []
        while i < len(self.index):
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i = i + 1
        return hits


def queryIndex(p, t, index):
    """ Function to Query the Indexes. """
    k = index.kmer_len
    offsets = []
    for i in index.query(p):
        # verify that rest of P matches
        if p[k:] == t[i+k:i+len(p)]:
            offsets.append(i)
    return offsets


def approximate_match(p, t, n):
    """ Approximate Matching using the Indexing and Boyer Moore. """
    segment_length = int(round(len(p) / (n+1)))
    all_matches = set()
    for i in range(n+1):
        start = i*segment_length
        end = min((i+1)*segment_length, len(p))
        p_bm = BoyerMoore(p[start:end], alphabet='ACGT')
        matches = boyer_moore_implementation(p[start:end], p_bm, t)
        # Extend matching segments to see if whole p matches
        for m in matches:
            if m < start or m-start+len(p) > len(t):
                continue
            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            for j in range(end, len(p)):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            if mismatches <= n:
                all_matches.add(m - start)
    return list(all_matches)
