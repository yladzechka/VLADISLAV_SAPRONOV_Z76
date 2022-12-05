import sqlite3


connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('Name1', 12345))
cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('Name2', 54321))

connection.commit()
connection.close()