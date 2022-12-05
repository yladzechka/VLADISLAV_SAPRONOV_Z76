from flask import Flask, render_template
import sqlite3


def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection


app = Flask(__name__)


@app.route('/')
def index():
    connection = get_db_connection()
    users = connection.execute('SELECT * from users').fetchall()
    return render_template('index.html', users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
