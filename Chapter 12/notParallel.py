from os import getpid

def length(word):
    'returns length of string word'
    print('Process {} handling {}'.format(getpid(), word))
    return len(word)

animals = ['hawk', 'hen', 'hog', 'hyena']
print([length(x) for x in animals])
