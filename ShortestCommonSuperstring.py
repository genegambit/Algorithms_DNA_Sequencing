
import itertools


def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching a prefix of 'b' that 
    is at least 'min_length' characters long.  If no such overlap exists,
    return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1


def scs(ss):
    """ Returns shortest common superstring of given strings,
        assuming no string is a strict substring of another- 
        using the Overlap."""
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss)-1):
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    return shortest_sup

# Example.
print(scs(['ACGGATGAGC', 'GAGCGGA', 'GAGCGAG']))