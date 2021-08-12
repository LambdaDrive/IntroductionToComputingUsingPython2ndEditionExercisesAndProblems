def avg(listoflists):
    soma = 0
    media = 0
    for grades in listoflists:
        for i in range(len(grades)):
                soma+=grades[i]
        print(soma/len(grades))
        soma = 0

            
