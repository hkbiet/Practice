def squares(array):
    res = []
    for i in range(len(array)):
        res.append(0)

    i = 0
    j = len(array)-1
    res_i = 0
    res_j = len(array)-1

    while i <= j:
        if array[i]**2 > array[j]**2:
            res[res_j] = array[i]**2
            i += 1
        else:
            res[res_j] = array[j]**2
            j -= 1
        res_j -= 1
    return res

array = [-5,-4,-3,1,2]
array.sort()
print("INPUT : ", array)
res = squares(array)
print(res)
