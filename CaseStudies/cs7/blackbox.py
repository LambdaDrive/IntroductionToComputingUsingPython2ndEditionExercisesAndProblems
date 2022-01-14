from random import randrange, seed
from platform import node

def blackbox():
    seed(node())  # generate seed based on computer's network name
    secret = randrange(10**5,10**6)   # generate six digit integer
    try:
        key = int(input('Enter key: '))
        if key != secret:
            print('Failed...')
        else:
            print('Success!')
    except:
        print('Failed...')
