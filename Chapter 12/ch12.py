def partition(intermediate1):
    '''intermediate1 is a list containing [(key, value)] lists;
       returns iterable container with a (key, values) tuple for
       every unique key in intermediate1; values is a list that
       contains all values in intermediate1 associated with key
    '''
    dct = {}                  # dictionary of (key, value) pairs

    # for every (key, value) pair in every list of intermediate1
    for lst in intermediate1: 
        for key, value in lst: 

            if key in dct: # if key already in dictionary dct, add
                dct[key].append(value) # value to list dct[key]
            else:          # if key not in dictionary dct, add
                dct[key] = [value]     # (key, [value]) to dct

    return dct.items()  # return container of (key, values) tuples



class SeqMapReduce(object):
    'a sequential MapReduce implementation'

    def __init__(self, mapper, reducer):
        'functions mapper and reducer are problem specific'
        self.mapper = mapper
        self.reducer = reducer

    def process(self, data):
        'runs MapReduce on data with mapper and reducer functions'
        intermediate1 = [self.mapper(x) for x in data]  # Map
        intermediate2 = partition(intermediate1)
        return [self.reducer(x) for x in intermediate2] # Reduce



from multiprocessing import Pool
class MapReduce(object):
    'a parallel implementation of MapReduce'

    def __init__(self, mapper, reducer, numProcs=None):
        'initializes map and reduce functions and process pool'

        self.mapper = mapper
        self.reducer = reducer
        self.pool = Pool(numProcs)

    def process(self, data):
        'runs MapReduce on sequence data'

        intermediate1 = self.pool.map(self.mapper, data)  # Map
        intermediate2 = partition(intermediate1)
        return self.pool.map(self.reducer, intermediate2) # Reduce



#
# Word frequency
#

from os import getpid
def occurence(word):
    'returns list containing tuple (word, 1)'
    # print('Process {} executing occurence on {}'.format(getpid(), word))
    return [(word, 1)]

def occurenceCount(keyVal):
    # print('Process {} executing countOccurences on {}'.format(getpid(), keyVal))
    return (keyVal[0], sum(keyVal[1]))



#
# Inverted word index from local files
#

from string import punctuation
def getWordsFromFile(file):
    '''returns list of items [(word, file)]
       for every word in file'''
    infile = open(file)
    content = infile.read()
    infile.close()

    # remove punctuation (covered in Section 4.1)
    transTable = str.maketrans(punctuation, ' '*len(punctuation))
    content = content.translate(transTable)

    # construct set of items [(word, file)] with no duplicates
    res = set()
    for word in content.split():
        res.add((word, file))
    return res
    
def getWordIndex(keyVal):
    'returns input value'
    return keyVal

'''
if __name__ == '__main__':
    files = ['a.txt', 'b.txt', 'c.txt']
    print(SeqMapReduce(getWordsFromFile, getWordIndex).process(files))
'''



#
# Inverted word index from web text files
#

from urllib.request import urlopen
from re import findall

def getProperFromURL(url):
    '''returns list of items [(word, url)] for every word
       in the content of web page associated with url'''

    content = urlopen(url).read().decode()
    pattern = '[A-Z][A-Za-z\'\-]*'      # RE for capitalized words
    propers = set(findall(pattern, content)) # removes duplicates

    res = []              # for every capitalized word
    for word in propers:  # create pair (word, url)
        res.append((word, url))
    return res

'''
from time import time

if __name__ == '__main__':

    urls = [              # URLS of eight Charles Dickens novels
        'http://www.gutenberg.org/cache/epub/2701/pg2701.txt',
        'http://www.gutenberg.org/cache/epub/1400/pg1400.txt',
        'http://www.gutenberg.org/cache/epub/46/pg46.txt',
        'http://www.gutenberg.org/cache/epub/730/pg730.txt',
        'http://www.gutenberg.org/cache/epub/766/pg766.txt',
        'http://www.gutenberg.org/cache/epub/1023/pg1023.txt',
        'http://www.gutenberg.org/cache/epub/580/pg580.txt',
        'http://www.gutenberg.org/cache/epub/786/pg786.txt']

    t1 = time()   # sequential start time
    SeqMapReduce(getProperFromURL, getWordIndex).process(urls)
    t2 = time()   # sequential stop time, parallel start time
    MapReduce(getProperFromURL, getWordIndex, 4).process(urls)
    t3 = time()   # parallel stop time

    print('Sequential: {:5.2f} seconds.'.format(t2-t1))
    print('Parallel:   {:5.2f} second.'.format(t3-t2))
'''



##################################
# Solutions to Practice Problems #
##################################



# Practice Problem 12.3
import sqlite3
def webData(db, url, links, freq):
    '''db is the name of a database file containing tables
       Hyperlinks and Keywords
       url is the URL of a web page
       links is a list of hyperlink URLs in the web page
       freq is a dictionary that maps each word in the web page
       to its frequency;
       
       webData inserts row (url, word, freq[word]) into Keywords
       for every keyword in freq, and record (url, link) into
       Hyperlinks, for every link in links
    '''
    con = sqlite3.connect(db)
    cur = con.cursor()

    for word in freq:
        record = (url, word, freq[word])
        cur.execute("INSERT INTO Keywords VALUES (?,?,?)", record)

    for link in links:
        record = (url, link)
        cur.execute("INSERT INTO Keywords VALUES (?,?)", record)

    con.commit()
    con.close()


# Practice Problem 12.4
import sqlite3
def freqSearch(webdb):
    ''''webdb is a database file containing table Keywords;

        freqSearch is a simple search engine that takes a keyword
        from the user and prints URLs of web pages containing it
        in decreasing order of frequency of the word'''
    con = sqlite3.connect(webdb)
    cur = con.cursor()

    while True:    # serve forever
        keyword = input("Enter keyword: ")

        # select web pages containing keyword in
        # decreasing order of keyword frequency
        cur.execute("""SELECT Url, Freq
                       FROM Keywords
                       WHERE Word = ?
                       ORDER BY Freq DESC""", (keyword,))
        print('{:15}{:4}'.format('URL', 'FREQ'))
        for url, freq in cur:
            print('{:15}{:4}'.format(url, freq))




# Practice Problem 12.6
#
# Inverted character index
#

def getChars(word):
    '''word is a string; the function returns a list of tuples
       (c, word) for every character c of word'''
    return [(c, word) for c in word]

def getCharIndex(keyVal):
    '''keyVal is a 2-tuple (c, lst) where lst is a list
       of words (strings)

       function returns (c, lst') where lst' is lst with
       duplicates removed'''
    return (keyVal[0], list(set(keyVal[1])))


# Practice Problem 12.8
#
# divisor indexing
#

from math import sqrt
def divisors(number):
    '''returns list of (i, number) tuples for
       every prime i dividing number'''
    res = []          # accumulator of factors of number
    n = number
    i = 2
    while n > 1:
        if n%i == 0:  # if i is a factor of n
            # collect i and repeatedly divide n by i
            # while i is a factor of n
            res.append((i,number))
            while n%i == 0:
                n //= i
        i+=1          # go to next i
    return res

def identity(keyVal):
    return keyVal

'''
from random import sample
from time import time
if __name__ == '__main__':
    # create list of 64 large random integers 
    numbers = sample(range(10000000, 20000000), 64)
    t1 = time()
    SeqMapReduce(divisors, identity).process(numbers)
    t2 = time()
    MapReduce(divisors, identity).process(numbers)
    t3 = time()
    print('Sequential: {:5.2f} seconds.'.format(t2-t1))
    print('Parallel:   {:5.2f} seconds.'.format(t3-t2))
'''
