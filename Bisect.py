
# Text Preprocessing: Text Preprocessing involves building an index from the Text (T), 
# with substrings of specified lengths. These substrings are referred to as k-mers. 
# Indexing is used to determine the location (index) at which the pattern occurs within a text.
# If the location is found then the location os referred to as the index hit. The index hit may 
# or may not be a match, it is just a pointer to the locations in the text where the search should be thorough.


import bisect


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