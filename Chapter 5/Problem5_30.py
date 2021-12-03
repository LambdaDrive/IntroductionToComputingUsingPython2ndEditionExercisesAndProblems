def many(filename):
    file = open(filename)
    content = file.read()
    file.close()
    content = content.replace('.', '')
    content = content.split()
    lenght1 = 0
    lenght2 = 0
    lenght3 = 0
    lenght4 = 0
    for word in content:
        if len(word) == 1:
            lenght1 += 1
        elif len(word) == 2:
            lenght2 += 1
        elif len(word) == 3:
            lenght3 += 1
        elif len(word) == 4:
            lenght4 += 1
    print('Words of lenght 1 :{}\nWords of lenght 2 :{}\nWords of lenght 3 :{}\nWords of lenght 4 :{}'.format(lenght1, lenght2, lenght3, lenght4))
    
