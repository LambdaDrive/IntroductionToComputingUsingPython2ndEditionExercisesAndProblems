#12.16 Write function ranking() that takes as input the name of a database file containing
#a table named Hyperlinks of the same format as the table in Figure 12.2(a). The function
#should add to the database a new table that contains the number of incoming hyperlinks for
#every URL listed in the Link column of Hyperlinks. Name the new table and its columns
#Ranks, Url, and Rank, respectively. When executed against database file links.db, the
#wildcard query on the Rank table should produce this output:
#>>> cur.execute( 'SELECT * FROM Ranks' )
#<sqlite3.Cursor object at 0x15d2560>
#>>> for record in cur:
#print(record)
#
#( 'five.html' , 1)
#( 'four.html' , 3)
#( 'one.html' , 1)
#( 'three.html' , 1)
#( 'two.html' , 2)

import sqlite3

def ranking(dbfile):

    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    cur.execute("""CREATE TABLE Ranks(Url text, Rank int )""")
    res = cur.execute("SELECT Link, COUNT(*) FROM Hyperlinks GROUP BY Link")
    data = res.fetchall()
    cur.executemany("INSERT INTO Ranks VALUES(?, ?)", data)
    con.commit()
    con.close()
