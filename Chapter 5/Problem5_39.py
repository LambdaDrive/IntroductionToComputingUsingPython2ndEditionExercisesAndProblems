def exclamation(string):
    for letter in string:
        if letter in 'AEIOUaeiou':
            print(letter * 4, end = '')
        else:
            print(letter, end ='')
    print('!')
