from chalice import Chalice
import psycopg2, os
from .Access import db_connect, db_cursor
#
# db_user = os.environ['DB_USER']
# db_pass = os.environ['DB_PASS']
# db_host = os.environ['DB_HOST']
# db_port = os.environ['DB_PORT']
# db_name = os.environ['DB_NAME']

# dsn = f"dbname={db_name} user={db_user} password={db_pass} host={db_host} port={db_port}"

def add_new_users(users):
    with db_connect() as conn:
        conn = db_connect()
        c = conn.cursor()
        for user in users:
            c.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (user['username'], user['password'], user['email']))
        conn.commit()

def get_all_users():
    users = []
    with db_connect() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users;")
        users = c.fetchall()
        conn.commit()
    return [assemble_user_object(user) for user in users]

def assemble_user_object(user):
    return {
    'id': user[0],
    'username': user[1],
    'password': user[2],
    'email': user[3]
    }
