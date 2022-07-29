def numOnes(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return numOnes(n//2)+numOnes(n%2)
