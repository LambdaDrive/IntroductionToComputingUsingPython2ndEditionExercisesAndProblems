def lastfirst(stringlist):
    resultlist = [[],[]]
    for i in range(len(stringlist)):
        stringsepareted = stringlist[i].split(',')
        resultlist[1].append(stringsepareted[0])
        resultlist[0].append(stringsepareted[1])
    return resultlist
