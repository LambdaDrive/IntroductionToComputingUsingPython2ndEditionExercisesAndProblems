def average():
    numberwords = 0
    numberletters = 0
    sentence = input('Enter a sentence:')
    sentence = sentence.split()
    for word in sentence:
        numberwords += 1
        numberletters += len(word)
    return numberletters/numberwords
