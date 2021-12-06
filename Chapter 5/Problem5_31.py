def subsetSum(numlist, target):
    if len(numlist)< 3:
        print("The list must have 3 or more numbers!")
        return ''
    for i in range(len(numlist)):
        for a in range(len(numlist)-1, 0, -1):
            for b in range(i+1, a):
                if i < b and a > b:
                    if numlist[i]+numlist[a]+numlist[b] == target:
                        return True
    return False
