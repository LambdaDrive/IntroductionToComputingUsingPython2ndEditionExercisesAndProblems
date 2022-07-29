def permutations(lista):
    if len(lista) <= 1:
        return [lista]
    else:
        permuta = []
        for permutation in permutations(lista[1:]):
            for i in range(len(lista)):
                permuta.append(permutation[:i] + lista[0:1] + permutation[i:])
        return permuta

