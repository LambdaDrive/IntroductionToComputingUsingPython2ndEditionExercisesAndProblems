def mirror(string):
    newstring = ''
    dictionary = {'d':'b', 'b':'d','p':'q', 'q':'p'}
    for i in range(-1, -len(string)-1, -1):
        if string[i] in 'aeiu':
            return 'INVALID'
        elif string[i] in dictionary.keys():
            newstring += dictionary[string[i]]
        else:
            newstring += string[i]
    return newstring
