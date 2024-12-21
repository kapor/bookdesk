import sqlite3

def connect():
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library1 (id INTEGER PRIMARY KEY, title text, author text, year integer, type text, publisher text, artist text, quality text, price real, location text, genre text, weight real, pages integer, isbn real, description text, image integer, notes text)")
    conn.commit()
    conn.close()

def insert(title,author,year,type,publisher,artist,quality,price,location,genre,weight,pages,isbn,description,image,notes):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO library1 VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(title,author,year,type,publisher,artist,quality,price,location,genre,weight,pages,isbn,description,image,notes))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library1")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",type="",publisher="",artist="",quality="",price="",location="",genre="",weight="",pages="",isbn="",description="",image="",notes=""):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library1 WHERE title=? OR author=? OR year=? OR type=? OR publisher=? OR artist=? OR quality=? OR price=? OR location=? OR genre=? OR weight=? OR pages=? OR isbn=? OR description=? OR notes=?", (title,author,year,publisher,type,artist,quality,price,location,genre,weight,pages,isbn,description,image,notes))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM library1 WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,type,publisher,artist,quality,price,location,genre,weight,pages,isbn,description,image,notes):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("UPDATE library1 SET title=?, author=?, year=?, type=?, publisher=?, artist=?, quality=?, price=?, location=?, genre=?, weight=?, pages=?, isbn=?, description=?, image=?, notes=? WHERE id=?",(title,author,year,type,publisher,artist,quality,price,location,genre,weight,pages,isbn,description,image,notes,id))
    conn.commit()
    conn.close()

connect()
insert("title","author","year","type","publisher","artist","quality","price","location","genre","weight","pages","isbn","description","image","notes")
delete(7)
# update(4, "no title","author","year","type","publisher","artist","quality","price","location","genre","weight","pages","isbn","description","image","notes")
#print(view())
# print(search(author="author"))
