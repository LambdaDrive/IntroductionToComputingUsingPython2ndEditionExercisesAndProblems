def pairs1(lista, number):
    trunes = False
    for i in range(len(lista)-1):
        for a in range(len(lista)-1, i,-1):
            if lista[i] + lista[a] == number:
                trunes = True
    return trunes
