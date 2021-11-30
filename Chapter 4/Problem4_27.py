def fcopy(firstfile, secondfile):
    file = open(firstfile)
    content = file.read()
    file.close()
    file = open(secondfile, 'w')
    file.write(content)
    file.close()
    
