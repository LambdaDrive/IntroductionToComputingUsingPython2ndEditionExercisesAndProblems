def hexASCII():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in letters:
        code = ord(letter)
        print(letter,':{:x}'.format(code))
