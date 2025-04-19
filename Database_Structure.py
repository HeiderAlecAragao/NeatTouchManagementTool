import sqlite3 as sql

conn = sql.connect('ClientInfo.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS clients(clientID INTEGER PRIMARY KEY NOT NULL, 
                name TEXT NOT NULL,
                phone INTEGER NOT NULL,               
                address TEXT NOT NULL,
                city TEXT,
                dimension REAL,                 
                price REAL,
                startdate TEXT)

            ''')


conn.commit()
conn.close()