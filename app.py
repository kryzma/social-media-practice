from flask import Flask, send_from_directory
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(':memory:')  # In-memory database
    conn.row_factory = sqlite3.Row  # This enables name-based access to columns
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute('''
    CREATE TABLE accounts (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def home():
    return send_from_directory('static', 'sus_dog.jpg')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0')

