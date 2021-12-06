def mystery(n):
    numtimes = 0
    while n > 1:
        n = n // 2
        numtimes += 1
    return numtimes
