from multiprocessing import Pool
from os import getpid

def length(word):
    'returns length of string word'

    # print the id of the process executing the function
    print('Process {} handling {}'.format(getpid(), word))
    return len(word)

# main program
pool = Pool(2)
res = pool.map(length, ['hawk', 'hen', 'hog', 'hyena'])
print(res)
