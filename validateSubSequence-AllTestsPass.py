def isValidSubsequence(array, sequence):
    # Passing all tests.
    sequence_traverser = 0
    array_traverser = 0

    while sequence_traverser < len(sequence) and array_traverser < len(array):
        if array[array_traverser] == sequence[sequence_traverser]:
            array_traverser = array_traverser + 1
            sequence_traverser = sequence_traverser + 1
        else:
            array_traverser = array_traverser + 1
    if sequence_traverser == len(sequence):
        if sequence[sequence_traverser-1] == array[array_traverser-1]:
            return True
    return False
