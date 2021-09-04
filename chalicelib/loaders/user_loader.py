from chalice import Chalice
import psycopg2, os
from .access import db_connect, db_cursor

def add_new_users(users):
    with db_connect(os.environ) as conn:
        c = conn.cursor()
        create_user_table(c)

        for user in users:
            c.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (user['username'], user['password'], user['email']))
        conn.commit()

def get_all_users():
    users = []
    with db_cursor(os.environ) as c:
        c.execute("SELECT * FROM users;")
        users = c.fetchall()
    return [assemble_user_object(user) for user in users]

def assemble_user_object(user):
    return {
    'id': user[0],
    'username': user[1],
    'password': user[2],
    'email': user[3]
    }

def create_user_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        	user_id serial PRIMARY KEY,
        	username VARCHAR ( 50 ) UNIQUE NOT NULL,
        	password VARCHAR ( 50 ) NOT NULL,
        	email VARCHAR ( 255 ) UNIQUE NOT NULL,
            last_login TIMESTAMP
        );"""
    )
