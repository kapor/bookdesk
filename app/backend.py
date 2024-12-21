import sqlite3

def connect():
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library2 (id INTEGER PRIMARY KEY, title text, author text, year integer, type text, publisher text, artist text, quality text, price real, location text)")
    conn.commit()
    conn.close()

def insert(title,author,year,type,publisher,artist,quality,price,location):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO library2 VALUES (NULL,?,?,?,?,?,?,?,?,?)",(title,author,year,type,publisher,artist,quality,price,location))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library2")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",type="",publisher="",artist="",quality="",price="",location=""):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library2 WHERE title=? OR author=? OR year=? OR type=? OR publisher=? OR artist=? OR quality=? OR price=? OR location=?", (title,author,year,publisher,type,artist,quality,price,location))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM library2 WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,type,publisher,artist,quality,price,location):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("UPDATE library2 SET title=?, author=?, year=?, type=?, publisher=?, artist=?, quality=?, price=?, location=? WHERE id=?",(title,author,year,type,publisher,artist,quality,price,location,id))
    conn.commit()
    conn.close()

connect()
# insert("title","author","year","type","publisher","artist","quality","price","location")
# delete(7)
# update(4, "no title","author","year","type","publisher","artist","quality","price","location","genre","weight","pages","isbn","description","image","notes")
#print(view())
# print(search(author="author"))
