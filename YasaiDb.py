# -*- coding:utf-8 -*-
import sys
import sqlite3
from contextlib import closing

dbname = '/var/Yasai/Yasai.db'

################################################## 
## 初期化
def init_db():
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()

        try:
            c.execute('PRAGMA foregin_keys')
            c.execute( '''create table images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,  
                timestamp TEXT
                ) ''')
            c.execute('''create table image_paths (
                id INTEGER,
                size INTEGER,
                path TEXT,
                PRIMARY KEY(id, size),
                FOREIGN KEY(id) REFERENCES images(id)
            )''')
        except sqlite3.Error:
            print sys.exc_info()
################################################## 

def insert_photo(path, timestamp):
    try:
        with closing(sqlite3.connect(dbname)) as conn:
            c = conn.cursor()

            ts = timestamp.strftime("%Y%m%d%H%M%S")
            print ("insert into images(" + path + ", " + ts + ")")
            c.execute("insert into images(name, timestamp) values (?, ?)",
                (path, ts) )

            print ("last_ienrt_rowid")
            c.execute("select last_insert_rowid()")
            row = c.fetchone()
            id = row[0]

            SIZE_ORIGINAL = 0
            print ("insert into image_paths({0}, {1}, {2})".format(id, SIZE_ORIGINAL, path))
            c.execute("insert into image_paths(id, size, path) values (?, ?, ?)",
                (id, SIZE_ORIGINAL, path) )

            conn.commit()
        return True
    except sqlite3.Error as exc:
        print exc
        print sys.exc_info()

if __name__ == "__main__":
    init_db()