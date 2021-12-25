def approxPi(error):
    constant = 4
    mutable = 1
    step = 1
    soma = 0
    prev = 0
    while True:
        if step % 2 != 0:
            soma+= constant/mutable
        else:
            soma -= constant/mutable
        if soma > 0 and prev > 0:
            if abs(soma - prev) < error:
                return soma
        prev = soma
        step += 1
        mutable += 2
        
