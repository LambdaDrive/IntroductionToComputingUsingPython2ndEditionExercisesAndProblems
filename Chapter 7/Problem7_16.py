def index(filename, listwords):
    try:
        file = open(filename)
    except FileNotFoundError:
        print('File {} not found'.format(filename))
    content = file.read()
    file.close()
    content = content.splitlines()
    worddict = {}
    for word in listwords:
        for i in range(len(content)):
            if word in content[i]:
                if word in worddict.keys():
                    worddict[word] += ', '+ str(i+1)
                else:
                    worddict[word] = str(i+1)
                    
    for key in worddict.keys():
        print('{:10} {:10}'.format(key,worddict[key]))
      
    
    
