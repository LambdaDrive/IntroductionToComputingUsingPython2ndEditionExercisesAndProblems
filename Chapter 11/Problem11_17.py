from re import findall

def scary(arquivo):
    
    arquiv = open(arquivo)
    content = arquiv.read()
    arquiv.close()
   
    content = content.lower()

    pattern = '[a-zA-Z]+'
    words = findall(pattern, content)
    words = list(set(words))
    words.sort()

    arquiv = open('dictionary.txt', 'a')
    for word in words:
        arquiv.write(word + '\n')
    arquiv.close()
