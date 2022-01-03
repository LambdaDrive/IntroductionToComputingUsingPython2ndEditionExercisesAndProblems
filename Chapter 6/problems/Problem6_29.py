def networks(nstudents,listuple):
    dic = {}
    ngroups = 0
    for tupla in listuple:
        if len(dic) < 1:
            dic[ngroups] = set(tupla)
        elif len(dic) >= 1:
            if tupla in dic[ngroups]:
                for number in tupla:
                    if number not in dic[ngroups]:
                        dic[ngroups].add(number)
            else:
                ngroups += 1
                dic[ngroups] = set(tupla)
    for i in range(len(dic)):
        print('Social network {} is {}'.format(i, dic[i]))
