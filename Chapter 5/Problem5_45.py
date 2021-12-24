def avgavg(gradeslist):
    avg = []
    avgavg = 0
    soma = 0
    for student in gradeslist:
        for grade in student:
            soma += grade
        avg.append(soma/len(student))
        soma = 0
    for grade in avg:
        soma += grade
    avgavg = soma/len(avg)
    print(avg,'\n',avgavg)
