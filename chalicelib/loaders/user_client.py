from chalice import Chalice
import os, logging, psycopg2
from .access import db_connect, db_cursor

class UserClient:

    def __init__(self):
        self.logger = logging.getLogger("User Client")

    def get_all_users(self):
        users = []
        with db_cursor(os.environ) as c:
            self.create_user_table(c)
            c.execute("SELECT * FROM users;")
            users = c.fetchall()
        return users

    def get_user_by_id(self, id):
        user = []
        with db_cursor(os.environ) as c:
            self.create_user_table(c)
            c.execute(f"SELECT * FROM users WHERE user_id = {id};")
            user = c.fetchone()
        return user if user else None

    def add_new_user(self, user):
        with db_connect(os.environ) as conn:
            c = conn.cursor()
            self.create_user_table(c)
            if user:
                c.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (user['username'], user['password'], user['email']))
                conn.commit()
            else:
                raise ValueError("User object is of NoneType")

    def create_user_table(self, cursor):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
            	user_id serial PRIMARY KEY,
            	username VARCHAR ( 50 ) UNIQUE NOT NULL,
            	password VARCHAR ( 50 ) NOT NULL,
            	email VARCHAR ( 255 ) UNIQUE NOT NULL
            );"""
        )
