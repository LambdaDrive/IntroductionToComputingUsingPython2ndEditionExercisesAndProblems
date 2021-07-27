listaNomes = eval(input('Entre com uma lista de nomes:'))
for nome in listaNomes:
    if nome[0] in 'ABCDEFGHIJKLM':
        print(nome)
