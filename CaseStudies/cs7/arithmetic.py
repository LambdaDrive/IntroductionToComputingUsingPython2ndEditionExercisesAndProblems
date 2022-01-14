def arithmetic(numList):
    '''returns True if list of integers numList
       is an arithmetic sequence, False otherwise'''
    if len(numList) < 2:
        return True
    diff = numList[1] - numList[0]
    for i in range(len(numList)):
        if numList[i+1] - numList[i] != diff:
            return False
    return True
