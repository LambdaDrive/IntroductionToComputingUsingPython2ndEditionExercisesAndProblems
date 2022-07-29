def coins(n):
    moedas = [n]
    while moedas[-1] >= 8:
        for i in range(len(moedas)):
            if moedas[i] % 4 == 0:
                moedas.append(moedas[i] - 6)
            elif moedas[i] % 3 == 0:
                moedas.append(moedas[i] - 7)
            elif moedas[i] % 2 ==  0:
                moedas.append((moedas[i] / 2) + 1)
            elif moedas[i] % 10 == 0:
                moedas.append(moedas[i] - 9)
    if 8 in moedas:
        return True
    else:
        return False