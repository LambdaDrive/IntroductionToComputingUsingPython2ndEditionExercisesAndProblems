def sublist(list1, list2):
    index1 = []
    result = False
    for i in range(len(list1)):
        try:
            index1.append(list2.index(list1[i]))
        except ValueError:
            return False
    for i in range(len(index1) - 1):
        if index1[i]<index1[i+1]:
            result = True
        else:
            result = False
            break
    return result
