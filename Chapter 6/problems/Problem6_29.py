def networks(nstudents,listuple):
    dic = {}
    ngroups = 0
    for tupla in listuple:
        if len(dic) < 1:
            dic[ngroups] = set(tupla)
        elif len(dic) >= 1:
            if set(tupla).isdisjoint(dic[ngroups]):
                ngroups += 1
                dic[ngroups] = set(tupla)    
            else:                
                dic[ngroups] = dic[ngroups].union(set(tupla).difference(dic[ngroups]))
    for i in range(len(dic)):
        print('Social network {} is {}'.format(i, dic[i]))
