def address(lista):
    lista.sort()
    if len(lista) % 2 == 0:
        return lista[(len(lista)//2) - 1]
    else:
        return lista[(len(lista)//2)]
