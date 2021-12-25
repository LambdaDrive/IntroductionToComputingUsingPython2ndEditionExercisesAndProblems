def d2x(n, x):
    result = []
    resultconv = ''
    while n >= 1:
        result.append(str(n % x))
        n = n // x
    result.reverse()
    for item in result:
        resultconv += item
    return resultconv
