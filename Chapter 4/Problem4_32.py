def censor(filename):
    file = open(filename)
    content = file.read()
    file.close()
    content = content.split(' ')
    for i in range(0, len(content)):
        if len(content[i])==4:
            content[i] = 'xxxx'
    newcontent = ''
    for word in content:
        newcontent += ' ' + word
    file = open('censored.txt', 'w')
    file.write(newcontent)
    file.close()
