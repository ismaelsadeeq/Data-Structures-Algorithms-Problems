def firstDuplicateValue(array):
    tmp = []
    for i in array:
        if i in tmp:
            return i
        else:
            tmp.append(i)
    return -1
