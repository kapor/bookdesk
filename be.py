import sqlite3

def connect():
    conn=sqlite3.connect("bookdesk")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library1 (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, type TEXT, genre TEXT, isbn INTEGER)")
    conn.commit()
    conn.close()

connect()