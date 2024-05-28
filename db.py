# db.py
import psycopg2
import os

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB', 'exampledb'),
        user=os.getenv('POSTGRES_USER', 'user'),
        password=os.getenv('POSTGRES_PASSWORD', 'password'),
        host='db', 
        port='5432'
    )
    return conn

def init_db():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
        ''')
        conn.commit()
    conn.close()

def fetch_users():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute('SELECT id, username, email FROM accounts;')
        users = cur.fetchall()
    conn.close()
    return users