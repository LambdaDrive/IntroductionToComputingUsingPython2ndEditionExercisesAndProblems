from math import ceil, sqrt
from os import getpid
from multiprocessing import Pool
from time import time

def prime(n):
    'returns True if integer n is prime, False otherwise'
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    upper = ceil(sqrt(n))
    i = 3
    while i <= upper:
        if n%i == 0:
            return False
        i += 2
    return True

def countPrimes(start):
    'returns the number of primes in range [start, start+rng)'
    soma = 0
    primelist = []
    twinprime = 0
    rng = 100000
    formatStr = 'process {} processing range [{}, {})'
    print(formatStr.format(getpid(), start, start+rng))
    for i in range(start, start+rng):
        if prime(i):
            primelist.append(i)
    for i in range(len(primelist)-1):
        if primelist[i+1]-primelist[i]==2:
            twinprime += 1
    return twinprime

if __name__ == '__main__':
    
    p = Pool()
    # starts in a list of left boundaries of integer ranges
    starts = [12345678, 23456789, 34567890, 45678901,
             56789012, 67890123, 78901234, 89012345]

    t1 = time()                       # start time
    print(p.map(countPrimes, starts)) # run countPrimes()
    t2 = time()                       # end time

    p.close()
    print('Time taken: {} seconds.'.format(t2-t1))

