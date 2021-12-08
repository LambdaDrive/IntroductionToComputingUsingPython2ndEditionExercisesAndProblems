def mssl(intlist):
    bigger = []
    for i in range(len(intlist)):
        for a in range(len(intlist), 0, -1):
            if sum(intlist[i:a])>sum(bigger):
                bigger = intlist[i:a]
    if sum(bigger) < 0:
        return 0
    else:
        return sum(bigger)
