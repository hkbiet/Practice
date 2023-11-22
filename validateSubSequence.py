def isValidSubsequence(array, sequence):
    for item in sequence:
        if item in array:
            item_index = array.index(item)
            array = array[item_index+1:]
            continue
        else:
            return False
    return True
