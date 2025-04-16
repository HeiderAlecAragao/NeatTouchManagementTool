import sqlite3 as sql

conn = sql.connect('ClientInfo.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE clients(clientID INTEGER PRIMARY KEY NOT NULL, 
                phone INTEGER NOT NULL,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                dimension REAL, 
                city TEXT,
                price REAL,
                startdate TEXT)

            ''')


conn.commit()
conn.close()