def names():
    dic = {}
    while True:
        name = input('Enter next name:')
        if name == '':
            for keys in dic.keys():
                print('There is {} student named {}'.format(dic[keys],keys))
        if name in dic.keys():
            dic[name] += 1
        else:
            dic[name] = 1
        
