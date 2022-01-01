def scaryDict(filename):
    file = open(filename)
    content = file.read()
    file.close()
    for symbol in '!?,;.-"()[]1234567890':
        content = content.replace(symbol, '')
    content = content.split()
    for word in content:            
        if len(word) < 3:
            content.remove(word)
    content = list(set(content))
    content.sort()    
    newfile = ''
    for word in content:
        newfile += word + '\n'
    file = open('dictionary.txt', 'w')
    file.write(newfile)
    file.close()
    print(newfile)
