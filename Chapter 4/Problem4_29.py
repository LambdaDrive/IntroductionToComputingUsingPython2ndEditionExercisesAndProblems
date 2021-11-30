def stats(textfile):
    file = open(textfile)
    content = file.read()
    file.close()
    numlines = content.count('\n')
    numchar = len(content)
    content = content.split()
    numwords = len(content)
    print('line count:{}\nword count:{}\ncharacter count:{}'.format(numlines, numwords, numchar))
    
