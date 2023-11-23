def isValidSubsequence(array, sequence):
    seqIdx = 0
    for item in array:
        if seqIdx == len(sequence):
            return True
        if item == sequence[seqIdx]:
            seqIdx += 1
    return seqIdx == len(sequence)
