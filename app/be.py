import sqlite3

def connect():
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library1 (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, type TEXT, publisher TEXT, artist TEXT, quality TEXT, price REAL, location TEXT, genre TEXT, weight REAL, pages INTEGER, isbn REAL, description TEXT, image INTEGER, notes TEXT)")
    conn.commit()
    conn.close()

def insert(title,author,year,type,publisher,artist,quality,price,location,genre,weight,pages,isbn,description,image,notes):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO library1 VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (title, author, year, type, publisher, artist, quality, price, location, genre, weight, pages, isbn, description, image, notes))
    conn.commit()
    conn.close()

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
    cur.execute("SELECT * FROM library1 WHERE title=? OR author=? OR year=? OR type=? OR publisher=? OR artist=? OR quality=? OR price=? OR location=? OR genre=? OR weight=? OR pages=? OR isbn=? OR description=? OR image=? OR notes=?", (title, author, year, type, publisher, artist, quality, price, location, genre, weight, pages, isbn, description, image, notes))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM library1 WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,type,publisher,artist,quality,price,location,genre,weight,pages,isbn,description,image,notes):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("UPDATE library1 SET title=?, author=?, year=?, type=?, publisher=?, artist=?, quality=?, price=?, location=?, genre=?, weight=?, pages=?, isbn=?, description=?, image=?, notes=? WHERE id=?", (title, author, year, type, publisher, artist, quality, price, location, genre, weight, pages, isbn, description, image, notes, id))
    conn.commit()
    conn.close()




connect()

update(2, "Hello", "Bob Dylan", 1940, "Hardcover", "Random House", "Randy Jackson", "Quality", 200, "EVERYWHERE", "Genre", 20, 20, 3300293842, "hello hi how are you hhheee", 100, "Notes")
# insert("Hello", "Bob Dylan", 1940, "Hardcover", "Random House", "Justin Nash", "Quality", 200, "Location", "Genre", 20, 20, 92234234, "hello hi how are you hhheee", 100, "Notes")
# print(search(author="Bob"))
# delete(3)
print(view())
