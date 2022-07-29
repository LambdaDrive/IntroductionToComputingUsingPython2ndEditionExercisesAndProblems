def anagrams(arquivo, word):
    letterlist = []
    letterlistpalavra = []
    wordlist = []
    isequal = False
    file = open(arquivo)
    content = file.read().split('\n')
    file.close()
    for letter in word:
        letterlist.append(letter)
    letterlist.sort()
    for palavra in content:
        for letter in palavra:
            letterlistpalavra.append(letter)
        letterlistpalavra.sort()
        if len(palavra) == len(word):
            for letter in palavra:
                if letterlistpalavra == letterlist:
                    isequal = True
                else:
                    isequal = False
            if isequal == True:
                wordlist.append(palavra)
        isequal = False
        letterlistpalavra = []
    for palavra in wordlist:
        print(palavra)

