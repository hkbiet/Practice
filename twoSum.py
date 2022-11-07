def twoNumberSum(array, targetSum):
    array.sort()
    i = 0
    j = -1

    while((array[i] + array[j]) != targetSum):
        if (array[i] + array[j]) < targetSum and i < len(array):
            i +=1
        elif (array[i] + array[j]) > targetSum and (j+len(array) >= 0):
            j -= 1
        if i >= len(array) or (j+len(array) < 0):
            return []
    return [array[i], array[j]]