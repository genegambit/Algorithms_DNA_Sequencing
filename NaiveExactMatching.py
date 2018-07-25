
def naive_exact_matching(pattern, txt):
    """ This function implements the Naive Exact Matching Algorithm. """
    # All occurrences where Pattern matches againsts Text.
    occurrences = []
    # Loop through every position where the pattern can start.
    for i in range(len(txt) - len(pattern) + 1):
        match = True
        # Compare every character of pattern againsts every
        # corresponding position in the Text.
        for j, _ in enumerate(pattern):
            if txt[i+j] != pattern[j]:
                match = False
                break
        # Grab the location of the Exact Match.
        if match:
            occurrences.append(i)
    return occurrences
