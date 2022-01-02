def different(table):
    distinc = set()
    for i in range(len(table)):
        for a in range(len(table[i])):
            distinc.add(table[i][a])
    return len(distinc)
