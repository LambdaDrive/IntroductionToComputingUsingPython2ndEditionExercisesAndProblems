def ticker(filename):
    file = open(filename)
    content = file.read()
    file.close()
    content.splitlines()
    dictionary = {}
    for i in range(0, len(content)-1, 2):
        dictionary[content[i]] = content[i+1]
    resp = 'a'
    while resp != '':
        resp = input('Enter company name:')
        if resp in dictionary.keys():
            print('Ticker symbol:{}'.format(dictionary[resp]))
    
