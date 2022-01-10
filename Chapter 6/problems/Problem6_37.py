def zipf(filename):
    file = open(filename)
    content = file.read()
    file.close()
    content = content.lower()
    content = content.split()
    ocur = []
    words = set()
    top10ocur = []
    for word in content:
        words.add(word)
    listwords = {}
    for word in words:
        listwords[word] = 0
    for word in content:
        listwords[word] += 1
    for key in listwords.keys():
        ocur.append(listwords[key])
    ocur.sort()
    for i in range(-1, -11, -1):
        top10ocur.append(ocur[i])
    for number in top10ocur:
        print(number/len(content))
