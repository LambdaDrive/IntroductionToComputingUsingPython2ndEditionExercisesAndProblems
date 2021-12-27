def easyCrypto(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    cry = {}
    for i in range(len(letters)-1):
        if i % 2 != 0:
            cry[letters[i]] = letters[i+1]
        else:
            cry[letters[i]] = letters[i-1]
    print(cry)
    
