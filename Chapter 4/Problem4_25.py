def vowelCount(string):
    numbera = string.count('a') + string.count('A')
    numbere = string.count('e') + string.count('E')
    numberi = string.count('i') + string.count('I')
    numbero = string.count('o') + string.count('O')
    numberu = string.count('u') + string.count('U')
    print('a, e, i, o, and u appear, respectively, {}, {}, {}, {}, {} times'.format(numbera, numbere, numberi, numbero, numberu))
    
    
