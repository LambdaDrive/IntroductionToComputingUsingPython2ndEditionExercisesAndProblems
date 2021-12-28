def easyCrypto(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    cry = {}
    result = ''
    for i in range(len(letters)-1):   
        if i % 2 == 0:
            cry[letters[i]] = letters[i+1]
        else:
            cry[letters[i]] = letters[i-1]
        cry['z'] = 'y'
    for letter in string:
        if letter.isupper():
            result += cry[letter.lower()].capitalize()
        else:
            result += cry[letter]
    print(result)
    
