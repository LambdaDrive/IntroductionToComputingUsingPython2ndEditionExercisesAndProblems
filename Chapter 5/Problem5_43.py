def evenrow(matrix):
    even = False
    soma = 0
    for row in matrix:
        for number in row:
            soma += number
        if soma % 2 == 0:
            even = True
        else:
            even = False
        soma = 0
    return even
