import sqlite3

def search2(dbfile):

    con = sqlite3.connect(dbfile)
    cur = con.cursor()

    while True:
        
        keyword = input("Enter keyword: ")

        cur.execute("""SELECT Keywords.Url, Ranks.Rank FROM Keywords, Ranks WHERE Keywords.Word = ? AND Keywords.Url = Ranks.Url ORDER BY Rank DESC;""", (keyword,))
        print('{:15}{:4}'.format('URL', 'RANK'))
        for url, rank in cur:
            print('{:15}{:4}'.format(url, rank))

