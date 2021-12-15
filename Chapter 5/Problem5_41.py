def poly(coefficients, x):
    soma = 0
    for i in range(len(coefficients)):
        if i == 0:
            soma += coefficients[i]
        else:
            soma += coefficients[i]*(x**i)
    return soma
