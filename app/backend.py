import sqlite3

def connect():
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library1 (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("bookdesk.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO library1 VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
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

# def search(title="",author="",year="",isbn=""):
#     conn=sqlite3.connect("bookdesk.db")
#     cur=conn.cursor()
#     cur.execute("SELECT * FROM library1 WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
#     rows=cur.fetchall()
#     conn.close()
#     return rows

# def delete(id):
#     conn=sqlite3.connect("bookdesk.db")
#     cur=conn.cursor()
#     cur.execute("DELETE FROM library1 WHERE id=?",(id,))
#     conn.commit()
#     conn.close()

# def update(id,title,author,year,isbn):
#     conn=sqlite3.connect("bookdesk.db")
#     cur=conn.cursor()
#     cur.execute("UPDATE library1 SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
#     conn.commit()
#     conn.close()

connect()
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))
