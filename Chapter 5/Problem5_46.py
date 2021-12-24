def inversions(string):
    inv = 0
    for i in range(len(string)):
        for a in range(i, len(string)):
            if string[i]>string[a]:
                inv += 1
    return inv
