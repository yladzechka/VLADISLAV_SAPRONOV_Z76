import sqlite3


connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)", ('First post!!!', 'Hello everyone!', 'Author1'))
cur.execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)", ('Second post!!!', 'Goodbye!', 'Author2'))

connection.commit()
connection.close()