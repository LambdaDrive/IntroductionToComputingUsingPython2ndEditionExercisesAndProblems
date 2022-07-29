def crawl(filename):
    if open(filename).read() == '':
        print('Visiting '+ filename)
    else:
        print('Visiting '+ filename)
        file = open(filename)
        content = file.read()
        file.close()
        content = content.split()
        for arquivo in content:
            crawl(arquivo)



