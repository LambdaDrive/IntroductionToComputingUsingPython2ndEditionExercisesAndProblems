#12.17 Develop an application that takes the name of a text file as input, computes the
#frequency of every word in the file, and stores the resulting (word, frequency) pairs in a new
#table named Wordcounts of a new database file. The table should have columns Word and
#Freq for storing the (word, frequency) pairs.

import re
import sqlite3

def frequent(textfile):
    
    arquivo = open(textfile)
    content = arquivo.read()
    arquivo.close()

    listwords = re.findall('[a-zA-Z]*', content)
    
    contdict = dict()
    
    for word in listwords:
        if word == '':
            pass
        else:
            if word not in contdict.keys():
                contdict[word] = 1
            else:
                contdict[word] += 1
    
    listfreq = []
    
    for key in contdict.keys():
        listfreq.append((key, contdict[key]))
    
    con = sqlite3.connect('frequencydatabase.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE Wordcounts(Word, Freq)")
    cur.executemany("INSERT INTO Wordcounts VALUES(?, ?)", listfreq)

    con.commit()
    con.close()
