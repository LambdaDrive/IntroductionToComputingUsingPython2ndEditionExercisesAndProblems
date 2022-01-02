def translate(dic):
    while True:
        trans = ''
        phrase = input('Entre the phrase:')
        phrase = phrase.split()
        for word in phrase:
            if word in dic.keys():
                trans += dic[word] + ' '
            else:
                trans += '____ '
        print(trans)
